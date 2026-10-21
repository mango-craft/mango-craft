# Iris (shader)

Aggiornata il 19/10/2026 · nel pack dalla 0.5.2 (ruolo e licenza: `../docs/0301-mod.md`; versione: `../docs/0403-distinta-mod.md`) · fonti: API di Modrinth, sorgenti di Iris (ramo 1.21.1), Sodium, Flywheel, Colorwheel, ImmediatelyFast, Fusion, Lodestone, Exposure, Shoulder Surfing, packwiz; log dell'istanza di prova. Ricerca: `../lavoro/versioni/v0.5.2.md`.

## Cose da non rompere

- Con Sodium 0.8 funziona **solo Iris 1.8.14-beta.1** (`iris@KduFYu4t`, 13/6/2026, LGPL-3.0): il changelog di Sodium 0.8.12 dice "Iris works as of 1.8.13". L'ultima *release*, la 1.8.12 (17/6/2025), è fatta per Sodium 0.6 e con Sodium 0.8 va in crash (issue Iris #3126 e #3220).
- Il workflow Modrinth da solo sceglie l'ultima release: Iris si aggiunge o aggiorna **solo indicando la versione** (`iris@<id>`). Il controllo dei nomi non fermerebbe l'errore: la 1.8.12 chiede `sodium [0.6,)`, che la 0.8 soddisfa.
- Prima di aggiornare Sodium, verificare che Iris lo supporti. Non si può tornare a Sodium 0.6: Supplementaries rifiuta Sodium più vecchio della 0.8.12-beta.1.
- Il ramo 1.21.1 di Iris è fermo al 13/6/2026.

## Fatti verificati

- La 1.8.14-beta.1 non dichiara dipendenze; dichiara Minecraft `[1.21,1.21.1)`, che NeoForge accetta sulla 1.21.1 (scheda `../theme-knowledge/neoforge.md`). È compilata su NeoForge 21.1.229. Contiene le sue librerie (glsl-transformer, jcpp, 4 moduli di Forgified Fabric API già nel pack con versioni uguali o più nuove). Incompatibile solo con Embeddium (non nel pack).
- Nel log, con Iris attiva senza shader: "Shaders are disabled because no valid shaderpack is selected"; ImmediatelyFast, Xaero's e EMF la riconoscono; Sodium spegne tre suoi mixin del cielo su richiesta di Iris; mappe dei mixin non lette e controllo degli aggiornamenti non disponibile per la beta: tutto innocuo (B14).
- `config/iris.properties`: `shaderPack`, `enableShaders`, `allowUnknownShaders`, `enableDebugOptions`, `disableUpdateMessage`, `maxShadowRenderDistance` (32), `colorSpace` (SRGB). Le impostazioni di ogni pacchetto stanno in un file `.txt` accanto al pacchetto con lo stesso nome: cambiando versione del pacchetto cambia il nome e vanno reimpostate. Nessun file di Iris nel pack (impostazioni video lasciate a chi gioca, decisione del 19/10).
- Iris non valuta l'hardware: la qualità si sceglie nei profili di ogni pacchetto.
- packwiz mette i pacchetti di shader di Modrinth nella cartella `shaderpacks/` (verificato nel sorgente di packwiz); dalla 0.5.3 il workflow Modrinth li accetta (loader "iris").

## Gli shader nel pack

Compatibilità delle mod del pack con uno shader attivo e pacchetti di shader (licenze, scelta): tema `../theme-knowledge/shader.md`.

## Storia nel pack

0.5.2 Iris + Enhanced Celestials 2: Shader Support (`../lavoro/versioni/v0.5.2.md`); 0.5.3 due pacchetti (`v0.5.3.md`).
