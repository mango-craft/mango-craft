# Revisione 2026.11-01 — Repository a fianco per Mango Smithing

**Stato**: ✅ chiusa il 02/11/2026 (aperta lo stesso giorno). Esito nella sezione 6. Il diario è in [diario.md](diario.md).

## 1. Obiettivo

Dopo il confronto con Tetra (31/10/2026; fatti in `1.21.1/theme-knowledge/strumenti.md`, strade in `1.21.1/lavoro/0503-temi-aperti.md`, sezione 5), Matteo ritiene che l'avanzamento degli strumenti alla Tetra richieda una **mod dedicata**, addon di Truly Modular. Questa revisione crea il suo repository accanto a questo, con un `AGENTS.md` di base e l'**ossatura comune** ai due. Il perimetro della mod non è qui: si decide nel repository nuovo, nella sua prima versione.

## 2. Decisioni

- **02/11/2026** — Matteo: la mod si fa, in un **repository a fianco**, con l'ossatura comune a questo; il perimetro si vede là.
- **02/11/2026** — Matteo: il nome è **Mango Smithing** (repository `mango-smithing`, nome tecnico `mango_smithing`). Scartato `mango-forge`, che si confonde con Forge e NeoForge.
- **02/11/2026** — **Ossatura comune**: le parti uguali o con la stessa forma sono elencate in `AGENTS.md`, sezione 10, di tutti e due; una modifica a una parte comune si fa in tutti e due. `claude-session` diventa uguale nei due: prende il nome della chiave e del repository dalla cartella.
- **02/11/2026** — Il repository nuovo è nell'organizzazione `mango-craft`, pubblico come questo, licenza MIT; ha la sua deploy key (`~/.ssh/github_mango_smithing`, alias SSH `github-mango-smithing`).
- **02/11/2026** — Matteo: il repository **resta a parte**, i tempi dello sviluppo si vedranno, **non è bloccante**. In mango-craft resta solo la nota che il miglioramento è demandato a una mod in sviluppo; la conoscenza utile alla mod passa là.
- **02/11/2026** — Restano in mango-craft i fatti sui **materiali delle mod del pack** (tema `strumenti`), perché servono anche alle fornaci, a B05 e al vincolo sugli id prima del mondo vero; passano a mango-smithing il confronto con Tetra, i fatti su Truly Modular, Next Level, Apotheosis con gli oggetti modulari, le alternative, il perimetro proposto e le prove da fare.

## 3. Lavoro

1. ✅ La nota sul perimetro proposto (31/10) salvata nello stage, con una copia di lavoro nello stage del repository nuovo.
2. ✅ Repository locale `mango-smithing` accanto a questo, rami `main` e `dev`: `AGENTS.md`, `CLAUDE.md`, `README.md`, `LICENSE`, `.gitignore`, `.gitattributes`, `.claude/settings.json`, `ai-agents/` (sessione, modello del contesto locale, stage), `docs/` (indice e `0001-progetto`), `lavoro/`, `revisioni/`. Contesto locale suo, fuori da git.
3. ✅ Qui: `claude-session` uguale per i due; `AGENTS.md` (repository a fianco, riga in «un fatto, un posto», sezione 10); `ai-agents/README.md` (chiave del repository, trappola di `git push` con `git -C`); decisione in `0503`, sezione 5; riga in `0501`; rimando nel tema degli strumenti.
4. ✅ Conoscenza passata a mango-smithing: schede `mod-knowledge/` (Truly Modular, Next Level, Tetra, Apotheosis) e `lavoro/0503-temi-aperti.md` (perché la mod, alternative, perimetro proposto, domande, sviluppo e prove, rischi, la valutazione del 23/10 sui gradini); rapporti grezzi del 31/10 copiati nel suo stage.
5. ✅ Qui solo la nota: tema `strumenti` senza le valutazioni (restano i fatti sui materiali), `0503` sezione 5 ridotta alla decisione e a cosa resta al pack, riga 6 della sezione 4, `0501` senza la 0.7.x degli strumenti, `0601` (Next Level, date corrette), rimandi in `0402`, `0502`, `fornaci`, indice dei temi.
6. ✅ Chiusura: esito qui sotto. GitHub e il primo push di mango-smithing sono in «Aperto».

## 4. Prove

- `shellcheck` pulito su `claude-session`; il nome della chiave ricavato dalla cartella dà `github_mango_craft` qui e `github_mango_smithing` là.
- Dopo il punto 4: una sessione aperta con `ai-agents/bin/claude-session` nel repository nuovo carica la sua chiave e il push riesce.

## 5. Aperto

- **GitHub** (Matteo, quando vuole): il repository vuoto `mango-craft/mango-smithing`, la deploy key con scrittura, l'alias SSH; poi il primo push di `main` e `dev` da una sessione aperta là.
- Il primo lavoro del repository nuovo è decidere il perimetro (versione 0.1.0 o un piano, lo decide Matteo là).

## 6. Esito

✅ Chiusa il 02/11/2026. Il repository `mango-smithing` esiste sul PC, con l'ossatura comune (sezione 10 di `AGENTS.md` nei due) e la conoscenza di partenza; su GitHub ancora no (punto aperto). In mango-craft gli strumenti a tappe sono una nota che rimanda alla mod.
