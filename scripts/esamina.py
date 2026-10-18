#!/usr/bin/env python3
"""Esamina mod di Modrinth che NON sono nel pack, per valutarle prima di aggiungerle.

Uso: python3 scripts/esamina.py <cartella pack> <cartella risultati> <filtro> <voce> [<voce> …]

- <voce>: come in modrinth_resolve.py (slug, slug@versione, id di versione).
- <filtro>: espressione regolare sui percorsi dei file .json dentro `data/` e `assets/`;
  per i file che corrispondono si elencano i valori (chiave = valore). "-" = nessun valore.

Per ogni mod scrive `<cartella risultati>/<slug>.md`: versione scelta, mod id e dipendenze
dichiarate nel .jar (con le versioni richieste), cartelle di dati con il numero di file e,
per i file filtrati, i valori. Non copia i file: elenca i valori che servono per l'analisi
(il contenuto delle mod resta dei rispettivi autori).

Non esegue codice delle mod: apre i .jar come archivi zip. Serve la rete verso Modrinth:
gira nelle GitHub Actions (workflow "Esamina mod").
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
MAX_VALUE = 160       # caratteri per valore


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


def examine(entry: str, mc: str, loader: str, regex, out_dir: Path) -> str:
    v = resolve(entry, mc, loader)
    project = api(f"/project/{v['project_id']}")
    f = next((x for x in v["files"] if x.get("primary")), v["files"][0])
    data = get(f["url"])
    if hashlib.sha512(data).hexdigest() != f["hashes"]["sha512"]:
        raise SystemExit(f"{entry}: hash del file diverso da quello di Modrinth")
    out = {"mods": [], "problems": [], "folders": Counter(), "values": [], "filter": regex}
    walk(data, f["filename"], 0, out)

    lines = [f"# {project['title']} ({project['slug']})", "",
             "File generato da `scripts/esamina.py` (workflow \"Esamina mod\"): la mod **non** è nel pack. "
             "Non modificarlo a mano.", "",
             f"- Versione: **{v['version_number']}** ({v.get('version_type')}, {v['date_published'][:10]}), "
             f"file `{f['filename']}`, id versione `{v['id']}`",
             f"- Licenza su Modrinth: {project.get('license', {}).get('id', '?')} · download: {project.get('downloads', '?')}",
             f"- Filtro dei valori: `{regex.pattern if regex else '-'}`", "",
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
    if out["problems"]:
        lines += ["", "## Problemi", ""] + [f"- {p}" for p in out["problems"]]
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"{project['slug']}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return f"{project['slug']} {v['version_number']}: {len(out['values'])} valori"


def main(pack_dir: str, out_dir: str, filt: str, entries: list[str]) -> None:
    pv = tomllib.loads((Path(pack_dir) / "pack.toml").read_text(encoding="utf-8"))["versions"]
    mc = pv["minecraft"]
    loader = next((l for l in ("neoforge", "fabric", "quilt", "forge") if l in pv), None)
    regex = None if filt.strip() in ("", "-") else re.compile(filt)
    for e in entries:
        print(examine(e.strip(), mc, loader, regex, Path(out_dir)))


if __name__ == "__main__":
    if len(sys.argv) < 5:
        raise SystemExit(__doc__)
    main(sys.argv[1], sys.argv[2], sys.argv[3], [a for a in sys.argv[4:] if a.strip()])
