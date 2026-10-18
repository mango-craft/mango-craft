#!/usr/bin/env python3
"""Inventario del pack: cosa contiene davvero ogni file di mod.

Uso: python3 scripts/inventory.py <cartella pack> <cartella inventario>

Per ogni metafile (*.pw.toml) che punta a un .jar:
- scarica il file (Modrinth dal suo CDN, CurseForge da forgecdn) e ne controlla l'hash;
- salva `<inventario>/mods/<nome metafile>.json` con: mod id, versione e dipendenze
  (da neoforge.mods.toml), oggetti e blocchi con il nome inglese, entità, liquidi,
  effetti, biomi, tutti i dati (ricette, tabelle del bottino, strutture, tag con il
  contenuto…), i tipi di ricetta usati e le ricette di Botany Pots;
- guarda anche dentro i .jar incorporati (META-INF/jarjar).
I file già inventariati con lo stesso hash non vengono riscaricati; quelli di mod
tolte dal pack vengono cancellati.

Inventaria anche Minecraft (`minecraft.json`, dai dati di misode/mcmeta) e
NeoForge (`neoforge.json`, dal suo jar: contiene i tag comuni `c:`).

Serve la rete verso Modrinth, CurseForge e Maven: gira nelle GitHub Actions.
Il risultato si controlla con `check_ids.py`. Solo libreria standard.
"""
import hashlib
import io
import json
import re
import sys
import tomllib
import urllib.parse
import urllib.request
import zipfile
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

USER_AGENT = "mango-craft-inventory (github.com/mango-craft/mango-craft)"
MCMETA = "https://raw.githubusercontent.com/misode/mcmeta/{mc}-summary/"
NEOFORGE_JAR = ("https://maven.neoforged.net/releases/net/neoforged/neoforge/"
                "{v}/neoforge-{v}-universal.jar")
FORMAT = 2  # cambiare se cambia il formato dei file: forza un nuovo inventario

# Chiavi dei file di lingua -> campo dell'inventario
LANG_KINDS = {"item": "items", "block": "blocks", "entity": "entities",
              "fluid_type": "fluids", "fluid": "fluids", "effect": "effects",
              "biome": "biomes"}
# Registri di Minecraft che finiscono nei campi principali invece che in "data"
VANILLA_FIELDS = {"item": "items", "block": "blocks", "entity_type": "entities",
                  "fluid": "fluids", "mob_effect": "effects", "worldgen/biome": "biomes"}
# Categorie di dati di cui si tiene solo il numero (sono tante e non servono per nome)
COUNT_ONLY = {"advancement"}
# Registri di Minecraft che non servono ai controlli (risorse grafiche e sonore)
VANILLA_SKIP = {"model", "texture", "block_definition", "atlas", "font", "sound_event"}


def get(url: str, timeout: int = 180) -> bytes:
    last = None
    for _ in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:  # rete instabile: riprova
            last = e
    raise RuntimeError(f"download fallito: {url} ({last})")


def categorize(rest: list[str]) -> tuple[str, str] | None:
    """Percorso dentro data/<ns>/ (già diviso) -> (categoria, percorso dell'id)."""
    if len(rest) < 2:
        return None
    head = rest[0]
    if head == "tags":
        if len(rest) >= 4 and rest[1] == "worldgen":
            cat, idp = f"tags/worldgen/{rest[2]}", rest[3:]
        else:
            cat, idp = f"tags/{rest[1]}", rest[2:]
    elif head == "worldgen" and len(rest) >= 3:
        cat, idp = f"worldgen/{rest[1]}", rest[2:]
    elif head == "data_maps" and len(rest) >= 3:
        if rest[1] == "worldgen" and len(rest) >= 4:
            cat, idp = f"data_maps/worldgen/{rest[2]}", rest[3:]
        else:
            cat, idp = f"data_maps/{rest[1]}", rest[2:]
    elif head == "neoforge" and len(rest) >= 3:
        cat, idp = f"neoforge/{rest[1]}", rest[2:]
    else:
        cat, idp = head, rest[1:]
    if not idp:
        return None
    path = "/".join(idp)
    path = re.sub(r"\.(json|nbt|mcfunction)$", "", path)
    return cat, path


def tag_values(d) -> list:
    vals = d.get("values", []) if isinstance(d, dict) else []
    out = []
    for v in vals:
        if isinstance(v, str):
            out.append(v)
        elif isinstance(v, dict) and "id" in v:
            out.append(v["id"] if v.get("required", True) else f"{v['id']}?")
    return out


class Inv:
    def __init__(self):
        self.mods: list[dict] = []
        self.namespaces: set[str] = set()
        self.names: dict[str, dict[str, str]] = defaultdict(dict)  # campo -> id -> nome
        self.data: dict[str, set[str]] = defaultdict(set)
        self.counts: Counter = Counter()
        self.tags: dict[str, dict[str, list]] = defaultdict(dict)
        self.recipe_types: Counter = Counter()
        self.botanypots: list[dict] = []
        self.nested: list[str] = []
        self.problems: list[str] = []

    def to_json(self) -> dict:
        return {
            "mods": self.mods,
            "nested": sorted(self.nested),
            "namespaces": sorted(self.namespaces),
            **{k: dict(sorted(v.items())) for k, v in sorted(self.names.items())},
            "data": {k: sorted(v) for k, v in sorted(self.data.items())},
            "data_counts": dict(sorted(self.counts.items())),
            "tags": {k: dict(sorted(v.items())) for k, v in sorted(self.tags.items())},
            "recipe_types": dict(sorted(self.recipe_types.items())),
            "botanypots": sorted(self.botanypots, key=lambda r: r["id"]),
            "problems": self.problems,
        }


def parse_mods_toml(text: str, manifest_version: str | None, where: str) -> tuple[list, list]:
    try:
        d = tomllib.loads(text)
    except tomllib.TOMLDecodeError as e:
        return [], [f"{where}: mods.toml non leggibile ({e})"]
    mods = []
    deps = d.get("dependencies", {}) or {}
    for m in d.get("mods", []) or []:
        version = str(m.get("version", ""))
        if "${" in version and manifest_version:
            version = manifest_version
        entry = {"modid": m.get("modId"), "name": m.get("displayName"), "version": version,
                 "jar": where, "deps": []}
        for dep in deps.get(m.get("modId"), []) or []:
            kind = dep.get("type")
            if kind is None:
                kind = "required" if dep.get("mandatory") else "optional"
            entry["deps"].append({"modid": dep.get("modId"), "type": str(kind).lower(),
                                  "range": dep.get("versionRange"), "side": dep.get("side")})
        mods.append(entry)
    return mods, []


def analyze_jar(data: bytes, inv: Inv, where: str = "", depth: int = 0) -> None:
    try:
        z = zipfile.ZipFile(io.BytesIO(data))
    except zipfile.BadZipFile:
        inv.problems.append(f"{where or 'jar'}: non è uno zip valido")
        return
    names = z.namelist()
    manifest_version = None
    if "META-INF/MANIFEST.MF" in names:
        m = re.search(r"^Implementation-Version:\s*(\S+)", z.read("META-INF/MANIFEST.MF").decode("utf-8", "replace"), re.M)
        manifest_version = m.group(1) if m else None
    item_models, blockstates = set(), set()
    # Jar incorporati: quelli elencati in META-INF/jarjar/metadata.json (possono stare
    # ovunque, es. META-INF/jars/ con Architectury) più ogni .jar dentro META-INF/
    nested = {n for n in names if n.startswith("META-INF/") and n.endswith(".jar")}
    if "META-INF/jarjar/metadata.json" in names:
        try:
            meta = json.loads(z.read("META-INF/jarjar/metadata.json").decode("utf-8-sig"))
            nested |= {j["path"] for j in meta.get("jars", []) if j.get("path") in names}
        except Exception:
            inv.problems.append(f"{where or 'jar'}: META-INF/jarjar/metadata.json non leggibile")
    for n in names:
        if n.endswith("/"):
            continue
        if n in nested:
            if depth < 3:
                inv.nested.append(n.rsplit("/", 1)[1])
                analyze_jar(z.read(n), inv, n.rsplit("/", 1)[1], depth + 1)
            continue
        if n in ("META-INF/neoforge.mods.toml", "META-INF/mods.toml"):
            mods, probs = parse_mods_toml(z.read(n).decode("utf-8", "replace"), manifest_version, where)
            inv.mods.extend(mods)
            inv.problems.extend(probs)
            continue
        parts = n.split("/")
        if parts[0] == "assets" and len(parts) >= 4:
            ns = parts[1]
            inv.namespaces.add(ns)
            if len(parts) == 4 and parts[2] == "lang" and parts[3] == "en_us.json":
                try:
                    lang = json.loads(z.read(n).decode("utf-8-sig"))
                except Exception:
                    inv.problems.append(f"{n}: JSON non valido")
                    continue
                for key, val in lang.items():
                    kp = key.split(".")
                    if len(kp) == 3 and kp[0] in LANG_KINDS and isinstance(val, str):
                        inv.names[LANG_KINDS[kp[0]]][f"{kp[1]}:{kp[2]}"] = val
            elif len(parts) == 4 and parts[2] == "blockstates" and n.endswith(".json"):
                blockstates.add(f"{ns}:{parts[3][:-5]}")
            elif len(parts) == 5 and parts[2] == "models" and parts[3] == "item" and n.endswith(".json"):
                item_models.add(f"{ns}:{parts[4][:-5]}")
        elif parts[0] == "data" and len(parts) >= 4:
            ns = parts[1]
            inv.namespaces.add(ns)
            c = categorize(parts[2:])
            if not c:
                continue
            cat, path = c
            rid = f"{ns}:{path}"
            if cat in COUNT_ONLY:
                inv.counts[cat] += 1
                continue
            inv.data[cat].add(rid)
            if not n.endswith(".json") or not (cat.startswith("tags/") or cat == "recipe"):
                continue
            try:
                d = json.loads(z.read(n).decode("utf-8-sig"))
            except Exception:
                inv.problems.append(f"{n}: JSON non valido")
                continue
            if cat.startswith("tags/"):
                prev = inv.tags[cat].get(rid, [])
                inv.tags[cat][rid] = prev + [v for v in tag_values(d) if v not in prev]
            elif isinstance(d, dict):
                rtype = str(d.get("type"))
                inv.recipe_types[rtype] += 1
                if rtype.startswith(("botanypots:", "botanytrees:")):
                    rec = {k: v for k, v in d.items() if k != "display"}
                    rec["id"] = rid
                    inv.botanypots.append(rec)
    for rid in item_models:
        inv.names["items"].setdefault(rid, "")
    for rid in blockstates:
        inv.names["blocks"].setdefault(rid, "")


def metafiles(pack: Path) -> list[dict]:
    out = []
    for p in sorted(pack.rglob("*.pw.toml")):
        d = tomllib.loads(p.read_text(encoding="utf-8"))
        filename = d.get("filename", "")
        if not filename.endswith(".jar"):
            continue
        dl = d.get("download", {})
        if dl.get("mode") == "metadata:curseforge":
            fid = str(d["update"]["curseforge"]["file-id"])
            url = (f"https://mediafilez.forgecdn.net/files/{fid[:4]}/{int(fid[4:])}/"
                   f"{urllib.parse.quote(filename)}")
            source = "curseforge"
        else:
            url, source = dl["url"], "modrinth"
        out.append({"slug": p.name[: -len(".pw.toml")], "name": d.get("name"), "file": filename,
                    "side": d.get("side"), "source": source, "url": url,
                    "hash_format": dl.get("hash-format"), "hash": dl.get("hash")})
    return out


def inventory_mod(m: dict, out: Path) -> str:
    data = get(m["url"])
    h = hashlib.new(m["hash_format"], data).hexdigest()
    if h != m["hash"]:
        raise RuntimeError(f"hash diverso ({m['hash_format']} {h[:12]}… invece di {m['hash'][:12]}…)")
    inv = Inv()
    analyze_jar(data, inv)
    doc = {"format": FORMAT, "status": "ok", **{k: m[k] for k in ("name", "file", "side", "source", "hash_format", "hash")},
           **inv.to_json()}
    write_json(out, doc)
    return "ok"


def write_json(path: Path, doc: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(doc, indent=1, ensure_ascii=False, sort_keys=False) + "\n", encoding="utf-8")


def up_to_date(path: Path, key: str, value) -> bool:
    if not path.exists():
        return False
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return False
    return d.get("format") == FORMAT and d.get("status") == "ok" and d.get(key) == value


def inventory_minecraft(mc: str, out: Path) -> None:
    if up_to_date(out, "version", mc):
        return
    base = MCMETA.format(mc=mc)
    regs = json.loads(get(base + "registries/data.min.json"))
    inv = Inv()
    inv.namespaces.add("minecraft")
    inv.mods.append({"modid": "minecraft", "name": "Minecraft", "version": mc, "jar": "", "deps": []})
    for reg, names in regs.items():
        ids = [f"minecraft:{n}" for n in names]
        if reg in VANILLA_FIELDS:
            for i in ids:
                inv.names[VANILLA_FIELDS[reg]][i] = ""
        elif reg.startswith("tag/"):
            cat = "tags/" + reg[4:]
            try:
                contents = json.loads(get(base + f"data/{reg}/data.min.json"))
            except Exception:
                contents = {}
            for n in names:
                inv.tags[cat][f"minecraft:{n}"] = tag_values(contents.get(n, {}))
        elif reg in COUNT_ONLY:
            inv.counts[reg] = len(ids)
        elif not reg.startswith("experiment/") and reg not in VANILLA_SKIP:
            inv.data[reg].update(ids)
    write_json(out, {"format": FORMAT, "status": "ok", "version": mc, **inv.to_json()})


def inventory_neoforge(version: str, out: Path) -> None:
    if up_to_date(out, "version", version):
        return
    data = get(NEOFORGE_JAR.format(v=version))
    inv = Inv()
    analyze_jar(data, inv)
    write_json(out, {"format": FORMAT, "status": "ok", "version": version, **inv.to_json()})


def main(pack_dir: str, inv_dir: str) -> int:
    pack, inv_root = Path(pack_dir), Path(inv_dir)
    versions = tomllib.loads((pack / "pack.toml").read_text(encoding="utf-8"))["versions"]
    failures = []
    for label, fn, arg, path in (("Minecraft", inventory_minecraft, versions["minecraft"], inv_root / "minecraft.json"),
                                 ("NeoForge", inventory_neoforge, versions.get("neoforge"), inv_root / "neoforge.json")):
        if not arg:
            continue
        try:
            fn(arg, path)
        except Exception as e:
            failures.append(f"{label}: {e}")

    mods = metafiles(pack)
    mods_dir = inv_root / "mods"
    wanted = {m["slug"] for m in mods}
    if mods_dir.exists():
        for f in mods_dir.glob("*.json"):
            if f.stem not in wanted:
                f.unlink()
                print(f"tolto {f.name} (mod non più nel pack)")
    todo = [m for m in mods if not up_to_date(mods_dir / f"{m['slug']}.json", "hash", m["hash"])]
    print(f"{len(mods)} mod nel pack, {len(todo)} da inventariare")

    def work(m):
        target = mods_dir / f"{m['slug']}.json"
        try:
            inventory_mod(m, target)
            return m["slug"], None
        except Exception as e:
            write_json(target, {"format": FORMAT, "status": f"errore: {e}",
                                **{k: m[k] for k in ("name", "file", "side", "source", "hash_format", "hash")}})
            return m["slug"], str(e)

    with ThreadPoolExecutor(max_workers=8) as ex:
        for slug, error in ex.map(work, todo):
            print(f"{'ERRORE' if error else 'ok'}  {slug}" + (f": {error}" if error else ""))
            if error:
                failures.append(f"{slug}: {error}")
    if failures:
        # Un download non riuscito (es. mod CurseForge bloccata) non è un errore del pack:
        # check_ids.py lo segnala come avviso. Un hash diverso invece sì.
        print("\nInventario incompleto:\n- " + "\n- ".join(failures))
        if any("hash diverso" in f for f in failures):
            return 1
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    sys.exit(main(*sys.argv[1:]))
