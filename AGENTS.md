# Guida per gli agenti — Mango Craft

Istruzioni per qualsiasi agente AI che lavora su questo repository (standard aperto `AGENTS.md`). Qui ci sono le **regole stabili** e la **struttura del repository**. Come sono organizzati i documenti: sezione 4. All'inizio di un lavoro leggi almeno il piano (`1.21.1/lavoro/0501-piano.md`), le note tecniche (`1.21.1/docs/0303-note-tecniche.md`), il bug report (`1.21.1/docs/0402-bug-report.md`) e il file della versione in corso (`1.21.1/lavoro/versioni/`, quella con stato 🔧 o 📋 nel README).

---

## 1. Cos'è

Modpack **personale, single player**, giocato con **Prism Launcher**: oggi per Minecraft **1.21.1 NeoForge**. Il proprietario (Matteo) decide **mod per mod**: un agente propone, verifica e prepara, non aggiunge niente senza approvazione esplicita. Obiettivo, temi e principi: [`docs/0001-progetto.md`](docs/0001-progetto.md).

## 2. Come rispondere

- **Italiano**, conciso, leggibile da telefono: frasi brevi, elenchi solo quando servono, niente gergo tecnico non spiegato.
- **Verificare prima di affermare**: versioni, compatibilità, licenze e dipendenze si controllano nelle fonti (API di Modrinth, codice sorgente della mod, file del pack, inventario), non a memoria. Se una cosa non si è potuta verificare, dirlo.
- **Proporre con una raccomandazione chiara** (🟢 consigliata · 🟡 dipende · 🔴 sconsigliata) e lasciare la scelta a Matteo.
- **Errori**: se un'affermazione precedente era sbagliata, correggerla esplicitamente.

## 3. Struttura del repository

```
README.md · LICENSE · AGENTS.md (questa guida) · CLAUDE.md (la importa)
docs/                       documentazione comune a tutte le versioni (gruppi 00–02)
scripts/                    inventario, controlli, risoluzione delle mod, note di release
.github/workflows/          controllo a ogni modifica, aggiunta mod, release
ai-agents/stage/            risultati grezzi delle ricerche, una cartella per ricerca (non è documentazione)
1.21.1/                     una cartella per versione di Minecraft
├── pack/                   SOLO ciò che finisce nel gioco: pack.toml, index.toml, mods/*.pw.toml, config/…
│   └── config/paxi/datapacks/matteo_tweaks/   il datapack del pack, con i suoi readme
├── docs/                   documentazione della versione (gruppi 03–04)
├── mod-knowledge/          una scheda per mod: conoscenza verificata, con data e fonti
├── theme-knowledge/        una scheda per tema trasversale (più mod insieme, piattaforma): stessa forma
├── lavoro/                 documenti vivi di lavoro (gruppi 05–06) e, in versioni/, un file per versione
└── data/                   dati: inventario generato dai workflow, dati grezzi dei conteggi
```

Tutto ciò che sta fuori da `pack/` non viene mai installato. Una versione nuova di Minecraft avrà la sua cartella accanto, con la stessa struttura.

## 4. Documentazione

Cinque livelli, dal grezzo al distillato:

| Livello | Dove | Cos'è | Vivo o fermo |
|---|---|---|---|
| **Stage** | `ai-agents/stage/` | Risultati grezzi delle ricerche (report, tabelle, estratti, script), nella lingua in cui sono nati | fermo: si aggiunge, non si modifica |
| **Versioni** | `<versione>/lavoro/versioni/vX.Y.Z.md` | Un file per versione del pack: obiettivo, valutazioni, decisioni, lavoro, prove, esito. È la tracciabilità: il perché delle scelte | la versione in corso è viva; le rilasciate sono chiuse |
| **Schede delle mod** | `<versione>/mod-knowledge/` | Una scheda per mod (nome dello slug): fatti verificati, chiavi di config, compatibilità, storia nel pack. In testa "Aggiornata il …", lo stato e le fonti | vive: si aggiornano quando si riverifica un fatto |
| **Schede dei temi** | `<versione>/theme-knowledge/` | Una scheda per argomento che attraversa più mod o la piattaforma (esperienza, Nether, shader…): stessa forma, rimanda alle schede delle mod | vive, come sopra |
| **Documentazione** | `docs/`, `<versione>/docs/` | Com'è il pack oggi: mod, config, note tecniche, changelog, bug report, distinta | viva |

**Stage.** Una cartella per ricerca, `<data>_<versione MC>-v<versione del pack>_<nome>` (senza il segmento della versione se la ricerca non riguarda una versione). Non è una fonte per lo stato attuale e non ha un indice (regole in [`ai-agents/README.md`](ai-agents/README.md)). Il workflow Esamina mod scrive qui.

**File delle versioni.** Nome `vX.Y.Z.md`, senza codice numerico. Sezioni: 1 Obiettivo, 2 Valutazioni (il distillato delle ricerche, con il rimando allo stage), 3 Decisioni (una riga ciascuna, con la data, più le domande ancora aperte), 4 Lavoro, 5 Prove, 6 Rischi, 7 Esito. Si apre alla pianificazione della versione e si chiude al rilascio (Esito = Stato, tag, problemi noti). Le decisioni valide per più versioni stanno nei temi aperti (`0503`). Le righe di decisione non si correggono a posteriori: una decisione cambiata è una riga nuova.

**Schede.** Si crea o si aggiorna una scheda quando si verifica un fatto (nel sorgente, nell'inventario o in gioco). Un fatto che riguarda **una mod** va nella scheda della mod; uno che riguarda **due o più mod insieme** o tutto il pack va nella scheda del tema; l'una rimanda all'altra. I nomi delle schede sono unici nelle due cartelle. Le mod senza conoscenza verificata hanno solo la riga in `0301`. Una scheda può riguardare anche una mod candidata o scartata (lo stato è in testa). Gli indici sono i `README.md` delle due cartelle.

**Codici.** I documenti di `docs/` e dei livelli vivi di `lavoro/` hanno un codice di quattro cifre prima del nome: `GGnn-nome.md`. `GG` è il **gruppo** (tema), `nn` il progressivo. Un codice non cambia e non si riusa mai (i codici 0610, 0611, 0620, 0630, 0701–0713 e 09xx appartengono a documenti dissolti nel riordino del 19/10/2026: non si riusano); un documento nuovo prende il primo numero libero del suo gruppo. Lo stesso codice indica lo stesso tipo di documento in ogni versione di Minecraft (0402 è sempre il bug report). I file delle versioni, le schede e le cartelle di stage non hanno codice.

| Gruppo | Tema | Cartella | Tipo |
|---|---|---|---|
| **00** | Progetto: obiettivo, temi, principi | `docs/` | documentazione comune |
| **01** | Guide d'uso: installazione, istanze | `docs/` | documentazione comune |
| **02** | Sviluppo: formati, script, workflow, rilascio, decisioni tecniche | `docs/` | documentazione comune |
| **03** | Contenuto del pack: mod, config, note tecniche | `<versione>/docs/` | documentazione della versione |
| **04** | Versioni: changelog, bug report, distinta delle mod | `<versione>/docs/` | documentazione della versione |
| **05** | Pianificazione: piano, prove in gioco, temi aperti | `<versione>/lavoro/` | lavoro vivo |
| **06** | Mod candidate e scartate (indici) | `<versione>/lavoro/` | lavoro vivo |
| **07–99** | liberi per gruppi futuri | | |

**Indici.** Ogni cartella di documenti ha un `README.md` con l'indice dei suoi documenti. Quando si aggiunge, rinomina o toglie un documento (o una scheda, o un file di versione) si aggiorna il README della sua cartella.

**Un fatto, un posto.** Ogni informazione che cambia sta in **un solo posto vivo**; gli altri ci rimandano. Le righe dei file delle versioni e lo stage sono fotografie: possono ripetere informazioni, ma non vanno corretti a posteriori.

| Informazione | Dove |
|---|---|
| Cosa c'è nel pack, per tema, perché e con che licenza (senza numeri di versione) | `0301-mod` |
| File di config portati dal pack e impostazioni decise | `0302-config` |
| Regole da non rompere, in breve (con il rimando alla scheda che le motiva) | `0303-note-tecniche` |
| Fatti verificati su una mod, chiavi di config, formati, fonti | scheda in `mod-knowledge/` |
| Fatti verificati che attraversano più mod o la piattaforma | scheda in `theme-knowledge/` |
| Cosa è cambiato in ogni versione | `0401-changelog` |
| Problemi trovati | `0402-bug-report` |
| Versione, data ed esito della verifica di ogni file | `0403-distinta-mod` |
| Tappe e avanzamento | `0501-piano` |
| Controlli stabili da fare in gioco | `0502-prove-in-gioco` |
| Argomenti non ancora affrontati e decisioni aperte che valgono per più versioni | `0503-temi-aperti` |
| Mod candidate / scartate (indici, con il rimando alla valutazione) | `0601` / `0602` |
| Obiettivo, valutazioni, decisioni, lavoro e prove di una versione | `lavoro/versioni/vX.Y.Z.md` |
| Risultati grezzi di una ricerca | `ai-agents/stage/` |
| Come funziona una parte del datapack già fatta | il readme dentro il datapack |
| Regole del repository e dei documenti | questo file |

**Lingua e forma.** Italiano; lo stage può restare in inglese. Link relativi tra i documenti. Dentro `pack/` i nomi seguono le regole del gioco (sezione 7), non i codici.

## 5. Versioni, tag e istanze

- **Rami**: si lavora su **`dev`**. **`main`** contiene solo versioni provate: riceve `dev` con un **merge vero** (`git merge --no-ff dev`: niente fast-forward, per conservare il grafico dei rami; niente pull request) quando le prove di uscita della tappa sono fatte nell'istanza di prova e Matteo dà l'ok. Niente commit diretti su `main`; se capitasse (es. un commit automatico), si riporta `main` dentro `dev`.
- **Cosa va su `main` e quando**: mod, config e datapack solo con una versione e il suo tag. Documenti e workflow anche senza versione, con lo stesso merge, ma solo se su `dev` non c'è una tappa in corso (altrimenti aspettano la versione).
- **Versioni**: ogni versione rilasciata è un **tag** `<versione MC>-v<versione pack>` creato su `main`, es. `1.21.1-v0.3.0`. I tag di release non si spostano e non si cancellano. Le **0.x** sono tappe di prova (pre-release su GitHub); il **mondo vero parte dalla 1.0.0**, la prima versione con tutte le mod che generano il mondo. Il piano delle tappe è in `<versione>/lavoro/0501-piano.md`.
- **Istanze di Prism** (tutte con `packwiz-installer-bootstrap.jar` nella cartella `minecraft/` dell'istanza e comando prima dell'avvio `"$INST_JAVA" -jar packwiz-installer-bootstrap.jar <URL>`; guida completa in `docs/0101-installazione.md`):
  - prova → `https://raw.githubusercontent.com/mango-craft/mango-craft/refs/heads/dev/1.21.1/pack/pack.toml`
  - mondo vero → `…/refs/tags/1.21.1-vX.Y.Z/1.21.1/pack/pack.toml` (si aggiorna cambiando il tag, dopo un backup del mondo)
  - archivio → un tag vecchio, con `--bootstrap-no-update` dopo il primo avvio
- **NeoForge si imposta a mano in Prism**: packwiz-installer non riesce a cambiarlo. Ogni voce del changelog indica la versione richiesta.
- Le mod di queste istanze **non si toccano dalla scheda Mod di Prism**: si modifica il repository.
- GitHub tiene in cache i file grezzi per circa 5 minuti: dopo un push, aspettare prima di avviare.
- **Prova di una tappa, in due tempi** (decisione del 19/10/2026: «ha funzionato» non vuol dire «è tutto perfetto»). **Prove di uscita**: poche e rapide, nell'istanza di prova, prima del merge in `main` e del tag; il caso di prova di ogni cosa cambiata sta nella sezione 5 del file della versione. Sono: il gioco parte e carica un mondo; i log dell'istanza dev, confrontati con quelli della versione precedente, non hanno errori nuovi gravi; ciò che la versione ha cambiato funziona con un controllo semplice. **Bloccano l'uscita solo**: avvio o mondo che non vanno, crash in gioco normale, la modifica principale della versione che non fa il suo lavoro, rischio per il mondo. **Prove nel tempo**: tutto il resto (`1.21.1/lavoro/0502-prove-in-gioco.md` e le voci «nel tempo» del file della versione) si fa giocando e non blocca: la versione esce con i suoi problemi noti e si può già giocare. **Ogni problema nuovo, anche minore** (errori nel log, grafica mancante, ricette rotte, avvisi del controllo dei nomi), va nel **bug report** (`0402`) con un codice nuovo `Bnn` che non si riusa mai. Prima del merge, la voce della versione nel **changelog** (`0401`) riceve **Stato** (provata, data, tag) e **Problemi noti** (i codici comparsi o risolti); il piano (`0501`) segna la tappa come fatta e il file della versione (`lavoro/versioni/vX.Y.Z.md`) riceve l'**Esito** e si chiude. Quando un problema si risolve, la riga passa tra i risolti con la versione che lo chiude.

## 6. Aggiungere o cambiare una mod

1. Approvazione esplicita di Matteo.
2. **Mod da Modrinth**: workflow **Aggiungi mod Modrinth** sul ramo `dev` (`gh workflow run modrinth-add.yml --ref dev -f mods="slug1 slug2@versione …"`). Sceglie l'ultima **release** per 1.21.1 + NeoForge (per i pacchetti di shader: + Iris; o la versione indicata), la aggiunge con `packwiz modrinth add` (versione, hash e dipendenze obbligatorie presi da Modrinth) e nel commit elenca versioni, tipo e data scelti e i metafile nuovi (le dipendenze sono **librerie nuove** da segnalare).
3. **Mod solo CurseForge**: workflow **Aggiungi mod CurseForge** (link al file esatto `…/files/<id>`, oppure al progetto per l'ultimo file compatibile), che usa `packwiz curseforge add` rifiutando le dipendenze (di solito sono già nel pack da Modrinth; una libreria solo CurseForge va aggiunta nella stessa chiamata, prima della mod). I .jar non entrano mai nel repository. Quelle con distribuzione bloccata vanno scaricate a mano: l'installer mostra pagina e percorso.
4. **Controllo automatico** (in ogni workflow che tocca il pack): indice, metafile, **inventario** dei .jar (`<versione>/data/inventario/`) e **controllo dei nomi** (`controllo.md`: dipendenze mancanti, versioni richieste di NeoForge e delle altre mod, mod incompatibili tra loro, nomi del datapack inesistenti). L'output di packwiz va in `data/inventario/ultimo-workflow.log`. Se qualcosa fallisce, leggere questi due file nel ramo: i log dei workflow non sono leggibili da qui.
5. A mano, solo se i workflow non si possono usare: versione dall'API di Modrinth (`/v2/project/<slug>/version?game_versions=["1.21.1"]&loaders=["neoforge"]`), hash verificati con la ricerca inversa `/v2/version_file/<sha512>?algorithm=sha512` (stessa versione, stesso sha1; gli hash lunghi vanno letti a pezzi), metafile scritto a mano (formato in `docs/0201-sviluppo.md`), indice con `python3 scripts/packwiz_index.py 1.21.1/pack`, controllo con `python3 scripts/check_pack.py 1.21.1/pack`.
6. Licenza, data, se genera mondo o strutture (⚠️ = va aggiunta **prima del mondo vero**).
7. Documenti: scheda in `mod-knowledge/` (e in `theme-knowledge/` se tocca un tema) se c'è conoscenza verificata da registrare; riga della mod in `0301-mod` (ruolo, licenza, "Dalla X.Y.Z"), riga in `0403-distinta-mod` (versione, data, esito), voce della versione in corso in `0401-changelog`, avanzamento in `0501-piano` e decisione nel file della versione; se la mod porta problemi noti, `0402-bug-report`; se era tra le candidate, toglierla da `0601` (e aggiornare la sua scheda).

## 7. Regole del datapack `matteo_tweaks`

- **Niente datapack esterni**: tutto nel nostro. Si copia solo da licenze che lo permettono (MIT, LGPL), citando la fonte nel readme della cartella; le ARR solo come confronto.
- Ogni file ha una **condizione di caricamento** (`neoforge:conditions` con `mod_loaded`/`item_exists`, oppure `bookshelf:load_conditions` con `block_exists`; per le etichette, voci con `"required": false`): togliere una mod non deve dare errori.
- Ogni nome usato si controlla sull'**inventario** prima di scriverlo (`python3 scripts/check_ids.py <pack> <inventario>` funziona anche in locale).
- Dentro `data/` **tutti i nomi in minuscolo**: un `README.md` maiuscolo lì dentro dà "Invalid path in pack". I readme si chiamano `readme.md`, uno per cartella: sono la documentazione delle parti già fatte.
- Paxi carica il pacchetto in tutti i mondi, sopra gli altri (vince sui file con lo stesso percorso).
- `global_loot_modifiers.json` di NeoForge: un modificatore non elencato è spento; un nome elencato senza file dà errore.
- Le lune di Enhanced Celestials si ricaricano solo riaprendo il mondo; il resto con `/reload`. I modificatori di struttura (es. Berserker) richiedono il riavvio del mondo.
- Le parti da scrivere sono progettate nel file della versione che le porta (`<versione>/lavoro/versioni/`); i formati dei file stanno nelle schede (`botany-pots`, `farming-for-blockheads`, `cataclysm` per le mod; `esperienza` per i temi…).

## 8. Ambiente di lavoro di Claude

- Lo spazio di lavoro raggiunge **solo GitHub** dalla riga di comando. L'API di Modrinth si legge con lo strumento web. **CurseForge non è raggiungibile**: i suoi dati si ricavano dalle pagine o dai workflow.
- Compilare ed eseguire codice scaricato (packwiz compreso) **non è permesso** qui: i file di packwiz si scrivono con script propri, e packwiz vero gira nelle GitHub Actions.
- Quello che da qui non si raggiunge (Modrinth, CDN, Maven) lo fanno i workflow, che salvano i risultati nel repository: l'**inventario** in `<versione>/data/inventario/` dice cosa contiene ogni .jar (oggetti, blocchi, tag, tabelle del bottino, strutture, ricette di Botany Pots, dipendenze). Usarlo prima di scrivere nomi nel datapack.
- I log del gioco dell'istanza di prova si leggono dal PC di Matteo (solo la cartella `logs` dell'istanza dev, accesso concesso da lui) quando la sessione è collegata: se la cartella non si apre dalla shell, si copiano i file nella sessione.
- Da qui si possono mandare commit sui rami (`dev`, e `main` tramite merge) e avviare i workflow (`gh workflow run`), ma **non mandare tag** né scrivere tramite l'API di GitHub (pull request mai provate): per una release si usa il workflow **Release** con il tag come parametro. I log dei workflow non sono leggibili da qui: si controlla l'esito (`gh run view`) e il risultato (i file nel repository).
- Il PC di Matteo può essere collegato alla sessione: **non toccare la cartella di Prism senza il suo via**.
- Repository **pubblico**: niente dati personali (percorsi locali, email, nomi utente del PC) nei file.
- I risultati grezzi di una ricerca vanno in `ai-agents/stage/<data>_<versione>_<nome>/` (il workflow Esamina mod lo fa da solo); il distillato in un file di versione e in una scheda.
- Il progetto Claude "Minecraft modpack" contiene solo `context.md`, un riassunto generato da `scripts/contesto_progetto.py` (istruzioni in `CLAUDE.md`): non è una fonte, si rigenera.
