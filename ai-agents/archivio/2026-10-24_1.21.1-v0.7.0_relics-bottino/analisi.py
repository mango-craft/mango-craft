#!/usr/bin/env python3
"""Bottino di Relics contro le nostre casse (24/10/2026).

Uso: python3 analisi.py <sorgente relics> <sorgente rar-compat> <repo mango-craft>
- sorgenti: github.com/Octo-Studios/relics e /rar-compat, ramo 1.21.1 (commit a50b42c e 2b6d624 il 24/10);
- legge da ogni reliquia le categorie di `LootTemplate.builder()...entry(LootEntries.X)`;
- confronta i nomi delle 152 tabelle dei nostri 15 file (`matteo_tweaks/loot_modifiers/artifacts/`) con la regola
  delle tabelle di Relics (`[\\w]+:chests\\/...`, `LootEntries.java`) e con i nomi delle categorie;
- conta le tabelle `chests/` nell'inventario del pack.
"""
import collections, glob, json, os, re, sys

relics, rar, repo = sys.argv[1:4]
per = {}
for mod, root in (("rar", rar), ("relics", relics)):
    for f in glob.glob(root + "/src/main/java/**/*.java", recursive=True):
        t = open(f).read()
        m = re.search(r"LootTemplate\.builder\(\)(.*?)\.build\(\)\)", t, re.S)
        if m:
            per[f"{mod}:{os.path.basename(f)[:-5]}"] = re.findall(r"LootEntries\.([A-Z_]+)", m.group(1))
print("## Categorie per reliquia\n")
for k, v in sorted(per.items()):
    print(f"- {k}: {', '.join(v)}")

W = r"[\w]+:chests\/[\w_\/]*"
base = re.compile(W + r"[\w]+[\w_\/]*")
nomi = {"VILLAGE": "(village|pillage)", "MINESHAFT": "(mine)", "BASTION": "(bastion|piglin)",
        "NETHER_LIKE": "(nether|infern|hell|chasm|lava|magma|m[eo]lt|fire|flame|blaze|ember|pyre)",
        "END_LIKE": "(end|stronghold)"}
dp = os.path.join(repo, "1.21.1/pack/config/paxi/datapacks/matteo_tweaks/data/matteo_tweaks/loot_modifiers/artifacts")
tab = []
for f in sorted(glob.glob(dp + "/*.json")):
    tab += [(os.path.basename(f)[:-5], i) for i in re.findall(r'"loot_table_id":\s*"([^"]+)"', open(f).read())]
dentro = [t for _, t in tab if base.fullmatch(t)]
fuori = [(f, t) for f, t in tab if not base.fullmatch(t)]
print(f"\n## Nostre casse: {len(tab)}; nel bottino di Relics: {len(dentro)}; fuori: {len(fuori)}\n")
for f, t in fuori:
    print(f"- {t} (file {f})")
c = collections.Counter()
for t in dentro:
    m = [k for k, p in nomi.items() if re.fullmatch(W + p + r"[\w_\/]*", t)]
    if t == "minecraft:chests/ruined_portal":
        m.append("NETHER_LIKE")
    c[",".join(m) or "solo bioma e dimensione"] += 1
print("\n## Categorie per nome tra le casse dentro\n")
for k, v in c.most_common():
    print(f"- {k}: {v}")
allt = set()
for f in glob.glob(os.path.join(repo, "1.21.1/data/inventario/mods/*.json")) + [os.path.join(repo, "1.21.1/data/inventario/minecraft.json")]:
    d = json.load(open(f))
    if isinstance(d.get("data"), dict):
        allt.update(d["data"].get("loot_table") or [])
print(f"\n## Inventario: {len(allt)} tabelle, {sum(1 for t in allt if base.fullmatch(t))} con `chests/` (anche sottotabelle)")
