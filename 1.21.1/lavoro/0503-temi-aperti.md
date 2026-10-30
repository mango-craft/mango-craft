# Temi aperti — Minecraft 1.21.1

Gli argomenti del modpack non ancora affrontati, o rimasti a metà, e dove si trovano le mod in valutazione. Documento vivo: quando un tema entra in una tappa, il lavoro passa nel piano (`0501-piano.md`) e qui resta un rimando; quando è chiuso si toglie, con una riga nelle decisioni del file della versione (`versioni/`).

Ultimo aggiornamento: 30/10/2026.

## 1. Mod in valutazione

Non si ripetono qui, per non avere due elenchi da tenere allineati:
- **candidate**, ognuna con il momento in cui rivalutarla: `0601-mod-candidate.md`;
- **scartate**, con il motivo: `0602-mod-scartate.md`.

## 2. Argomenti non ancora trattati

| Tema | Cosa manca | Dove se ne parla già | Quando (proposta) |
|---|---|---|---|
| **Achievement e progressione** (nuovo, 19/10) | Schermata dei progressi più comoda, eventuale scheda di traguardi del pack | sezione 3; tema `../theme-knowledge/achievement.md`; ricerca in `versioni/v0.6.0.md` | Tema della **0.8** (indicazione di Matteo del 25/10, `0501-piano.md`), dopo i contenuti delle 0.7.x |
| **Difficoltà** | Le fonti di difficoltà non sono mai state bilanciate insieme: World Tier ed Elites di Apotheosis, config di Cataclysm, buff permanenti di Cataclysm Delight, Born in Chaos (Krampus), lune di sangue (gli effetti nuovi della luna: sezione 4, n. 1) | `../docs/0302-config.md`, Impostazioni decise; readme delle lune nel datapack | Mondo di prova |
| **Memoria e prestazioni** | Crash per memoria finita con 8 GB (B33); Every Compat pesa il 40% dei blocchi e li tiene tutti (B22, decisione del 19/10). La leva è la memoria dell'istanza (12 GB): riprovare B33 con 12 GB, poi rimisurare avvio e memoria e, se serve, valutare altre ottimizzazioni | `../docs/0402-bug-report.md`, B22 e B33 | Mondo di prova |
| **Aggiornamento delle mod prima del mondo vero** | Le versioni sono quelle verificate tra il 16 e il 19/10 e quelle delle mod entrate dopo. Non c'è un controllo automatico degli aggiornamenti: servirebbe un workflow che elenca le versioni nuove (senza installarle) e un giro di aggiornamenti prima del mondo vero. owo-lib e l'ultimo NeoForge invece hanno una versione piccola a sé, dopo la 0.7.3 (decisione del 30/10, B17) | `../docs/0303-note-tecniche.md`; `0502` (owo-lib) | Fase senza numero, dopo i contenuti e prima del mondo di prova (indicazione di Matteo del 25/10, `0501-piano.md`) |
| **Licenze da verificare** | La licenza di diverse mod (addon di Farmer's Delight, Let's Do, Botany Pots e altre) non è ancora stata controllata | Legenda di `../docs/0301-mod.md` | Fase senza numero, con gli aggiornamenti (indicazione di Matteo del 25/10, `0501-piano.md`) |
| **Strumenti con materiali avanzati, a tappe** (nuovo, 23/10) | Idea di Matteo: come gestire a step la creazione degli strumenti con i materiali avanzati delle mod (Truly Modular, Aether, Undergarden, Twilight Forest, Mekanism…), così che ogni materiale sia una tappa e non un salto. Da valutare: quali materiali esistono, in che ordine si ottengono, cosa cambiare (ricette, parti di Truly Modular) | Tema `../theme-knowledge/strumenti.md` (fatti e valutazione del 23/10); strade e decisioni nella **sezione 5** | Da esplorare e decidere (Matteo, 25/10): una 0.7.x senza numero fisso, prima della progressione (`0501-piano.md`). I materiali che contano prima del mondo vero |
| **Pozioni ed effetti** (nuovo, 24/10) | Fatti nella 0.7.2: censimento nella base dati e lista nera degli amuleti di Apotheosis. Restano: automazione (Create automatizza l'alambicco ma non i sistemi delle mod), doppioni tra le mod, progressione | Tema `../theme-knowledge/pozioni.md` | Da decidere |
| **Guida del pack** | Ogni mod ha il suo manuale, ma il pack non ha una guida sua (come iniziare, cosa si collega a cosa). Si lega agli achievement | sezione 3 | Insieme agli achievement |

**Passati in una versione** (qui solo il rimando; il lavoro è nei file di `versioni/`): fornaci a livelli → 0.7.1; accessori che crescono → 0.7.0 (sezione 6); lista nera degli amuleti → 0.7.2; computer → 0.7.3, in lavorazione; archeologia e reperti → 0.7.4, pianificata.

Restano nei loro documenti, perché sono già pianificati: densità delle strutture e Chunky (mondo di prova, `0501`), controlli durante la creazione del mondo e prove di compatibilità (`0502-prove-in-gioco.md`).

## 3. Achievement e progressione

Proposto dall'utente il 19/10/2026. Ricerca completa: `versioni/v0.6.0.md`, sezione 2; fatti sulle mod nel tema `../theme-knowledge/achievement.md`.

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

Le decisioni che riguardano solo una versione stanno nel suo file (`versioni/`, sezione Decisioni, "Da decidere"). Qui quelle che attraversano più versioni, **e solo qui**: gli altri documenti ci rimandano. Quando una si chiude, la riga passa nelle Decisioni della versione che la applica e si toglie da qui; i numeri non cambiano (altri documenti citano il n. 5).

| # | Decisione | Proposta | Dove si applica |
|---|---|---|---|
| 1 | Effetti nuovi della luna di sangue di Enhanced Celestials 2 (mostri che compaiono più vicini, assedio di zombi ai villaggi): tenerli? Oggi attivi | da decidere, anche prima del mondo di prova (proposta: con la progressione, 0.8) | datapack delle lune (scheda `../mod-knowledge/enhanced-celestials-2.md`) |
| 2 | Achievement: partire dalla schermata dei progressi (Reliable o Lucid) e se e quando scrivere la scheda "Mango Craft" nel datapack | 🟢 una mod per la schermata, poi la scheda | sezione 3; tema `../theme-knowledge/achievement.md` |
| 3 | Tasti in conflitto: Sophisticated e Traveler's aprono entrambi con **B**, Psi e Ars Nouveau usano entrambi **C**. I tasti stanno in `options.txt`, che il pack non porta (decisione del 19/10): si cambiano a mano (Controlling aiuta a trovare i conflitti) | un elenco dei tasti consigliati nei documenti | prima del mondo vero |
| 4 | Lingua del gioco: italiano o no, e che fare con le mod senza traduzione italiana (quante siano non è stato contato). Enhanced Celestials 2 le traduzioni le scaricherebbe da internet: spente nella 0.5.2 (`../docs/0302-config.md`) | da chiarire | prima del mondo vero |
| 5 | **Soglia del mondo vero** (deciso da Matteo il 19/10/2026 per la 1.0.0; dal 25/10/2026 vale per la versione con cui si crea il mondo vero, che arriva prima della 1.0.0): le altre versioni seguono le prove di uscita rapide di `AGENTS.md` (sezione 5); la versione del mondo vero ha una soglia più alta, perché dopo la creazione del mondo vero alcune cose non si correggono più. Per uscire servono: **(a)** fatte tutte le prove della sezione «Mondo di prova» di `0502-prove-in-gioco.md`; **(b)** definitive e provate in un mondo di prova le cose che non si cambiano a mondo creato: mod che generano mondo o strutture (⚠️ in `../docs/0301-mod.md`), Sparse Structures completo, varianti e legni di Every Compat, Jaden's, Chunky con la config finale, e le decisioni dei punti 3 e 4 qui sopra; **(c)** nessun problema di effetto «alto» (crash) aperto nel bug report, quindi B33 va riprovato con 12 GB. Un problema «medio» o «basso» non blocca se non mette a rischio il mondo | già deciso | versione del mondo vero |
| 6 | Strumenti a tappe: quali gradini e quali materiali di Truly Modular scrivere a mano | 🟢 prima la tabella dei materiali letta in gioco, poi i gradini | sezione 5; i materiali scritti **prima del mondo vero** |
| 7 | Slot degli accessori: Ars Nouveau e Artifacts si contendono testa, collana e cintura di Curios (1 slot ciascuno). Se diventano stretti si aumentano con un file nel datapack (formato verificato il 23/10: `data/<ns>/curios/slots/<slot>.json`, tema `../theme-knowledge/accessori.md`). I tre menu dove indossare oggetti restano (decisione del 21/10, `versioni/v0.6.0.md`) | solo se servono, dopo averli usati | mondo di prova |

## 5. Strumenti con materiali avanzati, a tappe

Idea di Matteo del 23/10/2026. Fatti verificati e ricerca su Truly Modular nel tema `../theme-knowledge/strumenti.md` (grezzo: `../../ai-agents/archivio/2026-10-23_truly-modular-materiali/`). Qui le strade e cosa decidere.

**Cosa c'è già**: Truly Modular crea da solo **18 materiali** dagli strumenti delle mod (Aether, Deep Aether, Twilight Forest, Undergarden, Deeper and Darker, Cataclysm, Unusual End, Psi, Cognition), con statistiche coerenti con quelle vanilla; le forgiature delle mod (es. diamante → resonarium) diventano potenziamenti delle parti modulari. Le tappe di oggi le danno dimensioni e boss, non i livelli di scavo.

**Le strade**:
1. 🟢 **Tabella dei materiali**: statistiche vere lette in gioco (`/miapi material <id>`) e momento in cui ogni materiale si ottiene; da lì i gradini. Si può riusare il metodo dei vasi (regole in CSV → generatore di file).
2. 🟡 **Materiali scritti a mano** nel datapack: correggere le stranezze (Undergarden più duro della netherite, zanite nel gruppo «pietra»), aggiungere i mancanti (fiery, iesnium), fissare gli id. I cancelli si fanno con un progresso richiesto dal materiale (es. aver battuto un boss).
3. 🟡 **Cancelli nelle ricette** degli strumenti non modulari: solo se non si punta tutto su Truly Modular.
- 🔴 Cambiare i livelli di scavo dei blocchi: tocca il mondo di tutte le mod.

**Prima cosa da fare**: le prove in gioco elencate nel tema (statistiche di 3–4 materiali, skyroot, un potenziamento in forgiatura, un materiale di prova dal datapack).

**Quando**: una 0.7.x da esplorare e decidere (Matteo, 25/10), prima della progressione (`0501-piano.md`). La stessa scala dei materiali può servire alle ricette dei livelli delle fornaci (Iron Furnaces, `../theme-knowledge/fornaci.md`) e, se si vorrà, a quelle dei computer. I materiali che contano vanno scritti **prima del mondo vero**: gli id dei materiali generati possono cambiare con un aggiornamento della mod. Prima di scriverli va adattata la regola delle condizioni di caricamento (`AGENTS.md`, sezione 7): per questi file vale `load_condition` di Truly Modular.

## 6. Accessori: potenziamento ed evoluzione

Chiuso il 24/10/2026: Matteo ha scelto **Relics + Reliquified Artifacts**, nel pack dalla 0.7.0 (`versioni/v0.7.0.md`). Le strade valutate e i fatti sono nel tema `../theme-knowledge/accessori.md`.
