# Advanced Peripherals (advancedperipherals)

File generato da `scripts/esamina.py` (workflow "Esamina mod"): la mod **non** è nel pack. Non modificarlo a mano.

- Versione: **1.21.1-0.8.2a** (alpha, 2026-10-04), file `AdvancedPeripherals-1.21.1-0.8.2a.jar`, id versione `fxjzpAbL`
- Licenza su Modrinth: Apache-2.0 · download: 391895
- Filtro dei valori: `worldgen/(structure|structure_set|template_pool)|tags/worldgen` · filtro dei testi del codice: `(?i)villag|scientist|structure`

## Mod nel file e dipendenze dichiarate

- `advancedperipherals` 1.21.1-0.8.2a
  - required: `neoforge` [21.1.238,)
  - required: `minecraft` [1.21.1,)
  - required: `computercraft` [1.119.0,)
  - optional: `ae2` [19.2.13,)
  - optional: `minecolonies` [1.1.1300-1.21.1-snapshot,)
  - optional: `patchouli` [1.21-88,)
  - optional: `mekanism` [1.21.1-10.7.15.81,)

## Cartelle di dati (file .json)

- `advancedperipherals:advancement/recipes/combat/armor`: 1
- `advancedperipherals:advancement/recipes/redstone`: 29
- `advancedperipherals:advancement/recipes/tools`: 5
- `advancedperipherals:advancements`: 8
- `advancedperipherals:computercraft/pocket_upgrade`: 7
- `advancedperipherals:computercraft/turtle_upgrade`: 14
- `advancedperipherals:loot_table/blocks`: 16
- `advancedperipherals:loot_tables/chest`: 1
- `advancedperipherals:patchouli_books/manual`: 1
- `advancedperipherals:recipe`: 34
- `advancedperipherals:recipe/armor`: 1
- `advancedperipherals:recipes`: 1
- `advancedperipherals:tags/item`: 1
- `advancedperipherals:tags/item/p2p_attunements`: 1
- `curios:tags/item`: 1
- `minecraft:tags/block`: 3
- `minecraft:tags/block/mineable`: 1
- `minecraft:tags/point_of_interest_type`: 1
- `neoforge:tags/block`: 1

## Valori dei file filtrati


## Testi nel codice


### `de/srendi/advancedperipherals/common/addons/computercraft/peripheral/ColonyPeripheral.class`

- "getStructurePack"
- "()Lcom/minecolonies/api/colony/managers/interfaces/IRegisteredStructureManager;"
- "com/minecolonies/api/colony/managers/interfaces/IRegisteredStructureManager"
- "(Lcom/minecolonies/api/colony/managers/interfaces/IRegisteredStructureManager;)Ljava/util/function/Function;"
- "(Lcom/minecolonies/api/colony/workorders/IWorkOrder;Lcom/minecolonies/api/colony/managers/interfaces/IRegisteredStructureManager;)Ljava/util/Map;"
- "(Lcom/minecolonies/api/colony/buildings/IBuilding;Lcom/minecolonies/api/colony/managers/interfaces/IRegisteredStructureManager;)Ljava/util/Map;"
- "Lcom/minecolonies/api/colony/managers/interfaces/IRegisteredStructureManager;"
- "(Lcom/minecolonies/api/colony/managers/interfaces/IRegisteredStructureManager;Lcom/minecolonies/api/colony/workorders/IServerWorkOrder;)Ljava/util/Map;"
- "(Lcom/minecolonies/api/colony/managers/interfaces/IRegisteredStructureManager;Lcom/minecolonies/api/colony/buildings/IBuilding;)Ljava/util/Map;"

### `de/srendi/advancedperipherals/common/addons/minecolonies/MineColonies.class`

- "getStructurePack"
- "structure"
- "com/minecolonies/api/colony/managers/interfaces/IRegisteredStructureManager"
- "()Lcom/minecolonies/api/colony/managers/interfaces/IRegisteredStructureManager;"
- "com/minecolonies/core/colony/buildings/AbstractBuildingStructureBuilder"
- "(Lcom/minecolonies/api/colony/buildings/IBuilding;Lcom/minecolonies/api/colony/managers/interfaces/IRegisteredStructureManager;)Ljava/util/Map;"
- "Lcom/minecolonies/api/colony/managers/interfaces/IRegisteredStructureManager;"
- "(Lcom/minecolonies/api/colony/buildings/IBuilding;Lcom/minecolonies/api/colony/managers/interfaces/IRegisteredStructureManager;)Ljava/util/Map<Ljava/lang/String;Ljava/lang/Object;>;"
- "(Lcom/minecolonies/api/colony/workorders/IWorkOrder;Lcom/minecolonies/api/colony/managers/interfaces/IRegisteredStructureManager;)Ljava/util/Map;"
- "(Lcom/minecolonies/api/colony/workorders/IWorkOrder;Lcom/minecolonies/api/colony/managers/interfaces/IRegisteredStructureManager;)Ljava/util/Map<Ljava/lang/String;Ljava/lang/Object;>;"
- "Lcom/minecolonies/core/colony/buildings/AbstractBuildingStructureBuilder;"

### `de/srendi/advancedperipherals/common/configuration/WorldConfig.class`

- "Enable the villager structures for the computer scientist."
- "enableVillagerStructures"
- "The weight of the villager structures."
- "villagerStructureWeight"
- "Enable computer scientist trades."
- "enableComputerScientistTrades"

### `de/srendi/advancedperipherals/common/data/EnUsLanguageProvider.class`

- "de/srendi/advancedperipherals/common/setup/APVillagers"
- "COMPUTER_SCIENTIST"
- "net/minecraft/world/entity/npc/VillagerProfession"
- "Computer Scientist"
- "addVillager"
- "entity.minecraft.villager"

### `de/srendi/advancedperipherals/common/data/PoiTypeProvider.class`

- "Lnet/minecraft/data/tags/TagsProvider$TagAppender<Lnet/minecraft/world/entity/ai/village/poi/PoiType;>;"

### `de/srendi/advancedperipherals/common/setup/APRegistration.class`

- "de/srendi/advancedperipherals/common/setup/APVillagers"
- "VILLAGER_PROFESSIONS"
- "VILLAGER_PROFESSION"
- "Lnet/neoforged/neoforge/registries/DeferredRegister<Lnet/minecraft/world/entity/ai/village/poi/PoiType;>;"
- "Lnet/neoforged/neoforge/registries/DeferredRegister<Lnet/minecraft/world/entity/npc/VillagerProfession;>;"

### `de/srendi/advancedperipherals/common/setup/APVillagers.class`

- "net/minecraft/world/entity/npc/VillagerProfession"
- "advancedperipherals:computer_scientist"
- "VILLAGER_WORK_TOOLSMITH"
- "computer_scientist"
- "net/minecraft/world/entity/ai/village/poi/PoiType"
- "de/srendi/advancedperipherals/common/setup/APVillagers"
- "COMPUTER_SCIENTIST_POI"
- "VILLAGER_PROFESSIONS"
- "COMPUTER_SCIENTIST"
- "Ljava/util/function/Supplier<Lnet/minecraft/world/entity/ai/village/poi/PoiType;>;"
- "Ljava/util/function/Supplier<Lnet/minecraft/world/entity/npc/VillagerProfession;>;"
- "Lde/srendi/advancedperipherals/common/setup/APVillagers;"
- "()Lnet/minecraft/world/entity/npc/VillagerProfession;"
- "()Lnet/minecraft/world/entity/ai/village/poi/PoiType;"
- "APVillagers.java"

### `de/srendi/advancedperipherals/common/util/fakeplayer/APFakePlayer.class`

- "net/minecraft/world/level/block/StructureBlock"

### `de/srendi/advancedperipherals/common/village/VillageStructures.class`

- "net/minecraft/world/level/levelgen/structure/pools/StructureTemplatePool"
- "net/minecraft/world/level/levelgen/structure/pools/SinglePoolElement"
- "enableVillagerStructures"
- "Register generating scientist_{} village house"
- "net/minecraft/world/level/levelgen/structure/pools/StructureTemplatePool$Projection"
- "Lnet/minecraft/world/level/levelgen/structure/pools/StructureTemplatePool$Projection;"
- "villagerStructureWeight"
- "de/srendi/advancedperipherals/common/village/VillageStructures"
- "(Lnet/minecraft/core/Registry;Lnet/minecraft/core/Holder;Lnet/minecraft/resources/ResourceLocation;Ljava/lang/String;Lnet/minecraft/world/level/levelgen/structure/pools/StructureTemplatePool$Projection;I)V"
- "Lde/srendi/advancedperipherals/common/village/VillageStructures;"
- "Lnet/minecraft/world/level/levelgen/structure/pools/StructureTemplatePool;"
- "Lnet/minecraft/world/level/levelgen/structure/pools/SinglePoolElement;"
- "Lnet/minecraft/core/Registry<Lnet/minecraft/world/level/levelgen/structure/pools/StructureTemplatePool;>;"
- "Lnet/minecraft/core/Holder<Lnet/minecraft/world/level/levelgen/structure/templatesystem/StructureProcessorList;>;"
- "Ljava/util/List<Lcom/mojang/datafixers/util/Pair<Lnet/minecraft/world/level/levelgen/structure/pools/StructurePoolElement;Ljava/lang/Integer;>;>;"
- "(Lnet/minecraft/core/Registry<Lnet/minecraft/world/level/levelgen/structure/pools/StructureTemplatePool;>;Lnet/minecraft/core/Holder<Lnet/minecraft/world/level/levelgen/structure/templatesystem/StructureProcessorList;>;Lnet/minecraft/resources/ResourceLocation;Ljava/lang/String;Lnet/minecraft/world/…"
- "addStructures"
- "VillageStructures.java"
- "village/\u0001/houses"
- "villages/scientist_\u0001"

### `de/srendi/advancedperipherals/common/village/VillagerTrade$TradeBuilder.class`

- "de/srendi/advancedperipherals/common/village/VillagerTrade$TradeBuilder"
- "villagerEvent"
- "Lnet/neoforged/neoforge/event/village/VillagerTradesEvent;"
- "Lde/srendi/advancedperipherals/common/village/VillagerTrade$Type;"
- "Lnet/neoforged/neoforge/event/village/WandererTradesEvent;"
- "net/neoforged/neoforge/event/village/WandererTradesEvent"
- "net/neoforged/neoforge/event/village/VillagerTradesEvent"
- "Pocket upgrade {} does not exist or was removed by a datapack, skipping villager trade"
- "(Lnet/minecraft/world/item/ItemStack;)Lde/srendi/advancedperipherals/common/village/VillagerTrade$TradeBuilder;"
- "de/srendi/advancedperipherals/common/village/VillagerTrade"
- "(Lde/srendi/advancedperipherals/common/village/VillagerTrade$Type;ILnet/minecraft/world/item/ItemStack;II)V"
- "(Lnet/neoforged/neoforge/event/village/VillagerTradesEvent;Lde/srendi/advancedperipherals/common/village/VillagerTrade$Type;)V"
- "Lde/srendi/advancedperipherals/common/village/VillagerTrade$TradeBuilder;"
- "(Lnet/neoforged/neoforge/event/village/WandererTradesEvent;Lde/srendi/advancedperipherals/common/village/VillagerTrade$Type;)V"
- "(I)Lde/srendi/advancedperipherals/common/village/VillagerTrade$TradeBuilder;"
- "(Lnet/minecraft/world/level/ItemLike;)Lde/srendi/advancedperipherals/common/village/VillagerTrade$TradeBuilder;"
- "(ZLnet/minecraft/resources/ResourceLocation;)Lde/srendi/advancedperipherals/common/village/VillagerTrade$TradeBuilder;"
- "Lde/srendi/advancedperipherals/common/village/VillagerTrade;"
- "VillagerTrade.java"
- "de/srendi/advancedperipherals/common/village/VillagerTrade$Type"

### `de/srendi/advancedperipherals/common/village/VillagerTrade$Type.class`

- "de/srendi/advancedperipherals/common/village/VillagerTrade$Type"
- "Lde/srendi/advancedperipherals/common/village/VillagerTrade$Type;"
- "[Lde/srendi/advancedperipherals/common/village/VillagerTrade$Type;"
- "()[Lde/srendi/advancedperipherals/common/village/VillagerTrade$Type;"
- "(Ljava/lang/String;)Lde/srendi/advancedperipherals/common/village/VillagerTrade$Type;"
- "Ljava/lang/Enum<Lde/srendi/advancedperipherals/common/village/VillagerTrade$Type;>;"
- "VillagerTrade.java"
- "de/srendi/advancedperipherals/common/village/VillagerTrade"

### `de/srendi/advancedperipherals/common/village/VillagerTrade.class`

- "de/srendi/advancedperipherals/common/village/VillagerTrade"
- "Lde/srendi/advancedperipherals/common/village/VillagerTrade$Type;"
- "de/srendi/advancedperipherals/common/village/VillagerTrade$Type"
- "net/minecraft/world/entity/npc/VillagerTrades$ItemListing"
- "(Lde/srendi/advancedperipherals/common/village/VillagerTrade$Type;ILnet/minecraft/world/item/ItemStack;II)V"
- "Lde/srendi/advancedperipherals/common/village/VillagerTrade;"
- "VillagerTrade.java"
- "de/srendi/advancedperipherals/common/village/VillagerTrade$TradeBuilder"
- "net/minecraft/world/entity/npc/VillagerTrades"

### `de/srendi/advancedperipherals/common/village/VillagerTrades.class`

- "de/srendi/advancedperipherals/common/village/VillagerTrade$TradeBuilder"
- "de/srendi/advancedperipherals/common/village/VillagerTrade$Type"
- "Lde/srendi/advancedperipherals/common/village/VillagerTrade$Type;"
- "(Lnet/neoforged/neoforge/event/village/WandererTradesEvent;Lde/srendi/advancedperipherals/common/village/VillagerTrade$Type;)V"
- "(Lnet/minecraft/world/level/ItemLike;)Lde/srendi/advancedperipherals/common/village/VillagerTrade$TradeBuilder;"
- "(I)Lde/srendi/advancedperipherals/common/village/VillagerTrade$TradeBuilder;"
- "net/neoforged/neoforge/event/village/VillagerTradesEvent"
- "()Lnet/minecraft/world/entity/npc/VillagerProfession;"
- "de/srendi/advancedperipherals/common/setup/APVillagers"
- "COMPUTER_SCIENTIST"
- "(Lnet/neoforged/neoforge/event/village/VillagerTradesEvent;Lde/srendi/advancedperipherals/common/village/VillagerTrade$Type;)V"
- "(ZLnet/minecraft/resources/ResourceLocation;)Lde/srendi/advancedperipherals/common/village/VillagerTrade$TradeBuilder;"
- "net/minecraft/world/entity/npc/Villager"
- "getVillagerData"
- "()Lnet/minecraft/world/entity/npc/VillagerData;"
- "net/minecraft/world/entity/npc/VillagerData"
- "de/srendi/advancedperipherals/common/village/VillagerTrades"
- "Lde/srendi/advancedperipherals/common/village/VillagerTrades;"
- "(Lnet/neoforged/neoforge/event/village/WandererTradesEvent;)V"
- "Lnet/neoforged/neoforge/event/village/WandererTradesEvent;"
- "registerVillagerTrades"
- "(Lnet/neoforged/neoforge/event/village/VillagerTradesEvent;)V"
- "Lnet/neoforged/neoforge/event/village/VillagerTradesEvent;"
- "onVillagerDrop"
- "villager"
- "Lnet/minecraft/world/entity/npc/Villager;"
- "VillagerTrades.java"
- "de/srendi/advancedperipherals/common/village/VillagerTrade"
