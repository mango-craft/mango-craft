# Revisione 2026.11-01 — diario

Il piano è in [piano.md](piano.md). Le voci sono in ordine di tempo; la più recente è in fondo.

---

## 02/11/2026 — Nota, nome e ossatura

- **Agente:** claude-code (claude-opus-5-5)
- **Richiesta di Matteo:** «Salva questa tua nota a parte, e creiamo un repository a fianco a questo con un AGENTS.md basico e l'ossatura di base comune a questo e l'altro repository. I dettagli sul perimetro da trattare specifico lo vedremo là. Però, come chiamiamo la mod? mango-?»
- **Nome:** proposti `mango-smithing` (consigliato), `mango-forgia`, `mango-tempra`, `mango-anvil`; scartato `mango-forge`. Matteo sceglie `mango-smithing`.
- **Controlli:** `mango-craft` su GitHub è un'organizzazione (un repository pubblico); il token della sessione vale solo per questo repository, quindi il repository nuovo su GitHub lo crea Matteo. In WSL non ci sono Java né Gradle (verificato il 02/11).
- **Fatto:** nota nello stage; ossatura del repository nuovo scritta e committata (primo commit su `main`, ramo `dev` uguale, remoto `origin` sull'alias `github-mango-smithing`); `claude-session` reso uguale per i due (`shellcheck` pulito); qui le regole della sezione 10 di `AGENTS.md`, la trappola di `git push` con `git -C` (vista il 31/10) in `ai-agents/README.md`, la decisione in `0503`.

## 02/11/2026 — La conoscenza passa alla mod, qui la nota

- **Agente:** claude-code (claude-opus-5-5)
- **Richiesta di Matteo:** «Al momento quello rimane come repo a parte, e vediamo con che tempi lo sviluppo, comunque non è bloccante. Qui deve rimanere solo la nota che questo miglioramento è demandato ad una mod in sviluppo. Pensi ci sia altro contesto utile da passare all'altro repo sotto forma di documenti?»
- **Il primo push non c'è stato:** la chiave caricata da `claude-session` era scaduta (12 ore), «The agent has no identities». Resta da fare con una sessione nuova.
- **Diviso così:** a mango-smithing la valutazione e la conoscenza per la mod (Truly Modular, Next Level, Tetra, Apotheosis, alternative, perimetro proposto, domande, prove, la valutazione del 23/10 sui gradini), riscritta come schede con le fonti; qui i fatti sui materiali delle mod del pack, che usano anche fornaci, B05 e il vincolo sugli id prima del mondo vero. Riletto per l'occasione il sorgente di Next Level (32 upgrade, formato, comando, dipendenze di Gradle).
- **Correzione:** `0601` dava per Next Level «ultimo commit 7/2/2026, Miapi 2.2.1»: verificato il 31/10, ultimo commit il 19/10/2026, Miapi 2.3.6.
- **Controlli:** link relativi di mango-smithing tutti validi; nessun documento di mango-craft cita più le sezioni tolte.
