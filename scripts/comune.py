"""Costanti e funzioni usate da più script. Solo libreria standard.

Gli script si lanciano come `python3 scripts/<nome>.py`: la cartella scripts/ è nel percorso
di ricerca, quindi basta `from comune import …`.
"""
import hashlib
import re
from pathlib import Path

# La cartella data/ del nostro datapack, dentro la cartella di una versione (es. 1.21.1/)
DATAPACK_DATA = "pack/config/paxi/datapacks/matteo_tweaks/data"


def impronta_datapack(data: Path) -> str:
    """sha256 dei file del datapack che il gioco legge (.json e .mcfunction, con il percorso; non i readme).

    Il dump del gioco vale per il datapack che aveva l'istanza: scripts/dump_importa.py salva questa impronta
    in meta.json e la base dati la confronta con quella attuale. Se sono diverse, i confronti con il gioco
    non bloccano finché non si rifà il dump.
    """
    h = hashlib.sha256()
    for f in sorted(data.rglob("*")):
        if f.is_file() and f.suffix in (".json", ".mcfunction"):
            h.update(f.relative_to(data).as_posix().encode())
            h.update(b"\0")
            h.update(f.read_bytes())
            h.update(b"\0")
    return h.hexdigest()


# ---- Tabelle e modificatori del bottino in forma compatta (0.7.5): li usano l'inventario e la base dati.
# Se cambia la forma, alzare FORMAT in inventory.py (l'inventario va rifatto).
# Delle tabelle dei blocchi si tiene solo il nome (sono quasi tutte «il blocco lascia se stesso»)
LOOT_NAME_ONLY = ("blocks/",)
GLOBAL_LOOT_MODIFIERS = "neoforge:global_loot_modifiers"
RESOURCE_ID = re.compile(r"#?[a-z0-9_.-]+:[a-z0-9_./-]+")


def _mc(t) -> str:
    return str(t or "").removeprefix("minecraft:")


def loot_number(v):
    """Tiri o quantità: il numero, {min, max} se uniforme, {n, p} se binomiale, altrimenti {type}."""
    if isinstance(v, (int, float)) or v is None:
        return v
    if not isinstance(v, dict):
        return str(v)
    t = _mc(v.get("type", "uniform"))
    if t == "constant":
        return v.get("value")
    if t == "uniform":
        return {"min": loot_number(v.get("min")), "max": loot_number(v.get("max"))}
    if t == "binomial":
        return {"n": loot_number(v.get("n")), "p": loot_number(v.get("p"))}
    return {"type": t}


def loot_condition(c):
    """Condizione in forma corta: le probabilità e le tabelle con i valori, le altre col solo tipo."""
    if not isinstance(c, dict):
        return str(c)
    t = _mc(c.get("condition"))
    if t == "random_chance":
        return {"random_chance": loot_number(c.get("chance"))}
    if t == "random_chance_with_enchanted_bonus":
        return {"random_chance_enchanted": loot_number(c.get("unenchanted_chance"))}
    if t in ("any_of", "all_of", "alternative"):
        return {t: [loot_condition(x) for x in c.get("terms") or []]}
    if t == "inverted":
        return {"not": loot_condition(c.get("term"))}
    if t == "neoforge:loot_table_id":
        return {"loot_table_id": c.get("loot_table_id")}
    if t == "reference":
        return {"reference": c.get("name")}
    return t


def load_conditions(d: dict) -> list:
    """Le condizioni di caricamento di NeoForge (`neoforge:conditions`) e di Bookshelf (`bookshelf:load_conditions`,
    una voce per nome), in forma corta."""
    def one(c):
        if not isinstance(c, dict):
            return str(c)
        t = str(c.get("type", "")).removeprefix("neoforge:")
        if t in ("mod_loaded", "item_exists", "tag_empty"):
            return f"{t}:{c.get('modid') or c.get('item') or c.get('tag')}"
        if t == "not":
            return {"not": one(c.get("value"))}
        if t in ("and", "or"):
            return {t: [one(x) for x in c.get("values") or []]}
        return t
    out = [one(c) for c in d.get("neoforge:conditions") or []]
    for c in d.get("bookshelf:load_conditions") or []:
        if isinstance(c, dict) and c.get("type") in ("bookshelf:block_exists", "bookshelf:item_exists"):
            out += [f"{c['type'].removeprefix('bookshelf:')}:{v}" for v in c.get("values") or []]
        elif isinstance(c, dict):
            out.append(str(c.get("type")))
    return out


def _functions(fs) -> tuple[list, object]:
    """(nomi delle funzioni tranne set_count, quantità data da set_count)."""
    names, count = [], None
    for f in fs or []:
        if not isinstance(f, dict):
            continue
        t = _mc(f.get("function"))
        if t == "set_count" and not f.get("add"):
            count = loot_number(f.get("count"))
        elif t == "set_potion":
            names.append(f"set_potion={f.get('id')}")
        else:
            names.append(t)
    return names, count


def loot_entry(e) -> dict:
    if not isinstance(e, dict):
        return {"kind": "?"}
    t = _mc(e.get("type"))
    out = {"kind": t}
    if t == "loot_table":
        v = e.get("value", e.get("name"))
        if isinstance(v, dict):
            out["inline"] = loot_table(v)
        else:
            out["id"] = v
    elif t in ("alternatives", "group", "sequence"):
        out["children"] = [loot_entry(x) for x in e.get("children") or []]
    elif "name" in e:
        out["id"] = e["name"]
    if t == "tag":
        out["expand"] = bool(e.get("expand", False))
    if t not in ("alternatives", "group", "sequence"):
        out["weight"] = e.get("weight", 1)
    if e.get("quality"):
        out["quality"] = e["quality"]
    fnames, count = _functions(e.get("functions"))
    if count is not None:
        out["count"] = count
    if fnames:
        out["functions"] = fnames
    if e.get("conditions"):
        out["conditions"] = [loot_condition(c) for c in e["conditions"]]
    return out


def loot_table(d: dict) -> dict:
    """Una tabella del bottino in forma compatta: tipo, condizioni di caricamento, pool con tiri e voci."""
    out = {"type": d.get("type")}
    if load := load_conditions(d):
        out["load"] = load
    pools = []
    for p in d.get("pools") or []:
        if not isinstance(p, dict):
            continue
        pool = {"rolls": loot_number(p.get("rolls", 1))}
        if p.get("bonus_rolls"):
            pool["bonus_rolls"] = loot_number(p["bonus_rolls"])
        if p.get("conditions"):
            pool["conditions"] = [loot_condition(c) for c in p["conditions"]]
        fnames, _ = _functions(p.get("functions"))
        if fnames:
            pool["functions"] = fnames
        pool["entries"] = [loot_entry(e) for e in p.get("entries") or []]
        pools.append(pool)
    out["pools"] = pools
    fnames, _ = _functions(d.get("functions"))
    if fnames:
        out["functions"] = fnames
    return out


def loot_modifier(d: dict) -> dict:
    """Un modificatore del bottino: tipo, tabelle bersaglio (`!` = esclusa), le altre condizioni, i parametri
    semplici e i nomi citati negli altri campi (tabelle tirate, oggetti aggiunti). Ogni mod ha il suo formato."""
    targets = []

    def walk(c, neg=False):
        if isinstance(c, dict):
            t = _mc(c.get("condition"))
            if t == "neoforge:loot_table_id":
                targets.append(("!" if neg else "") + str(c.get("loot_table_id")))
            for x in c.get("terms") or []:
                walk(x, neg)
            if t == "inverted":
                walk(c.get("term"), not neg)
    conds = d.get("conditions") or []
    for c in conds:
        walk(c)
    out = {"type": d.get("type"), "targets": targets, "conditions": [loot_condition(c) for c in conds]}
    if load := load_conditions(d):
        out["load"] = load
    params, refs = {}, []

    def ids(v):
        if isinstance(v, str):
            if RESOURCE_ID.fullmatch(v) and v not in refs:
                refs.append(v)
        elif isinstance(v, dict):
            for x in v.values():
                ids(x)
        elif isinstance(v, list):
            for x in v:
                ids(x)
    for k, v in d.items():
        if k in ("type", "conditions", "neoforge:conditions", "fabric:load_conditions"):
            continue
        if isinstance(v, (str, int, float, bool)):
            params[k] = v
        ids(v)
    out["params"] = params
    out["refs"] = refs
    return out
