# KubeJS

Aggiornata il 26/10/2026 · stato: **nel pack dalla 0.7.2** (solo per il dump dei dati del gioco) · versione 2101.7.2-build.377, con Rhino 2101.2.7-build.85 e Better Advanced Tooltips 2101.1.0-build.5 · licenza LGPL-3.0 (Rhino MPL-2.0, Better Advanced Tooltips MIT) · fonti: sorgente di KubeJS (ramo `2101`, commit `1b4e9b8` del 18/09/2026), patch di NeoForge (ramo `1.21.1`: `PotionBrewing`, `BrewingStandBlockEntity`) e `BrewingRecipe`, API di Modrinth, inventario del pack. Temi: `../theme-knowledge/pozioni.md`.

## Perché è nel pack

Non per cambiare il gioco: lo script del pack **legge soltanto**. Serve a chiedere al gioco i dati che nei file dei jar non ci sono (effetti delle pozioni, categoria degli effetti, ricette dell'alambicco, effetti dei cibi) e a scriverli per la base dati del repository. Scelta di Matteo del 24/10/2026 (`../lavoro/versioni/v0.7.2.md`), dopo il confronto con Registry Dump (solo gli id, che l'inventario ha già) e Info Dump (contenuto non documentato).

## Lo script del pack

`../pack/kubejs/server_scripts/mango_dump.js` → comando **`/mango_dump`**, scrive in `logs/mango-craft-dump/` dell'istanza (formato e sezioni nel commento in testa). Si importa con `scripts/dump_importa.py` in `../data/dump/`.

## Fatti verificati nel sorgente

- **Comandi semplici**: `ServerEvents.basicCommand('<nome>', event => …)` registra il comando `/<nome>`, usabile in single player o da operatore (`KubeJSCommands`, `requires(spOrOP)`); l'evento dà `getLevel()`, `getServer()`, `getPlayer()` e `respond(Component)`.
- **File**: `JsonIO.write(percorso, dati)` crea le cartelle e scrive JSON leggibile; un percorso scritto come testo è relativo alla cartella del gioco, e **fuori dalla cartella del gioco non si scrive** (`KubeJSPaths.verifyFilePath`). Oggetti e liste JavaScript si convertono da soli in JSON (`JsonUtils.of`).
- **Classi Java**: `Java.loadClass` apre `net.minecraft` e `net.neoforged` (non `net.neoforged.fml`), `java.util` e poco altro: niente `java.io`, `java.nio`, riflessione (`kubejs.classfilter.txt`). I campi privati delle classi del gioco non si leggono.
- **Nomi già presi** (`BuiltinKubeJSPlugin.registerBindings`): KubeJS mette al primo livello degli script nomi come `Items` (la classe `Items` del gioco), `Item`, `Blocks`, `Block`, `Text`, `Component`, `JsonIO`, `Platform`, `Java`, `Utils`, `NBT`, `Ingredient`, `Fluid`, `Color`, `BlockPos`, `Direction`, `Registry`, `Stats`, `UUID`, `Duration`, `ID`, `console`, `global`; anche le mod con un plugin ne aggiungono (Almost Unified: `AlmostUnified`). Uno script che dichiara al primo livello un `const` con lo stesso nome **non si carica** (Rhino: «redeclaration of var Items», prova del 25/10/2026). Il nostro script non dichiara niente al primo livello: le classi le carica dentro il comando, con il prefisso `$`.
- **Rhino e le dichiarazioni** (prova del 26/10/2026): un `const` dentro un blocco (`try`, `if`) di una funzione dà «redeclaration of var <nome>» **a ogni chiamata**, anche la prima; al primo livello di una funzione invece funziona. Il nostro script usa solo `var`.
- **`Ingredient.getItems()` è nascosto** agli script (`@HideFromJS` in `IngredientMixin`): gli oggetti di un ingrediente si leggono con `getStackArray()` (`IngredientKJS`, prefisso `kjs$` tolto).
- **Niente `getClass()`** sugli oggetti Java («Cannot find function getClass», prova del 26/10/2026): il nome della classe si ricava dal testo dell'oggetto (`String(oggetto)`, la parte prima di `@`).
- **Mod caricate**: `Platform.getMods()` dà id e versione di ogni mod (letti da NeoForge).
- **Alambicco** (patch di NeoForge 1.21.1): `level.potionBrewing()`; `isIngredient(oggetto)`, `hasMix(bottiglia, ingrediente)`, `mix(ingrediente, bottiglia)` (l'ordine è questo) comprendono anche le ricette NeoForge; `getRecipes()` elenca solo quelle NeoForge (`BrewingRecipe` ha `getInput()`, `getIngredient()`, `getOutput()`; le classi proprie delle mod no). Le miscele del gioco base sono in liste private: il dump le trova **provando** ogni ingrediente su ogni pozione.
- **Registri ed etichette** (formato 2 del dump, 26/10/2026): `registry.keySet()`, `registry.getTagNames()` (flusso di `TagKey`) e `registry.getTag(tagKey)` (`Optional` di `HolderSet.Named`, con `size()` e i `Holder`, `unwrapKey()`), usati anche dal server web di KubeJS (`KubeJSWeb`); `level.getRecipeManager().getRecipes()` dà i `RecipeHolder` (`id()`, `value().getType()`); i registri dinamici (`Registries.LOOT_TABLE`, `Registries.STRUCTURE_SET`) da `level.registryAccess().registryOrThrow(...)`. Verificato nel sorgente di KubeJS e NeoForge; nel gioco al primo dump del formato 2.
- Il jar di KubeJS contiene una copia di Better Advanced Tooltips (build.1); il pack porta la build.5 come mod a sé, e NeoForge tiene la più recente.

## Da sapere

- Al primo avvio KubeJS crea `kubejs/` (config, README) e uno script d'esempio in ogni cartella di script che non c'era: `startup_scripts/main.js` e `client_scripts/main.js` (scrivono «Hello, World!» nel log, innocui; visto il 25/10/2026). `server_scripts/` no, perché c'è il nostro.
- Gli errori degli script finiscono in `logs/kubejs/server.log`; il nostro script scrive anche gli errori di ogni sezione in `meta.json`.
- Better Advanced Tooltips aggiunge informazioni ai tooltip in modalità F3+H (etichette con Maiusc, componenti con Alt).
