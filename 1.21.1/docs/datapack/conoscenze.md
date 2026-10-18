# Datapack `matteo_tweaks` — conoscenze e piano (round del 17/10/2026)

Tutto quello che serve per scrivere il datapack del prossimo pacchetto, ricavato dai sorgenti 1.21.1 delle mod. La tabella pianta per pianta dei vasi è in un documento a parte: `datapack/vasi-copertura.md`. Le decisioni del round sono in `decisioni/2026-10-17-round-opzionali.md`.

---

## 0. Principi (decisi dall'utente)

1. **Un solo datapack, il nostro.** Niente datapack esterni installati: quelli esistenti servono solo da ispirazione.
2. **Copiare solo quando la licenza lo permette** (MIT, LGPL), citando la fonte nel readme della cartella. Le licenze ARR solo come confronto.
3. **Ogni file si carica solo se la sua mod c'è** (condizioni di caricamento), così togliere o aggiungere mod non dà errori.
4. **Un criterio di bilanciamento unico** per tutto (sezione 2.4).
5. **Readme in ogni cartella**, in minuscolo dentro `data/` (un `README.md` maiuscolo lì dentro fa comparire "Invalid path in pack" nel log).
6. **Verifica nel mondo di prova** prima del mondo vero.

## 1. Organizzazione proposta (da adattare al repository)

```
matteo_tweaks/
├── pack.mcmeta
├── README.md                       panoramica, fonti e licenze
└── data/
    ├── matteo_tweaks/
    │   ├── recipe/
    │   │   ├── botanypots/<mod>/crop|soil/     vasi, una cartella per mod
    │   │   ├── botanytrees/<mod>/...           alberi (es. Bountiful Fares)
    │   │   ├── market/<mod>/...                mercato di Farming for Blockheads
    │   │   └── create/mixing/experience/...    conversione dell'esperienza
    │   ├── loot_table/tree_drops/<mod>/...     raccolti degli alberi nei vasi
    │   └── loot_modifiers/artifacts/           (già esistente)
    ├── <mod>/market_presets/...                prezzi del mercato per mod
    ├── create_enchantment_industry/data_maps/fluid/unit/experience.json
    ├── cataclysm/tags/worldgen/structure/berserker_spawn.json
    ├── c/tags/item/foods/cooked_fish.json      (solo se si approva la correzione del pesce)
    ├── neoforge/loot_modifiers/                (già esistente)
    └── enhancedcelestials/...                  (già esistente)
```

---

## 2. Vasi (Botany Pots 21.1.44 / Botany Trees 21.1.7)

### 2.1 Stato della copertura
- **526 piante** nelle mod del pack e in quelle approvate in questo round (Jaden's Nether Expansion e Nether Depths Upgrade escluse, da aggiungere).
- **263 già coperte**: da Botany Pots, da Botany Trees, dalle mod stesse (Veggies Delight 14 ricette, Rustic Delight 8) o dal nostro datapack (Ars).
- **202 scoperte** + **50** che avrebbe coperto BotanyCompatLayer (non più installato) = **252 da scrivere**.
- **8 piante di Regions Unexplored** che Botany Pots copre con nomi pre-0.6 (alias): da verificare in gioco.
- **3 escluse** perché non adatte ai vasi (due fagioli magici, il tronco della vite di Vinery).
- **13 terreni** da aggiungere.

| Mod | Da scrivere |
|---|---:|
| Hexalia | 31 |
| Bountiful Fares | 30 (8 alberi) |
| Deep Aether | 21 |
| Undergarden | 21 (Botany Pots ha solo i suoi terreni) |
| Farm & Charm | 20 (ex BotanyCompatLayer) |
| Unusual End | 19 |
| Cultural Delights | 13 |
| Twilight Forest | 12 (cespugli di bacche) |
| Expanded Delight | 10 |
| Regions Unexplored | 9 |
| HerbalBrews | 9 (ex BotanyCompatLayer) |
| Vinery, Meadow | 8 ciascuna (ex BotanyCompatLayer) |
| Hexerei, Aether's Delight | 7 ciascuna |
| Roaster's Delight | 5 (sorgente chiuso: nomi da ricavare in gioco) |
| Ender's Delight, My Nether's Delight | 4 ciascuna |
| Twilight's Flavor & Delight, Aether | 3 ciascuna |
| Reactive, Rustic Delight (2 peperoni) | 2 ciascuna |
| Veggies Delight, Ars Elemental, Deeper and Darker, Friends & Foes | 1 ciascuna |
| Jaden's Nether Expansion, Nether Depths Upgrade | da inventariare (zucca del dolore, torciafiore delle anime, verruca distorta, funghi cerebrage, sporeshroom; alghe di lava) |

### 2.2 Formato (1.21.1)
- **Coltura**: `botanypots:block_derived_crop` con `"block"`; seme, aspetto e raccolto si ricavano dal blocco (stato a età massima) e dalla sua loot table. Esempio minimo, come nelle ricette vanilla di Botany Pots: `{"type":"botanypots:block_derived_crop","block":"minecraft:wheat"}`. Terreno di default: `botanypots:soil/dirt`.
- **Terreno**: `botanypots:block_derived_soil`, un file per blocco.
- **Raccolti espliciti** quando la loot table dà solo la pianta o i semi (tipico delle piante raccolte col click destro): `"drops":[{"type":"botanypots:loot_table","table_id":"..."}]` oppure `{"type":"botanypots:items","items":[{"result":{"id":"...","count":1},"chance":1.0}]}`.
- **Terreni speciali**: acqua = tag `botanypots:soil/water`; funghi = blocchi `minecraft:mushroom_grow_block` o `botanypots:soil/mushroom`; Nether = `minecraft:nylium` o `botanypots:soil/nether`; End = `botanypots:soil/end`; poi `sand`, `sculk`, `moss`.
- **Piante appese**: `render_options.rotation: X_180`, come le liane delle grotte.
- **Alberi**: schema di Botany Trees, `block_derived_crop` sull'alberello, `grow_time` 2400 e raccolto da una loot table nostra (modello: `botanytrees:tree_drops/...`).
- **Condizioni di caricamento**: `bookshelf:load_conditions` con `bookshelf:block_exists` sui blocchi usati (come i file attuali di Ars) oppure `neoforge:conditions` con `neoforge:mod_loaded`.
- **Attenzione**: le ricette in formato 1.20 (es. quella inclusa in Ars Elemental, con namespace `botany_pots`) vengono ignorate.

### 2.3 Casi particolari
- **Piante raccolte col click destro** (Hexerei, Vinery, cespugli di bacche di Twilight, voidpepper di Ender's Delight, bullet pepper di My Nether's Delight, cespuglio di tè di Bountiful Fares, warped bush di Unusual End): servono raccolti espliciti, già indicati pianta per pianta nella tabella.
- **Alberi di Bountiful Fares**: le 8 ricette e le loot table esistono nel sorgente di Botany Trees (LGPL-2.1, commit successivo alla 21.1.7). Si copiano citando la fonte e si tolgono quando esce la nuova versione di Botany Trees.
- **Terreni da aggiungere**: terra ricca e terreno arato di Twilight's Flavor & Delight; terra risorgente, il suo terreno arato e il compost letios di My Nether's Delight; terra infusa e terreno arato di Hexalia (servono anche al saltsprout); terra e terreno arato fertilizzati di Farm & Charm; loam di Vinery; terre di Aether e Deep Aether e la terra erbosa di Bountiful Fares (facoltativi).
- **Terreni particolari di alcune piante**: alga sirena di Hexalia in acqua, piante di Ender's Delight su pietra dell'End.
- **Roaster's Delight**: sorgente chiuso, i nomi di pianta del caffè, tè, camomilla, menta e matcha vanno letti in gioco (F3 o EMI).
- **Regions Unexplored 0.6** ha rinominato alcuni blocchi (es. `leaf_pile` → `leaf_litter`, `mauve_shrub` → `lavender_wisteria_shrub`, `stone_bud`/`medium_grass` → `grass_sprouts`, `cactus_flower` → `saguaro_cactus_flower`). Botany Pots usa i vecchi nomi: se gli alias non funzionano, si riscrivono le 8 ricette.

### 2.4 Bilanciamento (proposta da confermare)
- **Tempi di crescita**: quelli di default di Botany Pots per le colture normali, come le ricette vanilla che non li specificano. Alberi a 2400 tick come Botany Trees.
- **Raccolti**: quelli della loot table del blocco maturo. Dove servono raccolti espliciti, la stessa quantità che si ottiene raccogliendo a mano nel mondo.
- **Terreni speciali**: bonus simili a quelli già esistenti (terra ricca di FD: +15% di velocità sul terreno arato). Terra risorgente e terra ricca di Twilight come la terra ricca di FD.
- **Niente scorciatoie**: nessuna pianta "rara" o magica (es. fagioli magici) diventa coltivabile se nel gioco base non lo è.

### 2.5 Fonti utilizzabili
| Fonte | Licenza | Uso | Copre |
|---|---|---|---|
| Sorgenti delle mod | — | Base: nomi, stadi, loot table | Tutto |
| BotanyCompatLayer | MIT | Copiabile citandolo, **ma serve lo zip** (da qui non si scarica) | Aether, Farm & Charm, Vinery, Meadow, HerbalBrews, Rustic Delight |
| Botany Pots Mega Addon (GitHub NamelessGamer06) | MIT | Copiabile citandolo | My Nether's Delight, Expanded Delight, parte di Cultural Delights |
| Botany Trees (sorgente) | LGPL-2.1 | Copiabile citandolo | Alberi di Bountiful Fares |
| LayaTweaks BotanyPots | ARR | Solo confronto | Ars, Cultural Delights |
| More Crop Compatibility, Wizardon's Tweaks | MIT (contenuto non verificato) | Eventuale confronto | Cultural Delights, Expanded Delight |
| Bozze generate (255 ricette) | nostre | Punto di partenza, da rivedere | Tutte le scoperte |

### 2.6 Verifica in gioco
Nel mondo di prova con i trucchi attivi:
- `/botanypots debug missing seeds true true`: elenca i semi senza ricetta e scrive bozze JSON in `<istanza>/botanypots/generated/crops`.
- `/botanypots debug missing soils true`: lo stesso per i terreni.
- `/botanypots debug check_crops`: piazza un vaso e segnala nel log le colture che non producono niente (scova i raccolti sbagliati).

---

## 3. Mercato di Farming for Blockheads 21.1.14

### 3.1 Formato (dai file della mod)
- Voce: `data/<namespace>/recipe/market/<mod>/<oggetto>.json`
  ```json
  {"neoforge:conditions":[{"type":"neoforge:item_exists","item":"vinery:red_grape_seeds"}],
   "type":"farmingforblockheads:market","category":"farmingforblockheads:seeds",
   "preset":"vinery:seeds","result":{"item":"vinery:red_grape_seeds"}}
  ```
- Prezzo (preset): `data/<mod>/market_presets/seeds.json` con `{"payment":{"ingredient":{"item":"minecraft:emerald"},"count":1}}`.
- Categorie: `farmingforblockheads:seeds`, `saplings`, `flowers`, `other`.
- Nota: dalla 1.21.2 i preset sono stati sostituiti da un altro sistema; il formato sopra vale per la 1.21.1.

### 3.2 Cosa c'è già e cosa manca
| Mod | Già nel mercato | Mancano |
|---|---|---|
| Farmer's Delight | 15 voci (colture, selvatiche, colonie, terra ricca, compost) | — |
| Cultural Delights | alberello di avocado, semi di cetriolo e melanzana | chicchi di mais |
| Expanded Delight | asparagi, peperoncino, alberello di cannella | arachidi, patata dolce, mirtilli rossi |
| Rustic Delight | peperoni, caffè, cotone | — |
| My Nether's Delight | compost letios, terra risorgente | bullet pepper, canna polverosa |
| Ars Nouveau / Ars Elemental | 4 alberelli di archwood + Magebloom / archwood giallo | Sourceberry |
| Twilight Forest | 12 voci (alberelli, torchberry, terra uberosa) | — |
| Supplementaries, Create | semi di lino, fertilizzante per alberi | — |
| **Nessuna voce** | Aether, Deep Aether, Aether's Delight, Bountiful Fares, Hexerei, Hexalia, Farm & Charm, Vinery, Meadow, HerbalBrews, Veggies Delight, Ender's Delight, Twilight's Flavor & Delight, Regions Unexplored (nemmeno gli alberelli), Undergarden | tutto |

### 3.3 Approccio
- Idea presa dallo script di Craftoria (KubeJS, non utilizzabile così): mettere in vendita **tutti gli alberelli e tutti i semi** delle mod mancanti, con una lista di esclusioni (alberelli magici di Twilight, alberello dell'altro mondo di Occultism, piante "rare" vanilla come torciafiore e baccello di brocca).
- Noi lo facciamo con file JSON statici, uno per oggetto, generati da uno script a partire dall'inventario delle piante.
- **Prezzi**: 1 smeraldo come i preset base; da decidere se alzare quelli di alberelli particolari o piante di altre dimensioni (Aether, Undergarden, Nether).

---

## 4. Esperienza (Cognition + Create: Enchantment Industry)

### 4.1 I liquidi
| Liquido | Mod | mB per punto | Etichetta standard `c:experience` | Chi lo accetta |
|---|---|---:|---|---|
| `create_enchantment_industry:experience` | Create: Enchantment Industry 2.4.2 | **1** | **no** | Incantatore (Blaze Enchanter), lanterna, stampante di CEI: **solo questo liquido** (verificato nel codice: l'incantatore accetta solo `CEIFluids.EXPERIENCE`) |
| `cognition:cognitium_source` | Cognition 2.4.13 | 20 | sì | Obelisco (più una lista di liquidi ammessi in config), pompa degli zaini Sophisticated |
| `sophisticatedcore:xp_still` | Sophisticated Core | 20 | sì | Pompa e calamita degli zaini; l'Obelisco lo accetta di serie |

Lo standard NeoForge è **20 mB per punto** (documentato in `Tags.java`).

### 4.2 Regole (per non duplicare o perdere esperienza)
- **Mai** mettere il liquido di Create nell'etichetta `c:experience`: la pompa degli zaini lo tratterebbe a 20 mB per punto → esperienza moltiplicata per 20.
- **Mai** aggiungere il liquido di Create alla lista `AllowedFluids` di Cognition: l'Obelisco copia i mB 1 a 1 → perdita del 95%.
- I serbatoi di Mekanism tengono **un solo liquido alla volta**: i due liquidi non si mescolano per sbaglio.
- **Experience Hatch** di Create con liquidi "stranieri": con la quantità impostata su "tutto", ogni click deposita solo 1/20 dell'esperienza (si perde al massimo l'arrotondamento). Usare quantità fisse (10–1000 punti).

### 4.3 File del datapack
1. **Unità del liquido di Cognition per Create** (fa capire il cognitium all'Experience Hatch e alle altre parti di Create che leggono questa tabella; **non** all'incantatore):
   `data/create_enchantment_industry/data_maps/fluid/unit/experience.json`
   ```json
   {"values":{"cognition:cognitium_source":20}}
   ```
   Create include già 20 per Sophisticated, Mob Grinding Utils, Just Dire Things, Ender IO, Industrial Foregoing, PneumaticCraft, Cyclic, Reliquary e 25 per CoFH.
2. **Conversione nel Mescolatore di Create**, senza perdite, nelle due direzioni (formato di Create 6 per la 1.21.1, come le sue ricette compat):
   ```json
   {"neoforge:conditions":[
      {"type":"neoforge:mod_loaded","modid":"cognition"},
      {"type":"neoforge:mod_loaded","modid":"create_enchantment_industry"}],
    "type":"create:mixing",
    "ingredients":[{"type":"neoforge:single","amount":50,"fluid":"create_enchantment_industry:experience"}],
    "results":[{"amount":1000,"id":"cognition:cognitium_source"}]}
   ```
   e la ricetta inversa (1000 mB di cognitium → 50 mB di esperienza di Create). Le quantità vanno controllate rispetto alla capienza della bacinella.

### 4.4 Schema della base
- **Deposito**: Obelisco di Cognition (circa 1000 livelli), eventualmente serbatoi di Mekanism col cognitium per l'eccedenza.
- **Produzione da Create** (lanterna, scarico di oggetti) → Mescolatore → cognitium verso l'Obelisco.
- **Macchine di Create** (incantatore, stampante): un piccolo circuito separato col liquido di Create, alimentato dal Mescolatore al contrario (cognitium → esperienza di Create).
- **Zaini**: pompa XP + calamita, il loro liquido va direttamente nell'Obelisco.

### 4.5 Prova nel mondo di prova
Convertire una quantità esatta avanti e indietro e controllare che i punti tornino identici. Provare l'Experience Hatch su un serbatoio di Mekanism.

---

## 5. Correzioni e piccoli file

| File | Contenuto | Stato |
|---|---|---|
| `data/cataclysm/tags/worldgen/structure/berserker_spawn.json` | `{"replace":false,"values":["betterfortresses:fortress"]}`: i Berserker infuocati tornano a comparire nelle fortezze di YUNG's. Dopo l'aggiunta riavviare il mondo, `/reload` non basta | Approvato |
| `data/c/tags/item/foods/cooked_fish.json` (+ `c:foods/cooked_fishes` e `bountifulfares:cooked_fishes`) | Aggiunge `starcatcher:cooked_starcaught_fish`, così il pesce cotto di Starcatcher vale nei taco e fish and chips di Cultural Delights e nella zuppa di Bountiful Fares | **Proposta in sospeso** |
| Ricette dei vasi per Jaden's Nether Expansion e Nether Depths Upgrade | Piante del Nether nuove | Da inventariare |

### Config (non datapack, ma da preparare insieme)
- **Every Compat**: spegnere i moduli che non servono; tenere Handcrafted, Macaw's, credenze di FD, Storage Drawers, Create, Rechiseled, Friends & Foes, Twilight Forest, Regions Unexplored.
- **Jaden's Nether Expansion** (`config/netherexp-startup.toml`, sezione `packSettings`, serve riavvio): `improvedNetherBiomeSource` e `netherWorldGenOverhaul` come paracadute.
- **Moog's Nether Structures**: lasciare spenta la sostituzione della fortezza vanilla.
- **Sparse Structures**: regolazioni per struttura dopo il mondo di prova.
- **Cognition**: lasciare `AllowedFluids` com'è.

---

## 6. Fatti utili (verificati nei sorgenti)

- **Starcatcher**: 132 pesci in `c:foods/raw_fish`, `minecraft:fishes`, `minecraft:cat_food`. FD include `c:foods/raw_fish` in `c:foods/safe_raw_fish` (escluso il pesce palla), quindi i pesci valgono nelle ricette "pesce crudo qualsiasi" di FD (zuppa di pesce, involtini, pasta al nero), Brewin' And Chewin' (pasta al formaggio, aringhe), Veggies Delight (fish and chips, torta di rape) e Farm & Charm (cibo per gatti). Starcatcher's Delight: filetti per rarità sul tagliere (anche loro "pesce crudo") e 50 piatti nella pentola di FD e di Farm & Charm. Pesce cotto in fornace: generico, fuori dalle etichette.
- **Ricette per etichetta nelle mod di cucina del pack**: `c:eggs` circa 70, `c:foods/raw_chicken` circa 17, `c:foods/raw_beef` circa 15, `c:foods/raw_meat` circa 9. Un ingrediente nuovo è utile solo se entra in una di queste etichette o ha ricette proprie.
- **Regions Unexplored 0.6**: usa Lithostitched, non TerraBlender. Biomi Nether: Mycotoxic Undergrowth (da Nether Wastes), Glistering Meadow (da Soul Sand Valley), Blackstone Basin (da Crimson Forest), Infernal Holt (da Basalt Deltas). Le sue piante del Nether sono già nei vasi.
- **Cataclysm**: Burning Arena solo in Nether Wastes; Soul Black Smith nei 4 biomi vanilla; Berserker legati a `cataclysm:berserker_spawn`.
- **Farming for Blockheads**: le sue 5 terre fertilizzate sono già terreni di Botany Pots (anche nel tag `botanypots:soil/dirt`).

---

## 7. Dati grezzi

Nel repository:
- `1.21.1/data/vasi/copertura.json`: inventario delle 526 piante con proprietà, loot table e 255 bozze di ricetta;
- `1.21.1/data/vasi/script/`: gli script che hanno generato l'inventario (riferimento, non vanno rilanciati così come sono);
- `1.21.1/docs/datapack/vasi-copertura.md`: la tabella pianta per pianta;
- `1.21.1/docs/valutazioni/`: le ricerche complete (in inglese) su Nether, animali, esperienza e datapack esistenti.
