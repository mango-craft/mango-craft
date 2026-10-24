# Relics: reliquie nel 10% delle casse (dalla 0.7.0)

Relics mette una reliquia nel **20%** delle casse aperte da un giocatore, solo nelle tabelle `<mod>:chests/…`, scegliendola per nome della cassa, bioma e dimensione (scheda `artifacts`, sezione su Reliquified Artifacts). Per il nostro pack è troppo: conta **ogni** cassa delle strutture grandi, non solo il tesoro finale. Matteo ha scelto il **10%** (24/10/2026, `lavoro/versioni/v0.7.0.md`).

## Come

Il file [`loot_modifiers/relic_loot.json`](loot_modifiers/relic_loot.json) riscrive **allo stesso percorso** il modificatore di Relics (`relics:relic_loot`, già nel suo elenco `global_loot_modifiers.json`): Paxi carica il nostro sopra quello della mod. Rispetto all'originale (`"conditions": []`) ha una condizione in più:

```jsonc
{
  // Solo se Relics è installata: senza Relics il tipo "relics:relic_loot" non esiste.
  "neoforge:conditions": [ { "type": "neoforge:mod_loaded", "modid": "relics" } ],
  "type": "relics:relic_loot",
  // NeoForge controlla queste condizioni PRIMA di far lavorare il modificatore
  // (LootModifier.apply). Metà delle volte si ferma qui: 20% × 0,5 = 10%.
  "conditions": [ { "condition": "minecraft:random_chance", "chance": 0.5 } ]
}
```

- **Cambiare la probabilità**: `chance` = probabilità voluta ÷ 0,2 (0,75 → 15%; 1 → 20%, come la mod).
- **Perché non la config di Relics**: il 20% si cambia solo accendendo la sua «config estesa» (`enabledExtendedConfigs`), segnata come WIP, che crea un file per ogni reliquia e non si aggiorna da sola quando la mod cambia.
- **Dopo ogni aggiornamento di Relics**: controllare che il suo file si chiami ancora `data/relics/loot_modifiers/relic_loot.json` e abbia lo stesso formato.
