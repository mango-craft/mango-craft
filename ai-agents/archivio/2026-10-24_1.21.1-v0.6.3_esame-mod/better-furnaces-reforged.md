# Better Furnaces Reforged (better-furnaces-reforged)

File generato da `scripts/esamina.py` (workflow "Esamina mod"): la mod **non** è nel pack. Non modificarlo a mano.

- Versione: **1.21.1-1.1.2518.1+neoforge** (beta, 2025-04-25), file `BetterFurnacesReforged-1.21.1-1.1.2518.1-neoforge.jar`, id versione `YUwxtJ8j`
- Licenza su Modrinth: MIT · download: 513242
- Filtro dei valori: `(recipe|recipes|tags/item|tags/block)/` · filtro dei testi del codice: `(?i)^(.*(speed|cook|tier|augment|upgrade|generator|factory|fuel|multiplier|energy|rainbow).*)$`

## Mod nel file e dipendenze dichiarate

- `betterfurnacesreforged` 1.1.2518.1
  - required: `minecraft` [1.21,1.21.1]
  - required: `factory_api` [2.2.3.2518.0,)

## Cartelle di dati (file .json)

- `betterfurnacesreforged:advancement`: 6
- `betterfurnacesreforged:advancement/recipes`: 49
- `betterfurnacesreforged:advancements`: 6
- `betterfurnacesreforged:advancements/recipes`: 49
- `betterfurnacesreforged:recipe`: 34
- `betterfurnacesreforged:recipe/rock_generation`: 6
- `betterfurnacesreforged:recipes`: 34
- `betterfurnacesreforged:recipes/rock_generation`: 6
- `betterfurnacesreforged:tags/block`: 3
- `betterfurnacesreforged:tags/block/tier`: 10
- `betterfurnacesreforged:tags/blocks`: 3
- `betterfurnacesreforged:tags/blocks/tier`: 10
- `minecraft:tags/block`: 3
- `minecraft:tags/block/mineable`: 1
- `minecraft:tags/blocks`: 3
- `minecraft:tags/blocks/mineable`: 1
- `ultimatefurnaces:recipe`: 28
- `ultimatefurnaces:recipes`: 28

## Valori dei file filtrati


### `data/betterfurnacesreforged/advancement/recipes/advanced_fuel_efficiency_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:fuel_efficiency_upgrade"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:advanced_fuel_efficiency_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:advanced_fuel_efficiency_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/advanced_ore_processing_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:ore_processing_upgrade"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:advanced_ore_processing_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:advanced_ore_processing_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/amethyst_diamond_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:amethyst_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:amethyst_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:amethyst_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/amethyst_forge.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:amethyst_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:amethyst_forge"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnacesd:amethyst_forge"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/amethyst_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:gold_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:amethyst_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:amethyst_furnace"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/amethyst_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:gold_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:amethyst_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:amethyst_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/blasting_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "minecraft:smooth_stone"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:blasting_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:blasting_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/cobblestone_generator.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "minecraft:smooth_stone"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:cobblestone_generator"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:cobblestone_generator"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/color_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:gold_conductor_block"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:color_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:color_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/copper_forge.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:copper_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:copper_forge"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:copper_forge"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/copper_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "minecraft:furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:copper_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:copper_furnace"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/copper_iron_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:copper_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:copper_iron_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:copper_iron_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/copper_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "minecraft:furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:copper_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:copper_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/diamond_forge.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:diamond_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:diamond_forge"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:diamond_forge"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/diamond_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:gold_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:diamond_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:diamond_furnace"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/diamond_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:gold_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:diamond_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:diamond_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/extreme_forge.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:extreme_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:extreme_forge"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:extreme_forge"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/extreme_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:netherhot_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:extreme_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:extreme_furnace"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/extreme_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:netherhot_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:extreme_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:extreme_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/factory_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "minecraft:diamond"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:factory_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:factory_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/fuel_efficiency_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].tag` = "minecraft:coals"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:fuel_efficiency_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:fuel_efficiency_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/fuel_verifier.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].tag` = "minecraft:coals"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:fuel_verifier"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:fuel_verifier"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/gold_conductor_block.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "minecraft:gold_ingot"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:gold_conductor_block"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:gold_conductor_block"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/gold_forge.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:gold_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:gold_forge"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:gold_forge"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/gold_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:iron_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:gold_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:gold_furnace"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/gold_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:iron_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:gold_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:gold_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/iron_conductor_block.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "minecraft:iron_ingot"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:iron_conductor_block"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:iron_conductor_block"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/iron_forge.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:iron_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:iron_forge"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:iron_forge"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/iron_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "minecraft:furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:iron_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:iron_furnace"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/iron_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "minecraft:furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:iron_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:iron_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/netherhot_conductor_block.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "minecraft:magma_cream"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:netherhot_conductor_block"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:netherhot_conductor_block"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/netherhot_forge.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:netherhot_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:netherhot_forge"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:netherhot_forge"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/netherhot_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:diamond_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:netherhot_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:netherhot_furnace"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/netherhot_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:diamond_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:netherhot_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:netherhot_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/ore_processing_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:iron_conductor_block"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:ore_processing_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:ore_processing_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/platinum_forge.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:platinum_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:platinum_forge"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:platinum_forge"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/platinum_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:diamond_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:platinum_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:platinum_furnace"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/platinum_netherhot_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:platinum_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:netherhot_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:netherhot_furnace"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/platinum_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:diamond_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:platinum_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:platinum_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/raw_ore_processing_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:netherhot_conductor_block"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:raw_ore_processing_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:raw_ore_processing_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/smoking_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].tag` = "minecraft:logs"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:smoking_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:smoking_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/steel_forge.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:steel_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:steel_forge"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:steel_forge"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/steel_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:iron_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:steel_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:steel_furnace"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/steel_gold_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:steel_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:steel_gold_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:steel_gold_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/steel_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:iron_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:steel_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:steel_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/ultimate_forge.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:ultimate_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:ultimate_forge"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:ultimate_forge"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/ultimate_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:extreme_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:ultimate_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:ultimate_furnace"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/ultimate_ore_processing_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:advanced_ore_processing_upgrade"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:ultimate_ore_processing_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:ultimate_ore_processing_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancement/recipes/ultimate_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:extreme_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:ultimate_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:ultimate_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/advanced_fuel_efficiency_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:fuel_efficiency_upgrade"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:advanced_fuel_efficiency_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:advanced_fuel_efficiency_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/advanced_ore_processing_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:ore_processing_upgrade"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:advanced_ore_processing_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:advanced_ore_processing_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/amethyst_diamond_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:amethyst_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:amethyst_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:amethyst_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/amethyst_forge.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:amethyst_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:amethyst_forge"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnacesd:amethyst_forge"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/amethyst_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:gold_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:amethyst_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:amethyst_furnace"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/amethyst_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:gold_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:amethyst_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:amethyst_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/blasting_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "minecraft:smooth_stone"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:blasting_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:blasting_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/cobblestone_generator.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "minecraft:smooth_stone"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:cobblestone_generator"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:cobblestone_generator"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/color_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:gold_conductor_block"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:color_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:color_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/copper_forge.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:copper_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:copper_forge"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:copper_forge"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/copper_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "minecraft:furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:copper_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:copper_furnace"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/copper_iron_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:copper_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:copper_iron_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:copper_iron_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/copper_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "minecraft:furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:copper_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:copper_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/diamond_forge.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:diamond_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:diamond_forge"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:diamond_forge"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/diamond_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:gold_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:diamond_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:diamond_furnace"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/diamond_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:gold_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:diamond_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:diamond_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/extreme_forge.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:extreme_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:extreme_forge"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:extreme_forge"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/extreme_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:netherhot_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:extreme_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:extreme_furnace"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/extreme_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:netherhot_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:extreme_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:extreme_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/factory_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "minecraft:diamond"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:factory_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:factory_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/fuel_efficiency_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].tag` = "minecraft:coals"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:fuel_efficiency_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:fuel_efficiency_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/fuel_verifier.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].tag` = "minecraft:coals"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:fuel_verifier"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:fuel_verifier"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/gold_conductor_block.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "minecraft:gold_ingot"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:gold_conductor_block"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:gold_conductor_block"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/gold_forge.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:gold_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:gold_forge"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:gold_forge"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/gold_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:iron_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:gold_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:gold_furnace"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/gold_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:iron_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:gold_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:gold_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/iron_conductor_block.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "minecraft:iron_ingot"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:iron_conductor_block"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:iron_conductor_block"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/iron_forge.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:iron_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:iron_forge"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:iron_forge"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/iron_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "minecraft:furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:iron_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:iron_furnace"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/iron_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "minecraft:furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:iron_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:iron_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/netherhot_conductor_block.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "minecraft:magma_cream"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:netherhot_conductor_block"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:netherhot_conductor_block"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/netherhot_forge.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:netherhot_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:netherhot_forge"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:netherhot_forge"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/netherhot_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:diamond_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:netherhot_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:netherhot_furnace"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/netherhot_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:diamond_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:netherhot_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:netherhot_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/ore_processing_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:iron_conductor_block"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:ore_processing_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:ore_processing_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/platinum_forge.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:platinum_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:platinum_forge"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:platinum_forge"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/platinum_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:diamond_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:platinum_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:platinum_furnace"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/platinum_netherhot_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:platinum_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:netherhot_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:netherhot_furnace"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/platinum_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:diamond_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:platinum_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:platinum_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/raw_ore_processing_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:netherhot_conductor_block"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:raw_ore_processing_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:raw_ore_processing_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/smoking_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].tag` = "minecraft:logs"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:smoking_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:smoking_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/steel_forge.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:steel_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:steel_forge"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:steel_forge"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/steel_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:iron_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:steel_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:steel_furnace"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/steel_gold_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:steel_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:steel_gold_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:steel_gold_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/steel_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:iron_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:steel_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:steel_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/ultimate_forge.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:ultimate_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:ultimate_forge"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:ultimate_forge"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/ultimate_furnace.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:extreme_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:ultimate_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:ultimate_furnace"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/ultimate_ore_processing_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:advanced_ore_processing_upgrade"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "betterfurnacesreforged:ultimate_ore_processing_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["betterfurnacesreforged:ultimate_ore_processing_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/advancements/recipes/ultimate_upgrade.json`

- `parent` = "minecraft:recipes/root"
- `criteria.has_ingredient.conditions.items[0].item` = "betterfurnacesreforged:extreme_furnace"
- `criteria.has_ingredient.trigger` = "minecraft:inventory_changed"
- `criteria.has_the_recipe.conditions.recipe` = "ultimatefurnaces:ultimate_upgrade"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `requirements[0]` = ["has_ingredient", "has_the_recipe"]
- `rewards.recipes` = ["ultimatefurnaces:ultimate_upgrade"]
- `sends_telemetry_event` = false

### `data/betterfurnacesreforged/recipe/advanced_fuel_efficiency_upgrade.json`

- `pattern` = ["010", "343", "636"]
- `result.id` = "betterfurnacesreforged:advanced_fuel_efficiency_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:diamond"
- `key.1.item` = "minecraft:ghast_tear"
- `key.3.item` = "minecraft:ender_eye"
- `key.4.item` = "betterfurnacesreforged:fuel_efficiency_upgrade"
- `key.6.item` = "minecraft:diamond"

### `data/betterfurnacesreforged/recipe/advanced_ore_processing_upgrade.json`

- `pattern` = ["010", "343", "070"]
- `result.id` = "betterfurnacesreforged:advanced_ore_processing_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:diamond"
- `key.1.item` = "minecraft:piston"
- `key.3.item` = "minecraft:obsidian"
- `key.4.item` = "betterfurnacesreforged:ore_processing_upgrade"
- `key.7.item` = "minecraft:piston"

### `data/betterfurnacesreforged/recipe/autoinput_upgrade.json`

- `pattern` = ["131", "121", "131"]
- `result.id` = "betterfurnacesreforged:autoinput_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.1.item` = "minecraft:gold_ingot"
- `key.2.item` = "minecraft:diamond"
- `key.3.item` = "betterfurnacesreforged:piping_upgrade"

### `data/betterfurnacesreforged/recipe/autooutput_upgrade.json`

- `pattern` = ["131", "424", "131"]
- `result.id` = "betterfurnacesreforged:autooutput_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.1.item` = "minecraft:iron_ingot"
- `key.2.tag` = "c:glass_blocks"
- `key.3.item` = "betterfurnacesreforged:piping_upgrade"
- `key.4.item` = "minecraft:gold_ingot"

### `data/betterfurnacesreforged/recipe/blasting_upgrade.json`

- `pattern` = ["III", "IXI", "###"]
- `result.id` = "betterfurnacesreforged:blasting_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.X.item` = "betterfurnacesreforged:iron_conductor_block"
- `key.I.item` = "minecraft:iron_ingot"
- `key.#.item` = "minecraft:smooth_stone"

### `data/betterfurnacesreforged/recipe/cobblestone_generator.json`

- `pattern` = [" 1 ", "343", "676"]
- `result.id` = "betterfurnacesreforged:cobblestone_generator"
- `type` = "minecraft:crafting_shaped"
- `key.1.item` = "minecraft:coal_block"
- `key.3.item` = "minecraft:iron_ingot"
- `key.4.item` = "minecraft:bucket"
- `key.6.item` = "minecraft:smooth_stone"
- `key.7.item` = "betterfurnacesreforged:fuel_verifier"

### `data/betterfurnacesreforged/recipe/color_upgrade.json`

- `pattern` = ["012", "345", "678"]
- `result.id` = "betterfurnacesreforged:color_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:white_dye"
- `key.1.item` = "minecraft:black_dye"
- `key.2.item` = "minecraft:brown_dye"
- `key.3.item` = "minecraft:red_dye"
- `key.4.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.5.item` = "minecraft:yellow_dye"
- `key.6.item` = "minecraft:green_dye"
- `key.7.item` = "minecraft:blue_dye"
- `key.8.item` = "minecraft:pink_dye"

### `data/betterfurnacesreforged/recipe/diamond_furnace.json`

- `pattern` = ["010", "141", "010"]
- `result.id` = "betterfurnacesreforged:diamond_furnace"
- `type` = "minecraft:crafting_shaped"
- `key.0.tag` = "c:glass_blocks"
- `key.1.item` = "minecraft:diamond"
- `key.4.item` = "betterfurnacesreforged:gold_furnace"

### `data/betterfurnacesreforged/recipe/diamond_upgrade.json`

- `pattern` = ["010", "141", "010"]
- `result.id` = "betterfurnacesreforged:diamond_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.tag` = "c:glass_blocks"
- `key.1.item` = "minecraft:diamond"
- `key.4.item` = "minecraft:gold_ingot"

### `data/betterfurnacesreforged/recipe/energy_upgrade.json`

- `pattern` = ["010", "343", "010"]
- `result.id` = "betterfurnacesreforged:energy_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:gold_ingot"
- `key.1.tag` = "c:glass_blocks"
- `key.3.item` = "minecraft:redstone_block"
- `key.4.item` = "betterfurnacesreforged:netherhot_conductor_block"

### `data/betterfurnacesreforged/recipe/extreme_forge.json`

- `pattern` = ["012", "141", "676"]
- `result.id` = "betterfurnacesreforged:extreme_forge"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:netherite_ingot"
- `key.1.item` = "betterfurnacesreforged:netherhot_conductor_block"
- `key.2.item` = "minecraft:netherite_ingot"
- `key.4.item` = "betterfurnacesreforged:extreme_furnace"
- `key.6.item` = "minecraft:netherite_ingot"
- `key.7.tag` = "minecraft:soul_fire_base_blocks"

### `data/betterfurnacesreforged/recipe/extreme_furnace.json`

- `pattern` = ["010", "343", "676"]
- `result.id` = "betterfurnacesreforged:extreme_furnace"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:coal_block"
- `key.1.item` = "minecraft:ender_eye"
- `key.3.item` = "minecraft:end_crystal"
- `key.4.item` = "betterfurnacesreforged:netherhot_furnace"
- `key.6.item` = "minecraft:end_stone"
- `key.7.item` = "minecraft:nether_bricks"

### `data/betterfurnacesreforged/recipe/extreme_upgrade.json`

- `pattern` = ["010", "343", "676"]
- `result.id` = "betterfurnacesreforged:extreme_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:coal_block"
- `key.1.item` = "minecraft:ender_eye"
- `key.3.item` = "minecraft:end_crystal"
- `key.4.item` = "minecraft:magma_cream"
- `key.6.item` = "minecraft:end_stone"
- `key.7.item` = "minecraft:nether_bricks"

### `data/betterfurnacesreforged/recipe/factory_upgrade.json`

- `pattern` = ["121", "141", "131"]
- `result.id` = "betterfurnacesreforged:factory_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.1.item` = "minecraft:diamond"
- `key.2.item` = "betterfurnacesreforged:autoinput_upgrade"
- `key.3.item` = "betterfurnacesreforged:autooutput_upgrade"
- `key.4.item` = "betterfurnacesreforged:redstone_signal_upgrade"

### `data/betterfurnacesreforged/recipe/fuel_efficiency_upgrade.json`

- `pattern` = ["010", "343", "010"]
- `result.id` = "betterfurnacesreforged:fuel_efficiency_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:lapis_block"
- `key.1.item` = "minecraft:ender_pearl"
- `key.3.item` = "minecraft:ender_pearl"
- `key.4.item` = "minecraft:coal"

### `data/betterfurnacesreforged/recipe/fuel_verifier.json`

- `pattern` = ["000", "040", "000"]
- `result.id` = "betterfurnacesreforged:fuel_verifier"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:cobblestone"
- `key.4.tag` = "minecraft:coals"

### `data/betterfurnacesreforged/recipe/generator_upgrade.json`

- `pattern` = ["010", " 2 ", "010"]
- `result.id` = "betterfurnacesreforged:generator_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:iron_ingot"
- `key.1.item` = "minecraft:lightning_rod"
- `key.2.item` = "betterfurnacesreforged:energy_upgrade"

### `data/betterfurnacesreforged/recipe/gold_conductor_block.json`

- `pattern` = ["010", "141", "010"]
- `result.id` = "betterfurnacesreforged:gold_conductor_block"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:gold_ingot"
- `key.1.item` = "minecraft:iron_bars"
- `key.4.item` = "minecraft:iron_ingot"

### `data/betterfurnacesreforged/recipe/gold_furnace.json`

- `pattern` = ["010", "040"]
- `result.id` = "betterfurnacesreforged:gold_furnace"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:gold_ingot"
- `key.1.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.4.item` = "betterfurnacesreforged:iron_furnace"

### `data/betterfurnacesreforged/recipe/gold_upgrade.json`

- `pattern` = ["010", "040"]
- `result.id` = "betterfurnacesreforged:gold_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:gold_ingot"
- `key.1.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.4.item` = "minecraft:iron_ingot"

### `data/betterfurnacesreforged/recipe/iron_conductor_block.json`

- `pattern` = ["010", "141", "010"]
- `result.id` = "betterfurnacesreforged:iron_conductor_block"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:iron_ingot"
- `key.1.tag` = "c:glass_blocks"
- `key.4.item` = "minecraft:gold_ingot"

### `data/betterfurnacesreforged/recipe/iron_furnace.json`

- `pattern` = ["010", "040"]
- `result.id` = "betterfurnacesreforged:iron_furnace"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:iron_ingot"
- `key.1.item` = "betterfurnacesreforged:iron_conductor_block"
- `key.4.item` = "minecraft:furnace"

### `data/betterfurnacesreforged/recipe/iron_upgrade.json`

- `pattern` = ["010", "040"]
- `result.id` = "betterfurnacesreforged:iron_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:iron_ingot"
- `key.1.item` = "betterfurnacesreforged:iron_conductor_block"
- `key.4.item` = "minecraft:cobblestone"

### `data/betterfurnacesreforged/recipe/liquid_fuel_upgrade.json`

- `pattern` = ["0 0", "343", "030"]
- `result.id` = "betterfurnacesreforged:liquid_fuel_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:iron_ingot"
- `key.3.tag` = "c:glass_blocks"
- `key.4.item` = "minecraft:bucket"

### `data/betterfurnacesreforged/recipe/netherhot_conductor_block.json`

- `pattern` = ["010", "141", "010"]
- `result.id` = "betterfurnacesreforged:netherhot_conductor_block"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:redstone_block"
- `key.1.item` = "minecraft:blaze_rod"
- `key.4.item` = "betterfurnacesreforged:gold_conductor_block"

### `data/betterfurnacesreforged/recipe/netherhot_furnace.json`

- `pattern` = [" 1 ", "343", "676"]
- `result.id` = "betterfurnacesreforged:netherhot_furnace"
- `type` = "minecraft:crafting_shaped"
- `key.1.item` = "minecraft:tnt"
- `key.3.item` = "minecraft:diamond_block"
- `key.4.item` = "betterfurnacesreforged:netherhot_conductor_block"
- `key.6.item` = "minecraft:magma_cream"
- `key.7.item` = "betterfurnacesreforged:diamond_furnace"

### `data/betterfurnacesreforged/recipe/netherhot_upgrade.json`

- `pattern` = [" 1 ", "343", "676"]
- `result.id` = "betterfurnacesreforged:netherhot_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.1.item` = "minecraft:tnt"
- `key.3.item` = "minecraft:diamond_block"
- `key.4.item` = "betterfurnacesreforged:netherhot_conductor_block"
- `key.6.item` = "minecraft:magma_cream"
- `key.7.item` = "minecraft:diamond"

### `data/betterfurnacesreforged/recipe/ore_processing_upgrade.json`

- `pattern` = ["000", "040", "000"]
- `result.id` = "betterfurnacesreforged:ore_processing_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:stone"
- `key.4.item` = "betterfurnacesreforged:iron_conductor_block"

### `data/betterfurnacesreforged/recipe/piping_upgrade.json`

- `pattern` = ["121", "111", "121"]
- `result.id` = "betterfurnacesreforged:piping_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.1.item` = "minecraft:iron_ingot"
- `key.2.tag` = "c:glass_blocks"

### `data/betterfurnacesreforged/recipe/raw_ore_processing_upgrade.json`

- `pattern` = ["121", "030", "101"]
- `result.id` = "betterfurnacesreforged:raw_ore_processing_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:netherite_scrap"
- `key.1.item` = "betterfurnacesreforged:netherhot_conductor_block"
- `key.2.item` = "minecraft:netherite_ingot"
- `key.3.item` = "minecraft:raw_iron_block"

### `data/betterfurnacesreforged/recipe/redstone_signal_upgrade.json`

- `pattern` = ["202", "131", "202"]
- `result.id` = "betterfurnacesreforged:redstone_signal_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:comparator"
- `key.1.item` = "minecraft:repeater"
- `key.2.item` = "minecraft:redstone"
- `key.3.item` = "betterfurnacesreforged:iron_conductor_block"

### `data/betterfurnacesreforged/recipe/rock_generation/blackstone.json`

- `type` = "betterfurnacesreforged:rock_generating"
- `result.item` = "minecraft:blackstone"
- `duration` = 150

### `data/betterfurnacesreforged/recipe/rock_generation/cobbled_deepslate.json`

- `type` = "betterfurnacesreforged:rock_generating"
- `result.item` = "minecraft:cobbled_deepslate"
- `duration` = 125

### `data/betterfurnacesreforged/recipe/rock_generation/cobblestone.json`

- `type` = "betterfurnacesreforged:rock_generating"
- `result.item` = "minecraft:cobblestone"
- `duration` = 80

### `data/betterfurnacesreforged/recipe/rock_generation/deepslate.json`

- `type` = "betterfurnacesreforged:rock_generating"
- `result.item` = "minecraft:deepslate"
- `duration` = 150

### `data/betterfurnacesreforged/recipe/rock_generation/obsidian.json`

- `type` = "betterfurnacesreforged:rock_generating"
- `result.item` = "minecraft:obsidian"
- `duration` = 600

### `data/betterfurnacesreforged/recipe/rock_generation/stone.json`

- `type` = "betterfurnacesreforged:rock_generating"
- `result.item` = "minecraft:stone"
- `duration` = 100

### `data/betterfurnacesreforged/recipe/smoking_upgrade.json`

- `pattern` = [" # ", "#X#", " # "]
- `result.id` = "betterfurnacesreforged:smoking_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.X.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.#.tag` = "minecraft:logs"

### `data/betterfurnacesreforged/recipe/storage_upgrade.json`

- `pattern` = ["121", "232", "121"]
- `result.id` = "betterfurnacesreforged:storage_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.1.item` = "minecraft:stone"
- `key.2.tag` = "c:glass_blocks"
- `key.3.item` = "minecraft:chest"

### `data/betterfurnacesreforged/recipe/xp_tank_upgrade.json`

- `pattern` = ["030", "343", "030"]
- `result.id` = "betterfurnacesreforged:xp_tank_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:iron_block"
- `key.3.tag` = "c:glass_blocks"
- `key.4.item` = "minecraft:experience_bottle"

### `data/betterfurnacesreforged/recipes/advanced_fuel_efficiency_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["012", "345", "678"]
- `key.0.item` = "minecraft:diamond"
- `key.1.item` = "minecraft:ghast_tear"
- `key.2.item` = "minecraft:diamond"
- `key.3.item` = "minecraft:ender_eye"
- `key.4.item` = "betterfurnacesreforged:fuel_efficiency_upgrade"
- `key.5.item` = "minecraft:ender_eye"
- `key.6.item` = "minecraft:diamond"
- `key.7.item` = "minecraft:ender_eye"
- `key.8.item` = "minecraft:diamond"
- `result.item` = "betterfurnacesreforged:advanced_fuel_efficiency_upgrade"
- `result.count` = 1

### `data/betterfurnacesreforged/recipes/advanced_ore_processing_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["012", "345", "678"]
- `key.0.item` = "minecraft:diamond"
- `key.1.item` = "minecraft:piston"
- `key.2.item` = "minecraft:diamond"
- `key.3.item` = "minecraft:obsidian"
- `key.4.item` = "betterfurnacesreforged:ore_processing_upgrade"
- `key.5.item` = "minecraft:obsidian"
- `key.6.item` = "minecraft:diamond"
- `key.7.item` = "minecraft:piston"
- `key.8.item` = "minecraft:diamond"
- `result.item` = "betterfurnacesreforged:advanced_ore_processing_upgrade"
- `result.count` = 1

### `data/betterfurnacesreforged/recipes/autoinput_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["131", "121", "131"]
- `key.1.item` = "minecraft:gold_ingot"
- `key.2.item` = "minecraft:diamond"
- `key.3.item` = "betterfurnacesreforged:piping_upgrade"
- `result.item` = "betterfurnacesreforged:autoinput_upgrade"
- `result.count` = 1

### `data/betterfurnacesreforged/recipes/autooutput_upgrade.json`

- `pattern` = ["131", "424", "131"]
- `result.item` = "betterfurnacesreforged:autooutput_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.1.item` = "minecraft:iron_ingot"
- `key.2.tag` = "c:glass_blocks"
- `key.3.item` = "betterfurnacesreforged:piping_upgrade"
- `key.4.item` = "minecraft:gold_ingot"

### `data/betterfurnacesreforged/recipes/blasting_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["III", "IXI", "###"]
- `key.#.item` = "minecraft:smooth_stone"
- `key.X.item` = "betterfurnacesreforged:iron_conductor_block"
- `key.I.item` = "minecraft:iron_ingot"
- `result.item` = "betterfurnacesreforged:blasting_upgrade"

### `data/betterfurnacesreforged/recipes/cobblestone_generator.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = [" 1 ", "345", "678"]
- `key.1.item` = "minecraft:coal_block"
- `key.3.item` = "minecraft:iron_ingot"
- `key.4.item` = "minecraft:bucket"
- `key.5.item` = "minecraft:iron_ingot"
- `key.6.item` = "minecraft:smooth_stone"
- `key.7.item` = "betterfurnacesreforged:fuel_verifier"
- `key.8.item` = "minecraft:smooth_stone"
- `result.item` = "betterfurnacesreforged:cobblestone_generator"
- `result.count` = 1

### `data/betterfurnacesreforged/recipes/color_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["012", "345", "678"]
- `key.0.item` = "minecraft:white_dye"
- `key.1.item` = "minecraft:black_dye"
- `key.2.item` = "minecraft:brown_dye"
- `key.3.item` = "minecraft:red_dye"
- `key.4.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.5.item` = "minecraft:yellow_dye"
- `key.6.item` = "minecraft:green_dye"
- `key.7.item` = "minecraft:blue_dye"
- `key.8.item` = "minecraft:pink_dye"
- `result.item` = "betterfurnacesreforged:color_upgrade"

### `data/betterfurnacesreforged/recipes/diamond_furnace.json`

- `pattern` = ["010", "141", "010"]
- `result.item` = "betterfurnacesreforged:diamond_furnace"
- `type` = "minecraft:crafting_shaped"
- `key.0.tag` = "c:glass_blocks"
- `key.1.item` = "minecraft:diamond"
- `key.4.item` = "betterfurnacesreforged:gold_furnace"

### `data/betterfurnacesreforged/recipes/diamond_upgrade.json`

- `pattern` = ["010", "141", "010"]
- `result.item` = "betterfurnacesreforged:diamond_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.tag` = "c:glass_blocks"
- `key.1.item` = "minecraft:diamond"
- `key.4.item` = "minecraft:gold_ingot"

### `data/betterfurnacesreforged/recipes/energy_upgrade.json`

- `pattern` = ["010", "343", "010"]
- `result.item` = "betterfurnacesreforged:energy_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:gold_ingot"
- `key.1.tag` = "c:glass_blocks"
- `key.3.item` = "minecraft:redstone_block"
- `key.4.item` = "betterfurnacesreforged:netherhot_conductor_block"

### `data/betterfurnacesreforged/recipes/extreme_forge.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["012", "141", "676"]
- `key.0.item` = "minecraft:netherite_ingot"
- `key.1.item` = "betterfurnacesreforged:netherhot_conductor_block"
- `key.2.item` = "minecraft:netherite_ingot"
- `key.4.item` = "betterfurnacesreforged:extreme_furnace"
- `key.6.item` = "minecraft:netherite_ingot"
- `key.7.tag` = "minecraft:soul_fire_base_blocks"
- `result.item` = "betterfurnacesreforged:extreme_forge"

### `data/betterfurnacesreforged/recipes/extreme_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["012", "345", "678"]
- `key.0.item` = "minecraft:coal_block"
- `key.1.item` = "minecraft:ender_eye"
- `key.2.item` = "minecraft:coal_block"
- `key.3.item` = "minecraft:end_crystal"
- `key.4.item` = "betterfurnacesreforged:netherhot_furnace"
- `key.5.item` = "minecraft:end_crystal"
- `key.6.item` = "minecraft:end_stone"
- `key.7.item` = "minecraft:nether_bricks"
- `key.8.item` = "minecraft:end_stone"
- `result.item` = "betterfurnacesreforged:extreme_furnace"
- `result.count` = 1

### `data/betterfurnacesreforged/recipes/extreme_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["012", "345", "678"]
- `key.0.item` = "minecraft:coal_block"
- `key.1.item` = "minecraft:ender_eye"
- `key.2.item` = "minecraft:coal_block"
- `key.3.item` = "minecraft:end_crystal"
- `key.4.item` = "minecraft:magma_cream"
- `key.5.item` = "minecraft:end_crystal"
- `key.6.item` = "minecraft:end_stone"
- `key.7.item` = "minecraft:nether_bricks"
- `key.8.item` = "minecraft:end_stone"
- `result.item` = "betterfurnacesreforged:extreme_upgrade"
- `result.count` = 1

### `data/betterfurnacesreforged/recipes/factory_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["121", "141", "131"]
- `key.1.item` = "minecraft:diamond"
- `key.2.item` = "betterfurnacesreforged:autoinput_upgrade"
- `key.3.item` = "betterfurnacesreforged:autooutput_upgrade"
- `key.4.item` = "betterfurnacesreforged:redstone_signal_upgrade"
- `result.item` = "betterfurnacesreforged:factory_upgrade"
- `result.count` = 1

### `data/betterfurnacesreforged/recipes/fuel_efficiency_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["012", "345", "678"]
- `key.0.item` = "minecraft:lapis_block"
- `key.1.item` = "minecraft:ender_pearl"
- `key.2.item` = "minecraft:lapis_block"
- `key.3.item` = "minecraft:ender_pearl"
- `key.4.item` = "minecraft:coal"
- `key.5.item` = "minecraft:ender_pearl"
- `key.6.item` = "minecraft:lapis_block"
- `key.7.item` = "minecraft:ender_pearl"
- `key.8.item` = "minecraft:lapis_block"
- `result.item` = "betterfurnacesreforged:fuel_efficiency_upgrade"
- `result.count` = 1

### `data/betterfurnacesreforged/recipes/fuel_verifier.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["012", "345", "678"]
- `key.0.item` = "minecraft:cobblestone"
- `key.1.item` = "minecraft:cobblestone"
- `key.2.item` = "minecraft:cobblestone"
- `key.3.item` = "minecraft:cobblestone"
- `key.4.tag` = "minecraft:coals"
- `key.5.item` = "minecraft:cobblestone"
- `key.6.item` = "minecraft:cobblestone"
- `key.7.item` = "minecraft:cobblestone"
- `key.8.item` = "minecraft:cobblestone"
- `result.item` = "betterfurnacesreforged:fuel_verifier"
- `result.count` = 1

### `data/betterfurnacesreforged/recipes/generator_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["010", " 2 ", "010"]
- `key.0.item` = "minecraft:iron_ingot"
- `key.1.item` = "minecraft:lightning_rod"
- `key.2.item` = "betterfurnacesreforged:energy_upgrade"
- `result.item` = "betterfurnacesreforged:generator_upgrade"
- `result.count` = 1

### `data/betterfurnacesreforged/recipes/gold_conductor_block.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["012", "345", "678"]
- `key.0.item` = "minecraft:gold_ingot"
- `key.1.item` = "minecraft:iron_bars"
- `key.2.item` = "minecraft:gold_ingot"
- `key.3.item` = "minecraft:iron_bars"
- `key.4.item` = "minecraft:iron_ingot"
- `key.5.item` = "minecraft:iron_bars"
- `key.6.item` = "minecraft:gold_ingot"
- `key.7.item` = "minecraft:iron_bars"
- `key.8.item` = "minecraft:gold_ingot"
- `result.item` = "betterfurnacesreforged:gold_conductor_block"
- `result.count` = 1

### `data/betterfurnacesreforged/recipes/gold_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["012", "345"]
- `key.0.item` = "minecraft:gold_ingot"
- `key.1.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.2.item` = "minecraft:gold_ingot"
- `key.3.item` = "minecraft:gold_ingot"
- `key.4.item` = "betterfurnacesreforged:iron_furnace"
- `key.5.item` = "minecraft:gold_ingot"
- `result.item` = "betterfurnacesreforged:gold_furnace"
- `result.count` = 1

### `data/betterfurnacesreforged/recipes/gold_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["012", "345"]
- `key.0.item` = "minecraft:gold_ingot"
- `key.1.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.2.item` = "minecraft:gold_ingot"
- `key.3.item` = "minecraft:gold_ingot"
- `key.4.item` = "minecraft:iron_ingot"
- `key.5.item` = "minecraft:gold_ingot"
- `result.item` = "betterfurnacesreforged:gold_upgrade"
- `result.count` = 1

### `data/betterfurnacesreforged/recipes/iron_conductor_block.json`

- `pattern` = ["010", "141", "010"]
- `result.item` = "betterfurnacesreforged:iron_conductor_block"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:iron_ingot"
- `key.1.tag` = "c:glass_blocks"
- `key.4.item` = "minecraft:gold_ingot"

### `data/betterfurnacesreforged/recipes/iron_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["012", "345"]
- `key.0.item` = "minecraft:iron_ingot"
- `key.1.item` = "betterfurnacesreforged:iron_conductor_block"
- `key.2.item` = "minecraft:iron_ingot"
- `key.3.item` = "minecraft:iron_ingot"
- `key.4.item` = "minecraft:furnace"
- `key.5.item` = "minecraft:iron_ingot"
- `result.item` = "betterfurnacesreforged:iron_furnace"
- `result.count` = 1

### `data/betterfurnacesreforged/recipes/iron_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["012", "345"]
- `key.0.item` = "minecraft:iron_ingot"
- `key.1.item` = "betterfurnacesreforged:iron_conductor_block"
- `key.2.item` = "minecraft:iron_ingot"
- `key.3.item` = "minecraft:iron_ingot"
- `key.4.item` = "minecraft:cobblestone"
- `key.5.item` = "minecraft:iron_ingot"
- `result.item` = "betterfurnacesreforged:iron_upgrade"
- `result.count` = 1

### `data/betterfurnacesreforged/recipes/liquid_fuel_upgrade.json`

- `pattern` = ["0 0", "343", "030"]
- `result.item` = "betterfurnacesreforged:liquid_fuel_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:iron_ingot"
- `key.3.tag` = "c:glass_blocks"
- `key.4.item` = "minecraft:bucket"

### `data/betterfurnacesreforged/recipes/netherhot_conductor_block.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["012", "345", "678"]
- `key.0.item` = "minecraft:redstone_block"
- `key.1.item` = "minecraft:blaze_rod"
- `key.2.item` = "minecraft:redstone_block"
- `key.3.item` = "minecraft:blaze_rod"
- `key.4.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.5.item` = "minecraft:blaze_rod"
- `key.6.item` = "minecraft:redstone_block"
- `key.7.item` = "minecraft:blaze_rod"
- `key.8.item` = "minecraft:redstone_block"
- `result.item` = "betterfurnacesreforged:netherhot_conductor_block"
- `result.count` = 1

### `data/betterfurnacesreforged/recipes/netherhot_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = [" 1 ", "345", "678"]
- `key.1.item` = "minecraft:tnt"
- `key.3.item` = "minecraft:diamond_block"
- `key.4.item` = "betterfurnacesreforged:netherhot_conductor_block"
- `key.5.item` = "minecraft:diamond_block"
- `key.6.item` = "minecraft:magma_cream"
- `key.7.item` = "betterfurnacesreforged:diamond_furnace"
- `key.8.item` = "minecraft:magma_cream"
- `result.item` = "betterfurnacesreforged:netherhot_furnace"
- `result.count` = 1

### `data/betterfurnacesreforged/recipes/netherhot_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = [" 1 ", "345", "678"]
- `key.1.item` = "minecraft:tnt"
- `key.3.item` = "minecraft:diamond_block"
- `key.4.item` = "betterfurnacesreforged:netherhot_conductor_block"
- `key.5.item` = "minecraft:diamond_block"
- `key.6.item` = "minecraft:magma_cream"
- `key.7.item` = "minecraft:diamond"
- `key.8.item` = "minecraft:magma_cream"
- `result.item` = "betterfurnacesreforged:netherhot_upgrade"
- `result.count` = 1

### `data/betterfurnacesreforged/recipes/ore_processing_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["012", "345", "678"]
- `key.0.item` = "minecraft:stone"
- `key.1.item` = "minecraft:stone"
- `key.2.item` = "minecraft:stone"
- `key.3.item` = "minecraft:stone"
- `key.4.item` = "betterfurnacesreforged:iron_conductor_block"
- `key.5.item` = "minecraft:stone"
- `key.6.item` = "minecraft:stone"
- `key.7.item` = "minecraft:stone"
- `key.8.item` = "minecraft:stone"
- `result.item` = "betterfurnacesreforged:ore_processing_upgrade"
- `result.count` = 1

### `data/betterfurnacesreforged/recipes/piping_upgrade.json`

- `pattern` = ["121", "111", "121"]
- `result.item` = "betterfurnacesreforged:piping_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.1.item` = "minecraft:iron_ingot"
- `key.2.tag` = "c:glass_blocks"

### `data/betterfurnacesreforged/recipes/raw_ore_processing_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["121", "030", "101"]
- `key.0.item` = "minecraft:netherite_scrap"
- `key.1.item` = "betterfurnacesreforged:netherhot_conductor_block"
- `key.2.item` = "minecraft:netherite_ingot"
- `key.3.item` = "minecraft:raw_iron_block"
- `result.item` = "betterfurnacesreforged:raw_ore_processing_upgrade"
- `result.count` = 1

### `data/betterfurnacesreforged/recipes/redstone_signal_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["202", "131", "202"]
- `key.0.item` = "minecraft:comparator"
- `key.1.item` = "minecraft:repeater"
- `key.2.item` = "minecraft:redstone"
- `key.3.item` = "betterfurnacesreforged:iron_conductor_block"
- `result.item` = "betterfurnacesreforged:redstone_signal_upgrade"
- `result.count` = 1

### `data/betterfurnacesreforged/recipes/rock_generation/blackstone.json`

- `type` = "betterfurnacesreforged:rock_generating"
- `result.item` = "minecraft:blackstone"
- `duration` = 150

### `data/betterfurnacesreforged/recipes/rock_generation/cobbled_deepslate.json`

- `type` = "betterfurnacesreforged:rock_generating"
- `result.item` = "minecraft:cobbled_deepslate"
- `duration` = 125

### `data/betterfurnacesreforged/recipes/rock_generation/cobblestone.json`

- `type` = "betterfurnacesreforged:rock_generating"
- `result.item` = "minecraft:cobblestone"
- `duration` = 80

### `data/betterfurnacesreforged/recipes/rock_generation/deepslate.json`

- `type` = "betterfurnacesreforged:rock_generating"
- `result.item` = "minecraft:deepslate"
- `duration` = 150

### `data/betterfurnacesreforged/recipes/rock_generation/obsidian.json`

- `type` = "betterfurnacesreforged:rock_generating"
- `result.item` = "minecraft:obsidian"
- `duration` = 600

### `data/betterfurnacesreforged/recipes/rock_generation/stone.json`

- `type` = "betterfurnacesreforged:rock_generating"
- `result.item` = "minecraft:stone"
- `duration` = 100

### `data/betterfurnacesreforged/recipes/smoking_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = [" # ", "#X#", " # "]
- `key.#.tag` = "minecraft:logs"
- `key.X.item` = "betterfurnacesreforged:gold_conductor_block"
- `result.item` = "betterfurnacesreforged:smoking_upgrade"

### `data/betterfurnacesreforged/recipes/storage_upgrade.json`

- `pattern` = ["121", "232", "121"]
- `result.item` = "betterfurnacesreforged:storage_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.1.item` = "minecraft:stone"
- `key.2.tag` = "c:glass_blocks"
- `key.3.item` = "minecraft:chest"

### `data/betterfurnacesreforged/recipes/xp_tank_upgrade.json`

- `pattern` = ["030", "343", "030"]
- `result.item` = "betterfurnacesreforged:xp_tank_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:iron_block"
- `key.3.tag` = "c:glass_blocks"
- `key.4.item` = "minecraft:experience_bottle"

### `data/betterfurnacesreforged/tags/block/forge.json`

- `replace` = false
- `values` = ["betterfurnacesreforged:extreme_forge", "betterfurnacesreforged:copper_forge", "betterfurnacesreforged:iron_forge", "betterfurnacesreforged:gold_forge", "betterfurnacesreforged:amethyst_forge", "betterfurnacesreforged:diamond_forge", "betterfurnacesreforged:platinum_forge", "betterfurnacesreforged:…

### `data/betterfurnacesreforged/tags/block/furnace.json`

- `replace` = false
- `values` = ["betterfurnacesreforged:copper_furnace", "betterfurnacesreforged:iron_furnace", "betterfurnacesreforged:steel_furnace", "betterfurnacesreforged:gold_furnace", "betterfurnacesreforged:amethyst_furnace", "betterfurnacesreforged:diamond_furnace", "betterfurnacesreforged:platinum_furnace", "betterfurna…

### `data/betterfurnacesreforged/tags/block/furnace_like.json`

- `replace` = false
- `values` = ["#betterfurnacesreforged:furnace", "#betterfurnacesreforged:forge"]

### `data/betterfurnacesreforged/tags/block/tier/amethyst.json`

- `replace` = false
- `values` = ["betterfurnacesreforged:amethyst_furnace", "betterfurnacesreforged:amethyst_forge"]

### `data/betterfurnacesreforged/tags/block/tier/copper.json`

- `replace` = false
- `values` = ["betterfurnacesreforged:copper_furnace", "betterfurnacesreforged:copper_forge"]

### `data/betterfurnacesreforged/tags/block/tier/diamond.json`

- `replace` = false
- `values` = ["betterfurnacesreforged:diamond_furnace", "betterfurnacesreforged:diamond_forge"]

### `data/betterfurnacesreforged/tags/block/tier/extreme.json`

- `replace` = false
- `values` = ["betterfurnacesreforged:extreme_furnace", "betterfurnacesreforged:extreme_forge"]

### `data/betterfurnacesreforged/tags/block/tier/gold.json`

- `replace` = false
- `values` = ["betterfurnacesreforged:gold_furnace", "betterfurnacesreforged:gold_forge"]

### `data/betterfurnacesreforged/tags/block/tier/iron.json`

- `replace` = false
- `values` = ["betterfurnacesreforged:iron_furnace", "betterfurnacesreforged:iron_forge"]

### `data/betterfurnacesreforged/tags/block/tier/netherhot.json`

- `replace` = false
- `values` = ["betterfurnacesreforged:netherhot_furnace", "betterfurnacesreforged:netherhot_forge"]

### `data/betterfurnacesreforged/tags/block/tier/platinum.json`

- `replace` = false
- `values` = ["betterfurnacesreforged:platinum_furnace", "betterfurnacesreforged:platinum_forge"]

### `data/betterfurnacesreforged/tags/block/tier/steel.json`

- `replace` = false
- `values` = ["betterfurnacesreforged:steel_furnace", "betterfurnacesreforged:steel_forge"]

### `data/betterfurnacesreforged/tags/block/tier/ultimate.json`

- `replace` = false
- `values` = ["betterfurnacesreforged:ultimate_furnace", "betterfurnacesreforged:ultimate_forge"]

### `data/minecraft/tags/block/mineable/pickaxe.json`

- `replace` = false
- `values` = ["betterfurnacesreforged:fuel_verifier", "betterfurnacesreforged:cobblestone_generator", "#betterfurnacesreforged:furnace", "#betterfurnacesreforged:forge"]

### `data/minecraft/tags/block/needs_diamond_tool.json`

- `replace` = false
- `values` = ["#betterfurnacesreforged:tier/extreme", "#betterfurnacesreforged:tier/ultimate"]

### `data/minecraft/tags/block/needs_iron_tool.json`

- `replace` = false
- `values` = ["#betterfurnacesreforged:tier/gold", "#betterfurnacesreforged:tier/diamond", "#betterfurnacesreforged:tier/netherhot", "#betterfurnacesreforged:tier/amethyst", "#betterfurnacesreforged:tier/platinum"]

### `data/minecraft/tags/block/needs_stone_tool.json`

- `replace` = false
- `values` = ["betterfurnacesreforged:fuel_verifier", "betterfurnacesreforged:cobblestone_generator", "#betterfurnacesreforged:tier/iron", "#betterfurnacesreforged:tier/copper", "#betterfurnacesreforged:tier/steel"]

### `data/ultimatefurnaces/recipe/amethyst_diamond_upgrade.json`

- `pattern` = ["000", "121", "000"]
- `result.id` = "betterfurnacesreforged:amethyst_diamond_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.tag` = "c:glass_blocks"
- `key.1.item` = "minecraft:diamond"
- `key.2.item` = "minecraft:amethyst_shard"

### `data/ultimatefurnaces/recipe/amethyst_forge.json`

- `pattern` = ["151", "232", "141"]
- `result.id` = "betterfurnacesreforged:amethyst_forge"
- `type` = "minecraft:crafting_shaped"
- `key.1.item` = "minecraft:amethyst_shard"
- `key.2.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.3.item` = "betterfurnacesreforged:amethyst_furnace"
- `key.4.tag` = "minecraft:soul_fire_base_blocks"
- `key.5.item` = "minecraft:amethyst_block"

### `data/ultimatefurnaces/recipe/amethyst_furnace.json`

- `pattern` = ["020", "131", "010"]
- `result.id` = "betterfurnacesreforged:amethyst_furnace"
- `type` = "minecraft:crafting_shaped"
- `key.0.tag` = "c:glass_blocks"
- `key.1.item` = "minecraft:amethyst_block"
- `key.2.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.3.item` = "betterfurnacesreforged:gold_furnace"

### `data/ultimatefurnaces/recipe/amethyst_upgrade.json`

- `pattern` = ["020", "131", "010"]
- `result.id` = "betterfurnacesreforged:amethyst_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.tag` = "c:glass_blocks"
- `key.1.item` = "minecraft:amethyst_block"
- `key.2.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.3.item` = "minecraft:gold_ingot"

### `data/ultimatefurnaces/recipe/copper_forge.json`

- `pattern` = ["121", "343", "151"]
- `result.id` = "betterfurnacesreforged:copper_forge"
- `type` = "minecraft:crafting_shaped"
- `key.1.item` = "minecraft:copper_ingot"
- `key.2.item` = "betterfurnacesreforged:iron_conductor_block"
- `key.3.item` = "minecraft:copper_block"
- `key.4.item` = "betterfurnacesreforged:copper_furnace"
- `key.5.tag` = "minecraft:soul_fire_base_blocks"

### `data/ultimatefurnaces/recipe/copper_furnace.json`

- `pattern` = ["000", "040", "000"]
- `result.id` = "betterfurnacesreforged:copper_furnace"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:copper_ingot"
- `key.4.item` = "minecraft:furnace"

### `data/ultimatefurnaces/recipe/copper_iron_upgrade.json`

- `pattern` = ["010", "141", "010"]
- `result.id` = "betterfurnacesreforged:copper_iron_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:iron_ingot"
- `key.1.tag` = "c:glass_blocks"
- `key.4.item` = "minecraft:copper_ingot"

### `data/ultimatefurnaces/recipe/copper_upgrade.json`

- `pattern` = ["000", "040", "000"]
- `result.id` = "betterfurnacesreforged:copper_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:copper_ingot"
- `key.4.item` = "minecraft:cobblestone"

### `data/ultimatefurnaces/recipe/diamond_forge.json`

- `pattern` = ["151", "232", "141"]
- `result.id` = "betterfurnacesreforged:diamond_forge"
- `type` = "minecraft:crafting_shaped"
- `key.1.item` = "minecraft:diamond"
- `key.2.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.3.item` = "betterfurnacesreforged:diamond_furnace"
- `key.4.tag` = "minecraft:soul_fire_base_blocks"
- `key.5.item` = "minecraft:diamond_block"

### `data/ultimatefurnaces/recipe/diamond_furnace.json`

- `pattern` = ["000", "121", "000"]
- `result.id` = "betterfurnacesreforged:diamond_furnace"
- `type` = "minecraft:crafting_shaped"
- `key.0.tag` = "c:glass_blocks"
- `key.1.item` = "minecraft:diamond"
- `key.2.item` = "betterfurnacesreforged:amethyst_furnace"

### `data/ultimatefurnaces/recipe/gold_forge.json`

- `pattern` = ["121", "232", "141"]
- `result.id` = "betterfurnacesreforged:gold_forge"
- `type` = "minecraft:crafting_shaped"
- `key.1.item` = "minecraft:gold_ingot"
- `key.2.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.3.item` = "betterfurnacesreforged:gold_furnace"
- `key.4.tag` = "minecraft:soul_fire_base_blocks"

### `data/ultimatefurnaces/recipe/gold_furnace.json`

- `pattern` = ["000", "040"]
- `result.id` = "betterfurnacesreforged:gold_furnace"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:gold_ingot"
- `key.4.item` = "betterfurnacesreforged:steel_furnace"

### `data/ultimatefurnaces/recipe/iron_forge.json`

- `pattern` = ["121", "232", "141"]
- `result.id` = "betterfurnacesreforged:iron_forge"
- `type` = "minecraft:crafting_shaped"
- `key.1.item` = "minecraft:iron_ingot"
- `key.2.item` = "betterfurnacesreforged:iron_conductor_block"
- `key.3.item` = "betterfurnacesreforged:iron_furnace"
- `key.4.tag` = "minecraft:soul_fire_base_blocks"

### `data/ultimatefurnaces/recipe/iron_furnace.json`

- `pattern` = ["010", "141", "010"]
- `result.id` = "betterfurnacesreforged:iron_furnace"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:iron_ingot"
- `key.1.tag` = "c:glass_blocks"
- `key.4.item` = "betterfurnacesreforged:copper_furnace"

### `data/ultimatefurnaces/recipe/netherhot_forge.json`

- `pattern` = ["121", "232", "141"]
- `result.id` = "betterfurnacesreforged:netherhot_forge"
- `type` = "minecraft:crafting_shaped"
- `key.1.item` = "minecraft:redstone"
- `key.2.item` = "betterfurnacesreforged:netherhot_conductor_block"
- `key.3.item` = "betterfurnacesreforged:netherhot_furnace"
- `key.4.tag` = "minecraft:soul_fire_base_blocks"

### `data/ultimatefurnaces/recipe/netherhot_furnace.json`

- `pattern` = ["101", "212", "343"]
- `result.id` = "betterfurnacesreforged:netherhot_furnace"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:tnt"
- `key.1.item` = "minecraft:diamond"
- `key.2.item` = "betterfurnacesreforged:netherhot_conductor_block"
- `key.3.item` = "minecraft:magma_cream"
- `key.4.item` = "betterfurnacesreforged:platinum_furnace"

### `data/ultimatefurnaces/recipe/platinum_forge.json`

- `pattern` = ["151", "232", "141"]
- `result.id` = "betterfurnacesreforged:platinum_forge"
- `type` = "minecraft:crafting_shaped"
- `key.1.tag` = "c:ingots/platinum"
- `key.2.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.3.item` = "betterfurnacesreforged:platinum_furnace"
- `key.4.tag` = "minecraft:soul_fire_base_blocks"
- `key.5.tag` = "c:storage_blocks/platinum"

### `data/ultimatefurnaces/recipe/platinum_furnace.json`

- `pattern` = ["000", "040", "000"]
- `result.id` = "betterfurnacesreforged:platinum_furnace"
- `type` = "minecraft:crafting_shaped"
- `key.0.tag` = "c:ingots/platinum"
- `key.4.item` = "betterfurnacesreforged:diamond_furnace"

### `data/ultimatefurnaces/recipe/platinum_netherhot_upgrade.json`

- `pattern` = ["101", "212", "343"]
- `result.id` = "betterfurnacesreforged:platinum_netherhot_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:tnt"
- `key.1.item` = "minecraft:diamond"
- `key.2.item` = "betterfurnacesreforged:netherhot_conductor_block"
- `key.3.item` = "minecraft:magma_cream"
- `key.4.tag` = "c:ingots/platinum"

### `data/ultimatefurnaces/recipe/platinum_upgrade.json`

- `pattern` = ["000", "040", "000"]
- `result.id` = "betterfurnacesreforged:platinum_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.tag` = "c:ingots/platinums"
- `key.4.item` = "minecraft:diamond"

### `data/ultimatefurnaces/recipe/steel_forge.json`

- `pattern` = ["151", "232", "141"]
- `result.id` = "betterfurnacesreforged:steel_forge"
- `type` = "minecraft:crafting_shaped"
- `key.1.tag` = "c:ingots/steel"
- `key.2.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.3.item` = "betterfurnacesreforged:steel_furnace"
- `key.4.tag` = "minecraft:soul_fire_base_blocks"
- `key.5.tag` = "c:storage_blocks/steel"

### `data/ultimatefurnaces/recipe/steel_furnace.json`

- `pattern` = ["010", "040"]
- `result.id` = "betterfurnacesreforged:steel_furnace"
- `type` = "minecraft:crafting_shaped"
- `key.0.tag` = "c:ingots/steel"
- `key.1.item` = "betterfurnacesreforged:iron_conductor_block"
- `key.4.item` = "betterfurnacesreforged:iron_furnace"

### `data/ultimatefurnaces/recipe/steel_gold_upgrade.json`

- `pattern` = ["000", "040"]
- `result.id` = "betterfurnacesreforged:steel_gold_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:gold_ingot"
- `key.4.tag` = "c:ingots/steel"

### `data/ultimatefurnaces/recipe/steel_upgrade.json`

- `pattern` = ["010", "040"]
- `result.id` = "betterfurnacesreforged:steel_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.tag` = "c:ingots/steel"
- `key.1.item` = "betterfurnacesreforged:iron_conductor_block"
- `key.4.item` = "minecraft:iron_ingot"

### `data/ultimatefurnaces/recipe/ultimate_forge.json`

- `pattern` = ["111", "121", "343"]
- `result.id` = "betterfurnacesreforged:ultimate_forge"
- `type` = "minecraft:crafting_shaped"
- `key.1.item` = "minecraft:netherite_ingot"
- `key.2.item` = "betterfurnacesreforged:ultimate_furnace"
- `key.3.item` = "minecraft:emerald_block"
- `key.4.tag` = "minecraft:soul_fire_base_blocks"

### `data/ultimatefurnaces/recipe/ultimate_furnace.json`

- `pattern` = ["131", "254", "676"]
- `result.id` = "betterfurnacesreforged:ultimate_furnace"
- `type` = "minecraft:crafting_shaped"
- `key.1.item` = "minecraft:netherite_ingot"
- `key.2.item` = "betterfurnacesreforged:iron_conductor_block"
- `key.3.item` = "betterfurnacesreforged:netherhot_conductor_block"
- `key.4.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.5.item` = "betterfurnacesreforged:extreme_furnace"
- `key.6.item` = "minecraft:emerald_block"
- `key.7.item` = "minecraft:coal_block"

### `data/ultimatefurnaces/recipe/ultimate_ore_processing_upgrade.json`

- `pattern` = ["313", "242", "313"]
- `result.id` = "betterfurnacesreforged:ultimate_ore_processing_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.1.item` = "minecraft:dragon_head"
- `key.2.item` = "betterfurnacesreforged:raw_ore_processing_upgrade"
- `key.3.item` = "minecraft:emerald_block"
- `key.4.item` = "betterfurnacesreforged:advanced_ore_processing_upgrade"

### `data/ultimatefurnaces/recipe/ultimate_upgrade.json`

- `pattern` = ["131", "254", "676"]
- `result.id` = "betterfurnacesreforged:ultimate_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.1.item` = "minecraft:netherite_ingot"
- `key.2.item` = "betterfurnacesreforged:iron_conductor_block"
- `key.3.item` = "betterfurnacesreforged:netherhot_conductor_block"
- `key.4.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.5.item` = "minecraft:ender_eye"
- `key.6.item` = "minecraft:emerald_block"
- `key.7.item` = "minecraft:coal_block"

### `data/ultimatefurnaces/recipes/amethyst_diamond_upgrade.json`

- `pattern` = ["000", "121", "000"]
- `result.item` = "betterfurnacesreforged:amethyst_diamond_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.tag` = "c:glass_blocks"
- `key.1.item` = "minecraft:diamond"
- `key.2.item` = "minecraft:amethyst_shard"

### `data/ultimatefurnaces/recipes/amethyst_forge.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["151", "232", "141"]
- `key.1.item` = "minecraft:amethyst_shard"
- `key.2.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.3.item` = "betterfurnacesreforged:amethyst_furnace"
- `key.4.tag` = "minecraft:soul_fire_base_blocks"
- `key.5.item` = "minecraft:amethyst_block"
- `result.item` = "betterfurnacesreforged:amethyst_forge"

### `data/ultimatefurnaces/recipes/amethyst_furnace.json`

- `pattern` = ["020", "131", "010"]
- `result.item` = "betterfurnacesreforged:amethyst_furnace"
- `type` = "minecraft:crafting_shaped"
- `key.0.tag` = "c:glass_blocks"
- `key.1.item` = "minecraft:amethyst_block"
- `key.2.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.3.item` = "betterfurnacesreforged:gold_furnace"

### `data/ultimatefurnaces/recipes/amethyst_upgrade.json`

- `pattern` = ["020", "131", "010"]
- `result.item` = "betterfurnacesreforged:amethyst_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.tag` = "c:glass_blocks"
- `key.1.item` = "minecraft:amethyst_block"
- `key.2.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.3.item` = "minecraft:gold_ingot"

### `data/ultimatefurnaces/recipes/copper_forge.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["121", "343", "151"]
- `key.1.item` = "minecraft:copper_ingot"
- `key.2.item` = "betterfurnacesreforged:iron_conductor_block"
- `key.3.item` = "minecraft:copper_block"
- `key.4.item` = "betterfurnacesreforged:copper_furnace"
- `key.5.tag` = "minecraft:soul_fire_base_blocks"
- `result.item` = "betterfurnacesreforged:copper_forge"
- `result.count` = 1

### `data/ultimatefurnaces/recipes/copper_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["000", "040", "000"]
- `key.0.item` = "minecraft:copper_ingot"
- `key.4.item` = "minecraft:furnace"
- `result.item` = "betterfurnacesreforged:copper_furnace"

### `data/ultimatefurnaces/recipes/copper_iron_upgrade.json`

- `pattern` = ["010", "141", "010"]
- `result.item` = "betterfurnacesreforged:copper_iron_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:iron_ingot"
- `key.1.tag` = "c:glass_blocks"
- `key.4.item` = "minecraft:copper_ingot"

### `data/ultimatefurnaces/recipes/copper_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["000", "040", "000"]
- `key.0.item` = "minecraft:copper_ingot"
- `key.4.item` = "minecraft:cobblestone"
- `result.item` = "betterfurnacesreforged:copper_upgrade"
- `result.count` = 1

### `data/ultimatefurnaces/recipes/diamond_forge.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["151", "232", "141"]
- `key.1.item` = "minecraft:diamond"
- `key.2.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.3.item` = "betterfurnacesreforged:diamond_furnace"
- `key.4.tag` = "minecraft:soul_fire_base_blocks"
- `key.5.item` = "minecraft:diamond_block"
- `result.item` = "betterfurnacesreforged:diamond_forge"
- `result.count` = 1

### `data/ultimatefurnaces/recipes/diamond_furnace.json`

- `pattern` = ["000", "121", "000"]
- `result.item` = "betterfurnacesreforged:diamond_furnace"
- `type` = "minecraft:crafting_shaped"
- `key.0.tag` = "c:glass_blocks"
- `key.1.item` = "minecraft:diamond"
- `key.2.item` = "betterfurnacesreforged:amethyst_furnace"

### `data/ultimatefurnaces/recipes/gold_forge.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["121", "232", "141"]
- `key.1.item` = "minecraft:gold_ingot"
- `key.2.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.3.item` = "betterfurnacesreforged:gold_furnace"
- `key.4.tag` = "minecraft:soul_fire_base_blocks"
- `result.item` = "betterfurnacesreforged:gold_forge"
- `result.count` = 1

### `data/ultimatefurnaces/recipes/gold_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["   ", "000", "040"]
- `key.0.item` = "minecraft:gold_ingot"
- `key.4.item` = "betterfurnacesreforged:steel_furnace"
- `result.item` = "betterfurnacesreforged:gold_furnace"
- `result.count` = 1

### `data/ultimatefurnaces/recipes/iron_forge.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["121", "232", "141"]
- `key.1.item` = "minecraft:iron_ingot"
- `key.2.item` = "betterfurnacesreforged:iron_conductor_block"
- `key.3.item` = "betterfurnacesreforged:iron_furnace"
- `key.4.tag` = "minecraft:soul_fire_base_blocks"
- `result.item` = "betterfurnacesreforged:iron_forge"
- `result.count` = 1

### `data/ultimatefurnaces/recipes/iron_furnace.json`

- `pattern` = ["010", "141", "010"]
- `result.item` = "betterfurnacesreforged:iron_furnace"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:iron_ingot"
- `key.1.tag` = "c:glass_blocks"
- `key.4.item` = "betterfurnacesreforged:copper_furnace"

### `data/ultimatefurnaces/recipes/netherhot_forge.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["121", "232", "141"]
- `key.1.item` = "minecraft:redstone"
- `key.2.item` = "betterfurnacesreforged:netherhot_conductor_block"
- `key.3.item` = "betterfurnacesreforged:netherhot_furnace"
- `key.4.tag` = "minecraft:soul_fire_base_blocks"
- `result.item` = "betterfurnacesreforged:netherhot_forge"
- `result.count` = 1

### `data/ultimatefurnaces/recipes/netherhot_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["101", "212", "343"]
- `key.0.item` = "minecraft:tnt"
- `key.1.item` = "minecraft:diamond"
- `key.2.item` = "betterfurnacesreforged:netherhot_conductor_block"
- `key.3.item` = "minecraft:magma_cream"
- `key.4.item` = "betterfurnacesreforged:platinum_furnace"
- `result.item` = "betterfurnacesreforged:netherhot_furnace"
- `result.count` = 1

### `data/ultimatefurnaces/recipes/platinum_forge.json`

- `pattern` = ["151", "232", "141"]
- `result.item` = "betterfurnacesreforged:platinum_forge"
- `type` = "minecraft:crafting_shaped"
- `key.1.tag` = "c:ingots/platinum"
- `key.2.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.3.item` = "betterfurnacesreforged:platinum_furnace"
- `key.4.tag` = "minecraft:soul_fire_base_blocks"
- `key.5.tag` = "c:storage_blocks/platinum"

### `data/ultimatefurnaces/recipes/platinum_furnace.json`

- `pattern` = ["000", "040", "000"]
- `result.item` = "betterfurnacesreforged:platinum_furnace"
- `type` = "minecraft:crafting_shaped"
- `key.0.tag` = "c:platinum_ingots"
- `key.4.item` = "betterfurnacesreforged:diamond_furnace"

### `data/ultimatefurnaces/recipes/platinum_netherhot_upgrade.json`

- `pattern` = ["101", "212", "343"]
- `result.item` = "betterfurnacesreforged:platinum_netherhot_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:tnt"
- `key.1.item` = "minecraft:diamond"
- `key.2.item` = "betterfurnacesreforged:netherhot_conductor_block"
- `key.3.item` = "minecraft:magma_cream"
- `key.4.tag` = "c:platinum_ingots"

### `data/ultimatefurnaces/recipes/platinum_upgrade.json`

- `pattern` = ["000", "040", "000"]
- `result.item` = "betterfurnacesreforged:platinum_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.tag` = "c:platinum_ingots"
- `key.4.item` = "minecraft:diamond"

### `data/ultimatefurnaces/recipes/steel_forge.json`

- `pattern` = ["151", "232", "141"]
- `result.item` = "betterfurnacesreforged:steel_forge"
- `type` = "minecraft:crafting_shaped"
- `key.1.tag` = "c:ingots/steel"
- `key.2.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.3.item` = "betterfurnacesreforged:steel_furnace"
- `key.4.tag` = "minecraft:soul_fire_base_blocks"
- `key.5.tag` = "c:storage_blocks/steel"

### `data/ultimatefurnaces/recipes/steel_furnace.json`

- `pattern` = ["010", "040"]
- `result.item` = "betterfurnacesreforged:steel_furnace"
- `type` = "minecraft:crafting_shaped"
- `key.0.tag` = "c:steel_ingots"
- `key.1.item` = "betterfurnacesreforged:iron_conductor_block"
- `key.4.item` = "betterfurnacesreforged:iron_furnace"

### `data/ultimatefurnaces/recipes/steel_gold_upgrade.json`

- `pattern` = ["000", "040"]
- `result.item` = "betterfurnacesreforged:steel_gold_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.item` = "minecraft:gold_ingot"
- `key.4.tag` = "c:steel_ingots"

### `data/ultimatefurnaces/recipes/steel_upgrade.json`

- `pattern` = ["010", "040"]
- `result.item` = "betterfurnacesreforged:steel_upgrade"
- `type` = "minecraft:crafting_shaped"
- `key.0.tag` = "c:steel_ingots"
- `key.1.item` = "betterfurnacesreforged:iron_conductor_block"
- `key.4.item` = "minecraft:iron_ingot"

### `data/ultimatefurnaces/recipes/ultimate_forge.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["111", "121", "343"]
- `key.1.item` = "minecraft:netherite_ingot"
- `key.2.item` = "betterfurnacesreforged:ultimate_furnace"
- `key.3.item` = "minecraft:emerald_block"
- `key.4.tag` = "minecraft:soul_fire_base_blocks"
- `result.item` = "betterfurnacesreforged:ultimate_forge"
- `result.count` = 1

### `data/ultimatefurnaces/recipes/ultimate_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["131", "254", "676"]
- `key.1.item` = "minecraft:netherite_ingot"
- `key.2.item` = "betterfurnacesreforged:iron_conductor_block"
- `key.3.item` = "betterfurnacesreforged:netherhot_conductor_block"
- `key.4.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.5.item` = "betterfurnacesreforged:extreme_furnace"
- `key.6.item` = "minecraft:emerald_block"
- `key.7.item` = "minecraft:coal_block"
- `result.item` = "betterfurnacesreforged:ultimate_furnace"
- `result.count` = 1

### `data/ultimatefurnaces/recipes/ultimate_ore_processing_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["313", "242", "313"]
- `key.1.item` = "minecraft:dragon_head"
- `key.2.item` = "betterfurnacesreforged:raw_ore_processing_upgrade"
- `key.3.item` = "minecraft:emerald_block"
- `key.4.item` = "betterfurnacesreforged:advanced_ore_processing_upgrade"
- `result.item` = "betterfurnacesreforged:ultimate_ore_processing_upgrade"
- `result.count` = 1

### `data/ultimatefurnaces/recipes/ultimate_upgrade.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["131", "254", "676"]
- `key.1.item` = "minecraft:netherite_ingot"
- `key.2.item` = "betterfurnacesreforged:iron_conductor_block"
- `key.3.item` = "betterfurnacesreforged:netherhot_conductor_block"
- `key.4.item` = "betterfurnacesreforged:gold_conductor_block"
- `key.5.item` = "minecraft:ender_eye"
- `key.6.item` = "minecraft:emerald_block"
- `key.7.item` = "minecraft:coal_block"
- `result.item` = "betterfurnacesreforged:ultimate_upgrade"
- `result.count` = 1

## Testi nel codice


### `wily/betterfurnaces/BFRConfig.class`

- "wily/factoryapi/base/config/FactoryConfigDisplay$Instance"
- "wily/factoryapi/base/config/FactoryConfigDisplay"
- "wily/factoryapi/base/config/FactoryConfig$StorageHandler"
- "wily/factoryapi/base/config/FactoryConfig"
- "wily/factoryapi/base/config/FactoryConfigControl$Int"
- "wily/factoryapi/base/config/FactoryConfigControl"
- "wily/factoryapi/base/config/FactoryConfig$StorageAccess"
- "wily/factoryapi/base/config/FactoryConfigControl$FromInt"
- "Lwily/factoryapi/base/config/FactoryConfig$StorageHandler;"
- "TIER_SPEED_CONTROL"
- "Lwily/factoryapi/base/config/FactoryConfigControl$Int;"
- "Lwily/factoryapi/base/config/FactoryConfig;"
- "Lwily/factoryapi/base/config/FactoryConfig<Ljava/lang/Boolean;>;"
- "Lwily/factoryapi/base/config/FactoryConfig<Ljava/lang/Integer;>;"
- "copperTierSpeed"
- "ironTierSpeed"
- "steelTierSpeed"
- "goldTierSpeed"
- "amethystTierSpeed"
- "diamondTierSpeed"
- "platinumTierSpeed"
- "netherhotTierSpeed"
- "extremeTierSpeed"
- "ultimateTierSpeed"
- "Lwily/factoryapi/base/config/FactoryConfig<Lnet/minecraft/resources/ResourceLocation;>;"
- "additionalLiquidFuels"
- "Lwily/factoryapi/base/config/FactoryConfig<Ljava/util/List<Lnet/minecraft/resources/ResourceLocation;>;>;"
- "wily/factoryapi/FactoryAPIPlatform"
- "(Ljava/lang/String;)Lwily/factoryapi/base/config/FactoryConfigDisplay;"
- "<T:Ljava/lang/Object;>(Ljava/lang/String;)Lwily/factoryapi/base/config/FactoryConfigDisplay<TT;>;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "wily/factoryapi/FactoryAPI"
- "(Lnet/minecraft/network/chat/Component;)Lwily/factoryapi/base/config/FactoryConfigDisplay$Instance;"
- "Lwily/factoryapi/base/config/FactoryConfigControl;"
- "(Ljava/lang/String;Lwily/factoryapi/base/config/FactoryConfigDisplay;Lwily/factoryapi/base/config/FactoryConfigControl;Ljava/lang/Object;Ljava/util/function/Consumer;Lwily/factoryapi/base/config/FactoryConfig$StorageAccess;)Lwily/factoryapi/base/config/FactoryConfig;"
- "(Lwily/factoryapi/base/config/FactoryConfig;)Lwily/factoryapi/base/config/FactoryConfig;"
- "()Lwily/factoryapi/base/config/FactoryConfigControl;"

### `wily/betterfurnaces/BetterFurnacesReforged.class`

- "wily/factoryapi/base/config/FactoryConfig$StorageHandler"
- "wily/factoryapi/base/config/FactoryConfig"
- "wily/factoryapi/base/network/CommonNetwork$Identifier"
- "wily/factoryapi/base/network/CommonNetwork"
- "wily/factoryapi/FactoryEvent$PayloadRegistry"
- "wily/factoryapi/FactoryEvent"
- "(Lwily/factoryapi/FactoryEvent$PayloadRegistry;)V"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "Lwily/factoryapi/base/config/FactoryConfig$StorageHandler;"
- "(Lnet/minecraft/resources/ResourceLocation;Lwily/factoryapi/base/config/FactoryConfig$StorageHandler;)Lwily/factoryapi/base/config/FactoryConfig$StorageHandler;"
- "Lwily/factoryapi/base/config/FactoryConfig;"
- "wily/factoryapi/FactoryAPI"
- "(Lnet/minecraft/server/MinecraftServer;Ljava/lang/String;)Lwily/factoryapi/base/config/FactoryConfig$StorageHandler;"
- "Lwily/factoryapi/base/network/CommonNetwork$Identifier;"
- "(ZLwily/factoryapi/base/network/CommonNetwork$Identifier;)V"
- "wily/betterfurnaces/network/CobblestoneGeneratorSyncPayload"
- "Lwily/factoryapi/FactoryEvent$PayloadRegistry;"
- "wily/factoryapi/FactoryAPIPlatform"
- "(Ljava/lang/String;)Lwily/factoryapi/util/ModInfo;"
- "wily/factoryapi/util/ModInfo"
- "(Lwily/factoryapi/util/ModInfo;)Ljava/util/function/Supplier;"

### `wily/betterfurnaces/BetterFurnacesReforgedClient.class`

- "wily/factoryapi/FactoryAPIClient$PlayerEvent"
- "wily/factoryapi/FactoryAPIClient"
- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "wily/factoryapi/FactoryEvent$PackRegistry"
- "wily/factoryapi/FactoryEvent"
- "wily/factoryapi/FactoryAPIClient$MenuScreenRegister"
- "wily/factoryapi/base/config/FactoryConfig$StorageHandler"
- "wily/factoryapi/base/config/FactoryConfig"
- "wily/betterfurnaces/items/ColorUpgradeItem$ColorUpgradeMenu"
- "wily/betterfurnaces/items/ColorUpgradeItem"
- "ColorUpgradeMenu"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "(Lwily/factoryapi/base/RegisterListing$Holder;)V"
- "(Lwily/factoryapi/FactoryAPIClient$MenuScreenRegister;)V"
- "wily/factoryapi/FactoryAPIPlatform"
- "(Ljava/lang/String;)Lwily/factoryapi/util/ModInfo;"
- "(Lwily/factoryapi/util/ModInfo;Ljava/util/function/Function;)V"
- "Lwily/factoryapi/FactoryEvent;"
- "()Lwily/factoryapi/FactoryAPIClient$PlayerEvent;"
- "(Lwily/factoryapi/FactoryEvent$PackRegistry;)V"
- "Lwily/factoryapi/base/RegisterListing$Holder;"
- "wily/factoryapi/FactoryAPI"
- "Lwily/factoryapi/FactoryEvent$PackRegistry;"
- "java/lang/invoke/StringConcatFactory"
- "COLOR_UPGRADE_CONTAINER"
- "wily/betterfurnaces/client/screen/ColorUpgradeScreen"
- "(Lwily/betterfurnaces/items/ColorUpgradeItem$ColorUpgradeMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)V"
- "(Lwily/betterfurnaces/items/ColorUpgradeItem$ColorUpgradeMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)Lwily/betterfurnaces/client/screen/ColorUpgradeScreen;"
- "FUEL_VERIFIER_CONTAINER"
- "wily/betterfurnaces/client/screen/FuelVerifierScreen"
- "(Lwily/betterfurnaces/inventory/FuelVerifierMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)V"
- "(Lwily/betterfurnaces/inventory/FuelVerifierMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)Lwily/betterfurnaces/client/screen/FuelVerifierScreen;"
- "COB_GENERATOR_CONTAINER"
- "wily/betterfurnaces/client/screen/CobblestoneGeneratorScreen"
- "(Lwily/betterfurnaces/inventory/CobblestoneGeneratorMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)V"
- "(Lwily/betterfurnaces/inventory/CobblestoneGeneratorMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)Lwily/betterfurnaces/client/screen/CobblestoneGeneratorScreen;"
- "Lwily/factoryapi/FactoryAPIClient$MenuScreenRegister;"
- "(Lwily/factoryapi/base/RegisterListing$Holder;Lnet/minecraft/client/Minecraft;)V"
- "(Lwily/factoryapi/base/RegisterListing$Holder;)Ljava/util/function/Consumer;"
- "(Lwily/factoryapi/base/RegisterListing$Holder;Ljava/util/function/BiConsumer;)V"
- "Lwily/factoryapi/base/config/FactoryConfig$StorageHandler;"

### `wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity$1.class`

- "wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity$1"
- "CobblestoneGeneratorBlockEntity.java"
- "wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity"
- "Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity;"
- "(Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity;)V"
- "Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity$1;"

### `wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity$2.class`

- "wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity$2"
- "wily/factoryapi/base/FactoryItemSlot"
- "CobblestoneGeneratorBlockEntity.java"
- "wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity"
- "(Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity;Lnet/minecraft/world/Container;Lwily/factoryapi/base/SlotsIdentifier;Lwily/factoryapi/base/TransportState;III)V"
- "(Lnet/minecraft/world/Container;Lwily/factoryapi/base/SlotsIdentifier;Lwily/factoryapi/base/TransportState;III)V"
- "Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity$2;"
- "Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity;"
- "Lwily/factoryapi/base/SlotsIdentifier;"
- "Lwily/factoryapi/base/TransportState;"

### `wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity$3.class`

- "wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity$3"
- "wily/factoryapi/base/FactoryItemSlot"
- "CobblestoneGeneratorBlockEntity.java"
- "wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity"
- "(Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity;Lnet/minecraft/world/Container;Lwily/factoryapi/base/SlotsIdentifier;Lwily/factoryapi/base/TransportState;III)V"
- "(Lnet/minecraft/world/Container;Lwily/factoryapi/base/SlotsIdentifier;Lwily/factoryapi/base/TransportState;III)V"
- "Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity$3;"
- "Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity;"
- "Lwily/factoryapi/base/SlotsIdentifier;"
- "Lwily/factoryapi/base/TransportState;"

### `wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity$4.class`

- "wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity$4"
- "wily/betterfurnaces/inventory/SlotUpgrade"
- "CobblestoneGeneratorBlockEntity.java"
- "wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity"
- "(Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity;Lwily/betterfurnaces/blockentity/InventoryBlockEntity;III)V"
- "Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity$4;"
- "Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity;"
- "wily/betterfurnaces/items/FuelEfficiencyUpgradeItem"

### `wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity$5.class`

- "wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity$5"
- "wily/betterfurnaces/inventory/SlotUpgrade"
- "CobblestoneGeneratorBlockEntity.java"
- "wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity"
- "(Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity;Lwily/betterfurnaces/blockentity/InventoryBlockEntity;III)V"
- "Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity$5;"
- "Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity;"
- "wily/betterfurnaces/items/OreProcessingUpgradeItem"

### `wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity.class`

- "wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity"
- "CobblestoneGeneratorBlockEntity.java"
- "wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity$5"
- "wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity$4"
- "wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity$3"
- "wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity$2"
- "wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity$1"
- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "Ljava/util/List<Lnet/minecraft/world/item/crafting/RecipeHolder<Lwily/betterfurnaces/recipes/CobblestoneGeneratorRecipe;>;>;"
- "Lwily/betterfurnaces/recipes/CobblestoneGeneratorRecipe;"
- "UPGRADE"
- "UPGRADE1"
- "(Lnet/minecraft/core/Direction;)Lit/unimi/dsi/fastutil/Pair<[ILwily/factoryapi/base/TransportState;>;"
- "wily/factoryapi/base/TransportState"
- "Lwily/factoryapi/base/TransportState;"
- "Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity;"
- "wily/factoryapi/ItemContainerPlatform"
- "(Lnet/minecraft/world/item/ItemStack;)Lwily/factoryapi/util/FluidInstance;"
- "wily/factoryapi/util/FluidInstance"
- "(Lnet/minecraft/world/level/material/Fluid;I)Lwily/factoryapi/util/FluidInstance;"
- "(Lwily/factoryapi/util/FluidInstance;)Z"
- "wily/betterfurnaces/inventory/CobblestoneGeneratorMenu"
- "COB_GENERATOR_TILE"
- "Lwily/factoryapi/base/RegisterListing$Holder;"
- "(Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity;)V"
- "wily/betterfurnaces/blocks/CobblestoneGeneratorBlock"
- "()Ljava/util/List<Lnet/minecraft/world/item/crafting/RecipeHolder<Lwily/betterfurnaces/recipes/CobblestoneGeneratorRecipe;>;>;"
- "wily/factoryapi/base/network/CommonRecipeManager"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "(Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity;)Ljava/util/function/Supplier;"
- "wily/betterfurnaces/recipes/CobblestoneGeneratorRecipe"
- "Lwily/factoryapi/base/FactoryItemHandler;"
- "wily/factoryapi/base/FactoryItemHandler"
- "()Lwily/factoryapi/base/IPlatformItemHandler;"
- "wily/factoryapi/base/IPlatformItemHandler"
- "FUEL"
- "upgrade"
- "upgrade1"
- "getFuelEfficiencyMultiplier"
- "wily/betterfurnaces/items/FuelEfficiencyUpgradeItem"
- "wily/betterfurnaces/items/OreProcessingUpgradeItem"
- "wily/factoryapi/util/CompoundTagUtil"
- "(Lwily/factoryapi/base/FactoryStorage;Lnet/minecraft/core/Direction;)Lwily/factoryapi/base/ArbitrarySupplier;"
- "<T::Lwily/factoryapi/base/IPlatformHandler;>(Lwily/factoryapi/base/FactoryStorage<TT;>;Lnet/minecraft/core/Direction;)Lwily/factoryapi/base/ArbitrarySupplier<TT;>;"
- "wily/factoryapi/base/FactoryStorage"
- "Lwily/factoryapi/base/FactoryStorage;"
- "()Lwily/factoryapi/base/IPlatformHandler;"
- "(Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity;)Lwily/factoryapi/base/ArbitrarySupplier;"
- "wily/factoryapi/base/ArbitrarySupplier"
- "()Lwily/factoryapi/base/ArbitrarySupplier;"
- "Lwily/factoryapi/base/FactoryStorage<TT;>;"
- "(Ljava/util/function/Consumer<Lwily/factoryapi/base/FactoryItemSlot;>;Lnet/minecraft/world/entity/player/Player;)V"
- "wily/factoryapi/base/SlotsIdentifier"
- "Lwily/factoryapi/base/SlotsIdentifier;"
- "(Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity;Lnet/minecraft/world/Container;Lwily/factoryapi/base/SlotsIdentifier;Lwily/factoryapi/base/TransportState;III)V"
- "(Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity;Lwily/betterfurnaces/blockentity/InventoryBlockEntity;III)V"
- "Ljava/util/function/Consumer<Lwily/factoryapi/base/FactoryItemSlot;>;"
- "wily/factoryapi/FactoryAPIPlatform"
- "getPlatformFactoryStorage"
- "(Lnet/minecraft/world/level/block/entity/BlockEntity;)Lwily/factoryapi/base/IFactoryStorage;"
- "wily/factoryapi/base/IFactoryStorage"
- "wily/factoryapi/util/FactoryItemUtil"
- "Lwily/factoryapi/base/IPlatformItemHandler;"

### `wily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type.class`

- "wily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type"
- "Ljava/lang/Enum<Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;>;"
- "FactoryUpgradeSettings.java"
- "wily/betterfurnaces/blockentity/FactoryUpgradeSettings"
- "Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;"
- "[Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;"
- "()[Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;"
- "(Ljava/lang/String;)Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;"

### `wily/betterfurnaces/blockentity/FactoryUpgradeSettings.class`

- "wily/betterfurnaces/blockentity/FactoryUpgradeSettings"
- "FactoryUpgradeSettings.java"
- "wily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type"
- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "wily/betterfurnaces/init/ModObjects$UpgradeSetting"
- "UpgradeSetting"
- "(Lnet/minecraft/world/item/ItemStack;)Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "()[Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;"
- "[Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;"
- "(Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;Lnet/minecraft/world/item/ItemStack;)Z"
- "Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;"
- "(Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;)Lwily/factoryapi/base/RegisterListing$Holder;"
- "(Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;[I)V"
- "Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings;"
- "(Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;I)I"
- "(Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;)[I"
- "(Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;II)V"

### `wily/betterfurnaces/blockentity/ForgeBlockEntity.class`

- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "[Lwily/factoryapi/base/BlockSide;"
- "Lwily/factoryapi/base/RegisterListing$Holder;"
- "getFuelIndexes"
- "getUpgradeIndexes"
- "getEnergyCapacity"
- "()[Lwily/factoryapi/base/BlockSide;"
- "(Ljava/util/function/Consumer<Lwily/factoryapi/base/FactoryItemSlot;>;Lnet/minecraft/world/entity/player/Player;)V"
- "wily/betterfurnaces/inventory/SlotFuel"
- "wily/betterfurnaces/inventory/SlotUpgrade"
- "Ljava/util/function/Consumer<Lwily/factoryapi/base/FactoryItemSlot;>;"
- "wily/factoryapi/base/BlockSide"
- "Lwily/factoryapi/base/BlockSide;"

### `wily/betterfurnaces/blockentity/FuelVerifierBlockEntity$1.class`

- "wily/betterfurnaces/blockentity/FuelVerifierBlockEntity$1"
- "FuelVerifierBlockEntity.java"
- "wily/betterfurnaces/blockentity/FuelVerifierBlockEntity"
- "Lwily/betterfurnaces/blockentity/FuelVerifierBlockEntity;"
- "(Lwily/betterfurnaces/blockentity/FuelVerifierBlockEntity;)V"
- "Lwily/betterfurnaces/blockentity/FuelVerifierBlockEntity$1;"

### `wily/betterfurnaces/blockentity/FuelVerifierBlockEntity.class`

- "wily/betterfurnaces/blockentity/FuelVerifierBlockEntity"
- "FuelVerifierBlockEntity.java"
- "wily/betterfurnaces/blockentity/FuelVerifierBlockEntity$1"
- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "(Lnet/minecraft/core/Direction;)Lit/unimi/dsi/fastutil/Pair<[ILwily/factoryapi/base/TransportState;>;"
- "wily/factoryapi/base/TransportState"
- "Lwily/factoryapi/base/TransportState;"
- "Lwily/betterfurnaces/blockentity/FuelVerifierBlockEntity;"
- "wily/betterfurnaces/inventory/FuelVerifierMenu"
- "FUEL_VERIFIER_TILE"
- "Lwily/factoryapi/base/RegisterListing$Holder;"
- "(Lwily/betterfurnaces/blockentity/FuelVerifierBlockEntity;)V"
- "Lwily/factoryapi/base/FactoryItemHandler;"
- "wily/factoryapi/base/FactoryItemHandler"
- "wily/factoryapi/base/FuelManager"
- "fuel"
- "wily/factoryapi/util/CompoundTagUtil"
- "(Lwily/factoryapi/base/FactoryStorage;Lnet/minecraft/core/Direction;)Lwily/factoryapi/base/ArbitrarySupplier;"
- "<T::Lwily/factoryapi/base/IPlatformHandler;>(Lwily/factoryapi/base/FactoryStorage<TT;>;Lnet/minecraft/core/Direction;)Lwily/factoryapi/base/ArbitrarySupplier<TT;>;"
- "wily/factoryapi/base/FactoryStorage"
- "Lwily/factoryapi/base/FactoryStorage;"
- "()Lwily/factoryapi/base/IPlatformHandler;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "(Lwily/betterfurnaces/blockentity/FuelVerifierBlockEntity;)Lwily/factoryapi/base/ArbitrarySupplier;"
- "wily/factoryapi/base/ArbitrarySupplier"
- "()Lwily/factoryapi/base/ArbitrarySupplier;"
- "Lwily/factoryapi/base/FactoryStorage<TT;>;"
- "(Ljava/util/function/Consumer<Lwily/factoryapi/base/FactoryItemSlot;>;Lnet/minecraft/world/entity/player/Player;)V"
- "wily/betterfurnaces/inventory/SlotFuel"
- "Ljava/util/function/Consumer<Lwily/factoryapi/base/FactoryItemSlot;>;"

### `wily/betterfurnaces/blockentity/IInventoryBlockEntity.class`

- "(Lnet/minecraft/core/Direction;)Lit/unimi/dsi/fastutil/Pair<[ILwily/factoryapi/base/TransportState;>;"
- "()Lnet/minecraft/core/NonNullList<Lwily/factoryapi/base/FactoryItemSlot;>;"
- "(Lnet/minecraft/world/entity/player/Player;)Lnet/minecraft/core/NonNullList<Lwily/factoryapi/base/FactoryItemSlot;>;"
- "(Lwily/factoryapi/base/FactoryItemSlot;)V"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "Lnet/minecraft/core/NonNullList<Lwily/factoryapi/base/FactoryItemSlot;>;"
- "(Ljava/util/function/Consumer<Lwily/factoryapi/base/FactoryItemSlot;>;Lnet/minecraft/world/entity/player/Player;)V"

### `wily/betterfurnaces/blockentity/InventoryBlockEntity$1.class`

- "wily/factoryapi/base/FactoryItemHandler"
- "(Lwily/betterfurnaces/blockentity/InventoryBlockEntity;ILnet/minecraft/world/level/block/entity/BlockEntity;Lwily/factoryapi/base/TransportState;)V"
- "(ILnet/minecraft/world/level/block/entity/BlockEntity;Lwily/factoryapi/base/TransportState;)V"
- "Lwily/factoryapi/base/TransportState;"
- "wily/factoryapi/base/FactoryItemSlot"

### `wily/betterfurnaces/blockentity/InventoryBlockEntity.class`

- "wily/factoryapi/base/IFactoryStorage"
- "Lnet/minecraft/core/NonNullList<Lwily/factoryapi/base/FactoryItemSlot;>;"
- "Lwily/factoryapi/base/FactoryItemHandler;"
- "wily/factoryapi/base/TransportState"
- "Lwily/factoryapi/base/TransportState;"
- "(Lwily/betterfurnaces/blockentity/InventoryBlockEntity;ILnet/minecraft/world/level/block/entity/BlockEntity;Lwily/factoryapi/base/TransportState;)V"
- "()Lnet/minecraft/core/NonNullList<Lwily/factoryapi/base/FactoryItemSlot;>;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "wily/factoryapi/util/CompoundTagUtil"
- "wily/factoryapi/base/FactoryItemHandler"
- "()Lwily/factoryapi/base/IPlatformItemHandler;"

### `wily/betterfurnaces/blockentity/SmeltingBlockEntity$1.class`

- "wily/betterfurnaces/blockentity/FactoryUpgradeSettings"
- "wily/betterfurnaces/items/UpgradeItem$Type"
- "wily/betterfurnaces/items/UpgradeItem"
- "FACTORY"
- "Lwily/betterfurnaces/items/UpgradeItem$Type;"
- "getUpgradeTypeStack"
- "(Lwily/betterfurnaces/items/UpgradeItem$Type;)Lnet/minecraft/world/item/ItemStack;"

### `wily/betterfurnaces/blockentity/SmeltingBlockEntity$2.class`

- "cookTime"
- "totalCookTime"
- "energyStorage"
- "Lwily/factoryapi/base/IPlatformEnergyStorage;"
- "wily/factoryapi/base/IPlatformEnergyStorage"
- "getEnergyStored"
- "getMaxEnergyStored"
- "setEnergyStored"

### `wily/betterfurnaces/blockentity/SmeltingBlockEntity.class`

- "wily/factoryapi/FactoryAPI$Loader"
- "wily/factoryapi/FactoryAPI"
- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "wily/betterfurnaces/items/UpgradeItem$Type"
- "wily/betterfurnaces/items/UpgradeItem"
- "wily/betterfurnaces/blocks/SmeltingBlock$Tier"
- "Tier"
- "wily/factoryapi/ItemContainerPlatform$ItemEnergyContext"
- "wily/factoryapi/ItemContainerPlatform"
- "ItemEnergyContext"
- "wily/factoryapi/ItemContainerPlatform$ItemFluidContext"
- "cookTime"
- "totalCookTime"
- "Lnet/minecraft/world/item/crafting/RecipeType<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings;"
- "energyStorage"
- "Lwily/factoryapi/base/IPlatformEnergyStorage;"
- "Lwily/factoryapi/base/FactoryItemFluidHandler;"
- "generatorTank"
- "Ljava/util/Map<Lnet/minecraft/world/item/crafting/RecipeType<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;Lwily/betterfurnaces/blockentity/LRUCache<Lnet/minecraft/world/item/Item;Ljava/util/Optional<Lnet/minecraft/world/item/crafting/RecipeHolder<Lnet/minecraft/world/item/crafting/Abs…"
- "getCookTime"
- "wily/factoryapi/base/FactoryEnergyStorage"
- "getEnergyCapacity"
- "()Lwily/factoryapi/FactoryAPI$Loader;"
- "Lwily/factoryapi/base/RegisterListing$Holder;"
- "getFuelIndexes"
- "Lwily/betterfurnaces/items/UpgradeItem$Type;"
- "hasUpgradeType"
- "(Lwily/betterfurnaces/items/UpgradeItem$Type;)Z"
- "getUpgradeIndexes"
- "getEnergyConsume"
- "getRecipeCookingTime"
- "(Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;)I"
- "net/minecraft/world/item/crafting/AbstractCookingRecipe"
- "getCookingTime"
- "Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;"
- "(Lwily/betterfurnaces/blockentity/LRUCache<Lnet/minecraft/world/item/Item;Ljava/util/Optional<Lnet/minecraft/world/item/crafting/RecipeHolder<Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;>;>;Lnet/minecraft/world/item/Item;)I"
- "Lwily/betterfurnaces/blockentity/LRUCache<Lnet/minecraft/world/item/Item;Ljava/util/Optional<Lnet/minecraft/world/item/crafting/RecipeHolder<Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;>;>;"
- "Ljava/util/Optional<Lnet/minecraft/world/item/crafting/RecipeHolder<Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;>;"
- "()Lwily/betterfurnaces/blockentity/LRUCache<Lnet/minecraft/world/item/Item;Ljava/util/Optional<Lnet/minecraft/world/item/crafting/RecipeHolder<Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;>;>;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "(Lnet/minecraft/world/item/ItemStack;Lnet/minecraft/world/item/crafting/RecipeType<Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;)Ljava/util/Optional<Lnet/minecraft/world/item/crafting/RecipeHolder<Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;>;"
- "wily/factoryapi/base/network/CommonRecipeManager"
- "Lnet/minecraft/world/item/crafting/RecipeType<Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "(Lnet/minecraft/world/item/ItemStack;)Ljava/util/Optional<Lnet/minecraft/world/item/crafting/RecipeHolder<Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;>;"
- "hasUpgrade"
- "(Lwily/betterfurnaces/items/UpgradeItem;)Z"
- "FUEL"
- "getEnderMultiplier"
- "getUpgradeTypeStack"
- "(Lwily/betterfurnaces/items/UpgradeItem$Type;)Lnet/minecraft/world/item/ItemStack;"
- "wily/betterfurnaces/items/FuelEfficiencyUpgradeItem"
- "multiplier"
- "isEnergy"
- "ENERGY"
- "wily/factoryapi/base/IPlatformEnergyStorage"
- "getEnergyStored"
- "GENERATOR"
- "getDefaultCookTime"
- "getSpeed"
- "speed"
- "Lwily/factoryapi/base/FactoryItemHandler;"
- "wily/factoryapi/base/FactoryItemHandler"
- "lambda$getSpeed$2"
- "getUpgrades"
- "()Ljava/util/List<Lwily/betterfurnaces/items/UpgradeItem;>;"
- "Lwily/betterfurnaces/items/UpgradeItem;"
- "Ljava/util/List<Lwily/betterfurnaces/items/UpgradeItem;>;"
- "allUpgradesMatch"
- "(Ljava/util/function/Predicate<Lwily/betterfurnaces/items/UpgradeItem;>;)Z"
- "upgradeItem"
- "Ljava/util/function/Predicate<Lwily/betterfurnaces/items/UpgradeItem;>;"
- "hasUpgradeFromSameType"
- "getUpgradeSlotFromSameType"
- "(Lwily/betterfurnaces/items/UpgradeItem;)I"
- "getUpgradeTypeSlot"
- "(Lwily/betterfurnaces/items/UpgradeItem$Type;)I"
- "tier"
- "Lwily/betterfurnaces/blocks/SmeltingBlock$Tier;"
- "defaultCookTime"
- "getUpgradeStack"
- "(Ljava/util/function/Predicate<Lwily/betterfurnaces/items/UpgradeItem;>;)Lnet/minecraft/world/item/ItemStack;"
- "getUpgradeSlot"
- "lambda$getUpgradeTypeStack$3"
- "(Lwily/betterfurnaces/items/UpgradeItem$Type;Lwily/betterfurnaces/items/UpgradeItem;)Z"
- "(Lwily/betterfurnaces/items/UpgradeItem$Type;)Ljava/util/function/Predicate;"
- "(Lwily/betterfurnaces/items/UpgradeItem;)Lnet/minecraft/world/item/ItemStack;"
- "(Lwily/betterfurnaces/items/UpgradeItem;)Ljava/util/function/Predicate;"
- "lambda$getUpgradeTypeSlot$4"
- "(Ljava/util/function/Predicate<Lwily/betterfurnaces/items/UpgradeItem;>;)I"
- "getUpgradeSlotItem"
- "(Lwily/factoryapi/util/FluidInstance;)I"
- "wily/factoryapi/util/FluidInstance"
- "wily/factoryapi/base/FuelManager"
- "Lwily/factoryapi/util/FluidInstance;"
- "Lnet/minecraft/world/item/crafting/RecipeHolder<Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "tooltip.betterfurnacesreforged.\u0001_tier"
- "java/lang/invoke/StringConcatFactory"
- "tooltip.betterfurnacesreforged.generator"
- "(I)Lnet/minecraft/world/item/crafting/RecipeHolder<Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "canGeneratorWork"
- "(Lnet/minecraft/world/item/ItemStack;)Lwily/factoryapi/util/FluidInstance;"
- "getEnergySpace"
- "FACTORY"
- "wily/factoryapi/FactoryAPIPlatform"
- "getPlatformFactoryStorage"
- "(Lnet/minecraft/world/level/block/entity/BlockEntity;)Lwily/factoryapi/base/IFactoryStorage;"
- "wily/factoryapi/base/FactoryStorage"
- "Lwily/factoryapi/base/FactoryStorage;"
- "wily/factoryapi/base/IFactoryStorage"
- "(Lwily/factoryapi/base/FactoryStorage;Lnet/minecraft/core/Direction;)Lwily/factoryapi/base/ArbitrarySupplier;"
- "wily/factoryapi/base/ArbitrarySupplier"
- "receiveEnergy"
- "consumeEnergy"
- "isEnergyContainer"
- "getEnergy"
- "extractEnergy"
- "(ILnet/minecraft/world/item/ItemStack;)Lwily/factoryapi/ItemContainerPlatform$ItemEnergyContext;"
- "contextEnergy"
- "wily/betterfurnaces/items/LiquidFuelUpgradeItem"
- "getFuelTank"
- "()Lwily/factoryapi/base/FactoryItemFluidHandler;"
- "wily/factoryapi/base/FactoryItemFluidHandler"
- "(ILnet/minecraft/world/item/ItemStack;)Lwily/factoryapi/ItemContainerPlatform$ItemFluidContext;"
- "()Lwily/factoryapi/util/FluidInstance;"
- "(Lwily/factoryapi/util/FluidInstance;Z)I"
- "(IZ)Lwily/factoryapi/util/FluidInstance;"
- "getOreProcessingMultiplier"
- "isFuel"
- "storageFuel"
- "Lwily/factoryapi/ItemContainerPlatform$ItemFluidContext;"
- "fuel"
- "[Lnet/minecraft/world/item/crafting/RecipeType<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "get_cook_time"
- "colorUpgrade"
- "wily/betterfurnaces/blockentity/FactoryUpgradeSettings"
- "()[Lwily/factoryapi/base/BlockSide;"
- "wily/factoryapi/base/BlockSide"
- "Lwily/factoryapi/base/BlockSide;"
- "(Lnet/minecraft/world/level/block/state/BlockState;[Lwily/factoryapi/base/BlockSide;)Lnet/minecraft/core/Direction;"
- "Lwily/factoryapi/base/config/FactoryConfig;"
- "wily/factoryapi/base/config/FactoryConfig"
- "wily/betterfurnaces/items/OreProcessingUpgradeItem"
- "Lwily/betterfurnaces/items/OreProcessingUpgradeItem;"
- "(Lnet/minecraft/world/item/crafting/RecipeHolder<Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;II)Z"
- "()Lwily/factoryapi/base/IPlatformItemHandler;"
- "wily/factoryapi/base/IPlatformItemHandler"
- "(Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;Lnet/minecraft/world/item/ItemStack;)Lnet/minecraft/world/item/ItemStack;"
- "wily/factoryapi/util/FactoryItemUtil"
- "(Lnet/minecraft/world/item/crafting/RecipeHolder<Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;II)V"
- "(Lnet/minecraft/world/level/material/Fluid;I)Lwily/factoryapi/util/FluidInstance;"
- "(Lnet/minecraft/world/item/ItemStack;Lwily/factoryapi/util/FluidInstance;)Lwily/factoryapi/ItemContainerPlatform$ItemFluidContext;"
- "(Lnet/minecraft/world/item/ItemStack;)Lwily/factoryapi/base/IPlatformFluidHandler;"
- "wily/betterfurnaces/items/XpTankUpgradeItem"
- "getGeneratorTank"
- "wily/betterfurnaces/items/GeneratorUpgradeItem"
- "wily/factoryapi/util/CompoundTagUtil"
- "CookTime"
- "CookTimeTotal"
- "wily/factoryapi/base/IPlatformFluidHandler"
- "(Lwily/factoryapi/base/FactoryItemFluidHandler;)Ljava/util/function/Consumer;"
- "energy"
- "<T::Lwily/factoryapi/base/IPlatformHandler;>(Lwily/factoryapi/base/FactoryStorage<TT;>;Lnet/minecraft/core/Direction;)Lwily/factoryapi/base/ArbitrarySupplier<TT;>;"
- "wily/factoryapi/base/TransportState"
- "Lwily/factoryapi/base/TransportState;"
- "(Lwily/factoryapi/base/IPlatformFluidHandler;Lnet/minecraft/core/Direction;Lwily/factoryapi/base/TransportState;)Lwily/factoryapi/base/IPlatformFluidHandler;"
- "(Ljava/lang/Object;)Lwily/factoryapi/base/ArbitrarySupplier;"
- "()Lwily/factoryapi/base/ArbitrarySupplier;"
- "(Lwily/factoryapi/base/IPlatformItemHandler;Lnet/minecraft/core/Direction;[ILwily/factoryapi/base/TransportState;)Lwily/factoryapi/base/IPlatformItemHandler;"
- "(ZZ)Lwily/factoryapi/base/TransportState;"
- "(Lwily/factoryapi/base/IPlatformEnergyStorage;Lnet/minecraft/core/Direction;Lwily/factoryapi/base/TransportState;)Lwily/factoryapi/base/IPlatformEnergyStorage;"
- "Lwily/factoryapi/base/FactoryStorage<TT;>;"
- "(Lnet/minecraft/core/Direction;)Lit/unimi/dsi/fastutil/Pair<[ILwily/factoryapi/base/TransportState;>;"
- "(Ljava/util/function/Consumer<Lwily/factoryapi/base/FactoryItemSlot;>;Lnet/minecraft/world/entity/player/Player;)V"
- "(Lwily/factoryapi/base/FactoryItemSlot;)Z"
- "wily/betterfurnaces/inventory/SlotFuel"
- "wily/betterfurnaces/inventory/SlotUpgrade"
- "Ljava/util/function/Consumer<Lwily/factoryapi/base/FactoryItemSlot;>;"
- "Lnet/minecraft/world/item/crafting/RecipeHolder<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "Lwily/factoryapi/base/IPlatformItemHandler;"
- "Lwily/factoryapi/base/FactoryItemSlot;"
- "upgradeType"

### `wily/betterfurnaces/blocks/BFRBlock.class`

- "wily/factoryapi/base/network/OpenExtraMenuPayload"

### `wily/betterfurnaces/blocks/CobblestoneGeneratorBlock.class`

- "wily/betterfurnaces/blocks/CobblestoneGeneratorBlock"
- "CobblestoneGeneratorBlock.java"
- "wily/betterfurnaces/items/UpgradeItem$Type"
- "wily/betterfurnaces/items/UpgradeItem"
- "COBBLESTONE_GENERATOR"
- "cobblestone_generator"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "Lwily/betterfurnaces/blocks/CobblestoneGeneratorBlock;"
- "upgradeType"
- "Lwily/betterfurnaces/items/UpgradeItem$Type;"
- "FUEL"
- "wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity"
- "wily/factoryapi/base/FactoryItemSlot"
- "Lwily/factoryapi/base/FactoryItemHandler;"
- "wily/factoryapi/base/FactoryItemHandler"
- "Lwily/betterfurnaces/items/UpgradeItem;"
- "Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity;"

### `wily/betterfurnaces/blocks/ForgeBlock.class`

- "wily/betterfurnaces/blocks/SmeltingBlock$Tier"
- "Tier"
- "wily/betterfurnaces/items/UpgradeItem$Type"
- "wily/betterfurnaces/items/UpgradeItem"
- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "defaultCookTime"
- "(Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;Lwily/betterfurnaces/blocks/SmeltingBlock$Tier;)V"
- "wily/factoryapi/util/VoxelShapeUtil"
- "interactUpgrade"
- "upgradeType"
- "Lwily/betterfurnaces/items/UpgradeItem$Type;"
- "ALTERNATIVE_FUEL"
- "Lwily/factoryapi/base/FactoryItemHandler;"
- "wily/factoryapi/base/FactoryItemHandler"
- "Lwily/factoryapi/base/RegisterListing$Holder;"

### `wily/betterfurnaces/blocks/FuelVerifierBlock.class`

- "wily/betterfurnaces/blocks/FuelVerifierBlock"
- "FuelVerifierBlock.java"
- "FUEL_VERIFIER"
- "fuel_verifier"
- "Lwily/betterfurnaces/blocks/FuelVerifierBlock;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "wily/betterfurnaces/blockentity/FuelVerifierBlockEntity"
- "Lwily/betterfurnaces/blockentity/FuelVerifierBlockEntity;"

### `wily/betterfurnaces/blocks/SmeltingBlock$Tier.class`

- "wily/betterfurnaces/blocks/SmeltingBlock$Tier"
- "Tier"
- "defaultCookTime"
- "Lwily/betterfurnaces/blocks/SmeltingBlock$Tier;"
- "name;defaultCookTime"
- "(Lwily/betterfurnaces/blocks/SmeltingBlock$Tier;)Ljava/lang/String;"
- "(Lwily/betterfurnaces/blocks/SmeltingBlock$Tier;)I"
- "(Lwily/betterfurnaces/blocks/SmeltingBlock$Tier;Ljava/lang/Object;)Z"

### `wily/betterfurnaces/blocks/SmeltingBlock.class`

- "wily/betterfurnaces/blocks/SmeltingBlock$Tier"
- "Tier"
- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "wily/betterfurnaces/items/UpgradeItem$Type"
- "wily/betterfurnaces/items/UpgradeItem"
- "tier"
- "Lwily/betterfurnaces/blocks/SmeltingBlock$Tier;"
- "(Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;Lwily/betterfurnaces/blocks/SmeltingBlock$Tier;)V"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "wily/factoryapi/util/FactoryItemUtil"
- "Lwily/factoryapi/base/RegisterListing$Holder;"
- "getUpgradeStack"
- "(Lwily/betterfurnaces/items/UpgradeItem;)Lnet/minecraft/world/item/ItemStack;"
- "Lwily/factoryapi/base/FactoryItemHandler;"
- "wily/factoryapi/base/FactoryItemHandler"
- "colorUpgrade"
- "interactUpgrade"
- "wily/factoryapi/ItemContainerPlatform"
- "wily/factoryapi/base/Bearer"
- "(Ljava/lang/Object;)Lwily/factoryapi/base/Bearer;"
- "GENERATOR"
- "hasUpgrade"
- "(Lwily/betterfurnaces/items/UpgradeItem;)Z"
- "(Lnet/minecraft/world/item/ItemStack;)Lwily/factoryapi/util/FluidInstance;"
- "wily/factoryapi/util/FluidInstance"
- "getUpgradeSlotItem"
- "wily/factoryapi/FactoryAPIPlatform"
- "(Lnet/minecraft/world/item/ItemStack;)Lwily/factoryapi/base/IPlatformFluidHandler;"
- "(ILnet/minecraft/world/entity/player/Player;Lnet/minecraft/world/InteractionHand;)Lwily/factoryapi/util/FluidInstance;"
- "wily/factoryapi/base/IPlatformFluidHandler"
- "(Lwily/factoryapi/util/FluidInstance;Z)I"
- "wily/betterfurnaces/items/LiquidFuelUpgradeItem"
- "wily/factoryapi/base/FactoryStorage"
- "Lwily/factoryapi/base/FactoryStorage;"
- "(Lwily/factoryapi/base/FactoryStorage;Lnet/minecraft/core/Direction;)Lwily/factoryapi/base/ArbitrarySupplier;"
- "(Lnet/minecraft/world/item/ItemStack;Lwily/factoryapi/base/Bearer;Lnet/minecraft/world/entity/player/Player;Lnet/minecraft/world/InteractionHand;Lwily/factoryapi/base/IPlatformFluidHandler;)V"
- "(Lwily/factoryapi/base/IPlatformFluidHandler;)V"
- "(Lnet/minecraft/world/item/ItemStack;Lwily/factoryapi/base/Bearer;Lnet/minecraft/world/entity/player/Player;Lnet/minecraft/world/InteractionHand;)Ljava/util/function/Consumer;"
- "wily/factoryapi/base/ArbitrarySupplier"
- "Lwily/betterfurnaces/items/UpgradeItem;"
- "Lwily/factoryapi/base/Bearer<Ljava/lang/Integer;>;"
- "Lwily/factoryapi/base/Bearer;"
- "hasUpgradeFromSameType"
- "getUpgradeIndexes"
- "wily/factoryapi/base/FactoryItemSlot"
- "wily/factoryapi/util/CompoundTagUtil"
- "Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings;"
- "wily/betterfurnaces/blockentity/FactoryUpgradeSettings"
- "FACTORY"
- "Lwily/betterfurnaces/items/UpgradeItem$Type;"
- "hasUpgradeType"
- "(Lwily/betterfurnaces/items/UpgradeItem$Type;)Z"
- "()Lwily/factoryapi/util/FluidInstance;"
- "(Lwily/factoryapi/util/FluidInstance;)Z"
- "Lwily/factoryapi/base/IPlatformFluidHandler;"

### `wily/betterfurnaces/client/BFRClientConfig.class`

- "wily/factoryapi/base/config/FactoryConfig$StorageHandler"
- "wily/factoryapi/base/config/FactoryConfig"
- "wily/factoryapi/base/config/FactoryConfigDisplay$Instance"
- "wily/factoryapi/base/config/FactoryConfigDisplay"
- "wily/factoryapi/base/config/FactoryConfig$StorageAccess"
- "Lwily/factoryapi/base/config/FactoryConfig$StorageHandler;"
- "Lwily/factoryapi/base/config/FactoryConfig;"
- "Lwily/factoryapi/base/config/FactoryConfig<Ljava/lang/Boolean;>;"
- "(Ljava/lang/String;)Lwily/factoryapi/base/config/FactoryConfig$StorageHandler;"
- "(Lnet/minecraft/network/chat/Component;)Lwily/factoryapi/base/config/FactoryConfigDisplay$Instance;"
- "wily/factoryapi/base/config/FactoryConfigControl"
- "Lwily/factoryapi/base/config/FactoryConfigControl;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "(Ljava/lang/String;Lwily/factoryapi/base/config/FactoryConfigDisplay;Lwily/factoryapi/base/config/FactoryConfigControl;Ljava/lang/Object;Ljava/util/function/Consumer;Lwily/factoryapi/base/config/FactoryConfig$StorageAccess;)Lwily/factoryapi/base/config/FactoryConfig;"
- "(Lwily/factoryapi/base/config/FactoryConfig;)Lwily/factoryapi/base/config/FactoryConfig;"

### `wily/betterfurnaces/client/renderer/ForgeRenderer.class`

- "java/lang/invoke/StringConcatFactory"
- "wily/factoryapi/FactoryAPIClient"
- "wily/factoryapi/util/DirectionUtil"

### `wily/betterfurnaces/client/renderer/FurnaceRenderer$FurnaceOverlay.class`

- "GENERATOR"
- "java/lang/invoke/StringConcatFactory"
- "generator"

### `wily/betterfurnaces/client/renderer/FurnaceRenderer.class`

- "wily/factoryapi/FactoryAPIClient"
- "wily/factoryapi/util/DirectionUtil"

### `wily/betterfurnaces/client/screen/AbstractBasicScreen.class`

- "<T:Lnet/minecraft/world/inventory/AbstractContainerMenu;>Lnet/minecraft/client/gui/screens/inventory/AbstractContainerScreen<TT;>;Lwily/factoryapi/base/client/IWindowWidget;"
- "wily/factoryapi/base/client/IWindowWidget"

### `wily/betterfurnaces/client/screen/AbstractUpgradeScreen.class`

- "wily/betterfurnaces/client/screen/AbstractUpgradeScreen"
- "<T:Lwily/betterfurnaces/inventory/AbstractUpgradeMenu;>Lwily/betterfurnaces/client/screen/AbstractBasicScreen<TT;>;"
- "AbstractUpgradeScreen.java"
- "(Lwily/betterfurnaces/inventory/AbstractUpgradeMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)V"
- "textures/container/upgrades_gui.png"
- "Lwily/betterfurnaces/client/screen/AbstractUpgradeScreen<TT;>;"
- "Lwily/betterfurnaces/client/screen/AbstractUpgradeScreen;"
- "Lwily/betterfurnaces/inventory/AbstractUpgradeMenu;"
- "wily/factoryapi/base/client/FactoryGuiGraphics"
- "(Lnet/minecraft/client/gui/GuiGraphics;)Lwily/factoryapi/base/client/FactoryGuiGraphics;"
- "wily/betterfurnaces/inventory/AbstractUpgradeMenu"

### `wily/betterfurnaces/client/screen/BFRConfigScreen.class`

- "wily/factoryapi/base/client/screen/FactoryConfigScreen"
- "wily/factoryapi/base/config/FactoryConfig"
- "Lwily/factoryapi/base/config/FactoryConfig;"
- "copperTierSpeed"
- "ironTierSpeed"
- "steelTierSpeed"
- "goldTierSpeed"
- "amethystTierSpeed"
- "diamondTierSpeed"
- "platinumTierSpeed"
- "extremeTierSpeed"
- "ultimateTierSpeed"

### `wily/betterfurnaces/client/screen/BetterFurnacesDrawables.class`

- "wily/factoryapi/base/client/drawable/IFactoryDrawableType$DrawableImage"
- "wily/factoryapi/base/client/drawable/IFactoryDrawableType"
- "wily/factoryapi/base/client/drawable/IFactoryDrawableType$Direction"
- "wily/factoryapi/base/client/drawable/IFactoryDrawableType$DrawableProgress"
- "ENERGY_CELL"
- "Lwily/factoryapi/base/client/drawable/IFactoryDrawableType$DrawableProgress;"
- "THIN_ENERGY_CELL"
- "Lwily/factoryapi/base/client/drawable/IFactoryDrawableType$DrawableImage;"
- "FACTORY_UPGRADE_WINDOW"
- "Lwily/factoryapi/base/client/drawable/IFactoryDrawableType;"
- "FUEL_SLOT_OUTLINE"
- "FACTORY_BUTTON"
- "(I)Lwily/factoryapi/base/client/drawable/IFactoryDrawableType;"
- "(Lnet/minecraft/resources/ResourceLocation;IIII)Lwily/factoryapi/base/client/drawable/IFactoryDrawableType$DrawableImage;"
- "([IZLwily/factoryapi/base/client/drawable/IFactoryDrawableType$Direction;)Lwily/factoryapi/base/client/drawable/IFactoryDrawableType$DrawableProgress;"
- "(ZLwily/factoryapi/base/client/drawable/IFactoryDrawableType$Direction;)Lwily/factoryapi/base/client/drawable/IFactoryDrawableType$DrawableProgress;"
- "Lwily/factoryapi/base/client/drawable/IFactoryDrawableType$Direction;"
- "wily/factoryapi/FactoryAPI"
- "(Lnet/minecraft/resources/ResourceLocation;IIZ)Lwily/factoryapi/base/client/drawable/IFactoryDrawableType$DrawableImage;"

### `wily/betterfurnaces/client/screen/CobblestoneGeneratorScreen.class`

- "wily/betterfurnaces/client/screen/CobblestoneGeneratorScreen"
- "Lwily/betterfurnaces/client/screen/AbstractBasicScreen<Lwily/betterfurnaces/inventory/CobblestoneGeneratorMenu;>;"
- "CobblestoneGeneratorScreen.java"
- "wily/betterfurnaces/network/CobblestoneGeneratorSyncPayload$Sync"
- "wily/betterfurnaces/network/CobblestoneGeneratorSyncPayload"
- "wily/factoryapi/base/network/CommonNetwork$Payload"
- "wily/factoryapi/base/network/CommonNetwork"
- "Lwily/factoryapi/util/FluidInstance;"
- "Lwily/factoryapi/base/client/drawable/FactoryDrawableButton;"
- "(Lwily/betterfurnaces/inventory/CobblestoneGeneratorMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)V"
- "Lwily/betterfurnaces/client/screen/CobblestoneGeneratorScreen;"
- "Lwily/betterfurnaces/inventory/CobblestoneGeneratorMenu;"
- "wily/factoryapi/base/client/drawable/FactoryDrawableButton"
- "Lwily/factoryapi/base/client/drawable/IFactoryDrawableType;"
- "(IILwily/factoryapi/base/client/drawable/IFactoryDrawableType;)V"
- "(Lwily/factoryapi/base/client/drawable/FactoryDrawableButton;Ljava/lang/Integer;)V"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "(Lwily/betterfurnaces/client/screen/CobblestoneGeneratorScreen;)Ljava/util/function/BiConsumer;"
- "(Ljava/util/function/BiConsumer;)Lwily/factoryapi/base/client/drawable/AbstractDrawableButton;"
- "(F)Lwily/factoryapi/base/client/drawable/AbstractDrawableButton;"
- "(I)Lwily/factoryapi/base/client/drawable/IFactoryDrawableType;"
- "(Lwily/factoryapi/base/client/drawable/IFactoryDrawableType;)Lwily/factoryapi/base/client/drawable/AbstractDrawableButton;"
- "(Lnet/minecraft/client/gui/GuiGraphics;IIIILwily/factoryapi/util/FluidInstance;Z)V"
- "wily/factoryapi/base/client/FactoryGuiGraphics"
- "(Lnet/minecraft/client/gui/GuiGraphics;)Lwily/factoryapi/base/client/FactoryGuiGraphics;"
- "wily/factoryapi/util/FluidRenderUtil"
- "(Lwily/factoryapi/util/FluidInstance;)I"
- "wily/factoryapi/util/FluidInstance"
- "wily/factoryapi/FactoryAPIClient"
- "wily/betterfurnaces/inventory/CobblestoneGeneratorMenu"
- "wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity"
- "()Lwily/factoryapi/base/client/drawable/AbstractDrawableStatic;"
- "(Lnet/minecraft/network/chat/Component;)Lwily/factoryapi/base/client/drawable/AbstractDrawableStatic;"
- "(Ljava/lang/Boolean;)Lwily/factoryapi/base/client/drawable/AbstractDrawableButton;"
- "java/lang/invoke/StringConcatFactory"
- "(Ljava/util/List;)Lwily/factoryapi/base/client/drawable/AbstractDrawableStatic;"
- "Lwily/betterfurnaces/network/CobblestoneGeneratorSyncPayload$Sync;"
- "(Lnet/minecraft/core/BlockPos;Lwily/betterfurnaces/network/CobblestoneGeneratorSyncPayload$Sync;)V"
- "(Lwily/factoryapi/base/network/CommonNetwork$Payload;)V"
- "textures/container/cobblestone_generator_gui.png"
- "(Lnet/minecraft/world/level/material/Fluid;)Lwily/factoryapi/util/FluidInstance;"

### `wily/betterfurnaces/client/screen/ColorUpgradeScreen.class`

- "wily/betterfurnaces/client/screen/ColorUpgradeScreen"
- "Lwily/betterfurnaces/client/screen/AbstractUpgradeScreen<Lwily/betterfurnaces/items/ColorUpgradeItem$ColorUpgradeMenu;>;"
- "wily/betterfurnaces/client/screen/AbstractUpgradeScreen"
- "ColorUpgradeScreen.java"
- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "wily/betterfurnaces/items/ColorUpgradeItem$ColorUpgradeMenu"
- "wily/betterfurnaces/items/ColorUpgradeItem"
- "ColorUpgradeMenu"
- "wily/factoryapi/base/network/CommonNetwork$Payload"
- "wily/factoryapi/base/network/CommonNetwork"
- "Lwily/factoryapi/base/client/drawable/FactoryDrawableSlider;"
- "(Lwily/betterfurnaces/items/ColorUpgradeItem$ColorUpgradeMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)V"
- "(Lwily/betterfurnaces/inventory/AbstractUpgradeMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)V"
- "(Lwily/betterfurnaces/network/SliderColorSyncPayload$Channel;)Lwily/factoryapi/base/client/drawable/FactoryDrawableSlider;"
- "Lwily/betterfurnaces/client/screen/ColorUpgradeScreen;"
- "Lwily/betterfurnaces/items/ColorUpgradeItem$ColorUpgradeMenu;"
- "wily/factoryapi/base/client/drawable/FactoryDrawableSlider"
- "wily/factoryapi/base/client/drawable/FactoryDrawableButton"
- "Lwily/factoryapi/base/client/drawable/IFactoryDrawableType;"
- "(IILwily/factoryapi/base/client/drawable/IFactoryDrawableType;)V"
- "(I)Lwily/factoryapi/base/client/drawable/IFactoryDrawableType;"
- "(Lwily/factoryapi/base/client/drawable/IFactoryDrawableType;)Lwily/factoryapi/base/client/drawable/AbstractDrawableButton;"
- "Lwily/factoryapi/base/RegisterListing$Holder;"
- "(Lnet/minecraft/network/chat/Component;)Lwily/factoryapi/base/client/drawable/AbstractDrawableStatic;"
- "(Lwily/factoryapi/base/client/drawable/FactoryDrawableButton;Ljava/lang/Integer;)V"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "(Lwily/betterfurnaces/client/screen/ColorUpgradeScreen;)Ljava/util/function/BiConsumer;"
- "(Ljava/util/function/BiConsumer;)Lwily/factoryapi/base/client/drawable/AbstractDrawableButton;"
- "(Lwily/betterfurnaces/network/SliderColorSyncPayload$Channel;Lwily/factoryapi/base/client/drawable/FactoryDrawableSlider;)Lnet/minecraft/network/chat/Component;"
- "(Lwily/factoryapi/base/client/drawable/FactoryDrawableSlider;)Lnet/minecraft/network/chat/Component;"
- "(IILjava/util/function/Function;Lwily/factoryapi/base/client/drawable/IFactoryDrawableType;Lwily/factoryapi/base/client/drawable/IFactoryDrawableType;IIII)V"
- "(F)Lwily/factoryapi/base/client/drawable/AbstractDrawableButton;"
- "(Lwily/betterfurnaces/network/SliderColorSyncPayload$Channel;Lwily/factoryapi/base/client/drawable/FactoryDrawableSlider;Ljava/lang/Integer;)V"
- "(Lwily/factoryapi/base/client/drawable/FactoryDrawableSlider;Ljava/lang/Integer;)V"
- "(Lwily/betterfurnaces/client/screen/ColorUpgradeScreen;Lwily/betterfurnaces/network/SliderColorSyncPayload$Channel;)Ljava/util/function/BiConsumer;"
- "(Lwily/factoryapi/base/client/drawable/FactoryDrawableSlider;Lwily/betterfurnaces/network/SliderColorSyncPayload$Channel;)V"
- "(Lwily/factoryapi/base/network/CommonNetwork$Payload;)V"
- "java/lang/invoke/StringConcatFactory"
- "()Lwily/factoryapi/base/client/drawable/AbstractDrawableStatic;"
- "Lwily/factoryapi/base/client/drawable/FactoryDrawableButton;"

### `wily/betterfurnaces/client/screen/FactoryUpgradeWindow.class`

- "wily/betterfurnaces/client/screen/FactoryUpgradeWindow"
- "Lwily/factoryapi/base/client/FactoryScreenWindow<Lwily/betterfurnaces/client/screen/SmeltingScreen<*>;>;"
- "wily/factoryapi/base/client/FactoryScreenWindow"
- "FactoryUpgradeWindow.java"
- "wily/factoryapi/base/client/drawable/IFactoryDrawableType$DrawableImage"
- "wily/factoryapi/base/client/drawable/IFactoryDrawableType"
- "wily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type"
- "wily/betterfurnaces/blockentity/FactoryUpgradeSettings"
- "wily/factoryapi/base/network/CommonNetwork$Payload"
- "wily/factoryapi/base/network/CommonNetwork"
- "(Lwily/factoryapi/base/client/drawable/AbstractDrawableButton;IILwily/betterfurnaces/client/screen/SmeltingScreen;)V"
- "(Lwily/factoryapi/base/client/drawable/AbstractDrawableButton<*>;IILwily/betterfurnaces/client/screen/SmeltingScreen<*>;)V"
- "FACTORY_UPGRADE_WINDOW"
- "Lwily/factoryapi/base/client/drawable/IFactoryDrawableType$DrawableImage;"
- "(II)Lwily/factoryapi/base/client/drawable/DrawableStatic;"
- "(Lwily/factoryapi/base/client/drawable/AbstractDrawableButton;Lwily/factoryapi/base/client/drawable/DrawableStatic;Lnet/minecraft/client/gui/screens/inventory/AbstractContainerScreen;)V"
- "Lwily/betterfurnaces/client/screen/FactoryUpgradeWindow;"
- "Lwily/factoryapi/base/client/drawable/AbstractDrawableButton<*>;"
- "Lwily/factoryapi/base/client/drawable/AbstractDrawableButton;"
- "storedFactoryUpgradeType"
- "wily/factoryapi/base/client/drawable/FactoryDrawableButton"
- "Lwily/factoryapi/base/client/drawable/IFactoryDrawableType;"
- "(IILwily/factoryapi/base/client/drawable/IFactoryDrawableType;)V"
- "(I)Lwily/factoryapi/base/client/drawable/IFactoryDrawableType;"
- "(Lwily/factoryapi/base/client/drawable/IFactoryDrawableType;)Lwily/factoryapi/base/client/drawable/AbstractDrawableButton;"
- "java/lang/invoke/StringConcatFactory"
- "(Ljava/util/List;)Lwily/factoryapi/base/client/drawable/AbstractDrawableStatic;"
- "(Ljava/lang/Boolean;)Lwily/factoryapi/base/client/drawable/AbstractDrawableButton;"
- "(Lwily/factoryapi/base/client/drawable/FactoryDrawableButton;Ljava/lang/Integer;)V"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "(Lwily/betterfurnaces/client/screen/FactoryUpgradeWindow;)Ljava/util/function/BiConsumer;"
- "(Ljava/util/function/BiConsumer;)Lwily/factoryapi/base/client/drawable/AbstractDrawableButton;"
- "wily/factoryapi/base/BlockSide"
- "Lwily/factoryapi/base/BlockSide;"
- "(IILwily/factoryapi/base/BlockSide;)Lwily/factoryapi/base/client/drawable/FactoryDrawableButton;"
- "wily/factoryapi/util/StorageStringUtil"
- "(Lnet/minecraft/network/chat/Component;)Lwily/factoryapi/base/client/drawable/AbstractDrawableStatic;"
- "(Ljava/awt/Color;)Lwily/factoryapi/base/client/drawable/AbstractDrawableButton;"
- "(ZLwily/factoryapi/base/client/drawable/FactoryDrawableButton;Ljava/lang/Integer;)V"
- "(Lwily/betterfurnaces/client/screen/FactoryUpgradeWindow;Z)Ljava/util/function/BiConsumer;"
- "fuel"
- "Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings;"
- "Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;"
- "(Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;I)I"
- "(Lwily/factoryapi/base/BlockSide;)I"
- "(IILwily/factoryapi/base/client/drawable/FactoryDrawableButton;Ljava/lang/Integer;)V"
- "(Lwily/betterfurnaces/client/screen/FactoryUpgradeWindow;II)Ljava/util/function/BiConsumer;"
- "wily/factoryapi/util/FactoryScreenUtil"
- "(Lnet/minecraft/core/BlockPos;Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;[II)V"
- "(Lwily/factoryapi/base/network/CommonNetwork$Payload;)V"
- "(Lnet/minecraft/core/BlockPos;Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;II)V"
- "Lwily/factoryapi/base/client/drawable/FactoryDrawableButton;"

### `wily/betterfurnaces/client/screen/ForgeScreen.class`

- "wily/factoryapi/base/client/drawable/IFactoryDrawableType$DrawableImage"
- "wily/factoryapi/base/client/drawable/IFactoryDrawableType"
- "wily/factoryapi/base/client/drawable/IFactoryDrawableType$DrawableProgress"
- "factoryShowButtonY"
- "()Lwily/factoryapi/base/client/drawable/DrawableStatic;"
- "Lwily/factoryapi/base/client/drawable/IFactoryDrawableType$DrawableImage;"
- "(II)Lwily/factoryapi/base/client/drawable/DrawableStatic;"
- "energyTankDraw"
- "()Lwily/factoryapi/base/client/drawable/DrawableStaticProgress;"
- "ENERGY_CELL"
- "Lwily/factoryapi/base/client/drawable/IFactoryDrawableType$DrawableProgress;"
- "(II)Lwily/factoryapi/base/client/drawable/DrawableStaticProgress;"
- "fuel"
- "wily/factoryapi/base/client/FactoryGuiGraphics"
- "(Lnet/minecraft/client/gui/GuiGraphics;)Lwily/factoryapi/base/client/FactoryGuiGraphics;"
- "getCookScaled"

### `wily/betterfurnaces/client/screen/FuelVerifierScreen.class`

- "wily/betterfurnaces/client/screen/FuelVerifierScreen"
- "Lwily/betterfurnaces/client/screen/AbstractBasicScreen<Lwily/betterfurnaces/inventory/FuelVerifierMenu;>;"
- "FuelVerifierScreen.java"
- "(Lwily/betterfurnaces/inventory/FuelVerifierMenu;Lnet/minecraft/world/entity/player/Inventory;Lnet/minecraft/network/chat/Component;)V"
- "Lwily/betterfurnaces/client/screen/FuelVerifierScreen;"
- "Lwily/betterfurnaces/inventory/FuelVerifierMenu;"
- "gui.betterfurnacesreforged.fuel.melts"
- "wily/betterfurnaces/inventory/FuelVerifierMenu"
- "gui.betterfurnacesreforged.fuel.items"
- "wily/factoryapi/base/client/FactoryGuiGraphics"
- "(Lnet/minecraft/client/gui/GuiGraphics;)Lwily/factoryapi/base/client/FactoryGuiGraphics;"
- "textures/container/fuel_verifier_gui.png"

### `wily/betterfurnaces/client/screen/SmeltingScreen.class`

- "wily/factoryapi/base/client/drawable/IFactoryDrawableType$DrawableImage"
- "wily/factoryapi/base/client/drawable/IFactoryDrawableType"
- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "wily/betterfurnaces/items/UpgradeItem$Type"
- "wily/betterfurnaces/items/UpgradeItem"
- "wily/factoryapi/base/client/drawable/IFactoryDrawableType$DrawableProgress"
- "wily/factoryapi/base/client/drawable/IFactoryDrawableType$Direction"
- "wily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type"
- "wily/betterfurnaces/blockentity/FactoryUpgradeSettings"
- "wily/factoryapi/base/network/CommonNetwork$Payload"
- "wily/factoryapi/base/network/CommonNetwork"
- "Lwily/factoryapi/base/client/drawable/FactoryDrawableButton;"
- "factoryShowButtonY"
- "()Lwily/factoryapi/base/client/drawable/DrawableStatic;"
- "Lwily/factoryapi/base/client/drawable/IFactoryDrawableType$DrawableImage;"
- "(II)Lwily/factoryapi/base/client/drawable/DrawableStatic;"
- "energyTankDraw"
- "()Lwily/factoryapi/base/client/drawable/DrawableStaticProgress;"
- "GENERATOR"
- "Lwily/factoryapi/base/RegisterListing$Holder;"
- "hasUpgrade"
- "(Lwily/betterfurnaces/items/UpgradeItem;)Z"
- "Lwily/betterfurnaces/items/UpgradeItem$Type;"
- "hasUpgradeType"
- "(Lwily/betterfurnaces/items/UpgradeItem$Type;)Z"
- "THIN_ENERGY_CELL"
- "Lwily/factoryapi/base/client/drawable/IFactoryDrawableType$DrawableProgress;"
- "ENERGY_CELL"
- "(II)Lwily/factoryapi/base/client/drawable/DrawableStaticProgress;"
- "generatorTankDraw"
- "storedFactoryUpgradeType"
- "FACTORY"
- "getUpgradeTypeStack"
- "(Lwily/betterfurnaces/items/UpgradeItem$Type;)Lnet/minecraft/world/item/ItemStack;"
- "wily/betterfurnaces/items/FactoryUpgradeItem"
- "Lwily/betterfurnaces/items/FactoryUpgradeItem;"
- "wily/factoryapi/base/client/drawable/FactoryDrawableButton"
- "FACTORY_BUTTON"
- "Lwily/factoryapi/base/client/drawable/IFactoryDrawableType;"
- "(IILwily/factoryapi/base/client/drawable/IFactoryDrawableType;)V"
- "Lwily/factoryapi/base/client/drawable/IFactoryDrawableType$Direction;"
- "(Lwily/factoryapi/base/client/drawable/IFactoryDrawableType$Direction;)Lwily/factoryapi/base/client/drawable/AbstractDrawableButton;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "(Ljava/util/function/Supplier;)Lwily/factoryapi/base/client/drawable/AbstractDrawableStatic;"
- "(Lwily/factoryapi/base/client/drawable/FactoryDrawableButton;Ljava/lang/Integer;)V"
- "(Ljava/util/function/BiConsumer;)Lwily/factoryapi/base/client/drawable/AbstractDrawableButton;"
- "wily/betterfurnaces/client/screen/FactoryUpgradeWindow"
- "(Lwily/factoryapi/base/client/drawable/AbstractDrawableButton;IILwily/betterfurnaces/client/screen/SmeltingScreen;)V"
- "(Ljava/lang/Boolean;)Lwily/factoryapi/base/client/drawable/AbstractDrawableButton;"
- "(Ljava/util/List;)Lwily/factoryapi/base/client/drawable/AbstractDrawableStatic;"
- "(Lnet/minecraft/network/chat/Component;)Lwily/factoryapi/base/client/drawable/AbstractDrawableStatic;"
- "()Lwily/factoryapi/base/client/drawable/AbstractDrawableStatic;"
- "wily/factoryapi/base/client/drawable/DrawableStatic"
- "tooltip.factory_api.fluid_stored"
- "getFuelTank"
- "()Lwily/factoryapi/base/FactoryItemFluidHandler;"
- "(Ljava/lang/String;Lwily/factoryapi/base/IPlatformFluidHandler;)Lnet/minecraft/network/chat/MutableComponent;"
- "getUpgradeSlotItem"
- "wily/factoryapi/FactoryAPIPlatform"
- "(Lnet/minecraft/world/item/ItemStack;)Lwily/factoryapi/base/IPlatformFluidHandler;"
- "ENERGY"
- "wily/factoryapi/base/client/drawable/DrawableStaticProgress"
- "tooltip.factory_api.energy_stored"
- "energyStorage"
- "Lwily/factoryapi/base/IPlatformEnergyStorage;"
- "wily/factoryapi/util/StorageStringUtil"
- "getEnergyTooltip"
- "(Ljava/lang/String;Lwily/factoryapi/base/IPlatformEnergyStorage;)Lnet/minecraft/network/chat/MutableComponent;"
- "wily/factoryapi/base/IPlatformFluidHandler"
- "()Lwily/factoryapi/util/FluidInstance;"
- "(Ljava/lang/String;Lwily/factoryapi/util/FluidInstance;JZ)Lnet/minecraft/network/chat/MutableComponent;"
- "Lwily/factoryapi/base/IPlatformFluidHandler;"
- "wily/factoryapi/base/client/FactoryGuiGraphics"
- "(Lnet/minecraft/client/gui/GuiGraphics;)Lwily/factoryapi/base/client/FactoryGuiGraphics;"
- "getCookScaled"
- "getEnergyStored"
- "getMaxEnergyStored"
- "wily/factoryapi/base/FactoryItemFluidHandler"
- "(Lnet/minecraft/client/gui/GuiGraphics;Lwily/factoryapi/util/FluidInstance;IZ)V"
- "getGeneratorTank"
- "Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings;"
- "Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;"
- "(Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;)[I"
- "fuel"
- "FUEL_SLOT_OUTLINE"
- "(Lwily/factoryapi/base/network/CommonNetwork$Payload;)V"

### `wily/betterfurnaces/compat/BFRRecipeTypes.class`

- "Lmezz/jei/api/recipe/RecipeType<Lwily/betterfurnaces/recipes/CobblestoneGeneratorRecipe;>;"
- "wily/betterfurnaces/recipes/CobblestoneGeneratorRecipe"

### `wily/betterfurnaces/compat/BfJeiPlugin$1.class`

- "wily/factoryapi/base/client/IWindowWidget"
- "Lwily/factoryapi/base/client/IWindowWidget;"

### `wily/betterfurnaces/compat/BfJeiPlugin$CobblestoneGeneratorCategory.class`

- "wily/betterfurnaces/compat/BfJeiPlugin$CobblestoneGeneratorCategory"
- "Ljava/lang/Object;Lmezz/jei/api/recipe/category/IRecipeCategory<Lwily/betterfurnaces/recipes/CobblestoneGeneratorRecipe;>;"
- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "CobblestoneGeneratorCategory"
- "COBBLESTONE_GENERATOR"
- "Lwily/factoryapi/base/RegisterListing$Holder;"
- "wily/betterfurnaces/blocks/CobblestoneGeneratorBlock"
- "wily/betterfurnaces/client/screen/CobblestoneGeneratorScreen"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "Lwily/betterfurnaces/compat/BfJeiPlugin$CobblestoneGeneratorCategory;"
- "(Lwily/betterfurnaces/recipes/CobblestoneGeneratorRecipe;Lmezz/jei/api/gui/ingredient/IRecipeSlotsView;Lnet/minecraft/client/gui/GuiGraphics;DD)V"
- "wily/betterfurnaces/recipes/CobblestoneGeneratorRecipe"
- "java/lang/invoke/StringConcatFactory"
- "wily/factoryapi/util/FactoryScreenUtil"
- "Lwily/factoryapi/util/FluidInstance;"
- "(Lnet/minecraft/client/gui/GuiGraphics;IIIILwily/factoryapi/util/FluidInstance;Z)V"
- "Lwily/betterfurnaces/recipes/CobblestoneGeneratorRecipe;"
- "()Lmezz/jei/api/recipe/RecipeType<Lwily/betterfurnaces/recipes/CobblestoneGeneratorRecipe;>;"
- "(Lmezz/jei/api/gui/builder/IRecipeLayoutBuilder;Lwily/betterfurnaces/recipes/CobblestoneGeneratorRecipe;Lmezz/jei/api/recipe/IFocusGroup;)V"
- "cookTime"

### `wily/betterfurnaces/compat/BfJeiPlugin.class`

- "wily/betterfurnaces/compat/BfJeiPlugin$CobblestoneGeneratorCategory"
- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "CobblestoneGeneratorCategory"
- "Lwily/factoryapi/base/config/FactoryConfig;"
- "wily/factoryapi/base/config/FactoryConfig"
- "COBBLESTONE_GENERATOR"
- "Lwily/factoryapi/base/RegisterListing$Holder;"
- "(Lmezz/jei/api/registration/IRecipeCatalystRegistration;Lwily/factoryapi/base/RegisterListing$Holder;)V"
- "(Lwily/factoryapi/base/RegisterListing$Holder;)V"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "(Lmezz/jei/api/registration/IRecipeRegistration;Lwily/factoryapi/base/RegisterListing$Holder;)V"
- "FUELING"
- "wily/betterfurnaces/client/screen/CobblestoneGeneratorScreen"
- "wily/betterfurnaces/items/TierUpgradeItem"
- "tooltip.betterfurnacesreforged.upgrade.tier"
- "Lwily/betterfurnaces/items/TierUpgradeItem;"

### `wily/betterfurnaces/compat/ProjectMMOCompat.class`

- "wily/factoryapi/FactoryAPIPlatform"

### `wily/betterfurnaces/gitup/UpThreadCheck.class`

- "java/lang/invoke/StringConcatFactory"

### `wily/betterfurnaces/init/BlockEntityTypes.class`

- "wily/factoryapi/FactoryAPIPlatform$BlockEntitySupplier"
- "wily/factoryapi/FactoryAPIPlatform"
- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "Lwily/factoryapi/base/RegisterListing$Holder;"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lnet/minecraft/world/level/block/entity/BlockEntityType<Lwily/betterfurnaces/blockentity/SmeltingBlockEntity;>;>;"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lnet/minecraft/world/level/block/entity/BlockEntityType<Lwily/betterfurnaces/blockentity/ForgeBlockEntity;>;>;"
- "FUEL_VERIFIER_TILE"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lnet/minecraft/world/level/block/entity/BlockEntityType<Lwily/betterfurnaces/blockentity/FuelVerifierBlockEntity;>;>;"
- "COB_GENERATOR_TILE"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lnet/minecraft/world/level/block/entity/BlockEntityType<Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity;>;>;"
- "wily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity"
- "(Lnet/minecraft/core/BlockPos;Lnet/minecraft/world/level/block/state/BlockState;)Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "()Lwily/factoryapi/FactoryAPIPlatform$BlockEntitySupplier;"
- "COBBLESTONE_GENERATOR"
- "(Lwily/factoryapi/FactoryAPIPlatform$BlockEntitySupplier;[Lnet/minecraft/world/level/block/Block;)Lnet/minecraft/world/level/block/entity/BlockEntityType;"
- "wily/betterfurnaces/blockentity/FuelVerifierBlockEntity"
- "(Lnet/minecraft/core/BlockPos;Lnet/minecraft/world/level/block/state/BlockState;)Lwily/betterfurnaces/blockentity/FuelVerifierBlockEntity;"
- "FUEL_VERIFIER"
- "(Lwily/factoryapi/base/RegisterListing$Holder;)Lnet/minecraft/world/level/block/Block;"
- "Lwily/factoryapi/base/RegisterListing;"
- "(Ljava/lang/String;Ljava/util/function/Supplier;)Lwily/factoryapi/base/RegisterListing$Holder;"
- "fuel_verifier"
- "cobblestone_generator"

### `wily/betterfurnaces/init/ModObjects$1.class`

- "Ljava/lang/Object;Lnet/minecraft/world/item/crafting/RecipeType<Lwily/betterfurnaces/recipes/CobblestoneGeneratorRecipe;>;"

### `wily/betterfurnaces/init/ModObjects$2.class`

- "wily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type"
- "wily/betterfurnaces/blockentity/FactoryUpgradeSettings"
- "$SwitchMap$wily$betterfurnaces$blockentity$FactoryUpgradeSettings$Type"
- "()[Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;"
- "Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;"

### `wily/betterfurnaces/init/ModObjects$BlockTint.class`

- "wily/factoryapi/util/ColorUtil"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `wily/betterfurnaces/init/ModObjects$UpgradeSetting.class`

- "wily/betterfurnaces/init/ModObjects$UpgradeSetting"
- "UpgradeSetting"
- "Lwily/betterfurnaces/init/ModObjects$UpgradeSetting;"
- "(Lwily/betterfurnaces/init/ModObjects$UpgradeSetting;)Ljava/lang/String;"
- "(Lwily/betterfurnaces/init/ModObjects$UpgradeSetting;)I"
- "(Lwily/betterfurnaces/init/ModObjects$UpgradeSetting;Ljava/lang/Object;)Z"

### `wily/betterfurnaces/init/ModObjects.class`

- "wily/betterfurnaces/init/ModObjects$UpgradeSetting"
- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "wily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type"
- "wily/betterfurnaces/blockentity/FactoryUpgradeSettings"
- "UpgradeSetting"
- "wily/betterfurnaces/items/UpgradeItem$Type"
- "wily/betterfurnaces/items/UpgradeItem"
- "wily/factoryapi/base/network/CommonNetwork$PlayBuf"
- "wily/factoryapi/base/network/CommonNetwork"
- "wily/betterfurnaces/blocks/SmeltingBlock$Tier"
- "Tier"
- "wily/betterfurnaces/recipes/CobblestoneGeneratorRecipe$Serializer"
- "wily/betterfurnaces/recipes/CobblestoneGeneratorRecipe"
- "net/minecraft/world/item/CreativeModeTab$DisplayItemsGenerator"
- "DisplayItemsGenerator"
- "wily/betterfurnaces/items/ColorUpgradeItem$ColorUpgradeMenu"
- "wily/betterfurnaces/items/ColorUpgradeItem"
- "ColorUpgradeMenu"
- "Lwily/factoryapi/base/RegisterListing;"
- "Lwily/factoryapi/base/RegisterListing<Lnet/minecraft/world/level/block/Block;>;"
- "Lwily/factoryapi/base/RegisterListing<Lnet/minecraft/world/item/Item;>;"
- "Lwily/factoryapi/base/RegisterListing$Holder;"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lnet/minecraft/world/item/CreativeModeTab;>;"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lnet/minecraft/world/item/crafting/RecipeSerializer<Lwily/betterfurnaces/recipes/CobblestoneGeneratorRecipe;>;>;"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lnet/minecraft/world/item/crafting/RecipeType<Lwily/betterfurnaces/recipes/CobblestoneGeneratorRecipe;>;>;"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lnet/minecraft/world/inventory/MenuType<Lwily/betterfurnaces/inventory/SmeltingMenu;>;>;"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lnet/minecraft/world/inventory/MenuType<Lwily/betterfurnaces/inventory/ForgeMenu;>;>;"
- "COLOR_UPGRADE_CONTAINER"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lnet/minecraft/world/inventory/MenuType<Lwily/betterfurnaces/items/ColorUpgradeItem$ColorUpgradeMenu;>;>;"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lwily/betterfurnaces/blocks/SmeltingBlock;>;"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lwily/betterfurnaces/blocks/ForgeBlock;>;"
- "COBBLESTONE_GENERATOR"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lwily/betterfurnaces/blocks/CobblestoneGeneratorBlock;>;"
- "COB_GENERATOR_CONTAINER"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lnet/minecraft/world/inventory/MenuType<Lwily/betterfurnaces/inventory/CobblestoneGeneratorMenu;>;>;"
- "FUEL_VERIFIER"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lwily/betterfurnaces/blocks/FuelVerifierBlock;>;"
- "FUEL_VERIFIER_CONTAINER"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lnet/minecraft/world/inventory/MenuType<Lwily/betterfurnaces/inventory/FuelVerifierMenu;>;>;"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lwily/betterfurnaces/blocks/BFRBlock;>;"
- "IRON_UPGRADE"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lwily/betterfurnaces/items/TierUpgradeItem;>;"
- "GOLD_UPGRADE"
- "DIAMOND_UPGRADE"
- "NETHERHOT_UPGRADE"
- "EXTREME_UPGRADE"
- "FUEL"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lwily/betterfurnaces/items/FuelEfficiencyUpgradeItem;>;"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lwily/betterfurnaces/items/OreProcessingUpgradeItem;>;"
- "ADVANCED_FUEL"
- "FACTORY"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lwily/betterfurnaces/items/FactoryUpgradeItem;>;"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lwily/betterfurnaces/items/ColorUpgradeItem;>;"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lwily/betterfurnaces/items/LiquidFuelUpgradeItem;>;"
- "ENERGY"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lwily/betterfurnaces/items/EnergyFuelUpgradeItem;>;"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lwily/betterfurnaces/items/XpTankUpgradeItem;>;"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lwily/betterfurnaces/items/UpgradeItem;>;"
- "GENERATOR"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lwily/betterfurnaces/items/GeneratorUpgradeItem;>;"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lwily/betterfurnaces/items/StorageUpgradeItem;>;"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lnet/minecraft/core/component/DataComponentType<Lwily/betterfurnaces/init/ModObjects$BlockTint;>;>;"
- "Lwily/factoryapi/base/RegisterListing$Holder<Lnet/minecraft/core/component/DataComponentType<Lwily/betterfurnaces/init/ModObjects$UpgradeSetting;>;>;"
- "wily/factoryapi/FactoryAPIPlatform"
- "registerFactoryUpgradeSetting"
- "(Ljava/lang/String;)Lwily/factoryapi/base/RegisterListing$Holder;"
- "(Ljava/lang/String;)Lwily/factoryapi/base/RegisterListing$Holder<Lnet/minecraft/core/component/DataComponentType<Lwily/betterfurnaces/init/ModObjects$UpgradeSetting;>;>;"
- "lambda$registerFactoryUpgradeSetting$54"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "(Ljava/lang/String;Ljava/util/function/Supplier;)Lwily/factoryapi/base/RegisterListing$Holder;"
- "(Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;)Lwily/factoryapi/base/RegisterListing$Holder;"
- "(Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;)Lwily/factoryapi/base/RegisterListing$Holder<Lnet/minecraft/core/component/DataComponentType<Lwily/betterfurnaces/init/ModObjects$UpgradeSetting;>;>;"
- "$SwitchMap$wily$betterfurnaces$blockentity$FactoryUpgradeSettings$Type"
- "Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings$Type;"
- "lambda$registerFactoryUpgradeSetting$50"
- "(Ljava/util/stream/IntStream;)Lwily/betterfurnaces/init/ModObjects$UpgradeSetting;"
- "lambda$registerFactoryUpgradeSetting$51"
- "(Lwily/betterfurnaces/init/ModObjects$UpgradeSetting;)Ljava/util/stream/IntStream;"
- "lambda$registerFactoryUpgradeSetting$52"
- "(Lnet/minecraft/network/RegistryFriendlyByteBuf;Lwily/betterfurnaces/init/ModObjects$UpgradeSetting;)V"
- "lambda$registerFactoryUpgradeSetting$53"
- "(Lnet/minecraft/network/RegistryFriendlyByteBuf;)Lwily/betterfurnaces/init/ModObjects$UpgradeSetting;"
- "Lwily/betterfurnaces/init/ModObjects$UpgradeSetting;"
- "(Lnet/minecraft/resources/ResourceLocation;)Lwily/betterfurnaces/items/StorageUpgradeItem;"
- "wily/betterfurnaces/items/StorageUpgradeItem"
- "(Lnet/minecraft/resources/ResourceLocation;)Lwily/betterfurnaces/items/GeneratorUpgradeItem;"
- "wily/betterfurnaces/items/GeneratorUpgradeItem"
- "(Lnet/minecraft/resources/ResourceLocation;)Lwily/betterfurnaces/items/UpgradeItem;"
- "Lwily/betterfurnaces/items/UpgradeItem$Type;"
- "(Lnet/minecraft/world/item/Item$Properties;Lwily/betterfurnaces/items/UpgradeItem$Type;Ljava/lang/String;)V"
- "(Lnet/minecraft/resources/ResourceLocation;)Lwily/betterfurnaces/items/XpTankUpgradeItem;"
- "wily/betterfurnaces/items/XpTankUpgradeItem"
- "(Lnet/minecraft/resources/ResourceLocation;)Lwily/betterfurnaces/items/EnergyFuelUpgradeItem;"
- "wily/betterfurnaces/items/EnergyFuelUpgradeItem"
- "tooltip.betterfurnacesreforged.upgrade.energy"
- "getPlatformEnergyComponent"
- "(Lnet/minecraft/resources/ResourceLocation;)Lwily/betterfurnaces/items/LiquidFuelUpgradeItem;"
- "wily/betterfurnaces/items/LiquidFuelUpgradeItem"
- "(Lnet/minecraft/resources/ResourceLocation;)Lwily/betterfurnaces/items/ColorUpgradeItem;"
- "(Lnet/minecraft/resources/ResourceLocation;)Lwily/betterfurnaces/items/FactoryUpgradeItem;"
- "wily/betterfurnaces/items/FactoryUpgradeItem"
- "factory"
- "(Lnet/minecraft/resources/ResourceLocation;)Lwily/betterfurnaces/items/OreProcessingUpgradeItem;"
- "wily/betterfurnaces/items/OreProcessingUpgradeItem"
- "(Lnet/minecraft/resources/ResourceLocation;)Lwily/betterfurnaces/items/FuelEfficiencyUpgradeItem;"
- "wily/betterfurnaces/items/FuelEfficiencyUpgradeItem"
- "(Lnet/minecraft/resources/ResourceLocation;)Lwily/betterfurnaces/items/TierUpgradeItem;"
- "wily/betterfurnaces/items/TierUpgradeItem"
- "(Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;Lwily/factoryapi/base/RegisterListing$Holder;)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;"
- "(ILnet/minecraft/world/entity/player/Inventory;Lwily/factoryapi/base/network/CommonNetwork$PlayBuf;)Lnet/minecraft/world/inventory/AbstractContainerMenu;"
- "(ILnet/minecraft/world/entity/player/Inventory;Lwily/factoryapi/base/network/CommonNetwork$PlayBuf;)Lwily/betterfurnaces/inventory/FuelVerifierMenu;"
- "()Lwily/factoryapi/base/FactoryExtraMenuSupplier;"
- "wily/factoryapi/base/FactoryExtraMenuSupplier"
- "(Lwily/factoryapi/base/FactoryExtraMenuSupplier;)Lnet/minecraft/world/inventory/MenuType;"
- "wily/betterfurnaces/inventory/FuelVerifierMenu"
- "Lwily/factoryapi/base/network/CommonNetwork$PlayBuf;"
- "()Lwily/betterfurnaces/blocks/FuelVerifierBlock;"
- "wily/betterfurnaces/blocks/FuelVerifierBlock"
- "(ILnet/minecraft/world/entity/player/Inventory;Lwily/factoryapi/base/network/CommonNetwork$PlayBuf;)Lwily/betterfurnaces/inventory/CobblestoneGeneratorMenu;"
- "wily/betterfurnaces/inventory/CobblestoneGeneratorMenu"
- "()Lwily/betterfurnaces/blocks/CobblestoneGeneratorBlock;"
- "wily/betterfurnaces/blocks/CobblestoneGeneratorBlock"
- "extremeTierSpeed"
- "Lwily/factoryapi/base/config/FactoryConfig;"
- "(Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;Lwily/betterfurnaces/blocks/SmeltingBlock$Tier;)V"
- "netherhotTierSpeed"
- "diamondTierSpeed"
- "goldTierSpeed"
- "ironTierSpeed"
- "(ILnet/minecraft/world/entity/player/Inventory;)Lwily/betterfurnaces/items/ColorUpgradeItem$ColorUpgradeMenu;"
- "(ILnet/minecraft/world/entity/player/Inventory;Lwily/factoryapi/base/network/CommonNetwork$PlayBuf;)Lwily/betterfurnaces/inventory/ForgeMenu;"
- "(ILnet/minecraft/world/entity/player/Inventory;Lwily/factoryapi/base/network/CommonNetwork$PlayBuf;)Lwily/betterfurnaces/inventory/SmeltingMenu;"
- "Lwily/betterfurnaces/recipes/CobblestoneGeneratorRecipe$Serializer;"
- "()Lnet/minecraft/world/item/CreativeModeTab$DisplayItemsGenerator;"
- "(Lnet/minecraft/world/item/CreativeModeTab$DisplayItemsGenerator;)Lnet/minecraft/world/item/CreativeModeTab$Builder;"
- "(Lnet/minecraft/world/item/CreativeModeTab$Output;Lwily/factoryapi/base/RegisterListing$Holder;)V"
- "(Lwily/factoryapi/base/RegisterListing$Holder;)V"
- "(Ljava/lang/String;Lnet/minecraft/core/Registry;)Lwily/factoryapi/base/RegisterListing;"
- "color_upgrade"
- "(Ljava/lang/String;Ljava/util/function/Function;)Lwily/factoryapi/base/RegisterListing$Holder;"
- "(Lwily/factoryapi/base/RegisterListing$Holder;Lwily/factoryapi/base/RegisterListing;)Lwily/factoryapi/base/RegisterListing$Holder;"
- "cobblestone_generator"
- "fuel_verifier"
- "iron_upgrade"
- "gold_upgrade"
- "diamond_upgrade"
- "netherhot_upgrade"
- "extreme_upgrade"
- "fuel_efficiency_upgrade"
- "ore_processing_upgrade"
- "raw_ore_processing_upgrade"
- "advanced_fuel_efficiency_upgrade"
- "advanced_ore_processing_upgrade"
- "factory_upgrade"
- "piping_upgrade"
- "autooutput_upgrade"
- "autoinput_upgrade"
- "redstone_signal_upgrade"
- "liquid_fuel_upgrade"
- "energy_upgrade"
- "xp_tank_upgrade"
- "blasting_upgrade"
- "smoking_upgrade"
- "generator_upgrade"
- "storage_upgrade"
- "upgrade_color"

### `wily/betterfurnaces/init/Registration$1.class`

- "(Lwily/factoryapi/base/RegisterListing$Holder;Lwily/factoryapi/base/RegisterListing;)Lwily/factoryapi/base/RegisterListing$Holder;"
- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `wily/betterfurnaces/init/Registration.class`

- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "Lwily/factoryapi/base/RegisterListing;"
- "Lwily/factoryapi/base/RegisterListing<Lnet/minecraft/world/level/block/entity/BlockEntityType<*>;>;"
- "Lwily/factoryapi/base/RegisterListing<Lnet/minecraft/world/inventory/MenuType<*>;>;"
- "Lwily/factoryapi/base/RegisterListing<Lnet/minecraft/world/item/crafting/RecipeSerializer<*>;>;"
- "Lwily/factoryapi/base/RegisterListing<Lnet/minecraft/world/item/crafting/RecipeType<*>;>;"
- "Lwily/factoryapi/base/RegisterListing<Lnet/minecraft/core/component/DataComponentType<*>;>;"
- "Lwily/factoryapi/base/RegisterListing<Lnet/minecraft/world/item/CreativeModeTab;>;"
- "(Lwily/factoryapi/base/RegisterListing$Holder;Lwily/factoryapi/base/RegisterListing;)Lwily/factoryapi/base/RegisterListing$Holder;"
- "<T:Lnet/minecraft/world/level/block/Block;>(Lwily/factoryapi/base/RegisterListing$Holder<TT;>;Lwily/factoryapi/base/RegisterListing<Lnet/minecraft/world/item/Item;>;)Lwily/factoryapi/base/RegisterListing$Holder<TT;>;"
- "(Lwily/factoryapi/base/RegisterListing$Holder;)Lwily/betterfurnaces/init/Registration$1;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "(Lwily/factoryapi/base/RegisterListing$Holder;)Ljava/util/function/Supplier;"
- "(Ljava/lang/String;Ljava/util/function/Supplier;)Lwily/factoryapi/base/RegisterListing$Holder;"
- "Lwily/factoryapi/base/RegisterListing$Holder<TT;>;"
- "Lwily/factoryapi/base/RegisterListing$Holder;"
- "Lwily/factoryapi/base/RegisterListing<Lnet/minecraft/world/item/Item;>;"
- "()Ljava/util/stream/Stream<Lwily/factoryapi/base/RegisterListing$Holder<Lnet/minecraft/world/level/block/Block;>;>;"
- "()Ljava/util/stream/Stream<Lwily/factoryapi/base/RegisterListing$Holder<+Lnet/minecraft/world/level/block/Block;>;>;"
- "()Ljava/util/stream/Stream<Lwily/factoryapi/base/RegisterListing$Holder<Lnet/minecraft/world/item/Item;>;>;"
- "wily/factoryapi/FactoryAPIPlatform"
- "(Lnet/minecraft/world/item/Item$Properties;Lwily/factoryapi/base/RegisterListing$Holder;)Lnet/minecraft/world/item/Item$Properties;"
- "(Ljava/lang/String;Lnet/minecraft/core/Registry;)Lwily/factoryapi/base/RegisterListing;"

### `wily/betterfurnaces/inventory/AbstractInventoryMenu.class`

- "Lwily/factoryapi/base/FactoryItemHandler;"
- "(Lwily/factoryapi/base/FactoryItemSlot;)V"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "wily/factoryapi/util/FactoryItemUtil"
- "wily/factoryapi/base/FactoryItemHandler"

### `wily/betterfurnaces/inventory/AbstractUpgradeMenu.class`

- "wily/betterfurnaces/inventory/AbstractUpgradeMenu"
- "AbstractUpgradeMenu.java"
- "Lwily/betterfurnaces/inventory/AbstractUpgradeMenu;"

### `wily/betterfurnaces/inventory/CobblestoneGeneratorMenu.class`

- "wily/betterfurnaces/inventory/CobblestoneGeneratorMenu"
- "Lwily/betterfurnaces/inventory/AbstractInventoryMenu<Lwily/betterfurnaces/blockentity/CobblestoneGeneratorBlockEntity;>;"
- "CobblestoneGeneratorMenu.java"
- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "Lwily/betterfurnaces/inventory/CobblestoneGeneratorMenu;"
- "COB_GENERATOR_CONTAINER"
- "Lwily/factoryapi/base/RegisterListing$Holder;"

### `wily/betterfurnaces/inventory/ForgeMenu.class`

- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "Lwily/factoryapi/base/RegisterListing$Holder;"

### `wily/betterfurnaces/inventory/FuelVerifierMenu.class`

- "wily/betterfurnaces/inventory/FuelVerifierMenu"
- "Lwily/betterfurnaces/inventory/AbstractInventoryMenu<Lwily/betterfurnaces/blockentity/FuelVerifierBlockEntity;>;"
- "FuelVerifierMenu.java"
- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "maxFuelValue"
- "Lwily/betterfurnaces/inventory/FuelVerifierMenu;"
- "FUEL_VERIFIER_CONTAINER"
- "Lwily/factoryapi/base/RegisterListing$Holder;"
- "wily/factoryapi/base/FuelManager"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `wily/betterfurnaces/inventory/HideableSlot.class`

- "wily/factoryapi/base/FactoryItemSlot"
- "(Lwily/factoryapi/base/FactoryItemSlot;)Z"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "(Lwily/betterfurnaces/blockentity/InventoryBlockEntity;IIILjava/util/function/Predicate<Lwily/factoryapi/base/FactoryItemSlot;>;)V"
- "Lwily/factoryapi/base/FactoryItemHandler;"
- "wily/factoryapi/base/SlotsIdentifier"
- "Lwily/factoryapi/base/SlotsIdentifier;"
- "wily/factoryapi/base/TransportState"
- "Lwily/factoryapi/base/TransportState;"
- "(Lnet/minecraft/world/Container;Lwily/factoryapi/base/SlotsIdentifier;Lwily/factoryapi/base/TransportState;III)V"
- "Ljava/util/function/Predicate<Lwily/factoryapi/base/FactoryItemSlot;>;"
- "Lwily/factoryapi/base/FactoryItemSlot;"

### `wily/betterfurnaces/inventory/SlotFuel.class`

- "wily/betterfurnaces/inventory/SlotFuel"
- "SlotFuel.java"
- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "Lwily/betterfurnaces/inventory/SlotFuel;"
- "(Lwily/betterfurnaces/blockentity/InventoryBlockEntity;IIILjava/util/function/Predicate<Lwily/factoryapi/base/FactoryItemSlot;>;)V"
- "Ljava/util/function/Predicate<Lwily/factoryapi/base/FactoryItemSlot;>;"
- "wily/betterfurnaces/items/UpgradeItem"
- "wily/factoryapi/base/FuelManager"
- "isFuel"
- "wily/factoryapi/ItemContainerPlatform"
- "isEnergyContainer"
- "ENERGY"
- "Lwily/factoryapi/base/RegisterListing$Holder;"
- "hasUpgrade"
- "(Lwily/betterfurnaces/items/UpgradeItem;)Z"
- "wily/betterfurnaces/items/LiquidFuelUpgradeItem"

### `wily/betterfurnaces/inventory/SlotHeater.class`

- "wily/factoryapi/base/FactoryItemSlot"
- "wily/betterfurnaces/items/UpgradeItem$Type"
- "wily/betterfurnaces/items/UpgradeItem"
- "Lwily/factoryapi/base/FactoryItemHandler;"
- "wily/factoryapi/base/SlotsIdentifier"
- "Lwily/factoryapi/base/SlotsIdentifier;"
- "wily/factoryapi/base/TransportState"
- "Lwily/factoryapi/base/TransportState;"
- "(Lnet/minecraft/world/Container;Lwily/factoryapi/base/SlotsIdentifier;Lwily/factoryapi/base/TransportState;III)V"
- "upgradeType"
- "Lwily/betterfurnaces/items/UpgradeItem$Type;"
- "ALTERNATIVE_FUEL"

### `wily/betterfurnaces/inventory/SlotInput.class`

- "(Lwily/betterfurnaces/blockentity/SmeltingBlockEntity;IIILjava/util/function/Predicate<Lwily/factoryapi/base/FactoryItemSlot;>;)V"
- "Ljava/util/function/Predicate<Lwily/factoryapi/base/FactoryItemSlot;>;"

### `wily/betterfurnaces/inventory/SlotOutput.class`

- "(Lwily/factoryapi/base/FactoryItemSlot;)Z"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "(Lnet/minecraft/world/entity/player/Player;Lwily/betterfurnaces/blockentity/InventoryBlockEntity;IIILjava/util/function/Predicate<Lwily/factoryapi/base/FactoryItemSlot;>;)V"
- "Ljava/util/function/Predicate<Lwily/factoryapi/base/FactoryItemSlot;>;"
- "Lwily/factoryapi/base/FactoryItemSlot;"

### `wily/betterfurnaces/inventory/SlotUpgrade.class`

- "wily/betterfurnaces/inventory/SlotUpgrade"
- "wily/factoryapi/base/FactoryItemSlot"
- "SlotUpgrade.java"
- "wily/betterfurnaces/items/UpgradeItem$Type"
- "wily/betterfurnaces/items/UpgradeItem"
- "Lwily/factoryapi/base/FactoryItemHandler;"
- "wily/factoryapi/base/SlotsIdentifier"
- "Lwily/factoryapi/base/SlotsIdentifier;"
- "wily/factoryapi/base/TransportState"
- "Lwily/factoryapi/base/TransportState;"
- "(Lnet/minecraft/world/Container;Lwily/factoryapi/base/SlotsIdentifier;Lwily/factoryapi/base/TransportState;III)V"
- "Lwily/betterfurnaces/inventory/SlotUpgrade;"
- "hasUpgrade"
- "(Lwily/betterfurnaces/items/UpgradeItem;)Z"
- "upgradeType"
- "Lwily/betterfurnaces/items/UpgradeItem$Type;"
- "ALTERNATIVE_FUEL"
- "hasUpgradeFromSameType"
- "wily/factoryapi/base/FactoryItemHandler"
- "Lwily/betterfurnaces/items/UpgradeItem;"

### `wily/betterfurnaces/inventory/SmeltingMenu$1.class`

- "energyStorage"
- "Lwily/factoryapi/base/IPlatformEnergyStorage;"
- "wily/factoryapi/base/IPlatformEnergyStorage"
- "setEnergyStored"

### `wily/betterfurnaces/inventory/SmeltingMenu.class`

- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "Lwily/factoryapi/base/RegisterListing$Holder;"
- "getCookScaled"
- "getEnergyStored"
- "getMaxEnergyStored"

### `wily/betterfurnaces/items/ColorUpgradeItem$ColorUpgradeMenu.class`

- "wily/betterfurnaces/items/ColorUpgradeItem$ColorUpgradeMenu"
- "wily/betterfurnaces/inventory/AbstractUpgradeMenu"
- "ColorUpgradeItem.java"
- "wily/betterfurnaces/items/ColorUpgradeItem"
- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "ColorUpgradeMenu"
- "COLOR_UPGRADE_CONTAINER"
- "Lwily/factoryapi/base/RegisterListing$Holder;"
- "Lwily/betterfurnaces/items/ColorUpgradeItem$ColorUpgradeMenu;"

### `wily/betterfurnaces/items/ColorUpgradeItem.class`

- "wily/betterfurnaces/items/ColorUpgradeItem"
- "wily/betterfurnaces/items/UpgradeItem"
- "ColorUpgradeItem.java"
- "wily/betterfurnaces/items/ColorUpgradeItem$ColorUpgradeMenu"
- "wily/betterfurnaces/items/UpgradeItem$Type"
- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "ColorUpgradeMenu"
- "Lwily/betterfurnaces/items/UpgradeItem$Type;"
- "(Lnet/minecraft/world/item/Item$Properties;Lwily/betterfurnaces/items/UpgradeItem$Type;Ljava/lang/String;)V"
- "Lwily/betterfurnaces/items/ColorUpgradeItem;"
- "Lwily/factoryapi/base/RegisterListing$Holder;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `wily/betterfurnaces/items/EnergyFuelUpgradeItem.class`

- "wily/betterfurnaces/items/EnergyFuelUpgradeItem"
- "wily/betterfurnaces/items/UpgradeItem"
- "EnergyFuelUpgradeItem.java"
- "wily/betterfurnaces/items/UpgradeItem$Type"
- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "ALTERNATIVE_FUEL"
- "Lwily/betterfurnaces/items/UpgradeItem$Type;"
- "(Lnet/minecraft/world/item/Item$Properties;Lwily/betterfurnaces/items/UpgradeItem$Type;Lnet/minecraft/network/chat/Component;)V"
- "Lwily/betterfurnaces/items/EnergyFuelUpgradeItem;"
- "isUpgradeCompatibleWith"
- "(Lwily/betterfurnaces/items/UpgradeItem;)Z"
- "GENERATOR"
- "Lwily/factoryapi/base/RegisterListing$Holder;"
- "Lwily/betterfurnaces/items/UpgradeItem;"

### `wily/betterfurnaces/items/FactoryUpgradeItem.class`

- "wily/betterfurnaces/items/FactoryUpgradeItem"
- "wily/betterfurnaces/items/UpgradeItem"
- "FactoryUpgradeItem.java"
- "wily/betterfurnaces/items/UpgradeItem$Type"
- "FACTORY"
- "Lwily/betterfurnaces/items/UpgradeItem$Type;"
- "(Lnet/minecraft/world/item/Item$Properties;Lwily/betterfurnaces/items/UpgradeItem$Type;Ljava/lang/String;)V"
- "Lwily/betterfurnaces/items/FactoryUpgradeItem;"
- "wily/betterfurnaces/blockentity/FactoryUpgradeSettings"
- "(Lnet/minecraft/world/item/ItemStack;)Lwily/betterfurnaces/blockentity/FactoryUpgradeSettings;"

### `wily/betterfurnaces/items/FuelEfficiencyUpgradeItem.class`

- "wily/betterfurnaces/items/FuelEfficiencyUpgradeItem"
- "wily/betterfurnaces/items/UpgradeItem"
- "FuelEfficiencyUpgradeItem.java"
- "wily/betterfurnaces/items/UpgradeItem$Type"
- "multiplier"
- "FUEL"
- "Lwily/betterfurnaces/items/UpgradeItem$Type;"
- "(Lnet/minecraft/world/item/Item$Properties;Lwily/betterfurnaces/items/UpgradeItem$Type;)V"
- "Lwily/betterfurnaces/items/FuelEfficiencyUpgradeItem;"
- "tooltip.betterfurnacesreforged.upgrade.infinitely"
- "tooltip.betterfurnacesreforged.upgrade.double"
- "tooltip.betterfurnacesreforged.upgrade.quadruple"
- "tooltip.betterfurnacesreforged.upgrade.multiple"
- "tooltip.betterfurnacesreforged.upgrade.fuel"

### `wily/betterfurnaces/items/GeneratorUpgradeItem.class`

- "wily/betterfurnaces/items/GeneratorUpgradeItem"
- "Lwily/betterfurnaces/items/UpgradeItem;Lwily/factoryapi/base/IFluidHandlerItem<Lwily/factoryapi/base/FactoryItemFluidHandler;>;"
- "wily/betterfurnaces/items/UpgradeItem"
- "wily/factoryapi/base/IFluidHandlerItem"
- "GeneratorUpgradeItem.java"
- "wily/betterfurnaces/items/UpgradeItem$Type"
- "wily/factoryapi/base/RegisterListing$Holder"
- "wily/factoryapi/base/RegisterListing"
- "Lwily/betterfurnaces/items/UpgradeItem$Type;"
- "tooltip.betterfurnacesreforged.upgrade.generator"
- "wily/factoryapi/FactoryAPIPlatform"
- "getPlatformEnergyComponent"
- "(Lnet/minecraft/world/item/Item$Properties;Lwily/betterfurnaces/items/UpgradeItem$Type;Lnet/minecraft/network/chat/Component;)V"
- "Lwily/betterfurnaces/items/GeneratorUpgradeItem;"
- "(Lwily/factoryapi/util/FluidInstance;)Z"
- "wily/factoryapi/util/FluidInstance"
- "Lwily/factoryapi/util/FluidInstance;"
- "isUpgradeCompatibleWith"
- "(Lwily/betterfurnaces/items/UpgradeItem;)Z"
- "ENERGY"
- "Lwily/factoryapi/base/RegisterListing$Holder;"
- "upgradeType"
- "Lwily/betterfurnaces/items/UpgradeItem;"

### `wily/betterfurnaces/items/LiquidFuelUpgradeItem.class`

- "wily/betterfurnaces/items/LiquidFuelUpgradeItem"
- "Lwily/betterfurnaces/items/UpgradeItem;Lwily/factoryapi/base/IFluidHandlerItem<Lwily/factoryapi/base/FactoryItemFluidHandler;>;"
- "wily/betterfurnaces/items/UpgradeItem"
- "wily/factoryapi/base/IFluidHandlerItem"
- "LiquidFuelUpgradeItem.java"
- "wily/betterfurnaces/items/UpgradeItem$Type"
- "ALTERNATIVE_FUEL"
- "Lwily/betterfurnaces/items/UpgradeItem$Type;"
- "(Lnet/minecraft/world/item/Item$Properties;Lwily/betterfurnaces/items/UpgradeItem$Type;Ljava/lang/String;)V"
- "Lwily/betterfurnaces/items/LiquidFuelUpgradeItem;"
- "wily/factoryapi/base/FuelManager"
- "isFuel"
- "wily/factoryapi/ItemContainerPlatform"
- "(Lnet/minecraft/world/item/ItemStack;)Lwily/factoryapi/util/FluidInstance;"
- "wily/factoryapi/util/FluidInstance"
- "additionalLiquidFuels"
- "Lwily/factoryapi/base/config/FactoryConfig;"
- "wily/factoryapi/base/config/FactoryConfig"
- "(Lwily/factoryapi/util/FluidInstance;)Z"
- "Lwily/factoryapi/util/FluidInstance;"

### `wily/betterfurnaces/items/OreProcessingUpgradeItem.class`

- "wily/betterfurnaces/items/OreProcessingUpgradeItem"
- "wily/betterfurnaces/items/UpgradeItem"
- "OreProcessingUpgradeItem.java"
- "wily/betterfurnaces/items/UpgradeItem$Type"
- "multiplier"
- "Lwily/betterfurnaces/items/UpgradeItem$Type;"
- "(Lnet/minecraft/world/item/Item$Properties;Lwily/betterfurnaces/items/UpgradeItem$Type;)V"
- "Lwily/betterfurnaces/items/OreProcessingUpgradeItem;"
- "isUpgradeCompatibleWith"
- "(Lwily/betterfurnaces/items/UpgradeItem;)Z"
- "upgradeType"
- "Lwily/betterfurnaces/items/UpgradeItem;"
- "tooltip.betterfurnacesreforged.upgrade.infinitely"
- "tooltip.betterfurnacesreforged.upgrade.ore"
- "tooltip.betterfurnacesreforged.upgrade.raw"
- "tooltip.betterfurnacesreforged.upgrade.allore"
- "tooltip.betterfurnacesreforged.upgrade.double"
- "tooltip.betterfurnacesreforged.upgrade.quadruple"
- "tooltip.betterfurnacesreforged.upgrade.multiple"
- "tooltip.betterfurnacesreforged.upgrade.ores"

### `wily/betterfurnaces/items/StorageUpgradeItem.class`

- "wily/betterfurnaces/items/StorageUpgradeItem"
- "wily/betterfurnaces/items/UpgradeItem"
- "StorageUpgradeItem.java"
- "wily/betterfurnaces/items/UpgradeItem$Type"
- "Lwily/betterfurnaces/items/UpgradeItem$Type;"
- "(Lnet/minecraft/world/item/Item$Properties;Lwily/betterfurnaces/items/UpgradeItem$Type;Ljava/lang/String;)V"
- "Lwily/betterfurnaces/items/StorageUpgradeItem;"
- "isUpgradeCompatibleWith"
- "(Lwily/betterfurnaces/items/UpgradeItem;)Z"
- "upgradeType"
- "Lwily/betterfurnaces/items/UpgradeItem;"

### `wily/betterfurnaces/items/TierUpgradeItem.class`

- "wily/betterfurnaces/items/TierUpgradeItem"
- "wily/betterfurnaces/items/UpgradeItem"
- "TierUpgradeItem.java"
- "wily/betterfurnaces/items/UpgradeItem$Type"
- "TIER"
- "Lwily/betterfurnaces/items/UpgradeItem$Type;"
- "tooltip.betterfurnacesreforged.upgrade.tier"
- "(Lnet/minecraft/world/item/Item$Properties;Lwily/betterfurnaces/items/UpgradeItem$Type;Lnet/minecraft/network/chat/Component;)V"
- "Lwily/betterfurnaces/items/TierUpgradeItem;"
- "UPGRADE_SHIFT_RIGHT_CLICK"
- "Lwily/factoryapi/base/FactoryItemHandler;"
- "wily/factoryapi/base/FactoryItemHandler"
- "wily/factoryapi/util/CompoundTagUtil"
- "getDefaultCookTime"
- "CookTimeTotal"

### `wily/betterfurnaces/items/UpgradeItem$Type.class`

- "wily/betterfurnaces/items/UpgradeItem$Type"
- "Ljava/lang/Enum<Lwily/betterfurnaces/items/UpgradeItem$Type;>;"
- "UpgradeItem.java"
- "wily/betterfurnaces/items/UpgradeItem"
- "FUEL"
- "Lwily/betterfurnaces/items/UpgradeItem$Type;"
- "ALTERNATIVE_FUEL"

… altri testi tagliati (limite di 1500)
