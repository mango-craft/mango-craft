# Etichette dei terreni e file sostituiti (Botany Pots)

Tutto quello che c'è in questa cartella è **generato** da `scripts/botanypots_genera.py` (0.6.1): non si modifica a mano, si cambia la regola in `1.21.1/data/vasi/` e si rilancia lo script. Il nome della cartella è quello della mod di cui si estendono o sostituiscono i file (Botany Pots).

## `recipe/<mod>/soil/`: terreni delle mod sostituiti

Sono file di terreno che Botany Pots porta per il gioco base e per alcune mod (`minecraft`, `farmersdelight`, `farmingforblockheads`, `cataclysm`, `twilightforest`, `undergarden`) e che il nostro datapack **sostituisce**: stesso percorso, quindi stesso id, e Paxi carica il datapack sopra alle mod. Lo script li scrive quando la classe di rarità di un terreno (`1.21.1/data/vasi/terreno_rarita.csv`) dà un bonus diverso da quello del file originale; il contenuto è il file della mod con i bonus nuovi. I terreni che non sono blocchi (i secchi con i pesci) prendono la grafica da `terreno_custom.csv`: senza, il terreno sparirebbe (B37).

## `tags/item/soil/`: etichette dei terreni

Aggiungono i terreni delle altre mod alle etichette di Botany Pots, dalla regola `1.21.1/data/vasi/terreno_tag_custom.csv`. Le colture accettano come terreno qualunque oggetto dell'etichetta che chiedono:

| File | Etichetta | Cosa aggiunge |
|---|---|---|
| `dirt.json` | `botanypots:soil/dirt` | le terre delle mod: terra ricca di Twilight's Flavor & Delight, terra risorgente di My Nether's Delight, terra infusa di Hexalia, terra fertilizzata di Farm & Charm, terre dell'Aether e di Deep Aether, terra erbosa di Bountiful Fares… La maggior parte delle colture è "di terra" |
| `lava.json` | `botanypots:soil/lava` | i secchi con i pesci di lava di Nether Depths Upgrade (ci crescono le alghe di lava della stessa mod) |
| `water.json` | `botanypots:soil/water` | i secchi di legno dell'Aether (acqua e pesci) e i secchi con i pesci di Deep Aether |

Le voci sono `"required": false`: se una mod manca, la voce si ignora e non c'è nessun errore.
