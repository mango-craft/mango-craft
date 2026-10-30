# Subtle Effects

Aggiornata il 19/10/2026 · nel pack dalla 0.1.1 (ruolo e licenza: `../docs/0301-mod.md`; versione: `../docs/0403-distinta-mod.md`) · fonti: sorgente della mod (ricerca del 19/10, materiale grezzo in `../../ai-agents/archivio/2026-10-19_1.21.1-v0.6.0_config-mod/`).

- Versione 1.15.0, config con Fzzy Config 0.7.7, solo client: `config/subtle_effects/blocks.toml`, `rainWaterRipples` (`true` di serie) e `rainWaterRipplesDensity` (0.35). Un file parziale funziona: Fzzy segnala le chiavi mancanti e riscrive il file completo.
- Riconosce Particle Rain solo per la sua particella di nebbia: nessuna gestione automatica delle increspature. Se in gioco le increspature della pioggia compaiono doppie con Particle Rain, spegnere `rainWaterRipples` (non verificato che succeda).
- Con alcuni pacchetti di shader certi effetti non si vedono (`../theme-knowledge/shader.md`).
