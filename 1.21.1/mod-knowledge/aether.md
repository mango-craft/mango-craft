# The Aether (+ Deep Aether, Aether's Delight)

Aggiornata il 30/10/2026 · nel pack dalla 0.1.1 (ruolo: `../docs/0301-mod.md`) · fonti: log dell'istanza di prova, inventario del pack, API di Modrinth (30/10), sorgenti di owo-lib e Accessories, issue su GitHub.

## Fatti verificati

- L'Aether porta **dentro di sé** Accessories 1.1.0-beta.48, Cumulus 2.0.7 e Nitrogen 1.1.25 (inventario, file incorporati). **owo-lib** invece è un metafile a sé (`owo-lib.pw.toml`, dalla 0.1.1; 0.12.15.6 dalla 0.7.4): su Modrinth è una dipendenza obbligatoria dell'Aether. È per owo-lib che NeoForge è rimasto fermo a 21.1.259 fino alla 0.7.3 (bug B17); la 0.12.15.6 lo corregge: dalla 0.7.4 c'è NeoForge 21.1.265 e si entra nell'Aether senza disconnessioni (prova del 30/10; scheda `../theme-knowledge/neoforge.md`).
- **Menu degli accessori**: l'Aether ha una schermata sua (oltre a Curios e al menu standard di Accessories), quindi in gioco i menu sono tre: tema `../theme-knowledge/accessori.md`.
- **B07**: bug noto di Accessories quando un'entità subisce danno; Forgified Fabric API dovrebbe evitarlo. Prova "Miapi + Accessories" in `../lavoro/0502-prove-in-gioco.md`: se fallisce si tolgono Aether, Deep Aether e Aether's Delight (con loro esce Accessories), per scelta dell'utente del 16–17/10.
- **B23**: il modello diagonale (Diagonal Walls) non si costruisce per il muro di aerogel dell'Aether e i muri di tronco di Deep Aether.
- Vasi (Botany Pots): le piante e i terreni di Aether e Deep Aether sono nel nostro datapack dalla 0.6.1, generati dalle regole dei vasi (`../lavoro/versioni/v0.6.1.md`; scheda `botany-pots/botany-pots.md`).
- Deep Aether: modelli mancanti nel log per `magnetic_cog`, `magnetic_staff`, `sentry_alarm`, `mimic_eye` (B12).
