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
| 5 | [0.6.0](versioni/v0.6.0.md) | Config e correzioni: correzione Berserker, config di Artifacts, Carry On, Inventory Essentials e FallingTree, 152 casse con gli artefatti (comprese Mowzie's e quattro strutture con «vault»); Every Compat invariato (tutti i blocchi, niente `RUN_ONCE`). Divisione della tappa **approvata il 19/10** | ✅ provata (21/10) e rilasciata (22/10, pre-release `1.21.1-v0.6.0`) |
| 5.1 | [0.6.1](versioni/v0.6.1.md) | Vasi: piante, terreni e alberi mancanti (conti in `versioni/v0.6.1.md`), con uno script generatore | in lavorazione: script e 241 colture + 18 terreni scritti il 22/10 (da provare); mancano alberi di Bountiful Fares, graticci, Jaden's/Nether Depths e le prove |
| 5.2 | [0.6.2](versioni/v0.6.2.md) | Mercato di Farming for Blockheads: semi e alberelli delle mod mancanti | da fare |
| 5.3 | [0.6.3](versioni/v0.6.3.md) | Esperienza Create ↔ Cognition: unità del liquido e scambio nel Mescolatore (spostata fuori dalla 0.6.0 per decisione di Matteo, 21/10) | da fare |
| 6 | 0.6.x → **1.0.0** | Mondo di prova: Chunky, mappa di Xaero, densità delle strutture, Nether, `/botanypots debug`, esperienza; correzioni; poi release 1.0.0 e mondo vero (suddivisione proposta qui sotto) | da fare |

NeoForge resta fermo (motivo in `../docs/0303-note-tecniche.md`): se una mod nuova ne chiede uno più recente, va segnalato nella sua tappa (il controllo dei nomi lo verifica da solo).

## Proposta del 21/10/2026 per dopo la tappa 5 (in sospeso)

Richiesta di Matteo: il piano delle prossime versioni. **Non è deciso, in sospeso**: il 22/10 Matteo ha approvato solo la 0.6.x con le sue figlie (0.6.0–0.6.3) e ha detto che per le versioni successive «ci sarà tempo». Quando approverà, le righe passano nella tabella qui sopra e la «tappa 6» di oggi (mondo di prova) prende il suo nuovo numero negli altri documenti (`0502`, `0503`, `../docs/0302-config.md`).

**Ordine**: prima il contenuto, poi gli aggiornamenti, poi il mondo di prova. Il mondo di prova deve girare con il pack **finale**: aggiornare una mod può cambiare nomi e generazione del mondo, e dopo la 1.0.0 certe cose non si correggono più (`0503`, sezione 4, n. 5). Ogni versione ha poche prove di uscita rapide (`AGENTS.md`, sezione 5); il resto si prova giocando.

| Versione | Contenuto | Cosa decide Matteo | Prove di uscita |
|---|---|---|---|
| **0.7.0** (tappa 6) | **Progressione**: una mod per la schermata dei progressi (🟢 Reliable Advancements o Lucid Advancements, provate una alla volta) e la decisione sugli effetti nuovi della luna di sangue | quale mod; tenere o spegnere i due effetti nuovi | il gioco parte; la schermata si apre e mostra i progressi di Minecraft e delle mod; luna di sangue come deciso |
| **0.7.1** | 🟡 Scheda «Mango Craft» (20–40 traguardi nel datapack) e guida del pack; solo se Matteo li vuole (`0503`, sezione 3) | se farli e quanti | i traguardi compaiono e si sbloccano; nessun errore di caricamento |
| **0.7.2** | 🟡 Solo se Matteo lo decide: mod che cambiano il terreno (Tectonic, con StructBlend) o Malum se esce la 1.9 (`0601`) | sì o no, **prima** del mondo di prova | mondo nuovo: biomi e strutture sensati, nessun errore |
| **0.8.0** (tappa 7) | **Aggiornamenti e licenze**: workflow che elenca le versioni nuove senza installarle, giro di aggiornamenti, controllo delle licenze, ritorno all'ultimo NeoForge se è uscita owo-lib 0.12.15.6 (B17) | quali mod aggiornare | avvio e mondo come prima; log confrontato con la versione precedente; ogni mod importante aggiornata provata con un controllo semplice |
| **0.9.x** (tappa 8) | **Mondo di prova**: le prove della sezione «Mondo di prova» di `0502` (Chunky e mappa di Xaero, densità delle strutture, Nether, vasi, esperienza, Every Compat), difficoltà, slot degli accessori se stretti, B33 con 12 GB; ogni correzione è una 0.9.x | tasti in conflitto e lingua (entro la 0.8.0) | quelle di `0502` e della soglia della 1.0.0 |
| **1.0.0** | Se la soglia è raggiunta (`0503`, sezione 4, n. 5): release e mondo vero | l'OK finale | la soglia della 1.0.0 |

Senza versione propria: i tasti in conflitto (B, C) vanno solo in un elenco nei documenti; la lingua del gioco è ancora da chiarire (`0503`, sezione 2).
