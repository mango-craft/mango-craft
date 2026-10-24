# Datapack `matteo_tweaks`

Ritocchi del modpack. **Paxi** carica questo pacchetto in **tutti i mondi**, anche al momento della creazione: non va copiato nella cartella `datapacks` del singolo mondo.

> **Perché ci sono questi README.** I file `.json` dei datapack non accettano commenti: con un `//` dentro il gioco scarta il file. Le spiegazioni stanno quindi in un `readme.md` in ogni cartella. Il gioco legge solo i `.json` e ignora tutto il resto.
>
> Dentro `data/` i nomi dei file devono essere **tutti minuscoli**: un `README.md` maiuscolo viene ignorato lo stesso, ma lascia un errore "Invalid path in pack" nel log. Per questo lì si chiamano `readme.md`.

## Cosa contiene

| Parte | Cosa fa | Dove | Spiegazione |
|---|---|---|---|
| **Reliquie nelle casse** (dalla 0.7.0) | Relics mette le reliquie nel 10% delle casse `chests/` (invece del 20%) | `data/relics/loot_modifiers/` | [relics/readme.md](data/relics/readme.md) |
| **Artefatti nelle casse che Relics non vede** | Aggiunge gli oggetti di Artifacts a 25 casse fuori da `chests/` (Twilight Forest, YUNG's Better Dungeons, nave dell'End, Galeone, cittadella) | `data/matteo_tweaks/loot_modifiers/artifacts/` più l'elenco in `data/neoforge/loot_modifiers/` | [artifacts/readme.md](data/matteo_tweaks/loot_modifiers/artifacts/readme.md) e [neoforge/loot_modifiers/readme.md](data/neoforge/loot_modifiers/readme.md) |
| **Artefatti negli scavi** (dalla 0.7.0) | Le 5 tabelle vanilla degli scavi con gli artefatti a 1/16; i 5 modificatori di Artifacts resi innocui | `data/minecraft/loot_table/archaeology/`, `data/artifacts/loot_modifiers/inject/archaeology/` | [artifacts/readme.md](data/artifacts/readme.md) e [archaeology/readme.md](data/minecraft/loot_table/archaeology/readme.md) |
| **Artefatti solo negli slot di Curios** (dalla 0.7.0) | Toglie gli slot di Artifacts dalle etichette di Accessories (Reliquified Artifacts ignora la config di Artifacts) | `data/accessories/tags/item/` | [accessories/readme.md](data/accessories/readme.md) |
| **Vasi di Botany Pots** | Ars Nouveau (Magebloom, Sourceberry, 5 frutti di archwood) a mano; 8 alberi di Bountiful Fares copiati da Botany Trees; le piante e i terreni delle altre mod (247 colture, 18 terreni) generati da `scripts/botanypots_genera.py` dalle regole in `1.21.1/data/vasi/` | `data/matteo_tweaks/recipe/botanypots/`, `data/botanypots/tags/item/soil/` | [botanypots/readme.md](data/matteo_tweaks/recipe/botanypots/readme.md) |
| **Mercato di Farming for Blockheads** | Vende le piante delle mod che il mercato non conosce (438 voci) con prezzi alti per origine e rarità, e riscrive i listini della mod con lo stesso criterio; generato da `scripts/mercato_genera.py` dalle regole in `1.21.1/data/mercato/` | `data/matteo_tweaks/recipe/market/`, `data/matteo_tweaks/market_presets/`, `data/<mod>/market_presets/` | [market/readme.md](data/matteo_tweaks/recipe/market/readme.md) |
| **Esperienza Create ↔ Cognition** | La tabella delle unità di Create: Enchantment Industry capisce il cognitium; il Mescolatore converte 50 mB di esperienza di Create ↔ 1000 mB di cognitium | `data/create_enchantment_industry/data_maps/fluid/unit/`, `data/matteo_tweaks/recipe/create/mixing/experience/` | [experience/readme.md](data/matteo_tweaks/recipe/create/mixing/experience/readme.md) |
| **Lune di sangue** | Più rare (peso 5 invece di 10 nel calendario) e meno affollate (mostri ×2 e ×4), per Enhanced Celestials 2 | `data/enhancedcelestials2defaultlunarevents/enhancedcelestials2core/lunar/` | [lunar/readme.md](data/enhancedcelestials2defaultlunarevents/enhancedcelestials2core/lunar/readme.md) |
| **Pesce cotto di Starcatcher** | Vale come "pesce cotto" nelle ricette di cucina | `data/c/tags/item/foods/`, `data/bountifulfares/tags/item/` | [c/readme.md](data/c/readme.md) |

## Mappa delle cartelle

```
matteo_tweaks/
├── pack.mcmeta                  nome e versione del pacchetto (pack_format 48 = MC 1.21.1)
├── README.md                    questo file
└── data/
    ├── matteo_tweaks/           i nostri file nuovi
    │   ├── loot_modifiers/
    │   │   └── artifacts/       10 modificatori di bottino per le 25 casse che Relics non vede
    │   ├── loot_table/
    │   │   └── tree_drops/      i raccolti degli 8 alberi di Bountiful Fares (copiati da Botany Trees)
    │   └── recipe/
    │       └── botanypots/
    │           ├── alberi/      8 alberi di Bountiful Fares nei vasi (copiati da Botany Trees, LGPL-2.1)
    │           ├── crop/        7 colture di Ars Nouveau (cosa cresce nel vaso)
    │           ├── soil/        5 terreni (i tronchi di archwood)
    │           └── <mod>/       colture e terreni delle altre mod, generati dallo script (crop/ e soil/)
    ├── botanypots/
    │   └── tags/item/soil/      i terreni di terra delle altre mod (generato)
    ├── neoforge/
    │   └── loot_modifiers/      l'elenco dei modificatori da attivare
    ├── relics/
    │   └── loot_modifiers/      relic_loot.json riscritto: reliquie nel 10% delle casse
    ├── artifacts/
    │   └── loot_modifiers/inject/archaeology/   i 5 modificatori degli scavi di Artifacts, resi innocui
    ├── minecraft/
    │   ├── loot_table/archaeology/   5 tabelle vanilla degli scavi con gli artefatti (senza condizione: vedi il readme)
    │   └── market_presets/      listini del mercato per semi e alberelli vanilla (generati)
    ├── accessories/
    │   └── tags/item/           etichette degli slot di Accessories senza gli artefatti
    ├── enhancedcelestials2defaultlunarevents/
    │   └── enhancedcelestials2core/
    │       └── lunar/
    │           ├── event_probability/   frequenza della luna di sangue
    │           └── event_modifier/      mostri della luna e della super luna di sangue
    ├── c/
    │   └── tags/item/foods/     etichette comuni del pesce cotto (+ Starcatcher)
    └── bountifulfares/
        └── tags/item/           etichetta del pesce cotto di Bountiful Fares (+ Starcatcher)
```

## Le cartelle dentro `data/`

La prima cartella dentro `data/` si chiama **namespace** e dice a chi appartiene il file. Un percorso come `data/matteo_tweaks/recipe/botanypots/crop/frostaya_pod.json` diventa, per il gioco, l'identificativo `matteo_tweaks:botanypots/crop/frostaya_pod`.

- **`matteo_tweaks`** contiene i file nuovi. Il nome è inventato e serve solo a non scontrarsi con i file delle mod.
- **`neoforge`** contiene un file che NeoForge cerca proprio in quel punto: l'elenco dei modificatori di bottino.
- **`c`** e **`bountifulfares`** contengono etichette (tag): con `"replace": false` si **aggiungono** a quelle delle mod invece di sostituirle.
- **`enhancedcelestials2defaultlunarevents`**, **`relics`**, **`artifacts`** e **`minecraft`** hanno lo stesso percorso dei file originali (di Enhanced Celestials 2, Relics, Artifacts e del gioco), quindi **li sostituiscono**. Paxi carica il pacchetto "in cima" a tutti gli altri, perciò in caso di file con lo stesso nome vincono le nostre copie.

## Se una mod viene tolta dal pack

Ogni file controlla prima di caricarsi che la sua mod ci sia:

- **Artefatti**: `"neoforge:conditions"` con `mod_loaded` su `artifacts`; **Relics**: su `relics`; etichette di Accessories: voci con `"required": false`.
- **Eccezione, scavi**: le 5 tabelle vanilla in `data/minecraft/loot_table/archaeology/` **non** hanno condizione, perché in NeoForge una tabella con condizione falsa diventa vuota. Senza Artifacts quegli scavi danno niente in 1 caso su 16 (readme della cartella).
- **Vasi**: `"bookshelf:load_conditions"` con `block_exists` sui blocchi usati.
- **Lune**: le legge solo Enhanced Celestials 2. Se la mod non c'è, nessuno le apre.

Se togli una mod, quindi, i suoi file vengono saltati senza errori.

## Quando hanno effetto le modifiche

| Parte | Dopo aver cambiato un file |
|---|---|
| Artefatti, reliquie, scavi, etichette e vasi | Basta `/reload` in gioco |
| Lune | Bisogna uscire e rientrare nel mondo: Enhanced Celestials 2 le legge solo all'apertura |

Il bottino delle casse si decide la **prima volta che vengono aperte**. Le casse già aperte non cambiano, mentre quelle ancora chiuse, anche in strutture già esplorate, seguono le regole nuove.

## Controlli

- **È caricato?** Con `/datapack list enabled` deve comparire `matteo_tweaks`.
- **Errori?** Cerca `matteo_tweaks` nel file `logs/latest.log` dell'istanza: un JSON scritto male viene segnalato lì, con il nome del file.

## Togliere una parte

- **Un livello di artefatti**: basta togliere la sua riga da `data/neoforge/loot_modifiers/global_loot_modifiers.json`, perché un modificatore che non è in elenco resta spento. Puoi cancellare anche il file, ma **non** cancellare il file lasciando la riga: un nome in elenco senza file dà errore al caricamento.
- **Una coltura o un terreno nei vasi**: cancella il suo file.
- **Le lune**: cancella i tre file e tornano i valori originali di Enhanced Celestials 2.
- **Tutto il pacchetto**: togli la cartella `matteo_tweaks` da `config/paxi/datapacks/`.
