# UnlimitedPeripheralWorks (unlimitedperipheralworks)

File generato da `scripts/esamina.py` (workflow "Esamina mod"): la mod **non** è nel pack. Non modificarlo a mano.

- Versione: **1.21.1-1.9.2** (alpha, 2026-09-17), file `peripheralworks-forge-1.21.1-1.9.2.jar`, id versione `l84f9GYD`
- Licenza su Modrinth: MIT · download: 140428
- Filtro dei valori: `worldgen/(structure|structure_set|template_pool)|tags/worldgen` · filtro dei testi del codice: `(?i)villag|scientist|structure`

## Mod nel file e dipendenze dichiarate

- `peripheralworks` 1.9.2
  - required: `neoforge` [21.1.217,21.2)
  - required: `minecraft` [1.21.1,1.21.2)
  - required: `computercraft` [1.113.1,)
  - required: `peripheralium` [1.4.6,)
  - required: `broccolium` [1.4.6,)
  - required: `tweakium` [1.4.9,)
  - optional: `hostilenetworks` [6.5.1,)
  - optional: `extrahnn` [2.2.5,)
- `broccolium` 1.4.6 (dentro `broccolium-forge-1.21.1-1.4.6.jar`)
  - required: `neoforge` [21.1.9,)
- `peripheralium` 1.4.6 (dentro `peripheralium-forge-1.21.1-1.4.6.jar`)
  - required: `neoforge` [21.1.9,)
  - required: `computercraft` [1.113.0,)
  - required: `broccolium` [1.4.6,)
  - required: `tweakium` [1.4.6,)
- `tweakium` 1.4.9 (dentro `tweakium-forge-1.21.1-1.4.9.jar`)
  - required: `neoforge` [21.1.9,)
  - required: `computercraft` [1.113.1,)
  - required: `broccolium` [1.4.6,)

## Cartelle di dati (file .json)

- `computercraft:tags/block`: 1
- `minecraft:recipe`: 5
- `peripheralium:loot_table/blocks`: 1
- `peripheralium:recipe`: 4
- `peripheralworks:computercraft/pocket_upgrade`: 13
- `peripheralworks:computercraft/turtle_upgrade`: 9
- `peripheralworks:loot_table/blocks`: 14
- `peripheralworks:recipe`: 23
- `peripheralworks:tags/block`: 2
- `peripheralworks:tags/entity_type`: 1
- `peripheralworks:tags/item`: 2
- `peripheralworks:tags/item/p2p_attunements`: 1

## Valori dei file filtrati


## Testi nel codice


### `site/siredvin/peripheralworks/ForgePeripheralWorks.class`

- "easy_villagers"

### `site/siredvin/peripheralworks/common/configuration/integration/EasyVillagersConfiguration.class`

- "site/siredvin/peripheralworks/common/configuration/integration/EasyVillagersConfiguration"
- "Lsite/siredvin/peripheralworks/common/configuration/integration/EasyVillagersConfiguration;"
- "easy_villagers"
- "EasyVillagersConfiguration.kt"

### `site/siredvin/peripheralworks/data/ModTagsProvider.class`

- "STRUCTURE_VOID"

### `site/siredvin/peripheralworks/integrations/easy_villagers/AutoTraderPlugin.class`

- "site/siredvin/peripheralworks/integrations/easy_villagers/AutoTraderPlugin"
- "site/siredvin/peripheralworks/integrations/easy_villagers/TraderPlugin"
- "(Lde/maxhenkel/easyvillagers/blocks/tileentity/AutoTraderTileentity;)V"
- "de/maxhenkel/easyvillagers/blocks/tileentity/TraderTileentityBase"
- "(Lde/maxhenkel/easyvillagers/blocks/tileentity/TraderTileentityBase;)V"
- "Lde/maxhenkel/easyvillagers/blocks/tileentity/AutoTraderTileentity;"
- "Lsite/siredvin/peripheralworks/integrations/easy_villagers/AutoTraderPlugin;"
- "de/maxhenkel/easyvillagers/blocks/tileentity/AutoTraderTileentity"
- "getVillagerEntity"
- "()Lde/maxhenkel/easyvillagers/entity/EasyVillagerEntity;"
- "de/maxhenkel/easyvillagers/entity/EasyVillagerEntity"
- "villager"
- "Lde/maxhenkel/easyvillagers/entity/EasyVillagerEntity;"
- "Lsite/siredvin/peripheralworks/integrations/easy_villagers/TraderPlugin;"

### `site/siredvin/peripheralworks/integrations/easy_villagers/Integration$AutoTraderProvider.class`

- "site/siredvin/peripheralworks/integrations/easy_villagers/Integration$AutoTraderProvider"
- "Lsite/siredvin/peripheralworks/integrations/easy_villagers/Integration$AutoTraderProvider;"
- "easy_villager_trader"
- "site/siredvin/peripheralworks/common/configuration/integration/EasyVillagersConfiguration"
- "Lsite/siredvin/peripheralworks/common/configuration/integration/EasyVillagersConfiguration;"
- "de/maxhenkel/easyvillagers/blocks/tileentity/AutoTraderTileentity"
- "site/siredvin/peripheralworks/integrations/easy_villagers/AutoTraderPlugin"
- "(Lde/maxhenkel/easyvillagers/blocks/tileentity/AutoTraderTileentity;)V"
- "de/maxhenkel/easyvillagers/blocks/tileentity/TraderTileentityBase"
- "site/siredvin/peripheralworks/integrations/easy_villagers/TraderPlugin"
- "(Lde/maxhenkel/easyvillagers/blocks/tileentity/TraderTileentityBase;)V"
- "site/siredvin/peripheralworks/integrations/easy_villagers/Integration"

### `site/siredvin/peripheralworks/integrations/easy_villagers/Integration.class`

- "site/siredvin/peripheralworks/integrations/easy_villagers/Integration"
- "Lsite/siredvin/peripheralworks/integrations/easy_villagers/Integration;"
- "site/siredvin/peripheralworks/integrations/easy_villagers/Integration$AutoTraderProvider"
- "Lsite/siredvin/peripheralworks/integrations/easy_villagers/Integration$AutoTraderProvider;"

### `site/siredvin/peripheralworks/integrations/easy_villagers/TraderPlugin.class`

- "site/siredvin/peripheralworks/integrations/easy_villagers/TraderPlugin"
- "(Lde/maxhenkel/easyvillagers/blocks/tileentity/TraderTileentityBase;)V"
- "Lde/maxhenkel/easyvillagers/blocks/tileentity/TraderTileentityBase;"
- "Lsite/siredvin/peripheralworks/integrations/easy_villagers/TraderPlugin;"
- "hasVillager"
- "de/maxhenkel/easyvillagers/blocks/tileentity/TraderTileentityBase"
- "getVillagerEntity"
- "()Lde/maxhenkel/easyvillagers/entity/EasyVillagerEntity;"
- "getVillagerData"
- "villager"
- "Lde/maxhenkel/easyvillagers/entity/EasyVillagerEntity;"
- "de/maxhenkel/easyvillagers/entity/EasyVillagerEntity"

### `site/siredvin/peripheralworks/integrations/integrateddynamics/Integration.class`

- "(Lorg/cyclops/cyclopscore/datastructure/DimPos;)Lnet/minecraft/nbt/CompoundTag;"
- "org/cyclops/cyclopscore/datastructure/DimPos"
- "Lorg/cyclops/cyclopscore/datastructure/DimPos;"
- "(Lorg/cyclops/cyclopscore/datastructure/DimPos;Lnet/minecraft/nbt/Tag;)V"
- "(Lsite/siredvin/peripheralworks/integrations/integrateddynamics/Integration;Lorg/cyclops/cyclopscore/datastructure/DimPos;)Lorg/cyclops/integrateddynamics/core/evaluate/variable/ValueTypeNbt$ValueNbt;"
- "(Lorg/cyclops/cyclopscore/datastructure/DimPos;)Lorg/cyclops/integrateddynamics/core/evaluate/variable/ValueTypeNbt$ValueNbt;"
- "()Lorg/cyclops/cyclopscore/datastructure/DimPos;"

### `site/siredvin/broccolium/modules/base/util/world/PistonSimulation.class`

- "(Lnet/minecraft/world/level/Level;Lnet/minecraft/world/level/block/piston/PistonStructureResolver;Lnet/minecraft/core/Direction;Z)V"
- "net/minecraft/world/level/block/piston/PistonStructureResolver"
- "Lnet/minecraft/world/level/block/piston/PistonStructureResolver;"
- "(Lsite/siredvin/broccolium/modules/base/util/world/PistonSimulation;Lnet/minecraft/world/level/Level;Lnet/minecraft/world/level/block/piston/PistonStructureResolver;Lnet/minecraft/core/Direction;ZILjava/lang/Object;)V"

### `site/siredvin/tweakium/modules/peripheral/representation/EnrichersKt.class`

- "getVillagerData"
- "villagerData"
- "villagerData$lambda$0"
- "net/minecraft/world/entity/npc/Villager"
- "forVillager"
- "(Lnet/minecraft/world/entity/npc/Villager;)Ljava/util/Map;"
- "$i$a$-forEach-EnrichersKt$villagerData$1$1"

### `site/siredvin/tweakium/modules/peripheral/representation/LuaRepresentation.class`

- "forVillager"
- "(Lnet/minecraft/world/entity/npc/Villager;)Ljava/util/Map;"
- "(Lnet/minecraft/world/entity/npc/Villager;)Ljava/util/Map<Ljava/lang/String;Ljava/lang/Object;>;"
- "villager"
- "net/minecraft/world/entity/npc/Villager"
- "getVillagerData"
- "()Lnet/minecraft/world/entity/npc/VillagerData;"
- "net/minecraft/world/entity/npc/VillagerData"
- "()Lnet/minecraft/world/entity/npc/VillagerProfession;"
- "net/minecraft/world/entity/npc/VillagerProfession"
- "Lnet/minecraft/world/entity/npc/VillagerProfession;"
- "getVillagerXp"
- "()Lnet/minecraft/world/entity/npc/VillagerType;"
- "net/minecraft/world/entity/npc/VillagerType"
- "Lnet/minecraft/world/entity/npc/VillagerData;"
- "Lnet/minecraft/world/entity/npc/Villager;"
