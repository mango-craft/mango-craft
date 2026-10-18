# Sviluppo: formati, script, workflow e rilasci

Guida tecnica per chi modifica il pack (persone o agenti). Le regole generali sono in [`AGENTS.md`](../AGENTS.md).

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
| `import_mrpack.py <file.mrpack> <pack> [nomi.json]` | Converte un pacchetto .mrpack nei metafile packwiz (usato per importare la 0.1.1) |
| `release_notes.py <pack> <changelog> <versione>` | Prepara le note di una release, con l'elenco delle mod CurseForge escluse dal .mrpack |
| `inventory.py <pack> <inventario>` | Scarica i .jar del pack (serve la rete: gira nelle Actions) e salva per ogni mod cosa contiene: mod id e dipendenze, oggetti e blocchi con il nome, tag, tabelle del bottino, strutture, tipi di ricetta, ricette di Botany Pots. Anche Minecraft e NeoForge. Riscarica solo i file cambiati |
| `check_ids.py <pack> <inventario> [--report FILE]` | Sull'inventario: dipendenze obbligatorie mancanti e nomi del datapack che non esistono (oggetti, blocchi, tag, tabelle, modificatori, condizioni mai vere). Funziona anche senza rete |
| `modrinth_resolve.py <pack> <voci…>` | Sceglie le versioni Modrinth: `slug` = ultima release per Minecraft e loader del pack; `slug@versione` o link = versione esatta |
| `ci_pack.sh <pack>` | Tutti i controlli in fila (refresh, check_pack, inventario, check_ids), usato dai workflow |
| `ci_commit.sh "<messaggio>"` | Commit e push dei file rigenerati dai workflow |

## Workflow di GitHub (`.github/workflows/`)

| Workflow | Quando parte | Cosa fa |
|---|---|---|
| **Controllo pack** (`check.yml`) | A ogni push su `main` o `dev` e a ogni pull request | `ci_pack.sh`: indice, controlli, inventario, controllo dei nomi. Salva indice, inventario e `controllo.md` con un commit automatico (non sulle pull request), poi fallisce se un controllo è fallito |
| **Aggiungi mod Modrinth** (`modrinth-add.yml`) | A mano, sul ramo scelto (`gh workflow run modrinth-add.yml --ref dev -f mods="…"`) | Sceglie le versioni (`modrinth_resolve.py`), le aggiunge con `packwiz modrinth add` insieme alle dipendenze obbligatorie, lancia `ci_pack.sh` e fa il commit elencando versioni scelte e metafile nuovi |
| **Aggiungi mod CurseForge** (`curseforge-add.yml`) | A mano, sul ramo scelto (scheda *Actions* → *Run workflow*) | Aggiunge una o più mod dai link ai file esatti (`…/files/<id>`), rifiutando le dipendenze, poi lancia `ci_pack.sh` e fa il commit |
| **Release** (`release.yml`) | Al push di un tag `<versione MC>-vX.Y.Z`, oppure a mano indicando il tag da creare | Controlla che il tag corrisponda a `pack.toml`, esporta un `.mrpack` con le sole mod Modrinth, crea lo zip della documentazione e pubblica la release |

packwiz viene installato in ogni workflow con `go install` a un commit fissato. I workflow che fanno commit girano uno alla volta per ramo; i loro commit non fanno ripartire altri workflow (regola di GitHub), per questo ognuno lancia da sé tutti i controlli. Le dipendenze di una mod CurseForge si rifiutano perché packwiz riconosce come "già presenti" solo le mod prese da CurseForge, e aggiungerebbe doppioni di quelle prese da Modrinth.

## Rilasciare una versione

Si lavora sul ramo **`dev`**, seguito dall'istanza di prova. **`main`** riceve solo versioni provate.

1. Su `dev`: aggiorna `version` in `<versione>/pack/pack.toml` (e `[versions]` se cambia NeoForge).
2. Aggiungi la voce in `<versione>/CHANGELOG.md`: titolo `## X.Y.Z — data`, versione di NeoForge, se serve un mondo nuovo, cosa cambia, **Stato**: 🧪 in prova su `dev`.
3. Rigenera l'indice e lancia i controlli, poi commit e push su `dev`. Aspetta che il **Controllo pack** sia verde (e, se ha fatto un commit automatico, scarica l'aggiornamento).
4. **Prova** nell'istanza che segue `dev` (dopo circa 5 minuti, per la cache di GitHub): avvio, mondo nuovo, log. Ogni problema nuovo, anche minore, va in `<versione>/docs/bug-report.md` con un codice nuovo; nella voce del CHANGELOG si aggiornano **Stato** (provata, data, tag) e **Problemi noti** (codici).
5. Se la prova passa, unisci `dev` in `main` con un merge vero, che conserva il grafico dei rami: `git checkout main && git merge --no-ff dev -m "Versione X.Y.Z" && git push`, poi torna su `dev`.
6. Crea il tag su `main`, in uno dei due modi:
   - **dal computer**: `git tag 1.21.1-vX.Y.Z && git push origin 1.21.1-vX.Y.Z`;
   - **da GitHub** (è il modo che usa Claude, che non può mandare tag): scheda *Actions* → **Release** → *Run workflow*, scrivendo il tag. Il workflow crea il tag sull'ultimo commit di `main` e rifiuta un tag già esistente.
7. Il workflow **Release** pubblica i file. Le versioni **0.x** escono come *pre-release* (tappe di prova); il mondo vero parte dalla **1.0.0** e si aggiorna cambiando il tag nel suo indirizzo.

I tag di release non si spostano e non si cancellano: per correggere una versione se ne fa una nuova.

Documenti e workflow possono andare su `main` anche senza una versione, con lo stesso merge, ma solo se su `dev` non c'è una tappa in corso. Mod, config e datapack arrivano su `main` solo con una versione.

## Mod solo CurseForge

Il `.mrpack` pubblico non le contiene, perché `packwiz modrinth export` le includerebbe come file e ridistribuirle non è permesso. Le note della release le elencano con il link al file esatto. Nelle istanze collegate al repository le scarica packwiz-installer.
