# Existing Botany Pots / Botany Trees / Farming for Blockheads compat for the pack (MC 1.21.1 NeoForge)

Research date: 2026-10-17. Pack baseline: Botany Pots (BP) 21.1.44, Botany Trees (BT) 21.1.7, BP Tiers 7.0.11, Bookshelf 21.1.81, Paxi, Farming for Blockheads (FfB) 21.1.14.

## Search coverage and limits

- **Modrinth** (API through WebFetch): searched `botany pots` (32 hits), `botany` (53), `botanypots` (11), `pots compat` (14), `delight botany`, `aether botany`, `let's do botany`, `farming for blockheads`, `farmingforblockheads`, `blockheads`, `market compat`, `market seeds saplings`, `vinery`, `hexerei`, `bountiful fares`. I read every relevant hit's project and version metadata.
- **CurseForge** (search pages through WebFetch): searched data-packs for `Botany` (21 results), `pots` (63), `blockheads`, `market`, and mc-mods for `Botany Pots` (40), `botany` (pages 1–2 of 160), `farming for blockheads`. I opened every relevant project page.
- **GitHub**:
  - Code search was not possible. The `gh` token is invalid, `api.github.com/search` is blocked by the session policy, and `github.com/search` is robots-blocked.
  - I used grep.app and the Sourcegraph public stream API instead. They index only popular repos, so small datapack repos are mostly missing.
  - `git clone` works. I cloned (shallow, into new dirs under `scratchpad/repos/x_*`): every candidate that has a source repo, the target mods' own repos (most were already in `scratchpad/repos/`), and the Craftoria, Farmopolis and ATM10 pack data. All of it was treated as data only and nothing was executed.
- **Downloads**: `cdn.modrinth.com`, `api.modrinth.com` and CurseForge files are blocked for the shell, and WebFetch is robots-blocked on the CDN. That means **zip contents of Modrinth/CF-only datapacks could NOT be inspected**. For those, the format verdict comes from metadata: published for BP 1.21.1 after BP's first public 1.21.1 release (21.1.34, 2025-08-17).

**Format check reference** (BP 21.1.x, from `repos/bp121/.../data/botanypots/recipe/`):
- Folder `data/<ns>/recipe/` (singular).
- `"type": "botanypots:block_derived_crop"` with `block` and optional `input`, `soil` (Ingredient, e.g. `{"tag":"botanypots:soil/water"}`), `grow_time`, `display`, `drops` (`botanypots:items` / `botanypots:loot_table`).
- `botanypots:block_derived_soil` with `block` and `growth_modifier`.
- `botanypots:crop` / `botanypots:soil` with `input`, `display`, `drops`.
- Plus `bookshelf:load_conditions`.

The 1.20.x format does **not** load. It uses the `recipes/` folder, `"seed"`, `"categories": ["dirt"]`, `"growthTicks"`, and `drops: [{chance, output, minRolls}]`. My Nether's Botany is a clean example of the old format.

**Built-in tool worth knowing (BP 21.1.44):** `/botanypots debug missing seeds <include_saplings> <generate>` and `/botanypots debug missing soils <generate>` (permission level 4; singleplayer with cheats is enough).
- With `generate=true`, it writes ready `block_derived_crop` / `block_derived_soil` JSON for every plant or soil not yet covered to `<instance>/botanypots/generated/crops|soils/<ns>/...`.
- It guesses the soil (water for lily pads and coral, mushroom, sand for cactus, sculk) and adds load conditions.
- Source: `MissingCommand.java`, `MissingCropGenerator.java`.
- This makes "write our own" largely a generate-and-review job.

## 1. Summary per target mod

Legend: **native** = shipped by BP 21.1.44, BT 21.1.7 or the target mod itself. "Plantables" is a rough list from the mod repos' blockstates and items, not exhaustive.

| Target mod (pack version) | Plantables seen | Best existing source | Coverage / gaps |
|---|---|---|---|
| **Veggies Delight** 1.9.3 | 7 crops + 7 wild | **Native: the mod ships its own BP recipes** (`data/veggiesdelight/recipe/integration/botany/`, 1.21.1 format, since VD 1.8.2/1.8.3, Aug–Sep 2025) | Complete. Nothing to write. |
| **Rustic Delight** 1.7.1 | cotton, bell pepper, coffee + 5 wild | **Native: the mod ships `data/botanypots/recipe/rusticdelight/crop/*`** (fixed Apr 2026, wild pale/dark peppers Jul 2026) | Complete. Mega Addon and BotanyCompatLayer add **duplicate** RD recipes with different IDs. Avoid stacking them. |
| **Cultural Delights** 0.19.1 | corn, cucumber, eggplant, white eggplant, beans/beanstalk, 4 wild, avocado + lemon sapling | Mega Addon (MIT, verified), LayaTweaks (ARR, verified), More Crop Compatibility (MIT, unverified) | All three cover only corn/cucumber/eggplant; LayaTweaks also has avocado as a fruit-only "crop". More Crop Compat adds the wild variants; its companion BT pack adds an avocado tree. **No pack covers white eggplant, beans/beanstalk, wild beans or lemon sapling.** |
| **Expanded Delight** 0.1.4 | asparagus, chili, peanut, sweet potato, cranberry, 4 wild, cinnamon sapling | Mega Addon (5 crops, MIT, verified); Wizardon's BP Tweaks (claims ED, MIT, unverified) | Mega lacks the wild variants and the cinnamon tree. Wizardon's completeness is unknown. |
| **My Nether's Delight** 1.10.4.1 | bullet pepper, powdery cane/cannon, crimson/warped fungus colony, resurgent soil + farmland | Mega Addon (MIT, verified): bullet pepper, both colonies, both resurgent soils | **Powdery cane (powder cannon) missing.** My Nether's Botany has it but is 1.20.1 format (reference only). |
| **Bountiful Fares** 3.0.12 | maize, spongekin, passion fruit, elderberry, chamomile, violet bellflower, wild crops; 8 fruit saplings | **Trees: BT repo commit `eee0890` (2026-06-03, AFTER BT 21.1.7 shipped, unreleased)**: 8 recipes + 8 loot tables, LGPL-2.1 | Trees: copy from BT repo (or wait for BT 21.1.8+). **Crops: nothing found.** |
| **Hexerei** 0.5.0.3 | mandrake, belladonna, mugwort, yellow dock, sage, lily pad; mahogany/willow/witch hazel | **Trees native in BT 21.1.7** | **Crops: nothing found.** |
| **Hexalia** 1.3.6 | mandrake, sunfire tomato, rabbage, chillberry, nightshade, galeberries, saltsprout, dreamshroom, pale mushroom, lotus, siren kelp, spirit/celestial bloom…; cottonwood + willow sapling | "Hexalia x Botany Pot Compatibility" (CurseForge, **1.20.1 Forge only**, MIT): outdated format | **Nothing usable on 1.21.1.** The CF mod can serve as a design reference (12 crops on infused dirt, siren kelp on water). Trees not covered by BT. |
| **The Aether** 1.5.10 | berry bush, white/purple flower, aether soils; skyroot/golden oak saplings | Trees **native BT 21.1.7**; plants: **BotanyCompatLayer** (claims "The Aether", MIT, unverified) | Probably covered by BotanyCompatLayer (contents unseen). |
| **Deep Aether** 1.1.5.1 | flowers, lightcap/aercloud mushrooms, vines, tall alien plant; 6 saplings | Trees **native BT 21.1.7** (6 saplings) | **Plants: nothing found.** BotanyCompatLayer does not list Deep Aether. |
| **Aether's Delight** 0.1.4.2 | ginger, leek, parsnip, peppermint + 3 wild | none | **Nothing found.** |
| **Farm & Charm** 1.1.28 | Let's Do crops | **BotanyCompatLayer** (MIT, unverified) | Claimed "not every entry". "Pots and Plants" (CF) is 1.20.1 only. |
| **Vinery** 1.5.5 | grapes (several), cherry/apple | BotanyCompatLayer (claims); trees **native BT 21.1.7** (apple, dark cherry) | VineryBotany (CF) and Pots and Plants are 1.20.1 only. |
| **Meadow** 1.4.9 | flowers/herbs; alpine birch, pine, yellow pine | BotanyCompatLayer (claims); trees **native BT 21.1.7** | Plants depend on BotanyCompatLayer. |
| **HerbalBrews** 1.1.4 | tea/herb crops | BotanyCompatLayer (claims) | Pots and Plants is 1.20.1 only. |
| **Brewin' And Chewin'** 4.5.0 | **corn, red/white grape bushes, wild corn, wild grapes** (it does have crops) | none | **Nothing found.** |
| **Ender's Delight** 1.3.1 | amberveil mushroom, chorusflame / ethereal saffron / voidpepper bush | none | **Nothing found.** |
| **Twilight's Flavor & Delight** 3.2.6 | mushgloom colony, ironwood sapling (repo) | none | **Nothing found.** Twilight Forest itself is native in BP and BT. |
| **Undergarden Delight** 2.0.2 | unknown (ARR, no source) | none | Nothing found. Undergarden itself is native in BP and BT. "Undergarden Botany Pots Compats" (CF) is for 1.16–1.20.1 and Undergarden only. |
| **Unusual End** 2.3.1b | unknown (ARR, no source) | none | Nothing found. |
| **Delightful Fares** 1.1.2 | unknown (ARR, no source) | none | Nothing found. |
| **Farmer's Delight: Extended** 0.2.2 | no plant blocks in repo | n/a | Probably nothing needed. |
| **Cataclysm Delight** 1.0.10b | no plant blocks in repo | n/a | Probably nothing needed. Cataclysm itself is native in BP. |
| **Aspect Alchemy** 2.0.0 | no plant blocks in repo | n/a | Probably nothing needed. |
| **Ars Nouveau** 5.13.3 | magebloom, sourceberry, 4 archwood pods; 4 archwood trees | **LayaTweaks** (all 6 crops + archwood log/wood soils; ARR; verified 1.21.1 format); trees **native BT 21.1.7** | Complete via LayaTweaks. |
| **Ars Elemental** (if used) | flashpine pod; yellow archwood | LayaTweaks (flashpine + soils); tree **native BT** | Ars Elemental's **own** bundled BP file (`data/botany_pots/recipe/ars_elemental/flashing_archwood.json`) is **dead**: 1.20 format plus a `mod_loaded "botany_pots"` condition that never matches. |
| **Roaster's Delight** | not in the current pack list | none | Nothing found in any search. |
| **Regions Unexplored** 0.6.2 | plants + ~35 saplings | **Native BP + BT 21.1.7** | Complete. |

**Target mods with no existing 1.21.1 coverage at all:**
- Crops: Bountiful Fares, Hexerei, Hexalia (and its trees), Deep Aether (plants), Aether's Delight, Brewin' And Chewin', Ender's Delight, Twilight's Flavor & Delight, Undergarden Delight, Unusual End, Delightful Fares.
- Gaps inside otherwise covered mods: Cultural Delights extras (white eggplant, beans, lemon), Expanded Delight extras (wild variants, cinnamon tree), MND powdery cane.

## 2. Candidate details

### A. Usable on 1.21.1

**Botany Pots Mega Addon Project** (NeoForge mod jar)
- Links: https://www.curseforge.com/minecraft/mc-mods/botany-pots-mega-addon-project, source https://github.com/NamelessGamer06/Botany-Pots-Mega-Addon-Pack
- 1.21.1 NeoForge only. v1.1.0, 2026-06-23, 481 downloads, **MIT**.
- **Format: verified valid.** All files are `block_derived_crop` / `block_derived_soil` with `bookshelf:load_conditions`. The Java part is an empty template, so the jar is effectively a datapack.
- Content (17 files):
  - Cultural Delights: corn (`corn_upper`), cucumbers, eggplants.
  - Expanded Delight: asparagus, chili, cranberry (water soil), peanut, sweet potato.
  - Miner's Delight: cave carrot (not in pack).
  - My Nether's Delight: bullet pepper on a netherrack/soul soil/resurgent tag, crimson/warped fungus colonies on resurgent soil, plus resurgent soil and resurgent farmland soils.
  - Rustic Delight: 3 crops, which duplicate RD's own.
- Verdict: **usable partially.** Best copy-in source for the MIT parts: MND, Expanded Delight, Cultural Delights. Skip its Rustic Delight files.
- Clone: `scratchpad/repos/x_megaaddon/repo`.

**LayaTweaks BotanyPots** (datapack)
- Links: https://modrinth.com/datapack/layatweaks-botanypots (also on CurseForge), source https://github.com/LayaReed/Laya_Tweaks_Datapacks (`LayaTweaks_BotanyPots/`)
- 1.21.1. v1.4, 2025-12-26, ~160 + 1.1K downloads.
- **License: ARR** (Modrinth); the GitHub repo has no LICENSE file. Install as-is, do not copy into our pack.
- **Format: verified valid**: `block_derived_crop` with `botanypots:aging` display and `botanypots:items` drops; those IDs exist in BP 21.1.44.
- Coverage of our mods:
  - **Ars Nouveau**: magebloom, sourceberry, bastion pod, bombegranate, frostaya, mendosteen, each on its archwood log/wood soil.
  - **Ars Elemental**: flashpine pod.
  - **Cultural Delights**: corn cob, cucumber, eggplant, avocado as a fruit-only crop.
  - Not in the pack: Croptopia, Cobblemon, Extra Delight. All load-conditioned.
- Side effects:
  - (a) It **overrides 6 BP vanilla recipes** (`minecraft/crop/sculk*`, `glow_lichen`) with simpler drops and no load conditions, undoing BP 21.1.43's sculk rebalance.
  - (b) Its item tags `soil/yellow_archwood` and `soil/apricorn` hard-reference Ars Elemental / Cobblemon items. If those mods are absent, the tags fail to load and log an error (harmless).
- Verdict: **usable as-is** for Ars Nouveau/Ars Elemental, with the vanilla-override caveat.
- Clone: `scratchpad/repos/x_modpacks/laya`.

**BotanyCompatLayer** (datapack, already chosen)
- Link: https://modrinth.com/datapack/botanycompatlayer
- 1.21 / 1.21.1. v1.0.0, 2026-09-28, 156 KB zip. **MIT**. Requires BP + Bookshelf. No source.
- Claims: The Aether, Let's Do (Alpine Whispers, BloomingNature, Brewery, Candlelight, **Farm & Charm, HerbalBrews, Meadow, Vinery**), Ribbits, **Rustic Delight**, Biomes O' Plenty, BF Blockpack, Clutter, Crop Critters, End's Delight, Hybrid Aquatic, Nature's Delight, Nature's Spirit, Oritech, Tinkers', Vegan Delight. Also natural soils.
- The author says "not every entry" is covered. **Contents not inspectable** from here.
- Verdict: **usable as-is** (post-public-release BP 21.1.x, so the format is almost certainly right). Check in game with `/botanypots debug missing seeds` that the Let's Do and Aether items disappear from the list. Watch for Rustic Delight duplicates.

**Botany Pots – More Crop Compatibility** (datapack)
- Link: https://modrinth.com/datapack/botany-pots-more-crop-compatibility
- 1.21.1. v1.1, 2026-02-15, ~800 downloads. **MIT**. No source; contents not inspectable.
- Covers Cultural Delights corn, cucumber, eggplant **+ wild variants**. Also Vegan Delight, Pineapple Delight, Cobblemon (not in pack).
- Also "fixes" corn and rice multi-block harvests, so it probably **overrides BP's own `farmersdelight/crop/rice.json`**.
- Tested on Fabric, but the JSON is loader-agnostic.
- Verdict: **usable as-is (unverified)**. Pick either this or Mega for Cultural Delights, not both.

**Botany Trees x Farmer's Delight – Expanded Compatibility** (datapack)
- Link: https://modrinth.com/datapack/botany-trees-x-farmers-delight-expanded-compatibility
- 1.21.1. 2026-02-15, ~250 downloads. MIT. No source.
- Adds a Cultural Delights avocado tree, axe-in-tool-slot giving stripped logs + FD bark, and Cobblemon/Legendary Monuments trees.
- Overrides BT vanilla tree recipes and was written before BT 21.1.4–21.1.7 (which added load conditions and changes). It may revert those.
- Verdict: **optional / use with care.** The only useful part for us is the avocado tree.

**BotanyPots × Farmer's Delight – Improved Compatibility** (datapack)
- Link: https://modrinth.com/datapack/botanypots-farmers-delight-rich-soil-compatibility
- 1.21.1. 2026-02-11. MIT.
- Adds rich soil for all dirt crops, hoe-tilling rich soil to rich farmland, and knives for straw.
- BP 21.1.42 already fixed "rich soil not growing dirt crops".
- Verdict: **mostly redundant now.** Only tilling and knife straw are extra. Not a target-mod pack.

**Wizardon's Botany Pots Tweaks** (datapack)
- Link: https://www.curseforge.com/minecraft/data-packs/wizardons-botany-pots-tweaks
- 1.21.1. v0.2, 2026-08-21, 198 downloads. MIT. No source; contents unseen.
- Claims Expanded Delight, Extra Delight, Avaritia's Delight, Ex Deorum, Oritech, Just Dire Things.
- Verdict: **usable as-is (unverified)**. It is an alternative for Expanded Delight. Its completeness (wild variants, cinnamon) is unknown.

**Botany Trees: Bountiful Fares support (unreleased upstream)**
- Link: https://github.com/Darkhax-Minecraft/BotanyTrees branch `1.21.1`, commit `eee0890` (2026-06-03)
- LGPL-2.1.
- Contents:
  - `data/botanytrees/recipe/bountifulfares/{apple,golden_apple,hoary_apple,lemon,orange,palm,plum,walnut}.json`
  - matching `data/botanytrees/loot_table/tree_drops/bountifulfares/*.json`
- Format verified.
- BT 21.1.7 (2026-06-02) does **not** include it. Irregular Implements (also 2026-06-02) may or may not be in 21.1.7.
- Verdict: **copy into our datapack** (keep paths and the LGPL notice), or drop it once BT 21.1.8+ ships.
- Clone: `scratchpad/repos/bt`.

**Fertiliser for Blockheads** (NeoForge mod)
- Links: https://modrinth.com/mod/fertiliser-for-blockheads, source https://github.com/Trioxide-Technical-Services/Fertiliser-for-Blockheads (branch `NeoForge-1.21.1`)
- 1.20.1 / 1.21.1. 2026-04-11, ~770 downloads. MIT.
- Adds the missing "rich + healthy" fertilized farmland blocks, with recipes.
- At startup it **generates a datapack** in `config/fertiliserforblockheads/botany_pots_compat`. It writes BP `block_derived_soil` recipes for all FfB fertilized farmlands, with growth/yield modifiers synced to FfB's config. These override BP's built-in `farmingforblockheads/soil/*`.
- Verdict: **optional, not a target-mod pack**. BP natively already has FfB soils.

### B. Outdated format (1.20.x): reference only

| Name | Where | Covers | License | Note |
|---|---|---|---|---|
| Hexalia x Botany Pot Compatibility | https://www.curseforge.com/minecraft/mc-mods/hexalia-x-botany-pot-compatibility | Hexalia: 12 crops (spirit bloom, dreamshroom, ghost fern, chillberries, celestial bloom, pale mushroom, saltsprout, siren kelp, witchweed, mandrake, sunfire tomato, rabbage) | MIT | 1.20.1 Forge jar, v1.0.0 2026-07-05. Useful list of soils (infused dirt; siren kelp on water). |
| My Nether's Botany | https://modrinth.com/datapack/my-nethers-botany, https://github.com/MrrrpMreow/my-nethers-botany | MND resurgent soils, fungus colonies, **powder cannon** (transitional display) + tilling | MIT | 1.20.1 Fabric; old format (`recipes/`, `seed`, `categories`, `growthTicks`). Reference for powdery cane. Clone: `scratchpad/repos/x_modpacks/mnbotany`. |
| Pots and Plants – Botany Pots Compat | https://www.curseforge.com/minecraft/data-packs/botanypots-compat | Let's Do HerbalBrews, Brewery, Vinery, Farm & Charm; Sandwichable | MIT | 1.20.1 only (2025-06-24). |
| VineryBotany | https://www.curseforge.com/minecraft/data-packs/vinerybotany | Vinery grapes (lattice / loam soils) | ARR | 1.20.1 only. |
| Undergarden Botany Pots Compats | https://www.curseforge.com/minecraft/mc-mods/undergarden-botany-pots-compats | Undergarden (not Undergarden Delight) | ARR | 1.16.5–1.20.1; Undergarden is native in BP 1.21.1 anyway. |
| Botany Pots Extras | https://modrinth.com/datapack/botany-pots-extras-le | Cinderscapes, BWG, FD soils, Supplementaries, TConstruct, Unicopia… | CC0 | 1.20.1 Fabric; none of our targets. |

### C. Not relevant (checked)

Most of these grow ores or resources, or cover Cobblemon / Pixelmon / Croptopia / Garnished / MineColonies / Pam's / Mystical:
- BotanyCompat (dratrav)
- Botany Pots Additions: pot variants, only a Mystical Agriculture recipe
- Botany Pots / Trees: Cultivating Dreams
  - Pots: ores.
  - Trees: Aether, Deep Aether, Ars, RU, Twilight, Undergarden, BOP… all **already native in BT 21.1.7**; MIT.
- Botany M trees: ARR; Aether, Deep Aether, Twilight, Undergarden trees; redundant with BT 21.1.7.
- Garnished Botany Pots, Croptopia & BP compat
- Cobblemon packs, Mystical Extended Tier
- Ore Planting and its add-ons
- KubeJS Botany Pots: the pack has no KubeJS
- Energy / Ender / Dim pots

## 3. Farming for Blockheads market

**Built-in entries in FfB 21.1.14** for our namespaces (from the FfB repo, `data/farmingforblockheads/recipe/market/<ns>/`):

| Namespace | Entries |
|---|---|
| farmersdelight (15) | crops, wild crops, colonies, rich soil, compost |
| culturaldelights | avocado sapling, cucumber seeds, eggplant seeds (**no corn kernels**) |
| expandeddelight | asparagus seeds, chili pepper seeds, cinnamon sapling (**no peanut, sweet potato, cranberries**) |
| rusticdelight | bell pepper seeds, coffee beans, cotton seeds |
| mynethersdelight | letios compost, resurgent soil (**no bullet pepper, powdery cane**) |
| ars_nouveau | 4 archwood saplings, magebloom crop (**no sourceberry**) |
| ars_elemental | yellow archwood sapling |
| twilightforest (12) | saplings, torchberries, uberous soil |
| supplementaries, create | flax seeds; tree fertilizer |

**No built-in entries** for: aether, deep_aether, aethersdelight, bountifulfares, hexerei, hexalia, farm_and_charm, vinery, meadow, herbalbrews, veggiesdelight, brewinandchewin, endersdelight, twilightdelight, regions_unexplored (none at all, not even saplings), undergarden.

**Existing market add-ons:**
- **Harvest Market Compat – Croptopia & Delight**: https://www.curseforge.com/minecraft/data-packs/harvest-market-compat-croptopia-delight
  - ARR, 2026-07-27, **MC 26.1–26.2 only**.
  - Covers Croptopia (85), FD (4), Rustic Delight (3), all of which FfB 1.21.1 already has.
  - FfB 1.21.2+ replaced `market_presets` with a `defaults.json` system.
  - Verdict: **not usable / not relevant**.
- **ATM10** (`kubejs/server_scripts/Unification/crops.js`): KubeJS market entries for Herbs and Harvest saplings only. Not relevant.
- **Craftoria** (`kubejs/server_scripts/Mods/FarmingForBlockheads/market.js`, repo TeamAOF/Craftoria, no LICENSE file):
  - A ~50-line KubeJS script that adds **every `#minecraft:saplings` and every `#c:seeds` item** without an existing entry. It uses the `minecraft:saplings` / `minecraft:seeds` presets and a small blacklist (TF magic saplings, Occultism otherworld sapling, torchflower, pitcher pod, magebloom crop, AA coffee).
  - Not usable as-is because the pack has no KubeJS.
  - **The idea carries over**: generate static JSON for the seeds and saplings of our target namespaces.
- Nothing else on Modrinth (searches `farming for blockheads`, `farmingforblockheads`, `blockheads`, `market compat`) or CurseForge (`blockheads`, `market` data-packs; FfB mc-mods addons).

**Verdict: no existing 1.21.1 FfB market pack covers our gap mods. A market datapack has to be written.**

Format for 1.21.1, from FfB's own files:
- Entry: `data/<anyns>/recipe/market/<modid>/<item>.json`

```json
{"neoforge:conditions":[{"type":"neoforge:item_exists","item":"vinery:red_grape_seeds"}],
 "type":"farmingforblockheads:market","category":"farmingforblockheads:seeds",
 "preset":"vinery:seeds","result":{"item":"vinery:red_grape_seeds"}}
```

- Preset: `data/<modid>/market_presets/seeds.json` containing `{"payment":{"ingredient":{"item":"minecraft:emerald"},"count":1}}`.
- Categories: `farmingforblockheads:seeds|saplings|flowers|other`.

## 4. Practical takeaways

1. **Already done natively (no work):** Veggies Delight and Rustic Delight (both ship BP recipes); Hexerei, Aether, Deep Aether, Vinery, Meadow, RU, Ars, Twilight and Undergarden **trees** (BT 21.1.7).
2. **Install as-is:**
   - BotanyCompatLayer: Aether plants, Farm & Charm, Vinery, Meadow, HerbalBrews.
   - LayaTweaks: Ars Nouveau / Ars Elemental crops. ARR; accept that it overrides 6 BP vanilla sculk/lichen recipes.
   - Optionally More Crop Compatibility for the Cultural Delights wild crops.
3. **Copy into our datapack:**
   - From Mega Addon (MIT): MND, Expanded Delight, Cultural Delights crops.
   - From the BT repo (LGPL-2.1): the 8 Bountiful Fares tree recipes and loot tables.
4. **Still to write**:
   - Crops: Bountiful Fares, Hexerei, Hexalia, Deep Aether plants, Aether's Delight, Brewin' And Chewin', Ender's Delight, Twilight's Flavor & Delight, CD extras, ED wild variants + cinnamon tree, MND powdery cane, Hexalia trees.
   - The whole FfB market extension.
   - For BP, start from `/botanypots debug missing seeds true true` in a test instance with the full pack. Then fix soils (Hexalia infused dirt, Hexalia siren kelp water, Ender's Delight end stone, etc.).
