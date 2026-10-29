# Iron Smelters (iron-smelters)

File generato da `scripts/esamina.py` (workflow "Esamina mod"): la mod **non** è nel pack. Non modificarlo a mano.

- Versione: **21.1.0.6** (release, 2026-09-03), file `IronSmelters-neoforge-1.21.1-21.1.0.6.jar`, id versione `5u0nZKsv`
- Licenza su Modrinth: MIT · download: 26263
- Filtro dei valori: `(recipe|recipes|tags/item|tags/block)/` · filtro dei testi del codice: `(?i)^(.*(speed|cook|tier|augment|upgrade|generator|factory|fuel|multiplier|energy|rainbow).*)$`

## Mod nel file e dipendenze dichiarate

- `ironsmelters` 21.1.0.6
  - required: `neoforge` [4,)
  - required: `minecraft` [1.21.1]

## Cartelle di dati (file .json)

- `ironsmelters:advancement/recipes/decorations`: 24
- `ironsmelters:loot_table/blocks`: 15
- `ironsmelters:recipe`: 24
- `minecraft:tags/block`: 1
- `minecraft:tags/block/mineable`: 1

## Valori dei file filtrati


### `data/ironsmelters/advancement/recipes/decorations/blast_furnace_to_copper_blast_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_copper.conditions.items[0].items` = "#c:ingots/copper"
- `criteria.has_copper.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:blast_furnace_to_copper_blast_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_copper"]
- `rewards.recipes` = ["ironsmelters:blast_furnace_to_copper_blast_furnace"]

### `data/ironsmelters/advancement/recipes/decorations/blast_furnace_to_iron_blast_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_iron.conditions.items[0].items` = "#c:ingots/iron"
- `criteria.has_iron.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:blast_furnace_to_iron_blast_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_iron"]
- `rewards.recipes` = ["ironsmelters:blast_furnace_to_iron_blast_furnace"]

### `data/ironsmelters/advancement/recipes/decorations/copper_blast_furnace_to_iron_blast_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_iron.conditions.items[0].items` = "#c:ingots/iron"
- `criteria.has_iron.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:copper_blast_furnace_to_iron_blast_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_iron"]
- `rewards.recipes` = ["ironsmelters:copper_blast_furnace_to_iron_blast_furnace"]

### `data/ironsmelters/advancement/recipes/decorations/copper_furnace_to_iron_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_iron.conditions.items[0].items` = "#c:ingots/iron"
- `criteria.has_iron.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:copper_furnace_to_iron_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_iron"]
- `rewards.recipes` = ["ironsmelters:copper_furnace_to_iron_furnace"]

### `data/ironsmelters/advancement/recipes/decorations/copper_smoker_to_iron_smoker.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_iron.conditions.items[0].items` = "#c:ingots/iron"
- `criteria.has_iron.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:copper_smoker_to_iron_smoker"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_iron"]
- `rewards.recipes` = ["ironsmelters:copper_smoker_to_iron_smoker"]

### `data/ironsmelters/advancement/recipes/decorations/copper_to_iron_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_furnace.conditions.items[0].items` = "#c:player_workstations/furnaces"
- `criteria.has_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_iron.conditions.items[0].items` = "#c:ingots/iron"
- `criteria.has_iron.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:copper_to_iron_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_iron", "has_furnace"]
- `rewards.recipes` = ["ironsmelters:copper_to_iron_upgrade"]

### `data/ironsmelters/advancement/recipes/decorations/diamond_blast_furnace_to_obsidian_blast_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_obsidian.conditions.items[0].items` = "#c:obsidians/normal"
- `criteria.has_obsidian.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:diamond_blast_furnace_to_obsidian_blast_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_obsidian"]
- `rewards.recipes` = ["ironsmelters:diamond_blast_furnace_to_obsidian_blast_furnace"]

### `data/ironsmelters/advancement/recipes/decorations/diamond_furnace_to_obsidian_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_obsidian.conditions.items[0].items` = "#c:obsidians/normal"
- `criteria.has_obsidian.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:diamond_furnace_to_obsidian_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_obsidian"]
- `rewards.recipes` = ["ironsmelters:diamond_furnace_to_obsidian_furnace"]

### `data/ironsmelters/advancement/recipes/decorations/diamond_smoker_to_obsidian_smoker.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_obsidian.conditions.items[0].items` = "#c:obsidians/normal"
- `criteria.has_obsidian.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:diamond_smoker_to_obsidian_smoker"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_obsidian"]
- `rewards.recipes` = ["ironsmelters:diamond_smoker_to_obsidian_smoker"]

### `data/ironsmelters/advancement/recipes/decorations/diamond_to_obsidian_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_furnace.conditions.items[0].items` = "#c:player_workstations/furnaces"
- `criteria.has_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_obsidian.conditions.items[0].items` = "#c:obsidians/normal"
- `criteria.has_obsidian.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:diamond_to_obsidian_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_obsidian", "has_furnace"]
- `rewards.recipes` = ["ironsmelters:diamond_to_obsidian_upgrade"]

### `data/ironsmelters/advancement/recipes/decorations/furnace_to_copper_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_copper.conditions.items[0].items` = "#c:ingots/copper"
- `criteria.has_copper.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:furnace_to_copper_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_copper"]
- `rewards.recipes` = ["ironsmelters:furnace_to_copper_furnace"]

### `data/ironsmelters/advancement/recipes/decorations/furnace_to_iron_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_iron.conditions.items[0].items` = "#c:ingots/iron"
- `criteria.has_iron.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:furnace_to_iron_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_iron"]
- `rewards.recipes` = ["ironsmelters:furnace_to_iron_furnace"]

### `data/ironsmelters/advancement/recipes/decorations/gold_blast_furnace_to_diamond_blast_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_diamond.conditions.items[0].items` = "#c:gems/diamond"
- `criteria.has_diamond.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:gold_blast_furnace_to_diamond_blast_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_diamond"]
- `rewards.recipes` = ["ironsmelters:gold_blast_furnace_to_diamond_blast_furnace"]

### `data/ironsmelters/advancement/recipes/decorations/gold_furnace_to_diamond_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_diamond.conditions.items[0].items` = "#c:gems/diamond"
- `criteria.has_diamond.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:gold_furnace_to_diamond_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_diamond"]
- `rewards.recipes` = ["ironsmelters:gold_furnace_to_diamond_furnace"]

### `data/ironsmelters/advancement/recipes/decorations/gold_smoker_to_diamond_smoker.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_diamond.conditions.items[0].items` = "#c:gems/diamond"
- `criteria.has_diamond.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:gold_smoker_to_diamond_smoker"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_diamond"]
- `rewards.recipes` = ["ironsmelters:gold_smoker_to_diamond_smoker"]

### `data/ironsmelters/advancement/recipes/decorations/gold_to_diamond_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_diamond.conditions.items[0].items` = "#c:gems/diamond"
- `criteria.has_diamond.trigger` = "minecraft:inventory_changed"
- `criteria.has_furnace.conditions.items[0].items` = "#c:player_workstations/furnaces"
- `criteria.has_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:gold_to_diamond_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_diamond", "has_furnace"]
- `rewards.recipes` = ["ironsmelters:gold_to_diamond_upgrade"]

### `data/ironsmelters/advancement/recipes/decorations/iron_blast_furnace_to_gold_blast_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_gold.conditions.items[0].items` = "#c:ingots/gold"
- `criteria.has_gold.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:iron_blast_furnace_to_gold_blast_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_gold"]
- `rewards.recipes` = ["ironsmelters:iron_blast_furnace_to_gold_blast_furnace"]

### `data/ironsmelters/advancement/recipes/decorations/iron_furnace_to_gold_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_gold.conditions.items[0].items` = "#c:ingots/gold"
- `criteria.has_gold.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:iron_furnace_to_gold_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_gold"]
- `rewards.recipes` = ["ironsmelters:iron_furnace_to_gold_furnace"]

### `data/ironsmelters/advancement/recipes/decorations/iron_smoker_to_gold_smoker.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_gold.conditions.items[0].items` = "#c:ingots/gold"
- `criteria.has_gold.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:iron_smoker_to_gold_smoker"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_gold"]
- `rewards.recipes` = ["ironsmelters:iron_smoker_to_gold_smoker"]

### `data/ironsmelters/advancement/recipes/decorations/iron_to_gold_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_furnace.conditions.items[0].items` = "#c:player_workstations/furnaces"
- `criteria.has_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_gold.conditions.items[0].items` = "#c:ingots/gold"
- `criteria.has_gold.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:iron_to_gold_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_gold", "has_furnace"]
- `rewards.recipes` = ["ironsmelters:iron_to_gold_upgrade"]

### `data/ironsmelters/advancement/recipes/decorations/smoker_to_copper_smoker.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_copper.conditions.items[0].items` = "#c:ingots/copper"
- `criteria.has_copper.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:smoker_to_copper_smoker"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_copper"]
- `rewards.recipes` = ["ironsmelters:smoker_to_copper_smoker"]

### `data/ironsmelters/advancement/recipes/decorations/smoker_to_iron_smoker.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_iron.conditions.items[0].items` = "#c:ingots/iron"
- `criteria.has_iron.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:smoker_to_iron_smoker"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_iron"]
- `rewards.recipes` = ["ironsmelters:smoker_to_iron_smoker"]

### `data/ironsmelters/advancement/recipes/decorations/stone_to_copper_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_copper.conditions.items[0].items` = "#c:ingots/copper"
- `criteria.has_copper.trigger` = "minecraft:inventory_changed"
- `criteria.has_furnace.conditions.items[0].items` = "#c:player_workstations/furnaces"
- `criteria.has_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:stone_to_copper_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_copper", "has_furnace"]
- `rewards.recipes` = ["ironsmelters:stone_to_copper_upgrade"]

### `data/ironsmelters/advancement/recipes/decorations/stone_to_iron_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_furnace.conditions.items[0].items` = "#c:player_workstations/furnaces"
- `criteria.has_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_iron.conditions.items[0].items` = "#c:ingots/iron"
- `criteria.has_iron.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ironsmelters:stone_to_iron_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_the_recipe", "has_iron", "has_furnace"]
- `rewards.recipes` = ["ironsmelters:stone_to_iron_upgrade"]

### `data/ironsmelters/recipe/blast_furnace_to_copper_blast_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.I.item` = "minecraft:blast_furnace"
- `key.O.tag` = "c:ingots/copper"
- `pattern` = ["OOO", "OIO", "OOO"]
- `result.count` = 1
- `result.id` = "ironsmelters:copper_blast_furnace"

### `data/ironsmelters/recipe/blast_furnace_to_iron_blast_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.I.item` = "minecraft:blast_furnace"
- `key.O.tag` = "c:ingots/iron"
- `pattern` = ["OOO", "OIO", "OOO"]
- `result.count` = 1
- `result.id` = "ironsmelters:iron_blast_furnace"

### `data/ironsmelters/recipe/copper_blast_furnace_to_iron_blast_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.G.tag` = "c:glass_blocks"
- `key.I.item` = "ironsmelters:copper_blast_furnace"
- `key.O.tag` = "c:ingots/iron"
- `pattern` = ["OOO", "GIG", "OOO"]
- `result.count` = 1
- `result.id` = "ironsmelters:iron_blast_furnace"

### `data/ironsmelters/recipe/copper_furnace_to_iron_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.G.tag` = "c:glass_blocks"
- `key.I.item` = "ironsmelters:copper_furnace"
- `key.O.tag` = "c:ingots/iron"
- `pattern` = ["OOO", "GIG", "OOO"]
- `result.count` = 1
- `result.id` = "ironsmelters:iron_furnace"

### `data/ironsmelters/recipe/copper_smoker_to_iron_smoker.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.G.tag` = "c:glass_blocks"
- `key.I.item` = "ironsmelters:copper_smoker"
- `key.O.tag` = "c:ingots/iron"
- `pattern` = ["OOO", "GIG", "OOO"]
- `result.count` = 1
- `result.id` = "ironsmelters:iron_smoker"

### `data/ironsmelters/recipe/copper_to_iron_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.G.tag` = "c:glass_blocks"
- `key.I.tag` = "c:ingots/iron"
- `key.S.tag` = "c:cobblestones"
- `pattern` = ["III", "GSG", "III"]
- `result.count` = 1
- `result.id` = "ironsmelters:upgrade_copper_to_iron"

### `data/ironsmelters/recipe/diamond_blast_furnace_to_obsidian_blast_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.I.item` = "ironsmelters:diamond_blast_furnace"
- `key.O.tag` = "c:obsidians/normal"
- `pattern` = ["OOO", "OIO", "OOO"]
- `result.count` = 1
- `result.id` = "ironsmelters:obsidian_blast_furnace"

### `data/ironsmelters/recipe/diamond_furnace_to_obsidian_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.I.item` = "ironsmelters:diamond_furnace"
- `key.O.tag` = "c:obsidians/normal"
- `pattern` = ["OOO", "OIO", "OOO"]
- `result.count` = 1
- `result.id` = "ironsmelters:obsidian_furnace"

### `data/ironsmelters/recipe/diamond_smoker_to_obsidian_smoker.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.I.item` = "ironsmelters:diamond_smoker"
- `key.O.tag` = "c:obsidians/normal"
- `pattern` = ["OOO", "OIO", "OOO"]
- `result.count` = 1
- `result.id` = "ironsmelters:obsidian_smoker"

### `data/ironsmelters/recipe/diamond_to_obsidian_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.I.tag` = "c:obsidians/normal"
- `key.S.tag` = "c:cobblestones"
- `pattern` = ["III", "ISI", "III"]
- `result.count` = 1
- `result.id` = "ironsmelters:upgrade_diamond_to_obsidian"

### `data/ironsmelters/recipe/furnace_to_copper_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.I.item` = "minecraft:furnace"
- `key.O.tag` = "c:ingots/copper"
- `pattern` = ["OOO", "OIO", "OOO"]
- `result.count` = 1
- `result.id` = "ironsmelters:copper_furnace"

### `data/ironsmelters/recipe/furnace_to_iron_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.I.item` = "minecraft:furnace"
- `key.O.tag` = "c:ingots/iron"
- `pattern` = ["OOO", "OIO", "OOO"]
- `result.count` = 1
- `result.id` = "ironsmelters:iron_furnace"

### `data/ironsmelters/recipe/gold_blast_furnace_to_diamond_blast_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.G.tag` = "c:glass_blocks"
- `key.I.item` = "ironsmelters:gold_blast_furnace"
- `key.O.tag` = "c:gems/diamond"
- `pattern` = ["OOO", "GIG", "OOO"]
- `result.count` = 1
- `result.id` = "ironsmelters:diamond_blast_furnace"

### `data/ironsmelters/recipe/gold_furnace_to_diamond_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.G.tag` = "c:glass_blocks"
- `key.I.item` = "ironsmelters:gold_furnace"
- `key.O.tag` = "c:gems/diamond"
- `pattern` = ["OOO", "GIG", "OOO"]
- `result.count` = 1
- `result.id` = "ironsmelters:diamond_furnace"

### `data/ironsmelters/recipe/gold_smoker_to_diamond_smoker.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.G.tag` = "c:glass_blocks"
- `key.I.item` = "ironsmelters:gold_smoker"
- `key.O.tag` = "c:gems/diamond"
- `pattern` = ["OOO", "GIG", "OOO"]
- `result.count` = 1
- `result.id` = "ironsmelters:diamond_smoker"

### `data/ironsmelters/recipe/gold_to_diamond_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.G.tag` = "c:glass_blocks"
- `key.I.tag` = "c:gems/diamond"
- `key.S.tag` = "c:cobblestones"
- `pattern` = ["III", "GSG", "III"]
- `result.count` = 1
- `result.id` = "ironsmelters:upgrade_gold_to_diamond"

### `data/ironsmelters/recipe/iron_blast_furnace_to_gold_blast_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.I.item` = "ironsmelters:iron_blast_furnace"
- `key.O.tag` = "c:ingots/gold"
- `pattern` = ["OOO", "OIO", "OOO"]
- `result.count` = 1
- `result.id` = "ironsmelters:gold_blast_furnace"

### `data/ironsmelters/recipe/iron_furnace_to_gold_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.I.item` = "ironsmelters:iron_furnace"
- `key.O.tag` = "c:ingots/gold"
- `pattern` = ["OOO", "OIO", "OOO"]
- `result.count` = 1
- `result.id` = "ironsmelters:gold_furnace"

### `data/ironsmelters/recipe/iron_smoker_to_gold_smoker.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.I.item` = "ironsmelters:iron_smoker"
- `key.O.tag` = "c:ingots/gold"
- `pattern` = ["OOO", "OIO", "OOO"]
- `result.count` = 1
- `result.id` = "ironsmelters:gold_smoker"

### `data/ironsmelters/recipe/iron_to_gold_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.I.tag` = "c:ingots/gold"
- `key.S.tag` = "c:cobblestones"
- `pattern` = ["III", "ISI", "III"]
- `result.count` = 1
- `result.id` = "ironsmelters:upgrade_iron_to_gold"

### `data/ironsmelters/recipe/smoker_to_copper_smoker.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.I.item` = "minecraft:smoker"
- `key.O.tag` = "c:ingots/copper"
- `pattern` = ["OOO", "OIO", "OOO"]
- `result.count` = 1
- `result.id` = "ironsmelters:copper_smoker"

### `data/ironsmelters/recipe/smoker_to_iron_smoker.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.I.item` = "minecraft:smoker"
- `key.O.tag` = "c:ingots/iron"
- `pattern` = ["OOO", "OIO", "OOO"]
- `result.count` = 1
- `result.id` = "ironsmelters:iron_smoker"

### `data/ironsmelters/recipe/stone_to_copper_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.I.tag` = "c:ingots/copper"
- `key.S.tag` = "c:cobblestones"
- `pattern` = ["III", "ISI", "III"]
- `result.count` = 1
- `result.id` = "ironsmelters:upgrade_stone_to_copper"

### `data/ironsmelters/recipe/stone_to_iron_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `key.I.tag` = "c:ingots/iron"
- `key.S.tag` = "c:cobblestones"
- `pattern` = ["III", "ISI", "III"]
- `result.count` = 1
- `result.id` = "ironsmelters:upgrade_stone_to_iron"

### `data/minecraft/tags/block/features_cannot_replace.json`

- `values` = ["ironsmelters:gold_furnace", "ironsmelters:copper_furnace", "ironsmelters:obsidian_furnace", "ironsmelters:copper_blast_furnace", "ironsmelters:gold_blast_furnace", "ironsmelters:gold_smoker", "ironsmelters:copper_smoker", "ironsmelters:iron_furnace", "ironsmelters:diamond_furnace", "ironsmelters:i…

### `data/minecraft/tags/block/mineable/pickaxe.json`

- `values` = ["ironsmelters:gold_furnace", "ironsmelters:copper_furnace", "ironsmelters:obsidian_furnace", "ironsmelters:copper_blast_furnace", "ironsmelters:gold_blast_furnace", "ironsmelters:gold_smoker", "ironsmelters:copper_smoker", "ironsmelters:iron_furnace", "ironsmelters:diamond_furnace", "ironsmelters:i…

## Testi nel codice


### `com/blamejared/ironsmelters/ISCommon.class`

- "UPGRADE"
- "com/blamejared/ironsmelters/component/Upgrade"
- "upgrade"
- "UPGRADES"
- "Lcom/blamejared/ironsmelters/component/Upgrade;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `com/blamejared/ironsmelters/IronSmelters.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `com/blamejared/ironsmelters/api/SmelterType.class`

- "upgradeFrom"
- "id;displayName;config;upgradeFrom"
- "java/lang/invoke/StringConcatFactory"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `com/blamejared/ironsmelters/block/ISAbstractFurnaceBlock.class`

- "furnaceMultiplier"
- "java/lang/invoke/StringConcatFactory"

### `com/blamejared/ironsmelters/block/ISBlastFurnaceBlock.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `com/blamejared/ironsmelters/block/ISBlocks.class`

- "java/lang/invoke/StringConcatFactory"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `com/blamejared/ironsmelters/block/ISFurnaceBlock.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `com/blamejared/ironsmelters/block/ISSmokerBlock.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `com/blamejared/ironsmelters/block/entity/AbstractISBlockEntity.class`

- "furnaceMultiplier"
- "getCookingProgress"
- "setCookingProgress"
- "getCookingTotalTime"
- "callGetTotalCookTime"
- "setCookingTotalTime"
- "Lnet/minecraft/world/item/crafting/RecipeType<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "(Lnet/minecraft/world/level/block/entity/BlockEntityType<*>;Lnet/minecraft/core/BlockPos;Lnet/minecraft/world/level/block/state/BlockState;Lnet/minecraft/world/item/crafting/RecipeType<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;)V"
- "fuelItem"
- "fuel"
- "hasFuel"

### `com/blamejared/ironsmelters/block/entity/ISBlastFurnaceBlockEntity.class`

- "fuel"

### `com/blamejared/ironsmelters/block/entity/ISBlockEntityTypes.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `com/blamejared/ironsmelters/block/entity/ISSmokerBlockEntity.class`

- "fuel"

### `com/blamejared/ironsmelters/component/ISComponents.class`

- "com/blamejared/ironsmelters/component/Upgrade"
- "upgrade"
- "UPGRADE"
- "Lcom/blamejared/ironsmelters/registry/RegistryObject<Lnet/minecraft/core/component/DataComponentType<Lcom/blamejared/ironsmelters/component/Upgrade;>;>;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `com/blamejared/ironsmelters/component/Upgrade$1.class`

- "com/blamejared/ironsmelters/component/Upgrade$1"
- "Upgrade.java"
- "com/blamejared/ironsmelters/component/Upgrade"

### `com/blamejared/ironsmelters/component/Upgrade.class`

- "com/blamejared/ironsmelters/component/Upgrade"
- "com/blamejared/ironsmelters/component/Upgrade$1"
- "(Lcom/blamejared/ironsmelters/component/Upgrade;)Ljava/lang/String;"
- "(Lcom/blamejared/ironsmelters/component/Upgrade;)I"
- "(Lcom/blamejared/ironsmelters/component/Upgrade;Ljava/lang/Object;)Z"
- "Lcom/mojang/serialization/Codec<Lcom/blamejared/ironsmelters/component/Upgrade;>;"
- "Lcom/blamejared/ironsmelters/component/Upgrade;"
- "upgrade"
- "Upgrade.java"
- "(Lcom/blamejared/ironsmelters/component/Upgrade;)Ljava/util/Optional;"
- "(Lcom/blamejared/ironsmelters/component/Upgrade;)Lcom/blamejared/ironsmelters/api/SmelterType;"
- "(Lcom/blamejared/ironsmelters/component/Upgrade;)Ljava/lang/Boolean;"
- "(Ljava/util/Optional;Lcom/blamejared/ironsmelters/api/SmelterType;Ljava/lang/Boolean;)Lcom/blamejared/ironsmelters/component/Upgrade;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `com/blamejared/ironsmelters/config/SmelterConfig.class`

- "furnaceMultiplier"
- "blastFurnaceMultiplier"
- "smokerMultiplier"
- "Furnace Speed Multiplier"
- "Blast Furnace Speed Multiplier"
- "Smoker Speed Multiplier"
- "SmelterConfig[furnaceMultiplier=\u0001, blastFurnaceMultiplier=\u0001, smokerMultiplier=\u0001]"
- "java/lang/invoke/StringConcatFactory"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `com/blamejared/ironsmelters/data/ISBlockStatesProvider.class`

- "net/neoforged/neoforge/client/model/generators/BlockStateProvider"
- "()Lnet/neoforged/neoforge/client/model/generators/BlockModelProvider;"
- "net/neoforged/neoforge/client/model/generators/BlockModelProvider"
- "(Ljava/lang/String;Lnet/minecraft/resources/ResourceLocation;Lnet/minecraft/resources/ResourceLocation;Lnet/minecraft/resources/ResourceLocation;)Lnet/neoforged/neoforge/client/model/generators/ModelBuilder;"
- "net/neoforged/neoforge/client/model/generators/BlockModelBuilder"
- "(Lnet/neoforged/neoforge/client/model/generators/BlockModelBuilder;Lnet/neoforged/neoforge/client/model/generators/BlockModelBuilder;)Ljava/util/function/Function;"
- "()Lnet/neoforged/neoforge/client/model/generators/ItemModelProvider;"
- "net/neoforged/neoforge/client/model/generators/ItemModelProvider"
- "(Lnet/minecraft/world/level/block/Block;)Lnet/neoforged/neoforge/client/model/generators/ItemModelBuilder;"
- "(Ljava/lang/String;Lnet/minecraft/resources/ResourceLocation;Lnet/minecraft/resources/ResourceLocation;Lnet/minecraft/resources/ResourceLocation;Lnet/minecraft/resources/ResourceLocation;)Lnet/neoforged/neoforge/client/model/generators/ModelBuilder;"
- "Lnet/neoforged/neoforge/client/model/generators/BlockModelBuilder;"
- "(Lnet/neoforged/neoforge/client/model/generators/BlockModelBuilder;Lnet/neoforged/neoforge/client/model/generators/BlockModelBuilder;Lnet/minecraft/world/level/block/state/BlockState;)Lnet/neoforged/neoforge/client/model/generators/ModelFile;"
- "(Lnet/minecraft/world/level/block/state/BlockState;)Lnet/neoforged/neoforge/client/model/generators/ModelFile;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `com/blamejared/ironsmelters/data/ISBlockTags.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `com/blamejared/ironsmelters/data/ISData.class`

- "getGenerator"
- "()Lnet/minecraft/data/DataGenerator;"
- "net/minecraft/data/DataGenerator"
- "generator"
- "Lnet/minecraft/data/DataGenerator;"

### `com/blamejared/ironsmelters/data/ISLangProvider.class`

- "ironsmelters.upgrade.text"
- "Upgrades a Smelter from %s to %s"
- "upgradeFrom"
- "%s to %s Smelter Upgrade"
- "upgrade"
- "upgrade_\u0001_to_\u0001"
- "java/lang/invoke/StringConcatFactory"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `com/blamejared/ironsmelters/data/ISLoot.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `com/blamejared/ironsmelters/data/ISRecipesProvider.class`

- "UPGRADES"
- "stone_to_copper_upgrade"
- "stone_to_iron_upgrade"
- "copper_to_iron_upgrade"
- "iron_to_gold_upgrade"
- "gold_to_diamond_upgrade"
- "diamond_to_obsidian_upgrade"
- "java/lang/invoke/StringConcatFactory"

### `com/blamejared/ironsmelters/data/IsItemModelProvider.class`

- "net/neoforged/neoforge/client/model/generators/ItemModelProvider"
- "UPGRADES"
- "(Lnet/minecraft/world/item/Item;)Lnet/neoforged/neoforge/client/model/generators/ItemModelBuilder;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `com/blamejared/ironsmelters/item/ISItems.class`

- "upgradeFrom"
- "com/blamejared/ironsmelters/component/Upgrade"
- "(Lcom/blamejared/ironsmelters/component/Upgrade;)Ljava/util/function/Function;"
- "com/blamejared/ironsmelters/item/UpgradeItem"
- "UPGRADE"
- "()Lnet/minecraft/world/item/CreativeModeTab$DisplayItemsGenerator;"
- "(Lnet/minecraft/world/item/CreativeModeTab$DisplayItemsGenerator;)Lnet/minecraft/world/item/CreativeModeTab$Builder;"
- "UPGRADES"
- "upgradeComponent"
- "Lcom/blamejared/ironsmelters/component/Upgrade;"
- "upgrade"
- "(Lcom/blamejared/ironsmelters/component/Upgrade;Lnet/minecraft/world/item/Item$Properties;)Lnet/minecraft/world/item/Item;"
- "upgrade_\u0001_to_\u0001"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "java/lang/invoke/StringConcatFactory"
- "net/minecraft/world/item/CreativeModeTab$DisplayItemsGenerator"
- "DisplayItemsGenerator"

### `com/blamejared/ironsmelters/item/UpgradeItem.class`

- "UPGRADE"
- "com/blamejared/ironsmelters/component/Upgrade"
- "ironsmelters.upgrade.text"
- "com/blamejared/ironsmelters/item/UpgradeItem"
- "Lcom/blamejared/ironsmelters/item/UpgradeItem;"
- "upgrade"
- "Lcom/blamejared/ironsmelters/component/Upgrade;"
- "UpgradeItem.java"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `com/blamejared/ironsmelters/mixin/AccessAbstractFurnaceBlockEntity.class`

- "callGetTotalCookTime"
- "getTotalCookTime"
- "()Lnet/minecraft/world/item/crafting/RecipeManager$CachedCheck<Lnet/minecraft/world/item/crafting/SingleRecipeInput;+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "getCookingProgress"
- "cookingProgress"
- "setCookingProgress"
- "getCookingTotalTime"
- "cookingTotalTime"
- "setCookingTotalTime"

### `com/blamejared/ironsmelters/platform/NeoForgePlatformHelper.class`

- "factory"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `com/blamejared/ironsmelters/platform/NeoForgeRegistrationFactory$Provider$1.class`

- "com/blamejared/ironsmelters/platform/NeoForgeRegistrationFactory$Provider$1"
- "(Lcom/blamejared/ironsmelters/platform/NeoForgeRegistrationFactory$Provider;Lnet/neoforged/neoforge/registries/DeferredHolder;)V"
- "Lcom/blamejared/ironsmelters/platform/NeoForgeRegistrationFactory$Provider$1;"
- "Lcom/blamejared/ironsmelters/platform/NeoForgeRegistrationFactory$Provider;"
- "NeoForgeRegistrationFactory.java"
- "com/blamejared/ironsmelters/platform/NeoForgeRegistrationFactory$Provider"
- "com/blamejared/ironsmelters/platform/NeoForgeRegistrationFactory"

### `com/blamejared/ironsmelters/platform/NeoForgeRegistrationFactory$Provider.class`

- "com/blamejared/ironsmelters/platform/NeoForgeRegistrationFactory$Provider"
- "com/blamejared/ironsmelters/platform/NeoForgeRegistrationFactory$Provider$1"
- "(Lcom/blamejared/ironsmelters/platform/NeoForgeRegistrationFactory$Provider;Lnet/neoforged/neoforge/registries/DeferredHolder;)V"
- "Lcom/blamejared/ironsmelters/platform/NeoForgeRegistrationFactory$Provider;"
- "Lcom/blamejared/ironsmelters/platform/NeoForgeRegistrationFactory$Provider<TT;>;"
- "NeoForgeRegistrationFactory.java"
- "com/blamejared/ironsmelters/platform/NeoForgeRegistrationFactory"

### `com/blamejared/ironsmelters/platform/NeoForgeRegistrationFactory.class`

- "com/blamejared/ironsmelters/platform/NeoForgeRegistrationFactory$Provider"
- "com/blamejared/ironsmelters/platform/NeoForgeRegistrationFactory"
- "com/blamejared/ironsmelters/registry/RegistrationProvider$Factory"
- "Lcom/blamejared/ironsmelters/platform/NeoForgeRegistrationFactory;"
- "NeoForgeRegistrationFactory.java"
- "Lcom/blamejared/ironsmelters/registry/RegistrationProvider$Factory;"
- "com/blamejared/ironsmelters/platform/NeoForgeRegistrationFactory$Provider$1"
- "java/lang/invoke/StringConcatFactory"
- "Factory"

### `com/blamejared/ironsmelters/platform/Services.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "java/lang/invoke/StringConcatFactory"

### `com/blamejared/ironsmelters/registry/RegistrationProvider$Factory.class`

- "com/blamejared/ironsmelters/registry/RegistrationProvider$Factory"
- "Lcom/blamejared/ironsmelters/registry/RegistrationProvider$Factory;"
- "Factory"

### `com/blamejared/ironsmelters/registry/RegistrationProvider.class`

- "com/blamejared/ironsmelters/registry/RegistrationProvider$Factory"
- "Lcom/blamejared/ironsmelters/registry/RegistrationProvider$Factory;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "Factory"
