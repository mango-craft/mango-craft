# Tabelle vanilla degli scavi, con gli artefatti (dalla 0.7.0)

Le 5 tabelle degli scavi in cui Artifacts metteva un artefatto (perché e come: [`../../../artifacts/readme.md`](../../../artifacts/readme.md)). Sono le tabelle **vanilla della 1.21.1**, copiate dai dati ufficiali del gioco (`misode/mcmeta`, tag `1.21.1-data-json`), con **una voce in più**:

```jsonc
{ "type": "minecraft:loot_table", "value": "artifacts:inject/archaeology/desert_pyramid", "weight": 8 }
```

**I pesi**: ogni voce vanilla ha il peso moltiplicato per 15, la voce nuova ha come peso la somma dei pesi vanilla. Così l'artefatto esce esattamente in 1 scavo su 16, come faceva Artifacts, e gli oggetti vanilla mantengono le loro proporzioni.

| Tabella | Somma dei pesi vanilla | Peso della voce degli artefatti | Su |
|---|---|---|---|
| `desert_pyramid` | 8 | 8 | 128 |
| `desert_well` | 8 | 8 | 128 |
| `ocean_ruin_cold` | 15 | 15 | 240 |
| `ocean_ruin_warm` | 15 | 15 | 240 |
| `trail_ruins_rare` | 12 | 12 | 192 |

## Eccezione alla regola delle condizioni di caricamento

Questi 5 file **non hanno** `neoforge:conditions`: in NeoForge una tabella con una condizione falsa diventa **vuota** (non torna quella vanilla), quindi una condizione su Artifacts svuoterebbe gli scavi vanilla senza Artifacts. Senza Artifacts, invece, la voce in più punta a una tabella che non esiste e in quel caso su 16 lo scavo non dà niente: nessun errore grave.

## Chi altro usa queste tabelle (verificato il 24/10/2026 sui 253 jar)

- **Come tabella principale** (comportamento uguale a prima): strutture vanilla, Dungeons and Taverns (rovine del deserto), YUNG's Better Desert Temples, pozzi del deserto di YUNG's Extras e Lithostitched, Towns and Towers, il granchio **Alakarkinos** di Ars Nouveau (tira queste tabelle in automatico, circa una volta al minuto).
- **Come sotto-tabella** (da qui in poi anche lì escono artefatti): 5 tabelle di **Better Archeology** (sabbia del deserto, sabbia rossa, ghiaia delle pianure, sabbia sott'acqua, terra della taiga). Approvato da Matteo il 24/10.
- **Corail Tombstone** aggiunge una sua pool a queste tabelle quando si caricano: lo fa anche sulle nostre.
- Nessun'altra mod ha una copia di queste tabelle. Se una mod nuova ne portasse una, la nostra vince (Paxi): va controllato.
