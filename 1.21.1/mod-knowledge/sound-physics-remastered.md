# Sound Physics Remastered

Aggiornata il 19/10/2026 · nel pack dalla 0.1.1 (ruolo e licenza: `../docs/0301-mod.md`; versione: `../docs/0403-distinta-mod.md`) · fonti: sorgente della mod (ricerca del 19/10, materiale grezzo in `../../ai-agents/stage/2026-10-19_1.21.1-v0.6.0_config-mod/`).

- Versione 1.5.1 (solo alpha/beta per abitudine dell'autore). Config `config/sound_physics_remastered/soundphysics.properties` (client; una chiave mancante prende il valore di serie). Chiavi della qualità, con valore di serie e intervallo: `environment_evaluation_ray_count` 32 (8–64), `environment_evaluation_ray_bounces` 4 (2–64), `max_occlusion_rays` 16 (1–128), `strict_occlusion` false, `sound_direction_evaluation` true, `redirect_non_occluded_sounds` true, `update_moving_sounds` false, `sound_update_interval` 5, `max_sound_processing_distance` 512, `evaluate_ambient_sounds` false.
- Costa un po' di CPU: se pesa, abbassare i raggi. Nessun file nel pack.
- Segnala nella sua config di serie suoni che non esistono (quelli di Enhanced Celestials 1 e alcuni di Cataclysm): innocuo (B14).
