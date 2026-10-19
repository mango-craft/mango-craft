# Tema: esperienza liquida e deposito

Aggiornata il 19/10/2026 · mod coinvolte: Create: Enchantment Industry, Cognition (ex Experience Obelisk), Sophisticated Backpacks/Core, XP Tome, Supplementaries · fonti: sorgenti di Create: Enchantment Industry 2.4.2, Cognition 2.4.13, Sophisticated Core, NeoForge (`Tags.java`), inventario del pack. Ricerca: `../lavoro/versioni/v0.2.3.md` (analisi del 17/10); materiale grezzo `../../ai-agents/stage/2026-10-17_1.21.1-v0.2.3_esperienza/`.

## Cose da non rompere

- Il liquido di Create: Enchantment Industry vale **1 mB per punto**, gli altri **20**. **Mai** mescolarli per etichetta o per config:
  - mai mettere `create_enchantment_industry:experience` nell'etichetta `c:experience`: la pompa degli zaini lo tratterebbe a 20 mB per punto → esperienza moltiplicata per 20;
  - mai aggiungerlo alla lista `AllowedFluids` di Cognition: l'Obelisco copia i mB 1 a 1 → perdita del 95% (`isFluidValid` controlla solo che il liquido sia nella lista).

## I liquidi

| Liquido | Mod | mB per punto | In `c:experience` | Chi lo accetta |
|---|---|---:|---|---|
| `create_enchantment_industry:experience` | Create: Enchantment Industry 2.4.2 | **1** | **no** | Incantatore (Blaze Enchanter), lanterna, stampante di CEI: **solo questo liquido** (l'incantatore accetta solo `CEIFluids.EXPERIENCE`) |
| `cognition:cognitium_source` | Cognition 2.4.13 | 20 | sì | Obelisco (più la lista `AllowedFluids` in `config/cognition-common.toml`: mob_grinding_utils, cofh_core, industrialforegoing, sophisticatedcore `xp_still`, enderio, reliquary), pompa degli zaini Sophisticated |
| `sophisticatedcore:xp_still` | Sophisticated Core | 20 | sì | Pompa e calamita degli zaini; l'Obelisco lo accetta di serie |
| `supplementaries:experience` | Supplementaries | — | no | Barattoli di Supplementaries; da capire se conta per le conversioni |

Lo standard NeoForge è 20 mB per punto (`Tags.java`). I serbatoi di Mekanism tengono un solo liquido alla volta: i due liquidi non si mescolano per sbaglio. **Experience Hatch** di Create con liquidi "stranieri": con la quantità impostata su "tutto" ogni click deposita solo 1/20 dell'esperienza (si perde al massimo l'arrotondamento): usare quantità fisse (10–1000 punti).

## File del datapack (versione 0.6.0, `../lavoro/versioni/v0.6.0.md`)

1. **Unità del liquido di Cognition per Create** (lo fa capire all'Experience Hatch e alle parti di Create che leggono questa tabella; non all'incantatore): `data/create_enchantment_industry/data_maps/fluid/unit/experience.json` con `{"values":{"cognition:cognitium_source":20}}`. La tabella esiste nel jar (`create_enchantment_industry:unit/experience`) e include già 20 per Sophisticated, Mob Grinding Utils, Just Dire Things, Ender IO, Industrial Foregoing, PneumaticCraft, Cyclic, Reliquary e 25 per CoFH: il nostro file si aggiunge.
2. **Conversione nel Mescolatore** senza perdite, nelle due direzioni (formato di Create 6 per la 1.21.1):
   ```json
   {"neoforge:conditions":[{"type":"neoforge:mod_loaded","modid":"cognition"},{"type":"neoforge:mod_loaded","modid":"create_enchantment_industry"}],
    "type":"create:mixing",
    "ingredients":[{"type":"neoforge:single","amount":50,"fluid":"create_enchantment_industry:experience"}],
    "results":[{"amount":1000,"id":"cognition:cognitium_source"}]}
   ```
   e la ricetta inversa (1000 mB di cognitium → 50 mB di esperienza di Create). Le quantità vanno controllate rispetto alla capienza della bacinella.

## Schema della base

Deposito: Obelisco di Cognition (circa 1000 livelli), eventualmente serbatoi di Mekanism per l'eccedenza. Produzione da Create (lanterna, scarico di oggetti) → Mescolatore → cognitium verso l'Obelisco. Macchine di Create (incantatore, stampante): un piccolo circuito separato col liquido di Create, alimentato dal Mescolatore al contrario. Zaini: pompa XP + calamita, il loro liquido va direttamente nell'Obelisco. XP Tome per portarsi dietro l'esperienza.

Prova: convertire una quantità esatta avanti e indietro e controllare che i punti tornino identici; provare l'Experience Hatch su un serbatoio di Mekanism.
