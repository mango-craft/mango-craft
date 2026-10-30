# Enhanced Celestials 2 (Core, Default Lunar Events, Shader Support)

Aggiornata il 30/10/2026 · slug dei metafile: `enhanced-celestials-2-core`, `enhanced-celestials-2-default-lunar-events`, `enhanced-celestials-2-shader-support` · nel pack dalla 0.5.1 (Core + Default Lunar Events) e 0.5.2 (Shader Support); ruolo e licenza in `../docs/0301-mod.md`, versioni in `../docs/0403-distinta-mod.md` · fonti: i .jar letti con il workflow Esamina mod (il sorgente di EC2 non è pubblico), sorgente di Enhanced Celestials 1, testi dell'editor dell'autore, log dell'istanza di prova. Materiale grezzo: `../../ai-agents/archivio/2026-10-18_1.21.1-v0.5.1_enhanced-celestials-2/`. Ricerca: `../lavoro/versioni/v0.5.1.md`.

## Le mod

- **Core** (id `enhancedcelestials2core`): il motore: calendario delle lune, formato dei dati, comandi. Nessuna luna. Richiede CorgiLib ≥ 5.0.0.9 e **Data Anchor ≥ 2.0.0.16** (nel pack 2.0.0.17 dalla 0.5.1). Incompatibile con Enhanced Celestials 1.
- **Default Lunar Events** (`enhancedcelestials2defaultlunarevents`): le 7 lune classiche (sangue, raccolto, blu, super e le tre super). Richiede Core e CorgiLib.
- **Shader Support** (`enhancedcelestials2shaders`, nel log "Enhanced Celestials Shader Support v2.1.0"): con uno shader attivo colora cielo, luna e bagliore. Richiede Core ≥ 2.0.3.1, CorgiLib, Sodium e Iris. Dai testi del codice controlla con l'API di Iris se c'è un pacchetto attivo (`isShaderPackInUse`) e colora lo schermo sopra la scena: **funziona con qualsiasi pacchetto di shader**, non serve supporto dal pacchetto.
- Enhanced Celestials 1 (6.0.2.6) mostrava a ogni ingresso nel mondo una schermata che annuncia EC2 (`EC2AnnouncementTrigger`, verificato nel sorgente) e non riceve più commit dal 6/8/2026. Data Anchor serve solo a Enhanced Celestials.

## Formato dei dati

Ogni luna è divisa in file piccoli in `data/<namespace>/enhancedcelestials2core/lunar/`:
- `event/`: la luna e l'elenco dei suoi effetti;
- `event_probability/`: quanto spesso compare, dimensione per dimensione: `priority`, `spawn_requirements` con `rules` (`min_nights_between`, `valid_moon_phase`) e `weight` (10 le lune normali, 5 le super);
- `event_modifier/`: **un effetto per file** (es. `spawn_category_multiplier`, `mob_spawn_distances`, `village_siege_probability`, colori, musica…);
- `dimension_settings/`: almeno 3 giorni tra due lune, al massimo 98 senza lune, anno di 100 giorni, niente lune con la pioggia.

Il **peso** non è una probabilità: conta rispetto ai pesi delle altre lune e alle regole del calendario. Come i pesi diventano frequenza non si può leggere (codice chiuso): si verifica in gioco con `/ec lunarForecast`. Con EC1 (codice pubblico, probabilità 10%/5%) una simulazione dello stesso algoritmo dava circa 5 lune di sangue ogni 100 giorni con i valori della mod e circa 3 con il nostro 5%.

Le lune si leggono **all'apertura del mondo**: `/reload` non basta.

## Le lune (Default Lunar Events)

Stesse lune e stessi valori di EC1 (sangue: mostri ×2,25, comparsa in superficie, niente letto; raccolto: colture ×2; blu: fortuna, esperienza ×2, incantamenti e incudine meno cari, beacon più ampio; super luna: slime ovunque; le super ×4,5 / ×4 solo con la luna piena; bottino in più in 16 tabelle vanilla con la luna blu). In più, solo in EC2, per la luna di sangue: mostri che compaiono entro **64 blocchi** dal giocatore (super luna 32) e **assedio di zombi ai villaggi** con probabilità 50% (super luna 100%).

## Il nostro datapack

Tre file in `config/paxi/datapacks/matteo_tweaks/data/enhancedcelestials2defaultlunarevents/enhancedcelestials2core/lunar/` con lo stesso percorso di quelli della mod (quindi li sostituiscono): luna di sangue peso **5** invece di 10, mostri **×2** invece di ×2,25, super luna **×4** invece di ×4,5. Scritti da noi con il formato della mod (EC2 è "tutti i diritti riservati": non si copiano i suoi file). Gli effetti nuovi (mostri più vicini, assedio) restano attivi: decisione aperta in `../lavoro/0503-temi-aperti.md`, sezione 4. Documentazione completa nel readme della cartella.

## Comandi

- `/ec lunarForecast`: le lune dei prossimi giorni (per contare le lune di sangue: obiettivo circa 3 ogni 100 giorni).
- `/ec setLunarEvent enhancedcelestials2defaultlunarevents:blood_moon`: avvia una luna, solo con il cielo sereno e di notte. Provato in gioco il 19/10 ("The Blood Moon rises…").
- `/ec dumpModifiers <luna>`: elenca gli effetti attivi (devono comparire i nostri ×2 e ×4).
- `/ec scheduleEvent`: programma una luna fra N giorni.
- `/ecc …`: comandi del **client** per le impostazioni (`/ecc translate config`, `/ecc translate contribute`, `/ecc config`).
- EC2 **sostituisce `/time`**: `/time set` porta all'ora indicata del giorno dopo e dice in che giorno del calendario si è (provato: "Set time to 18000 for the next day. You are now on day 1.").

## Config

- `config/enhancedcelestials2core/translations.json` (Gson; nomi dei campi letti dal codice): `Translation_Mode` (`AUTOMATIC` di serie, `MANUAL`, `DISABLED`), `Prompt_Language_When_Translation_Incomplete`, `override_existing_translations`. Con `AUTOMATIC` scarica e applica da sola le traduzioni della comunità da `translations.corgitaco.dev`; senza il file scrive in chat a ogni ingresso nel mondo "translation settings not yet configured" (B32). Nel pack dalla 0.5.2: `DISABLED`, `false`, `false` (`../docs/0302-config.md`). Lingue nel jar: en, fr, ja, ru, uk, zh (niente italiano).
- `config/enhancedcelestials2core/mixins.properties` (opzioni dei mixin); il Core sostituisce il comando `/time` con un mixin (`TimeCommandMixin`).
- `config/enhancedcelestials2core/<addon>-prompt.json`: la sua sola presenza spegne l'avviso "addon mancante" (per Default Lunar Events e Shader Support; non serve, le abbiamo).
- Il Core ha un editor sperimentale (`/ecc config`) che **non** è per i modpack.

## Problemi

B32 (messaggio sulle traduzioni) risolto nella 0.5.2. Sound Physics segnala tre suoni di EC1 non più esistenti nella sua config di serie (innocuo, B14).

## Storia nel pack

0.1.1 Enhanced Celestials 1 con il datapack delle lune; 0.5.1 passaggio a EC2 e datapack riscritto (`../lavoro/versioni/v0.5.1.md`); 0.5.2 Shader Support e config delle traduzioni (`v0.5.2.md`).
