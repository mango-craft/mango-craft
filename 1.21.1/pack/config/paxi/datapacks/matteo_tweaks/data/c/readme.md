# Pesce cotto di Starcatcher nelle etichette

Starcatcher cuoce tutti i suoi pesci in un unico `starcatcher:cooked_starcaught_fish`, che di suo non è in nessuna etichetta di pesce cotto: le ricette che chiedono "pesce cotto qualsiasi" non lo accettano. Questi file lo aggiungono:

| File | Etichetta | Chi la usa |
|---|---|---|
| `data/c/tags/item/foods/cooked_fish.json` | `c:foods/cooked_fish` | etichetta comune di NeoForge (ricette di Cultural Delights, Farm & Charm tramite `farm_and_charm:cooked_fishes`…) |
| `data/c/tags/item/foods/cooked_fishes.json` | `c:foods/cooked_fishes` | variante usata da alcune mod (definita da Forgified Fabric API) |
| `data/bountifulfares/tags/item/cooked_fishes.json` | `bountifulfares:cooked_fishes` | zuppa di pesce di Bountiful Fares |

`"replace": false` aggiunge senza togliere niente. `"required": false` rende la voce facoltativa: se Starcatcher non c'è, l'etichetta resta com'è e non ci sono errori (le etichette non hanno le condizioni di caricamento).

Decisione del 18/10/2026. Prova: `/give @s starcatcher:cooked_starcaught_fish`, poi in EMI cercare le ricette che lo usano.
