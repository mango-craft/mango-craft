# Berserker infuocati nelle fortezze di YUNG's

I Berserker infuocati di Cataclysm compaiono solo nelle strutture elencate nell'etichetta `cataclysm:berserker_spawn`, che di serie contiene soltanto `minecraft:fortress`. YUNG's Better Nether Fortresses sostituisce la fortezza vanilla con la sua `betterfortresses:fortress`, quindi nel nostro Nether i Berserker non comparivano mai (B02).

| File | Etichetta | Cosa fa |
|---|---|---|
| `data/cataclysm/tags/worldgen/structure/berserker_spawn.json` | `cataclysm:berserker_spawn` | aggiunge `betterfortresses:fortress` a quelle in cui compaiono |

`"replace": false` aggiunge senza togliere niente (la fortezza vanilla resta nell'elenco). `"required": false` rende la voce facoltativa: se YUNG's non c'è, l'etichetta resta com'è e non ci sono errori (le etichette non hanno le condizioni di caricamento).

Vale solo per le fortezze **generate dopo**: un modificatore di struttura si legge al riavvio del mondo e non cambia quelle già esplorate. Prova: Nether nuovo o non ancora esplorato, `/locate structure betterfortresses:fortress`, entrare e aspettare i Berserker.

Decisione del 19/10/2026 (`1.21.1/lavoro/versioni/v0.6.0.md`); fatti nella scheda `cataclysm`.
