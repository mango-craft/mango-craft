@AGENTS.md
@1.21.1/lavoro/0501-piano.md
@1.21.1/docs/0303-note-tecniche.md
@ai-agents/contesto-locale.md

## Solo per Claude

- Le regole sono in `AGENTS.md`; qui sono importati anche il piano (`0501`), le note tecniche (`0303`) e il contesto locale, perché sono brevi e servono sempre. All'inizio di un lavoro leggi anche il bug report (`1.21.1/docs/0402-bug-report.md`), il file della versione in corso (`1.21.1/lavoro/versioni/`, quella con stato 🔧 o 📋 nel README) e, se ce n'è una aperta, la revisione in corso (`revisioni/README.md`); i temi aperti (`1.21.1/lavoro/0503-temi-aperti.md`) quando si decide cosa fare dopo. Le schede di `1.21.1/mod-knowledge/` (una per mod) e di `1.21.1/theme-knowledge/` (una per tema) si leggono quando si tocca una mod o un tema; l'archivio (`ai-agents/archivio/`) quasi mai. Gli altri documenti solo se servono (indici nei `README.md` delle cartelle).
- **Contesto locale, non versionato**: tutto ciò che riguarda il PC di Matteo (percorso dell'istanza di Prism e dei suoi log, come si lancia Python, strumenti installati, preferenze della sessione) sta in `ai-agents/contesto-locale.md`, importato qui sopra e in `.gitignore`. Non va mai copiato in file versionati (repository pubblico, `AGENTS.md` sezione 8). Se manca, copiarlo dal modello `ai-agents/contesto-locale.esempio.md` e chiedere a Matteo i valori prima di cercare l'istanza.
- **Sessione e permessi**: Matteo apre la sessione con `ai-agents/bin/claude-session`; permessi e sandbox in `.claude/settings.json` (non si modifica senza chiedere), le regole con percorsi del PC in `.claude/settings.local.json` (`ai-agents/README.md`).
- **File di appoggio**: quelli che servono solo a Claude durante la sessione vanno nella cartella temporanea della sessione; nello stage (`ai-agents/stage/`) solo ciò che Matteo deve leggere.
- **Memoria automatica** di Claude Code (fuori dal repository): solo per come lavorare con Matteo. Un fatto del pack, una decisione o un percorso del PC vanno nel loro posto (`AGENTS.md` sezione 4, contesto locale), non nella memoria.
