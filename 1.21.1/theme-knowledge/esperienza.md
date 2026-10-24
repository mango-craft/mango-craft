# Tema: esperienza liquida e deposito

Aggiornata il 24/10/2026 · mod coinvolte: Create: Enchantment Industry, Cognition (ex Experience Obelisk), Sophisticated Backpacks/Core, XP Tome, Supplementaries · fonti: sorgenti di Create: Enchantment Industry 2.4.2, Cognition 2.4.13, Sophisticated Core, NeoForge (`Tags.java`), Create (ramo `mc1.21.1/dev`, commit `7ff2760`, letto il 21/10: `BasinBlockEntity` e ricette generate del Mescolatore), inventario del pack; NeoForge 1.21.1 (`DataMapLoader`, `DataMapFile`, letti il 24/10); jar di Moonlight 3.7.2 e Supplementaries 4.0.2 (24/10). Ricerca: `../lavoro/versioni/v0.2.3.md` (analisi del 17/10); materiale grezzo `../../ai-agents/stage/2026-10-17_1.21.1-v0.2.3_esperienza/`.

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
| (esperienza dei barattoli) | Supplementaries / Moonlight | — | — | **Non è un liquido**: è un «soft fluid» di Moonlight (`data/moonlight/moonlight/soft_fluid/experience.json`) per i barattoli, con le bottiglie d'esperienza come contenitore e **equivalente all'etichetta `#c:experience`**; `fluid.supplementaries.experience` è solo il suo nome tradotto. Non entra nello scambio (verificato il 24/10) |

Lo standard NeoForge è 20 mB per punto (`Tags.java`). I serbatoi di Mekanism tengono un solo liquido alla volta: i due liquidi non si mescolano per sbaglio. **Experience Hatch** di Create con liquidi "stranieri": con la quantità impostata su "tutto" ogni click deposita solo 1/20 dell'esperienza (si perde al massimo l'arrotondamento): usare quantità fisse (10–1000 punti).

## File del datapack (dalla 0.6.3, `../lavoro/versioni/v0.6.3.md`; scritti il 24/10)

Nomi dei liquidi presi dalle etichette delle mod stesse (`c:experience` di Cognition, `create:bottomless/deny` di Create: Enchantment Industry): `cognition:cognitium_source` e `create_enchantment_industry:experience`. Il nome tradotto `cognition:cognitium` è il **tipo** di liquido, non il liquido: nelle ricette non funzionerebbe (e il controllo dei nomi non lo saprebbe distinguere).

1. **Unità del liquido di Cognition per Create** (lo fa capire all'Experience Hatch e alle parti di Create che leggono questa tabella; non all'incantatore): `data/create_enchantment_industry/data_maps/fluid/unit/experience.json` con `{"values":{"cognition:cognitium_source":{"neoforge:conditions":[…mod_loaded cognition…],"neoforge:value":20}}}`. La tabella esiste nel jar (`create_enchantment_industry:unit/experience`) e include già 20 per Sophisticated, Mob Grinding Utils, Just Dire Things, Ender IO, Industrial Foregoing, PneumaticCraft, Cyclic, Reliquary e 25 per CoFH (non c'è Cognition). **Il nostro file si aggiunge e non sostituisce** (sorgente di NeoForge 1.21.1, 24/10): il caricatore legge lo stesso file da tutti i pacchetti (`listMatchingResourceStacks`) e li unisce; `replace` è falso se manca. La condizione si scrive **per valore** (`neoforge:conditions` + `neoforge:value`, `ConditionalOps` in `DataMapFile`), come fa la mod nel suo file; se Create: Enchantment Industry manca, la mappa non è registrata e il file non si legge.
2. **Conversione nel Mescolatore** senza perdite, nelle due direzioni (formato di Create 6 per la 1.21.1):
   ```json
   {"neoforge:conditions":[{"type":"neoforge:mod_loaded","modid":"cognition"},{"type":"neoforge:mod_loaded","modid":"create_enchantment_industry"}],
    "type":"create:mixing",
    "ingredients":[{"type":"neoforge:single","amount":50,"fluid":"create_enchantment_industry:experience"}],
    "results":[{"amount":1000,"id":"cognition:cognitium_source"}]}
   ```
   e la ricetta inversa (1000 mB di cognitium → 50 mB di esperienza di Create). Nel datapack: `data/matteo_tweaks/recipe/create/mixing/experience/` (`create_in_cognitium.json`, `cognitium_in_create.json`). Le ricette del Mescolatore con soli liquidi in ingresso esistono già nel pack (52, per esempio i coloranti di Create: Dragons Plus): il Mescolatore le esegue. Solo i due liquidi esatti, mai l'etichetta `c:experience`, che contiene anche liquidi a 25 mB per punto (CoFH). Capienza della bacinella verificata il 21/10 nel sorgente di Create: **2 serbatoi di ingresso e 2 di uscita da 1000 mB ciascuno**, quindi 1000 mB di cognitium ci stanno esattamente (50 punti, il lotto più grande possibile). Formato dei liquidi nelle ricette del Mescolatore: ingredienti `{"type":"neoforge:single","amount":…,"fluid":…}`, risultati `{"amount":…,"id":…}`.

**Le due ricette nella stessa bacinella fanno avanti e indietro** (visto in gioco da Matteo e verificato nel sorgente di Create, commit `7ff2760`, il 24/10): le ricette della bacinella prendono i liquidi dal serbatoio che la bacinella espone all'esterno, che unisce **uscita e ingresso** (`BasinBlockEntity`: `CombinedTankWrapper(outputTank, inputTank)`; `BasinRecipe.apply` scorre tutti i serbatoi). Quindi il cognitium appena prodotto nell'uscita viene ripreso dalla ricetta inversa, e così via. Non si crea né si perde esperienza (il rapporto è esatto), ma l'uscita cambia liquido a ogni ciclo e un tubo che la svuota può prendere quello sbagliato e intasarsi. Il calore non serve a separarle: una ricetta senza calore gira anche su una bacinella scaldata (`HeatCondition.NONE` accetta ogni livello). Il **filtro della bacinella** sì: una ricetta parte solo se il suo risultato passa il filtro, e per i liquidi il filtro è il liquido contenuto nell'oggetto (un secchio: `BasinRecipe.match`, `FilterItemStack.test` con `GenericItemEmptying`); filtro vuoto = tutto passa.

## Schema della base

Deposito: Obelisco di Cognition (circa 1000 livelli), eventualmente serbatoi di Mekanism per l'eccedenza. Produzione da Create (lanterna, scarico di oggetti) → Mescolatore → cognitium verso l'Obelisco. Macchine di Create (incantatore, stampante): un piccolo circuito separato col liquido di Create, alimentato dal Mescolatore al contrario. Zaini: pompa XP + calamita, il loro liquido va direttamente nell'Obelisco. XP Tome per portarsi dietro l'esperienza.

Prova: convertire una quantità esatta avanti e indietro e controllare che i punti tornino identici; provare l'Experience Hatch su un serbatoio di Mekanism.
