# Ars Nouveau nei vasi di Botany Pots

In Botany Pots per la 1.21.1 **colture e terreni sono ricette**: per questo stanno nella cartella `recipe/`. Una ricetta "coltura" dice cosa si pianta, su quale terreno e cosa si raccoglie; una ricetta "terreno" dice quale blocco si può mettere nel vaso come terra.

## Cosa c'è

| Cartella | File | Cosa fa |
|---|---|---|
| `crop/` | `ars_magebloom.json`, `ars_sourceberry.json` | Magebloom e Sourceberry, su terra normale |
| `crop/` | `frostaya_pod.json`, `bombegranate_pod.json`, `bastion_pod.json`, `mendosteen_pod.json`, `flashpine_pod.json` | I frutti di archwood, piantati sul tronco come il cacao |
| `soil/` | `blue_`, `red_`, `purple_`, `green_`, `yellow_archwood_log.json` | Permettono di mettere i tronchi di archwood nel vaso come terreno |

**Gli alberelli di archwood non sono qui**: li supporta già **Botany Trees** (tronchi, foglie con le cesoie, alberello al 5%).

### Perché i frutti stanno sul tronco

In Ars gli alberi cresciuti da un alberello **non fanno frutti**: li hanno solo quelli generati con il mondo. Il frutto si pianta sul tronco del colore giusto, come il cacao sul tronco della giungla, e nei vasi vale la stessa regola:

| Tronco (terreno) | Frutto (coltura) | Mod |
|---|---|---|
| Archwood blu | Frostaya | Ars Nouveau |
| Archwood rosso | Bombegranate | Ars Nouveau |
| Archwood viola | Bastion | Ars Nouveau |
| Archwood verde | Mendosteen | Ars Nouveau |
| Archwood giallo | Flashpine | Ars Elemental |

Nel vaso si mette il tronco come terreno e poi il frutto come seme. Ogni raccolto dà **3 frutti**, come un frutto maturo raccolto a mano.

## Com'è fatta una coltura semplice

I commenti `//` servono solo a spiegare: nel file vero non ci sono, e non si possono mettere.

```jsonc
{
  // SE CARICARE: solo se il blocco esiste, cioè se Ars Nouveau è installata.
  "bookshelf:load_conditions": [
    { "type": "bookshelf:block_exists", "values": ["ars_nouveau:magebloom_crop"] }
  ],

  // "block_derived" = ricava quasi tutto dal blocco della pianta:
  //  - il raccolto è quello che il blocco darebbe se rotto quando è maturo;
  //  - l'aspetto nel vaso sono le sue fasi di crescita.
  "type": "botanypots:block_derived_crop",
  "block": "ars_nouveau:magebloom_crop",

  // L'oggetto da mettere nel vaso come seme.
  "input": { "item": "ars_nouveau:magebloom_crop" }

  // Mancano "soil" e "grow_time", quindi valgono i default:
  // terra normale, e 1200 tick (1 minuto) di crescita prima di terreno e potenziamenti del vaso.
}
```

## Com'è fatto un frutto di archwood

```jsonc
{
  // SE CARICARE: servono sia il frutto sia il tronco.
  // Il Flashpine controlla blocchi "ars_elemental:", gli altri "ars_nouveau:".
  "bookshelf:load_conditions": [
    { "type": "bookshelf:block_exists",
      "values": ["ars_nouveau:frostaya_pod", "ars_nouveau:blue_archwood_log"] }
  ],

  "type": "botanypots:block_derived_crop",
  "block": "ars_nouveau:frostaya_pod",       // il seme è l'oggetto del frutto stesso
                                             // raccolto: quello del frutto maturo (età 2) = 3 frutti

  // SU QUALE TERRENO: qualunque blocco del tag dei tronchi blu di Ars
  // (tronco, legno, e le versioni scortecciate). Nel vaso però si possono mettere
  // solo i blocchi che hanno anche una ricetta "terreno", cioè i tronchi in soil/.
  "soil": { "type": "bookshelf:block_tag", "tag": "ars_nouveau:cascading_logs" },

  // ASPETTO: le 3 fasi di crescita del frutto, ruotate e abbassate
  // per sembrare appese al tronco (stessi valori che Botany Pots usa per il cacao).
  "display": {
    "type": "botanypots:transitional",
    "phases": [
      { "type": "botanypots:simple",
        "block_state": { "block": "ars_nouveau:frostaya_pod", "properties": { "age": "0" } },
        "options": { "rotation": "X_270", "offset": [0, -0.1, 0] } }
      // ... poi età 1 ed età 2, uguali
    ]
  }
}
```

## Com'è fatto un terreno

```jsonc
{
  "bookshelf:load_conditions": [
    { "type": "bookshelf:block_exists", "values": ["ars_nouveau:blue_archwood_log"] }
  ],
  // Il blocco diventa un terreno valido. Senza altri campi: crescita normale, nessun bonus.
  "type": "botanypots:block_derived_soil",
  "block": "ars_nouveau:blue_archwood_log"
}
```

## Aggiungere un'altra pianta

- **Pianta normale**: copia `ars_magebloom.json` in `crop/`, cambia `block`, `input` e la condizione di caricamento.
- **Pianta che vuole un terreno speciale**: aggiungi `"soil"` alla coltura e, se il terreno non è già supportato, una ricetta in `soil/`.
- `/reload` in gioco, poi prova a piantarla.

Per trovare i semi che non hanno ancora una ricetta, Botany Pots ha i comandi `/botanypots debug ...`.

## Nota su Ars Elemental

Ars Elemental contiene già un file per far crescere l'archwood giallo nei vasi, ma è scritto nel formato vecchio di Botany Pots e controlla una mod chiamata `botany_pots` (il nome giusto è `botanypots`). Quindi non si carica mai e non va in conflitto con nulla. L'alberello giallo è coperto da Botany Trees, il Flashpine da questa cartella.
