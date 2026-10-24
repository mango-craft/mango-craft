# Distinta delle mod — Minecraft 1.21.1

_Documento vivo: versione, data ed esito della verifica di ogni file del pack (nata come verifica formale del 16/10/2026). Ogni mod aggiunta riceve qui la sua riga; ruolo e licenza sono in `0301-mod.md` (per le librerie, che lì hanno solo il nome, la licenza sta nelle note qui). La versione installata davvero è quella del metafile in `../pack/mods/`: quando una mod si aggiorna, si aggiorna la sua riga qui._

_Controllo formale del 16/10/2026 · fonte: API di Modrinth (filtro `loaders=neoforge`, `game_versions=1.21.1`), CurseForge per le mod che stanno solo lì_

**Risultato: 148 voci controllate (142 mod + 1 resource pack + 5 dipendenze/moduli) — ✅ 119 · ⚠️ 29 · ❌ 0.**
Nessuna mod è senza versione NeoForge 1.21.1. Tutti i progetti sono quelli degli autori originali (salvo gli addon di terzi segnalati).

Legenda esito: ✅ build release ufficiale · ⚠️ build ufficiale ma solo beta/alpha oppure ferma a prima di metà 2025 · ❌ nessuna build.
"MR" = Modrinth, "CF" = CurseForge. La colonna Progetto riporta lo slug esatto, utile per non prendere progetti omonimi in Prism.

## Correzioni emerse dalla verifica

- **Sodium Dynamic Lights → LambDynamicLights**: la prima era un port non ufficiale fermo a gennaio 2025; LambDynamicLights è l'originale, con build NeoForge 1.21.1 (4.8.11, agosto 2026). Le due sono incompatibili tra loro.
- **Enhanced Celestials**: scelta la mod originale (6.0.2.6), che include già lune di sangue e del raccolto. Sostituita dalla 0.5.1 con Enhanced Celestials 2 (Core + Default Lunar Events), il suo seguito ufficiale (`../lavoro/versioni/v0.5.1.md`).
- **Versioni aggiornate**: Sodium 0.8.13 · Apotheosis 8.9.0 · Truly Modular (Miapi) 2.3.9 · HerbalBrews 1.1.4 · BotanyPotsAdditions 1.1.0 · Animal Pens 2.5.0 · Easy Villagers 1.1.47.
- **Release da fissare** (le versioni più nuove sono beta): Create Crafts & Additions 1.6.0 · Create: Enchantment Industry 2.4.2 · Simple Backups 4.0.21 · JEI 19.51.0.418 · Polymorph 1.1.0.
- **Create 6.0.10**: tutti gli addon Create verificati sono compilati per questa versione.

## Avvisi ⚠️ in breve

- **Solo beta/alpha, ma è l'abitudine dell'autore o la mod è dichiaratamente in beta**: Serene Seasons, Pipez, Sound Physics Remastered, The Undergarden, Expanded Delight, Aether's Delight, Fresh Animations. Si usano lo stesso.
- **Ramo 1.21.1 concluso** (ultima build tra il 2024 e metà 2025, nessuna più recente da nessuna parte): tutta la serie YUNG's, Dungeons and Taverns, Sparse Structures, Hexerei, Ender Storage, Illager Invasion, Mouse Tweaks, Controlling, Pick Up Notifier, Travelers Titles, Animal Feeding Trough. Sono build stabili e definitive, rischio basso.

## Da sapere quando si cercano le mod

- **Solo su CurseForge** (le scarica packwiz-installer; quelle bloccate vanno scaricate a mano): The Twilight Forest, Roaster's Delight, Spice of Life: Carrot Edition, BotanyPotsAdditions, Ars Elemental, AllTheLeaks (dalla 0.2.3), Goblin Traders e la sua libreria Framework (dalla 0.4.0)
- **Slug da non sbagliare**: Friends & Foes → `friends-and-foes-forge` · Create Slice & Dice → `slice-and-dice` · Deeper and Darker → `deeperdarker` · Unusual End → `unusual_end` · Moog's End Structures → `mes-moogs-end-structures` · Born in Chaos → `borninchaos`. Evitare i progetti omonimi non ufficiali (ImmediatelyFast "Reforged", Entity Culling di altri autori, Compass to Map per JourneyMap)
- **NeoForge**: almeno 21.1.229 (richiesto da BotanyPotsAdditions; il controllo dei nomi verifica da solo le richieste di ogni mod). Versione usata: changelog; perché è ferma: `0303-note-tecniche.md`

## Tabella completa

### Cucina e bevande

| Mod | Progetto | Versione NeoForge 1.21.1 | Data | Tipo | Esito | Note |
|---|---|---|---|---|---|---|
| Farmer's Delight | [`farmers-delight`](https://modrinth.com/mod/farmers-delight) MR | 1.21.1-1.3.4 | 2026-08-29 | release | ✅ |  |
| Brewin' And Chewin' | [`brewin-and-chewin`](https://modrinth.com/mod/brewin-and-chewin) MR | 4.5.0+1.21.1-neoforge | 2026-06-24 | release | ✅ |  |
| Ender's Delight | [`enders-delight`](https://modrinth.com/mod/enders-delight) MR | 1.3.1 | 2026-08-03 | release | ✅ |  |
| Veggies Delight | [`veggies-delight`](https://modrinth.com/mod/veggies-delight) MR | 1.9.3 | 2026-07-22 | release | ✅ |  |
| Expanded Delight | [`expanded-delight`](https://modrinth.com/mod/expanded-delight) MR | 0.1.4-neoforge | 2026-01-10 | beta | ⚠️ | Tutte le build 1.21.1 sono beta; mod molto usata |
| Cultural Delights | [`cultural-delights`](https://modrinth.com/mod/cultural-delights) MR | 0.19.1-1.21.1 | 2026-10-11 | release | ✅ |  |
| Farmer's Delight: Extended | [`farmers-delight-extended`](https://modrinth.com/mod/farmers-delight-extended) MR | 1.21.1-0.2.2 | 2025-12-04 | release | ✅ |  |
| Create Slice & Dice | [`slice-and-dice`](https://modrinth.com/mod/slice-and-dice) MR | 4.3.4 | 2026-09-20 | release | ✅ |  |
| Create: Central Kitchen | [`create-central-kitchen`](https://modrinth.com/mod/create-central-kitchen) MR | 2.6.2b | 2026-10-09 | release | ✅ | Compilata per Create 6.0.10 |
| [Let's Do] HerbalBrews | [`lets-do-herbalbrews`](https://modrinth.com/mod/lets-do-herbalbrews) MR | 1.1.4 | 2026-09-19 | release | ✅ |  |
| Roaster's Delight | [`roasters-delight`](https://www.curseforge.com/minecraft/mc-mods/roasters-delight) CF | roasters_delight-1.0.0.1 | 2026-10-03 | release | ✅ | Solo CurseForge; progetto di due settimane |
| Delightful Fares | [`delightful-fares`](https://modrinth.com/mod/delightful-fares) MR | 1.1.2 | 2026-06-13 | release | ✅ |  |
| Twilight's Flavor & Delight | [`twilight-delight`](https://modrinth.com/mod/twilight-delight) MR | 3.2.6 | 2026-10-09 | release | ✅ |  |
| Undergarden Delight | [`undergarden-delight`](https://modrinth.com/mod/undergarden-delight) MR | 2.0.2 | 2026-07-09 | release | ✅ |  |
| Cataclysm Delight | [`l_enders-cataclysm-delight`](https://modrinth.com/mod/l_enders-cataclysm-delight) MR | 1.21.1-1.0.10b | 2026-06-11 | release | ✅ |  |
| Starcatcher's Delight | [`starcatchers-delight`](https://modrinth.com/mod/starcatchers-delight) MR | 3.2-NEOFORGE-1.21.1 | 2026-09-16 | release | ✅ |  |
| Aether's Delight | [`the-aethers-delight`](https://modrinth.com/mod/the-aethers-delight) MR | 0.1.4.2 | 2025-10-27 | beta | ⚠️ | Solo beta, ultima di ottobre 2025; legata all'Aether |
| Spice of Life: Carrot Edition | [`spice-of-life-carrot-edition`](https://www.curseforge.com/minecraft/mc-mods/spice-of-life-carrot-edition) CF | solcarrot-1.21.1-1.16.6 | 2025-12-24 | release | ✅ | Solo CurseForge |

### Botany Pots

| Mod | Progetto | Versione NeoForge 1.21.1 | Data | Tipo | Esito | Note |
|---|---|---|---|---|---|---|
| Botany Pots | [`botany-pots`](https://modrinth.com/mod/botany-pots) MR | 21.1.44 | 2026-06-13 | release | ✅ |  |
| Botany Trees | [`botany-trees`](https://modrinth.com/mod/botany-trees) MR | 21.1.7 | 2026-06-02 | release | ✅ |  |
| Botany Pots Tiers | [`botany-pots-tiers`](https://modrinth.com/mod/botany-pots-tiers) MR | 7.0.11 | 2026-04-05 | release | ✅ |  |
| BotanyPotsAdditions | [`botanypotsadditions`](https://www.curseforge.com/minecraft/mc-mods/botanypotsadditions) CF | botanypotsadditions-1.1.0 | 2026-10-14 | release | ✅ | Solo CurseForge; richiede NeoForge ≥ 21.1.229 e Botany Pots ≥ 21.1.42 |

### Natura, erbe e pozioni

| Mod | Progetto | Versione NeoForge 1.21.1 | Data | Tipo | Esito | Note |
|---|---|---|---|---|---|---|
| Hexalia | [`hexalia`](https://modrinth.com/mod/hexalia) MR | 1.3.6 | 2026-08-16 | release | ✅ |  |
| Hexerei | [`hexerei`](https://modrinth.com/mod/hexerei) MR | 0.5.0.3 | 2025-04-02 | release (beta su CF) | ⚠️ | Ultima build di aprile 2025; CurseForge la segna beta |
| ~~Toil and Trouble~~ | [`toil-and-trouble`](https://modrinth.com/mod/toil-and-trouble) MR | 1.4.3+1.21.1 | 2025-11-03 | release | ✅ | Tolta dal pack il 16/10/2026 (doppione di Hexerei) |
| Aspect Alchemy | [`aspect-alchemy`](https://modrinth.com/mod/aspect-alchemy) MR | 2.0.0 | 2026-05-04 | release | ✅ |  |
| Bountiful Fares | [`bountiful-fares`](https://modrinth.com/mod/bountiful-fares) MR | 3.0.12 | 2026-08-19 | release | ✅ |  |
| [Let's Do] Vinery | [`lets-do-vinery`](https://modrinth.com/mod/lets-do-vinery) MR | 1.5.5 | 2026-10-07 | release | ✅ |  |
| [Let's Do] Meadow | [`lets-do-meadow`](https://modrinth.com/mod/lets-do-meadow) MR | 1.4.9 | 2026-09-18 | release | ✅ |  |
| [Let's Do] Farm & Charm | [`lets-do-farm-charm`](https://modrinth.com/mod/lets-do-farm-charm) MR | 1.1.28 | 2026-10-12 | release | ✅ |  |
| Seasonal Let's Do | [`seasonal-lets-do`](https://modrinth.com/mod/seasonal-lets-do) MR | 1.5.0+1.21 | 2026-04-06 | release | ✅ |  |
| Let's Do Addon Compat | [`lets-do-addon-compat`](https://modrinth.com/mod/lets-do-addon-compat) MR | 2.3.1-neoforge | 2025-10-04 | release | ✅ |  |
| ~~Let's Do EMI Compat~~ | [`lets-do-emi-compat`](https://modrinth.com/mod/lets-do-emi-compat) MR | 2.0.3 | 2026-07-26 | release | ✅ | Tolta dal pack il 16/10/2026 (superflua con JEI + plugin EMI nativi) |
| Serene Seasons | [`serene-seasons`](https://modrinth.com/mod/serene-seasons) MR | 10.1.0.9 | 2026-09-05 | beta | ⚠️ | Tutte le build 1.21.1 segnate beta (abitudine dell'autore) |
| Snow! Real Magic! | [`snow-real-magic`](https://modrinth.com/mod/snow-real-magic) MR | 12.2.3+neoforge | 2026-09-27 | release | ✅ |  |

### Tech

| Mod | Progetto | Versione NeoForge 1.21.1 | Data | Tipo | Esito | Note |
|---|---|---|---|---|---|---|
| Create | [`create`](https://modrinth.com/mod/create) MR | 6.0.10+mc1.21.1 | 2026-04-21 | release | ✅ |  |
| Create Crafts & Additions | [`createaddition`](https://modrinth.com/mod/createaddition) MR | neoforge-1.21.1-1.6.0 | 2026-06-02 | release | ✅ | Ultima release; la 1.7.x è beta |
| Create: Connected | [`create-connected`](https://modrinth.com/mod/create-connected) MR | 1.3.3-mc1.21.1 | 2026-08-31 | release | ✅ |  |
| Create: Enchantment Industry | [`create-enchantment-industry`](https://modrinth.com/mod/create-enchantment-industry) MR | 2.4.2 | 2026-06-13 | release | ✅ | Ultima release; la 2.5.x è beta/alpha |
| Create: Dragons Plus (dipendenza) | [`create-dragons-plus`](https://modrinth.com/mod/create-dragons-plus) MR | 1.11.9 | 2026-09-17 | release | ✅ | Dipendenza di Enchantment Industry |
| Create: Integrated Farming | [`create-integrated-farming`](https://modrinth.com/mod/create-integrated-farming) MR | 1.4.3 | 2026-09-21 | release | ✅ |  |
| Mekanism | [`mekanism`](https://modrinth.com/mod/mekanism) MR | 10.7.19.85 | 2026-04-10 | release | ✅ |  |
| Mekanism Generators | [`mekanism-generators`](https://modrinth.com/mod/mekanism-generators) MR | 10.7.19.85 | 2026-04-10 | release | ✅ | Stessa versione di Mekanism |
| Mekanism: Ponders | [`mekanism-ponders`](https://modrinth.com/mod/mekanism-ponders) MR | 1.0.3-1.21.1 | 2026-04-28 | release | ✅ |  |
| Pipez | [`pipez`](https://modrinth.com/mod/pipez) MR | neoforge-1.21.1-1.2.31 | 2026-07-01 | beta | ⚠️ | Per la 1.21.1 esistono solo beta (progetto ufficiale) |

### Storage, zaini e trasporto

| Mod | Progetto | Versione NeoForge 1.21.1 | Data | Tipo | Esito | Note |
|---|---|---|---|---|---|---|
| Storage Drawers | [`storagedrawers`](https://modrinth.com/mod/storagedrawers) MR | 1.21.1-13.11.4 | 2025-09-14 | release | ✅ |  |
| Tom's Simple Storage | [`toms-storage`](https://modrinth.com/mod/toms-storage) MR | 1.21-2.4.2 | 2026-08-30 | release | ✅ |  |
| Ender Storage | [`ender-storage`](https://modrinth.com/mod/ender-storage) MR | 2.13.0.191 | 2025-02-05 | release | ⚠️ | Ultima build di febbraio 2025 |
| Sophisticated Backpacks | [`sophisticated-backpacks`](https://modrinth.com/mod/sophisticated-backpacks) MR | 1.21.1-3.26.12.2208 | 2026-10-13 | release | ✅ |  |
| Sophisticated Core (dipendenza) | [`sophisticated-core`](https://modrinth.com/mod/sophisticated-core) MR | 1.21.1-1.5.13.2404 | 2026-10-15 | release | ✅ | Dipendenza di Sophisticated Backpacks |
| Sophisticated Backpacks Create Integration | [`sophisticated-backpacks-create-integration`](https://modrinth.com/mod/sophisticated-backpacks-create-integration) MR | 1.21.1-0.2.0.168 | 2026-09-07 | release | ✅ |  |
| Traveler's Backpack | [`travelersbackpack`](https://modrinth.com/mod/travelersbackpack) MR | 1.21.1-10.1.39 | 2026-08-29 | release | ✅ |  |

### Equipaggiamento e incantamenti

| Mod | Progetto | Versione NeoForge 1.21.1 | Data | Tipo | Esito | Note |
|---|---|---|---|---|---|---|
| Truly Modular: Modular Item API (Miapi) | [`modular-item-api`](https://modrinth.com/mod/modular-item-api) MR | 2.3.9-1.21-neoforge | 2026-08-24 | release | ✅ |  |
| Truly Modular: Arsenal | [`truly-modular-arsenal`](https://modrinth.com/mod/truly-modular-arsenal) MR | 2.4-1.21-neoforge | 2026-04-01 | release | ✅ |  |
| Truly Modular: Archery | [`truly-modular-archery`](https://modrinth.com/mod/truly-modular-archery) MR | 2.2-1.21-neoforge | 2026-04-01 | release | ✅ |  |
| Truly Modular: Armory | [`truly-modular-armory`](https://modrinth.com/mod/truly-modular-armory) MR | 2.2-1.21-neoforge | 2026-04-01 | release | ✅ |  |
| Apotheosis | [`apotheosis`](https://modrinth.com/mod/apotheosis) MR | 1.21.1-8.9.0 | 2026-09-27 | release | ✅ | 8.9.0, più recente della 8.7.x annotata |
| Apothic Attributes (modulo) | [`apothic-attributes`](https://modrinth.com/mod/apothic-attributes) MR | 1.21.1-2.11.0 | 2026-09-29 | release | ✅ | Modulo di Apotheosis |
| Apothic Spawners (modulo) | [`apothic-spawners`](https://modrinth.com/mod/apothic-spawners) MR | 1.21.1-1.4.0 | 2026-07-20 | release | ✅ | Modulo di Apotheosis |
| Apothic Enchanting (modulo) | [`apothic-enchanting`](https://modrinth.com/mod/apothic-enchanting) MR | 1.21.1-1.6.4 | 2026-10-08 | release | ✅ | Modulo di Apotheosis |

### Strutture

| Mod | Progetto | Versione NeoForge 1.21.1 | Data | Tipo | Esito | Note |
|---|---|---|---|---|---|---|
| YUNG's Better Dungeons | [`yungs-better-dungeons`](https://modrinth.com/mod/yungs-better-dungeons) MR | 1.21.1-NeoForge-5.1.4 | 2024-12-01 | release | ⚠️ | Ramo 1.21.1 concluso: ultima build tra fine 2024 e metà 2025 |
| YUNG's Better Mineshafts | [`yungs-better-mineshafts`](https://modrinth.com/mod/yungs-better-mineshafts) MR | 1.21.1-NeoForge-5.1.1 | 2024-10-14 | release | ⚠️ | Ramo 1.21.1 concluso: ultima build tra fine 2024 e metà 2025 |
| YUNG's Better Strongholds | [`yungs-better-strongholds`](https://modrinth.com/mod/yungs-better-strongholds) MR | 1.21.1-NeoForge-5.1.3 | 2025-03-06 | release | ⚠️ | Ramo 1.21.1 concluso: ultima build tra fine 2024 e metà 2025 |
| YUNG's Better Nether Fortresses | [`yungs-better-nether-fortresses`](https://modrinth.com/mod/yungs-better-nether-fortresses) MR | 1.21.1-NeoForge-3.1.5 | 2025-06-01 | release | ⚠️ | Ramo 1.21.1 concluso: ultima build tra fine 2024 e metà 2025 |
| YUNG's Better Ocean Monuments | [`yungs-better-ocean-monuments`](https://modrinth.com/mod/yungs-better-ocean-monuments) MR | 1.21.1-NeoForge-4.1.2 | 2024-11-21 | release | ⚠️ | Ramo 1.21.1 concluso: ultima build tra fine 2024 e metà 2025 |
| YUNG's Better Desert Temples | [`yungs-better-desert-temples`](https://modrinth.com/mod/yungs-better-desert-temples) MR | 1.21.1-NeoForge-4.1.5 | 2025-03-07 | release | ⚠️ | Ramo 1.21.1 concluso: ultima build tra fine 2024 e metà 2025 |
| YUNG's Better Jungle Temples | [`yungs-better-jungle-temples`](https://modrinth.com/mod/yungs-better-jungle-temples) MR | 1.21.1-NeoForge-3.1.2 | 2024-11-21 | release | ⚠️ | Ramo 1.21.1 concluso: ultima build tra fine 2024 e metà 2025 |
| YUNG's Better Witch Huts | [`yungs-better-witch-huts`](https://modrinth.com/mod/yungs-better-witch-huts) MR | 1.21.1-NeoForge-4.1.1 | 2024-10-14 | release | ⚠️ | Ramo 1.21.1 concluso: ultima build tra fine 2024 e metà 2025 |
| YUNG's Bridges | [`yungs-bridges`](https://modrinth.com/mod/yungs-bridges) MR | 1.21.1-NeoForge-5.1.1 | 2024-10-14 | release | ⚠️ | Ramo 1.21.1 concluso: ultima build tra fine 2024 e metà 2025 |
| YUNG's Extras | [`yungs-extras`](https://modrinth.com/mod/yungs-extras) MR | 1.21.1-NeoForge-5.1.1 | 2024-10-14 | release | ⚠️ | Ramo 1.21.1 concluso: ultima build tra fine 2024 e metà 2025 |
| When Dungeons Arise | [`when-dungeons-arise`](https://modrinth.com/mod/when-dungeons-arise) MR | 2.1.68 | 2025-10-26 | release | ✅ |  |
| Dungeons and Taverns | [`dungeons-and-taverns`](https://modrinth.com/mod/dungeons-and-taverns) MR | v4.4.4+mod | 2024-09-29 | release | ⚠️ | Ultima build di settembre 2024 |
| Towns and Towers | [`towns-and-towers`](https://modrinth.com/mod/towns-and-towers) MR | 1.13.11 | 2026-08-15 | release | ✅ |  |
| Moog's End Structures (MES) | [`mes-moogs-end-structures`](https://modrinth.com/mod/mes-moogs-end-structures) MR | 2.1.1 | 2026-09-17 | release | ✅ |  |
| Sparse Structures | [`sparsestructures`](https://modrinth.com/mod/sparsestructures) MR | 3.0 | 2025-04-23 | release | ⚠️ | Ultima build di aprile 2025 |
| Explorer's Compass | [`explorers-compass`](https://modrinth.com/mod/explorers-compass) MR | 1.21.1-3.4.0-neoforge | 2026-04-08 | release | ✅ |  |
| Compass to Map: Xaero's | [`compass-to-map-xaeros`](https://modrinth.com/mod/compass-to-map-xaeros) MR | 0.1.2+neoforge-1.21.1 | 2026-09-07 | release | ✅ | Non confondere con la variante per JourneyMap |

### Dimensioni

| Mod | Progetto | Versione NeoForge 1.21.1 | Data | Tipo | Esito | Note |
|---|---|---|---|---|---|---|
| The Twilight Forest | [`the-twilight-forest`](https://www.curseforge.com/minecraft/mc-mods/the-twilight-forest) CF | 4.8.3345 | 2026-03-22 | release | ✅ | Solo CurseForge |
| Deeper and Darker | [`deeperdarker`](https://modrinth.com/mod/deeperdarker) MR | 1.4.1-neoforge-1.21.1 | 2026-06-05 | release | ✅ |  |
| The Undergarden | [`the-undergarden`](https://modrinth.com/mod/the-undergarden) MR | 0.9.6 | 2026-04-02 | beta | ⚠️ | Solo beta: la mod è ancora in beta, ma aggiornata |
| YUNG's Better End Island | [`yungs-better-end-island`](https://modrinth.com/mod/yungs-better-end-island) MR | 1.21.1-NeoForge-3.1.2 | 2025-03-13 | release | ⚠️ | Ramo 1.21.1 concluso: ultima build tra fine 2024 e metà 2025 |
| Unusual End | [`unusual_end`](https://modrinth.com/mod/unusual_end) MR | 2.3.1b-neo | 2026-09-11 | release | ✅ |  |
| The Aether | [`aether`](https://modrinth.com/mod/aether) MR | 1.21.1-1.5.10-neoforge | 2025-09-28 | release | ✅ |  |
| Deep Aether | [`deep-aether`](https://modrinth.com/mod/deep-aether) MR | 1.21.1-1.1.5.1 | 2026-03-29 | release | ✅ |  |

### Boss e nemici

| Mod | Progetto | Versione NeoForge 1.21.1 | Data | Tipo | Esito | Note |
|---|---|---|---|---|---|---|
| L_Ender's Cataclysm | [`l_enders-cataclysm`](https://modrinth.com/mod/l_enders-cataclysm) MR | 3.33 | 2026-09-20 | release | ✅ |  |
| Mowzie's Mobs | [`mowzies-mobs`](https://modrinth.com/mod/mowzies-mobs) MR | 1.8.2 | 2026-03-15 | release | ✅ |  |
| Born in Chaos | [`borninchaos`](https://modrinth.com/mod/borninchaos) MR | 1.7.6 | 2026-06-17 | release | ✅ |  |
| Born In Configuration | [`born-in-configuration`](https://modrinth.com/mod/born-in-configuration) MR | 4.0 [NEO] | 2026-10-07 | release | ✅ | Addon di terzi; la 4.0 ha 9 giorni, ripiego 3.2.2 |
| Friends & Foes | [`friends-and-foes-forge`](https://modrinth.com/mod/friends-and-foes-forge) MR | 5.0.2 | 2026-10-09 | release | ✅ | Il progetto NeoForge è friends-and-foes-forge |
| Mutant Monsters | [`mutant-monsters`](https://modrinth.com/mod/mutant-monsters) MR | v21.1.1-1.21.1-NeoForge | 2025-11-17 | release | ✅ |  |
| Illager Invasion | [`illager-invasion`](https://modrinth.com/mod/illager-invasion) MR | v21.1.6-1.21.1-NeoForge | 2025-05-03 | release | ⚠️ | Ultima build di maggio 2025 |
| Ender Dragon Fight Remastered | [`edf-remastered`](https://modrinth.com/mod/edf-remastered) MR | 5.0.2+mod | 2026-07-16 | release | ✅ |  |
| Gateways to Eternity | [`gateways-to-eternity`](https://modrinth.com/mod/gateways-to-eternity) MR | 1.21.1-5.1.0 | 2026-06-19 | release | ✅ |  |

### Villager

| Mod | Progetto | Versione NeoForge 1.21.1 | Data | Tipo | Esito | Note |
|---|---|---|---|---|---|---|
| Easy Villagers | [`easy-villagers`](https://modrinth.com/mod/easy-villagers) MR | neoforge-1.21.1-1.1.47 | 2026-10-11 | release | ✅ |  |
| Easy Auto Cycler | [`easy-auto-cycler`](https://modrinth.com/mod/easy-auto-cycler) MR | 3.1.0 | 2026-08-01 | release | ✅ | Solo client; usa Easy Villagers |

### Animali e pesca

| Mod | Progetto | Versione NeoForge 1.21.1 | Data | Tipo | Esito | Note |
|---|---|---|---|---|---|---|
| Starcatcher | [`starcatcher`](https://modrinth.com/mod/starcatcher) MR | 3.3.6-NEOFORGE-1.21.1 | 2026-10-09 | release | ✅ |  |
| Animal Pens | [`animalpens`](https://modrinth.com/mod/animalpens) MR | 2.5.0-1.21 | 2026-10-05 | release | ✅ |  |
| Animal Feeding Trough | [`animal_feeding_trough`](https://modrinth.com/mod/animal_feeding_trough) MR | 1.1.2+1.21(.1)-neoforge | 2024-09-22 | release | ⚠️ | Ultima build 1.21.1 di settembre 2024 (release); le successive sono per versioni più nuove |

### Utilità di gioco

| Mod | Progetto | Versione NeoForge 1.21.1 | Data | Tipo | Esito | Note |
|---|---|---|---|---|---|---|
| Chunk Loaders | [`chunk-loaders`](https://modrinth.com/mod/chunk-loaders) MR | 1.2.9-neoforge-mc1.21 | 2025-07-31 | release | ✅ |  |
| Corail Tombstone | [`corail-tombstone`](https://modrinth.com/mod/corail-tombstone) MR | neoforge-1.21.1-9.5.6 | 2026-09-09 | release | ✅ |  |
| Waystones | [`waystones`](https://modrinth.com/mod/waystones) MR | 21.1.46+neoforge-1.21.1 | 2026-09-25 | release | ✅ |  |
| Xaero's Minimap & World Map - Waystones Compatibility | [`xaeros-minimap-world-map-waystones-compatibility-forge`](https://modrinth.com/mod/xaeros-minimap-world-map-waystones-compatibility-forge) MR | 2.1.0 | 2026-04-24 | release | ✅ | Slug con -forge ma il file è NeoForge 1.21.1 |
| Akashic Tome | [`akashic-tome`](https://modrinth.com/mod/akashic-tome) MR | 1.21.1-1.8-30 | 2026-03-17 | release | ✅ |  |
| OmniTools (Omni Wrench) | [`omnitools`](https://modrinth.com/mod/omnitools) MR | 1.21.1-1.2.1 | 2026-01-09 | release | ✅ |  |

### Comodità

| Mod | Progetto | Versione NeoForge 1.21.1 | Data | Tipo | Esito | Note |
|---|---|---|---|---|---|---|
| Mouse Tweaks | [`mouse-tweaks`](https://modrinth.com/mod/mouse-tweaks) MR | 1.21-2.26.1-neoforge | 2024-08-17 | release | ⚠️ | Unica build per 1.21/1.21.1, agosto 2024 |
| Inventory Essentials | [`inventory-essentials`](https://modrinth.com/mod/inventory-essentials) MR | 21.1.20+neoforge-1.21.1 | 2026-10-02 | release | ✅ |  |
| Controlling | [`controlling`](https://modrinth.com/mod/controlling) MR | 19.0.5 | 2025-03-30 | release | ⚠️ | Ultima build di marzo 2025 |
| Crafting Tweaks | [`crafting-tweaks`](https://modrinth.com/mod/crafting-tweaks) MR | 21.1.11+neoforge-1.21.1 | 2026-08-21 | release | ✅ |  |
| Simple Backups | [`simple-backups`](https://modrinth.com/mod/simple-backups) MR | 1.21-4.0.21 | 2025-10-26 | release | ✅ | Ultima release; dalla 4.0.22 alla 4.0.30 sono beta |
| Torchmaster | [`torchmaster`](https://modrinth.com/mod/torchmaster) MR | 21.1.13-release | 2026-09-22 | release | ✅ |  |
| Comforts | [`comforts`](https://modrinth.com/mod/comforts) MR | 9.0.5+1.21.1 | 2026-01-24 | release | ✅ |  |
| Carry On | [`carry-on`](https://modrinth.com/mod/carry-on) MR | 2.2.6 | 2026-07-26 | release | ✅ |  |
| RightClickHarvest | [`rightclickharvest`](https://modrinth.com/mod/rightclickharvest) MR | 4.6.1+1.21.1 | 2026-01-22 | release | ✅ |  |
| FallingTree | [`fallingtree`](https://modrinth.com/mod/fallingtree) MR | 1.21.1-1.21.1.11 | 2025-08-01 | release | ✅ |  |
| Leaves Be Gone | [`leaves-be-gone`](https://modrinth.com/mod/leaves-be-gone) MR | v21.1.1-1.21.1-NeoForge | 2026-05-04 | release | ✅ |  |

### Interfaccia e mappa

| Mod | Progetto | Versione NeoForge 1.21.1 | Data | Tipo | Esito | Note |
|---|---|---|---|---|---|---|
| EMI | [`emi`](https://modrinth.com/mod/emi) MR | 1.1.24+1.21.1+neoforge | 2026-05-13 | release | ✅ |  |
| JEI | [`jei`](https://modrinth.com/mod/jei) MR | 19.51.0.418 | 2026-09-02 | release | ✅ | Ultima release; la 19.64 è beta |
| EMI Loot | [`emi-loot`](https://modrinth.com/mod/emi-loot) MR | 0.7.9+1.21+neoforge | 2026-01-04 | release | ✅ |  |
| EMI Ores | [`emi-ores`](https://modrinth.com/mod/emi-ores) MR | 1.3+1.21.1+neoforge | 2026-06-15 | release | ✅ |  |
| Jade | [`jade`](https://modrinth.com/mod/jade) MR | 15.10.6+neoforge | 2026-08-06 | release | ✅ |  |
| AppleSkin | [`appleskin`](https://modrinth.com/mod/appleskin) MR | 3.0.9+mc1.21 | 2026-04-01 | release | ✅ |  |
| Polymorph | [`polymorph`](https://modrinth.com/mod/polymorph) MR | 1.1.0+1.21.1 | 2025-07-21 | release | ✅ | Ultima release; la 1.2.0 è beta |
| Enchantment Descriptions | [`enchantment-descriptions`](https://modrinth.com/mod/enchantment-descriptions) MR | 21.1.11 | 2026-08-20 | release | ✅ |  |
| Pick Up Notifier | [`pick-up-notifier`](https://modrinth.com/mod/pick-up-notifier) MR | v21.1.1-1.21.1-NeoForge | 2025-04-11 | release | ⚠️ | Ultima build di aprile 2025 |
| YUNG's Menu Tweaks | [`yungs-menu-tweaks`](https://modrinth.com/mod/yungs-menu-tweaks) MR | 1.21.1-NeoForge-2.1.2 | 2025-02-04 | release | ⚠️ | Ultima build di febbraio 2025 |
| Xaero's Minimap | [`xaeros-minimap`](https://modrinth.com/mod/xaeros-minimap) MR | neoforge-1.21.1-26.6.0 | 2026-10-05 | release | ✅ |  |
| Xaero's World Map | [`xaeros-world-map`](https://modrinth.com/mod/xaeros-world-map) MR | neoforge-1.21.1-1.47.0 | 2026-10-05 | release | ✅ |  |

### Atmosfera

| Mod | Progetto | Versione NeoForge 1.21.1 | Data | Tipo | Esito | Note |
|---|---|---|---|---|---|---|
| Shoulder Surfing Reloaded | [`shoulder-surfing-reloaded`](https://modrinth.com/mod/shoulder-surfing-reloaded) MR | 1.21.1-5.2.0+neoforge | 2026-09-29 | release | ✅ |  |
| Sound Physics Remastered | [`sound-physics-remastered`](https://modrinth.com/mod/sound-physics-remastered) MR | neoforge-1.21.1-1.5.1 | 2025-09-25 | alpha | ⚠️ | Solo alpha/beta (abitudine dell'autore, 55M di download) |
| AmbientSounds | [`ambientsounds`](https://modrinth.com/mod/ambientsounds) MR | 6.3.10 | 2026-10-08 | release | ✅ |  |
| Subtle Effects | [`subtle-effects`](https://modrinth.com/mod/subtle-effects) MR | 1.15.0 | 2026-10-07 | release | ✅ |  |
| Particle Rain | [`particle-rain`](https://modrinth.com/mod/particle-rain) MR | v4.0.1+1.21.1-neoforge | 2026-10-07 | release | ✅ |  |
| LambDynamicLights | [`lambdynamiclights`](https://modrinth.com/mod/lambdynamiclights) MR | 4.8.11+1.21.1 | 2026-08-31 | release | ✅ | Sostituisce Sodium Dynamic Lights (port non ufficiale); ultima build per la 1.21 |
| ~~Enhanced Celestials~~ | ~~`enhanced-celestials`~~ | ~~6.0.2.6-neoforge~~ | ~~2026-08-07~~ | ~~release~~ | — | Tolta nella 0.5.1: sostituita da Enhanced Celestials 2 (righe in fondo) |
| Travelers Titles | [`travelers-titles`](https://modrinth.com/mod/travelers-titles) MR | 1.21.1-NeoForge-5.1.3 | 2025-03-11 | release | ⚠️ | Ultima build di marzo 2025 |
| Not Enough Animations | [`not-enough-animations`](https://modrinth.com/mod/not-enough-animations) MR | 1.12.6-1.21.1 - NeoForge | 2026-09-19 | release | ✅ |  |
| Entity Model Features (EMF) | [`entity-model-features`](https://modrinth.com/mod/entity-model-features) MR | 3.3.12-neoforge-1.21 | 2026-10-15 | release | ✅ |  |
| Entity Texture Features (ETF) | [`entitytexturefeatures`](https://modrinth.com/mod/entitytexturefeatures) MR | 7.2.5-neoforge-1.21 | 2026-10-04 | release | ✅ |  |
| Fresh Animations (resource pack) | [`fresh-animations`](https://modrinth.com/resourcepack/fresh-animations) MR | 1.10.4 | 2026-02-24 | beta | ⚠️ | Tutte le versioni segnate beta; richiede in pratica EMF + ETF |

### Performance

| Mod | Progetto | Versione NeoForge 1.21.1 | Data | Tipo | Esito | Note |
|---|---|---|---|---|---|---|
| Sodium | [`sodium`](https://modrinth.com/mod/sodium) MR | mc1.21.1-0.8.13-neoforge | 2026-08-28 | release | ✅ | 0.8.13, non 0.8.12 |
| Lithium | [`lithium`](https://modrinth.com/mod/lithium) MR | mc1.21.1-0.15.4-neoforge | 2026-06-27 | release | ✅ |  |
| FerriteCore | [`ferrite-core`](https://modrinth.com/mod/ferrite-core) MR | 7.0.3-neoforge | 2026-01-25 | release | ✅ |  |
| ModernFix | [`modernfix`](https://modrinth.com/mod/modernfix) MR | 5.27.26+mc1.21.1 | 2026-10-08 | release | ✅ |  |
| ImmediatelyFast | [`immediatelyfast`](https://modrinth.com/mod/immediatelyfast) MR | 1.6.14+1.21.1-neoforge | 2026-09-13 | release | ✅ |  |
| Entity Culling | [`entityculling`](https://modrinth.com/mod/entityculling) MR | 1.11.3-1.21.1 - NeoForge | 2026-10-08 | release | ✅ |  |
| Structure Layout Optimizer | [`structure-layout-optimizer`](https://modrinth.com/mod/structure-layout-optimizer) MR | 1.0.12+1.21.1-neoforge | 2026-01-09 | release | ✅ |  |

### Fix e compatibilità

| Mod | Progetto | Versione NeoForge 1.21.1 | Data | Tipo | Esito | Note |
|---|---|---|---|---|---|---|
| Forgified Fabric API | [`forgified-fabric-api`](https://modrinth.com/mod/forgified-fabric-api) MR | 0.116.15+2.3.5+1.21.1 | 2026-08-24 | release | ✅ |  |
| AlmostUnified | [`almostunified`](https://modrinth.com/mod/almostunified) MR | 1.21.1-1.4.2+neoforge | 2026-05-22 | release | ✅ |  |

### Aggiunte dopo la verifica

| Mod | Progetto | Versione NeoForge 1.21.1 | Data | Tipo | Esito | Note |
|---|---|---|---|---|---|---|
| Ars Nouveau | [`ars-nouveau`](https://modrinth.com/mod/ars-nouveau) MR | 5.13.3 | 2026-10-03 | release | ✅ | Richiede Curios e GeckoLib. Aggiunta il 16/10/2026 |
| Artifacts | [`artifacts`](https://modrinth.com/mod/artifacts) MR | 13.2.5 | 2026-09-02 | release | ✅ | Curios e Accessories opzionali. Aggiunta il 16/10/2026 |
| Paxi | [`paxi`](https://modrinth.com/mod/paxi) MR | 1.21.1-NeoForge-5.1.3 | 2025-05-01 | release | ⚠️ | Ramo 1.21.1 concluso (ultima build maggio 2025); richiede YUNG's API. Aggiunta il 16/10/2026 |
| Ars Delight (Flavors & Delight) | [`arsdelight`](https://modrinth.com/mod/arsdelight) MR | 2.2.5 | 2026-10-06 | release | ✅ | Richiede Ars Nouveau e Farmer's Delight. Aggiunta il 16/10/2026 |
| Ars Creo | [`ars-creo`](https://modrinth.com/mod/ars-creo) MR | 5.4.0 | 2026-05-24 | release | ✅ | Dello sviluppatore di Ars; richiede Create 6.0.9+. Aggiunta il 16/10/2026 |
| Ars Mekanica | [`ars-mekanica`](https://modrinth.com/mod/ars-mekanica) MR | 1.3.0 | 2026-07-27 | release | ✅ | Richiede Mekanism. Aggiunta il 16/10/2026 |
| Ars Elemental | [`ars-elemental`](https://www.curseforge.com/minecraft/mc-mods/ars-elemental) CF | 0.7.10.4 | 2026-10-04 | release | ✅ | **solo CurseForge**. Aggiunta il 16/10/2026 |
| Ars QOL | — | 1.2.1 | 2026-10-05 | release | ✅ | Progetto piccolo e nuovo (cercarlo per nome in Prism). Aggiunta il 16/10/2026 |
| Ars Unification | [`ars-unification`](https://modrinth.com/mod/ars-unification) MR | 1.2.19 | — | release | ✅ | Aggiunta il 16/10/2026 |
| Not Enough Glyphs | [`not-enough-glyphs`](https://modrinth.com/mod/not-enough-glyphs) MR | 4.6.x | — | release | ✅ | Aggiunta il 16/10/2026 |
| Ars Controle | [`ars-controle`](https://modrinth.com/mod/ars-controle) MR | 1.6.16 | 2026-09-10 | release | ✅ | Aggiunta il 16/10/2026 |
| Occultism | [`occultism`](https://modrinth.com/mod/occultism) MR | 1.224.5 | 2026-10-11 | release | ✅ | Richiede Modonomicon, Curios, GeckoLib, SmartBrainLib. Aggiunta il 16/10/2026 |
| Ars Ocultas | [`ars-ocultas`](https://modrinth.com/mod/ars-ocultas) MR | 1.21.1-2.6.1 | 2026-08-06 | release | ✅ | Ars 5.3–6.0 e Occultism ≥ 1.220.4. Aggiunta il 16/10/2026 |
| Occult Delight | [`occult-delight`](https://modrinth.com/mod/occult-delight) MR | 1.0.0 | 2026-07-31 | release | ⚠️ | Una sola release. Aggiunta il 16/10/2026 |
| ~~Create: Occult Engineering~~ | ~~`occult-engineering`~~ | ~~1.21.1-0.13.1~~ | ~~2026-08-03~~ | ~~beta~~ | — | Tolta il 16/10/2026 |
| Reactive Alchemy | [`reactive`](https://modrinth.com/mod/reactive) MR | 1.21.1-10.2.1 | 2026-09-27 | release | ✅ | Richiede Patchouli. Aggiunta il 16/10/2026 |
| Psi | [`psi`](https://modrinth.com/mod/psi) MR | 1.21.1-110 | 2026-09-01 | release | ✅ | Richiede Patchouli. Aggiunta il 16/10/2026 |
| Scriptor Magicae | [`JyJgaOrk`](https://modrinth.com/mod/JyJgaOrk) MR | 2.0.14-1.21.1-neoforge | 2026-09-17 | release | ✅ | Richiede Unfocused e Kotlin for Forge. Aggiunta il 16/10/2026 |
| Regions Unexplored | [`regions-unexplored`](https://modrinth.com/mod/regions-unexplored) MR | 0.6.2-neoforge-21.1 | 2026-07-12 | release | ✅ | Aggiunta il 17/10/2026 |
| Chunky | [`chunky`](https://modrinth.com/mod/chunky) MR | 1.4.23 | 2025-04-04 | release | ✅ | Aggiunta il 17/10/2026 |
| Clumps | [`clumps`](https://modrinth.com/mod/clumps) MR | 19.0.0.1 | 2024-08-13 | release | ✅ | Aggiunta il 17/10/2026 |
| Rechiseled | [`rechiseled`](https://modrinth.com/mod/rechiseled) MR | 1.2.6-neoforge-mc1.21 | 2026-09-13 | release | ✅ | Aggiunta il 17/10/2026 |
| Supplementaries | [`supplementaries`](https://modrinth.com/mod/supplementaries) MR | 1.21.1-4.0.2 | 2026-10-16 | release | ✅ | Aggiunta il 17/10/2026 |
| Handcrafted | [`handcrafted`](https://modrinth.com/mod/handcrafted) MR | 4.0.3 | 2025-03-22 | release | ✅ | Aggiunta il 17/10/2026 |
| Construction Sticks | [`construction-sticks`](https://modrinth.com/mod/construction-sticks) MR | 1.5.0 | 2026-08-29 | release | ✅ | Aggiunta il 17/10/2026 |
| Lithostitched (dipendenza) | [`lithostitched`](https://modrinth.com/mod/lithostitched) MR | 1.8.1-neoforge-21.1 | 2026-10-14 | release | ✅ | Richiesta da regions-unexplored. MIT. Aggiunta il 17/10/2026 |
| Fusion (Connected Textures) (dipendenza) | [`fusion-connected-textures`](https://modrinth.com/mod/fusion-connected-textures) MR | 1.3.16-neoforge-mc1.21.1 | 2026-10-05 | release | ✅ | Richiesta da rechiseled. All-Rights-Reserved. Aggiunta il 17/10/2026 |
| Moonlight Lib (dipendenza) | [`moonlight`](https://modrinth.com/mod/moonlight) MR | 1.21.1-3.7.2 | 2026-10-10 | release | ✅ | Richiesta da supplementaries. LGPL-with-additional-dependency-clause. Aggiunta il 17/10/2026 |
| XP Tome | [`xp-tome`](https://modrinth.com/mod/xp-tome) MR | v2.4 | 2024-10-24 | release | ✅ | Nessuna dipendenza. Aggiunta il 17/10/2026 |
| Just Enough Breeding | [`justenoughbreeding`](https://modrinth.com/mod/justenoughbreeding) MR | 3.3.1 | 2026-10-02 | release | ✅ | Dipendenze tutte opzionali (JEI/EMI). Aggiunta il 17/10/2026 |
| Just Enough Professions | [`just-enough-professions-jep`](https://modrinth.com/mod/just-enough-professions-jep) MR | 4.0.5 | 2026-04-22 | release | ✅ | Richiede JEI. Aggiunta il 17/10/2026 |
| NetherPortalFix | [`netherportalfix`](https://modrinth.com/mod/netherportalfix) MR | 21.1.1+neoforge-1.21.1 | 2024-08-13 | release | ✅ | Richiede Balm; unica build 1.21.1. Aggiunta il 17/10/2026 |
| AllTheLeaks | [`alltheleaks`](https://www.curseforge.com/minecraft/mc-mods/alltheleaks) CF | 1.1.13+1.21.1-neoforge | 2026-09-22 | release | ✅ | **solo CurseForge**. Nel sorgente richiede solo NeoForge ≥ 21.1.195; si dichiara incompatibile con versioni vecchie di GeckoLib, Entity Culling, AmbientSounds e Occultism (le nostre sono più nuove). Aggiunta il 17/10/2026 |
| SeasonHud | [`seasonhud`](https://modrinth.com/mod/seasonhud) MR | 1.21.1-2.0.10 | 2026-08-31 | release | ✅ | Dipendenze opzionali (Serene Seasons, Xaero). Aggiunta il 17/10/2026 |
| Smarter Farmers | [`smarter-farmers-farmers-replant`](https://modrinth.com/mod/smarter-farmers-farmers-replant) MR | 1.21-2.2.4 | 2025-10-18 | release | ✅ | Richiede Moonlight. Aggiunta il 17/10/2026 |
| Open Together | [`open-together`](https://modrinth.com/mod/open-together) MR | 21.1.2 | 2026-09-10 | release | ✅ | Richiede Puzzles Lib. Aggiunta il 17/10/2026 |
| My Nether's Delight | [`my-nethers-delight`](https://modrinth.com/mod/my-nethers-delight) MR | 1.10.4.1 | 2026-09-11 | release | ✅ | ARR su Modrinth (MIT nel file di build); ⚠️ canna polverosa selvatica nel Nether. Pack 0.3.0 (18/10/2026) |
| Chef's Delight | [`chefs-delight`](https://modrinth.com/mod/chefs-delight) MR | 1.0.6-neoforge-1.21.1 | 2026-10-03 | release | ✅ | ⚠️ case nei villaggi; richiede NeoForge ≥ 21.1.219. Pack 0.3.0 |
| Create Confectionery | [`create-confectionery`](https://modrinth.com/mod/create-confectionery) MR | 1.1.3.b | 2026-08-15 | release | ✅ | Fatta con MCreator. Pack 0.3.0 |
| Rustic Delight | [`rustic-delight`](https://modrinth.com/mod/rustic-delight) MR | 1.7.1 | 2026-07-31 | release | ✅ | ⚠️ colture selvatiche; ha già le sue ricette per Botany Pots. Pack 0.3.0 |
| Ocean's Delight | [`oceans-delight`](https://modrinth.com/mod/oceans-delight) MR | 1.0.4 | 2026-04-17 | release | ✅ | Usa l'effetto Comfort di FD (a rischio con FD 1.4). Pack 0.3.0 |
| Autochef's Delight | [`autochefs-delight`](https://modrinth.com/mod/autochefs-delight) MR | 2.0.3+neoforge | 2026-04-30 | release | ✅ | Modifica la pentola di FD. Pack 0.3.0 |
| Farming for Blockheads | [`farming-for-blockheads`](https://modrinth.com/mod/farming-for-blockheads) MR | 21.1.14+neoforge-1.21.1 | 2026-09-25 | release | ✅ | Richiede Balm; niente irrigatori nella 1.21.1. Pack 0.3.0 |
| Cognition (ex Experience Obelisk) | [`cognition`](https://modrinth.com/mod/cognition) MR | 2.4.13 | 2026-07-10 | release | ✅ | Richiede GeckoLib; liquido `cognition:cognitium_source` (20 mB per punto, `c:experience`). Pack 0.3.0 |
| Macaw's Roofs | [`macaws-roofs`](https://modrinth.com/mod/macaws-roofs) MR | 2.3.2 | 2025-05-04 | release | ✅ | Pack 0.4.0 (18/10/2026) |
| Macaw's Paths and Pavings | [`macaws-paths-and-pavings`](https://modrinth.com/mod/macaws-paths-and-pavings) MR | 1.1.1 | 2025-09-24 | release | ✅ | Pack 0.4.0 |
| Macaw's Bridges | [`macaws-bridges`](https://modrinth.com/mod/macaws-bridges) MR | 3.1.2 | 2026-02-15 | release | ✅ | Pack 0.4.0 |
| Macaw's Windows | [`macaws-windows`](https://modrinth.com/mod/macaws-windows) MR | 2.4.2 | 2025-12-10 | release | ✅ | Pack 0.4.0 |
| Diagonal Fences | [`diagonal-fences`](https://modrinth.com/mod/diagonal-fences) MR | v21.1.1-1.21.1-NeoForge | 2024-11-18 | release | ⚠️ | Ramo 1.21.1 fermo al 2024; richiede Puzzles Lib. Pack 0.4.0 |
| Diagonal Walls | [`diagonal-walls`](https://modrinth.com/mod/diagonal-walls) MR | v21.1.2-1.21.1-NeoForge | 2024-11-19 | release | ⚠️ | Ramo 1.21.1 fermo al 2024. Pack 0.4.0 |
| Diagonal Windows | [`diagonal-windows`](https://modrinth.com/mod/diagonal-windows) MR | v21.1.1-1.21.1-NeoForge | 2024-11-18 | release | ⚠️ | Ramo 1.21.1 fermo al 2024. Pack 0.4.0 |
| Chimes | [`chimes`](https://modrinth.com/mod/chimes) MR | 2.1.1 | 2026-10-02 | release | ✅ | Pack 0.4.0 |
| Exposure | [`exposure`](https://modrinth.com/mod/exposure) MR | 1.9.19 | 2026-09-23 | release | ✅ | Pack 0.4.0 |
| Guard Villagers | [`guard-villagers`](https://modrinth.com/mod/guard-villagers) MR | 2.4.12 | 2026-08-30 | release | ✅ | ⚠️ guardie nei villaggi generati. Pack 0.4.0 |
| Every Compat (Wood Good) | [`every-compat`](https://modrinth.com/mod/every-compat) MR | 1.21-2.11.54 | 2026-10-17 | release | ✅ | Richiede Moonlight. Pack 0.4.0 |
| Create: Copycats+ | [`copycats`](https://modrinth.com/mod/copycats) MR | 3.0.9+mc.1.21.1-neoforge | 2026-09-06 | release | ✅ | Richiede Create. Pack 0.4.0 |
| Goblin Traders | [`goblin-traders`](https://www.curseforge.com/minecraft/mc-mods/goblin-traders) CF | 1.11.2 | — | release | ✅ | **solo CurseForge**; richiede Framework. Pack 0.4.0 |
| Framework (dipendenza) | [`framework`](https://www.curseforge.com/minecraft/mc-mods/framework) CF | 0.13.11 | — | release | ✅ | Libreria di MrCrayfish, **solo CurseForge**; licenza da verificare. Pack 0.4.0 |
| Jaden's Nether Expansion | [`jadens-nether-expansion`](https://modrinth.com/mod/jadens-nether-expansion) MR | 2.4.1 | 2026-08-22 | release | ✅ | Richiede Elysium API e Lodestone; Nether più alto (mondo nuovo). Pack 0.5.0 |
| MNS - Moog's Nether Structures | [`mns-moogs-nether-structures`](https://modrinth.com/mod/mns-moogs-nether-structures) MR | 3.1.1 | 2026-09-17 | release | ✅ | Richiede Moog's Structure Lib (già nel pack). Pack 0.5.0 |
| Nether Depths Upgrade | [`nether-depths-upgrade`](https://modrinth.com/mod/nether-depths-upgrade) MR | 3.3 | 2026-09-21 | release | ✅ | Pack 0.5.0 |
| Aures - Farmers Structures | [`aures-farmers-structures`](https://modrinth.com/mod/aures-farmers-structures) MR | 1.0.2 | 2026-05-18 | release | ✅ | Nessuna dipendenza dichiarata. Pack 0.5.0 |
| Better Archeology | [`better-archeology`](https://modrinth.com/mod/better-archeology) MR | 1.21.1-1.3.9 | 2026-10-08 | release | ✅ | Pack 0.5.0 |
| Nature's Compass | [`natures-compass`](https://modrinth.com/mod/natures-compass) MR | 1.21.1-3.4.0-neoforge | 2026-04-08 | release | ✅ | Nessuna dipendenza. Pack 0.5.0 |
| Aquamirae | [`aquamirae`](https://modrinth.com/mod/aquamirae) MR | 7.2.13 | 2026-10-17 | release | ✅ | Richiede GeckoLib e Fragmentum. Pack 0.5.0 |
| Creeper Overhaul | [`creeper-overhaul`](https://modrinth.com/mod/creeper-overhaul) MR | 4.0.6 | 2025-01-04 | release | ⚠️ | Ramo 1.21.1 fermo a gennaio 2025; richiede Resourceful Lib, Resourceful Config e GeckoLib (già nel pack). Pack 0.5.0 |
| Paragliders | [`paragliders`](https://modrinth.com/mod/paragliders) MR | 21.1.5 | 2026-03-22 | release | ✅ | Pack 0.5.0 |
| Elysium API (dipendenza) | [`elysium-api`](https://modrinth.com/mod/elysium-api) MR | 1.21.1-2.0.1 | 2026-08-22 | release | ✅ | Richiesta da jadens-nether-expansion. GPL-2.0-only. Pack 0.5.0 |
| Lodestone (dipendenza) | [`lodestonelib`](https://modrinth.com/mod/lodestonelib) MR | 1.8.2 | 2026-01-12 | release | ✅ | Richiesta da jadens-nether-expansion. LGPL-3.0-only. Pack 0.5.0 |
| Fragmentum (dipendenza) | [`fragmentum`](https://modrinth.com/mod/fragmentum) MR | 5.4.0 | 2026-10-16 | release | ✅ | Richiesta da aquamirae. Licenza Obscuria (LicenseRef-Obscuria-Ecosystem). Pack 0.5.0 |
| Enhanced Celestials 2: Core | [`enhanced-celestials-2-core`](https://modrinth.com/mod/enhanced-celestials-2-core) MR | 2.0.3.3-neoforge | 2026-09-07 | release | ✅ | Richiede CorgiLib ≥ 5.0.0.9 e Data Anchor ≥ 2.0.0.16; incompatibile con Enhanced Celestials. Pack 0.5.1 |
| Enhanced Celestials 2: Default Lunar Events | [`enhanced-celestials-2-default-lunar-events`](https://modrinth.com/mod/enhanced-celestials-2-default-lunar-events) MR | 2.0.1.3-neoforge | 2026-09-03 | release | ✅ | Richiede il Core. Pack 0.5.1 |
| Iris Shaders | [`iris`](https://modrinth.com/mod/iris) MR | 1.8.14-beta.1+1.21.1-neoforge | 2026-06-13 | beta | ⚠️ | Beta voluta: l'unica che funziona con Sodium 0.8 (la release 1.8.12 va in crash; `0303`). Dichiara Minecraft `[1.21,1.21.1)`, accettato da NeoForge sulla 1.21.1. Contiene 4 moduli di Fabric API già nel pack con versioni uguali o più nuove. Solo lato client. Pack 0.5.2 |
| Enhanced Celestials 2: Shader Support | [`enhanced-celestials-2-shader-support`](https://modrinth.com/mod/enhanced-celestials-2-shader-support) MR | 2.0.0.3-neoforge | 2026-09-03 | release | ✅ | Richiede Core ≥ 2.0.3.1, CorgiLib, Sodium e Iris. Solo lato client. Pack 0.5.2 |
| Complementary Reimagined (pacchetto di shader) | [`complementary-reimagined`](https://modrinth.com/shader/complementary-reimagined) MR | r5.9.3 | 2026-09-15 | release | ✅ | Per Iris; cartella `shaderpacks`. Pack 0.5.3 |
| MakeUp - Ultra Fast (pacchetto di shader) | [`makeup-ultra-fast-shaders`](https://modrinth.com/shader/makeup-ultra-fast-shaders) MR | 9.5g | 2026-10-04 | release | ✅ | Per Iris; cartella `shaderpacks`. Pack 0.5.3 |
| Relics | [`relics-mod`](https://modrinth.com/mod/relics-mod) MR | 0.12.9 | 2026-10-18 | beta | ⚠️ | Tutte le build 1.21.1 sono beta (scelta con `relics-mod@CWPAvFMI`). Richiede ShatterLib/OctoLib e Curios. Pack 0.7.0 |
| Reliquified Artifacts | [`reliquified-artifacts`](https://modrinth.com/mod/reliquified-artifacts) MR | 1.0.9 | 2026-10-12 | beta | ⚠️ | Beta; vuole esattamente Artifacts 13.2.5. Richiede Relics e Artifacts. ARR. Pack 0.7.0 |
| ShatterLib \| OctoLib (dipendenza) | [`shatterbyte-lib`](https://modrinth.com/mod/shatterbyte-lib) MR | 0.6.2 | 2026-05-04 | release | ✅ | Richiesta da relics-mod. ARR. Pack 0.7.0 |

## Librerie principali (arrivano come dipendenze)

Versioni ricontrollate sui metafile del pack il 18/10/2026 (prima alcune erano quelle della verifica, non quelle installate). Moog's Structure Lib è passata dalla 3.0.3 alla 3.4.2 nella 0.5.0, perché Moog's Nether Structures chiede almeno la 3.3.0 (bug B28).

Tutte con build NeoForge 1.21.1: YUNG's API 5.1.9 · Placebo 9.9.4 · Moog's Structure Lib 3.4.2 · Create: Dragons Plus 1.11.9 · Sophisticated Core 1.5.13 · Fzzy Config 0.7.7 · Bookshelf 21.1.81 · Prickle 21.1.11 · CorgiLib 5.0.0.9 · Data Anchor 2.0.0.17 (dalla 0.5.1; prima 2.0.0.14) · Puzzles Lib 21.1.64 · Resourceful Config 3.0.11 · CreativeCore 2.13.50. Non verificate una per una ma standard: Architectury, Balm, GeckoLib, Curios, Accessories, Citadel, Lionfish API, Blueprint, TerraBlender, NexusLib, Cristel Lib, Resourceful Lib.
