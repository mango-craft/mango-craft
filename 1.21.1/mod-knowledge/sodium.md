# Sodium

Aggiornata il 19/10/2026 · nel pack dalla 0.1.1, versione 0.8.13 (`../docs/0403-distinta-mod.md`) · fonti: sorgente di Sodium 0.8.13, changelog su Modrinth, log dell'istanza di prova.

## Fatti verificati

- Supplementaries rifiuta Sodium più vecchio della 0.8.12-beta.1; Iris funziona con la 0.8 solo nella 1.8.14-beta.1 (scheda `iris.md`). Embeddium non serve più: Sodium esce ufficialmente per NeoForge.
- **Si regola da solo in parte** (`SodiumOptions`, `ChunkBuilder`, `Workarounds`): thread per costruire i chunk = processori meno 6, tra 1 e 10 (sul Ryzen 7 9700X dell'utente: 10); correzioni automatiche per alcuni driver NVIDIA ("threaded optimizations"), AMD (25.10.2+) e Intel; contesto OpenGL "senza errori" solo se la scheda lo supporta (OpenGL 4.6 o `GL_KHR_no_error`).
- Il resto di `config/sodium-options.json` è fisso e già impostato per le prestazioni: `chunk_build_defer_mode` ALWAYS, `animate_only_visible_textures`, `use_entity_culling`, `use_fog_occlusion`, `use_block_face_culling`, `use_no_error_gl_context` tutti `true`, `quad_splitting_mode` SAFE, `cpu_render_ahead_limit` 3, qualità di pioggia e foglie "come la grafica". Nessun file di Sodium nel pack (decisione del 19/10: impostazioni video a chi gioca).
- Con Iris installata spegne tre suoi mixin del cielo (`mixin.features.render.world.sky`): atteso.
- Nel log: "Class … does not support optimized vertex writing code paths" per `VertexMultiConsumer$Double`, `BufferBuilder`, `SpriteCoordinateExpander`: innocuo (B14).
