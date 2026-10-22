# Dati

Dati usati dai documenti e dagli script; non sono documenti (niente codici). L'inventario lo rigenerano i workflow.

| File | Contenuto |
|---|---|
| `inventario/` | **Generato dai workflow**, non modificarlo a mano. `mods/<metafile>.json`: cosa contiene ogni .jar del pack (mod id, dipendenze, oggetti e blocchi con il nome inglese, entità, liquidi, tag con il contenuto, tabelle del bottino, strutture, tipi di ricetta, ricette di Botany Pots). `minecraft.json` e `neoforge.json`: lo stesso per il gioco base e NeoForge (tag comuni `c:`). `controllo.md`: esito di `scripts/check_ids.py` |
| `modrinth-progetti.json` | Slug, nome e ID Modrinth delle mod considerate finora (usato per dare i nomi ai metafile) |
| `vasi/copertura.json` | Inventario delle 526 piante delle mod del pack (17/10/2026), con proprietà, loot table, copertura nei vasi e 255 bozze di ricetta per Botany Pots. Da qui sono nate le regole in `coltura_settings.csv` (0.6.1); oggi è solo storia. Gli script che l'hanno prodotto e la tabella leggibile sono in `ai-agents/stage/2026-10-17_1.21.1-v0.2.3_vasi/` |
| `vasi/coltura_settings.csv`, `coltura_tag_settings.csv`, `coltura_raccolto_settings.csv`, `terreno_tag_settings.csv` | **Le regole nostre** per i vasi, una tabella per cosa (dal 22/10/2026 sostituiscono `aggiunte.json`): le colture da scrivere (seme, tempo, blocchi richiesti, grafica, note), i tag che ogni coltura ammette, i raccolti scritti a mano, i terreni da mettere nei tag `botanypots:soil/*`. Le legge `scripts/botanypots_genera.py`, che scrive il datapack, e `scripts/botanypots_db.py`, che le carica come tabelle `*_SETTINGS` |
| `vasi/rarita_pots_settings.csv`, `vasi/terreno_rarita.csv` | A mano: la scala di rarità dei terreni (classe → bonus di crescita e resa nel vaso) e la classe di ogni terreno con il motivo. Da qui `scripts/botanypots_genera.py` scrive i file di terreno (nuovi o in sostituzione di quelli delle mod). Il database `vasi/vasi.sqlite` che lo script costruisce da inventario, datapack e questi due file **non va nel repository** |
