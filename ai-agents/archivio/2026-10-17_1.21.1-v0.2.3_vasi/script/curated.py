"""Curated inventory of plantables per mod (hand-checked against 1.21.1 sources).

E(mod, block, kind, cov, input=None, soil='dirt', special='', drops=None, derived=True, note='', prio='')
 cov: bp | bt | mod | mt | none | bt-unreleased | alias | mod-invalid
 bcl-claimed mods are flagged at mod level (BCL_MODS) - content unverified.
 drops: explicit drops needed when derived=False (list of item ids, or 'loot:<table>')
"""

ENTRIES = []


def E(mod, block, kind, cov, input=None, soil="dirt", special="", drops=None, derived=True, note="", prio="", display=None):
    ns = mod_ns(mod)
    b = block if (":" in block or block.startswith("?")) else f"{ns}:{block}"
    i = None
    if input:
        i = input if ":" in input else f"{ns}:{input}"
    ENTRIES.append(dict(mod=mod, block=b, kind=kind, cov=cov, input=i, soil=soil, special=special,
                        drops=drops, derived=derived, note=note, prio=prio, display=display))


NS = {
    "farmers-delight": "farmersdelight", "veggies-delight": "veggiesdelight", "expanded-delight": "expandeddelight",
    "cultural-delights": "culturaldelights", "lets-do-herbalbrews": "herbalbrews", "twilight-delight": "twilightdelight",
    "the-aethers-delight": "aethersdelight", "enders-delight": "endersdelight", "rustic-delight": "rusticdelight",
    "my-nethers-delight": "mynethersdelight", "hexalia": "hexalia", "hexerei": "hexerei", "bountiful-fares": "bountifulfares",
    "lets-do-vinery": "vinery", "lets-do-meadow": "meadow", "lets-do-farm-charm": "farm_and_charm",
    "ars-nouveau": "ars_nouveau", "ars-elemental": "ars_elemental", "occultism": "occultism", "reactive": "reactive",
    "aether": "aether", "deep-aether": "deep_aether", "the-undergarden": "undergarden", "deeperdarker": "deeperdarker",
    "unusual_end": "unusualend", "twilight-forest": "twilightforest", "regions-unexplored": "regions_unexplored",
    "supplementaries": "supplementaries", "l_enders-cataclysm": "cataclysm", "farming-for-blockheads": "farmingforblockheads",
    "friends-and-foes-forge": "friendsandfoes", "roasters-delight": "roastersdelight",
}


def mod_ns(mod):
    return NS.get(mod, mod)


# inventory key in inv.json for each mod slug
INV_KEY = {
    "farmers-delight": "farmersdelight", "veggies-delight": "veggiesdelight", "expanded-delight": "expandeddelight",
    "cultural-delights": "culturaldelights", "lets-do-herbalbrews": "herbalbrews", "twilight-delight": "twilightdelight",
    "the-aethers-delight": "aethersdelight", "enders-delight": "endersdelight", "rustic-delight": "rusticdelight",
    "my-nethers-delight": "mynethersdelight", "hexalia": "hexalia", "hexerei": "hexerei", "bountiful-fares": "bountifulfares",
    "lets-do-vinery": "vinery", "lets-do-meadow": "meadow", "lets-do-farm-charm": "farm_and_charm",
    "ars-nouveau": "ars_nouveau", "ars-elemental": "ars_elemental", "occultism": "occultism", "reactive": "reactive",
    "aether": "aether", "deep-aether": "deep_aether", "the-undergarden": "undergarden", "deeperdarker": "deeperdarker",
    "unusual_end": "unusualend", "twilight-forest": "twilightforest", "regions-unexplored": "regions_unexplored",
    "supplementaries": "supplementaries", "l_enders-cataclysm": "cataclysm", "farming-for-blockheads": "farmingforblockheads",
    "friends-and-foes-forge": "friendsandfoes",
}

BCL_MODS = {"aether", "lets-do-farm-charm", "lets-do-herbalbrews", "lets-do-meadow", "lets-do-vinery", "rustic-delight"}

# ---------------------------------------------------------------- mods without plants
NO_PLANTS = {
    "farmers-delight-extended": "Solo ricette/cibi (verificato: nessun blocco nel sorgente 0.2.x)",
    "delightful-fares": "Sorgente chiuso; da descrizione Modrinth: bollitore e tè, nessuna coltura",
    "undergarden-delight": "Sorgente chiuso; da descrizione: coltelli, pasti, mobili; nessuna coltura",
    "l_enders-cataclysm-delight": "Verificato (sorgente 1.21.1): solo cibi, unico blocco una torta",
    "brewin-and-chewin": "4.5.0 (versione nel pack, tag verificato): nessuna pianta. Il ramo di sviluppo (post-4.5.0) aggiunge mais e uva (corn_crop, wild_corn, red/white_grape_bush, wild_grapes): da rivedere quando esce",
    "arsdelight": "Verificato: solo cibi/blocchi di cibo (usa le piante di Ars Nouveau)",
    "occult-delight": "Verificato: un solo blocco (Occult Cooking Pot)",
    "oceans-delight": "Verificato: solo cibi",
    "chefs-delight": "Sorgente chiuso; da descrizione: villici cuoco/chef, nessuna pianta",
    "create-confectionery": "Sorgente chiuso (MCreator); da descrizione: cioccolato, nessuna pianta",
    "autochefs-delight": "Verificato: solo mixin, nessuna risorsa",
    "aspect-alchemy": "Verificato: solo calderoni",
    "seasonal-lets-do": "Solo compatibilità stagioni per i Let's Do",
    "snow-real-magic": "Nessuna pianta nuova (cambia solo neve e piante esistenti)",
    "psi": "Verificato: nessuna pianta",
    "l_enders-cataclysm": "Nessuna pianta (Botany Pots nativo aggiunge solo the_baby_leviathan_bucket come terreno acqua)",
}

# ---------------------------------------------------------------- Farmer's Delight (BP native)
m = "farmers-delight"
E(m, "cabbages", "crop", "bp", "cabbage_seeds")
E(m, "tomatoes", "crop", "bp", "tomato_seeds", special="pianta rampicante (budding_tomatoes -> tomatoes su corda)")
E(m, "onions", "crop", "bp", "onion")
E(m, "rice", "crop", "bp", "rice", soil="water", special="2 blocchi (rice + rice_panicles)")
E(m, "brown_mushroom_colony", "mushroom colony", "bp", "brown_mushroom_colony", soil="mushroom")
E(m, "red_mushroom_colony", "mushroom colony", "bp", "red_mushroom_colony", soil="mushroom")
for w in ["wild_cabbages", "wild_onions", "wild_tomatoes", "wild_carrots", "wild_potatoes", "wild_beetroots"]:
    E(m, w, "wild crop", "bp", w)
E(m, "wild_rice", "wild crop", "bp", "wild_rice", special="alta 2 blocchi")
E(m, "sandy_shrub", "bush", "bp", "sandy_shrub", soil="sand")

# ---------------------------------------------------------------- Veggies Delight (bundled, valid)
m = "veggies-delight"
for b, s in [("bellpepper_crop", "bellpepper_seeds"), ("broccoli_crop", "broccoli_seeds"), ("cauliflower_crop", "cauliflower_seeds"),
             ("garlic_crop", "garlic_clove"), ("sweet_potato_crop", "sweet_potato"), ("turnip_crop", "turnip_seeds"), ("zucchini_crop", "zucchini_seeds")]:
    E(m, b, "crop", "mod", s)
for w in ["wild_bellpeppers", "wild_broccoli", "wild_cauliflowers", "wild_garlic", "wild_sweet_potatoes", "wild_turnips", "wild_zucchinis"]:
    E(m, w, "wild crop", "mod", w)
E(m, "mature_dandelion", "flower", "none", "mature_dandelion", note="drop dandelion_leaf; il bonemeal la duplica")

# ---------------------------------------------------------------- Expanded Delight (nothing)
m = "expanded-delight"
E(m, "asparagus_crop", "crop", "none", "asparagus_seeds")
E(m, "chili_pepper_crop", "crop", "none", "chili_pepper_seeds")
E(m, "peanut_crop", "crop", "none", "peanut")
E(m, "sweet_potato_crop", "crop", "none", "sweet_potato", note="stesso nome di veggiesdelight:sweet_potato ma item diverso")
E(m, "cranberry_plant", "water bush", "none", "cranberries", soil="water",
  special="si piazza sull'acqua come una ninfea (LilypadCropItem); raccolta a clic destro", note="loot a age=3 dà cranberries: derivato ok")
E(m, "cinnamon_sapling", "sapling", "none", "cinnamon_sapling", special="albero: serve ricetta stile Botany Trees (drop cinnamon_log + sapling)",
  derived=False, drops=["expandeddelight:cinnamon_log", "expandeddelight:cinnamon_sapling (5%)", "expandeddelight:cinnamon_leaves (cesoie)"])
for w in ["wild_asparagus", "wild_chili_pepper", "wild_peanuts", "wild_sweet_potato"]:
    E(m, w, "wild crop", "none", w)

# ---------------------------------------------------------------- Cultural Delights (nothing)
m = "cultural-delights"
E(m, "cucumbers", "crop", "none", "cucumber_seeds")
E(m, "eggplants", "crop", "none", "eggplant_seeds", note="le wild_eggplants droppano anche white_eggplant (non coltivabile a parte: il blocco white_eggplants non è registrato)")
E(m, "corn", "crop", "none", "corn_kernels", special="alta 3 blocchi (proprietà height 0..2); il display di default mostra solo il blocco basso: meglio display con height",
  note="loot (height=0, age=7): corn_cob + corn_kernels")
E(m, "beans", "climbing crop", "none", "beans", special="come i pomodori di FD: i semi piazzano budding_beans (age 0..4) che diventa beans su corda; usare block=beans come fa BP con farmersdelight:tomatoes",
  note="raccolta: bean_pod")
E(m, "avocado_sapling", "sapling", "none", "avocado_sapling", special="albero da frutto (fruiting_avocado_leaves): ricetta stile Botany Trees", derived=False,
  drops=["culturaldelights:avocado_log", "culturaldelights:avocado", "culturaldelights:avocado_sapling (5%)"])
E(m, "avocado_pit", "sapling", "none", "avocado_pit", special="nocciolo = alberello (SaplingBlock con grower proprio): stessa ricetta dell'avocado", derived=False,
  drops=["culturaldelights:avocado_log", "culturaldelights:avocado", "culturaldelights:avocado_pit (5%)"])
E(m, "lemon_sapling", "sapling", "none", "lemon_sapling", special="albero da frutto (fruiting_lemon_leaves): ricetta stile Botany Trees", derived=False,
  drops=["culturaldelights:lemon_log", "culturaldelights:lemon", "culturaldelights:lemon_sapling (5%)"],
  note="non confondere con bountifulfares:lemon_sapling")
for w in ["wild_cucumbers", "wild_eggplants", "wild_corn", "wild_beans"]:
    E(m, w, "wild crop", "none", w)
E(m, "agave", "wild herb", "none", "agave")
E(m, "mint", "wild herb", "none", "mint")
E(m, "magic_beans", "special", "none", "magic_beans", special="fagiolo magico che genera un beanstalk gigante: non adatto ai vasi", prio="skip")

# ---------------------------------------------------------------- HerbalBrews (BCL claimed)
m = "lets-do-herbalbrews"
E(m, "coffee_plant", "crop", "none", "coffee_beans", note="clic destro dà coffee_beans; loot a age=3 ok")
E(m, "tea_plant", "crop", "none", "tea_blossom", note="loot age=3: green_tea_leaf + tea_blossom")
E(m, "rooibos_plant", "crop", "none", "rooibos_leaf")
E(m, "yerba_mate_plant", "crop", "none", "yerba_mate_leaf")
for w in ["wild_coffee_plant", "wild_rooibos_plant", "wild_yerba_mate_plant"]:
    E(m, w, "wild crop", "none", w)
E(m, "hibiscus", "flower", "none", "hibiscus")
E(m, "lavender", "flower", "none", "lavender")

# ---------------------------------------------------------------- Twilight's Flavor & Delight
m = "twilight-delight"
E(m, "fiddlehead_clump", "colony", "none", "fiddlehead_clump", soil="mushroom",
  special="colonia stile FD (MushroomColonyBlock) + parte alta fiddlehead_clump_upper", note="drop twilightforest:fiddlehead")
E(m, "mushgloom_colony", "mushroom colony", "none", "mushgloom_colony", soil="mushroom", note="drop twilightforest:mushgloom")
E(m, "ironwood_sapling", "sapling", "none", "ironwood_sapling", special="albero: ricetta stile Botany Trees", derived=False,
  drops=["twilightdelight:ironwood_log", "twilightdelight:ironwood_sapling (5%)", "twilightdelight:ironwood_leaves (cesoie)"])

# ---------------------------------------------------------------- Aether's Delight
m = "the-aethers-delight"
E(m, "ginger_crop", "crop", "none", "ginger")
E(m, "leek_crop", "crop", "none", "leek")
E(m, "parsnip_crop", "crop", "none", "parsnip")
E(m, "peppermint_bush", "berry bush", "none", "peppermint_bush_stem",
  special="come il cespuglio di bacche dell'Aether: lo stelo cresce in cespuglio; display peppermint_bush",
  derived=False, drops=["aethersdelight:peppermint_leaf"], note="loot del cespuglio: peppermint_bush/stem/leaf (con condizioni): meglio drops espliciti")
for w in ["wild_ginger", "wild_leek", "wild_parsnip"]:
    E(m, w, "wild crop", "none", w)

# ---------------------------------------------------------------- Ender's Delight
m = "enders-delight"
E(m, "amberveil_mushroom", "end mushroom", "none", "amberveil", soil="end")
E(m, "chorusflame_bush", "end bush", "none", "chorusflame", soil="end", note="age 0..2")
E(m, "ethereal_saffron_bush", "end bush", "none", "ethereal_saffron", soil="end")
E(m, "voidpepper_bush", "end bush", "none", "voidpepper", soil="end", derived=False, drops=["endersdelight:voidpepper"],
  special="block entity; proprietà pepper=true/false (BP non la imposta): drops espliciti")

# ---------------------------------------------------------------- Roaster's Delight (closed)
m = "roasters-delight"
for n in ["? (pianta del caffè; seme: chicco non tostato)", "? (cespuglio del tè)", "? (camomilla)", "? (menta)", "? (matcha)"]:
    E(m, n, "unknown", "none", None, special="ID sconosciuti (sorgente chiuso, ARR): ricavarli in gioco con /botanypots debug missing seeds", prio="verify")

# ---------------------------------------------------------------- Rustic Delight (bundled valid + BCL claimed)
m = "rustic-delight"
E(m, "bell_peppers", "crop", "mod", "bell_pepper_seeds")
E(m, "coffee", "crop", "mod", "coffee_beans")
E(m, "cotton", "crop", "mod", "cotton_seeds")
for w in ["wild_bell_peppers", "wild_coffee", "wild_cotton", "wild_dark_bell_peppers", "wild_pale_bell_peppers"]:
    E(m, w, "wild crop", "mod", w)
E(m, "dark_bell_peppers", "crop", "none", "dark_bell_pepper_seeds", note="mancante nella compat inclusa nella mod")
E(m, "pale_bell_peppers", "crop", "none", "pale_bell_pepper_seeds", note="mancante nella compat inclusa nella mod")

# ---------------------------------------------------------------- My Nether's Delight
m = "my-nethers-delight"
E(m, "bullet_pepper", "nether bush", "none", "bullet_pepper", soil="nether",
  special="PowderyFlowerBlock age 0..3 + proprietà lit; raccolta a clic destro", derived=False, drops=["mynethersdelight:bullet_pepper"],
  note="sopravvive su #mynethersdelight:powdery_cannon_plantable_on (netherrack, nylium, sabbia, terra, soul soil, magma)")
E(m, "powdery_cannon", "cane", "none", "powder_cannon", soil="nether",
  special="multi-blocco tipo bambù (powdery_chubby_sapling -> powdery_cannon/powdery_cane); display come il bambù di BP",
  derived=False, drops=["mynethersdelight:powder_cannon", "mynethersdelight:bullet_pepper"])
E(m, "crimson_fungus_colony", "fungus colony", "none", "crimson_fungus_colony", soil="nether", note="drop minecraft:crimson_fungus")
E(m, "warped_fungus_colony", "fungus colony", "none", "warped_fungus_colony", soil="nether", note="drop minecraft:warped_fungus")

# ---------------------------------------------------------------- Hexalia
m = "hexalia"
E(m, "mandrake_crop", "crop", "none", "mandrake_seeds")
E(m, "rabbage_crop", "crop", "none", "rabbage_seeds")
E(m, "sunfire_tomato_crop", "crop", "none", "sunfire_tomato_seeds")
E(m, "chillberry_bush", "berry bush", "none", "chillberries", note="loot a age=3: chillberries")
E(m, "saltsprout", "bush", "none", "saltsprout", soil="sand", note="sabbia o infused_farmland; age 0..2")
E(m, "galeberries_vine", "hanging vine", "none", "galeberries", special="tipo cave vines (appesa): rotation X_180; BP imposta berries=true da solo")
E(m, "wild_mandrake", "wild crop", "none", "wild_mandrake", note="loot: mandrake_seeds")
E(m, "wild_sunfire_tomato", "wild crop", "none", "wild_sunfire_tomato", note="loot: sunfire_tomato_seeds")
for f in ["aegiflora", "astrylis", "begonia", "celestial_bloom", "dahlia", "ghost_fern", "grimshade", "lavender", "lourdes", "morphora",
          "nautilite", "nightshade_bush", "spirit_bloom", "witchweed"]:
    E(m, f, "flower", "none", f, soil="dirt")
E(m, "withered_aegiflora", "flower", "none", "withered_aegiflora", prio="low")
E(m, "withered_celestial_bloom", "flower", "none", "withered_celestial_bloom", prio="low")
E(m, "windsong", "flower", "none", "windsong", special="ha un block entity (si attiva col Hex Focus): solo estetica nel vaso", prio="low")
E(m, "dreamshroom", "mushroom", "none", "dreamshroom", soil="mushroom")
E(m, "pale_mushroom", "mushroom", "none", "pale_mushroom", soil="mushroom", special="flower_amount 1..4 (tipo pink petals)")
E(m, "lotus_flower", "water plant", "none", "lotus_flower", soil="water", special="ninfea (WaterlilyBlock)")
E(m, "siren_kelp", "water plant", "none", "siren_kelp", soil="water", special="tipo seagrass")
E(m, "cottonwood_sapling", "sapling", "none", "cottonwood_sapling", special="albero: ricetta stile Botany Trees", derived=False,
  drops=["hexalia:cottonwood_log", "hexalia:cottonwood_sapling (5%)", "hexalia:cottonwood_catkin?"])
E(m, "willow_sapling", "sapling", "none", "willow_sapling", special="albero: ricetta stile Botany Trees (diverso dal salice di Hexerei)", derived=False,
  drops=["hexalia:willow_log", "hexalia:willow_sapling (5%)"])

# ---------------------------------------------------------------- Hexerei
m = "hexerei"
E(m, "mandrake_plant", "herb bush", "none", "mandrake_plant", derived=False, drops=["hexerei:mandrake_flowers", "hexerei:mandrake_root"],
  special="PickablePlant age 0..3: i prodotti si raccolgono a clic destro, il loot dà solo la pianta")
E(m, "belladonna_plant", "herb bush", "none", "belladonna_plant", derived=False, drops=["hexerei:belladonna_flowers", "hexerei:belladonna_berries"],
  special="PickablePlant age 0..3")
E(m, "mugwort_bush", "herb bush", "none", "mugwort_bush", derived=False, drops=["hexerei:mugwort_leaves", "hexerei:mugwort_flowers"],
  special="doppia altezza (half lower/upper) + age 0..3")
E(m, "yellow_dock_bush", "herb bush", "none", "yellow_dock_bush", derived=False, drops=["hexerei:yellow_dock_leaves", "hexerei:yellow_dock_flowers"],
  special="doppia altezza (half lower/upper) + age 0..3")
E(m, "sage_crop", "crop", "none", "sage_seed")
E(m, "willow_vines", "hanging vine", "none", "willow_vines", special="liana appesa (GrowingPlantHead): rotation X_180", prio="low")
E(m, "flowering_lily_pad", "water plant", "none", "flowering_lily_pad", soil="water")
for s in ["mahogany_sapling", "willow_sapling", "witch_hazel_sapling"]:
    E(m, s, "sapling", "bt", s)

# ---------------------------------------------------------------- Bountiful Fares
m = "bountiful-fares"
for s, inp in [("apple_sapling", None), ("golden_apple_sapling", None), ("hoary_apple_sapling", None), ("lemon_sapling", None),
               ("orange_sapling", None), ("palm_sapling", "coconut"), ("plum_sapling", None), ("walnut_sapling", None)]:
    E(m, s, "sapling", "bt-unreleased", inp or s,
      note="Botany Trees ha la compat nel sorgente (commit 3/6/2026) ma NON nella 21.1.7 rilasciata: copiare ricetta + loot table tree_drops da BT (LGPL-2.1)")
E(m, "leeks", "crop", "none", "leek_seeds")
E(m, "maize_crop", "crop", "none", "maize_seeds", special="alta 2 blocchi (half lower/upper)")
E(m, "hoary_apple_sapling_crop", "special", "none", "hoary_seeds", special="i semi crescono (age 0..1) e diventano un alberello di melo canuto", prio="low",
  derived=False, drops=["bountifulfares:hoary_apple_sapling"])
E(m, "tea_shrub", "bush", "none", "tea_berries", derived=False, drops=["bountifulfares:tea_leaves", "bountifulfares:tea_berries"],
  special="age 0..4 + berries; foglie con le cesoie, bacche col bonemeal")
E(m, "scorchkin_stem", "stem crop", "none", "scorchkin_seeds", soil="custom: blocco solido sopra + lava vicino (in pratica: soil/lava o nether)",
  special="stelo APPESO al soffitto che fa crescere il frutto scorchkin sotto, solo vicino alla lava", derived=False,
  drops=["bountifulfares:scorchkin"], display="bountifulfares:scorchkin")
E(m, "spongekin_stem", "stem crop", "none", "spongekin_seeds", soil="water",
  special="stelo subacqueo; il frutto spongekin cresce sopra", derived=False, drops=["bountifulfares:spongekin"], display="bountifulfares:spongekin")
E(m, "spongekin_sprout", "water plant", "none", "spongekin_sprout", soil="water", note="loot: spongekin_seeds", prio="low")
for t, seed, prod in [("elderberry", "elderberries", "elderberries"), ("lapisberry", "lapisberry_seeds", "lapisberries"), ("passion_fruit", "passion_fruit", "passion_fruit")]:
    E(m, f"trellis:{t}", "trellis crop", "none", seed, derived=False, drops=[f"bountifulfares:{prod}"],
      special="coltura su graticcio (data-driven, nessun blocco dedicato): serve ricetta botanypots:crop con display a scelta (es. wild_*_vine o il graticcio)")
for f in ["chamomile_flowers", "honeysuckle", "violet_bellflower"]:
    E(m, f, "flower", "none", f)
E(m, "prismarine_blossom", "water plant", "none", "prismarine_blossom", soil="water", note="loot: prismarine_crystals/shard")
for w in ["wild_beetroots", "wild_carrots", "wild_potatoes", "wild_wheat", "wild_leeks"]:
    E(m, w, "wild crop", "none", w)
E(m, "wild_maize", "wild crop", "none", "wild_maize", special="alta 2 blocchi")
E(m, "wild_elderberry_vine", "wild crop", "none", "wild_elderberry_vine")
E(m, "wild_passion_fruit_vine", "wild crop", "none", "wild_passion_fruit_vine")

# ---------------------------------------------------------------- Vinery (BCL claimed)
m = "lets-do-vinery"
for col in ["red", "white"]:
    E(m, f"{col}_grape_bush", "berry bush", "none", f"{col}_grape_seeds", derived=False, drops=[f"vinery:{col}_grape"],
      special="uva a clic destro: il loot dà solo i semi")
    E(m, f"savanna_grape_bush_{col}", "berry bush", "none", f"savanna_grape_seeds_{col}", derived=False, drops=[f"vinery:savanna_grapes_{col}"],
      special="luce minima 14")
    E(m, f"taiga_grape_bush_{col}", "berry bush", "none", f"taiga_grape_seeds_{col}", derived=False, drops=[f"vinery:taiga_grapes_{col}"],
      special="nel mondo vuole podzol/coarse dirt vicino")
    E(m, f"jungle_grape_bush_{col}", "vine bush", "none", f"jungle_grape_seeds_{col}", derived=False, drops=[f"vinery:jungle_grapes_{col}"],
      special="è una liana (VineBlock) attaccata di lato: display da sistemare (rotazione/offset)")
E(m, "grapevine_stem", "special", "none", "grapevine_stem", special="vite su graticcio (lattice): sistema a più blocchi, meglio usare i cespugli", prio="skip")
for s in ["apple_tree_sapling", "dark_cherry_sapling"]:
    E(m, s, "sapling", "bt", s)

# ---------------------------------------------------------------- Meadow (BCL claimed)
m = "lets-do-meadow"
for f in ["alpine_poppy", "delphinium", "enzian", "eriophorum", "fire_lily", "saxifrage"]:
    E(m, f, "flower", "none", f)
E(m, "tall_eriophorum", "tall flower", "none", "tall_eriophorum", special="alta 2 blocchi")
E(m, "small_fir", "tall plant", "none", "small_fir", special="alta 2 blocchi", prio="low")
for s in ["alpine_birch_sapling", "pine_sapling", "yellow_pine_sapling"]:
    E(m, s, "sapling", "bt", s)

# ---------------------------------------------------------------- Farm & Charm (BCL claimed)
m = "lets-do-farm-charm"
E(m, "barley_crop", "crop", "none", "barley_seeds")
E(m, "corn_crop", "crop", "none", "kernels")
E(m, "lettuce_crop", "crop", "none", "lettuce_seeds", note="big/giant: il derivato prende lo stato normale")
E(m, "oat_crop", "crop", "none", "oat_seeds")
E(m, "onion_crop", "crop", "none", "onion")
E(m, "strawberry_crop", "crop", "none", "strawberry_seeds")
E(m, "tomato_crop", "climbing crop", "none", "tomato_seeds", special="rampicante con corda (tomato_crop + tomato_crop_body); il loot dà anche farm_and_charm:rope se supported")
for w in ["wild_barley", "wild_beetroots", "wild_carrots", "wild_emmer", "wild_lettuce", "wild_nettle", "wild_oat", "wild_onions",
          "wild_potatoes", "wild_ribwort", "wild_strawberries", "wild_tomatoes"]:
    E(m, w, "wild crop", "none", w)
E(m, "wild_corn", "wild crop", "none", "wild_corn", special="alta 2 blocchi")

# ---------------------------------------------------------------- Ars Nouveau / Elemental (covered)
m = "ars-nouveau"
E(m, "magebloom_crop", "crop", "mt", "magebloom_crop")
E(m, "sourceberry_bush", "berry bush", "mt", "sourceberry_bush")
for p, soil in [("bombegranate_pod", "ars_nouveau:blazing_logs"), ("bastion_pod", "ars_nouveau:vexing_logs"),
                ("frostaya_pod", "ars_nouveau:cascading_logs"), ("mendosteen_pod", "ars_nouveau:flourishing_logs")]:
    E(m, p, "pod", "mt", p, soil=f"archwood log (#{soil})")
for c in ["blue", "green", "purple", "red"]:
    E(m, f"{c}_archwood_sapling", "sapling", "bt", f"{c}_archwood_sapling")
m = "ars-elemental"
E(m, "flashpine_pod", "pod", "mt", "flashpine_pod", soil="yellow archwood log")
E(m, "yellow_archwood_sapling", "sapling", "bt", "yellow_archwood_sapling",
  note="la mod include anche data/botany_pots/recipe/ars_elemental/flashing_archwood.json: formato 1.20 (botanypots:crop con categories) in namespace sbagliato botany_pots e condizione mod_loaded 'botany_pots': ignorato in 1.21.1")
E(m, "sparkflower", "flower", "none", "sparkflower")

# ---------------------------------------------------------------- Occultism (BP/BT native)
m = "occultism"
E(m, "datura", "crop", "bp", "datura_seeds")
E(m, "otherflower", "flower", "bp", "otherflower")
E(m, "otherflower_natural", "flower", "bp", "otherflower_natural")
E(m, "otherworld_sapling", "sapling", "bt", "otherworld_sapling")
E(m, "otherworld_sapling_natural", "sapling", "bt", "otherworld_sapling_natural")

# ---------------------------------------------------------------- Reactive
m = "reactive"
E(m, "flower_vine", "vine", "none", "flower_vine", special="nasce da reazioni alchemiche, non è una coltura", prio="low")
E(m, "mind_lichen", "lichen", "none", "mind_lichen", special="variante del glow lichen creata dalle reazioni", prio="low")

# ---------------------------------------------------------------- Aether (BCL claimed)
m = "aether"
E(m, "berry_bush", "berry bush", "none", "berry_bush_stem", special="lo stelo (berry_bush_stem) cresce in cespuglio", derived=False,
  drops=["aether:blue_berry"], note="nel mondo vuole terra dell'Aether; nel vaso va bene la terra normale")
E(m, "purple_flower", "flower", "none", "purple_flower")
E(m, "white_flower", "flower", "none", "white_flower")
E(m, "skyroot_sapling", "sapling", "bt", "skyroot_sapling")
E(m, "golden_oak_sapling", "sapling", "bt", "golden_oak_sapling")

# ---------------------------------------------------------------- Deep Aether
m = "deep-aether"
E(m, "squash_stem", "stem crop", "none", "squash_seeds", derived=False, display="deep_aether:blue_squash",
  drops=["deep_aether:blue_squash (34%)", "deep_aether:green_squash (33%)", "deep_aether:purple_squash (33%)"],
  special="come la zucca: il frutto è casuale fra blue/green/purple_squash")
E(m, "golden_vines", "hanging vine", "none", "goldenleaf_berries", special="tipo cave vines (appesa): rotation X_180; BP imposta berries=true")
E(m, "lightcap_mushrooms", "mushroom", "none", "lightcap_mushrooms", soil="mushroom")
for f in ["aerlavender", "aether_cattails", "echaisy", "enchanted_blossom", "golden_aspess", "iaspove", "radiant_orchid", "sky_tulips"]:
    E(m, f, "flower", "none", f)
E(m, "tall_aerlavender", "flower", "none", "tall_aerlavender")
E(m, "tall_aether_cattails", "tall flower", "none", "tall_aether_cattails", special="alta 2 blocchi")
E(m, "golden_flower", "tall flower", "none", "golden_flower", special="alta 2 blocchi")
for g in ["feather_grass", "mini_golden_grass", "short_golden_grass", "medium_golden_grass"]:
    E(m, g, "grass", "none", g, prio="low")
for g in ["tall_feather_grass", "tall_golden_grass"]:
    E(m, g, "grass", "none", g, special="alta 2 blocchi", prio="low")
E(m, "yagroot_vine", "vine", "none", "yagroot_vine", prio="low")
for s in ["roseroot_sapling", "blue_roseroot_sapling", "conberry_sapling", "cruderoot_sapling", "sunroot_sapling", "yagroot_sapling"]:
    E(m, s, "sapling", "bt", s)

# ---------------------------------------------------------------- Undergarden
m = "the-undergarden"
E(m, "underbean_bush", "berry bush", "none", "underbeans", note="loot a age=3: underbeans")
E(m, "blisterberry_bush", "berry bush", "none", "blisterberry", note="loot a age=3: blisterberry + rotten_blisterberry")
E(m, "ditchbulb_plant", "bush", "none", "ditchbulb", note="age 0..1; loot age=1: ditchbulb")
E(m, "droopvine", "hanging vine", "none", "droopvine_item", special="appesa (tipo cave vines): rotation X_180; il frutto dipende da glowy=true (BP non lo imposta)",
  derived=False, drops=["undergarden:droopvine_item"])
E(m, "gloomgourd_stem", "stem crop", "none", "gloomgourd_seeds", derived=False, display="undergarden:gloomgourd",
  drops=["loot:undergarden:blocks/gloomgourd"], special="come melone/zucca (StemBlock)")
E(m, "glitterkelp", "water plant", "none", "glitterkelp", soil="water", special="tipo kelp")
for mu in ["blood_mushroom", "indigo_mushroom", "ink_mushroom", "veil_mushroom", "puff_mushroom"]:
    E(m, mu, "mushroom", "none", mu, soil="mushroom")
for f in ["amorous_bristle", "butterbunch", "miserabell"]:
    E(m, f, "flower", "none", f)
E(m, "shimmerweed", "flower", "none", "shimmerweed")
E(m, "tall_shimmerweed", "tall flower", "none", "tall_shimmerweed", special="alta 2 blocchi", note="loot: shimmerweed")
for g in ["deepturf", "ashen_deepturf", "frozen_deepturf"]:
    E(m, g, "grass", "none", g, prio="low")
E(m, "tall_deepturf", "grass", "none", "tall_deepturf", prio="low")
E(m, "mushroom_veil", "vine", "none", "mushroom_veil", special="liana appesa", prio="low")
for s in ["grongle_sapling", "smogstem_sapling", "wigglewood_sapling"]:
    E(m, s, "sapling", "bt", s)

# ---------------------------------------------------------------- Deeper and Darker
m = "deeperdarker"
for c in ["gloomy_grass", "gloomy_sculk", "glowing_flowers", "glowing_grass", "glowing_roots", "ice_lily", "lily_flower", "sculk_tendrils", "sculk_vines"]:
    E(m, c, "plant", "bp", c)
E(m, "glowing_vines", "hanging vine", "bp", "bloom_berries")
E(m, "gloomy_cactus", "cactus", "none", "gloomy_cactus", soil="sculk (nel mondo solo su gloomy_sculk)",
  note="BP tratta gloomy_sculk come coltura, non come terreno: usare botanypots:soil/sculk")
E(m, "echo_sapling", "sapling", "bt", "echo_sapling")

# ---------------------------------------------------------------- Unusual End
m = "unusual_end"
E(m, "chorus_cane", "cane", "none", "chorus_cane", soil="end", special="colonna tipo canna (blooming_chorus_cane è la variante fiorita, drop chorus_cane)")
E(m, "chorus_fungus", "end fungus", "none", "chorus_fungus", soil="end")
E(m, "chorus_roots", "end plant", "none", "chorus_roots", soil="end")
E(m, "endstone_sprouts", "end plant", "none", "endstone_sprouts", soil="end", prio="low")
E(m, "purpur_grass", "end plant", "none", "purpur_grass", soil="end", prio="low")
E(m, "flowering_purpur_grass", "end flower", "none", "flowering_purpur_grass", soil="end", note="loot: chorus_petal")
E(m, "crystal_flower", "flower", "none", "crystal_flower", note="loot: shiny_crystal; terra/erba/gloopstone")
E(m, "gloopy_bush", "plant", "none", "gloopy_bush")
E(m, "gloopy_tendrils", "plant", "none", "gloopy_tendrils", prio="low")
E(m, "shiny_spirea", "flower", "none", "shiny_spirea")
E(m, "flowering_gloopy_pile", "tall plant", "none", "flowering_gloopy_pile", special="alta 2 blocchi", prio="low")
E(m, "warped_bush", "end bush", "none", "warped_bush", soil="end", derived=False, drops=["unusualend:warped_berries"], display="unusualend:grown_warped_bush",
  special="col bonemeal diventa grown_warped_bush, che a clic destro dà warped_berries")
E(m, "warped_algae", "end plant", "none", "warped_algae", soil="end")
E(m, "small_warped_algae", "end plant", "none", "small_warped_algae", soil="end", prio="low")
E(m, "warped_sprouts", "end plant", "none", "warped_sprouts", soil="end", prio="low")
E(m, "warped_endstone_sprouts", "end plant", "none", "warped_endstone_sprouts", soil="end", prio="low")
E(m, "small_warped_squash", "special", "none", "small_warped_squash", soil="end", derived=False, drops=["unusualend:warped_squash_wedge", "unusualend:warped_squash"],
  display="unusualend:warped_squash", special="zucca della Warped Reef (piccola -> grande col bonemeal)")
E(m, "gloopilon_bulb", "hanging crop", "none", "gloopilon_seeds", soil="custom: dripping_gloopstone sopra",
  special="cresce APPESO sotto dripping gloopstone (seeds -> stem -> bulb age 0..2): rotation X_180", derived=False, drops=["unusualend:gloopilon_slice"])
E(m, "chorus_cane_flower", "flower", "none", "chorus_cane_flower", prio="low", special="fiore da parete/pavimento (face)")

# ---------------------------------------------------------------- Twilight Forest
m = "twilight-forest"
for c in ["clover_patch", "fiddlehead", "huge_lily_pad", "huge_water_lily", "mayapple", "moss_patch", "mushgloom", "root_strand", "thorn_rose", "torchberry_plant"]:
    E(m, c, "plant", "bp", c)
for s in ["canopy", "darkwood", "hollow_oak", "mangrove", "mining", "rainbow_oak", "sorting", "time", "transformation", "twilight_oak"]:
    E(m, f"{s}_sapling", "sapling", "bt", f"{s}_sapling")
for b in ["raspberry", "blueberry", "blackberry", "maloberry"]:
    E(m, f"{b}_bush", "berry bush", "none", f"{b}_bush", soil="dirt", derived=False, drops=[f"loot:twilightforest:blocks/{b}_bush_berries"],
      special="TF berry bush age 0..3 (+ layers neve); le bacche vengono da una loot table separata")
for b in ["blightberry", "duskberry", "skyberry", "stingberry"]:
    E(m, f"{b}_bush", "berry bush", "none", f"{b}_bush", soil="nether", derived=False, drops=[f"loot:twilightforest:blocks/{b}_bush_berries"],
      special="cespuglio della Dark Tower: vive su netherrack/blackstone/soul sand/soul soil")
for o in ["iron", "gold", "copper", "essence"]:
    table = "essence_berry_bush_berries" if o == "essence" else f"{o}_oreberry_bush_berries"
    E(m, f"{o}_oreberry", "oreberry bush", "none", f"{o}_oreberry", soil="stone (#c:stones; botanypots:soil/moss li include)", derived=False,
      drops=[f"loot:twilightforest:blocks/{table}"], special="cespuglio di bacche-minerale: su pietra, luce < 13 nel mondo")
E(m, "magic_beans", "special", "none", "magic_beans", special="beanstalk gigante: non adatto ai vasi", prio="skip")

# ---------------------------------------------------------------- Supplementaries
m = "supplementaries"
E(m, "flax", "crop", "bp", "flax_seeds", special="alta 2 blocchi")
E(m, "wild_flax", "wild crop", "bp", "wild_flax")

# ---------------------------------------------------------------- Regions Unexplored (only uncovered/alias here; covered ones added from inventory)
m = "regions-unexplored"
E(m, "blue_bioshroom", "sapling (fungo gigante)", "none", "blue_bioshroom", soil="mushroom", special="come green/pink/yellow_bioshroom di Botany Trees (che però salta il blu)",
  derived=False, drops=["regions_unexplored:blue_bioshroom_stem", "regions_unexplored:blue_bioshroom_block", "regions_unexplored:glowing_blue_bioshroom_block", "regions_unexplored:blue_bioshroom (5%)"])
E(m, "salmon_poppy", "flower", "none", "salmon_poppy")
E(m, "salmon_wisteria_shrub", "tall shrub", "none", "salmon_wisteria_shrub", special="alta 2 blocchi")
for c in ["lavender", "salmon", "sky"]:
    E(m, f"{c}_wisteria_vines", "hanging vine", "none", f"{c}_wisteria_vines", special="liana appesa (tip)", prio="low")
E(m, "tall_hyacinth_stock", "special", "none", "tall_hyacinth_stock", soil="water", special="pianta subacquea a colonna (forma tip/frustum)", prio="low")
E(m, "redstone_bud", "special", "none", "redstone_bud", soil="stone", special="germoglio su pietra che droppa redstone: farm di redstone, valutare", prio="low")
E(m, "saguaro_cactus_flower", "special", "none", "saguaro_cactus_flower", soil="sand", note="ex cactus_flower (alias); BP ha solo saguaro_cactus", prio="low")
E(m, "grass_sprouts", "grass", "alias", "grass_sprouts", note="BP 1.21.1 lo copre coi vecchi ID stone_bud/medium_grass, rinominati in RU 0.6 (alias)")
E(m, "lavender_wisteria_shrub", "tall shrub", "alias", "lavender_wisteria_shrub", note="BP lo copre col vecchio ID mauve_shrub (alias RU 0.6)")
E(m, "sky_wisteria_shrub", "tall shrub", "alias", "sky_wisteria_shrub", note="BP lo copre col vecchio ID enchanted_birch_shrub (alias RU 0.6)")
for l in ["maple", "red_maple", "orange_maple", "silver_birch", "enchanted_birch"]:
    E(m, f"{l}_leaf_litter", "leaf litter", "alias", f"{l}_leaf_litter", note=f"BP lo copre col vecchio ID {l}_leaf_pile (alias RU 0.6)")

# ---------------------------------------------------------------- Friends & Foes (not in requested list, but in pack)
m = "friends-and-foes-forge"
E(m, "buttercup", "flower", "none", "buttercup", note="mod fuori dalla lista richiesta ma presente nel pack", prio="low")

# ---------------------------------------------------------------- Soils
SOILS = [
    # (mod, block, coverage, note)
    ("farmers-delight", "farmersdelight:rich_soil", "bp", ""),
    ("farmers-delight", "farmersdelight:rich_soil_farmland", "bp", "growth_modifier 0.15"),
    ("farmers-delight", "farmersdelight:organic_compost", "bp", ""),
    ("farming-for-blockheads", "farmingforblockheads:fertilized_farmland_rich", "bp", "soil recipe + nel tag botanypots:soil/dirt (yield +10%)"),
    ("farming-for-blockheads", "farmingforblockheads:fertilized_farmland_rich_stable", "bp", ""),
    ("farming-for-blockheads", "farmingforblockheads:fertilized_farmland_healthy", "bp", ""),
    ("farming-for-blockheads", "farmingforblockheads:fertilized_farmland_healthy_stable", "bp", ""),
    ("farming-for-blockheads", "farmingforblockheads:fertilized_farmland_stable", "bp", ""),
    ("twilight-forest", "twilightforest:uberous_soil", "bp", ""),
    ("the-undergarden", "undergarden:deepsoil / deepsoil_farmland / coarse_deepsoil / deepturf_block / ashen_deepturf_block / frozen_deepturf_block / depthrock / shiverstone / tremblecrust / gwibling_bucket", "bp", "10 terreni nativi"),
    ("deeperdarker", "deeperdarker:gloomslate / sculk_stone / blooming_moss_block", "bp", ""),
    ("supplementaries", "supplementaries:planter", "bp", ""),
    ("l_enders-cataclysm", "cataclysm:the_baby_leviathan_bucket", "bp", "acqua"),
    ("twilight-delight", "twilightdelight:twilight_rich_soil", "none", "per le colonie (fiddlehead_clump, mushgloom_colony)"),
    ("twilight-delight", "twilightdelight:twilight_rich_soil_farmland", "none", ""),
    ("my-nethers-delight", "mynethersdelight:resurgent_soil", "none", "terra del Nether (stile rich soil)"),
    ("my-nethers-delight", "mynethersdelight:resurgent_soil_farmland", "none", ""),
    ("my-nethers-delight", "mynethersdelight:letios_compost", "none", "compost del Nether"),
    ("hexalia", "hexalia:infused_dirt", "none", "nel tag minecraft:dirt"),
    ("hexalia", "hexalia:infused_farmland", "none", "serve anche al saltsprout"),
    ("lets-do-farm-charm", "farm_and_charm:fertilized_soil", "none (BCL?)", ""),
    ("lets-do-farm-charm", "farm_and_charm:fertilized_farmland", "none (BCL?)", ""),
    ("lets-do-vinery", "vinery:loam", "none (BCL?)", "facoltativo"),
    ("aether", "aether:aether_dirt / aether_grass_block / enchanted_aether_grass_block / aether_farmland", "none (BCL?)", "la descrizione di BCL parla di 'extra natural soil blocks'"),
    ("deep-aether", "deep_aether:aether_mud / aether_coarse_dirt / aerglow_grass_block / golden_heights_grass_block / aether_moss_block", "none", "facoltativi"),
    ("bountiful-fares", "bountifulfares:grassy_dirt", "none", "facoltativo (nel tag minecraft:dirt)"),
]
