> **Nota del 17/10/2026**: BotanyCompatLayer **non verrà installato** (decisione: niente datapack esterni). Le piante segnate "(e) / Solo BCL" vanno quindi scritte nel nostro datapack, eventualmente copiando i file di BotanyCompatLayer (MIT) se si recupera lo zip. Piano e regole in `datapack/conoscenze.md`.

# Copertura Botany Pots / Botany Trees delle piante del modpack (1.21.1)

Generato il 17/10/2026 dai sorgenti 1.21.1 delle mod (rami e versioni verificati, vedi in fondo). Copertura: **(a)** Botany Pots 21.1.44 nativo, **(b)** Botany Trees 21.1.7 nativo, **(c)** compat inclusa nella mod, **(d)** il nostro `matteo_tweaks`, **(e)** BotanyCompatLayer (dichiarato, contenuto non verificabile), **(f)** non coperta.

## Riepilogo

Piante censite: **526**. Coperte (a-d): **263**. Coperte solo con vecchi ID di RU (alias, da verificare): **8**. Solo BCL dichiarato (da verificare): **50**. Non coperte: **202**. Da saltare (non adatte ai vasi): **3**.

| Mod | Piante | Coperte (a-d) | Alias RU | Solo BCL? | **Non coperte** | Da saltare |
|---|---:|---:|---:|---:|---:|---:|
| Farmer's Delight 1.3.4 | 14 | 14 |  |  | **0** |  |
| Veggies Delight 1.9.3 | 15 | 14 |  |  | **1** |  |
| Expanded Delight 0.1.4 | 10 | 0 |  |  | **10** |  |
| Cultural Delights 0.19.1 | 14 | 0 |  |  | **13** | 1 |
| Farmer's Delight: Extended | nessuna pianta | | | | | |
| [Let's Do] HerbalBrews 1.1.4 | 9 | 0 |  | 9 | **0** |  |
| Delightful Fares | nessuna pianta | | | | | |
| Twilight's Flavor & Delight 3.2.6 | 3 | 0 |  |  | **3** |  |
| Undergarden Delight | nessuna pianta | | | | | |
| Cataclysm Delight | nessuna pianta | | | | | |
| Aether's Delight 0.1.4.2 | 7 | 0 |  |  | **7** |  |
| Ender's Delight 1.3.1 | 4 | 0 |  |  | **4** |  |
| Brewin' and Chewin' 4.5.0 | nessuna pianta | | | | | |
| Ars Nouveau's Flavors & Delight | nessuna pianta | | | | | |
| Occult Delight | nessuna pianta | | | | | |
| Roaster's Delight 1.0.0.1 (CurseForge, sorgente chiuso) | 5 | 0 |  |  | **5** |  |
| Rustic Delight 1.7.1 (in arrivo) | 10 | 8 |  | 2 | **0** |  |
| My Nether's Delight 1.10.4 (in arrivo) | 4 | 0 |  |  | **4** |  |
| Ocean's Delight (in arrivo) | nessuna pianta | | | | | |
| Chef's Delight (in arrivo) | nessuna pianta | | | | | |
| Create Confectionery (in arrivo) | nessuna pianta | | | | | |
| Autochef's Delight (in arrivo) | nessuna pianta | | | | | |
| Hexalia 1.3.6 | 31 | 0 |  |  | **31** |  |
| Hexerei 0.5.0.3 | 10 | 3 |  |  | **7** |  |
| Aspect Alchemy | nessuna pianta | | | | | |
| Bountiful Fares 3.0.12 | 30 | 0 |  |  | **30** |  |
| [Let's Do] Vinery 1.5.5 | 11 | 2 |  | 8 | **0** | 1 |
| [Let's Do] Meadow 1.4.9 | 11 | 3 |  | 8 | **0** |  |
| [Let's Do] Farm & Charm 1.1.28 | 20 | 0 |  | 20 | **0** |  |
| Seasonal Let's Do | nessuna pianta | | | | | |
| Snow! Real Magic! | nessuna pianta | | | | | |
| Ars Nouveau 5.13.3 | 10 | 10 |  |  | **0** |  |
| Ars Elemental (CurseForge) | 3 | 2 |  |  | **1** |  |
| Occultism 1.224.5 | 5 | 5 |  |  | **0** |  |
| Reactive 10.2.1 | 2 | 0 |  |  | **2** |  |
| Psi | nessuna pianta | | | | | |
| The Aether 1.5.10 | 5 | 2 |  | 3 | **0** |  |
| Deep Aether 1.1.5.1 | 27 | 6 |  |  | **21** |  |
| The Undergarden 0.9.6 | 24 | 3 |  |  | **21** |  |
| Deeper and Darker 1.4.1 | 12 | 11 |  |  | **1** |  |
| Unusual End 2.3.1b | 19 | 0 |  |  | **19** |  |
| The Twilight Forest 4.8.3345 (CurseForge) | 33 | 20 |  |  | **12** | 1 |
| Regions Unexplored 0.6.2 | 175 | 158 | 8 |  | **9** |  |
| Supplementaries 4.0.2 | 2 | 2 |  |  | **0** |  |
| L_Ender's Cataclysm 3.33 | nessuna pianta | | | | | |
| Friends & Foes (fuori lista, già nel pack) | 1 | 0 |  |  | **1** |  |

## Cose da sapere

- **Botany Trees 21.1.7 non copre Bountiful Fares.** La compat (8 alberi) è nel sorgente dal 3/6/2026, un giorno dopo l'ultima release: nel pack non c'è. Si possono copiare ricette e loot table `tree_drops` da BT (LGPL-2.1) nel nostro datapack.
- **Undergarden**: Botany Pots 21.1.44 ha solo i 10 terreni, nessuna coltura (fagioli, blisterberry, gloomgourd, funghi, fiori). Gli alberelli sono in Botany Trees.
- **Compat incluse nelle mod**: Veggies Delight (14 ricette) e Rustic Delight (8 ricette) sono nel formato 1.21.1 corretto; a Rustic mancano però `dark_bell_peppers` e `pale_bell_peppers`. Ars Elemental include un file **vecchio formato 1.20** (`data/botany_pots/...`, tipo `botanypots:crop` con `categories`, condizione `mod_loaded: botany_pots`) che in 1.21.1 viene ignorato: innocuo, l'alberello è comunque in Botany Trees.
- **Regions Unexplored 0.6** ha rinominato vari blocchi (leaf_pile → leaf_litter, mauve_shrub → lavender_wisteria_shrub, enchanted_birch_shrub → sky_wisteria_shrub, stone_bud/medium_grass → grass_sprouts, cactus_flower → saguaro_cactus_flower). Botany Pots usa ancora i vecchi ID (8 ricette): RU registra degli alias, quindi probabilmente funzionano, ma va controllato in gioco.
- **Brewin' and Chewin' 4.5.0** (nel pack) non ha piante; mais e uva esistono solo nel ramo di sviluppo.
- **BotanyCompatLayer**: nessun sorgente pubblico (Modrinth senza source_url, nessun repo GitHub dell'autore CptGummiball) e lo zip non è scaricabile da qui. Le piante delle mod che dichiara (Aether, Farm & Charm, HerbalBrews, Meadow, Vinery, Rustic Delight) sono segnate **(e)**: vanno verificate in gioco dopo averlo installato. Non copre Botany Trees e dice di aver escluso saplings e semi ambigui.
- **Roaster's Delight**: sorgente chiuso (ARR), ID sconosciuti. Dalla pagina CurseForge: pianta del caffè (seme: chicco non tostato), cespuglio del tè, camomilla, menta, matcha. Vanno ricavati in gioco.
- **Molti cespugli raccolti a clic destro** (Hexerei, Vinery, TF berry bush, Ender's Delight voidpepper, MND bullet pepper, Bountiful Fares tea shrub, Unusual End warped bush) hanno una loot table che dà solo la pianta o i semi: con `block_derived_crop` il vaso darebbe solo quello. Servono `drops` espliciti (indicati sotto).

Controllo in gioco consigliato (mondo di prova con i cheat, serve il livello di permesso 4): `/botanypots debug missing seeds true true` elenca ogni seme o pianta senza ricetta e scrive delle bozze JSON in `<istanza>/botanypots/generated/crops` (tiene già conto di BCL e di questo datapack); `/botanypots debug missing soils true` fa lo stesso per i terreni; `/botanypots debug check_crops` piazza un vaso sotto i piedi e segnala nel log le colture che non producono nulla (utile per scovare i drop sbagliati).

## Tabelle per mod

### Cucina

#### Farmer's Delight 1.3.4

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `farmersdelight:cabbages` | `farmersdelight:cabbage_seeds` | crop | (a) Botany Pots nativo |  |
| `farmersdelight:tomatoes` | `farmersdelight:tomato_seeds` | crop | (a) Botany Pots nativo | pianta rampicante (budding_tomatoes -> tomatoes su corda) |
| `farmersdelight:onions` | `farmersdelight:onion` | crop | (a) Botany Pots nativo |  |
| `farmersdelight:rice` | `farmersdelight:rice` | crop | (a) Botany Pots nativo | 2 blocchi (rice + rice_panicles) |
| `farmersdelight:brown_mushroom_colony` | `farmersdelight:brown_mushroom_colony` | mushroom colony | (a) Botany Pots nativo |  |
| `farmersdelight:red_mushroom_colony` | `farmersdelight:red_mushroom_colony` | mushroom colony | (a) Botany Pots nativo |  |
| `farmersdelight:wild_cabbages` | `farmersdelight:wild_cabbages` | wild crop | (a) Botany Pots nativo |  |
| `farmersdelight:wild_onions` | `farmersdelight:wild_onions` | wild crop | (a) Botany Pots nativo |  |
| `farmersdelight:wild_tomatoes` | `farmersdelight:wild_tomatoes` | wild crop | (a) Botany Pots nativo |  |
| `farmersdelight:wild_carrots` | `farmersdelight:wild_carrots` | wild crop | (a) Botany Pots nativo |  |
| `farmersdelight:wild_potatoes` | `farmersdelight:wild_potatoes` | wild crop | (a) Botany Pots nativo |  |
| `farmersdelight:wild_beetroots` | `farmersdelight:wild_beetroots` | wild crop | (a) Botany Pots nativo |  |
| `farmersdelight:wild_rice` | `farmersdelight:wild_rice` | wild crop | (a) Botany Pots nativo | alta 2 blocchi |
| `farmersdelight:sandy_shrub` | `farmersdelight:sandy_shrub` | bush | (a) Botany Pots nativo |  |

#### Veggies Delight 1.9.3

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `veggiesdelight:bellpepper_crop` | `veggiesdelight:bellpepper_seeds` | crop | (c) compat inclusa nella mod | file: botany/bellpepper.json |
| `veggiesdelight:broccoli_crop` | `veggiesdelight:broccoli_seeds` | crop | (c) compat inclusa nella mod | file: botany/broccoli.json |
| `veggiesdelight:cauliflower_crop` | `veggiesdelight:cauliflower_seeds` | crop | (c) compat inclusa nella mod | file: botany/cauliflower.json |
| `veggiesdelight:garlic_crop` | `veggiesdelight:garlic_clove` | crop | (c) compat inclusa nella mod | file: botany/garlic.json |
| `veggiesdelight:sweet_potato_crop` | `veggiesdelight:sweet_potato` | crop | (c) compat inclusa nella mod | file: botany/sweet_potato.json |
| `veggiesdelight:turnip_crop` | `veggiesdelight:turnip_seeds` | crop | (c) compat inclusa nella mod | file: botany/turnip.json |
| `veggiesdelight:zucchini_crop` | `veggiesdelight:zucchini_seeds` | crop | (c) compat inclusa nella mod | file: botany/zucchini.json |
| `veggiesdelight:wild_bellpeppers` | `veggiesdelight:wild_bellpeppers` | wild crop | (c) compat inclusa nella mod | file: botany/wild_bellpepper.json |
| `veggiesdelight:wild_broccoli` | `veggiesdelight:wild_broccoli` | wild crop | (c) compat inclusa nella mod | file: botany/wild_broccoli.json |
| `veggiesdelight:wild_cauliflowers` | `veggiesdelight:wild_cauliflowers` | wild crop | (c) compat inclusa nella mod | file: botany/wild_cauliflowers.json |
| `veggiesdelight:wild_garlic` | `veggiesdelight:wild_garlic` | wild crop | (c) compat inclusa nella mod | file: botany/wild_garlic.json |
| `veggiesdelight:wild_sweet_potatoes` | `veggiesdelight:wild_sweet_potatoes` | wild crop | (c) compat inclusa nella mod | file: botany/wild_sweet_potatoes.json |
| `veggiesdelight:wild_turnips` | `veggiesdelight:wild_turnips` | wild crop | (c) compat inclusa nella mod | file: botany/wild_turnips.json |
| `veggiesdelight:wild_zucchinis` | `veggiesdelight:wild_zucchinis` | wild crop | (c) compat inclusa nella mod | file: botany/wild_zucchinis.json |
| `veggiesdelight:mature_dandelion` | `veggiesdelight:mature_dandelion` | flower | (f) non coperta | drop dandelion_leaf; il bonemeal la duplica |

#### Expanded Delight 0.1.4

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `expandeddelight:asparagus_crop` | `expandeddelight:asparagus_seeds` | crop | (f) non coperta |  |
| `expandeddelight:chili_pepper_crop` | `expandeddelight:chili_pepper_seeds` | crop | (f) non coperta |  |
| `expandeddelight:peanut_crop` | `expandeddelight:peanut` | crop | (f) non coperta |  |
| `expandeddelight:sweet_potato_crop` | `expandeddelight:sweet_potato` | crop | (f) non coperta | stesso nome di veggiesdelight:sweet_potato ma item diverso |
| `expandeddelight:cranberry_plant` | `expandeddelight:cranberries` | water bush | (f) non coperta | si piazza sull'acqua come una ninfea (LilypadCropItem); raccolta a clic destro; loot a age=3 dà cranberries: derivato ok |
| `expandeddelight:cinnamon_sapling` | `expandeddelight:cinnamon_sapling` | sapling | (f) non coperta | albero: serve ricetta stile Botany Trees (drop cinnamon_log + sapling) |
| `expandeddelight:wild_asparagus` | `expandeddelight:wild_asparagus` | wild crop | (f) non coperta |  |
| `expandeddelight:wild_chili_pepper` | `expandeddelight:wild_chili_pepper` | wild crop | (f) non coperta |  |
| `expandeddelight:wild_peanuts` | `expandeddelight:wild_peanuts` | wild crop | (f) non coperta |  |
| `expandeddelight:wild_sweet_potato` | `expandeddelight:wild_sweet_potato` | wild crop | (f) non coperta |  |

#### Cultural Delights 0.19.1

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `culturaldelights:cucumbers` | `culturaldelights:cucumber_seeds` | crop | (f) non coperta |  |
| `culturaldelights:eggplants` | `culturaldelights:eggplant_seeds` | crop | (f) non coperta | le wild_eggplants droppano anche white_eggplant (non coltivabile a parte: il blocco white_eggplants non è registrato) |
| `culturaldelights:corn` | `culturaldelights:corn_kernels` | crop | (f) non coperta | alta 3 blocchi (proprietà height 0..2); il display di default mostra solo il blocco basso: meglio display con height; loot (height=0, age=7): corn_cob + corn_kernels |
| `culturaldelights:beans` | `culturaldelights:beans` | climbing crop | (f) non coperta | come i pomodori di FD: i semi piazzano budding_beans (age 0..4) che diventa beans su corda; usare block=beans come fa BP con farmersdelight:tomatoes; raccolta: bean_pod |
| `culturaldelights:avocado_sapling` | `culturaldelights:avocado_sapling` | sapling | (f) non coperta | albero da frutto (fruiting_avocado_leaves): ricetta stile Botany Trees |
| `culturaldelights:avocado_pit` | `culturaldelights:avocado_pit` | sapling | (f) non coperta | nocciolo = alberello (SaplingBlock con grower proprio): stessa ricetta dell'avocado |
| `culturaldelights:lemon_sapling` | `culturaldelights:lemon_sapling` | sapling | (f) non coperta | albero da frutto (fruiting_lemon_leaves): ricetta stile Botany Trees; non confondere con bountifulfares:lemon_sapling |
| `culturaldelights:wild_cucumbers` | `culturaldelights:wild_cucumbers` | wild crop | (f) non coperta |  |
| `culturaldelights:wild_eggplants` | `culturaldelights:wild_eggplants` | wild crop | (f) non coperta |  |
| `culturaldelights:wild_corn` | `culturaldelights:wild_corn` | wild crop | (f) non coperta |  |
| `culturaldelights:wild_beans` | `culturaldelights:wild_beans` | wild crop | (f) non coperta |  |
| `culturaldelights:agave` | `culturaldelights:agave` | wild herb | (f) non coperta |  |
| `culturaldelights:mint` | `culturaldelights:mint` | wild herb | (f) non coperta |  |
| `culturaldelights:magic_beans` | `culturaldelights:magic_beans` | special _(saltare)_ | (f) non coperta | fagiolo magico che genera un beanstalk gigante: non adatto ai vasi |

**Farmer's Delight: Extended**: nessuna pianta. Solo ricette/cibi (verificato: nessun blocco nel sorgente 0.2.x).

#### [Let's Do] HerbalBrews 1.1.4

_Mod dichiarata da BotanyCompatLayer: le righe (e) potrebbero essere coperte da BCL, da verificare._

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `herbalbrews:coffee_plant` | `herbalbrews:coffee_beans` | crop | (e) BCL (dichiarato, non verificato) | clic destro dà coffee_beans; loot a age=3 ok |
| `herbalbrews:tea_plant` | `herbalbrews:tea_blossom` | crop | (e) BCL (dichiarato, non verificato) | loot age=3: green_tea_leaf + tea_blossom |
| `herbalbrews:rooibos_plant` | `herbalbrews:rooibos_leaf` | crop | (e) BCL (dichiarato, non verificato) |  |
| `herbalbrews:yerba_mate_plant` | `herbalbrews:yerba_mate_leaf` | crop | (e) BCL (dichiarato, non verificato) |  |
| `herbalbrews:wild_coffee_plant` | `herbalbrews:wild_coffee_plant` | wild crop | (e) BCL (dichiarato, non verificato) |  |
| `herbalbrews:wild_rooibos_plant` | `herbalbrews:wild_rooibos_plant` | wild crop | (e) BCL (dichiarato, non verificato) |  |
| `herbalbrews:wild_yerba_mate_plant` | `herbalbrews:wild_yerba_mate_plant` | wild crop | (e) BCL (dichiarato, non verificato) |  |
| `herbalbrews:hibiscus` | `herbalbrews:hibiscus` | flower | (e) BCL (dichiarato, non verificato) |  |
| `herbalbrews:lavender` | `herbalbrews:lavender` | flower | (e) BCL (dichiarato, non verificato) |  |

**Delightful Fares**: nessuna pianta. Sorgente chiuso; da descrizione Modrinth: bollitore e tè, nessuna coltura.

#### Twilight's Flavor & Delight 3.2.6

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `twilightdelight:fiddlehead_clump` | `twilightdelight:fiddlehead_clump` | colony | (f) non coperta | colonia stile FD (MushroomColonyBlock) + parte alta fiddlehead_clump_upper; drop twilightforest:fiddlehead |
| `twilightdelight:mushgloom_colony` | `twilightdelight:mushgloom_colony` | mushroom colony | (f) non coperta | drop twilightforest:mushgloom |
| `twilightdelight:ironwood_sapling` | `twilightdelight:ironwood_sapling` | sapling | (f) non coperta | albero: ricetta stile Botany Trees |

**Undergarden Delight**: nessuna pianta. Sorgente chiuso; da descrizione: coltelli, pasti, mobili; nessuna coltura.

**Cataclysm Delight**: nessuna pianta. Verificato (sorgente 1.21.1): solo cibi, unico blocco una torta.

#### Aether's Delight 0.1.4.2

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `aethersdelight:ginger_crop` | `aethersdelight:ginger` | crop | (f) non coperta |  |
| `aethersdelight:leek_crop` | `aethersdelight:leek` | crop | (f) non coperta |  |
| `aethersdelight:parsnip_crop` | `aethersdelight:parsnip` | crop | (f) non coperta |  |
| `aethersdelight:peppermint_bush` | `aethersdelight:peppermint_bush_stem` | berry bush | (f) non coperta | come il cespuglio di bacche dell'Aether: lo stelo cresce in cespuglio; display peppermint_bush; loot del cespuglio: peppermint_bush/stem/leaf (con condizioni): meglio drops espliciti |
| `aethersdelight:wild_ginger` | `aethersdelight:wild_ginger` | wild crop | (f) non coperta |  |
| `aethersdelight:wild_leek` | `aethersdelight:wild_leek` | wild crop | (f) non coperta |  |
| `aethersdelight:wild_parsnip` | `aethersdelight:wild_parsnip` | wild crop | (f) non coperta |  |

#### Ender's Delight 1.3.1

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `endersdelight:amberveil_mushroom` | `endersdelight:amberveil` | end mushroom | (f) non coperta |  |
| `endersdelight:chorusflame_bush` | `endersdelight:chorusflame` | end bush | (f) non coperta | age 0..2 |
| `endersdelight:ethereal_saffron_bush` | `endersdelight:ethereal_saffron` | end bush | (f) non coperta |  |
| `endersdelight:voidpepper_bush` | `endersdelight:voidpepper` | end bush | (f) non coperta | block entity; proprietà pepper=true/false (BP non la imposta): drops espliciti |

**Brewin' and Chewin' 4.5.0**: nessuna pianta. 4.5.0 (versione nel pack, tag verificato): nessuna pianta. Il ramo di sviluppo (post-4.5.0) aggiunge mais e uva (corn_crop, wild_corn, red/white_grape_bush, wild_grapes): da rivedere quando esce.

**Ars Nouveau's Flavors & Delight**: nessuna pianta. Verificato: solo cibi/blocchi di cibo (usa le piante di Ars Nouveau).

**Occult Delight**: nessuna pianta. Verificato: un solo blocco (Occult Cooking Pot).

#### Roaster's Delight 1.0.0.1 (CurseForge, sorgente chiuso)

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `? (pianta del caffè; seme: chicco non tostato)` | ? | unknown | (f) non coperta | ID sconosciuti (sorgente chiuso, ARR): ricavarli in gioco con /botanypots debug missing seeds |
| `? (cespuglio del tè)` | ? | unknown | (f) non coperta | ID sconosciuti (sorgente chiuso, ARR): ricavarli in gioco con /botanypots debug missing seeds |
| `? (camomilla)` | ? | unknown | (f) non coperta | ID sconosciuti (sorgente chiuso, ARR): ricavarli in gioco con /botanypots debug missing seeds |
| `? (menta)` | ? | unknown | (f) non coperta | ID sconosciuti (sorgente chiuso, ARR): ricavarli in gioco con /botanypots debug missing seeds |
| `? (matcha)` | ? | unknown | (f) non coperta | ID sconosciuti (sorgente chiuso, ARR): ricavarli in gioco con /botanypots debug missing seeds |

#### Rustic Delight 1.7.1 (in arrivo)

_Mod dichiarata da BotanyCompatLayer: le righe (e) potrebbero essere coperte da BCL, da verificare._

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `rusticdelight:bell_peppers` | `rusticdelight:bell_pepper_seeds` | crop | (c) compat inclusa nella mod | file: recipe/rusticdelight/crop/bell_peppers.json |
| `rusticdelight:coffee` | `rusticdelight:coffee_beans` | crop | (c) compat inclusa nella mod | file: recipe/rusticdelight/crop/coffee.json |
| `rusticdelight:cotton` | `rusticdelight:cotton_seeds` | crop | (c) compat inclusa nella mod | file: recipe/rusticdelight/crop/cotton.json |
| `rusticdelight:wild_bell_peppers` | `rusticdelight:wild_bell_peppers` | wild crop | (c) compat inclusa nella mod | file: recipe/rusticdelight/crop/wild_bell_peppers.json |
| `rusticdelight:wild_coffee` | `rusticdelight:wild_coffee` | wild crop | (c) compat inclusa nella mod | file: recipe/rusticdelight/crop/wild_coffee.json |
| `rusticdelight:wild_cotton` | `rusticdelight:wild_cotton` | wild crop | (c) compat inclusa nella mod | file: recipe/rusticdelight/crop/wild_cotton.json |
| `rusticdelight:wild_dark_bell_peppers` | `rusticdelight:wild_dark_bell_peppers` | wild crop | (c) compat inclusa nella mod | file: recipe/rusticdelight/crop/wild_dark_bell_peppers.json |
| `rusticdelight:wild_pale_bell_peppers` | `rusticdelight:wild_pale_bell_peppers` | wild crop | (c) compat inclusa nella mod | file: recipe/rusticdelight/crop/wild_pale_bell_peppers.json |
| `rusticdelight:dark_bell_peppers` | `rusticdelight:dark_bell_pepper_seeds` | crop | (e) BCL (dichiarato, non verificato) | mancante nella compat inclusa nella mod |
| `rusticdelight:pale_bell_peppers` | `rusticdelight:pale_bell_pepper_seeds` | crop | (e) BCL (dichiarato, non verificato) | mancante nella compat inclusa nella mod |

#### My Nether's Delight 1.10.4 (in arrivo)

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `mynethersdelight:bullet_pepper` | `mynethersdelight:bullet_pepper` | nether bush | (f) non coperta | PowderyFlowerBlock age 0..3 + proprietà lit; raccolta a clic destro; sopravvive su #mynethersdelight:powdery_cannon_plantable_on (netherrack, nylium, sabbia, terra, soul soil, magma) |
| `mynethersdelight:powdery_cannon` | `mynethersdelight:powder_cannon` | cane | (f) non coperta | multi-blocco tipo bambù (powdery_chubby_sapling -> powdery_cannon/powdery_cane); display come il bambù di BP |
| `mynethersdelight:crimson_fungus_colony` | `mynethersdelight:crimson_fungus_colony` | fungus colony | (f) non coperta | drop minecraft:crimson_fungus |
| `mynethersdelight:warped_fungus_colony` | `mynethersdelight:warped_fungus_colony` | fungus colony | (f) non coperta | drop minecraft:warped_fungus |

**Ocean's Delight (in arrivo)**: nessuna pianta. Verificato: solo cibi.

**Chef's Delight (in arrivo)**: nessuna pianta. Sorgente chiuso; da descrizione: villici cuoco/chef, nessuna pianta.

**Create Confectionery (in arrivo)**: nessuna pianta. Sorgente chiuso (MCreator); da descrizione: cioccolato, nessuna pianta.

**Autochef's Delight (in arrivo)**: nessuna pianta. Verificato: solo mixin, nessuna risorsa.

### Natura

#### Hexalia 1.3.6

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `hexalia:mandrake_crop` | `hexalia:mandrake_seeds` | crop | (f) non coperta |  |
| `hexalia:rabbage_crop` | `hexalia:rabbage_seeds` | crop | (f) non coperta |  |
| `hexalia:sunfire_tomato_crop` | `hexalia:sunfire_tomato_seeds` | crop | (f) non coperta |  |
| `hexalia:chillberry_bush` | `hexalia:chillberries` | berry bush | (f) non coperta | loot a age=3: chillberries |
| `hexalia:saltsprout` | `hexalia:saltsprout` | bush | (f) non coperta | sabbia o infused_farmland; age 0..2 |
| `hexalia:galeberries_vine` | `hexalia:galeberries` | hanging vine | (f) non coperta | tipo cave vines (appesa): rotation X_180; BP imposta berries=true da solo |
| `hexalia:wild_mandrake` | `hexalia:wild_mandrake` | wild crop | (f) non coperta | loot: mandrake_seeds |
| `hexalia:wild_sunfire_tomato` | `hexalia:wild_sunfire_tomato` | wild crop | (f) non coperta | loot: sunfire_tomato_seeds |
| `hexalia:aegiflora` | `hexalia:aegiflora` | flower | (f) non coperta |  |
| `hexalia:astrylis` | `hexalia:astrylis` | flower | (f) non coperta |  |
| `hexalia:begonia` | `hexalia:begonia` | flower | (f) non coperta |  |
| `hexalia:celestial_bloom` | `hexalia:celestial_bloom` | flower | (f) non coperta |  |
| `hexalia:dahlia` | `hexalia:dahlia` | flower | (f) non coperta |  |
| `hexalia:ghost_fern` | `hexalia:ghost_fern` | flower | (f) non coperta |  |
| `hexalia:grimshade` | `hexalia:grimshade` | flower | (f) non coperta |  |
| `hexalia:lavender` | `hexalia:lavender` | flower | (f) non coperta |  |
| `hexalia:lourdes` | `hexalia:lourdes` | flower | (f) non coperta |  |
| `hexalia:morphora` | `hexalia:morphora` | flower | (f) non coperta |  |
| `hexalia:nautilite` | `hexalia:nautilite` | flower | (f) non coperta |  |
| `hexalia:nightshade_bush` | `hexalia:nightshade_bush` | flower | (f) non coperta |  |
| `hexalia:spirit_bloom` | `hexalia:spirit_bloom` | flower | (f) non coperta |  |
| `hexalia:witchweed` | `hexalia:witchweed` | flower | (f) non coperta |  |
| `hexalia:withered_aegiflora` | `hexalia:withered_aegiflora` | flower _(bassa priorità)_ | (f) non coperta |  |
| `hexalia:withered_celestial_bloom` | `hexalia:withered_celestial_bloom` | flower _(bassa priorità)_ | (f) non coperta |  |
| `hexalia:windsong` | `hexalia:windsong` | flower _(bassa priorità)_ | (f) non coperta | ha un block entity (si attiva col Hex Focus): solo estetica nel vaso |
| `hexalia:dreamshroom` | `hexalia:dreamshroom` | mushroom | (f) non coperta |  |
| `hexalia:pale_mushroom` | `hexalia:pale_mushroom` | mushroom | (f) non coperta | flower_amount 1..4 (tipo pink petals) |
| `hexalia:lotus_flower` | `hexalia:lotus_flower` | water plant | (f) non coperta | ninfea (WaterlilyBlock) |
| `hexalia:siren_kelp` | `hexalia:siren_kelp` | water plant | (f) non coperta | tipo seagrass |
| `hexalia:cottonwood_sapling` | `hexalia:cottonwood_sapling` | sapling | (f) non coperta | albero: ricetta stile Botany Trees |
| `hexalia:willow_sapling` | `hexalia:willow_sapling` | sapling | (f) non coperta | albero: ricetta stile Botany Trees (diverso dal salice di Hexerei) |

#### Hexerei 0.5.0.3

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `hexerei:mandrake_plant` | `hexerei:mandrake_plant` | herb bush | (f) non coperta | PickablePlant age 0..3: i prodotti si raccolgono a clic destro, il loot dà solo la pianta |
| `hexerei:belladonna_plant` | `hexerei:belladonna_plant` | herb bush | (f) non coperta | PickablePlant age 0..3 |
| `hexerei:mugwort_bush` | `hexerei:mugwort_bush` | herb bush | (f) non coperta | doppia altezza (half lower/upper) + age 0..3 |
| `hexerei:yellow_dock_bush` | `hexerei:yellow_dock_bush` | herb bush | (f) non coperta | doppia altezza (half lower/upper) + age 0..3 |
| `hexerei:sage_crop` | `hexerei:sage_seed` | crop | (f) non coperta |  |
| `hexerei:willow_vines` | `hexerei:willow_vines` | hanging vine _(bassa priorità)_ | (f) non coperta | liana appesa (GrowingPlantHead): rotation X_180 |
| `hexerei:flowering_lily_pad` | `hexerei:flowering_lily_pad` | water plant | (f) non coperta |  |
| `hexerei:mahogany_sapling` | `hexerei:mahogany_sapling` | sapling | (b) Botany Trees nativo |  |
| `hexerei:willow_sapling` | `hexerei:willow_sapling` | sapling | (b) Botany Trees nativo |  |
| `hexerei:witch_hazel_sapling` | `hexerei:witch_hazel_sapling` | sapling | (b) Botany Trees nativo |  |

**Aspect Alchemy**: nessuna pianta. Verificato: solo calderoni.

#### Bountiful Fares 3.0.12

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `bountifulfares:apple_sapling` | `bountifulfares:apple_sapling` | sapling | (f) non coperta (BT solo nel sorgente, non nella 21.1.7) | Botany Trees ha la compat nel sorgente (commit 3/6/2026) ma NON nella 21.1.7 rilasciata: copiare ricetta + loot table tree_drops da BT (LGPL-2.1) |
| `bountifulfares:golden_apple_sapling` | `bountifulfares:golden_apple_sapling` | sapling | (f) non coperta (BT solo nel sorgente, non nella 21.1.7) | Botany Trees ha la compat nel sorgente (commit 3/6/2026) ma NON nella 21.1.7 rilasciata: copiare ricetta + loot table tree_drops da BT (LGPL-2.1) |
| `bountifulfares:hoary_apple_sapling` | `bountifulfares:hoary_apple_sapling` | sapling | (f) non coperta (BT solo nel sorgente, non nella 21.1.7) | Botany Trees ha la compat nel sorgente (commit 3/6/2026) ma NON nella 21.1.7 rilasciata: copiare ricetta + loot table tree_drops da BT (LGPL-2.1) |
| `bountifulfares:lemon_sapling` | `bountifulfares:lemon_sapling` | sapling | (f) non coperta (BT solo nel sorgente, non nella 21.1.7) | Botany Trees ha la compat nel sorgente (commit 3/6/2026) ma NON nella 21.1.7 rilasciata: copiare ricetta + loot table tree_drops da BT (LGPL-2.1) |
| `bountifulfares:orange_sapling` | `bountifulfares:orange_sapling` | sapling | (f) non coperta (BT solo nel sorgente, non nella 21.1.7) | Botany Trees ha la compat nel sorgente (commit 3/6/2026) ma NON nella 21.1.7 rilasciata: copiare ricetta + loot table tree_drops da BT (LGPL-2.1) |
| `bountifulfares:palm_sapling` | `bountifulfares:coconut` | sapling | (f) non coperta (BT solo nel sorgente, non nella 21.1.7) | Botany Trees ha la compat nel sorgente (commit 3/6/2026) ma NON nella 21.1.7 rilasciata: copiare ricetta + loot table tree_drops da BT (LGPL-2.1) |
| `bountifulfares:plum_sapling` | `bountifulfares:plum_sapling` | sapling | (f) non coperta (BT solo nel sorgente, non nella 21.1.7) | Botany Trees ha la compat nel sorgente (commit 3/6/2026) ma NON nella 21.1.7 rilasciata: copiare ricetta + loot table tree_drops da BT (LGPL-2.1) |
| `bountifulfares:walnut_sapling` | `bountifulfares:walnut_sapling` | sapling | (f) non coperta (BT solo nel sorgente, non nella 21.1.7) | Botany Trees ha la compat nel sorgente (commit 3/6/2026) ma NON nella 21.1.7 rilasciata: copiare ricetta + loot table tree_drops da BT (LGPL-2.1) |
| `bountifulfares:leeks` | `bountifulfares:leek_seeds` | crop | (f) non coperta |  |
| `bountifulfares:maize_crop` | `bountifulfares:maize_seeds` | crop | (f) non coperta | alta 2 blocchi (half lower/upper) |
| `bountifulfares:hoary_apple_sapling_crop` | `bountifulfares:hoary_seeds` | special _(bassa priorità)_ | (f) non coperta | i semi crescono (age 0..1) e diventano un alberello di melo canuto |
| `bountifulfares:tea_shrub` | `bountifulfares:tea_berries` | bush | (f) non coperta | age 0..4 + berries; foglie con le cesoie, bacche col bonemeal |
| `bountifulfares:scorchkin_stem` | `bountifulfares:scorchkin_seeds` | stem crop | (f) non coperta | stelo APPESO al soffitto che fa crescere il frutto scorchkin sotto, solo vicino alla lava |
| `bountifulfares:spongekin_stem` | `bountifulfares:spongekin_seeds` | stem crop | (f) non coperta | stelo subacqueo; il frutto spongekin cresce sopra |
| `bountifulfares:spongekin_sprout` | `bountifulfares:spongekin_sprout` | water plant _(bassa priorità)_ | (f) non coperta | loot: spongekin_seeds |
| `trellis:elderberry` | `bountifulfares:elderberries` | trellis crop | (f) non coperta | coltura su graticcio (data-driven, nessun blocco dedicato): serve ricetta botanypots:crop con display a scelta (es. wild_*_vine o il graticcio) |
| `trellis:lapisberry` | `bountifulfares:lapisberry_seeds` | trellis crop | (f) non coperta | coltura su graticcio (data-driven, nessun blocco dedicato): serve ricetta botanypots:crop con display a scelta (es. wild_*_vine o il graticcio) |
| `trellis:passion_fruit` | `bountifulfares:passion_fruit` | trellis crop | (f) non coperta | coltura su graticcio (data-driven, nessun blocco dedicato): serve ricetta botanypots:crop con display a scelta (es. wild_*_vine o il graticcio) |
| `bountifulfares:chamomile_flowers` | `bountifulfares:chamomile_flowers` | flower | (f) non coperta |  |
| `bountifulfares:honeysuckle` | `bountifulfares:honeysuckle` | flower | (f) non coperta |  |
| `bountifulfares:violet_bellflower` | `bountifulfares:violet_bellflower` | flower | (f) non coperta |  |
| `bountifulfares:prismarine_blossom` | `bountifulfares:prismarine_blossom` | water plant | (f) non coperta | loot: prismarine_crystals/shard |
| `bountifulfares:wild_beetroots` | `bountifulfares:wild_beetroots` | wild crop | (f) non coperta |  |
| `bountifulfares:wild_carrots` | `bountifulfares:wild_carrots` | wild crop | (f) non coperta |  |
| `bountifulfares:wild_potatoes` | `bountifulfares:wild_potatoes` | wild crop | (f) non coperta |  |
| `bountifulfares:wild_wheat` | `bountifulfares:wild_wheat` | wild crop | (f) non coperta |  |
| `bountifulfares:wild_leeks` | `bountifulfares:wild_leeks` | wild crop | (f) non coperta |  |
| `bountifulfares:wild_maize` | `bountifulfares:wild_maize` | wild crop | (f) non coperta | alta 2 blocchi |
| `bountifulfares:wild_elderberry_vine` | `bountifulfares:wild_elderberry_vine` | wild crop | (f) non coperta |  |
| `bountifulfares:wild_passion_fruit_vine` | `bountifulfares:wild_passion_fruit_vine` | wild crop | (f) non coperta |  |

#### [Let's Do] Vinery 1.5.5

_Mod dichiarata da BotanyCompatLayer: le righe (e) potrebbero essere coperte da BCL, da verificare._

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `vinery:red_grape_bush` | `vinery:red_grape_seeds` | berry bush | (e) BCL (dichiarato, non verificato) | uva a clic destro: il loot dà solo i semi |
| `vinery:savanna_grape_bush_red` | `vinery:savanna_grape_seeds_red` | berry bush | (e) BCL (dichiarato, non verificato) | luce minima 14 |
| `vinery:taiga_grape_bush_red` | `vinery:taiga_grape_seeds_red` | berry bush | (e) BCL (dichiarato, non verificato) | nel mondo vuole podzol/coarse dirt vicino |
| `vinery:jungle_grape_bush_red` | `vinery:jungle_grape_seeds_red` | vine bush | (e) BCL (dichiarato, non verificato) | è una liana (VineBlock) attaccata di lato: display da sistemare (rotazione/offset) |
| `vinery:white_grape_bush` | `vinery:white_grape_seeds` | berry bush | (e) BCL (dichiarato, non verificato) | uva a clic destro: il loot dà solo i semi |
| `vinery:savanna_grape_bush_white` | `vinery:savanna_grape_seeds_white` | berry bush | (e) BCL (dichiarato, non verificato) | luce minima 14 |
| `vinery:taiga_grape_bush_white` | `vinery:taiga_grape_seeds_white` | berry bush | (e) BCL (dichiarato, non verificato) | nel mondo vuole podzol/coarse dirt vicino |
| `vinery:jungle_grape_bush_white` | `vinery:jungle_grape_seeds_white` | vine bush | (e) BCL (dichiarato, non verificato) | è una liana (VineBlock) attaccata di lato: display da sistemare (rotazione/offset) |
| `vinery:grapevine_stem` | `vinery:grapevine_stem` | special _(saltare)_ | (e) BCL (dichiarato, non verificato) | vite su graticcio (lattice): sistema a più blocchi, meglio usare i cespugli |
| `vinery:apple_tree_sapling` | `vinery:apple_tree_sapling` | sapling | (b) Botany Trees nativo |  |
| `vinery:dark_cherry_sapling` | `vinery:dark_cherry_sapling` | sapling | (b) Botany Trees nativo |  |

#### [Let's Do] Meadow 1.4.9

_Mod dichiarata da BotanyCompatLayer: le righe (e) potrebbero essere coperte da BCL, da verificare._

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `meadow:alpine_poppy` | `meadow:alpine_poppy` | flower | (e) BCL (dichiarato, non verificato) |  |
| `meadow:delphinium` | `meadow:delphinium` | flower | (e) BCL (dichiarato, non verificato) |  |
| `meadow:enzian` | `meadow:enzian` | flower | (e) BCL (dichiarato, non verificato) |  |
| `meadow:eriophorum` | `meadow:eriophorum` | flower | (e) BCL (dichiarato, non verificato) |  |
| `meadow:fire_lily` | `meadow:fire_lily` | flower | (e) BCL (dichiarato, non verificato) |  |
| `meadow:saxifrage` | `meadow:saxifrage` | flower | (e) BCL (dichiarato, non verificato) |  |
| `meadow:tall_eriophorum` | `meadow:tall_eriophorum` | tall flower | (e) BCL (dichiarato, non verificato) | alta 2 blocchi |
| `meadow:small_fir` | `meadow:small_fir` | tall plant _(bassa priorità)_ | (e) BCL (dichiarato, non verificato) | alta 2 blocchi |
| `meadow:alpine_birch_sapling` | `meadow:alpine_birch_sapling` | sapling | (b) Botany Trees nativo |  |
| `meadow:pine_sapling` | `meadow:pine_sapling` | sapling | (b) Botany Trees nativo |  |
| `meadow:yellow_pine_sapling` | `meadow:yellow_pine_sapling` | sapling | (b) Botany Trees nativo |  |

#### [Let's Do] Farm & Charm 1.1.28

_Mod dichiarata da BotanyCompatLayer: le righe (e) potrebbero essere coperte da BCL, da verificare._

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `farm_and_charm:barley_crop` | `farm_and_charm:barley_seeds` | crop | (e) BCL (dichiarato, non verificato) |  |
| `farm_and_charm:corn_crop` | `farm_and_charm:kernels` | crop | (e) BCL (dichiarato, non verificato) |  |
| `farm_and_charm:lettuce_crop` | `farm_and_charm:lettuce_seeds` | crop | (e) BCL (dichiarato, non verificato) | big/giant: il derivato prende lo stato normale |
| `farm_and_charm:oat_crop` | `farm_and_charm:oat_seeds` | crop | (e) BCL (dichiarato, non verificato) |  |
| `farm_and_charm:onion_crop` | `farm_and_charm:onion` | crop | (e) BCL (dichiarato, non verificato) |  |
| `farm_and_charm:strawberry_crop` | `farm_and_charm:strawberry_seeds` | crop | (e) BCL (dichiarato, non verificato) |  |
| `farm_and_charm:tomato_crop` | `farm_and_charm:tomato_seeds` | climbing crop | (e) BCL (dichiarato, non verificato) | rampicante con corda (tomato_crop + tomato_crop_body); il loot dà anche farm_and_charm:rope se supported |
| `farm_and_charm:wild_barley` | `farm_and_charm:wild_barley` | wild crop | (e) BCL (dichiarato, non verificato) |  |
| `farm_and_charm:wild_beetroots` | `farm_and_charm:wild_beetroots` | wild crop | (e) BCL (dichiarato, non verificato) |  |
| `farm_and_charm:wild_carrots` | `farm_and_charm:wild_carrots` | wild crop | (e) BCL (dichiarato, non verificato) |  |
| `farm_and_charm:wild_emmer` | `farm_and_charm:wild_emmer` | wild crop | (e) BCL (dichiarato, non verificato) |  |
| `farm_and_charm:wild_lettuce` | `farm_and_charm:wild_lettuce` | wild crop | (e) BCL (dichiarato, non verificato) |  |
| `farm_and_charm:wild_nettle` | `farm_and_charm:wild_nettle` | wild crop | (e) BCL (dichiarato, non verificato) |  |
| `farm_and_charm:wild_oat` | `farm_and_charm:wild_oat` | wild crop | (e) BCL (dichiarato, non verificato) |  |
| `farm_and_charm:wild_onions` | `farm_and_charm:wild_onions` | wild crop | (e) BCL (dichiarato, non verificato) |  |
| `farm_and_charm:wild_potatoes` | `farm_and_charm:wild_potatoes` | wild crop | (e) BCL (dichiarato, non verificato) |  |
| `farm_and_charm:wild_ribwort` | `farm_and_charm:wild_ribwort` | wild crop | (e) BCL (dichiarato, non verificato) |  |
| `farm_and_charm:wild_strawberries` | `farm_and_charm:wild_strawberries` | wild crop | (e) BCL (dichiarato, non verificato) |  |
| `farm_and_charm:wild_tomatoes` | `farm_and_charm:wild_tomatoes` | wild crop | (e) BCL (dichiarato, non verificato) |  |
| `farm_and_charm:wild_corn` | `farm_and_charm:wild_corn` | wild crop | (e) BCL (dichiarato, non verificato) | alta 2 blocchi |

**Seasonal Let's Do**: nessuna pianta. Solo compatibilità stagioni per i Let's Do.

**Snow! Real Magic!**: nessuna pianta. Nessuna pianta nuova (cambia solo neve e piante esistenti).

### Magia

#### Ars Nouveau 5.13.3

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `ars_nouveau:magebloom_crop` | `ars_nouveau:magebloom_crop` | crop | (d) matteo_tweaks | file: crop/ars_magebloom.json |
| `ars_nouveau:sourceberry_bush` | `ars_nouveau:sourceberry_bush` | berry bush | (d) matteo_tweaks | file: crop/ars_sourceberry.json |
| `ars_nouveau:bombegranate_pod` | `ars_nouveau:bombegranate_pod` | pod | (d) matteo_tweaks | file: crop/bombegranate_pod.json |
| `ars_nouveau:bastion_pod` | `ars_nouveau:bastion_pod` | pod | (d) matteo_tweaks | file: crop/bastion_pod.json |
| `ars_nouveau:frostaya_pod` | `ars_nouveau:frostaya_pod` | pod | (d) matteo_tweaks | file: crop/frostaya_pod.json |
| `ars_nouveau:mendosteen_pod` | `ars_nouveau:mendosteen_pod` | pod | (d) matteo_tweaks | file: crop/mendosteen_pod.json |
| `ars_nouveau:blue_archwood_sapling` | `ars_nouveau:blue_archwood_sapling` | sapling | (b) Botany Trees nativo |  |
| `ars_nouveau:green_archwood_sapling` | `ars_nouveau:green_archwood_sapling` | sapling | (b) Botany Trees nativo |  |
| `ars_nouveau:purple_archwood_sapling` | `ars_nouveau:purple_archwood_sapling` | sapling | (b) Botany Trees nativo |  |
| `ars_nouveau:red_archwood_sapling` | `ars_nouveau:red_archwood_sapling` | sapling | (b) Botany Trees nativo |  |

#### Ars Elemental (CurseForge)

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `ars_elemental:flashpine_pod` | `ars_elemental:flashpine_pod` | pod | (d) matteo_tweaks | file: crop/flashpine_pod.json |
| `ars_elemental:yellow_archwood_sapling` | `ars_elemental:yellow_archwood_sapling` | sapling | (b) Botany Trees nativo | la mod include anche data/botany_pots/recipe/ars_elemental/flashing_archwood.json: formato 1.20 (botanypots:crop con categories) in namespace sbagliato botany_pots e condizione mod_loaded 'botany_pots': ignorato in 1.21.1 |
| `ars_elemental:sparkflower` | `ars_elemental:sparkflower` | flower | (f) non coperta |  |

#### Occultism 1.224.5

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `occultism:datura` | `occultism:datura_seeds` | crop | (a) Botany Pots nativo |  |
| `occultism:otherflower` | `occultism:otherflower` | flower | (a) Botany Pots nativo |  |
| `occultism:otherflower_natural` | `occultism:otherflower_natural` | flower | (a) Botany Pots nativo |  |
| `occultism:otherworld_sapling` | `occultism:otherworld_sapling` | sapling | (b) Botany Trees nativo |  |
| `occultism:otherworld_sapling_natural` | `occultism:otherworld_sapling_natural` | sapling | (b) Botany Trees nativo |  |

#### Reactive 10.2.1

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `reactive:flower_vine` | `reactive:flower_vine` | vine _(bassa priorità)_ | (f) non coperta | nasce da reazioni alchemiche, non è una coltura |
| `reactive:mind_lichen` | `reactive:mind_lichen` | lichen _(bassa priorità)_ | (f) non coperta | variante del glow lichen creata dalle reazioni |

**Psi**: nessuna pianta. Verificato: nessuna pianta.

### Mondi

#### The Aether 1.5.10

_Mod dichiarata da BotanyCompatLayer: le righe (e) potrebbero essere coperte da BCL, da verificare._

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `aether:berry_bush` | `aether:berry_bush_stem` | berry bush | (e) BCL (dichiarato, non verificato) | lo stelo (berry_bush_stem) cresce in cespuglio; nel mondo vuole terra dell'Aether; nel vaso va bene la terra normale |
| `aether:purple_flower` | `aether:purple_flower` | flower | (e) BCL (dichiarato, non verificato) |  |
| `aether:white_flower` | `aether:white_flower` | flower | (e) BCL (dichiarato, non verificato) |  |
| `aether:skyroot_sapling` | `aether:skyroot_sapling` | sapling | (b) Botany Trees nativo |  |
| `aether:golden_oak_sapling` | `aether:golden_oak_sapling` | sapling | (b) Botany Trees nativo |  |

#### Deep Aether 1.1.5.1

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `deep_aether:squash_stem` | `deep_aether:squash_seeds` | stem crop | (f) non coperta | come la zucca: il frutto è casuale fra blue/green/purple_squash |
| `deep_aether:golden_vines` | `deep_aether:goldenleaf_berries` | hanging vine | (f) non coperta | tipo cave vines (appesa): rotation X_180; BP imposta berries=true |
| `deep_aether:lightcap_mushrooms` | `deep_aether:lightcap_mushrooms` | mushroom | (f) non coperta |  |
| `deep_aether:aerlavender` | `deep_aether:aerlavender` | flower | (f) non coperta |  |
| `deep_aether:aether_cattails` | `deep_aether:aether_cattails` | flower | (f) non coperta |  |
| `deep_aether:echaisy` | `deep_aether:echaisy` | flower | (f) non coperta |  |
| `deep_aether:enchanted_blossom` | `deep_aether:enchanted_blossom` | flower | (f) non coperta |  |
| `deep_aether:golden_aspess` | `deep_aether:golden_aspess` | flower | (f) non coperta |  |
| `deep_aether:iaspove` | `deep_aether:iaspove` | flower | (f) non coperta |  |
| `deep_aether:radiant_orchid` | `deep_aether:radiant_orchid` | flower | (f) non coperta |  |
| `deep_aether:sky_tulips` | `deep_aether:sky_tulips` | flower | (f) non coperta |  |
| `deep_aether:tall_aerlavender` | `deep_aether:tall_aerlavender` | flower | (f) non coperta |  |
| `deep_aether:tall_aether_cattails` | `deep_aether:tall_aether_cattails` | tall flower | (f) non coperta | alta 2 blocchi |
| `deep_aether:golden_flower` | `deep_aether:golden_flower` | tall flower | (f) non coperta | alta 2 blocchi |
| `deep_aether:feather_grass` | `deep_aether:feather_grass` | grass _(bassa priorità)_ | (f) non coperta |  |
| `deep_aether:mini_golden_grass` | `deep_aether:mini_golden_grass` | grass _(bassa priorità)_ | (f) non coperta |  |
| `deep_aether:short_golden_grass` | `deep_aether:short_golden_grass` | grass _(bassa priorità)_ | (f) non coperta |  |
| `deep_aether:medium_golden_grass` | `deep_aether:medium_golden_grass` | grass _(bassa priorità)_ | (f) non coperta |  |
| `deep_aether:tall_feather_grass` | `deep_aether:tall_feather_grass` | grass _(bassa priorità)_ | (f) non coperta | alta 2 blocchi |
| `deep_aether:tall_golden_grass` | `deep_aether:tall_golden_grass` | grass _(bassa priorità)_ | (f) non coperta | alta 2 blocchi |
| `deep_aether:yagroot_vine` | `deep_aether:yagroot_vine` | vine _(bassa priorità)_ | (f) non coperta |  |
| `deep_aether:roseroot_sapling` | `deep_aether:roseroot_sapling` | sapling | (b) Botany Trees nativo |  |
| `deep_aether:blue_roseroot_sapling` | `deep_aether:blue_roseroot_sapling` | sapling | (b) Botany Trees nativo |  |
| `deep_aether:conberry_sapling` | `deep_aether:conberry_sapling` | sapling | (b) Botany Trees nativo |  |
| `deep_aether:cruderoot_sapling` | `deep_aether:cruderoot_sapling` | sapling | (b) Botany Trees nativo |  |
| `deep_aether:sunroot_sapling` | `deep_aether:sunroot_sapling` | sapling | (b) Botany Trees nativo |  |
| `deep_aether:yagroot_sapling` | `deep_aether:yagroot_sapling` | sapling | (b) Botany Trees nativo |  |

#### The Undergarden 0.9.6

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `undergarden:underbean_bush` | `undergarden:underbeans` | berry bush | (f) non coperta | loot a age=3: underbeans |
| `undergarden:blisterberry_bush` | `undergarden:blisterberry` | berry bush | (f) non coperta | loot a age=3: blisterberry + rotten_blisterberry |
| `undergarden:ditchbulb_plant` | `undergarden:ditchbulb` | bush | (f) non coperta | age 0..1; loot age=1: ditchbulb |
| `undergarden:droopvine` | `undergarden:droopvine_item` | hanging vine | (f) non coperta | appesa (tipo cave vines): rotation X_180; il frutto dipende da glowy=true (BP non lo imposta) |
| `undergarden:gloomgourd_stem` | `undergarden:gloomgourd_seeds` | stem crop | (f) non coperta | come melone/zucca (StemBlock) |
| `undergarden:glitterkelp` | `undergarden:glitterkelp` | water plant | (f) non coperta | tipo kelp |
| `undergarden:blood_mushroom` | `undergarden:blood_mushroom` | mushroom | (f) non coperta |  |
| `undergarden:indigo_mushroom` | `undergarden:indigo_mushroom` | mushroom | (f) non coperta |  |
| `undergarden:ink_mushroom` | `undergarden:ink_mushroom` | mushroom | (f) non coperta |  |
| `undergarden:veil_mushroom` | `undergarden:veil_mushroom` | mushroom | (f) non coperta |  |
| `undergarden:puff_mushroom` | `undergarden:puff_mushroom` | mushroom | (f) non coperta |  |
| `undergarden:amorous_bristle` | `undergarden:amorous_bristle` | flower | (f) non coperta |  |
| `undergarden:butterbunch` | `undergarden:butterbunch` | flower | (f) non coperta |  |
| `undergarden:miserabell` | `undergarden:miserabell` | flower | (f) non coperta |  |
| `undergarden:shimmerweed` | `undergarden:shimmerweed` | flower | (f) non coperta |  |
| `undergarden:tall_shimmerweed` | `undergarden:tall_shimmerweed` | tall flower | (f) non coperta | alta 2 blocchi; loot: shimmerweed |
| `undergarden:deepturf` | `undergarden:deepturf` | grass _(bassa priorità)_ | (f) non coperta |  |
| `undergarden:ashen_deepturf` | `undergarden:ashen_deepturf` | grass _(bassa priorità)_ | (f) non coperta |  |
| `undergarden:frozen_deepturf` | `undergarden:frozen_deepturf` | grass _(bassa priorità)_ | (f) non coperta |  |
| `undergarden:tall_deepturf` | `undergarden:tall_deepturf` | grass _(bassa priorità)_ | (f) non coperta |  |
| `undergarden:mushroom_veil` | `undergarden:mushroom_veil` | vine _(bassa priorità)_ | (f) non coperta | liana appesa |
| `undergarden:grongle_sapling` | `undergarden:grongle_sapling` | sapling | (b) Botany Trees nativo |  |
| `undergarden:smogstem_sapling` | `undergarden:smogstem_sapling` | sapling | (b) Botany Trees nativo |  |
| `undergarden:wigglewood_sapling` | `undergarden:wigglewood_sapling` | sapling | (b) Botany Trees nativo |  |

#### Deeper and Darker 1.4.1

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `deeperdarker:gloomy_grass` | `deeperdarker:gloomy_grass` | plant | (a) Botany Pots nativo |  |
| `deeperdarker:gloomy_sculk` | `deeperdarker:gloomy_sculk` | plant | (a) Botany Pots nativo |  |
| `deeperdarker:glowing_flowers` | `deeperdarker:glowing_flowers` | plant | (a) Botany Pots nativo |  |
| `deeperdarker:glowing_grass` | `deeperdarker:glowing_grass` | plant | (a) Botany Pots nativo |  |
| `deeperdarker:glowing_roots` | `deeperdarker:glowing_roots` | plant | (a) Botany Pots nativo |  |
| `deeperdarker:ice_lily` | `deeperdarker:ice_lily` | plant | (a) Botany Pots nativo |  |
| `deeperdarker:lily_flower` | `deeperdarker:lily_flower` | plant | (a) Botany Pots nativo |  |
| `deeperdarker:sculk_tendrils` | `deeperdarker:sculk_tendrils` | plant | (a) Botany Pots nativo |  |
| `deeperdarker:sculk_vines` | `deeperdarker:sculk_vines` | plant | (a) Botany Pots nativo |  |
| `deeperdarker:glowing_vines` | `deeperdarker:bloom_berries` | hanging vine | (a) Botany Pots nativo |  |
| `deeperdarker:gloomy_cactus` | `deeperdarker:gloomy_cactus` | cactus | (f) non coperta | BP tratta gloomy_sculk come coltura, non come terreno: usare botanypots:soil/sculk |
| `deeperdarker:echo_sapling` | `deeperdarker:echo_sapling` | sapling | (b) Botany Trees nativo |  |

#### Unusual End 2.3.1b

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `unusualend:chorus_cane` | `unusualend:chorus_cane` | cane | (f) non coperta | colonna tipo canna (blooming_chorus_cane è la variante fiorita, drop chorus_cane) |
| `unusualend:chorus_fungus` | `unusualend:chorus_fungus` | end fungus | (f) non coperta |  |
| `unusualend:chorus_roots` | `unusualend:chorus_roots` | end plant | (f) non coperta |  |
| `unusualend:endstone_sprouts` | `unusualend:endstone_sprouts` | end plant _(bassa priorità)_ | (f) non coperta |  |
| `unusualend:purpur_grass` | `unusualend:purpur_grass` | end plant _(bassa priorità)_ | (f) non coperta |  |
| `unusualend:flowering_purpur_grass` | `unusualend:flowering_purpur_grass` | end flower | (f) non coperta | loot: chorus_petal |
| `unusualend:crystal_flower` | `unusualend:crystal_flower` | flower | (f) non coperta | loot: shiny_crystal; terra/erba/gloopstone |
| `unusualend:gloopy_bush` | `unusualend:gloopy_bush` | plant | (f) non coperta |  |
| `unusualend:gloopy_tendrils` | `unusualend:gloopy_tendrils` | plant _(bassa priorità)_ | (f) non coperta |  |
| `unusualend:shiny_spirea` | `unusualend:shiny_spirea` | flower | (f) non coperta |  |
| `unusualend:flowering_gloopy_pile` | `unusualend:flowering_gloopy_pile` | tall plant _(bassa priorità)_ | (f) non coperta | alta 2 blocchi |
| `unusualend:warped_bush` | `unusualend:warped_bush` | end bush | (f) non coperta | col bonemeal diventa grown_warped_bush, che a clic destro dà warped_berries |
| `unusualend:warped_algae` | `unusualend:warped_algae` | end plant | (f) non coperta |  |
| `unusualend:small_warped_algae` | `unusualend:small_warped_algae` | end plant _(bassa priorità)_ | (f) non coperta |  |
| `unusualend:warped_sprouts` | `unusualend:warped_sprouts` | end plant _(bassa priorità)_ | (f) non coperta |  |
| `unusualend:warped_endstone_sprouts` | `unusualend:warped_endstone_sprouts` | end plant _(bassa priorità)_ | (f) non coperta |  |
| `unusualend:small_warped_squash` | `unusualend:small_warped_squash` | special | (f) non coperta | zucca della Warped Reef (piccola -> grande col bonemeal) |
| `unusualend:gloopilon_bulb` | `unusualend:gloopilon_seeds` | hanging crop | (f) non coperta | cresce APPESO sotto dripping gloopstone (seeds -> stem -> bulb age 0..2): rotation X_180 |
| `unusualend:chorus_cane_flower` | `unusualend:chorus_cane_flower` | flower _(bassa priorità)_ | (f) non coperta | fiore da parete/pavimento (face) |

#### The Twilight Forest 4.8.3345 (CurseForge)

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `twilightforest:clover_patch` | `twilightforest:clover_patch` | plant | (a) Botany Pots nativo |  |
| `twilightforest:fiddlehead` | `twilightforest:fiddlehead` | plant | (a) Botany Pots nativo |  |
| `twilightforest:huge_lily_pad` | `twilightforest:huge_lily_pad` | plant | (a) Botany Pots nativo |  |
| `twilightforest:huge_water_lily` | `twilightforest:huge_water_lily` | plant | (a) Botany Pots nativo |  |
| `twilightforest:mayapple` | `twilightforest:mayapple` | plant | (a) Botany Pots nativo |  |
| `twilightforest:moss_patch` | `twilightforest:moss_patch` | plant | (a) Botany Pots nativo |  |
| `twilightforest:mushgloom` | `twilightforest:mushgloom` | plant | (a) Botany Pots nativo |  |
| `twilightforest:root_strand` | `twilightforest:root_strand` | plant | (a) Botany Pots nativo |  |
| `twilightforest:thorn_rose` | `twilightforest:thorn_rose` | plant | (a) Botany Pots nativo |  |
| `twilightforest:torchberry_plant` | `twilightforest:torchberry_plant` | plant | (a) Botany Pots nativo |  |
| `twilightforest:canopy_sapling` | `twilightforest:canopy_sapling` | sapling | (b) Botany Trees nativo |  |
| `twilightforest:darkwood_sapling` | `twilightforest:darkwood_sapling` | sapling | (b) Botany Trees nativo |  |
| `twilightforest:hollow_oak_sapling` | `twilightforest:hollow_oak_sapling` | sapling | (b) Botany Trees nativo |  |
| `twilightforest:mangrove_sapling` | `twilightforest:mangrove_sapling` | sapling | (b) Botany Trees nativo |  |
| `twilightforest:mining_sapling` | `twilightforest:mining_sapling` | sapling | (b) Botany Trees nativo |  |
| `twilightforest:rainbow_oak_sapling` | `twilightforest:rainbow_oak_sapling` | sapling | (b) Botany Trees nativo |  |
| `twilightforest:sorting_sapling` | `twilightforest:sorting_sapling` | sapling | (b) Botany Trees nativo |  |
| `twilightforest:time_sapling` | `twilightforest:time_sapling` | sapling | (b) Botany Trees nativo |  |
| `twilightforest:transformation_sapling` | `twilightforest:transformation_sapling` | sapling | (b) Botany Trees nativo |  |
| `twilightforest:twilight_oak_sapling` | `twilightforest:twilight_oak_sapling` | sapling | (b) Botany Trees nativo |  |
| `twilightforest:raspberry_bush` | `twilightforest:raspberry_bush` | berry bush | (f) non coperta | TF berry bush age 0..3 (+ layers neve); le bacche vengono da una loot table separata |
| `twilightforest:blueberry_bush` | `twilightforest:blueberry_bush` | berry bush | (f) non coperta | TF berry bush age 0..3 (+ layers neve); le bacche vengono da una loot table separata |
| `twilightforest:blackberry_bush` | `twilightforest:blackberry_bush` | berry bush | (f) non coperta | TF berry bush age 0..3 (+ layers neve); le bacche vengono da una loot table separata |
| `twilightforest:maloberry_bush` | `twilightforest:maloberry_bush` | berry bush | (f) non coperta | TF berry bush age 0..3 (+ layers neve); le bacche vengono da una loot table separata |
| `twilightforest:blightberry_bush` | `twilightforest:blightberry_bush` | berry bush | (f) non coperta | cespuglio della Dark Tower: vive su netherrack/blackstone/soul sand/soul soil |
| `twilightforest:duskberry_bush` | `twilightforest:duskberry_bush` | berry bush | (f) non coperta | cespuglio della Dark Tower: vive su netherrack/blackstone/soul sand/soul soil |
| `twilightforest:skyberry_bush` | `twilightforest:skyberry_bush` | berry bush | (f) non coperta | cespuglio della Dark Tower: vive su netherrack/blackstone/soul sand/soul soil |
| `twilightforest:stingberry_bush` | `twilightforest:stingberry_bush` | berry bush | (f) non coperta | cespuglio della Dark Tower: vive su netherrack/blackstone/soul sand/soul soil |
| `twilightforest:iron_oreberry` | `twilightforest:iron_oreberry` | oreberry bush | (f) non coperta | cespuglio di bacche-minerale: su pietra, luce < 13 nel mondo |
| `twilightforest:gold_oreberry` | `twilightforest:gold_oreberry` | oreberry bush | (f) non coperta | cespuglio di bacche-minerale: su pietra, luce < 13 nel mondo |
| `twilightforest:copper_oreberry` | `twilightforest:copper_oreberry` | oreberry bush | (f) non coperta | cespuglio di bacche-minerale: su pietra, luce < 13 nel mondo |
| `twilightforest:essence_oreberry` | `twilightforest:essence_oreberry` | oreberry bush | (f) non coperta | cespuglio di bacche-minerale: su pietra, luce < 13 nel mondo |
| `twilightforest:magic_beans` | `twilightforest:magic_beans` | special _(saltare)_ | (f) non coperta | beanstalk gigante: non adatto ai vasi |

#### Regions Unexplored 0.6.2

Coperte da Botany Pots (121): acacia_shrub, alpha_dandelion, alpha_rose, ashen_grass, ashen_shrub, aster, baobab_shrub, barley, barrel_cactus, birch_shrub, black_snowbelle, blackwood_shrub, bladed_grass, bladed_tall_grass, bleeding_heart, blue_lupine, blue_magnolia_flowers, blue_magnolia_shrub, blue_snowbelle, brimsprout, brimwood_shrub, brown_snowbelle, cattail, cherry_shrub, clover, cobalt_roots, corpse_flower, cyan_snowbelle, cypress_shrub, daisy, dark_oak_shrub, day_lily, dead_pine_shrub, dead_shrub, dead_steppe_shrub, dorcel, duckweed, duskmelon, elephant_ear, eucalyptus_shrub, felicia_daisy, fireweed, flowering_lily_pad, flowering_shrub, frozen_grass, glistering_bloom, glistering_fern, glistering_ivy, glistering_sprout, golden_larch_shrub, gray_snowbelle, green_snowbelle, hibiscus, hyacinth_bloom, hyacinth_flowers, hyssop, joshua_shrub, jungle_shrub, kapok_shrub, kapok_vines, larch_shrub, light_blue_snowbelle, light_gray_snowbelle, lime_snowbelle, magenta_snowbelle, magnolia_shrub, mallow, mangrove_shrub, maple_shrub, meadow_sage, mycotoxic_daisy, mycotoxic_grass, mycotoxic_mushrooms, oak_shrub, orange_coneflower, orange_maple_shrub, orange_snowbelle, palm_shrub, pine_shrub, pink_lupine, pink_magnolia_flowers, pink_magnolia_shrub, pink_snowbelle, poppy_bush, prismoss_sprout, purple_coneflower, purple_lupine, purple_snowbelle, red_lupine, red_maple_shrub, red_snowbelle, redwood_shrub, saguaro_cactus, salmon_poppy_bush, salmonberry_bush, sandy_grass, sandy_tall_grass, silver_birch_shrub, small_desert_shrub, socotra_shrub, spanish_moss, spruce_shrub, steppe_grass, steppe_shrub, steppe_tall_grass, tall_blue_bioshroom, tall_green_bioshroom, tall_pink_bioshroom, tall_yellow_bioshroom, tassel, tsubaki, waratah, white_magnolia_flowers, white_magnolia_shrub, white_snowbelle, white_trillium, willow_shrub, wilting_trillium, windswept_grass, yellow_lupine, yellow_snowbelle.

Coperte da Botany Trees (37): alpha_sapling, apple_oak_sapling, ashen_sapling, bamboo_sapling, baobab_sapling, blackwood_sapling, blue_magnolia_sapling, brimwood_sapling, cobalt_sapling, cypress_sapling, dead_pine_sapling, dead_sapling, eucalyptus_sapling, flowering_sapling, golden_larch_sapling, green_bioshroom, joshua_sapling, kapok_sapling, larch_sapling, lavender_wisteria_sapling, magnolia_sapling, maple_sapling, orange_maple_sapling, palm_sapling, pine_sapling, pink_bioshroom, pink_magnolia_sapling, red_maple_sapling, redwood_sapling, salmon_wisteria_sapling, silver_birch_sapling, sky_wisteria_sapling, small_oak_sapling, socotra_sapling, white_magnolia_sapling, willow_sapling, yellow_bioshroom.

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `regions_unexplored:blue_bioshroom` | `regions_unexplored:blue_bioshroom` | sapling (fungo gigante) | (f) non coperta | come green/pink/yellow_bioshroom di Botany Trees (che però salta il blu) |
| `regions_unexplored:salmon_poppy` | `regions_unexplored:salmon_poppy` | flower | (f) non coperta |  |
| `regions_unexplored:salmon_wisteria_shrub` | `regions_unexplored:salmon_wisteria_shrub` | tall shrub | (f) non coperta | alta 2 blocchi |
| `regions_unexplored:lavender_wisteria_vines` | `regions_unexplored:lavender_wisteria_vines` | hanging vine _(bassa priorità)_ | (f) non coperta | liana appesa (tip) |
| `regions_unexplored:salmon_wisteria_vines` | `regions_unexplored:salmon_wisteria_vines` | hanging vine _(bassa priorità)_ | (f) non coperta | liana appesa (tip) |
| `regions_unexplored:sky_wisteria_vines` | `regions_unexplored:sky_wisteria_vines` | hanging vine _(bassa priorità)_ | (f) non coperta | liana appesa (tip) |
| `regions_unexplored:tall_hyacinth_stock` | `regions_unexplored:tall_hyacinth_stock` | special _(bassa priorità)_ | (f) non coperta | pianta subacquea a colonna (forma tip/frustum) |
| `regions_unexplored:redstone_bud` | `regions_unexplored:redstone_bud` | special _(bassa priorità)_ | (f) non coperta | germoglio su pietra che droppa redstone: farm di redstone, valutare |
| `regions_unexplored:saguaro_cactus_flower` | `regions_unexplored:saguaro_cactus_flower` | special _(bassa priorità)_ | (f) non coperta | ex cactus_flower (alias); BP ha solo saguaro_cactus |
| `regions_unexplored:grass_sprouts` | `regions_unexplored:grass_sprouts` | grass | (a?) Botany Pots con vecchio ID (alias RU 0.6, da verificare) | BP 1.21.1 lo copre coi vecchi ID stone_bud/medium_grass, rinominati in RU 0.6 (alias) |
| `regions_unexplored:lavender_wisteria_shrub` | `regions_unexplored:lavender_wisteria_shrub` | tall shrub | (a?) Botany Pots con vecchio ID (alias RU 0.6, da verificare) | BP lo copre col vecchio ID mauve_shrub (alias RU 0.6) |
| `regions_unexplored:sky_wisteria_shrub` | `regions_unexplored:sky_wisteria_shrub` | tall shrub | (a?) Botany Pots con vecchio ID (alias RU 0.6, da verificare) | BP lo copre col vecchio ID enchanted_birch_shrub (alias RU 0.6) |
| `regions_unexplored:maple_leaf_litter` | `regions_unexplored:maple_leaf_litter` | leaf litter | (a?) Botany Pots con vecchio ID (alias RU 0.6, da verificare) | BP lo copre col vecchio ID maple_leaf_pile (alias RU 0.6) |
| `regions_unexplored:red_maple_leaf_litter` | `regions_unexplored:red_maple_leaf_litter` | leaf litter | (a?) Botany Pots con vecchio ID (alias RU 0.6, da verificare) | BP lo copre col vecchio ID red_maple_leaf_pile (alias RU 0.6) |
| `regions_unexplored:orange_maple_leaf_litter` | `regions_unexplored:orange_maple_leaf_litter` | leaf litter | (a?) Botany Pots con vecchio ID (alias RU 0.6, da verificare) | BP lo copre col vecchio ID orange_maple_leaf_pile (alias RU 0.6) |
| `regions_unexplored:silver_birch_leaf_litter` | `regions_unexplored:silver_birch_leaf_litter` | leaf litter | (a?) Botany Pots con vecchio ID (alias RU 0.6, da verificare) | BP lo copre col vecchio ID silver_birch_leaf_pile (alias RU 0.6) |
| `regions_unexplored:enchanted_birch_leaf_litter` | `regions_unexplored:enchanted_birch_leaf_litter` | leaf litter | (a?) Botany Pots con vecchio ID (alias RU 0.6, da verificare) | BP lo copre col vecchio ID enchanted_birch_leaf_pile (alias RU 0.6) |

#### Supplementaries 4.0.2

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `supplementaries:flax` | `supplementaries:flax_seeds` | crop | (a) Botany Pots nativo | alta 2 blocchi |
| `supplementaries:wild_flax` | `supplementaries:wild_flax` | wild crop | (a) Botany Pots nativo |  |

**L_Ender's Cataclysm 3.33**: nessuna pianta. Nessuna pianta (Botany Pots nativo aggiunge solo the_baby_leviathan_bucket come terreno acqua).

### In arrivo / extra

#### Friends & Foes (fuori lista, già nel pack)

| Blocco | Seme / input | Tipo | Copertura | Note |
|---|---|---|---|---|
| `friendsandfoes:buttercup` | `friendsandfoes:buttercup` | flower _(bassa priorità)_ | (f) non coperta | mod fuori dalla lista richiesta ma presente nel pack |

## Terreni

Ogni terreno nei vasi richiede una ricetta `botanypots:block_derived_soil` per blocco. La terra fertilizzata di Farming for Blockheads è **nativa** (5 ricette in `recipe/farmingforblockheads/soil` e anche nel tag `botanypots:soil/dirt`, quindi vale per tutte le colture su terra).

| Mod | Blocco | Copertura | Note |
|---|---|---|---|
| Farmer's Delight 1.3.4 | `farmersdelight:rich_soil` | bp |  |
| Farmer's Delight 1.3.4 | `farmersdelight:rich_soil_farmland` | bp | growth_modifier 0.15 |
| Farmer's Delight 1.3.4 | `farmersdelight:organic_compost` | bp |  |
| Farming for Blockheads 21.1.14 (in arrivo) | `farmingforblockheads:fertilized_farmland_rich` | bp | soil recipe + nel tag botanypots:soil/dirt (yield +10%) |
| Farming for Blockheads 21.1.14 (in arrivo) | `farmingforblockheads:fertilized_farmland_rich_stable` | bp |  |
| Farming for Blockheads 21.1.14 (in arrivo) | `farmingforblockheads:fertilized_farmland_healthy` | bp |  |
| Farming for Blockheads 21.1.14 (in arrivo) | `farmingforblockheads:fertilized_farmland_healthy_stable` | bp |  |
| Farming for Blockheads 21.1.14 (in arrivo) | `farmingforblockheads:fertilized_farmland_stable` | bp |  |
| The Twilight Forest 4.8.3345 (CurseForge) | `twilightforest:uberous_soil` | bp |  |
| The Undergarden 0.9.6 | `undergarden:deepsoil / deepsoil_farmland / coarse_deepsoil / deepturf_block / ashen_deepturf_block / frozen_deepturf_block / depthrock / shiverstone / tremblecrust / gwibling_bucket` | bp | 10 terreni nativi |
| Deeper and Darker 1.4.1 | `deeperdarker:gloomslate / sculk_stone / blooming_moss_block` | bp |  |
| Supplementaries 4.0.2 | `supplementaries:planter` | bp |  |
| L_Ender's Cataclysm 3.33 | `cataclysm:the_baby_leviathan_bucket` | bp | acqua |
| Twilight's Flavor & Delight 3.2.6 | `twilightdelight:twilight_rich_soil` | none | per le colonie (fiddlehead_clump, mushgloom_colony) |
| Twilight's Flavor & Delight 3.2.6 | `twilightdelight:twilight_rich_soil_farmland` | none |  |
| My Nether's Delight 1.10.4 (in arrivo) | `mynethersdelight:resurgent_soil` | none | terra del Nether (stile rich soil) |
| My Nether's Delight 1.10.4 (in arrivo) | `mynethersdelight:resurgent_soil_farmland` | none |  |
| My Nether's Delight 1.10.4 (in arrivo) | `mynethersdelight:letios_compost` | none | compost del Nether |
| Hexalia 1.3.6 | `hexalia:infused_dirt` | none | nel tag minecraft:dirt |
| Hexalia 1.3.6 | `hexalia:infused_farmland` | none | serve anche al saltsprout |
| [Let's Do] Farm & Charm 1.1.28 | `farm_and_charm:fertilized_soil` | none (BCL?) |  |
| [Let's Do] Farm & Charm 1.1.28 | `farm_and_charm:fertilized_farmland` | none (BCL?) |  |
| [Let's Do] Vinery 1.5.5 | `vinery:loam` | none (BCL?) | facoltativo |
| The Aether 1.5.10 | `aether:aether_dirt / aether_grass_block / enchanted_aether_grass_block / aether_farmland` | none (BCL?) | la descrizione di BCL parla di 'extra natural soil blocks' |
| Deep Aether 1.1.5.1 | `deep_aether:aether_mud / aether_coarse_dirt / aerglow_grass_block / golden_heights_grass_block / aether_moss_block` | none | facoltativi |
| Bountiful Fares 3.0.12 | `bountifulfares:grassy_dirt` | none | facoltativo (nel tag minecraft:dirt) |

## Da creare

Formato di riferimento: `botanypots:block_derived_crop` come nei file di `matteo_tweaks` e di Botany Pots 21.1.44. Con `block_derived_crop` il seme, il display e i drop si ricavano dal blocco (stato a età massima, `berries=true` se esiste) e dalla sua loot table; il terreno di default è `botanypots:soil/dirt`. Indico **drops espliciti** quando la loot table non dà il raccolto: si scrivono con `"drops": [{"type": "botanypots:loot_table", "table_id": "..."}]` oppure `{"type": "botanypots:items", "items": [{"result": {"id": "...", "count": 1}, "chance": 1.0}]}`. Terreni: `water` = `{"tag":"botanypots:soil/water"}`, `mushroom` = either(block_tag `minecraft:mushroom_grow_block`, `botanypots:soil/mushroom`) come le colonie di FD, `nether` = either(block_tag `minecraft:nylium`, `botanypots:soil/nether`), `end` = `botanypots:soil/end`, `sand`, `sculk`, `stone` = `botanypots:soil/moss` (pietra + terra). Le piante appese usano `render_options.rotation: X_180` (come cave vines). Gli alberi seguono lo schema di Botany Trees: `block_derived_crop` sull'alberello, `grow_time` 2400 e `drops` da una loot table nostra (modello: `botanytrees:tree_drops/...`).

### 1. Non coperte (da scrivere)

#### Veggies Delight 1.9.3 (1)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `veggiesdelight:mature_dandelion` | `veggiesdelight:mature_dandelion` | - | dandelion_leaf, mature_dandelion | dirt | drop dandelion_leaf; il bonemeal la duplica |

#### Expanded Delight 0.1.4 (10)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `expandeddelight:asparagus_seeds` | `expandeddelight:asparagus_crop` | age=0..7 | asparagus, asparagus_seeds | dirt |  |
| `expandeddelight:chili_pepper_seeds` | `expandeddelight:chili_pepper_crop` | age=0..7 | chili_pepper, chili_pepper_seeds | dirt |  |
| `expandeddelight:peanut` | `expandeddelight:peanut_crop` | age=0..7 | peanut | dirt |  |
| `expandeddelight:sweet_potato` | `expandeddelight:sweet_potato_crop` | age=0..7 | sweet_potato | dirt | stesso nome di veggiesdelight:sweet_potato ma item diverso |
| `expandeddelight:cranberries` | `expandeddelight:cranberry_plant` | age=0..3 | cranberries | water | si piazza sull'acqua come una ninfea (LilypadCropItem); raccolta a clic destro; loot a age=3 dà cranberries: derivato ok |
| `expandeddelight:cinnamon_sapling` | `expandeddelight:cinnamon_sapling` | - | cinnamon_sapling | dirt | albero: serve ricetta stile Botany Trees (drop cinnamon_log + sapling); **drops:** expandeddelight:cinnamon_log, expandeddelight:cinnamon_sapling (5%), expandeddelight:cinnamon_leaves (cesoie) |
| `expandeddelight:wild_asparagus` | `expandeddelight:wild_asparagus` | - | asparagus, wild_asparagus | dirt |  |
| `expandeddelight:wild_chili_pepper` | `expandeddelight:wild_chili_pepper` | - | chili_pepper, wild_chili_pepper | dirt |  |
| `expandeddelight:wild_peanuts` | `expandeddelight:wild_peanuts` | - | peanut, wild_peanuts | dirt |  |
| `expandeddelight:wild_sweet_potato` | `expandeddelight:wild_sweet_potato` | - | sweet_potato, wild_sweet_potato | dirt |  |

#### Cultural Delights 0.19.1 (13)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `culturaldelights:cucumber_seeds` | `culturaldelights:cucumbers` | age=0..7 | cucumber, cucumber_seeds | dirt |  |
| `culturaldelights:eggplant_seeds` | `culturaldelights:eggplants` | age=0..7 | eggplant, eggplant_seeds | dirt | le wild_eggplants droppano anche white_eggplant (non coltivabile a parte: il blocco white_eggplants non è registrato) |
| `culturaldelights:corn_kernels` | `culturaldelights:corn` | age=0..7, height=0..2 | corn_cob, corn_kernels | dirt | alta 3 blocchi (proprietà height 0..2); il display di default mostra solo il blocco basso: meglio display con height; loot (height=0, age=7): corn_cob + corn_kernels |
| `culturaldelights:beans` | `culturaldelights:beans` | age=0..3 | bean_pod, beans | dirt | come i pomodori di FD: i semi piazzano budding_beans (age 0..4) che diventa beans su corda; usare block=beans come fa BP con farmersdelight:tomatoes; raccolta: bean_pod |
| `culturaldelights:avocado_sapling` | `culturaldelights:avocado_sapling` | - | avocado_sapling | dirt | albero da frutto (fruiting_avocado_leaves): ricetta stile Botany Trees; **drops:** culturaldelights:avocado_log, culturaldelights:avocado, culturaldelights:avocado_sapling (5%) |
| `culturaldelights:avocado_pit` | `culturaldelights:avocado_pit` | - | avocado_pit | dirt | nocciolo = alberello (SaplingBlock con grower proprio): stessa ricetta dell'avocado; **drops:** culturaldelights:avocado_log, culturaldelights:avocado, culturaldelights:avocado_pit (5%) |
| `culturaldelights:lemon_sapling` | `culturaldelights:lemon_sapling` | - | lemon_sapling | dirt | albero da frutto (fruiting_lemon_leaves): ricetta stile Botany Trees; **drops:** culturaldelights:lemon_log, culturaldelights:lemon, culturaldelights:lemon_sapling (5%); non confondere con bountifulfares:lemon_sapling |
| `culturaldelights:wild_cucumbers` | `culturaldelights:wild_cucumbers` | - | cucumber, cucumber_seeds, wild_cucumbers | dirt |  |
| `culturaldelights:wild_eggplants` | `culturaldelights:wild_eggplants` | - | eggplant_seeds, white_eggplant, wild_eggplants | dirt |  |
| `culturaldelights:wild_corn` | `culturaldelights:wild_corn` | - | corn_kernels, wild_corn | dirt |  |
| `culturaldelights:wild_beans` | `culturaldelights:wild_beans` | - | beans, wild_beans | dirt |  |
| `culturaldelights:agave` | `culturaldelights:agave` | - | agave | dirt |  |
| `culturaldelights:mint` | `culturaldelights:mint` | - | mint | dirt |  |

#### Twilight's Flavor & Delight 3.2.6 (3)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `twilightdelight:fiddlehead_clump` | `twilightdelight:fiddlehead_clump` | age=0..3 | fiddlehead_clump, twilightforest:fiddlehead | mushroom | colonia stile FD (MushroomColonyBlock) + parte alta fiddlehead_clump_upper; drop twilightforest:fiddlehead |
| `twilightdelight:mushgloom_colony` | `twilightdelight:mushgloom_colony` | age=0..3 | mushgloom_colony, twilightforest:mushgloom | mushroom | drop twilightforest:mushgloom |
| `twilightdelight:ironwood_sapling` | `twilightdelight:ironwood_sapling` | - | ironwood_sapling | dirt | albero: ricetta stile Botany Trees; **drops:** twilightdelight:ironwood_log, twilightdelight:ironwood_sapling (5%), twilightdelight:ironwood_leaves (cesoie) |

#### Aether's Delight 0.1.4.2 (7)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `aethersdelight:ginger` | `aethersdelight:ginger_crop` | age=0..4 | ginger | dirt |  |
| `aethersdelight:leek` | `aethersdelight:leek_crop` | age=0..4 | leek | dirt |  |
| `aethersdelight:parsnip` | `aethersdelight:parsnip_crop` | age=0..4 | parsnip | dirt |  |
| `aethersdelight:peppermint_bush_stem` | `aethersdelight:peppermint_bush` | - | peppermint_bush, peppermint_bush_stem, peppermint_leaf | dirt | come il cespuglio di bacche dell'Aether: lo stelo cresce in cespuglio; display peppermint_bush; **drops:** aethersdelight:peppermint_leaf; loot del cespuglio: peppermint_bush/stem/leaf (con condizioni): meglio drops espliciti |
| `aethersdelight:wild_ginger` | `aethersdelight:wild_ginger` | - | ginger | dirt |  |
| `aethersdelight:wild_leek` | `aethersdelight:wild_leek` | - | leek | dirt |  |
| `aethersdelight:wild_parsnip` | `aethersdelight:wild_parsnip` | - | parsnip | dirt |  |

#### Ender's Delight 1.3.1 (4)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `endersdelight:amberveil` | `endersdelight:amberveil_mushroom` | - | amberveil | end |  |
| `endersdelight:chorusflame` | `endersdelight:chorusflame_bush` | age=0..2 | chorusflame | end | age 0..2 |
| `endersdelight:ethereal_saffron` | `endersdelight:ethereal_saffron_bush` | - | ethereal_saffron | end |  |
| `endersdelight:voidpepper` | `endersdelight:voidpepper_bush` | pepper=true/false | voidpepper | end | block entity; proprietà pepper=true/false (BP non la imposta): drops espliciti; **drops:** endersdelight:voidpepper |

#### Roaster's Delight 1.0.0.1 (CurseForge, sorgente chiuso) (5)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| ? | `? (pianta del caffè; seme: chicco non tostato)` | - | - | dirt | ID sconosciuti (sorgente chiuso, ARR): ricavarli in gioco con /botanypots debug missing seeds |
| ? | `? (cespuglio del tè)` | - | - | dirt | ID sconosciuti (sorgente chiuso, ARR): ricavarli in gioco con /botanypots debug missing seeds |
| ? | `? (camomilla)` | - | - | dirt | ID sconosciuti (sorgente chiuso, ARR): ricavarli in gioco con /botanypots debug missing seeds |
| ? | `? (menta)` | - | - | dirt | ID sconosciuti (sorgente chiuso, ARR): ricavarli in gioco con /botanypots debug missing seeds |
| ? | `? (matcha)` | - | - | dirt | ID sconosciuti (sorgente chiuso, ARR): ricavarli in gioco con /botanypots debug missing seeds |

#### My Nether's Delight 1.10.4 (in arrivo) (4)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `mynethersdelight:bullet_pepper` | `mynethersdelight:bullet_pepper` | age=0..2, lit=true/false | bullet_pepper | nether | PowderyFlowerBlock age 0..3 + proprietà lit; raccolta a clic destro; **drops:** mynethersdelight:bullet_pepper; sopravvive su #mynethersdelight:powdery_cannon_plantable_on (netherrack, nylium, sabbia, terra, soul soil, magma) |
| `mynethersdelight:powder_cannon` | `mynethersdelight:powdery_cannon` | age=0..1, lit=true | bullet_pepper, powder_cannon | nether | multi-blocco tipo bambù (powdery_chubby_sapling -> powdery_cannon/powdery_cane); display come il bambù di BP; **drops:** mynethersdelight:powder_cannon, mynethersdelight:bullet_pepper |
| `mynethersdelight:crimson_fungus_colony` | `mynethersdelight:crimson_fungus_colony` | age=0..3 | minecraft:crimson_fungus, crimson_fungus_colony | nether | drop minecraft:crimson_fungus |
| `mynethersdelight:warped_fungus_colony` | `mynethersdelight:warped_fungus_colony` | age=0..3 | minecraft:warped_fungus, warped_fungus_colony | nether | drop minecraft:warped_fungus |

#### Hexalia 1.3.6 (31)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `hexalia:mandrake_seeds` | `hexalia:mandrake_crop` | age=0..3 | mandrake, mandrake_seeds | dirt |  |
| `hexalia:rabbage_seeds` | `hexalia:rabbage_crop` | age=0..3 | rabbage, rabbage_seeds | dirt |  |
| `hexalia:sunfire_tomato_seeds` | `hexalia:sunfire_tomato_crop` | age=0..3 | sunfire_tomato, sunfire_tomato_seeds | dirt |  |
| `hexalia:chillberries` | `hexalia:chillberry_bush` | age=0..3 | chillberries | dirt | loot a age=3: chillberries |
| `hexalia:saltsprout` | `hexalia:saltsprout` | age=0..2 | saltsprout | sand | sabbia o infused_farmland; age 0..2 |
| `hexalia:galeberries` | `hexalia:galeberries_vine` | berries=true/false | galeberries | dirt | tipo cave vines (appesa): rotation X_180; BP imposta berries=true da solo |
| `hexalia:wild_mandrake` | `hexalia:wild_mandrake` | - | mandrake_seeds | dirt | loot: mandrake_seeds |
| `hexalia:wild_sunfire_tomato` | `hexalia:wild_sunfire_tomato` | - | sunfire_tomato_seeds | dirt | loot: sunfire_tomato_seeds |
| `hexalia:aegiflora` | `hexalia:aegiflora` | - | aegiflora | dirt |  |
| `hexalia:astrylis` | `hexalia:astrylis` | - | astrylis | dirt |  |
| `hexalia:begonia` | `hexalia:begonia` | - | begonia | dirt |  |
| `hexalia:celestial_bloom` | `hexalia:celestial_bloom` | - | celestial_bloom | dirt |  |
| `hexalia:dahlia` | `hexalia:dahlia` | - | dahlia | dirt |  |
| `hexalia:ghost_fern` | `hexalia:ghost_fern` | - | ghost_fern | dirt |  |
| `hexalia:grimshade` | `hexalia:grimshade` | - | grimshade | dirt |  |
| `hexalia:lavender` | `hexalia:lavender` | - | lavender | dirt |  |
| `hexalia:lourdes` | `hexalia:lourdes` | - | lourdes | dirt |  |
| `hexalia:morphora` | `hexalia:morphora` | - | morphora | dirt |  |
| `hexalia:nautilite` | `hexalia:nautilite` | - | nautilite | dirt |  |
| `hexalia:nightshade_bush` | `hexalia:nightshade_bush` | - | nightshade_bush | dirt |  |
| `hexalia:spirit_bloom` | `hexalia:spirit_bloom` | - | spirit_bloom | dirt |  |
| `hexalia:witchweed` | `hexalia:witchweed` | - | witchweed | dirt |  |
| `hexalia:withered_aegiflora` | `hexalia:withered_aegiflora` _(bassa priorità)_ | - | withered_aegiflora | dirt |  |
| `hexalia:withered_celestial_bloom` | `hexalia:withered_celestial_bloom` _(bassa priorità)_ | - | withered_celestial_bloom | dirt |  |
| `hexalia:windsong` | `hexalia:windsong` _(bassa priorità)_ | - | windsong | dirt | ha un block entity (si attiva col Hex Focus): solo estetica nel vaso |
| `hexalia:dreamshroom` | `hexalia:dreamshroom` | - | dreamshroom | mushroom |  |
| `hexalia:pale_mushroom` | `hexalia:pale_mushroom` | flower_amount=1..4 | pale_mushroom | mushroom | flower_amount 1..4 (tipo pink petals) |
| `hexalia:lotus_flower` | `hexalia:lotus_flower` | - | lotus_flower | water | ninfea (WaterlilyBlock) |
| `hexalia:siren_kelp` | `hexalia:siren_kelp` | - | siren_kelp | water | tipo seagrass |
| `hexalia:cottonwood_sapling` | `hexalia:cottonwood_sapling` | stage=0..1 | cottonwood_sapling | dirt | albero: ricetta stile Botany Trees; **drops:** hexalia:cottonwood_log, hexalia:cottonwood_sapling (5%), hexalia:cottonwood_catkin? |
| `hexalia:willow_sapling` | `hexalia:willow_sapling` | stage=0..1 | willow_sapling | dirt | albero: ricetta stile Botany Trees (diverso dal salice di Hexerei); **drops:** hexalia:willow_log, hexalia:willow_sapling (5%) |

#### Hexerei 0.5.0.3 (7)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `hexerei:mandrake_plant` | `hexerei:mandrake_plant` | age=0..3 | mandrake_plant | dirt | PickablePlant age 0..3: i prodotti si raccolgono a clic destro, il loot dà solo la pianta; **drops:** hexerei:mandrake_flowers, hexerei:mandrake_root |
| `hexerei:belladonna_plant` | `hexerei:belladonna_plant` | age=0..3 | belladonna_plant | dirt | PickablePlant age 0..3; **drops:** hexerei:belladonna_flowers, hexerei:belladonna_berries |
| `hexerei:mugwort_bush` | `hexerei:mugwort_bush` | age=0..3, half=lower/upper | mugwort_bush | dirt | doppia altezza (half lower/upper) + age 0..3; **drops:** hexerei:mugwort_leaves, hexerei:mugwort_flowers |
| `hexerei:yellow_dock_bush` | `hexerei:yellow_dock_bush` | age=0..3, half=lower/upper | yellow_dock_bush | dirt | doppia altezza (half lower/upper) + age 0..3; **drops:** hexerei:yellow_dock_leaves, hexerei:yellow_dock_flowers |
| `hexerei:sage_seed` | `hexerei:sage_crop` | age=0..7 | sage, sage_seed | dirt |  |
| `hexerei:willow_vines` | `hexerei:willow_vines` _(bassa priorità)_ | - | willow_vines | dirt | liana appesa (GrowingPlantHead): rotation X_180 |
| `hexerei:flowering_lily_pad` | `hexerei:flowering_lily_pad` | - | flowering_lily_pad | water |  |

#### Bountiful Fares 3.0.12 (30)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `bountifulfares:apple_sapling` | `bountifulfares:apple_sapling` | - | apple_sapling | dirt | Botany Trees ha la compat nel sorgente (commit 3/6/2026) ma NON nella 21.1.7 rilasciata: copiare ricetta + loot table tree_drops da BT (LGPL-2.1) |
| `bountifulfares:golden_apple_sapling` | `bountifulfares:golden_apple_sapling` | - | golden_apple_sapling | dirt | Botany Trees ha la compat nel sorgente (commit 3/6/2026) ma NON nella 21.1.7 rilasciata: copiare ricetta + loot table tree_drops da BT (LGPL-2.1) |
| `bountifulfares:hoary_apple_sapling` | `bountifulfares:hoary_apple_sapling` | - | hoary_apple_sapling | dirt | Botany Trees ha la compat nel sorgente (commit 3/6/2026) ma NON nella 21.1.7 rilasciata: copiare ricetta + loot table tree_drops da BT (LGPL-2.1) |
| `bountifulfares:lemon_sapling` | `bountifulfares:lemon_sapling` | - | lemon_sapling | dirt | Botany Trees ha la compat nel sorgente (commit 3/6/2026) ma NON nella 21.1.7 rilasciata: copiare ricetta + loot table tree_drops da BT (LGPL-2.1) |
| `bountifulfares:orange_sapling` | `bountifulfares:orange_sapling` | - | orange_sapling | dirt | Botany Trees ha la compat nel sorgente (commit 3/6/2026) ma NON nella 21.1.7 rilasciata: copiare ricetta + loot table tree_drops da BT (LGPL-2.1) |
| `bountifulfares:coconut` | `bountifulfares:palm_sapling` | - | coconut | dirt | Botany Trees ha la compat nel sorgente (commit 3/6/2026) ma NON nella 21.1.7 rilasciata: copiare ricetta + loot table tree_drops da BT (LGPL-2.1) |
| `bountifulfares:plum_sapling` | `bountifulfares:plum_sapling` | - | plum_sapling | dirt | Botany Trees ha la compat nel sorgente (commit 3/6/2026) ma NON nella 21.1.7 rilasciata: copiare ricetta + loot table tree_drops da BT (LGPL-2.1) |
| `bountifulfares:walnut_sapling` | `bountifulfares:walnut_sapling` | - | walnut_sapling | dirt | Botany Trees ha la compat nel sorgente (commit 3/6/2026) ma NON nella 21.1.7 rilasciata: copiare ricetta + loot table tree_drops da BT (LGPL-2.1) |
| `bountifulfares:leek_seeds` | `bountifulfares:leeks` | age=0..7 | leek, leek_seeds | dirt |  |
| `bountifulfares:maize_seeds` | `bountifulfares:maize_crop` | age=0..7, half=lower/upper | maize | dirt | alta 2 blocchi (half lower/upper) |
| `bountifulfares:hoary_seeds` | `bountifulfares:hoary_apple_sapling_crop` _(bassa priorità)_ | age=0..1 | hoary_seeds | dirt | i semi crescono (age 0..1) e diventano un alberello di melo canuto; **drops:** bountifulfares:hoary_apple_sapling |
| `bountifulfares:tea_berries` | `bountifulfares:tea_shrub` | age=0..4, berries=true/false | tea_berries | dirt | age 0..4 + berries; foglie con le cesoie, bacche col bonemeal; **drops:** bountifulfares:tea_leaves, bountifulfares:tea_berries |
| `bountifulfares:scorchkin_seeds` | `bountifulfares:scorchkin_stem` | age=0..3, attached=true/false | scorchkin_seeds | custom: blocco solido sopra + lava vicino (in pratica: soil/lava o nether) | stelo APPESO al soffitto che fa crescere il frutto scorchkin sotto, solo vicino alla lava; **drops:** bountifulfares:scorchkin; display: `bountifulfares:scorchkin` |
| `bountifulfares:spongekin_seeds` | `bountifulfares:spongekin_stem` | age=0..3, attached=true/false | spongekin_seeds | water | stelo subacqueo; il frutto spongekin cresce sopra; **drops:** bountifulfares:spongekin; display: `bountifulfares:spongekin` |
| `bountifulfares:spongekin_sprout` | `bountifulfares:spongekin_sprout` _(bassa priorità)_ | - | spongekin_seeds, spongekin_sprout | water | loot: spongekin_seeds |
| `bountifulfares:elderberries` | `trellis:elderberry` | - | - | dirt | coltura su graticcio (data-driven, nessun blocco dedicato): serve ricetta botanypots:crop con display a scelta (es. wild_*_vine o il graticcio); **drops:** bountifulfares:elderberries |
| `bountifulfares:lapisberry_seeds` | `trellis:lapisberry` | - | - | dirt | coltura su graticcio (data-driven, nessun blocco dedicato): serve ricetta botanypots:crop con display a scelta (es. wild_*_vine o il graticcio); **drops:** bountifulfares:lapisberries |
| `bountifulfares:passion_fruit` | `trellis:passion_fruit` | - | - | dirt | coltura su graticcio (data-driven, nessun blocco dedicato): serve ricetta botanypots:crop con display a scelta (es. wild_*_vine o il graticcio); **drops:** bountifulfares:passion_fruit |
| `bountifulfares:chamomile_flowers` | `bountifulfares:chamomile_flowers` | flower_amount=1..4 | chamomile_flowers | dirt |  |
| `bountifulfares:honeysuckle` | `bountifulfares:honeysuckle` | - | honeysuckle | dirt |  |
| `bountifulfares:violet_bellflower` | `bountifulfares:violet_bellflower` | - | violet_bellflower | dirt |  |
| `bountifulfares:prismarine_blossom` | `bountifulfares:prismarine_blossom` | - | prismarine_blossom, minecraft:prismarine_crystals, minecraft:prismarine_shard | water | loot: prismarine_crystals/shard |
| `bountifulfares:wild_beetroots` | `bountifulfares:wild_beetroots` | - | wild_beetroots, minecraft:beetroot_seeds | dirt |  |
| `bountifulfares:wild_carrots` | `bountifulfares:wild_carrots` | - | wild_carrots, minecraft:carrot | dirt |  |
| `bountifulfares:wild_potatoes` | `bountifulfares:wild_potatoes` | - | wild_potatoes, minecraft:potato | dirt |  |
| `bountifulfares:wild_wheat` | `bountifulfares:wild_wheat` | - | wild_wheat, minecraft:wheat_seeds | dirt |  |
| `bountifulfares:wild_leeks` | `bountifulfares:wild_leeks` | - | leek_seeds, wild_leeks | dirt |  |
| `bountifulfares:wild_maize` | `bountifulfares:wild_maize` | half=lower/upper | maize_seeds, wild_maize | dirt | alta 2 blocchi |
| `bountifulfares:wild_elderberry_vine` | `bountifulfares:wild_elderberry_vine` | - | elderberries, wild_elderberry_vine | dirt |  |
| `bountifulfares:wild_passion_fruit_vine` | `bountifulfares:wild_passion_fruit_vine` | - | passion_fruit, wild_passion_fruit_vine | dirt |  |

#### Ars Elemental (CurseForge) (1)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `ars_elemental:sparkflower` | `ars_elemental:sparkflower` | - | sparkflower | dirt |  |

#### Reactive 10.2.1 (2)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `reactive:flower_vine` | `reactive:flower_vine` _(bassa priorità)_ | - | flower_vine | dirt | nasce da reazioni alchemiche, non è una coltura |
| `reactive:mind_lichen` | `reactive:mind_lichen` _(bassa priorità)_ | - | mind_lichen | dirt | variante del glow lichen creata dalle reazioni |

#### Deep Aether 1.1.5.1 (21)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `deep_aether:squash_seeds` | `deep_aether:squash_stem` | age=0..7 | - | dirt | come la zucca: il frutto è casuale fra blue/green/purple_squash; **drops:** deep_aether:blue_squash (34%), deep_aether:green_squash (33%), deep_aether:purple_squash (33%); display: `deep_aether:blue_squash` |
| `deep_aether:goldenleaf_berries` | `deep_aether:golden_vines` | berries=true/false | goldenleaf_berries | dirt | tipo cave vines (appesa): rotation X_180; BP imposta berries=true |
| `deep_aether:lightcap_mushrooms` | `deep_aether:lightcap_mushrooms` | - | lightcap_mushrooms | mushroom |  |
| `deep_aether:aerlavender` | `deep_aether:aerlavender` | - | aerlavender | dirt |  |
| `deep_aether:aether_cattails` | `deep_aether:aether_cattails` | - | aether_cattails | dirt |  |
| `deep_aether:echaisy` | `deep_aether:echaisy` | - | echaisy | dirt |  |
| `deep_aether:enchanted_blossom` | `deep_aether:enchanted_blossom` | - | enchanted_blossom | dirt |  |
| `deep_aether:golden_aspess` | `deep_aether:golden_aspess` | - | golden_aspess | dirt |  |
| `deep_aether:iaspove` | `deep_aether:iaspove` | - | iaspove | dirt |  |
| `deep_aether:radiant_orchid` | `deep_aether:radiant_orchid` | - | radiant_orchid | dirt |  |
| `deep_aether:sky_tulips` | `deep_aether:sky_tulips` | - | sky_tulips | dirt |  |
| `deep_aether:tall_aerlavender` | `deep_aether:tall_aerlavender` | - | tall_aerlavender | dirt |  |
| `deep_aether:tall_aether_cattails` | `deep_aether:tall_aether_cattails` | half=lower/upper | tall_aether_cattails | dirt | alta 2 blocchi |
| `deep_aether:golden_flower` | `deep_aether:golden_flower` | half=lower/upper | golden_flower | dirt | alta 2 blocchi |
| `deep_aether:feather_grass` | `deep_aether:feather_grass` _(bassa priorità)_ | - | cloudbloom_bouquet, feather_grass | dirt |  |
| `deep_aether:mini_golden_grass` | `deep_aether:mini_golden_grass` _(bassa priorità)_ | - | aether:ambrosium_shard, golden_grass_seeds, mini_golden_grass, minecraft:wheat_seeds | dirt |  |
| `deep_aether:short_golden_grass` | `deep_aether:short_golden_grass` _(bassa priorità)_ | - | aether:ambrosium_shard, golden_grass_seeds, short_golden_grass, minecraft:wheat_seeds | dirt |  |
| `deep_aether:medium_golden_grass` | `deep_aether:medium_golden_grass` _(bassa priorità)_ | - | aether:ambrosium_shard, golden_grass_seeds, medium_golden_grass, minecraft:wheat_seeds | dirt |  |
| `deep_aether:tall_feather_grass` | `deep_aether:tall_feather_grass` _(bassa priorità)_ | half=lower/upper | cloudbloom_bouquet, tall_feather_grass | dirt | alta 2 blocchi |
| `deep_aether:tall_golden_grass` | `deep_aether:tall_golden_grass` _(bassa priorità)_ | half=lower/upper | aether:ambrosium_shard, golden_grass_seeds, medium_golden_grass, minecraft:wheat_seeds | dirt | alta 2 blocchi |
| `deep_aether:yagroot_vine` | `deep_aether:yagroot_vine` _(bassa priorità)_ | - | yagroot_vine | dirt |  |

#### The Undergarden 0.9.6 (21)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `undergarden:underbeans` | `undergarden:underbean_bush` | age=0..3 | underbeans | dirt | loot a age=3: underbeans |
| `undergarden:blisterberry` | `undergarden:blisterberry_bush` | age=0..3 | blisterberry, rotten_blisterberry | dirt | loot a age=3: blisterberry + rotten_blisterberry |
| `undergarden:ditchbulb` | `undergarden:ditchbulb_plant` | age=0..1 | ditchbulb | dirt | age 0..1; loot age=1: ditchbulb |
| `undergarden:droopvine_item` | `undergarden:droopvine` | glowy=true/false | droopvine_item | dirt | appesa (tipo cave vines): rotation X_180; il frutto dipende da glowy=true (BP non lo imposta); **drops:** undergarden:droopvine_item |
| `undergarden:gloomgourd_seeds` | `undergarden:gloomgourd_stem` | age=0..7 | gloomgourd_seeds | dirt | come melone/zucca (StemBlock); **drops:** loot:undergarden:blocks/gloomgourd; display: `undergarden:gloomgourd` |
| `undergarden:glitterkelp` | `undergarden:glitterkelp` | age=0..25 | glitterkelp | water | tipo kelp |
| `undergarden:blood_mushroom` | `undergarden:blood_mushroom` | - | blood_mushroom | mushroom |  |
| `undergarden:indigo_mushroom` | `undergarden:indigo_mushroom` | - | indigo_mushroom | mushroom |  |
| `undergarden:ink_mushroom` | `undergarden:ink_mushroom` | - | ink_mushroom | mushroom |  |
| `undergarden:veil_mushroom` | `undergarden:veil_mushroom` | - | veil_mushroom | mushroom |  |
| `undergarden:puff_mushroom` | `undergarden:puff_mushroom` | - | puff_mushroom | mushroom |  |
| `undergarden:amorous_bristle` | `undergarden:amorous_bristle` | - | amorous_bristle | dirt |  |
| `undergarden:butterbunch` | `undergarden:butterbunch` | - | butterbunch | dirt |  |
| `undergarden:miserabell` | `undergarden:miserabell` | - | miserabell | dirt |  |
| `undergarden:shimmerweed` | `undergarden:shimmerweed` | - | shimmerweed | dirt |  |
| `undergarden:tall_shimmerweed` | `undergarden:tall_shimmerweed` | half=lower/upper | shimmerweed | dirt | alta 2 blocchi; loot: shimmerweed |
| `undergarden:deepturf` | `undergarden:deepturf` _(bassa priorità)_ | - | deepturf | dirt |  |
| `undergarden:ashen_deepturf` | `undergarden:ashen_deepturf` _(bassa priorità)_ | - | ashen_deepturf | dirt |  |
| `undergarden:frozen_deepturf` | `undergarden:frozen_deepturf` _(bassa priorità)_ | - | frozen_deepturf | dirt |  |
| `undergarden:tall_deepturf` | `undergarden:tall_deepturf` _(bassa priorità)_ | half=lower/upper | deepturf | dirt |  |
| `undergarden:mushroom_veil` | `undergarden:mushroom_veil` _(bassa priorità)_ | - | mushroom_veil | dirt | liana appesa |

#### Deeper and Darker 1.4.1 (1)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `deeperdarker:gloomy_cactus` | `deeperdarker:gloomy_cactus` | - | gloomy_cactus | sculk (nel mondo solo su gloomy_sculk) | BP tratta gloomy_sculk come coltura, non come terreno: usare botanypots:soil/sculk |

#### Unusual End 2.3.1b (19)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `unusualend:chorus_cane` | `unusualend:chorus_cane` | - | chorus_cane | end | colonna tipo canna (blooming_chorus_cane è la variante fiorita, drop chorus_cane) |
| `unusualend:chorus_fungus` | `unusualend:chorus_fungus` | - | chorus_fungus | end |  |
| `unusualend:chorus_roots` | `unusualend:chorus_roots` | - | chorus_roots | end |  |
| `unusualend:endstone_sprouts` | `unusualend:endstone_sprouts` _(bassa priorità)_ | - | endstone_sprouts | end |  |
| `unusualend:purpur_grass` | `unusualend:purpur_grass` _(bassa priorità)_ | - | purpur_grass | end |  |
| `unusualend:flowering_purpur_grass` | `unusualend:flowering_purpur_grass` | - | chorus_petal, flowering_purpur_grass | end | loot: chorus_petal |
| `unusualend:crystal_flower` | `unusualend:crystal_flower` | - | crystal_flower, shiny_crystal | dirt | loot: shiny_crystal; terra/erba/gloopstone |
| `unusualend:gloopy_bush` | `unusualend:gloopy_bush` | - | gloopy_bush | dirt |  |
| `unusualend:gloopy_tendrils` | `unusualend:gloopy_tendrils` _(bassa priorità)_ | - | gloopy_tendrils | dirt |  |
| `unusualend:shiny_spirea` | `unusualend:shiny_spirea` | - | shiny_spirea | dirt |  |
| `unusualend:flowering_gloopy_pile` | `unusualend:flowering_gloopy_pile` _(bassa priorità)_ | half=lower/upper | flowering_gloopy_pile | dirt | alta 2 blocchi |
| `unusualend:warped_bush` | `unusualend:warped_bush` | - | warped_bush | end | col bonemeal diventa grown_warped_bush, che a clic destro dà warped_berries; **drops:** unusualend:warped_berries; display: `unusualend:grown_warped_bush` |
| `unusualend:warped_algae` | `unusualend:warped_algae` | - | warped_algae | end |  |
| `unusualend:small_warped_algae` | `unusualend:small_warped_algae` _(bassa priorità)_ | - | small_warped_algae | end |  |
| `unusualend:warped_sprouts` | `unusualend:warped_sprouts` _(bassa priorità)_ | - | warped_sprouts | end |  |
| `unusualend:warped_endstone_sprouts` | `unusualend:warped_endstone_sprouts` _(bassa priorità)_ | - | warped_endstone_sprouts | end |  |
| `unusualend:small_warped_squash` | `unusualend:small_warped_squash` | - | small_warped_squash | end | zucca della Warped Reef (piccola -> grande col bonemeal); **drops:** unusualend:warped_squash_wedge, unusualend:warped_squash; display: `unusualend:warped_squash` |
| `unusualend:gloopilon_seeds` | `unusualend:gloopilon_bulb` | age=0..2 | gloopilon_slice | custom: dripping_gloopstone sopra | cresce APPESO sotto dripping gloopstone (seeds -> stem -> bulb age 0..2): rotation X_180; **drops:** unusualend:gloopilon_slice |
| `unusualend:chorus_cane_flower` | `unusualend:chorus_cane_flower` _(bassa priorità)_ | - | chorus_cane_flower | dirt | fiore da parete/pavimento (face) |

#### The Twilight Forest 4.8.3345 (CurseForge) (12)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `twilightforest:raspberry_bush` | `twilightforest:raspberry_bush` | age=0..3 | raspberry_bush | dirt | TF berry bush age 0..3 (+ layers neve); le bacche vengono da una loot table separata; **drops:** loot:twilightforest:blocks/raspberry_bush_berries |
| `twilightforest:blueberry_bush` | `twilightforest:blueberry_bush` | age=0..3 | blueberry_bush | dirt | TF berry bush age 0..3 (+ layers neve); le bacche vengono da una loot table separata; **drops:** loot:twilightforest:blocks/blueberry_bush_berries |
| `twilightforest:blackberry_bush` | `twilightforest:blackberry_bush` | age=0..3 | blackberry_bush | dirt | TF berry bush age 0..3 (+ layers neve); le bacche vengono da una loot table separata; **drops:** loot:twilightforest:blocks/blackberry_bush_berries |
| `twilightforest:maloberry_bush` | `twilightforest:maloberry_bush` | age=0..3 | maloberry_bush | dirt | TF berry bush age 0..3 (+ layers neve); le bacche vengono da una loot table separata; **drops:** loot:twilightforest:blocks/maloberry_bush_berries |
| `twilightforest:blightberry_bush` | `twilightforest:blightberry_bush` | age=0..3 | blightberry_bush | nether | cespuglio della Dark Tower: vive su netherrack/blackstone/soul sand/soul soil; **drops:** loot:twilightforest:blocks/blightberry_bush_berries |
| `twilightforest:duskberry_bush` | `twilightforest:duskberry_bush` | age=0..3 | duskberry_bush | nether | cespuglio della Dark Tower: vive su netherrack/blackstone/soul sand/soul soil; **drops:** loot:twilightforest:blocks/duskberry_bush_berries |
| `twilightforest:skyberry_bush` | `twilightforest:skyberry_bush` | age=0..3 | skyberry_bush | nether | cespuglio della Dark Tower: vive su netherrack/blackstone/soul sand/soul soil; **drops:** loot:twilightforest:blocks/skyberry_bush_berries |
| `twilightforest:stingberry_bush` | `twilightforest:stingberry_bush` | age=0..3 | stingberry_bush | nether | cespuglio della Dark Tower: vive su netherrack/blackstone/soul sand/soul soil; **drops:** loot:twilightforest:blocks/stingberry_bush_berries |
| `twilightforest:iron_oreberry` | `twilightforest:iron_oreberry` | age=0..3 | iron_oreberry | stone (#c:stones; botanypots:soil/moss li include) | cespuglio di bacche-minerale: su pietra, luce < 13 nel mondo; **drops:** loot:twilightforest:blocks/iron_oreberry_bush_berries |
| `twilightforest:gold_oreberry` | `twilightforest:gold_oreberry` | age=0..3 | gold_oreberry | stone (#c:stones; botanypots:soil/moss li include) | cespuglio di bacche-minerale: su pietra, luce < 13 nel mondo; **drops:** loot:twilightforest:blocks/gold_oreberry_bush_berries |
| `twilightforest:copper_oreberry` | `twilightforest:copper_oreberry` | age=0..3 | copper_oreberry | stone (#c:stones; botanypots:soil/moss li include) | cespuglio di bacche-minerale: su pietra, luce < 13 nel mondo; **drops:** loot:twilightforest:blocks/copper_oreberry_bush_berries |
| `twilightforest:essence_oreberry` | `twilightforest:essence_oreberry` | age=0..3 | essence_oreberry | stone (#c:stones; botanypots:soil/moss li include) | cespuglio di bacche-minerale: su pietra, luce < 13 nel mondo; **drops:** loot:twilightforest:blocks/essence_berry_bush_berries |

#### Regions Unexplored 0.6.2 (9)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `regions_unexplored:blue_bioshroom` | `regions_unexplored:blue_bioshroom` | - | blue_bioshroom | mushroom | come green/pink/yellow_bioshroom di Botany Trees (che però salta il blu); **drops:** regions_unexplored:blue_bioshroom_stem, regions_unexplored:blue_bioshroom_block, regions_unexplored:glowing_blue_bioshroom_block, regions_unexplored:blue_bioshroom (5%) |
| `regions_unexplored:salmon_poppy` | `regions_unexplored:salmon_poppy` | - | salmon_poppy | dirt |  |
| `regions_unexplored:salmon_wisteria_shrub` | `regions_unexplored:salmon_wisteria_shrub` | half=lower/upper | salmon_wisteria_shrub | dirt | alta 2 blocchi |
| `regions_unexplored:lavender_wisteria_vines` | `regions_unexplored:lavender_wisteria_vines` _(bassa priorità)_ | - | lavender_wisteria_vines | dirt | liana appesa (tip) |
| `regions_unexplored:salmon_wisteria_vines` | `regions_unexplored:salmon_wisteria_vines` _(bassa priorità)_ | - | salmon_wisteria_vines | dirt | liana appesa (tip) |
| `regions_unexplored:sky_wisteria_vines` | `regions_unexplored:sky_wisteria_vines` _(bassa priorità)_ | - | sky_wisteria_vines | dirt | liana appesa (tip) |
| `regions_unexplored:tall_hyacinth_stock` | `regions_unexplored:tall_hyacinth_stock` _(bassa priorità)_ | - | tall_hyacinth_stock | water | pianta subacquea a colonna (forma tip/frustum) |
| `regions_unexplored:redstone_bud` | `regions_unexplored:redstone_bud` _(bassa priorità)_ | - | minecraft:redstone, redstone_bud | stone | germoglio su pietra che droppa redstone: farm di redstone, valutare |
| `regions_unexplored:saguaro_cactus_flower` | `regions_unexplored:saguaro_cactus_flower` _(bassa priorità)_ | - | saguaro_cactus_flower | sand | ex cactus_flower (alias); BP ha solo saguaro_cactus |

#### Friends & Foes (fuori lista, già nel pack) (1)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `friendsandfoes:buttercup` | `friendsandfoes:buttercup` _(bassa priorità)_ | - | buttercup | dirt | mod fuori dalla lista richiesta ma presente nel pack |

### 2. Dichiarate da BotanyCompatLayer (scrivere solo ciò che BCL non copre)

Dopo aver installato BCL, `/botanypots debug missing seeds` dice quali di queste mancano ancora.

#### [Let's Do] HerbalBrews 1.1.4 (9)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `herbalbrews:coffee_beans` | `herbalbrews:coffee_plant` | age=0..3 | coffee_beans | dirt | clic destro dà coffee_beans; loot a age=3 ok |
| `herbalbrews:tea_blossom` | `herbalbrews:tea_plant` | age=0..3 | green_tea_leaf, tea_blossom | dirt | loot age=3: green_tea_leaf + tea_blossom |
| `herbalbrews:rooibos_leaf` | `herbalbrews:rooibos_plant` | age=0..3 | rooibos_leaf | dirt |  |
| `herbalbrews:yerba_mate_leaf` | `herbalbrews:yerba_mate_plant` | age=0..3 | yerba_mate_leaf | dirt |  |
| `herbalbrews:wild_coffee_plant` | `herbalbrews:wild_coffee_plant` | - | coffee_beans, wild_coffee_plant | dirt |  |
| `herbalbrews:wild_rooibos_plant` | `herbalbrews:wild_rooibos_plant` | - | rooibos_leaf, wild_rooibos_plant | dirt |  |
| `herbalbrews:wild_yerba_mate_plant` | `herbalbrews:wild_yerba_mate_plant` | - | wild_yerba_mate_plant, yerba_mate_leaf | dirt |  |
| `herbalbrews:hibiscus` | `herbalbrews:hibiscus` | - | hibiscus, tea_blossom | dirt |  |
| `herbalbrews:lavender` | `herbalbrews:lavender` | - | lavender, lavender_blossom, tea_blossom | dirt |  |

#### Rustic Delight 1.7.1 (in arrivo) (2)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `rusticdelight:dark_bell_pepper_seeds` | `rusticdelight:dark_bell_peppers` | age=0..7 | bell_pepper_black, bell_pepper_blue, bell_pepper_purple, dark_bell_pepper_seeds | dirt | mancante nella compat inclusa nella mod |
| `rusticdelight:pale_bell_pepper_seeds` | `rusticdelight:pale_bell_peppers` | age=0..7 | bell_pepper_orange, bell_pepper_pink, bell_pepper_white, pale_bell_pepper_seeds | dirt | mancante nella compat inclusa nella mod |

#### [Let's Do] Vinery 1.5.5 (8)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `vinery:red_grape_seeds` | `vinery:red_grape_bush` | age=0..3 | red_grape_seeds | dirt | uva a clic destro: il loot dà solo i semi; **drops:** vinery:red_grape |
| `vinery:savanna_grape_seeds_red` | `vinery:savanna_grape_bush_red` | age=0..3 | savanna_grape_seeds_red | dirt | luce minima 14; **drops:** vinery:savanna_grapes_red |
| `vinery:taiga_grape_seeds_red` | `vinery:taiga_grape_bush_red` | age=0..3 | taiga_grape_seeds_red | dirt | nel mondo vuole podzol/coarse dirt vicino; **drops:** vinery:taiga_grapes_red |
| `vinery:jungle_grape_seeds_red` | `vinery:jungle_grape_bush_red` | age=0..3 | jungle_grape_seeds_red | dirt | è una liana (VineBlock) attaccata di lato: display da sistemare (rotazione/offset); **drops:** vinery:jungle_grapes_red |
| `vinery:white_grape_seeds` | `vinery:white_grape_bush` | age=0..3 | white_grape_seeds | dirt | uva a clic destro: il loot dà solo i semi; **drops:** vinery:white_grape |
| `vinery:savanna_grape_seeds_white` | `vinery:savanna_grape_bush_white` | age=0..3 | savanna_grape_seeds_white | dirt | luce minima 14; **drops:** vinery:savanna_grapes_white |
| `vinery:taiga_grape_seeds_white` | `vinery:taiga_grape_bush_white` | age=0..3 | taiga_grape_seeds_white | dirt | nel mondo vuole podzol/coarse dirt vicino; **drops:** vinery:taiga_grapes_white |
| `vinery:jungle_grape_seeds_white` | `vinery:jungle_grape_bush_white` | age=0..3 | jungle_grape_seeds_white | dirt | è una liana (VineBlock) attaccata di lato: display da sistemare (rotazione/offset); **drops:** vinery:jungle_grapes_white |

#### [Let's Do] Meadow 1.4.9 (8)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `meadow:alpine_poppy` | `meadow:alpine_poppy` | - | alpine_poppy | dirt |  |
| `meadow:delphinium` | `meadow:delphinium` | - | delphinium | dirt |  |
| `meadow:enzian` | `meadow:enzian` | - | enzian | dirt |  |
| `meadow:eriophorum` | `meadow:eriophorum` | - | eriophorum | dirt |  |
| `meadow:fire_lily` | `meadow:fire_lily` | - | fire_lily | dirt |  |
| `meadow:saxifrage` | `meadow:saxifrage` | - | saxifrage | dirt |  |
| `meadow:tall_eriophorum` | `meadow:tall_eriophorum` | half=lower/upper | tall_eriophorum | dirt | alta 2 blocchi |
| `meadow:small_fir` | `meadow:small_fir` _(bassa priorità)_ | half=lower/upper | small_fir, minecraft:wheat_seeds | dirt | alta 2 blocchi |

#### [Let's Do] Farm & Charm 1.1.28 (20)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `farm_and_charm:barley_seeds` | `farm_and_charm:barley_crop` | age=0..4 | barley, barley_seeds | dirt |  |
| `farm_and_charm:kernels` | `farm_and_charm:corn_crop` | age=0..4 | corn, kernels | dirt |  |
| `farm_and_charm:lettuce_seeds` | `farm_and_charm:lettuce_crop` | age=0..3 | lettuce | dirt | big/giant: il derivato prende lo stato normale |
| `farm_and_charm:oat_seeds` | `farm_and_charm:oat_crop` | age=0..5 | oat, oat_seeds | dirt |  |
| `farm_and_charm:onion` | `farm_and_charm:onion_crop` | age=0..4 | onion | dirt |  |
| `farm_and_charm:strawberry_seeds` | `farm_and_charm:strawberry_crop` | age=0..5 | strawberry, strawberry_seeds | dirt |  |
| `farm_and_charm:tomato_seeds` | `farm_and_charm:tomato_crop` | age=0..4 | rope, tomato, tomato_seeds | dirt | rampicante con corda (tomato_crop + tomato_crop_body); il loot dà anche farm_and_charm:rope se supported |
| `farm_and_charm:wild_barley` | `farm_and_charm:wild_barley` | - | barley, barley_seeds, wild_barley | dirt |  |
| `farm_and_charm:wild_beetroots` | `farm_and_charm:wild_beetroots` | - | wild_beetroots, minecraft:beetroot, minecraft:beetroot_seeds | dirt |  |
| `farm_and_charm:wild_carrots` | `farm_and_charm:wild_carrots` | - | wild_carrots, minecraft:carrot | dirt |  |
| `farm_and_charm:wild_emmer` | `farm_and_charm:wild_emmer` | - | wild_emmer, minecraft:wheat, minecraft:wheat_seeds | dirt |  |
| `farm_and_charm:wild_lettuce` | `farm_and_charm:wild_lettuce` | - | lettuce, lettuce_seeds, wild_lettuce | dirt |  |
| `farm_and_charm:wild_nettle` | `farm_and_charm:wild_nettle` | - | wild_nettle | dirt |  |
| `farm_and_charm:wild_oat` | `farm_and_charm:wild_oat` | - | oat, oat_seeds, wild_oat | dirt |  |
| `farm_and_charm:wild_onions` | `farm_and_charm:wild_onions` | - | onion, wild_onions | dirt |  |
| `farm_and_charm:wild_potatoes` | `farm_and_charm:wild_potatoes` | - | wild_potatoes, minecraft:poisonous_potato, minecraft:potato | dirt |  |
| `farm_and_charm:wild_ribwort` | `farm_and_charm:wild_ribwort` | - | wild_ribwort | dirt |  |
| `farm_and_charm:wild_strawberries` | `farm_and_charm:wild_strawberries` | - | strawberry, strawberry_seeds, wild_strawberries | dirt |  |
| `farm_and_charm:wild_tomatoes` | `farm_and_charm:wild_tomatoes` | - | tomato, tomato_seeds, wild_tomatoes | dirt |  |
| `farm_and_charm:wild_corn` | `farm_and_charm:wild_corn` | half=lower/upper | corn, kernels, wild_corn | dirt | alta 2 blocchi |

#### The Aether 1.5.10 (3)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `aether:berry_bush_stem` | `aether:berry_bush` | - | berry_bush, berry_bush_stem, blue_berry | dirt | lo stelo (berry_bush_stem) cresce in cespuglio; **drops:** aether:blue_berry; nel mondo vuole terra dell'Aether; nel vaso va bene la terra normale |
| `aether:purple_flower` | `aether:purple_flower` | - | purple_flower | dirt |  |
| `aether:white_flower` | `aether:white_flower` | - | white_flower | dirt |  |

### 3. Regions Unexplored: coperte con vecchi ID (verificare)

Se in gioco questi semi non entrano nel vaso, basta copiare la ricetta di Botany Pots cambiando l'ID.

#### Regions Unexplored 0.6.2 (8)

| Seme / input | Blocco coltura | Crescita (max) | Drop dalla loot table | Terreno | Speciale / drops espliciti |
|---|---|---|---|---|---|
| `regions_unexplored:grass_sprouts` | `regions_unexplored:grass_sprouts` | - | minecraft:wheat_seeds, grass_sprouts | dirt | BP 1.21.1 lo copre coi vecchi ID stone_bud/medium_grass, rinominati in RU 0.6 (alias) |
| `regions_unexplored:lavender_wisteria_shrub` | `regions_unexplored:lavender_wisteria_shrub` | half=lower/upper | lavender_wisteria_shrub | dirt | BP lo copre col vecchio ID mauve_shrub (alias RU 0.6) |
| `regions_unexplored:sky_wisteria_shrub` | `regions_unexplored:sky_wisteria_shrub` | half=lower/upper | sky_wisteria_shrub | dirt | BP lo copre col vecchio ID enchanted_birch_shrub (alias RU 0.6) |
| `regions_unexplored:maple_leaf_litter` | `regions_unexplored:maple_leaf_litter` | flower_amount=1..4 | maple_leaf_litter | dirt | BP lo copre col vecchio ID maple_leaf_pile (alias RU 0.6) |
| `regions_unexplored:red_maple_leaf_litter` | `regions_unexplored:red_maple_leaf_litter` | flower_amount=1..4 | red_maple_leaf_litter | dirt | BP lo copre col vecchio ID red_maple_leaf_pile (alias RU 0.6) |
| `regions_unexplored:orange_maple_leaf_litter` | `regions_unexplored:orange_maple_leaf_litter` | flower_amount=1..4 | orange_maple_leaf_litter | dirt | BP lo copre col vecchio ID orange_maple_leaf_pile (alias RU 0.6) |
| `regions_unexplored:silver_birch_leaf_litter` | `regions_unexplored:silver_birch_leaf_litter` | flower_amount=1..4 | silver_birch_leaf_litter | dirt | BP lo copre col vecchio ID silver_birch_leaf_pile (alias RU 0.6) |
| `regions_unexplored:enchanted_birch_leaf_litter` | `regions_unexplored:enchanted_birch_leaf_litter` | flower_amount=1..4 | enchanted_birch_leaf_litter | dirt | BP lo copre col vecchio ID enchanted_birch_leaf_pile (alias RU 0.6) |

### 4. Saltate

- `culturaldelights:magic_beans`: fagiolo magico che genera un beanstalk gigante: non adatto ai vasi
- `vinery:grapevine_stem`: vite su graticcio (lattice): sistema a più blocchi, meglio usare i cespugli
- `twilightforest:magic_beans`: beanstalk gigante: non adatto ai vasi

### 5. Terreni da aggiungere

- `twilightdelight:twilight_rich_soil` (Twilight's Flavor & Delight 3.2.6): per le colonie (fiddlehead_clump, mushgloom_colony)
- `twilightdelight:twilight_rich_soil_farmland` (Twilight's Flavor & Delight 3.2.6)
- `mynethersdelight:resurgent_soil` (My Nether's Delight 1.10.4 (in arrivo)): terra del Nether (stile rich soil)
- `mynethersdelight:resurgent_soil_farmland` (My Nether's Delight 1.10.4 (in arrivo))
- `mynethersdelight:letios_compost` (My Nether's Delight 1.10.4 (in arrivo)): compost del Nether
- `hexalia:infused_dirt` (Hexalia 1.3.6): nel tag minecraft:dirt
- `hexalia:infused_farmland` (Hexalia 1.3.6): serve anche al saltsprout
- `farm_and_charm:fertilized_soil` ([Let's Do] Farm & Charm 1.1.28)
- `farm_and_charm:fertilized_farmland` ([Let's Do] Farm & Charm 1.1.28)
- `vinery:loam` ([Let's Do] Vinery 1.5.5): facoltativo
- `aether:aether_dirt / aether_grass_block / enchanted_aether_grass_block / aether_farmland` (The Aether 1.5.10): la descrizione di BCL parla di 'extra natural soil blocks'
- `deep_aether:aether_mud / aether_coarse_dirt / aerglow_grass_block / golden_heights_grass_block / aether_moss_block` (Deep Aether 1.1.5.1): facoltativi
- `bountifulfares:grassy_dirt` (Bountiful Fares 3.0.12): facoltativo (nel tag minecraft:dirt)

## Fonti e versioni

- Botany Pots: sorgente `Darkhax-Minecraft/BotanyPots` ramo 1.21.1 al commit 335c997 = release 21.1.44 (13/6/2026). Botany Trees: ramo 1.21.1, release 21.1.7 (2/6/2026); i commit successivi aggiungono solo Irregular Implements e Bountiful Fares.
- Mod: sorgenti 1.21.1 clonati in `scratchpad/repos` (Bountiful Fares dal ramo `1.21-ML` 3.0.13, Brewin' and Chewin' dal tag `4.5.0+1.21.1`, Hexalia confrontato fra 1.3.6 e HEAD: stesse piante). Sorgente chiuso: Delightful Fares, Undergarden Delight, Chef's Delight, Create Confectionery, Roaster's Delight (valutati dalla descrizione).
- BotanyCompatLayer: solo la descrizione Modrinth (v1.0.0, 28/9/2026, MIT).
- Il dettaglio macchina-leggibile è in `crop_coverage.json` (stesso contenuto, con loot e proprietà di crescita). Per ogni pianta non coperta c'è anche `recipe_draft`: una bozza di ricetta 1.21.1 (load condition, block, input, soil, display, rotation, drops espliciti) da rivedere prima dell'uso; mancano solo le colture su graticcio di Bountiful Fares e Roaster's Delight.
- Script di generazione: `research/cropscripts/` (covindex.py, inventory.py, javainfo.py, curated.py, build_outputs.py).
