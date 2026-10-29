# FurnaceMk2 (furnacemk2)

File generato da `scripts/esamina.py` (workflow "Esamina mod"): la mod **non** è nel pack. Non modificarlo a mano.

- Versione: **0.1.11** (release, 2025-07-29), file `furnacemk2-1.21.1-0.1.11.jar`, id versione `dDvEGlWn`
- Licenza su Modrinth: MIT · download: 10151
- Filtro dei valori: `(recipe|recipes|tags/item|tags/block)/` · filtro dei testi del codice: `(?i)^(.*(speed|cook|tier|augment|upgrade|generator|factory|fuel|multiplier|energy|rainbow).*)$`

## Mod nel file e dipendenze dichiarate

- `furnacemk2` 0.1.11
  - required: `neoforge` [21.1.0,)
  - required: `minecraft` [1.21.1, 1.22)
  - required: `vapourware` [0.2.36,)

## Cartelle di dati (file .json)

- `furnacemk2:loot_table/blocks`: 1
- `furnacemk2:recipe`: 5
- `minecraft:tags/block/mineable`: 1

## Valori dei file filtrati


### `data/furnacemk2/recipe/attuned_crystal.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = [" #E", "#D#", "E# "]
- `key.#.item` = "minecraft:lapis_lazuli"
- `key.E.tag` = "c:gems/emerald"
- `key.D.tag` = "c:gems/diamond"
- `result.id` = "furnacemk2:crystal_gem_item"
- `result.count` = 1

### `data/furnacemk2/recipe/experience_core.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = [" # ", "DLD", " # "]
- `key.#.tag` = "c:gems/emerald"
- `key.D.tag` = "c:gems/diamond"
- `key.L.item` = "minecraft:lapis_block"
- `result.id` = "furnacemk2:experience_core"
- `result.count` = 1

### `data/furnacemk2/recipe/furnace_mk2.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["#B#", "CGC", "CFC"]
- `key.#.item` = "minecraft:smooth_stone"
- `key.B.item` = "minecraft:blast_furnace"
- `key.C.tag` = "minecraft:stone_tool_materials"
- `key.G.item` = "minecraft:glass_bottle"
- `key.F.item` = "minecraft:furnace"
- `result.id` = "furnacemk2:furnacemk2"
- `result.count` = 1

### `data/furnacemk2/recipe/insulation_core.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["#C#", "WWW", "#C#"]
- `key.#.tag` = "minecraft:sand"
- `key.C.item` = "minecraft:clay"
- `key.W.item` = "minecraft:white_concrete"
- `result.id` = "furnacemk2:insulation_core"
- `result.count` = 1

### `data/furnacemk2/recipe/thermal_core.json`

- `type` = "minecraft:crafting_shaped"
- `pattern` = ["#L#", "#M#", "BBB"]
- `key.#.item` = "minecraft:nether_brick"
- `key.L.item` = "minecraft:lava_bucket"
- `key.M.item` = "minecraft:magma_block"
- `key.B.item` = "minecraft:blackstone"
- `result.id` = "furnacemk2:thermal_core"
- `result.count` = 1

### `data/minecraft/tags/block/mineable/pickaxe.json`

- `replace` = false
- `values` = ["furnacemk2:furnacemk2"]

## Testi nel codice


### `vapourdrive/furnacemk2/config/ConfigSettings.class`

- "Base efficiency multiplier for the FurnaceMk2"
- "Base experience multiplier for the FurnaceMk2"
- "Base speed multiplier for the FurnaceMk2"
- "furnaceBaseSpeed"
- "FURNACE_BASE_SPEED"
- "Upgraded efficiency multiplier for the FurnaceMk2"
- "furnaceUpgradedEfficiency"
- "FURNACE_UPGRADED_EFFICIENCY"
- "Upgraded experience multiplier for the FurnaceMk2"
- "furnaceUpgradedExperience"
- "FURNACE_UPGRADED_EXPERIENCE"
- "Upgraded speed multiplier for the FurnaceMk2"
- "furnaceUpgradedSpeed"
- "FURNACE_UPGRADED_SPEED"

### `vapourdrive/furnacemk2/furnace/FurnaceData$Data.class`

- "FUEL"
- "COOK_PROGRESS"
- "COOK_MAX"

### `vapourdrive/furnacemk2/furnace/FurnaceMk2Block.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `vapourdrive/furnacemk2/furnace/FurnaceMk2Item.class`

- "FURNACE_BASE_SPEED"
- "\u0001% speed"
- "\u0001% fuel efficiency"
- "java/lang/invoke/StringConcatFactory"

### `vapourdrive/furnacemk2/furnace/FurnaceMk2Menu.class`

- "vapourdrive/vapourware/shared/base/slots/SlotFuel"
- "COOK_PROGRESS"
- "COOK_MAX"
- "getCookProgress"
- "java/lang/invoke/StringConcatFactory"

### `vapourdrive/furnacemk2/furnace/FurnaceMk2Screen.class`

- "getCookProgress"
- "COOK_BAR_XPOS"
- "COOK_BAR_YPOS"
- "COOK_BAR_ICONX"
- "COOK_BAR_ICONY"
- "COOK_BAR_WIDTH"
- "COOK_BAR_HEIGHT"
- "cookPercentage"
- "java/lang/invoke/StringConcatFactory"

### `vapourdrive/furnacemk2/furnace/FurnaceMk2Tile$1.class`

- "AUGMENT"
- "FUEL"

### `vapourdrive/furnacemk2/furnace/FurnaceMk2Tile.class`

- "vapourdrive/vapourware/shared/base/AbstractBaseFuelUserTile"
- "vapourdrive/furnacemk2/furnace/itemhandlers/FurnaceAugmentHandler"
- "AUGMENT_SLOTS"
- "augmentHandler"
- "Lvapourdrive/furnacemk2/furnace/itemhandlers/FurnaceAugmentHandler;"
- "vapourdrive/vapourware/shared/base/itemhandlers/FuelHandler"
- "FUEL_SLOT"
- "(Lvapourdrive/vapourware/shared/base/AbstractBaseFuelUserTile;I)V"
- "fuelHandler"
- "Lvapourdrive/vapourware/shared/base/itemhandlers/FuelHandler;"
- "COOK_PROGRESS"
- "doCookProcesses"
- "COOK_MAX"
- "getCookTime"
- "FUEL"
- "progressCook"
- "getSpeedMultiplier"
- "getExperienceMultiplier"
- "invFuel"
- "cookProgress"
- "cookMax"
- "AUGMENT"
- "FURNACE_BASE_SPEED"
- "FURNACE_UPGRADED_SPEED"
- "FURNACE_UPGRADED_EFFICIENCY"
- "FURNACE_UPGRADED_EXPERIENCE"
- "getCurrentFuel"
- "getMaxFuel"
- "speed"
- "getEfficiencyMultiplier"
- "addFuel"
- "consumeFuel"
- "java/lang/invoke/StringConcatFactory"

### `vapourdrive/furnacemk2/furnace/itemhandlers/FurnaceAugmentHandler.class`

- "vapourdrive/furnacemk2/furnace/itemhandlers/FurnaceAugmentHandler"
- "Lvapourdrive/furnacemk2/furnace/itemhandlers/FurnaceAugmentHandler;"
- "FurnaceAugmentHandler.java"

### `vapourdrive/furnacemk2/furnace/itemhandlers/FurnaceIngredientHandler.class`

- "java/lang/invoke/StringConcatFactory"

### `vapourdrive/furnacemk2/furnace/slots/SlotCore.class`

- "upgradeslot"
- "upgradeItem"

### `vapourdrive/furnacemk2/FurnaceMk2.class`

- "java/lang/management/ManagementFactory"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `vapourdrive/furnacemk2/items/ItemCrystal.class`

- "java/lang/invoke/StringConcatFactory"

### `vapourdrive/furnacemk2/items/ItemFurnaceCore.class`

- "speed"
- "FURNACE_UPGRADED_SPEED"
- "FURNACE_UPGRADED_EXPERIENCE"
- "FURNACE_UPGRADED_EFFICIENCY"
- "\u0001% speed"
- "\u0001% fuel efficiency"
- "java/lang/invoke/StringConcatFactory"

### `vapourdrive/furnacemk2/jei/JEI_plugin.class`

- "FUELING"

### `vapourdrive/furnacemk2/setup/ClientSetup.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `vapourdrive/furnacemk2/setup/Registration.class`

- "speed"
- "()Lnet/neoforged/neoforge/network/IContainerFactory;"
- "(Lnet/neoforged/neoforge/network/IContainerFactory;)Lnet/minecraft/world/inventory/MenuType;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `vapourdrive/furnacemk2/utils/FurnaceUtils.class`

- "getCookingTime"
- "getCookTime"
- "lambda$getCookTime$1"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
