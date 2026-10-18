# Piano — Minecraft 1.21.1

Le tappe verso la **1.0.0**, la prima versione per il mondo vero, e lo stato di avanzamento. Documento vivo: si aggiorna a ogni tappa. Il flusso di lavoro (ramo `dev`, merge in `main`, tag, pre-release 0.x, prova di ogni tappa) è in `AGENTS.md`. Cosa è uscito davvero in ogni versione: `../docs/0401-changelog.md`.

## Tappe (piano deciso il 18/10/2026)

| Tappa | Versione | Contenuto | Stato |
|---|---|---|---|
| 0 | — | Strumenti: workflow **Aggiungi mod Modrinth** (versione, hash e dipendenze presi da Modrinth con packwiz) e **Inventario** (elenco di oggetti, blocchi e tabelle letto dai file delle mod, per controllare i nomi usati nel datapack) | ✅ fatta (18/10, su `main`) |
| 1 | 0.2.3 | Le aggiunte del vecchio pacchetto 0.2.3: Regions Unexplored, Supplementaries, Handcrafted, Rechiseled, Construction Sticks, Chunky, Clumps, XP Tome, Just Enough Breeding/Professions, NetherPortalFix, SeasonHud, Smarter Farmers, Open Together, AllTheLeaks (CurseForge) + Lithostitched, Fusion, Moonlight; cassaforte del Galeone nel datapack | ✅ provata e rilasciata (18/10, pre-release `1.21.1-v0.2.3`) |
| 2 | 0.3.0 | Cucina, agricoltura, esperienza: My Nether's Delight, Chef's Delight, Create Confectionery, Rustic Delight, Ocean's Delight, Autochef's Delight, Farming for Blockheads, Cognition; **pesce cotto di Starcatcher** nelle etichette del pesce cotto (approvato 18/10) | ✅ provata e rilasciata (18/10, pre-release `1.21.1-v0.3.0`) |
| 3 | 0.4.0 | Decorazione e tech: Macaw's Roofs/Paths/Bridges/Windows, Diagonal Fences/Walls/Windows, Chimes, Exposure, Goblin Traders, Guard Villagers, Every Compat, Copycats+ | 🧪 su `dev`, da provare |
| 4 | 0.5.0 | Esplorazione: Jaden's Nether Expansion (+ Elysium API, Lodestone), Moog's Nether Structures, Nether Depths Upgrade, Aures Farmers Structures, Better Archeology, Nature's Compass, Aquamirae, Creeper Overhaul, Paragliders | da fare |
| 5 | 0.6.0 | Datapack e config: correzione Berserker, esperienza Create ↔ Cognition, mercato di Farming for Blockheads, vasi (piante, terreni e alberi mancanti: conti in `0620-progetto-datapack.md`), config di Every Compat, Jaden's, Moog's, Artifacts | da fare |
| 6 | 0.6.x → **1.0.0** | Mondo di prova: Chunky, mappa di Xaero, densità delle strutture, Nether, `/botanypots debug`, esperienza; correzioni; poi release 1.0.0 e mondo vero | da fare |

**Stato per gruppi** (aggiornato al 18/10/2026) · ✅ fatto · 🧪 da provare · ⏳ previsto

| Gruppo di mod | Cosa | Stato |
|---|---|---|
| Base del pack | Cucina e Farmer's Delight, vasi, natura e pozioni, Create e Mekanism, storage e zaini, Truly Modular e Apotheosis, strutture, dimensioni, boss, villager, magia, comodità, interfaccia, atmosfera, performance, fix (199 file) | ✅ 0.1.1 |
| Biomi e costruzione | Regions Unexplored, Supplementaries, Handcrafted, Rechiseled, Construction Sticks (+ 3 librerie) | ✅ 0.2.3 |
| Utilità | Chunky, Clumps, XP Tome, Just Enough Breeding e Professions, NetherPortalFix, SeasonHud, Smarter Farmers, Open Together, AllTheLeaks | ✅ 0.2.3 |
| Cucina, seconda ondata | My Nether's, Chef's, Rustic, Ocean's e Autochef's Delight, Create Confectionery | ✅ 0.3.0 |
| Agricoltura ed esperienza | Farming for Blockheads, Cognition | ✅ 0.3.0 |
| Decorazione | Macaw's ×4, Diagonal ×3, Chimes, Exposure, Every Compat | 🧪 0.4.0 su `dev` |
| Villaggi e tech | Guard Villagers, Goblin Traders (+ Framework, entrambe solo CurseForge), Copycats+ | 🧪 0.4.0 su `dev` |
| Nether | Jaden's Nether Expansion, Moog's Nether Structures, Nether Depths Upgrade | ⏳ 0.5.0 |
| Esplorazione e mob | Aures Farmers Structures, Better Archeology, Nature's Compass, Paragliders, Aquamirae, Creeper Overhaul | ⏳ 0.5.0 |

| Datapack e config | Cosa | Stato |
|---|---|---|
| Lune di sangue | 5% delle notti, mostri ×2; super luna ×4 | ✅ 0.1.1 |
| Artefatti nelle casse | 153 casse di strutture modded, Galeone compreso | ✅ 0.2.3 |
| Artefatti: correzioni | 15 nomi di casse di When Dungeons Arise e Dungeons and Taverns sbagliati; casse di Mowzie's Mobs e Born in Chaos | ⏳ 0.6.0 |
| Vasi: Ars Nouveau | Magebloom, Sourceberry, 5 frutti di archwood | ✅ 0.1.1 |
| Vasi: tutto il resto | Piante, terreni e alberi mancanti (conti in 0620), piante di Jaden's e Nether Depths, nomi vecchi di Regions Unexplored | ⏳ 0.6.0 |
| Pesce cotto di Starcatcher | Nelle etichette del pesce cotto | ✅ 0.3.0 |
| Esperienza | Scambio Create ↔ Cognition nel Mescolatore, valore del liquido di Cognition | ⏳ 0.6.0 |
| Mercato di Farming for Blockheads | Voci per le mod che il mercato non conosce | ⏳ 0.6.0 |
| Berserker di Cataclysm | Tornano nelle fortezze di YUNG's | ⏳ 0.6.0 |
| Config AlmostUnified | 19 etichette di cibo intercambiabili | ✅ 0.1.1 |
| Config Sparse Structures | Densità generale ✅ 0.1.1; regolazione struttura per struttura | ⏳ 0.6.x (mondo di prova) |
| Altre config | Every Compat, Jaden's, Moog's, Artifacts (dettaglio in `../docs/0302-config.md`) | ⏳ 0.6.0 |

NeoForge resta fermo (motivo in `../docs/0303-note-tecniche.md`): se una mod nuova ne chiede uno più recente, va segnalato nella sua tappa (il controllo dei nomi lo verifica da solo).
