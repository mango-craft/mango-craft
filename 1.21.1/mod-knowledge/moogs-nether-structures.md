# Moog's Nether Structures (+ Moog's Structure Lib)

Aggiornata il 19/10/2026 · nel pack dalla 0.5.0: Moog's Nether Structures 3.1.1, Moog's Structure Lib 3.4.2 (`../docs/0403-distinta-mod.md`) · fonti: sorgenti (tag `3.1.1-1.21` e `3.4.2-neoforge`), log dell'istanza di prova.

## Cose da non rompere

- Richiede Moog's Structure Lib **≥ 3.3.0**: con la 3.0.3 il gioco non partiva (B28). packwiz non aggiorna una libreria già presente: il controllo dei nomi ora lo segnala (scheda `../theme-knowledge/neoforge.md` per la regola generale).
- La sostituzione della fortezza vanilla con la mega-fortezza è **spenta di serie e deve restare così**: la fortezza la rifà YUNG's (e i Berserker di Cataclysm dipendono da quella: `cataclysm.md`).

## Fatti verificati

- 52 strutture fino alla mega-fortezza. Config globale scritta dalla libreria: `config/moogs_structures.json`, `presets.mns.replace_nether_fortress` = `false` (preset dichiarato in `data/mns/moogs_structures/replace_vanilla.json`, letto da `MslConfig.loadAndSync`). Con il preset spento la mega-fortezza genera comunque come gruppo proprio più raro (`mns:mega_fortress`, spacing 116 / separation 76 prima del ×1,65 della libreria). Nessun file nel pack.
- I moltiplicatori di frequenza della libreria (`frequency.*`) e Sparse Structures sui gruppi di Moog's: come si sommano non è stato analizzato.
- Prova nel mondo di prova: `/locate structure betterfortresses:fortress` e `mns:mega_fortress`.
