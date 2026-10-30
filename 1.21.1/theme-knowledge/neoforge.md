# NeoForge (piattaforma)

Aggiornata il 30/10/2026 · nel pack: NeoForge **21.1.259** (la versione usata è nel changelog di ogni versione, `../docs/0401-changelog.md`) · fonti: sorgenti di NeoForge e FancyModLoader (ramo `1.21.1`), owo-lib, API di Modrinth (30/10), log dell'istanza di prova.

## Cose da non rompere

- **Fermo a 21.1.259**: dalla 21.1.261 NeoForge ha cambiato il codice di rete e owo-lib 0.12.15.5 non "spacchetta" più i suoi pacchetti → "Connection lost" appena si entra nel mondo (bug B17, aggirato). owo-lib è un metafile a sé (`owo-lib.pw.toml`), dipendenza obbligatoria dell'Aether su Modrinth: **non** è incorporata nell'Aether. La correzione è uscita il 16/10/2026: owo-lib **0.12.15.6-beta.1** per NeoForge 1.21.1 (`wbdHEItB`, beta; changelog: «Resolve issue with latest neoforge update due to changes to internal network code»). Decisione del 30/10: owo-lib si aggiorna in una versione piccola a sé dopo la 0.7.3 e lì si prova l'ultimo NeoForge 21.1.x; finché quella prova non passa, NeoForge resta fermo. Scheda: `../mod-knowledge/aether.md`.
- Il minimo richiesto dalle mod del pack è 21.1.229 (BotanyPotsAdditions); il controllo dei nomi verifica da solo le richieste di ogni mod.

## Fatti verificati

- **Mod per la 1.21 sulla 1.21.1**: NeoForge accetta anche le mod che dichiarano solo Minecraft 1.21 (per esempio Iris chiede `[1.21,1.21.1)`): nella 1.21.1 il caricatore prova anche la versione 1.21 quando il controllo normale fallisce (sorgente di FancyModLoader, `VersionSupportMatrix`). Allo stesso modo accetta le mod scritte per NeoForge 21.0 (prova la 21.0.166).
- **File di config TOML**: un file parziale funziona (le chiavi mancanti prendono il valore di serie; un valore non valido torna al valore di serie chiave per chiave; le chiavi sconosciute si tolgono), ma al primo avvio il gioco lo riscrive, con una copia di backup e un avviso nel log; un file illeggibile viene ricreato da zero (`ConfigTracker.loadConfig`, `ModConfigSpec.correct`). Per il pack conviene portare file **completi**, partendo da quelli generati dal gioco nell'istanza di prova.
- **Config "server"** nella 1.21.1: globali in `config/<mod>-server.toml`; un mondo può sovrascriverle con una copia in `saves/<mondo>/serverconfig/` (`ServerLifecycleHooks`). La cartella `defaultconfigs/` non c'entra.
- Versione di FancyModLoader nel log: 4.0.45. Java 21 (gestito da Prism).
- Le mod di Modrinth che dichiarano "environment unknown" vengono segnate da packwiz per entrambi i lati (avviso innocuo nel log del workflow, successo con i pacchetti di shader).
