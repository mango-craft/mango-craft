# Secondo confronto con i modpack (17/10/2026)

> **Documento storico**: fotografia del momento in cui è stato scritto, non si aggiorna. Lo stato attuale è nei documenti vivi (vedi il README della cartella).

Pack analizzati: **grandi 1.21.1 NeoForge** (ATM10, Better MC 5, Craftoria, All of Create Aeronautics, Create Chronicles, FTB Evolution, Farmopolis) e **a tema** cozy/stregoneria/avventura (Society: Sunlit Valley, Farming Experience, Farming Crossing 5/6, Cottage Witch, CottageCore Dream Life, Homestead, Mayview, Create: Perfect World, WitchHazel, MMC5, Prominence II). Tutte le candidate hanno una build NeoForge 1.21.1 verificata.

**Piccole e utili (nessuna sovrapposizione)** — ✅ tutte approvate il 17/10/2026 (→ 0301)
| Mod | Dove | Versione · licenza | Cosa fa |
|---|---|---|---|
| Just Enough Breeding | 5 grandi + FE | 3.3.1 · MIT | Cibo per far accoppiare ogni animale, in EMI |
| Just Enough Professions | 4 grandi | 4.0.5 · MIT | Blocchi di lavoro dei villager, in EMI (via JEI) |
| NetherPortalFix | 7 grandi su 7 | 21.1.1 · ARR (Balm ✓) | Riporta al portale da cui sei entrato |
| AllTheLeaks | 7 grandi su 7 | 1.1.13 · MIT · **solo CurseForge** | Corregge perdite di memoria |
| SeasonHud | SSV | 2.0.10 · MIT | Mostra la stagione di Serene Seasons sotto la minimappa |
| Smarter Farmers | FE | 2.2.4 · ARR (Moonlight ✓) | I villager contadini ripiantano il seme giusto, anche modded |
| Open Together | FC5 | 21.1.2 · MPL-2.0 (Puzzles ✓) | Le porte doppie si aprono insieme |

**Contenuti a tema (da scegliere)**
| Mod | Versione · licenza | Cosa fa | Note |
|---|---|---|---|
| Farming for Blockheads | 21.1.14 · ARR (Balm ✓) | Mercato di semi e alberelli, irrigatori, fertilizzanti, nido per galline | La sua mangiatoia doppia Animal Feeding Trough. Addon Fertiliser for Blockheads per Botany Pots |
| Create Confectionery | 1.1.3.b · MIT | Cioccolato e dolci con Create | — |
| Overweight Farming | 2.2.0 · ARR | Raccolti giganti rari | — |
| Macaw's Roofs (+ Paths, Bridges, Windows) | Roofs 2.3.2 · ARR (Paths MIT) | Tetti, sentieri, ponti, finestre | Copre ciò che Handcrafted e Supplementaries non fanno |
| Every Compat | 2.11.52 · ARR (Moonlight ✓) | Varianti dei blocchi di Handcrafted, Storage Drawers, Botany Pots ecc. per i legni modded | Tanti blocchi in più, caricamento più lento |
| Diagonal Fences / Walls / Windows | MPL-2.0 (Puzzles ✓) | Recinti e muri in diagonale | Snow! Real Magic! ha già la compatibilità |
| Better Archeology | 1.3.8 · MIT | Fossili, reperti e siti di scavo | ⚠️ genera strutture → prima del mondo vero |
| Exposure | 1.9.19 · MIT | Macchine fotografiche e foto da sviluppare | — |
| Chimes | 2.1.1 · ARR | Campane a vento | — |
| Personality | 5.0.2 · Abnormals (Blueprint ✓) | Sedersi ovunque, strisciare | — |
| Small Ships / Paragliders | 2.0.2 ARR / 21.1.5 GPL-3.0 | Navi a vela / parapendio | Paragliders genera statue → prima del mondo vero |
| Goblin Traders / Guard Villagers | 1.11.2 MIT (+Framework) / 2.4.12 | Mercanti goblin / guardie dei villaggi | — |
| Autochef's Delight | 2.0.3 · ARR | Ingredienti impilati nella pentola di FD, aiuta l'automazione | — |
| Copycats+ · Create: Bells & Whistles · Create: Hypertubes | ARR · GPL · Apache | Blocchi copia di Create, accessori per treni, tubi di trasporto | Bells & Whistles: build di marzo 2025 |
| Creeper Overhaul · Variants & Ventures | ARR · CC-BY-NC-ND | Varianti dei mob | — |
| Ribbits · Aures Farmers Structures · Formations · Villages & Pillages · Vanilla Backport | — | Villaggi delle rane, strutture a tema FD, strutture, villaggi, contenuti delle versioni nuove | Il pack ha già molte strutture; ⚠️ tutte da decidere prima del mondo vero |

**Visti spesso ma non per noi**: shader (Iris), quest da scrivere (FTB Quests), mod da server, KubeJS, menu personalizzati; Cooking for Blockheads (seconda cucina), Sophisticated Storage (doppione di Tom's e Drawers), mobili alternativi (Handcrafted c'è), Aquaculture e altre pesche (alternative a Starcatcher, vedi 0611), Relics (Artifacts), Quality Food (rompe gli stack), Just Enough Resources (EMI Loot/Ores), Loot Integrations (c'è il nostro datapack), Building/Mining Gadgets, Mystical Agriculture, suite tech. Amendments torna nei pack a tema: resta da provare con Reactive Alchemy.

## Appendice: note grezze della ricerca (in inglese)

### Gap analysis notes (2026-10-17)
Packs: ATM10 (CF rel. 494), Craftoria 1.37.0 (GitHub MODLIST 522), BMC5 (CF 382), FTB Evolution (CF 526),
Create Chronicles Endventure 2.0.0 (CF 320), All of Create Aeronautics (CF 260), Farmopolis (GitHub manifest 7.2, 278; repo 8.2).
Counts: counts.tsv (script scripts_count.py). Fuzzy-match false positives fixed by hand: sophisticated-storage, autochefs-delight, farmers-structures, toast-control.

Verified (Modrinth API unless noted), NeoForge 1.21.1 latest:
- netherportalfix 21.1.1 2024-08-13 ARR, Balm
- alltheleaks 1.1.13 2026-09-22 MIT (CF only)
- justenoughbreeding 3.3.1 2026-10-02 MIT, JEI/REI/EMI, no required deps
- just-enough-professions-jep 4.0.5 2026-04-22 MIT, req JEI
- more-overlays-updated 1.24.2 2026-04-19 MIT
- just-zoom 3.0.1 2026-10-04 DSMSLv3.1, req Konkrete
- visual-workbench 21.1.2 2026-09-02 MPL-2.0, req Puzzles Lib
- extreme_sound_muffler 3.56 2026-04-08 LGPL-3.0
- better-advancements 0.4.3.21 beta 2024-10-27 Dont-Be-a-Jerk
- sophisticated-storage 1.21.1-1.6.5.2176 2026-10-13 ARR, req Sophisticated Core
- cooking-for-blockheads 21.1.24 2026-07-10 ARR, Balm
- farming-for-blockheads 21.1.14 2026-09-25 ARR, Balm
- autochefs-delight 2.0.3 2026-04-30 ARR, req FD (Snownee)
- copycats 3.0.9 2026-09-06 ARR, req Create, opt JEI
- bellsandwhistles v0.4.7 2025-03-13 GPL-3.0+, req Create
- hypertube 0.6.0 2026-07-30 Apache-2.0, req Create
- creeper-overhaul 4.0.6 2025-01-04 ARR, req Resourceful Lib/Config, GeckoLib
- variants-and-ventures 1.0.28 2026-09-26 CC-BY-NC-ND-4.0, req Resourceful Lib
- vanillabackport 1.1.7.10 2026-06-11 LicenseRef-VBL, req Platform
- formations-overworld 1.0.5c 2026-09-16 / formations-nether 1.0.5b 2026-09-11 ARR, req Formations lib
- villages-and-pillages 2.0.0 2026-10-01 CC-BY-NC-ND-4.0
- aures-farmers-structures 1.0.2 2026-05-18 ARR
- exposure 1.9.19 2026-09-23 MIT
- jade-addons 6.1.1 2026-08-31 ARR (CF)

### Themed packs analysed (2026-10-17)
1. Society: Sunlit Valley — 1.20.1 Forge, 4.1.5B (2026-10-07), 367 projects (pakku-lock.json, github.com/Chakyl/society-sunlit-valley) -> society_mods.txt
2. Farming Experience — 1.21.1 NeoForge (also 1.20.1 Fabric), 26.08.26 (2026-08-26), 106 deps; list github.com/axperty/farmingexperience wiki/included_mods.md
3. Farming Crossing 5: Made to Order — 1.21.1 NeoForge, v2.1.5 (2025-08-18), ~231 mods from CF description -> fc5_mods.txt
4. Farming Crossing 6: Dinner Party — 1.21.1 NeoForge, v1.1.8 (2026-09-25), partial (BWG, WilderNature, Let's Do, Tide 2, Create Confectionery, Prefab, Controllable)
5. Cottage Witch — 1.19.2 Forge, 297 mods (moddex.gg) -> cottagewitch_mods.txt
6. Homestead — 1.20.1 Fabric, 341 mods (partial: Tectonic, Geophilic, Repurposed Structures, YUNG, Nature's Spirit, BWG, FD, Let's Do, Chipped, Twigs, Cluttered, Beautify, Sophisticated Backpacks, Create, Tom's)
7. Mayview — 1.21.1 NeoForge, 1.1.2c (2026-04-20), partial (Tectonic, BWG, YUNG, Moog's, Fresh Animations, ETF, NEA, Subtle Effects, Selling Bin, Daily Shop, Spud's Shops, Immersive Aircraft, Create, Small Ships, Macaw's, Another Furniture, Handcrafted, FramedBlocks, Chimes, FD, Let's Do, Slice&Dice, C&A, CEI)
8. WitchHazel Halloween Magic — 1.21.1 NeoForge v2.0.0 (2026-09-05), partial magic list (Ars, Hexerei, Iron's, Malum, Nature's Aura, Occultism, Psi, Roots, Forbidden&Arcanus, Theurgy, Eternal Starlight, Dragon Mounts Remastered, Tarot Cards)
9. Medieval MC MMC5 — 1.21.1 NeoForge v33 (2026-05-04), 250+ mods, partial (BWG, WDA, Capital Cities, Taverns and Trial Dungeons, MineColonies, Iron's, Ars, Waystones, JourneyMap)
10. Prominence II — 1.20.1 Fabric v4.1.x, 656 mods, partial (RPG; Better Archeology, BoMD, Deeper and Darker, Vinery...)
11. Create: Perfect World — 1.21.1 NeoForge, Modrinth (2026-02-17) partial (Terralith, Tectonic, Serene Seasons, Dynamic Trees, Ocean's Delight, End's Delight, Immersive Sounds, Diagonal Walls/Fences/Windows, EnhancedVisuals, Spawn Animations, Integrated Farming, Copycats+)
Cisco's Fantasy Medieval RPG: 1.19.2 Forge (Lite 16f 2025-07-18), no public list -> skipped.

### Candidates verified on Modrinth API (NeoForge + 1.21.1 filter), 2026-10-17
| Mod | Packs | NF 1.21.1 version (date) | License | Deps | Overlap |
|---|---|---|---|---|---|
| Farming for Blockheads | SSV, FC5, Faewild | 21.1.14 (2026-09-25) | ARR | Balm | trough = Animal Feeding Trough; market/shipping bin/sprinklers/fertiliser/chicken nest new. Addon Fertiliser for Blockheads (MIT) -> Botany Pots |
| Overweight Farming | FE, CW | 2.2.0 (2025-11-17) | ARR | - | none |
| Smarter Farmers | FE | 2.2.4 (2025-10-18) | ARR | Moonlight | none |
| Just Enough Breeding | FE | 3.3.1 (2026-10-02) | MIT | (EMI/JEI optional) | none |
| Watering Cans [Dew Drop] | SSV | 1.0.2 (2026-08-30), only 1 release | CC-BY-NC-SA-4.0 | Bot's Lib (new) | none |
| Create Confectionery | FC5, FC6 | 1.1.3.b (2026-08-15) | MIT | Create | none |
| Ribbits | FE, SSV | 4.1.6 (2025-12-19) | LGPL-3.0 | GeckoLib, YUNG's API | +1 swamp village |
| Guard Villagers | CCDL | 2.4.12 (2026-08-30) | custom | - | low |
| Goblin Traders | CW, CCDL | 1.11.2 (2025-04-16, CF; GitHub tag v1.21.1-1.11.2) | MIT | Framework >=0.9.4 (new) | none |
| Personality (sit/crawl) | CW | 5.0.2 (2026-05-06) | Abnormals License | Blueprint | none |
| Chimes | SSV, CW, MV | 2.1.1 (2026-10-02) | ARR | - | none |
| SeasonHud | SSV | 1.21.1-2.0.10 (2026-08-31) | MIT | Serene Seasons; Xaero opt | none |
| Open Together (Fuzs) | (FC5 uses Double Doors) | 21.1.2 (2026-09-10) | MPL-2.0 | Puzzles Lib | none |
| Every Compat | SSV, FC5 | 1.21-2.11.52 (2026-09-17) | ARR | Moonlight | modules: handcrafted, storagedrawers, botanypots, farmersdelight, create, rechiseled, twilightforest, regions_unexplored, friendsandfoes... |
| Diagonal Fences/Walls/Windows | SSV, FC5, CW, CPW | Fences v21.1.1 (2024-11-18) | MPL-2.0 | Puzzles Lib | none |
| Macaw's Roofs (+Bridges/Paths/Windows) | FC5, MV, CW, CCDL | Roofs 2.3.2 (2025-05-04) | ARR (Paths/Fences/Doors MIT) | - | low |
| Twigs | SSV, HS | 1.21.1-3.1.2 (2026-06-03) | ARR | - | low (small decor) |
| Dramatic Doors | SSV, CW | 1.21.1-3.3.2 (2025-05-01) | MIT | - | none |
| Better Archeology | SSV, P2 | 1.21.1-1.3.8 (2026-08-04) | MIT | Architectury, Resourceful Config | none |
| Paragliders | SSV (FC5 Hang Glider) | 21.1.5 (2026-03-22) | GPL-3.0+ | - | stamina wheel |
| Small Ships | SSV, MV | 2.0.2 (2026-10-16) | ARR | - | none |
| Exposure | SSV (FC5/CW Camera Mod) | 1.9.19 (2026-09-23) | MIT | - | none |
Rejected after check: Cosmetic Armor Reworked (no NF 1.21.1 file), Falling Leaves (Subtle Effects already), Mob Lassos (Carry On), Domestication Innovation (only fork Redomesticate 1.10.1 GPL), Autumnity/Environmental (biomes vs RU), Incubation (FfB nest), Quality Food 2.3.6 MIT (stack splitting), Cooking for Blockheads 21.1.24 (2nd kitchen), Better Advancements (beta 0.4.3.21), Villager Names 8.5 (needs Collective), Beautify 2.0.2 (2024-11; hanging pots ~Supplementaries), Cluttered 3.0.3 (furniture ~Handcrafted), Night Lights 1.3.0.
