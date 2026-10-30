# Tema: archeologia e reperti

Aggiornata il 24/10/2026 · stato: **quadro iniziale**; gestione delle tabelle di scavo e casse di Better Archeology da fare in una versione dedicata, prima della progressione (decisione di Matteo del 24/10, `../lavoro/0503-temi-aperti.md`) · mod coinvolte: Better Archeology, Jaden's Nether Expansion, L_Ender's Cataclysm, Moog's End Structures, YUNG's Better Jungle Temples, YUNG's Better Desert Temples, YUNG's Extras, Lithostitched, Towns and Towers, Dungeons and Taverns, Supplementaries, Ars Nouveau, Corail Tombstone, Artifacts con Relics e Reliquified Artifacts · fonti: inventario del pack (24/10); scansione dei 253 jar dell'istanza di prova e sorgenti di Artifacts, Ars Nouveau e NeoForge (grezzo: `../../ai-agents/archivio/2026-10-24_1.21.1-v0.7.0_relics-bottino/scavi-risultati.md`); dati vanilla 1.21.1 (`misode/mcmeta`). Schede vicine: `../mod-knowledge/artifacts.md` (reliquie, bottino di Relics), `accessori.md`.

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

## Da analizzare (versione dell'archeologia)

- Le tabelle di scavo di tutte le mod: cosa danno, quanto valgono, doppioni; eventuali miglioramenti (Matteo, 24/10).
- I tesori delle casse di Better Archeology nella toppa delle reliquie.
- Gli scavi senza artefatti (rovine dei sentieri comuni, Jaden's, Cataclysm…): lasciarli così o no.
- Quali tabelle tocca Corail Tombstone.
- **Metodo** (approvato il 24/10): tabelle del bottino nella base dati e file generati, come vasi e mercato: `../lavoro/versioni/v0.7.4.md`, sezione 2.
