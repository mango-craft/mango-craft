# Dati

Dati usati dai documenti e dagli script; non sono documenti (niente codici). L'inventario lo rigenerano i workflow.

| File | Contenuto |
|---|---|
| `inventario/` | **Generato dai workflow**, non modificarlo a mano. `mods/<metafile>.json`: cosa contiene ogni .jar del pack (mod id, dipendenze, oggetti e blocchi con il nome inglese, entità, liquidi, tag con il contenuto, tabelle del bottino, strutture, tipi di ricetta, ricette di Botany Pots). `minecraft.json` e `neoforge.json`: lo stesso per il gioco base e NeoForge (tag comuni `c:`). `controllo.md`: esito di `scripts/check_ids.py` |
| `modrinth-progetti.json` | Slug, nome e ID Modrinth delle mod considerate finora (usato per dare i nomi ai metafile) |
| `vasi/copertura.json` | Inventario delle 526 piante delle mod del pack, con proprietà, loot table, copertura nei vasi e 255 bozze di ricetta per Botany Pots |
| `vasi/script/` | Gli script che hanno generato l'inventario (17/10/2026). Riferimento: usano percorsi dell'area di lavoro di allora |
