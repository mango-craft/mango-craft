# Truly Modular e i materiali delle altre mod

Ricerca del 23/10/2026, solo lettura. Pack: Minecraft 1.21.1 NeoForge, Truly Modular (Miapi) **2.3.9**, Arsenal 2.4, Armory 2.2, Archery 2.2.

Legenda: ✅ verificato (file e riga, log, URL) · 🔶 dedotto dal codice, non provato in gioco · ❓ non verificato.

Sorgente letto: tag **`2.3.9-1.21`** di `github.com/Truly-Modular/Modular-Item-API`, commit `2562eda924e7f83c60837f2c6a22a10c86a985e1` (24/08/2026, stesso giorno della release su Modrinth). Copia locale: `/tmp/claude-0/-home-claude/d3876890-5907-520c-8a85-0a2ec892bcbc/scratchpad/repos/miapi-2.3.9`. Le cartelle `arsenal/`, `armory/` e `archery/` del repository sono sottomoduli vuoti: per quelle ho letto i .jar.

---

## Risposte brevi

1. **Sì, Truly Modular crea da solo i materiali delle altre mod**, ma solo dagli **strumenti**: cerca le spade e le asce delle mod. Non usa i tag `c:ingots/*`. Le statistiche sono ricavate dal danno della spada e dell'ascia e dal "Tier" dello strumento. La chiave di config è `generated_materials.generate_materials` (più `generate_other_materials`). Nella nostra config sono entrambe **`true`**. Nel log dell'istanza dev del 21/10 risultano **18 materiali generati**: Aether, Deep Aether, Twilight Forest, Undergarden, Deeper and Darker, Cataclysm, Unusual End, Psi e Cognition. ✅
2. **I materiali scritti a mano** vanno in `data/<namespace>/miapi/materials/<percorso>.json` e il loro ID diventa `<namespace>:<percorso>`. **Un datapack normale funziona**, quindi anche Paxi: il caricatore legge tutti i datapack e il file più in alto vince. ✅ (codice; in gioco 🔶) La condizione di caricamento è **`load_condition`** di Miapi, non `neoforge:conditions`. ✅ Un materiale generato **non si sovrascrive per ID**. Si **sostituisce**: basta un materiale nostro che usi lo stesso oggetto (es. il lingotto), e allora il generatore salta quello strumento. ✅ (codice)
3. **Non esiste un "Tetracelium" per Truly Modular su 1.21.1 NeoForge** su Modrinth. L'unico pacchetto di materiali, **Truly Compatible**, esiste solo per 1.20/1.20.1. ✅ CurseForge non l'ho potuto controllare. ❓
4. **Nessuna issue aperta riguarda i materiali delle mod.** Le 4 issue aperte toccano Accessories, Farmer's Delight, Epic Fight e la grafica in terza persona. Problemi veri, visti nel codice e nel nostro log:
   - errori di registrazione doppia, che sono solo rumore e spiegano B05;
   - durezza gonfiata per Undergarden (cloggrum e forgotten);
   - fiery e skyroot non generati;
   - effetti delle armi gestiti da eventi della mod, che non passano;
   - ID dei materiali generati fragili agli aggiornamenti.

---

## 1. Generazione automatica: come funziona

### Condizioni (✅ `common/src/main/java/smartin/miapi/material/generated/GeneratedMaterialManager.java`)

Si avvia a ogni caricamento dei dati, dopo i tag. Il metodo `onReloadServer` è chiamato in coda a `ReloadableServerResources.updateRegistryTags`: mixin `neoforge/.../ReloadAbleServerResourcesMixin.java` riga 22. Quindi si avvia anche con `/reload`.

1. `generate_materials` falso → niente (riga 118).
2. Prende **tutti gli oggetti che sono `TieredItem`** (spade, asce, picconi… con un "Tier"). Servono tutte queste condizioni (righe 122-134):
   - il Tier ha un ingrediente di riparazione non vuoto;
   - il primo ingrediente non è nel tag `miapi:forbidden`;
   - l'oggetto non corrisponde a `block_regex`;
   - **nessun** oggetto dell'ingrediente di riparazione è già un materiale di Truly Modular. È questo che permette di sostituirli (vedi sezione 2).
3. Raggruppa per Tier, unendo i Tier "uguali": stesso tag di scavo, stessi ingredienti, statistiche entro lo 0,1% (righe 135-161, `isSameTier` 297-328).
4. **Tiene solo i gruppi con almeno una `SwordItem` e una `AxeItem`** (righe 162-170). Lo dice anche `COMPAT.md`: «Swords and Axes need to implement as the same tool family».
5. `generate_other_materials` vero → crea il materiale (righe 172-193). **Nessun limite di numero**: il `limit(max_generated_materials)` per questi è commentato (righe 194-226).
6. Legni e pietre, a parte (righe 230-282):
   - ogni oggetto in `minecraft:planks` o `minecraft:stone_tool_materials` che oggi corrisponde al materiale "wood" o "stone" diventa una **copia con le stesse statistiche**, con nome e colori propri (`GeneratedMaterialFromCopy.java`);
   - qui vale `max_generated_materials` (200 per tipo);
   - nel codice queste copie si registrano **solo sul client** (righe 46-58). Sono estetiche.
7. Ricette del tavolo da forgiatura (`SmithingRecipeUtil.java`). Se una mod ha una ricetta di potenziamento che produce la sua spada partendo da una spada di un materiale già noto, il materiale nuovo diventa "da forgiatura": si ottiene potenziando una parte modulare, come la netherite (righe 75-137, 169-195).

### Statistiche (✅ `GeneratedMaterial.java` righe 141-176)

| Statistica | Da dove viene |
|---|---|
| `hardness` (danno delle lame) | danno della **prima** `SwordItem` del gruppo, cioè dei soli modificatori dell'oggetto: per il ferro 3+2 = 5 |
| `density` (danno in più delle armi pesanti) | danno dell'ascia − danno della spada, minimo 0 |
| `flexibility` (archi, armi leggere) | velocità di scavo del Tier ÷ 4; **0 se il gruppo è "crystal"** |
| `tier` | danno del piccone; se manca, danno della spada − 2 |
| `durability` | usi del Tier − 15 |
| `mining_speed`, `enchantability` | dal Tier |
| livello di scavo | il tag `incorrect_for_…` del Tier (quello della mod, es. `twilightforest:incorrect_for_ironwood_tool`) |
| gruppo (decide su quali parti si può usare) | nome dell'oggetto di riparazione: contiene `ingot` → `metal`; contiene `stone` → `stone`; `bone` → `bone`; assi → `wood`; altrimenti `crystal` |

I materiali vanilla del .jar seguono la stessa formula, quindi le scale sono confrontabili. Il ferro (`data/miapi/miapi/materials/metal/iron.json`) ha hardness 5, tier 3 e durability 235 (250 − 15). Il diamante ha 6, 4 e 1546. La netherite ha 7, 5 e 2016. ✅ Nel codice della 2.3.9 i materiali generati **non impostano `toughness`** (vale 0). ✅

**Stime per i materiali del pack** 🔶 (formula qui sopra e codice delle mod; i valori veri si leggono in gioco con `/miapi material <id>`):

| Materiale | Gruppo | hardness | density | flex | tier | durability | scavo (velocità / livello) | Note |
|---|---|---|---|---|---|---|---|---|
| Holystone (Aether) | stone | 4 | 4 | 1 | 2 | 116 | 4 / pietra | come la pietra |
| Zanite (Aether) | **stone** | 5 | 3 | 1,5 | 3 | 235 | 6 / ferro | "zanite_**gemstone**" contiene "stone" |
| Gravitite (Aether) | crystal | 6 | 2 | 0 | 4 | 1546 | 8 / diamante | come il diamante |
| Ironwood (TF) | metal | 5 | 3 | 1,6 | 3 | 497 | 6,5 / tag proprio | incantabilità 25 |
| Steeleaf (TF) | metal | 6 | 3 | 2 | 4 | 116 | 8 / tag proprio | durata bassissima |
| Knightmetal (TF) | metal | 6 | 3 | 2 | 4 | 497 | 8 / tag proprio | |
| Cloggrum (Undergarden) | metal | **10** | 0 | 1,5 | 4 | 271 | 6 / ferro | "spada" letta = **battleaxe** |
| Froststeel (Undergarden) | metal | 5 | 3 | 1,75 | 3 | 560 | 7 / ferro | incantabilità 20 |
| Utherium (Undergarden) | crystal | 6,5 | 2 | 0 | 4,5 | 1264 | 8,5 / diamante | |
| Forgotten (Undergarden) | metal | **10** | 0 | 2 | 4 | 1861 | 8 / tag proprio | battleaxe; forgiatura da cloggrum |
| Resonarium (DD) | crystal | 6 | 2 | 0 | 4 | 1586 | 8,5 / tag proprio | forgiatura da **diamante** |
| Warden (DD) | crystal | 8 | 2 | 0 | 6 | 2504 | 10 / tag proprio | forgiatura da **netherite**; supera la netherite |

Le altre (skyjade e stratus di Deep Aether, black steel, pearlescent, psimetal, cognitive alloy) non le ho calcolate: non ho il sorgente o il .jar. Stratus si forgia dalla gravitite: ricetta nel .jar di Deep Aether, `data/deep_aether/recipe/stratus_sword_smithing.json`. ✅

Fonti delle stime: TF `src/main/java/twilightforest/util/TFToolMaterials.java` e `init/TFItems.java` righe 73-175, commit `9e40a757` del ramo `1.21.1` del 13/10/2026 (il pack ha la 4.8.3345: possibili piccole differenze). Undergarden `registry/UGItemTiers.java`, `UGItems.java` righe 69-92 e `item/tool/BattleaxeItem.java` (estende `SwordItem`, danno 7 + bonus), commit `6d7f02de`. DD `util/DDTiers.java` e `content/DDItems.java`, commit `d42d22a2`. Aether `item/combat/AetherItemTiers.java`, commit `e07d30e1`.

### Proprietà copiate dallo strumento originale (✅ `GeneratedMaterialPropertyManager.java`)

Le copia per lama, ascia, piccone, pala, zappa e armature, ognuna con un interruttore e un elenco di esclusioni nella config:
- **azione col tasto destro** (`CopyItemAbility`: chiama `use` dell'oggetto originale);
- **effetti al colpo** (`CopyItemOnHit`: chiama `hurtEnemy`/`postHurtEnemy` dell'originale);
- descrizione;
- **tag dell'oggetto** (anche `ItemStack.is(tag)` risponde sì: mixin `MiapiItemStackMixin` riga 49);
- componenti diversi dagli strumenti vanilla (es. resistenza al fuoco);
- incantesimi già presenti;
- attributi extra.

Limite 🔶: un effetto che la mod gestisce **in un evento** che controlla l'oggetto esatto non passa all'oggetto modulare. Esempio verificato nel codice: il bonus del knightmetal contro i nemici con armatura sta in `twilightforest/events/ToolEvents.java` riga 118 (`weapon.is(TFItems.KNIGHTMETAL_SWORD)`). L'effetto della spada fiery invece sta in `hurtEnemy` (`FierySwordItem.java`) e passerebbe, ma fiery non viene generato (vedi sotto).

### La nostra config (✅ `/mnt/user-data/uploads/config/miapi_server.jsonc`)

Tutti i valori sono quelli predefiniti:
- `generate_materials: true` (riga 7)
- `max_generated_materials: 200` (riga 9; vale solo per legni e pietre)
- `block_regex: "^(chipped|everycompat).*"` (riga 14)
- `generate_wood_materials`, `generate_stone_materials`, `generate_other_materials`: tutte `true` (righe 16, 18, 20)
- tutte le `generate_properties` attive; `lore_property` esclude `mythic` (righe 22-92)
- `smithing.enable: true`, `allow_smithing_multi_ingredient_recipes.enable: true`
- `live_update: false` (riga 180): se cambia un materiale, gli oggetti già fatti si aggiornano solo rifacendoli
- `loot_category.is_swapping_materials_enabled: true` (riga 185), vedi i rischi

Nomi e valori predefiniti: `common/.../config/MiapiServerConfig.java` righe 180-268. ✅

### Cosa è stato generato davvero nel nostro pack (✅ log `/mnt/user-data/uploads/logs/latest.log`, 21/10/2026)

- Server: «Loaded **130** Materials» (riga 4636). Corrisponde a 110 file del .jar, 18 generati e 2 non identificati ❓.
- Client: «Loaded **242** Materials» (riga 6481). Gli altri 112 sono le copie di legni e pietre, solo estetiche.
- Stessi numeri nel log del 19/10.
- I 18 nomi sono negli errori «Entry with name … already exists» (estratto: `estratti/log-materiali.txt`):

| Mod | Materiali generati (ID `miapi:generated/…`) |
|---|---|
| The Aether | gravitite (`block.aether.enchanted_gravitite…`), holystone, zanite |
| Deep Aether | skyjade, stratus |
| Twilight Forest | ironwood, steeleaf, knightmetal |
| Undergarden | cloggrum (chiave: battleaxe), froststeel, utherium, forgotten (chiave: battleaxe) |
| Deeper and Darker | resonarium, warden |
| Cataclysm | black steel |
| Unusual End | pearlescent |
| Psi | psimetal |
| Cognition | cognitive alloy |

**Assenti, e perché:**
- **Fiery** (TF): ha spada e piccone ma **non l'ascia**. ✅ `TFItems.java` righe 90-91.
- **Giant, ice, glass** (TF): niente ascia. ✅ Glass non ha nemmeno l'ingrediente di riparazione.
- **Valkyrie** (Aether): niente spada, solo la lancia, e tag di riparazione vuoto. ✅
- **Skyroot** (Aether): ha spada e ascia ma non risulta nel log. **Motivo non trovato** ❓. Le assi di skyroot non sono in `minecraft:planks`, né nel .jar né nell'inventario. Da controllare in gioco con `/miapi get-hand-material` tenendo in mano le assi di skyroot.
- **Iesnium** (Occultism): solo picconi. ✅
- **Mekanism**: nessuno strumento a materiale (Mekanism Tools non è nel pack). ✅
- **Create**: nessuno strumento d'ottone. ✅
- **Ignitium, cursium, witherite** (Cataclysm): solo armature o lingotti. ✅
- **Ars Nouveau**: niente set spada+ascia. ✅

Coppie spada+ascia in tutto l'inventario: script `scripts/sword_axe_sets.py` nello scratchpad. Anche Born in Chaos (sweet), Create Confectionery (candy cane) e Scriptor (bound) hanno spada+ascia ma non risultano generati; non ho indagato oltre.

Le parti modulari accettano solo certi gruppi di materiale. Es. le lame di Arsenal: `wood, metal, flint, bone, stone, crystal, glass`. Elenco completo in `estratti/gruppi-ammessi-moduli.txt`. ✅ Tutti i 18 generati sono in gruppi accettati da lame e attrezzi.

---

## 2. Materiali scritti a mano (datapack)

### Percorso e ID (✅)

- Cartella: `data/<namespace>/miapi/materials/…/<nome>.json`. Si registra in `common/.../datapack/ReloadHelpers.java` righe 28-36 (`"miapi/materials"`, priorità −2: **prima** della generazione, che ha −1). L'ordine va dal numero più basso: `ReloadEvent.java` righe 20-21 e 70.
- ID = `<namespace>:<percorso senza .json>`, es. `data/matteo_tweaks/miapi/materials/tf/fiery.json` → `matteo_tweaks:tf/fiery` (`HierarchicalReloadBuilder.java` righe 101-103).
- Caricamento su NeoForge: `neoforge/.../MiapiReloadListenerForge.java` righe 38-55. Usa `listResourceStacks` su **tutti i datapack** e per lo stesso file tiene **l'ultimo**, cioè quello più in alto. Quindi un datapack Paxi può aggiungere materiali e anche **rimpiazzare** un file del .jar con lo stesso percorso, es. `data/miapi/miapi/materials/metal/iron.json`. ✅ codice, 🔶 in gioco.
- **Condizione di caricamento**: campo `"load_condition"` in testa al file, con le condizioni di Miapi. Es. `{"type": "mod_loaded", "mod": "twilightforest"}` (righe 70-84; condizione `IsModLoadedCondition.java`). Il caricatore di Miapi legge il testo grezzo e **non applica `neoforge:conditions`**. 🔶 Un campo estraneo verrebbe letto come statistica: i documenti dicono che ogni campo non riconosciuto è un numero. La regola del datapack in AGENTS.md (sezione 7) per questi file andrebbe adattata.

### Formato: esempio reale (✅ `data/miapi/miapi/materials/metal/iron.json` del .jar; copia in `estratti/miapi-metal-iron.json`)

```json
{
  "icon": "textures/item/iron_ingot.png",
  "groups": ["metal"],
  "hardness": 5, "density": 3.8, "flexibility": 1, "durability": 235,
  "armor_durability": 15, "armor_toughness": 0.0, "enchantability": 14, "toughness": 0, "tier": 3,
  "color": "FCFCFC",
  "color_palette": { "type": "grayscale_map", "colors": { "24": "181818", "68": "444444", "107": "6b6b6b", "150": "969696", "190": "bebebe", "216": "d8d8d8", "255": "ffffff" }, "filler": "interpolate" },
  "textures": ["metallic", "bright"],
  "mining_speed": 6,
  "mining_level": "minecraft:incorrect_for_iron_tool",
  "items": [
    { "item": "minecraft:iron_ingot", "value": 1.0 },
    { "item": "minecraft:iron_nugget", "value": 0.11112 }
  ]
}
```

Campi riconosciuti (✅ `material/codec/CodecMaterial.java` righe 153-178):
- aspetto: `icon`, `color_palette`, `dye_color_palette`, `textures`, `color`, `translation` (nome senza resource pack);
- gruppi: `groups`, `hidden_groups`, `gui_groups`;
- proprietà: `properties`, `display_properties`, `hidden_properties`, divise per etichetta di parte: `default`, `blade`, `tool`, `axe`, `pickaxe`, `armor`…;
- scavo e ingredienti: `mining_level`, `items` (con `item` o `tag` e un `value`);
- altro: `generate_converters`, `variants`.

Ogni altro campo numerico è una statistica. Per i colori c'è anche `"type": "image_generated_item", "item": "<id>"`, che ricava la tavolozza dalla texture dell'oggetto (`palette/MaterialRenderControllers.java` riga 57). ✅

Altre due forme:
- **Ereditarietà**: `{"parent": "miapi:glass/glass", "data": {…}}`, es. `glass/black.json` del .jar. ✅ Il `parent` deve essere un materiale da datapack, non uno generato (`HierarchicalReloadBuilder.java` riga 129).
- **Estensione**: `data/<ns>/miapi/material_extensions/*.json` con `"key"`, come fa Armory. Si applica **solo ai materiali da datapack**, non a quelli generati (`MaterialProperty.java` righe 102-117). ✅

### Sostituire o bloccare un materiale generato (✅ codice)

- **Sostituire**: un nostro materiale che elenca in `items` l'ingrediente di riparazione della mod (es. `twilightforest:steeleaf_ingot`). Il generatore vede che l'oggetto è già un materiale e salta quello strumento (`GeneratedMaterialManager.java` righe 131-132). Però si perdono le proprietà copiate in automatico, a meno di riscriverle a mano.
- **Bloccare**:
  - `block_regex` (sull'ID degli oggetti);
  - il tag `minecraft:miapi_forbidden`, che `miapi:forbidden` include;
  - i `blocked` di ogni proprietà (regex sull'ID del materiale).
- **Partire da quello generato**: il comando **`/miapi material <id>`** (con suggerimenti) manda al client il JSON del materiale, copiabile negli appunti. C'è anche `/miapi get-hand-material`. Per i generati il JSON è già nel formato da datapack (`MaterialCommand.java`, `MaterialHelper.java`). ✅ codice, 🔶 in gioco.
- Strumento web citato dagli autori: **Truly Modular Material Helper** (`COMPAT.md`; già in `0301-mod`).

### Esempio proposto, non provato 🔶: Fiery (TF), che oggi manca

Valori ricavati con la stessa formula dal Tier `FIERY` (1024 usi, velocità 9, danno 4, incantabilità 10). La densità è stimata perché manca l'ascia. Il tag `twilightforest:incorrect_for_fiery_tool` esiste nell'inventario. ✅

```json
{
  "load_condition": { "type": "mod_loaded", "mod": "twilightforest" },
  "translation": "Infuocato ",
  "icon": { "type": "item", "item": "twilightforest:fiery_ingot" },
  "groups": ["metal"],
  "hardness": 7, "density": 3, "flexibility": 2.25, "tier": 5,
  "durability": 1009, "mining_speed": 9, "enchantability": 10,
  "mining_level": "twilightforest:incorrect_for_fiery_tool",
  "color_palette": { "type": "image_generated_item", "item": "twilightforest:fiery_ingot" },
  "properties": { "default": { "fire_proof": true } },
  "items": [ { "item": "twilightforest:fiery_ingot", "value": 1.0 } ]
}
```

Per l'effetto di fuoco al colpo si potrebbe aggiungere `"copy_item_on_hit": ["twilightforest:fiery_sword"]` sotto `blade`. Il nome della chiave è dedotto da `CopyItemOnHit.KEY` e va provato.

---

## 3. Addon e compatibilità

Ricerca sull'API di Modrinth per "truly modular", "truly", "miapi" e "tetracelium" (con filtro 1.21.1). ✅

| Nome | Link | 1.21.1 NeoForge | Ultima versione | Licenza | Cosa copre |
|---|---|---|---|---|---|
| **Truly Compatible** (datapack) | https://modrinth.com/mod/truly-compatible | **No** (solo 1.20, 1.20.1) | 1.0.2d, 03/10/2026 | GPL-3.0-only | Materiali di Alex's Caves e Alex's Mobs, Apotheosis, AllTheOres, Aquaculture 2, Born in Chaos, **Cataclysm**, **Create**, Create Crafts & Additions, Farmer's Delight, Ice and Fire, Iron's Spellbooks, Silent Gear e altri. Nell'elenco, che la pagina dichiara incompleto, non compaiono TF, Aether e Undergarden. La pagina parla di un port 1.21 fatto da "Piccioto" sul Discord di Truly Modular: non verificabile da qui ❓ |
| Truly modular x Epic Fight (Unofficial) | https://modrinth.com/mod/truly-modular-x-epic-fight-unofficial | Sì | 1.0.0, 08/08/2026 | MIT | Combattimento Epic Fight; non risultano materiali. Epic Fight non è nel pack |
| Create: Truly Modular | https://modrinth.com/mod/create-truly-modular | No (1.20.1) | 22/05/2025 | MIT | Elmo da sub e serbatoi di Create; niente materiali |
| Back Weapon Slot MI | https://modrinth.com/mod/back-weapon-slot-mi | No (1.20.1 Forge) | 23/12/2024 | MIT | Slot per l'arma sulla schiena |
| TFC Modular | https://modrinth.com/mod/tfc-modular | No (1.20.1 Forge) | 15/01/2026 | MIT | TerraFirmaCraft |
| (per confronto) tetracelium | https://modrinth.com/mod/tetracelium | No (1.20.1) | 12/04/2026 | ARR | È per Tetra, non per Truly Modular |

Nessuna mod del pack porta file `miapi/materials` propri: ho controllato le 253 voci dell'inventario, e solo i 4 .jar di Truly Modular hanno dati `miapi`. ✅ "Truly Modular: Next Level" è già in `0601`: mai rilasciata. Il motivo per cui non c'è un Tetracelium è dichiarato dagli autori in `COMPAT.md`: la compatibilità si affida alla generazione automatica e al Material Helper.

---

## 4. Problemi noti

**Issue su GitHub** (https://github.com/Truly-Modular/Modular-Item-API/issues): 4 aperte oggi. ✅ Le chiuse e la ricerca non sono leggibili da qui: la ricerca di GitHub è bloccata per gli strumenti web e l'API richiede di collegare il repository con credenziali, cosa che non ho fatto. ❓

| # | Titolo | Stato | Riguarda il pack? |
|---|---|---|---|
| 118 | Crash with Accessories when an entity takes damage | aperta (07/04/2026) | **Sì**: Accessories è dentro l'Aether. È già **B07**. L'autore dice che l'ultima release dovrebbe evitarlo; il segnalatore non ha confermato |
| 87 | Farmer's Delight compat (1.21.1 NeoForge) | aperta, etichetta `fixedInNextRelease` | Sì (FD): il pugnale sul tagliere sarebbe risolto; le parti d'ascia montate sul piccone non scortecciano i tronchi |
| 102 | Crash con Epic Fight | aperta | No |
| 143 | Texture rotte in terza persona | aperta (07/10/2026) | Forse (grafica) |

Nessuna issue aperta parla di materiali delle mod. Nel changelog di Modrinth ci sono correzioni ai materiali generati fino alla 2.3.7 (gruppi nell'interfaccia), alla 2.3.0 (statistiche e toughness), alla 2.1.1 (livello di scavo e danno dell'ascia) e alla 2.2.1 («material decoding that could brick worlds with removed materials»). ✅

**Problemi visti nel codice e nel nostro log:**
- **Errori «Error during Smithing recipe generation!»** (B05). Sono **rumore**. Quando un materiale non ha ricette di forgiatura, `testForSmithingMaterial` lo registra **due volte** (`SmithingRecipeUtil.java` righe 92-94 e 130-132). La seconda volta dà «already exists» e l'errore viene catturato. Il materiale resta registrato una volta. ✅ Sono 18 errori per caricamento, più qualcuno per i materiali da forgiatura e un «Exception during SmithingRecipe setup!» finale. 🔶 In un caso limite quell'eccezione finale potrebbe saltare la registrazione di un materiale messo in coda dopo.
- **Durezza gonfiata dell'Undergarden**. Il codice legge il danno della **prima** `SwordItem` trovata. Per cloggrum e forgotten è la battleaxe (danno 7 + bonus = 10), quindi la durezza stimata è 10, più della netherite (7). ✅ codice e log (ID `…cloggrum_battleaxe`), 🔶 valore in gioco.
- **Gruppi decisi dal nome**: zanite finisce in `stone`; gravitite, utherium, resonarium e warden finiscono in `crystal`, con flessibilità 0. ✅
- **`allow_smithing_multi_ingredient_recipes`** sembra funzionare **al contrario** del commento della config: se è attivo, le ricette con più oggetti di base vengono **saltate** (righe 107-109). ✅ codice; effetto pratico minore.
- **ID dei generati fragili**: l'ID è il "nome tecnico" dell'oggetto di riparazione più quello della prima spada. Se un aggiornamento cambia l'ordine degli oggetti o l'ingrediente, l'ID cambia, e le parti già fatte perdono il materiale. 🔶 I materiali scritti a mano hanno un ID stabile.
- **Bottino**: con `is_swapping_materials_enabled` attivo, gli strumenti dei forzieri convertiti in modulari possono ricevere un materiale **qualsiasi del registro**, generati compresi. Il materiale resta simile all'originale (`MaterialSwapLootFunction.java` righe 162-205; limiti −3,5 e +0,4 nella config). 🔶 Possibile fuga di materiali di altre dimensioni nei forzieri dell'Overworld.
- **B04** (Apotheosis non legge il tier delle armi modulari all'avvio) ha la stessa origine già nota: errori catturati.

---

## 5. Cosa ne segue per la progressione a tappe (valutazione, da decidere)

- 🟢 **La base c'è già**: 18 materiali delle mod sono usabili senza fare nulla. Hanno il **livello di scavo della mod** (i tag propri di TF, DD e Undergarden restano validi) e statistiche sulla stessa scala dei vanilla.
- 🟢 **I potenziamenti delle mod vengono ricopiati da soli** come materiali da forgiatura: diamante → resonarium, netherite → warden, gravitite → stratus, cloggrum → forgotten. ✅ ricette, 🔶 risultato in EMI. Sono già "tappe" naturali.
- 🟡 **Correggere a mano** i casi storti (cloggrum e forgotten) e **aggiungere i mancanti**: fiery, skyroot se serve, iesnium, metalli di Mekanism (`c:ingots/steel`, `osmium`, `bronze`…), ottone di Create, metalli di Cataclysm. Tutto con file JSON nel datapack Paxi, `load_condition` e ID stabili. Va fatto **prima del mondo vero**.
- 🟡 **Cancelli per traguardo**: un materiale può dare alle parti la proprietà `crafting_condition`. Il controllo `craftAble` riceve le proprietà del materiale (`ModuleTagProperty.java` righe 34-66, `CraftingConditionProperty.java` righe 104-129). Esiste la condizione `advancement`. Quindi si potrebbe vietare la lavorazione dell'ironwood finché non si ha un certo progresso del Bosco. 🔶 Da provare.
- 🔴 `assume_item_id` (fa "fingere" all'oggetto modulare di essere quello della mod, per gli effetti a evento): i documenti stessi lo definiscono pericolosissimo.

---

## 6. Da provare in gioco (istanza dev)

1. `/miapi material miapi:generated/` + Tab: compaiono i 18? Leggere il JSON di zanite, cloggrum (hardness 10?) e warden.
2. Banco modulare: una lama di zanite e una testa di piccone di ironwood. Il piccone di ironwood rompe i blocchi di TF come quello originale?
3. EMI: ci sono le ricette `miapi:generated_material_recipe.*`? Potenziare una lama di diamante in resonarium.
4. Skyroot: `/miapi get-hand-material` con le assi di skyroot in mano, per capire perché manca.
5. Un file nel datapack Paxi (es. fiery con `load_condition`), poi `/reload`: «Loaded 131 Materials» e il materiale nel banco. Prova di sostituzione con steeleaf: il generato sparisce.
6. `crafting_condition` con `advancement` in un materiale di prova: blocca la lavorazione prima del traguardo?
7. Effetti: knightmetal (bonus contro le armature: atteso **no**); psimetal (tasto destro e colpo: nessun crash?).
8. B07 (Accessories), come già previsto in `0502`.
9. Forzieri: compaiono armi modulari di materiali di altre mod?

---

## 7. Fonti

- Sorgente di Truly Modular, tag `2.3.9-1.21` (commit `2562eda9`), https://github.com/Truly-Modular/Modular-Item-API. File letti:
  - in `common/src/main/java/smartin/miapi/`: `material/generated/{GeneratedMaterialManager, GeneratedMaterial, GeneratedMaterialPropertyManager, GeneratedMaterialFromCopy, SmithingRecipeUtil, MaterialHelper}.java`, `material/{MaterialProperty, MaterialCommand}.java`, `material/codec/CodecMaterial.java`, `datapack/{ReloadHelpers, HierarchicalReloadBuilder, ReloadEvent}.java`, `config/MiapiServerConfig.java`, `modules/properties/{CraftingConditionProperty, FakeItemTagProperty}.java`, `modules/properties/onHit/CopyItemOnHit.java`, `modules/abilities/CopyItemAbility.java`, `modules/conditions/IsModLoadedCondition.java`, `loot/MaterialSwapLootFunction.java`;
  - `neoforge/src/main/java/smartin/miapi/forge/MiapiReloadListenerForge.java`;
  - `COMPAT.md`, `CHANGELOG.md`, `docs/datapack/material/**`.
- .jar del pack in `/mnt/user-data/uploads/mods/`: `Truly-Modular-*` (110 materiali, tutti vanilla; gruppi ammessi dalle parti), `aether-1.21.1-1.5.10`, `deep_aether-1.21.1-1.1.5.1`, `unusualend-2.3.1b`. Lettura con `python3 -I` e zipfile, più un lettore della struttura delle classi (solo superclasse e costanti): `scripts/classinfo.py` nello scratchpad.
- Config reale: `/mnt/user-data/uploads/config/miapi_server.jsonc`. Log reali: `/mnt/user-data/uploads/logs/latest.log` (21/10) e `2026-10-19-2.log.gz`.
- Inventario: `/home/claude/mango-craft/1.21.1/data/inventario/mods/*.json`.
- Sorgenti delle mod:
  - Twilight Forest, ramo `1.21.1`, commit `9e40a757` (13/10/2026);
  - Undergarden, ramo `1.21`, commit `6d7f02de`;
  - Deeper and Darker, ramo `neoforge-1.21`, commit `d42d22a2`, con le ricette `src/generated/.../recipe/*_sword_smithing.json`;
  - Aether, ramo `1.21.1-develop`, commit `e07d30e1`.
- Modrinth API:
  - https://api.modrinth.com/v2/project/modular-item-api (licenza PolyForm Shield, sorgente);
  - `…/project/modular-item-api/version?game_versions=["1.21.1"]&loaders=["neoforge"]` (2.3.9 del 24/08/2026 è l'ultima; changelog);
  - `…/v2/search?query=truly%20modular`, `…query=truly&facets=[["versions:1.21.1"]]`, `…query=miapi`, `…query=tetracelium`;
  - `…/project/truly-compatible` e `/version`;
  - `…/project/truly-modular-x-epic-fight-unofficial/version`.
- GitHub: https://github.com/Truly-Modular/Modular-Item-API/issues (elenco delle aperte), `/issues/118`, `/issues/87`.
- Estratti salvati qui: `estratti/log-materiali.txt`, `estratti/miapi-metal-iron.json`, `estratti/miapi-glass-black-parent.json`, `estratti/gruppi-ammessi-moduli.txt`.
