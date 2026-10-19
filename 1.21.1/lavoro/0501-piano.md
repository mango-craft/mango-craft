# Piano — Minecraft 1.21.1

Le tappe verso la **1.0.0**, la prima versione per il mondo vero, e lo stato di avanzamento. Documento vivo: si aggiorna a ogni tappa. Il flusso di lavoro (ramo `dev`, merge in `main`, tag, pre-release 0.x, prova di ogni tappa) è in `AGENTS.md`. Valutazioni, decisioni, lavoro e prove di ogni versione: `versioni/`. Cosa è uscito davvero: `../docs/0401-changelog.md`; cosa c'è nel pack: `../docs/0301-mod.md`.

## Tappe (piano deciso il 18/10/2026)

| Tappa | Versione | Contenuto | Stato |
|---|---|---|---|
| 0 | — | Strumenti: workflow **Aggiungi mod Modrinth** (versione, hash e dipendenze presi da Modrinth con packwiz) e **Inventario** (elenco di oggetti, blocchi e tabelle letto dai file delle mod, per controllare i nomi usati nel datapack) | ✅ fatta (18/10, su `main`) |
| 1 | [0.2.3](versioni/v0.2.3.md) | Le aggiunte del vecchio pacchetto 0.2.3: Regions Unexplored, Supplementaries, Handcrafted, Rechiseled, Construction Sticks, Chunky, Clumps, XP Tome, Just Enough Breeding/Professions, NetherPortalFix, SeasonHud, Smarter Farmers, Open Together, AllTheLeaks (CurseForge) + Lithostitched, Fusion, Moonlight; cassaforte del Galeone nel datapack | ✅ provata e rilasciata (18/10, pre-release `1.21.1-v0.2.3`) |
| 2 | [0.3.0](versioni/v0.3.0.md) | Cucina, agricoltura, esperienza: My Nether's Delight, Chef's Delight, Create Confectionery, Rustic Delight, Ocean's Delight, Autochef's Delight, Farming for Blockheads, Cognition; **pesce cotto di Starcatcher** nelle etichette del pesce cotto (approvato 18/10) | ✅ provata e rilasciata (18/10, pre-release `1.21.1-v0.3.0`) |
| 3 | [0.4.0](versioni/v0.4.0.md) | Decorazione e tech: Macaw's Roofs/Paths/Bridges/Windows, Diagonal Fences/Walls/Windows, Chimes, Exposure, Goblin Traders, Guard Villagers, Every Compat, Copycats+ | ✅ provata e rilasciata (18/10, pre-release `1.21.1-v0.4.0`) |
| 4 | [0.5.0](versioni/v0.5.0.md) | Esplorazione: Jaden's Nether Expansion (+ Elysium API, Lodestone), Moog's Nether Structures, Nether Depths Upgrade, Aures Farmers Structures, Better Archeology, Nature's Compass, Aquamirae (+ Fragmentum), Creeper Overhaul, Paragliders | ✅ provata e rilasciata (18/10, pre-release `1.21.1-v0.5.0`) |
| 4.1 | [0.5.1](versioni/v0.5.1.md) | Lune: Enhanced Celestials 2 (Core + Default Lunar Events) al posto di Enhanced Celestials, luna di sangue ribilanciata nel formato nuovo, Data Anchor aggiornata (decisa il 18/10) | ✅ provata e rilasciata (18/10, pre-release `1.21.1-v0.5.1`) |
| 4.2 | [0.5.2](versioni/v0.5.2.md) | Supporto agli shader: Iris 1.8.14-beta.1 ed Enhanced Celestials 2: Shader Support (nessuna mod di compatibilità obbligatoria: `versioni/v0.5.2.md`); gli shader restano facoltativi; config delle traduzioni di EC2 (B32) (decisa il 18/10) | ✅ provata e rilasciata (19/10, pre-release `1.21.1-v0.5.2`) |
| 4.3 | [0.5.3](versioni/v0.5.3.md) | Due pacchetti di shader facoltativi scelti per le mod del pack (Complementary Reimagined, MakeUp - Ultra Fast); impostazioni video lasciate a chi gioca (Sodium si regola già da solo); Every Compat resta nella 0.6.0 (decisa il 19/10) | ✅ provata e rilasciata (19/10, pre-release `1.21.1-v0.5.3`) |
| 5 | [0.6.0](versioni/v0.6.0.md) | Datapack e config: correzione Berserker, esperienza Create ↔ Cognition, mercato di Farming for Blockheads, vasi (piante, terreni e alberi mancanti: conti in `versioni/v0.6.1.md`), config di Every Compat, Artifacts e, se serve, Jaden's. Progettazione in `versioni/v0.6.0.md`, che propone di dividerla in 0.6.0 (config e correzioni), 0.6.1 (vasi, `v0.6.1.md`), 0.6.2 (mercato, `v0.6.2.md`) | in progettazione |
| 6 | 0.6.x → **1.0.0** | Mondo di prova: Chunky, mappa di Xaero, densità delle strutture, Nether, `/botanypots debug`, esperienza; correzioni; poi release 1.0.0 e mondo vero | da fare |

NeoForge resta fermo (motivo in `../docs/0303-note-tecniche.md`): se una mod nuova ne chiede uno più recente, va segnalato nella sua tappa (il controllo dei nomi lo verifica da solo).
