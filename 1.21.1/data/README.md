# Dati

Dati usati dai documenti e dagli script; non sono documenti (niente codici). L'inventario lo rigenerano i workflow.

| File | Contenuto |
|---|---|
| `inventario/` | **Generato dai workflow**, non modificarlo a mano. `mods/<metafile>.json`: cosa contiene ogni .jar del pack (mod id, dipendenze, oggetti e blocchi con il nome inglese, entità, liquidi, tag con il contenuto, tabelle del bottino, strutture, tipi di ricetta, ricette di Botany Pots). `minecraft.json` e `neoforge.json`: lo stesso per il gioco base e NeoForge (tag comuni `c:`). `controllo.md`: esito di `scripts/check_ids.py` |
| `modrinth-progetti.json` | Slug, nome e ID Modrinth delle mod considerate finora (usato per dare i nomi ai metafile) |
| `vasi/copertura.json` | Inventario delle 526 piante delle mod del pack (17/10/2026), con proprietà, loot table, copertura nei vasi e 255 bozze di ricetta per Botany Pots. Lo legge `scripts/vasi_genera.py`, che genera le ricette dei vasi (0.6.1). Gli script che l'hanno prodotto e la tabella leggibile sono in `ai-agents/stage/2026-10-17_1.21.1-v0.2.3_vasi/` |
| `vasi/aggiunte.json` | A mano, per `scripts/vasi_genera.py`: i terreni dei vasi (con il bonus di crescita e se entrano nell'etichetta della terra), le colture senza bozza (Roaster's Delight, sorgente chiuso; alghe di lava; germogli cremisi), le colture libere (graticci di Bountiful Fares, senza blocco proprio), i raccolti scritti a mano per le piante che senza cesoie non darebbero niente e le esclusioni con il motivo |
| `vasi/rarita_pots_settings.csv`, `vasi/terreno_rarita.csv` | A mano, per `scripts/vasi_db.py`: la scala di rarità dei terreni (classe → bonus di crescita e resa nel vaso) e la classe di ogni terreno con il motivo. Il database `vasi/vasi.sqlite` che lo script costruisce da inventario, datapack e questi due file **non va nel repository** |
