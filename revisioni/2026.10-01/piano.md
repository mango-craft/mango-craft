# Revisione 2026.10-01 — Lavoro in locale con Claude Code

**Stato**: 🔧 aperta il 29/10/2026. Modifiche fatte lo stesso giorno; restano le prove che può fare solo Matteo (sotto, «Prove») e i punti aperti. Il diario è in [diario.md](diario.md).

## 1. Obiettivo

Dal 29/10/2026 lo sviluppo si fa in locale, con Claude Code in WSL. Matteo chiede di valutare lo stato del repository e di riadattarne la struttura al lavoro in locale, prendendo dall'altro suo repository (`kmango-selfhost-vm`, privato) l'organizzazione del lancio degli agenti e la gestione dello stage, e i concetti di base utili anche qui.

Cosa si prende dall'altro repository e cosa no:

| Concetto | Lì | Qui |
|---|---|---|
| Script di sessione con le credenziali solo in memoria | `ai-agents/bin/claude-session` | ✅ stesso schema: deploy key di GitHub, token facoltativo per `gh` |
| Permessi e sandbox versionati | `.claude/settings.json` | ✅ con le conferme per push, tag, merge, workflow |
| Stage fuori da git, per Matteo, nessun rimando | `ai-agents/stage/` | ✅; lo stage versionato di prima diventa `ai-agents/archivio/`, fermo |
| Il filo di un lavoro con più passaggi | `reviews/AAAA.MM-NN/` (plan, log) | ✅ `revisioni/` (piano, diario), solo per il lavoro sul repository: per il pack ci sono già i file delle versioni |
| Autonomia a gradi e «modifica completa» | `AGENTS.md` | ✅ `AGENTS.md`, sezione 9 |
| Commento in testa ad `AGENTS.md` (sotto le 200 righe, solo regole) | `AGENTS.md` | ✅ |
| Log giornalieri (infrastruttura, PC, modifiche) | `ai-agents/logs/` | ❌ le modifiche le raccontano già file delle versioni, changelog e git; il PC lo descrive il contesto locale. Lì il repository è privato, qui pubblico |
| Registro delle decisioni architetturali | `docs/11-decisions.md` | ❌ qui le decisioni stanno nei file delle versioni e delle revisioni, le regole in `AGENTS.md` |

## 2. Decisioni

- **29/10/2026** — Matteo: si riadatta la struttura imitando l'altro repository per il lancio degli agenti e per lo stage.
- **29/10/2026** — Matteo: il contesto locale non è `CLAUDE.local.md` ma un file con nome generico in `ai-agents/` (`contesto-locale.md`, fuori da git), importato da `CLAUDE.md`, così lo trovano tutti gli agenti.
- **29/10/2026** — Matteo: «procedi con tutte le modifiche»: i sei punti della proposta (sessione; permessi e sandbox; stage fuori da git con l'archivio; revisioni; niente log giornalieri; autonomia e lavoro finito in `AGENTS.md`).
- **29/10/2026** — Matteo: Prism sta su Windows, in `Z:`, raggiungibile da WSL in `/mnt/z/` (percorso nel contesto locale).

## 3. Lavoro

1. ✅ `ai-agents/stage/` (23 cartelle) → `ai-agents/archivio/` con `git mv`; rimandi aggiornati in 41 file di `1.21.1/` e `docs/` (cambia solo il percorso, anche nei file delle versioni chiuse).
2. ✅ Stage nuovo fuori da git (`.gitignore`, resta il README); `.claude/settings.local.json` e `ai-agents/contesto-locale.md` in `.gitignore`.
3. ✅ Contesto locale: `ai-agents/contesto-locale.md` (Prism, istanza `mango-craft-dev`, log, strumenti, remoto) e il modello versionato `contesto-locale.esempio.md`; import in `CLAUDE.md`.
4. ✅ `ai-agents/bin/claude-session` (shellcheck pulito).
5. ✅ `.claude/settings.json` (permessi, sandbox, token nascosto ai comandi nella sandbox) e `.claude/settings.local.json` (cartella di Prism non modificabile, `accounts.json` non leggibile).
6. ✅ Workflow **Esamina mod**: artefatto invece del commit; `scripts/ci_commit.sh` non salva più lo stage; `esamina.py` gira anche in locale.
7. ✅ `revisioni/` con il suo README e questa revisione.
8. ✅ Documenti: `AGENTS.md` (sezioni 3, 4, 8, nuova 9, commento in testa), `CLAUDE.md`, `ai-agents/README.md`, `docs/0201-sviluppo.md`, `README.md`, `docs/README.md`, `1.21.1/lavoro/README.md`.

## 4. Prove

- [x] `bash scripts/controllo_locale.sh 1.21.1/pack` verde.
- [x] `shellcheck` pulito su `ai-agents/bin/claude-session` e `scripts/*.sh`.
- [x] Tutti i link relativi dei file Markdown versionati puntano a file esistenti (controllo con uno script, fuori dall'archivio).
- [x] La sandbox si accende: nella sessione del 29/10 `~/.ssh` e `accounts.json` risultano bloccati in lettura, la scrittura è limitata al repository.
- [x] (Matteo) Avvio con `ai-agents/bin/claude-session`: la chiave si carica e `git push` su `dev` funziona (fuori dalla sandbox, con conferma). Il 30/10: `git fetch`, `git ls-remote` e `git push --dry-run` riusciti (la chiave può scrivere); il primo push vero è quello di questa revisione.
- [x] (Matteo) `gh` installato (`sudo dnf install gh`), avvio con `--gh`: `gh run list` risponde. Il 30/10: elenco dei workflow e delle esecuzioni, log leggibili, lancio di un workflow riuscito; i segreti del repository rispondono 403 (il token non ha altri permessi). Solo con `gh` da solo nel comando (diario, 30/10).
- [ ] `/context` mostra `ai-agents/contesto-locale.md` tra i file di memoria.
- [x] Al primo uso, **Esamina mod** produce l'artefatto e `gh run download` lo porta nello stage. Il 30/10 la prima volta è partita la versione vecchia, perché i commit non erano ancora su GitHub; dopo il push l'artefatto c'è, si scarica, e nessun commit sul ramo (diario).

## 5. Aperto

- **Sessioni su claude.ai**: Matteo le usa ancora? Se no, la parte «Da claude.ai» di `AGENTS.md` (sezione 8) si riduce e il workflow Esamina mod si può togliere, perché in locale `esamina.py` basta.
- **Contesto caricato a ogni sessione**: circa 41 KB (`AGENTS.md` 21, `0501` 11, `0303` 8). Se cresce, la tabella delle tappe fatte di `0501` è il primo candidato a sparire (ripete changelog e indice delle versioni).
- **Merge in `main`**: aspetta la 0.7.3, perché su `dev` c'è una tappa in corso.

## 6. Esito

—
