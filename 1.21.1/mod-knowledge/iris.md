# Iris (shader)

Aggiornata il 19/10/2026 · nel pack dalla 0.5.2 (ruolo e licenza: `../docs/0301-mod.md`; versione: `../docs/0403-distinta-mod.md`) · fonti: API di Modrinth, sorgenti di Iris (ramo 1.21.1), Sodium, Flywheel, Colorwheel, ImmediatelyFast, Fusion, Lodestone, Exposure, Shoulder Surfing, packwiz; log dell'istanza di prova. Ricerca: `../lavoro/versioni/v0.5.2.md`.

## Cose da non rompere

- Con Sodium 0.8 funziona **solo Iris 1.8.14-beta.1** (`iris@KduFYu4t`, 13/6/2026, LGPL-3.0): il changelog di Sodium 0.8.12 dice "Iris works as of 1.8.13". L'ultima *release*, la 1.8.12 (17/6/2025), è fatta per Sodium 0.6 e con Sodium 0.8 va in crash (issue Iris #3126 e #3220).
- Il workflow Modrinth da solo sceglie l'ultima release: Iris si aggiunge o aggiorna **solo indicando la versione** (`iris@<id>`). Il controllo dei nomi non fermerebbe l'errore: la 1.8.12 chiede `sodium [0.6,)`, che la 0.8 soddisfa.
- Prima di aggiornare Sodium, verificare che Iris lo supporti. Non si può tornare a Sodium 0.6: Supplementaries rifiuta Sodium più vecchio della 0.8.12-beta.1.
- Il ramo 1.21.1 di Iris è fermo al 13/6/2026.

## Fatti verificati

- La 1.8.14-beta.1 non dichiara dipendenze; dichiara Minecraft `[1.21,1.21.1)`, che NeoForge accetta sulla 1.21.1 (scheda `neoforge.md`). È compilata su NeoForge 21.1.229. Contiene le sue librerie (glsl-transformer, jcpp, 4 moduli di Forgified Fabric API già nel pack con versioni uguali o più nuove). Incompatibile solo con Embeddium (non nel pack).
- Nel log, con Iris attiva senza shader: "Shaders are disabled because no valid shaderpack is selected"; ImmediatelyFast, Xaero's e EMF la riconoscono; Sodium spegne tre suoi mixin del cielo su richiesta di Iris; mappe dei mixin non lette e controllo degli aggiornamenti non disponibile per la beta: tutto innocuo (B14).
- `config/iris.properties`: `shaderPack`, `enableShaders`, `allowUnknownShaders`, `enableDebugOptions`, `disableUpdateMessage`, `maxShadowRenderDistance` (32), `colorSpace` (SRGB). Le impostazioni di ogni pacchetto stanno in un file `.txt` accanto al pacchetto con lo stesso nome: cambiando versione del pacchetto cambia il nome e vanno reimpostate. Nessun file di Iris nel pack (impostazioni video lasciate a chi gioca, decisione del 19/10).
- Iris non valuta l'hardware: la qualità si sceglie nei profili di ogni pacchetto.
- packwiz mette i pacchetti di shader di Modrinth nella cartella `shaderpacks/` (verificato nel sorgente di packwiz); dalla 0.5.3 il workflow Modrinth li accetta (loader "iris").

## Le mod del pack con uno shader attivo

| Mod | Con Iris | Fonte |
|---|---|---|
| Create 6 / Flywheel 1.0.6 | Con uno shader attivo Flywheel spegne la sua accelerazione ("Flywheel backend fell back from indirect to off" nel log) e Create disegna in modo normale: corretto ma più lento con molti macchinari. Per recuperare le prestazioni c'è **Colorwheel** (scheda `colorwheel.md`) | `Backends.java` di Flywheel; log |
| ImmediatelyFast | Compatibilità già inclusa; se non trova certe parti di Iris chiude il gioco: nella 1.8.14 ci sono | sorgente (`IrisCompat`) |
| Fusion 1.3.16 | Supporta le texture PBR di Iris, compilata proprio sulla 1.8.14-beta.1 | build.gradle di Fusion |
| EMF / ETF, Shoulder Surfing, Tombstone | Compatibilità con Iris già nel codice | sorgenti, inventario |
| Reactive Alchemy | Con Iris usa un disegno apposito per il Gateway (le funzioni che usa esistono nella 1.8.14) | sorgente |
| Exposure | Trattamento speciale solo con Distant Horizons, che non è nel pack | sorgente |
| Lodestone (Jaden's), Twilight Forest, Ars Nouveau, Psi, Hexerei, Starcatcher | Hanno shader propri: con uno shader attivo alcuni effetti possono vedersi male. Ars: i blocchi Skyweave diventano neri; correzione (Ars Skyweave Shader Fix) solo su CurseForge, candidata | sorgenti, CurseForge |
| Subtle Effects, Particle Rain | Con alcuni pacchetti certi effetti o particelle non si vedono | descrizioni su Modrinth |
| LambDynamicLights, Entity Culling, Not Enough Animations, Aether, Deeper and Darker, Mekanism | Nessun codice per Iris, nessun problema noto | sorgenti |
| Xaero's, Cataclysm | Non verificato (codice chiuso o senza riferimenti a Iris) | — |

Nessuna mod del pack si dichiara incompatibile con Iris, e viceversa. Alcune mod attivano il loro codice per Iris appena la trovano (ImmediatelyFast, Fusion, Shoulder Surfing, Reactive): verificate nel codice, non in gioco con uno shader attivo per ciascuna.

## Pacchetti di shader nel pack

`complementary-reimagined.md`, `makeup-ultra-fast-shaders.md` (dalla 0.5.3, spenti di serie). Licenze dei pacchetti diffusi: Complementary ammesso nei modpack se scaricato da Modrinth e non modificato; MakeUp LGPL-3.0; Miniature e Mellow MIT; Photon licenza propria; BSL, Bliss, Solas tutti i diritti riservati. Il nostro `modrinth_resolve.py` sceglie per i pacchetti di shader le versioni per Iris.

## Storia nel pack

0.5.2 Iris + Enhanced Celestials 2: Shader Support (`../lavoro/versioni/v0.5.2.md`); 0.5.3 due pacchetti (`v0.5.3.md`).
