# Jaden's Nether Expansion (+ Elysium API, Lodestone)

Aggiornata il 19/10/2026 · nel pack dalla 0.5.0, versione 2.4.1 (`../docs/0403-distinta-mod.md`; ruolo: `../docs/0301-mod.md`) · fonti: sorgente (ramo 1.21.1 @0e5a1ea), inventario, log dell'istanza di prova. Decisione: `../lavoro/versioni/v0.5.0.md`.

## Fatti verificati

- Rende il Nether più alto (soffitto a quota 192) e cambia la disposizione dei biomi tramite due datapack interni (`netherexp:nether_worldgen_overhaul`, `netherexp:nether_mosaic_biome_source`): serve un mondo nuovo. Generare il Nether nuovo è pesante (rallentamento di 2,5 secondi entrando: conviene pregenerarlo con Chunky nel mondo di prova).
- **Config** `config/netherexp-common.toml`, sezione `[worldSettings]`: `netherWorldGenOverhaul` e `improvedNetherBiomeSource`, entrambi `true` di serie, con riavvio del gioco. Metterli a `false` è il paracadute se il Nether nuovo desse problemi (nessun file nel pack). `netherexp-startup.toml` contiene solo `startupSettings` (splash, profanity, developerMode) e `packSettings.soulCampfireSoulSoil`.
- Librerie: Elysium API 2.0.1 (GPL-2.0) e Lodestone 1.8.2 (LGPL-3.0); Biolith dentro Jaden's ignora i mondi di prova di un'altra mod (B14). Lodestone ha shader propri: con uno shader attivo alcuni effetti nel Nether possono vedersi male (`../theme-knowledge/shader.md`).
- **B29**: 5 ricette della mod citano oggetti che nella versione riscritta non esistono più (`iron_scrap`, `warphopper_fur`, `igneous_reeds`, `indented_soul_slate_tiles`) e una di Just Enough Breeding (uovo del False Carcass); mancano 2 suoni, 2 etichette e parametri di shader di Lodestone. **B31**: le stalattiti di netherrack piazzano blocchi fuori dal chunk in generazione (11 avvisi, qualche stalattite tagliata). File di licenza tra le texture con nome non valido (B14).
- Piante per i vasi: `netherexp:soul_torchflower_crop`, `sorrowsquash_stem_plant`, `crimson_sprouts`, `twilight_vines` (`../lavoro/versioni/v0.6.1.md`). Nessuna voce nel mercato.
