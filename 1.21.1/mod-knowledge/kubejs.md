# KubeJS

Aggiornata il 24/10/2026 · stato: **nel pack dalla 0.7.2** (solo per il dump dei dati del gioco) · versione 2101.7.2-build.377, con Rhino 2101.2.7-build.85 e Better Advanced Tooltips 2101.1.0-build.5 · licenza LGPL-3.0 (Rhino MPL-2.0, Better Advanced Tooltips MIT) · fonti: sorgente di KubeJS (ramo `2101`, commit `1b4e9b8` del 18/09/2026), patch di NeoForge (ramo `1.21.1`: `PotionBrewing`, `BrewingStandBlockEntity`) e `BrewingRecipe`, API di Modrinth, inventario del pack. Temi: `../theme-knowledge/pozioni.md`.

## Perché è nel pack

Non per cambiare il gioco: lo script del pack **legge soltanto**. Serve a chiedere al gioco i dati che nei file dei jar non ci sono (effetti delle pozioni, categoria degli effetti, ricette dell'alambicco, effetti dei cibi) e a scriverli per la base dati del repository. Scelta di Matteo del 24/10/2026 (`../lavoro/versioni/v0.7.2.md`), dopo il confronto con Registry Dump (solo gli id, che l'inventario ha già) e Info Dump (contenuto non documentato).

## Lo script del pack

`../pack/kubejs/server_scripts/mango_dump.js` → comando **`/mango_dump`**, scrive in `logs/mango-craft-dump/` dell'istanza (formato e sezioni nel commento in testa). Si importa con `scripts/dump_importa.py` in `../data/dump/`.

## Fatti verificati nel sorgente

- **Comandi semplici**: `ServerEvents.basicCommand('<nome>', event => …)` registra il comando `/<nome>`, usabile in single player o da operatore (`KubeJSCommands`, `requires(spOrOP)`); l'evento dà `getLevel()`, `getServer()`, `getPlayer()` e `respond(Component)`.
- **File**: `JsonIO.write(percorso, dati)` crea le cartelle e scrive JSON leggibile; un percorso scritto come testo è relativo alla cartella del gioco, e **fuori dalla cartella del gioco non si scrive** (`KubeJSPaths.verifyFilePath`). Oggetti e liste JavaScript si convertono da soli in JSON (`JsonUtils.of`).
- **Classi Java**: `Java.loadClass` apre `net.minecraft` e `net.neoforged` (non `net.neoforged.fml`), `java.util` e poco altro: niente `java.io`, `java.nio`, riflessione (`kubejs.classfilter.txt`). I campi privati delle classi del gioco non si leggono.
- **Mod caricate**: `Platform.getMods()` dà id e versione di ogni mod (letti da NeoForge).
- **Alambicco** (patch di NeoForge 1.21.1): `level.potionBrewing()`; `isIngredient(oggetto)`, `hasMix(bottiglia, ingrediente)`, `mix(ingrediente, bottiglia)` (l'ordine è questo) comprendono anche le ricette NeoForge; `getRecipes()` elenca solo quelle NeoForge (`BrewingRecipe` ha `getInput()`, `getIngredient()`, `getOutput()`; le classi proprie delle mod no). Le miscele del gioco base sono in liste private: il dump le trova **provando** ogni ingrediente su ogni pozione.
- Il jar di KubeJS contiene una copia di Better Advanced Tooltips (build.1); il pack porta la build.5 come mod a sé, e NeoForge tiene la più recente.

## Da sapere

- Al primo avvio KubeJS crea `kubejs/` (config, README); gli script d'esempio li crea solo se la cartella non c'era, e packwiz la crea prima con il nostro script.
- Gli errori degli script finiscono in `logs/kubejs/server.log`; il nostro script scrive anche gli errori di ogni sezione in `meta.json`.
- Better Advanced Tooltips aggiunge informazioni ai tooltip in modalità F3+H (etichette con Maiusc, componenti con Alt).
