# L_Ender's Cataclysm (+ Cataclysm Delight)

Aggiornata il 19/10/2026 · nel pack dalla 0.1.1 (ruolo: `../docs/0301-mod.md`) · fonti: file della mod (inventario), sorgente, log dell'istanza di prova.

## Fatti verificati

- Strutture: Burning Arena solo in Nether Wastes; Soul Black Smith nei 4 biomi vanilla del Nether.
- I **Berserker infuocati** compaiono nelle strutture dell'etichetta `cataclysm:berserker_spawn`, che contiene solo `minecraft:fortress`. YUNG's Better Nether Fortresses sostituisce la fortezza vanilla con `betterfortresses:fortress` (esiste nell'inventario): i Berserker non compaiono mai (B02). Correzione nella 0.6.0 (`../lavoro/versioni/v0.6.0.md`): `data/cataclysm/tags/worldgen/structure/berserker_spawn.json` con `{"replace": false, "values": [{"id": "betterfortresses:fortress", "required": false}]}`. I modificatori di struttura richiedono il riavvio del mondo e valgono solo per le fortezze generate dopo.
- Usa **Curios** (Miapi e Hexalia usano Accessories): verificare che convivano (`../lavoro/0502-prove-in-gioco.md`).
- La config di Cataclysm e i buff permanenti di Cataclysm Delight sono tra le leve della difficoltà, mai bilanciate insieme (tema aperto in `../lavoro/0503-temi-aperti.md`).
- Nel log: suoni mancanti e animazioni GeckoLib non valide (B12), innocui.
