# ai-agents

Ciò che serve agli agenti AI che lavorano sul repository e ciò che lasciano. Le regole sono in [`AGENTS.md`](../AGENTS.md) (sezioni 4, 8 e 9); i permessi di Claude Code in [`.claude/settings.json`](../.claude/settings.json), nella radice: Claude Code li legge solo da lì.

```
ai-agents/
├── bin/
│   └── claude-session            apre la sessione di Claude Code con le credenziali solo in memoria
├── contesto-locale.esempio.md    modello del contesto locale
├── contesto-locale.md            il contesto locale del PC (fuori da git)
├── stage/                        file di lavoro per Matteo (fuori da git, tranne il README)
└── archivio/                     lo stage versionato fino al 29/10/2026: fermo
```

## La sessione

Dalla radice del repository:

```bash
ai-agents/bin/claude-session                 # la deploy key di GitHub, per il push
ai-agents/bin/claude-session --gh            # in più: un token di GitHub per gh (workflow)
ai-agents/bin/claude-session --continue      # le altre opzioni passano a claude
```

Lo script carica la deploy key `~/.ssh/github_mango_craft` (o quella in `MANGO_GITHUB_KEY`) in un agent SSH dedicato, che muore con la sessione (al più tardi dopo 12 ore); un agent già aperto nel terminale non passa, perché potrebbe contenere la chiave personale. Con `--gh` chiede, senza mostrarlo, un token **fine-grained** limitato a questo repository, con il solo permesso Actions in lettura e scrittura (il push passa dalla deploy key), e lo tiene solo in memoria. Poi avvisa se manca il contesto locale, stampa cosa ha caricato (senza i valori) e avvia `claude`.

**Permessi** (`.claude/settings.json`, versionato; non si modifica senza chiederlo a Matteo): script, git e lettura degli esiti dei workflow senza conferma; **push, tag, merge, avvio di workflow e release chiedono sempre conferma**; `~/.ssh` non si legge. La **sandbox** è accesa: i comandi scrivono solo nel repository e nella cartella temporanea, e in rete raggiungono solo i domini elencati nei `WebFetch(domain:…)`; `gh`, `git push`, `fetch` e `pull` girano fuori, e il token di GitHub è nascosto agli altri comandi. Le regole personali (la cartella di Prism non si modifica, `accounts.json` non si legge) stanno in `.claude/settings.local.json`, fuori da git perché contengono un percorso del PC; anche le approvazioni «non chiedere più» finiscono lì.

**Trappola della sandbox**: dentro la sandbox `git status` mostra nella radice e in `.claude/` file che non esistono (`.bashrc`, `.gitconfig`, `.mcp.json`, `.claude/hooks`…): sono `/dev/null` montati dalla sandbox per proteggere quei percorsi. Non si aggiungono mai: `git add` con i percorsi del lavoro fatto, non `git add -A` nella radice.

**Trappola di `gh`** (prova del 30/10/2026): `gh` gira fuori dalla sandbox, con il token, solo se il comando è `gh …` da solo. In una pipe (`gh … | tail`) o dopo `cd … &&` gira dentro, dove il token è nascosto, e risponde «not logged in». L'output si filtra dopo, non nello stesso comando.

**I workflow girano con la versione su GitHub**, non con quella locale: un workflow cambiato in un commit non ancora mandato parte nella versione vecchia (successo il 30/10/2026: un commit nello stage che la versione nuova non faceva più). Prima si fa il push, poi si lancia.

## Contesto locale

`contesto-locale.md` dice com'è fatto il PC: dove sta l'istanza di Prism e i suoi log, come si lancia Python, quali strumenti ci sono. Sta **fuori da git** perché il repository è pubblico; il modello versionato è `contesto-locale.esempio.md`. Claude Code lo carica da solo (import in [`CLAUDE.md`](../CLAUDE.md)); gli altri agenti lo leggono perché lo dice `AGENTS.md`. Lo gestisce Matteo: un agente lo aggiorna solo con un fatto nuovo detto da lui o verificato sul PC. Mai segreti.

## stage/

Il posto per ciò che un agente produce **per Matteo** ma che non fa parte del progetto: risultati grezzi delle ricerche, esami delle mod (`python3 scripts/esamina.py`), confronti, bozze, output lunghi. Git lo ignora (resta tracciato solo il suo README).

- **Un file o una cartella per lavoro**, con la data davanti: `AAAA-MM-GG-argomento.md`, o `AAAA-MM-GG-argomento/` se i file sono più d'uno (es. `2026-11-02-esame-mod/`).
- **Nessun file del progetto vi rimanda.** Ciò che deve restare (un fatto verificato, una valutazione, una decisione) va nel suo posto: file della versione, scheda della mod o del tema, revisione. Il distillato deve reggersi da solo, con le sue fonti (API di Modrinth, sorgente, inventario, dump), perché lo stage su GitHub non c'è.
- **Mai segreti**, nemmeno qui.
- **Si svuota a mano**, quando un lavoro è chiuso: lo decide Matteo; gli agenti non cancellano niente da `stage/` senza chiederglielo.
- **Non è il posto del filo di un lavoro.** Un lavoro sul repository con decisioni e più passaggi è una revisione, in [`../revisioni/`](../revisioni/README.md); il lavoro di una versione del pack sta nel suo file in `<versione>/lavoro/versioni/`.

I file che servono solo all'agente durante una sessione (output intermedi, script di prova) non vanno qui ma nella cartella temporanea della sessione: `stage/` è per ciò che Matteo deve leggere.

Gli esami delle mod fuori dal pack si fanno in locale con `scripts/esamina.py` (comando in [`docs/0201-sviluppo.md`](../docs/0201-sviluppo.md)), con il risultato qui; il workflow Esamina mod non c'è più dal 30/10/2026.

## archivio/

Lo stage come era fino al 29/10/2026, quando era versionato: una cartella per ricerca, `<data>_<versione di Minecraft>-v<versione del pack>_<nome>/` (senza il segmento della versione quando la ricerca non riguardava una versione del pack), con report, tabelle, estratti di sorgenti e script, nella lingua in cui sono nati. I file delle versioni e le schede ci rimandano.

- È **fermo**: non si aggiunge, non si modifica, non si cancella.
- **Non è una fonte per lo stato attuale**: descrive un momento. Lo stato del pack è in `<versione>/docs/`, la conoscenza sulle mod in `<versione>/mod-knowledge/` e sui temi in `<versione>/theme-knowledge/`, il lavoro di ogni versione in `<versione>/lavoro/versioni/`.
- Non ha un indice: il nome della cartella dice data, versione e argomento.
