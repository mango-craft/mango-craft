# Temi aperti — Minecraft 1.21.1

Gli argomenti del modpack non ancora affrontati, o rimasti a metà, e dove si trovano le mod in valutazione. Documento vivo: quando un tema entra in una tappa, il lavoro passa nel piano (`0501-piano.md`) e qui resta un rimando; quando è chiuso si toglie, con una riga nelle decisioni del file della versione (`versioni/`).

Ultimo aggiornamento: 24/10/2026.

## 1. Mod in valutazione

Non si ripetono qui, per non avere due elenchi da tenere allineati:
- **candidate**, ognuna con il momento in cui rivalutarla: `0601-mod-candidate.md`;
- **scartate**, con il motivo: `0602-mod-scartate.md`.

## 2. Argomenti non ancora trattati

| Tema | Cosa manca | Dove se ne parla già | Quando (proposta) |
|---|---|---|---|
| **Achievement e progressione** (nuovo, 19/10) | Schermata dei progressi più comoda, eventuale scheda di traguardi del pack | sezione 3; tema `../theme-knowledge/achievement.md`; ricerca in `versioni/v0.6.0.md` | Proposta aggiornata del 24/10: 0.7.6, ultima dei contenuti (`0501-piano.md`) |
| **Difficoltà** | Le fonti di difficoltà non sono mai state bilanciate insieme: World Tier ed Elites di Apotheosis, config di Cataclysm, buff permanenti di Cataclysm Delight, Born in Chaos (Krampus), lune di sangue. In più va deciso se tenere i due effetti nuovi della luna di sangue di Enhanced Celestials 2 (mostri più vicini, assedio di zombi ai villaggi) | `../docs/0302-config.md`, Impostazioni decise; readme delle lune nel datapack | Mondo di prova; la decisione sulle lune anche prima (proposta: 0.7.6) |
| **Tasti in conflitto** | Sophisticated e Traveler's aprono entrambi con B, Psi e Ars Nouveau usano entrambi C. I tasti stanno in `options.txt`, che il pack non porta (decisione del 19/10): vanno cambiati a mano, serve solo un elenco dei tasti consigliati | `0302`, Impostazioni decise | Prima del mondo vero |
| **Memoria e prestazioni** | Crash per memoria finita con 8 GB (B33); Every Compat pesa il 40% dei blocchi (B22). Decisione del 19/10: Every Compat **tiene tutti i blocchi**, quindi il costo resta. Misurato nel log (19/10): la generazione delle sue risorse pesa 2,4 secondi su un ricaricamento di oltre 35, e `RUN_ONCE` (scartato la sera del 19/10) avrebbe tolto solo quelli. La leva principale è la memoria dell'istanza (12 GB, B33); dopo va rimisurato tutto (avvio, memoria) e, se serve, valutate altre ottimizzazioni | `../docs/0402-bug-report.md`, B22 e B33 | 0.6.0, poi mondo di prova |
| **Aggiornamento delle mod prima della 1.0.0** | Le versioni sono quelle verificate tra il 16 e il 19/10. Non c'è un controllo automatico degli aggiornamenti: servirebbe un workflow che elenca le versioni nuove (senza installarle) e un giro di aggiornamenti prima del mondo vero. Ci rientra il ritorno all'ultimo NeoForge quando esce owo-lib 0.12.15.6 (B17) | `../docs/0303-note-tecniche.md`; `0502` (owo-lib) | Proposta del 21/10: 0.8.0, `0501-piano.md` |
| **Licenze da verificare** | La licenza di diverse mod (addon di Farmer's Delight, Let's Do, Botany Pots e altre) non è ancora stata controllata | Legenda di `../docs/0301-mod.md` | Proposta del 21/10: 0.8.0, `0501-piano.md` |
| **Slot degli accessori** | Ars Nouveau e Artifacts si contendono testa, collana e cintura (Curios); se gli slot diventano stretti si aumentano con un file nel datapack (formato verificato il 23/10: `data/<ns>/curios/slots/<slot>.json`, tema `accessori`). **Tre menu** dove indossare (Curios, menu standard di Accessories, menu dell'Aether; scoperto il 21/10): Matteo ha deciso di **lasciarli così** (21/10, `versioni/v0.6.0.md`); fatti nel tema `../theme-knowledge/accessori.md` | `0302`, Impostazioni decise | Mondo di prova |
| **Lingua del gioco** | Non è stato deciso se giocare in italiano né cosa fare con le mod senza traduzione italiana (quante siano non è stato contato). Enhanced Celestials 2 le traduzioni le scaricherebbe da internet: spente nella 0.5.2 | `0302` (traduzioni di EC2) | Da chiarire |
| **Fornaci: livelli e potenziamenti fuori dalle mod tech** (nuovo, 23/10) | Idea di Matteo: una progressione delle fornaci (livelli, accessori che le potenziano) che non passi da Create o Mekanism. Da valutare: mod che aggiungono fornaci a livelli o potenziamenti (candidate da cercare), oppure una nostra scala nel datapack sul modello della rarità dei terreni dei vasi (`../mod-knowledge/botany-pots/analisi.md`). **Ricerca fatta il 24/10**: senza mod si cambiano solo i tempi di cottura (i livelli sono blocchi); 🟢 Iron Furnaces (ricette dei livelli e dei potenziamenti riscrivibili nel datapack con i nostri materiali, velocità nella config), 🟡 FurnaceMk2 (un gradino in stile vanilla, con l'esperienza raccolta; scheda `../mod-knowledge/furnacemk2.md`), Iron Smelters e Jumbo Furnace (cottura in parallelo, complementare); le altre scartate (raddoppiano i minerali o sono beta) | Tema `../theme-knowledge/fornaci.md`; candidate in `0601`, scartate in `0602` | **Decisione di Matteo del 24/10: Iron Furnaces e FurnaceMk2 entrambe nel pack** (in punti diversi delle sue automazioni). **Nella 0.7.1** con Jumbo Furnace, ricette e valori originali (decisioni del 24/10, `0501-piano.md`, `versioni/v0.7.1.md`); in prova dal 24/10; le ricette dei livelli si possono riscrivere più avanti con la scala dei materiali degli strumenti |
| **Strumenti con materiali avanzati, a tappe** (nuovo, 23/10) | Idea di Matteo: come gestire a step la creazione degli strumenti con i materiali avanzati delle mod (Truly Modular, Aether, Undergarden, Twilight Forest, Mekanism…), così che ogni materiale sia una tappa e non un salto. Da valutare: quali materiali esistono, in che ordine si ottengono, cosa cambiare (ricette, parti di Truly Modular) | Tema `../theme-knowledge/strumenti.md` (fatti e valutazione del 23/10); strade e decisioni nella **sezione 5** | Indicazione di Matteo del 24/10: **in fondo, subito prima della progressione**; proposta aggiornata: 0.7.5 (`0501-piano.md`). I materiali che contano prima del mondo vero |
| **Accessori: potenziamento ed evoluzione** (nuovo, 23/10) | Idea di Matteo: gli accessori (Artifacts, Ars Nouveau, Curios) non crescono: valutare un modo per potenziarli o farli evolvere a tappe (ricette di aggiornamento nel datapack, mod dedicate). Si lega agli slot degli accessori qui sopra | Tema `../theme-knowledge/accessori.md`, sezione «Potenziamento ed evoluzione» (ricerca del 23/10); scheda `../mod-knowledge/artifacts.md`; strade e decisioni nella **sezione 6** | **Deciso da Matteo il 24/10: Relics + Reliquified Artifacts nella 0.7.0**, versione a parte (cambia molto il bottino): `0501-piano.md`, `versioni/v0.7.0.md`; in prova dal 24/10 |
| **Archeologia e reperti** (nuovo, 24/10) | Richiesta di Matteo: **gestire le tabelle di scavo** per valutare miglioramenti (analisi al momento della versione) e aggiungere alla toppa delle reliquie i **tesori delle casse di Better Archeology**, che né Relics né il nostro datapack vedono | Tema `../theme-knowledge/archeologia.md` (quadro del 24/10); scheda `../mod-knowledge/artifacts.md`; metodo data-driven (tabelle del bottino nella base dati) in `versioni/v0.7.4.md` | Decisione di Matteo del 24/10: **dopo le versioni già decise, sempre prima della progressione**; proposta aggiornata: 0.7.4 (`0501-piano.md`) |
| **Pozioni ed effetti** (nuovo, 24/10) | Richiesta di Matteo. **Analisi iniziale fatta il 24/10**: 350 effetti in 46 mod, 129 pozioni delle mod in 67 famiglie e 18 mod, sette sistemi oltre all'alambicco; doppioni (rapidità, resistenza, bagliore… in più mod); gli amuleti di Apotheosis rendono permanente qualsiasi pozione (lista nera vuota); Create automatizza le pozioni dell'alambicco ma non quelle di Born in Chaos. **Nella 0.7.2**: censimento nella base dati e lista nera degli amuleti (da decidere). Restano: automazione, doppioni, progressione | Tema `../theme-knowledge/pozioni.md` | 0.7.2 in lavorazione (`versioni/v0.7.2.md`) |
| **Guida del pack** | Ogni mod ha il suo manuale, ma il pack non ha una guida sua (come iniziare, cosa si collega a cosa). Si lega agli achievement | sezione 3 | Insieme agli achievement |

Restano nei loro documenti, perché sono già pianificati: densità delle strutture e Chunky (mondo di prova, `0501`), controlli durante la creazione del mondo e prove di compatibilità (`0502-prove-in-gioco.md`), parti del datapack (`versioni/v0.6.0.md`, `v0.6.1.md`, `v0.6.2.md`).

## 3. Achievement e progressione

Proposto dall'utente il 19/10/2026. Ricerca completa: `versioni/v0.6.0.md`, sezione 2; fatti sulle mod nella tema `../theme-knowledge/achievement.md`.

**Cosa c'è già**: circa 1.000–1.500 progressi veri nelle mod (più i 122 di Minecraft), sparsi in decine di schede. Alcuni alberi fanno già da guida (Create, Mekanism, Farmer's Delight, Aether, Ars Nouveau). Twilight Forest usa i progressi dei boss come lucchetto per aprire le zone: quelli non vanno mai toccati.

**Le strade, dalla più leggera**:
1. 🟢 **Una schermata dei progressi migliore** (una mod sola, lato client, da provare nell'istanza di prova):
   - **Reliable Advancements** (MIT): albero a tutta finestra con zoom; ha anche un editor in gioco per scrivere progressi;
   - **Lucid Advancements** (GPL-3.0): elenco con ricerca, filtri e percentuale di completamento, testi in italiano.
2. 🟢 **Una scheda "Mango Craft"** nel nostro datapack: 20–40 traguardi che collegano le mod tra loro (cucina, vasi, Create, magia, dimensioni), con piccole ricompense. Nessuna mod nuova; si scrive come il resto del datapack, con le condizioni di caricamento.
3. 🟡 **Un libro di missioni** (Questlog, Apache-2.0) solo se serve anche una guida del pack con pagine di testo (tema "Guida del pack" qui sopra).

Sconsigliate: FTB Quests (già scartata), Odyssey Quests (beta appena riscritta), le mod che danno bonus permanenti per ogni progresso (con migliaia di sblocchi di ricette sbilanciano il gioco).

**Da decidere**: se partire dalla schermata (1) e quale delle due, e se e quando scrivere la scheda del pack (2). Le mod sono tra le candidate (`0601-mod-candidate.md`).

## 4. Decisioni aperte che valgono per più versioni

Le decisioni che riguardano solo una versione stanno nel suo file (`versioni/`, sezione Decisioni, "Da decidere"). Qui quelle che attraversano più versioni; quando una si chiude, la riga passa nelle Decisioni della versione che la applica e si toglie da qui.

| # | Decisione | Proposta | Dove si applica |
|---|---|---|---|
| 1 | Effetti nuovi della luna di sangue di Enhanced Celestials 2 (mostri più vicini, assedio di zombi ai villaggi): tenerli? Oggi attivi | da decidere, anche prima del mondo di prova | datapack delle lune (scheda `../mod-knowledge/enhanced-celestials-2.md`) |
| 2 | Achievement: partire dalla schermata dei progressi (Reliable o Lucid) e se e quando scrivere la scheda "Mango Craft" nel datapack | 🟢 una mod per la schermata, poi la scheda | sezione 3; tema `../theme-knowledge/achievement.md` |
| 3 | Tasti in conflitto (B, C): elenco dei tasti consigliati | da fare a mano nelle opzioni | prima del mondo vero |
| 4 | Lingua del gioco: italiano o no, e che fare con le mod senza traduzione | da chiarire | prima del mondo vero |
| 6 | Strumenti a tappe: quali gradini e quali materiali di Truly Modular scrivere a mano | 🟢 prima la tabella dei materiali letta in gioco, poi i gradini | sezione 5; i materiali scritti **prima del mondo vero** |
| 7 | Accessori: artefatti di «livello II» nel datapack, oppure Relics + Reliquified Artifacts | ✅ **deciso da Matteo il 24/10: Relics + Reliquified Artifacts**, nella 0.7.0 (la prova si fa nell'istanza di prova, come per ogni 0.x) | sezione 6; `versioni/v0.7.0.md` |
| 5 | **Prove di uscita della 1.0.0** (deciso da Matteo il 19/10/2026, si applica alla 1.0.0): le tappe 0.x seguono le prove di uscita rapide di `AGENTS.md` (sezione 5); la 1.0.0 ha una soglia più alta, perché dopo la creazione del mondo vero alcune cose non si correggono più. Per uscire servono: **(a)** fatte tutte le prove della sezione «Mondo di prova» di `0502-prove-in-gioco.md`; **(b)** definitive e provate in un mondo di prova le cose che non si cambiano a mondo creato: mod che generano mondo o strutture (⚠️ in `../docs/0301-mod.md`), Sparse Structures completo, varianti e legni di Every Compat, Jaden's, Chunky con la config finale, e le decisioni dei punti 3 e 4 qui sopra; **(c)** nessun problema di effetto «alto» (crash) aperto nel bug report, quindi B33 va riprovato con 12 GB. Un problema «medio» o «basso» non blocca se non mette a rischio il mondo | già deciso | 1.0.0 |

## 5. Strumenti con materiali avanzati, a tappe

Idea di Matteo del 23/10/2026. Fatti verificati e ricerca su Truly Modular nel tema `../theme-knowledge/strumenti.md` (grezzo: `../../ai-agents/stage/2026-10-23_truly-modular-materiali/`). Qui le strade e cosa decidere.

**Cosa c'è già**: Truly Modular crea da solo **18 materiali** dagli strumenti delle mod (Aether, Deep Aether, Twilight Forest, Undergarden, Deeper and Darker, Cataclysm, Unusual End, Psi, Cognition), con statistiche coerenti con quelle vanilla; le forgiature delle mod (es. diamante → resonarium) diventano potenziamenti delle parti modulari. Le tappe di oggi le danno dimensioni e boss, non i livelli di scavo.

**Le strade**:
1. 🟢 **Tabella dei materiali**: statistiche vere lette in gioco (`/miapi material <id>`) e momento in cui ogni materiale si ottiene; da lì i gradini. Si può riusare il metodo dei vasi (regole in CSV → generatore di file).
2. 🟡 **Materiali scritti a mano** nel datapack: correggere le stranezze (Undergarden più duro della netherite, zanite nel gruppo «pietra»), aggiungere i mancanti (fiery, iesnium), fissare gli id. I cancelli si fanno con un progresso richiesto dal materiale (es. aver battuto un boss).
3. 🟡 **Cancelli nelle ricette** degli strumenti non modulari: solo se non si punta tutto su Truly Modular.
- 🔴 Cambiare i livelli di scavo dei blocchi: tocca il mondo di tutte le mod.

**Prima cosa da fare**: le prove in gioco elencate nel tema (statistiche di 3–4 materiali, skyroot, un potenziamento in forgiatura, un materiale di prova dal datapack).

**Quando**: proposta aggiornata del 24/10: 0.7.5, subito prima della progressione (`0501-piano.md`). I materiali che contano vanno scritti **prima del mondo vero**: gli id dei materiali generati possono cambiare con un aggiornamento della mod. Prima di scriverli va adattata la regola delle condizioni di caricamento (`AGENTS.md`, sezione 7): per questi file vale `load_condition` di Truly Modular.

## 6. Accessori: potenziamento ed evoluzione

Idea di Matteo del 23/10/2026. Fatti verificati nel tema `../theme-knowledge/accessori.md` (sezione «Potenziamento ed evoluzione») e nella scheda `../mod-knowledge/artifacts.md` (grezzo: `../../ai-agents/stage/2026-10-23_accessori-evoluzione/`). Qui le strade e cosa decidere.

**Cosa c'è già**: catene «base → migliore» in Ars Nouveau, Twilight Forest, Aether, Deep Aether, Unusual End e negli zaini; gli artefatti di Artifacts non hanno livelli; Apotheosis non tocca gli accessori.

**Le strade** (la 1 e la 3 sono alternative: con Reliquified Artifacts gli artefatti sono rifatti da capo, e non è verificato se i dati di Artifacts valgono ancora):
1. 🟢 **Artefatti di «livello II» nel datapack**: la stessa copia con valori più alti (le abilità sono dati dell'oggetto), ottenuta con l'infusione di Apothic Enchanting, una ricetta o le casse dei boss. Pilota con 3–5 artefatti. In più, ricette di passaggio dove esistono già «fratelli» più forti (anelli e pendenti dell'Aether).
2. 🟡 **Attributi o slot in più** sugli accessori potenziati (`curios:attribute_modifiers`).
3. 🟡 **Relics + Reliquified Artifacts** (mod candidate, `0601-mod-candidate.md`): gli artefatti salgono di livello usandoli. Sono in All The Mods 10 e Craftoria; però sono in beta, in Craftoria un aggiornamento ha azzerato i livelli, e bloccano Artifacts alla 13.2.5. Casse (`neoforge:add_table`) e slot di Accessories (`remove` nelle etichette) si sistemano col datapack. Solo dopo una prova in un'istanza a parte; dopo la 1.0.0, versioni ferme.
- 🔴 More Relics, L2 Artifacts, Tiered More.

**Prima cosa da fare**: le prove con `/give` (comandi nel grezzo, sezione 5).

**Decisione del 24/10**: Matteo sceglie la strada 3, **Relics + Reliquified Artifacts**, in una versione a parte, la **0.7.0** (`0501-piano.md`, `versioni/v0.7.0.md`): cambia molto, soprattutto nelle tabelle del bottino. Le ricette di passaggio per gli accessori delle altre mod (anelli e pendenti dell'Aether…) non dipendono da Artifacts e restano possibili.

