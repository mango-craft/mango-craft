#!/usr/bin/env python3
"""Controllo dei nomi sull'inventario: dipendenze delle mod e nomi usati nel datapack.

Uso: python3 scripts/check_ids.py <cartella pack> <cartella inventario> [--report FILE]

Si basa sull'inventario creato da inventory.py (non serve la rete).

Errori (uscita 1):
- una mod richiede (dipendenza obbligatoria) una mod che non c'è;
- nel datapack, per mod presenti nel pack: oggetti, blocchi, liquidi, entità, tag,
  tabelle del bottino o modificatori che non esistono;
- condizioni di caricamento che non possono mai essere vere (il file non si
  caricherebbe mai, senza dare errori in gioco);
- mod il cui file scaricato non corrisponde all'hash del metafile.
Avvisi:
- tabelle del bottino nominate dai modificatori che non esistono (in gioco non danno
  errori, semplicemente non vengono mai toccate);
- mod non inventariate (download non riuscito): i loro nomi non si possono verificare.
Informazioni: file del datapack inattivi perché la loro mod non è nel pack.
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from inventory import categorize  # noqa: E402
import re  # noqa: E402
import tomllib  # noqa: E402


def _ver(v: str) -> tuple:
    """'21.1.259' -> (21, 1, 259). Toglie un prefisso con la versione di Minecraft ('1.21.1-2.6.1' -> 2.6.1)
    e i suffissi ('-beta', '+build'); le parti non numeriche si ignorano."""
    v = re.sub(r"^(?:mc)?1\.\d+(?:\.\d+)?-(?=\d)", "", v.strip())
    return tuple(int(x) for x in re.findall(r"\d+", v.split("+")[0].split("-")[0]))


def in_range(version: str, rng: str | None) -> bool:
    """Intervallo in stile Maven: [a,b), (a,], [a] = esattamente a; senza parentesi = qualunque versione."""
    if not rng or rng.strip() in ("*", ""):
        return True
    parts = re.findall(r"[\[(][^\])]*[\])]", rng)
    if not parts:
        # Senza parentesi è una versione "consigliata" (regola di Maven, usata da NeoForge):
        # va bene qualunque versione. Lo stesso per gli intervalli scritti male.
        return True
    v = _ver(version)
    for part in parts:
        lo, _, hi = part[1:-1].partition(",")
        if "," not in part:
            hi = lo  # [x] = esattamente x
        ok_lo = not lo.strip() or (v >= _ver(lo) if part[0] == "[" else v > _ver(lo))
        ok_hi = not hi.strip() or (v <= _ver(hi) if part[-1] == "]" else v < _ver(hi))
        if ok_lo and ok_hi:
            return True
    return False

BUILTIN_MODS = {"minecraft", "neoforge", "forge", "java", "fml"}
# Tipo di riferimento -> campo dell'inventario (o categoria di dati)
FIELDS = {"item": ("items", "blocks"), "block": ("blocks",), "fluid": ("fluids",),
          "entity_type": ("entities",), "potion": ("potions",)}


class Index:
    def __init__(self):
        self.modids: set[str] = set()
        self.namespaces: set[str] = set()
        self.names: dict[str, set[str]] = defaultdict(set)
        self.data: dict[str, set[str]] = defaultdict(set)
        self.tags: dict[str, set[str]] = defaultdict(set)
        self.mods: list[tuple[str, dict]] = []   # (sorgente, voce mod)
        self.unverified: list[str] = []          # mod non inventariate
        self.hash_errors: list[str] = []

    def add_doc(self, label: str, d: dict) -> None:
        for m in d.get("mods", []):
            if m.get("modid"):
                self.modids.add(m["modid"])
                self.mods.append((label, m))
        self.namespaces.update(d.get("namespaces", []))
        for field in ("items", "blocks", "fluids", "entities", "effects", "biomes", "potions"):
            self.names[field].update(d.get(field, {}))
        for cat, ids in d.get("data", {}).items():
            self.data[cat].update(ids)
        for cat, tags in d.get("tags", {}).items():
            self.tags[cat].update(tags)
        # I nomi dei liquidi: l'inventario li ricava dalle traduzioni, che non sempre usano il nome del registro
        # (Cognition traduce `cognitium` ma il liquido è `cognition:cognitium_source`). Valgono anche i liquidi
        # che una mod elenca come obbligatori nelle etichette di liquidi (24/10/2026).
        # Limite: un nome preso dalle traduzioni può essere il tipo di liquido e non il liquido (`cognition:cognitium`):
        # il controllo lo accetta lo stesso. Il nome giusto si prende dalle etichette della mod; la prova finale è il log.
        for vals in (d.get("tags", {}).get("tags/fluid") or {}).values():
            self.names["fluids"].update(v for v in vals if isinstance(v, str) and not v.startswith("#") and not v.endswith("?"))

    def has(self, kind: str, rid: str) -> bool:
        if kind in FIELDS:
            return any(rid in self.names[f] for f in FIELDS[kind])
        if kind == "biome":
            return rid in self.names["biomes"] or rid in self.data["worldgen/biome"]
        if kind.startswith("tag:"):
            return rid in self.tags[f"tags/{kind[4:]}"]
        return rid in self.data[kind]


def load_index(inv: Path) -> Index:
    idx = Index()
    for name in ("minecraft.json", "neoforge.json"):
        p = inv / name
        if p.exists():
            idx.add_doc(name[:-5], json.loads(p.read_text(encoding="utf-8")))
    for p in sorted((inv / "mods").glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        status = d.get("status", "")
        if status == "ok":
            idx.add_doc(p.stem, d)
        elif "hash diverso" in status:
            idx.hash_errors.append(f"{p.stem}: {status}")
        else:
            idx.unverified.append(f"{p.stem} ({d.get('source')}): {status}")
    return idx


def add_datapack_definitions(idx: Index, files: list[tuple[Path, str, str, str, dict]]) -> None:
    """Quello che il nostro datapack definisce esiste, anche se nessuna mod lo ha."""
    for _, ns, cat, rid, _ in files:
        idx.namespaces.add(ns)
        if cat.startswith("tags/"):
            idx.tags[cat].add(rid)
        else:
            idx.data[cat].add(rid)


def parse_conditions(d: dict) -> tuple[set, list, bool]:
    """-> (mod richieste, [(tipo, id)] richiesti, analizzabile)."""
    mods, ids, ok = set(), [], True

    def neo(c):
        nonlocal ok
        t = c.get("type", "")
        if t == "neoforge:mod_loaded":
            mods.add(c.get("modid"))
        elif t == "neoforge:item_exists":
            ids.append(("item", c.get("item")))
        elif t == "neoforge:and":
            for v in c.get("values", []):
                neo(v)
        elif t in ("neoforge:or", "neoforge:not"):
            ok = False  # non si può dire a priori: niente controllo sulle condizioni
    for c in d.get("neoforge:conditions", []) or []:
        neo(c)
    for c in d.get("bookshelf:load_conditions", []) or []:
        t, vals = c.get("type", ""), c.get("values", [])
        if t == "bookshelf:mod_loaded":
            mods.update(vals)
        elif t == "bookshelf:block_exists":
            ids += [("block", v) for v in vals]
        elif t == "bookshelf:item_exists":
            ids += [("item", v) for v in vals]
        elif t:
            ok = False
    return mods, ids, ok


def collect_refs(node, refs: list, key: str | None = None, parent: dict | None = None) -> None:
    """Raccoglie (tipo, id) dai campi che contengono nomi di registro."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k in ("neoforge:conditions", "bookshelf:load_conditions"):
                continue
            if isinstance(v, (str, list)) and k in ("item", "items", "block", "blocks", "fluid",
                                                    "tag", "loot_table_id", "lootTable", "loot_table"):
                for s in ([v] if isinstance(v, str) else v):
                    if not isinstance(s, str) or ":" not in s:
                        continue
                    if k == "tag" or s.startswith("#"):
                        reg = "block" if ("block" in str(node.get("type", "")) or k.startswith("block")) else "item"
                        refs.append((f"tag:{reg}", s.lstrip("#")))
                    elif k in ("item", "items"):
                        refs.append(("item", s))
                    elif k in ("block", "blocks"):
                        refs.append(("block", s))
                    elif k == "fluid":
                        refs.append(("fluid", s))
                    elif k == "loot_table_id":
                        refs.append(("loot_table?", s))
                    else:
                        refs.append(("loot_table", s))
            elif isinstance(v, str) and ":" in v and (
                    (k == "table" and node.get("type") == "neoforge:add_table")
                    or (k == "value" and node.get("type") == "minecraft:loot_table")):
                # tabella tirata da un modificatore `neoforge:add_table` o voce che rimanda a un'altra tabella;
                # `minecraft:empty` non è un file ma vale come «niente»
                if v != "minecraft:empty":
                    refs.append(("loot_table", v))
            elif k == "id" and isinstance(v, str) and ":" in v and ("count" in node or key in ("result", "results", "output")):
                # un risultato con `amount` e senza `count` è un liquido (ricette di Create con liquidi)
                refs.append(("fluid" if "amount" in node and "count" not in node else "item", v))
            else:
                collect_refs(v, refs, k, node)
    elif isinstance(node, list):
        for v in node:
            collect_refs(v, refs, key, parent)


def tag_refs(cat: str, d: dict) -> list:
    reg = cat[len("tags/"):]
    kind = {"item": "item", "block": "block", "fluid": "fluid", "entity_type": "entity_type",
            "worldgen/biome": "biome"}.get(reg, reg)
    out = []
    for v in d.get("values", []):
        if isinstance(v, dict):
            if not v.get("required", True):
                continue
            v = v.get("id", "")
        if not isinstance(v, str) or ":" not in v:
            continue
        out.append((f"tag:{reg}", v[1:]) if v.startswith("#") else (kind, v))
    return out


def datapack_files(pack: Path) -> list:
    out = []
    for dp in sorted((pack / "config" / "paxi" / "datapacks").glob("*/data")):
        for p in sorted(dp.rglob("*.json")):
            parts = p.relative_to(dp).parts
            c = categorize(list(parts[1:]))
            if not c:
                continue
            cat, path = c
            try:
                d = json.loads(p.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue  # lo segnala già check_pack.py
            out.append((p, parts[0], cat, f"{parts[0]}:{path}", d))
    return out


def main(pack_dir: str, inv_dir: str, report: str | None) -> int:
    pack, inv = Path(pack_dir), Path(inv_dir)
    idx = load_index(inv)
    errors, warnings, inactive = [], [], []
    errors += [f"File scaricato diverso dal metafile: {e}" for e in idx.hash_errors]

    # 1. Dipendenze obbligatorie e versione di NeoForge richiesta
    present = idx.modids | BUILTIN_MODS
    versions = tomllib.loads((pack / "pack.toml").read_text(encoding="utf-8")).get("versions", {})
    provided: dict[str, list[str]] = defaultdict(list)   # mod id -> versioni presenti (anche annidate)
    for _, m in idx.mods:
        v = str(m.get("version") or "")
        if re.search(r"\d", v) and "${" not in v:
            provided[m["modid"]].append(v)
    for label, m in idx.mods:
        who = m["modid"] + (f" (dentro {m['jar']})" if m.get("jar") else "")
        for dep in m.get("deps", []):
            if dep.get("type") == "incompatible" and dep.get("modid") in idx.modids:
                # L'intervallo dice quali versioni sono incompatibili (es. solo quelle vecchie)
                vers = provided.get(dep["modid"])
                if not vers or in_range(max(vers, key=_ver), dep.get("range")):
                    errors.append(f"Mod incompatibili insieme: `{who}` [{label}] dichiara incompatibile `{dep['modid']}` {dep.get('range') or ''}, che è nel pack".rstrip())
            if dep.get("type") != "required":
                continue
            if dep.get("modid") not in present:
                errors.append(f"Dipendenza mancante: `{who}` [{label}] richiede `{dep['modid']}` {dep.get('range') or ''}".rstrip())
            # Solo NeoForge: gli intervalli su minecraft in gioco non vengono fatti rispettare
            # (es. mod con [1.21,1.21.1) girano lo stesso), darebbero falsi errori
            elif dep.get("modid") == "neoforge" and versions.get("neoforge"):
                if not in_range(versions[dep["modid"]], dep.get("range")):
                    errors.append(f"Versione non adatta: `{who}` [{label}] richiede {dep['modid']} {dep['range']}, il pack usa {versions[dep['modid']]}")
            # Le altre mod: si confronta con la versione più alta presente (NeoForge sceglie quella)
            elif dep.get("modid") not in BUILTIN_MODS and provided.get(dep["modid"]):
                best = max(provided[dep["modid"]], key=_ver)
                if not in_range(best, dep.get("range")):
                    errors.append(f"Versione non adatta: `{who}` [{label}] richiede {dep['modid']} {dep['range']}, nel pack c'è {best}")

    # 2. Datapack
    files = datapack_files(pack)
    add_datapack_definitions(idx, files)
    can_verify = not idx.unverified
    for p, ns, cat, rid, d in files:
        rel = p.relative_to(pack).as_posix()
        if not isinstance(d, dict):
            continue
        mods, cond_ids, analyzable = parse_conditions(d)
        missing_mods = [m for m in mods if m not in present]
        missing_ns = [i for _, i in cond_ids if i and i.split(":")[0] not in idx.namespaces]
        if missing_mods or missing_ns:
            note = " (o è in una mod non inventariata)" if idx.unverified else ""
            inactive.append(f"`{rel}`: inattivo, manca {', '.join(missing_mods + missing_ns)}{note}")
            continue
        if analyzable:
            for kind, i in cond_ids:
                if i and not idx.has(kind, i):
                    errors.append(f"`{rel}`: condizione mai vera, `{i}` non esiste ({kind}): il file non si caricherà mai")
        if cat.startswith("tags/"):
            refs = tag_refs(cat, d)
        elif cat == "loot_modifiers" and rid == "neoforge:global_loot_modifiers":
            refs = [("loot_modifiers", e) for e in d.get("entries", []) if isinstance(e, str)]
        else:
            refs = []
            collect_refs(d, refs)
        for kind, i in refs:
            ins = i.split(":")[0]
            soft = kind == "loot_table?"
            k = "loot_table" if soft else kind
            if ins not in idx.namespaces:
                if soft:
                    continue  # tabella di una mod non nel pack: innocuo
                msg = f"`{rel}`: `{i}` ({k}) appartiene a `{ins}`, che non è nel pack"
                (warnings if not can_verify else errors).append(msg + ("" if can_verify else " (o è in una mod non inventariata)"))
                continue
            if not idx.has(k, i):
                msg = f"`{rel}`: `{i}` ({k}) non esiste"
                (warnings if soft else errors).append(msg)
    warnings += [f"Mod non inventariata, nomi non verificabili: {u}" for u in idx.unverified]
    errors, warnings = list(dict.fromkeys(errors)), list(dict.fromkeys(warnings))  # niente doppioni

    lines = ["# Controllo dei nomi", "",
             "File generato da `scripts/check_ids.py` sull'inventario di questa cartella. Non modificarlo a mano.", "",
             f"- Mod nell'inventario: {len(idx.mods)} (mod id), namespace: {len(idx.namespaces)}",
             f"- File del datapack controllati: {len(files)} ({len(inactive)} inattivi)",
             f"- **Errori: {len(errors)}** · avvisi: {len(warnings)}", ""]
    for title, items in (("Errori", errors), ("Avvisi", warnings), ("File inattivi (mod non nel pack)", inactive)):
        lines.append(f"## {title}")
        lines.append("")
        lines += [f"- {x}" for x in sorted(set(items))] or ["- nessuno"]
        lines.append("")
    text = "\n".join(lines)
    print(text)
    if report:
        Path(report).parent.mkdir(parents=True, exist_ok=True)
        Path(report).write_text(text, encoding="utf-8")
    return 1 if errors else 0


if __name__ == "__main__":
    args = sys.argv[1:]
    rep = None
    if "--report" in args:
        i = args.index("--report")
        rep = args[i + 1]
        args = args[:i] + args[i + 2:]
    if len(args) != 2:
        raise SystemExit(__doc__)
    sys.exit(main(args[0], args[1], rep))
