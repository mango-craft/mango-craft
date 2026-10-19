# Lune di sangue più rare (Enhanced Celestials 2)

Dalla 0.5.1 le lune vengono da **Enhanced Celestials 2** (EC2): la mod **Core** fa il calendario e legge i dati, la mod **Default Lunar Events** porta le lune (sangue, raccolto, blu, super). Prima c'era Enhanced Celestials 1, con un formato diverso (storia e confronto: `1.21.1/lavoro/0708-enhanced-celestials-2.md` nel repository).

## Come funziona

In EC2 ogni luna è divisa in file piccoli, tutti dentro `data/enhancedcelestials2defaultlunarevents/enhancedcelestials2core/lunar/`:

- `event/` → la luna e l'elenco dei suoi effetti;
- `event_probability/` → **quanto spesso** compare, dimensione per dimensione;
- `event_modifier/` → **un effetto per file** (moltiplicatore dei mostri, colore del cielo, musica…).

I nostri file hanno **lo stesso percorso e lo stesso nome** di quelli della mod, quindi li **sostituiscono**: Paxi carica il nostro pacchetto sopra la mod e a parità di nome vince il nostro. Tutti gli altri file (le altre lune, gli altri effetti) restano quelli della mod. I file li legge solo EC2: senza la mod restano inerti.

Sono scritti da noi con gli stessi campi di quelli della mod (EC2 è "tutti i diritti riservati": non copiamo i suoi file, solo il formato).

| File | Cosa cambia | Mod | Nostro |
|---|---|---|---|
| `event_probability/blood_moon.json` | Peso della luna di sangue nel calendario | 10 | **5** |
| `event_modifier/blood_moon_spawn_category_multiplier.json` | Mostri durante la luna di sangue | ×2,25 | **×2** |
| `event_modifier/super_blood_moon_spawn_category_multiplier.json` | Mostri durante la super luna di sangue | ×4,5 | **×4** |

## I campi

I commenti `//` servono solo a spiegare: nel file vero non ci sono, e non si possono mettere.

```jsonc
// event_probability/blood_moon.json
{
  "dimensions": {
    "minecraft:overworld": {                     // vale solo nell'Overworld
      "priority": 0,
      "spawn_requirements": {
        "rules": [
          { "type": "enhancedcelestials2core:min_nights_between",
            "settings": { "min_nights": 4 } },   // notti minime tra due lune di sangue
          { "type": "enhancedcelestials2core:valid_moon_phase",
            "settings": { "valid_moon_phases": [0, 1, 2, 3, 4, 5, 6, 7] } }   // tutte le fasi
        ],
        "weight": 5                              // peso nel calendario (mod: 10). Più basso = più rara
      }
    }
  },
  "lunar_event": "enhancedcelestials2defaultlunarevents:blood_moon"   // la luna a cui si riferisce
}

// event_modifier/blood_moon_spawn_category_multiplier.json
{
  "type": "enhancedcelestials2core:spawn_category_multiplier",
  "settings": { "multipliers": { "monster": 2.0 } }   // mostri ×2 (mod: 2.25); 1.0 = come una notte normale
}
```

Il **peso** non è una probabilità: conta rispetto ai pesi delle altre lune (raccolto e blu 10, le super 5) e alle regole del calendario (almeno 3 giorni tra due lune qualsiasi, al massimo 98 senza lune, niente lune con la pioggia). Con la mod originale si contavano circa 5 lune di sangue ogni 100 giorni; l'obiettivo, come prima, è circa 3. Il valore 5 è un punto di partenza da verificare con le previsioni (sotto).

## Effetti della luna di sangue lasciati come nella mod

EC2 aggiunge due effetti che EC1 non aveva, e li lasciamo attivi:
- i mostri compaiono più vicini al giocatore (`blood_moon_mob_spawn_distances`: 64 blocchi; super luna 32);
- **assedio di zombi** ai villaggi (`blood_moon_village_siege_probability`: 50%; super luna 100%).

Per spegnerli basta un file con lo stesso nome in `event_modifier/` (per l'assedio: `"probability": 0.0`).

## Quando ha effetto e come provare

EC2 legge questi file **all'apertura del mondo**: dopo una modifica bisogna uscire e rientrare, `/reload` non basta.

- Il comando delle previsioni lunari mostra le lune dei prossimi giorni: serve a contare le lune di sangue e tarare il peso.
- Il comando che avvia una luna e quello che elenca gli effetti attivi ("dumpmodifiers") servono a controllare che i nostri ×2 e ×4 siano quelli usati.
- EC2 **sostituisce il comando `/time`**: `/time set` porta all'ora indicata del giorno dopo e dice in che giorno del calendario si è (provato in gioco: `/time set 18000` → "Set time to 18000 for the next day. You are now on day 1.").

I comandi di EC2 iniziano con `/ecc` (il tasto Tab completa i nomi); con EC1 erano `/ec lunarForecast` e `/ec setLunarEvent`.
