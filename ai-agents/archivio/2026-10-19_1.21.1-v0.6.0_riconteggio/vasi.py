import json, glob, re, collections, os
INV = "1.21.1/data/inventario/mods"
cop = json.load(open("1.21.1/data/vasi/copertura.json"))
blocks, items, owner = set(), set(), {}
bp_blocks, bp_inputs, bp_soils = collections.defaultdict(list), collections.defaultdict(list), collections.defaultdict(list)
types = collections.Counter()
for f in glob.glob(f"{INV}/*.json"):
    slug = os.path.basename(f)[:-5]
    d = json.load(open(f))
    for b in (d.get("blocks") or {}): blocks.add(b); owner.setdefault(b, slug)
    for i in (d.get("items") or {}): items.add(i); owner.setdefault(i, slug)
    for r in d.get("botanypots") or []:
        t = r.get("type", "?"); types[t] += 1
        if "block" in r and "soil" not in t: bp_blocks[r["block"]].append(slug)
        if "soil" in t and "block" in r: bp_soils[r["block"]].append(slug)
        s = json.dumps(r)
        for m in re.findall(r'"(?:item|id)": "([a-z0-9_.-]+:[a-z0-9_/.-]+)"', s):
            bp_inputs[m].append(slug)
# our datapack
for p in glob.glob("1.21.1/pack/config/paxi/datapacks/matteo_tweaks/data/**/*.json", recursive=True):
    try: r = json.load(open(p))
    except Exception: continue
    t = r.get("type", "") if isinstance(r, dict) else ""
    if t.startswith("botanypots:"):
        types[t + " (nostro)"] += 1
        if "block" in r and "soil" not in t: bp_blocks[r["block"]].append("matteo_tweaks")
        if "soil" in t and "block" in r: bp_soils[r["block"]].append("matteo_tweaks")
print("tipi di ricette Botany Pots:", dict(types))
plants = cop["plants"]
prev = collections.Counter(p["coverage"] for p in plants)
print("copertura del 17/10:", dict(prev))
now = collections.Counter(); changed = []; missing = []
per_mod = collections.defaultdict(lambda: collections.Counter())
for p in plants:
    exists = p["block"] in blocks
    cov = p["block"] in bp_blocks or (p.get("input") and p["input"] in bp_inputs)
    if not exists: missing.append((p["mod"], p["block"], p["coverage"]))
    state = "coperta" if cov else ("manca il blocco" if not exists else "scoperta")
    if p["coverage"] in ("skip",): state = "esclusa"
    now[state] += 1
    per_mod[p["mod"]][state] += 1
    if p["coverage"] in ("none", "bcl", "bt-unreleased") and cov: changed.append((p["mod"], p["block"], bp_blocks.get(p["block"]) or bp_inputs.get(p.get("input"))))
    if p["coverage"] in ("bp","bt","mod","mt") and not cov: changed.append((p["mod"], p["block"], "ERA coperta, ora no"))
print("oggi:", dict(now))
print("cambiate dal 17/10:", len(changed)); [print("  ", c) for c in changed[:40]]
print("blocchi spariti:", len(missing)); [print("  ", m) for m in missing[:40]]
print()
for m, c in sorted(per_mod.items(), key=lambda x: -x[1]["scoperta"]):
    if c["scoperta"] or c["manca il blocco"]: print(f"{m:35s} scoperte {c['scoperta']:3d}  coperte {c['coperta']:3d}  blocco mancante {c['manca il blocco']}")
# mods with plant-like blocks not in copertura scope
scope_mods = set(p["mod"] for p in plants) | set(cop["summary"].keys())
pat = re.compile(r"(sapling|_crop|crops|_bush|seeds?$|_vine|sprout|_plant$|mushroom|fungus|propagule|_berries|cactus|_flower$|_bulb|_cane|_kelp|_algae|_root)")
extra = collections.defaultdict(list)
for b in sorted(blocks):
    s = owner[b]
    if s in scope_mods: continue
    if b.split(":")[0] in ("minecraft",): continue
    if pat.search(b.split(":")[1]) and b not in bp_blocks and "potted" not in b and "wall_" not in b:
        extra[s].append(b)
print("\nmod fuori dal conteggio del 17/10 con blocchi che sembrano piante non coperte:")
for s, bl in sorted(extra.items(), key=lambda x: -len(x[1])):
    print(f"  {s} ({len(bl)}): {', '.join(x.split(':')[1] for x in bl[:25])}{' …' if len(bl)>25 else ''}")
