# Botany Pots: analisi di terreni e colture

Aggiornata il 22/10/2026 · fonti: sorgente di Botany Pots 21.1.44 (commit `335c997`, lo stesso del rilascio su Modrinth) e di Bookshelf 21.1.81 (`5dead24`), inventario dei 255 jar del pack, datapack `matteo_tweaks` · scheda: `botany-pots.md` · base dati: `scripts/botanypots_db.py` (modello qui sotto) · query: `query/`.

Documento vivo: raccoglie i fatti verificati sul funzionamento dei vasi, il modello della base dati e le decisioni sulla progressione dei terreni (0.6.1, in corso).

## 1. Come funziona il vaso (dal codice)

1. Il vaso ha due slot: **terreno** e **seme**. Con l'oggetto nello slot del terreno cerca il **file di terreno** che lo accetta; con l'oggetto nello slot del seme cerca il **file di coltura**. Sono due ricerche separate (`BotanyPotBlockEntity`, `RecipeCache`).
2. La coltura cresce se l'oggetto del terreno sta in almeno uno dei **tag** scritti nel campo `soil` del file di coltura (`BasicCrop.isGrowthSustained`). Se `soil` manca vale `botanypots:soil/dirt`. Il campo accetta un tag di oggetti, un tag di blocchi (`bookshelf:block_tag`) o una lista di alternative (`bookshelf:either`), senza limite di numero.
3. Un tag di blocchi si confronta con l'oggetto di ogni blocco della lista (`BlockTagIngredient`, Bookshelf). Nel pack ogni terreno ha l'oggetto con lo stesso nome del blocco: lo script si ferma se non è così.
4. I **bonus** stanno nel file di terreno: `growth_modifier`, `yield_modifier`, `light_level` (0 se mancano). Tempo (`grow_time`, 1200 tick), resa base (`yield`, 1) e scala (`yield_scale`, 1) stanno nel file di coltura.
5. Tempo effettivo = tempo ÷ (1 + crescita del terreno + efficienza dell'attrezzo + bonus del vaso), arrotondato per difetto. Resa = resa base + scala × (vaso + terreno + attrezzo); la parte intera sono estrazioni sicure, il resto una probabilità (`Helpers`).
6. Il gioco non guarda bioma, dimensione né il mondo: solo i due oggetti negli slot.
7. Ogni file ha un **id** = cartella della mod + percorso sotto `recipe/` (`botanypots:farmersdelight/soil/rich_soil`). Tra file con lo stesso id vince il pacchetto più in alto: il nostro datapack (Paxi lo carica in posizione `TOP`). Per sostituire un file di una mod si scrive un file **nello stesso percorso**; con una condizione sempre falsa lo si spegne. Non ancora provato in gioco.
8. I file hanno **condizioni di caricamento** (`bookshelf:block_exists`, `item_exists`, `neoforge:mod_loaded`): i file di mod assenti si spengono da soli. Dei 1.448 file dei jar ne restano attivi 346 colture e 107 terreni; il datapack ne aggiunge 262 e 23.
9. Il file di terreno non sa chi ci crescerà, e il file di coltura non elenca terreni: la coppia terreno-coltura **si calcola** dai tag.

## 2. Fatti sui dati del pack (22/10/2026)

- Colture attive: 608. Condizioni sul terreno distinte: 19. Colture con una sola alternativa: 566 (481 implicite `soil/dirt`); con due: 42; nessuna con più di due.
- Terreni con file: 130 (124 oggetti distinti in tag usati dalle colture; 6, come neve e ossidiana, non servono nessuna coltura). Oggetti nei tag usati dalle colture senza file di terreno: 114 (candidati).
- Un terreno sta quasi sempre in più tag: la terra in 4, il micelio in 5. Tag annidati fino a 2 livelli; nessun ciclo; 242 tag di oggetti e 183 di blocchi hanno più di una madre.
- Terreni con bonus oggi: 19 (11 delle mod, 8 nostri a 0,15). Resa solo in due terreni di Farming for Blockheads (0,10).
- Il nostro tag `soil/dirt` (17 voci) allarga molto alcuni terreni: le terre dell'Aether passano da 1 a 483 colture; il compost del Nether (`letios_compost`, senza file nelle mod) serve 521 colture, più della terra (507), perché sta anche nei tag dei funghi e del Nether.
- Coppie terreno-coltura: 31.086 sui terreni in vaso, 32.785 con i candidati.

## 3. Modello della base dati

Costruita da `scripts/botanypots_db.py` in `1.21.1/data/vasi/vasi.sqlite` (non nel repository). Vocabolario: **terreno** = l'oggetto nello slot del terreno; **coltura** = la pianta (il suo blocco), descritta da un file; **seme** = l'oggetto nello slot del seme; **tag** = lista con ambito (oggetti/blocchi) e nome.

| Tabella | Contenuto | Chiave |
|---|---|---|
| `TAG` | i tag nominati dalle colture e tutti quelli che contengono | `tag_id`; unici `ambito` + `nome` |
| `TERRENO` | ogni oggetto che può stare nello slot: `stato` in_vaso (ha un file vincente) o candidato | `terreno_id` |
| `COLTURA` | ogni pianta con un file | `coltura_id` |
| `POTS_TERRENO` | i file di terreno attivi: bonus, fonte | `ricetta_id` + `fonte` |
| `POTS_COLTURA` | i file di coltura attivi: tempo, resa base, scala | `ricetta_id` + `fonte` |
| viste `POTS_TERRENO_VINCENTE`, `POTS_COLTURA_VINCENTE` | il file che il gioco usa per ogni id: il nostro datapack vince; tra due jar con lo stesso id l'ordine non è noto (`avviso` = 1, non blocca) | — |
| `POTS_COLTURA_SEME` | i semi di ogni file (origine: file, blocco, eccezione) | ricetta + fonte + seme |
| `POTS_COLTURA_TAG` | i tag ammessi da ogni file, uno per riga; `implicito` per `soil/dirt` non scritto | ricetta + fonte + tag |
| `TERRENO_TAG` | **esplosa**: per ogni terreno tutti i tag in cui sta, con il tag che lo elenca davvero (`tag_diretto_id`), il livello e `da_noi` | terreno + tag + tag diretto |
| `RARITA_POTS_SETTINGS` | la scala: classe → bonus di crescita e resa (CSV a mano) | `classe` |
| `TERRENO_RARITA` | la classe di ogni terreno e il motivo (CSV a mano) | `terreno_id` |
| `TERRENO_TAG_CUSTOM` | i terreni che mettiamo nei tag `botanypots:soil/*` (CSV a mano) | terreno + tag |
| `COLTURA_CUSTOM`, `COLTURA_TAG_CUSTOM`, `COLTURA_RACCOLTO_CUSTOM` | le colture che scriviamo: seme, tempo, grafica, note; i tag ammessi; i raccolti (CSV a mano) | coltura (+ ordine / gruppo, id) |
| vista `POTS_COMPATIBILITA` | terreno × coltura dai file vincenti, con il tag ponte e `da_noi` | — |

Il join delle regole: `TERRENO → TERRENO_TAG → TAG ← POTS_COLTURA_TAG ← POTS_COLTURA`. L'esplosione dei tag (annidamenti risolti, blocchi tradotti in oggetti) avviene solo all'importazione; `da_noi` si ottiene esplodendo due volte, senza e con le voci del datapack. Le condizioni di caricamento si valutano all'importazione sull'inventario. Fuori dal modello: grafica e raccolti dei file delle mod (fase 2), concime e interazioni.

**Il flusso** (dal 22/10): le regole stanno nei CSV `*_custom.csv` e `terreno_rarita.csv` → `scripts/botanypots_genera.py` scrive il datapack (e, per un terreno di una mod a cui la classe dà un bonus diverso, il file allo stesso percorso di quello della mod) → l'inventario e il datapack entrano nella base dati, dove le regole compaiono anche come tabelle `*_CUSTOM` e il loro effetto come righe `nostro` / `da_noi`. Il generatore è stato verificato rigenerando file identici a quelli scritti prima a mano in `aggiunte.json`.

Il database si rifà da solo a ogni `query` se inventario, datapack o CSV sono più recenti; il workflow di controllo (`check.yml`) a ogni push verifica che i file generati corrispondano alle regole (`botanypots_genera.py --verifica`) e rifà il database con i controlli. Controlli eseguiti a ogni `refresh` (il database si sostituisce solo se passano): chiavi esterne; un solo file vincente per terreno e per coltura; nessun seme che trova due colture; ogni coltura con seme, tag e almeno un terreno; coppie della vista uguali al conteggio diretto sui file.

## 4. Decisioni e domande aperte

- 22/10 (sera): **scala di rarità** in `rarita_pots_settings.csv`: 10 classi «natura» (common … mythic) e 10 «craft-diff-0…9», stessi valori per ora (i craft si potranno bilanciare a parte). Crescita 0, 0, 10, 10, 20, 20, 30, 30, 30, 30; resa 0, 6, 2, 6, 2, 6, 2, 6, 10, 14. Simulazione sul codice (tick arrotondati per difetto, bonus sommati a quelli del vaso): la scala sale a ogni gradino nel vaso con tramoggia e nei tre livelli di Botany Pots Tiers (elite +2/+2, ultra +6/+3, mega +10/+4: nel codice sono punti sommati, non moltiplicatori); nel vaso semplice raccolto a mano la resa non conta (`BotanyPotBlock.useItemOn` fa un solo raccolto), quindi i gradini di sola resa valgono quanto quello sotto. Con resa +5 e vasi alti la scala si invertiva; con +10 anche nel vaso con tramoggia: da qui il +2 sui gradini di velocità.
- 22/10 (sera): classi dei 130 terreni in vaso in `terreno_rarita.csv` (ogni terreno ha la sua riga, anche common); 12 file delle mod sostituiti allo stesso percorso (terra ricca FD e aratura, compost organico, 5 arature FFB, terra arata, catalizzatore, uberosa, aratura dell'Undergarden): **da provare in gioco** col tooltip del seme.
- 22/10 (sera): anche i terreni «non di terra» hanno una scala, dove c'è varietà: secchi d'acqua (acqua common, pesci vanilla e girino uncommon, pesce palla e gwibling rare, axolotl super-rare, leviatano neonato di Cataclysm epic) e terra delle anime uncommon rispetto alla sabbia delle anime. Lava, sabbia, sculk, End, funghi e tronchi restano common: un solo terreno o tutti equivalenti.
- Aperto: terreni dell'Undergarden (8) e di Deeper and Darker (3), oggi common; per la regola «altra dimensione» sarebbero rare come quelli dell'Aether. Erba incantata dell'Aether messa super-rare senza aver verificato come si ottiene. I preset del mercato di Farming for Blockheads per i terreni sono disattivati (`enabled: false`): se si attivano nella 0.6.2, le classi dei compost vanno riviste.
- Da provare in gioco: la sostituzione di un file di una mod (sezione 1, punto 7); un oggetto senza file di terreno messo a mano nello slot (per il codice cresce, ma nel vaso semplice non si raccoglie).
- Da decidere: `letios_compost` nel tag `soil/dirt` (oggi serve 521 colture); terreni dell'Undergarden e di Deeper and Darker; provare in gioco la sostituzione di un file di una mod scritta dal generatore (basta assegnare a un terreno con file originale una classe con bonus diverso).
