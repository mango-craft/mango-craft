# Datapack `matteo_tweaks`

Ritocchi del modpack. **Paxi** carica questo pacchetto in **tutti i mondi**, anche al momento della creazione: non va copiato nella cartella `datapacks` del singolo mondo.

> **Perché ci sono questi README.** I file `.json` dei datapack non accettano commenti: con un `//` dentro il gioco scarta il file. Le spiegazioni stanno quindi in un `readme.md` in ogni cartella. Il gioco legge solo i `.json` e ignora tutto il resto.
>
> Dentro `data/` i nomi dei file devono essere **tutti minuscoli**: un `README.md` maiuscolo viene ignorato lo stesso, ma lascia un errore "Invalid path in pack" nel log. Per questo lì si chiamano `readme.md`.

## Cosa contiene

| Parte | Cosa fa | Dove | Spiegazione |
|---|---|---|---|
| **Artefatti nelle strutture modded** | Aggiunge gli oggetti di Artifacts a 153 casse di strutture modded | `data/matteo_tweaks/loot_modifiers/artifacts/` più l'elenco in `data/neoforge/loot_modifiers/` | [artifacts/readme.md](data/matteo_tweaks/loot_modifiers/artifacts/readme.md) e [neoforge/loot_modifiers/readme.md](data/neoforge/loot_modifiers/readme.md) |
| **Ars Nouveau nei vasi** | Magebloom, Sourceberry e i 5 frutti di archwood in Botany Pots | `data/matteo_tweaks/recipe/botanypots/` | [botanypots/readme.md](data/matteo_tweaks/recipe/botanypots/readme.md) |
| **Lune di sangue** | Più rare (5% delle notti) e meno affollate (mostri ×2 e ×4) | `data/enhancedcelestials/enhancedcelestials/lunar/event/` | [lunar/event/readme.md](data/enhancedcelestials/enhancedcelestials/lunar/event/readme.md) |

## Mappa delle cartelle

```
matteo_tweaks/
├── pack.mcmeta                  nome e versione del pacchetto (pack_format 48 = MC 1.21.1)
├── README.md                    questo file
└── data/
    ├── matteo_tweaks/           i nostri file nuovi
    │   ├── loot_modifiers/
    │   │   └── artifacts/       15 modificatori di bottino, uno per livello di rarità
    │   └── recipe/
    │       └── botanypots/
    │           ├── crop/        7 colture (cosa cresce nel vaso)
    │           └── soil/        5 terreni (i tronchi di archwood)
    ├── neoforge/
    │   └── loot_modifiers/      l'elenco dei modificatori da attivare
    └── enhancedcelestials/
        └── enhancedcelestials/
            └── lunar/
                └── event/       2 file che sostituiscono quelli di Enhanced Celestials
```

## Le tre cartelle dentro `data/`

La prima cartella dentro `data/` si chiama **namespace** e dice a chi appartiene il file. Un percorso come `data/matteo_tweaks/recipe/botanypots/crop/frostaya_pod.json` diventa, per il gioco, l'identificativo `matteo_tweaks:botanypots/crop/frostaya_pod`.

- **`matteo_tweaks`** contiene i file nuovi. Il nome è inventato e serve solo a non scontrarsi con i file delle mod.
- **`neoforge`** contiene un file che NeoForge cerca proprio in quel punto: l'elenco dei modificatori di bottino.
- **`enhancedcelestials`** ha lo stesso percorso dei file originali della mod, quindi **li sostituisce**. Paxi carica il pacchetto "in cima" a tutti gli altri, perciò in caso di file con lo stesso nome vincono le nostre copie.

## Se una mod viene tolta dal pack

Ogni file controlla prima di caricarsi che la sua mod ci sia:

- **Artefatti**: `"neoforge:conditions"` con `mod_loaded` su `artifacts`.
- **Vasi**: `"bookshelf:load_conditions"` con `block_exists` sui blocchi usati.
- **Lune**: le legge solo Enhanced Celestials. Se la mod non c'è, nessuno le apre.

Se togli una mod, quindi, i suoi file vengono saltati senza errori.

## Quando hanno effetto le modifiche

| Parte | Dopo aver cambiato un file |
|---|---|
| Artefatti e vasi | Basta `/reload` in gioco |
| Lune | Bisogna uscire e rientrare nel mondo: Enhanced Celestials le legge solo all'apertura |

Il bottino delle casse si decide la **prima volta che vengono aperte**. Le casse già aperte non cambiano, mentre quelle ancora chiuse, anche in strutture già esplorate, seguono le regole nuove.

## Controlli

- **È caricato?** Con `/datapack list enabled` deve comparire `matteo_tweaks`.
- **Errori?** Cerca `matteo_tweaks` nel file `logs/latest.log` dell'istanza: un JSON scritto male viene segnalato lì, con il nome del file.

## Togliere una parte

- **Un livello di artefatti**: basta togliere la sua riga da `data/neoforge/loot_modifiers/global_loot_modifiers.json`, perché un modificatore che non è in elenco resta spento. Puoi cancellare anche il file, ma **non** cancellare il file lasciando la riga: un nome in elenco senza file dà errore al caricamento.
- **Una coltura o un terreno nei vasi**: cancella il suo file.
- **Le lune**: cancella i due file e tornano i valori originali di Enhanced Celestials.
- **Tutto il pacchetto**: togli la cartella `matteo_tweaks` da `config/paxi/datapacks/`.
