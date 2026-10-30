# Probabilità di Relics in altri pack (24/10/2026)

Letto dai repository pubblici, senza installare niente.

- **All The Mods 10** (`AllTheMods/ATM-10`, commit `51627af` del 22/10/2026): nessun `config/relics.yaml` né `config/relics/`; negli script KubeJS solo etichette (le reliquie di Reliquified Artifacts tolte dagli slot di Accessories, `kubejs/server_scripts/Tweaks/tags.js`). Probabilità: quella di serie, 20%.
- **Craftoria** (`TeamAOF/Craftoria`, `main` @`b1b25e5` del 22/10/2026; Relics 0.12.8):
  - `d3fade9` (09/09/2026, «lowered chance of finding relics from 20% > 10%»): aggiunge `relicGenChance: 0.1` in `config/relics/loot.yaml`; in quel momento `config/relics.yaml` aveva `enabledExtendedConfigs: true`.
  - `74b44cc` (13/09/2026, versione 1.37.0): `enabledExtendedConfigs: false`. Nel changelog della 1.37.0 c'è ancora «Lowered chance of finding relics from 20% > 10%».
  - Relics (`RelicsConfigs.register`, uguale da `fd64e8b` del 27/07/2025): `relics/loot` si registra solo con la config estesa accesa. Quindi oggi il file di Craftoria non viene letto.
  - In `config/artifacts/relics/*.yaml` (44 file) c'è ancora un formato vecchio del bottino (regola → probabilità).
- **Relics**: `c74a0f5` (30/07/2025, «Decreased relics gen chance»): valore di serie da 0.33 a 0.2.
- **NeoForge 1.21.1** (`neoforged/NeoForge`, ramo `1.21.1`, `e0e7ab5`): `LootModifier.apply` controlla `conditions` prima di `doApply`; `AddTableLootModifier` (`neoforge:add_table`, campi `conditions` e `table`).
