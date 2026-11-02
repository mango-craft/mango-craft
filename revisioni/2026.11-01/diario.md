# Revisione 2026.11-01 — diario

Il piano è in [piano.md](piano.md). Le voci sono in ordine di tempo; la più recente è in fondo.

---

## 02/11/2026 — Nota, nome e ossatura

- **Agente:** claude-code (claude-opus-5-5)
- **Richiesta di Matteo:** «Salva questa tua nota a parte, e creiamo un repository a fianco a questo con un AGENTS.md basico e l'ossatura di base comune a questo e l'altro repository. I dettagli sul perimetro da trattare specifico lo vedremo là. Però, come chiamiamo la mod? mango-?»
- **Nome:** proposti `mango-smithing` (consigliato), `mango-forgia`, `mango-tempra`, `mango-anvil`; scartato `mango-forge`. Matteo sceglie `mango-smithing`.
- **Controlli:** `mango-craft` su GitHub è un'organizzazione (un repository pubblico); il token della sessione vale solo per questo repository, quindi il repository nuovo su GitHub lo crea Matteo. In WSL non ci sono Java né Gradle (verificato il 02/11).
- **Fatto:** nota nello stage; ossatura del repository nuovo scritta e committata (primo commit su `main`, ramo `dev` uguale, remoto `origin` sull'alias `github-mango-smithing`); `claude-session` reso uguale per i due (`shellcheck` pulito); qui le regole della sezione 10 di `AGENTS.md`, la trappola di `git push` con `git -C` (vista il 31/10) in `ai-agents/README.md`, la decisione in `0503`.
