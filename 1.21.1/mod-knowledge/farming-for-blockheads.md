# Farming for Blockheads

Aggiornata il 30/10/2026 · nel pack dalla 0.3.0, versione 21.1.14 (`../docs/0403-distinta-mod.md`) · fonti: file della mod (inventario), sorgente 21.1.14 (ramo `1.21.1`, commit `a764fa2`: `MarketPresetRegistry`, `MarketRecipe`, `MarketMenu`, `MarketPresetLoader`). Lavoro della 0.6.2 (rilasciata il 24/10): `../lavoro/versioni/v0.6.2.md`; tema `../theme-knowledge/piante.md`.

## Fatti verificati

- Le sue 5 terre fertilizzate sono già terreni di Botany Pots (anche nell'etichetta `botanypots:soil/dirt`).
- Il jar contiene 810 voci di mercato e 84 listini (preset), per decine di mod non nel pack (BYG 117, Pam's 96+49, Croptopia 85…): inattive. Per le mod del pack ci sono 46 voci, ma **solo 31 sono attive** (24/10, base dati `MERCATO_VOCE_ATTIVA`): le altre usano listini **spenti** (`enabled: false` nel file del preset). Spenti: alberelli, torchberry e terra uberosa di Twilight Forest (12), selvatiche, colonie e terre di Farmer's Delight (11), il «delight» di My Nether's Delight (2), e di Minecraft fiori, funghi, terre, uova e colture (48). Attivi: 12 vanilla (semi, alberelli, farina d'ossa), Ars Nouveau 5, Rustic/Expanded/Cultural Delights 3 ciascuna, Farmer's Delight 2 (semi), Supplementaries, Create, Ars Elemental 1. La tabella del 17/10 in `v0.6.2.md` li contava tutti come presenti: era sbagliata.
- **Quando una voce è attiva** (`MarketPresetRegistry.isRecipeEnabled`): l'oggetto esiste, il suo preset esiste ed è acceso. Un preset è acceso se nel file ha `enabled` vero (o manca) e non sta in `disabledDefaultPresets` della config; un preset spento si accende solo con `enabledOptionalPresets`. Una voce senza preset esistente è spenta.
- **Il pagamento è uno stack in uno slot** (`MarketMenu`: `getCount() >= count`): una quantità sopra 64 non si può pagare mai. Sopra i 64 si passa ai blocchi.
- Una voce può portare un **pagamento proprio** (`payment`, facoltativo) che vince sul preset; il preset deve comunque esistere ed essere acceso. Campi facoltativi: `icon`, `sortIndex`.
- I **preset** si leggono da `data/<qualsiasi namespace>/market_presets/<nome>.json` (id `<namespace>:<nome>`) e dalla cartella `config/market_presets/`; il nostro datapack può quindi aggiungere listini suoi (`matteo_tweaks:…`) e **riscrivere quelli delle mod allo stesso percorso**. Il pagamento (`payment.tooltip`) può avere un testo.
- Le **categorie** (`market_categories/`) sono 4 e stanno nel jar; una categoria sconosciuta in una voce non passa.
- **Monete che si rigenerano nel pack** (verificato nei jar il 24/10, per scegliere i prezzi): verghe di blaze (spawner), gusci di shulker (duplicazione vanilla, shulker posseduti di Occultism), frammenti d'eco (infusione di Apothic Enchanting 1→4, cristallizzazione di Occultism dalla polvere d'eco), zanite (frantumazione di Create), ironwood (si fonde da liveroot, ferro e oro), netherite (raddoppiata da Occultism e Mekanism, ma serve il minerale). Le monete scelte per le dimensioni sono in `1.21.1/data/mercato/mercato_base.csv`, con il motivo.

## Formato del mercato (1.21.1)

- Voce: `data/<namespace>/recipe/market/<mod>/<oggetto>.json`
  ```json
  {"neoforge:conditions":[{"type":"neoforge:item_exists","item":"vinery:red_grape_seeds"}],
   "type":"farmingforblockheads:market","category":"farmingforblockheads:seeds",
   "preset":"vinery:seeds","result":{"item":"vinery:red_grape_seeds"}}
  ```
- Prezzo (preset): `data/<mod>/market_presets/seeds.json` con `{"payment":{"ingredient":{"item":"minecraft:emerald"},"count":1},"enabled":true}` (`enabled` facoltativo, vero se manca).
- Categorie: `farmingforblockheads:seeds`, `saplings`, `flowers`, `other`.
- Dalla 1.21.2 i preset sono stati sostituiti da un altro sistema: il formato sopra vale per la 1.21.1.
