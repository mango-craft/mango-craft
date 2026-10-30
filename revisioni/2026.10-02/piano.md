# Revisione 2026.10-02 — Pulizia dopo l'analisi del 30/10

**Stato**: 🔧 aperta il 30/10/2026. Il diario è in [diario.md](diario.md).

## 1. Obiettivo

Il 30/10/2026 Matteo chiede di rianalizzare struttura, documentazione e codice e di trovare problemi, incoerenze e sprechi. L'analisi (tre analisi in parallelo, controlli meccanici, verifica dei punti principali) ha trovato 63 rilievi; il rapporto completo è rimasto sul PC, nello stage. Questa revisione li applica, tranne ciò che cambia il gioco, che va in una versione del pack. Ogni punto del lavoro qui sotto dice cosa non andava, così la revisione si regge da sola.

## 2. Decisioni

- **30/10/2026** — Matteo: «applica tutto», con le raccomandazioni riviste dopo la spiegazione di dump e packwiz.
- **30/10/2026** — **I workflow non fanno più commit da soli, tranne quelli di aggiunta mod.** Il Controllo pack controlla e basta: rifà indice, inventario e `controllo.md` e fallisce se sono diversi da quelli del commit. Il controllo locale li scrive prima del push, inventario compreso (`inventory.py` gira in locale e scarica solo i jar cambiati: provato il 30/10, una mod Modrinth e una CurseForge in mezzo secondo, risultato identico al workflow). I workflow di aggiunta mod tengono il loro commit, solo su `dev`; Release crea solo il tag, solo da `main`.
- **30/10/2026** — **packwiz resta nel Controllo pack** come verifica indipendente dell'indice che scrive `packwiz_index.py` in locale, ma compilato una volta e riusato (cache), con Go fissato.
- **30/10/2026** — **owo-lib e NeoForge**: owo-lib 0.12.15.6 per NeoForge 1.21.1 è uscita il 16/10 e corregge il problema di rete dei NeoForge recenti (B17). Si aggiorna in una versione piccola a sé, subito dopo la 0.7.3, e lì si passa all'ultimo NeoForge 21.1.x. Il numero della versione lo decide Matteo.
- **30/10/2026** — **Permessi**: i comandi git che cancellano chiedono conferma (`.claude/settings.json`).
- **30/10/2026** — **Dump**: niente da cambiare ora. Se si tocca comunque lo script del dump, si tolgono i valori delle etichette «mineable» (3,7 MB, nessun controllo li usa); `minecraft:mushroom_grow_block` e le altre restano, perché le regole dei vasi le usano.
- **30/10/2026** — **Versione in `pack.toml`**: si alza quando la versione si apre, non al rilascio (com'era dalla 0.7.0 alla 0.7.2). La 0.7.3 passa a 0.7.3 subito.
- **30/10/2026** — **Mod approvate**: restano in `0601` con «approvata, nella vX.Y.Z» finché non entrano nel pack; `0301` elenca solo ciò che c'è.
- **30/10/2026** — **Nomi delle schede**: lo slug del metafile oppure un nome breve leggibile, con lo slug nella testata (non si rinominano le cinque schede che non hanno lo slug).
- **30/10/2026** — **Readme del datapack**: uno per parte (la cartella principale di ogni lavoro), non uno per ogni sottocartella.

## 3. Lavoro

1. ✅ **Workflow e controlli**
   - Controllo pack solo di controllo, con permesso di sola lettura; azione comune per packwiz con cache e Go fissato.
   - Workflow di aggiunta mod: rifiutano un ramo diverso da `dev`, partono dall'ultimo commit del ramo, packwiz senza lo stdin del ciclo.
   - Release: rifiuta un ramo diverso da `main` e un tag fuori da `main`; prima di esportare controlla che l'indice di packwiz sia identico a quello del commit.
   - `ci_commit.sh` gira solo nelle Actions, non tocca la configurazione git, gestisce il conflitto nel rebase.
   - `ci_pack.sh` e `controllo_locale.sh` con una sola coda di controlli; il controllo locale rifà anche l'inventario; gli avvisi della base dati si vedono.
2. ✅ **Script**
   - Base dati: il ciclo lento (21 s su 22), i campi multipli nel controllo dei nomi fantasma, il registro dell'etichetta del Berserker, l'impronta del datapack solo su `.json` e `.mcfunction` (una funzione per i due script), import inutili.
   - `dump_importa.py` non scrive niente se il dump ha errori.
   - `modrinth_resolve.py`: `slug@numero` filtrato per Minecraft e loader; un id di versione tutto minuscolo.
   - `log_confronta.py`: esadecimali e UUID. `release_notes.py`: versione esatta. `inventory.py`: un tag vanilla non scaricato è un errore. `vasi_verifica_jar.py`: anche i terreni sostituiti. `botanypots_genera.py`: cancella solo i percorsi generati.
   - Tolti `import_mrpack.py`, `data/modrinth-progetti.json`, `data/vasi/copertura.json` (restano nella storia di git).
   - `.gitattributes`, `.gitignore`.
3. [ ] **Documenti del pack** (`1.21.1/`, `README.md`, `docs/0001`, `docs/0101`): i rilievi 27–50 del rapporto: script e file citati che non esistono più, Regions Unexplored, B47, librerie in `0301` e `0403`, conti dei vasi, README del datapack, `0302`, tema accessori, `0503` ripulito, `0601`, legenda del changelog, owo-lib «dipendenza» e non «incorporata», memoria a 12 GB nel `README.md`, fatti di Sparse Structures.
4. ✅ **Contesto più leggero**: tappe fatte di `0501` in una riga; `AGENTS.md` sezioni 4, 5, 7, 8 senza ripetere i README (limite nel commento in testa: 20.000 caratteri invece di 200 righe); `CLAUDE.md` con le sole cose per Claude; `0303` con una regola e un rimando per voce; decisioni aperte solo in `0503`. Caricati a ogni sessione: da 48.700 a 33.300 caratteri.
5. ✅ **Permessi** in `.claude/settings.json`: chiedono conferma `git clean`, `git reset --hard`, `git checkout --`, `git restore`, `git branch -D`, `git stash drop` e `clear`.
6. ✅ **Versione**: `pack.toml` a 0.7.3; owo-lib e NeoForge come tappa 6.4 in `0501`, con il numero da decidere.

## 4. Prove

- [ ] `bash scripts/controllo_locale.sh 1.21.1/pack` verde, `shellcheck` pulito.
- [ ] Dopo il push, Controllo pack verde **senza commit**; poi una prova che fallisca davvero se un file generato non è aggiornato.
- [x] Il `refresh` della base dati da 23,4 a 2 secondi, con gli stessi controlli (il controllo locale intero da circa 25 a 2,7 secondi).
- [x] Generatori con `--verifica` invariati: vasi 340 file, mercato 469, lista nera; il generatore dei vasi, rilanciato in una copia, scrive gli stessi file.

## 5. Aperto

- Numero della versione di owo-lib e NeoForge, e cosa succede all'archeologia (oggi 0.7.4).

## 6. Esito

—
