#!/usr/bin/env python3
"""Esamina mod di Modrinth che NON sono nel pack, per valutarle prima di aggiungerle.

Uso: python3 scripts/esamina.py <cartella pack> <cartella risultati> <filtro> [--stringhe <regex>] <voce> [<voce> …]

- <voce>: come in modrinth_resolve.py (slug, slug@versione, id di versione).
- <filtro>: espressione regolare sui percorsi dei file .json dentro `data/` e `assets/`;
  per i file che corrispondono si elencano i valori (chiave = valore). "-" = nessun valore.
- --stringhe: espressione regolare sui testi scritti nel codice compilato (.class): nomi di
  file di config, chiavi, comandi. Si leggono solo le costanti del file, senza eseguirlo.

Per ogni mod scrive `<cartella risultati>/<slug>.md` (una cartella dello stage,
`ai-agents/stage/<data>-esame-mod/`, materiale grezzo fuori da git): versione scelta,
mod id e dipendenze dichiarate nel .jar (con le versioni richieste), cartelle di dati con il numero di file e,
per i file filtrati, i valori. Non copia i file: elenca i valori che servono per l'analisi
(il contenuto delle mod resta dei rispettivi autori).

Non esegue codice delle mod: apre i .jar come archivi zip. Serve la rete verso Modrinth.
"""
import hashlib
import io
import json
import re
import sys
import tomllib
import zipfile
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from inventory import get, parse_mods_toml  # noqa: E402
from modrinth_resolve import api, resolve  # noqa: E402

MAX_LINES = 4000      # righe di valori per mod, al massimo
MAX_VALUE = 300       # caratteri per valore
MAX_STRINGS = 1500    # testi del codice per mod, al massimo


def class_strings(data: bytes) -> list[str]:
    """Testi (costanti UTF-8) di un file .class: si legge la tabella delle costanti, niente altro."""
    if data[:4] != b"\xca\xfe\xba\xbe":
        return []
    count, i, k, out = int.from_bytes(data[8:10], "big"), 10, 1, []
    while k < count and i < len(data):
        tag = data[i]
        i += 1
        if tag == 1:
            n = int.from_bytes(data[i:i + 2], "big")
            out.append(data[i + 2:i + 2 + n].decode("utf-8", "replace"))
            i += 2 + n
        elif tag in (3, 4, 9, 10, 11, 12, 17, 18):
            i += 4
        elif tag in (5, 6):
            i += 8
            k += 1
        elif tag in (7, 8, 16, 19, 20):
            i += 2
        elif tag == 15:
            i += 3
        else:
            break
        k += 1
    return out


def flatten(node, prefix=""):
    if isinstance(node, dict):
        for k, v in node.items():
            yield from flatten(v, f"{prefix}.{k}" if prefix else str(k))
    elif isinstance(node, list):
        if node and all(not isinstance(x, (dict, list)) for x in node):
            yield prefix, json.dumps(node, ensure_ascii=False)
        else:
            for i, v in enumerate(node):
                yield from flatten(v, f"{prefix}[{i}]")
    else:
        yield prefix, json.dumps(node, ensure_ascii=False)


def walk(data: bytes, where: str, depth: int, out: dict) -> None:
    z = zipfile.ZipFile(io.BytesIO(data))
    names = z.namelist()
    manifest_version = None
    if "META-INF/MANIFEST.MF" in names:
        m = re.search(r"Implementation-Version:\s*(\S+)", z.read("META-INF/MANIFEST.MF").decode("utf-8", "replace"))
        manifest_version = m.group(1) if m else None
    for toml_name in ("META-INF/neoforge.mods.toml", "META-INF/mods.toml"):
        if toml_name in names:
            mods, problems = parse_mods_toml(z.read(toml_name).decode("utf-8", "replace"), manifest_version, where)
            out["mods"] += mods
            out["problems"] += problems
            break
    for n in names:
        if n.endswith(".jar") and n.startswith("META-INF/") and depth < 2:
            try:
                walk(z.read(n), n.rsplit("/", 1)[-1], depth + 1, out)
            except zipfile.BadZipFile:
                out["problems"].append(f"{n}: non è uno zip valido")
            continue
        if n.endswith(".class") and out["strings_re"]:
            for s in class_strings(z.read(n)):
                if out["strings_re"].search(s):
                    out["strings"].append((n, s if len(s) <= MAX_VALUE else s[:MAX_VALUE] + "…"))
            continue
        if not n.endswith(".json") or not n.startswith(("data/", "assets/")):
            continue
        parts = n.split("/")
        if parts[0] == "data" and len(parts) > 3:
            out["folders"][f"{parts[1]}:{'/'.join(parts[2:-1])}"] += 1
        if out["filter"] and out["filter"].search(n):
            try:
                doc = json.loads(z.read(n).decode("utf-8-sig"))
            except (json.JSONDecodeError, UnicodeDecodeError) as e:
                out["values"].append((n, "(file non leggibile)", str(e)[:80]))
                continue
            for k, v in flatten(doc):
                out["values"].append((n, k, v if len(v) <= MAX_VALUE else v[:MAX_VALUE] + "…"))


def examine(entry: str, mc: str, loader: str, regex, strings_re, out_dir: Path) -> str:
    v = resolve(entry, mc, loader)
    project = api(f"/project/{v['project_id']}")
    f = next((x for x in v["files"] if x.get("primary")), v["files"][0])
    data = get(f["url"])
    if hashlib.sha512(data).hexdigest() != f["hashes"]["sha512"]:
        raise SystemExit(f"{entry}: hash del file diverso da quello di Modrinth")
    out = {"mods": [], "problems": [], "folders": Counter(), "values": [], "filter": regex,
           "strings_re": strings_re, "strings": []}
    walk(data, f["filename"], 0, out)

    lines = [f"# {project['title']} ({project['slug']})", "",
             "File generato da `scripts/esamina.py`: la mod **non** è nel pack. "
             "Non modificarlo a mano.", "",
             f"- Versione: **{v['version_number']}** ({v.get('version_type')}, {v['date_published'][:10]}), "
             f"file `{f['filename']}`, id versione `{v['id']}`",
             f"- Licenza su Modrinth: {project.get('license', {}).get('id', '?')} · download: {project.get('downloads', '?')}",
             f"- Filtro dei valori: `{regex.pattern if regex else '-'}`"
             + (f" · filtro dei testi del codice: `{strings_re.pattern}`" if strings_re else ""), "",
             "## Mod nel file e dipendenze dichiarate", ""]
    seen = set()
    for m in out["mods"]:
        key = (m["modid"], m["version"])
        if key in seen:
            continue
        seen.add(key)
        where = f" (dentro `{m['jar']}`)" if m["jar"] != f["filename"] else ""
        lines.append(f"- `{m['modid']}` {m['version']}{where}")
        for d in m["deps"]:
            lines.append(f"  - {d['type']}: `{d['modid']}` {d.get('range') or ''}".rstrip())
    lines += ["", "## Cartelle di dati (file .json)", ""]
    lines += [f"- `{k}`: {n}" for k, n in sorted(out["folders"].items())] or ["- nessuna"]
    if out["filter"]:
        lines += ["", "## Valori dei file filtrati", ""]
        current, count = None, 0
        for path, k, val in out["values"]:
            if count >= MAX_LINES:
                lines.append(f"\n… altri valori tagliati (limite di {MAX_LINES} righe)")
                break
            if path != current:
                lines += ["", f"### `{path}`", ""]
                current = path
            lines.append(f"- `{k}` = {val}")
            count += 1
    if strings_re:
        lines += ["", "## Testi nel codice", ""]
        seen_s, current = set(), None
        for cls, s in out["strings"]:
            if (cls, s) in seen_s:
                continue
            if len(seen_s) >= MAX_STRINGS:
                lines.append(f"\n… altri testi tagliati (limite di {MAX_STRINGS})")
                break
            seen_s.add((cls, s))
            if cls != current:
                lines += ["", f"### `{cls}`", ""]
                current = cls
            lines.append(f"- {json.dumps(s, ensure_ascii=False)}")
    if out["problems"]:
        lines += ["", "## Problemi", ""] + [f"- {p}" for p in out["problems"]]
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"{project['slug']}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return f"{project['slug']} {v['version_number']}: {len(out['values'])} valori, {len(out['strings'])} testi"


def main(pack_dir: str, out_dir: str, filt: str, entries: list[str], strings: str = "-") -> None:
    pv = tomllib.loads((Path(pack_dir) / "pack.toml").read_text(encoding="utf-8"))["versions"]
    mc = pv["minecraft"]
    loader = next((l for l in ("neoforge", "fabric", "quilt", "forge") if l in pv), None)
    regex = None if filt.strip() in ("", "-") else re.compile(filt)
    strings_re = None if strings.strip() in ("", "-") else re.compile(strings)
    for e in entries:
        print(examine(e.strip(), mc, loader, regex, strings_re, Path(out_dir)))


if __name__ == "__main__":
    args = sys.argv[1:]
    strings = "-"
    if "--stringhe" in args:
        i = args.index("--stringhe")
        strings = args[i + 1] if i + 1 < len(args) else "-"
        del args[i:i + 2]
    if len(args) < 4:
        raise SystemExit(__doc__)
    main(args[0], args[1], args[2], [a for a in args[3:] if a.strip()], strings)
