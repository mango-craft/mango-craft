# Changelog — Mango Craft 1.21.1

_Documento vivo: una voce nuova per ogni versione, in cima._

Una voce per ogni versione, dalla più recente. Ogni voce dice:
- **Stato**: 🔧 in lavorazione (e in prova) sul ramo `dev` · ✅ provata e rilasciata (tag `1.21.1-vX.Y.Z`; le 0.x sono pre-release, e da una di queste partirà il mondo vero);
- **NeoForge** da impostare a mano in Prism e se serve un **mondo nuovo**;
- cosa cambia: mod, datapack, config;
- **Problemi noti**: i codici del [bug report](0402-bug-report.md) comparsi o risolti in quella versione.

La voce di una versione diventa anche la nota della sua release su GitHub.

## 0.7.5 — in lavorazione · archeologia e reperti

- **NeoForge**: 21.1.265 (invariato).
- **Mondo nuovo**: non serve.
- **Stato**: 🔧 in lavorazione sul ramo `dev`.

## 0.7.4 — 30/10/2026 · piattaforma (pre-release di prova)

- **NeoForge**: **21.1.265** (prima 21.1.259): da cambiare a mano in Prism prima dell'avvio.
- **Mondo nuovo**: non serve. Versione di prova: non è la versione del mondo vero.
- **Librerie aggiornate**: **owo-lib** 0.12.15.6 (dipendenza dell'Aether: corregge B17, il «Connection lost» con i NeoForge recenti), **Forgified Fabric API** 2.3.6 (vuole NeoForge 21.1.262 o più recente), **Puzzles Lib** 21.1.66.
- **Datapack, funzioni di prova**: `/function matteo_tweaks:test/releases/v0.7.4/…` (portale dell'Aether, spada con Saccheggio III).
- **Stato**: ✅ provata il 30/10/2026 (avvio con NeoForge 21.1.265, mondo e Aether senza disconnessioni, Saccheggio, shader con Iris; dump con tutti i controlli passati; log confrontato con quello della 0.7.3, nessun errore nuovo grave) e rilasciata come pre-release `1.21.1-v0.7.4`.
- **Problemi noti**: **B17 risolto** (con i NeoForge recenti non si viene più disconnessi entrando nel mondo). Nuovo B48, minore: Aure's Farmer's Structures genera tre strutture pensate per Aquaculture, che non abbiamo, e il gioco ne salta tartarughe e oggetti. Qualche messaggio innocuo in più in B14.

## 0.7.3 — 30/10/2026 · computer (pre-release di prova)

- **NeoForge**: 21.1.259 (invariato).
- **Mondo nuovo**: non serve; le case del Computer Scientist compaiono solo nei chunk nuovi. Versione di prova: non è la versione del mondo vero.

- **Datapack, vasi (correzione B47)**: le 3 colture dei graticci di Bountiful Fares (sambuco, lapisberry, frutto della passione) ora si caricano (aspetto del graticcio `bountifulfares:trellis`); tolta la coltura degli endstone sprouts warped, che Unusual End non registra. Trovato con il dump del gioco: dalla 0.6.1 il gioco le saltava in silenzio.
- **Strumenti**: dump del gioco nel **formato 2** (nomi registrati, ricette caricate, etichette finali, tabelle del bottino, insiemi di strutture); la base dati confronta i nostri file con il gioco (ricette, tag, tabelle), il controllo dei nomi avvisa per i nomi che il gioco non registra; l'importatore segna a quale datapack si riferisce il dump.
- **Mod nuove**: **CC: Tweaked** 1.120.2 (computer programmabili in Lua: computer, monitor, tartarughe, modem; leggono inventari, serbatoi e batterie di tutte le mod e le macchine di Create e Mekanism) e **Advanced Peripherals** 0.8.2a (periferiche che collegano i computer al giocatore e al mondo: Player Detector, Chat Box, Inventory Manager, Geo Scanner, occhiali smart, automi; legge bacino e serbatoi di Create). Entrambe alpha; nessuna libreria nuova; config di serie. ⚠️ Advanced Peripherals aggiunge ai villaggi le **case del Computer Scientist**, con il suo mestiere.
- **Datapack, funzioni di prova**: `/function matteo_tweaks:test/releases/v0.7.3/…` dà gli oggetti delle prove dei computer e, con un clic in chat, copia le righe di Lua da incollare nel computer.
- **Stato**: ✅ provata il 30/10/2026 (avvio e mondo; computer, Player Detector, Chat Box con modem e cavi, bacino di Create verificati da Matteo con le funzioni di prova; dump del gioco con tutti i controlli passati; log confrontato con quello del 29/10, nessun errore nuovo grave) e rilasciata come pre-release `1.21.1-v0.7.3`.
- **Problemi noti**: B47 risolto (le 3 colture dei graticci si caricano). Nessun problema nuovo: qualche messaggio innocuo in più in B14 (3 ricette del manuale di Advanced Peripherals per mod che non abbiamo); B46 ancora presente.

## 0.7.2 — 26/10/2026 · fornaci e pozioni (pre-release di prova)

Contiene anche la **0.7.1** (fornaci), che non esce a sé: Matteo prova le due insieme (24/10/2026).

- **NeoForge**: 21.1.259 (invariato).
- **Mondo nuovo**: non serve. Versione di prova: non è la versione del mondo vero.
- **Mod nuove (0.7.1)**: **Iron Furnaces** 4.3.2 (fornaci dal rame alla netherite e arcobaleno, potenziamenti sul posto, accessori compresi generatore, fabbrica e riscaldatore), **FurnaceMk2** 0.1.11 con la libreria **VapourWare** 0.2.37 (una fornace migliorata con tre nuclei e l'esperienza raccolta in un cristallo), **Jumbo Furnace** 5.0.0.9 da CurseForge (cubo di 27 fornaci che cuoce molte cose insieme). Ricette e valori originali.
- **Mod nuove (0.7.2)**: **KubeJS** 2101.7.2 con le librerie **Rhino** e **Better Advanced Tooltips**, solo per il comando `/mango_dump`: scrive i dati del gioco (effetti, pozioni, alambicco, cibi) per la base dati del repository; non cambia niente in gioco. Better Advanced Tooltips mostra etichette e componenti degli oggetti nei tooltip con F3+H.
- **Datapack, amuleti di pozione (0.7.2)**: una lista nera per gli amuleti di Apotheosis, cioè le pozioni che non possono diventare un effetto continuo (permanente con l'amuleto infrangibile): **Flying** (Apothic Attributes, volo creativo), **Weightlessness** (Reactive), **Acidity** e **Stupor** (Bountiful Fares), **Serenity** (Unusual End), con le varianti lunghe e forti (11 pozioni). Tutte le altre, comprese quelle del gioco base, fanno ancora l'amuleto.
- **Datapack, funzioni di prova (0.7.2)**: `/function matteo_tweaks:test/releases/v0.7.2/…` dà in un colpo gli oggetti delle prove di uscita e scrive in chat cosa controllare.
- **Strumenti (0.7.2)**: l'inventario ricava i nomi veri delle pozioni delle mod; effetti e pozioni entrano nella base dati (350 effetti e 129 pozioni delle mod), insieme ai dati del gioco quando c'è un dump (`scripts/dump_importa.py`): effetti di ogni pozione, categoria degli effetti, ricette dell'alambicco, effetti dei cibi, e quali pozioni fanno davvero un amuleto. Primo dump il 26/10: 376 effetti, 173 pozioni (139 possono fare l'amuleto), 963 miscele dell'alambicco, 1.584 oggetti con effetti. La lista nera la scrive `scripts/pozioni_genera.py` da una regola in CSV, e il controllo di ogni workflow verifica che file e regola coincidano.
- **Invariato**: config (salvo lo script di KubeJS, nuovo).
- **Stato**: ✅ provata il 25 e 26/10/2026 (avvio e mondo; fornaci, lista nera degli amuleti e funzioni di prova verificate da Matteo; due dump del gioco con «errori: 0»; log confrontati con quello della 0.7.0, nessun errore nuovo grave) e rilasciata come pre-release `1.21.1-v0.7.2`.
- **Problemi noti**: B45 (lo script del dump non si caricava) comparso e risolto nella prova; nuovo B46 (Copycats+ ed EMI dopo un `/reload`, minore); B14 con qualche messaggio innocuo in più dovuto a KubeJS. Nessun errore delle fornaci, della lista nera o delle funzioni di prova.

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

- **NeoForge**: 21.1.259. Non usare la 21.1.262 o successive (qui c'era «21.1.261», che non è mai uscita: corretto il 30/10/2026): owo-lib 0.12.15.5 (dipendenza dell'Aether; corretto il 30/10/2026: non è incluso nel suo jar) fa cadere la connessione all'ingresso nel mondo. Si aggiornerà quando esce owo-lib 0.12.15.6.
- **Mondo nuovo**: non serve (è la stessa versione già provata).
- **Contenuto**: identico al pacchetto `modpack-matteo-0.1.1.mrpack` provato in gioco: 193 file di mod e librerie da Modrinth, il resource pack Fresh Animations (da attivare a mano nel gioco), le configurazioni (`almostunified/tags.json`, `sparsestructures.json5`) e il datapack `matteo_tweaks` caricato da Paxi.
- **Mod solo CurseForge** (5): The Twilight Forest 4.8.3345, Ars Elemental 0.7.10.4, Roaster's Delight 1.0.0.1, Spice of Life: Carrot Edition 1.16.6, BotanyPotsAdditions 1.1.0. Le scarica l'installer; quelle con distribuzione bloccata vanno scaricate a mano una volta (l'installer mostra pagina e percorso).
- **Novità tecnica**: prima versione gestita con packwiz su GitHub. Serve a verificare il nuovo sistema su una versione che già funziona.
- **Stato**: ✅ provata il 17/10 come pacchetto `.mrpack` e il 18/10 dal repository, release `1.21.1-v0.1.1`.
- **Problemi noti**: B01–B05, B07–B14, B16 (vedi bug report); B17 aggirato fissando NeoForge 21.1.259; B18 risolto in questa versione; B19 risolto già nella 0.1.0.

---

## Prima del repository (pacchetti `.mrpack`, 16–17/10/2026)

Versioni costruite a mano come file `.mrpack`, prima di passare a GitHub. Dettagli in [`../../ai-agents/archivio/2026-10-16_pre-repo_pacchetti-mrpack/pacchetti-mrpack.md`](../../ai-agents/archivio/2026-10-16_pre-repo_pacchetti-mrpack/pacchetti-mrpack.md).

- **0.2.3** (17/10): Just Enough Breeding e Professions, NetherPortalFix, SeasonHud, Smarter Farmers, Open Together, AllTheLeaks. Mai provata in gioco: rifatta come 0.2.3 del repository.
- **0.2.2** (17/10): XP Tome.
- **0.2.1** (17/10): cassaforte del Galeone tra le casse con gli artefatti.
- **0.2.0** (17/10): Regions Unexplored, Chunky, Clumps, Supplementaries, Handcrafted, Rechiseled, Construction Sticks (+ Lithostitched, Fusion, Moonlight).
- **0.1.1** (17/10): NeoForge da 21.1.262 a 21.1.259 per il "Connection lost" (B17); readme del datapack in minuscolo (B18). Provata: base del repository.
- **0.1.0** (16/10): primo pacchetto, 158 mod e resource pack più 36 librerie, config e datapack `matteo_tweaks`. Primo avvio il 17/10: parte in 32 secondi, poi "Connection lost" entrando nel mondo.
