# Turtlematic (turtlematic)

File generato da `scripts/esamina.py` (workflow "Esamina mod"): la mod **non** è nel pack. Non modificarlo a mano.

- Versione: **1.21.1-1.4.10** (release, 2026-08-08), file `turtlematic-forge-1.21.1-1.4.10.jar`, id versione `BYUhSZ5W`
- Licenza su Modrinth: MIT · download: 38822
- Filtro dei valori: `worldgen/(structure|structure_set|template_pool)|tags/worldgen` · filtro dei testi del codice: `(?i)villag|scientist|structure`

## Mod nel file e dipendenze dichiarate

- `turtlematic` 1.4.10
  - required: `neoforge` [21.1.9,21.2)
  - required: `minecraft` [1.21.1,1.21.2)
  - required: `computercraft` [1.116.1,)
  - required: `tweakium` [1.4.6,)
  - required: `broccolium` [1.4.6,)
  - required: `peripheralium` [1.4.6,)
- `peripheralium` 1.4.6 (dentro `peripheralium-forge-1.21.1-1.4.6.jar`)
  - required: `neoforge` [21.1.9,)
  - required: `computercraft` [1.113.0,)
  - required: `broccolium` [1.4.6,)
  - required: `tweakium` [1.4.6,)
- `tweakium` 1.4.9 (dentro `tweakium-forge-1.21.1-1.4.9.jar`)
  - required: `neoforge` [21.1.9,)
  - required: `computercraft` [1.113.1,)
  - required: `broccolium` [1.4.6,)
- `broccolium` 1.4.6 (dentro `broccolium-forge-1.21.1-1.4.6.jar`)
  - required: `neoforge` [21.1.9,)

## Cartelle di dati (file .json)

- `peripheralium:loot_table/blocks`: 1
- `peripheralium:recipe`: 4
- `turtlematic:computercraft/turtle_upgrade`: 39
- `turtlematic:recipe`: 19
- `turtlematic:tags/block`: 3
- `turtlematic:tags/entity_type`: 3
- `turtlematic:tags/item`: 1

## Valori dei file filtrati


## Testi nel codice


### `site/siredvin/turtlematic/data/ModEnLanguageProvider.class`

- "§5It seems too empty for use it now. Feed it with villager soul first"
- "  §6§nCan restock villager trades"

### `site/siredvin/turtlematic/common/recipe/VillagerSoulHarvestIngredient.class`

- "site/siredvin/turtlematic/common/recipe/VillagerSoulHarvestIngredient"
- "(Lnet/minecraft/world/entity/npc/VillagerProfession;)V"
- "Lnet/minecraft/world/entity/npc/VillagerProfession;"
- "Lsite/siredvin/turtlematic/common/recipe/VillagerSoulHarvestIngredient;"
- "net/minecraft/world/entity/npc/VillagerProfession"
- "villager_\u0001"
- "VILLAGER"
- "$i$a$-replaceFirstCharWithCharSequence-VillagerSoulHarvestIngredient$description$1"
- "net/minecraft/world/entity/npc/Villager"
- "getVillagerData"
- "()Lnet/minecraft/world/entity/npc/VillagerData;"
- "net/minecraft/world/entity/npc/VillagerData"
- "()Lnet/minecraft/world/entity/npc/VillagerProfession;"
- "VillagerSoulHarvestIngredient.kt"
- "SMAP\nVillagerSoulHarvestIngredient.kt\nKotlin\n*S Kotlin\n*F\n+ 1 VillagerSoulHarvestIngredient.kt\nsite/siredvin/turtlematic/common/recipe/VillagerSoulHarvestIngredient\n+ 2 fake.kt\nkotlin/jvm/internal/FakeKt\n*L\n1#1,20:1\n1#2:21\n*E\n"

### `site/siredvin/turtlematic/common/recipe/SoulHarvestRecipeRegistry.class`

- "site/siredvin/turtlematic/common/recipe/VillagerSoulHarvestIngredient"
- "net/minecraft/world/entity/npc/VillagerProfession"
- "Lnet/minecraft/world/entity/npc/VillagerProfession;"
- "(Lnet/minecraft/world/entity/npc/VillagerProfession;)V"

### `site/siredvin/turtlematic/computercraft/peripheral/misc/StickyPistonPeripheral.class`

- "net/minecraft/world/level/block/piston/PistonStructureResolver"
- "Cannot resolve piston structure"
- "(Lnet/minecraft/world/level/Level;Lnet/minecraft/world/level/block/piston/PistonStructureResolver;Lnet/minecraft/core/Direction;Z)V"
- "Lnet/minecraft/world/level/block/piston/PistonStructureResolver;"

### `site/siredvin/turtlematic/computercraft/peripheral/misc/PistonPeripheral.class`

- "net/minecraft/world/level/block/piston/PistonStructureResolver"
- "Cannot resolve piston structure"
- "(Lnet/minecraft/world/level/Level;Lnet/minecraft/world/level/block/piston/PistonStructureResolver;Lnet/minecraft/core/Direction;Z)V"
- "Lnet/minecraft/world/level/block/piston/PistonStructureResolver;"

### `site/siredvin/turtlematic/computercraft/peripheral/forged/MercantileAutomataCorePeripheral.class`

- "getVillagerData"

### `site/siredvin/turtlematic/computercraft/peripheral/forged/BrewingAutomataCorePeripheral.class`

- "net/minecraft/world/entity/monster/ZombieVillager"

### `site/siredvin/turtlematic/computercraft/plugins/AutomataTradePlugin.class`

- "net/minecraft/world/entity/npc/Villager"

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

### `site/siredvin/broccolium/modules/base/util/world/PistonSimulation.class`

- "(Lnet/minecraft/world/level/Level;Lnet/minecraft/world/level/block/piston/PistonStructureResolver;Lnet/minecraft/core/Direction;Z)V"
- "net/minecraft/world/level/block/piston/PistonStructureResolver"
- "Lnet/minecraft/world/level/block/piston/PistonStructureResolver;"
- "(Lsite/siredvin/broccolium/modules/base/util/world/PistonSimulation;Lnet/minecraft/world/level/Level;Lnet/minecraft/world/level/block/piston/PistonStructureResolver;Lnet/minecraft/core/Direction;ZILjava/lang/Object;)V"
