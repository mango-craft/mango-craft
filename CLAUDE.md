@AGENTS.md
@1.21.1/lavoro/0501-piano.md
@1.21.1/docs/0303-note-tecniche.md

## Solo per Claude

- Le regole sono in `AGENTS.md`; qui sono importati anche il piano (`0501`) e le note tecniche (`0303`), perché sono brevi e servono sempre. All'inizio di un lavoro leggi anche il bug report (`1.21.1/docs/0402-bug-report.md`) e il file della versione in corso (`1.21.1/lavoro/versioni/`, quella con stato 🔧 o 📋 nel README); i temi aperti (`1.21.1/lavoro/0503-temi-aperti.md`) quando si decide cosa fare dopo. Le schede di `1.21.1/mod-knowledge/` si leggono quando si tocca una mod o un tema; lo stage (`ai-agents/stage/`) quasi mai. Gli altri documenti solo se servono (indici nei `README.md` delle cartelle).
- Il progetto Claude "Minecraft modpack" fa da bacheca su claude.ai e contiene un solo documento, `context.md`, **generato** dai documenti del repository con `python3 scripts/contesto_progetto.py 1.21.1` (non si scrive a mano). Rigeneralo e ricaricalo nel progetto (stesso percorso, `claude/context.md`) a ogni commit che cambia piano, changelog, bug report, mod, note tecniche, schede, temi aperti o il file della versione in corso.
