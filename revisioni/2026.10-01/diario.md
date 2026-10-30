# Revisione 2026.10-01 — diario

Il piano è in [piano.md](piano.md). Le voci sono in ordine di tempo; la più recente è in fondo.

---

## 29/10/2026 — La valutazione

- **Agente:** claude-code (claude-opus-5-5)
- **Richiesta di Matteo:** valutare lo stato del repository e a che punto siamo; riadattare la struttura al lavoro in locale; imitare l'altro repository del PC (`kmango-selfhost-vm`) nel lancio degli agenti e nella gestione dello stage; dire quali concetti di base esportare.
- **Letto dell'altro repository:** `AGENTS.md`, `ai-agents/README.md` (sessione, log, stage), `ai-agents/bin/claude-session`, `.claude/settings.json`, `reviews/README.md` e due revisioni.
- **Stato di questo:** controllo locale verde (266 metafile, 876 JSON del datapack, vasi, mercato e lista nera coerenti); `dev` allineato con GitHub e 6 commit avanti a `main`; 0.7.3 aperta con il solo punto 0 fatto. Ambiente locale incompleto: niente contesto locale, niente `gh` (i workflow non si lanciano da qui), niente permessi versionati. `packwiz` manca ma non serve.
- **Differenza di fondo:** qui lo stage era versionato, fermo e citato dai documenti (circa 60 rimandi in 45 file) come fonte; lì è locale e nessuno ci rimanda. Lì il repository è privato, qui pubblico.
- **Proposta:** sei punti più una domanda (le sessioni su claude.ai), nel piano.

## 29/10/2026 — Il contesto locale

- **Agente:** claude-code (claude-opus-5-5)
- Matteo chiede a cosa serve `CLAUDE.local.md`, se lo gestisce Claude e se non sia meglio in `ai-agents/` con un nome generico.
- **Verificato nella documentazione di Claude Code** (pagina sulla memoria, 29/10): Claude Code lo legge da solo all'avvio, dalla radice, dopo `CLAUDE.md`; non lo scrive e non lo mette in `.gitignore`. Un import `@percorso` dentro il progetto non chiede conferma (solo quelli esterni). Non è documentato cosa succede se il file importato manca: lo script di sessione avvisa, e `AGENTS.md` dice di chiedere a Matteo.
- **Decisione di Matteo:** in `ai-agents/`, nome generico.

## 29/10/2026 — Le modifiche

- **Agente:** claude-code (claude-opus-5-5)
- Matteo: «procedi con tutte le modifiche»; Prism su `Z:`. Verificato: `/mnt/z` è montato da WSL; un'istanza, `mango-craft-dev`, che segue `dev`, con i log e il dump (letti solo i nomi dei file e della cartella `logs/`).
- **Stage:** `git mv` dell'intera cartella in `ai-agents/archivio/`; i rimandi dei documenti cambiati con una sostituzione del solo percorso, anche nei file delle versioni chiuse (la regola «non si correggono a posteriori» riguarda il contenuto; lo stesso era stato fatto nel riordino del 19/10). Il contenuto dell'archivio non è stato toccato.
- **Esamina mod:** con lo stage fuori da git il workflow non poteva più salvarci con un commit: ora fa un artefatto, e in locale si usa direttamente `esamina.py`. Tolto lo stage da `ci_commit.sh` (e corretto lì un vecchio avviso di shellcheck, una variabile del ciclo non usata).
- **Permessi e sandbox:** le regole di sintassi verificate nella documentazione (pagine sui permessi e sulla sandbox, 29/10): l'ordine è deny, poi ask, poi allow; i percorsi assoluti si scrivono `//percorso`; i domini dei `WebFetch(domain:…)` valgono anche per la rete della sandbox; `sandbox.credentials.envVars` nasconde il token ai comandi nella sandbox, e `gh` gira fuori. La sandbox si è accesa già in questa sessione appena scritto il file: `~/.ssh` e `accounts.json` bloccati in lettura.
- **Trappola trovata:** dentro la sandbox `git status` mostra nella radice file come `.bashrc`, `.gitconfig`, `.mcp.json`: sono `/dev/null` montati dalla sandbox, non file veri. Annotata in `ai-agents/README.md`; i commit si fanno con i percorsi espliciti.
- **Commit:** «Lo stage versionato diventa ai-agents/archivio (solo percorsi)» e «Lavoro in locale: sessione, permessi e sandbox, contesto locale, stage fuori da git, revisioni».
- **Aperto:** le prove che può fare solo Matteo (piano, sezione 4); la domanda sulle sessioni su claude.ai; il push.

## 30/10/2026 — Le prove di GitHub e dei workflow

- **Agente:** claude-code (claude-opus-5-5)
- **Richiesta di Matteo:** «dovresti avere accesso sia a GitHub che alle action, fai qualche test». Sessione aperta con `--gh`, `gh` installato.
- **Riuscite:** `gh auth status` (token fine-grained), `gh workflow list`, `gh run list`, `gh run view --log`; `gh api …/actions/secrets` risponde 403, come deve; `git fetch`, `git ls-remote` e `git push --dry-run origin dev` (la deploy key può scrivere; niente mandato).
- **Trappola di `gh`:** con `cd … &&` o in una pipe `gh` gira nella sandbox, senza token, e dice «not logged in». Annotata in `ai-agents/README.md`.
- **Esamina mod** lanciato su `cc-tweaked@1ewzHZYg advancedperipherals@fxjzpAbL` (le mod della 0.7.3): è partita la versione su GitHub, ancora quella vecchia, perché i commit di questa revisione non erano mandati. Ha fatto un commit su `dev` (77517bd, i due esami in `ai-agents/stage/`) invece dell'artefatto. Esame identico a quello del 24/10 nell'archivio (stesse versioni): niente di nuovo per la 0.7.3.
- **Sistemato:** i 3 commit locali riportati sopra 77517bd. Il `git rebase` si è fermato: il commit della sessione crea `.claude/settings.json`, che c'era già sul disco (identico) e che la sandbox non lascia scrivere. I due commit rimasti ricostruiti con `git merge-tree` e `git commit-tree` senza toccare il disco; contenuto verificato uguale al `dev` di prima più i due file. Poi la cartella tolta da git: resta nello stage locale come `2026-10-30-esame-mod/`.
- **Aperto:** il push (con la conferma di Matteo); dopo, rilanciare Esamina mod per provare l'artefatto; `/context`.
