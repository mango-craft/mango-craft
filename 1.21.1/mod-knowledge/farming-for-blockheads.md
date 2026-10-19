# Farming for Blockheads

Aggiornata il 19/10/2026 · nel pack dalla 0.3.0, versione 21.1.14 (`../docs/0403-distinta-mod.md`) · fonti: file della mod (inventario), sorgente. Lavoro in corso: `../lavoro/versioni/v0.6.2.md`.

## Fatti verificati

- Le sue 5 terre fertilizzate sono già terreni di Botany Pots (anche nell'etichetta `botanypots:soil/dirt`).
- Il jar contiene 810 voci di mercato, per decine di mod non nel pack (BYG 117, Pam's 96+49, Croptopia 85…): inattive. Per le mod del pack: Farmer's Delight 15, Twilight Forest 12, Ars Nouveau 5 + Ars Elemental 1, Cultural Delights 3, Expanded Delight 3, Rustic Delight 3, My Nether's Delight 2, Supplementaries 1, Create 1 (dettaglio in `v0.6.2.md`).

## Formato del mercato (1.21.1)

- Voce: `data/<namespace>/recipe/market/<mod>/<oggetto>.json`
  ```json
  {"neoforge:conditions":[{"type":"neoforge:item_exists","item":"vinery:red_grape_seeds"}],
   "type":"farmingforblockheads:market","category":"farmingforblockheads:seeds",
   "preset":"vinery:seeds","result":{"item":"vinery:red_grape_seeds"}}
  ```
- Prezzo (preset): `data/<mod>/market_presets/seeds.json` con `{"payment":{"ingredient":{"item":"minecraft:emerald"},"count":1}}`.
- Categorie: `farmingforblockheads:seeds`, `saplings`, `flowers`, `other`.
- Dalla 1.21.2 i preset sono stati sostituiti da un altro sistema: il formato sopra vale per la 1.21.1.
