# Contesto locale — modello

Modello del file `ai-agents/contesto-locale.md`, che resta **fuori da git** (`.gitignore`) perché contiene i percorsi del PC e il repository è pubblico. Per crearlo: copiare questo file con quel nome e sostituire i valori tra `<…>`. Claude Code lo carica da solo (import in `CLAUDE.md`); gli altri agenti lo leggono perché lo dice `AGENTS.md`, sezione 8. Lo gestisce Matteo; un agente lo aggiorna solo quando Matteo gli dice un fatto nuovo del PC.

Mai segreti qui dentro: né token né password né chiavi.

## Prism Launcher

- Cartella di Prism, vista da WSL: `<es. /mnt/<disco>/…/PrismLauncher>`
- Istanza di prova, che segue `dev`: `<cartella di Prism>/instances/<nome>/minecraft/`
- Log dell'istanza di prova: `…/minecraft/logs/` (`latest.log`, gli avvii precedenti come `AAAA-MM-GG-N.log.gz`, `kubejs/`, il dump in `mango-craft-dump/`)
- Istanza del mondo vero: `<nome, o «non ancora creata»>`
- File da non leggere mai: `<cartella di Prism>/accounts.json` (credenziali dell'account Microsoft)

## Strumenti sul PC

- Sistema: `<es. Fedora Linux in WSL 2>`
- Python: `<comando e versione, es. python3 3.14>`
- `gh`: `<installato e come si autentica, o «non installato»>`
- `packwiz`: `<installato o no; non serve per aggiungere mod>`
- Altri: `<shellcheck, bwrap e socat per la sandbox…>`

## Git

- Remoto: `<alias SSH del remoto>`, con la deploy key `<~/.ssh/nome>` (la carica `ai-agents/bin/claude-session`)

## Preferenze della sessione

- `<eventuali preferenze di Matteo per il lavoro in locale>`
