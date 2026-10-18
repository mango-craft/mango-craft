# Supporto agli shader: Iris e compatibilità (18/10/2026)

> **Documento storico**: fotografia del momento in cui è stato scritto, non si aggiorna. Lo stato attuale è nei documenti vivi (vedi il README della cartella).

Richiesta dell'utente: preparare il pack agli shader nella **0.5.2** (Iris ed Enhanced Celestials 2: Shader Support), anche se oggi non li usa. Verifiche fatte sull'API di Modrinth, sui metafile e sull'inventario del pack e sui sorgenti pubblici delle mod (Iris, Sodium, Flywheel, Colorwheel, ImmediatelyFast, Fusion, Lodestone, Exposure, Shoulder Surfing, packwiz).

## Cosa aggiungere

- **Sodium** è nel pack: **0.8.13** (`sodium-neoforge-0.8.13+mc1.21.1.jar`).
- **Iris 1.8.14-beta.1** (`iris@KduFYu4t`, 13/6/2026, LGPL-3.0): è **l'unica** versione per NeoForge 1.21.1 che funziona con Sodium 0.8.
  - Il changelog di Sodium 0.8.12 dice "Iris works as of 1.8.13" (verificato su Modrinth, 18/10).
  - L'ultima *release*, la 1.8.12 (17/6/2025), è fatta per Sodium 0.6 e con Sodium 0.8 va in crash (issue Iris #3126 e #3220).
  - Il workflow sceglie l'ultima release, quindi va chiamato con **`iris@KduFYu4t`**. Il controllo dei nomi **non** fermerebbe l'errore: la 1.8.12 chiede `sodium [0.6,)`, che la 0.8.13 soddisfa.
  - La beta non dichiara dipendenze. È compilata su NeoForge 21.1.229, quindi va bene con la nostra 21.1.259. Contiene già le sue librerie (glsl-transformer, jcpp, 4 moduli di Forgified Fabric API). È incompatibile solo con Embeddium, che non è nel pack.
  - Il ramo 1.21.1 di Iris è fermo al 13/6/2026: non c'è una versione più nuova.
- **Enhanced Celestials 2: Shader Support 2.0.0.3** (`4uOjogNm`, 3/9/2026, ARR, solo lato client). Richiede Core ≥ 2.0.3.1, CorgiLib, Sodium e Iris (qualsiasi versione).
- **Nessun'altra mod obbligatoria.**

## Le mod del pack con Iris

| Mod | Con Iris | Fonte |
|---|---|---|
| Create 6 / Flywheel 1.0.6 | Già gestito: con uno shader attivo Flywheel spegne la sua accelerazione e Create disegna in modo normale. Il risultato è corretto ma più lento con molti macchinari. Per recuperare le prestazioni c'è **Colorwheel** 1.3.0 (`colorwheel@8rq5KP4U`, LGPL-3.0), compilata su Iris 1.8.8 e Sodium 0.6, che funziona solo con pacchetti di shader supportati. Esclude "Iris & Oculus Flywheel Compat": se ne usa una sola | Flywheel `Backends.java`; mods.toml di Colorwheel |
| ImmediatelyFast | Compatibilità già inclusa. Se non trova certe parti di Iris chiude il gioco: verificato che nella 1.8.14 ci sono | sorgente di ImmediatelyFast (`IrisCompat`) e di Iris |
| Fusion 1.3.16 | Supporta le texture PBR di Iris ed è compilata proprio sulla 1.8.14-beta.1 | build.gradle di Fusion |
| EMF / ETF, Shoulder Surfing, Tombstone | Compatibilità con Iris già nel codice | sorgenti, inventario |
| Reactive Alchemy | Con Iris installata usa un disegno apposito per il Gateway (le funzioni di Iris che usa esistono nella 1.8.14) | sorgente |
| Exposure | Trattamento speciale solo con Distant Horizons, che non è nel pack | sorgente |
| Lodestone (per Jaden's), Twilight Forest, Ars Nouveau, Psi, Hexerei, Starcatcher | Hanno shader propri: **con uno shader attivo** alcuni effetti possono vedersi male. Ars: i blocchi Skyweave diventano neri; la correzione (Ars Skyweave Shader Fix, circa 2.000 download) è solo su CurseForge | sorgenti, pagina CurseForge |
| Subtle Effects, Particle Rain | Con alcuni pacchetti di shader certi effetti o particelle non si vedono | descrizioni su Modrinth |
| LambDynamicLights, Entity Culling, Not Enough Animations, Aether, Deeper and Darker, Mekanism | Nessun codice per Iris, nessun problema noto | sorgenti |

## Mod di contorno facoltative

- **Colorwheel** 🟡: utile solo usando gli shader con molti macchinari di Create. È compilata su una Iris più vecchia: le 78 funzioni di Iris che usa ci sono tutte nella 1.8.14, ma il funzionamento non è verificato.
- **Ars Skyweave Shader Fix** 🟡: solo CurseForge, poco diffusa.
- Shader Folder, Iris Search, Bad Horse Fix: solo comodità.

## Pacchetti di shader

packwiz li gestisce: finiscono nella cartella `shaderpacks/` (verificato nel sorgente). Il nostro `modrinth_resolve.py` però scarta le versioni che non sono per NeoForge, quindi per aggiungerli andrebbe adattato. Licenze dei più diffusi:

| Pacchetto | Licenza |
|---|---|
| Complementary Reimagined / Unbound | Ammessi nei modpack se scaricati da Modrinth e non modificati |
| MakeUp Ultra Fast | LGPL-3.0 |
| Miniature, Mellow | MIT |
| Photon | Licenza propria |
| BSL, Bliss | ARR; BSL dice "non ridistribuire senza permesso" |

## Rischi

- Iris da usare è una **beta**, e non ce n'è un'altra compatibile.
- Non si può tornare a Sodium 0.6 per usare la Iris stabile: Supplementaries rifiuta Sodium più vecchio della 0.8.12-beta.1.
- Alcune mod attivano il loro codice per Iris appena la trovano installata (ImmediatelyFast, Fusion, Shoulder Surfing, Reactive Alchemy). Sono state controllate le parti di Iris che usano, non l'avvio in gioco.
- Nessuna mod del pack si dichiara incompatibile con Iris, e Iris non dichiara incompatibile nessuna mod del pack.

## Non verificato

- EC2 Shader Support con Sodium 0.8 e Iris 1.8.14 (codice chiuso): va provata in gioco, anche senza shader attivi.
- Issue recenti su GitHub di Iris (l'API non era raggiungibile dall'area di lavoro).
- Xaero's e Cataclysm (codice chiuso o senza riferimenti a Iris).
