import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import curated as C

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
inv = json.load(open(os.path.join(HERE, "inv.json")))
cov = json.load(open(os.path.join(HERE, "cov.json")))

ORDER = [
    ("Cucina", ["farmers-delight", "veggies-delight", "expanded-delight", "cultural-delights", "farmers-delight-extended",
                "lets-do-herbalbrews", "delightful-fares", "twilight-delight", "undergarden-delight", "l_enders-cataclysm-delight",
                "the-aethers-delight", "enders-delight", "brewin-and-chewin", "arsdelight", "occult-delight", "roasters-delight",
                "rustic-delight", "my-nethers-delight", "oceans-delight", "chefs-delight", "create-confectionery", "autochefs-delight"]),
    ("Natura", ["hexalia", "hexerei", "aspect-alchemy", "bountiful-fares", "lets-do-vinery", "lets-do-meadow", "lets-do-farm-charm",
                "seasonal-lets-do", "snow-real-magic"]),
    ("Magia", ["ars-nouveau", "ars-elemental", "occultism", "reactive", "psi"]),
    ("Mondi", ["aether", "deep-aether", "the-undergarden", "deeperdarker", "unusual_end", "twilight-forest", "regions-unexplored",
               "supplementaries", "l_enders-cataclysm"]),
    ("In arrivo / extra", ["farming-for-blockheads", "friends-and-foes-forge"]),
]
TITLES = {
    "farmers-delight": "Farmer's Delight 1.3.4", "veggies-delight": "Veggies Delight 1.9.3", "expanded-delight": "Expanded Delight 0.1.4",
    "cultural-delights": "Cultural Delights 0.19.1", "farmers-delight-extended": "Farmer's Delight: Extended", "lets-do-herbalbrews": "[Let's Do] HerbalBrews 1.1.4",
    "delightful-fares": "Delightful Fares", "twilight-delight": "Twilight's Flavor & Delight 3.2.6", "undergarden-delight": "Undergarden Delight",
    "l_enders-cataclysm-delight": "Cataclysm Delight", "the-aethers-delight": "Aether's Delight 0.1.4.2", "enders-delight": "Ender's Delight 1.3.1",
    "brewin-and-chewin": "Brewin' and Chewin' 4.5.0", "arsdelight": "Ars Nouveau's Flavors & Delight", "occult-delight": "Occult Delight",
    "roasters-delight": "Roaster's Delight 1.0.0.1 (CurseForge, sorgente chiuso)", "rustic-delight": "Rustic Delight 1.7.1 (in arrivo)",
    "my-nethers-delight": "My Nether's Delight 1.10.4 (in arrivo)", "oceans-delight": "Ocean's Delight (in arrivo)", "chefs-delight": "Chef's Delight (in arrivo)",
    "create-confectionery": "Create Confectionery (in arrivo)", "autochefs-delight": "Autochef's Delight (in arrivo)",
    "hexalia": "Hexalia 1.3.6", "hexerei": "Hexerei 0.5.0.3", "aspect-alchemy": "Aspect Alchemy", "bountiful-fares": "Bountiful Fares 3.0.12",
    "lets-do-vinery": "[Let's Do] Vinery 1.5.5", "lets-do-meadow": "[Let's Do] Meadow 1.4.9", "lets-do-farm-charm": "[Let's Do] Farm & Charm 1.1.28",
    "seasonal-lets-do": "Seasonal Let's Do", "snow-real-magic": "Snow! Real Magic!", "ars-nouveau": "Ars Nouveau 5.13.3",
    "ars-elemental": "Ars Elemental (CurseForge)", "occultism": "Occultism 1.224.5", "reactive": "Reactive 10.2.1", "psi": "Psi",
    "aether": "The Aether 1.5.10", "deep-aether": "Deep Aether 1.1.5.1", "the-undergarden": "The Undergarden 0.9.6",
    "deeperdarker": "Deeper and Darker 1.4.1", "unusual_end": "Unusual End 2.3.1b", "twilight-forest": "The Twilight Forest 4.8.3345 (CurseForge)",
    "regions-unexplored": "Regions Unexplored 0.6.2", "supplementaries": "Supplementaries 4.0.2", "l_enders-cataclysm": "L_Ender's Cataclysm 3.33",
    "farming-for-blockheads": "Farming for Blockheads 21.1.14 (in arrivo)", "friends-and-foes-forge": "Friends & Foes (fuori lista, già nel pack)",
}
COV_LABEL = {
    "bp": "(a) Botany Pots nativo", "bt": "(b) Botany Trees nativo", "mod": "(c) compat inclusa nella mod", "mt": "(d) matteo_tweaks",
    "bcl": "(e) BCL (dichiarato, non verificato)", "none": "(f) non coperta", "bt-unreleased": "(f) non coperta (BT solo nel sorgente, non nella 21.1.7)",
    "alias": "(a?) Botany Pots con vecchio ID (alias RU 0.6, da verificare)",
}
SOIL_JSON = {
    "dirt": None,
    "water": {"tag": "botanypots:soil/water"},
    "mushroom": {"type": "bookshelf:either", "ingredients": [{"type": "bookshelf:block_tag", "tag": "minecraft:mushroom_grow_block"}, {"tag": "botanypots:soil/mushroom"}]},
    "nether": {"type": "bookshelf:either", "ingredients": [{"type": "bookshelf:block_tag", "tag": "minecraft:nylium"}, {"tag": "botanypots:soil/nether"}]},
    "end": {"tag": "botanypots:soil/end"},
    "sand": {"tag": "botanypots:soil/sand"},
    "sculk": {"tag": "botanypots:soil/sculk"},
    "stone": {"tag": "botanypots:soil/moss"},
}


def soil_key(s):
    for k in ("water", "mushroom", "nether", "end", "sand", "sculk", "stone", "dirt"):
        if s.startswith(k):
            return k
    return "custom"


def block_info(mod, block):
    key = C.INV_KEY.get(mod)
    if not key or key not in inv:
        return None
    return inv[key]["blocks"].get(block)


def growth(props):
    if not props:
        return ""
    parts = []
    for k in ("age", "stage", "growth", "height", "half", "berries", "pepper", "lit", "flower_amount", "has_torchberries", "glowy", "attached"):
        if k in props:
            v = props[k]
            if all(x.isdigit() for x in v):
                parts.append(f"{k}={min(int(x) for x in v)}..{max(int(x) for x in v)}" if len(v) > 1 else f"{k}={v[0]}")
            else:
                parts.append(f"{k}={'/'.join(v)}")
    return ", ".join(parts)


def cov_paths(block, inp):
    res = []
    for r in cov:
        if "error" in r:
            continue
        ids = [v for k, v in r.get("ids", [])]
        if r.get("block") == block or (inp and inp in ids and r.get("type", "").endswith("crop")):
            res.append(f"{r['src']}:{r['path']}")
    return sorted(set(res))




def recipe_hint(r):
    """Draft 1.21.1 recipe for uncovered plants (review before use)."""
    b = r["block"]
    if r["coverage"] in COVERED or r["prio"] == "skip" or b.startswith("?") or ":trellis" in b or b.split(":")[1].startswith("trellis") or not r["input"]:
        return None
    h = {"bookshelf:load_conditions": [{"type": "bookshelf:block_exists", "values": [b]}],
         "type": "botanypots:block_derived_crop", "block": b, "input": {"item": r["input"]}}
    if r["soil_json"] is not None:
        h["soil"] = r["soil_json"]
    if "sapling" in r["kind"]:
        h["grow_time"] = 2400
    if r.get("display"):
        h["display"] = {"type": "botanypots:simple", "block_state": {"block": r["display"]}}
    if "hanging" in r["kind"] or "appes" in (r["special"] or "").lower():
        h["render_options"] = {"rotation": "X_180"}
    if not r["derived"] and r["drops"]:
        drops, items = [], []
        for d in r["drops"]:
            if d.startswith("loot:"):
                drops.append({"type": "botanypots:loot_table", "table_id": d[5:]})
                continue
            if "?" in d or "cesoie" in d:
                continue
            m = re.match(r"([a-z0-9_.:-]+)(?: \((\d+)%\))?", d)
            if m:
                e = {"result": {"id": m.group(1), "count": 1}}
                if m.group(2):
                    e["chance"] = int(m.group(2)) / 100
                items.append(e)
        if items:
            drops.append({"type": "botanypots:items", "items": items})
        if drops:
            h["drops"] = drops
    return h


rows = []
seen = set()
for e in C.ENTRIES:
    b = e["block"]
    info = block_info(e["mod"], b) if (":" in b and not b.split(":")[1].startswith("trellis") and not b.startswith("?")) else None
    cov_code = e["cov"]
    if cov_code == "none" and e["mod"] in C.BCL_MODS:
        cov_code = "bcl"
    paths = cov_paths(b, e["input"]) if cov_code in ("bp", "bt", "mod", "mt", "alias") else []
    r = dict(e)
    r["coverage"] = cov_code
    r["coverage_label"] = COV_LABEL[cov_code]
    r["coverage_files"] = paths
    r["growth_property"] = growth(info["props"]) if info else ""
    r["loot_drops"] = (info or {}).get("loot")
    r["soil_key"] = soil_key(e["soil"])
    r["soil_json"] = SOIL_JSON.get(r["soil_key"])
    rows.append(r)
    seen.add(b)

# auto-add RU covered entries
ru = inv["regions_unexplored"]
RU_ALIAS_OLD = {"medium_grass", "stone_bud", "cactus_flower", "maple_leaf_pile", "red_maple_leaf_pile", "orange_maple_leaf_pile",
                "silver_birch_leaf_pile", "enchanted_birch_leaf_pile", "mauve_shrub", "mauve_sapling", "enchanted_birch_shrub", "enchanted_birch_sapling"}
for c in ru["candidates"]:
    b = c["block"]
    if b in seen or b.split(":")[1] in RU_ALIAS_OLD:
        continue
    srcs = c["cov_block"] + c["cov_item"]
    if not srcs or any("/soil/" in s for s in srcs):
        continue
    code = "bt" if any(s.startswith("bt:") for s in srcs) else "bp"
    kind = "sapling" if code == "bt" else ("mushroom" if "shroom" in b else "plant")
    info = ru["blocks"].get(b)
    rows.append(dict(mod="regions-unexplored", block=b, kind=kind, cov=code, input=b, soil="(vedi ricetta)", special="", drops=None,
                     derived=True, note="", prio="", display=None, coverage=code, coverage_label=COV_LABEL[code],
                     coverage_files=sorted(set(srcs)), growth_property=growth(info["props"]) if info else "",
                     loot_drops=(info or {}).get("loot"), soil_key="", soil_json=None))
    seen.add(b)

by_mod = {}
for r in rows:
    by_mod.setdefault(r["mod"], []).append(r)

COVERED = ("bp", "bt", "mod", "mt")


def counts(lst):
    c = {"tot": len(lst), "cov": 0, "alias": 0, "bcl": 0, "none": 0, "skip": 0}
    for r in lst:
        if r["prio"] == "skip":
            c["skip"] += 1
        elif r["coverage"] in COVERED:
            c["cov"] += 1
        elif r["coverage"] == "alias":
            c["alias"] += 1
        elif r["coverage"] == "bcl":
            c["bcl"] += 1
        else:
            c["none"] += 1
    return c


# ---------------------------------------------------------------- JSON
jout = {
    "generated": "2026-10-17",
    "scope": "Minecraft 1.21.1 NeoForge, modpack personale (Prism Launcher)",
    "botany_pots_version": "21.1.44 (sorgente bp121 = rilascio)",
    "botany_trees_version": "21.1.7 (la compat Bountiful Fares e Irregular Implements è solo nel sorgente, non rilasciata)",
    "coverage_codes": COV_LABEL,
    "bcl": {"slug": "botanycompatlayer", "version": "1.0.0", "contents_verified": False,
            "claimed_mods_in_pack": sorted(C.BCL_MODS),
            "note": "Nessun sorgente pubblico (source_url null, nessun repo GitHub trovato); il file zip su cdn.modrinth.com non è scaricabile da qui. La descrizione dice: non tutte le piante, esclusi saplings e semi ambigui, Botany Trees non richiesto."},
    "mods_without_plants": C.NO_PLANTS,
    "soils": [dict(mod=m, block=b, coverage=c, note=n) for m, b, c, n in C.SOILS],
    "summary": {},
    "plants": [],
}
for group, mods in ORDER:
    for m in mods:
        if m in by_mod:
            jout["summary"][m] = counts(by_mod[m])
        elif m in C.NO_PLANTS:
            jout["summary"][m] = {"tot": 0, "note": C.NO_PLANTS[m]}
for r in rows:
    d = {k: r[k] for k in ("mod", "block", "input", "kind", "coverage", "coverage_label", "coverage_files", "soil", "soil_key",
                           "soil_json", "growth_property", "loot_drops", "derived", "drops", "display", "special", "note", "prio")}
    d["recipe_draft"] = recipe_hint(r)
    jout["plants"].append(d)
json.dump(jout, open(os.path.join(OUT, "crop_coverage.json"), "w"), indent=1, ensure_ascii=False)

# ---------------------------------------------------------------- MD
L = []
A = L.append
tot = counts(rows)
A("# Copertura Botany Pots / Botany Trees delle piante del modpack (1.21.1)")
A("")
A("Generato il 17/10/2026 dai sorgenti 1.21.1 delle mod (rami e versioni verificati, vedi in fondo). "
  "Copertura: **(a)** Botany Pots 21.1.44 nativo, **(b)** Botany Trees 21.1.7 nativo, **(c)** compat inclusa nella mod, "
  "**(d)** il nostro `matteo_tweaks`, **(e)** BotanyCompatLayer (dichiarato, contenuto non verificabile), **(f)** non coperta.")
A("")
A("## Riepilogo")
A("")
A(f"Piante censite: **{tot['tot']}**. Coperte (a-d): **{tot['cov']}**. Coperte solo con vecchi ID di RU (alias, da verificare): **{tot['alias']}**. "
  f"Solo BCL dichiarato (da verificare): **{tot['bcl']}**. Non coperte: **{tot['none']}**. Da saltare (non adatte ai vasi): **{tot['skip']}**.")
A("")
A("| Mod | Piante | Coperte (a-d) | Alias RU | Solo BCL? | **Non coperte** | Da saltare |")
A("|---|---:|---:|---:|---:|---:|---:|")
for group, mods in ORDER:
    for m in mods:
        if m in by_mod:
            c = counts(by_mod[m])
            A(f"| {TITLES.get(m, m)} | {c['tot']} | {c['cov']} | {c['alias'] or ''} | {c['bcl'] or ''} | **{c['none']}** | {c['skip'] or ''} |")
        elif m in C.NO_PLANTS:
            A(f"| {TITLES.get(m, m)} | nessuna pianta | | | | | |")
A("")
A("## Cose da sapere")
A("")
FINDINGS = [
    "**Botany Trees 21.1.7 non copre Bountiful Fares.** La compat (8 alberi) è nel sorgente dal 3/6/2026, un giorno dopo l'ultima release: nel pack non c'è. Si possono copiare ricette e loot table `tree_drops` da BT (LGPL-2.1) nel nostro datapack.",
    "**Undergarden**: Botany Pots 21.1.44 ha solo i 10 terreni, nessuna coltura (fagioli, blisterberry, gloomgourd, funghi, fiori). Gli alberelli sono in Botany Trees.",
    "**Compat incluse nelle mod**: Veggies Delight (14 ricette) e Rustic Delight (8 ricette) sono nel formato 1.21.1 corretto; a Rustic mancano però `dark_bell_peppers` e `pale_bell_peppers`. Ars Elemental include un file **vecchio formato 1.20** (`data/botany_pots/...`, tipo `botanypots:crop` con `categories`, condizione `mod_loaded: botany_pots`) che in 1.21.1 viene ignorato: innocuo, l'alberello è comunque in Botany Trees.",
    "**Regions Unexplored 0.6** ha rinominato vari blocchi (leaf_pile → leaf_litter, mauve_shrub → lavender_wisteria_shrub, enchanted_birch_shrub → sky_wisteria_shrub, stone_bud/medium_grass → grass_sprouts, cactus_flower → saguaro_cactus_flower). Botany Pots usa ancora i vecchi ID (8 ricette): RU registra degli alias, quindi probabilmente funzionano, ma va controllato in gioco.",
    "**Brewin' and Chewin' 4.5.0** (nel pack) non ha piante; mais e uva esistono solo nel ramo di sviluppo.",
    "**BotanyCompatLayer**: nessun sorgente pubblico (Modrinth senza source_url, nessun repo GitHub dell'autore CptGummiball) e lo zip non è scaricabile da qui. Le piante delle mod che dichiara (Aether, Farm & Charm, HerbalBrews, Meadow, Vinery, Rustic Delight) sono segnate **(e)**: vanno verificate in gioco dopo averlo installato. Non copre Botany Trees e dice di aver escluso saplings e semi ambigui.",
    "**Roaster's Delight**: sorgente chiuso (ARR), ID sconosciuti. Dalla pagina CurseForge: pianta del caffè (seme: chicco non tostato), cespuglio del tè, camomilla, menta, matcha. Vanno ricavati in gioco.",
    "**Molti cespugli raccolti a clic destro** (Hexerei, Vinery, TF berry bush, Ender's Delight voidpepper, MND bullet pepper, Bountiful Fares tea shrub, Unusual End warped bush) hanno una loot table che dà solo la pianta o i semi: con `block_derived_crop` il vaso darebbe solo quello. Servono `drops` espliciti (indicati sotto).",
]
for f in FINDINGS:
    A(f"- {f}")
A("")
A("Controllo in gioco consigliato (mondo di prova con i cheat, serve il livello di permesso 4): `/botanypots debug missing seeds true true` elenca ogni seme o pianta senza ricetta e scrive delle bozze JSON in `<istanza>/botanypots/generated/crops` (tiene già conto di BCL e di questo datapack); `/botanypots debug missing soils true` fa lo stesso per i terreni; `/botanypots debug check_crops` piazza un vaso sotto i piedi e segnala nel log le colture che non producono nulla (utile per scovare i drop sbagliati).")
A("")

A("## Tabelle per mod")
A("")
for group, mods in ORDER:
    A(f"### {group}")
    A("")
    for m in mods:
        if m not in by_mod:
            if m in C.NO_PLANTS:
                A(f"**{TITLES.get(m, m)}**: nessuna pianta. {C.NO_PLANTS[m]}.")
                A("")
            continue
        lst = by_mod[m]
        A(f"#### {TITLES.get(m, m)}")
        A("")
        if m in C.BCL_MODS:
            A("_Mod dichiarata da BotanyCompatLayer: le righe (e) potrebbero essere coperte da BCL, da verificare._")
            A("")
        if m == "regions-unexplored":
            covered = [r for r in lst if r["coverage"] in COVERED]
            bp_ = sorted(r["block"].split(":")[1] for r in covered if r["coverage"] == "bp")
            bt_ = sorted(r["block"].split(":")[1] for r in covered if r["coverage"] == "bt")
            A(f"Coperte da Botany Pots ({len(bp_)}): " + ", ".join(bp_) + ".")
            A("")
            A(f"Coperte da Botany Trees ({len(bt_)}): " + ", ".join(bt_) + ".")
            A("")
            lst = [r for r in lst if r["coverage"] not in COVERED]
        A("| Blocco | Seme / input | Tipo | Copertura | Note |")
        A("|---|---|---|---|---|")
        for r in lst:
            note = "; ".join(x for x in [r["special"], r["note"]] if x)
            if r["coverage_files"] and r["coverage"] in ("mod", "mt"):
                note = (note + "; " if note else "") + "file: " + ", ".join(p.split(":", 1)[1] for p in r["coverage_files"][:2])
            pr = " _(saltare)_" if r["prio"] == "skip" else (" _(bassa priorità)_" if r["prio"] == "low" else "")
            A(f"| `{r['block']}` | {('`' + r['input'] + '`') if r['input'] else '?'} | {r['kind']}{pr} | {r['coverage_label']} | {note} |")
        A("")

A("## Terreni")
A("")
A("Ogni terreno nei vasi richiede una ricetta `botanypots:block_derived_soil` per blocco. La terra fertilizzata di Farming for Blockheads è **nativa** (5 ricette in `recipe/farmingforblockheads/soil` e anche nel tag `botanypots:soil/dirt`, quindi vale per tutte le colture su terra).")
A("")
A("| Mod | Blocco | Copertura | Note |")
A("|---|---|---|---|")
for m, b, c, n in C.SOILS:
    A(f"| {TITLES.get(m, m)} | `{b}` | {c} | {n} |")
A("")

# ---------------------------------------------------------------- Da creare
A("## Da creare")
A("")
A("Formato di riferimento: `botanypots:block_derived_crop` come nei file di `matteo_tweaks` e di Botany Pots 21.1.44. "
  "Con `block_derived_crop` il seme, il display e i drop si ricavano dal blocco (stato a età massima, `berries=true` se esiste) e dalla sua loot table; "
  "il terreno di default è `botanypots:soil/dirt`. Indico **drops espliciti** quando la loot table non dà il raccolto: si scrivono con "
  "`\"drops\": [{\"type\": \"botanypots:loot_table\", \"table_id\": \"...\"}]` oppure "
  "`{\"type\": \"botanypots:items\", \"items\": [{\"result\": {\"id\": \"...\", \"count\": 1}, \"chance\": 1.0}]}`. "
  "Terreni: `water` = `{\"tag\":\"botanypots:soil/water\"}`, `mushroom` = either(block_tag `minecraft:mushroom_grow_block`, `botanypots:soil/mushroom`) come le colonie di FD, "
  "`nether` = either(block_tag `minecraft:nylium`, `botanypots:soil/nether`), `end` = `botanypots:soil/end`, `sand`, `sculk`, `stone` = `botanypots:soil/moss` (pietra + terra). "
  "Le piante appese usano `render_options.rotation: X_180` (come cave vines). Gli alberi seguono lo schema di Botany Trees: `block_derived_crop` sull'alberello, "
  "`grow_time` 2400 e `drops` da una loot table nostra (modello: `botanytrees:tree_drops/...`).")
A("")


def da_creare_rows(filter_fn, title, intro=None):
    sel = [r for r in rows if filter_fn(r)]
    if not sel:
        return
    A(f"### {title}")
    A("")
    if intro:
        A(intro)
        A("")
    for group, mods in ORDER:
        for m in mods:
            lst = [r for r in sel if r["mod"] == m]
            if not lst:
                continue
            A(f"#### {TITLES.get(m, m)} ({len(lst)})")
            A("")
            A("| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |")
            A("|---|---|---|---|---|---|")
            for r in lst:
                loot = ", ".join(x.replace(mod_ns_prefix(r), "") for x in (r["loot_drops"] or [])) or "-"
                sp = []
                if r["special"]:
                    sp.append(r["special"])
                if not r["derived"] and r["drops"]:
                    sp.append("**drops:** " + ", ".join(r["drops"]))
                if r.get("display"):
                    sp.append(f"display: `{r['display']}`")
                if r["note"]:
                    sp.append(r["note"])
                pr = " _(bassa priorità)_" if r["prio"] == "low" else ""
                A(f"| {('`' + r['input'] + '`') if r['input'] else '?'} | `{r['block']}`{pr} | {r['growth_property'] or '-'} | {loot} | {r['soil']} | {'; '.join(sp)} |")
            A("")


def mod_ns_prefix(r):
    return r["block"].split(":")[0] + ":"


da_creare_rows(lambda r: r["coverage"] in ("none", "bt-unreleased") and r["prio"] not in ("skip",),
               "1. Non coperte (da scrivere)")
da_creare_rows(lambda r: r["coverage"] == "bcl" and r["prio"] != "skip",
               "2. Dichiarate da BotanyCompatLayer (scrivere solo ciò che BCL non copre)",
               "Dopo aver installato BCL, `/botanypots debug missing seeds` dice quali di queste mancano ancora.")
da_creare_rows(lambda r: r["coverage"] == "alias",
               "3. Regions Unexplored: coperte con vecchi ID (verificare)",
               "Se in gioco questi semi non entrano nel vaso, basta copiare la ricetta di Botany Pots cambiando l'ID.")
A("### 4. Saltate")
A("")
for r in rows:
    if r["prio"] == "skip":
        A(f"- `{r['block']}`: {r['special']}")
A("")
A("### 5. Terreni da aggiungere")
A("")
for m, b, c, n in C.SOILS:
    if c.startswith("none"):
        A(f"- `{b}` ({TITLES.get(m, m)}){': ' + n if n else ''}")
A("")
A("## Fonti e versioni")
A("")
A("- Botany Pots: sorgente `Darkhax-Minecraft/BotanyPots` ramo 1.21.1 al commit 335c997 = release 21.1.44 (13/6/2026). Botany Trees: ramo 1.21.1, release 21.1.7 (2/6/2026); i commit successivi aggiungono solo Irregular Implements e Bountiful Fares.")
A("- Mod: sorgenti 1.21.1 clonati in `scratchpad/repos` (Bountiful Fares dal ramo `1.21-ML` 3.0.13, Brewin' and Chewin' dal tag `4.5.0+1.21.1`, Hexalia confrontato fra 1.3.6 e HEAD: stesse piante). Sorgente chiuso: Delightful Fares, Undergarden Delight, Chef's Delight, Create Confectionery, Roaster's Delight (valutati dalla descrizione).")
A("- BotanyCompatLayer: solo la descrizione Modrinth (v1.0.0, 28/9/2026, MIT).")
A("- Il dettaglio macchina-leggibile è in `crop_coverage.json` (stesso contenuto, con loot e proprietà di crescita). Per ogni pianta non coperta c'è anche `recipe_draft`: una bozza di ricetta 1.21.1 (load condition, block, input, soil, display, rotation, drops espliciti) da rivedere prima dell'uso; mancano solo le colture su graticcio di Bountiful Fares e Roaster's Delight.")
A("- Script di generazione: `research/cropscripts/` (covindex.py, inventory.py, javainfo.py, curated.py, build_outputs.py).")
open(os.path.join(OUT, "crop_coverage.md"), "w").write("\n".join(L) + "\n")
print("rows", len(rows), tot)
