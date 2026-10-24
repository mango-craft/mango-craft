# Iron Furnaces (iron-furnaces)

File generato da `scripts/esamina.py` (workflow "Esamina mod"): la mod **non** è nel pack. Non modificarlo a mano.

- Versione: **4.3.2** (release, 2025-09-26), file `ironfurnaces-neoforge-1.21.1-4.3.2.jar`, id versione `WZ25JeYB`
- Licenza su Modrinth: Apache-2.0 · download: 10248007
- Filtro dei valori: `(recipe|recipes|tags/item|tags/block)/` · filtro dei testi del codice: `(?i)^(.*(speed|cook|tier|augment|upgrade|generator|factory|fuel|multiplier|energy|rainbow).*)$`

## Mod nel file e dipendenze dichiarate

- `ironfurnaces` 4.3.2
  - required: `neoforge` [21.1,)
  - required: `minecraft` [1.21,1.22)

## Cartelle di dati (file .json)

- `c:tags/item`: 1
- `c:tags/item/furnaces`: 13
- `ironfurnaces:advancements`: 1
- `ironfurnaces:loot_table/blocks`: 14
- `ironfurnaces:recipe`: 7
- `ironfurnaces:recipe/augments`: 6
- `ironfurnaces:recipe/furnaces`: 17
- `ironfurnaces:recipe/generator_blasting`: 12
- `ironfurnaces:recipe/upgrades`: 16
- `ironfurnaces:tags/item`: 1
- `minecraft:tags/block/mineable`: 1

## Valori dei file filtrati


### `data/c/tags/item/furnaces/allthemodium.json`

- `replace` = false
- `values` = ["ironfurnaces:allthemodium_furnace"]

### `data/c/tags/item/furnaces/copper.json`

- `replace` = false
- `values` = ["ironfurnaces:copper_furnace"]

### `data/c/tags/item/furnaces/crystal.json`

- `replace` = false
- `values` = ["ironfurnaces:crystal_furnace"]

### `data/c/tags/item/furnaces/diamond.json`

- `replace` = false
- `values` = ["ironfurnaces:diamond_furnace"]

### `data/c/tags/item/furnaces/emerald.json`

- `replace` = false
- `values` = ["ironfurnaces:emerald_furnace"]

### `data/c/tags/item/furnaces/gold.json`

- `replace` = false
- `values` = ["ironfurnaces:gold_furnace"]

### `data/c/tags/item/furnaces/iron.json`

- `replace` = false
- `values` = ["ironfurnaces:iron_furnace"]

### `data/c/tags/item/furnaces/netherite.json`

- `replace` = false
- `values` = ["ironfurnaces:netherite_furnace"]

### `data/c/tags/item/furnaces/obsidian.json`

- `replace` = false
- `values` = ["ironfurnaces:obsidian_furnace"]

### `data/c/tags/item/furnaces/rainbow.json`

- `replace` = false
- `values` = ["ironfurnaces:million_furnace"]

### `data/c/tags/item/furnaces/silver.json`

- `replace` = false
- `values` = ["ironfurnaces:silver_furnace"]

### `data/c/tags/item/furnaces/unobtainium.json`

- `replace` = false
- `values` = ["ironfurnaces:unobtainium_furnace"]

### `data/c/tags/item/furnaces/vibranium.json`

- `replace` = false
- `values` = ["ironfurnaces:vibranium_furnace"]

### `data/c/tags/item/furnaces.json`

- `replace` = false
- `values` = ["minecraft:furnace", "ironfurnaces:allthemodium_furnace", "ironfurnaces:copper_furnace", "ironfurnaces:crystal_furnace", "ironfurnaces:diamond_furnace", "ironfurnaces:emerald_furnace", "ironfurnaces:gold_furnace", "ironfurnaces:iron_furnace", "ironfurnaces:netherite_furnace", "ironfurnaces:obsidian…

### `data/ironfurnaces/recipe/augments/augment_blasting.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["#R#", "PXP", "#R#"]
- `key.#.tag` = "c:stones"
- `key.P.item` = "minecraft:paper"
- `key.R.tag` = "c:dusts/redstone"
- `key.X.item` = "minecraft:blast_furnace"
- `result.id` = "ironfurnaces:augment_blasting"

### `data/ironfurnaces/recipe/augments/augment_factory.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["#R#", "PXP", "#R#"]
- `key.#.tag` = "c:stones"
- `key.P.item` = "minecraft:paper"
- `key.R.tag` = "c:dusts/redstone"
- `key.X.item` = "minecraft:piston"
- `result.id` = "ironfurnaces:augment_factory"

### `data/ironfurnaces/recipe/augments/augment_fuel.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["#R#", "PXP", "#R#"]
- `key.#.tag` = "c:stones"
- `key.P.item` = "minecraft:paper"
- `key.R.tag` = "c:dusts/redstone"
- `key.X.item` = "minecraft:coal"
- `result.id` = "ironfurnaces:augment_fuel"

### `data/ironfurnaces/recipe/augments/augment_generator.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["#R#", "PXP", "#R#"]
- `key.#.tag` = "c:stones"
- `key.P.item` = "minecraft:paper"
- `key.R.tag` = "c:dusts/redstone"
- `key.X.item` = "minecraft:repeater"
- `result.id` = "ironfurnaces:augment_generator"

### `data/ironfurnaces/recipe/augments/augment_smoking.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["#R#", "PXP", "#R#"]
- `key.#.tag` = "c:stones"
- `key.P.item` = "minecraft:paper"
- `key.R.tag` = "c:dusts/redstone"
- `key.X.item` = "minecraft:smoker"
- `result.id` = "ironfurnaces:augment_smoking"

### `data/ironfurnaces/recipe/augments/augment_speed.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["#R#", "PXP", "#R#"]
- `key.#.tag` = "c:stones"
- `key.P.item` = "minecraft:paper"
- `key.R.tag` = "c:dusts/redstone"
- `key.X.item` = "minecraft:sugar"
- `result.id` = "ironfurnaces:augment_speed"

### `data/ironfurnaces/recipe/furnaces/allthemodium_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["B#B", "#X#", "B#B"]
- `key.#.tag` = "c:ingots/allthemodium"
- `key.X.tag` = "c:furnaces/netherite"
- `key.B.tag` = "c:storage_blocks/allthemodium"
- `result.id` = "ironfurnaces:allthemodium_furnace"
- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "allthemodium"

### `data/ironfurnaces/recipe/furnaces/copper_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["###", "#X#", "###"]
- `key.#.tag` = "c:ingots/copper"
- `key.X.item` = "minecraft:furnace"
- `result.id` = "ironfurnaces:copper_furnace"
- `neoforge:conditions[0].value.type` = "neoforge:tag_empty"
- `neoforge:conditions[0].value.tag` = "c:ingots/copper"
- `neoforge:conditions[0].type` = "neoforge:not"

### `data/ironfurnaces/recipe/furnaces/crystal_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["###", "#X#", "#E#"]
- `key.#.tag` = "c:glass_blocks/colorless"
- `key.X.tag` = "c:furnaces/diamond"
- `key.E.item` = "minecraft:ender_eye"
- `result.id` = "ironfurnaces:crystal_furnace"

### `data/ironfurnaces/recipe/furnaces/diamond_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["###", "GXG", "###"]
- `key.#.tag` = "c:gems/diamond"
- `key.X.tag` = "c:furnaces/gold"
- `key.G.tag` = "c:glass_blocks/colorless"
- `result.id` = "ironfurnaces:diamond_furnace"

### `data/ironfurnaces/recipe/furnaces/emerald_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["###", "#X#", "###"]
- `key.#.tag` = "c:gems/emerald"
- `key.X.tag` = "c:furnaces/diamond"
- `result.id` = "ironfurnaces:emerald_furnace"

### `data/ironfurnaces/recipe/furnaces/gold_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["###", "#X#", "#Y#"]
- `key.#.tag` = "c:ingots/gold"
- `key.X.tag` = "c:furnaces/iron"
- `key.Y.tag` = "c:storage_blocks/gold"
- `result.id` = "ironfurnaces:gold_furnace"

### `data/ironfurnaces/recipe/furnaces/gold_furnace2.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["###", "#X#", "#Y#"]
- `key.Y.tag` = "c:storage_blocks/gold"
- `key.X.tag` = "c:furnaces/silver"
- `key.#.tag` = "c:glass_blocks/colorless"
- `result.id` = "ironfurnaces:gold_furnace"

### `data/ironfurnaces/recipe/furnaces/iron_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["###", "#X#", "###"]
- `key.#.tag` = "c:ingots/iron"
- `key.X.item` = "minecraft:furnace"
- `result.id` = "ironfurnaces:iron_furnace"

### `data/ironfurnaces/recipe/furnaces/iron_furnace2.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["YYY", "#X#", "YYY"]
- `key.#.tag` = "c:glass_blocks/colorless"
- `key.X.tag` = "c:furnaces/copper"
- `key.Y.tag` = "c:ingots/iron"
- `result.id` = "ironfurnaces:iron_furnace"

### `data/ironfurnaces/recipe/furnaces/million_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["###", "#C#", "###"]
- `key.C.item` = "ironfurnaces:rainbow_core"
- `key.#.item` = "ironfurnaces:rainbow_plating"
- `result.id` = "ironfurnaces:million_furnace"

### `data/ironfurnaces/recipe/furnaces/netherite_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["N#N", "#X#", "NSN"]
- `key.#.item` = "minecraft:magma_cream"
- `key.X.tag` = "c:furnaces/obsidian"
- `key.S.tag` = "minecraft:soul_fire_base_blocks"
- `key.N.item` = "minecraft:netherite_ingot"
- `result.id` = "ironfurnaces:netherite_furnace"

### `data/ironfurnaces/recipe/furnaces/obsidian_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["#Y#", "YXY", "#Y#"]
- `key.#.tag` = "c:obsidians"
- `key.X.tag` = "c:furnaces/emerald"
- `key.Y.tag` = "c:rods/blaze"
- `result.id` = "ironfurnaces:obsidian_furnace"

### `data/ironfurnaces/recipe/furnaces/obsidian_furnace2.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["#Y#", "YXY", "#Y#"]
- `key.#.tag` = "c:obsidians"
- `key.X.tag` = "c:furnaces/crystal"
- `key.Y.tag` = "c:rods/blaze"
- `result.id` = "ironfurnaces:obsidian_furnace"

### `data/ironfurnaces/recipe/furnaces/silver_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["#G#", "GXG", "#G#"]
- `key.#.tag` = "c:ingots/silver"
- `key.X.tag` = "c:furnaces/iron"
- `key.G.tag` = "c:glass_blocks/colorless"
- `result.id` = "ironfurnaces:silver_furnace"
- `neoforge:conditions[0].value.type` = "neoforge:tag_empty"
- `neoforge:conditions[0].value.tag` = "c:ingots/silver"
- `neoforge:conditions[0].type` = "neoforge:not"

### `data/ironfurnaces/recipe/furnaces/silver_furnace2.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["###", "#X#", "###"]
- `key.#.tag` = "c:ingots/silver"
- `key.X.tag` = "c:furnaces/copper"
- `result.id` = "ironfurnaces:silver_furnace"
- `neoforge:conditions[0].value.type` = "neoforge:tag_empty"
- `neoforge:conditions[0].value.tag` = "c:ingots/silver"
- `neoforge:conditions[0].type` = "neoforge:not"

### `data/ironfurnaces/recipe/furnaces/unobtainium_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["B#B", "#X#", "B#B"]
- `key.#.tag` = "c:ingots/unobtainium"
- `key.X.tag` = "c:furnaces/vibranium"
- `key.B.tag` = "c:storage_blocks/unobtainium"
- `result.id` = "ironfurnaces:unobtainium_furnace"
- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "allthemodium"

### `data/ironfurnaces/recipe/furnaces/vibranium_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["B#B", "#X#", "B#B"]
- `key.#.tag` = "c:ingots/vibranium"
- `key.X.tag` = "c:furnaces/allthemodium"
- `key.B.tag` = "c:storage_blocks/vibranium"
- `result.id` = "ironfurnaces:vibranium_furnace"
- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "allthemodium"

### `data/ironfurnaces/recipe/generator_blasting/amethyst.json`

- `type` = "ironfurnaces:generator_blasting"
- `energy` = 40000
- `ingredient.item` = "minecraft:amethyst_shard"

### `data/ironfurnaces/recipe/generator_blasting/copper_ingot.json`

- `type` = "ironfurnaces:generator_blasting"
- `energy` = 10000
- `ingredient.item` = "minecraft:copper_ingot"

### `data/ironfurnaces/recipe/generator_blasting/diamond.json`

- `type` = "ironfurnaces:generator_blasting"
- `energy` = 500000
- `ingredient.item` = "minecraft:diamond"

### `data/ironfurnaces/recipe/generator_blasting/emerald.json`

- `type` = "ironfurnaces:generator_blasting"
- `energy` = 125000
- `ingredient.item` = "minecraft:emerald"

### `data/ironfurnaces/recipe/generator_blasting/gold_ingot.json`

- `type` = "ironfurnaces:generator_blasting"
- `energy` = 40000
- `ingredient.item` = "minecraft:gold_ingot"

### `data/ironfurnaces/recipe/generator_blasting/iron_ingot.json`

- `type` = "ironfurnaces:generator_blasting"
- `energy` = 20000
- `ingredient.item` = "minecraft:iron_ingot"

### `data/ironfurnaces/recipe/generator_blasting/lapis_lazuli.json`

- `type` = "ironfurnaces:generator_blasting"
- `energy` = 40000
- `ingredient.item` = "minecraft:lapis_lazuli"

### `data/ironfurnaces/recipe/generator_blasting/netherite_ingot.json`

- `type` = "ironfurnaces:generator_blasting"
- `energy` = 750000
- `ingredient.item` = "minecraft:netherite_ingot"

### `data/ironfurnaces/recipe/generator_blasting/nether_star.json`

- `type` = "ironfurnaces:generator_blasting"
- `energy` = 1000000
- `ingredient.item` = "minecraft:nether_star"

### `data/ironfurnaces/recipe/generator_blasting/prismarine.json`

- `type` = "ironfurnaces:generator_blasting"
- `energy` = 40000
- `ingredient.item` = "minecraft:prismarine_shard"

### `data/ironfurnaces/recipe/generator_blasting/quartz.json`

- `type` = "ironfurnaces:generator_blasting"
- `energy` = 40000
- `ingredient.item` = "minecraft:quartz"

### `data/ironfurnaces/recipe/generator_blasting/redstone.json`

- `type` = "ironfurnaces:generator_blasting"
- `energy` = 10000
- `ingredient.item` = "minecraft:redstone"

### `data/ironfurnaces/recipe/heater.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["#F#", "#X#", "#C#"]
- `key.#.tag` = "c:stones"
- `key.C.item` = "minecraft:furnace"
- `key.F.item` = "minecraft:comparator"
- `key.X.tag` = "c:storage_blocks/redstone"
- `result.id` = "ironfurnaces:heater"

### `data/ironfurnaces/recipe/item_copy.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = [" # ", "#X#", " # "]
- `key.#.item` = "minecraft:paper"
- `key.X.item` = "minecraft:furnace"
- `result.id` = "ironfurnaces:item_copy"

### `data/ironfurnaces/recipe/item_heater.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["#R#", "RXR", "#R#"]
- `key.#.tag` = "c:stones"
- `key.R.tag` = "c:dusts/redstone"
- `key.X.item` = "minecraft:comparator"
- `result.id` = "ironfurnaces:item_heater"

### `data/ironfurnaces/recipe/item_spooky.json`

- `type` = "minecraft:crafting_shapeless"
- `ingredients[0].item` = "minecraft:carved_pumpkin"
- `ingredients[1].item` = "minecraft:furnace"
- `result.id` = "ironfurnaces:item_spooky"

### `data/ironfurnaces/recipe/item_xmas.json`

- `type` = "minecraft:crafting_shapeless"
- `ingredients[0].item` = "minecraft:yellow_dye"
- `ingredients[1].item` = "minecraft:red_dye"
- `ingredients[2].item` = "minecraft:paper"
- `ingredients[3].item` = "minecraft:furnace"
- `result.id` = "ironfurnaces:item_xmas"

### `data/ironfurnaces/recipe/rainbow_core.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["ROY", "FGF", "BPM"]
- `key.R.item` = "minecraft:red_stained_glass"
- `key.O.item` = "minecraft:orange_stained_glass"
- `key.Y.item` = "minecraft:yellow_stained_glass"
- `key.F.item` = "ironfurnaces:netherite_furnace"
- `key.G.item` = "minecraft:green_stained_glass"
- `key.B.item` = "minecraft:blue_stained_glass"
- `key.P.item` = "minecraft:purple_stained_glass"
- `key.M.item` = "minecraft:magenta_stained_glass"
- `result.id` = "ironfurnaces:rainbow_core"

### `data/ironfurnaces/recipe/rainbow_plating.json`

- `type` = "minecraft:crafting_shapeless"
- `ingredients[0].item` = "ironfurnaces:iron_furnace"
- `ingredients[1].item` = "ironfurnaces:gold_furnace"
- `ingredients[2].item` = "ironfurnaces:diamond_furnace"
- `ingredients[3].item` = "ironfurnaces:emerald_furnace"
- `ingredients[4].item` = "ironfurnaces:obsidian_furnace"
- `ingredients[5].item` = "ironfurnaces:crystal_furnace"
- `ingredients[6].item` = "ironfurnaces:copper_furnace"
- `ingredients[7].item` = "ironfurnaces:silver_furnace"
- `result.id` = "ironfurnaces:rainbow_plating"
- `result.count` = 8
- `conditions[0].type` = "neoforge:not"
- `conditions[0].value.type` = "neoforge:tag_empty"
- `conditions[0].value.tag` = "c:ingots/silver"

### `data/ironfurnaces/recipe/upgrades/upgrade_allthemodium.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["B#B", "#X#", "B#B"]
- `key.#.tag` = "c:ingots/allthemodium"
- `key.B.tag` = "c:storage_blocks/allthemodium"
- `key.X.tag` = "ironfurnaces:netherite_upgrade_crafting"
- `result.id` = "ironfurnaces:upgrade_allthemodium"
- `conditions[0].type` = "neoforge:mod_loaded"
- `conditions[0].modid` = "allthemodium"

### `data/ironfurnaces/recipe/upgrades/upgrade_copper.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["###", "#X#", "###"]
- `key.#.tag` = "c:ingots/copper"
- `key.X.tag` = "minecraft:stone_tool_materials"
- `result.id` = "ironfurnaces:upgrade_copper"
- `conditions[0].value.type` = "neoforge:tag_empty"
- `conditions[0].value.tag` = "c:ingots/copper"
- `conditions[0].type` = "neoforge:not"

### `data/ironfurnaces/recipe/upgrades/upgrade_crystal.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["###", "#X#", "#E#"]
- `key.#.tag` = "c:glass_blocks/colorless"
- `key.X.tag` = "c:gems/diamond"
- `key.E.item` = "minecraft:ender_eye"
- `result.id` = "ironfurnaces:upgrade_crystal"

### `data/ironfurnaces/recipe/upgrades/upgrade_diamond.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["###", "GXG", "###"]
- `key.#.tag` = "c:gems/diamond"
- `key.X.tag` = "c:ingots/gold"
- `key.G.tag` = "c:glass_blocks/colorless"
- `result.id` = "ironfurnaces:upgrade_diamond"

### `data/ironfurnaces/recipe/upgrades/upgrade_emerald.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["###", "#X#", "###"]
- `key.#.tag` = "c:gems/emerald"
- `key.X.tag` = "c:gems/diamond"
- `result.id` = "ironfurnaces:upgrade_emerald"

### `data/ironfurnaces/recipe/upgrades/upgrade_gold.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["###", "#X#", "#Y#"]
- `key.#.tag` = "c:ingots/gold"
- `key.X.tag` = "c:ingots/iron"
- `key.Y.tag` = "c:storage_blocks/gold"
- `result.id` = "ironfurnaces:upgrade_gold"

### `data/ironfurnaces/recipe/upgrades/upgrade_gold2.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["###", "#X#", "#Y#"]
- `key.#.tag` = "c:ingots/gold"
- `key.X.tag` = "c:ingots/silver"
- `key.Y.tag` = "c:storage_blocks/gold"
- `result.id` = "ironfurnaces:upgrade_gold2"
- `conditions[0].value.type` = "neoforge:tag_empty"
- `conditions[0].value.tag` = "c:ingots/silver"
- `conditions[0].type` = "neoforge:not"

### `data/ironfurnaces/recipe/upgrades/upgrade_iron.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["###", "#X#", "###"]
- `key.#.tag` = "c:ingots/iron"
- `key.X.tag` = "minecraft:stone_tool_materials"
- `result.id` = "ironfurnaces:upgrade_iron"

### `data/ironfurnaces/recipe/upgrades/upgrade_iron2.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["###", "GXG", "###"]
- `key.#.tag` = "c:ingots/iron"
- `key.X.tag` = "c:ingots/copper"
- `key.G.tag` = "c:glass_blocks/colorless"
- `result.id` = "ironfurnaces:upgrade_iron2"
- `conditions[0].value.type` = "neoforge:tag_empty"
- `conditions[0].value.tag` = "c:ingots/copper"
- `conditions[0].type` = "neoforge:not"

### `data/ironfurnaces/recipe/upgrades/upgrade_netherite.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["N#N", "#X#", "NSN"]
- `key.#.item` = "minecraft:magma_cream"
- `key.X.tag` = "c:obsidians"
- `key.S.tag` = "minecraft:soul_fire_base_blocks"
- `key.N.item` = "minecraft:netherite_ingot"
- `result.id` = "ironfurnaces:upgrade_netherite"

### `data/ironfurnaces/recipe/upgrades/upgrade_obsidian.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["#Y#", "YXY", "#Y#"]
- `key.#.tag` = "c:obsidians"
- `key.X.tag` = "c:gems/emerald"
- `key.Y.tag` = "c:rods/blaze"
- `result.id` = "ironfurnaces:upgrade_obsidian"

### `data/ironfurnaces/recipe/upgrades/upgrade_obsidian2.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["#Y#", "YXY", "#Y#"]
- `key.#.tag` = "c:obsidians"
- `key.X.tag` = "c:glass_blocks/colorless"
- `key.Y.tag` = "c:rods/blaze"
- `result.id` = "ironfurnaces:upgrade_obsidian2"

### `data/ironfurnaces/recipe/upgrades/upgrade_silver.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["###", "#S#", "#X#"]
- `key.#.tag` = "c:ingots/silver"
- `key.X.tag` = "c:ingots/copper"
- `key.S.tag` = "minecraft:stone_tool_materials"
- `result.id` = "ironfurnaces:upgrade_silver"
- `conditions[0].value.type` = "neoforge:tag_empty"
- `conditions[0].value.tag` = "c:ingots/silver"
- `conditions[0].type` = "neoforge:not"
- `conditions[1].value.type` = "neoforge:tag_empty"
- `conditions[1].value.tag` = "c:ingots/copper"
- `conditions[1].type` = "neoforge:not"

### `data/ironfurnaces/recipe/upgrades/upgrade_silver2.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["#G#", "GXG", "#G#"]
- `key.#.tag` = "c:ingots/silver"
- `key.X.tag` = "c:ingots/iron"
- `key.G.tag` = "c:glass_blocks/colorless"
- `result.id` = "ironfurnaces:upgrade_silver2"
- `conditions[0].value.type` = "neoforge:tag_empty"
- `conditions[0].value.tag` = "c:ingots/silver"
- `conditions[0].type` = "neoforge:not"

### `data/ironfurnaces/recipe/upgrades/upgrade_unobtainium.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["B#B", "#X#", "B#B"]
- `key.#.tag` = "c:ingots/unobtainium"
- `key.B.tag` = "c:storage_blocks/unobtainium"
- `key.X.tag` = "c:ingots/vibranium"
- `result.id` = "ironfurnaces:upgrade_unobtainium"
- `conditions[0].type` = "neoforge:mod_loaded"
- `conditions[0].modid` = "allthemodium"

### `data/ironfurnaces/recipe/upgrades/upgrade_vibranium.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["B#B", "#X#", "B#B"]
- `key.#.tag` = "c:ingots/vibranium"
- `key.B.tag` = "c:storage_blocks/vibranium"
- `key.X.tag` = "c:ingots/allthemodium"
- `result.id` = "ironfurnaces:upgrade_vibranium"
- `conditions[0].type` = "neoforge:mod_loaded"
- `conditions[0].modid` = "allthemodium"

### `data/ironfurnaces/tags/item/netherite_upgrade_crafting.json`

- `replace` = false
- `values` = ["minecraft:netherite_scrap", "minecraft:netherite_ingot"]

### `data/minecraft/tags/block/mineable/pickaxe.json`

- `replace` = false
- `values` = ["ironfurnaces:copper_furnace", "ironfurnaces:iron_furnace", "ironfurnaces:silver_furnace", "ironfurnaces:gold_furnace", "ironfurnaces:diamond_furnace", "ironfurnaces:emerald_furnace", "ironfurnaces:crystal_furnace", "ironfurnaces:obsidian_furnace", "ironfurnaces:netherite_furnace", "ironfurnaces:al…

## Testi nel codice


### `ironfurnaces/blocks/BlockWirelessEnergyHeater.class`

- "ironfurnaces/blocks/BlockWirelessEnergyHeater"
- "ironfurnaces/tileentity/BlockWirelessEnergyHeaterTile"
- "getEnergy"
- "ENERGY"
- "setEnergy"
- "Lironfurnaces/blocks/BlockWirelessEnergyHeater;"
- "Lnet/minecraft/world/level/block/entity/BlockEntityType<+Lironfurnaces/tileentity/BlockWirelessEnergyHeaterTile;>;"
- "<T:Lnet/minecraft/world/level/block/entity/BlockEntity;>(Lnet/minecraft/world/level/Level;Lnet/minecraft/world/level/block/entity/BlockEntityType<TT;>;Lnet/minecraft/world/level/block/entity/BlockEntityType<+Lironfurnaces/tileentity/BlockWirelessEnergyHeaterTile;>;)Lnet/minecraft/world/level/block/e…"
- "Lironfurnaces/tileentity/BlockWirelessEnergyHeaterTile;"
- "energy"
- "BlockWirelessEnergyHeater.java"
- "(Lnet/minecraft/world/level/Level;Lnet/minecraft/core/BlockPos;Lnet/minecraft/world/level/block/state/BlockState;Lironfurnaces/tileentity/BlockWirelessEnergyHeaterTile;)V"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `ironfurnaces/blocks/furnaces/BlockCrystalFurnace.class`

- "SMOKING_AUGMENT"

### `ironfurnaces/blocks/furnaces/BlockIronFurnaceBase.class`

- "getCookTimeConfig"
- "totalCookTime"
- "ironfurnaces/items/augments/ItemAugment"
- "interactAugment"
- "ironfurnaces/items/augments/ItemAugmentRed"
- "ironfurnaces/items/augments/ItemAugmentGreen"
- "SMOKING_AUGMENT"
- "BLASTING_AUGMENT"
- "isGenerator"
- "isFactory"
- "getTier"
- "tier"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `ironfurnaces/blocks/furnaces/BlockItemHeater.class`

- "ENERGY"
- "displayEnergy"
- "energy"

### `ironfurnaces/blocks/furnaces/BlockMillionFurnace.class`

- "GENERATOR_AUGMENT"
- "RAINBOW_GENERATING"
- "rainbow"

### `ironfurnaces/blocks/furnaces/BlockNetheriteFurnace.class`

- "SMOKING_AUGMENT"
- "BLASTING_AUGMENT"

### `ironfurnaces/capability/CapabilityIronFurnaces.class`

- "net/neoforged/neoforge/capabilities/Capabilities$EnergyStorage"
- "energyStorage"
- "Lironfurnaces/energy/FEnergyStorage;"
- "(Lnet/minecraft/world/level/Level;Lnet/minecraft/core/BlockPos;Lnet/minecraft/world/level/block/state/BlockState;Lnet/minecraft/world/level/block/entity/BlockEntity;Lnet/minecraft/core/Direction;)Lnet/neoforged/neoforge/energy/IEnergyStorage;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "EnergyStorage"

### `ironfurnaces/capability/PlayerFurnacesListProvider.class`

- "java/lang/invoke/StringConcatFactory"

### `ironfurnaces/Config.class`

- "rainbow_furnace.generation"
- "energy.tier_0"
- "furnaceEnergyCapacityTier0"
- "energy.tier_1"
- "furnaceEnergyCapacityTier1"
- "energy.tier_2"
- "furnaceEnergyCapacityTier2"
- "iron_furnace.tier"
- "ironFurnaceTier"
- "copper_furnace.tier"
- "copperFurnaceTier"
- "gold_furnace.tier"
- "goldFurnaceTier"
- "diamond_furnace.tier"
- "diamondFurnaceTier"
- "emerald_furnace.tier"
- "emeraldFurnaceTier"
- "silver_furnace.tier"
- "silverFurnaceTier"
- "crystal_furnace.tier"
- "crystalFurnaceTier"
- "obsidian_furnace.tier"
- "obsidianFurnaceTier"
- "netherite_furnace.tier"
- "netheriteFurnaceTier"
- "million_furnace.tier"
- "millionFurnaceTier"
- "iron_furnace.speed"
- "ironFurnaceSpeed"
- "gold_furnace.speed"
- "goldFurnaceSpeed"
- "diamond_furnace.speed"
- "diamondFurnaceSpeed"
- "emerald_furnace.speed"
- "emeraldFurnaceSpeed"
- "obsidian_furnace.speed"
- "obsidianFurnaceSpeed"
- "crystal_furnace.speed"
- "crystalFurnaceSpeed"
- "netherite_furnace.speed"
- "netheriteFurnaceSpeed"
- "copper_furnace.speed"
- "copperFurnaceSpeed"
- "silver_furnace.speed"
- "silverFurnaceSpeed"
- "rainbow_furnace.speed"
- "millionFurnaceSpeed"
- "rainbow_furnace.rainbow_generation"
- "allthemodium_furnace.speed"
- "allthemodiumFurnaceSpeed"
- "vibranium_furnace.speed"
- "vibraniumFurnaceSpeed"
- "unobtainium_furnace.speed"
- "unobtainiumFurnaceSpeed"
- "allthemodium_furnace.tier"
- "allthemodiumFurnaceTier"
- "vibranium_furnace.tier"
- "vibraniumFurnaceTier"
- "unobtainium_furnace.tier"
- "unobtainiumFurnaceTier"

### `ironfurnaces/container/BlockWirelessEnergyHeaterContainer.class`

- "ironfurnaces/container/BlockWirelessEnergyHeaterContainerBase"
- "ironfurnaces/tileentity/BlockWirelessEnergyHeaterTile"
- "ironfurnaces/container/BlockWirelessEnergyHeaterContainer"
- "Lironfurnaces/tileentity/BlockWirelessEnergyHeaterTile;"
- "Lironfurnaces/container/BlockWirelessEnergyHeaterContainer;"
- "BlockWirelessEnergyHeaterContainer.java"

### `ironfurnaces/container/BlockWirelessEnergyHeaterContainerBase$1.class`

- "ironfurnaces/container/BlockWirelessEnergyHeaterContainerBase$1"
- "Lironfurnaces/container/BlockWirelessEnergyHeaterContainerBase;"
- "ironfurnaces/container/BlockWirelessEnergyHeaterContainerBase"
- "getMaxEnergy"
- "Lironfurnaces/tileentity/BlockWirelessEnergyHeaterTile;"
- "ironfurnaces/tileentity/BlockWirelessEnergyHeaterTile"
- "setMaxEnergy"
- "(Lironfurnaces/container/BlockWirelessEnergyHeaterContainerBase;)V"
- "Lironfurnaces/container/BlockWirelessEnergyHeaterContainerBase$1;"
- "BlockWirelessEnergyHeaterContainerBase.java"

### `ironfurnaces/container/BlockWirelessEnergyHeaterContainerBase$2.class`

- "ironfurnaces/container/BlockWirelessEnergyHeaterContainerBase$2"
- "Lironfurnaces/container/BlockWirelessEnergyHeaterContainerBase;"
- "ironfurnaces/container/BlockWirelessEnergyHeaterContainerBase"
- "getEnergy"
- "Lironfurnaces/tileentity/BlockWirelessEnergyHeaterTile;"
- "ironfurnaces/tileentity/BlockWirelessEnergyHeaterTile"
- "setEnergy"
- "(Lironfurnaces/container/BlockWirelessEnergyHeaterContainerBase;)V"
- "Lironfurnaces/container/BlockWirelessEnergyHeaterContainerBase$2;"
- "BlockWirelessEnergyHeaterContainerBase.java"

### `ironfurnaces/container/BlockWirelessEnergyHeaterContainerBase.class`

- "ironfurnaces/tileentity/BlockWirelessEnergyHeaterTile"
- "ironfurnaces/container/BlockWirelessEnergyHeaterContainerBase"
- "Lironfurnaces/tileentity/BlockWirelessEnergyHeaterTile;"
- "(Lironfurnaces/tileentity/BlockWirelessEnergyHeaterTile;III)V"
- "getEnergy"
- "ironfurnaces/container/BlockWirelessEnergyHeaterContainerBase$1"
- "(Lironfurnaces/container/BlockWirelessEnergyHeaterContainerBase;)V"
- "ironfurnaces/container/BlockWirelessEnergyHeaterContainerBase$2"
- "getMaxEnergy"
- "Lironfurnaces/container/BlockWirelessEnergyHeaterContainerBase;"
- "getEnergyScaled"
- "BlockWirelessEnergyHeaterContainerBase.java"

### `ironfurnaces/container/furnaces/BlockIronFurnaceContainerBase$1.class`

- "getAugmentGUI"

### `ironfurnaces/container/furnaces/BlockIronFurnaceContainerBase$10.class`

- "generatorRecentRecipeRF"
- "addGeneratorData"

### `ironfurnaces/container/furnaces/BlockIronFurnaceContainerBase$11.class`

- "ironfurnaces/util/container/FactoryDataSlot"
- "factoryCookTime"
- "addFactoryData"

### `ironfurnaces/container/furnaces/BlockIronFurnaceContainerBase$12.class`

- "ironfurnaces/util/container/FactoryDataSlot"
- "factoryTotalCookTime"
- "addFactoryData"

### `ironfurnaces/container/furnaces/BlockIronFurnaceContainerBase$13.class`

- "getMaxEnergy"
- "setMaxEnergy"
- "addEnergyData"

### `ironfurnaces/container/furnaces/BlockIronFurnaceContainerBase$14.class`

- "getEnergy"
- "setEnergy"
- "addEnergyData"

### `ironfurnaces/container/furnaces/BlockIronFurnaceContainerBase$2.class`

- "currentAugment"

### `ironfurnaces/container/furnaces/BlockIronFurnaceContainerBase$3.class`

- "getIsGenerator"
- "currentAugment"

### `ironfurnaces/container/furnaces/BlockIronFurnaceContainerBase$4.class`

- "getIsFactory"
- "currentAugment"

### `ironfurnaces/container/furnaces/BlockIronFurnaceContainerBase$7.class`

- "cookTime"

### `ironfurnaces/container/furnaces/BlockIronFurnaceContainerBase$8.class`

- "totalCookTime"

### `ironfurnaces/container/furnaces/BlockIronFurnaceContainerBase$9.class`

- "generatorBurn"
- "addGeneratorData"

### `ironfurnaces/container/furnaces/BlockIronFurnaceContainerBase.class`

- "ironfurnaces/container/slots/SlotIronFurnaceFuel"
- "ironfurnaces/container/slots/SlotIronFurnaceAugmentRed"
- "ironfurnaces/container/slots/SlotIronFurnaceAugmentGreen"
- "ironfurnaces/container/slots/SlotIronFurnaceAugmentBlue"
- "ironfurnaces/container/slots/SlotIronFurnaceInputGenerator"
- "ironfurnaces/container/slots/SlotIronFurnaceInputFactory"
- "ironfurnaces/container/slots/SlotIronFurnaceOutputFactory"
- "addEnergyData"
- "addGeneratorData"
- "addFactoryData"
- "factoryCookTime"
- "factoryTotalCookTime"
- "getEnergy"
- "energyStorage"
- "Lironfurnaces/energy/FEnergyStorage;"
- "ironfurnaces/energy/FEnergyStorage"
- "getMaxEnergyStored"
- "getTier"
- "getAugmentGUI"
- "isFactory"
- "isGenerator"
- "tooltip.ironfurnaces.gui_fuel"
- "isRainbowFurnace"
- "cookTime"
- "totalCookTime"
- "generatorRecentRecipeRF"
- "generatorBurn"
- "ironfurnaces/items/augments/ItemAugmentSmoking"
- "ironfurnaces/items/augments/ItemAugmentBlasting"
- "hasGeneratorBlastingRecipe"
- "isItemFuel"
- "isItemAugment"
- "getMaxEnergy"
- "getIsFactory"
- "getIsGenerator"
- "getCookScaled"
- "getFactoryCookScaled"
- "getFactoryCooktimeSize"
- "getGeneratorBurnScaled"
- "isGeneratorBurning"
- "getEnergyScaled"

### `ironfurnaces/container/slots/SlotHeater.class`

- "Lironfurnaces/tileentity/BlockWirelessEnergyHeaterTile;"
- "(Lironfurnaces/tileentity/BlockWirelessEnergyHeaterTile;III)V"

### `ironfurnaces/container/slots/SlotIronFurnace.class`

- "getAugmentGUI"

### `ironfurnaces/container/slots/SlotIronFurnaceAugmentBlue.class`

- "ironfurnaces/container/slots/SlotIronFurnaceAugmentBlue"
- "ironfurnaces/items/augments/ItemAugmentBlue"
- "getAugmentGUI"
- "Lironfurnaces/container/slots/SlotIronFurnaceAugmentBlue;"
- "SlotIronFurnaceAugmentBlue.java"

### `ironfurnaces/container/slots/SlotIronFurnaceAugmentGreen.class`

- "ironfurnaces/container/slots/SlotIronFurnaceAugmentGreen"
- "ironfurnaces/items/augments/ItemAugmentGreen"
- "getAugmentGUI"
- "Lironfurnaces/container/slots/SlotIronFurnaceAugmentGreen;"
- "SlotIronFurnaceAugmentGreen.java"

### `ironfurnaces/container/slots/SlotIronFurnaceAugmentRed.class`

- "ironfurnaces/container/slots/SlotIronFurnaceAugmentRed"
- "ironfurnaces/items/augments/ItemAugmentRed"
- "getAugmentGUI"
- "Lironfurnaces/container/slots/SlotIronFurnaceAugmentRed;"
- "SlotIronFurnaceAugmentRed.java"

### `ironfurnaces/container/slots/SlotIronFurnaceFuel.class`

- "ironfurnaces/container/slots/SlotIronFurnaceFuel"
- "isItemFuel"
- "getAugmentGUI"
- "Lironfurnaces/container/slots/SlotIronFurnaceFuel;"
- "SlotIronFurnaceFuel.java"

### `ironfurnaces/container/slots/SlotIronFurnaceInput.class`

- "getAugmentGUI"

### `ironfurnaces/container/slots/SlotIronFurnaceInputFactory.class`

- "ironfurnaces/container/slots/SlotIronFurnaceInputFactory"
- "getTier"
- "isFactory"
- "getAugmentGUI"
- "Lironfurnaces/container/slots/SlotIronFurnaceInputFactory;"
- "SlotIronFurnaceInputFactory.java"

### `ironfurnaces/container/slots/SlotIronFurnaceInputGenerator.class`

- "ironfurnaces/container/slots/SlotIronFurnaceInputGenerator"
- "ironfurnaces/items/augments/ItemAugmentBlasting"
- "hasGeneratorBlastingRecipe"
- "ironfurnaces/items/augments/ItemAugmentSmoking"
- "isItemFuel"
- "isGenerator"
- "getAugmentGUI"
- "Lironfurnaces/container/slots/SlotIronFurnaceInputGenerator;"
- "SlotIronFurnaceInputGenerator.java"

### `ironfurnaces/container/slots/SlotIronFurnaceOutputFactory.class`

- "ironfurnaces/container/slots/SlotIronFurnaceOutputFactory"
- "getTier"
- "isFactory"
- "getAugmentGUI"
- "Lironfurnaces/container/slots/SlotIronFurnaceOutputFactory;"
- "SlotIronFurnaceOutputFactory.java"

### `ironfurnaces/energy/FEnergyStorage.class`

- "net/neoforged/neoforge/energy/EnergyStorage"
- "ironfurnaces/energy/FEnergyStorage"
- "getEnergyStored"
- "getMaxEnergyStored"
- "energy"
- "onEnergyChanged"
- "(I)Lnet/neoforged/neoforge/energy/EnergyStorage;"
- "Lironfurnaces/energy/FEnergyStorage;"
- "getEnergy"
- "setEnergy"
- "setEnergyDirectly"
- "FEnergyStorage.java"

### `ironfurnaces/gui/BlockWirelessEnergyHeaterScreen.class`

- "ironfurnaces/gui/BlockWirelessEnergyHeaterScreenBase"
- "(Lironfurnaces/container/BlockWirelessEnergyHeaterContainer;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)V"
- "ironfurnaces/gui/BlockWirelessEnergyHeaterScreen"
- "Lironfurnaces/gui/BlockWirelessEnergyHeaterScreen;"
- "blockWirelessEnergyHeaterContainer"
- "Lironfurnaces/container/BlockWirelessEnergyHeaterContainer;"
- "Lironfurnaces/gui/BlockWirelessEnergyHeaterScreenBase<Lironfurnaces/container/BlockWirelessEnergyHeaterContainer;>;"
- "BlockWirelessEnergyHeaterScreen.java"

### `ironfurnaces/gui/BlockWirelessEnergyHeaterScreenBase.class`

- "ironfurnaces/gui/BlockWirelessEnergyHeaterScreenBase"
- "ironfurnaces/container/BlockWirelessEnergyHeaterContainer"
- "getEnergy"
- "getMaxEnergy"
- "displayEnergy"
- "getEnergyScaled"
- "(Lironfurnaces/container/BlockWirelessEnergyHeaterContainer;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)V"
- "Lironfurnaces/gui/BlockWirelessEnergyHeaterScreenBase;"
- "Lironfurnaces/container/BlockWirelessEnergyHeaterContainer;"
- "Lironfurnaces/gui/BlockWirelessEnergyHeaterScreenBase<TT;>;"
- "energy"
- "<T:Lironfurnaces/container/BlockWirelessEnergyHeaterContainer;>Lnet/minecraft/client/gui/screens/inventory/AbstractContainerScreen<TT;>;"
- "BlockWirelessEnergyHeaterScreenBase.java"

### `ironfurnaces/gui/furnaces/BlockIronFurnaceScreenBase.class`

- "ironfurnaces/util/gui/FurnaceGuiEnergy"
- "energyBar"
- "Lironfurnaces/util/gui/FurnaceGuiEnergy;"
- "augmentButton"
- "isRainbowFurnace"
- "getIsFactory"
- "tooltip.ironfurnaces.gui_open_augments"
- "getAugmentGUI"
- "getIsGenerator"
- "getEnergy"
- "getMaxEnergy"
- "GUI_FACTORY"
- "GUI_GENERATOR"
- "GUI_AUGMENTS"
- "getCookScaled"
- "isGeneratorBurning"
- "getGeneratorBurnScaled"
- "getEnergyScaled"
- "getTier"
- "getFactoryCooktimeSize"
- "getFactoryCookScaled"
- "renderGeneratorBg"
- "renderFactoryBg"
- "addFactoryButtons"
- "mouseClickedAugmentButton"
- "textures/gui/furnace_factory.png"
- "textures/gui/furnace_generator.png"
- "textures/gui/furnace_generator_netherite.png"
- "GUI_GENERATOR_NETHERITE"
- "textures/gui/furnace_generator_allthemodium.png"
- "GUI_GENERATOR_ALLTHEMODIUM"
- "textures/gui/furnace_generator_vibranium.png"
- "GUI_GENERATOR_VIBRANIUM"
- "textures/gui/furnace_generator_unobtainium.png"
- "GUI_GENERATOR_UNOBTAINIUM"
- "textures/gui/augment.png"
- "fuel"
- "java/lang/invoke/StringConcatFactory"

### `ironfurnaces/init/ClientSetup.class`

- "ironfurnaces/gui/BlockWirelessEnergyHeaterScreen"
- "(Lironfurnaces/container/BlockWirelessEnergyHeaterContainer;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)V"
- "(Lironfurnaces/container/BlockWirelessEnergyHeaterContainer;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)Lironfurnaces/gui/BlockWirelessEnergyHeaterScreen;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `ironfurnaces/init/Registration$1.class`

- "generator_blasting"
- "Ljava/lang/Object;Lnet/minecraft/world/item/crafting/RecipeType<Lironfurnaces/recipes/GeneratorRecipe;>;"

### `ironfurnaces/init/Registration$RecipeTypes.class`

- "generator_blasting"
- "ironfurnaces/recipes/GeneratorRecipe"
- "GENERATOR_BLASTING"
- "generator_smoking"
- "ironfurnaces/recipes/SimpleGeneratorRecipe"
- "GENERATOR_SMOKING"
- "generator_regular"
- "GENERATOR_REGULAR"
- "Lmezz/jei/api/recipe/RecipeType<Lironfurnaces/recipes/GeneratorRecipe;>;"
- "Lmezz/jei/api/recipe/RecipeType<Lironfurnaces/recipes/SimpleGeneratorRecipe;>;"

### `ironfurnaces/init/Registration.class`

- "()Lnet/minecraft/world/item/CreativeModeTab$DisplayItemsGenerator;"
- "(Lnet/minecraft/world/item/CreativeModeTab$DisplayItemsGenerator;)Lnet/minecraft/world/item/CreativeModeTab$Builder;"
- "IRON_UPGRADE"
- "GOLD_UPGRADE"
- "DIAMOND_UPGRADE"
- "EMERALD_UPGRADE"
- "OBSIDIAN_UPGRADE"
- "CRYSTAL_UPGRADE"
- "NETHERITE_UPGRADE"
- "COPPER_UPGRADE"
- "SILVER_UPGRADE"
- "OBSIDIAN2_UPGRADE"
- "IRON2_UPGRADE"
- "GOLD2_UPGRADE"
- "SILVER2_UPGRADE"
- "BLASTING_AUGMENT"
- "SMOKING_AUGMENT"
- "FACTORY_AUGMENT"
- "GENERATOR_AUGMENT"
- "SPEED_AUGMENT"
- "FUEL_AUGMENT"
- "RAINBOW_CORE"
- "RAINBOW_PLATING"
- "RAINBOW_COAL"
- "()Lnet/neoforged/neoforge/network/IContainerFactory;"
- "(Lnet/neoforged/neoforge/network/IContainerFactory;)Lnet/minecraft/world/inventory/MenuType;"
- "ironfurnaces/items/ItemRainbowCoal"
- "ironfurnaces/items/augments/ItemAugmentFuel"
- "ironfurnaces/items/augments/ItemAugmentSpeed"
- "ironfurnaces/items/augments/ItemAugmentGenerator"
- "ironfurnaces/items/augments/ItemAugmentFactory"
- "ironfurnaces/items/augments/ItemAugmentSmoking"
- "ironfurnaces/items/augments/ItemAugmentBlasting"
- "ironfurnaces/container/BlockWirelessEnergyHeaterContainer"
- "ironfurnaces/blocks/BlockWirelessEnergyHeater"
- "ironfurnaces/items/upgrades/ItemUpgradeUnobtainium"
- "ironfurnaces/items/upgrades/ItemUpgradeVibranium"
- "ironfurnaces/items/upgrades/ItemUpgradeAllthemodium"
- "ironfurnaces/items/upgrades/ItemUpgradeSilver2"
- "ironfurnaces/items/upgrades/ItemUpgradeGold2"
- "ironfurnaces/items/upgrades/ItemUpgradeIron2"
- "ironfurnaces/items/upgrades/ItemUpgradeObsidian2"
- "ironfurnaces/items/upgrades/ItemUpgradeSilver"
- "ironfurnaces/items/upgrades/ItemUpgradeCopper"
- "ironfurnaces/items/upgrades/ItemUpgradeNetherite"
- "ironfurnaces/items/upgrades/ItemUpgradeCrystal"
- "ironfurnaces/items/upgrades/ItemUpgradeObsidian"
- "ironfurnaces/items/upgrades/ItemUpgradeEmerald"
- "ironfurnaces/items/upgrades/ItemUpgradeDiamond"
- "ironfurnaces/items/upgrades/ItemUpgradeGold"
- "ironfurnaces/items/upgrades/ItemUpgradeIron"
- "energy"
- "ENERGY"
- "generator_blasting"
- "GENERATOR_RECIPE_TYPE"
- "GENERATOR_RECIPE_SERIALIZER"
- "upgrade_iron"
- "upgrade_gold"
- "upgrade_diamond"
- "upgrade_emerald"
- "upgrade_obsidian"
- "upgrade_crystal"
- "upgrade_netherite"
- "upgrade_copper"
- "upgrade_silver"
- "upgrade_obsidian2"
- "upgrade_iron2"
- "upgrade_gold2"
- "upgrade_silver2"
- "upgrade_allthemodium"
- "ALLTHEMODIUM_UPGRADE"
- "upgrade_vibranium"
- "VIBRANIUM_UPGRADE"
- "upgrade_unobtainium"
- "UNOBTAINIUM_UPGRADE"
- "augment_blasting"
- "augment_smoking"
- "augment_factory"
- "augment_generator"
- "augment_speed"
- "augment_fuel"
- "rainbow_core"
- "rainbow_plating"
- "rainbow_coal"
- "GENERATOR_ID"
- "Ljava/util/function/Supplier<Lnet/minecraft/world/item/crafting/RecipeType<Lironfurnaces/recipes/GeneratorRecipe;>;>;"
- "Ljava/util/function/Supplier<Lnet/minecraft/world/item/crafting/RecipeSerializer<Lironfurnaces/recipes/GeneratorRecipe;>;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/upgrades/ItemUpgradeIron;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/upgrades/ItemUpgradeGold;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/upgrades/ItemUpgradeDiamond;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/upgrades/ItemUpgradeEmerald;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/upgrades/ItemUpgradeObsidian;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/upgrades/ItemUpgradeCrystal;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/upgrades/ItemUpgradeNetherite;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/upgrades/ItemUpgradeCopper;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/upgrades/ItemUpgradeSilver;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/upgrades/ItemUpgradeObsidian2;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/upgrades/ItemUpgradeIron2;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/upgrades/ItemUpgradeGold2;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/upgrades/ItemUpgradeSilver2;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/upgrades/ItemUpgradeAllthemodium;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/upgrades/ItemUpgradeVibranium;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/upgrades/ItemUpgradeUnobtainium;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/level/block/Block;Lironfurnaces/blocks/BlockWirelessEnergyHeater;>;"
- "Ljava/util/function/Supplier<Lnet/minecraft/world/level/block/entity/BlockEntityType<Lironfurnaces/tileentity/BlockWirelessEnergyHeaterTile;>;>;"
- "Ljava/util/function/Supplier<Lnet/minecraft/world/inventory/MenuType<Lironfurnaces/container/BlockWirelessEnergyHeaterContainer;>;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/augments/ItemAugmentBlasting;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/augments/ItemAugmentSmoking;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/augments/ItemAugmentFactory;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/augments/ItemAugmentGenerator;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/augments/ItemAugmentSpeed;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/augments/ItemAugmentFuel;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/Item;Lironfurnaces/items/ItemRainbowCoal;>;"
- "()Lironfurnaces/items/ItemRainbowCoal;"
- "()Lironfurnaces/items/augments/ItemAugmentFuel;"
- "()Lironfurnaces/items/augments/ItemAugmentSpeed;"
- "()Lironfurnaces/items/augments/ItemAugmentGenerator;"
- "()Lironfurnaces/items/augments/ItemAugmentFactory;"
- "()Lironfurnaces/items/augments/ItemAugmentSmoking;"
- "()Lironfurnaces/items/augments/ItemAugmentBlasting;"
- "(ILnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/RegistryFriendlyByteBuf;)Lironfurnaces/container/BlockWirelessEnergyHeaterContainer;"
- "()Lironfurnaces/blocks/BlockWirelessEnergyHeater;"
- "()Lironfurnaces/items/upgrades/ItemUpgradeUnobtainium;"
- "()Lironfurnaces/items/upgrades/ItemUpgradeVibranium;"
- "()Lironfurnaces/items/upgrades/ItemUpgradeAllthemodium;"
- "()Lironfurnaces/items/upgrades/ItemUpgradeSilver2;"
- "()Lironfurnaces/items/upgrades/ItemUpgradeGold2;"
- "()Lironfurnaces/items/upgrades/ItemUpgradeIron2;"
- "()Lironfurnaces/items/upgrades/ItemUpgradeObsidian2;"
- "()Lironfurnaces/items/upgrades/ItemUpgradeSilver;"
- "()Lironfurnaces/items/upgrades/ItemUpgradeCopper;"
- "()Lironfurnaces/items/upgrades/ItemUpgradeNetherite;"
- "()Lironfurnaces/items/upgrades/ItemUpgradeCrystal;"
- "()Lironfurnaces/items/upgrades/ItemUpgradeObsidian;"
- "()Lironfurnaces/items/upgrades/ItemUpgradeEmerald;"
- "()Lironfurnaces/items/upgrades/ItemUpgradeDiamond;"
- "()Lironfurnaces/items/upgrades/ItemUpgradeGold;"
- "()Lironfurnaces/items/upgrades/ItemUpgradeIron;"
- "ironfurnaces/tileentity/BlockWirelessEnergyHeaterTile"
- "(Lnet/minecraft/core/BlockPos;Lnet/minecraft/world/level/block/state/BlockState;)Lironfurnaces/tileentity/BlockWirelessEnergyHeaterTile;"
- "ironfurnaces/recipes/GeneratorRecipe$Serializer"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "net/minecraft/world/item/CreativeModeTab$DisplayItemsGenerator"
- "DisplayItemsGenerator"
- "ironfurnaces/recipes/GeneratorRecipe"

### `ironfurnaces/IronFurnaces.class`

- "net/neoforged/neoforge/capabilities/Capabilities$EnergyStorage"
- "energyStorage"
- "Lironfurnaces/energy/FEnergyStorage;"
- "ironfurnaces/tileentity/BlockWirelessEnergyHeaterTile"
- "(Lnet/minecraft/world/level/Level;Lnet/minecraft/core/BlockPos;Lnet/minecraft/world/level/block/state/BlockState;Lnet/minecraft/world/level/block/entity/BlockEntity;Lnet/minecraft/core/Direction;)Lnet/neoforged/neoforge/energy/IEnergyStorage;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "EnergyStorage"

### `ironfurnaces/items/augments/ItemAugment.class`

- "tooltip.ironfurnaces.augment_right_click"
- "ironfurnaces/items/augments/ItemAugment"
- "Lironfurnaces/items/augments/ItemAugment;"
- "ItemAugment.java"

### `ironfurnaces/items/augments/ItemAugmentBlasting.class`

- "ironfurnaces/items/augments/ItemAugmentRed"
- "tooltip.ironfurnaces.augment_blasting"
- "ironfurnaces/items/augments/ItemAugmentBlasting"
- "Lironfurnaces/items/augments/ItemAugmentBlasting;"
- "ItemAugmentBlasting.java"

### `ironfurnaces/items/augments/ItemAugmentBlue.class`

- "ironfurnaces/items/augments/ItemAugment"
- "ironfurnaces/items/augments/ItemAugmentBlue"
- "Lironfurnaces/items/augments/ItemAugmentBlue;"
- "ItemAugmentBlue.java"

### `ironfurnaces/items/augments/ItemAugmentFactory.class`

- "ironfurnaces/items/augments/ItemAugmentBlue"
- "tooltip.ironfurnaces.augment_factory_pro"
- "tooltip.ironfurnaces.augment_factory_con"
- "ironfurnaces/items/augments/ItemAugmentFactory"
- "Lironfurnaces/items/augments/ItemAugmentFactory;"
- "ItemAugmentFactory.java"

### `ironfurnaces/items/augments/ItemAugmentFuel.class`

- "ironfurnaces/items/augments/ItemAugmentGreen"
- "tooltip.ironfurnaces.augment_fuel_pro"
- "tooltip.ironfurnaces.augment_fuel_con"
- "ironfurnaces/items/augments/ItemAugmentFuel"
- "Lironfurnaces/items/augments/ItemAugmentFuel;"
- "ItemAugmentFuel.java"

### `ironfurnaces/items/augments/ItemAugmentGenerator.class`

- "ironfurnaces/items/augments/ItemAugmentBlue"
- "tooltip.ironfurnaces.augment_generator_pro"
- "tooltip.ironfurnaces.augment_generator_con"
- "ironfurnaces/items/augments/ItemAugmentGenerator"
- "Lironfurnaces/items/augments/ItemAugmentGenerator;"
- "ItemAugmentGenerator.java"

### `ironfurnaces/items/augments/ItemAugmentGreen.class`

- "ironfurnaces/items/augments/ItemAugment"
- "ironfurnaces/items/augments/ItemAugmentGreen"
- "Lironfurnaces/items/augments/ItemAugmentGreen;"
- "ItemAugmentGreen.java"

### `ironfurnaces/items/augments/ItemAugmentRed.class`

- "ironfurnaces/items/augments/ItemAugment"
- "ironfurnaces/items/augments/ItemAugmentRed"
- "Lironfurnaces/items/augments/ItemAugmentRed;"
- "ItemAugmentRed.java"

### `ironfurnaces/items/augments/ItemAugmentSmoking.class`

- "ironfurnaces/items/augments/ItemAugmentRed"
- "tooltip.ironfurnaces.augment_smoking"
- "ironfurnaces/items/augments/ItemAugmentSmoking"
- "Lironfurnaces/items/augments/ItemAugmentSmoking;"
- "ItemAugmentSmoking.java"

### `ironfurnaces/items/augments/ItemAugmentSpeed.class`

- "ironfurnaces/items/augments/ItemAugmentGreen"
- "tooltip.ironfurnaces.augment_speed_pro"
- "tooltip.ironfurnaces.augment_speed_con"
- "ironfurnaces/items/augments/ItemAugmentSpeed"
- "Lironfurnaces/items/augments/ItemAugmentSpeed;"
- "ItemAugmentSpeed.java"

### `ironfurnaces/items/ItemFurnace.class`

- "tooltip.ironfurnaces.cooktime"
- "getCooktime"
- "millionFurnaceSpeed"
- "allthemodiumFurnaceSpeed"
- "vibraniumFurnaceSpeed"
- "unobtainiumFurnaceSpeed"
- "copperFurnaceSpeed"
- "crystalFurnaceSpeed"
- "diamondFurnaceSpeed"
- "emeraldFurnaceSpeed"
- "goldFurnaceSpeed"
- "ironFurnaceSpeed"
- "netheriteFurnaceSpeed"
- "obsidianFurnaceSpeed"
- "silverFurnaceSpeed"
- "java/lang/invoke/StringConcatFactory"

### `ironfurnaces/items/ItemFurnaceCopy.class`

- "java/lang/invoke/StringConcatFactory"

### `ironfurnaces/items/ItemHeater.class`

- "java/lang/invoke/StringConcatFactory"

### `ironfurnaces/items/ItemMillionFurnace.class`

- "tooltip.ironfurnaces.cooktime"
- "getCooktime"
- "tooltip.ironfurnaces.rainbow_gen1"
- "tooltip.ironfurnaces.rainbow_gen2"
- "tooltip.ironfurnaces.rainbow_blowup"
- "tooltip.ironfurnaces.rainbow_gen3"
- "tooltip.ironfurnaces.rainbow_gen4"
- "tooltip.ironfurnaces.rainbow_gen5"
- "java/lang/invoke/StringConcatFactory"

### `ironfurnaces/items/ItemRainbowCoal.class`

- "ironfurnaces/items/ItemRainbowCoal"
- "Lironfurnaces/items/ItemRainbowCoal;"
- "ItemRainbowCoal.java"

### `ironfurnaces/items/upgrades/ItemUpgrade.class`

- "ironfurnaces/items/upgrades/ItemUpgrade"
- "tooltip.ironfurnaces.upgrade_right_click"
- "energyStorage"
- "Lironfurnaces/energy/FEnergyStorage;"
- "factoryCookTime"
- "factoryTotalCookTime"
- "generatorBurn"
- "generatorRecentRecipeRF"
- "cookTime"
- "totalCookTime"
- "Lironfurnaces/items/upgrades/ItemUpgrade;"
- "FACTORY_COOKTIME"
- "FACTORY_TOTALCOOKTIME"
- "ironfurnaces/energy/FEnergyStorage"
- "ItemUpgrade.java"

### `ironfurnaces/items/upgrades/ItemUpgradeAllthemodium.class`

- "ironfurnaces/items/upgrades/ItemUpgrade"
- "ironfurnaces/items/upgrades/ItemUpgradeAllthemodium"
- "Lironfurnaces/items/upgrades/ItemUpgradeAllthemodium;"
- "ItemUpgradeAllthemodium.java"

### `ironfurnaces/items/upgrades/ItemUpgradeCopper.class`

- "ironfurnaces/items/upgrades/ItemUpgrade"
- "ironfurnaces/items/upgrades/ItemUpgradeCopper"
- "Lironfurnaces/items/upgrades/ItemUpgradeCopper;"
- "ItemUpgradeCopper.java"

### `ironfurnaces/items/upgrades/ItemUpgradeCrystal.class`

- "ironfurnaces/items/upgrades/ItemUpgrade"
- "ironfurnaces/items/upgrades/ItemUpgradeCrystal"
- "Lironfurnaces/items/upgrades/ItemUpgradeCrystal;"
- "ItemUpgradeCrystal.java"

### `ironfurnaces/items/upgrades/ItemUpgradeDiamond.class`

- "ironfurnaces/items/upgrades/ItemUpgrade"
- "ironfurnaces/items/upgrades/ItemUpgradeDiamond"
- "Lironfurnaces/items/upgrades/ItemUpgradeDiamond;"
- "ItemUpgradeDiamond.java"

### `ironfurnaces/items/upgrades/ItemUpgradeEmerald.class`

- "ironfurnaces/items/upgrades/ItemUpgrade"
- "ironfurnaces/items/upgrades/ItemUpgradeEmerald"
- "Lironfurnaces/items/upgrades/ItemUpgradeEmerald;"
- "ItemUpgradeEmerald.java"

### `ironfurnaces/items/upgrades/ItemUpgradeGold.class`

- "ironfurnaces/items/upgrades/ItemUpgrade"
- "ironfurnaces/items/upgrades/ItemUpgradeGold"
- "Lironfurnaces/items/upgrades/ItemUpgradeGold;"
- "ItemUpgradeGold.java"

### `ironfurnaces/items/upgrades/ItemUpgradeGold2.class`

- "ironfurnaces/items/upgrades/ItemUpgrade"
- "ironfurnaces/items/upgrades/ItemUpgradeGold2"
- "Lironfurnaces/items/upgrades/ItemUpgradeGold2;"
- "ItemUpgradeGold2.java"

### `ironfurnaces/items/upgrades/ItemUpgradeIron.class`

- "ironfurnaces/items/upgrades/ItemUpgrade"
- "ironfurnaces/items/upgrades/ItemUpgradeIron"
- "Lironfurnaces/items/upgrades/ItemUpgradeIron;"
- "ItemUpgradeIron.java"

### `ironfurnaces/items/upgrades/ItemUpgradeIron2.class`

- "ironfurnaces/items/upgrades/ItemUpgrade"
- "ironfurnaces/items/upgrades/ItemUpgradeIron2"
- "Lironfurnaces/items/upgrades/ItemUpgradeIron2;"
- "ItemUpgradeIron2.java"

### `ironfurnaces/items/upgrades/ItemUpgradeNetherite.class`

- "ironfurnaces/items/upgrades/ItemUpgrade"
- "ironfurnaces/items/upgrades/ItemUpgradeNetherite"
- "Lironfurnaces/items/upgrades/ItemUpgradeNetherite;"
- "ItemUpgradeNetherite.java"

### `ironfurnaces/items/upgrades/ItemUpgradeObsidian.class`

- "ironfurnaces/items/upgrades/ItemUpgrade"
- "ironfurnaces/items/upgrades/ItemUpgradeObsidian"
- "Lironfurnaces/items/upgrades/ItemUpgradeObsidian;"
- "ItemUpgradeObsidian.java"

### `ironfurnaces/items/upgrades/ItemUpgradeObsidian2.class`

- "ironfurnaces/items/upgrades/ItemUpgrade"
- "ironfurnaces/items/upgrades/ItemUpgradeObsidian2"
- "Lironfurnaces/items/upgrades/ItemUpgradeObsidian2;"
- "ItemUpgradeObsidian2.java"

### `ironfurnaces/items/upgrades/ItemUpgradeSilver.class`

- "ironfurnaces/items/upgrades/ItemUpgrade"
- "ironfurnaces/items/upgrades/ItemUpgradeSilver"
- "Lironfurnaces/items/upgrades/ItemUpgradeSilver;"
- "ItemUpgradeSilver.java"

### `ironfurnaces/items/upgrades/ItemUpgradeSilver2.class`

- "ironfurnaces/items/upgrades/ItemUpgrade"
- "ironfurnaces/items/upgrades/ItemUpgradeSilver2"
- "Lironfurnaces/items/upgrades/ItemUpgradeSilver2;"
- "ItemUpgradeSilver2.java"

### `ironfurnaces/items/upgrades/ItemUpgradeUnobtainium.class`

- "ironfurnaces/items/upgrades/ItemUpgrade"
- "ironfurnaces/items/upgrades/ItemUpgradeUnobtainium"
- "Lironfurnaces/items/upgrades/ItemUpgradeUnobtainium;"
- "ItemUpgradeUnobtainium.java"

### `ironfurnaces/items/upgrades/ItemUpgradeVibranium.class`

- "ironfurnaces/items/upgrades/ItemUpgrade"
- "ironfurnaces/items/upgrades/ItemUpgradeVibranium"
- "Lironfurnaces/items/upgrades/ItemUpgradeVibranium;"
- "ItemUpgradeVibranium.java"

### `ironfurnaces/jei/IronFurnacesJEIPlugin.class`

- "ironfurnaces/jei/RecipeCategoryGeneratorBlasting"
- "ironfurnaces/jei/RecipeCategoryGeneratorSmoking"
- "ironfurnaces/jei/RecipeCategoryGeneratorRegular"
- "ironfurnaces/recipes/SimpleGeneratorRecipe"
- "GENERATOR_REGULAR"
- "GENERATOR_RECIPE_TYPE"
- "ironfurnaces/recipes/GeneratorRecipe"
- "GENERATOR_BLASTING"
- "GENERATOR_SMOKING"
- "BLASTING_AUGMENT"
- "SMOKING_AUGMENT"
- "GENERATOR_AUGMENT"
- "FACTORY_AUGMENT"
- "FUELING"
- "Lnet/minecraft/world/item/crafting/RecipeHolder<Lironfurnaces/recipes/GeneratorRecipe;>;"
- "Ljava/util/List<Lironfurnaces/recipes/SimpleGeneratorRecipe;>;"
- "Ljava/util/List<Lironfurnaces/recipes/GeneratorRecipe;>;"
- "Ljava/util/List<Lnet/minecraft/world/item/crafting/RecipeHolder<Lironfurnaces/recipes/GeneratorRecipe;>;>;"

### `ironfurnaces/jei/RecipeCategoryGeneratorBlasting.class`

- "ironfurnaces/jei/RecipeCategoryGeneratorBlasting"
- "staticEnergy"
- "animatedEnergy"
- "GENERATOR_BLASTING"
- "GENERATOR_AUGMENT"
- "ironfurnaces/recipes/GeneratorRecipe"
- "getEnergy"
- "displayEnergy"
- "(Lironfurnaces/recipes/GeneratorRecipe;)Lnet/minecraft/resources/ResourceLocation;"
- "(Lironfurnaces/recipes/GeneratorRecipe;)Z"
- "(Lironfurnaces/recipes/GeneratorRecipe;DDLcom/mojang/blaze3d/platform/InputConstants$Key;)Z"
- "(Lironfurnaces/recipes/GeneratorRecipe;Lmezz/jei/api/gui/ingredient/IRecipeSlotsView;DD)Ljava/util/List;"
- "(Lironfurnaces/recipes/GeneratorRecipe;Lmezz/jei/api/gui/ingredient/IRecipeSlotsView;Lnet/minecraft/client/gui/GuiGraphics;DD)V"
- "(Lmezz/jei/api/gui/builder/IRecipeLayoutBuilder;Lironfurnaces/recipes/GeneratorRecipe;Lmezz/jei/api/recipe/IFocusGroup;)V"
- "category_generator_blasting"
- "Lironfurnaces/jei/RecipeCategoryGeneratorBlasting;"
- "()Lmezz/jei/api/recipe/RecipeType<Lironfurnaces/recipes/GeneratorRecipe;>;"
- "Lironfurnaces/recipes/GeneratorRecipe;"
- "(Lironfurnaces/recipes/GeneratorRecipe;Lmezz/jei/api/gui/ingredient/IRecipeSlotsView;DD)Ljava/util/List<Lnet/minecraft/network/chat/Component;>;"
- "Ljava/lang/Object;Lmezz/jei/api/recipe/category/IRecipeCategory<Lironfurnaces/recipes/GeneratorRecipe;>;"
- "RecipeCategoryGeneratorBlasting.java"

### `ironfurnaces/jei/RecipeCategoryGeneratorRegular.class`

- "ironfurnaces/jei/RecipeCategoryGeneratorRegular"
- "staticEnergy"
- "animatedEnergy"
- "GENERATOR_REGULAR"
- "GENERATOR_AUGMENT"
- "ironfurnaces/recipes/SimpleGeneratorRecipe"
- "getEnergy"
- "displayEnergy"
- "(Lironfurnaces/recipes/SimpleGeneratorRecipe;)Lnet/minecraft/resources/ResourceLocation;"
- "(Lironfurnaces/recipes/SimpleGeneratorRecipe;)Z"
- "(Lironfurnaces/recipes/SimpleGeneratorRecipe;DDLcom/mojang/blaze3d/platform/InputConstants$Key;)Z"
- "(Lironfurnaces/recipes/SimpleGeneratorRecipe;Lmezz/jei/api/gui/ingredient/IRecipeSlotsView;DD)Ljava/util/List;"
- "(Lironfurnaces/recipes/SimpleGeneratorRecipe;Lmezz/jei/api/gui/ingredient/IRecipeSlotsView;Lnet/minecraft/client/gui/GuiGraphics;DD)V"
- "(Lmezz/jei/api/gui/builder/IRecipeLayoutBuilder;Lironfurnaces/recipes/SimpleGeneratorRecipe;Lmezz/jei/api/recipe/IFocusGroup;)V"
- "category_generator_regular"
- "Lironfurnaces/jei/RecipeCategoryGeneratorRegular;"
- "()Lmezz/jei/api/recipe/RecipeType<Lironfurnaces/recipes/SimpleGeneratorRecipe;>;"
- "Lironfurnaces/recipes/SimpleGeneratorRecipe;"
- "(Lironfurnaces/recipes/SimpleGeneratorRecipe;Lmezz/jei/api/gui/ingredient/IRecipeSlotsView;DD)Ljava/util/List<Lnet/minecraft/network/chat/Component;>;"
- "Ljava/lang/Object;Lmezz/jei/api/recipe/category/IRecipeCategory<Lironfurnaces/recipes/SimpleGeneratorRecipe;>;"
- "RecipeCategoryGeneratorRegular.java"

### `ironfurnaces/jei/RecipeCategoryGeneratorSmoking.class`

- "ironfurnaces/jei/RecipeCategoryGeneratorSmoking"
- "staticEnergy"
- "animatedEnergy"
- "GENERATOR_SMOKING"
- "GENERATOR_AUGMENT"
- "ironfurnaces/recipes/SimpleGeneratorRecipe"
- "getEnergy"
- "displayEnergy"
- "(Lironfurnaces/recipes/SimpleGeneratorRecipe;)Lnet/minecraft/resources/ResourceLocation;"
- "(Lironfurnaces/recipes/SimpleGeneratorRecipe;)Z"
- "(Lironfurnaces/recipes/SimpleGeneratorRecipe;DDLcom/mojang/blaze3d/platform/InputConstants$Key;)Z"
- "(Lironfurnaces/recipes/SimpleGeneratorRecipe;Lmezz/jei/api/gui/ingredient/IRecipeSlotsView;DD)Ljava/util/List;"
- "(Lironfurnaces/recipes/SimpleGeneratorRecipe;Lmezz/jei/api/gui/ingredient/IRecipeSlotsView;Lnet/minecraft/client/gui/GuiGraphics;DD)V"
- "(Lmezz/jei/api/gui/builder/IRecipeLayoutBuilder;Lironfurnaces/recipes/SimpleGeneratorRecipe;Lmezz/jei/api/recipe/IFocusGroup;)V"
- "category_generator_smoking"
- "Lironfurnaces/jei/RecipeCategoryGeneratorSmoking;"
- "()Lmezz/jei/api/recipe/RecipeType<Lironfurnaces/recipes/SimpleGeneratorRecipe;>;"
- "Lironfurnaces/recipes/SimpleGeneratorRecipe;"
- "(Lironfurnaces/recipes/SimpleGeneratorRecipe;Lmezz/jei/api/gui/ingredient/IRecipeSlotsView;DD)Ljava/util/List<Lnet/minecraft/network/chat/Component;>;"
- "Ljava/lang/Object;Lmezz/jei/api/recipe/category/IRecipeCategory<Lironfurnaces/recipes/SimpleGeneratorRecipe;>;"
- "RecipeCategoryGeneratorSmoking.java"

### `ironfurnaces/network/Messages.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `ironfurnaces/network/PacketFurnaceSettings.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `ironfurnaces/network/PacketShowConfig.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `ironfurnaces/recipes/GeneratorRecipe$Serializer.class`

- "ironfurnaces/recipes/GeneratorRecipe"
- "energy"
- "ironfurnaces/recipes/GeneratorRecipe$Serializer"
- "Lcom/mojang/serialization/MapCodec<Lironfurnaces/recipes/GeneratorRecipe;>;"
- "Lnet/minecraft/network/codec/StreamCodec<Lnet/minecraft/network/RegistryFriendlyByteBuf;Lironfurnaces/recipes/GeneratorRecipe;>;"
- "Lironfurnaces/recipes/GeneratorRecipe$Serializer;"
- "Lironfurnaces/recipes/GeneratorRecipe$Serializer<TT;>;"
- "(Lnet/minecraft/network/RegistryFriendlyByteBuf;)Lironfurnaces/recipes/GeneratorRecipe;"
- "(Lnet/minecraft/network/RegistryFriendlyByteBuf;Lironfurnaces/recipes/GeneratorRecipe;)V"
- "Lironfurnaces/recipes/GeneratorRecipe;"
- "()Lcom/mojang/serialization/MapCodec<Lironfurnaces/recipes/GeneratorRecipe;>;"
- "()Lnet/minecraft/network/codec/StreamCodec<Lnet/minecraft/network/RegistryFriendlyByteBuf;Lironfurnaces/recipes/GeneratorRecipe;>;"
- "(Lironfurnaces/recipes/GeneratorRecipe;)Lnet/minecraft/world/item/crafting/Ingredient;"
- "(Lironfurnaces/recipes/GeneratorRecipe;)Ljava/lang/Integer;"
- "<T:Lironfurnaces/recipes/GeneratorRecipe;>Ljava/lang/Object;Lnet/minecraft/world/item/crafting/RecipeSerializer<Lironfurnaces/recipes/GeneratorRecipe;>;"
- "GeneratorRecipe.java"
- "(Ljava/lang/Integer;Lnet/minecraft/world/item/crafting/Ingredient;)Lironfurnaces/recipes/GeneratorRecipe;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `ironfurnaces/recipes/GeneratorRecipe.class`

- "ironfurnaces/recipes/GeneratorRecipe"
- "energy"
- "GENERATOR_RECIPE_SERIALIZER"
- "GENERATOR_RECIPE_TYPE"
- "Lironfurnaces/recipes/GeneratorRecipe;"
- "getEnergy"
- "GeneratorRecipe.java"
- "ironfurnaces/recipes/GeneratorRecipe$Serializer"

### `ironfurnaces/recipes/SimpleGeneratorRecipe.class`

- "ironfurnaces/recipes/SimpleGeneratorRecipe"
- "energy"
- "Lironfurnaces/recipes/SimpleGeneratorRecipe;"
- "getEnergy"
- "SimpleGeneratorRecipe.java"

### `ironfurnaces/tileentity/BlockWirelessEnergyHeaterTile$1.class`

- "ironfurnaces/tileentity/BlockWirelessEnergyHeaterTile$1"
- "Lironfurnaces/tileentity/BlockWirelessEnergyHeaterTile;"
- "ironfurnaces/energy/FEnergyStorage"
- "ironfurnaces/tileentity/BlockWirelessEnergyHeaterTile"
- "(Lironfurnaces/tileentity/BlockWirelessEnergyHeaterTile;III)V"
- "Lironfurnaces/tileentity/BlockWirelessEnergyHeaterTile$1;"
- "onEnergyChanged"
- "BlockWirelessEnergyHeaterTile.java"

### `ironfurnaces/tileentity/BlockWirelessEnergyHeaterTile.class`

- "ironfurnaces/tileentity/BlockWirelessEnergyHeaterTile$1"
- "(Lironfurnaces/tileentity/BlockWirelessEnergyHeaterTile;III)V"
- "ironfurnaces/tileentity/BlockWirelessEnergyHeaterTile"
- "energyStorage"
- "Lironfurnaces/energy/FEnergyStorage;"
- "ironfurnaces/energy/FEnergyStorage"
- "getEnergy"
- "setEnergy"
- "(I)Lnet/neoforged/neoforge/energy/EnergyStorage;"
- "Energy"
- "container.ironfurnaces.wireless_energy_heater"
- "ironfurnaces/container/BlockWirelessEnergyHeaterContainer"
- "Lironfurnaces/tileentity/BlockWirelessEnergyHeaterTile;"
- "(Lnet/minecraft/world/level/Level;Lnet/minecraft/core/BlockPos;Lnet/minecraft/world/level/block/state/BlockState;Lironfurnaces/tileentity/BlockWirelessEnergyHeaterTile;)V"
- "energy"
- "setMaxEnergy"
- "removeEnergy"
- "BlockWirelessEnergyHeaterTile.java"

### `ironfurnaces/tileentity/furnaces/BlockCopperFurnaceTile.class`

- "copperFurnaceSpeed"
- "copperFurnaceTier"
- "getCookTimeConfig"
- "getTier"

### `ironfurnaces/tileentity/furnaces/BlockCrystalFurnaceTile.class`

- "crystalFurnaceSpeed"
- "crystalFurnaceTier"
- "getCookTimeConfig"
- "getTier"

### `ironfurnaces/tileentity/furnaces/BlockDiamondFurnaceTile.class`

- "diamondFurnaceSpeed"
- "diamondFurnaceTier"
- "getCookTimeConfig"
- "getTier"

### `ironfurnaces/tileentity/furnaces/BlockEmeraldFurnaceTile.class`

- "emeraldFurnaceSpeed"
- "emeraldFurnaceTier"
- "getCookTimeConfig"
- "getTier"

### `ironfurnaces/tileentity/furnaces/BlockGoldFurnaceTile.class`

- "goldFurnaceSpeed"
- "goldFurnaceTier"
- "getCookTimeConfig"
- "getTier"

### `ironfurnaces/tileentity/furnaces/BlockIronFurnaceTile.class`

- "ironFurnaceSpeed"
- "ironFurnaceTier"
- "getCookTimeConfig"
- "getTier"

### `ironfurnaces/tileentity/furnaces/BlockIronFurnaceTileBase$1.class`

- "ironfurnaces/energy/FEnergyStorage"
- "lastGameTickEnergyUpdated"
- "onEnergyChanged"

### `ironfurnaces/tileentity/furnaces/BlockIronFurnaceTileBase.class`

- "currentAugment"
- "factoryCookTime"
- "factoryTotalCookTime"
- "furnaceEnergyCapacityTier2"
- "energyStorage"
- "Lironfurnaces/energy/FEnergyStorage;"
- "GENERATOR_RECIPE_TYPE"
- "recipeCheckGenerator"
- "ironfurnaces/energy/FEnergyStorage"
- "getEnergy"
- "setEnergy"
- "(I)Lnet/neoforged/neoforge/energy/EnergyStorage;"
- "ironfurnaces/items/augments/ItemAugmentBlasting"
- "ironfurnaces/items/augments/ItemAugmentSmoking"
- "totalCookTime"
- "getSpeed"
- "ironfurnaces/items/augments/ItemAugmentSpeed"
- "ironfurnaces/items/augments/ItemAugmentFuel"
- "getCookTimeConfig"
- "net/minecraft/world/item/crafting/AbstractCookingRecipe"
- "getCookingTime"
- "FACTORY_INPUT"
- "getFactorySpeed"
- "ironfurnaces/items/augments/ItemAugmentFactory"
- "ironfurnaces/items/augments/ItemAugmentGenerator"
- "getRecipeGeneratorBlasting"
- "ironfurnaces/recipes/GeneratorRecipe"
- "generatorBurn"
- "isGenerator"
- "rainbowCheckFurnaceTiers"
- "rainbowGenerating"
- "RAINBOW_GENERATING"
- "rainbowEnergyOut"
- "getAugment"
- "getCapacityFromTier"
- "setMaxEnergy"
- "getCookTime"
- "cookTime"
- "isFactory"
- "getMaxEnergyStored"
- "getTier"
- "getFactoryCookTime"
- "canFactorySmelt"
- "isFactoryCooking"
- "factorySmelt"
- "autoFactoryIO"
- "getGeneratorBurn"
- "generatorRecentRecipeRF"
- "removeEnergy"
- "autoIOGenerator"
- "energyOut"
- "ironfurnaces/tileentity/BlockWirelessEnergyHeaterTile"
- "furnaceEnergyCapacityTier1"
- "furnaceEnergyCapacityTier0"
- "net/neoforged/neoforge/capabilities/Capabilities$EnergyStorage"
- "net/neoforged/neoforge/energy/IEnergyStorage"
- "getEnergyStored"
- "receiveEnergy"
- "isItemFuel"
- "isItemGeneratorFuel"
- "SMOKING_AUGMENT"
- "BLASTING_AUGMENT"
- "smeltFactoryItemMult"
- "smeltFactoryItem"
- "RainbowGen"
- "FactoryCookTime"
- "FactoryTotalCookTime"
- "GeneratorBurn"
- "GeneratorRecent"
- "CookTime"
- "CookTimeTotal"
- "Augment"
- "Energy"
- "lastGameTickEnergyUpdated"
- "ironfurnaces/items/augments/ItemAugmentRed"
- "ironfurnaces/items/augments/ItemAugmentGreen"
- "ironfurnaces/items/augments/ItemAugmentBlue"
- "ironfurnaces/items/augments/ItemAugment"
- "hasGeneratorBlastingRecipe"
- "FUEL"
- "AUGMENT_RED"
- "AUGMENT_GREEN"
- "AUGMENT_BLUE"
- "GENERATOR_FUEL"
- "Lnet/minecraft/world/item/crafting/RecipeType<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "Lnet/minecraft/world/item/crafting/RecipeManager$CachedCheck<Lnet/minecraft/world/item/crafting/SingleRecipeInput;+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "Lnet/minecraft/world/item/crafting/RecipeManager$CachedCheck<Lnet/minecraft/world/item/crafting/SingleRecipeInput;+Lironfurnaces/recipes/GeneratorRecipe;>;"
- "energy"
- "(Lnet/minecraft/world/item/ItemStack;)Lnet/minecraft/world/item/crafting/RecipeHolder<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "(Lnet/minecraft/world/item/ItemStack;)Lnet/minecraft/world/item/crafting/RecipeHolder<+Lironfurnaces/recipes/GeneratorRecipe;>;"
- "speed"
- "recipe_cooktime"
- "Lnet/minecraft/world/item/crafting/RecipeHolder<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "Lnet/minecraft/world/item/crafting/RecipeHolder<+Lironfurnaces/recipes/GeneratorRecipe;>;"
- "rainbowGens"
- "rainbow"
- "energyRecipe"
- "Lnet/neoforged/neoforge/energy/IEnergyStorage;"
- "getAugmentGUI"
- "isRainbowFurnace"
- "isItemAugment"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "java/lang/invoke/StringConcatFactory"
- "EnergyStorage"

### `ironfurnaces/tileentity/furnaces/BlockMillionFurnaceTile.class`

- "millionFurnaceSpeed"
- "millionFurnaceTier"
- "getCookTimeConfig"
- "getTier"
- "java/lang/invoke/StringConcatFactory"

### `ironfurnaces/tileentity/furnaces/BlockNetheriteFurnaceTile.class`

- "netheriteFurnaceSpeed"
- "netheriteFurnaceTier"
- "getCookTimeConfig"
- "getTier"

### `ironfurnaces/tileentity/furnaces/BlockObsidianFurnaceTile.class`

- "obsidianFurnaceSpeed"
- "obsidianFurnaceTier"
- "getCookTimeConfig"
- "getTier"

### `ironfurnaces/tileentity/furnaces/BlockSilverFurnaceTile.class`

- "silverFurnaceSpeed"
- "silverFurnaceTier"
- "getCookTimeConfig"
- "getTier"

### `ironfurnaces/tileentity/furnaces/other/BlockAllthemodiumFurnaceTile.class`

- "allthemodiumFurnaceSpeed"
- "allthemodiumFurnaceTier"
- "getCookTimeConfig"
- "getTier"

### `ironfurnaces/tileentity/furnaces/other/BlockUnobtainiumFurnaceTile.class`

- "unobtainiumFurnaceSpeed"
- "unobtainiumFurnaceTier"
- "getCookTimeConfig"
- "getTier"

### `ironfurnaces/tileentity/furnaces/other/BlockVibraniumFurnaceTile.class`

- "vibraniumFurnaceSpeed"
- "vibraniumFurnaceTier"
- "getCookTimeConfig"
- "getTier"

### `ironfurnaces/util/container/FactoryDataSlot.class`

- "ironfurnaces/util/container/FactoryDataSlot"
- "Lironfurnaces/util/container/FactoryDataSlot;"
- "FactoryDataSlot.java"

### `ironfurnaces/util/EventHandler.class`

- "RAINBOW_COAL"

### `ironfurnaces/util/FurnaceSettings.class`

- "augmentGUI"
- "AugmentGUI"

### `ironfurnaces/util/gui/FurnaceGuiEnergy.class`

- "ironfurnaces/util/gui/FurnaceGuiEnergy"
- "displayEnergy"
- "Lironfurnaces/util/gui/FurnaceGuiEnergy;"
- "energy"
- "FurnaceGuiEnergy.java"

### `ironfurnaces/util/StringHelper.class`

- "displayEnergy"
- "energy"
- "java/lang/invoke/StringConcatFactory"
