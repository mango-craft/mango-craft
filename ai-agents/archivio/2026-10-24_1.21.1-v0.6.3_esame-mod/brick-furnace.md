# Brick Furnace (brick-furnace)

File generato da `scripts/esamina.py` (workflow "Esamina mod"): la mod **non** è nel pack. Non modificarlo a mano.

- Versione: **1.21.1-4.2.1.0** (release, 2025-11-06), file `brickfurnace-neoforge-1.21.1-4.2.1.0.jar`, id versione `QQeBRsPL`
- Licenza su Modrinth: MIT · download: 23598
- Filtro dei valori: `(recipe|recipes|tags/item|tags/block)/` · filtro dei testi del codice: `(?i)^(.*(speed|cook|tier|augment|upgrade|generator|factory|fuel|multiplier|energy|rainbow).*)$`

## Mod nel file e dipendenze dichiarate

- `brickfurnace` 1.21.1-4.2.1.0
  - required: `neoforge` [21.1.62,)
  - required: `minecraft` [1.21.1, 1.22)
  - optional: `jei` [19.19.0.219,)
  - optional: `roughlyenoughitems` [16.0.788,)
  - optional: `theoneprobe` [1.21_neo-12.0.3,)
  - optional: `immersiveengineering` [1.21.1-12.0.0,)

## Cartelle di dati (file .json)

- `brickfurnace:advancement`: 1
- `brickfurnace:advancement/recipes/decorations`: 2
- `brickfurnace:loot_table/blocks`: 3
- `brickfurnace:recipe`: 3
- `minecraft:tags/block/mineable`: 1

## Valori dei file filtrati


### `data/brickfurnace/advancement/recipes/decorations/brick_blast_furnace.json`

- `parent` = "minecraft:recipes/root"
- `rewards.recipes` = ["brickfurnace:brick_blast_furnace"]
- `criteria.has_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_furnace.conditions.items[0].items` = "brickfurnace:brick_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `criteria.has_the_recipe.conditions.recipe` = "brickfurnace:brick_blast_furnace"
- `requirements[0]` = ["has_furnace", "has_the_recipe"]

### `data/brickfurnace/advancement/recipes/decorations/brick_smoker.json`

- `parent` = "minecraft:recipes/root"
- `rewards.recipes` = ["brickfurnace:brick_smoker"]
- `criteria.has_furnace.trigger` = "minecraft:inventory_changed"
- `criteria.has_furnace.conditions.items[0].items` = "brickfurnace:brick_furnace"
- `criteria.has_the_recipe.trigger` = "minecraft:recipe_unlocked"
- `criteria.has_the_recipe.conditions.recipe` = "brickfurnace:brick_smoker"
- `requirements[0]` = ["has_furnace", "has_the_recipe"]

### `data/brickfurnace/recipe/brick_blast_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `pattern` = ["III", "IXI", "###"]
- `key.#.item` = "minecraft:bricks"
- `key.X.item` = "brickfurnace:brick_furnace"
- `key.I.tag` = "c:ingots/iron"
- `result.id` = "brickfurnace:brick_blast_furnace"

### `data/brickfurnace/recipe/brick_smoker.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `pattern` = [" # ", "#X#", " # "]
- `key.#.tag` = "minecraft:logs"
- `key.X.item` = "brickfurnace:brick_furnace"
- `result.id` = "brickfurnace:brick_smoker"

### `data/brickfurnace/recipe/brick_furnace.json`

- `type` = "minecraft:crafting_shaped"
- `category` = "misc"
- `pattern` = ["###", "# #", "###"]
- `key.#.tag` = "c:bricks/normal"
- `result.id` = "brickfurnace:brick_furnace"

### `data/minecraft/tags/block/mineable/pickaxe.json`

- `replace` = false
- `values` = ["brickfurnace:brick_furnace", "brickfurnace:brick_blast_furnace", "brickfurnace:brick_smoker"]

## Testi nel codice


### `de/cech12/brickfurnace/rei/BrickFurnaceReiClientPlugin$BrickBlastingDisplay.class`

- "net/minecraft/world/item/crafting/AbstractCookingRecipe"
- "getCookingTime"
- "getCookTimeFactor"
- "me/shedaniel/rei/plugin/common/displays/cooking/DefaultCookingDisplay"
- "Lnet/minecraft/world/item/crafting/RecipeHolder<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "(Lnet/minecraft/world/item/crafting/RecipeHolder<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;)V"

### `de/cech12/brickfurnace/rei/BrickFurnaceReiClientPlugin$BrickSmokingDisplay.class`

- "net/minecraft/world/item/crafting/AbstractCookingRecipe"
- "getCookingTime"
- "getCookTimeFactor"
- "me/shedaniel/rei/plugin/common/displays/cooking/DefaultCookingDisplay"
- "Lnet/minecraft/world/item/crafting/RecipeHolder<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "(Lnet/minecraft/world/item/crafting/RecipeHolder<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;)V"

### `de/cech12/brickfurnace/rei/BrickFurnaceReiClientPlugin$BrickSmeltingDisplay.class`

- "net/minecraft/world/item/crafting/AbstractCookingRecipe"
- "getCookingTime"
- "getCookTimeFactor"
- "me/shedaniel/rei/plugin/common/displays/cooking/DefaultCookingDisplay"
- "Lnet/minecraft/world/item/crafting/RecipeHolder<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "(Lnet/minecraft/world/item/crafting/RecipeHolder<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;)V"

### `de/cech12/brickfurnace/rei/BrickFurnaceReiClientPlugin.class`

- "me/shedaniel/rei/plugin/client/categories/cooking/DefaultCookingCategory"
- "FUEL"
- "net/minecraft/world/item/crafting/AbstractCookingRecipe"
- "Lme/shedaniel/rei/api/common/category/CategoryIdentifier<Lme/shedaniel/rei/plugin/common/displays/cooking/DefaultCookingDisplay;>;"
- "(Lme/shedaniel/rei/api/client/registry/category/CategoryRegistry;Lme/shedaniel/rei/api/common/category/CategoryIdentifier<Lme/shedaniel/rei/plugin/common/displays/cooking/DefaultCookingDisplay;>;Lnet/minecraft/world/level/block/Block;Ljava/lang/String;)V"
- "java/lang/invoke/StringConcatFactory"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `de/cech12/brickfurnace/Constants.class`

- "org/slf4j/LoggerFactory"

### `de/cech12/brickfurnace/block/BrickSmokerBlock.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `de/cech12/brickfurnace/block/BrickBlastFurnaceBlock.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `de/cech12/brickfurnace/block/BrickFurnaceBlock.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `de/cech12/brickfurnace/jei/BrickSmeltingCategory.class`

- "getCookTimeFactor"
- "mezz/jei/library/plugins/vanilla/cooking/AbstractCookingCategory"
- "Lmezz/jei/library/plugins/vanilla/cooking/AbstractCookingCategory<Lde/cech12/brickfurnace/crafting/BrickSmeltingRecipe;>;"

### `de/cech12/brickfurnace/jei/BrickBlastingCategory.class`

- "getCookTimeFactor"
- "mezz/jei/library/plugins/vanilla/cooking/AbstractCookingCategory"
- "Lmezz/jei/library/plugins/vanilla/cooking/AbstractCookingCategory<Lde/cech12/brickfurnace/crafting/BrickBlastingRecipe;>;"

### `de/cech12/brickfurnace/jei/BrickFurnaceJEIPlugin.class`

- "FUELING"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `de/cech12/brickfurnace/jei/BrickSmokingCategory.class`

- "getCookTimeFactor"
- "mezz/jei/library/plugins/vanilla/cooking/AbstractCookingCategory"
- "Lmezz/jei/library/plugins/vanilla/cooking/AbstractCookingCategory<Lde/cech12/brickfurnace/crafting/BrickSmokingRecipe;>;"

### `de/cech12/brickfurnace/init/ModBlockEntityTypes.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `de/cech12/brickfurnace/init/ModItems.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `de/cech12/brickfurnace/init/ModBlocks.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `de/cech12/brickfurnace/init/ModRecipeTypes.class`

- "Lnet/minecraft/world/item/crafting/SimpleCookingSerializer;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `de/cech12/brickfurnace/compat/immersiveengineering/BrickFurnaceHeater.class`

- "canCook"
- "defaultFurnaceEnergyCost"
- "defaultFurnaceSpeedupCost"
- "heatEnergyRatio"
- "energyToUse"
- "energyAvailable"
- "energyConsumed"

### `de/cech12/brickfurnace/compat/immersiveengineering/ImmersiveEngineering.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `de/cech12/brickfurnace/compat/TOPCompat.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `de/cech12/brickfurnace/compat/TOPCompat$PluginTOPRegistry$1.class`

- "top.brickfurnace.fuel"
- "cookTime"
- "cookTimeTotal"
- "java/lang/invoke/StringConcatFactory"

### `de/cech12/brickfurnace/platform/services/IConfigHelper.class`

- "COOK_TIME_FACTOR_DEFAULT"
- "COOK_TIME_FACTOR_DESCRIPTION"
- "Cook time factor of all added brick furnaces in relation to corresponding vanilla furnaces. (i. e. 0.5 - half the time, 1.0 same time, 2.0 twice the time)"
- "COOK_TIME_FACTOR_MIN"
- "COOK_TIME_FACTOR_MAX"
- "Burn time factor (fuel efficiency) of all added brick furnaces in relation to corresponding vanilla furnaces. (i. e. 0.5 - half the time [less efficient], 1.0 same time [default], 2.0 twice the time [more efficient])"
- "getCookTimeFactor"

### `de/cech12/brickfurnace/platform/Services.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "java/lang/invoke/StringConcatFactory"

### `de/cech12/brickfurnace/platform/NeoForgeConfigHelper.class`

- "COOK_TIME_FACTOR"
- "Cook time factor of all added brick furnaces in relation to corresponding vanilla furnaces. (i. e. 0.5 - half the time, 1.0 same time, 2.0 twice the time)"
- "cookTimeFactor"
- "Burn time factor (fuel efficiency) of all added brick furnaces in relation to corresponding vanilla furnaces. (i. e. 0.5 - half the time [less efficient], 1.0 same time [default], 2.0 twice the time [more efficient])"
- "getCookTimeFactor"

### `de/cech12/brickfurnace/blockentity/BrickBlastFurnaceBlockEntity.class`

- "getCookTimeFactor"

### `de/cech12/brickfurnace/blockentity/BrickFurnaceBlockEntity.class`

- "getCookTimeFactor"

### `de/cech12/brickfurnace/blockentity/BrickSmokerBlockEntity.class`

- "getCookTimeFactor"

### `de/cech12/brickfurnace/blockentity/AbstractBrickFurnaceBlockEntity.class`

- "getTotalCookTime"
- "net/minecraft/world/item/crafting/AbstractCookingRecipe"
- "getCookingTime"
- "getCookTimeFactor"
- "Lnet/minecraft/world/item/crafting/RecipeType<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "COOK_TIME"
- "COOK_TIME_TOTAL"
- "FUEL"
- "Lnet/minecraft/world/item/crafting/RecipeHolder<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "(Lnet/minecraft/world/level/block/entity/BlockEntityType<*>;Lnet/minecraft/core/BlockPos;Lnet/minecraft/world/level/block/state/BlockState;Lnet/minecraft/world/item/crafting/RecipeType<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;Lnet/minecraft/world/item/crafting/RecipeType<+Lnet/min…"
- "fuel"
- "(Lnet/minecraft/world/item/crafting/RecipeHolder<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;)I"
- "()Lnet/minecraft/world/item/crafting/RecipeHolder<+Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;>;"
- "abstractCookingRecipe"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `de/cech12/brickfurnace/BrickFurnaceMod.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `de/cech12/brickfurnace/CommonLoader.class`

- "java/lang/invoke/LambdaMetafactory"
- "metafactory"

### `de/cech12/brickfurnace/crafting/BrickSmeltingRecipe.class`

- "net/minecraft/world/item/crafting/AbstractCookingRecipe"
- "(Lnet/minecraft/world/item/crafting/RecipeType;Ljava/lang/String;Lnet/minecraft/world/item/crafting/CookingBookCategory;Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/item/ItemStack;FI)V"
- "()Lnet/minecraft/world/item/crafting/CookingBookCategory;"
- "getCookingTime"
- "getCookTimeFactor"
- "(Ljava/lang/String;Lnet/minecraft/world/item/crafting/CookingBookCategory;Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/item/ItemStack;FI)V"
- "Lnet/minecraft/world/item/crafting/SimpleCookingSerializer;"
- "net/minecraft/world/item/crafting/SimpleCookingSerializer"
- "()Lnet/minecraft/world/item/crafting/AbstractCookingRecipe$Factory;"
- "(Lnet/minecraft/world/item/crafting/AbstractCookingRecipe$Factory;I)V"
- "Lnet/minecraft/world/item/crafting/SimpleCookingSerializer<Lde/cech12/brickfurnace/crafting/BrickSmeltingRecipe;>;"
- "Lnet/minecraft/world/item/crafting/CookingBookCategory;"
- "(Ljava/lang/String;Lnet/minecraft/world/item/crafting/CookingBookCategory;Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/item/ItemStack;FI)Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;"
- "(Ljava/lang/String;Lnet/minecraft/world/item/crafting/CookingBookCategory;Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/item/ItemStack;FI)Lde/cech12/brickfurnace/crafting/BrickSmeltingRecipe;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "net/minecraft/world/item/crafting/AbstractCookingRecipe$Factory"
- "Factory"

### `de/cech12/brickfurnace/crafting/BrickSmokingRecipe.class`

- "net/minecraft/world/item/crafting/AbstractCookingRecipe"
- "(Lnet/minecraft/world/item/crafting/RecipeType;Ljava/lang/String;Lnet/minecraft/world/item/crafting/CookingBookCategory;Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/item/ItemStack;FI)V"
- "()Lnet/minecraft/world/item/crafting/CookingBookCategory;"
- "getCookingTime"
- "getCookTimeFactor"
- "(Ljava/lang/String;Lnet/minecraft/world/item/crafting/CookingBookCategory;Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/item/ItemStack;FI)V"
- "Lnet/minecraft/world/item/crafting/SimpleCookingSerializer;"
- "net/minecraft/world/item/crafting/SimpleCookingSerializer"
- "()Lnet/minecraft/world/item/crafting/AbstractCookingRecipe$Factory;"
- "(Lnet/minecraft/world/item/crafting/AbstractCookingRecipe$Factory;I)V"
- "Lnet/minecraft/world/item/crafting/SimpleCookingSerializer<Lde/cech12/brickfurnace/crafting/BrickSmokingRecipe;>;"
- "Lnet/minecraft/world/item/crafting/CookingBookCategory;"
- "(Ljava/lang/String;Lnet/minecraft/world/item/crafting/CookingBookCategory;Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/item/ItemStack;FI)Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;"
- "(Ljava/lang/String;Lnet/minecraft/world/item/crafting/CookingBookCategory;Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/item/ItemStack;FI)Lde/cech12/brickfurnace/crafting/BrickSmokingRecipe;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "net/minecraft/world/item/crafting/AbstractCookingRecipe$Factory"
- "Factory"

### `de/cech12/brickfurnace/crafting/BrickBlastingRecipe.class`

- "net/minecraft/world/item/crafting/AbstractCookingRecipe"
- "(Lnet/minecraft/world/item/crafting/RecipeType;Ljava/lang/String;Lnet/minecraft/world/item/crafting/CookingBookCategory;Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/item/ItemStack;FI)V"
- "()Lnet/minecraft/world/item/crafting/CookingBookCategory;"
- "getCookingTime"
- "getCookTimeFactor"
- "(Ljava/lang/String;Lnet/minecraft/world/item/crafting/CookingBookCategory;Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/item/ItemStack;FI)V"
- "Lnet/minecraft/world/item/crafting/SimpleCookingSerializer;"
- "net/minecraft/world/item/crafting/SimpleCookingSerializer"
- "()Lnet/minecraft/world/item/crafting/AbstractCookingRecipe$Factory;"
- "(Lnet/minecraft/world/item/crafting/AbstractCookingRecipe$Factory;I)V"
- "Lnet/minecraft/world/item/crafting/SimpleCookingSerializer<Lde/cech12/brickfurnace/crafting/BrickBlastingRecipe;>;"
- "Lnet/minecraft/world/item/crafting/CookingBookCategory;"
- "(Ljava/lang/String;Lnet/minecraft/world/item/crafting/CookingBookCategory;Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/item/ItemStack;FI)Lnet/minecraft/world/item/crafting/AbstractCookingRecipe;"
- "(Ljava/lang/String;Lnet/minecraft/world/item/crafting/CookingBookCategory;Lnet/minecraft/world/item/crafting/Ingredient;Lnet/minecraft/world/item/ItemStack;FI)Lde/cech12/brickfurnace/crafting/BrickBlastingRecipe;"
- "java/lang/invoke/LambdaMetafactory"
- "metafactory"
- "net/minecraft/world/item/crafting/AbstractCookingRecipe$Factory"
- "Factory"
