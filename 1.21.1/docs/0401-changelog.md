# Changelog — Mango Craft 1.21.1

_Documento vivo: una voce nuova per ogni versione, in cima._

Una voce per ogni versione, dalla più recente. Ogni voce dice:
- **Stato**: 🧪 in prova sul ramo `dev` · ✅ provata e rilasciata (tag `1.21.1-vX.Y.Z`; le 0.x sono pre-release di prova, il mondo vero parte dalla 1.0.0);
- **NeoForge** da impostare a mano in Prism e se serve un **mondo nuovo**;
- cosa cambia: mod, datapack, config;
- **Problemi noti**: i codici del [bug report](0402-bug-report.md) comparsi o risolti in quella versione.

La voce di una versione diventa anche la nota della sua release su GitHub.

## 0.7.1 — in lavorazione · fornaci (in prova)

- **NeoForge**: 21.1.259 (invariato).
- **Mondo nuovo**: non serve. Versione di prova: il mondo vero parte dalla 1.0.0.
- **Mod nuove**: **Iron Furnaces** 4.3.2 (fornaci dal rame alla netherite e arcobaleno, potenziamenti sul posto, accessori compresi generatore, fabbrica e riscaldatore), **FurnaceMk2** 0.1.11 con la libreria **VapourWare** 0.2.37 (una fornace migliorata con tre nuclei e l'esperienza raccolta in un cristallo), **Jumbo Furnace** 5.0.0.9 da CurseForge (cubo di 27 fornaci che cuoce molte cose insieme). Ricette e valori originali.
- **Invariato**: datapack e config.
- **Stato**: 🧪 in prova sul ramo `dev`.
- **Problemi noti**: da vedere nella prova.

## 0.7.0 — 24/10/2026 · accessori: Relics (pre-release di prova)

- **NeoForge**: 21.1.259 (invariato).
- **Mondo nuovo**: non serve per provare; le casse già aperte non cambiano. Versione di prova: il mondo vero parte dalla 1.0.0.
- **Mod nuove**: **Relics** 0.12.9 e **Reliquified Artifacts** 1.0.9 (entrambe beta), con la libreria **ShatterLib | OctoLib** 0.6.2. Gli artefatti di Artifacts diventano **reliquie**: salgono di livello usandole, con abilità rifatte; Relics porta 20 reliquie sue.
- **Datapack, bottino**: le reliquie nelle casse le mette Relics, nel **10%** delle casse `chests/` di tutte le mod (20% di serie, abbassato da noi), scelte per nome della cassa, bioma e dimensione. I nostri 15 file per 152 casse diventano **10 file per le 25 casse** che Relics non vede (Twilight Forest, YUNG's Better Dungeons, nave dell'End, cassaforte del Galeone, cittadella di Friends & Foes). Gli **scavi archeologici** danno ancora artefatti in 1 caso su 16 (5 tabelle vanilla riscritte; da ora anche in 5 punti di scavo di Better Archeology).
- **Datapack, slot**: gli artefatti si indossano solo negli slot di Curios (Reliquified Artifacts ignora la config di Artifacts: le etichette di Accessories si correggono nel datapack).
- **Strumenti**: il controllo dei nomi verifica anche le tabelle tirate da `neoforge:add_table` e le voci che rimandano a un'altra tabella.
- **Stato**: ✅ provata il 24/10/2026 (avvio e mondo, 29.379 ricette; nessun errore nuovo del datapack nel log; reliquie nelle casse, artefatti nelle casse nostre e negli scavi, livelli e slot come attesi) e rilasciata come pre-release `1.21.1-v0.7.0`.
- **Problemi noti**: nuovi B42 (Reliquified Artifacts svuota tre etichette di slot di Artifacts, voluto), B43 (avvisi di mixin di AllTheLeaks), B44 (piccoli difetti di grafica e suono di Relics), tutti minori; B41, B39, B38 e B04 come prima.

## 0.6.3 — 24/10/2026 · esperienza (pre-release di prova)

- **NeoForge**: 21.1.259 (invariato).
- **Mondo nuovo**: non serve. Versione di prova: il mondo vero parte dalla 1.0.0.
- **Datapack, esperienza liquida**: il liquido di Cognition (cognitium, 20 mB per punto) entra nella tabella delle unità di Create: Enchantment Industry, quindi l'Experience Hatch e le macchine di Create lo contano giusto. Due ricette del **Mescolatore** di Create scambiano i due liquidi senza perdite né guadagni: 50 mB di esperienza di Create ↔ 1000 mB di cognitium (50 punti da entrambe le parti). In una bacinella senza filtro le due ricette vanno avanti e indietro; per un verso solo si mette nel filtro il secchio del liquido che si vuole ottenere.
- **Strumenti**: il controllo dei nomi riconosce i liquidi dalle loro etichette e i risultati liquidi delle ricette di Create.
- **Invariato**: nessuna mod aggiunta o tolta; config invariate.
- **Stato**: ✅ provata il 24/10/2026 (avvio e mondo, 29.373 ricette, cioè le 2 del Mescolatore in più; nessun errore o avviso nuovo nel log; scambio nelle due direzioni come atteso) e rilasciata come pre-release `1.21.1-v0.6.3`.
- **Problemi noti**: nessuno nuovo; B41, B39, B38 e B04 come nella 0.6.2.

## 0.6.2 — 24/10/2026 · mercato (pre-release di prova)

- **NeoForge**: 21.1.259 (invariato).
- **Mondo nuovo**: non serve. Versione di prova: il mondo vero parte dalla 1.0.0.
- **Datapack, mercato di Farming for Blockheads**: si possono comprare le piante di quasi tutte le mod del pack (**438 voci nuove**: semi, alberelli, fiori, selvatiche, funghi), escluse le piante decorative (erba, cespugli, liane) e quelle magiche o rare. I prezzi sono **alti** di proposito, perché il mercato non sostituisca l'esplorazione: moneta e quantità per **origine** e **rarità** della mod. Overworld: da 9 a 14 smeraldi per le piante comuni, poi da 6 a 15 diamanti (le mod salgono di classe: common solo Minecraft, uncommon le mod di cucina, poi a salire fino ad Ars Nouveau). Le altre dimensioni si pagano con il loro materiale più raro: 4 frammenti di netherite (Nether), 8 gusci di shulker (End), 4–5 gravitite incantate (Aether, Deep Aether), 6 cristalli di regalium (Undergarden), 6 steeleaf (Twilight Forest), 4 cristalli d'anima (Otherside di Deeper and Darker). I listini della mod per i semi e gli alberelli vanilla, delle Delight e di Ars sono **rincarati** con lo stesso criterio (prima 1 smeraldo). Tutto è generato da `scripts/mercato_genera.py` dalle regole in `1.21.1/data/mercato/*.csv`.
- **Strumenti**: la base dati dei vasi diventa la base dati delle piante del pack (oggetti e blocchi come anagrafiche, rarità condivisa tra vasi e mercato); l'inventario conserva voci e listini del mercato.
- **Invariato**: nessuna mod aggiunta o tolta; config invariate.
- **Stato**: ✅ provata il 24/10/2026 (avvio e mondo, 29.371 ricette, cioè le 438 voci in più; nessun errore del mercato, dei vasi o del datapack nel log; mercato e acquisti come attesi) e rilasciata come pre-release `1.21.1-v0.6.2`.
- **Problemi noti**: nuovo B41 (avviso di Sodium sulle schermate di EMI, minore); B39 (timeout di Reactive) ricompare a ogni avvio; B38 intermittente; B04 invariato.

## 0.6.1 — 24/10/2026 · vasi (pre-release di prova)

- **NeoForge**: 21.1.259 (invariato).
- **Mondo nuovo**: non serve. Versione di prova: il mondo vero parte dalla 1.0.0.
- **Datapack, vasi di Botany Pots**: si possono coltivare nei vasi le piante di quasi tutte le mod del pack (**279 colture** che Botany Pots non conosceva), gli **8 alberi di Bountiful Fares** (copiati da Botany Trees, LGPL-2.1) e **38 terreni nuovi** (terre delle altre dimensioni, secchi con pesci delle mod su acqua e lava); 21 file di terreno delle mod sostituiti; le terre «di terra» delle mod nell'etichetta `botanypots:soil/dirt`. Tutto è generato da `scripts/botanypots_genera.py` dalle regole in `1.21.1/data/vasi/*.csv`; escluse con il motivo le piante magiche o rare e quelle che nel vaso non funzionano (`lavoro/versioni/v0.6.1.md`).
- **Scala di rarità dei terreni**: 10 classi (da common a mythic) più 10 per i terreni da fabbricare; crescita da 0 a +80% e resa da 0 a +35%. I vasi di Botany Pots Tiers restano più importanti: un vaso elite con la terra semplice produce circa quattro volte un vaso normale con il terreno migliore.
- **Invariato**: nessuna mod aggiunta o tolta; config invariate.
- **Stato**: ✅ provata il 24/10/2026 (avvio e mondo, 28.933 ricette, nessun errore dei vasi né del datapack nel log; `check_crops` senza errori dopo B40; vasi elite con e senza tramoggia come atteso) e rilasciata come pre-release `1.21.1-v0.6.1`. La scala di rarità definitiva e la prova «una pianta per tipo» non sono state rifatte in gioco (decisione di Matteo): passano nelle prove nel tempo.
- **Problemi noti**: B37 (terreni a secchio senza grafica) e B40 (due piante alte senza raccolto) risolti; nuovi B38 (una finestra di Every Compat senza modello) e B39 (timeout di Reactive), minori; B04 intermittente.

## 0.6.0 — 22/10/2026 · config e correzioni (pre-release di prova)

- **NeoForge**: 21.1.259 (invariato).
- **Mondo nuovo**: non serve; conviene per vedere i Berserker, che compaiono solo nelle fortezze del Nether generate dopo. Versione di prova: il mondo vero parte dalla 1.0.0.
- **Config nel pack** (file completi copiati dall'istanza di prova): **Artifacts solo con Curios** (niente slot doppi con Accessories), **Carry On** che solleva anche i blocchi normali, **Inventory Essentials** senza trascinamento con Shift (doppione di Mouse Tweaks), **FallingTree** che abbatte l'albero intero solo da accovacciati.
- **Datapack**: i **Berserker infuocati** di Cataclysm compaiono anche nelle fortezze di YUNG's Better Nether Fortresses (B02); gli **artefatti nelle casse**: tolti 15 nomi che non esistevano più (B01), aggiunte 14 casse (When Dungeons Arise, Dungeons and Taverns con le quattro strutture dal tesoro «vault», Mowzie's Mobs: B03), 152 casse in tutto; l'elenco delle casse escluse è nella scheda `artifacts`.
- **Invariato**: Every Compat tiene tutte le varianti e tutti i legni (generazione delle risorse di serie); nessuna mod aggiunta o tolta.
- **Menu degli accessori**: in gioco i menu per indossare oggetti sono tre (Curios, Accessories standard, Aether). È come sono fatte le mod; restano così (decisione del 21/10, tema `accessori`).
- **Regole**: le prove di una versione si dividono in prove di uscita (poche, rapide) e prove nel tempo (`AGENTS.md`, sezione 5).
- **Stato**: ✅ provata il 21/10/2026 (mondo nuovo, avvio in 78 secondi, 28.612 ricette, datapack caricato, nessun errore nuovo grave nel log; Artifacts, Carry On, Inventory Essentials e FallingTree funzionano) e rilasciata come pre-release `1.21.1-v0.6.0`. L'esperienza (scambio Create ↔ Cognition) è passata alla 0.6.3.
- **Problemi noti**: B01 risolto; B02 e B03 corretti, da verificare in gioco (fortezza nuova, cassa di Mowzie's); nuovi B34 (When Dungeons Arise, un pezzo della fonderia che manca), B35 (entità senza blocco valido nella generazione, mod non identificata) e B36 (suoni dei pesci vuoti, forse del gioco base), tutti minori; B22 invariato; B33 da riprovare con 12 GB di memoria.

## 0.5.3 — 19/10/2026 · pacchetti di shader (pre-release di prova)

- **NeoForge**: 21.1.259 (invariato).
- **Mondo nuovo**: no.
- **Shader**: due pacchetti **spenti di serie**, nella cartella `shaderpacks`: **Complementary Reimagined** (il più completo, profili da Potato a Ultra) e **MakeUp - Ultra Fast** (il più leggero, riconosce i blocchi di Create, Farmer's Delight, Twilight Forest, Ars Nouveau e altre mod del pack). Si scelgono in gioco dalle impostazioni video. Scelta: `../lavoro/versioni/v0.5.3.md`.
- **Impostazioni video**: nessun file nel pack, restano a chi gioca; Sodium di serie è già regolato per le prestazioni (`0302-config.md`).
- **Strumenti**: il workflow Aggiungi mod Modrinth accetta anche pacchetti di shader e resource pack.
- **Stato**: ✅ provata il 19/10/2026 (i due pacchetti funzionano, anche cambiandoli in gioco; la luna di sangue avviata da comando si vede con gli shader; pacchetti lasciati con le impostazioni di serie) e rilasciata come pre-release `1.21.1-v0.5.3`.
- **Problemi noti**: nuovo B33 (memoria finita dopo un ricaricamento delle risorse in gioco, con 8 GB): consigliati 12 GB per l'istanza, da riprovare. Avvisi innocui degli shader aggiunti a B14.

## 0.5.2 — 18/10/2026 · shader (pre-release di prova)

- **NeoForge**: 21.1.259 (invariato).
- **Mondo nuovo**: no.
- **Shader** (facoltativi): **Iris** 1.8.14-beta.1 (l'unica versione che funziona con Sodium 0.8, ancora beta) ed **Enhanced Celestials 2: Shader Support** (i colori delle lune con gli shader). Nessun pacchetto di shader incluso: senza attivarne uno il gioco resta com'era. Le mod del pack con parti apposta per Iris sono state controllate prima (`../lavoro/versioni/v0.5.2.md`); nessuna libreria nuova.
- **Config**: traduzioni di Enhanced Celestials 2 spente (`config/enhancedcelestials2core/translations.json`): niente traduzioni scaricate da internet e niente più messaggio in chat (B32).
- **Strumenti**: il workflow Esamina mod legge anche i testi del codice compilato delle mod (nomi dei file di config, comandi).
- **Stato**: ✅ provata il 19/10/2026 (mondo nuovo, avvio in 70 secondi, 28.612 ricette; Iris attiva senza shader, nessun errore nuovo) e rilasciata come pre-release `1.21.1-v0.5.2`.
- **Problemi noti**: B32 risolto (il messaggio in chat non compare più). Messaggi innocui di Iris aggiunti a B14.

## 0.5.1 — 18/10/2026 · lune (pre-release di prova)

- **NeoForge**: 21.1.259 (invariato).
- **Mondo nuovo**: no. Il calendario delle lune riparte da zero nei mondi esistenti.
- **Lune**: **Enhanced Celestials 2** (Core + Default Lunar Events) al posto di Enhanced Celestials, il suo seguito ufficiale. La vecchia mod mostrava a ogni ingresso nel mondo una schermata che annunciava questa. Stesse lune (sangue, raccolto, blu, super), con due effetti nuovi per la luna di sangue: mostri che compaiono più vicini e assedio di zombi ai villaggi.
- **Datapack**: lune di sangue ribilanciate nel formato nuovo: più rare (peso 5 invece di 10) e mostri ×2 / ×4 (super luna) invece di ×2,25 / ×4,5.
- **Librerie aggiornate**: **Data Anchor** dalla 2.0.0.14 alla 2.0.0.17 (Enhanced Celestials 2 chiede almeno la 2.0.0.16).
- **Strumenti**: il controllo dei nomi segnala anche le mod dichiarate incompatibili tra loro.
- **Stato**: ✅ provata il 18/10/2026 (due avvii in 73–88 secondi, 28.612 ricette come nella 0.5.0; Enhanced Celestials 2 carica le lune e i nostri tre file senza errori) e rilasciata come pre-release `1.21.1-v0.5.1`. Quante lune di sangue escono davvero si conta nel mondo di prova, con il comando delle previsioni.
- **Problemi noti**: nuovo B32 (Enhanced Celestials 2 scrive in chat, a ogni ingresso nel mondo, che le impostazioni di traduzione non sono configurate; si corregge nella 0.5.2).

## 0.5.0 — 18/10/2026 · tappa 4 (pre-release di prova)

- **NeoForge**: 21.1.259 (invariato).
- **Mondo nuovo**: **sì**. Jaden's Nether Expansion rende il Nether più alto (soffitto a quota 192) e cambia la disposizione dei biomi; quasi tutte le mod nuove generano strutture o mob. Versione di prova: il mondo vero parte dalla 1.0.0.
- **Nether**: **Jaden's Nether Expansion** (biomi ridecorati e sottobiomi, mob, strutture, piante; librerie nuove **Elysium API** e **Lodestone**), **Moog's Nether Structures** (52 strutture fino a una mega-fortezza; la fortezza vanilla resta a YUNG's, opzione spenta di serie), **Nether Depths Upgrade** (alghe e pesci nei mari di lava, canna da pesca per la lava, accanto alla pesca di Starcatcher).
- **Esplorazione**: **Aures Farmers Structures** (costruzioni rurali a tema Farmer's Delight), **Better Archeology** (fossili, reperti, siti di scavo), **Nature's Compass** (bussola che trova i biomi), **Paragliders** (parapendio; genera statue).
- **Mob**: **Aquamirae** (boss e mob degli oceani ghiacciati; libreria nuova **Fragmentum**), **Creeper Overhaul** (creeper diversi per bioma).
- **Librerie aggiornate**: **Moog's Structure Lib** dalla 3.0.3 alla 3.4.2 (Moog's Nether Structures chiede almeno la 3.3.0).
- **Stato**: ✅ provata il 18/10/2026 (mondo nuovo; nel Nether alghe e pesci di lava presenti, biomi di Jaden's attivi; avvio in 73–81 secondi, 28.612 ricette) e rilasciata come pre-release `1.21.1-v0.5.0`. Generare il Nether nuovo è pesante (un rallentamento di 2,5 secondi entrando): conviene pregenerarlo con Chunky nel mondo di prova.
- **Problemi noti**: B28 (il gioco non partiva per la libreria vecchia) risolto prima del rilascio; B29–B31 minori (ricette e suoni di Jaden's, ricette delle finestre di Create in un secondo mondo, stalattite di Jaden's tra due chunk).

## 0.4.0 — 18/10/2026 · tappa 3 (pre-release di prova)

- **NeoForge**: 21.1.259 (invariato).
- **Mondo nuovo**: sì per provarla (Guard Villagers mette le guardie nei villaggi generati, Goblin Traders fa comparire i mercanti nel sottosuolo e nel Nether). Versione di prova: il mondo vero parte dalla 1.0.0.
- **Decorazione**: **Macaw's Roofs**, **Macaw's Paths and Pavings**, **Macaw's Bridges**, **Macaw's Windows**, **Diagonal Fences**, **Diagonal Walls**, **Diagonal Windows**, **Chimes**, **Exposure** (macchine fotografiche), **Every Compat** (varianti per tutti i legni delle mod: per ora con la config di serie, che crea migliaia di blocchi; la config ridotta arriva con la 0.6.0).
- **Villaggi**: **Guard Villagers**, **Goblin Traders** (CurseForge, con la libreria **Framework**).
- **Tech**: **Create: Copycats+**.
- **Documenti** (non cambiano il gioco): riorganizzati con codici a quattro cifre, documentazione (`docs/`) separata dai documenti di lavoro (`lavoro/`); regole in `AGENTS.md`.
- **Stato**: ✅ provata il 18/10/2026 (mondo nuovo, avvio pulito) e rilasciata come pre-release `1.21.1-v0.4.0`.
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

Versioni costruite a mano come file `.mrpack`, prima di passare a GitHub. Dettagli in [`../../ai-agents/stage/2026-10-16_pre-repo_pacchetti-mrpack/pacchetti-mrpack.md`](../../ai-agents/stage/2026-10-16_pre-repo_pacchetti-mrpack/pacchetti-mrpack.md).

- **0.2.3** (17/10): Just Enough Breeding e Professions, NetherPortalFix, SeasonHud, Smarter Farmers, Open Together, AllTheLeaks. Mai provata in gioco: rifatta come 0.2.3 del repository.
- **0.2.2** (17/10): XP Tome.
- **0.2.1** (17/10): cassaforte del Galeone tra le casse con gli artefatti.
- **0.2.0** (17/10): Regions Unexplored, Chunky, Clumps, Supplementaries, Handcrafted, Rechiseled, Construction Sticks (+ Lithostitched, Fusion, Moonlight).
- **0.1.1** (17/10): NeoForge da 21.1.262 a 21.1.259 per il "Connection lost" (B17); readme del datapack in minuscolo (B18). Provata: base del repository.
- **0.1.0** (16/10): primo pacchetto, 158 mod e resource pack più 36 librerie, config e datapack `matteo_tweaks`. Primo avvio il 17/10: parte in 32 secondi, poi "Connection lost" entrando nel mondo.
