# FallingTree

Aggiornata il 19/10/2026 · nel pack dalla 0.1.1 (ruolo e licenza: `../docs/0301-mod.md`; versione: `../docs/0403-distinta-mod.md`) · fonti: sorgente della mod (ricerca del 19/10, materiale grezzo in `../../ai-agents/stage/2026-10-19_1.21.1-v0.6.0_config-mod/`).

- Versione 1.21.1.11. Config `config/fallingtree.json` (Gson, letto da entrambi i lati; il server lo sincronizza al client): `sneakMode`, di serie `SNEAK_DISABLE` (abbatte l'albero intero sempre, tranne accovacciati); `SNEAK_ENABLE` lo abbatte **solo** da accovacciati; `IGNORE` sempre. Un file parziale funziona se il JSON è valido (i campi mancanti tengono il valore di serie, il file viene riscritto).
- Decisione del 19/10: `sneakMode = SNEAK_ENABLE` (un colpo normale rompe un solo tronco, accovacciati cade l'albero intero; stesso principio per cui sono stati scartati i mod che scavano una vena in un colpo, `../lavoro/0602-mod-scartate.md`). Nel pack dalla 0.6.0 (provata il 21/10, `../lavoro/versioni/v0.6.0.md`): file completo copiato dall'istanza di prova, cambiata solo quella chiave. Le altre (`maxSize` 100, `breakMode` `INSTANTANEOUS`, `leavesBreaking` `true`, `treeBreaking` `true`…) restano di serie.
