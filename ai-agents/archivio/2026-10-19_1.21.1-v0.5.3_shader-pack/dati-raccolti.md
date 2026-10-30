# Pacchetti di shader: dati grezzi raccolti (19/10/2026, versione 0.5.3)

Dati letti dall'API di Modrinth e dai sorgenti su GitHub mentre si sceglievano i due pacchetti di shader della 0.5.3. Il distillato è in `1.21.1/lavoro/versioni/v0.5.3.md`; le schede in `1.21.1/mod-knowledge/`.

## Ricerca su Modrinth: shader per la 1.21.1, ordinati per download

`/v2/search?facets=[["project_type:shader"],["versions:1.21.1"]]&index=downloads&limit=20`

| slug | project_id | titolo | download | licenza | ultima modifica | latest_version |
|---|---|---|---|---|---|---|
| complementary-reimagined | HVnmMxH1 | Complementary Shaders - Reimagined | 60329720 | LicenseRef-Custom | 2026-05-21 | yCCduG44 |
| complementary-unbound | R6NEzAwj | Complementary Shaders - Unbound | 39241242 | LicenseRef-Custom | 2026-05-21 | VMHXIk50 |
| bsl-shaders | Q1vvjJYV | BSL Shaders | 26741517 | LicenseRef-All-Rights-Reserved | 2026-04-20 | hIibTfxn |
| photon-shader | lLqFfGNs | Photon Shaders | 23743452 | LicenseRef- | 2026-04-14 | gUv7fBPN |
| solas-shader | EpQFjzrQ | Solas Shader | 15195870 | LicenseRef-All-Rights-Reserved | 2026-07-01 | WcoEHPPx |
| bliss-shader | ZvMtQlho | Bliss Shaders | 12885261 | LicenseRef-All-Rights-Reserved | 2025-11-23 | kC2Y8q1P |
| rethinking-voxels | kmwfVOoi | Rethinking Voxels | 11904084 | LicenseRef-Complementary-Agreement | 2025-06-19 | cpD4esk9 |
| makeup-ultra-fast-shaders | izsIPI7a | MakeUp - Ultra Fast | 11383883 | LGPL-3.0-or-later | 2026-06-27 | zt4eHisU |
| super-duper-vanilla | LMIZZNxZ | Super Duper Vanilla | 7303567 | LicenseRef-FlameRender-TM-Studios-License | 2025-07-08 | KB0sOLSc |
| insanity-shader | EQWX2WiO | Insanity Shader | 6656990 | LicenseRef-AGNYA-License | 2024-06-13 | TK0ZSsk0 |
| mellow | BUxf36AP | Mellow | 5414465 | MIT | 2026-07-28 | y6zWED9s |
| astralex | RphJSnEs | AstraLex Shaders | 4353931 | LicenseRef-All-Rights-Reserved | 2024-06-16 | qSbtQS2o |
| miniature-shader | UaS8ROxa | Miniature Shader | 4062589 | MIT | 2026-07-29 | LWmZ94RG |
| nostalgia-shader | xEItlMn3 | Nostalgia Shader | 3923512 | LicenseRef-All-Rights-Reserved | 2025-02-28 | fzxeGgx7 |
| hysteria-shaders | iHC8BZn4 | Hysteria Shaders | 3083950 | LicenseRef-AGNYA-License | 2024-08-02 | u7oNAXa5 |
| kappa-shader | Y8161YLz | Kappa Shader | 2846544 | LicenseRef-All-Rights-Reserved | 2025-02-28 | 8p4viq8V |
| spooklementary | 6uJCfiCH | Spooklementary | 2699701 | LicenseRef-Complementary-License | 2025-12-05 | rcr90eRP |
| noble | sclYVqbt | Noble Shaders | 2006800 | GPL-3.0-only | 2026-07-22 | 3cIADbit |
| bsl-shaders-classic | pgzM6RBY | BSL Shaders - Classic | 1996988 | LicenseRef-All-Rights-Reserved | 2025-05-10 | a05qYRrG |
| visual-vibrance | l6Uqs2fS | Visual Vibrance | 1982101 | LicenseRef-- | 2026-02-01 | zGC385Y8 |

## Versioni per Iris + 1.21.1

Complementary Reimagined: r5.9.3 `Bqen1mJX` (release, 2026-09-15, `ComplementaryReimagined_r5.9.3.zip`, 553 KB) · r5.9.2 `vxxxESqv` (2026-09-14) · r5.9.1 `ErCjThzb` (2026-09-11) · r5.9 `111gsk0f` (2026-09-02) · r5.8.1 `yCCduG44` (2026-05-21). Loader: iris, optifine. Changelog r5.9.x: supporto a Minecraft 26.2, nebbia nelle Sulfur Caves, frame rate migliori, cielo diurno ritoccato, riflessi volumetrici nell'End, profili ad alte prestazioni ribilanciati. r5.8.1: supporto a Voxy, luci volumetriche riscritte, End rifatto.

Complementary Unbound: r5.9.1 `UhZjVKiD` (2026-09-11) · r5.9 `w6dISYOd` · r5.8.1 `VMHXIk50`.

MakeUp - Ultra Fast: 9.5g `pgb0JjoN` (release, 2026-10-04, 405 KB; Iris: nuovo glint degli incantamenti, portale dell'End) · 9.5f `IUFkxmHz` (2026-09-27; blocchi della 26.3, russo) · 9.5e `T3EhqZo1` (2026-09-05; ombre pixel-locked dei traslucidi).

## Licenza di Complementary (License.txt nel sorgente, "Complementary License Agreement 1.7")

Punto 1.2: ammesso nei modpack se (a) accreditato nella descrizione del pack quando è acceso di serie, (b) l'autore del pack si assume i problemi, (c) **il contenuto non è modificato in alcun modo, nemmeno variabili o blocchi aggiunti**, (d) aggiunto tramite i sistemi di Modrinth o CurseForge, mai con un upload diretto.

## Sorgente di Complementary Reimagined (GitHub ComplementaryDevelopment/ComplementaryReimagined, r5.9.2 c09950d)

- `shaders/block.properties`: 508 righe, solo id `minecraft:`; nessun namespace di mod. Commento in testa: invita a aggiungere i blocchi modded nelle sezioni foglie, fogliame, minerali, luci.
- `shaders/colorwheel.properties` e programmi `world1/clrwl_*`, `#ifdef GBUFFERS_COLORWHEEL` in `gbuffers_terrain.glsl`: supporto a Colorwheel.
- `shaders.properties`: `iris.features.optional = CUSTOM_IMAGES SSBO BLOCK_EMISSION_ATTRIBUTE FADE_VARIABLE ENTITY_TRANSLUCENT`; controlli `IRIS_VERSION` (10800, 10805, 10814, 11005, 11103) nel codice.

## Sorgente di MakeUp - Ultra Fast (GitHub javiergcim/MakeUpUltraFast, commit 13ac348 del 16/10/2026, LGPL-3.0)

`shaders/block.properties`: namespace citati (occorrenze): tfc 420, railways 246, byg 236, createframed 160, createbigcannons 131, botania 117, create 105, dtterralith 104, minecraft 95, createdeco 90, pamhc2crops 84, biomesoplenty 77, create_dd 73, simplefarming 52, pamhc2trees 49, environmental 45, dynamictrees 34, natures_spirit 32, interiors 32, cutecore 31, dense_dynamictrees 26, createcasing 26, pvj 25, handcrafted 22, atmospheric 22, thebetweenlands 17, terrestria 17, farmersdelight 17, twilightforest 16, moreflowerbushes 16, upgrade_aquatic 15, dtquark 15, extlights 13, ars_nouveau 13, extrabiomesxl 12, dtarsnouveau 10, createutilities 9, create_things_and_misc 9, cataclysm 9, betterend 9…

Confronto con l'inventario del pack (blocchi che esistono davvero): create 104/105, handcrafted 22/22, farmersdelight 17/17, twilightforest 13/16, ars_nouveau 13/13, cataclysm 9/9, create_connected 7/7, deeperdarker 4/4, occultism 4/4, undergarden 2/2, create_enchantment_industry 1/2. Le altre mod citate (byg, pamhc2crops, biomesoplenty…) non sono nel pack.

Profili (`shaders.properties`): no_effects, shadowless_low, shadowless_medium, shadowless_high, low, medium, high, extremeplus ("High (DoF)"); `profile.comment`: i profili shadowless sono per PC deboli, i tradizionali aggiungono ombre di qualità crescente.

## Colorwheel (descrizione su Modrinth)

Pacchetti supportati ufficialmente: Complementary Unbound/Reimagined (dalla r5.7), Euphoria Patches (1.7.0), Eclipse, Glimmer (v1.5), I Like Vanilla (v1.0.3), Just Colored Lighting (0.9.5), RenderPearl (v2.8.0-beta.3), Shrimple, Solas (v3.2), Spooklementary (v2.0.3), Steadfast. Non ufficiali con Colorwheel-Patcher: BSL 10.1, Bliss 2.1.x, Complementary 5.5.1–5.6.1, Euphoria 1.6.3–1.6.8, Photon 1.3a, Rethinking Voxels. Pacchetti non supportati: "fallback mode" con problemi di resa. Dipendenza obbligatoria: solo Iris/Oculus; senza Flywheel si disattiva da sola. Licenza LGPL-3.0-only.

## Enhanced Celestials 2: Shader Support (testi del codice, workflow Esamina mod)

Classi `LunarColorRenderer` (skyColor, moonColor, glowColor, getSkyLightColor, getMoonTextureColor), `LunarEffectCompute`, `NeoForgeClientHandler` (renderColorGrading, drawWithShader), `NeoForgePlatformHelper` con `net/irisshaders/iris/api/v0/IrisApi` e `isShaderPackInUse`. Nessun riferimento a pacchetti specifici. Versione nel jar: "Enhanced Celestials Shader Support v2.1.0 initializing" nel log del gioco (file 2.0.0.3).

## Photon (API di Modrinth)

Licenza propria (`LicenseRef-`, https://github.com/sixthsurge/photon/blob/main/LICENSE). La descrizione non parla di modpack né di mod; sezione "Mods" con Voxy e Distant Horizons; illuminazione colorata voxel solo con il profilo Ultra e Iris.
