# Changelog — Mango Craft 1.21.1

_Documento vivo: una voce nuova per ogni versione, in cima._

Una voce per ogni versione, dalla più recente. Ogni voce dice:
- **Stato**: 🧪 in prova sul ramo `dev` · ✅ provata e rilasciata (tag `1.21.1-vX.Y.Z`; le 0.x sono pre-release di prova, il mondo vero parte dalla 1.0.0);
- **NeoForge** da impostare a mano in Prism e se serve un **mondo nuovo**;
- cosa cambia: mod, datapack, config;
- **Problemi noti**: i codici del [bug report](0402-bug-report.md) comparsi o risolti in quella versione.

La voce di una versione diventa anche la nota della sua release su GitHub.

## 0.4.0 — 18/10/2026 · tappa 3 (pre-release di prova)

- **NeoForge**: 21.1.259 (invariato).
- **Mondo nuovo**: sì per provarla (Guard Villagers mette le guardie nei villaggi generati, Goblin Traders fa comparire i mercanti nel sottosuolo e nel Nether). Versione di prova: il mondo vero parte dalla 1.0.0.
- **Decorazione**: **Macaw's Roofs**, **Macaw's Paths and Pavings**, **Macaw's Bridges**, **Macaw's Windows**, **Diagonal Fences**, **Diagonal Walls**, **Diagonal Windows**, **Chimes**, **Exposure** (macchine fotografiche), **Every Compat** (varianti per tutti i legni delle mod: per ora con la config di serie, che crea migliaia di blocchi; la config ridotta arriva con la 0.6.0).
- **Villaggi**: **Guard Villagers**, **Goblin Traders** (CurseForge, con la libreria **Framework**).
- **Tech**: **Create: Copycats+**.
- **Documenti** (non cambiano il gioco): riorganizzati con codici a quattro cifre, documentazione (`docs/`) separata dai documenti di lavoro (`lavoro/`); regole in `AGENTS.md`.
- **Stato**: 🧪 in prova su `dev` (prima prova 18/10: mondo nuovo, avvio pulito).
- **Problemi noti**: B22 (Every Compat rallenta l'avvio, si corregge nella 0.6.0), B23–B27 (minori).

## 0.3.0 — 18/10/2026 · tappa 2 (pre-release di prova)

- **NeoForge**: 21.1.259 (invariato).
- **Mondo nuovo**: sì per provarla (My Nether's Delight e Rustic Delight generano piante selvatiche, Chef's Delight case nei villaggi). Versione di prova: il mondo vero parte dalla 1.0.0.
- **Cucina, seconda ondata**: **My Nether's Delight**, **Chef's Delight**, **Create Confectionery**, **Rustic Delight**, **Ocean's Delight**, **Autochef's Delight**.
- **Agricoltura**: **Farming for Blockheads** (mercato, fertilizzanti, nido, mangiatoia).
- **Esperienza**: **Cognition** (ex Experience Obelisk): obelisco per depositare l'esperienza, liquido compatibile con tubi e serbatoi. Lo scambio con il liquido di Create arriva con la 0.6.0.
- **Datapack**: il pesce cotto di Starcatcher vale come "pesce cotto" nelle ricette (etichette `c:foods/cooked_fish`, `c:foods/cooked_fishes`, `bountifulfares:cooked_fishes`).
- **Stato**: ✅ provata il 18/10 (mondo nuovo, 7 minuti), pre-release `1.21.1-v0.3.0`.
- **Problemi noti**: nuovi B06 (Animal Pen e My Nether's Delight sullo stesso punto del codice, da verificare), B12 (zuppa di guardiano di Ocean's Delight senza texture, una variante dell'altare di Cognition senza modello), B15 (cornici e quadri sotterranei in posizione non valida). Risolto B20 (pesce cotto di Starcatcher).

## 0.2.3 — 18/10/2026 · tappa 1 (pre-release di prova)

- **NeoForge**: 21.1.259 (invariato).
- **Mondo nuovo**: sì per provarla. Regions Unexplored genera i suoi biomi solo nei chunk nuovi. Versione di prova: il mondo vero parte dalla 1.0.0.
- **Contenuto**: le aggiunte del vecchio pacchetto `modpack-matteo-0.2.3.mrpack`, mai provate in gioco finora:
  - biomi: **Regions Unexplored** (+ libreria Lithostitched);
  - decorazione e costruzione: **Supplementaries** (+ Moonlight Lib), **Handcrafted**, **Rechiseled** (+ Fusion), **Construction Sticks**;
  - utilità e prestazioni: **Chunky**, **Clumps**, **XP Tome**;
  - piccole e utili: **Just Enough Breeding**, **Just Enough Professions**, **NetherPortalFix**, **SeasonHud**, **Smarter Farmers**, **Open Together**, **AllTheLeaks** (CurseForge).
- **Datapack**: la cassaforte del Galeone di Supplementaries entra tra le casse con gli artefatti (livello "avamposto dei predoni", 25%): 153 tabelle.
- **Repository** (non cambia il gioco): inventario automatico dei file delle mod e controllo dei nomi del datapack; workflow per aggiungere mod da Modrinth.
- **Stato**: ✅ provata il 18/10 (mondo nuovo, 10 minuti), pre-release `1.21.1-v0.2.3`.
- **Problemi noti**: nessuno nuovo (solo l'avviso atteso di Moonlight su Forgified Fabric API, in B14).

## 0.1.1 — 18/10/2026 · base del repository

- **NeoForge**: 21.1.259. Non usare la 21.1.261 o successive: owo-lib 0.12.15.5 (incluso nell'Aether) fa cadere la connessione all'ingresso nel mondo. Si aggiornerà quando esce owo-lib 0.12.15.6.
- **Mondo nuovo**: non serve (è la stessa versione già provata).
- **Contenuto**: identico al pacchetto `modpack-matteo-0.1.1.mrpack` provato in gioco: 193 file di mod e librerie da Modrinth, il resource pack Fresh Animations (da attivare a mano nel gioco), le configurazioni (`almostunified/tags.json`, `sparsestructures.json5`) e il datapack `matteo_tweaks` caricato da Paxi.
- **Mod solo CurseForge** (5): The Twilight Forest 4.8.3345, Ars Elemental 0.7.10.4, Roaster's Delight 1.0.0.1, Spice of Life: Carrot Edition 1.16.6, BotanyPotsAdditions 1.1.0. Le scarica l'installer; quelle con distribuzione bloccata vanno scaricate a mano una volta (l'installer mostra pagina e percorso).
- **Novità tecnica**: prima versione gestita con packwiz su GitHub. Serve a verificare il nuovo sistema su una versione che già funziona.
- **Stato**: ✅ provata il 17/10 come pacchetto `.mrpack` e il 18/10 dal repository, release `1.21.1-v0.1.1`.
- **Problemi noti**: B01–B05, B07–B14, B16 (vedi bug report); B17 aggirato fissando NeoForge 21.1.259; B18 risolto in questa versione; B19 risolto già nella 0.1.0.

---

## Prima del repository (pacchetti `.mrpack`, 16–17/10/2026)

Versioni costruite a mano come file `.mrpack`, prima di passare a GitHub. Dettagli in [`../lavoro/0901-pacchetti-mrpack.md`](../lavoro/0901-pacchetti-mrpack.md).

- **0.2.3** (17/10): Just Enough Breeding e Professions, NetherPortalFix, SeasonHud, Smarter Farmers, Open Together, AllTheLeaks. Mai provata in gioco: rifatta come 0.2.3 del repository.
- **0.2.2** (17/10): XP Tome.
- **0.2.1** (17/10): cassaforte del Galeone tra le casse con gli artefatti.
- **0.2.0** (17/10): Regions Unexplored, Chunky, Clumps, Supplementaries, Handcrafted, Rechiseled, Construction Sticks (+ Lithostitched, Fusion, Moonlight).
- **0.1.1** (17/10): NeoForge da 21.1.262 a 21.1.259 per il "Connection lost" (B17); readme del datapack in minuscolo (B18). Provata: base del repository.
- **0.1.0** (16/10): primo pacchetto, 158 mod e resource pack più 36 librerie, config e datapack `matteo_tweaks`. Primo avvio il 17/10: parte in 32 secondi, poi "Connection lost" entrando nel mondo.
