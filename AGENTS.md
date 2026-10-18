# Guida per gli agenti — Mango Craft

Istruzioni per qualsiasi agente AI che lavora su questo repository (standard aperto `AGENTS.md`). Contiene le regole stabili. Lo **stato attuale** del progetto (mod, decisioni aperte, test da fare) è in [`1.21.1/docs/context.md`](1.21.1/docs/context.md): **leggilo prima di iniziare** (almeno le sezioni 2, 3 e 7: è lungo).

---

## 1. Cos'è

Modpack **personale, single player**, per Minecraft **1.21.1 NeoForge**, giocato con **Prism Launcher**. Il proprietario (Matteo) decide **mod per mod**: un agente propone, verifica e prepara, non aggiunge niente senza approvazione esplicita.

Temi del pack: cucina (Farmer's Delight e addon), agricoltura (Botany Pots, Let's Do, stagioni), tech (Create, Mekanism), esplorazione (strutture, dimensioni, boss), magia (Ars Nouveau, Occultism…), decorazione.

## 2. Come rispondere

- **Italiano**, conciso, leggibile da telefono: frasi brevi, elenchi solo quando servono, niente gergo tecnico non spiegato.
- **Verificare prima di affermare**: versioni, compatibilità, licenze e dipendenze si controllano nelle fonti (API di Modrinth, codice sorgente della mod, file del pack), non a memoria. Se una cosa non si è potuta verificare, dirlo.
- **Proporre con una raccomandazione chiara** (🟢 consigliata · 🟡 dipende · 🔴 sconsigliata) e lasciare la scelta a Matteo.
- **Errori**: se un'affermazione precedente era sbagliata, correggerla esplicitamente.

## 3. Struttura del repository

```
README.md · LICENSE · AGENTS.md (questa guida) · CLAUDE.md (importa questa guida)
docs/                       guide comuni: prism.md (istanze), sviluppo.md (aggiungere mod, rilasciare)
scripts/                    risoluzione mod, controllo datapack, generatori
.github/workflows/          controllo a ogni modifica + release dai tag
1.21.1/
├── CHANGELOG.md            cosa cambia in ogni versione, se serve un mondo nuovo, versione di NeoForge
├── docs/                   context.md, bug-report.md, log delle decisioni, verifica versioni, valutazioni/, datapack/
├── data/                   dati grezzi delle ricerche (inventari, bozze)
└── pack/                   SOLO ciò che finisce nel gioco: pack.toml, index.toml, mods/*.pw.toml, config/…
    └── config/paxi/datapacks/matteo_tweaks/   il datapack del pack
```

Tutto ciò che sta fuori da `pack/` non viene mai installato.

## 4. Versioni, tag e istanze

- **Rami**: si lavora su **`dev`**. **`main`** contiene solo versioni provate: riceve `dev` con un **merge vero** (`git merge --no-ff dev`: niente fast-forward, per conservare il grafico dei rami; niente pull request) quando la tappa è stata provata nell'istanza di prova e Matteo dà l'ok. Niente commit diretti su `main`; se capitasse (es. un commit automatico), si riporta `main` dentro `dev`.
- **Cosa va su `main` e quando**: mod, config e datapack solo con una versione e il suo tag. Documenti e workflow anche senza versione, con lo stesso merge, ma solo se su `dev` non c'è una tappa in corso (altrimenti aspettano la versione).
- **Versioni**: ogni versione rilasciata è un **tag** `<versione MC>-v<versione pack>` creato su `main`, es. `1.21.1-v0.3.0`. I tag di release non si spostano e non si cancellano. Le **0.x** sono tappe di prova (pre-release su GitHub); il **mondo vero parte dalla 1.0.0**. Il piano delle tappe è in `context.md` (3.0).
- **Istanze di Prism** (tutte con `packwiz-installer-bootstrap.jar` nella cartella `minecraft/` dell'istanza e comando prima dell'avvio `"$INST_JAVA" -jar packwiz-installer-bootstrap.jar <URL>`):
  - prova → `https://raw.githubusercontent.com/mango-craft/mango-craft/refs/heads/dev/1.21.1/pack/pack.toml`
  - mondo vero → `…/refs/tags/1.21.1-vX.Y.Z/1.21.1/pack/pack.toml` (si aggiorna cambiando il tag, dopo un backup del mondo)
  - archivio → un tag vecchio, con `--bootstrap-no-update` dopo il primo avvio
- **NeoForge si imposta a mano in Prism**: packwiz-installer non riesce a cambiarlo. Ogni voce del CHANGELOG indica la versione richiesta.
- Le mod di queste istanze **non si toccano dalla scheda Mod di Prism**: si modifica il repository.
- GitHub tiene in cache i file grezzi per circa 5 minuti: dopo un push, aspettare prima di avviare.
- **Prova di una tappa**: leggere i log dell'istanza dev e confrontarli con quelli della versione precedente. **Ogni problema nuovo, anche minore** (errori nel log, grafica mancante, ricette rotte, avvisi del controllo dei nomi), va nel **bug report** (`1.21.1/docs/bug-report.md`) con un codice nuovo `Bnn` che non si riusa mai. Prima del merge, la voce della versione nel **CHANGELOG** riceve **Stato** (provata, data, tag) e **Problemi noti** (i codici comparsi o risolti). Quando un problema si risolve, la riga passa tra i risolti con la versione che lo chiude.

## 5. Aggiungere o cambiare una mod

1. Approvazione esplicita di Matteo.
2. **Mod da Modrinth**: workflow **Aggiungi mod Modrinth** sul ramo `dev` (`gh workflow run modrinth-add.yml --ref dev -f mods="slug1 slug2@versione …"`). Sceglie l'ultima **release** per 1.21.1 + NeoForge (o la versione indicata), la aggiunge con `packwiz modrinth add` (versione, hash e dipendenze obbligatorie presi da Modrinth) e nel commit elenca versioni, tipo e data scelti e i metafile nuovi (le dipendenze sono **librerie nuove** da segnalare).
3. **Controllo automatico** (in ogni workflow che tocca il pack): indice, metafile, **inventario** dei .jar (`<versione>/data/inventario/`) e **controllo dei nomi** (`controllo.md`: dipendenze mancanti, nomi del datapack inesistenti). Se fallisce, leggere `controllo.md` nel ramo: i log dei workflow non sono leggibili da qui.
4. A mano, solo se il workflow non si può usare: versione dall'API di Modrinth (`/v2/project/<slug>/version?game_versions=["1.21.1"]&loaders=["neoforge"]`), hash verificati con la ricerca inversa `/v2/version_file/<sha512>?algorithm=sha512` (stessa versione, stesso sha1; gli hash lunghi vanno letti a pezzi), metafile scritto a mano (formato in `docs/sviluppo.md`), indice con `python3 scripts/packwiz_index.py 1.21.1/pack`, controllo con `python3 scripts/check_pack.py 1.21.1/pack`.
5. Licenza, data, se genera mondo o strutture (⚠️ = va aggiunta **prima del mondo vero**).
6. Aggiornare `docs/verifica-versioni.md`, `CHANGELOG.md` (voce della versione in corso), `context.md` e, se la mod porta problemi noti, `docs/bug-report.md`.
7. **Mod solo CurseForge**: si aggiungono con il workflow **Aggiungi mod CurseForge** (link al file esatto, `…/files/<id>`), che usa `packwiz curseforge add` rifiutando le dipendenze (sono già nel pack da Modrinth). I .jar non entrano mai nel repository. Quelle con distribuzione bloccata vanno scaricate a mano: l'installer mostra pagina e percorso.

## 6. Regole del datapack `matteo_tweaks`

- **Niente datapack esterni**: tutto nel nostro. Si copia solo da licenze che lo permettono (MIT, LGPL), citando la fonte nel readme della cartella; le ARR solo come confronto.
- Ogni file ha una **condizione di caricamento** (`neoforge:conditions` con `mod_loaded`/`item_exists`, oppure `bookshelf:load_conditions` con `block_exists`): togliere una mod non deve dare errori.
- Dentro `data/` **tutti i nomi in minuscolo**: un `README.md` maiuscolo lì dentro dà "Invalid path in pack". I readme si chiamano `readme.md`.
- Paxi carica il pacchetto in tutti i mondi, sopra gli altri (vince sui file con lo stesso percorso).
- `global_loot_modifiers.json` di NeoForge: un modificatore non elencato è spento; un nome elencato senza file dà errore.
- Le lune di Enhanced Celestials si ricaricano solo riaprendo il mondo; il resto con `/reload`. I modificatori di struttura (es. Berserker) richiedono il riavvio del mondo.
- Piano e formati dettagliati: `1.21.1/docs/datapack/` (conoscenze, copertura dei vasi).

## 7. Cose da non rompere (lezioni imparate)

- **NeoForge fermo a 21.1.259**: dalla 21.1.261 owo-lib 0.12.15.5 (dentro l'Aether) fa cadere la connessione all'ingresso nel mondo. Si torna all'ultimo NeoForge solo quando esce owo-lib 0.12.15.6.
- **Esperienza liquida**: quella di Create: Enchantment Industry vale 1 mB per punto e non è `c:experience`; le altre (Cognition, Sophisticated) valgono 20 mB e sono `c:experience`. **Mai** mettere il liquido di Create in `c:experience`, **mai** aggiungerlo agli `AllowedFluids` di Cognition. L'incantatore di Create accetta solo il proprio liquido.
- **Regions Unexplored 0.6** usa Lithostitched (non TerraBlender), ha 4 biomi nel Nether e ha rinominato alcuni blocchi: Botany Pots usa ancora 8 nomi vecchi.
- **Frantumatore di Occultism**: lasciato ai valori di default per scelta.
- **Starcatcher**: i pesci crudi sono `c:foods/raw_fish`; il pesce cotto è generico (`starcatcher:cooked_starcaught_fish`) e lo mettiamo noi nelle etichette del pesce cotto (datapack, dalla 0.3.0).
- **Botany Pots 1.21.1**: le ricette in formato 1.20 vengono ignorate; le piante raccolte col click destro richiedono raccolti espliciti.

## 8. Ambiente di lavoro di Claude

- Lo spazio di lavoro raggiunge **solo GitHub** dalla riga di comando. L'API di Modrinth si legge con lo strumento web. **CurseForge non è raggiungibile**: i suoi dati si ricavano dalle pagine o dalla build di GitHub.
- Compilare ed eseguire codice scaricato (packwiz compreso) **non è permesso** qui: i file di packwiz si scrivono con script propri, e packwiz vero gira nelle GitHub Actions.
- Quello che da qui non si raggiunge (Modrinth, CDN, Maven) lo fanno i workflow, che salvano i risultati nel repository: l'**inventario** in `<versione>/data/inventario/` dice cosa contiene ogni .jar (oggetti, blocchi, tag, tabelle del bottino, strutture, ricette di Botany Pots, dipendenze). Usarlo prima di scrivere nomi nel datapack; `python3 scripts/check_ids.py <pack> <inventario>` lo verifica anche in locale.
- I log del gioco dell'istanza di prova si leggono dal PC di Matteo (solo la cartella `logs` dell'istanza dev, accesso concesso da lui) quando la sessione è collegata.
- Da qui si possono mandare commit sui rami (`dev`, e `main` tramite merge) e avviare i workflow (`gh workflow run`), ma **non mandare tag** né scrivere tramite l'API di GitHub (pull request mai provate): per una release si usa il workflow **Release** con il tag come parametro. I log dei workflow non sono leggibili da qui: si controlla l'esito (`gh run view`) e il risultato (i file nel repository).
- Il PC di Matteo può essere collegato alla sessione: **non toccare la cartella di Prism senza il suo via**.
- Repository **pubblico**: niente dati personali (percorsi locali, email, nomi utente del PC) nei file.

## 9. Documenti

| Dove | Cosa |
|---|---|
| `1.21.1/docs/context.md` | Stato del progetto: mod per categoria, test da fare, config, log |
| `1.21.1/docs/bug-report.md` | Tutti i problemi trovati, anche minori, con codice, versione, effetto e piano |
| `1.21.1/docs/decisioni/` | Log delle decisioni per round (approvate, scartate, da tenere d'occhio) |
| `1.21.1/docs/verifica-versioni.md` | Versione, data, licenza ed esito di ogni mod |
| `1.21.1/docs/valutazioni/` | Ricerche (Nether, animali, esperienza, confronti con altri modpack…) |
| `1.21.1/docs/datapack/` | Piano, formati, copertura dei vasi, fonti e licenze |
| `1.21.1/CHANGELOG.md` | Una voce per versione: stato, NeoForge, mondo nuovo, cosa cambia, problemi noti (codici del bug report). Diventa la nota della release |
| `docs/prism.md` | Come collegare le istanze di Prism |
| `docs/sviluppo.md` | Formati, script, workflow, come si rilascia |

Il progetto Claude "Minecraft modpack" tiene una copia di `context.md` come bacheca: quando cambia qui, va aggiornata anche lì.
