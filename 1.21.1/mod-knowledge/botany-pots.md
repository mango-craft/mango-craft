# Botany Pots (+ Botany Trees, BotanyPotsAdditions, Botany Pots Tiers)

Aggiornata il 22/10/2026 · nel pack dalla 0.1.1: Botany Pots 21.1.44, Botany Trees 21.1.7, Botany Pots Tiers 7.0.11, BotanyPotsAdditions 1.1.0, Bookshelf 21.1.81 (versioni in `../docs/0403-distinta-mod.md`) · fonti: sorgenti 1.21.1 di Botany Pots e Botany Trees, file delle mod del pack, inventario. Ricerca e conteggi: `../lavoro/versioni/v0.2.3.md`; grezzo `../../ai-agents/stage/2026-10-17_1.21.1-v0.2.3_vasi/`; lavoro in corso `../lavoro/versioni/v0.6.1.md`; sorgente di Botany Pots letto il 22/10 (`Darkhax-Minecraft/botanypots`, ramo `1.21.1`, commit `335c997`).

## Cose da non rompere

- Le ricette in formato 1.20 vengono **ignorate** (es. quella inclusa in Ars Elemental, con namespace `botany_pots`, B19: riscritta nel nostro datapack).
- Le piante raccolte col click destro richiedono **raccolti espliciti**: la loro loot table dà solo la pianta o i semi.
- Nessun datapack esterno (BotanyCompatLayer non si installa): tutto nel nostro, copiando solo da licenze che lo permettono.

## Formato delle ricette (1.21.1)

- **Coltura**: `botanypots:block_derived_crop` con `"block"`; seme, aspetto e raccolto si ricavano dal blocco (stato a età massima) e dalla sua loot table. Esempio minimo, come nelle ricette vanilla: `{"type":"botanypots:block_derived_crop","block":"minecraft:wheat"}`. Terreno di default: `botanypots:soil/dirt`.
- **Terreno**: `botanypots:block_derived_soil`, un file per blocco.
- **Raccolti espliciti**: `"drops":[{"type":"botanypots:loot_table","table_id":"…"}]` oppure `{"type":"botanypots:items","items":[{"result":{"id":"…","count":1},"chance":1.0}]}`.
- **Terreni speciali**: acqua = etichetta `botanypots:soil/water`; funghi = `minecraft:mushroom_grow_block` o `botanypots:soil/mushroom`; Nether = `minecraft:nylium` o `botanypots:soil/nether`; End = `botanypots:soil/end`; poi `sand`, `sculk`, `moss`. Nessun terreno di lava trovato nell'inventario (serve per le alghe di Nether Depths: da verificare).
- **Piante appese**: `render_options.rotation: X_180`, come le liane delle grotte.
- **Alberi**: schema di Botany Trees, `block_derived_crop` sull'alberello, `grow_time` 2400 e raccolto da una loot table nostra (modello: `botanytrees:tree_drops/…`).
- **Campi verificati nel sorgente (22/10)**: `block_derived_crop` = `block` (obbligatorio), `input`, `soil` (di serie l'etichetta `botanypots:soil/dirt`), `grow_time` (1200), `display`, `light_level`, `drops`, `render_options`, `function`, `pot_predicate`, `yield`, `yield_scale`; se manca `drops` si usa il raccolto del blocco maturo (stato con età massima, o `berries=true`). `block_derived_soil` = `block`, `input`, `display`, `growth_modifier` (0,15 per la terra ricca di Farmer's Delight), `light_level`, `render_options`, `yield_modifier`; **ricava l'oggetto dal blocco**: se il blocco non ha un oggetto la ricetta non si carica. Una terra nuova entra nelle colture di terra solo se il suo oggetto è nell'etichetta `botanypots:soil/dirt`.
- **Raccolto ricavato dal blocco = vaso senza attrezzo** (sorgente e jar dell'istanza di prova, 22/10): di serie lo slot attrezzo è vuoto (`default_harvest_stack` della config di Botany Pots). Le tabelle del bottino che chiedono le **cesoie** o un incantesimo (erba alta, liane, piante selvatiche) non danno la pianta intera se il giocatore non mette le cesoie nello slot attrezzo: o non danno niente (15 casi), o danno solo il prodotto normale (semi o ortaggio). Se la tabella esiste ma non dà niente, non scatta nemmeno il raccolto di ripiego. 15 piante (Undergarden, Unusual End, Deep Aether, Hexerei) non avrebbero dato niente e hanno il raccolto scritto a mano (`raccolti_diretti` in `../data/vasi/aggiunte.json`, quello che darebbero con le cesoie); altre 49 (piante selvatiche) danno senza cesoie il loro prodotto (semi, carota, patata, bacche…) invece della pianta selvatica intera che darebbero con le cesoie (verificato sui jar il 22/10, 47 su 49; le altre 2 danno lo stesso): vanno bene così e non si toccano. Controllo statico sui jar: `scripts/vasi_verifica_jar.py`.
- **Condizioni di caricamento**: `bookshelf:load_conditions` con `bookshelf:block_exists` sui blocchi usati (come i file attuali di Ars) oppure `neoforge:conditions` con `neoforge:mod_loaded`.
- Nel jar di Botany Pots: 1.183 ricette `block_derived_crop`, 239 `block_derived_soil`, 18 `soil`, 6 `pot_interaction`, 1 `fertilizer`, 1 `crop` (inventario).

## Casi particolari delle mod del pack

- **Piante raccolte col click destro** (Hexerei, Vinery, cespugli di bacche di Twilight, voidpepper di Ender's Delight, bullet pepper di My Nether's Delight, cespuglio di tè di Bountiful Fares, warped bush di Unusual End): raccolti espliciti, indicati pianta per pianta nella tabella in stage.
- **Alberi di Bountiful Fares**: le 8 ricette e le tabelle dei raccolti esistono nel sorgente di Botany Trees (LGPL-2.1, commit `eee0890`, dopo la 21.1.7; nessuna versione su Modrinth li ha ancora, controllato il 22/10). **Copiati dalla 0.6.1** in `alberi/` e `loot_table/tree_drops/` del nostro datapack, con la fonte nei readme; si tolgono quando esce la versione di Botany Trees che li contiene (altrimenti ogni alberello avrebbe due colture).
- **Terreno di lava** (verificato il 22/10): Botany Pots ce l'ha: l'etichetta `botanypots:soil/lava` (secchio di lava; anche quello di edelwood di Forbidden Arcanus). Le alghe di Nether Depths Upgrade lo usano.
- **Piante che condividono il seme con una vanilla** (Jaden's: `soul_torchflower_crop` ← `minecraft:torchflower_seeds`, `sorrowsquash_stem_plant` ← `minecraft:pumpkin_seeds`): il vaso sceglie la coltura dal seme, quindi una seconda ricetta con lo stesso seme confonderebbe la torchflower e la zucca di Botany Pots: non si scrivono.
- **Bountiful Fares, graticci** (verificato sul jar il 22/10): sambuco, lapisberry e frutto della passione **non sono blocchi**: sono dati (`data/bountifulfares/bountifulfares/trellis_crop/*.json`: seme, prodotto, 4 fasi, 1–3 raccolti) che il graticcio mostra con la sua tessitura. Un `block_derived_crop` non può derivarli: sono scritti come colture normali (`botanypots:crop`) con il seme, un raccolto fisso (la media di quello a mano) e l'aspetto del graticcio a foglie `vine_trellis`. Vengono dalla sezione `colture_libere` di `aggiunte.json`; l'aspetto in gioco è da provare.
- **Terreni da aggiungere**: terra ricca e arata di Twilight's Flavor & Delight; terra risorgente, arata e compost letios di My Nether's Delight; terra infusa e arata di Hexalia (servono anche al saltsprout); terra e arato fertilizzati di Farm & Charm; loam di Vinery; terre di Aether e Deep Aether e terra erbosa di Bountiful Fares (facoltativi). Le 5 terre fertilizzate di Farming for Blockheads sono già terreni (anche nell'etichetta `botanypots:soil/dirt`).
- **Terreni particolari**: alga sirena di Hexalia in acqua, piante di Ender's Delight su pietra dell'End.
- **Roaster's Delight** (sorgente chiuso): blocchi, fasi di crescita (età 0–3) e semi verificati sui jar il 22/10, dalle tabelle del bottino: `coffee_plant` ← `unroasted_coffee_bean`, `tea_bush` ← `tea_seeds`, `chamomile_crop` ← `chamomile_seeds`, `mint_crop` ← `mint_seeds`, `matcha_crop` ← `matcha_seeds`. Il comportamento in gioco resta da provare.
- **Regions Unexplored 0.6** ha rinominato alcuni blocchi (`leaf_pile` → `leaf_litter`, `mauve_shrub` → `lavender_wisteria_shrub`, `stone_bud`/`medium_grass` → `grass_sprouts`, `cactus_flower` → `saguaro_cactus_flower`); Botany Pots usa i nomi vecchi in 8 ricette: se gli alias non funzionano in gioco, si riscrivono.
- **Esclusi**: fagioli magici di Twilight Forest (e le altre piante "rare" o magiche), tronco della vite di Vinery.
- **Ars Nouveau** è già nel nostro datapack (Magebloom, Sourceberry, 5 frutti di archwood come colture sui tronchi; alberi di archwood coperti da Botany Trees): readme nella cartella del datapack.

## Fonti utilizzabili per le ricette

| Fonte | Licenza | Uso | Copre |
|---|---|---|---|
| Sorgenti delle mod | — | Base: nomi, stadi, loot table | Tutto |
| BotanyCompatLayer | MIT | Copiabile citandolo, ma serve lo zip (dallo spazio di lavoro non si scarica) | Aether, Farm & Charm, Vinery, Meadow, HerbalBrews, Rustic Delight |
| Botany Pots Mega Addon (GitHub NamelessGamer06) | MIT | Copiabile citandolo | My Nether's Delight, Expanded Delight, parte di Cultural Delights |
| Botany Trees (sorgente) | LGPL-2.1 | Copiabile citandolo | Alberi di Bountiful Fares |
| LayaTweaks BotanyPots | ARR | Solo confronto | Ars, Cultural Delights |
| More Crop Compatibility, Wizardon's Tweaks | MIT (contenuto non verificato) | Eventuale confronto | Cultural Delights, Expanded Delight |
| Bozze generate il 17/10 (255 ricette, in `../data/vasi/copertura.json`) | nostre | Punto di partenza: dal 22/10 le legge `scripts/vasi_genera.py`, che scrive i file del datapack (con `../data/vasi/aggiunte.json` per terreni e colture a mano) | Tutte le scoperte |

## Comandi di verifica (mondo di prova con i trucchi)

- `/botanypots debug missing seeds true true`: elenca i semi senza ricetta e scrive bozze JSON in `<istanza>/botanypots/generated/crops`.
- `/botanypots debug missing soils true`: lo stesso per i terreni.
- `/botanypots debug check_crops`: piazza un vaso e segnala nel log le colture che non producono niente.

## Da provare

BotanyPotsAdditions e Roaster's Delight da sole prima di affidarci un mondo lungo (mod recenti); Botany Pots Tiers + BotanyPotsAdditions insieme (`../lavoro/0502-prove-in-gioco.md`).
