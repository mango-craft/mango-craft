# Etichetta dei terreni di terra (Botany Pots)

`tags/item/soil/dirt.json` aggiunge all'etichetta `botanypots:soil/dirt` i terreni delle altre mod (terra ricca di Twilight's Flavor & Delight, terra risorgente di My Nether's Delight, terra infusa di Hexalia, terra fertilizzata di Farm & Charm, terre dell'Aether e di Deep Aether, terra erbosa di Bountiful Fares…). Le colture "di terra" (la maggior parte) accettano come terreno qualunque oggetto di questa etichetta.

- **File generato** da `scripts/botanypots_genera.py` (0.6.1) da `1.21.1/data/vasi/terreno_tag_settings.csv`, insieme alle ricette dei terreni in `data/matteo_tweaks/recipe/botanypots/<mod>/soil/`: non si modifica a mano, si cambia la regola e si rilancia lo script.
- Le voci sono `"required": false`: se una mod manca, la voce si ignora e non c'è nessun errore.
- Il nome della cartella è quello della mod di cui si estende l'etichetta (Botany Pots).
