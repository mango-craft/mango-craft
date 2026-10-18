# Pacchetto Modrinth `modpack-matteo-0.2.3.mrpack`

> **Documento storico**: fotografia del momento in cui è stato scritto, non si aggiorna. Lo stato attuale è nei documenti vivi (vedi il README della cartella).

_Generato il 16/10/2026, aggiornato il 17/10/2026 · Minecraft 1.21.1 · **NeoForge 21.1.259** · Prism Launcher (Aggiungi istanza → Importa)_

**0.2.3** (17/10/2026): aggiunte Just Enough Breeding, Just Enough Professions, NetherPortalFix, SeasonHud, Smarter Farmers e Open Together; nessuna libreria nuova (Balm, Moonlight, Puzzles Lib e JEI c'erano già). AllTheLeaks è solo CurseForge: va nella lista qui sotto.

**0.2.2** (17/10/2026): aggiunto XP Tome.

**0.2.1** (17/10/2026): datapack con la cassaforte del Galeone di Supplementaries tra le casse con artefatti; mod identiche alla 0.2.0.

**0.2.0** (17/10/2026): aggiunti Regions Unexplored, Chunky, Clumps, Supplementaries, Handcrafted, Rechiseled, Construction Sticks e le librerie Lithostitched, Fusion, Moonlight (204 file, 700 MB).

**0.1.1**: NeoForge da 21.1.262 a 21.1.259 (con la 21.1.261+ owo-lib 0.12.15.5 fa cadere la connessione all'ingresso nel mondo); file di spiegazione dentro `data/` rinominati `readme.md`. Le mod sono identiche alla 0.1.0.

**211 file** scaricati da Prism (172 mod e resource pack del pack + 39 librerie), **701 MB**. Ogni file ha versione esatta e codici di controllo verificati uno per uno sull'API di Modrinth (ricerca per sha512). Dentro c'è anche la cartella `config` del pack (`tags.json`, `sparsestructures.json5`, datapack `matteo_tweaks` con i README).

## Da aggiungere a mano in Prism (solo CurseForge)

| Mod | Versione | Note |
|---|---|---|
| The Twilight Forest | 4.8.3345 | Senza, il gioco non parte: Twilight's Flavor & Delight la richiede |
| Ars Elemental | 0.7.10.4 | |
| Roaster's Delight | 1.0.0.1 | |
| Spice of Life: Carrot Edition | 1.16.6 | |
| BotanyPotsAdditions | 1.1.0 | Richiede NeoForge ≥ 21.1.229 (il pacchetto usa 21.1.259) |
| AllTheLeaks | 1.1.13 | File `alltheleaks-1.1.13+1.21.1-neoforge.jar` (22/9/2026), MIT. Richiede solo NeoForge; dalla tab CurseForge di Prism o trascinando il .jar |

## Note di generazione

- **Accessories** non è nel pacchetto come file a sé: su Modrinth nessuna mod del pack la dichiara obbligatoria (Hexalia la dichiara facoltativa). Al primo avvio si vedrà se arriva incorporata in qualche mod, per esempio l'Aether; da questo dipende se il test Miapi + Accessories (3.2) serve ancora
- **Fabric API** esclusa di proposito: LambDynamicLights la dichiara solo per la versione Fabric; nel pack c'è Forgified Fabric API
- **Ars Creo** dichiara su Modrinth una dipendenza verso un progetto che non esiste più (`cC0JkO8i`); il suo file `neoforge.mods.toml` richiede solo Ars Nouveau e Create: ignorata
- **Cloth Config** aggiunta perché richiesta da Cristel Lib (Towns and Towers)
- **Librerie solo beta** per NeoForge 1.21.1: owo-lib (Aether), TerraBlender (Deep Aether), GlitchCore (Serene Seasons)
- Fresh Animations viene scaricato in `resourcepacks/` ma va attivato a mano nel gioco

## Mod e resource pack

| Nome | Versione | Tipo |
|---|---|---|
| [Let's Do] Farm & Charm | `1.1.28` | release |
| [Let's Do] HerbalBrews | `1.1.4` | release |
| [Let's Do] Meadow | `1.4.9` | release |
| [Let's Do] Vinery | `1.5.5` | release |
| Aether's Delight | `0.1.4.2` | beta |
| Akashic Tome | `1.21.1-1.8-30` | release |
| AlmostUnified | `1.21.1-1.4.2+neoforge` | release |
| AmbientSounds | `6.3.10` | release |
| Animal Feeding Trough | `1.1.2+1.21(.1)-neoforge` | release |
| Animal Pens | `2.5.0-1.21` | release |
| Apotheosis | `1.21.1-8.9.0` | release |
| Apothic Attributes (modulo) | `1.21.1-2.11.0` | release |
| Apothic Enchanting (modulo) | `1.21.1-1.6.4` | release |
| Apothic Spawners (modulo) | `1.21.1-1.4.0` | release |
| AppleSkin | `3.0.9+mc1.21` | release |
| Ars Controle | `1.6.16` | release |
| Ars Creo | `5.4.0` | release |
| Ars Delight (Flavors & Delight) | `2.2.5` | release |
| Ars Mekanica | `1.3.0+neoforge-1.21.1` | release |
| Ars Nouveau | `5.13.3` | release |
| Ars Ocultas | `1.21.1-2.6.1` | release |
| Ars QOL | `1.2.1` | release |
| Ars Unification | `1.2.19` | release |
| Artifacts | `13.2.5` | release |
| Aspect Alchemy | `2.0.0` | release |
| Born in Chaos | `1.7.6` | release |
| Born In Configuration | `4.0` | release |
| Botany Pots | `21.1.44` | release |
| Botany Pots Tiers | `7.0.11` | release |
| Botany Trees | `21.1.7` | release |
| Bountiful Fares | `3.0.12` | release |
| Brewin' And Chewin' | `4.5.0+1.21.1-neoforge` | release |
| Carry On | `2.2.6` | release |
| Cataclysm Delight | `1.21.1-1.0.10b` | release |
| Chunk Loaders | `1.2.9-neoforge-mc1.21` | release |
| Chunky | `1.4.23` | release |
| Clumps | `19.0.0.1` | release |
| Comforts | `9.0.5+1.21.1` | release |
| Compass to Map: Xaero's | `0.1.2+neoforge-1.21.1` | release |
| Construction Sticks | `1.5.0` | release |
| Controlling | `19.0.5` | release |
| Corail Tombstone | `neoforge-1.21.1-9.5.6` | release |
| Crafting Tweaks | `21.1.11+neoforge-1.21.1` | release |
| Create | `6.0.10+mc1.21.1` | release |
| Create Crafts & Additions | `neoforge-1.21.1-1.6.0` | release |
| Create Slice & Dice | `4.3.4` | release |
| Create: Central Kitchen | `2.6.2b` | release |
| Create: Connected | `1.3.3-mc1.21.1` | release |
| Create: Dragons Plus (dipendenza) | `1.11.9` | release |
| Create: Enchantment Industry | `2.4.2` | release |
| Create: Integrated Farming | `1.4.3` | release |
| Cultural Delights | `0.19.1-1.21.1` | release |
| Deep Aether | `1.21.1-1.1.5.1` | release |
| Deeper and Darker | `1.4.1-neoforge-1.21.1` | release |
| Delightful Fares | `1.1.2` | release |
| Dungeons and Taverns | `v4.4.4+mod` | release |
| Easy Auto Cycler | `3.1.0` | release |
| Easy Villagers | `neoforge-1.21.1-1.1.47` | release |
| EMI | `1.1.24+1.21.1+neoforge` | release |
| EMI Loot | `0.7.9+1.21+neoforge` | release |
| EMI Ores | `1.3+1.21.1+neoforge` | release |
| Enchantment Descriptions | `21.1.11` | release |
| Ender Dragon Fight Remastered | `5.0.2+mod` | release |
| Ender Storage | `2.13.0.191` | release |
| Ender's Delight | `1.3.1` | release |
| Enhanced Celestials | `6.0.2.6-neoforge` | release |
| Entity Culling | `1.11.3` | release |
| Entity Model Features (EMF) | `3.3.12-neoforge-1.21` | release |
| Entity Texture Features (ETF) | `7.2.5-neoforge-1.21` | release |
| Expanded Delight | `0.1.4-neoforge` | beta |
| Explorer's Compass | `1.21.1-3.4.0-neoforge` | release |
| FallingTree | `1.21.1-1.21.1.11` | release |
| Farmer's Delight | `1.21.1-1.3.4` | release |
| Farmer's Delight: Extended | `1.21.1-0.2.2` | release |
| FerriteCore | `7.0.3-neoforge` | release |
| Forgified Fabric API | `0.116.15+2.3.5+1.21.1` | release |
| Fresh Animations (resource pack) | `1.10.4` | beta |
| Friends & Foes | `neoforge-5.0.2+mc1.21.1` | release |
| Gateways to Eternity | `1.21.1-5.1.0` | release |
| Handcrafted | `4.0.3` | release |
| Hexalia | `1.3.6` | release |
| Hexerei | `0.5.0.3` | release |
| Illager Invasion | `v21.1.6-1.21.1-NeoForge` | release |
| ImmediatelyFast | `1.6.14+1.21.1-neoforge` | release |
| Inventory Essentials | `21.1.20+neoforge-1.21.1` | release |
| Jade | `15.10.6+neoforge` | release |
| JEI | `19.51.0.418` | release |
| Just Enough Breeding (JEBr) | `3.3.1` | release |
| Just Enough Professions (JEP) | `4.0.5` | release |
| L_Ender's Cataclysm | `3.33` | release |
| LambDynamicLights | `4.8.11+1.21.1` | release |
| Leaves Be Gone | `v21.1.1-1.21.1-NeoForge` | release |
| Let's Do Addon Compat | `2.3.1-neoforge` | release |
| Lithium | `mc1.21.1-0.15.4-neoforge` | release |
| Mekanism | `10.7.19.85` | release |
| Mekanism Generators | `10.7.19.85` | release |
| Mekanism: Ponders | `1.0.3-1.21.1` | release |
| ModernFix | `5.27.26+mc1.21.1` | release |
| Moog's End Structures (MES) | `2.1.1` | release |
| Mouse Tweaks | `1.21-2.26.1-neoforge` | release |
| Mowzie's Mobs | `1.8.2` | release |
| Mutant Monsters | `v21.1.1-1.21.1-NeoForge` | release |
| NetherPortalFix | `21.1.1+neoforge-1.21.1` | release |
| Not Enough Animations | `1.12.6` | release |
| Not Enough Glyphs | `4.6.1` | release |
| Occult Delight | `1.0.0` | release |
| Occultism | `1.21.1-neoforge-1.224.5` | release |
| OmniTools (Omni Wrench) | `1.21.1-1.2.1` | release |
| Open Together | `21.1.2` | release |
| Particle Rain | `v4.0.1+1.21.1-neoforge` | release |
| Paxi | `1.21.1-NeoForge-5.1.3` | release |
| Pick Up Notifier | `v21.1.1-1.21.1-NeoForge` | release |
| Pipez | `neoforge-1.21.1-1.2.31` | beta |
| Polymorph | `1.1.0+1.21.1` | release |
| Psi | `1.21.1-110-neoforge` | release |
| Reactive Alchemy | `1.21.1-10.2.1` | release |
| Rechiseled | `1.2.6-neoforge-mc1.21` | release |
| Regions Unexplored | `0.6.2-neoforge-21.1` | release |
| RightClickHarvest | `4.6.1+1.21.1` | release |
| Scriptor Magicae | `2.0.14-1.21.1-neoforge` | release |
| Seasonal Let's Do | `1.5.0+1.21` | release |
| SeasonHud | `1.21.1-2.0.10` | release |
| Serene Seasons | `10.1.0.9` | beta |
| Shoulder Surfing Reloaded | `1.21.1-5.2.0+neoforge` | release |
| Simple Backups | `1.21-4.0.21` | release |
| Smarter Farmers (farmers replant) | `1.21-2.2.4` | release |
| Snow! Real Magic! | `12.2.3+neoforge` | release |
| Sodium | `mc1.21.1-0.8.13-neoforge` | release |
| Sophisticated Backpacks | `1.21.1-3.26.12.2208` | release |
| Sophisticated Backpacks Create Integration | `1.21.1-0.2.0.168` | release |
| Sophisticated Core (dipendenza) | `1.21.1-1.5.13.2404` | release |
| Sound Physics Remastered | `neoforge-1.21.1-1.5.1` | alpha |
| Sparse Structures | `3.0` | release |
| Starcatcher | `3.3.6-NEOFORGE-1.21.1` | release |
| Starcatcher's Delight | `3.2-NEOFORGE-1.21.1` | release |
| Storage Drawers | `1.21.1-13.11.4` | release |
| Structure Layout Optimizer | `1.0.12+1.21.1-neoforge` | release |
| Subtle Effects | `1.15.0` | release |
| Supplementaries | `1.21.1-4.0.2` | release |
| The Aether | `1.21.1-1.5.10-neoforge` | release |
| The Undergarden | `0.9.6` | beta |
| Tom's Simple Storage | `1.21-2.4.2` | release |
| Torchmaster | `21.1.13-release` | release |
| Towns and Towers | `1.13.11` | release |
| Traveler's Backpack | `1.21.1-10.1.39` | release |
| Travelers Titles | `1.21.1-NeoForge-5.1.3` | release |
| Truly Modular: Archery | `2.2-1.21-neoforge` | release |
| Truly Modular: Armory | `2.2-1.21-neoforge` | release |
| Truly Modular: Arsenal | `2.4-1.21-neoforge` | release |
| Truly Modular: Modular Item API (Miapi) | `2.3.9-1.21-neoforge` | release |
| Twilight's Flavor & Delight | `3.2.6` | release |
| Undergarden Delight | `2.0.2` | release |
| Unusual End | `2.3.1b-neo` | release |
| Veggies Delight | `1.9.3` | release |
| Waystones | `21.1.46+neoforge-1.21.1` | release |
| When Dungeons Arise | `2.1.68` | release |
| Xaero's Minimap | `neoforge-1.21.1-26.6.0` | release |
| Xaero's Minimap & World Map - Waystones Compatibility | `2.1.0` | release |
| Xaero's World Map | `neoforge-1.21.1-1.47.0` | release |
| XP Tome | `v2.4` | release |
| YUNG's Better Desert Temples | `1.21.1-NeoForge-4.1.5` | release |
| YUNG's Better Dungeons | `1.21.1-NeoForge-5.1.4` | release |
| YUNG's Better End Island | `1.21.1-NeoForge-3.1.2` | release |
| YUNG's Better Jungle Temples | `1.21.1-NeoForge-3.1.2` | release |
| YUNG's Better Mineshafts | `1.21.1-NeoForge-5.1.1` | release |
| YUNG's Better Nether Fortresses | `1.21.1-NeoForge-3.1.5` | release |
| YUNG's Better Ocean Monuments | `1.21.1-NeoForge-4.1.2` | release |
| YUNG's Better Strongholds | `1.21.1-NeoForge-5.1.3` | release |
| YUNG's Better Witch Huts | `1.21.1-NeoForge-4.1.1` | release |
| YUNG's Bridges | `1.21.1-NeoForge-5.1.1` | release |
| YUNG's Extras | `1.21.1-NeoForge-5.1.1` | release |
| YUNG's Menu Tweaks | `1.21.1-NeoForge-2.1.2` | release |

## Librerie (dipendenze)

| Nome | Versione | Tipo | Richiesta da |
|---|---|---|---|
| Architectury API | `13.0.11+neoforge` | release | lets-do-meadow, truly-modular-arsenal, lets-do-herbalbrews, lets-do-farm-charm… |
| Balm | `21.0.66+neoforge-1.21.1` | release | inventory-essentials, crafting-tweaks, waystones |
| Blueprint | `8.2.0` | release | unusual_end |
| Bookshelf | `21.1.81` | release | botany-pots, botany-trees, botany-pots-tiers, enchantment-descriptions |
| Caelus API | `7.0.1+1.21.1` | release | truly-modular-arsenal, truly-modular-archery, truly-modular-armory, modular-item-api |
| Cloth Config API | `15.0.140+neoforge` | release | cristel-lib |
| CodeChicken Lib | `4.6.1.529` | release | ender-storage |
| CorgiLib | `1.21.1-5.0.0.9-NeoForge` | release | enhanced-celestials |
| CreativeCore | `2.13.51` | release | ambientsounds |
| Cristel Lib | `neoforge-1.21.1-3.1.7` | release | towns-and-towers |
| Curios API | `9.5.1+1.21.1` | release | occultism, l_enders-cataclysm, ars-controle |
| Data Anchor | `2.0.0.14-neoforge` | release | enhanced-celestials |
| Fusion (Connected Textures) | `1.3.16-neoforge-mc1.21.1` | release | rechiseled |
| Fzzy Config | `0.7.7+1.21+neoforge` | release | subtle-effects, emi-loot |
| Geckolib | `4.9.3` | release | borninchaos, occultism, hexalia, mowzies-mobs |
| GlitchCore | `2.1.0.2` | beta | serene-seasons |
| JamLib | `1.3.6+1.21.1` | release | rightclickharvest |
| Kiwi 🥝 | `15.8.7+neoforge` | release | snow-real-magic |
| Kotlin for Forge | `5.12.0` | release | slice-and-dice |
| Lionfish-API | `3.1` | release | l_enders-cataclysm |
| Lithostitched | `1.8.1-neoforge-21.1` | release | regions-unexplored |
| Modonomicon | `1.21.1-1.120.7` | release | occultism |
| Moog's Structure Lib (moogs_structures) | `3.0.3` | release | mes-moogs-end-structures |
| Moonlight Lib | `1.21.1-3.7.2` | release | supplementaries |
| NexusLib | `1.2.0` | release | bountiful-fares |
| oωo (owo-lib) | `0.12.15.5-beta.1+1.21` | beta | aether |
| Patchouli | `1.21.1-93-neoforge` | release | apotheosis, psi, aspect-alchemy |
| Placebo | `1.21.1-9.9.4` | release | apotheosis, apothic-attributes, apothic-spawners, apothic-enchanting… |
| Prickle | `21.1.11` | release | botany-pots, botany-trees, botany-pots-tiers, enchantment-descriptions |
| Puzzles Lib | `21.1.64` | release | mutant-monsters, illager-invasion, leaves-be-gone, pick-up-notifier |
| Resourceful Config | `3.0.11` | release | structure-layout-optimizer |
| Resourceful Lib | `3.0.12` | release | friends-and-foes-forge |
| Searchables | `1.0.2` | release | controlling |
| SmartBrainLib | `1.16.11` | release | occultism |
| SuperMartijn642's Config Lib | `1.1.8-neoforge-mc1.21` | release | chunk-loaders |
| SuperMartijn642's Core Lib | `1.1.24-neoforge-mc1.21` | release | chunk-loaders |
| TerraBlender | `4.1.0.8` | beta | deep-aether |
| Unfocused | `0.3.10-1.21.1-neoforge` | release | JyJgaOrk |
| YUNG's API | `1.21.1-NeoForge-5.1.9` | release | yungs-better-mineshafts, yungs-extras, travelers-titles, paxi… |

---

## Installazione a mano (fino al 17/10/2026)

Prima del repository il pack si installava importando il `.mrpack` in Prism e aggiungendo a mano le mod solo CurseForge (dal vecchio `context.md`, sezione 3.1).

**Distribuzione**: dal 18/10/2026 il pack si installa dal repository `mango-craft` con packwiz (istruzioni nel `README.md` e in `../../docs/0101-installazione.md`). Storico: l'ultimo pacchetto .mrpack è stato `modpack-matteo-0.2.3.mrpack` (17/10/2026; 211 file, 701 MB, **NeoForge 21.1.259** — vedi sotto perché non la 21.1.262; contenuto e note all'inizio di questo documento). In Prism: Aggiungi istanza → Importa → scegliere il file. Poi aggiungere a mano le 6 mod solo CurseForge (Twilight Forest, Ars Elemental, Roaster's Delight, Spice of Life: Carrot Edition, BotanyPotsAdditions, AllTheLeaks). I passi qui sotto restano validi per aggiunte singole. Prism è installato in versione portable sul PC dell'utente: non toccare la sua cartella senza il suo via.

1. Aggiungi istanza → Minecraft **1.21.1** → loader **NeoForge** (ultima 21.1.x, almeno 21.1.229)
2. Impostazioni → Java → **8 GB** di memoria. Assegnarne troppa non aiuta e può allungare le pause del garbage collector
3. Modifica istanza → Mod → Scarica mod (Modrinth / CurseForge), filtrando per NeoForge 1.21.1
4. Installare **a blocchi**, con un avvio di prova dopo ogni blocco: base tecnica + comodità + atmosfera → cucina + Botany Pots → natura → tech e storage → equipaggiamento → strutture → dimensioni → boss e nemici
5. Attenzioni in fase di download:
   - **YUNG's**: usare i progetti marcati **"(NeoForge) [1.20.4 - 1.21.1 ONLY]"**
   - **Dungeons and Taverns**: solo la mod base, **senza** i pacchetti overhaul
   - **Forgified Fabric API**: installarla sempre, fin dal primo blocco (con la base tecnica)
6. Datapack (es. quelli generati da Botany Pots): copiarli nella cartella `datapacks` del mondo, poi `/reload`
7. Dopo aver aggiunto mod di strutture o dimensioni: **creare un mondo nuovo**
8. **Backup del mondo** prima di ogni aggiornamento delle mod

## File di config pronti (16/10/2026)

**File pronti (16/10/2026)** — pacchetto `modpack-config.zip` + documento di progetto `file-di-configurazione.md` (contenuto completo dei file). Il datapack ha un `README.md` in ogni cartella con la spiegazione dei file (i `.json` non accettano commenti; il gioco ignora i `.md`). Vanno copiati nella cartella `minecraft/config` dell'istanza:

| File | Contenuto | Stato |
|---|---|---|
| `config/almostunified/tags.json` | 19 tag personalizzati: farina, impasto di grano, sale, mais, limone, porzioni di formaggio, formaggio di capra intercambiabili tra le mod (ogni oggetto aggiunto a tutti i tag che le ricette usano, perché AlmostUnified lavora sui tag già risolti) | ✅ pronto |
| `config/sparsestructures.json5` | Fattore generale 1.4; villaggi 1; magione 2 | ⚠️ da completare con i nomi dei gruppi di Dungeons and Taverns (Witch Villa e Swamp Village → fattore **3**, scelta dell'utente: tenerle ma molto più rare) e When Dungeons Arise (→ 2), letti in gioco con `/dumpstructuresets` |
| `config/paxi/datapacks/matteo_tweaks/` | Datapack: luna di sangue **5%** delle notti e mostri **×2**; super luna di sangue **×4** (frequenza invariata: 5% delle lune piene, almeno 20 notti di distanza; copie complete dei file di Enhanced Celestials 6.x). **Artefatti** nelle casse delle strutture modded: 15 modificatori `artifacts:roll_loot_table` (153 tabelle, compresa la cassaforte del Galeone di Supplementaries), uno per livello di bottino vanilla, attivi solo se Artifacts è caricata. **Ars in Botany Pots**: Magebloom, Sourceberry, 5 frutti di archwood sui tronchi | ✅ pronto · ⚠️ artefatti da completare per Mowzie's e Born in Chaos (oggi bug B03) |
