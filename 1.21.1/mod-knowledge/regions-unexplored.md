# Regions Unexplored

Aggiornata il 19/10/2026 · nel pack dalla 0.2.3, versione 0.6 (`../docs/0403-distinta-mod.md`; ruolo: `../docs/0301-mod.md`) · fonti: sorgente della mod, inventario, controllo dei nomi. Decisione: `../lavoro/versioni/v0.2.3.md`.

## Fatti verificati

- La 0.6 usa **Lithostitched** (non TerraBlender). Verificato nel codice il 17/10 che non toglie strutture, minerali né colture selvatiche e che Dungeons and Taverns, When Dungeons Arise, Hexalia e Farmer's Delight la riconoscono. Genera i suoi biomi solo nei chunk nuovi: va aggiunta prima del mondo vero (fatto).
- **4 biomi nel Nether**: Mycotoxic Undergrowth (da Nether Wastes), Glistering Meadow (da Soul Sand Valley), Blackstone Basin (da Crimson Forest), Infernal Holt (da Basalt Deltas). Le sue piante del Nether sono già nei vasi. Prova: `/locate biome regions_unexplored:infernal_holt`.
- Ha **rinominato alcuni blocchi** rispetto alla 0.5: `leaf_pile` → `leaf_litter`, `mauve_shrub` → `lavender_wisteria_shrub`, `stone_bud`/`medium_grass` → `grass_sprouts`, `cactus_flower` → `saguaro_cactus_flower`. Botany Pots usa ancora 8 nomi vecchi (alias da provare in gioco; scheda `botany-pots.md`); 17 sue piante restano da scrivere nei vasi.
- Modulo di Every Compat attivo per i suoi legni (`every-compat.md`); 638 file di progressi, quasi tutti sblocchi di ricette (`tema-achievement.md`).
- Tectonic è dichiarata compatibile con Regions Unexplored (candidata, `../lavoro/0601-mod-candidate.md`).
