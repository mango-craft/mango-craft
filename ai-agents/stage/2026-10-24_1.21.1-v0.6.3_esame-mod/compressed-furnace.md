# Compressed Furnace (compressed-furnace)

File generato da `scripts/esamina.py` (workflow "Esamina mod"): la mod **non** è nel pack. Non modificarlo a mano.

- Versione: **0.2.0** (release, 2026-01-19), file `compressedfurnace-1.21.1-neoforge-0.2.0.jar`, id versione `JR7nZkNB`
- Licenza su Modrinth: MIT · download: 33572
- Filtro dei valori: `(recipe|recipes|tags/item|tags/block)/` · filtro dei testi del codice: `(?i)^(.*(speed|cook|tier|augment|upgrade|generator|factory|fuel|multiplier|energy|rainbow).*)$`

## Mod nel file e dipendenze dichiarate

- `compressedfurnace` 0.2.0
  - required: `neoforge` [21.1.0,)
  - required: `minecraft` [1.21.1, 1.22)

## Cartelle di dati (file .json)

- `compressedfurnace:advancement/recipes/decorations/blasting`: 3
- `compressedfurnace:advancement/recipes/decorations/smelting`: 3
- `compressedfurnace:advancement/recipes/misc`: 21
- `compressedfurnace:advancement/recipes/misc/blasting`: 1
- `compressedfurnace:advancement/recipes/misc/crusher`: 37
- `compressedfurnace:advancement/recipes/misc/smelting`: 1
- `compressedfurnace:loot_table/blocks`: 21
- `compressedfurnace:recipe`: 21
- `compressedfurnace:recipe/blasting`: 4
- `compressedfurnace:recipe/crusher`: 37
- `compressedfurnace:recipe/crusher/ae2`: 6
- `compressedfurnace:recipe/crusher/basic_nether_ores`: 45
- `compressedfurnace:recipe/crusher/extream_reactor`: 2
- `compressedfurnace:recipe/crusher/mekanism`: 11
- `compressedfurnace:recipe/crusher/mystical_agradditions`: 9
- `compressedfurnace:recipe/smelting`: 4
- `minecraft:tags/block`: 2
- `minecraft:tags/block/mineable`: 1

## Valori dei file filtrati


### `data/compressedfurnace/advancement/recipes/decorations/blasting/has_raw_copper_block_to_has_copper_block.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_raw_copper_block.conditions.items[0].items` = "minecraft:raw_copper_block"
- `criteria.has_raw_copper_block.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:blasting/has_raw_copper_block_to_has_copper_block"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_raw_copper_block"]
- `rewards.recipes` = ["compressedfurnace:blasting/has_raw_copper_block_to_has_copper_block"]

### `data/compressedfurnace/advancement/recipes/decorations/blasting/has_raw_gold_block_to_has_gold_block.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_raw_gold_block.conditions.items[0].items` = "minecraft:raw_gold_block"
- `criteria.has_raw_gold_block.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:blasting/has_raw_gold_block_to_has_gold_block"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_raw_gold_block"]
- `rewards.recipes` = ["compressedfurnace:blasting/has_raw_gold_block_to_has_gold_block"]

### `data/compressedfurnace/advancement/recipes/decorations/blasting/has_raw_iron_block_to_has_iron_block.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_raw_iron_block.conditions.items[0].items` = "minecraft:raw_iron_block"
- `criteria.has_raw_iron_block.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:blasting/has_raw_iron_block_to_has_iron_block"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_raw_iron_block"]
- `rewards.recipes` = ["compressedfurnace:blasting/has_raw_iron_block_to_has_iron_block"]

### `data/compressedfurnace/advancement/recipes/decorations/smelting/has_raw_copper_block_to_has_copper_block.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_raw_copper_block.conditions.items[0].items` = "minecraft:raw_copper_block"
- `criteria.has_raw_copper_block.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:smelting/has_raw_copper_block_to_has_copper_block"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_raw_copper_block"]
- `rewards.recipes` = ["compressedfurnace:smelting/has_raw_copper_block_to_has_copper_block"]

### `data/compressedfurnace/advancement/recipes/decorations/smelting/has_raw_gold_block_to_has_gold_block.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_raw_gold_block.conditions.items[0].items` = "minecraft:raw_gold_block"
- `criteria.has_raw_gold_block.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:smelting/has_raw_gold_block_to_has_gold_block"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_raw_gold_block"]
- `rewards.recipes` = ["compressedfurnace:smelting/has_raw_gold_block_to_has_gold_block"]

### `data/compressedfurnace/advancement/recipes/decorations/smelting/has_raw_iron_block_to_has_iron_block.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_raw_iron_block.conditions.items[0].items` = "minecraft:raw_iron_block"
- `criteria.has_raw_iron_block.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:smelting/has_raw_iron_block_to_has_iron_block"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_raw_iron_block"]
- `rewards.recipes` = ["compressedfurnace:smelting/has_raw_iron_block_to_has_iron_block"]

### `data/compressedfurnace/advancement/recipes/misc/blasting/has_raw_scrap_to_has_netherite_scrap.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_raw_scrap.conditions.items[0].items` = "compressedfurnace:raw_scrap"
- `criteria.has_raw_scrap.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:blasting/has_raw_scrap_to_has_netherite_scrap"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_raw_scrap"]
- `rewards.recipes` = ["compressedfurnace:blasting/has_raw_scrap_to_has_netherite_scrap"]

### `data/compressedfurnace/advancement/recipes/misc/compressed_blast_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_blast_furnace.conditions.items[0].items` = "minecraft:blast_furnace"
- `criteria.has_blast_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_cobblestone.conditions.items[0].items` = "minecraft:cobblestone"
- `criteria.has_cobblestone.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:compressed_blast_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_cobblestone", "has_blast_furnace"]
- `rewards.recipes` = ["compressedfurnace:compressed_blast_furnace"]

### `data/compressedfurnace/advancement/recipes/misc/compressed_crusher.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_cobblestone.conditions.items[0].items` = "minecraft:cobblestone"
- `criteria.has_cobblestone.trigger` = "minecraft:inventory_changed"
- `criteria.has_compressed_furnace.conditions.items[0].items` = "compressedfurnace:compressed_furnace"
- `criteria.has_compressed_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_flint.conditions.items[0].items` = "minecraft:flint"
- `criteria.has_flint.trigger` = "minecraft:inventory_changed"
- `criteria.has_iron_ingot.conditions.items[0].items` = "minecraft:iron_ingot"
- `criteria.has_iron_ingot.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:compressed_crusher"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_cobblestone", "has_flint", "has_iron_ingot", "has_compressed_furnace"]
- `rewards.recipes` = ["compressedfurnace:compressed_crusher"]

### `data/compressedfurnace/advancement/recipes/misc/compressed_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_cobblestone.conditions.items[0].items` = "minecraft:cobblestone"
- `criteria.has_cobblestone.trigger` = "minecraft:inventory_changed"
- `criteria.has_furnace.conditions.items[0].items` = "minecraft:furnace"
- `criteria.has_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:compressed_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_cobblestone", "has_furnace"]
- `rewards.recipes` = ["compressedfurnace:compressed_furnace"]

### `data/compressedfurnace/advancement/recipes/misc/compressed_generator.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_compressed_furnace.conditions.items[0].items` = "compressedfurnace:compressed_furnace"
- `criteria.has_compressed_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_gold_ingot.conditions.items[0].items` = "minecraft:gold_ingot"
- `criteria.has_gold_ingot.trigger` = "minecraft:inventory_changed"
- `criteria.has_redstone.conditions.items[0].items` = "minecraft:redstone"
- `criteria.has_redstone.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:compressed_generator"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_gold_ingot", "has_redstone", "has_compressed_furnace"]
- `rewards.recipes` = ["compressedfurnace:compressed_generator"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_ancient_debris.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ancient_debris.conditions.items[0].items` = "minecraft:ancient_debris"
- `criteria.has_ancient_debris.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_ancient_debris"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_ancient_debris"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_ancient_debris"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_andesite_to_gravel.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_andesite.conditions.items[0].items` = "minecraft:andesite"
- `criteria.has_andesite.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_andesite_to_gravel"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_andesite"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_andesite_to_gravel"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_blaze_rod.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_blaze_rod.conditions.items[0].items` = "minecraft:blaze_rod"
- `criteria.has_blaze_rod.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_blaze_rod"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_blaze_rod"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_blaze_rod"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_coal.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_coal_ore.conditions.items[0].items` = "minecraft:coal_ore"
- `criteria.has_coal_ore.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_coal"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_coal_ore"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_coal"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_cobbled_to_gravel.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_cobbled_deepslate.conditions.items[0].items` = "minecraft:cobbled_deepslate"
- `criteria.has_cobbled_deepslate.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_cobbled_to_gravel"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_cobbled_deepslate"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_cobbled_to_gravel"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_cobble_to_gravel.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_cobblestone.conditions.items[0].items` = "minecraft:cobblestone"
- `criteria.has_cobblestone.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_cobble_to_gravel"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_cobblestone"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_cobble_to_gravel"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_copper.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_copper_ore.conditions.items[0].items` = "minecraft:copper_ore"
- `criteria.has_copper_ore.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_copper"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_copper_ore"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_copper"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_deepslate_coal.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_deepslate_coal_ore.conditions.items[0].items` = "minecraft:deepslate_coal_ore"
- `criteria.has_deepslate_coal_ore.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_deepslate_coal"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_deepslate_coal_ore"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_deepslate_coal"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_deepslate_copper.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_deepslate_copper_ore.conditions.items[0].items` = "minecraft:deepslate_copper_ore"
- `criteria.has_deepslate_copper_ore.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_deepslate_copper"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_deepslate_copper_ore"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_deepslate_copper"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_deepslate_diamond.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_deepslate_diamond_ore.conditions.items[0].items` = "minecraft:deepslate_diamond_ore"
- `criteria.has_deepslate_diamond_ore.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_deepslate_diamond"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_deepslate_diamond_ore"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_deepslate_diamond"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_deepslate_emerald.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_deepslate_emerald_ore.conditions.items[0].items` = "minecraft:deepslate_emerald_ore"
- `criteria.has_deepslate_emerald_ore.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_deepslate_emerald"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_deepslate_emerald_ore"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_deepslate_emerald"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_deepslate_gold.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_deepslate_gold_ore.conditions.items[0].items` = "minecraft:deepslate_gold_ore"
- `criteria.has_deepslate_gold_ore.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_deepslate_gold"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_deepslate_gold_ore"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_deepslate_gold"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_deepslate_iron.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_deepslate_iron_ore.conditions.items[0].items` = "minecraft:deepslate_iron_ore"
- `criteria.has_deepslate_iron_ore.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_deepslate_iron"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_deepslate_iron_ore"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_deepslate_iron"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_deepslate_lapis.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_deepslate_lapis_ore.conditions.items[0].items` = "minecraft:deepslate_lapis_ore"
- `criteria.has_deepslate_lapis_ore.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_deepslate_lapis"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_deepslate_lapis_ore"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_deepslate_lapis"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_deepslate_redstone.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_deepslate_redstone_ore.conditions.items[0].items` = "minecraft:deepslate_redstone_ore"
- `criteria.has_deepslate_redstone_ore.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_deepslate_redstone"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_deepslate_redstone_ore"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_deepslate_redstone"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_deepslate_to_cobbled.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_deepslate.conditions.items[0].items` = "minecraft:deepslate"
- `criteria.has_deepslate.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_deepslate_to_cobbled"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_deepslate"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_deepslate_to_cobbled"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_diamond.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_diamond_ore.conditions.items[0].items` = "minecraft:diamond_ore"
- `criteria.has_diamond_ore.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_diamond"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_diamond_ore"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_diamond"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_diorite_to_gravel.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_diorite.conditions.items[0].items` = "minecraft:diorite"
- `criteria.has_diorite.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_diorite_to_gravel"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_diorite"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_diorite_to_gravel"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_dripstone_to_pointed_dripstone.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_dripstone_block.conditions.items[0].items` = "minecraft:dripstone_block"
- `criteria.has_dripstone_block.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_dripstone_to_pointed_dripstone"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_dripstone_block"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_dripstone_to_pointed_dripstone"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_emerald.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_emerald_ore.conditions.items[0].items` = "minecraft:emerald_ore"
- `criteria.has_emerald_ore.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_emerald"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_emerald_ore"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_emerald"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_gold.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_gold_ore.conditions.items[0].items` = "minecraft:gold_ore"
- `criteria.has_gold_ore.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_gold"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_gold_ore"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_gold"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_granite_to_gravel.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_granite.conditions.items[0].items` = "minecraft:granite"
- `criteria.has_granite.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_granite_to_gravel"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_granite"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_granite_to_gravel"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_gravel_to_sand.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_gravel.conditions.items[0].items` = "minecraft:gravel"
- `criteria.has_gravel.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_gravel_to_sand"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_gravel"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_gravel_to_sand"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_honeycomb_block_to_honeycomb.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_honeycomb_block.conditions.items[0].items` = "minecraft:honeycomb_block"
- `criteria.has_honeycomb_block.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_honeycomb_block_to_honeycomb"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_honeycomb_block"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_honeycomb_block_to_honeycomb"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_iron.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_iron_ore.conditions.items[0].items` = "minecraft:iron_ore"
- `criteria.has_iron_ore.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_iron"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_iron_ore"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_iron"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_lapis.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_lapis_ore.conditions.items[0].items` = "minecraft:lapis_ore"
- `criteria.has_lapis_ore.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_lapis"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_lapis_ore"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_lapis"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_nether_gold.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_nether_gold_ore.conditions.items[0].items` = "minecraft:nether_gold_ore"
- `criteria.has_nether_gold_ore.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_nether_gold"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_nether_gold_ore"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_nether_gold"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_prismarine_bricks_to_prismarine_shard.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_prismarine_bricks.conditions.items[0].items` = "minecraft:prismarine_bricks"
- `criteria.has_prismarine_bricks.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_prismarine_bricks_to_prismarine_shard"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_prismarine_bricks"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_prismarine_bricks_to_prismarine_shard"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_prismarine_brick_stairs_to_prismarine_shard.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_prismarine_brick_stairs.conditions.items[0].items` = "minecraft:prismarine_brick_stairs"
- `criteria.has_prismarine_brick_stairs.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_prismarine_brick_stairs_to_prismarine_shard"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_prismarine_brick_stairs"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_prismarine_brick_stairs_to_prismarine_shard"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_prismarine_slab_to_prismarine_shard.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_prismarine_slab.conditions.items[0].items` = "minecraft:prismarine_slab"
- `criteria.has_prismarine_slab.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_prismarine_slab_to_prismarine_shard"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_prismarine_slab"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_prismarine_slab_to_prismarine_shard"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_prismarine_stairs_to_prismarine_shard.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_prismarine_stairs.conditions.items[0].items` = "minecraft:prismarine_stairs"
- `criteria.has_prismarine_stairs.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_prismarine_stairs_to_prismarine_shard"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_prismarine_stairs"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_prismarine_stairs_to_prismarine_shard"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_quartz.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_nether_quartz_ore.conditions.items[0].items` = "minecraft:nether_quartz_ore"
- `criteria.has_nether_quartz_ore.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_quartz"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_nether_quartz_ore"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_quartz"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_quartz_block.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_quartz_block.conditions.items[0].items` = "minecraft:quartz_block"
- `criteria.has_quartz_block.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_quartz_block"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_quartz_block"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_quartz_block"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_redstone.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_redstone_ore.conditions.items[0].items` = "minecraft:redstone_ore"
- `criteria.has_redstone_ore.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_redstone"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_redstone_ore"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_redstone"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_sandstone_to_sand.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_sandstone.conditions.items[0].items` = "minecraft:sandstone"
- `criteria.has_sandstone.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_sandstone_to_sand"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_sandstone"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_sandstone_to_sand"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_stone_to_cobble.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_stone.conditions.items[0].items` = "minecraft:stone"
- `criteria.has_stone.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_stone_to_cobble"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_stone"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_stone_to_cobble"]

### `data/compressedfurnace/advancement/recipes/misc/crusher/crushed_wool_to_string.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:crusher/crushed_wool_to_string"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `criteria.minecraft:wool.conditions.items[0].items` = "#minecraft:wool"
- `criteria.minecraft:wool.trigger` = "minecraft:inventory_changed"
- `requirements[0]` = ["has_the_recipe", "minecraft:wool"]
- `rewards.recipes` = ["compressedfurnace:crusher/crushed_wool_to_string"]

### `data/compressedfurnace/advancement/recipes/misc/double_compressed_blast_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_blast_furnace.conditions.items[0].items` = "minecraft:blast_furnace"
- `criteria.has_blast_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_cobbled_deepslate.conditions.items[0].items` = "minecraft:cobbled_deepslate"
- `criteria.has_cobbled_deepslate.trigger` = "minecraft:inventory_changed"
- `criteria.has_cobblestone.conditions.items[0].items` = "minecraft:cobblestone"
- `criteria.has_cobblestone.trigger` = "minecraft:inventory_changed"
- `criteria.has_compressed_blast_furnace.conditions.items[0].items` = "compressedfurnace:compressed_blast_furnace"
- `criteria.has_compressed_blast_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:double_compressed_blast_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_cobblestone", "has_blast_furnace", "has_cobbled_deepslate", "has_compressed_blast_furnace"]
- `rewards.recipes` = ["compressedfurnace:double_compressed_blast_furnace"]

### `data/compressedfurnace/advancement/recipes/misc/double_compressed_crusher.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_cobbled_deepslate.conditions.items[0].items` = "minecraft:cobbled_deepslate"
- `criteria.has_cobbled_deepslate.trigger` = "minecraft:inventory_changed"
- `criteria.has_cobblestone.conditions.items[0].items` = "minecraft:cobblestone"
- `criteria.has_cobblestone.trigger` = "minecraft:inventory_changed"
- `criteria.has_compressed_crusher.conditions.items[0].items` = "compressedfurnace:compressed_crusher"
- `criteria.has_compressed_crusher.trigger` = "minecraft:inventory_changed"
- `criteria.has_flint.conditions.items[0].items` = "minecraft:flint"
- `criteria.has_flint.trigger` = "minecraft:inventory_changed"
- `criteria.has_furnace.conditions.items[0].items` = "minecraft:furnace"
- `criteria.has_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:double_compressed_crusher"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_cobblestone", "has_flint", "has_furnace", "has_cobbled_deepslate", "has_compressed_crusher"]
- `rewards.recipes` = ["compressedfurnace:double_compressed_crusher"]

### `data/compressedfurnace/advancement/recipes/misc/double_compressed_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_cobbled_deepslate.conditions.items[0].items` = "minecraft:cobbled_deepslate"
- `criteria.has_cobbled_deepslate.trigger` = "minecraft:inventory_changed"
- `criteria.has_cobblestone.conditions.items[0].items` = "minecraft:cobblestone"
- `criteria.has_cobblestone.trigger` = "minecraft:inventory_changed"
- `criteria.has_compressed_furnace.conditions.items[0].items` = "compressedfurnace:compressed_furnace"
- `criteria.has_compressed_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_furnace.conditions.items[0].items` = "minecraft:furnace"
- `criteria.has_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:double_compressed_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_cobblestone", "has_furnace", "has_cobbled_deepslate", "has_compressed_furnace"]
- `rewards.recipes` = ["compressedfurnace:double_compressed_furnace"]

### `data/compressedfurnace/advancement/recipes/misc/double_compressed_generator.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_compressed_generator.conditions.items[0].items` = "compressedfurnace:compressed_generator"
- `criteria.has_compressed_generator.trigger` = "minecraft:inventory_changed"
- `criteria.has_gold_block.conditions.items[0].items` = "minecraft:gold_block"
- `criteria.has_gold_block.trigger` = "minecraft:inventory_changed"
- `criteria.has_redstone_block.conditions.items[0].items` = "minecraft:redstone_block"
- `criteria.has_redstone_block.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:double_compressed_generator"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_gold_block", "has_redstone_block", "has_compressed_generator"]
- `rewards.recipes` = ["compressedfurnace:double_compressed_generator"]

### `data/compressedfurnace/advancement/recipes/misc/powered_compressed_blast_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_compressed_blast_furnace.conditions.items[0].items` = "compressedfurnace:compressed_blast_furnace"
- `criteria.has_compressed_blast_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_compressed_generator.conditions.items[0].items` = "compressedfurnace:compressed_generator"
- `criteria.has_compressed_generator.trigger` = "minecraft:inventory_changed"
- `criteria.has_iron_ingot.conditions.items[0].items` = "minecraft:iron_ingot"
- `criteria.has_iron_ingot.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:powered_compressed_blast_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_iron_ingot", "has_compressed_blast_furnace", "has_compressed_generator"]
- `rewards.recipes` = ["compressedfurnace:powered_compressed_blast_furnace"]

### `data/compressedfurnace/advancement/recipes/misc/powered_compressed_crusher.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_compressed_crusher.conditions.items[0].items` = "compressedfurnace:compressed_crusher"
- `criteria.has_compressed_crusher.trigger` = "minecraft:inventory_changed"
- `criteria.has_compressed_generator.conditions.items[0].items` = "compressedfurnace:compressed_generator"
- `criteria.has_compressed_generator.trigger` = "minecraft:inventory_changed"
- `criteria.has_iron_ingot.conditions.items[0].items` = "minecraft:iron_ingot"
- `criteria.has_iron_ingot.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:powered_compressed_crusher"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_iron_ingot", "has_compressed_crusher", "has_compressed_generator"]
- `rewards.recipes` = ["compressedfurnace:powered_compressed_crusher"]

### `data/compressedfurnace/advancement/recipes/misc/powered_compressed_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_compressed_furnace.conditions.items[0].items` = "compressedfurnace:compressed_furnace"
- `criteria.has_compressed_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_compressed_generator.conditions.items[0].items` = "compressedfurnace:compressed_generator"
- `criteria.has_compressed_generator.trigger` = "minecraft:inventory_changed"
- `criteria.has_iron_ingot.conditions.items[0].items` = "minecraft:iron_ingot"
- `criteria.has_iron_ingot.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:powered_compressed_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_iron_ingot", "has_compressed_furnace", "has_compressed_generator"]
- `rewards.recipes` = ["compressedfurnace:powered_compressed_furnace"]

### `data/compressedfurnace/advancement/recipes/misc/powered_double_compressed_blast_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_double_compressed_generator.conditions.items[0].items` = "compressedfurnace:double_compressed_generator"
- `criteria.has_double_compressed_generator.trigger` = "minecraft:inventory_changed"
- `criteria.has_gold_ingot.conditions.items[0].items` = "minecraft:gold_ingot"
- `criteria.has_gold_ingot.trigger` = "minecraft:inventory_changed"
- `criteria.has_powered_compressed_blast_furnace.conditions.items[0].items` = "compressedfurnace:powered_compressed_blast_furnace"
- `criteria.has_powered_compressed_blast_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:powered_double_compressed_blast_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_gold_ingot", "has_powered_compressed_blast_furnace", "has_double_compressed_generator"]
- `rewards.recipes` = ["compressedfurnace:powered_double_compressed_blast_furnace"]

### `data/compressedfurnace/advancement/recipes/misc/powered_double_compressed_crusher.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_double_compressed_generator.conditions.items[0].items` = "compressedfurnace:double_compressed_generator"
- `criteria.has_double_compressed_generator.trigger` = "minecraft:inventory_changed"
- `criteria.has_gold_ingot.conditions.items[0].items` = "minecraft:gold_ingot"
- `criteria.has_gold_ingot.trigger` = "minecraft:inventory_changed"
- `criteria.has_powered_compressed_crusher.conditions.items[0].items` = "compressedfurnace:powered_compressed_crusher"
- `criteria.has_powered_compressed_crusher.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:powered_double_compressed_crusher"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_gold_ingot", "has_powered_compressed_crusher", "has_double_compressed_generator"]
- `rewards.recipes` = ["compressedfurnace:powered_double_compressed_crusher"]

### `data/compressedfurnace/advancement/recipes/misc/powered_double_compressed_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_double_compressed_generator.conditions.items[0].items` = "compressedfurnace:double_compressed_generator"
- `criteria.has_double_compressed_generator.trigger` = "minecraft:inventory_changed"
- `criteria.has_gold_ingot.conditions.items[0].items` = "minecraft:gold_ingot"
- `criteria.has_gold_ingot.trigger` = "minecraft:inventory_changed"
- `criteria.has_powered_compressed_furnace.conditions.items[0].items` = "compressedfurnace:powered_compressed_furnace"
- `criteria.has_powered_compressed_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:powered_double_compressed_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_gold_ingot", "has_powered_compressed_furnace", "has_double_compressed_generator"]
- `rewards.recipes` = ["compressedfurnace:powered_double_compressed_furnace"]

### `data/compressedfurnace/advancement/recipes/misc/powered_triple_compressed_blast_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_diamond.conditions.items[0].items` = "minecraft:diamond"
- `criteria.has_diamond.trigger` = "minecraft:inventory_changed"
- `criteria.has_powered_double_compressed_blast_furnace.conditions.items[0].items` = "compressedfurnace:powered_double_compressed_blast_furnace"
- `criteria.has_powered_double_compressed_blast_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:powered_triple_compressed_blast_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `criteria.has_triple_compressed_generator.conditions.items[0].items` = "compressedfurnace:triple_compressed_generator"
- `criteria.has_triple_compressed_generator.trigger` = "minecraft:inventory_changed"
- `requirements[0]` = ["has_the_recipe", "has_diamond", "has_powered_double_compressed_blast_furnace", "has_triple_compressed_generator"]
- `rewards.recipes` = ["compressedfurnace:powered_triple_compressed_blast_furnace"]

### `data/compressedfurnace/advancement/recipes/misc/powered_triple_compressed_crusher.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_diamond.conditions.items[0].items` = "minecraft:diamond"
- `criteria.has_diamond.trigger` = "minecraft:inventory_changed"
- `criteria.has_powered_double_compressed_crusher.conditions.items[0].items` = "compressedfurnace:powered_double_compressed_crusher"
- `criteria.has_powered_double_compressed_crusher.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:powered_triple_compressed_crusher"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `criteria.has_triple_compressed_generator.conditions.items[0].items` = "compressedfurnace:triple_compressed_generator"
- `criteria.has_triple_compressed_generator.trigger` = "minecraft:inventory_changed"
- `requirements[0]` = ["has_the_recipe", "has_diamond", "has_powered_double_compressed_crusher", "has_triple_compressed_generator"]
- `rewards.recipes` = ["compressedfurnace:powered_triple_compressed_crusher"]

### `data/compressedfurnace/advancement/recipes/misc/powered_triple_compressed_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_diamond.conditions.items[0].items` = "minecraft:diamond"
- `criteria.has_diamond.trigger` = "minecraft:inventory_changed"
- `criteria.has_powered_double_compressed_furnace.conditions.items[0].items` = "compressedfurnace:powered_double_compressed_furnace"
- `criteria.has_powered_double_compressed_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:powered_triple_compressed_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `criteria.has_triple_compressed_generator.conditions.items[0].items` = "compressedfurnace:triple_compressed_generator"
- `criteria.has_triple_compressed_generator.trigger` = "minecraft:inventory_changed"
- `requirements[0]` = ["has_the_recipe", "has_diamond", "has_powered_double_compressed_furnace", "has_triple_compressed_generator"]
- `rewards.recipes` = ["compressedfurnace:powered_triple_compressed_furnace"]

### `data/compressedfurnace/advancement/recipes/misc/smelting/has_raw_scrap_to_has_netherite_scrap.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_raw_scrap.conditions.items[0].items` = "compressedfurnace:raw_scrap"
- `criteria.has_raw_scrap.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:smelting/has_raw_scrap_to_has_netherite_scrap"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_raw_scrap"]
- `rewards.recipes` = ["compressedfurnace:smelting/has_raw_scrap_to_has_netherite_scrap"]

### `data/compressedfurnace/advancement/recipes/misc/triple_compressed_blast_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_blast_furnace.conditions.items[0].items` = "minecraft:blast_furnace"
- `criteria.has_blast_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_cobbled_deepslate.conditions.items[0].items` = "minecraft:cobbled_deepslate"
- `criteria.has_cobbled_deepslate.trigger` = "minecraft:inventory_changed"
- `criteria.has_cobblestone.conditions.items[0].items` = "minecraft:cobblestone"
- `criteria.has_cobblestone.trigger` = "minecraft:inventory_changed"
- `criteria.has_double_compressed_blast_furnace.conditions.items[0].items` = "compressedfurnace:double_compressed_blast_furnace"
- `criteria.has_double_compressed_blast_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:triple_compressed_blast_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_cobbled_deepslate", "has_cobblestone", "has_blast_furnace", "has_double_compressed_blast_furnace"]
- `rewards.recipes` = ["compressedfurnace:triple_compressed_blast_furnace"]

### `data/compressedfurnace/advancement/recipes/misc/triple_compressed_crusher.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_cobbled_deepslate.conditions.items[0].items` = "minecraft:cobbled_deepslate"
- `criteria.has_cobbled_deepslate.trigger` = "minecraft:inventory_changed"
- `criteria.has_double_compressed_crusher.conditions.items[0].items` = "compressedfurnace:double_compressed_crusher"
- `criteria.has_double_compressed_crusher.trigger` = "minecraft:inventory_changed"
- `criteria.has_flint.conditions.items[0].items` = "minecraft:flint"
- `criteria.has_flint.trigger` = "minecraft:inventory_changed"
- `criteria.has_furnace.conditions.items[0].items` = "minecraft:furnace"
- `criteria.has_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:triple_compressed_crusher"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_cobbled_deepslate", "has_flint", "has_furnace", "has_double_compressed_crusher"]
- `rewards.recipes` = ["compressedfurnace:triple_compressed_crusher"]

### `data/compressedfurnace/advancement/recipes/misc/triple_compressed_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_cobbled_deepslate.conditions.items[0].items` = "minecraft:cobbled_deepslate"
- `criteria.has_cobbled_deepslate.trigger` = "minecraft:inventory_changed"
- `criteria.has_cobblestone.conditions.items[0].items` = "minecraft:cobblestone"
- `criteria.has_cobblestone.trigger` = "minecraft:inventory_changed"
- `criteria.has_double_compressed_furnace.conditions.items[0].items` = "compressedfurnace:double_compressed_furnace"
- `criteria.has_double_compressed_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_furnace.conditions.items[0].items` = "minecraft:furnace"
- `criteria.has_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:triple_compressed_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_cobbled_deepslate", "has_cobblestone", "has_furnace", "has_double_compressed_furnace"]
- `rewards.recipes` = ["compressedfurnace:triple_compressed_furnace"]

### `data/compressedfurnace/advancement/recipes/misc/triple_compressed_generator.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_diamond.conditions.items[0].items` = "minecraft:diamond"
- `criteria.has_diamond.trigger` = "minecraft:inventory_changed"
- `criteria.has_double_compressed_generator.conditions.items[0].items` = "compressedfurnace:double_compressed_generator"
- `criteria.has_double_compressed_generator.trigger` = "minecraft:inventory_changed"
- `criteria.has_gold_block.conditions.items[0].items` = "minecraft:gold_block"
- `criteria.has_gold_block.trigger` = "minecraft:inventory_changed"
- `criteria.has_redstone_block.conditions.items[0].items` = "minecraft:redstone_block"
- `criteria.has_redstone_block.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "compressedfurnace:triple_compressed_generator"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_gold_block", "has_redstone_block", "has_diamond", "has_double_compressed_generator"]
- `rewards.recipes` = ["compressedfurnace:triple_compressed_generator"]

### `data/compressedfurnace/recipe/blasting/has_raw_copper_block_to_has_copper_block.json`

- `type` = "minecraft:blasting"
- `category` = "blocks"
- `cookingtime` = 100
- `experience` = 2.0
- `ingredient.item` = "minecraft:raw_copper_block"
- `result.count` = 1
- `result.id` = "minecraft:copper_block"

### `data/compressedfurnace/recipe/blasting/has_raw_gold_block_to_has_gold_block.json`

- `type` = "minecraft:blasting"
- `category` = "blocks"
- `cookingtime` = 100
- `experience` = 2.0
- `ingredient.item` = "minecraft:raw_gold_block"
- `result.count` = 1
- `result.id` = "minecraft:gold_block"

### `data/compressedfurnace/recipe/blasting/has_raw_iron_block_to_has_iron_block.json`

- `type` = "minecraft:blasting"
- `category` = "blocks"
- `cookingtime` = 100
- `experience` = 2.0
- `ingredient.item` = "minecraft:raw_iron_block"
- `result.count` = 1
- `result.id` = "minecraft:iron_block"

### `data/compressedfurnace/recipe/blasting/has_raw_scrap_to_has_netherite_scrap.json`

- `type` = "minecraft:blasting"
- `category` = "misc"
- `cookingtime` = 100
- `experience` = 2.0
- `ingredient.item` = "compressedfurnace:raw_scrap"
- `result.count` = 1
- `result.id` = "minecraft:netherite_scrap"

### `data/compressedfurnace/recipe/compressed_blast_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.A.item` = "minecraft:cobblestone"
- `key.B.item` = "minecraft:cobblestone"
- `key.C.item` = "minecraft:blast_furnace"
- `key.D.item` = "minecraft:cobblestone"
- `key.E.item` = "minecraft:cobblestone"
- `pattern` = ["ABA", "CEC", "DBD"]
- `result.count` = 1
- `result.id` = "compressedfurnace:compressed_blast_furnace"

### `data/compressedfurnace/recipe/compressed_crusher.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.A.item` = "minecraft:cobblestone"
- `key.B.item` = "minecraft:flint"
- `key.C.item` = "minecraft:iron_ingot"
- `key.D.item` = "minecraft:cobblestone"
- `key.E.item` = "compressedfurnace:compressed_furnace"
- `pattern` = ["ABA", "CEC", "DBD"]
- `result.count` = 1
- `result.id` = "compressedfurnace:compressed_crusher"

### `data/compressedfurnace/recipe/compressed_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.A.item` = "minecraft:cobblestone"
- `key.B.item` = "minecraft:cobblestone"
- `key.C.item` = "minecraft:furnace"
- `key.D.item` = "minecraft:cobblestone"
- `key.E.item` = "minecraft:cobblestone"
- `pattern` = ["ABA", "CEC", "DBD"]
- `result.count` = 1
- `result.id` = "compressedfurnace:compressed_furnace"

### `data/compressedfurnace/recipe/compressed_generator.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.D.item` = "minecraft:gold_ingot"
- `key.F.item` = "compressedfurnace:compressed_furnace"
- `key.G.item` = "minecraft:gold_ingot"
- `key.R.item` = "minecraft:redstone"
- `pattern` = ["GDG", "RFR", "GDG"]
- `result.count` = 1
- `result.id` = "compressedfurnace:compressed_generator"

### `data/compressedfurnace/recipe/crusher/ae2/ae_silicon.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "ae2"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.tag` = "minecraft:sand"
- `result.count` = 1
- `result.id` = "ae2:silicon"

### `data/compressedfurnace/recipe/crusher/ae2/certus_dust.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "ae2"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "ae2:certus_quartz_crystal"
- `result.count` = 1
- `result.id` = "ae2:certus_quartz_dust"

### `data/compressedfurnace/recipe/crusher/ae2/charged_certus_dust.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "ae2"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "ae2:charged_certus_quartz_crystal"
- `result.count` = 1
- `result.id` = "ae2:certus_quartz_dust"

### `data/compressedfurnace/recipe/crusher/ae2/ender_dust.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "ae2"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:ender_pearl"
- `result.count` = 1
- `result.id` = "ae2:ender_dust"

### `data/compressedfurnace/recipe/crusher/ae2/fluix_dust.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "ae2"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "ae2:fluix_crystal"
- `result.count` = 1
- `result.id` = "ae2:fluix_dust"

### `data/compressedfurnace/recipe/crusher/ae2/sky_dust.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "ae2"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "ae2:sky_stone_block"
- `result.count` = 1
- `result.id` = "ae2:sky_dust"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_basalt_aluminum.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:basalt_aluminum_ore"
- `result.count` = 2
- `result.id` = "bno:raw_aluminum"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_basalt_coal.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:basalt_coal_ore"
- `result.count` = 2
- `result.id` = "minecraft:coal"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_basalt_copper.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:basalt_copper_ore"
- `result.count` = 2
- `result.id` = "minecraft:raw_copper"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_basalt_iron.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:basalt_iron_ore"
- `result.count` = 2
- `result.id` = "minecraft:raw_iron"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_basalt_lead.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `neoforge:conditions[1].type` = "neoforge:mod_loaded"
- `neoforge:conditions[1].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:basalt_lead_ore"
- `result.count` = 2
- `result.id` = "mekanism:raw_lead"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_basalt_nickel.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:basalt_nickel_ore"
- `result.count` = 2
- `result.id` = "bno:raw_nickel"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_basalt_osmium.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `neoforge:conditions[1].type` = "neoforge:mod_loaded"
- `neoforge:conditions[1].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:basalt_osmium_ore"
- `result.count` = 2
- `result.id` = "mekanism:raw_osmium"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_basalt_silver.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:basalt_silver_ore"
- `result.count` = 2
- `result.id` = "bno:raw_silver"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_basalt_tin.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `neoforge:conditions[1].type` = "neoforge:mod_loaded"
- `neoforge:conditions[1].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:basalt_tin_ore"
- `result.count` = 2
- `result.id` = "mekanism:raw_tin"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_basalt_uranium.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `neoforge:conditions[1].type` = "neoforge:mod_loaded"
- `neoforge:conditions[1].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:basalt_uranium_ore"
- `result.count` = 2
- `result.id` = "mekanism:raw_uranium"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_basalt_zinc.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:basalt_zinc_ore"
- `result.count` = 2
- `result.id` = "bno:raw_zinc"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_nether_aluminum.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:nether_aluminum_ore"
- `result.count` = 2
- `result.id` = "bno:raw_aluminum"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_nether_coal.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:nether_coal_ore"
- `result.count` = 2
- `result.id` = "minecraft:coal"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_nether_copper.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:nether_copper_ore"
- `result.count` = 2
- `result.id` = "minecraft:raw_copper"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_nether_iron.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:nether_iron_ore"
- `result.count` = 2
- `result.id` = "minecraft:raw_iron"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_nether_lead.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `neoforge:conditions[1].type` = "neoforge:mod_loaded"
- `neoforge:conditions[1].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:nether_lead_ore"
- `result.count` = 2
- `result.id` = "mekanism:raw_lead"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_nether_nickel.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:nether_nickel_ore"
- `result.count` = 2
- `result.id` = "bno:raw_nickel"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_nether_osmium.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `neoforge:conditions[1].type` = "neoforge:mod_loaded"
- `neoforge:conditions[1].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:nether_osmium_ore"
- `result.count` = 2
- `result.id` = "mekanism:raw_osmium"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_nether_silver.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:nether_silver_ore"
- `result.count` = 2
- `result.id` = "bno:raw_silver"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_nether_tin.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `neoforge:conditions[1].type` = "neoforge:mod_loaded"
- `neoforge:conditions[1].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:nether_tin_ore"
- `result.count` = 2
- `result.id` = "mekanism:raw_tin"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_nether_uranium.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `neoforge:conditions[1].type` = "neoforge:mod_loaded"
- `neoforge:conditions[1].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:nether_uranium_ore"
- `result.count` = 2
- `result.id` = "mekanism:raw_uranium"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_nether_zinc.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:nether_zinc_ore"
- `result.count` = 2
- `result.id` = "bno:raw_zinc"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_soul_aluminum.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:soul_aluminum_ore"
- `result.count` = 2
- `result.id` = "bno:raw_aluminum"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_soul_coal.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:soul_coal_ore"
- `result.count` = 2
- `result.id` = "minecraft:coal"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_soul_copper.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:soul_copper_ore"
- `result.count` = 2
- `result.id` = "minecraft:raw_copper"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_soul_iron.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:soul_iron_ore"
- `result.count` = 2
- `result.id` = "minecraft:raw_iron"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_soul_lead.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `neoforge:conditions[1].type` = "neoforge:mod_loaded"
- `neoforge:conditions[1].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:soul_lead_ore"
- `result.count` = 2
- `result.id` = "mekanism:raw_lead"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_soul_nickel.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:soul_nickel_ore"
- `result.count` = 2
- `result.id` = "bno:raw_nickel"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_soul_osmium.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `neoforge:conditions[1].type` = "neoforge:mod_loaded"
- `neoforge:conditions[1].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:soul_osmium_ore"
- `result.count` = 2
- `result.id` = "mekanism:raw_osmium"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_soul_silver.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:soul_silver_ore"
- `result.count` = 2
- `result.id` = "bno:raw_silver"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_soul_tin.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `neoforge:conditions[1].type` = "neoforge:mod_loaded"
- `neoforge:conditions[1].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:soul_tin_ore"
- `result.count` = 2
- `result.id` = "mekanism:raw_tin"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_soul_uranium.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `neoforge:conditions[1].type` = "neoforge:mod_loaded"
- `neoforge:conditions[1].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:soul_uranium_ore"
- `result.count` = 2
- `result.id` = "mekanism:raw_uranium"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crushed_soul_zinc.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:soul_zinc_ore"
- `result.count` = 2
- `result.id` = "bno:raw_zinc"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crusher_basalt_diamond.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:basalt_diamond_ore"
- `result.count` = 2
- `result.id` = "minecraft:diamond"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crusher_basalt_emerald.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:basalt_emerald_ore"
- `result.count` = 2
- `result.id` = "minecraft:emerald"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crusher_basalt_lapis.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:basalt_lapis_ore"
- `result.count` = 2
- `result.id` = "minecraft:lapis_lazuli"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crusher_basalt_redstone.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:basalt_redstone_ore"
- `result.count` = 2
- `result.id` = "minecraft:redstone"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crusher_nether_diamond.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:nether_diamond_ore"
- `result.count` = 2
- `result.id` = "minecraft:diamond"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crusher_nether_emerald.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:nether_emerald_ore"
- `result.count` = 2
- `result.id` = "minecraft:emerald"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crusher_nether_lapis.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:nether_lapis_ore"
- `result.count` = 2
- `result.id` = "minecraft:lapis_lazuli"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crusher_nether_redstone.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:nether_redstone_ore"
- `result.count` = 2
- `result.id` = "minecraft:redstone"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crusher_soul_diamond.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:soul_diamond_ore"
- `result.count` = 2
- `result.id` = "minecraft:diamond"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crusher_soul_emerald.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:soul_emerald_ore"
- `result.count` = 2
- `result.id` = "minecraft:emerald"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crusher_soul_lapis.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:soul_lapis_ore"
- `result.count` = 2
- `result.id` = "minecraft:lapis_lazuli"

### `data/compressedfurnace/recipe/crusher/basic_nether_ores/crusher_soul_redstone.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bno"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bno:soul_redstone_ore"
- `result.count` = 2
- `result.id` = "minecraft:redstone"

### `data/compressedfurnace/recipe/crusher/crushed_ancient_debris.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:ancient_debris"
- `result.count` = 2
- `result.id` = "compressedfurnace:raw_scrap"

### `data/compressedfurnace/recipe/crusher/crushed_andesite_to_gravel.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:andesite"
- `result.count` = 1
- `result.id` = "minecraft:gravel"

### `data/compressedfurnace/recipe/crusher/crushed_blaze_rod.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:blaze_rod"
- `result.count` = 4
- `result.id` = "minecraft:blaze_powder"

### `data/compressedfurnace/recipe/crusher/crushed_coal.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:coal_ore"
- `result.count` = 2
- `result.id` = "minecraft:coal"

### `data/compressedfurnace/recipe/crusher/crushed_cobbled_to_gravel.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:cobbled_deepslate"
- `result.count` = 1
- `result.id` = "minecraft:gravel"

### `data/compressedfurnace/recipe/crusher/crushed_cobble_to_gravel.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:cobblestone"
- `result.count` = 1
- `result.id` = "minecraft:gravel"

### `data/compressedfurnace/recipe/crusher/crushed_copper.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:copper_ore"
- `result.count` = 2
- `result.id` = "minecraft:raw_copper"

### `data/compressedfurnace/recipe/crusher/crushed_deepslate_coal.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:deepslate_coal_ore"
- `result.count` = 2
- `result.id` = "minecraft:coal"

### `data/compressedfurnace/recipe/crusher/crushed_deepslate_copper.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:deepslate_copper_ore"
- `result.count` = 2
- `result.id` = "minecraft:raw_copper"

### `data/compressedfurnace/recipe/crusher/crushed_deepslate_diamond.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:deepslate_diamond_ore"
- `result.count` = 2
- `result.id` = "minecraft:diamond"

### `data/compressedfurnace/recipe/crusher/crushed_deepslate_emerald.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:deepslate_emerald_ore"
- `result.count` = 2
- `result.id` = "minecraft:emerald"

### `data/compressedfurnace/recipe/crusher/crushed_deepslate_gold.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:deepslate_gold_ore"
- `result.count` = 2
- `result.id` = "minecraft:raw_gold"

### `data/compressedfurnace/recipe/crusher/crushed_deepslate_iron.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:deepslate_iron_ore"
- `result.count` = 2
- `result.id` = "minecraft:raw_iron"

### `data/compressedfurnace/recipe/crusher/crushed_deepslate_lapis.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:deepslate_lapis_ore"
- `result.count` = 2
- `result.id` = "minecraft:lapis_lazuli"

### `data/compressedfurnace/recipe/crusher/crushed_deepslate_redstone.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:deepslate_redstone_ore"
- `result.count` = 2
- `result.id` = "minecraft:redstone"

### `data/compressedfurnace/recipe/crusher/crushed_deepslate_to_cobbled.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:deepslate"
- `result.count` = 1
- `result.id` = "minecraft:cobbled_deepslate"

### `data/compressedfurnace/recipe/crusher/crushed_diamond.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:diamond_ore"
- `result.count` = 2
- `result.id` = "minecraft:diamond"

### `data/compressedfurnace/recipe/crusher/crushed_diorite_to_gravel.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:diorite"
- `result.count` = 1
- `result.id` = "minecraft:gravel"

### `data/compressedfurnace/recipe/crusher/crushed_dripstone_to_pointed_dripstone.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:dripstone_block"
- `result.count` = 4
- `result.id` = "minecraft:pointed_dripstone"

### `data/compressedfurnace/recipe/crusher/crushed_emerald.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:emerald_ore"
- `result.count` = 2
- `result.id` = "minecraft:emerald"

### `data/compressedfurnace/recipe/crusher/crushed_gold.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:gold_ore"
- `result.count` = 2
- `result.id` = "minecraft:raw_gold"

### `data/compressedfurnace/recipe/crusher/crushed_granite_to_gravel.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:granite"
- `result.count` = 1
- `result.id` = "minecraft:gravel"

### `data/compressedfurnace/recipe/crusher/crushed_gravel_to_sand.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:gravel"
- `result.count` = 1
- `result.id` = "minecraft:sand"

### `data/compressedfurnace/recipe/crusher/crushed_honeycomb_block_to_honeycomb.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:honeycomb_block"
- `result.count` = 4
- `result.id` = "minecraft:honeycomb"

### `data/compressedfurnace/recipe/crusher/crushed_iron.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:iron_ore"
- `result.count` = 2
- `result.id` = "minecraft:raw_iron"

### `data/compressedfurnace/recipe/crusher/crushed_lapis.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:lapis_ore"
- `result.count` = 4
- `result.id` = "minecraft:lapis_lazuli"

### `data/compressedfurnace/recipe/crusher/crushed_nether_gold.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:nether_gold_ore"
- `result.count` = 2
- `result.id` = "minecraft:raw_gold"

### `data/compressedfurnace/recipe/crusher/crushed_prismarine_bricks_to_prismarine_shard.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:prismarine_bricks"
- `result.count` = 9
- `result.id` = "minecraft:prismarine_shard"

### `data/compressedfurnace/recipe/crusher/crushed_prismarine_brick_stairs_to_prismarine_shard.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:prismarine_brick_stairs"
- `result.count` = 5
- `result.id` = "minecraft:prismarine_shard"

### `data/compressedfurnace/recipe/crusher/crushed_prismarine_slab_to_prismarine_shard.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:prismarine_slab"
- `result.count` = 3
- `result.id` = "minecraft:prismarine_shard"

### `data/compressedfurnace/recipe/crusher/crushed_prismarine_stairs_to_prismarine_shard.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:prismarine_stairs"
- `result.count` = 4
- `result.id` = "minecraft:prismarine_shard"

### `data/compressedfurnace/recipe/crusher/crushed_quartz.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:nether_quartz_ore"
- `result.count` = 4
- `result.id` = "minecraft:quartz"

### `data/compressedfurnace/recipe/crusher/crushed_quartz_block.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:quartz_block"
- `result.count` = 4
- `result.id` = "minecraft:quartz"

### `data/compressedfurnace/recipe/crusher/crushed_redstone.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:redstone_ore"
- `result.count` = 4
- `result.id` = "minecraft:redstone"

### `data/compressedfurnace/recipe/crusher/crushed_sandstone_to_sand.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:sandstone"
- `result.count` = 1
- `result.id` = "minecraft:sand"

### `data/compressedfurnace/recipe/crusher/crushed_stone_to_cobble.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "minecraft:stone"
- `result.count` = 1
- `result.id` = "minecraft:cobblestone"

### `data/compressedfurnace/recipe/crusher/crushed_wool_to_string.json`

- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.tag` = "minecraft:wool"
- `result.count` = 4
- `result.id` = "minecraft:string"

### `data/compressedfurnace/recipe/crusher/extream_reactor/crushed_deepslate_yellorite.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bigreactors"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bigreactors:deepslate_yellorite_ore"
- `result.count` = 3
- `result.id` = "bigreactors:raw_yellorium"

### `data/compressedfurnace/recipe/crusher/extream_reactor/crushed_yellorite.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "bigreactors"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "bigreactors:yellorite_ore"
- `result.count` = 3
- `result.id` = "bigreactors:raw_yellorium"

### `data/compressedfurnace/recipe/crusher/mekanism/crushed_mek_deepslate_fluorite.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "mekanism:deepslate_fluorite_ore"
- `result.count` = 6
- `result.id` = "mekanism:fluorite_gem"

### `data/compressedfurnace/recipe/crusher/mekanism/crushed_mek_deepslate_lead.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "mekanism:deepslate_lead_ore"
- `result.count` = 2
- `result.id` = "mekanism:raw_lead"

### `data/compressedfurnace/recipe/crusher/mekanism/crushed_mek_deepslate_osmium.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "mekanism:deepslate_osmium_ore"
- `result.count` = 2
- `result.id` = "mekanism:raw_osmium"

### `data/compressedfurnace/recipe/crusher/mekanism/crushed_mek_deepslate_tin.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "mekanism:deepslate_tin_ore"
- `result.count` = 2
- `result.id` = "mekanism:raw_tin"

### `data/compressedfurnace/recipe/crusher/mekanism/crushed_mek_deepslate_uranium.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "mekanism:deepslate_uranium_ore"
- `result.count` = 2
- `result.id` = "mekanism:raw_uranium"

### `data/compressedfurnace/recipe/crusher/mekanism/crushed_mek_fluorite.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "mekanism:fluorite_ore"
- `result.count` = 6
- `result.id` = "mekanism:fluorite_gem"

### `data/compressedfurnace/recipe/crusher/mekanism/crushed_mek_fluorite_dust.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "mekanism:fluorite_gem"
- `result.count` = 1
- `result.id` = "mekanism:dust_fluorite"

### `data/compressedfurnace/recipe/crusher/mekanism/crushed_mek_lead.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "mekanism:lead_ore"
- `result.count` = 2
- `result.id` = "mekanism:raw_lead"

### `data/compressedfurnace/recipe/crusher/mekanism/crushed_mek_osmium.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "mekanism:osmium_ore"
- `result.count` = 2
- `result.id` = "mekanism:raw_osmium"

### `data/compressedfurnace/recipe/crusher/mekanism/crushed_mek_tin.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "mekanism:tin_ore"
- `result.count` = 2
- `result.id` = "mekanism:raw_tin"

### `data/compressedfurnace/recipe/crusher/mekanism/crushed_mek_uranium.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "mekanism"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "mekanism:uranium_ore"
- `result.count` = 2
- `result.id` = "mekanism:raw_uranium"

### `data/compressedfurnace/recipe/crusher/mystical_agradditions/crusher_deepslate_inferion.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "mysticalagriculture"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "mysticalagriculture:deepslate_inferium_ore"
- `result.count` = 4
- `result.id` = "mysticalagriculture:inferium_essence"

### `data/compressedfurnace/recipe/crusher/mystical_agradditions/crusher_deepslate_prosperity.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "mysticalagriculture"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "mysticalagriculture:deepslate_prosperity_ore"
- `result.count` = 3
- `result.id` = "mysticalagriculture:prosperity_shard"

### `data/compressedfurnace/recipe/crusher/mystical_agradditions/crusher_end_inferion.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "mysticalagriculture"
- `neoforge:conditions[1].type` = "neoforge:mod_loaded"
- `neoforge:conditions[1].modid` = "mysticalagradditions"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "mysticalagradditions:end_inferium_ore"
- `result.count` = 4
- `result.id` = "mysticalagriculture:inferium_essence"

### `data/compressedfurnace/recipe/crusher/mystical_agradditions/crusher_end_prosperity.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "mysticalagriculture"
- `neoforge:conditions[1].type` = "neoforge:mod_loaded"
- `neoforge:conditions[1].modid` = "mysticalagradditions"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "mysticalagradditions:end_prosperity_ore"
- `result.count` = 3
- `result.id` = "mysticalagriculture:prosperity_shard"

### `data/compressedfurnace/recipe/crusher/mystical_agradditions/crusher_inferion.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "mysticalagriculture"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "mysticalagriculture:inferium_ore"
- `result.count` = 4
- `result.id` = "mysticalagriculture:inferium_essence"

### `data/compressedfurnace/recipe/crusher/mystical_agradditions/crusher_nether_inferion.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "mysticalagriculture"
- `neoforge:conditions[1].type` = "neoforge:mod_loaded"
- `neoforge:conditions[1].modid` = "mysticalagradditions"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "mysticalagradditions:nether_inferium_ore"
- `result.count` = 4
- `result.id` = "mysticalagriculture:inferium_essence"

### `data/compressedfurnace/recipe/crusher/mystical_agradditions/crusher_nether_prosperity.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "mysticalagriculture"
- `neoforge:conditions[1].type` = "neoforge:mod_loaded"
- `neoforge:conditions[1].modid` = "mysticalagradditions"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "mysticalagradditions:nether_prosperity_ore"
- `result.count` = 3
- `result.id` = "mysticalagriculture:prosperity_shard"

### `data/compressedfurnace/recipe/crusher/mystical_agradditions/crusher_prosperity.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "mysticalagriculture"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "mysticalagriculture:prosperity_ore"
- `result.count` = 3
- `result.id` = "mysticalagriculture:prosperity_shard"

### `data/compressedfurnace/recipe/crusher/mystical_agradditions/crusher_soulium.json`

- `neoforge:conditions[0].type` = "neoforge:mod_loaded"
- `neoforge:conditions[0].modid` = "mysticalagriculture"
- `type` = "compressedfurnace:crusher"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `group` = "crusher"
- `ingredient.item` = "mysticalagriculture:soulium_ore"
- `result.count` = 4
- `result.id` = "mysticalagriculture:soulium_dust"

### `data/compressedfurnace/recipe/double_compressed_blast_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.A.item` = "minecraft:cobblestone"
- `key.B.item` = "minecraft:cobblestone"
- `key.C.item` = "minecraft:blast_furnace"
- `key.D.item` = "minecraft:cobbled_deepslate"
- `key.E.item` = "compressedfurnace:compressed_blast_furnace"
- `pattern` = ["ABA", "CEC", "DBD"]
- `result.count` = 1
- `result.id` = "compressedfurnace:double_compressed_blast_furnace"

### `data/compressedfurnace/recipe/double_compressed_crusher.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.A.item` = "minecraft:cobblestone"
- `key.B.item` = "minecraft:flint"
- `key.C.item` = "minecraft:furnace"
- `key.D.item` = "minecraft:cobbled_deepslate"
- `key.E.item` = "compressedfurnace:compressed_crusher"
- `pattern` = ["ABA", "CEC", "DBD"]
- `result.count` = 1
- `result.id` = "compressedfurnace:double_compressed_crusher"

### `data/compressedfurnace/recipe/double_compressed_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.A.item` = "minecraft:cobblestone"
- `key.B.item` = "minecraft:cobblestone"
- `key.C.item` = "minecraft:furnace"
- `key.D.item` = "minecraft:cobbled_deepslate"
- `key.E.item` = "compressedfurnace:compressed_furnace"
- `pattern` = ["ABA", "CEC", "DBD"]
- `result.count` = 1
- `result.id` = "compressedfurnace:double_compressed_furnace"

### `data/compressedfurnace/recipe/double_compressed_generator.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.D.item` = "minecraft:gold_block"
- `key.F.item` = "compressedfurnace:compressed_generator"
- `key.G.item` = "minecraft:gold_block"
- `key.R.item` = "minecraft:redstone_block"
- `pattern` = ["GDG", "RFR", "GDG"]
- `result.count` = 1
- `result.id` = "compressedfurnace:double_compressed_generator"

### `data/compressedfurnace/recipe/powered_compressed_blast_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.G.item` = "compressedfurnace:compressed_generator"
- `key.I.item` = "minecraft:iron_ingot"
- `key.X.item` = "compressedfurnace:compressed_blast_furnace"
- `pattern` = ["III", "GXG", "III"]
- `result.count` = 1
- `result.id` = "compressedfurnace:powered_compressed_blast_furnace"

### `data/compressedfurnace/recipe/powered_compressed_crusher.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.G.item` = "compressedfurnace:compressed_generator"
- `key.I.item` = "minecraft:iron_ingot"
- `key.X.item` = "compressedfurnace:compressed_crusher"
- `pattern` = ["III", "GXG", "III"]
- `result.count` = 1
- `result.id` = "compressedfurnace:powered_compressed_crusher"

### `data/compressedfurnace/recipe/powered_compressed_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.G.item` = "compressedfurnace:compressed_generator"
- `key.I.item` = "minecraft:iron_ingot"
- `key.X.item` = "compressedfurnace:compressed_furnace"
- `pattern` = ["III", "GXG", "III"]
- `result.count` = 1
- `result.id` = "compressedfurnace:powered_compressed_furnace"

### `data/compressedfurnace/recipe/powered_double_compressed_blast_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.G.item` = "compressedfurnace:double_compressed_generator"
- `key.I.item` = "minecraft:gold_ingot"
- `key.X.item` = "compressedfurnace:powered_compressed_blast_furnace"
- `pattern` = ["III", "GXG", "III"]
- `result.count` = 1
- `result.id` = "compressedfurnace:powered_double_compressed_blast_furnace"

### `data/compressedfurnace/recipe/powered_double_compressed_crusher.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.G.item` = "compressedfurnace:double_compressed_generator"
- `key.I.item` = "minecraft:gold_ingot"
- `key.X.item` = "compressedfurnace:powered_compressed_crusher"
- `pattern` = ["III", "GXG", "III"]
- `result.count` = 1
- `result.id` = "compressedfurnace:powered_double_compressed_crusher"

### `data/compressedfurnace/recipe/powered_double_compressed_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.G.item` = "compressedfurnace:double_compressed_generator"
- `key.I.item` = "minecraft:gold_ingot"
- `key.X.item` = "compressedfurnace:powered_compressed_furnace"
- `pattern` = ["III", "GXG", "III"]
- `result.count` = 1
- `result.id` = "compressedfurnace:powered_double_compressed_furnace"

### `data/compressedfurnace/recipe/powered_triple_compressed_blast_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.G.item` = "compressedfurnace:triple_compressed_generator"
- `key.I.item` = "minecraft:diamond"
- `key.X.item` = "compressedfurnace:powered_double_compressed_blast_furnace"
- `pattern` = ["III", "GXG", "III"]
- `result.count` = 1
- `result.id` = "compressedfurnace:powered_triple_compressed_blast_furnace"

### `data/compressedfurnace/recipe/powered_triple_compressed_crusher.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.G.item` = "compressedfurnace:triple_compressed_generator"
- `key.I.item` = "minecraft:diamond"
- `key.X.item` = "compressedfurnace:powered_double_compressed_crusher"
- `pattern` = ["III", "GXG", "III"]
- `result.count` = 1
- `result.id` = "compressedfurnace:powered_triple_compressed_crusher"

### `data/compressedfurnace/recipe/powered_triple_compressed_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.G.item` = "compressedfurnace:triple_compressed_generator"
- `key.I.item` = "minecraft:diamond"
- `key.X.item` = "compressedfurnace:powered_double_compressed_furnace"
- `pattern` = ["III", "GXG", "III"]
- `result.count` = 1
- `result.id` = "compressedfurnace:powered_triple_compressed_furnace"

### `data/compressedfurnace/recipe/smelting/has_raw_copper_block_to_has_copper_block.json`

- `type` = "minecraft:smelting"
- `category` = "blocks"
- `cookingtime` = 200
- `experience` = 2.0
- `ingredient.item` = "minecraft:raw_copper_block"
- `result.count` = 1
- `result.id` = "minecraft:copper_block"

### `data/compressedfurnace/recipe/smelting/has_raw_gold_block_to_has_gold_block.json`

- `type` = "minecraft:smelting"
- `category` = "blocks"
- `cookingtime` = 200
- `experience` = 2.0
- `ingredient.item` = "minecraft:raw_gold_block"
- `result.count` = 1
- `result.id` = "minecraft:gold_block"

### `data/compressedfurnace/recipe/smelting/has_raw_iron_block_to_has_iron_block.json`

- `type` = "minecraft:smelting"
- `category` = "blocks"
- `cookingtime` = 200
- `experience` = 2.0
- `ingredient.item` = "minecraft:raw_iron_block"
- `result.count` = 1
- `result.id` = "minecraft:iron_block"

### `data/compressedfurnace/recipe/smelting/has_raw_scrap_to_has_netherite_scrap.json`

- `type` = "minecraft:smelting"
- `category` = "misc"
- `cookingtime` = 200
- `experience` = 2.0
- `ingredient.item` = "compressedfurnace:raw_scrap"
- `result.count` = 1
- `result.id` = "minecraft:netherite_scrap"

### `data/compressedfurnace/recipe/triple_compressed_blast_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.A.item` = "minecraft:cobbled_deepslate"
- `key.B.item` = "minecraft:cobblestone"
- `key.C.item` = "minecraft:blast_furnace"
- `key.D.item` = "minecraft:cobbled_deepslate"
- `key.E.item` = "compressedfurnace:double_compressed_blast_furnace"
- `pattern` = ["ABA", "CEC", "DBD"]
- `result.count` = 1
- `result.id` = "compressedfurnace:triple_compressed_blast_furnace"

### `data/compressedfurnace/recipe/triple_compressed_crusher.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.A.item` = "minecraft:cobbled_deepslate"
- `key.B.item` = "minecraft:flint"
- `key.C.item` = "minecraft:furnace"
- `key.D.item` = "minecraft:cobbled_deepslate"
- `key.E.item` = "compressedfurnace:double_compressed_crusher"
- `pattern` = ["ABA", "CEC", "DBD"]
- `result.count` = 1
- `result.id` = "compressedfurnace:triple_compressed_crusher"

### `data/compressedfurnace/recipe/triple_compressed_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.A.item` = "minecraft:cobbled_deepslate"
- `key.B.item` = "minecraft:cobblestone"
- `key.C.item` = "minecraft:furnace"
- `key.D.item` = "minecraft:cobbled_deepslate"
- `key.E.item` = "compressedfurnace:double_compressed_furnace"
- `pattern` = ["ABA", "CEC", "DBD"]
- `result.count` = 1
- `result.id` = "compressedfurnace:triple_compressed_furnace"

### `data/compressedfurnace/recipe/triple_compressed_generator.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.D.item` = "minecraft:diamond"
- `key.F.item` = "compressedfurnace:double_compressed_generator"
- `key.G.item` = "minecraft:gold_block"
- `key.R.item` = "minecraft:redstone_block"
- `pattern` = ["GDG", "RFR", "GDG"]
- `result.count` = 1
- `result.id` = "compressedfurnace:triple_compressed_generator"

### `data/minecraft/tags/block/mineable/pickaxe.json`

- `values` = ["compressedfurnace:compressed_furnace", "compressedfurnace:double_compressed_furnace", "compressedfurnace:triple_compressed_furnace", "compressedfurnace:compressed_crusher", "compressedfurnace:double_compressed_crusher", "compressedfurnace:triple_compressed_crusher", "compressedfurnace:compressed_g…

### `data/minecraft/tags/block/needs_iron_tool.json`

- `values` = ["compressedfurnace:triple_compressed_furnace", "compressedfurnace:triple_compressed_crusher", "compressedfurnace:triple_compressed_generator", "compressedfurnace:powered_triple_compressed_furnace", "compressedfurnace:powered_triple_compressed_crusher", "compressedfurnace:triple_compressed_blast_fur…

### `data/minecraft/tags/block/needs_stone_tool.json`

- `values` = ["compressedfurnace:double_compressed_furnace", "compressedfurnace:double_compressed_crusher", "compressedfurnace:double_compressed_generator", "compressedfurnace:powered_double_compressed_furnace", "compressedfurnace:powered_double_compressed_crusher", "compressedfurnace:double_compressed_blast_fur…

## Testi nel codice


### `net/biorfn/compressedfurnace/blocks/AbstractCompressedBlock.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/blast/CompressedBlastFurnaceBlock.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/blast/DoubleCompressedBlastFurnaceBlock.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/blast/TripleCompressedBlastFurnaceBlock.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/crusher/CompressedCrusherBlock.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/crusher/DoubleCrusherBlock.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/crusher/TripleCrusherBlock.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/Furnace/CompressedFurnaceBlock.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/Furnace/DoubleCompressedFurnaceBlock.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/Furnace/TripleCompressedFurnaceBlock.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/generator/CompressedGeneratorBlock.class`

- "net/biorfn/compressedfurnace/blocks/generator/CompressedGeneratorBlock"
- "net/biorfn/compressedfurnace/blocks/generator/GeneratorBlock"
- "net/biorfn/compressedfurnace/entity/generator/CompressedGeneratorEntity"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "COMPRESSED_GENERATOR_TILE"
- "createGeneratorTicker"
- "compressed_generator"
- "Lcom/mojang/serialization/MapCodec<Lnet/biorfn/compressedfurnace/blocks/generator/CompressedGeneratorBlock;>;"
- "Lnet/biorfn/compressedfurnace/blocks/generator/CompressedGeneratorBlock;"
- "()Lcom/mojang/serialization/MapCodec<+Lnet/biorfn/compressedfurnace/blocks/generator/CompressedGeneratorBlock;>;"
- "compressedGeneratorEntity"
- "Lnet/biorfn/compressedfurnace/entity/generator/CompressedGeneratorEntity;"
- "CompressedGeneratorBlock.java"
- "(Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;)Lnet/biorfn/compressedfurnace/blocks/generator/CompressedGeneratorBlock;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/generator/DoubleCompressedGeneratorBlock.class`

- "net/biorfn/compressedfurnace/blocks/generator/DoubleCompressedGeneratorBlock"
- "net/biorfn/compressedfurnace/blocks/generator/GeneratorBlock"
- "net/biorfn/compressedfurnace/entity/generator/DoubleCompressedGeneratorEntity"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "DOUBLE_COMPRESSED_GENERATOR_TILE"
- "createGeneratorTicker"
- "double_compressed_generator"
- "Lcom/mojang/serialization/MapCodec<Lnet/biorfn/compressedfurnace/blocks/generator/DoubleCompressedGeneratorBlock;>;"
- "Lnet/biorfn/compressedfurnace/blocks/generator/DoubleCompressedGeneratorBlock;"
- "()Lcom/mojang/serialization/MapCodec<+Lnet/biorfn/compressedfurnace/blocks/generator/GeneratorBlock;>;"
- "doubleCompressedGeneratorEntity"
- "Lnet/biorfn/compressedfurnace/entity/generator/DoubleCompressedGeneratorEntity;"
- "DoubleCompressedGeneratorBlock.java"
- "(Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;)Lnet/biorfn/compressedfurnace/blocks/generator/DoubleCompressedGeneratorBlock;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/generator/GeneratorBlock.class`

- "net/biorfn/compressedfurnace/blocks/generator/GeneratorBlock"
- "net/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity"
- "Lnet/biorfn/compressedfurnace/blocks/generator/GeneratorBlock;"
- "()Lcom/mojang/serialization/MapCodec<+Lnet/biorfn/compressedfurnace/blocks/generator/GeneratorBlock;>;"
- "generatorBlockEntity"
- "Lnet/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity;"
- "createGeneratorTicker"
- "Lnet/minecraft/world/level/block/entity/BlockEntityType<+Lnet/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity;>;"
- "<T:Lnet/minecraft/world/level/block/entity/BlockEntity;>(Lnet/minecraft/world/level/Level;Lnet/minecraft/world/level/block/entity/BlockEntityType<TT;>;Lnet/minecraft/world/level/block/entity/BlockEntityType<+Lnet/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity;>;)Lnet/minecraft/world/…"
- "GeneratorBlock.java"
- "(Lnet/minecraft/world/level/Level;Lnet/minecraft/core/BlockPos;Lnet/minecraft/world/level/block/state/BlockState;Lnet/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity;)V"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/generator/TripleCompressedGeneratorBlock.class`

- "net/biorfn/compressedfurnace/blocks/generator/TripleCompressedGeneratorBlock"
- "net/biorfn/compressedfurnace/blocks/generator/GeneratorBlock"
- "net/biorfn/compressedfurnace/entity/generator/TripleCompressedGeneratorEntity"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "TRIPLE_COMPRESSED_GENERATOR_TILE"
- "createGeneratorTicker"
- "triple_compressed_generator"
- "Lcom/mojang/serialization/MapCodec<Lnet/biorfn/compressedfurnace/blocks/generator/TripleCompressedGeneratorBlock;>;"
- "Lnet/biorfn/compressedfurnace/blocks/generator/TripleCompressedGeneratorBlock;"
- "()Lcom/mojang/serialization/MapCodec<+Lnet/biorfn/compressedfurnace/blocks/generator/GeneratorBlock;>;"
- "tripleCompressedGeneratorEntity"
- "Lnet/biorfn/compressedfurnace/entity/generator/TripleCompressedGeneratorEntity;"
- "TripleCompressedGeneratorBlock.java"
- "(Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;)Lnet/biorfn/compressedfurnace/blocks/generator/TripleCompressedGeneratorBlock;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/powered/AbstractCompressedPoweredBlock.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/powered/blast/PoweredCompressedBlastFurnaceBlock.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/powered/blast/PoweredDoubleCompressedBlastFurnaceBlock.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/powered/blast/PoweredTripleCompressedBlastFurnaceBlock.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/powered/crusher/PoweredCompressedCrusherBlock.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/powered/crusher/PoweredDoubleCompressedCrusherBlock.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/powered/crusher/PoweredTripleCompressedCrusherBlock.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/powered/furnace/PoweredCompressedFurnaceBlock.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/powered/furnace/PoweredDoubleCompressedFurnaceBlock.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/blocks/powered/furnace/PoweredTripleCompressedFurnaceBlock.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/ClientSetup.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "COMPRESSED_GENERATOR_MENU"
- "DOUBLE_COMPRESSED_GENERATOR_MENU"
- "TRIPLE_COMPRESSED_GENERATOR_MENU"
- "net/biorfn/compressedfurnace/screen/generator/CompressedGeneratorScreen"
- "(Lnet/biorfn/compressedfurnace/menu/generator/CompressedGeneratorMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)V"
- "(Lnet/biorfn/compressedfurnace/menu/generator/CompressedGeneratorMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)Lnet/biorfn/compressedfurnace/screen/generator/CompressedGeneratorScreen;"
- "net/biorfn/compressedfurnace/screen/generator/DoubleCompressedGeneratorScreen"
- "(Lnet/biorfn/compressedfurnace/menu/generator/DoubleCompressedGeneratorMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)V"
- "(Lnet/biorfn/compressedfurnace/menu/generator/DoubleCompressedGeneratorMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)Lnet/biorfn/compressedfurnace/screen/generator/DoubleCompressedGeneratorScreen;"
- "net/biorfn/compressedfurnace/screen/generator/TripleCompressedGeneratorScreen"
- "(Lnet/biorfn/compressedfurnace/menu/generator/TripleCompressedGeneratorMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)V"
- "(Lnet/biorfn/compressedfurnace/menu/generator/TripleCompressedGeneratorMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)Lnet/biorfn/compressedfurnace/screen/generator/TripleCompressedGeneratorScreen;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/CompressedFurnace.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/CompressedFurnaceClient.class`

- "net/neoforged/neoforge/client/gui/IConfigScreenFactory"
- "()Lnet/neoforged/neoforge/client/gui/IConfigScreenFactory;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/config/Config.class`

- "Compressed Tier Settings"
- "Chance list for extra items in compressed tier."
- "Double Compressed Tier Settings"
- "Chance list for extra items in double compressed tier."
- "Triple Compressed Tier Settings"
- "Chance list for extra items in triple compressed tier."
- "Item transfer rate for compressed tier furnaces."
- "Item transfer rate for compressed tier powered furnaces."
- "Auto export delay (ticks) for compressed tier furnaces (20 ticks = 1 second)."
- "Auto export delay (ticks) for compressed tier powered furnaces (20 ticks = 1 second)."
- "Cooking Time Modifiers"
- "cooking"
- "Cooking time modifier for compressed tier (e.g., 0.9 for 10% faster cooking)."
- "compressedCookTimeModifier"
- "Cooking time modifier for double compressed tier (e.g., 0.8 for 20% faster cooking)."
- "doubleCompressedCookTimeModifier"
- "Cooking time modifier for triple compressed tier (e.g., 0.6 for 40% faster cooking)."
- "tripleCompressedCookTimeModifier"
- "Fuel Efficiency Multipliers"
- "fuel"
- "Fuel efficiency multiplier for compressed tier furnaces (e.g., 1.5 means burn time is 1.5x more efficient)."
- "compressedFuelMultiplier"
- "Fuel efficiency multiplier for double compressed tier furnaces (e.g., 2.0 means burn time is 2x more efficient)."
- "doubleCompressedFuelMultiplier"
- "Fuel efficiency multiplier for triple compressed tier furnaces (e.g., 2.5 means burn time is 2.5x more efficient)."
- "tripleCompressedFuelMultiplier"
- "Energy Capacity and TransferRate Configuration"
- "energy"
- "Energy capacity for compressed tiers."
- "compressedEnergyCapacity"
- "Max energy transfer rate (FE/t) for compressed tiers."
- "Energy capacity for double compressed tier generators."
- "doubleCompressedEnergyCapacity"
- "Max energy transfer rate (FE/t) for double compressed tier generators."
- "Energy capacity for triple compressed tier generators."
- "tripleCompressedEnergyCapacity"
- "Max energy transfer rate (FE/t) for triple compressed tier generators."
- "Generator Configuration"
- "generator"
- "Energy produced per tick by compressed tier generators."
- "compressedEnergyPerTick"
- "Lava tank capacity for compressed tier generators."
- "Energy produced per tick by double compressed tier generators."
- "doubleCompressedEnergyPerTick"
- "Lava tank capacity for double compressed tier generators."
- "Energy produced per tick by triple compressed tier generators."
- "tripleCompressedEnergyPerTick"
- "Lava tank capacity for triple compressed tier generators."
- "cookinAndFuel"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/data/DataGenerators.class`

- "getGenerator"
- "()Lnet/minecraft/data/DataGenerator;"
- "net/minecraft/data/DataGenerator"
- "net/biorfn/compressedfurnace/data/DataGenerators"
- "Lnet/biorfn/compressedfurnace/data/DataGenerators;"
- "generator"
- "Lnet/minecraft/data/DataGenerator;"
- "DataGenerators.java"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/data/EnUsLangProvider.class`

- "compressed_generator"
- "Compressed Generator"
- "double_compressed_generator"
- "Double Compressed Generator"
- "triple_compressed_generator"
- "Triple Compressed Generator"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "COMPRESSED_GENERATOR_ITEM"
- "DOUBLE_COMPRESSED_GENERATOR_ITEM"
- "TRIPLE_COMPRESSED_GENERATOR_ITEM"
- "generator"
- "energy"
- "Energy Capacity and TransferRate"
- "compressedEnergyCapacity"
- "Energy capacity for compressed tiers."
- "Max energy transfer rate (FE/t) for compressed tiers."
- "doubleCompressedEnergyCapacity"
- "Energy capacity for double compressed tier generators."
- "Max energy transfer rate (FE/t) for double compressed tier generators."
- "tripleCompressedEnergyCapacity"
- "Energy capacity for triple compressed tier generators."
- "Max energy transfer rate (FE/t) for triple compressed tier generators."
- "Generator Configuration"
- "compressedEnergyPerTick"
- "Energy produced per tick by compressed tier generators."
- "Lava tank capacity for compressed tier generators."
- "doubleCompressedEnergyPerTick"
- "Energy produced per tick by double compressed tier generators."
- "Lava tank capacity for double compressed tier generators."
- "tripleCompressedEnergyPerTick"
- "Energy produced per tick by triple compressed tier generators."
- "Lava tank capacity for triple compressed tier generators."
- "cooking"
- "Cooking Time Configuration"
- "compressedCookTimeModifier"
- "Cooking time modifier for compressed tier (e.g., 0.9 for 10% faster cooking)."
- "doubleCompressedCookTimeModifier"
- "Cooking time modifier for double compressed tier (e.g., 0.8 for 20% faster cooking)."
- "tripleCompressedCookTimeModifier"
- "Cooking time modifier for triple compressed tier (e.g., 0.6 for 40% faster cooking)."
- "fuel"
- "Fuel Configuration"
- "compressedFuelMultiplier"
- "Fuel efficiency multiplier for compressed tier furnaces (e.g., 1.5 means burn time is 1.5x more efficient)."
- "doubleCompressedFuelMultiplier"
- "Fuel efficiency multiplier for double compressed tier furnaces (e.g., 2.0 means burn time is 2x more efficient)."
- "tripleCompressedFuelMultiplier"
- "Fuel efficiency multiplier for triple compressed tier furnaces (e.g., 2.5 means burn time is 2.5x more efficient)."
- "Item transfer rate for compressed tier furnaces."
- "(Powered) Item transfer rate for compressed tier powered furnaces."
- "Auto export delay (ticks) for compressed tier furnaces (20 ticks = 1 second)."
- "(Powered) Auto export delay (ticks) for compressed tier powered furnaces (20 ticks = 1 second)."
- "Item transfer rate for double compressed tier furnaces."
- "(Powered) Item transfer rate for double compressed tier powered furnaces."
- "Auto export delay (ticks) for double compressed tier furnaces (20 ticks = 1 second)."
- "(Powered) Auto export delay (ticks) for double compressed tier powered furnaces (20 ticks = 1 second)."
- "Item transfer rate for triple compressed tier furnaces."
- "(Powered) Item transfer rate for triple compressed tier powered furnaces."
- "Auto export delay (ticks) for triple compressed tier furnaces (20 ticks = 1 second)."
- "(Powered) Auto export delay (ticks) for triple compressed tier powered furnaces (20 ticks = 1 second)."
- "java/lang/invoke/StringConcatFactory"

### `net/biorfn/compressedfurnace/data/MultiFurnaceBlackStateProvider.class`

- "net/neoforged/neoforge/client/model/generators/BlockStateProvider"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "COMPRESSED_GENERATOR"
- "generator"
- "DOUBLE_COMPRESSED_GENERATOR"
- "TRIPLE_COMPRESSED_GENERATOR"
- "(Lnet/minecraft/world/level/block/Block;)Lnet/neoforged/neoforge/client/model/generators/VariantBlockStateBuilder;"
- "net/neoforged/neoforge/client/model/generators/VariantBlockStateBuilder"
- "(Ljava/util/function/Function;)Lnet/neoforged/neoforge/client/model/generators/VariantBlockStateBuilder;"
- "()Lnet/neoforged/neoforge/client/model/generators/BlockModelProvider;"
- "net/neoforged/neoforge/client/model/generators/BlockModelProvider"
- "(Ljava/lang/String;Lnet/minecraft/resources/ResourceLocation;Lnet/minecraft/resources/ResourceLocation;Lnet/minecraft/resources/ResourceLocation;)Lnet/neoforged/neoforge/client/model/generators/ModelBuilder;"
- "(Lnet/minecraft/world/level/block/Block;Lnet/neoforged/neoforge/client/model/generators/ModelFile;)V"
- "net/neoforged/neoforge/client/model/generators/ConfiguredModel"
- "(Lnet/neoforged/neoforge/client/model/generators/ModelFile;IIZ)V"
- "TIER"
- "TIER1"
- "TIER2"
- "GENERATOR"
- "tier"
- "(Ljava/lang/String;Ljava/lang/String;Lnet/minecraft/world/level/block/state/BlockState;)[Lnet/neoforged/neoforge/client/model/generators/ConfiguredModel;"
- "(Lnet/minecraft/world/level/block/state/BlockState;)[Lnet/neoforged/neoforge/client/model/generators/ConfiguredModel;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "java/lang/invoke/StringConcatFactory"

### `net/biorfn/compressedfurnace/data/MultiFurnaceBlockLootTableProvider.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "dropSelfTieredItem"
- "COMPRESSED_GENERATOR"
- "DOUBLE_COMPRESSED_GENERATOR"
- "TRIPLE_COMPRESSED_GENERATOR"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/data/MultiFurnaceBlockTagProvider.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "COMPRESSED_GENERATOR"
- "DOUBLE_COMPRESSED_GENERATOR"
- "TRIPLE_COMPRESSED_GENERATOR"

### `net/biorfn/compressedfurnace/data/MultiFurnaceItemsModelProvider.class`

- "net/neoforged/neoforge/client/model/generators/ItemModelProvider"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "(Lnet/minecraft/world/item/Item;)Lnet/neoforged/neoforge/client/model/generators/ItemModelBuilder;"
- "(Lnet/minecraft/resources/ResourceLocation;)Lnet/neoforged/neoforge/client/model/generators/ItemModelBuilder;"
- "(Ljava/lang/String;Lnet/minecraft/resources/ResourceLocation;)Lnet/neoforged/neoforge/client/model/generators/ModelBuilder;"
- "net/neoforged/neoforge/client/model/generators/ItemModelBuilder"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "java/lang/invoke/StringConcatFactory"

### `net/biorfn/compressedfurnace/data/MultiFurnaceRecipeProvider.class`

- "generatorRecipes"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "addT1Fueled"
- "addT2Fueled"
- "addT3Fueled"
- "net/minecraft/data/recipes/SimpleCookingRecipeBuilder"
- "(Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/data/recipes/RecipeCategory;Lnet/minecraft/world/level/ItemLike;FI)Lnet/minecraft/data/recipes/SimpleCookingRecipeBuilder;"
- "(Ljava/lang/String;Lnet/minecraft/advancements/Criterion;)Lnet/minecraft/data/recipes/SimpleCookingRecipeBuilder;"
- "net/biorfn/compressedfurnace/recipes/GeneratorRecipeBuilder"
- "generator"
- "(Lnet/minecraft/world/item/crafting/Ingredient;I)Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipeBuilder;"
- "addFuelPowered"
- "COMPRESSED_GENERATOR"
- "DOUBLE_COMPRESSED_GENERATOR"
- "TRIPLE_COMPRESSED_GENERATOR"
- "compressed_generator"
- "double_compressed_generator"
- "triple_compressed_generator"
- "addGeneratorItemRecipe"
- "energy"
- "generator/\u0001_to_energy"
- "java/lang/invoke/StringConcatFactory"

### `net/biorfn/compressedfurnace/energy/FEnergyStorage.class`

- "net/neoforged/neoforge/energy/EnergyStorage"
- "net/biorfn/compressedfurnace/energy/FEnergyStorage"
- "getEnergyStored"
- "getMaxEnergyStored"
- "energy"
- "onEnergyChanged"
- "(I)Lnet/neoforged/neoforge/energy/EnergyStorage;"
- "net/neoforged/neoforge/energy/IEnergyStorage"
- "Lnet/biorfn/compressedfurnace/energy/FEnergyStorage;"
- "getEnergy"
- "setEnergy"
- "setEnergyDirectly"
- "FEnergyStorage.java"

### `net/biorfn/compressedfurnace/entity/AbstractCompressedEntityBlock$2.class`

- "cookingStateBySlot"
- "net/biorfn/compressedfurnace/util/entitiy/CookingState"
- "DEFAULT_COOK_TIME"
- "Lnet/biorfn/compressedfurnace/util/entitiy/CookingState;"
- "(Ljava/lang/Integer;)Lnet/biorfn/compressedfurnace/util/entitiy/CookingState;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/entity/AbstractCompressedEntityBlock.class`

- "cookingStateBySlot"
- "fuelTicksBySlot"
- "tierID"
- "DEFAULT_COOK_TIME"
- "net/biorfn/compressedfurnace/util/entitiy/CookingState"
- "createWithTier"
- "(Ljava/lang/String;I)Lnet/biorfn/compressedfurnace/util/entitiy/CookingState;"
- "TierID"
- "FuelPool"
- "fuelPool"
- "FuelTicksBySlot"
- "loadCookingState"
- "CookingStateBySlot"
- "allocateFuelTicks"
- "net/minecraft/world/item/crafting/AbstractCookingRecipe"
- "getFuelMultiplier"
- "FUEL"
- "isFuel"
- "compressedFuelMultiplier"
- "doubleCompressedFuelMultiplier"
- "tripleCompressedFuelMultiplier"
- "calculateTransferDelayBasedOnTier"
- "calculateTransferCountBasedOnTier"
- "Lnet/minecraft/world/item/crafting/RecipeType<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "Lnet/minecraft/world/item/crafting/RecipeManager$CachedCheck<Lnet/minecraft/world/item/crafting/SingleRecipeInput;+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "Ljava/util/Map<Ljava/lang/Integer;Lnet/biorfn/compressedfurnace/util/entitiy/CookingState;>;"
- "tierId"
- "(Lnet/minecraft/world/level/block/entity/BlockEntityType<*>;Lnet/minecraft/core/BlockPos;Lnet/minecraft/world/level/block/state/BlockState;Ljava/lang/String;Lnet/minecraft/world/item/crafting/RecipeType<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;Ljava/lang/String;)V"
- "fuelTicksBySlotTag"
- "cookingStateTag"
- "Ljava/util/Map$Entry<Ljava/lang/Integer;Lnet/biorfn/compressedfurnace/util/entitiy/CookingState;>;"
- "fuelStack"
- "cookingState"
- "Lnet/biorfn/compressedfurnace/util/entitiy/CookingState;"
- "fuelRemaining"
- "hasFuel"
- "requiredFuel"
- "allocatedFuel"
- "maxFuelTime"
- "fuel"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "java/lang/invoke/StringConcatFactory"

### `net/biorfn/compressedfurnace/entity/blast/CompressedBlastFurnaceEntity.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/entity/blast/DoubleCompressedBlastFurnaceEntity.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/entity/blast/TripleCompressedBlastFurnaceEntity.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/entity/crusher/CompressedCrusherEntity.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/entity/crusher/DoubleCrusherEntity.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/entity/crusher/TripleCrusherEntity.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/entity/furnace/CompressedFurnaceEntity.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/entity/furnace/DoubleCompressedFurnaceEntity.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/entity/furnace/TripleCompressedFurnaceEntity.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/entity/generator/CompressedGeneratorEntity.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "COMPRESSED_GENERATOR_TILE"
- "net/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity"
- "container.compressedfurnace.compressed_generator"
- "net/biorfn/compressedfurnace/menu/generator/CompressedGeneratorMenu"
- "net/biorfn/compressedfurnace/entity/generator/CompressedGeneratorEntity"
- "Lnet/biorfn/compressedfurnace/entity/generator/CompressedGeneratorEntity;"
- "CompressedGeneratorEntity.java"

### `net/biorfn/compressedfurnace/entity/generator/DoubleCompressedGeneratorEntity.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "DOUBLE_COMPRESSED_GENERATOR_TILE"
- "net/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity"
- "container.compressedfurnace.double_compressed_generator"
- "net/biorfn/compressedfurnace/menu/generator/DoubleCompressedGeneratorMenu"
- "net/biorfn/compressedfurnace/entity/generator/DoubleCompressedGeneratorEntity"
- "Lnet/biorfn/compressedfurnace/entity/generator/DoubleCompressedGeneratorEntity;"
- "DoubleCompressedGeneratorEntity.java"

### `net/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity$1.class`

- "net/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity$1"
- "Lnet/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity;"
- "net/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity"
- "fuelBurnTime"
- "energyStorage"
- "Lnet/biorfn/compressedfurnace/energy/FEnergyStorage;"
- "net/biorfn/compressedfurnace/energy/FEnergyStorage"
- "getEnergyStored"
- "getMaxEnergyStored"
- "setEnergy"
- "(Lnet/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity;)V"
- "Lnet/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity$1;"
- "GeneratorBlockEntity.java"

### `net/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity$2.class`

- "net/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity$2"
- "Lnet/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity;"
- "net/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity"
- "(Lnet/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity;ILjava/util/function/Predicate;)V"
- "Lnet/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity$2;"
- "GeneratorBlockEntity.java"

### `net/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity$3.class`

- "net/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity$3"
- "Lnet/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity;"
- "net/biorfn/compressedfurnace/energy/FEnergyStorage"
- "net/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity"
- "lastGameTickEnergyUpdated"
- "(Lnet/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity;IIII)V"
- "Lnet/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity$3;"
- "onEnergyChanged"
- "GeneratorBlockEntity.java"
- "createEnergyStorage"
- "(Ljava/lang/String;)Lnet/biorfn/compressedfurnace/energy/FEnergyStorage;"

### `net/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity.class`

- "net/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity"
- "tierID"
- "createEnergyStorage"
- "(Ljava/lang/String;)Lnet/biorfn/compressedfurnace/energy/FEnergyStorage;"
- "energyStorage"
- "Lnet/biorfn/compressedfurnace/energy/FEnergyStorage;"
- "fuelBurnTime"
- "net/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity$1"
- "(Lnet/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity;)V"
- "validateFuelCache"
- "net/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity$2"
- "(Lnet/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity;ILjava/util/function/Predicate;)V"
- "compressedEnergyCapacity"
- "doubleCompressedEnergyCapacity"
- "tripleCompressedEnergyCapacity"
- "net/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity$3"
- "(Lnet/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity;IIII)V"
- "getFuel"
- "fuelCache"
- "net/biorfn/compressedfurnace/util/entitiy/FuelManager"
- "buildFuels"
- "addCustomFuelRecipes"
- "processGeneratorRecipes"
- "net/biorfn/compressedfurnace/recipes/GeneratorRecipe"
- "getEnergy"
- "net/biorfn/compressedfurnace/blocks/generator/GeneratorBlock"
- "burnFuel"
- "hasEnergyToDistribute"
- "distributeEnergy"
- "net/biorfn/compressedfurnace/energy/FEnergyStorage"
- "getEnergyStored"
- "getMaxEnergyStored"
- "getEnergyPerTick"
- "setEnergy"
- "getFuelMultiplier"
- "startFuelBurning"
- "extractEnergy"
- "net/neoforged/neoforge/energy/IEnergyStorage"
- "receiveEnergy"
- "net/neoforged/neoforge/capabilities/Capabilities$EnergyStorage"
- "TierID"
- "FuelBurnTime"
- "Energy"
- "lastGameTickEnergyUpdated"
- "isFuel"
- "compressedEnergyPerTick"
- "doubleCompressedEnergyPerTick"
- "tripleCompressedEnergyPerTick"
- "compressedFuelMultiplier"
- "doubleCompressedFuelMultiplier"
- "tripleCompressedFuelMultiplier"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "GENERATOR_RECIPE_TYPE"
- "GENERATOR_FUEL_SLOT"
- "Lnet/minecraft/world/item/crafting/RecipeType<+Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;>;"
- "Lnet/minecraft/world/item/crafting/RecipeManager$CachedCheck<Lnet/minecraft/world/item/crafting/SingleRecipeInput;+Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;>;"
- "Lnet/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity;"
- "generatorRecipe"
- "Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;"
- "Ljava/util/List<+Lnet/minecraft/world/item/crafting/RecipeHolder<+Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;>;>;"
- "customFuelMap"
- "(Lnet/minecraft/world/level/Level;Lnet/minecraft/core/BlockPos;Lnet/minecraft/world/level/block/state/BlockState;Lnet/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity;)V"
- "fuel"
- "energyPerTick"
- "multiplier"
- "sendEnergy"
- "(ILnet/neoforged/neoforge/energy/IEnergyStorage;)I"
- "Lnet/neoforged/neoforge/energy/IEnergyStorage;"
- "energyAccepted"
- "lambda$validateFuelCache$7"
- "lambda$validateFuelCache$6"
- "lambda$getFuel$5"
- "lambda$getFuel$4"
- "lambda$getFuel$3"
- "lambda$getFuel$2"
- "lambda$getFuel$1"
- "GeneratorBlockEntity.java"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "EnergyStorage"

### `net/biorfn/compressedfurnace/entity/generator/TripleCompressedGeneratorEntity.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "TRIPLE_COMPRESSED_GENERATOR_TILE"
- "net/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity"
- "container.compressedfurnace.triple_compressed_generator"
- "net/biorfn/compressedfurnace/menu/generator/TripleCompressedGeneratorMenu"
- "net/biorfn/compressedfurnace/entity/generator/TripleCompressedGeneratorEntity"
- "Lnet/biorfn/compressedfurnace/entity/generator/TripleCompressedGeneratorEntity;"
- "TripleCompressedGeneratorEntity.java"

### `net/biorfn/compressedfurnace/entity/powered/AbstractCompressedPoweredEntityBlock$1.class`

- "energyStorage"
- "Lnet/biorfn/compressedfurnace/energy/FEnergyStorage;"
- "net/biorfn/compressedfurnace/energy/FEnergyStorage"
- "getEnergyStored"
- "getMaxEnergyStored"
- "net/biorfn/compressedfurnace/util/entitiy/CookingState"
- "setEnergy"
- "DEFAULT_COOK_TIME"
- "Lnet/biorfn/compressedfurnace/util/entitiy/CookingState;"
- "(Ljava/lang/Integer;)Lnet/biorfn/compressedfurnace/util/entitiy/CookingState;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/entity/powered/AbstractCompressedPoweredEntityBlock$2.class`

- "net/biorfn/compressedfurnace/energy/FEnergyStorage"
- "lastGameTickEnergyUpdated"
- "onEnergyChanged"
- "createEnergyStorage"
- "(Ljava/lang/String;)Lnet/biorfn/compressedfurnace/energy/FEnergyStorage;"

### `net/biorfn/compressedfurnace/entity/powered/AbstractCompressedPoweredEntityBlock.class`

- "cookingStateBySlot"
- "tierID"
- "createEnergyStorage"
- "(Ljava/lang/String;)Lnet/biorfn/compressedfurnace/energy/FEnergyStorage;"
- "energyStorage"
- "Lnet/biorfn/compressedfurnace/energy/FEnergyStorage;"
- "DEFAULT_COOK_TIME"
- "net/biorfn/compressedfurnace/util/entitiy/CookingState"
- "createWithTier"
- "(Ljava/lang/String;I)Lnet/biorfn/compressedfurnace/util/entitiy/CookingState;"
- "Energy"
- "net/biorfn/compressedfurnace/energy/FEnergyStorage"
- "setEnergy"
- "lastGameTickEnergyUpdated"
- "getEnergyStored"
- "CookingStateBySlot"
- "net/minecraft/world/item/crafting/AbstractCookingRecipe"
- "reciveEnergy"
- "receiveEnergy"
- "extractEnergy"
- "getMaxEnergyStored"
- "net/neoforged/neoforge/capabilities/Capabilities$EnergyStorage"
- "net/neoforged/neoforge/energy/IEnergyStorage"
- "compressedEnergyCapacity"
- "doubleCompressedEnergyCapacity"
- "tripleCompressedEnergyCapacity"
- "ENERGY_USAGE_PER_TICK"
- "tierId"
- "Lnet/minecraft/world/item/crafting/RecipeType<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "(Lnet/minecraft/world/level/block/entity/BlockEntityType<*>;Lnet/minecraft/core/BlockPos;Lnet/minecraft/world/level/block/state/BlockState;Ljava/lang/String;Lnet/minecraft/world/item/crafting/RecipeType<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;Ljava/lang/String;)V"
- "loadCookingState"
- "cookingState"
- "Lnet/biorfn/compressedfurnace/util/entitiy/CookingState;"
- "cookingStateTag"
- "hadEnergy"
- "energyNeighbor"
- "Lnet/neoforged/neoforge/energy/IEnergyStorage;"
- "energyToPull"
- "energyExtracted"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "EnergyStorage"

### `net/biorfn/compressedfurnace/entity/powered/blast/PoweredCompressedBlastFurnaceBlockEntity.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/entity/powered/blast/PoweredDoubleCompressedBlastFurnaceBlockEntity.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/entity/powered/blast/PoweredTripleCompressedBlastFurnaceBlockEntity.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/entity/powered/crusher/PoweredCompressedCrusherBlockEntity.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/entity/powered/crusher/PoweredDoubleCompressedCrusherBlockEntitiy.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/entity/powered/crusher/PoweredTripleCompressedCrusherBlockEntity.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/entity/powered/furnace/PoweredCompressedFurnaceBlockEntity.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/entity/powered/furnace/PoweredDoubleCompressedFurnaceBlockEntity.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/entity/powered/furnace/PoweredTripleCompressedFurnaceBlockEntity.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/jei/MultiFurnaceJEIPlugin.class`

- "net/biorfn/compressedfurnace/jei/RecipeCategoryGenerator"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "GENERATOR_RECIPE_TYPE"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems$RecipeTypes"
- "GENERATOR_RECIPE_JEI"
- "COMPRESSED_GENERATOR"
- "DOUBLE_COMPRESSED_GENERATOR"
- "TRIPLE_COMPRESSED_GENERATOR"
- "FUELING"
- "net/biorfn/compressedfurnace/menu/generator/CompressedGeneratorMenu"
- "COMPRESSED_GENERATOR_MENU"
- "net/biorfn/compressedfurnace/menu/generator/DoubleCompressedGeneratorMenu"
- "DOUBLE_COMPRESSED_GENERATOR_MENU"
- "net/biorfn/compressedfurnace/menu/generator/TripleCompressedGeneratorMenu"
- "TRIPLE_COMPRESSED_GENERATOR_MENU"
- "net/biorfn/compressedfurnace/screen/generator/CompressedGeneratorScreen"
- "net/biorfn/compressedfurnace/screen/generator/DoubleCompressedGeneratorScreen"
- "net/biorfn/compressedfurnace/screen/generator/TripleCompressedGeneratorScreen"
- "net/biorfn/compressedfurnace/recipes/GeneratorRecipe"
- "net/biorfn/compressedfurnace/util/entitiy/FuelManager"
- "getFuel"
- "vanillaFuels"
- "fuelRecipes"
- "Ljava/util/List<Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;>;"
- "(Lnet/minecraft/world/item/ItemStack;)Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;"
- "(Lnet/minecraft/world/item/crafting/RecipeHolder;)Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/jei/RecipeCategoryGenerator.class`

- "net/biorfn/compressedfurnace/jei/RecipeCategoryGenerator"
- "staticEnergy"
- "animatedEnergy"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems$RecipeTypes"
- "GENERATOR_RECIPE_JEI"
- "jei.compressedfurnace.generator"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "net/biorfn/compressedfurnace/recipes/GeneratorRecipe"
- "getEnergy"
- "displayEnergy"
- "(Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;)Lnet/minecraft/resources/ResourceLocation;"
- "(Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;)Z"
- "(Lmezz/jei/api/gui/builder/ITooltipBuilder;Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;Lmezz/jei/api/gui/ingredient/IRecipeSlotsView;DD)V"
- "(Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;Lmezz/jei/api/gui/ingredient/IRecipeSlotsView;Lnet/minecraft/client/gui/GuiGraphics;DD)V"
- "(Lmezz/jei/api/gui/builder/IRecipeLayoutBuilder;Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;Lmezz/jei/api/recipe/IFocusGroup;)V"
- "category_generator"
- "Lnet/biorfn/compressedfurnace/jei/RecipeCategoryGenerator;"
- "()Lmezz/jei/api/recipe/RecipeType<Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;>;"
- "Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;"
- "Ljava/lang/Object;Lmezz/jei/api/recipe/category/IRecipeCategory<Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;>;"
- "RecipeCategoryGenerator.java"

### `net/biorfn/compressedfurnace/jei/RecipeCatigoryCrusher.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems$RecipeTypes"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/menu/AbstractCompressedMenu.class`

- "FUEL"
- "tierID"
- "addTierSpecificSlots"
- "net/biorfn/compressedfurnace/menu/slots/FuelSlot"
- "net/minecraft/world/item/crafting/AbstractCookingRecipe"
- "Lnet/minecraft/world/item/crafting/RecipeType<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "Lnet/minecraft/world/item/crafting/RecipeManager$CachedCheck<Lnet/minecraft/world/item/crafting/SingleRecipeInput;+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "(Lnet/minecraft/world/inventory/MenuType<*>;ILnet/minecraft/world/level/Level;Lnet/minecraft/world/entity/player/Inventory;Ljava/lang/String;Lnet/minecraft/world/item/crafting/RecipeType<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;)V"
- "(Lnet/minecraft/world/inventory/MenuType<*>;ILnet/minecraft/world/level/Level;Lnet/minecraft/world/entity/player/Inventory;Ljava/lang/String;Lnet/minecraft/world/inventory/ContainerData;Lnet/minecraft/world/inventory/ContainerData;Lnet/minecraft/world/item/crafting/RecipeType<+Lnet/minecraft/world/i…"
- "isFuel"
- "cookingRecipe"
- "Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;"
- "Ljava/util/List<+Lnet/minecraft/world/item/crafting/RecipeHolder<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;>;"
- "Unexpected tier: \u0001"
- "java/lang/invoke/StringConcatFactory"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/menu/blast/CompressedBlastFurnaceMenu.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "isFuel"

### `net/biorfn/compressedfurnace/menu/blast/DoubleCompressedBlastFurnaceMenu.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "isFuel"

### `net/biorfn/compressedfurnace/menu/blast/TripleCompressedBlastFurnaceMenu.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "isFuel"

### `net/biorfn/compressedfurnace/menu/crusher/CompressedCrusherMenu.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "isFuel"

### `net/biorfn/compressedfurnace/menu/crusher/DoubleCrusherMenu.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "isFuel"

### `net/biorfn/compressedfurnace/menu/crusher/TripleCrusherMenu.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "isFuel"

### `net/biorfn/compressedfurnace/menu/furnace/CompressedFurnaceMenu.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "isFuel"

### `net/biorfn/compressedfurnace/menu/furnace/DoubleCompressedFurnaceMenu.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "isFuel"

### `net/biorfn/compressedfurnace/menu/furnace/TripleCompressedFurnaceMenu.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "isFuel"

### `net/biorfn/compressedfurnace/menu/generator/CompressedGeneratorMenu.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "COMPRESSED_GENERATOR_MENU"
- "net/biorfn/compressedfurnace/menu/generator/GeneratorMenu"
- "net/biorfn/compressedfurnace/menu/generator/CompressedGeneratorMenu"
- "Lnet/biorfn/compressedfurnace/menu/generator/CompressedGeneratorMenu;"
- "CompressedGeneratorMenu.java"

### `net/biorfn/compressedfurnace/menu/generator/DoubleCompressedGeneratorMenu.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "DOUBLE_COMPRESSED_GENERATOR_MENU"
- "net/biorfn/compressedfurnace/menu/generator/GeneratorMenu"
- "net/biorfn/compressedfurnace/menu/generator/DoubleCompressedGeneratorMenu"
- "Lnet/biorfn/compressedfurnace/menu/generator/DoubleCompressedGeneratorMenu;"
- "DoubleCompressedGeneratorMenu.java"

### `net/biorfn/compressedfurnace/menu/generator/GeneratorMenu.class`

- "net/biorfn/compressedfurnace/menu/generator/GeneratorMenu"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "GENERATOR_RECIPE_TYPE"
- "net/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity"
- "Container provider is not a MultiFurnaceBlockEntity in GeneratorMenu"
- "tierID"
- "net/biorfn/compressedfurnace/menu/slots/GeneratorFuelSlot"
- "isFuel"
- "GENERATOR_FUEL"
- "Lnet/minecraft/world/item/crafting/RecipeType<+Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;>;"
- "Lnet/biorfn/compressedfurnace/menu/generator/GeneratorMenu;"
- "tierId"
- "generatorBlockEntity"
- "Lnet/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity;"
- "getEnergy"
- "getMaxEnergy"
- "GeneratorMenu.java"

### `net/biorfn/compressedfurnace/menu/generator/TripleCompressedGeneratorMenu.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "TRIPLE_COMPRESSED_GENERATOR_MENU"
- "net/biorfn/compressedfurnace/menu/generator/GeneratorMenu"
- "net/biorfn/compressedfurnace/menu/generator/TripleCompressedGeneratorMenu"
- "Lnet/biorfn/compressedfurnace/menu/generator/TripleCompressedGeneratorMenu;"
- "TripleCompressedGeneratorMenu.java"

### `net/biorfn/compressedfurnace/menu/powered/AbstractCompressedPoweredMenu.class`

- "tierID"
- "Lnet/minecraft/world/item/crafting/RecipeType<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "(Lnet/minecraft/world/inventory/MenuType<*>;ILnet/minecraft/world/level/Level;Lnet/minecraft/world/entity/player/Inventory;Ljava/lang/String;Lnet/minecraft/world/item/crafting/RecipeType<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;)V"
- "(Lnet/minecraft/world/inventory/MenuType<*>;ILnet/minecraft/world/level/Level;Lnet/minecraft/world/entity/player/Inventory;Ljava/lang/String;Lnet/minecraft/world/inventory/ContainerData;Lnet/minecraft/world/inventory/ContainerData;Lnet/minecraft/world/item/crafting/RecipeType<+Lnet/minecraft/world/i…"
- "addTierSpecificSlots"
- "getEnergy"
- "getMaxEnergy"
- "Unexpected tier: \u0001"
- "java/lang/invoke/StringConcatFactory"

### `net/biorfn/compressedfurnace/menu/powered/blast/PoweredCompressedBlastFurnaceMenu.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/menu/powered/blast/PoweredDoubleCompressedBlastFurnaceMenu.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/menu/powered/blast/PoweredTripleCompressedBlastFurnaceMenu.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/menu/powered/crusher/PoweredCompressedCrusherMenu.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/menu/powered/crusher/PoweredDoubleCompressedCrusherMenu.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/menu/powered/crusher/PoweredTripleCompressedCrusherMenu.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/menu/powered/furnace/PoweredCompressedFurnaceMenu.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/menu/powered/furnace/PoweredDoubleCompressedFurnaceMenu.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/menu/powered/furnace/PoweredTripleCompressedFurnaceMenu.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/menu/slots/FuelSlot.class`

- "isFuel"
- "net/biorfn/compressedfurnace/menu/slots/FuelSlot"
- "Lnet/biorfn/compressedfurnace/menu/slots/FuelSlot;"
- "FuelSlot.java"

### `net/biorfn/compressedfurnace/menu/slots/GeneratorFuelSlot.class`

- "net/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity"
- "isFuel"
- "net/biorfn/compressedfurnace/menu/slots/GeneratorFuelSlot"
- "Lnet/biorfn/compressedfurnace/menu/slots/GeneratorFuelSlot;"
- "GeneratorFuelSlot.java"

### `net/biorfn/compressedfurnace/network/AutoExport.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/network/AutoSplitToggleButton.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/network/Messages.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/network/OpenGuidePacket.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/network/SetSideIO.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/network/SetSideIOReverse.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/network/XPButton.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/recipes/CrusherRecipe.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "net/minecraft/world/item/crafting/AbstractCookingRecipe"
- "(Lnet/minecraft/world/item/crafting/RecipeType;Ljava/lang/String;Lnet/minecraft/world/item/crafting/CookingBookCategory;Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/item/ItemStack;FI)V"
- "net/minecraft/world/item/crafting/CookingBookCategory"
- "cookingtime"
- "(Ljava/lang/String;Lnet/minecraft/world/item/crafting/CookingBookCategory;Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/item/ItemStack;FI)V"
- "Lnet/minecraft/world/item/crafting/CookingBookCategory;"
- "cookingTime"
- "()Lnet/minecraft/world/item/crafting/CookingBookCategory;"
- "(Lnet/biorfn/compressedfurnace/recipes/CrusherRecipe;)Lnet/minecraft/world/item/crafting/CookingBookCategory;"
- "getCookingTime"
- "(Ljava/lang/String;Lnet/minecraft/world/item/crafting/CookingBookCategory;Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/item/ItemStack;Ljava/lang/Float;Ljava/lang/Integer;)Lnet/biorfn/compressedfurnace/recipes/CrusherRecipe;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/recipes/CrusherRecipeBuilder.class`

- "(Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/item/ItemStack;FILnet/minecraft/world/item/crafting/AbstractCookingRecipe$Factory;Lnet/minecraft/data/recipes/RecipeCategory;Lnet/minecraft/world/item/crafting/CookingBookCategory;)V"
- "Lnet/minecraft/world/item/crafting/CookingBookCategory;"
- "cookingTime"
- "factory"
- "Lnet/minecraft/world/item/crafting/AbstractCookingRecipe$Factory;"
- "()Lnet/minecraft/world/item/crafting/AbstractCookingRecipe$Factory;"
- "net/minecraft/world/item/crafting/CookingBookCategory"
- "(Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/level/ItemLike;FILnet/minecraft/world/item/crafting/AbstractCookingRecipe$Factory;Lnet/minecraft/data/recipes/RecipeCategory;Lnet/minecraft/world/item/crafting/CookingBookCategory;)V"
- "(Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/level/ItemLike;IFILnet/minecraft/world/item/crafting/AbstractCookingRecipe$Factory;Lnet/minecraft/data/recipes/RecipeCategory;Lnet/minecraft/world/item/crafting/CookingBookCategory;)V"
- "net/minecraft/world/item/crafting/AbstractCookingRecipe$Factory"
- "(Ljava/lang/String;Lnet/minecraft/world/item/crafting/CookingBookCategory;Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/item/ItemStack;FI)Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;"
- "Lnet/minecraft/world/item/crafting/AbstractCookingRecipe$Factory<*>;"
- "cookingBookCategory"
- "(Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/level/ItemLike;FILnet/minecraft/world/item/crafting/AbstractCookingRecipe$Factory<*>;Lnet/minecraft/data/recipes/RecipeCategory;Lnet/minecraft/world/item/crafting/CookingBookCategory;)V"
- "(Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/level/ItemLike;IFILnet/minecraft/world/item/crafting/AbstractCookingRecipe$Factory<*>;Lnet/minecraft/data/recipes/RecipeCategory;Lnet/minecraft/world/item/crafting/CookingBookCategory;)V"
- "(Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/item/ItemStack;FILnet/minecraft/world/item/crafting/AbstractCookingRecipe$Factory<*>;Lnet/minecraft/data/recipes/RecipeCategory;Lnet/minecraft/world/item/crafting/CookingBookCategory;)V"
- "cookTime"
- "abstractcookingrecipe"
- "Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;"
- "(Ljava/lang/String;Lnet/minecraft/world/item/crafting/CookingBookCategory;Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/item/ItemStack;FI)V"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "java/lang/invoke/StringConcatFactory"
- "net/minecraft/world/item/crafting/AbstractCookingRecipe"
- "Factory"

### `net/biorfn/compressedfurnace/recipes/CrusherRecipeSerializer.class`

- "()Lnet/minecraft/world/item/crafting/CookingBookCategory;"
- "getCookingTime"
- "net/minecraft/world/item/crafting/CookingBookCategory"
- "(Ljava/lang/String;Lnet/minecraft/world/item/crafting/CookingBookCategory;Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/item/ItemStack;FI)V"
- "Lnet/minecraft/world/item/crafting/CookingBookCategory;"
- "cookingTime"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "java/lang/invoke/StringConcatFactory"

### `net/biorfn/compressedfurnace/recipes/GeneratorRecipe$Serializer.class`

- "net/biorfn/compressedfurnace/recipes/GeneratorRecipe"
- "energy"
- "net/biorfn/compressedfurnace/recipes/GeneratorRecipe$Serializer"
- "Lcom/mojang/serialization/MapCodec<Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;>;"
- "Lnet/minecraft/network/codec/StreamCodec<Lnet/minecraft/network/RegistryFriendlyByteBuf;Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;>;"
- "Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe$Serializer;"
- "Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe$Serializer<TT;>;"
- "(Lnet/minecraft/network/RegistryFriendlyByteBuf;)Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;"
- "(Lnet/minecraft/network/RegistryFriendlyByteBuf;Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;)V"
- "Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;"
- "()Lcom/mojang/serialization/MapCodec<Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;>;"
- "()Lnet/minecraft/network/codec/StreamCodec<Lnet/minecraft/network/RegistryFriendlyByteBuf;Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;>;"
- "(Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;)Lnet/minecraft/world/item/crafting/Ingredient;"
- "(Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;)Ljava/lang/Integer;"
- "<T:Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;>Ljava/lang/Object;Lnet/minecraft/world/item/crafting/RecipeSerializer<Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;>;"
- "GeneratorRecipe.java"
- "(Ljava/lang/Integer;Lnet/minecraft/world/item/crafting/Ingredient;)Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/recipes/GeneratorRecipe.class`

- "net/biorfn/compressedfurnace/recipes/GeneratorRecipe"
- "energy"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "GENERATOR_RECIPE_SERIALIZER"
- "GENERATOR_RECIPE_TYPE"
- "Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;"
- "getEnergy"
- "GeneratorRecipe.java"
- "net/biorfn/compressedfurnace/recipes/GeneratorRecipe$Serializer"

### `net/biorfn/compressedfurnace/recipes/GeneratorRecipeBuilder.class`

- "net/biorfn/compressedfurnace/recipes/GeneratorRecipeBuilder"
- "energy"
- "net/biorfn/compressedfurnace/recipes/GeneratorRecipe"
- "Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipeBuilder;"
- "generator"
- "(Lnet/minecraft/world/item/crafting/Ingredient;I)Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipeBuilder;"
- "GeneratorRecipeBuilder.java"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "java/lang/invoke/StringConcatFactory"

### `net/biorfn/compressedfurnace/registries/CapabilitiesRegistries.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "COMPRESSED_GENERATOR"
- "DOUBLE_COMPRESSED_GENERATOR"
- "TRIPLE_COMPRESSED_GENERATOR"
- "net/neoforged/neoforge/capabilities/Capabilities$EnergyStorage"
- "net/biorfn/compressedfurnace/entity/generator/GeneratorBlockEntity"
- "energyStorage"
- "Lnet/biorfn/compressedfurnace/energy/FEnergyStorage;"
- "powerGenerators"
- "(Lnet/minecraft/world/level/Level;Lnet/minecraft/core/BlockPos;Lnet/minecraft/world/level/block/state/BlockState;Lnet/minecraft/world/level/block/entity/BlockEntity;Lnet/minecraft/core/Direction;)Lnet/neoforged/neoforge/energy/IEnergyStorage;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "EnergyStorage"

### `net/biorfn/compressedfurnace/registries/ModCommands.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/registries/MultiFurnaceTabs.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "()Lnet/minecraft/world/item/CreativeModeTab$DisplayItemsGenerator;"
- "(Lnet/minecraft/world/item/CreativeModeTab$DisplayItemsGenerator;)Lnet/minecraft/world/item/CreativeModeTab$Builder;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "net/minecraft/world/item/CreativeModeTab$DisplayItemsGenerator"
- "DisplayItemsGenerator"

### `net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems$1.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems$1"
- "Lnet/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems$1;"
- "MultiFurnaceTieredItems.java"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems$2.class`

- "generator"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems$2"
- "Lnet/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems$2;"
- "Ljava/lang/Object;Lnet/minecraft/world/item/crafting/RecipeType<Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;>;"
- "MultiFurnaceTieredItems.java"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems$RecipeTypes.class`

- "generator"
- "net/biorfn/compressedfurnace/recipes/GeneratorRecipe"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems$RecipeTypes"
- "GENERATOR_RECIPE_JEI"
- "fuel"
- "mezz/jei/api/recipe/vanilla/IJeiFuelingRecipe"
- "FUELING"
- "Lmezz/jei/api/recipe/RecipeType<Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;>;"
- "Lmezz/jei/api/recipe/RecipeType<Lmezz/jei/api/recipe/vanilla/IJeiFuelingRecipe;>;"
- "Lnet/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems$RecipeTypes;"
- "MultiFurnaceTieredItems.java"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"

### `net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "()Lnet/neoforged/neoforge/network/IContainerFactory;"
- "(Lnet/neoforged/neoforge/network/IContainerFactory;)Lnet/minecraft/world/inventory/MenuType;"
- "net/biorfn/compressedfurnace/menu/generator/TripleCompressedGeneratorMenu"
- "TRIPLE_COMPRESSED_GENERATOR"
- "net/biorfn/compressedfurnace/blocks/generator/TripleCompressedGeneratorBlock"
- "DOUBLE_COMPRESSED_GENERATOR"
- "net/biorfn/compressedfurnace/menu/generator/DoubleCompressedGeneratorMenu"
- "net/biorfn/compressedfurnace/blocks/generator/DoubleCompressedGeneratorBlock"
- "COMPRESSED_GENERATOR"
- "net/biorfn/compressedfurnace/menu/generator/CompressedGeneratorMenu"
- "net/biorfn/compressedfurnace/blocks/generator/CompressedGeneratorBlock"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems$2"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems$1"
- "generator"
- "GENERATOR_RECIPE_TYPE"
- "GENERATOR_RECIPE_SERIALIZER"
- "compressed_generator"
- "COMPRESSED_GENERATOR_ITEM"
- "COMPRESSED_GENERATOR_TILE"
- "COMPRESSED_GENERATOR_MENU"
- "double_compressed_generator"
- "DOUBLE_COMPRESSED_GENERATOR_ITEM"
- "DOUBLE_COMPRESSED_GENERATOR_TILE"
- "DOUBLE_COMPRESSED_GENERATOR_MENU"
- "triple_compressed_generator"
- "TRIPLE_COMPRESSED_GENERATOR_ITEM"
- "TRIPLE_COMPRESSED_GENERATOR_TILE"
- "TRIPLE_COMPRESSED_GENERATOR_MENU"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/crafting/RecipeType<*>;Lnet/minecraft/world/item/crafting/RecipeType<Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;>;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/item/crafting/RecipeSerializer<*>;Lnet/minecraft/world/item/crafting/RecipeSerializer<Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;>;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/level/block/Block;Lnet/biorfn/compressedfurnace/blocks/generator/CompressedGeneratorBlock;>;"
- "Ljava/util/function/Supplier<Lnet/minecraft/world/level/block/entity/BlockEntityType<Lnet/biorfn/compressedfurnace/entity/generator/CompressedGeneratorEntity;>;>;"
- "Ljava/util/function/Supplier<Lnet/minecraft/world/inventory/MenuType<Lnet/biorfn/compressedfurnace/menu/generator/CompressedGeneratorMenu;>;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/level/block/Block;Lnet/biorfn/compressedfurnace/blocks/generator/DoubleCompressedGeneratorBlock;>;"
- "Ljava/util/function/Supplier<Lnet/minecraft/world/level/block/entity/BlockEntityType<Lnet/biorfn/compressedfurnace/entity/generator/DoubleCompressedGeneratorEntity;>;>;"
- "Ljava/util/function/Supplier<Lnet/minecraft/world/inventory/MenuType<Lnet/biorfn/compressedfurnace/menu/generator/DoubleCompressedGeneratorMenu;>;>;"
- "Lnet/neoforged/neoforge/registries/DeferredHolder<Lnet/minecraft/world/level/block/Block;Lnet/biorfn/compressedfurnace/blocks/generator/TripleCompressedGeneratorBlock;>;"
- "Ljava/util/function/Supplier<Lnet/minecraft/world/level/block/entity/BlockEntityType<Lnet/biorfn/compressedfurnace/entity/generator/TripleCompressedGeneratorEntity;>;>;"
- "Ljava/util/function/Supplier<Lnet/minecraft/world/inventory/MenuType<Lnet/biorfn/compressedfurnace/menu/generator/TripleCompressedGeneratorMenu;>;>;"
- "Lnet/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems;"
- "(ILnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/RegistryFriendlyByteBuf;)Lnet/biorfn/compressedfurnace/menu/generator/TripleCompressedGeneratorMenu;"
- "()Lnet/biorfn/compressedfurnace/blocks/generator/TripleCompressedGeneratorBlock;"
- "(ILnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/RegistryFriendlyByteBuf;)Lnet/biorfn/compressedfurnace/menu/generator/DoubleCompressedGeneratorMenu;"
- "()Lnet/biorfn/compressedfurnace/blocks/generator/DoubleCompressedGeneratorBlock;"
- "(ILnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/RegistryFriendlyByteBuf;)Lnet/biorfn/compressedfurnace/menu/generator/CompressedGeneratorMenu;"
- "()Lnet/biorfn/compressedfurnace/blocks/generator/CompressedGeneratorBlock;"
- "MultiFurnaceTieredItems.java"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems$RecipeTypes"
- "net/biorfn/compressedfurnace/entity/generator/TripleCompressedGeneratorEntity"
- "(Lnet/minecraft/core/BlockPos;Lnet/minecraft/world/level/block/state/BlockState;)Lnet/biorfn/compressedfurnace/entity/generator/TripleCompressedGeneratorEntity;"
- "net/biorfn/compressedfurnace/entity/generator/DoubleCompressedGeneratorEntity"
- "(Lnet/minecraft/core/BlockPos;Lnet/minecraft/world/level/block/state/BlockState;)Lnet/biorfn/compressedfurnace/entity/generator/DoubleCompressedGeneratorEntity;"
- "net/biorfn/compressedfurnace/entity/generator/CompressedGeneratorEntity"
- "(Lnet/minecraft/core/BlockPos;Lnet/minecraft/world/level/block/state/BlockState;)Lnet/biorfn/compressedfurnace/entity/generator/CompressedGeneratorEntity;"
- "net/biorfn/compressedfurnace/recipes/GeneratorRecipe$Serializer"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "net/biorfn/compressedfurnace/recipes/GeneratorRecipe"

### `net/biorfn/compressedfurnace/screen/AbstractCompressedScreen$1.class`

- "FUEL"

### `net/biorfn/compressedfurnace/screen/AbstractCompressedScreen.class`

- "getTierGUITexture"
- "tierID"
- "textures/gui/\u0001_factory.png"
- "textures/gui/\u0001_double_factory.png"
- "textures/gui/\u0001_triple_factory.png"
- "Unexpected tier: \u0001"
- "java/lang/invoke/StringConcatFactory"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/screen/generator/CompressedGeneratorScreen.class`

- "net/biorfn/compressedfurnace/screen/generator/GeneratorScreen"
- "(Lnet/biorfn/compressedfurnace/menu/generator/GeneratorMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;Ljava/lang/String;)V"
- "net/biorfn/compressedfurnace/screen/generator/CompressedGeneratorScreen"
- "(Lnet/biorfn/compressedfurnace/menu/generator/CompressedGeneratorMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)V"
- "Lnet/biorfn/compressedfurnace/screen/generator/CompressedGeneratorScreen;"
- "Lnet/biorfn/compressedfurnace/menu/generator/CompressedGeneratorMenu;"
- "Lnet/biorfn/compressedfurnace/screen/generator/GeneratorScreen<Lnet/biorfn/compressedfurnace/menu/generator/CompressedGeneratorMenu;>;"
- "CompressedGeneratorScreen.java"

### `net/biorfn/compressedfurnace/screen/generator/DoubleCompressedGeneratorScreen.class`

- "net/biorfn/compressedfurnace/screen/generator/GeneratorScreen"
- "(Lnet/biorfn/compressedfurnace/menu/generator/GeneratorMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;Ljava/lang/String;)V"
- "net/biorfn/compressedfurnace/screen/generator/DoubleCompressedGeneratorScreen"
- "(Lnet/biorfn/compressedfurnace/menu/generator/DoubleCompressedGeneratorMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)V"
- "Lnet/biorfn/compressedfurnace/screen/generator/DoubleCompressedGeneratorScreen;"
- "Lnet/biorfn/compressedfurnace/menu/generator/DoubleCompressedGeneratorMenu;"
- "Lnet/biorfn/compressedfurnace/screen/generator/GeneratorScreen<Lnet/biorfn/compressedfurnace/menu/generator/DoubleCompressedGeneratorMenu;>;"
- "DoubleCompressedGeneratorScreen.java"

### `net/biorfn/compressedfurnace/screen/generator/GeneratorScreen.class`

- "textures/gui/generator.png"
- "net/biorfn/compressedfurnace/screen/generator/GeneratorScreen"
- "net/biorfn/compressedfurnace/util/GuiEnergy"
- "energyBar"
- "Lnet/biorfn/compressedfurnace/util/GuiEnergy;"
- "net/biorfn/compressedfurnace/menu/generator/GeneratorMenu"
- "getEnergy"
- "getMaxEnergy"
- "getScaledEnergyHeight"
- "(Lnet/biorfn/compressedfurnace/menu/generator/GeneratorMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;Ljava/lang/String;)V"
- "Lnet/biorfn/compressedfurnace/screen/generator/GeneratorScreen;"
- "Lnet/biorfn/compressedfurnace/menu/generator/GeneratorMenu;"
- "Lnet/biorfn/compressedfurnace/screen/generator/GeneratorScreen<TT;>;"
- "energyHeight"
- "maxEnergy"
- "currentEnergy"
- "<T:Lnet/biorfn/compressedfurnace/menu/generator/GeneratorMenu;>Lnet/minecraft/client/gui/screens/inventory/AbstractContainerScreen<TT;>;"
- "GeneratorScreen.java"

### `net/biorfn/compressedfurnace/screen/generator/TripleCompressedGeneratorScreen.class`

- "net/biorfn/compressedfurnace/screen/generator/GeneratorScreen"
- "(Lnet/biorfn/compressedfurnace/menu/generator/GeneratorMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;Ljava/lang/String;)V"
- "net/biorfn/compressedfurnace/screen/generator/TripleCompressedGeneratorScreen"
- "(Lnet/biorfn/compressedfurnace/menu/generator/TripleCompressedGeneratorMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)V"
- "Lnet/biorfn/compressedfurnace/screen/generator/TripleCompressedGeneratorScreen;"
- "Lnet/biorfn/compressedfurnace/menu/generator/TripleCompressedGeneratorMenu;"
- "Lnet/biorfn/compressedfurnace/screen/generator/GeneratorScreen<Lnet/biorfn/compressedfurnace/menu/generator/TripleCompressedGeneratorMenu;>;"
- "TripleCompressedGeneratorScreen.java"

### `net/biorfn/compressedfurnace/screen/guide/GuideBookScreen.class`

- "fueledMachines"
- "generators"
- "fuelFurnace"
- "fuelCrusher"
- "fuelBlastFurnace"
- "returntoFueled"
- "returntoGenerators"
- "compressed_generator"
- "double_compressed_generator"
- "triple_compressed_generator"
- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "Fueled Machines."
- "For each tier you get an increase"
- "Generators"
- "Each tier gives you more"
- "lava tank or the fuel slot to"
- "Compressed Generator"
- "compressedEnergyCapacity"
- "Double Compressed Generator"
- "doubleCompressedEnergyCapacity"
- "Triple Compressed Generator"
- "tripleCompressedEnergyCapacity"
- "Each tier has a bigger internal"
- "and outputs as the fueled ones."
- "COMPRESSED_GENERATOR_ITEM"
- "DOUBLE_COMPRESSED_GENERATOR_ITEM"
- "TRIPLE_COMPRESSED_GENERATOR_ITEM"
- "Fueled Machines"
- "Fuel Furnace"
- "Fuel Crusher"
- "Fuel Blast Furnace"
- "Return to Fueled"
- "Generator"
- "Return to Generators"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "java/lang/invoke/StringConcatFactory"

### `net/biorfn/compressedfurnace/screen/OpenConfigScreen.class`

- "placeSliderInGridEnergy"
- "energy"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/screen/powered/AbstractCompressedPoweredScreen.class`

- "net/biorfn/compressedfurnace/util/GuiEnergy"
- "energyBar"
- "Lnet/biorfn/compressedfurnace/util/GuiEnergy;"
- "renderEnergyBar"
- "getScaledEnergyHeight"
- "getTierGUITexture"
- "getMaxEnergy"
- "getEnergy"
- "energyHeight"
- "maxEnergy"
- "currentEnergy"
- "java/lang/invoke/StringConcatFactory"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/util/entitiy/BurnUtil.class`

- "net/minecraft/world/item/crafting/AbstractCookingRecipe"
- "net/biorfn/compressedfurnace/util/entitiy/CookingState"
- "tierID"
- "cookingStateBySlot"
- "cookingRecipe"
- "Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;"
- "Ljava/util/Map<Ljava/lang/Integer;Lnet/biorfn/compressedfurnace/util/entitiy/CookingState;>;"
- "(Lnet/minecraft/core/RegistryAccess;Lnet/minecraft/world/item/crafting/RecipeHolder<*>;Lnet/minecraft/core/NonNullList<Lnet/minecraft/world/item/ItemStack;>;IIILnet/biorfn/compressedfurnace/util/entitiy/ExtraItemManager;Ljava/lang/String;Lnet/minecraft/world/level/Level;Lnet/minecraft/core/BlockPos;…"

### `net/biorfn/compressedfurnace/util/entitiy/CookingState.class`

- "net/biorfn/compressedfurnace/util/entitiy/CookingState"
- "getCookTimeForTier"
- "compressedCookTimeModifier"
- "doubleCompressedCookTimeModifier"
- "tripleCompressedCookTimeModifier"
- "Lnet/biorfn/compressedfurnace/util/entitiy/CookingState;"
- "createWithTier"
- "(Ljava/lang/String;I)Lnet/biorfn/compressedfurnace/util/entitiy/CookingState;"
- "tierID"
- "defaultCookTime"
- "CookingState.java"
- "CookingState{progress=\u0001, totalTime=\u0001}"
- "java/lang/invoke/StringConcatFactory"

### `net/biorfn/compressedfurnace/util/entitiy/ExtraItemManager.class`

- "getChancesForTier"
- "getThresholdForTier"
- "tierID"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `net/biorfn/compressedfurnace/util/entitiy/FuelManager.class`

- "net/biorfn/compressedfurnace/util/entitiy/FuelManager"
- "getFuel"
- "getTierMultiplier"
- "fuelCache"
- "buildFuels"
- "isNeverAFurnaceFuel"
- "compressedFuelMultiplier"
- "doubleCompressedFuelMultiplier"
- "tripleCompressedFuelMultiplier"
- "Lnet/biorfn/compressedfurnace/util/entitiy/FuelManager;"
- "tierMultiplier"
- "fuelItem"
- "defaultCookTime"
- "tierId"
- "fuelMap"
- "lambda$getFuel$2"
- "lambda$getFuel$1"
- "lambda$getFuel$0"
- "FuelManager.java"
- "A developer tried to explicitly make fire resistant item \u0001 a furnace fuel. That will not work!"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "java/lang/invoke/StringConcatFactory"

### `net/biorfn/compressedfurnace/util/entitiy/PSideConfigHelper.class`

- "java/lang/invoke/StringConcatFactory"

### `net/biorfn/compressedfurnace/util/entitiy/SideConfigHelper$SlotType.class`

- "FUEL"

### `net/biorfn/compressedfurnace/util/entitiy/SideConfigHelper.class`

- "FUEL"
- "java/lang/invoke/StringConcatFactory"

### `net/biorfn/compressedfurnace/util/entitiy/SlotManager.class`

- "tierID"
- "Unexpected tierID: \u0001"
- "java/lang/invoke/StringConcatFactory"

### `net/biorfn/compressedfurnace/util/GuiEnergy.class`

- "net/biorfn/compressedfurnace/util/GuiEnergy"
- "displayEnergy"
- "Lnet/biorfn/compressedfurnace/util/GuiEnergy;"
- "energy"
- "showEnergy"
- "GuiEnergy.java"

### `net/biorfn/compressedfurnace/util/RecipeValidation.class`

- "net/biorfn/compressedfurnace/registries/MultiFurnaceTieredItems"
- "GENERATOR_RECIPE_TYPE"
- "net/biorfn/compressedfurnace/recipes/GeneratorRecipe"
- "validateGeneratorRecipe"
- "(Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;Lnet/minecraft/world/item/crafting/RecipeHolder;)Z"
- "getEnergy"
- "Generator Recipe {} has an invalid energy! Energy: {}"
- "getCookingTime"
- "Crusher Recipe {} has an invalid cooking time!"
- "generatorRecipe"
- "Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;"
- "(Lnet/biorfn/compressedfurnace/recipes/GeneratorRecipe;Lnet/minecraft/world/item/crafting/RecipeHolder<*>;)Z"
- "Lnet/minecraft/world/item/crafting/RecipeManager$CachedCheck<Lnet/minecraft/world/item/crafting/SingleRecipeInput;+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "(Lnet/minecraft/world/level/Level;[ILnet/minecraft/world/item/crafting/RecipeManager$CachedCheck<Lnet/minecraft/world/item/crafting/SingleRecipeInput;+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;Ljava/util/List<Lnet/minecraft/world/item/ItemStack;>;)Z"

### `net/biorfn/compressedfurnace/util/StringHelper.class`

- "displayEnergy"
- "energy"
- "java/lang/invoke/StringConcatFactory"

### `net/biorfn/compressedfurnace/util/widgets/ConfigSlider.class`

- "java/lang/invoke/StringConcatFactory"
