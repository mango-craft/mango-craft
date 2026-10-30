# Sviluppo: formati, script, workflow e rilasci

Guida tecnica per chi modifica il pack (persone o agenti). Le regole generali, compresa la struttura del repository e dei documenti, sono in [`AGENTS.md`](../AGENTS.md).

## Formato dei file del pack

Il pack di ogni versione di Minecraft sta in `<versione>/pack/` e segue il formato di [packwiz](https://packwiz.infra.link/reference/pack-format/).

- `pack.toml`: nome, versione del pack, versioni di Minecraft e NeoForge, hash dell'indice.
- `index.toml`: elenco di tutti i file del pack con il loro hash sha256. I metafile hanno `metafile = true`; con `preserve = true` un file viene installato solo se manca (utile per file che il giocatore modifica).
- `mods/<slug>.pw.toml`, `resourcepacks/<slug>.pw.toml`: un file per mod. Esempio da Modrinth:
  ```toml
  name = "Farmer's Delight"
  filename = "FarmersDelight-1.21.1-1.3.4.jar"
  side = "both"

  [download]
  url = "https://cdn.modrinth.com/data/R2OftAxM/versions/XTVZDOol/FarmersDelight-1.21.1-1.3.4.jar"
  hash-format = "sha512"
  hash = "…"

  [update]
  [update.modrinth]
  mod-id = "R2OftAxM"
  version = "XTVZDOol"
  ```
  Le mod di CurseForge hanno invece `mode = "metadata:curseforge"` nella sezione `[download]` e `[update.curseforge]` con `project-id` e `file-id`: le scrive packwiz (vedi sotto).
- Tutti gli altri file (`config/…`, il datapack) vengono copiati così come sono nella cartella dell'istanza.

## Script (`scripts/`, solo Python standard)

| Script | Cosa fa |
|---|---|
| `packwiz_index.py <pack>` | Rigenera `index.toml` e l'hash in `pack.toml`, come `packwiz refresh` (conserva i `preserve = true`) |
| `check_pack.py <pack>` | Controlla metafile, indice, assenza di .jar, JSON e nomi minuscoli del datapack. Esce con errore se qualcosa non va |
| `release_notes.py <pack> <changelog> <versione>` | Prepara le note di una release, con l'elenco delle mod CurseForge escluse dal .mrpack |
| `inventory.py <pack> <inventario>` | Scarica i .jar del pack (serve la rete; solo quelli cambiati: gira nelle Actions e nel controllo locale) e salva per ogni mod cosa contiene: mod id e dipendenze, oggetti e blocchi con il nome, tag, tabelle del bottino, strutture, tipi di ricetta, ricette di Botany Pots, voci e listini del mercato, effetti (con la descrizione) e pozioni (il nome del registro si ricava da traduzioni e classi; i nomi dedotti stanno in `potions_deduced`). Le voci del vecchio `META-INF/mods.toml`, che NeoForge 1.21.1 non legge, sono segnate `legacy` e non contano per versioni e dipendenze. Anche Minecraft e NeoForge. Riscarica solo i file cambiati |
| `check_ids.py <pack> <inventario> [--report FILE]` | Sull'inventario: dipendenze obbligatorie mancanti o in una versione troppo vecchia, mod dichiarate incompatibili tra loro (NeoForge compreso; un intervallo senza parentesi, per Maven, accetta qualunque versione) e nomi del datapack che non esistono (oggetti, blocchi, tag, tabelle, modificatori, condizioni mai vere; se c'è il dump del gioco (`data/dump/registri.json`), avviso per ogni nome che l'inventario ha ma il gioco non registra, perché l'inventario prende oggetti e blocchi anche da modelli e traduzioni; nelle funzioni `.mcfunction` oggetti dei `give`, pozioni e funzioni chiamate). Funziona anche senza rete |
| `modrinth_resolve.py <pack> <voci…>` | Sceglie le versioni Modrinth: `slug` = ultima release per Minecraft e loader del pack (per i pacchetti di shader il loader è Iris, per i resource pack "minecraft"); `slug@versione` o link = versione esatta (id, oppure numero cercato tra le versioni per Minecraft e loader del pack); un id di 8 caratteri si prova prima come id |
| `controllo_locale.sh <pack>` | Da lanciare in locale prima di ogni push su `dev`: `ci_pack.sh --locale`. Aggiorna indice, inventario e `controllo.md`, che vanno nel commit |
| `log_confronta.py <log nuovo> <log vecchio> [--tutti]` | Confronta i log di due avvii (anche `.log.gz`): avvisi ed errori nuovi e spariti, con i numeri, gli UUID e gli hash esadecimali sostituiti, per non contare i valori che cambiano a ogni avvio. È la prova di uscita «nessun errore nuovo grave» di ogni versione; esce con 1 se c'è qualcosa di nuovo |
| `esamina.py <pack> <risultati> <filtro> [--stringhe <regex>] <voci…>` | Legge i .jar di mod **non** nel pack (scaricati da Modrinth, mai eseguiti): versione, mod id e dipendenze dichiarate, cartelle di dati e, per i file che corrispondono al filtro, i valori. Con `--stringhe`, anche i testi scritti nel codice compilato che corrispondono (nomi dei file di config, chiavi, comandi), letti dalla tabella delle costanti dei `.class`. Scrive `<slug>.md` nella cartella dei risultati indicata (una cartella dello stage, es. `ai-agents/stage/2026-11-02-esame-mod/`). Serve la rete verso Modrinth |
| `botanypots_genera.py <versione> [--dry-run] [--verifica] [--report FILE]` | Genera i file di Botany Pots del datapack dalle **regole nostre** (i CSV `*_custom.csv` e `terreno_rarita.csv` in `1.21.1/data/vasi/`): le cartelle `<mod>/` in `recipe/botanypots/`, i tag `botanypots:soil/*` e, per un terreno di una mod a cui la classe dà un bonus diverso, il file **allo stesso percorso** di quello della mod (lo sostituisce). Dice cosa salta e perché. Si rilancia quando cambia una regola o una mod; `--verifica` non scrive e fallisce se i file nel datapack non corrispondono alle regole (lo fa il workflow a ogni push) |
| `vasi_verifica_jar.py <cartella mods> [--pack CARTELLA] [--lungo]` | Controlla le ricette dei vasi contro i **.jar veri** (sola lettura, si lancia dove stanno i jar, es. sul PC): blocchi, semi, raccolti, oggetti dei terreni, etichetta della terra, e per le colture con raccolto ricavato dal blocco che la tabella del bottino dia qualcosa nel vaso senza attrezzo (le tabelle con le cesoie no). Statico: non sostituisce `/botanypots debug`. Esce con 1 se trova un problema |
| `botanypots_db.py <versione> refresh\|query "SQL"\|analisi NOME\|tabelle\|controlli` | Base dati SQLite delle **piante del pack**: ogni oggetto e blocco dell'inventario (`OGGETTO`, `BLOCCO`), l'anagrafica della rarità (`RARITA`, da `1.21.1/data/rarita.csv`), i vasi (terreni, colture, tag, file di Botany Pots attivi, tag esplosi, scelte di rarità, vista delle coppie terreno-coltura) il mercato di Farming for Blockheads (listini, voci, piantabili, candidati, prezzi) e le pozioni (effetti, pozioni con la famiglia, regole della lista nera degli amuleti; dal dump del gioco effetti delle pozioni, alambicco, cibi e amuleti possibili) e, dal formato 2 del dump, il **confronto con il gioco** del lavoro di tutte le versioni (`GIOCO_*`: nomi registrati, ricette caricate, etichette finali, tabelle del bottino, insiemi di strutture; `NOSTR*`: i nostri file del datapack; viste `NOSTRA_RICETTA_DIVERSA`, `NOSTRO_TAG_MANCANTE`, `NOSTRA_TABELLA_MANCANTE`, `GIOCO_ID_DIVERSO`, con i controlli; regola: l'inventario dà contenuti e candidati, il gioco dice cosa esiste, colonna `gioco` di `OGGETTO` e `BLOCCO`, vista `REGOLA_NOME_FANTASMA`, confronto `GIOCO_RICETTA_DIVERSA` tra le ricette lette dai file e quelle caricate), costruita da inventario, datapack, `1.21.1/data/vasi/*.csv`, `1.21.1/data/mercato/*.csv`, `1.21.1/data/pozioni/*.csv` e `1.21.1/data/dump/*.json`; `query` la crea se manca o se inventario, datapack o CSV sono più recenti; `refresh` la ricostruisce solo se vincoli e controlli passano (il workflow lo fa a ogni push). `analisi NOME` esegue `1.21.1/mod-knowledge/botany-pots/query/NOME.sql`. Modello, fatti e query: `1.21.1/mod-knowledge/botany-pots/` |
| `mercato_genera.py <versione> [--dry-run] [--verifica] [--report FILE]` | Genera le voci e i listini del mercato di Farming for Blockheads nel datapack dalle regole in `1.21.1/data/mercato/*.csv` (moneta e base per origine e rarità, moltiplicatori, origine e classe per mod, regole per tipo, eccezioni per oggetto, listini delle mod riscritti). Non rilegge i CSV: interroga la base dati delle piante (viste `MERCATO_PIANO_VOCE` e `MERCATO_PIANO_PRESET`). Stesse opzioni del generatore dei vasi |
| `dump_importa.py <cartella del dump> <versione>` | Importa i file scritti in gioco da `/mango_dump` (KubeJS; nell'istanza: `logs/mango-craft-dump/`) in `<versione>/data/dump/`, ordinati per avere diff leggibili; controlla formato (oggi 2), file mancanti, sezioni non scritte da quel dump ed errori del dump |
| `pozioni_genera.py <versione> [--dry-run] [--verifica] [--report FILE]` | Scrive la lista nera degli amuleti di pozione di Apotheosis (`data/apotheosis/tags/potion/potion_charm_blacklist.json`) dalla regola in `1.21.1/data/pozioni/pozione_custom.csv`, passando dalla base dati (vista `POZIONE_LISTA_NERA`); segnala le pozioni con il nome dedotto. Stesse opzioni del generatore del mercato |
| `ci_pack.sh <pack> [--locale]` | Tutti i controlli in fila: indice (packwiz nelle Actions, `packwiz_index.py` con `--locale`), `check_pack`, inventario, `check_ids`, `botanypots_genera.py --verifica`, il `refresh` della base dati (mostra solo i controlli falliti ❌ e gli avvisi che hanno trovato qualcosa ⚠️), `mercato_genera.py --verifica` e `pozioni_genera.py --verifica`. Rifà i file generati; esce con errore se un passo fallisce |
| `ci_commit.sh "<messaggio>"` | Commit e push dei file rigenerati dai workflow di aggiunta mod; solo nelle Actions (in locale esce subito) |
| `comune.py` | Costanti e funzioni usate da più script (percorso del datapack, impronta del datapack per il dump) |

## Workflow di GitHub (`.github/workflows/`)

| Workflow | Quando parte | Cosa fa |
|---|---|---|
| **Controllo pack** (`check.yml`) | A ogni push su `main` o `dev` e a ogni pull request | `ci_pack.sh` con packwiz: rifà indice, inventario e `controllo.md` e **fallisce se sono diversi da quelli del commit** (li scrive il controllo locale). Non fa commit. Conta solo l'ultimo push di un ramo |
| **Aggiungi mod Modrinth** (`modrinth-add.yml`) | A mano, solo su `dev` (`gh workflow run modrinth-add.yml --ref dev -f mods="…"`) | Sceglie le versioni (`modrinth_resolve.py`), le aggiunge con `packwiz modrinth add` insieme alle dipendenze obbligatorie, lancia `ci_pack.sh` e fa il commit elencando versioni scelte e metafile nuovi |
| **Aggiungi mod CurseForge** (`curseforge-add.yml`) | A mano, solo su `dev` (scheda *Actions* → *Run workflow*) | Aggiunge una o più mod dai link ai file esatti (`…/files/<id>`) o ai progetti (ultimo file compatibile), rifiutando le dipendenze, poi lancia `ci_pack.sh` e fa il commit |
| **Release** (`release.yml`) | Al push di un tag `<versione MC>-vX.Y.Z`, oppure a mano su `main` indicando il tag da creare | Rifiuta un commit che non è in `main`; controlla che il tag corrisponda a `pack.toml` e che l'indice di packwiz sia identico a quello del commit; esporta un `.mrpack` con le sole mod Modrinth, crea lo zip della documentazione e pubblica la release |

packwiz si compila una volta, a un commit fissato e con la versione di Go che dichiara, e poi si prende dalla cache di GitHub (azione comune `.github/actions/packwiz/`: per aggiornarlo si cambia lì il commit). In locale non serve: l'indice lo scrive `packwiz_index.py`, e il Controllo pack lo rifà con packwiz come verifica indipendente. I workflow di aggiunta mod sono gli unici che fanno commit: girano uno alla volta per ramo, partono dall'ultimo commit del ramo e, se nel frattempo il ramo è andato avanti, rifanno il push sopra (se gli stessi file sono cambiati si fermano: si rilancia). Dopo un loro commit, in locale `git pull`. Le dipendenze di una mod CurseForge si rifiutano perché packwiz riconosce come "già presenti" solo le mod prese da CurseForge, e aggiungerebbe doppioni di quelle prese da Modrinth.

## Lavorare in locale (Claude Code, WSL)

Dal 29/10/2026 lo sviluppo si fa in locale. Le regole dell'ambiente sono in [`AGENTS.md`](../AGENTS.md), sezioni 8 e 9; sessione, permessi, stage e archivio in [`ai-agents/README.md`](../ai-agents/README.md); qui le procedure.

- **Preparazione, una volta**: `sudo dnf install gh` (serve per lanciare i workflow); copiare `ai-agents/contesto-locale.esempio.md` in `ai-agents/contesto-locale.md` (fuori da git) e compilarlo con il percorso dell'istanza di Prism e quanto serve all'agente sul PC. Niente percorsi locali nei file versionati. Per `gh`, un token *fine-grained* di GitHub: *Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token*; proprietario l'organizzazione `mango-craft` (il repository è suo, non dell'account personale), accesso solo a `mango-craft/mango-craft`, il solo permesso **Actions** in lettura e scrittura (basta per lanciare i workflow e leggerne esito, log e artefatti; il push passa dalla deploy key). Va nel password manager e si incolla all'avvio con `--gh`.
- **Sessione**: `ai-agents/bin/claude-session` (o `--gh` per avere anche il token): carica la deploy key solo per la sessione, avvisa se manca il contesto locale e avvia Claude Code con i permessi e la sandbox di `.claude/settings.json`.
- **Esaminare una mod fuori dal pack**: `python3 scripts/esamina.py 1.21.1/pack ai-agents/stage/<data>-esame-mod "<filtro>" [--stringhe "<regex>"] <slug…>`; il risultato resta sul PC, il distillato va nel file della versione e nella scheda.
- **Controllo prima del push**: `bash scripts/controllo_locale.sh 1.21.1/pack` (indice, controllo del pack, inventario, nomi, generatori con `--verifica`, base dati): pochi secondi, l'inventario scarica solo i jar cambiati. Indice, inventario e `controllo.md` aggiornati vanno nel commit: il Controllo pack fallisce se mancano.
- **Log del gioco**: `python3 scripts/log_confronta.py <istanza>/logs/latest.log <istanza>/logs/<log della versione precedente>.log.gz`. Ogni firma nuova si classifica: innocua (B14), problema nuovo (`Bnn`), errore grave (blocca l'uscita).
- **Dump del gioco**: in gioco `/mango_dump`, poi `python3 scripts/dump_importa.py <istanza>/logs/mango-craft-dump 1.21.1` e `python3 scripts/botanypots_db.py 1.21.1 refresh`: i controlli confrontano i nostri file con il gioco.
- **Aggiungere una mod**: con i workflow (`gh workflow run modrinth-add.yml --ref dev -f mods="…"`), anche da locale: scelgono la versione, aggiornano l'inventario e fanno il commit; poi `git pull`. packwiz in locale non serve: l'indice lo scrive `packwiz_index.py`, e senza i workflow mancherebbe l'inventario.
- **Release**: `git tag -a 1.21.1-vX.Y.Z -m "Mango Craft 1.21.1-vX.Y.Z" && git push origin 1.21.1-vX.Y.Z` su `main`, oppure il workflow Release (sotto).

## Rilasciare una versione

La procedura passo per passo. Le regole (rami `dev` e `main`, tag, pre-release, cosa va su `main` e quando, cosa registrare dopo la prova) sono in [`AGENTS.md`](../AGENTS.md), sezione 5, e non si ripetono qui.

Quando una versione **si apre** (regola del 30/10/2026), su `dev`: `version` in `<versione>/pack/pack.toml` passa alla versione nuova (e `[versions]` se cambia NeoForge), e la voce in `<versione>/docs/0401-changelog.md` nasce con **Stato**: 🔧 in lavorazione. Così l'istanza che segue `dev` mostra la versione davvero in prova.

Al rilascio:

1. Nella voce del changelog: titolo `## X.Y.Z — data`, versione di NeoForge, se serve un mondo nuovo, cosa cambia, **Stato**: 🧪 in prova su `dev`.
2. Controllo locale, commit e push su `dev`. Aspetta che il **Controllo pack** sia verde.
3. **Prova di uscita** nell'istanza che segue `dev` (dopo circa 5 minuti, per la cache di GitHub): avvio, mondo nuovo, log. Poi bug report, changelog e piano come dice `AGENTS.md` (Prova di una tappa).
4. Se la prova passa, unisci `dev` in `main` con un merge vero, che conserva il grafico dei rami: `git checkout main && git merge --no-ff dev -m "Versione X.Y.Z" && git push`, poi torna su `dev`.
5. Crea il tag su `main`, in uno dei due modi:
   - **dal computer**: `git tag -a 1.21.1-vX.Y.Z -m "Mango Craft 1.21.1-vX.Y.Z" && git push origin 1.21.1-vX.Y.Z` (tag annotato, come quelli del workflow);
   - **con il workflow Release**: `gh workflow run release.yml --ref main -f tag=1.21.1-vX.Y.Z` (o scheda *Actions* → **Release** → *Run workflow*, scrivendo il tag). Il workflow crea il tag sull'ultimo commit di `main` e rifiuta un tag già esistente.
6. Il workflow **Release** pubblica i file; le versioni **0.x** escono come *pre-release*.

Per correggere una versione già rilasciata se ne fa una nuova (i tag non si spostano).

## Mod solo CurseForge

Il `.mrpack` pubblico non le contiene, perché `packwiz modrinth export` le includerebbe come file e ridistribuirle non è permesso. Le note della release le elencano con il link al file esatto. Nelle istanze collegate al repository le scarica packwiz-installer.
