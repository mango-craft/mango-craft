# Revisione 2026.10-02 — diario

Il piano è in [piano.md](piano.md). Le voci sono in ordine di tempo; la più recente è in fondo.

---

## 30/10/2026 — L'analisi

- **Agente:** claude-code (claude-opus-5-5)
- **Richiesta di Matteo:** «rianalizzare la struttura del repo, della documentazione e del codice: trova problemi, incoerenze ed eventuali sprechi».
- **Come:** tre analisi in parallelo, in sola lettura (documentazione; codice; dati, pack e peso), più controlli meccanici (link relativi, indici, codici, nomi delle schede, codici dei bug, percorsi citati). I punti principali riverificati a mano.
- **Risultato:** 63 rilievi senza doppioni; il rapporto è nello stage. I più importanti: owo-lib 0.12.15.6 già uscita (B17); memoria a 8 GB nel `README.md` contro 12 nella guida; Release che può taggare un ramo diverso da `main`; workflow di aggiunta che possono scrivere su `main` (successo il 18/10); `git *` permesso anche per i comandi che cancellano; `ci_commit.sh` lanciabile in locale; `refresh` della base dati 22 s di cui 21 persi; avvisi della base dati buttati; impronta del datapack che conta anche i readme.
- **Controllati e a posto:** link, indici, codici, schede citate, codici dei bug; `check_pack`, `check_ids`, generatori, base dati; metafile e inventario; workflow senza iniezione dagli input.
- **Correzione mia:** sul dump e su packwiz avevo raccomandato di togliere; rifatti i conti su richiesta di Matteo, ho corretto: il dump non pesa abbastanza da cambiarlo ora (e avrei tolto un'etichetta che i vasi usano), packwiz serve come verifica indipendente dell'indice e va solo messo in cache.
- **Matteo:** «applica tutto», con le raccomandazioni nuove. Piano scritto prima di cominciare.

## 30/10/2026 — Workflow, script, permessi

- **Agente:** claude-code (claude-opus-5-5). In parallelo un secondo agente corregge i documenti del pack (punto 3), in file diversi.
- **Workflow:** azione comune `.github/actions/packwiz/` (packwiz al commit fissato, Go 1.24.6 come dichiara il suo `go.mod`, cache). Controllo pack con permesso di sola lettura: rifà i file generati e fallisce se il commit non li aveva; non fa più commit. Aggiunta mod solo su `dev`, dall'ultimo commit del ramo, packwiz senza lo stdin del ciclo. Release solo da `main` (anche per un tag mandato da locale) e con l'indice confrontato con quello di packwiz prima di esportare.
- **Controlli:** `ci_pack.sh` è l'unica coda; `controllo_locale.sh` la lancia con `--locale` (indice da `packwiz_index.py`) e ora rifà anche l'inventario. La base dati segna ⚠️ gli avvisi che hanno trovato qualcosa e il controllo mostra solo quelli e i ❌: oggi 4 (2 pozioni dell'inventario che il gioco non ha; datapack cambiato dopo il dump, con le 3 ricette dei graticci di B47).
- **Base dati:** il ciclo quadratico era la riga che ricostruiva l'insieme dei nomi del gioco per ogni oggetto: 23,4 → 2 s. Firma delle fonti al posto delle date (si accorge anche dei file cancellati). Campi con più blocchi esplosi in `COLTURA_CUSTOM_BLOCCO` per il controllo dei nomi fantasma. Registro delle etichette di worldgen corretto (`worldgen/structure`): il Berserker resta comunque non confrontato, perché il dump non esporta quelle etichette (decisione: il dump non si cambia ora).
- **Impronta del datapack** in `scripts/comune.py`, solo `.json` e `.mcfunction`: l'impronta del dump del 29/10 era calcolata con la formula vecchia, quindi l'avviso «datapack cambiato» resta fino al prossimo dump (c'era già, per B47).
- **`dump_importa.py`**: se il dump ha errori o sezioni che quel dump non ha scritto (`meta.file`), non scrive niente.
- **Altri script:** `modrinth_resolve.py` (provato: `jei@19.70.0.467` trova la versione NeoForge, `2vmfujjt` è un id); `log_confronta.py` (latest contro 27/10: 342 firme nuove invece di 373); `release_notes.py`; `inventory.py` (verificato prima che tutti i 16 registri di etichette vanilla si scarichino); `vasi_verifica_jar.py` (21 terreni sostituiti in più); generatore dei vasi che cancella solo i file di vaso fuori dalla nostra cartella; `esamina.py` legge i jar con le funzioni dell'inventario (esame delle due mod della 0.7.3 identico).
- **Tolti:** `scripts/import_mrpack.py`, `1.21.1/data/modrinth-progetti.json`, `1.21.1/data/vasi/copertura.json` (nella storia: `90b7e8d`).
- **Prove:** `shellcheck` pulito, tutti gli script compilano, controllo locale verde in 2,7 s.

## 30/10/2026 — Contesto più leggero, versione 0.7.3

- **Agente:** claude-code (claude-opus-5-5)
- **`AGENTS.md`** riscritto con la stessa numerazione delle sezioni (gli altri documenti le citano): tabella dei livelli con il rimando ai README, schede con la regola nuova del nome, codici in una tabella più corta, sezione 5 a punti (istanze in `0101`, procedura di rilascio in `0201`), sezione 6 senza i passi che fa il workflow, sezione 7 con le eccezioni alla condizione di caricamento e la regola dei readme, sezione 8 senza ciò che sta in `ai-agents/README.md` e `0201`. Da 25.500 a 19.500 caratteri. La lettura della revisione aperta passa da `CLAUDE.md` ad `AGENTS.md`, che vale per tutti gli agenti.
- **`CLAUDE.md`**: restano l'import e la memoria automatica (il resto ripeteva `AGENTS.md`).
- **`0501`**: le 15 righe delle tappe fatte diventano una frase (le ripetono changelog e indice delle versioni); tappa 6.4 per owo-lib e NeoForge, numero da decidere; la 0.7.4 ha il contenuto deciso il 24/10 e il numero che dipende dalla 6.4. Da 11.100 a 4.800 caratteri.
- **`0303`**: una regola e un rimando per voce; vasi, mercato e lista nera in una voce sola («file generati»), le eccezioni alla condizione di caricamento in una. Rimessi dopo una rilettura tre dettagli che avevo tolto e sono regole (bacinella senza filtro, condizioni valutate sui nomi del gioco, «config estesa» di Relics spenta). Da 8.100 a 6.400 caratteri.
- **`pack.toml`** a 0.7.3 (regola nuova: la versione si alza all'apertura); l'indice non cambia.

## 30/10/2026 — Documenti del pack

- **Agente:** claude-code (claude-opus-5-5); le correzioni le ha fatte un secondo agente (stesso modello) nel suo perimetro, le ho rilette io prima del commit.
- **Fatto** (38 file): owo-lib «dipendenza dell'Aether, metafile a sé» in B17, schede `neoforge` e `aether`, `0502`, e nella vecchia voce 0.1.1 del changelog (corretta con la data); memoria a 12 GB nel `README.md`; script e file vecchi tolti dai rimandi; Regions Unexplored allineato al fatto del 24/10; riga di B47 con 5 celle; in `0403` tabella delle 36 librerie senza riga, Citadel tolta, CreativeCore 2.13.51, Jumbo Furnace tra le CurseForge, Iris e Fresh Animations di tipo release, slug corretti; in `0301` le librerie mancanti e niente legenda «⏳ Prevista»; conti dei vasi e del mercato tolti dai documenti vivi; README del datapack completo (Berserker, esperienza, mercato, terreni sostituiti) e `pack.mcmeta`; `0302` senza le parti vecchie; tema `accessori` e indice dei temi; `0503` senza gli argomenti chiusi (il n. 5 della sezione 4, citato altrove, non cambia); `0601` con la regola nuova; slug nella testata delle schede con un nome breve; Sparse Structures con i nomi del dump.
- **B15 unito a B35**: nei log dell'istanza dev dal 18/10 l'unico messaggio di questo tipo è `Block-attached entity at invalid position`, quasi sempre a y tra −45 e −58 come la «quota −50» di B15. Il log della 0.3.0, dove B15 contava 42 righe, non c'è più: è una deduzione, non un confronto diretto.
- **Lasciato com'è**: «non verificato» nel README del datapack per quando hanno effetto listini e mappa delle unità (nessuna fonte trovata); i numeri datati di `piante.md` e `analisi.md`.
- **Controlli**: controllo locale verde (indice rifatto per i readme e `pack.mcmeta`), link relativi tutti validi, nessun rimando a script o file tolti, schede citate tutte esistenti.

## 30/10/2026 — Le prove, revisione chiusa

- **Agente:** claude-code (claude-opus-5-5)
- **Push** dei tre commit su `dev` (7e37822..813e4b1). Controllo pack verde in 33 s senza commit: 23 s per compilare packwiz la prima volta (poi dalla cache), 3 s per i controlli.
- **Prova del fallimento**: ramo `prova-controllo` con un readme del datapack cambiato senza rifare l'indice, Controllo pack lanciato a mano: fallisce al passo «File generati aggiornati nel commit» con il messaggio che dice di lanciare il controllo locale. Ramo cancellato su GitHub e in locale (la sandbox protegge `.git/config`: l'avviso alla cancellazione è innocuo, il ramo non aveva voci lì).
- **Chiusa**: resta a Matteo il numero della tappa 6.4.
