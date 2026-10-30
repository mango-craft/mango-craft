<!-- Regole per gli agenti, caricate a ogni sessione di Claude Code tramite CLAUDE.md (i commenti
     HTML come questo vengono scartati). Qui solo regole, struttura e trappole; i dettagli stanno
     nei documenti citati. Tenerla sotto i 20.000 caratteri (wc -c AGENTS.md) e aggiornarla quando
     una correzione va ripetuta due volte. I permessi veri di Claude Code (cosa può eseguire,
     leggere, scrivere) sono in .claude/settings.json. -->

# Guida per gli agenti — Mango Craft

Istruzioni per qualsiasi agente AI che lavora su questo repository (standard aperto `AGENTS.md`): le **regole stabili** e la **struttura**. All'inizio di un lavoro leggi il piano (`1.21.1/lavoro/0501-piano.md`), le note tecniche (`1.21.1/docs/0303-note-tecniche.md`), il bug report (`1.21.1/docs/0402-bug-report.md`), il file della versione in corso (quella con stato 🔧 nell'indice delle versioni, `1.21.1/lavoro/README.md`; se non ce n'è, la prima 📋) e, se ce n'è una aperta, la revisione in corso (`revisioni/README.md`). I temi aperti (`0503`) quando si decide cosa fare dopo; le schede quando si tocca una mod o un tema.

---

## 1. Cos'è

Modpack **personale, single player**, giocato con **Prism Launcher**: oggi per Minecraft **1.21.1 NeoForge**. Il proprietario (Matteo) decide **mod per mod**: un agente propone, verifica e prepara, non aggiunge niente senza approvazione esplicita. Obiettivo, temi e principi: [`docs/0001-progetto.md`](docs/0001-progetto.md).

## 2. Come rispondere

- **Italiano**, conciso, leggibile da telefono: frasi brevi, elenchi solo quando servono, niente gergo tecnico non spiegato.
- **Nomi di mod e dimensioni in inglese**, sempre (Twilight Forest, Aether, Nether, End, Undergarden, Overworld): niente traduzioni come «Crepuscolo» (regola di Matteo, 24/10/2026).
- **Verificare prima di affermare**: versioni, compatibilità, licenze e dipendenze si controllano nelle fonti (API di Modrinth, codice sorgente della mod, file del pack, inventario, dump), non a memoria. Se una cosa non si è potuta verificare, dirlo.
- **Proporre con una raccomandazione chiara** (🟢 consigliata · 🟡 dipende · 🔴 sconsigliata) e lasciare la scelta a Matteo.
- **Errori**: se un'affermazione precedente era sbagliata, correggerla esplicitamente.

## 3. Struttura del repository

```
README.md · LICENSE · AGENTS.md (questa guida) · CLAUDE.md (la importa)
docs/                       documentazione comune a tutte le versioni (gruppi 00–02)
scripts/                    controlli, inventario, generatori, base dati, risoluzione delle mod, note di release
.github/                    workflow (controllo a ogni push, aggiunta mod, release) e l'azione comune di packwiz
.claude/settings.json       permessi e sandbox di Claude Code (sezione 8)
revisioni/                  il lavoro sul repository che non è una versione del pack (piano e diario)
ai-agents/                  materiale degli agenti (non è documentazione; ai-agents/README.md)
├── bin/claude-session      apre la sessione di Claude Code con le credenziali solo in memoria
├── contesto-locale.md      percorsi e strumenti del PC (fuori da git; modello: contesto-locale.esempio.md)
├── stage/                  file di lavoro per Matteo, risultati grezzi delle ricerche (fuori da git)
└── archivio/               lo stage versionato fino al 29/10/2026, fermo
1.21.1/                     una cartella per versione di Minecraft
├── pack/                   SOLO ciò che finisce nel gioco: pack.toml, index.toml, mods/*.pw.toml, config/…
│   └── config/paxi/datapacks/matteo_tweaks/   il datapack del pack, con i suoi readme
├── docs/                   documentazione della versione (gruppi 03–04)
├── mod-knowledge/          una scheda per mod: conoscenza verificata, con data e fonti
├── theme-knowledge/        una scheda per tema trasversale (più mod insieme, piattaforma): stessa forma
├── lavoro/                 documenti vivi di lavoro (gruppi 05–06) e, in versioni/, un file per versione
└── data/                   inventario e controllo dei nomi (generati), dump del gioco, regole in CSV dei generatori
```

Tutto ciò che sta fuori da `pack/` non viene mai installato. Una versione nuova di Minecraft avrà la sua cartella accanto, con la stessa struttura.

## 4. Documentazione

| Livello | Dove | Vivo o fermo | Regole |
|---|---|---|---|
| **Stage** | `ai-agents/stage/`, fuori da git: risultati grezzi, confronti e bozze per Matteo | locale, lo svuota Matteo | [`ai-agents/README.md`](ai-agents/README.md) |
| **Archivio** | `ai-agents/archivio/`: lo stage versionato fino al 29/10/2026 | fermo | come sopra |
| **Revisioni** | `revisioni/AAAA.MM-NN/`: piano e diario di un lavoro sul repository | aperta viva, chiuse storico | [`revisioni/README.md`](revisioni/README.md) |
| **Versioni** | `<versione>/lavoro/versioni/vX.Y.Z.md`: il perché delle scelte di una versione | in corso viva, rilasciate chiuse | sotto |
| **Schede** | `<versione>/mod-knowledge/` (una per mod), `<versione>/theme-knowledge/` (una per tema) | vive | sotto e i loro README |
| **Documentazione** | `docs/`, `<versione>/docs/`: com'è il pack oggi | viva | sotto |

**Stage.** Un file o una cartella per lavoro, `AAAA-MM-GG-argomento`. **Nessun file versionato rimanda allo stage**: ciò che deve restare va nel suo posto, con le sue fonti, e si regge da solo. Gli agenti non cancellano niente dallo stage senza chiederlo; i file che servono solo all'agente vanno nella cartella temporanea della sessione. L'archivio si può citare, ma non è una fonte per lo stato attuale.

**File delle versioni.** Nome `vX.Y.Z.md`. Sezioni: 1 Obiettivo, 2 Valutazioni (il distillato delle ricerche, con le fonti), 3 Decisioni (una riga datata ciascuna, più le domande aperte), 4 Lavoro, 5 Prove, 6 Rischi, 7 Esito. Si apre alla pianificazione e si chiude al rilascio (Esito = stato, tag, problemi noti). Le decisioni valide per più versioni stanno in `0503`. Una decisione cambiata è una riga nuova, non una correzione.

**Schede.** Si crea o si aggiorna una scheda quando si verifica un fatto (sorgente, inventario, dump, gioco). Un fatto su **una mod** va nella sua scheda; su **più mod** o su tutto il pack, nella scheda del tema; l'una rimanda all'altra. Nome: lo slug del metafile, o un nome breve leggibile con lo slug nella testata (regola del 30/10/2026); unico nelle due cartelle. In testa «Aggiornata il …», lo stato e le fonti. Una mod con molto materiale ha una cartella `<nome>/<nome>.md`; gli script restano in `scripts/`. Le mod senza conoscenza verificata hanno solo la riga in `0301`.

**Codici.** I documenti di `docs/` e quelli vivi di `lavoro/` si chiamano `GGnn-nome.md`: `GG` è il gruppo, `nn` il progressivo. Un codice non cambia e non si riusa (nemmeno quelli dei documenti dissolti il 19/10/2026: elenco in `1.21.1/lavoro/README.md`); un documento nuovo prende il primo numero libero del suo gruppo. Lo stesso codice è lo stesso tipo di documento in ogni versione di Minecraft.

| Gruppo | Tema | Cartella |
|---|---|---|
| **00** · **01** · **02** | Progetto · guide d'uso · sviluppo (formati, script, workflow, rilascio) | `docs/` |
| **03** · **04** | Contenuto del pack (mod, config, note tecniche) · versioni (changelog, bug report, distinta) | `<versione>/docs/` |
| **05** · **06** | Pianificazione (piano, prove in gioco, temi aperti) · mod candidate e scartate | `<versione>/lavoro/` |
| **07–99** | liberi | |

**Indici.** Ogni cartella di documenti ha un `README.md` con l'indice; quello dei file delle versioni è `1.21.1/lavoro/README.md`. Chi aggiunge, rinomina o toglie un documento aggiorna l'indice.

**Un fatto, un posto.** Ogni informazione che cambia sta in **un solo posto vivo**; gli altri ci rimandano. I file delle versioni e delle revisioni e l'archivio sono fotografie: possono ripetere, ma non si correggono (un percorso spostato sì).

| Informazione | Dove |
|---|---|
| Cosa c'è nel pack, perché, con che licenza (senza versioni) | `0301-mod` |
| File di config portati e impostazioni decise | `0302-config` |
| Regole da non rompere, in breve, con il rimando alla scheda | `0303-note-tecniche` |
| Fatti verificati su una mod / su più mod o la piattaforma | scheda in `mod-knowledge/` / `theme-knowledge/` |
| Cosa è cambiato in ogni versione | `0401-changelog` |
| Problemi trovati | `0402-bug-report` |
| Versione, data ed esito della verifica di ogni file | `0403-distinta-mod` |
| Tappe e avanzamento | `0501-piano` |
| Controlli stabili da fare in gioco | `0502-prove-in-gioco` |
| Argomenti non affrontati e decisioni aperte per più versioni | `0503-temi-aperti` (sezione 4) |
| Mod candidate e approvate non ancora aggiunte / scartate | `0601` / `0602` |
| Il perché delle scelte di una versione | `lavoro/versioni/vX.Y.Z.md` |
| Il filo di un lavoro sul repository | `revisioni/AAAA.MM-NN/` |
| Risultati grezzi di una ricerca | lo stage (fino al 29/10/2026 l'archivio) |
| Percorsi e strumenti del PC | `ai-agents/contesto-locale.md`, fuori da git |
| Come funziona una parte del datapack | il readme dentro il datapack |
| Regole del repository e dei documenti | questo file |

**Lingua e forma.** Italiano; stage e archivio possono restare in inglese. Link relativi tra i documenti. Dentro `pack/` i nomi seguono le regole del gioco (sezione 7), non i codici.

## 5. Versioni, tag e istanze

- **Rami**: si lavora su **`dev`**. **`main`** contiene solo versioni provate: riceve `dev` con un **merge vero** (`git merge --no-ff dev`, niente pull request) quando le prove di uscita sono fatte e Matteo dà l'ok. Niente commit diretti su `main`; se capitasse, si riporta `main` dentro `dev`.
- **Cosa va su `main`**: mod, config e datapack solo con una versione e il suo tag. Documenti e workflow anche senza versione, con lo stesso merge, ma solo se su `dev` non c'è una tappa in corso.
- **Versioni**: ogni versione rilasciata è un **tag** `<versione MC>-v<versione pack>` su `main` (es. `1.21.1-v0.3.0`), che non si sposta e non si cancella. Le **0.x** sono tappe (pre-release). `version` in `pack.toml` si alza quando la versione **si apre** (regola del 30/10/2026). Il **mondo vero** parte da una 0.x che supera la soglia (`0503`, sezione 4, n. 5); la **1.0.0** arriva dopo averci giocato a lungo (Matteo, 25/10/2026). Procedura di rilascio: `docs/0201-sviluppo.md`.
- **Istanze di Prism**: prova (segue `dev`), mondo vero (un tag), archivio (un tag vecchio); indirizzi e procedura in `docs/0101-installazione.md`. NeoForge si imposta a mano in Prism (packwiz-installer non lo cambia: il changelog dice quale). Le mod di queste istanze non si toccano dalla scheda Mod di Prism. Dopo un push, GitHub tiene in cache i file per circa 5 minuti.
- **Prova di una tappa, in due tempi** (19/10/2026):
  - **Prove di uscita**, poche e rapide, nell'istanza di prova, prima del merge e del tag: il gioco parte e carica un mondo; i log, confrontati con quelli della versione precedente, non hanno errori nuovi gravi; ciò che la versione ha cambiato funziona (casi nella sezione 5 del file della versione).
  - **Bloccano l'uscita solo**: avvio o mondo che non vanno, crash in gioco normale, la modifica principale che non fa il suo lavoro, rischio per il mondo.
  - **Prove nel tempo**: il resto (`0502` e le voci «nel tempo» della versione) si fa giocando e non blocca.
  - **Ogni problema nuovo**, anche minore, va in `0402` con un codice `Bnn` nuovo, mai riusato; risolto, passa tra i risolti con la versione che lo chiude.
  - **Prima del merge**: in `0401` Stato (provata, data, tag) e Problemi noti; in `0501` la tappa fatta; nel file della versione l'Esito; nell'indice delle versioni lo stato.

## 6. Aggiungere o cambiare una mod

1. Approvazione esplicita di Matteo.
2. **Mod da Modrinth**: workflow **Aggiungi mod Modrinth**, solo su `dev` (`gh workflow run modrinth-add.yml --ref dev -f mods="slug1 slug2@versione …"`). Senza versione sceglie l'ultima release per 1.21.1 + NeoForge (se non c'è: beta, poi alpha; per i pacchetti di shader il loader è Iris). Aggiunge con `packwiz modrinth add` (hash e dipendenze obbligatorie da Modrinth) e nel commit elenca versioni, tipo e data scelti e i metafile nuovi: le dipendenze sono **librerie nuove** da segnalare. Poi `git pull`.
3. **Mod solo CurseForge**: workflow **Aggiungi mod CurseForge** (link al file `…/files/<id>`, o al progetto per l'ultimo file compatibile): rifiuta le dipendenze, che di solito sono già nel pack da Modrinth (una libreria solo CurseForge va nella stessa chiamata, prima della mod). Quelle con distribuzione bloccata si scaricano a mano: l'installer mostra pagina e percorso.
4. **Controlli**: ogni workflow che tocca il pack rifà indice, inventario dei jar e **controllo dei nomi** (`<versione>/data/inventario/controllo.md`: dipendenze mancanti, versioni richieste, mod incompatibili, nomi del datapack inesistenti); l'output di packwiz va in `ultimo-workflow.log` accanto. Se qualcosa fallisce: quei due file e `gh run view <id> --log-failed`.
5. A mano, solo se i workflow non si possono usare: versione e hash dall'API di Modrinth (`scripts/modrinth_resolve.py`), metafile nel formato di `docs/0201-sviluppo.md`, poi il controllo locale (sezione 8).
6. Licenza, data, se genera mondo o strutture (⚠️ = va aggiunta **prima del mondo vero**).
7. Documenti: scheda se c'è conoscenza verificata; riga in `0301` (ruolo, licenza, «Dalla X.Y.Z»), riga in `0403` (versione, data, esito), voce in `0401`, avanzamento in `0501`, decisione nel file della versione; problemi noti in `0402`; se era in `0601`, toglierla (e aggiornare la sua scheda). I .jar non entrano mai nel repository.

## 7. Regole del datapack `matteo_tweaks`

- **Niente datapack esterni**: tutto nel nostro. Si copia solo da licenze che lo permettono (MIT, LGPL), citando la fonte nel readme; le ARR solo come confronto.
- Ogni file ha una **condizione di caricamento** (`neoforge:conditions` con `mod_loaded`/`item_exists`, `bookshelf:load_conditions` con `block_exists`; nelle etichette, voci con `"required": false`): togliere una mod non deve dare errori. Eccezioni volute, spiegate in `0303`: le 5 tabelle degli scavi e le funzioni di prova; listini del mercato e lune non ne hanno bisogno (li legge solo la loro mod).
- Ogni nome si controlla prima di scriverlo: `python3 scripts/check_ids.py <pack> <inventario>` (inventario più nomi registrati dal dump: vince il gioco, sezione 8).
- Dentro `data/` **tutti i nomi in minuscolo**: un `README.md` maiuscolo dà «Invalid path in pack». I readme si chiamano `readme.md`, **uno per parte** (la cartella principale di ogni lavoro; regola del 30/10/2026): sono la documentazione delle parti fatte.
- Paxi carica il pacchetto in tutti i mondi, sopra gli altri: vince sui file con lo stesso percorso.
- `global_loot_modifiers.json` di NeoForge: un modificatore non elencato è spento; un nome elencato senza file dà errore.
- Le lune di Enhanced Celestials si ricaricano solo riaprendo il mondo, i modificatori di struttura (es. Berserker) col riavvio del mondo; il resto con `/reload`.
- **Funzioni di prova** delle prove di uscita: `data/matteo_tweaks/function/test/releases/v<versione>/`, nomi corti che dicono cosa c'è dentro, più `tutte_le_prove` (stile di Matteo, 25/10/2026; readme in `function/test/`).
- Le parti da scrivere si progettano nel file della versione che le porta; i formati dei file stanno nelle schede (`botany-pots`, `farming-for-blockheads`, `cataclysm`, tema `esperienza`…).

## 8. Ambiente di lavoro degli agenti

Lo sviluppo si fa in locale, con Claude Code in WSL (dal 29/10/2026; il 30/10 Matteo ha eliminato il progetto claude.ai). Sessione, permessi, sandbox e trappole: [`ai-agents/README.md`](ai-agents/README.md); procedure: `docs/0201-sviluppo.md`, «Lavorare in locale».

- Repository **pubblico**: niente dati personali (percorsi locali, email, nomi utente del PC) nei file. Il **contesto locale** (istanza di Prism e log, Python, strumenti) sta in `ai-agents/contesto-locale.md`, fuori da git; se manca, si copia il modello `contesto-locale.esempio.md` e si chiedono i valori a Matteo prima di cercare l'istanza.
- **Cartella di Prism**: dall'istanza si legge soltanto `logs/` (log, `logs/kubejs/`, dump in `logs/mango-craft-dump/`); il resto non si tocca senza il via di Matteo. `accounts.json` non si legge mai.
- **Sessione**: Matteo la apre con `ai-agents/bin/claude-session`, con le credenziali solo in memoria (deploy key per il push; con `--gh` un token per `gh`). Se ne manca una, dirlo a Matteo (`ai-agents/bin/claude-session --gh --continue`). Un token non si stampa, non si scrive su file, non entra in un commit.
- **Permessi e sandbox**: `.claude/settings.json`, che non si modifica senza chiederlo. Push, tag, merge, avvio di workflow, release e i comandi git che cancellano chiedono conferma. I comandi girano nella sandbox (scrivono solo nel repository e nella cartella temporanea, rete solo verso i domini consentiti); `gh`, `git push`, `fetch` e `pull` girano fuori.
- **Inventario e dump**: l'inventario (`<versione>/data/inventario/`) dice cosa contiene ogni jar, anche nomi che il gioco non registra; il dump del gioco (`<versione>/data/dump/`, da `/mango_dump`) dice cosa esiste davvero. Dove non coincidono **vince il gioco** (regola del 29/10/2026, `0303`).
- **Prima di ogni push su `dev`**: `bash scripts/controllo_locale.sh 1.21.1/pack`. Aggiorna indice, inventario e `controllo.md`, che vanno nel commit; dopo il push il **Controllo pack** deve essere verde (fallisce se il commit non li aveva).
- **Stage**: i risultati grezzi vanno in `ai-agents/stage/AAAA-MM-GG-argomento`; il distillato, con le fonti, in un file di versione, una scheda o una revisione. Una mod fuori dal pack si esamina con `python3 scripts/esamina.py`.
- Gli script sono Python ≥ 3.11 con la sola libreria standard; i `.sh` sono bash, con `shellcheck` pulito.

## 9. Autonomia dell'agente e lavoro finito

Cosa un agente fa da solo e cosa no (29/10/2026). Le scelte su mod e contenuti restano di Matteo (sezione 1).

| Cosa | Come |
|---|---|
| Leggere il repository, le fonti in rete, i log e il dump dell'istanza; controlli e analisi; file nello stage | da solo |
| Documenti, schede, script e workflow; commit su `dev` | da solo. Se cambia una regola, la struttura o più parti insieme, prima un piano breve (nella revisione o nel file della versione), poi si procede; ci si ferma a chiedere solo se contraddice una decisione presa |
| Datapack, generatori e le loro regole (CSV) | progettati nel file della versione (sezione 7); si scrivono quando Matteo ha deciso la versione |
| Mod, config del pack, NeoForge, scelte di gioco | solo con l'approvazione esplicita di Matteo (sezione 6) |
| Push, tag, merge in `main`, avvio dei workflow, modifiche a `.claude/settings.json` | con la conferma di Matteo (Claude Code la chiede da sé per i primi quattro) |
| Cartella di Prism | solo lettura di `logs/`; il resto con il via di Matteo |

**Una modifica è finita quando:**
- il controllo locale è verde (se tocca pack, datapack, dati o script) e `shellcheck` è pulito sugli script bash toccati;
- i documenti che citano ciò che è cambiato sono aggiornati (`grep -rn`), indici compresi;
- la decisione ha la sua riga datata nel file della versione o nella revisione;
- c'è un commit su `dev` per unità di lavoro, con un messaggio che dice cosa e perché; dopo il push, **Controllo pack** è verde.
