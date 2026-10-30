# Datapack `matteo_tweaks`

Ritocchi del modpack. **Paxi** carica questo pacchetto in **tutti i mondi**, anche al momento della creazione: non va copiato nella cartella `datapacks` del singolo mondo.

> **Perché ci sono questi README.** I file `.json` dei datapack non accettano commenti: con un `//` dentro il gioco scarta il file. Le spiegazioni stanno quindi in un `readme.md` **per ogni parte**, nella cartella principale di quel lavoro (non in ogni sottocartella; regola del 30/10/2026). Il gioco legge solo i `.json` e ignora tutto il resto.
>
> Dentro `data/` i nomi dei file devono essere **tutti minuscoli**: un `README.md` maiuscolo viene ignorato lo stesso, ma lascia un errore "Invalid path in pack" nel log. Per questo lì si chiamano `readme.md`.

## Cosa contiene

I numeri esatti (quante colture, quante voci) cambiano con le regole: li dicono i generatori e il changelog di ogni versione, non questo file.

| Parte | Cosa fa | Dove | Spiegazione |
|---|---|---|---|
| **Reliquie nelle casse** (dalla 0.7.0) | Relics mette le reliquie nel 10% delle casse `chests/` (invece del 20%) | `data/relics/loot_modifiers/` | [relics/readme.md](data/relics/readme.md) |
| **Artefatti nelle casse che Relics non vede** | Aggiunge gli oggetti di Artifacts a 34 casse fuori da `chests/` (Twilight Forest, YUNG's Better Dungeons, nave dell'End, Galeone, cittadella; dalla 0.7.5 i tesori di Better Archeology) | `data/matteo_tweaks/loot_modifiers/artifacts/` più l'elenco in `data/neoforge/loot_modifiers/` | [artifacts/readme.md](data/matteo_tweaks/loot_modifiers/artifacts/readme.md) e [neoforge/loot_modifiers/readme.md](data/neoforge/loot_modifiers/readme.md) |
| **Artefatti negli scavi** (dalla 0.7.0) | Le 5 tabelle vanilla degli scavi con gli artefatti a 1/16; i 5 modificatori di Artifacts resi innocui | `data/minecraft/loot_table/archaeology/`, `data/artifacts/loot_modifiers/inject/archaeology/` | [artifacts/readme.md](data/artifacts/readme.md) e [archaeology/readme.md](data/minecraft/loot_table/archaeology/readme.md) |
| **Artefatti solo negli slot di Curios** (dalla 0.7.0) | Toglie gli slot di Artifacts dalle etichette di Accessories (Reliquified Artifacts ignora la config di Artifacts) | `data/accessories/tags/item/` | [accessories/readme.md](data/accessories/readme.md) |
| **Berserker nelle fortezze di YUNG's** (dalla 0.6.0) | I Berserker infuocati di Cataclysm compaiono anche nelle fortezze di YUNG's Better Nether Fortresses (B02) | `data/cataclysm/tags/worldgen/structure/` | [cataclysm/readme.md](data/cataclysm/readme.md) |
| **Lista nera degli amuleti di pozione** (dalla 0.7.2) | Le pozioni che non possono diventare amuleti di Apotheosis (effetto continuo, permanente se l'amuleto è infrangibile); generata da `scripts/pozioni_genera.py` dalla regola in `1.21.1/data/pozioni/` | `data/apotheosis/tags/potion/` | [apotheosis/readme.md](data/apotheosis/readme.md) |
| **Funzioni di prova** (dalla 0.7.2) | Danno in un colpo gli oggetti delle prove di uscita di una release e scrivono in chat cosa controllare: `/function matteo_tweaks:test/releases/v0.7.2/…` | `data/matteo_tweaks/function/test/releases/` | [test/readme.md](data/matteo_tweaks/function/test/readme.md) |
| **Vasi di Botany Pots** | Ars Nouveau (Magebloom, Sourceberry, 5 frutti di archwood) a mano; 8 alberi di Bountiful Fares copiati da Botany Trees; colture e terreni delle altre mod, i terreni delle mod con i bonus della nostra scala di rarità (sostituiti allo stesso percorso) e le etichette dei terreni (terra, lava, acqua), generati da `scripts/botanypots_genera.py` dalle regole in `1.21.1/data/vasi/` | `data/matteo_tweaks/recipe/botanypots/`, `data/matteo_tweaks/loot_table/tree_drops/`, `data/botanypots/` | [botanypots/readme.md](data/matteo_tweaks/recipe/botanypots/readme.md) e [data/botanypots/readme.md](data/botanypots/readme.md) |
| **Mercato di Farming for Blockheads** | Vende le piante delle mod che il mercato non conosce, con prezzi alti per origine e rarità, e riscrive i listini della mod con lo stesso criterio; generato da `scripts/mercato_genera.py` dalle regole in `1.21.1/data/mercato/` | `data/matteo_tweaks/recipe/market/`, `data/matteo_tweaks/market_presets/`, `data/<mod>/market_presets/` | [market/readme.md](data/matteo_tweaks/recipe/market/readme.md) |
| **Esperienza Create ↔ Cognition** | La tabella delle unità di Create: Enchantment Industry capisce il cognitium; il Mescolatore converte 50 mB di esperienza di Create ↔ 1000 mB di cognitium | `data/create_enchantment_industry/data_maps/fluid/unit/`, `data/matteo_tweaks/recipe/create/mixing/experience/` | [experience/readme.md](data/matteo_tweaks/recipe/create/mixing/experience/readme.md) e [create_enchantment_industry/readme.md](data/create_enchantment_industry/readme.md) |
| **Lune di sangue** | Più rare (peso 5 invece di 10 nel calendario) e meno affollate (mostri ×2 e ×4), per Enhanced Celestials 2 | `data/enhancedcelestials2defaultlunarevents/enhancedcelestials2core/lunar/` | [lunar/readme.md](data/enhancedcelestials2defaultlunarevents/enhancedcelestials2core/lunar/readme.md) |
| **Pesce cotto di Starcatcher** | Vale come "pesce cotto" nelle ricette di cucina | `data/c/tags/item/foods/`, `data/bountifulfares/tags/item/` | [c/readme.md](data/c/readme.md) |

## Mappa delle cartelle

```
matteo_tweaks/
├── pack.mcmeta                  nome e versione del pacchetto (pack_format 48 = MC 1.21.1)
├── README.md                    questo file
└── data/
    ├── matteo_tweaks/           i nostri file nuovi
    │   ├── function/test/releases/   funzioni di prova, una cartella per release (v0.7.2/…)
    │   ├── loot_modifiers/
    │   │   └── artifacts/       10 modificatori di bottino per le 34 casse che Relics non vede
    │   ├── loot_table/
    │   │   └── tree_drops/      i raccolti degli 8 alberi di Bountiful Fares (copiati da Botany Trees)
    │   ├── market_presets/      i nostri listini del mercato, per origine e classe di rarità (generati)
    │   └── recipe/
    │       ├── botanypots/
    │       │   ├── alberi/      8 alberi di Bountiful Fares nei vasi (copiati da Botany Trees, LGPL-2.1)
    │       │   ├── crop/        7 colture di Ars Nouveau (cosa cresce nel vaso)
    │       │   ├── soil/        5 terreni (i tronchi di archwood)
    │       │   └── <mod>/       colture e terreni delle altre mod, generati dallo script (crop/ e soil/)
    │       ├── market/<mod>/    le voci del mercato, una per pianta (generate)
    │       └── create/mixing/experience/   lo scambio di esperienza nel Mescolatore
    ├── botanypots/
    │   ├── recipe/<mod>/soil/   terreni delle mod sostituiti allo stesso percorso, con i bonus nostri (generati)
    │   └── tags/item/soil/      etichette dei terreni: terra, lava, acqua (generate)
    ├── <mod>/market_presets/    listini del mercato delle mod (e di minecraft) riscritti allo stesso percorso (generati)
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
    ├── cataclysm/
    │   └── tags/worldgen/structure/   strutture dei Berserker infuocati (+ fortezza di YUNG's)
    ├── apotheosis/
    │   └── tags/potion/         lista nera degli amuleti di pozione (generata)
    ├── create_enchantment_industry/
    │   └── data_maps/fluid/unit/   unità del liquido d'esperienza: + cognitium
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
- **`c`**, **`bountifulfares`**, **`accessories`**, **`apotheosis`**, **`cataclysm`** e le etichette di **`botanypots`** contengono etichette (tag): senza `"replace": true` si **aggiungono** a quelle delle mod invece di sostituirle (le etichette di Accessories tolgono voci con `remove`).
- **`create_enchantment_industry`** contiene una mappa di dati: NeoForge la **unisce** a quella della mod con lo stesso percorso.
- **`enhancedcelestials2defaultlunarevents`**, **`relics`**, **`artifacts`**, **`minecraft`**, i terreni in `botanypots/recipe/` e i listini in `<mod>/market_presets/` hanno lo stesso percorso dei file originali (delle mod e del gioco), quindi **li sostituiscono**. Paxi carica il pacchetto "in cima" a tutti gli altri, perciò in caso di file con lo stesso nome vincono le nostre copie.

## Se una mod viene tolta dal pack

Ogni file controlla prima di caricarsi che la sua mod ci sia, oppure lo legge solo la sua mod:

- **Artefatti** e **Relics**: `"neoforge:conditions"` con `mod_loaded` (`artifacts`, `relics`).
- **Vasi** (colture, terreni, alberi e loro raccolti): `"bookshelf:load_conditions"` con `block_exists` sui blocchi usati.
- **Mercato**: ogni voce ha `neoforge:item_exists` sulla pianta. I listini (`market_presets`) li legge solo Farming for Blockheads.
- **Esperienza**: le due ricette del Mescolatore con `mod_loaded` di Create: Enchantment Industry e Cognition; la mappa delle unità con la condizione sul valore.
- **Etichette** (Accessories, lista nera degli amuleti, Berserker, pesce cotto, terreni dei vasi): voci con `"required": false`, che si saltano se il nome non esiste.
- **Lune**: le legge solo Enhanced Celestials 2. Se la mod non c'è, nessuno le apre.
- **Eccezione, funzioni di prova**: i file `.mcfunction` non possono avere condizioni. Se nominano una mod tolta, quella funzione non si carica (errore nel log, nient'altro); `scripts/check_ids.py` ne controlla i nomi.
- **Eccezione, scavi**: le 5 tabelle vanilla in `data/minecraft/loot_table/archaeology/` **non** hanno condizione, perché in NeoForge una tabella con condizione falsa diventa vuota. Senza Artifacts quegli scavi danno niente in 1 caso su 16 (readme della cartella).

Se togli una mod, quindi, i suoi file vengono saltati senza errori (tranne le funzioni di prova che la nominano).

## Quando hanno effetto le modifiche

| Parte | Dopo aver cambiato un file |
|---|---|
| Artefatti, reliquie, scavi, etichette (anche la lista nera degli amuleti), vasi, ricette (voci del mercato, Mescolatore), funzioni di prova | Basta `/reload` in gioco |
| Lune | Bisogna uscire e rientrare nel mondo: Enhanced Celestials 2 le legge solo all'apertura |
| Berserker | Riavvio del mondo, e vale solo per le fortezze **generate dopo** |
| Listini del mercato, mappa delle unità dell'esperienza | Non verificato se basta `/reload`: nel dubbio, uscire e rientrare nel mondo |

Il bottino delle casse si decide la **prima volta che vengono aperte**. Le casse già aperte non cambiano, mentre quelle ancora chiuse, anche in strutture già esplorate, seguono le regole nuove.

## Controlli

- **È caricato?** Con `/datapack list enabled` deve comparire `matteo_tweaks`.
- **Errori?** Cerca `matteo_tweaks` nel file `logs/latest.log` dell'istanza: un JSON scritto male viene segnalato lì, con il nome del file.
- **Il gioco lo carica tutto?** `/mango_dump` e la base dati del repository confrontano i nostri file con quelli caricati dal gioco (`1.21.1/docs/0303-note-tecniche.md`, voce «Dump del gioco»).

## Togliere una parte

- **Un livello di artefatti**: basta togliere la sua riga da `data/neoforge/loot_modifiers/global_loot_modifiers.json`, perché un modificatore che non è in elenco resta spento. Puoi cancellare anche il file, ma **non** cancellare il file lasciando la riga: un nome in elenco senza file dà errore al caricamento.
- **Vasi, mercato, lista nera degli amuleti**: sono generati, quindi si cambia la regola in `1.21.1/data/` e si rilancia lo script; un file cancellato a mano torna al giro dopo.
- **Una coltura o un terreno scritti a mano** (Ars Nouveau, alberi): cancella il suo file.
- **Le lune**: cancella i tre file e tornano i valori originali di Enhanced Celestials 2.
- **Tutto il pacchetto**: togli la cartella `matteo_tweaks` da `config/paxi/datapacks/`.
