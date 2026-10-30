# Tema: archeologia e reperti

Aggiornata il 30/10/2026 · stato: **quadro iniziale**, con la **base dati del bottino** dal 30/10 (sezione sotto); gestione delle tabelle di scavo e casse di Better Archeology nella **0.7.5**, aperta il 30/10 (`../lavoro/versioni/v0.7.5.md`; decisione di Matteo del 24/10) · mod coinvolte: Better Archeology, Jaden's Nether Expansion, L_Ender's Cataclysm, Moog's End Structures, YUNG's Better Jungle Temples, YUNG's Better Desert Temples, YUNG's Extras, Lithostitched, Towns and Towers, Dungeons and Taverns, Supplementaries, Ars Nouveau, Corail Tombstone, Artifacts con Relics e Reliquified Artifacts · fonti: inventario del pack (24/10; dal 30/10 formato 8, con il contenuto delle tabelle); dump del gioco del 30/10; scansione dei 253 jar dell'istanza di prova e sorgenti di Artifacts, Ars Nouveau e NeoForge (grezzo: `../../ai-agents/archivio/2026-10-24_1.21.1-v0.7.0_relics-bottino/scavi-risultati.md`); dati vanilla 1.21.1 (`misode/mcmeta`). Schede vicine: `../mod-knowledge/artifacts.md` (reliquie, bottino di Relics), `accessori.md`.

## Dove si scava

| Fonte | Blocchi sospetti | Tabelle di scavo | Note |
|---|---|---|---|
| Minecraft | sabbia, ghiaia | 6: `minecraft:archaeology/desert_pyramid`, `desert_well`, `ocean_ruin_cold`, `ocean_ruin_warm`, `trail_ruins_common`, `trail_ruins_rare` | usate anche da strutture delle mod come tabella principale: Dungeons and Taverns (rovine del deserto), YUNG's Better Desert Temples, pozzi di YUNG's Extras e Lithostitched, Towns and Towers |
| **Better Archeology** | terra sospetta, sabbia rossa sospetta, terra fossilifera | 36 proprie (`betterarcheology:archeology/*`) | 25 strutture: accampamenti dell'archeologo (3), rovine (della sabbia e della mesa), rovine sepolte, catacombe, obelisco del deserto, tempio della luce, tempio della giungla, tumulo, motta, stonehenge, 4 rovine sottomarine, 7 siti di fossili, tomba del villico. 5 sue tabelle contengono quelle vanilla come sotto-tabella (sabbia del deserto, sabbia rossa, ghiaia delle pianure, sabbia sott'acqua, terra della taiga) |
| **Jaden's Nether Expansion** | sabbia d'anime sospetta | 14 (`netherexp:archaeology/*`): biomi del Nether, fortezza, bastione, teschi di bestia, mega fossili | 7 frammenti di vaso propri |
| L_Ender's Cataclysm | — | 2: piramide maledetta (una con la collana) | |
| Moog's End Structures | — | 1: sabbia dell'End (nelle strutture) | |
| YUNG's Better Jungle Temples | — | 1: smeraldi | |
| Towns and Towers | — | 2: rovine nella foresta (comuni, rare) | |
| YUNG's Extras | — | 1 propria (`yungsextras:desert/extra_archeology`) | |
| Supplementaries | mattoni di ghiaia sospetti | — | |

## Strumenti e automazione

- **Pennelli** di Better Archeology: di ferro, di diamante, di netherite (alla forgia).
- **Tavolo dell'archeologia** (Better Archeology): reperti non identificati → identificati; 3 incantamenti suoi (Penetrating Strike, Soaring Winds, Tunneling).
- **Alakarkinos** (Ars Nouveau): granchio che trasforma sabbia e ghiaia in bottino delle tabelle vanilla (6 ricette, pesi 100/25), con un giocatore finto, una volta al minuto circa; tira la tabella come principale, quindi con i modificatori.
- **Corail Tombstone**: aggiunge una sua pool (`tombstone:archeology_treasure`) alle tabelle degli scavi quando si caricano (codice, `LootTableLoadEvent`); quali tabelle esattamente non è verificato.

## Cosa si trova

- **Minecraft**: frammenti di vaso, diamanti, smeraldi, oggetti comuni.
- **Better Archeology**: frammenti di reperto → reperti da identificare; fossili di 7 animali (pollo, creeper, guardiano, ocelot, pecora, villico, lupo), testa e corpo; 4 totem (crescita, splendore, anima, torrente); vasi con bottino; il disco «Swings»; legno marcio.
- **Jaden's**: 7 frammenti di vaso, minerale fossile e combustibile fossile.
- **Artefatti** (reliquie dalla 0.7.0): 1 scavo su 16 nelle 5 tabelle vanilla che Artifacts usava (tutte tranne `trail_ruins_common`); dalla 0.7.0 anche nei 5 scavi di Better Archeology che usano quelle tabelle (circa 5% nella sabbia del deserto); l'Alakarkinos li trova come prima. Come sono scritte le 5 tabelle: readme `data/minecraft/loot_table/archaeology/` nel datapack.

## Reperti e reliquie fuori dagli scavi

Nelle casse `chests/` la reliquia la mette Relics (10%), nelle 25 casse fuori da quella regola il nostro datapack; in più mimic e mostri con artefatti addosso. Dettagli: scheda `../mod-knowledge/artifacts.md`.

**Buco noto**: le casse delle strutture di Better Archeology usano tabelle `betterarcheology:archeology/chest_…` (21, più 2 `loot_catacombs_*`): né Relics né il nostro datapack le vedono, quindi lì non escono reliquie. Decisione del 24/10: si aggiungono i tesori alla toppa nella versione dell'archeologia.

## Il bottino nella base dati (dalla 0.7.5)

Verificato il 30/10/2026 su inventario (formato 8), datapack e dump del gioco del 30/10. Le tabelle e i modificatori del bottino stanno nella base dati (`scripts/botanypots_db.py`, tabelle `BOTTINO_*`); la forma compatta in cui l'inventario li salva è in `scripts/comune.py`.

**Cosa c'è**: il contenuto di 2.044 tabelle dei jar e di Minecraft (le circa 14.000 dei blocchi, `blocks/`, restano solo come nomi), 309 modificatori, 37 liste globali di NeoForge, più i nostri file. Per ogni tabella: le pool con i tiri, le voci con peso, quantità, probabilità, condizioni e funzioni; le tabelle scritte dentro una voce (34) diventano tabelle a sé (`<tabella>#<pool>.<voce>`). Per ogni modificatore: le tabelle bersaglio, i parametri semplici e i nomi citati (tabelle tirate, oggetti aggiunti).

**Regole scritte nella base**:
- **Chi vince** tra più file con lo stesso nome: il nostro datapack, poi i jar delle mod, poi NeoForge e Minecraft. Tra due mod l'ordine non è noto: 11 tabelle, 10 di Artifacts riscritte da Reliquified Artifacts e una di Apothic Spawners che c'è anche in Apotheosis.
- **Modificatore attivo**: file vincente, caricabile ed elencato in almeno una lista globale (317 dei 319 modificatori).
- **Categoria**, dal tipo e dal nome: casse, scavi, mostri, pesca, «iniezioni» (le tabelle `inject/` tirate dai modificatori), altro. Vasi decorati, distributori, spawner e i proiettili degli spawner di Dungeons and Taverns hanno il tipo `chest` ma non sono casse.
- **Fonti di reliquie**: Relics (nome `<ns>:chests/…`), un nostro modificatore che tira una tabella di Artifacts, una voce con una tabella o un oggetto di Artifacts. Il tipo `artifacts:roll_loot_table` non conta, perché Reliquified Artifacts ne scarta le reliquie (scheda `../mod-knowledge/artifacts.md`).
- **Sottotabelle**: quelle che un'altra tabella nomina come voce. Di solito non si aprono da sole, e i modificatori non le vedono.

**Controlli** (a ogni push): nessuna cassa con due possibilità di reliquia (Relics più la nostra toppa); nessuna lista globale con `replace: true`; le tabelle lette dai file coincidono con quelle caricate dal gioco (blocca solo con un dump aggiornato). Come avviso: le tabelle che riscriviamo noi portate anche da un'altra mod (oggi 0). Come informazione: le casse senza reliquie (query `analisi casse-senza-reliquie`).

**Primi numeri** (30/10, file vincenti):
- casse 669, scavi 48, mostri 507, pesca 15, iniezioni 68, altro 731;
- reliquie: Relics vede 563 casse, la nostra toppa altre 25, e 103 tabelle hanno voci di Artifacts (tra queste le nostre 5 tabelle vanilla degli scavi);
- **confronto con il gioco**: le tabelle che i file danno per caricate coincidono con le 16.813 del dump (blocchi esclusi), quindi lettura e condizioni di caricamento sono giuste. Le condizioni di Bookshelf contano: 286 tabelle di Botany Trees sono per mod assenti;
- **scavi**: oltre a quelle del quadro qui sopra, ci sono 7 tabelle proprie di Dungeons and Taverns (`nova_structures:archaelogy/…`, scritto così), una di When Dungeons Arise (santuario Kisegi) e quella dell'End di Moog's End Structures, che ha il tipo `chest`;
- **65 casse radice senza reliquie**: Better Archeology 21 (il buco noto), Twilight Forest 16 (volute: una sola cassa per struttura, regola della 0.6.0), Towns and Towers 13 (avamposti e villaggi), Moog's End Structures 6, Friends & Foes 3 barili, YUNG's Extras 2, e una ciascuna Dungeons and Taverns, Supplementaries (la cassa del galeone; la cassaforte è coperta), Unusual End e YUNG's Better Dungeons.

## Da analizzare (versione dell'archeologia)

- Le tabelle di scavo di tutte le mod: cosa danno, quanto valgono, doppioni; eventuali miglioramenti (Matteo, 24/10).
- I tesori delle casse di Better Archeology nella toppa delle reliquie.
- Gli scavi senza artefatti (rovine dei sentieri comuni, Jaden's, Cataclysm…): lasciarli così o no.
- Quali tabelle tocca Corail Tombstone.
- **Metodo** (approvato il 24/10): tabelle del bottino nella base dati e file generati, come vasi e mercato: `../lavoro/versioni/v0.7.5.md`, sezione 2.
