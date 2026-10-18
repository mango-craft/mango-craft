# `global_loot_modifiers.json`: l'interruttore dei modificatori

NeoForge legge questo file da ogni datapack e da ogni mod. Solo i modificatori di bottino **nominati qui** vengono attivati. Un file che sta in una cartella `loot_modifiers` ma non compare in nessun elenco resta spento.

## Com'è fatto

I commenti `//` servono solo a spiegare: nel file vero non ci sono, e non si possono mettere.

```jsonc
{
  // false = AGGIUNGI i nostri nomi all'elenco che già esiste (quello di Artifacts e delle altre mod).
  // true  = CANCELLA gli elenchi caricati prima e tieni solo questo: spegnerebbe i modificatori
  //         delle mod, compresi i 37 di Artifacts per le casse vanilla. Non usarlo.
  "replace": false,

  "entries": [
    // Ogni voce è il nome di un file, scritto come "namespace:percorso" senza ".json".
    // "matteo_tweaks:artifacts/abandoned_mineshaft" corrisponde al file
    //   data/matteo_tweaks/loot_modifiers/artifacts/abandoned_mineshaft.json
    "matteo_tweaks:artifacts/abandoned_mineshaft",
    "matteo_tweaks:artifacts/ancient_city"
    // ... uno per ognuno dei 15 file in artifacts/
  ]
}
```

## Regole pratiche

- **Nuovo file in `artifacts/`** (per esempio un livello `buried_treasure.json`): aggiungi qui la riga `"matteo_tweaks:artifacts/buried_treasure"`, altrimenti resta spento.
- **Spegnere un livello**: togli la sua riga. Il file può restare dov'è.
- **Cancellare un file**: togli prima la sua riga. Un nome in elenco senza il suo file dà errore al caricamento.
- **L'ordine** delle righe conta solo se due modificatori toccano la stessa cassa. Qui non succede: ogni cassa compare in un solo livello.

Il funzionamento dei singoli modificatori è spiegato in [`../../matteo_tweaks/loot_modifiers/artifacts/readme.md`](../../matteo_tweaks/loot_modifiers/artifacts/readme.md).
