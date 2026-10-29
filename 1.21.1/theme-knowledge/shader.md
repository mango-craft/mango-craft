# Tema: shader

Aggiornata il 19/10/2026 · mod coinvolte: Iris, Sodium, Complementary Reimagined, MakeUp - Ultra Fast, Colorwheel, Enhanced Celestials 2: Shader Support, Create/Flywheel e le mod che hanno shader propri · fonti: API di Modrinth, sorgenti delle mod (ramo 1.21.1), log dell'istanza di prova. Ricerche: `../lavoro/versioni/v0.5.2.md` (supporto agli shader) e `v0.5.3.md` (pacchetti); grezzo `../../ai-agents/archivio/2026-10-19_1.21.1-v0.5.3_shader-pack/`.

Gli shader sono **facoltativi**: il pack porta Iris e due pacchetti spenti di serie; senza attivarne uno non cambia niente. Fatti su Iris e sulla versione obbligata con Sodium: `../mod-knowledge/iris.md`, `../mod-knowledge/sodium.md`. Pacchetti: `../mod-knowledge/complementary-reimagined.md`, `../mod-knowledge/makeup-ultra-fast-shaders.md`. Colori delle lune negli shader: `../mod-knowledge/enhanced-celestials-2.md`.

## Le mod del pack con uno shader attivo

| Mod | Con Iris | Fonte |
|---|---|---|
| Create 6 / Flywheel 1.0.6 | Con uno shader attivo Flywheel spegne la sua accelerazione ("Flywheel backend fell back from indirect to off" nel log) e Create disegna in modo normale: corretto ma più lento con molti macchinari. Per recuperare le prestazioni c'è **Colorwheel** (scheda `../mod-knowledge/colorwheel.md`) | `Backends.java` di Flywheel; log |
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

`../mod-knowledge/complementary-reimagined.md`, `../mod-knowledge/makeup-ultra-fast-shaders.md` (dalla 0.5.3, spenti di serie). Licenze dei pacchetti diffusi: Complementary ammesso nei modpack se scaricato da Modrinth e non modificato; MakeUp LGPL-3.0; Miniature e Mellow MIT; Photon licenza propria; BSL, Bliss, Solas tutti i diritti riservati. Il nostro `modrinth_resolve.py` sceglie per i pacchetti di shader le versioni per Iris.
