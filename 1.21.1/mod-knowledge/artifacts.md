# Artifacts

Aggiornata il 24/10/2026 · nel pack dalla 0.1.1, versione 13.2.5 (`../docs/0403-distinta-mod.md`; ruolo e licenza in `../docs/0301-mod.md`) · fonti: sorgente (ochotonida/artifacts @7cf7dc42), file generato dall'istanza di prova, inventario del pack, controllo dei nomi, file delle mod letti con il workflow Esamina mod. Materiale grezzo: `../../ai-agents/archivio/2026-10-19_1.21.1-v0.6.0_config-mod/`, `_riconteggio/` e `2026-10-19_1.21.1-v0.5.3_esame-mod/`.

## Config

`config/artifacts/general.toml` (un solo file, letto con night-config dalla mod: le chiavi mancanti prendono il valore di serie, ma nel pack si porta **completo**). Chiavi, dal file generato dall'istanza di prova:

| Sezione | Chiave | Di serie | Nel pack (0.6.0) |
|---|---|---|---|
| (livello base) | `archaeologyChance` | 0.0625 | invariata |
| | `artifactRarity` | 1.0 | invariata (regola tutte le casse, vanilla e modded) |
| | `entityEquipmentChance` | 0.0015 | invariata |
| `[campsite]` | `allowLightSources`, `campsiteCount` 40, `maxY` 40, `minY` -60, `mimicChance` 0.3, `minimalistCampsites`, `useModdedChests` | di serie | invariate |
| `[slots]` | `enableAccessoriesCompat` | `true` | **`false`** (riavvio) |
| | `enableCuriosCompat` | `true` | `true` (riavvio) |
| | `enableTrinketsCompat`, `addFaceSlot`, `removeSlotRestrictions` | `true` / `false` / `false` | invariate (Trinkets non c'è nel pack) |

Dove si trovano gli accessori nel pack (Curios, Accessories, menu dell'Aether): tema `../theme-knowledge/accessori.md`.

Decisione del 16/10: `enableAccessoriesCompat = false`, `enableCuriosCompat = true`, **prima di creare il mondo vero**, così Artifacts e Ars Nouveau condividono un'unica interfaccia Curios, non si possono indossare due copie dello stesso artefatto e Artifacts non passa mai per Accessories. Funziona con overlay di dati nel `pack.mcmeta` della mod (`overlay_disable_accessories` svuota le etichette degli slot di Accessories). File portato nel pack dalla 0.6.0 (provata il 21/10, `../lavoro/versioni/v0.6.0.md`).

Slot contesi con Ars Nouveau (testa, collana, cintura, 1 slot ciascuno): se diventano stretti si aumentano con un file di slot Curios nel datapack, formato da verificare (tema aperto, `../lavoro/0503-temi-aperti.md`).

## Artefatti nelle casse delle strutture modded (nostro datapack)

Artifacts mette i suoi oggetti solo nelle casse vanilla (si aggancia ai nomi come `minecraft:chests/abandoned_mineshaft`), e NeoForge applica i modificatori di bottino solo alla tabella "radice" scritta nella cassa. Il nostro datapack ha **15 file** in `data/matteo_tweaks/loot_modifiers/artifacts/`, uno per livello di rarità: ognuno applica una tabella di Artifacts (già bilanciata e soggetta alla sua config) a un elenco di casse modded, **148** in tutto dalla 0.6.0 (readme nella cartella, con i livelli). Regola: **una sola cassa per struttura, quella del tesoro finale**, non tutte le stanze.

### Cosa è stato fatto nella 0.6.0 (B01, B03)

- **Tolti i 15 nomi che non esistevano** (controllo dei nomi): When Dungeons Arise `desert_city_big`, `illager_fortress_small`, `giant_mushroom/red_giant_mushroom`, `giant_mushroom/twin_giant_mushroom`, `temple_treasure_small`, `house_tower_treasure`, `pillager_palace_treasure`; Dungeons and Taverns `ruin_loot_1…7` e `trident_trial_monument/ttm_treasure_chest`. Sono nomi di versioni vecchie: `ruin_loot_master` è la tabella radice che ora sceglie tra `dungeon_1…7` (già collegate), il palazzo Shiraz e le torri/templi hanno i nomi nuovi già nei file; `desert_city_big` non ha più una tabella con quel nome; il monumento del tridente ha tre tabelle nuove, di cui una collegata il 19/10 (vedi sotto).
- **Aggiunte, con il livello** (livello = tabella di Artifacts di riferimento, scelto per somiglianza con le casse già collegate della stessa struttura o dello stesso tipo): When Dungeons Arise `kisegi_sanctuary/kisegi_sanctuary_treasure` e `mechanical_nest/mechanical_nest_treasure` → corridoio della roccaforte (30%); `mining_complex/mining_complex_treasure` → miniera (30%). Dungeons and Taverns `ruin_loot_master`, `hamlet/hamlet_tresure`, `shrine/shrine_lesser_treasure` → dungeon (15%); `desert_ruins/desert_ruin_lesser_treasure` → piramide del deserto (20%); `illager_hideout_lesser_tresure` → avamposto dei predoni (25%). Mowzie's Mobs `monastery_chest` e `umvuthana_grove_chest` → dungeon (15%, prudente). I nomi con "tresure" sono scritti così dalla mod.
- **Letto nei file delle mod** (workflow Esamina mod, 19/10): tutte le tabelle di When Dungeons Arise e Dungeons and Taverns con "vault" nel nome sono di tipo **cassa** (`minecraft:chest`), non ricompense dei blocchi caveau. Una mia affermazione precedente ("le tabelle `vault` non sono casse") era **sbagliata**: per questo erano rimaste fuori anche strutture che hanno come tesoro proprio una tabella "vault".

### Aggiunte il 19/10 (decisione di Matteo)

Quattro strutture di Dungeons and Taverns erano rimaste senza cassa perché il loro tesoro si chiama "vault" (vedi la correzione sopra). Collegate, una cassa per struttura: `nether_keep/vault_keep` e `piglin_donjon/vault_piglin_donjon` → fortezza del Nether (15%); `toxic_lair/toxic_boss_vault` → dungeon (15%); `trident_trial_monument/ttm_boss_vault_trident` → grande rovina sottomarina (45%, come il vecchio nome del monumento). Totale: **152 casse**. Da provare in gioco: che quelle quattro casse esistano davvero nelle strutture e contengano l'artefatto (le tabelle sono di tipo cassa nei file della mod, ma non è stato visto in una struttura generata).

### Escluse di proposito

- **Born in Chaos**: le 7 tabelle (`minecraft:chests/basic_chest`, `chest_level_1`, `chest_level_2`, `chest_level_3`, `farm_drop`, `firewell_d`, `shater`) sono generiche, a livelli, e usano il prefisso `minecraft`. Non so quale struttura usi quale (i file delle strutture non si leggono dall'inventario), e collegarle metterebbe gli artefatti in ogni cassa. Da riconsiderare dopo aver visto le sue strutture in gioco.
- **Tabelle degli overhaul di Dungeons and Taverns** (`minecraft:chests/illager_mansion/…`, `nether_fortress/…`, `village/…`): gli overhaul non sono installati.
- **Barili, casse di cibo e scorte, stanze comuni, campi e villaggi senza un tesoro**: tutto il resto delle tabelle nell'elenco qui sotto.

Elenco generato dall'inventario del pack 0.5.3 (When Dungeons Arise: 141 tabelle di casse; Dungeons and Taverns: 119 in `nova_structures` e 17 in `minecraft`). «Nei file» sono le casse collegate, «Escluse» quelle lasciate fuori.

#### When Dungeons Arise

| Struttura | Nei file | Escluse |
|---|---|---|
| (casse sparse) | `mines_treasure_big`, `mines_treasure_medium`, `mines_treasure_small` | — |
| abandoned_temple | `abandoned_temple_top` | `abandoned_temple_entrance`, `abandoned_temple_map` |
| aviary | `aviary_treasure` | `aviary_barrels`, `aviary_normal` |
| bandit_towers | `bandit_towers_treasure` | `bandit_towers_barrels`, `bandit_towers_gardens`, `bandit_towers_normal`, `bandit_towers_rooms`, `bandit_towers_supply` |
| bandit_village | — | `bandit_village_barrels`, `bandit_village_normal`, `bandit_village_supply`, `bandit_village_tents` |
| bathhouse | — | `bathhouse_barrels`, `bathhouse_normal` |
| ceryneian_hind | `ceryneian_hind_treasure` | — |
| fishing_hut | — | `fishing_hut_barrels` |
| foundry | `foundry_treasure` | `foundry_chains`, `foundry_lava_pit`, `foundry_normal`, `foundry_passage_exterior`, `foundry_passage_normal` |
| greenwood_pub | — | `greenwood_pub_barrels_hallways`, `greenwood_pub_barrels_normal`, `greenwood_pub_normal` |
| heavenly_challenger | `heavenly_challenger_treasure` | `heavenly_challenger_normal`, `heavenly_challenger_supply`, `heavenly_challenger_theater` |
| heavenly_conqueror | `heavenly_conqueror_treasure` | `heavenly_conqueror_barrels`, `heavenly_conqueror_normal` |
| heavenly_rider | `heavenly_rider_treasure` | `heavenly_rider_barrels`, `heavenly_rider_normal` |
| illager_campsite | — | `illager_campsite_map`, `illager_campsite_supply`, `illager_campsite_tent` |
| illager_corsair | `illager_corsair_treasure` | `illager_corsair_barrels`, `illager_corsair_supply` |
| illager_fort | `illager_fort_treasure` | `illager_fort_barrels`, `illager_fort_normal` |
| illager_galley | `illager_galley_treasure` | `illager_galley_barrels`, `illager_galley_supply` |
| illager_windmill | `illager_windmill_treasure` | `illager_windmill_barrels` |
| infested_temple | `infested_temple_top_treasure` | `infested_temple_room_bookshelf`, `infested_temple_room_forge`, `infested_temple_room_garden`, `infested_temple_room_normal`, `infested_temple_room_supply`, `infested_temple_room_table`, `infested_temple_vault_normal`, `infested_temple_vault_ominous`, `infested_temple_vault_treasure` |
| jungle_tree_house | `jungle_tree_house_treasure` | `jungle_tree_house_barrels`, `jungle_tree_house_normal` |
| keep_kayra | `keep_kayra_garden_treasure`, `keep_kayra_library_treasure`, `keep_kayra_treasure` | `keep_kayra_garden_normal`, `keep_kayra_library_normal`, `keep_kayra_normal` |
| kisegi_sanctuary | `kisegi_sanctuary_treasure` | `kisegi_sanctuary_basement`, `kisegi_sanctuary_normal`, `kisegi_sanctuary_top`, `kisegi_sanctuary_vault_normal`, `kisegi_sanctuary_vault_normal_treasure`, `kisegi_sanctuary_vault_ominous`, `kisegi_sanctuary_vault_ominous_treasure` |
| lighthouse | `lighthouse_top` | — |
| mechanical_nest | `mechanical_nest_treasure` | `mechanical_nest_equipment`, `mechanical_nest_normal`, `mechanical_nest_supply` |
| merchant_campsite | — | `merchant_campsite_map`, `merchant_campsite_supply`, `merchant_campsite_tent` |
| mining_complex | `mining_complex_treasure` | `mining_complex_barrel`, `mining_complex_dripstone_normal`, `mining_complex_facility_normal`, `mining_complex_lush_normal` |
| mining_system | `mining_system_treasure` | `mining_system_barrels` |
| monastery | — | `monastery_barrels`, `monastery_bridges`, `monastery_map` |
| mushroom_house | `mushroom_house_treasure` | `mushroom_house_barrels`, `mushroom_house_normal` |
| mushroom_mines | `mushroom_mines_treasure` | `mushroom_mines_barrels`, `mushroom_mines_ores`, `mushroom_mines_tools` |
| mushroom_village | `mushroom_village_treasure` | `mushroom_village_barrels` |
| plague_asylum | `plague_asylum_treasure` | `plague_asylum_barrels`, `plague_asylum_cells`, `plague_asylum_normal`, `plague_asylum_potions`, `plague_asylum_storage` |
| scorched_mines | `scorched_mines_treasure` | `scorched_mines_barrels`, `scorched_mines_housing`, `scorched_mines_hub`, `scorched_mines_normal` |
| shiraz_palace | `shiraz_palace_elite`, `shiraz_palace_treasure` | `shiraz_palace_gardens`, `shiraz_palace_library`, `shiraz_palace_normal`, `shiraz_palace_rooms`, `shiraz_palace_supply`, `shiraz_palace_towers` |
| small_blimp | `small_blimp_treasure` | `small_blimp_coal_storage`, `small_blimp_redstone_chamber` |
| thornborn_towers | `thornborn_towers_top_treasure` | `thornborn_towers_barrels`, `thornborn_towers_rooms`, `thornborn_towers_top_rooms` |
| typhon | `typhon_treasure` | — |
| undead_pirate_ship | `undead_pirate_ship_treasure` | `undead_pirate_ship_barrels`, `undead_pirate_ship_enchants`, `undead_pirate_ship_supply` |

Nelle strutture di When Dungeons Arise con più tabelle «vault» (`infested_temple`, `kisegi_sanctuary`) il tesoro collegato è quello "top" o `_treasure`; le altre `vault_*` sono rimaste fuori perché la struttura è già coperta (una cassa per struttura).

#### Dungeons and Taverns (`nova_structures:chests/`)

| Struttura | Nei file | Escluse |
|---|---|---|
| (casse sparse) | `undead_crypts_grave` | `bunker_altar`, `firewatch_tower`, `food_supply`, `illager_camp`, `mangrove_witchhud`, `mining_supply`, `tavern_quest`, `water_supply` |
| badland_miner_outpost | `badland_miner_outpost` | `badland_miner_outpost_forge`, `badland_miner_outpost_towers` |
| conduit_ruin | `conduit_ruin_main` | `conduit_ruin_big`, `conduit_ruin_small` |
| creeping_crypt | `crypt_grave` | `crypt_hallway`, `vault_creeping` |
| desert_ruins | `desert_ruin_lesser_treasure`, `desert_ruin_main_temple` | `desert_ruin_grave`, `desert_ruin_house` |
| dungeon | `dungeon_1` … `dungeon_7` | — |
| end_castle | `greater_loot`, `treasure_lighthouse`, `vault_brigattine`, `vault_galleon`, `vault_slope` | `castle_bar`, `castle_brewing`, `lesser_loot`, `rocket_barrel`, `supply` |
| end_lighthouse | `vault_lighthouse` | `supply_lighthouse` |
| hamlet | `hamlet_tresure` | `hamlet` |
| illager_hideout | `illager_hideout_lesser_tresure`, `illager_hideout_tresure` | `illager_hideout_brewing`, `illager_hideout_fishing`, `illager_hideout_heart_loot`, `illager_hideout_library`, `illager_hideout_meat`, `illager_hideout_random`, `illager_hideout_raw_ores`, `illager_hideout_trash`, `illager_hideout_utility`, `illager_hideout_vegitarian`, `illager_hideout_weaponry` |
| jungle_ruins | `jungle_ruins_main_temple` | `jungle_ruins_house`, `jungle_ruins_main_temple_wild` |
| lone_citadel | `c_vault`, `c_vault_boss` | `c_banner`, `c_cold_barrel`, `c_dispenser`, `c_forge`, `c_forge_chest`, `c_grave`, `c_library`, `c_supply` |
| nether_keep | `vault_keep` | `vault_keep_generic` |
| nether_port | `nether_port_chest` | `nether_port_supplies` |
| nether_skeleton_tower | `skeleton_tower_chest` | `skeleton_tower_camp`, `skeleton_tower_supply` |
| piglin_camp | — | `chest` |
| piglin_donjon | `vault_piglin_donjon` | `donjon_generic` |
| piglin_outstation | `outstation_treasure` | `outstation_generic`, `outstation_tower`, `vault_piglin_outstation` |
| pillager_outpost | `pillager_outpost_treasure` | `pillager_outpost_kitchen` |
| ruin_loot | `ruin_loot_master` | — |
| shrine | `combat_treasure_1` … `combat_treasure_5`, `shrine_lesser_treasure` | `combat_pot`, `shrine_lesser_ominous`, `vault_shrine_ominous` |
| stray_fort | `stray_fort_tresure` | `stray_fort_archer`, `stray_fort_loot_generic` |
| toxic_lair | `toxic_boss_vault` | `brewing`, `generic`, `kitchen`, `toxic_ominous_vault`, `toxic_vault` |
| trident_trial_monument | `ttm_boss_vault_trident` | `ttm_boss_vault_heart`, `ttm_common_vault` |
| village | — | `village_birch_house` |
| witch_villa | `lab` | `bedroom`, `dirty_clothes`, `gardening`, `general_storage`, `kitchen`, `library`, `music_room`, `potion_brewing`, `pumpkin_room`, `slime_room` |

`piglin_camp/chest`, `illager_camp`, `bunker_altar` e `village_birch_house` sono casse uniche di un campo o di una casa: escluse come i campi e i villaggi di When Dungeons Arise (nessun tesoro).

#### Dungeons and Taverns, overhaul di strutture vanilla (`minecraft:chests/`)

Tutte escluse (overhaul non installati): `illager_mansion/ancient_city_raid_chest`, `illager_mansion/evoker_chest`, `illager_mansion/generic`, `illager_mansion/kitchen`, `illager_mansion/library_chest`, `illager_mansion/map_chest`, `illager_mansion/pillager_chest`, `illager_mansion/ravager_chest`, `illager_mansion/secret_room`, `illager_mansion/smithing_room`, `illager_mansion/vindicator_chest`, `illager_mansion/witch_chest`, `illager_mansion/wool`, `nether_fortress/fort_inside`, `nether_fortress/fort_inside_generic`, `village/village_jungle_house`, `village/village_swamp_house`.

### Altre mod

- **Mowzie's Mobs**: `monastery_chest` (set del Geomante e bastone dello Scultore) e `umvuthana_grove_chest` (maschere degli Umvuthana) sono le uniche casse delle loro strutture: collegate.
- Copertura delle altre mod (Twilight Forest, Unusual End, Supplementaries, YUNG's, Aether, Cataclysm…): nel readme del datapack, livello per livello.

## Abilità come componenti: potenziamenti nel datapack (23/10)

Dal sorgente 13.2.5 (`ochotonida/artifacts` @7cf7dc4) e dal jar del pack; grezzo in `../../ai-agents/archivio/2026-10-23_accessori-evoluzione/`.
- Le abilità di ogni artefatto sono **componenti dei dati dell'oggetto**. Ogni valore è o un rimando alla config o una **costante** (`config/value/type/ValueType.java`, `codec()`: alternativa tra `ConfigValue` e `Value.Constant`). Artifacts le legge **dalla singola copia** (`EquipmentHelper.reduceAbilities`). Quindi una copia con valori fissi è più forte delle altre, e la config non la tocca.
- Esempi di componenti: `artifacts:attribute_modifiers` (lista di `{attribute, amount, operation, id}`, con `id` di serie `artifacts:<oggetto>/<attributo>`, es. `artifacts:power_glove/generic.attack_damage`), `artifacts:enchantment_level_modifiers`, `artifacts:tool_tier_upgrade`.
- Un risultato di ricetta, di infusione (Apothic Enchanting, `apothic_enchanting:infusion`, `result` con componenti; **non** usare `keep_nbt_infusion`, che ricopierebbe i componenti dell'ingresso) o una voce di bottino (`minecraft:set_components`) può portare questi componenti. Per distinguere i livelli: un `minecraft:custom_data` nostro e gli ingredienti `neoforge:components` / `neoforge:difference`.
- Limiti: i valori fissi non seguono più `items.toml`; dopo un aggiornamento di Artifacts i nomi dei componenti vanno ricontrollati (c'è un `TODO (>1.21.1)` nel codice); `scripts/check_ids.py` non controlla i nomi dei componenti.
- **Reliquified Artifacts** (addon di Relics, 1.0.9 beta; verificato nel codice il 23/10, `Octo-Studios/rar-compat` @2b6d624 e `relics` @da846fc):
  - **Versione**: vuole esattamente Artifacts 13.2.5, cioè la nostra, che è anche l'ultima per 1.21.1 NeoForge (Modrinth, 23/10). Il vincolo è per il futuro: un aggiornamento di Artifacts aspetta una Reliquified Artifacts nuova (la 1.0.8 voleva la 13.2.3).
  - Rifà tutti i 48 artefatti con gli stessi nomi, con abilità diverse e livelli.
  - **Config**: annulla del tutto la lettura della config di Artifacts (`ConfigManagerMixin`): valgono i valori di serie, quindi il nostro `enableAccessoriesCompat = false` torna `true`. Non si corregge da config, ma l'effetto sì: gli artefatti finiscono negli slot di Accessories perché il jar di Artifacts mette `#artifacts:slot/*` nelle etichette `accessories:belt`, `hand`, `hat`, `necklace` e `shoes` (inventario). ATM10 lo corregge togliendoli da quelle etichette (changelog 8.1→8.2, #4409); da noi si fa nel datapack con il campo `remove` delle etichette di NeoForge (`TagFile`, verificato nel sorgente). Da provare in gioco.
  - **Casse**: riscrive `artifacts:roll_loot_table` (`RollLootTableModifierMixin`) scartando ogni reliquia, in qualunque tabella. Le nostre 152 casse e le casse vanilla di Artifacts non darebbero più artefatti. **Si corregge**: nei 15 file si cambia il tipo in `neoforge:add_table` (campo `table` al posto di `lootTable`), che fa la stessa cosa e non è toccato dalla mod.
  - **Scavi archeologici** (sorgente @7cf7dc4, letto il 24/10): Artifacts mette un artefatto nel 1/16 (`archaeologyChance`) di 5 tabelle `minecraft:archaeology/*` con `"replace": true`, perché lo scavo dà un oggetto solo. Con Reliquified Artifacts il bottino viene svuotato e l'artefatto scartato: in quel 1/16 lo scavo non dà niente. `neoforge:add_table` non sostituisce; la strada è riscrivere le 5 tabelle vanilla con una voce in più (peso per 1/16) e rendere innocui i 5 modificatori allo stesso percorso (`../lavoro/versioni/v0.7.0.md`).
  - **Bottino di Relics** (riletto nel codice il 24/10, `relics` @a50b42c, 0.12.10; grezzo `../../ai-agents/archivio/2026-10-24_1.21.1-v0.7.0_relics-bottino/`): `RelicLootModifier` aggiunge una reliquia nel **20%** delle casse (`relicGenChance = 0.2`), solo quando a generare il bottino è un giocatore (servono entità e posizione). Vale solo per le tabelle il cui nome è `<mod>:chests/…` (regola `[\w]+:chests\/…` di `LootEntries`): sono **127 delle nostre 152** casse, ma anche tutte le altre `chests/` del pack (563 tabelle nell'inventario, comprese sottotabelle che non si aprono mai da sole), case dei villaggi comprese. **Restano fuori 25 delle nostre**: 14 di Twilight Forest (labirinto, caverne delle colline, roccaforte, torre oscura, palazzo dell'aurora, labirinto di siepi, caverne dei troll: Twilight Forest non usa `chests/`, a parte `tower_room`), 7 di YUNG's Better Dungeons, 2 della nave dell'End (MES), la cassaforte del Galeone, i barili della cittadella di Friends & Foes; e i 5 scavi archeologici di Artifacts.
  - **Better Archeology non è coperta** (inventario, 24/10): le casse delle sue 25 strutture (catacombe, tempio della luce, tempio della giungla, tumulo, motta, rovine…) usano tabelle `betterarcheology:archeology/chest_…`, fuori dalla regola `chests/` di Relics, e non erano nemmeno tra le nostre 152. Oggi lì non escono né reliquie né artefatti (scavi a parte). Decisione di Matteo del 24/10: si aggiungono i tesori alla toppa più avanti, nella versione dell'archeologia, prima della progressione (tema `../theme-knowledge/archeologia.md`).
  - **Quale reliquia**: tra quelle che corrispondono si sceglie a peso. Ogni reliquia ha categorie scritte nel codice (`LootEntries`): per nome della cassa (villaggio, miniera, bastione, nomi «infernali», End e roccaforte: peso 500), per bioma (deserto, foresta, oceano, grotta…: 300), per dimensione (Overworld, Nether, End, e una valida ovunque: 100). Delle nostre 127, 105 non hanno un nome riconosciuto: decidono bioma e dimensione. Reliquified Artifacts dà categorie a 46 artefatti su 48; Relics ne aggiunge 20 sue. In Aether, Undergarden, Twilight Forest e Otherside escono solo le reliquie dei biomi con un nome riconosciuto (foresta, prato, palude, ghiacciaio…) o quella valida ovunque (Experience Disperser di Relics).
  - **Config**: probabilità, casse, biomi e pesi di ogni reliquia (anche con espressioni regolari) si cambiano solo con `enabledExtendedConfigs = true` nella config di Relics (segnata come «WIP» e non aggiornata in automatico quando la mod cambia): crea `relics/loot` (con `relicGenChance`) e un file per ogni reliquia. Nome ed estensione dei file: da vedere in gioco (in Craftoria: `config/relics.yaml`, `config/relics/loot.yaml`). **Senza config estesa** la probabilità si abbassa riscrivendo nel datapack `data/relics/loot_modifiers/relic_loot.json` con la condizione `minecraft:random_chance` (NeoForge controlla le condizioni di un modificatore prima di applicarlo, `LootModifier.apply`): `0.5` → 10%. Scelta del 24/10: strada A (`../lavoro/versioni/v0.7.0.md`).
  - **Nel pack dalla 0.7.0** (decisione di Matteo del 24/10, `../lavoro/versioni/v0.7.0.md`): Relics 0.12.9, Reliquified Artifacts 1.0.9, ShatterLib/OctoLib 0.6.2. Dall'inventario: Reliquified Artifacts riscrive le tabelle `artifacts:entities/mimic` e `artifacts:entity_equipment/*` (mostri con gli artefatti addosso), sposta 7 artefatti nello slot `charm` e 2 in `bracelet` di Curios; Relics aggiunge gli slot `back`, `charm`, `ring`, `belt`… e il modificatore `relics:relic_loot` (più `relics:greed_loot`).

