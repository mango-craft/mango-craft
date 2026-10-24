# Mercato di Farming for Blockheads (0.6.2)

Le voci del mercato per le piante che la mod non vende: una cartella per namespace, un file per oggetto, con la condizione `neoforge:item_exists` (togliere una mod non dà errori). I listini (prezzi) sono in `../../market_presets/` (`<origine>_<classe>.json`), e i listini delle mod riscritti con il nostro prezzo stanno **allo stesso percorso** del file originale (`data/<mod>/market_presets/`).

**Non si scrivono a mano**: li genera `scripts/mercato_genera.py` dalle regole in `1.21.1/data/mercato/*.csv`, passando dalla base dati delle piante (`scripts/botanypots_db.py`, viste `MERCATO_PIANO_VOCE` e `MERCATO_PIANO_PRESET`); la CI verifica che corrispondano. Si cambia la regola e si rilancia lo script.

Il prezzo: moneta e quantità base per **origine** (Overworld: smeraldi per common e uncommon, poi diamanti; Nether verghe di blaze; End gusci di shulker; Aether gemme di zanite; Undergarden cristalli di utherium; Twilight Forest lingotti di ironwood; Otherside frammenti d'eco) moltiplicate per la **classe di rarità** della mod o dell'oggetto (×1 … ×10), per eccesso; sopra 64 in blocchi. Le piante decorative (erba, cespugli, liane) e quelle magiche non si vendono. Motivi e numeri: `1.21.1/lavoro/versioni/v0.6.2.md`; formato e fatti della mod: `1.21.1/mod-knowledge/farming-for-blockheads.md`.
