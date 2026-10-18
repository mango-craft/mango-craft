# Lune di sangue più rare (Enhanced Celestials)

## Come funziona

Enhanced Celestials descrive ogni evento lunare con un file `.json` in `data/enhancedcelestials/enhancedcelestials/lunar/event/`. Questa cartella ha **lo stesso percorso e gli stessi nomi** dei file originali, quindi li **sostituisce**: Paxi carica il nostro pacchetto sopra la mod, e a parità di nome vince il nostro file.

Un datapack sostituisce il file **intero**, non i singoli valori. Per questo i due file sono **copie complete** degli originali di Enhanced Celestials 6.x, con cambiati solo i numeri della tabella qui sotto. Gli altri eventi (luna del raccolto, luna blu…) non sono toccati e restano quelli della mod.

| File | Valore | Originale | Nostro |
|---|---|---|---|
| `blood_moon.json` | Probabilità per notte | 10% | **5%** |
| | Mostri | ×2,25 | **×2** |
| | Notti minime tra due lune di sangue | 4 | 4 |
| `super_blood_moon.json` | Probabilità (solo con la luna piena) | 5% | 5% |
| | Mostri | ×4,5 | **×4** |
| | Notti minime tra due super lune | 20 | 20 |

## I campi che contano

I commenti `//` servono solo a spiegare: nel file vero non ci sono, e non si possono mettere. Il resto del file (colori, dimensione della luna, musica, messaggi in chat, effetti sui mob) è identico all'originale.

```jsonc
{
  "dimension_chances": {
    "minecraft:overworld": {                      // vale solo nell'Overworld
      "chance": 0.05,                             // probabilità per notte: 0.05 = 5% (originale 0.1)
      "min_number_of_nights_between": 4,          // notti minime tra due eventi uguali
      "valid_moon_phases": [0, 1, 2, 3, 4, 5, 6, 7]   // fasi lunari valide: 0 = piena, 4 = nuova.
                                                       // La super luna ha solo [0]: mai se non è piena
    }
  },
  "mob_settings": {
    "blocks_sleeping": { "type": "corgilib:any" },    // durante l'evento non si può dormire
    "spawn_category_multiplier": {
      "monster": 2.0                              // quanti mostri in più: ×2 (originale 2.25)
    }
    // ... qui ci sono anche i mob extra e gli effetti, lasciati come nell'originale
  }
  // ... colori del cielo, dimensione della luna, musica, messaggi: come nell'originale
}
```

## Ritoccare

- **Più rare o più frequenti**: cambia `chance`. Per esempio `0.03` vale 3%.
- **Più o meno mostri**: cambia `monster` in `spawn_category_multiplier`. Con `1.0` il numero di mostri resta quello di una notte normale.
- **Togliere del tutto la luna di sangue**: metti `"chance": 0`.
- **Toccare un altro evento** (luna del raccolto, luna blu): copia qui il file originale dal `.jar` di Enhanced Celestials, sempre dal percorso `data/enhancedcelestials/enhancedcelestials/lunar/event/`, e modificalo.

## Quando ha effetto e come provare

Enhanced Celestials legge questi file **solo all'apertura del mondo**: dopo una modifica bisogna uscire e rientrare, perché `/reload` non basta.

- `/ec lunarForecast` mostra i prossimi eventi lunari.
- `/ec setLunarEvent enhancedcelestials:blood_moon` fa partire subito una luna di sangue. Funziona solo a cielo sereno e richiede i trucchi attivi.
