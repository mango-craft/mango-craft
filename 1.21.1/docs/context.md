# Mango Craft — context.md

_Stato della progettazione · ultimo aggiornamento: 18/10/2026_

> **Stato del repository (18/10/2026)**: `main` e il tag `1.21.1-v0.1.1` contengono la **0.1.1**, la versione già provata in gioco. Si lavora sul ramo **`dev`** (seguito dall'istanza di prova); `main` avanza solo dopo la prova. Le aggiunte delle 0.2.x e le 30 mod approvate il 17/10 entrano a tappe secondo il **piano in 3.0**, fino alla **1.0.0** per il mondo vero. Questo documento descrive lo **stato della progettazione** completo, comprese le aggiunte non ancora nel pack.

Legenda: ✅ approvata · 👀 opzionale, da attenzionare · ⛔ scartata · ❓ da verificare · 🧪 da testare subito · ⚠️ attenzione

Struttura del documento: **1** Obiettivo e piattaforma · **2** Mod nel pack · **3** Da fare e da controllare · **4** Approvate per tema · **5** Opzionali per tema · **6** Scartate per tema · **7** Log decisioni

---

## 1. Obiettivo e piattaforma

Modpack personale da giocare **in single player** (non da pubblicare). Temi: Farmer's Delight con quanti più addon possibile · Botany Pots + addon · natura, erbe, tè e pozioni · tech (trasporto oggetti ed energia) · esplorazione (strutture, dimensioni, boss).

| Voce | Scelta | Note |
|---|---|---|
| Minecraft | **1.21.1** | Attenzione a non scegliere 1.21.11. La 1.21.1 è la versione "hub" del modding |
| Loader | **NeoForge 21.1.x** (ultima stabile) | Alcune mod chiedono build recenti (es. BotanyPotsAdditions ≥ 21.1.229) |
| Launcher | **Prism Launcher** | Scaricare le mod dal browser integrato (Modrinth/CurseForge) così le dipendenze arrivano da sole |
| Java | 21 | Gestito da Prism |
| Memoria | **8 GB** all'istanza | Il PC ha 32 GB; salire a 10–12 GB solo se servisse |
| Modalità | **Single player** | Niente mod pensate solo per il multiplayer |
| Shader | **Nessuno** | Scelta dell'utente |

---

## 2. Mod nel pack

Circa **172 mod** da installare a mano (3 legate all'Aether, condizionate a un test) + 1 resource pack. Le librerie le scarica Prism da solo: Architectury, Bookshelf, Prickle, Balm, GeckoLib, Placebo, Patchouli, Curios, Resourceful Lib/Config, Cristel Lib, Moog's Structure Lib, Lionfish API, Citadel, Puzzles Lib, Blueprint, TerraBlender, NexusLib, YUNG's API, Create: Dragons Plus, CreativeCore, Sophisticated Core, Fzzy Config, CorgiLib, Data Anchor, Kotlin for Forge (per Slice & Dice e Scriptor Magicae), Greenhouse Config (per Brewin' And Chewin'), Modonomicon e SmartBrainLib (per Occultism), Unfocused (per Scriptor Magicae), Lithostitched (per Regions Unexplored), Fusion (per Rechiseled), Moonlight (per Supplementaries)…

✅ **Verifica formale del 16/10/2026**: tutte le mod hanno una build NeoForge 1.21.1 (dettaglio in 3.6 e nel documento `verifica-versioni.md`).

- **Cucina e bevande (18)**: Farmer's Delight · Brewin' And Chewin' · Ender's Delight · Veggies Delight · Expanded Delight · Cultural Delights · Farmer's Delight: Extended · Create Slice & Dice · Create: Central Kitchen · HerbalBrews · Roaster's Delight · Delightful Fares · Twilight's Flavor & Delight · Undergarden Delight · Cataclysm Delight · Starcatcher's Delight · Aether's Delight ⚠️ · Spice of Life: Carrot Edition
- **Botany Pots (4)**: Botany Pots · Botany Trees · Botany Pots Tiers · BotanyPotsAdditions
- **Natura, erbe e pozioni (11)**: Hexalia · Hexerei · Aspect Alchemy · Bountiful Fares · [Let's Do] Vinery · [Let's Do] Meadow · [Let's Do] Farm & Charm · Seasonal Let's Do · Let's Do Addon Compat · Serene Seasons · Snow! Real Magic!
- **Tech (9)**: Create · Create Crafts & Additions · Create: Connected · Create: Enchantment Industry · Create: Integrated Farming · Mekanism · Mekanism Generators · Mekanism: Ponders · Pipez
- **Storage, zaini e trasporto (6)**: Storage Drawers · Tom's Simple Storage · Ender Storage · Sophisticated Backpacks · Sophisticated Backpacks Create Integration · Traveler's Backpack
- **Equipaggiamento e incantamenti (5)**: Truly Modular (Miapi) · TM: Arsenal · TM: Archery · TM: Armory · Apotheosis (+ moduli Apothic)
- **Strutture (17)**: YUNG's Better Dungeons · Mineshafts · Strongholds · Nether Fortresses · Ocean Monuments · Desert Temples · Jungle Temples · Witch Huts · Bridges · Extras · When Dungeons Arise · Dungeons and Taverns · Towns and Towers · Moog's End Structures · Sparse Structures · Explorer's Compass · Compass to Map: Xaero's
- **Dimensioni (7)**: The Twilight Forest · Deeper and Darker · The Undergarden · YUNG's Better End Island · Unusual End · The Aether ⚠️ · Deep Aether ⚠️
- **Boss e nemici (9)**: L_Ender's Cataclysm · Mowzie's Mobs · Born in Chaos · Born In Configuration · Friends & Foes · Mutant Monsters · Illager Invasion · Ender Dragon Fight Remastered · Gateways to Eternity
- **Villager (3)**: Easy Villagers · Easy Auto Cycler · Smarter Farmers
- **Animali e pesca (3)**: Starcatcher · Animal Pens · Animal Feeding Trough
- **Magia e oggetti magici (16)**: Ars Nouveau · Ars Delight (Flavors & Delight) · Ars Creo · Ars Mekanica · Ars Elemental · Ars QOL · Ars Unification · Not Enough Glyphs · Ars Controle · Artifacts · Occultism · Ars Ocultas · Occult Delight · Reactive Alchemy · Psi · Scriptor Magicae
- **Utilità di gioco (8)**: Chunk Loaders · Corail Tombstone · Waystones · Xaero's ↔ Waystones Compatibility · Akashic Tome · OmniTools · Chunky · XP Tome
- **Comodità (12)**: Mouse Tweaks · Inventory Essentials · Controlling · Crafting Tweaks · Simple Backups · Torchmaster · Comforts · Carry On · RightClickHarvest · FallingTree · Leaves Be Gone · Open Together
- **Interfaccia e mappa (15)**: EMI · JEI · EMI Loot · EMI Ores · Jade · AppleSkin · Polymorph · Enchantment Descriptions · Pick Up Notifier · YUNG's Menu Tweaks · Xaero's Minimap · Xaero's World Map · Just Enough Breeding · Just Enough Professions · SeasonHud
- **Atmosfera (11 + 1 resource pack)**: Shoulder Surfing Reloaded · Sound Physics Remastered · AmbientSounds · Subtle Effects · Particle Rain · LambDynamicLights · Enhanced Celestials · Travelers Titles · Not Enough Animations · Entity Model Features (EMF) · Entity Texture Features (ETF) · resource pack Fresh Animations
- **Performance (8)**: Sodium · Lithium · FerriteCore · ModernFix · ImmediatelyFast · Entity Culling · Structure Layout Optimizer · Clumps
- **Biomi (1)**: Regions Unexplored
- **Decorazione e costruzione (4)**: Supplementaries · Handcrafted · Rechiseled · Construction Sticks
- **Fix e compatibilità (5)**: Forgified Fabric API · AlmostUnified · Paxi · NetherPortalFix · AllTheLeaks

Ancora da decidere: le grandi aggiunte (5.9).

**Round del 17/10/2026 concluso**: approvate altre **30 mod** (non ancora nel pacchetto), datapack da ampliare (vasi, mercato, esperienza, correzioni) e passaggio a un repository GitHub con packwiz. Dettagli: documenti `decisioni/2026-10-17-round-opzionali.md` (decisioni, scartate, da tenere d'occhio), `datapack/conoscenze.md` (piano del datapack) e `datapack/vasi-copertura.md` (tabella delle piante). Le sezioni 4 e 5 di questo file verranno allineate quando il pack sarà nel repository.

⚠️ = entrano solo se passa il test Miapi/Accessories (vedi 3.2). Strumento esterno, non una mod: **Truly Modular Material Helper** (web app per datapack di materiali).

---

## 3. Da fare e da controllare

### 3.0 Piano verso la 1.0.0 (deciso il 18/10/2026)

**Flusso**: si lavora sul ramo `dev`, seguito dall'istanza di prova "Mango Craft (dev)". Quando una tappa passa la prova, `dev` si unisce a `main` con un merge vero (`--no-ff`, per conservare il grafico; niente pull request) e su `main` si crea il tag con il workflow Release. Documenti e workflow possono andare su `main` anche senza versione, solo se su `dev` non c'è una tappa in corso. Le **0.x** escono come pre-release, solo per prova; il **mondo vero parte dalla 1.0.0**, la prima versione con tutte le mod che generano il mondo.

| Tappa | Versione | Contenuto | Stato |
|---|---|---|---|
| 0 | — | Strumenti: workflow **Aggiungi mod Modrinth** (versione, hash e dipendenze presi da Modrinth con packwiz) e **Inventario** (elenco di oggetti, blocchi e tabelle letto dai file delle mod, per controllare i nomi usati nel datapack) | ✅ fatta (18/10, su `main`) |
| 1 | 0.2.3 | Le aggiunte del vecchio pacchetto 0.2.3: Regions Unexplored, Supplementaries, Handcrafted, Rechiseled, Construction Sticks, Chunky, Clumps, XP Tome, Just Enough Breeding/Professions, NetherPortalFix, SeasonHud, Smarter Farmers, Open Together, AllTheLeaks (CurseForge) + Lithostitched, Fusion, Moonlight; cassaforte del Galeone nel datapack | ✅ provata e rilasciata (18/10, pre-release `1.21.1-v0.2.3`) |
| 2 | 0.3.0 | Cucina, agricoltura, esperienza: My Nether's Delight, Chef's Delight, Create Confectionery, Rustic Delight, Ocean's Delight, Autochef's Delight, Farming for Blockheads, Cognition; **pesce cotto di Starcatcher** nelle etichette del pesce cotto (approvato 18/10) | 🧪 su `dev`, da provare |
| 3 | 0.4.0 | Decorazione e tech: Macaw's Roofs/Paths/Bridges/Windows, Diagonal Fences/Walls/Windows, Chimes, Exposure, Goblin Traders, Guard Villagers, Every Compat, Copycats+ | da fare |
| 4 | 0.5.0 | Esplorazione: Jaden's Nether Expansion (+ Elysium API, Lodestone), Moog's Nether Structures, Nether Depths Upgrade, Aures Farmers Structures, Better Archeology, Nature's Compass, Aquamirae, Creeper Overhaul, Paragliders | da fare |
| 5 | 0.6.0 | Datapack e config: correzione Berserker, esperienza Create ↔ Cognition, mercato di Farming for Blockheads, vasi (~270 piante, 13 terreni, alberi di Bountiful Fares), config di Every Compat, Jaden's, Moog's, Artifacts | da fare |
| 6 | 0.6.x → **1.0.0** | Mondo di prova: Chunky, mappa di Xaero, densità delle strutture, Nether, `/botanypots debug`, esperienza; correzioni; poi release 1.0.0 e mondo vero | da fare |

**Stato per gruppi** (aggiornato al 18/10/2026) · ✅ fatto · 🧪 da provare · ⏳ previsto

| Gruppo di mod | Cosa | Stato |
|---|---|---|
| Base del pack | Cucina e Farmer's Delight, vasi, natura e pozioni, Create e Mekanism, storage e zaini, Truly Modular e Apotheosis, strutture, dimensioni, boss, villager, magia, comodità, interfaccia, atmosfera, performance, fix (199 file) | ✅ 0.1.1 |
| Biomi e costruzione | Regions Unexplored, Supplementaries, Handcrafted, Rechiseled, Construction Sticks (+ 3 librerie) | ✅ 0.2.3 |
| Utilità | Chunky, Clumps, XP Tome, Just Enough Breeding e Professions, NetherPortalFix, SeasonHud, Smarter Farmers, Open Together, AllTheLeaks | ✅ 0.2.3 |
| Cucina, seconda ondata | My Nether's, Chef's, Rustic, Ocean's e Autochef's Delight, Create Confectionery | 🧪 0.3.0 su `dev` |
| Agricoltura ed esperienza | Farming for Blockheads, Cognition | 🧪 0.3.0 su `dev` |
| Decorazione | Macaw's ×4, Diagonal ×3, Chimes, Exposure, Every Compat | ⏳ 0.4.0 |
| Villaggi e tech | Guard Villagers, Goblin Traders, Copycats+ | ⏳ 0.4.0 |
| Nether | Jaden's Nether Expansion, Moog's Nether Structures, Nether Depths Upgrade | ⏳ 0.5.0 |
| Esplorazione e mob | Aures Farmers Structures, Better Archeology, Nature's Compass, Paragliders, Aquamirae, Creeper Overhaul | ⏳ 0.5.0 |

| Datapack e config | Cosa | Stato |
|---|---|---|
| Lune di sangue | 5% delle notti, mostri ×2; super luna ×4 | ✅ 0.1.1 |
| Artefatti nelle casse | 153 casse di strutture modded, Galeone compreso | ✅ 0.2.3 |
| Artefatti: correzioni | 15 nomi di casse di When Dungeons Arise e Dungeons and Taverns sbagliati; casse di Mowzie's Mobs e Born in Chaos | ⏳ 0.6.0 |
| Vasi: Ars Nouveau | Magebloom, Sourceberry, 5 frutti di archwood | ✅ 0.1.1 |
| Vasi: tutto il resto | ~250 piante, 13 terreni, alberi di Bountiful Fares, piante di Jaden's e Nether Depths, nomi vecchi di Regions Unexplored | ⏳ 0.6.0 |
| Pesce cotto di Starcatcher | Nelle etichette del pesce cotto | 🧪 0.3.0 su `dev` |
| Esperienza | Scambio Create ↔ Cognition nel Mescolatore, valore del liquido di Cognition | ⏳ 0.6.0 |
| Mercato di Farming for Blockheads | Voci per le mod che il mercato non conosce | ⏳ 0.6.0 |
| Berserker di Cataclysm | Tornano nelle fortezze di YUNG's | ⏳ 0.6.0 |
| Config AlmostUnified | 19 etichette di cibo intercambiabili | ✅ 0.1.1 |
| Config Sparse Structures | Densità generale ✅ 0.1.1; regolazione struttura per struttura | ⏳ 0.6.x (mondo di prova) |
| Altre config | Every Compat, Jaden's, Moog's, Artifacts (solo Curios) | ⏳ 0.6.0 |

Dopo ogni tappa: avvio dell'istanza di prova, mondo nuovo, controllo del log. NeoForge resta alla **21.1.259**: se una mod nuova ne chiede una più recente, va segnalato nella sua tappa.

### 3.1 Creazione dell'istanza in Prism

**Distribuzione**: dal 18/10/2026 il pack si installa dal repository `mango-craft` con packwiz (istruzioni nel `README.md` e in `docs/prism.md`). Storico: l'ultimo pacchetto .mrpack è stato `modpack-matteo-0.2.3.mrpack` (17/10/2026; 211 file, 701 MB, **NeoForge 21.1.259** — vedi sotto perché non la 21.1.262; contenuto e note in `storico/pacchetti-mrpack.md`). In Prism: Aggiungi istanza → Importa → scegliere il file. Poi aggiungere a mano le 6 mod solo CurseForge (Twilight Forest, Ars Elemental, Roaster's Delight, Spice of Life: Carrot Edition, BotanyPotsAdditions, AllTheLeaks). I passi qui sotto restano validi per aggiunte singole. Prism è installato in versione portable sul PC dell'utente: non toccare la sua cartella senza il suo via.

1. Aggiungi istanza → Minecraft **1.21.1** → loader **NeoForge** (ultima 21.1.x, almeno 21.1.229)
2. Impostazioni → Java → **8 GB** di memoria. Assegnarne troppa non aiuta e può allungare le pause del garbage collector
3. Modifica istanza → Mod → Scarica mod (Modrinth / CurseForge), filtrando per NeoForge 1.21.1
4. Installare **a blocchi**, con un avvio di prova dopo ogni blocco: base tecnica + comodità + atmosfera → cucina + Botany Pots → natura → tech e storage → equipaggiamento → strutture → dimensioni → boss e nemici
5. Attenzioni in fase di download:
   - **YUNG's**: usare i progetti marcati **"(NeoForge) [1.20.4 - 1.21.1 ONLY]"**
   - **Dungeons and Taverns**: solo la mod base, **senza** i pacchetti overhaul
   - **Forgified Fabric API**: installarla sempre, fin dal primo blocco (con la base tecnica)
6. Datapack (es. quelli generati da Botany Pots): copiarli nella cartella `datapacks` del mondo, poi `/reload`
7. Dopo aver aggiunto mod di strutture o dimensioni: **creare un mondo nuovo**
8. **Backup del mondo** prima di ogni aggiornamento delle mod

### 3.2 Test prioritari 🧪

- [ ] **Miapi + Accessories** (log del 17/10/2026: Accessories 1.1.0-beta.48 arriva **dentro l'Aether**, quindi il test serve ancora): mondo di prova con Truly Modular + Hexalia + Forgified Fabric API; prendere e infliggere danno. Issue Miapi #118 e Accessories #387 aperte al 12/10/2026. Se passa → si aggiungono Aether, Deep Aether e Aether's Delight e si ripete il test. Se non passa → l'Aether resta fuori e va scelto tra Truly Modular e Hexalia finché il bug non viene corretto
- [ ] **Curios + Accessories**: Cataclysm usa Curios, Miapi e Hexalia usano Accessories; verificare che convivano
- [ ] **BotanyPotsAdditions** e **Roaster's Delight**: provarle da sole prima di affidarci un mondo lungo (mod recenti, pochi download)
- [ ] **Botany Pots Tiers + BotanyPotsAdditions** insieme (blocchi diversi, dovrebbe funzionare)
- [ ] **Create: Central Kitchen + Create Slice & Dice** insieme: entrambe automatizzano Farmer's Delight, nei pack famosi non compaiono mai insieme
- [ ] **Create: Enchantment Industry + Apothic Enchanting**: incantamento automatico con il sistema di Apotheosis
- [ ] **Apotheosis + Truly Modular**: all'avvio Apotheosis va in errore leggendo il "tier" delle armi e degli attrezzi modulari di Miapi (NullPointerException in Miapi, 20 oggetti). Nessun crash; da provare se le armi Miapi ricevono affissi, gemme e riforgiatura e se i nomi generati sono corretti
- [ ] **NeoForge bloccata a 21.1.259**: dalla 21.1.261 NeoForge ha cambiato il codice di rete e owo-lib 0.12.15.5 (libreria di Accessories, incorporata nell'Aether) non "spacchetta" più i suoi pacchetti → "Connection lost" appena si entra nel mondo. Correzione già scritta in owo-lib 0.12.15.6-beta.1 (commit del 16/10/2026), non ancora pubblicata su Modrinth: quando esce, aggiornare owo-lib e si può tornare all'ultima NeoForge
- [ ] **Psi + Sodium**: issue Psi #853 (particelle di altre mod corrotte, peggio con Sodium) → provare con Particle Rain e Subtle Effects attive
- [ ] **Zaini nello slot schiena + morte**: morire con Traveler's (e Sophisticated) addosso e verificare che Corail Tombstone li conservi

### 3.3 Controlli durante la creazione

- [ ] **Addon FD**: ogni addon deve dichiarare compatibilità con FD 1.3.x; aggiungerli a piccoli gruppi
- [ ] **Polymorph**: `/polymorph conflicts` per elencare i conflitti di ricette
- [ ] **Botany Pots**: `/botanypots debug ...` per trovare semi non supportati (addon FD, alberi di Twilight Forest e Aether); l'opzione `gen_files` genera i datapack mancanti
- [ ] **Truly Modular**: controllare quali materiali delle altre mod mancano (Mekanism, Twilight Forest, Aether…) e coprirli con il Material Helper
- [ ] **OmniTools**: verificare in gioco cosa copre oltre a Create e Mekanism (es. Pipez)
- [ ] **Chunk Loaders**: confermare che sia la mod "a tier" usata in passato
- [ ] **Serene Seasons**: valutare l'impatto delle stagioni sul farming di FD
- [ ] **RightClickHarvest**: provarlo con le colture di FD e degli addon (es. rampicanti, colture a più blocchi)
- [ ] **Carry On**: provarlo su casse, cassetti di Storage Drawers e macchine Mekanism
- [ ] **Inventory Essentials**: provare l'ordinamento nelle GUI modded (toolbox di Create, macchine Mekanism, pentola di FD); se una dà problemi, aggiungerla alla lista ignorati
- [ ] **Animal Feeding Trough** e **Starcatcher's Delight**: verificare in Prism che esista la build NeoForge 1.21.1
- [ ] **Ars Nouveau**: il Worn Notebook si aggancia all'Akashic Tome? **Botany Pots**: alberi di archwood (4 di Ars + il giallo di Ars Elemental) già supportati da Botany Trees (tronchi, foglie, alberello 5%); nel datapack `matteo_tweaks` aggiunte Magebloom e Sourceberry e i **frutti** come il cacao: tronco di archwood come terreno + frutto come coltura (blu → Frostaya, rosso → Bombegranate, viola → Bastion, verde → Mendosteen, giallo → Flashpine), 3 frutti a raccolto. In Ars gli alberi da alberello non fanno frutti, solo quelli naturali: per questo i frutti stanno sul tronco e non sull'alberello. Ars Elemental ha già un file per i vasi, ma nel formato vecchio e con l'id `botany_pots` sbagliato: non si carica. Da provare in gioco
- [ ] **Addon di Ars**: Ars Creo chiede Create 6.0.9+; Ars Unification va provato con AlmostUnified attivo (glifi Frantuma/Taglia sulle ricette di Mekanism e FD); Ars QOL aggiunge uno slot Curios per il libro, controllare che non sposti gli altri
- [ ] **Artifacts nelle strutture modded**: ✅ 15 modificatori nel datapack `matteo_tweaks` coprono **153 tabelle** di casse (solo i tesori finali nelle strutture grandi). Verificate nei sorgenti 1.21.1: YUNG's, Twilight Forest, Aether, Deep Aether, Deeper and Darker, Undergarden, Cataclysm, Illager Invasion, Friends & Foes, Moog's End Structures, **Unusual End** (repository GitHub, versione 2.3.1). **When Dungeons Arise** e **Dungeons and Taverns**: nomi presi da versioni precedenti su GitHub (WDA 1.18.2 dell'autore + copia del 2025; DnT copia di marzo 2024), controllati sui file delle strutture; le strutture più nuove potrebbero mancare, un nome inesistente non dà errori. NeoForge applica i modificatori solo alla tabella "radice" della cassa: per questo servono. **Da completare**: Mowzie's Mobs e Born in Chaos (nessun sorgente trovato) → `.jar` (`data/<mod>/loot_table/chests/`), `/data get block <x y z> LootTable` o EMI Loot. Prova: `/loot spawn ~ ~ ~ loot <id>`; con `artifactRarity = 0` l'artefatto esce sempre. Escluse le casse di scorte, quelle decorative e le tabelle degli overhaul di DnT (non installati). Il workspace cloud raggiunge solo GitHub, non Modrinth/CurseForge: i `.jar` non si possono scaricare da qui
- [ ] **Doppioni di cibo**: cercare in EMI pomodoro, cipolla, farina, impasto, sale (FD, Farm & Charm, Create); di solito le ricette accettano i tag comuni
- [ ] **Zinco**: Mekanism non ha la lavorazione 3×/5× per lo zinco di Create; JAOPCA (MIT) può generarla, solo se serve
- [ ] **Strutture**: `/dumpstructuresets` per controllare la distanza tra le strutture; Structure Layout Optimizer da verificare in gioco
- [ ] **Scriptor Magicae**: incisione di incantesimi sugli oggetti all'incudine insieme ad Apothic Enchanting (stesso punto del codice dell'incudine)
- [x] **Polveri di Occultism** ✅ verificato nel codice (16/10/2026): AlmostUnified 1.4.2 ha un adattatore dedicato a Occultism che trasforma i risultati "a tag" del frantumatore (e dei minatori) nell'oggetto scelto. Le 7 polveri in comune sono tutte nei materiali di default di AU: ferro, oro, rame, smeraldo, lapislazzuli, netherite → escono quelle di **Mekanism**; ossidiana → quella di **Create**. Le altre polveri del frantumatore (carbone, diamante, osmio, stagno…) esistono solo in Mekanism, nessun doppione. In gioco basta un'occhiata in EMI (si vedono solo le polveri di Mekanism). Nota: l'integrazione con AU interna a Occultism è disattivata nella 1.21.1, ma non serve perché lavora AU sulle ricette
- [ ] **Licenze ancora ❓**: addon FD, Let's Do, Botany Pots e addon, Easy Villagers, Tombstone, OmniTools, Dungeons and Taverns, Explorer's Compass, Twilight Forest, Aether, Undergarden, Unusual End, Mowzie's Mobs, Friends & Foes, Ender Dragon Fight Remastered

### 3.4 Config da impostare

**File pronti (16/10/2026)** — pacchetto `modpack-config.zip` + documento di progetto `file-di-configurazione.md` (contenuto completo dei file). Il datapack ha un `README.md` in ogni cartella con la spiegazione dei file (i `.json` non accettano commenti; il gioco ignora i `.md`). Vanno copiati nella cartella `minecraft/config` dell'istanza:

| File | Contenuto | Stato |
|---|---|---|
| `config/almostunified/tags.json` | 19 tag personalizzati: farina, impasto di grano, sale, mais, limone, porzioni di formaggio, formaggio di capra intercambiabili tra le mod (ogni oggetto aggiunto a tutti i tag che le ricette usano, perché AlmostUnified lavora sui tag già risolti) | ✅ pronto |
| `config/sparsestructures.json5` | Fattore generale 1.4; villaggi 1; magione 2 | ⚠️ da completare con i nomi dei gruppi di Dungeons and Taverns (Witch Villa e Swamp Village → fattore **3**, scelta dell'utente: tenerle ma molto più rare) e When Dungeons Arise (→ 2), letti in gioco con `/dumpstructuresets` |
| `config/paxi/datapacks/matteo_tweaks/` | Datapack: luna di sangue **5%** delle notti e mostri **×2**; super luna di sangue **×4** (frequenza invariata: 5% delle lune piene, almeno 20 notti di distanza; copie complete dei file di Enhanced Celestials 6.x). **Artefatti** nelle casse delle strutture modded: 15 modificatori `artifacts:roll_loot_table` (153 tabelle, compresa la cassaforte del Galeone di Supplementaries), uno per livello di bottino vanilla, attivi solo se Artifacts è caricata. **Ars in Botany Pots**: Magebloom, Sourceberry, 5 frutti di archwood sui tronchi | ✅ pronto · ⚠️ artefatti da completare per Mowzie's e Born in Chaos (3.3) |

Limiti noti: le 5 ricette di Brewin' And Chewin' che chiedono il suo mais specifico non si sistemano con i tag; latte lasciato com'è (forme diverse); impasti speciali (mais, patata dolce) separati di proposito. Le strutture cambiano solo nei chunk nuovi.

- **Sparse Structures**: vedi tabella sopra (scelto 1.4 dentro la forbice 1.3–1.5)
- **Difficoltà** (si sommano World Tier ed Elites di Apotheosis, mod di boss e buff permanenti di Cataclysm Delight):
  - World Tier di Apotheosis (si sceglie in gioco) + datapack per i Tier Augments
  - Config di Cataclysm
  - Born in Chaos: Born In Configuration, oppure la gamerule `naughtinessMechanics` per disattivare il Krampus
  - Se servisse: In Control! ed Enhanced AI (vedi opzionali)
- **Carry On**: `pickupAllBlocks = true` per prendere in mano anche i blocchi normali (di default solo quelli con inventario o macchinari). La lista nera di default esclude già tutto Create, Ender Storage, Enchantment Industry e alcuni generatori di Mekanism (wind, heat)
- **FallingTree**: abbatte l'albero intero, stesso principio del vein mining → valutare l'opzione che lo attiva solo da accovacciati
- **Zaini**: Sophisticated e Traveler's aprono entrambi con **B** → cambiare il tasto di uno (es. Sophisticated su N). Traveler's: `allowShulkerBoxes = true` se si vogliono shulker box o zaini Sophisticated al suo interno
- **Inventory Essentials**: `enableShiftDrag = false` (doppione di Mouse Tweaks)
- **Artifacts** (`config/artifacts/general.toml`, sezione `[slots]`): `enableAccessoriesCompat = false`, lasciare `enableCuriosCompat = true`, **prima di creare il mondo**. Così Artifacts e Ars Nouveau condividono un'unica interfaccia Curios, non si possono indossare due copie dello stesso artefatto (con entrambe attive gli slot sono doppi e alcuni bonus si sommerebbero) e Artifacts non passa mai dal bug di Accessories. Non aggiungere l'Accessories Compatibility Layer. `artifactRarity` (default 1.0) regola la frequenza degli artefatti nel bottino: utile con tante mod di strutture
- **Slot Curios contesi**: Ars Nouveau e Artifacts usano entrambe testa, collana e cintura (1 slot ciascuno). Se diventano stretti, si possono aumentare con un file di slot Curios nel datapack del pack (da verificare il formato)
- **Strutture di palude** (deciso 16/10/2026): restano le capanne di Hexalia, Hexerei e YUNG's; Witch Villa e Swamp Village di Dungeons and Taverns restano ma molto più rare (fattore 3 in Sparse Structures)
- **Lune di sangue** (deciso 16/10/2026): 5% delle notti, mostri ×2; super luna ×4 (datapack `matteo_tweaks`). Altre leve di difficoltà se servisse: pesi di Mutant Monsters, Born In Configuration, `invader_spawn_rules` di Apotheosis
- **Subtle Effects**: se le increspature della pioggia compaiono doppie con Particle Rain, disattivare `rainWaterRipples`
- **Caricamento automatico in tutti i mondi** ✅: **Paxi** (vedi 4.14). I datapack vanno in `config/paxi/datapacks/`; l'ordine si fissa in `config/paxi/datapack_load_order.json` (facoltativo). Verificato nel codice: Paxi li registra come pacchetti obbligatori, quindi valgono anche alla creazione del mondo
- **Strutture di palude, dati verificati**: Hexalia `hexalia:herbalist_hut` (paludi, spacing 32); Hexerei `hexerei:witch_hut` (paludi, 20) e `hexerei:dark_coven` (paludi, 29), più `nature_coven`, `baba_yaga_hut` e `owl_post_office` nelle foreste; Dungeons and Taverns sotto `nova_structures` (sorgente non pubblico: nomi da leggere in gioco)
- **Sparse Structures** accetta in `customSpreadFactors` sia il nome di un gruppo (`structure_set`) sia quello di una struttura (in quel caso cambia tutto il gruppo); i fattori sono rispetto ai valori originali, non si moltiplicano con quello generale (verificato nel codice)
- **AlmostUnified**: la config di default unifica i metalli; i cibi sono gestiti dai tag personalizzati in `tags.json`. Al primo avvio controllare nel log le righe `[CustomTags]` (oggetti inesistenti vengono saltati senza errori)
- **Sound Physics Remastered**: costa un po' di CPU; se pesa, abbassarne la qualità
- **Tasto C**: Psi (tasto principale) e Ars Nouveau (apri libro) usano entrambi **C** → cambiarne uno (Controlling aiuta a trovare i conflitti)
- **Frantumatore di Occultism**: lasciato con i moltiplicatori di default (fino a 6 polveri per minerale con il Marid), **decisione dell'utente**: non modificarlo
- **Magazzino dimensionale di Occultism**: convive con Tom's Simple Storage (accettato: si sblocca con i rituali)
- **Akashic Tome**: lista dei nomi di libri ammessi, se qualche libro non viene riconosciuto

### 3.5 Rischi e note di compatibilità

- **Accessories su NeoForge 1.21.1**: bug nel codice di Accessories (chiamata a Fabric Loader quando una mod chiede uno slot fuori range); Miapi lo fa scattare quando un'entità subisce danno, ma può farlo qualunque mod. Riguarda già Hexalia. Fix: Forgified Fabric API, che fornisce la classe mancante (nell'issue di Miapi un utente l'ha risolto con Sinytra Connector, stesso principio ma più pesante)
- **Curios + Accessories** nello stesso pack: due librerie accessori diverse
- **FD 1.3.x**: ha cambiato tag e meccaniche, gli addon vecchi possono rompersi
- **Mod molto recenti** (Roaster's Delight, BotanyPotsAdditions): possibili bug
- **Hexerei**: versione 1.21.1 ferma al 2025, sviluppo rallentato
- **When Dungeons Arise**: ramo 1.21.1 fermo da ottobre 2025 (stabile, ma niente fix nuovi)
- **The Undergarden**: versione beta
- **Tante strutture insieme**: rischio di mondo affollato → una sola mod di spacing, massimo due mod di villaggi
- **Difficoltà cumulativa**: vedi 3.4; niente Improved Mobs
- **Occult Delight**: una sola release finora
- **Psi**: issue aperte su particelle (#853) e su un trucco dell'Exosuit (#869)

### 3.6 Verifica versioni NeoForge 1.21.1 (16/10/2026)

Controllo formale mod per mod (API di Modrinth, CurseForge per le mod che stanno solo lì). Tabella completa con slug, versione, data ed esito nel documento di progetto **`verifica-versioni.md`**.

- **Risultato**: 148 voci (142 mod + Fresh Animations + 5 dipendenze/moduli) → ✅ 119 · ⚠️ 29 · ❌ 0. Tutte hanno una build NeoForge 1.21.1, tutte dagli autori originali (o addon di terzi dichiarati)
- **Correzioni**: Sodium Dynamic Lights (port non ufficiale) → **LambDynamicLights**; Enhanced Celestials → mod **originale** 6.0.2.6 (la "2" è solo una libreria + addon)
- **Versioni da fissare in Prism** (le più nuove sono beta): Create Crafts & Additions 1.6.0 · Create: Enchantment Industry 2.4.2 · Simple Backups 4.0.21 · JEI 19.51.0.418 · Polymorph 1.1.0. **Create 6.0.10** per tutti gli addon
- **Solo beta/alpha ma ufficiali** (si usano lo stesso): Serene Seasons, Pipez, Sound Physics Remastered, The Undergarden, Expanded Delight, Aether's Delight, Fresh Animations
- **Ramo 1.21.1 concluso** (build stabili ferme tra il 2024 e metà 2025): serie YUNG's, Dungeons and Taverns, Sparse Structures, Hexerei, Ender Storage, Illager Invasion, Mouse Tweaks, Controlling, Pick Up Notifier, Travelers Titles, Animal Feeding Trough
- **Solo su CurseForge**: The Twilight Forest, Roaster's Delight, Spice of Life: Carrot Edition, BotanyPotsAdditions
- **Slug da non sbagliare**: Friends & Foes → `friends-and-foes-forge` · Create Slice & Dice → `slice-and-dice` · Deeper and Darker → `deeperdarker` · Unusual End → `unusual_end` · Moog's End Structures → `mes-moogs-end-structures` · Born in Chaos → `borninchaos`. Evitare i progetti omonimi non ufficiali (ImmediatelyFast "Reforged", Entity Culling di altri autori, Compass to Map per JourneyMap)
- **NeoForge**: almeno 21.1.229 (richiesto da BotanyPotsAdditions); usare l'ultima 21.1.x

### 3.7 Revisione sovrapposizioni (16/10/2026) — proposte da decidere

Verifica sui codici sorgente (file di lingua, tag, recipe) e sulle pagine delle mod.

**Decisi dall'utente**: **Animal Feeding Trough** e **Comforts** restano (proposti da togliere come doppioni di Animal Pens e del sacco a pelo di Traveler's Backpack, ma l'utente li vuole).

**Let's Do EMI Compat — verificato nel codice (16/10/2026) → ⛔ tolta (decisione dell'utente)**
- **Perché esiste**: le mod Let's Do avevano solo plugin per JEI e REI, quindi chi usava EMI *senza* JEI non vedeva le loro ricette. La mod le ricrea in EMI, compresi alcuni casi speciali (fonduta di Meadow, pigiatura dell'uva di Vinery)
- **Nel nostro pack**: JEI è installato sotto EMI, quindi le ricette di **HerbalBrews** (bollitore, calderone) e **Meadow** (calderone, pressa del formaggio, segheria) arrivano in EMI dai loro plugin JEI. **Vinery** (dalla 1.5.5, 7/10/2026) e **Farm & Charm** (da ottobre 2026) hanno ora un plugin EMI nativo
- **Problema**: la mod non controlla se il plugin nativo c'è → categorie doppie (torchio di Vinery due volte; la fermentazione di Vinery usa perfino lo stesso identificativo `vinery:wine_fermentation`, possibile conflitto)
- **Unico apporto rimasto**: le schermate della fonduta di Meadow e della pigiatura dell'uva
- **Proposta**: non installarla; aggiungerla solo se in gioco mancano ricette Let's Do che servono

**Da valutare (doppioni reali, scelta di gusto)**
- **[Let's Do] Farm & Charm → tenuta come "secondo orto e seconda cucina"** (l'utente preferisce FD ma vuole varietà). Integrazione verificata nel codice:
  - **Let's Do Addon Compat** (già nel pack) converte le ricette tra le due pentole in entrambe le direzioni, quindi ogni pentola cucina tutto, addon FD compresi; le ricette della ciotola di F&C diventano ricette del Mixer di Create
  - **Nativa in Farm & Charm**: la sua pentola funziona sul fornello di FD; la terra ricca di FD conta come terreno coltivato per F&C; la corda di FD vale come corda di F&C
  - **Colture intercambiabili via tag**: pomodoro, cipolla, lattuga/cavolo e mais di F&C funzionano nelle ricette di FD; quelli di FD funzionano nella maggior parte delle ricette di F&C (poche ricette di F&C chiedono il loro oggetto specifico: 5 col pomodoro, 4 con la lattuga, 2 con cipolla, 2 col mais)
  - **Restano separati**: impasto e farina (F&C usa i tag vecchi `c:dough` e `c:flour`, FD `c:foods/dough`, Create `c:flours`) → sistemabili con un piccolo datapack di tag (vedi 3.4)
  - Analisi precedente, per riferimento: la più ridondante tra le mod di cibo. Duplica pentola, tagliere e fornello di FD (con HerbalBrews i fornelli diventano tre), pomodoro, cipolla, mais, farina e impasto; il suo impasto ha un tag vecchio, quindi le ricette di pasta di FD non lo accettano. Unici: orzo, avena, fragole, lattuga, decorazioni da fattoria. Non è richiesta da Vinery, Meadow né HerbalBrews
- **Magia e calderoni**: vedi l'analisi approfondita qui sotto. **Deciso: Toil and Trouble ⛔ tolta, Hexerei resta** (opzione B)
- **Create Slice & Dice vs Create: Central Kitchen**: si sovrappongono su tagliere e pentola automatizzati; restano unici lo Slicer e lo Sprinkler di S&D. Nessun conflitto dichiarato; controllare in EMI le ricette doppie
- **Alcolici e formaggi**: Brewin' And Chewin' duplica uva e vino di Vinery e l'idromele di Bountiful Fares, Cultural Delights e Vinery; i formaggi sono quattro sistemi (Meadow, Expanded Delight, Brewin', Cultural Delights) con tag diversi. Brewin' è comunque richiesta da Cultural Delights per le conserve

**Da tenere (sovrapposizione solo apparente)**
- HerbalBrews, Roaster's Delight e Delightful Fares: nicchie diverse (si sovrappongono solo caffè e bollitore); Delightful Fares usa le erbe di Bountiful Fares
- Botany Pots Tiers e BotanyPotsAdditions: migliorano assi diversi (velocità contro slot, serra, irrigatore)
- Chunk Loaders e Mekanism: i primi servono a inizio partita, lo stabilizzatore di Mekanism arriva a fine gioco
- Tom's Simple Storage, Stock Keeper di Create 6 e QIO di Mekanism: momenti diversi della progressione
- Gateways to Eternity: integrato ufficialmente in Apotheosis (portali a ondate per livello)
- Subtle Effects, Particle Rain, Snow! Real Magic!: unico doppione le increspature della pioggia (vedi 3.4)
- I due zaini ed EMI + JEI: scelte volute

**Magia e calderoni — analisi approfondita (16/10/2026, sui sorgenti 1.21.1)**

Nel pack ci sono sei "calderoni" diversi. Cosa fa davvero ciascuno:

| Mod | Il suo calderone | Ruolo nel pack |
|---|---|---|
| **Hexalia** | Small Cauldron: acqua, calore, fino a 4 ingredienti, si mescola col mestolo; una miscela sbagliata si guasta e fa danno. 9 pozioni **proprie** (es. Bloodlust, Siphon, Homestead = ritorno allo spawn) | **Progressione magica principale**: mortaio → paste di erbe → pozioni, incensiere con aure (10 coppie), rituali (29) su bracieri salati alimentati dalle colture vicine, Mutavis (21 mutazioni di blocchi), equipaggiamento finale. Guida: Verdant Grimoire |
| **Hexerei** | Mixing Cauldron: 2 secchi di fluido + 8 oggetti, banco da lavoro (36 ricette); scaldato prepara anche le **pozioni dell'alambicco** | **Vita da strega e viaggio**: scope volanti, corvi, gufi postini, candele con effetti, piatto di salvia anti-spawn, borse, decorazioni |
| **Toil and Trouble** | Il calderone **vanilla** diventa un alambicco senza combustibile; latte, miele, slime | Comodità per le pozioni vanilla; nessun contenuto nuovo |
| **Aspect Alchemy** | Aspect Cauldron con aspetti nascosti da scoprire | **Laboratorio sperimentale**; solo oggetti vanilla |
| **HerbalBrews** | "Brewing Cauldron" che **unisce** 3 pozioni + Herbal Infusion in una Fiaschetta con tutti gli effetti | **Casa del tè** (9 bevande con effetto ad area) e **punto d'arrivo** della catena delle pozioni (dovrebbe accettare anche le pozioni delle altre mod: da provare) |
| **Meadow** | Pentola da cucina (carni, caglio, sale, latti) | Cucina, **nessuna magia** |

**Distanza tra le mod** (0 = identiche, 5 = nulla in comune): la coppia più vicina è **Hexerei–Toil and Trouble (2)**, perché entrambe fanno le pozioni dell'alambicco in un calderone. Poi Hexalia–Hexerei (3: stessi oggetti da casetta della strega, ma rituali e aure contro scope e famigli) e Toil and Trouble–Aspect Alchemy (3: stesso tipo di risultato, ricette fisse contro rompicapo). Tutte le altre coppie sono a 4–5.

**Doppioni di ingredienti nel gruppo**: mandragora (Hexalia e Hexerei, tag diversi), due legni di salice separati, barattolo per erbe e mortaio in entrambe, lavanda (Hexalia e HerbalBrews), sale (quello di Meadow vale nei bracieri di Hexalia, non il contrario: sistemabile coi tag), tre cappelli da strega.

**Conflitti**: solo Toil and Trouble modifica il calderone vanilla; tutti gli altri sono blocchi propri. Nessun conflitto trovato nel codice tra le sei.

**Come Toil and Trouble tocca il calderone vanilla** (verificato nel codice, ramo 1.21.1):
- Non lo sostituisce sempre: interviene **solo quando il gioco vanilla non ha un uso** per l'oggetto che hai in mano (secchi, bottiglie, lavaggio di cuoio tinto, stendardi e shulker restano identici)
- Click destro su un calderone vanilla vuoto, d'acqua o di lava con un oggetto "inutile" per il vanilla (es. verruca del Nether, un'erba, un cibo) → il blocco diventa il **suo calderone da infusione** (identico alla vista, mantiene il livello d'acqua) e l'oggetto entra
- Anche un oggetto **lasciato cadere** in un calderone vanilla vuoto lo converte (opzione `itemEntitiesConvertCauldrons`, attiva di default)
- Quando si svuota **torna un calderone vanilla**; se lo rompi droppa un calderone normale
- I calderoni delle altre mod (Meadow, Hexerei, Aspect Alchemy, HerbalBrews) non vengono toccati
- Effetti collaterali possibili: conversione involontaria cliccando un calderone decorativo con un oggetto qualsiasi; oggetti che cadono in un calderone vuoto vengono "assorbiti"; il calderone convertito non espone fluidi, quindi probabilmente i tubi di Create non lo riempiono né lo svuotano (da provare)
- Config utili: `itemEntitiesConvertCauldrons` (consigliato `false` se resta), `requiresHeat` (default `false`, cioè niente fuoco sotto), `brewingTime`, `useBrewingStandRecipes`

**Opzioni**
- **A — tenere tutto**, ognuna col suo ruolo (tabella sopra). Costo: tre modi di fare le pozioni vanilla (alambicco, Toil and Trouble, Hexerei) e alcuni doppioni in EMI
- **B — set snello consigliato**: Hexalia + Hexerei + Aspect Alchemy + HerbalBrews (+ Meadow per la cucina). Togliendo **Toil and Trouble** si perdono solo le pozioni senza combustibile nel calderone vanilla e i calderoni di latte, miele e slime; sparisce anche la libreria MRU
- **Togliere Hexerei** invece costerebbe cose che nient'altro nel pack offre (scope, corvi, gufi, candele, anti-spawn, borse): sconsigliato nonostante sia ferma ad aprile 2025

**Doppioni di ingredienti da sapere** (non si risolvono togliendo mod): mais da 4 mod (Cultural Delights, Farm & Charm, Brewin', Bountiful Fares), patata dolce (Veggies + Expanded, tag comune), latte frammentato su più tag. Eventualmente unificabili con una config personalizzata di AlmostUnified.

### 3.8 Quanto integrare: tag, datapack o script? (valutazione del 16/10/2026)

| Livello | Cosa fa | Pro | Contro | Quando |
|---|---|---|---|---|
| **1. Tag con AlmostUnified** (`custom_tags`) | Rende intercambiabili gli ingredienti doppi in tutte le ricette che usano i tag; AlmostUnified può anche nascondere i doppioni in EMI | Globale per tutti i mondi, nessun file di mondo da toccare, regge bene gli aggiornamenti delle mod | Non crea ricette nuove; non aiuta le ricette che chiedono un oggetto preciso | **Subito** |
| **2. Ricette via datapack** (con Paxi) | Ricette nuove tra mod (es. erbe di Hexerei o Hexalia nel bollitore di HerbalBrews; conversione tra il tagliere di F&C e quello di FD, che Let's Do Addon Compat non fa) | Integrazione vera, mirata | Un file JSON per ricetta; i formati cambiano con gli aggiornamenti e le ricette possono rompersi senza avvisi | **Solo mirato**, dopo aver giocato, dove manca davvero qualcosa |
| **3. Script con KubeJS** | Togliere, sostituire e ribilanciare ricette e bottini in massa | Potentissimo | È un progetto a sé (una mod in più + codice JavaScript da mantenere) | **Non ora**; da tenere di riserva |

Integrazione a livello di ricette già presente senza fare nulla: Let's Do Addon Compat (pentole FD ↔ F&C, ciotola → Mixer di Create), Create: Central Kitchen e Slice & Dice (automazione di FD), Seasonal Let's Do, ricette di FD basate sui tag. Limite: Aspect Alchemy non è integrabile, perché i suoi ingredienti sono fissati nel codice.

**Proposta**: completare il livello 1 (oltre a farina e impasto: sale, mais, limoni; formaggi e latte con cautela, perché sono forme diverse), tenere il datapack per strutture e lune, e aggiungere ricette via datapack solo quando in gioco manca qualcosa.

---

## 4. Mod approvate ✅ (per tema)

### 4.1 Cucina e bevande

**Farmer's Delight** 1.3.x (MIT) — la base. La 1.3 ha cambiato tag e meccaniche: gli addon vecchi possono rompersi.

**Addon FD** (verificati per NeoForge 1.21.1)

- **Brewin' And Chewin'** (MIT) — fermentazione nel keg: alcolici, formaggi, fudge
- **Ender's Delight** — cucina con risorse dell'End
- **Veggies Delight** — nuove verdure (la 1.9.3 supporta FD 1.3.1+)
- **Expanded Delight** — nuove colture, formaggio, dolci
- **Cultural Delights** — cucine dal mondo; il pickling richiede Brewin' And Chewin'
- **Farmer's Delight: Extended** — solo ricette, nessuna nuova coltura
- **Create Slice & Dice** — automazione FD con Create

**Addon FD legati ad altre mod del pack**

- **Twilight's Flavor & Delight** — cibi e ingredienti di Twilight Forest
- **Undergarden Delight** 2.0.2 — cibi e ingredienti dell'Undergarden
- **Cataclysm Delight** (MIT) — cibi dai materiali dei boss di Cataclysm con **buff permanenti**, che si sommano a quelli di Apotheosis
- **Starcatcher's Delight** — si cucinano in FD i pesci di Starcatcher
- **Aether's Delight** ⚠️ — integrazione con The Aether, solo se entra l'Aether

**Automazione e varietà**

- **Create: Central Kitchen** 2.6.2b (LGPL-3.0) — automazione della cucina FD con packager e bracci meccanici; supporta Brewin' And Chewin' e Cultural Delights. ⚠️ Da provare insieme a Slice & Dice
- **Spice of Life: Carrot Edition** 1.16.6 (ARR) — cuori extra per ogni cibo diverso mangiato: dà uno scopo ai tanti addon FD

**Tè e bevande con effetti**

| Mod | Licenza | Note |
|---|---|---|
| **[Let's Do] HerbalBrews** 1.1.4 | codice MIT, asset ARR | Mod ufficiale e diffusa. Sorgente su GitHub (Let-s-Do-Collection/HerbalBrews), issue nel repo, Discord, wiki; accetta contributi (es. traduzioni). Tè (lavanda, nero, verde…), caffè e fiale; bollitori di rame/ferro da mettere su una fornace. Molti tè danno effetti positivi ai giocatori in un raggio; le fiale danno effetti lunghi. Serie "Let's Do", non un addon FD |
| **Roaster's Delight** 1.0.0.1 | ARR | Addon FD ispirato a Farmer's Respite: caffè (tostatura, macinatura), tè, bollitore e moka, effetto Caffeinated con "crollo" finale, dolci da caffetteria; colture stagionali compatibili con Serene Seasons. Richiede GeckoLib. ⚠️ Uscita a inizio ottobre 2026, poco più di 100 download → provarla da sola |
| **Delightful Fares** 1.1.x | ARR | Bollitore + bustine di tè; ponte fra FD e **Bountiful Fares**. Nuovi tipi di tè ancora in sviluppo |

### 4.2 Botany Pots

| Mod | Note |
|---|---|
| **Botany Pots** 21.1.44 (Darkhax) | Dipendenze: Bookshelf + Prickle. Vasi base, cerati e hopper (auto-raccolta). La 21.1.42 sistema la Rich Soil di FD. Dichiara oltre 1.300 colture/terreni supportati, ma la lista per la 1.21.1 non è pubblica |
| **Botany Trees** 21.1.7 (Darkhax) | Alberi nei vasi = mini farm di legno. Supporto dichiarato: vanilla, Quark, Biomes O' Plenty, Forbidden Arcanus, Simple Farming, BYG, Better Default Biomes, Silent Gear. Nel sorgente 1.21.1 (giugno 2026) ci sono anche Twilight Forest, Aether, Deep Aether, Undergarden, Deeper and Darker, Hexerei, Meadow, Vinery, Bountiful Fares, Ars Nouveau e Ars Elemental. Per altri alberi mancanti: comandi debug di Botany Pots |
| **Botany Pots Tiers** 7.0.11 | Vasi Elite (×2 velocità e raccolto), Ultra (×6), Creative (×10). Maturo e molto usato |
| **BotanyPotsAdditions** 1.1.0 (solo CurseForge) | Richiede NeoForge ≥ 21.1.229 e Botany Pots ≥ 21.1.42. Vasi serra (+50% raccolto), sprinkler a FE + acqua, vasi doppi/quadrupli, varianti hopper. Sinergia con l'energia di Mekanism. Stabile da luglio 2026 ma pochissimi download → 🧪 testarla subito |

### 4.3 Natura, erbe e pozioni

Su questo tema ci sono anche HerbalBrews, Roaster's Delight e Brewin' And Chewin' (vedi 4.1).

| Mod | Licenza | Note |
|---|---|---|
| **Hexalia** 1.3.x | MIT | Stregoneria popolare e magia della natura: erbe, mortaio e pestello, miscele, incensiere (censer), piante incantate, rituali con offerte, sale e forze elementali. Sviluppo molto attivo, pensata per addon e datapack (addon: Hexforged). Consiglia EMI. ⚠️ Usa **Accessories** → crash noto con Miapi (vedi 3.2) |
| **Hexerei** 0.5.0.3 | LGPL-3.0 | Vita da strega: erbe da essiccare (salvia, mandragora, belladonna, artemisia, romice), **Mixing Cauldron** che fa da banco da lavoro con fluidi (36 ricette: scope, borse, sfera di cristallo…) e, se scaldato, prepara anche le pozioni dell'alambicco; candele infuse con 14 effetti ad area; **scope volanti**, **corvi** che raccolgono e mietono, posta coi gufi, piatto di salvia che blocca gli spawn nel raggio di 48 blocchi, capanne e covi. Guida: Book of Shadows. ⚠️ Beta ferma ad aprile 2025 |
| **Aspect Alchemy** 2.0.0 | MIT | Laboratorio sperimentale: Aspect Cauldron da scaldare, fino a 3 ingredienti con "aspetti" nascosti, svelati con gli avanzamenti; un effetto entra se la somma della sua potenza arriva a 2 (basta anche un solo ingrediente forte), fino al livello V, durata sempre 3 minuti. Bottiglie da 2–4 sorsi, frecce intinte, "bagno" nel calderone. ⚠️ Usa solo **49 oggetti vanilla fissati nel codice**: le erbe delle altre mod non funzionano e non è modificabile via datapack. Guida: Alchemists Guide |
| **Bountiful Fares** | Heccology License (custom) | Alberi da frutto, erbe, effetti dei cibi, fermentazione (idromele, sidro). Dipendenza: NexusLib. Indipendente da FD; con Delightful Fares si collega a FD |
| **[Let's Do] Vinery** 1.5.x | ❓ | Vigneti, presse, botti, vini che danno effetti tipo pozione |
| **[Let's Do] Meadow** 1.4.x | ❓ | Pascoli di montagna, fiori, formaggi |
| **[Let's Do] Farm & Charm** 1.1.x | ❓ | Base agricola della serie Let's Do |
| **Serene Seasons** | ARR | Stagioni: colori del fogliame, temperature, neve, crescita delle colture |
| **Seasonal Let's Do** | Apache-2.0 | Stagioni di Serene Seasons sulle colture Let's Do (HerbalBrews compreso) |
| **Let's Do Addon Compat** 2.3.1 | MIT | **Il ponte Let's Do ↔ Farmer's Delight** (verificato nel codice): converte ogni ricetta della pentola di Farm & Charm in ricetta della pentola di FD e viceversa (comprese quelle di tutti gli addon FD); trasforma le ricette della ciotola di Farm & Charm (impasto, burro…) in ricette del Mixer di Create; fa contare la lattuga come cavolo nelle insalate di FD e cipolla e lattuga come condimenti per le pizze di Brewin' And Chewin'. Ultimo aggiornamento ottobre 2025, ma il formato delle ricette che converte è ancora quello attuale |
| **Snow! Real Magic!** 12.2.3 | MIT | Neve su piante, lastre e scale: valorizza gli inverni di Serene Seasons |

### 4.4 Tech

| Ruolo | Mod | Note |
|---|---|---|
| Meccanico / early game | **Create** 6.0.10 | Versione su cui sono compilati tutti gli addon Create del pack. Visivo, si integra con FD tramite Slice & Dice; la logistica "packaging" di Create 6 copre il trasporto oggetti |
| Ponte rotazione ↔ FE | **Create Crafts & Additions** 1.6.0 (ultima release; la 1.7.x è beta) | Collega Create all'energia elettrica |
| Elettrico / mid–late | **Mekanism + Mekanism Generators** 10.7.19 (stessa versione per entrambi) | Processing minerali, generatori dal solare alla fusione |
| Tubi | **Pipez** | Semplici, poco lag, anche tubo universale (item/fluidi/energia/gas Mekanism) |
| Incantamento automatico | **Create: Enchantment Industry** 2.4.2 (LGPL-3.0; ultima release, la 2.5.x è beta) | XP liquida e incantamento automatico; richiede Create: Dragons Plus. Da provare con Apothic Enchanting |
| Agricoltura con Create | **Create: Integrated Farming** 1.4.3 (LGPL-3.0) | Raccoglitore a vuoto e reti da pesca; gestisce le colture FD |
| Guida Mekanism | **Mekanism: Ponders** 1.0.4 (LGPL-3.0) | Scene Ponder animate, come quelle di Create, per Mekanism e Generators |
| Pezzi extra per Create | **Create: Connected** 1.3.3 (AGPL-3.0) | Frizioni e cambi speciali, componenti redstone, batteria cinetica che conserva la carica, vault e serbatoi orientabili, migliorie a Sequenced Gearshift e filtri. Ogni funzione disattivabile da config |

### 4.5 Storage, zaini e trasporto

| Mod | Licenza | Note |
|---|---|---|
| **Storage Drawers** 13.x | MIT | Cassetti per storage di massa, interazione a click, controller, upgrade |
| **Tom's Simple Storage** | MIT | Collega casse e barili a un unico terminale (anche con crafting), connettori filtrati, terminale wireless. Il **beacon** estende il raggio del wireless: livello 1 = tutta la dimensione, livello 4 = anche le altre dimensioni. Sviluppo attivissimo |
| **Ender Storage** (covers1624) 1.21.1-2.13 | ❓ | Ender Chest, Ender Pouch ed **Ender Tank** collegati da un codice di 3 colori: stesso codice = stesso contenuto, anche tra dimensioni. Ultimo aggiornamento circa un anno fa |

**Zaini — doppio zaino** (approvato il 16/10/2026)

| Mod | Licenza | Note |
|---|---|---|
| **Sophisticated Backpacks** 3.26.x (+ Sophisticated Core) | ARR (GPL-3.0 fino a febbraio 2025) | Lo zaino "tecnico": da 27 a 120 slot, fino a 7 upgrade (magnete, raccolta, auto-alimentazione, rifornimento, scambio attrezzi, crafting, fornaci, incudine, serbatoi, batteria, compattazione, cestino…). Integrazione con EMI, Mouse Tweaks, wrench di Create e chiavi di Storage Drawers. Gli upgrade funzionano anche con lo zaino nell'inventario. Bug aperto: duplicazione piazzandolo (#1719) |
| **Sophisticated Backpacks Create Integration** | ARR | Zaini piazzati sui contraption e negli schematic di Create, con gli upgrade attivi |
| **Traveler's Backpack** 10.1.39 | LGPL-3.0 | Lo zaino "da avventura", indossato nello slot schiena (si vede addosso): da 27 a 99 slot, 2–6 upgrade + slot attrezzi (tasto Z per ciclarli), serbatoi per fluidi, sacco a pelo integrato, varianti a tema con abilità, backup degli zaini persi. Bug aperto: crash se piazzato su una tramoggia (#1595) |

Come convivono: Traveler's nello slot schiena, Sophisticated nello slot del petto o nell'inventario. Entrambi aprono con **B** → cambiare il tasto di uno (vedi 3.4).

Zaini dentro zaini (verificato nel codice):
- **Sophisticated dentro Sophisticated**: solo con l'**Inception Upgrade** (lo zaino interno non deve averne uno a sua volta). Shulker box ammesse di default
- **Traveler's dentro Traveler's**: mai, bloccato nel codice. Shulker box e altri oggetti con inventario solo con `allowShulkerBoxes = true`
- **Traveler's dentro Sophisticated**: sì, di default
- **Sophisticated dentro Traveler's**: solo con `allowShulkerBoxes = true` nella config di Traveler's

**Lava farm** — schema scelto, senza mod in più: **Hose Pulley di Create** calato nell'oceano di lava del Nether (una massa di almeno 10.000 blocchi è considerata infinita) → Ender Tank (stesso codice colore) → Ender Tank in base → Pipez verso le macchine. Il lato Nether va tenuto caricato con un chunk loader.
Alternative: Quantum Entangloporter di Mekanism al posto degli Ender Tank; gamerule vanilla `lavaSourceConversion` (la lava si rigenera come l'acqua, più "cheat").

### 4.6 Equipaggiamento e incantamenti

| Mod | Licenza | Note |
|---|---|---|
| **Truly Modular: Modular Item API (Miapi)** 2.3.9 | PolyForm Shield 1.0.0 | API data-driven per oggetti modulari; dipendenza Architectury API. Da sola non aggiunge contenuti. "Materiali generativi": crea materiali in automatico dai contenuti delle altre mod. Sorgente su GitHub, wiki, Discord. Licenza: sorgente disponibile e modificabile, ma non open source in senso OSI. ⚠️ Crash con Accessories (vedi 3.2) |
| TM: **Arsenal** 2.4 | GPL-3.0 | Armi da mischia e attrezzi (12 lame, guardie, impugnature anche doppie, pomoli, moduli attrezzo) |
| TM: **Archery** | ❓ | Archi, balestre, frecce modulari |
| TM: **Armory** 2.2 | MIT | Armature modulari (cotta di maglia, piastre, pesante, wingsuit per elytra, scuba) |
| **Apotheosis** 1.21.1-8.9.0 | ❓ | Overhaul degli incantamenti, affissi e gemme sull'equipaggiamento (supportati anche sugli oggetti modulari), spawner, **World Tiers**, mob potenziati (Apothic Elites). Dipendenze: Placebo, Patchouli, Apothic Attributes, Apothic Spawners, Apothic Enchanting |
| **Truly Modular Material Helper** | strumento web | Crea datapack di compatibilità materiali senza scrivere codice |

### 4.7 Strutture

| Mod | Licenza | Note |
|---|---|---|
| **YUNG's** Better Dungeons, Mineshafts, Strongholds, Nether Fortresses, Ocean Monuments, Desert Temples, Jungle Temples, Witch Huts, Bridges, Extras (+ YUNG's API 5.1.9) | LGPL | Rifanno le strutture vanilla invece di aggiungerne → non affollano il mondo. ⚠️ Progetti NeoForge separati |
| **When Dungeons Arise** 2.1.68 | ARR | Dungeon enormi (castelli, fortezze, navi volanti) |
| **Dungeons and Taverns** v4.4.4 | ❓ | Taverne, avamposti, piccoli dungeon. Solo la mod base |
| **Towns and Towers** 1.13.11 | CC-BY-NC-SA | Varianti di villaggi e avamposti per bioma; tiene i villaggi vanilla (le Waystones nei villaggi restano). Richiede Cristel Lib. Tombstone ha già un fix di compatibilità |
| **Moog's End Structures** | LGPL | Strutture per l'End; richiede Moog's Structure Lib |
| **Sparse Structures** 3.0 | MIT | Distanzia tutte le strutture; **unica** mod di spacing |
| **Explorer's Compass** 3.4.0 | ❓ | Bussola che punta a una struttura scelta per nome |
| **Compass to Map: Xaero's** 0.1.2 | ARR | Segna sulla mappa di Xaero's il bersaglio della bussola |

Structure Layout Optimizer è in 4.13.

### 4.8 Dimensioni

| Mod | Licenza | Note |
|---|---|---|
| **The Twilight Forest** 4.8.3345 | ❓ | Dimensione con progressione a boss |
| **Deeper and Darker** 1.4.1 | AGPL | Deep Dark espanso + dimensione Otherside |
| **The Undergarden** 0.9.6 (beta) | ❓ | Dimensione sotterranea con mob e boss propri |
| **YUNG's Better End Island** + **Unusual End** 2.3.1b | ❓ | End rinnovato: isola centrale e biomi nuovi. Unusual End richiede Blueprint |
| **The Aether** 1.5.10 + **Deep Aether** 1.1.5.1 ⚠️ | ❓ | Isole nel cielo, dungeon con boss. Deep Aether richiede TerraBlender. **Condizionate al test** Miapi/Accessories (3.2); se fallisce si toglie l'Aether e si tiene Truly Modular |

### 4.9 Boss e nemici

| Mod | Licenza | Note |
|---|---|---|
| **L_Ender's Cataclysm** 3.33 | CC-BY-NC-ND | I boss più impegnativi della 1.21.1, ognuno con la sua struttura e armi uniche. Richiede Lionfish API e Curios (forse Citadel 2.7.1) |
| **Mowzie's Mobs** 1.8.2 | ❓ | Pochi boss molto curati, con armi uniche; GeckoLib |
| **Born in Chaos** 1.7.6 | ARR | Mob horror e boss notturni; GeckoLib |
| **Born In Configuration** | MIT | Trasforma le gamerule di Born in Chaos in un file di config |
| **Friends & Foes** 5.0.2 | ❓ | Mob delle Mob Vote mai aggiunti (es. Copper Golem, Glare, Iceologer, Illusioner); Resourceful Lib |
| **Mutant Monsters** v21.1.1 | AGPL | Versioni mutanti di zombie, creeper, scheletro, enderman; Puzzles Lib |
| **Illager Invasion** v21.1.6 | MIT | Nuovi illager e incursioni più varie |
| **Ender Dragon Fight Remastered** 5.0.2 | ❓ | Scontro con il drago rifatto, più fasi e attacchi |
| **Gateways to Eternity** 5.1.0 | MIT | Portali da cui escono ondate di nemici e boss; stesso autore di Apotheosis |

Leve di difficoltà: vedi 3.4. Corail Tombstone rende meno punitive le morti durante i boss.

### 4.10 Villager

Già nel pack: **Apotheosis (Apothic Enchanting)** riduce molto il bisogno dei bibliotecari, con il tavolo da incantamento a statistiche (Eterna, Quanta, Arcana, "indizi") e la **biblioteca degli incantamenti**, dove si depositano libri e si estrae l'incantamento al livello voluto.

| Mod | Licenza | Note |
|---|---|---|
| **Easy Villagers** 1.21.1-1.1.42 | ❓ | Stesso autore di Pipez. Villager raccoglibili come oggetto; blocchi Trader, Auto Trader, Breeder, Converter (cura da zombie per gli sconti), Incubator |
| **Easy Auto Cycler** | ❓ | Solo client. Cicla i trade in automatico e si ferma su quello cercato (filtri, livello minimo, valuta). Su NeoForge 1.21.1 richiede Easy Villagers |

### 4.11 Utilità di gioco

| Mod | Licenza | Note |
|---|---|---|
| **Chunk Loaders** (SuperMartijn642) | ARR | Single (1 chunk), Basic (3×3), Advanced (5×5), Ultimate (7×7); mappa per scegliere i chunk; i chunk caricati ricevono i random tick. I mob non spawnano senza giocatore vicino. Anche Mekanism ha chunk loading (Dimensional Stabilizer, Anchor Upgrade) |
| **Corail Tombstone** 9.5.x | ❓ | Tomba con l'inventario alla morte + perk, oggetti, lore, esplorazione; tutto configurabile |
| **Waystones** (BlayTheNinth) 21.1.x | ❓ | Pietre del viaggio: teletrasporto tra quelle attivate (anche pergamene e Warp Stone); generate nei villaggi; pulsante opzionale nell'inventario. Dipendenza: Balm |
| **Xaero's ↔ Waystones Compatibility** | ARR | Waypoint automatico su minimappa e mappa quando attivi una waystone |
| **Akashic Tome** (Vazkii) 1.21.1-1.8-30 | CC-BY-NC-SA-3.0 | Un solo libro che contiene i libri guida di tutte le mod; shift+click destro su un blocco di una mod apre il suo libro. Create (Ponder), Mekanism e FD non hanno un libro fisico |
| **OmniTools** (Omni Wrench) 1.21.1-1.2.1 | ❓ | Wrench universale; integrazioni ufficiali attuali Create e Mekanism. Mod giovane, lista in crescita |

### 4.12 Interfaccia e mappa

| Mod | Note |
|---|---|
| **EMI** 1.1.x + **JEI** | EMI come interfaccia (albero delle ricette con quantità totali, preferiti legati a una ricetta); JEI sotto per i plugin delle mod che supportano solo JEI |
| **EMI Loot** · **EMI Ores** | Drop di mob e casse, distribuzione dei minerali, dentro EMI (MIT / LGPL) |
| **Jade** | Info sul blocco guardato (calderoni, bollitori, macchine…) |
| **AppleSkin** | Fame e saturazione dei cibi |
| **Polymorph** 1.1.0 | Con decine di addon FD i conflitti di ricette sono probabili: un pulsante permette di scegliere il risultato |
| **Xaero's Minimap + World Map** | Leggere, standard nei modpack, molti addon di compatibilità |
| **Enchantment Descriptions** 21.1.11 | LGPL-2.1. Descrizione di ogni incantamento nel tooltip. Apothic Enchanting la supporta: da solo descrive solo i propri incantamenti |
| **Pick Up Notifier** | MPL-2.0. Avviso a lato dello schermo con gli oggetti raccolti e la quantità |
| **YUNG's Menu Tweaks** | LGPL-3.0. Schermate del menu più curate, in particolare la creazione del mondo |

### 4.13 Performance (client, single player)

| Mod | Ruolo |
|---|---|
| **Sodium** 0.8.13 (NeoForge 1.21.1) | Motore di rendering, fino a +115% nel rendering del mondo su alcuni PC |
| **Lithium** | Logica di gioco (fisica, IA, tick dei blocchi) senza cambiare le meccaniche |
| **FerriteCore** | Meno RAM |
| **ModernFix** | Avvio più rapido, meno memoria, bugfix |
| **ImmediatelyFast** | Rendering di interfacce, contenitori, testo |
| **Entity Culling** | Non disegna entità e blocchi non visibili |
| **Structure Layout Optimizer** 1.0.12 (MIT) | Velocizza la generazione delle grandi strutture jigsaw; richiede Resourceful Config |

### 4.14 Fix e compatibilità

| Mod | Note |
|---|---|
| **Paxi** 1.21.1-NeoForge-5.1.3 | ✅ Approvata il 16/10/2026. LGPL-3.0, di YUNG (usa YUNG's API, già presente). Carica in automatico in ogni mondo i datapack messi in `config/paxi/datapacks/` (e i resource pack in `config/paxi/resourcepacks/`) |
| **AlmostUnified** 1.4.2 | ✅ Approvata il 16/10/2026, per sicurezza e per mod future. ARR. Unifica minerali e lingotti doppi tra le mod (oggi nel pack non ce ne sono: ogni metallo arriva da una mod sola). La config di default copre i metalli |
| **Forgified Fabric API** 0.116.15+2.3.5+1.21.1 (Sinytra) | ✅ Approvata il 16/10/2026, fissa nel pack. Apache-2.0. Port di Fabric API su NeoForge: libreria comune per mod multi-loader, include anche il "Forgified Fabric Loader". **Perché la teniamo a prescindere**: Accessories 1.1.0-beta.53 (ultima per 1.21.1, ferma a febbraio 2026) chiama per errore una classe di Fabric Loader quando una mod chiede uno slot fuori range (`ExpandedSimpleContainer.validIndex`) → su NeoForge crash `NoClassDefFoundError`. Con FFAPI la classe esiste e il crash non scatta. Accessories è già nel pack con Hexalia, quindi serve anche senza Miapi. Sviluppo attivo (ultimo commit sul ramo 1.21.1: 15/10/2026). Contro: libreria grossa (decine di moduli), una variabile in più quando si indaga un crash |

### 4.15 Comodità (approvate il 16/10/2026)

| Mod | Licenza | Note |
|---|---|---|
| **Mouse Tweaks** 2.26.1 | BSD-3 | Trascinare e scorrere per spostare oggetti |
| **Controlling** 19.0.5 | MIT | Ricerca tra i tasti e conflitti |
| **Crafting Tweaks** 21.1.x | ARR | Pulsanti per ruotare, bilanciare e svuotare la griglia |
| **Simple Backups** 4.0.21 (ultima release; le successive sono beta) | Apache-2.0 | Backup automatici del mondo |
| **Torchmaster** 21.1.13 | MIT | Mega Torch: niente spawn ostili attorno alla base |
| **Comforts** 9.0.5 | LGPL-3.0 | Sacchi a pelo e amache: si dorme in esplorazione senza spostare lo spawn |
| **Carry On** 2.2.6 (luglio 2026) | LGPL-3.0 | Prendere in mano casse, macchinari, blocchi e animali e spostarli senza svuotarli (shift + click destro a mani vuote). Più il blocco è complesso, più si rallenta. Config in 3.4 |
| **RightClickHarvest** 4.6.1 | MIT | Raccolta e ripianta con click destro |
| **FallingTree** 1.21.1.11 | LGPL-3.0 | Abbatte l'albero intero (configurabile, vedi 3.4) |
| **Leaves Be Gone** 21.1.1 | MPL-2.0 | Le foglie cadono subito dopo il taglio |
| **Inventory Essentials** 21.1.20 | ARR (sorgente visibile) | Ordinamento con click centrale; rimpiazzo automatico di attrezzi rotti e pile finite; non tocca mai hotbar e armatura. Stesso autore di Crafting Tweaks, usa Balm (già presente). Disattivare `enableShiftDrag` (doppione di Mouse Tweaks). Scelta al posto di Client Sort e Inventory Profiles Next (6.10) |

### 4.16 Atmosfera (approvate il 16/10/2026, tutte lato client)

| Mod | Licenza | Note |
|---|---|---|
| **Sound Physics Remastered** 1.5.1 | GPL-3.0 | Riverbero e occlusione: grotte e dungeon suonano realistici |
| **AmbientSounds** 6.3.10 | LGPL-3.0 | Suoni ambientali per bioma e ora del giorno; richiede CreativeCore |
| **Subtle Effects** 1.15.0 | ARR (sorgente su GitHub) | Particelle ambientali, battito a poca vita, stomaco che brontola |
| **Particle Rain** 4.0.1 | MIT | Pioggia, neve e nebbia a particelle |
| **LambDynamicLights** 4.8.11 | Lambda License | Luce dalla torcia tenuta in mano. Mod originale (sostituisce Sodium Dynamic Lights, port non ufficiale); ultima build per la 1.21 |
| **Enhanced Celestials** 6.0.2.6 | ❓ | Mod originale: lune di sangue (più mostri) e lune del raccolto (raccolto doppio delle colture) già incluse, più lune blu e super lune. Eventi definiti via datapack, quindi tarabili. Richiede CorgiLib + Data Anchor |
| **Travelers Titles** 5.1.3 | LGPL-3.0 | Titolo a schermo quando entri in un bioma o in una dimensione |
| **Not Enough Animations** 1.12.6 | tr7zw Protective (sorgente disponibile) | Animazioni in terza persona (mangiare, mappe, scale) |
| **Entity Model Features** 3.3.12 + **Entity Texture Features** | LGPL-3.0 | Motori per modelli e texture animate dei mob |
| **Fresh Animations** (resource pack) | licenza del pack | Mob vanilla animati; si attiva tra i resource pack |
| **Shoulder Surfing Reloaded** 5.2.0 | MIT | Telecamera in terza persona sopra la spalla, con mirino; comoda nei boss e in esplorazione |

### 4.17 Animali e pesca (approvate il 16/10/2026)

| Mod | Licenza | Note |
|---|---|---|
| **Starcatcher** | custom (codice) + ARR (asset) | Pesca rifatta: minigioco di abilità, oltre 100 pesci legati a bioma, meteo, ora e quota, esche, cassetta degli attrezzi da pesca, trofei, acquari, catalogo da completare. Addon FD: Starcatcher's Delight (4.1) |
| **Animal Pens** 2.5.0 | GPL-3.0+ | Recinti, acquari e voliere: gli animali stanno "dentro" il blocco (meno lag) e producono latte, lana, uova, scaglie; nutrirli li fa riprodurre. Richiede Architectury (già presente) |
| **Animal Feeding Trough** 1.1.2 | MIT | Trogolo da cui gli animali vicini mangiano da soli. ❓ Verificare in Prism la build 1.21.1 (presente in Craftoria) |

**Starcatcher e la cucina** (verificato nel codice di Starcatcher 1.21.1 e Starcatcher's Delight 3.2, 17/10/2026)
- I 132 pesci di Starcatcher sono nelle etichette `c:foods/raw_fish`, `minecraft:fishes` e `minecraft:cat_food`. Farmer's Delight mette `c:foods/raw_fish` dentro `c:foods/safe_raw_fish` (tolto il pesce palla), quindi i pesci crudi valgono nelle ricette "pesce crudo qualsiasi": FD (zuppa di pesce, involtini di cavolo, pasta al nero di seppia), Brewin' And Chewin' (pasta al formaggio, aringhe affumicate), Veggies Delight (fish and chips, torta di rape), Farm & Charm (cibo per gatti)
- **Starcatcher's Delight**: sul tagliere ogni pesce dà un filetto della sua rarità (5 livelli) più lische; i filetti sono in `c:foods/safe_raw_fish`. 50 piatti nella pentola di FD, con la qualità che cresce con la rarità del pesce (es. fish and chips comune → leggendario); le stesse ricette anche nella pentola di Farm & Charm
- ⚠️ Cotto in fornace, affumicatore o falò, ogni pesce diventa un generico "pesce stellato cotto" che **non** è in `c:foods/cooked_fish`: non vale nelle ricette col pesce cotto di Cultural Delights (taco, fish and chips) e Bountiful Fares (zuppa di pesce, misto costiero). Si sistema con un'etichetta nel datapack `matteo_tweaks` (proposta, non fatta)
- Starcatcher aveva nel codice l'integrazione dei pesci di altre mod nel minigioco (Aquaculture, Nether Depths Upgrade, Critters and Companions, Eternal Starlight, Upgrade Aquatic…), ma l'autore l'ha disattivata l'8/7/2026: nella 3.3.6 del pack resta solo quella con Tide

### 4.18 Magia e oggetti magici (approvate il 16/10/2026)

La magia "popolare" (Hexalia, Hexerei, Aspect Alchemy, HerbalBrews) è in 4.3; analisi completa in 5.10.

| Mod | Licenza | Note |
|---|---|---|
| **Ars Nouveau** 5.13.3 (3/10/2026) | codice LGPL-3.0, grafica ARR | Incantesimi componibili (forma + effetti + potenziamenti) con tono naturalistico: fonti di energia magica (anche dalla crescita delle colture), famigli, rituali, Starbuncle che trasportano oggetti. Richiede **Curios** e **GeckoLib** (già presenti). Supporto **EMI e JEI** nativo, plugin Jade. Guida propria (Worn Notebook, data al primo ingresso), dovrebbe agganciarsi all'Akashic Tome senza config (da provare). Usa gli slot Curios testa, collana e cintura |
| ↳ **Ars Delight** (Ars Nouveau's Flavors & Delight) 2.2.5 (6/10/2026) | LGPL-2.1 | 49+ cibi con ingredienti di Ars per Farmer's Delight |
| ↳ **Ars Creo** 5.4.0 (24/5/2026) | dello sviluppatore di Ars | Ars ↔ Create: torrette di incantesimi sui contraption, ruota degli Starbuncle (energia rotazionale). Create 6.0.9+ |
| ↳ **Ars Mekanica** 1.3.0 (27/7/2026) | LGPL-2.1 | Ars ↔ Mekanism: Source Dynamo (energia magica → FE), legno di Ars nella segheria |
| ↳ **Ars Elemental** 0.7.10.4 (4/10/2026) | LGPL-3.0 · solo CurseForge | Il grande addon di contenuti: glifi elementali, foci, armature, braccialetti (slot Curios propri) |
| ↳ **Ars QOL** 1.2.1 (5/10/2026) | MIT | Slot Curios per il libro degli incantesimi, con tasto rapido |
| ↳ **Ars Unification** 1.2.19 | LGPL-3.0 | I glifi Frantuma/Taglia usano le ricette di Mekanism e del tagliere di FD; convive con AlmostUnified |
| ↳ **Not Enough Glyphs** 4.6.x | LGPL-3.0 | Glifi extra e SpellBinder |
| ↳ **Ars Controle** 1.6.16 (10/9/2026) | LGPL-3.0 | Prisma di teletrasporto, collegamenti di scrutamento, filtri |
| **Artifacts** 13.2.5 (2/9/2026) | MIT | Ninnoli magici da trovare: accampamenti, mimic, casse. Nessuna dipendenza obbligatoria. Con Curios **e** Accessories presenti registra i suoi slot in **entrambe** → config consigliata in 3.4 (usare solo Curios). Nessuna sovrapposizione con Apotheosis, che non mette affissi sugli accessori. Bottino nelle strutture modded: datapack del pack (3.3) |
| **Occultism** 1.224.5 (11/10/2026) | MIT | Evocazione di spiriti con rituali e pentacoli di gesso: lavoratori (frantumatore, fornace, taglialegna, contadino, trasportatore), magazzino dimensionale, miniera dimensionale, famigli. EMI e JEI nativi, compat Apotheosis. Richiede Modonomicon, Curios, GeckoLib, SmartBrainLib. Frantumatore lasciato di default (3.4) |
| ↳ **Ars Ocultas** 1.21.1-2.6.1 (6/8/2026) | LGPL-3.0 | Ponte Ars ↔ Occultism: spiriti lavoratori dentro i barattoli di contenimento di Ars (area 7×7, ricevono da tubi e Starbuncle), Altare sacrificale |
| ↳ **Occult Delight** 1.0.0 (31/7/2026) | MIT | Pentola di Farmer's Delight che prende gli ingredienti dal magazzino dimensionale |
| **Reactive Alchemy** 1.21.1-10.2.1 (27/9/2026) | CC-BY-NC-4.0 | Crogiolo (calderone vanilla convertito) dove gli oggetti diventano "poteri" che reagiscono con regole diverse in ogni mondo: effetti nell'area, trasmutazione, bastoni del potere, portale. Richiede Patchouli. JEI (EMI tramite JEI) |
| **Psi** 1.21.1-110 (1/9/2026) | licenza Psi (sorgente pubblico) | Magia programmabile: incantesimi su griglia 9×9 caricati in un CAD a pezzi; Exosuit e attrezzi in psimetallo. Richiede Patchouli. Tasto C da cambiare (3.4) |
| **Scriptor Magicae** 2.0.14 (17/9/2026) | CC0 | Incantesimi scritti in una lingua casuale per ogni mondo, da decifrare con tomi antichi; costo in tempo di ricarica, non mana. Richiede Unfocused e Kotlin for Forge. EMI e JEI |

---

### 4.19 Biomi, decorazione e utilità (approvate il 17/10/2026)

| Mod | Licenza | Note |
|---|---|---|
| **Regions Unexplored** 0.6.2 (12/7/2026) | MIT | ~50 biomi "vanilla migliorato" via TerraBlender (+ libreria Lithostitched, MIT). Verificato nel codice: mette i suoi biomi nelle etichette `minecraft:is_overworld` (minerali di Mekanism e zinco di Create), `c:is_hot/wet/swamp…` (colture selvatiche di FD, capanna di Hexalia), `minecraft:is_forest/taiga/jungle/hill/river` (When Dungeons Arise) e nei gruppi delle strutture vanilla; Dungeons and Taverns cita già 58 suoi biomi per nome; Botany Trees supporta i suoi alberi. Scelta al posto di BWG (ARR, meno etichette, DnT lo conosce solo col vecchio nome `byg:`). ⚠️ Solo nei chunk nuovi → **prima del mondo vero** |
| **Chunky** 1.4.23 | GPL-3.0 | Pre-generazione del mondo (`/chunky radius <blocchi>` poi `/chunky start`) |
| **Clumps** 19.0.0.1 | MIT | Unisce le sfere di esperienza |
| **Supplementaries** 4.0.2 (16/10/2026) | licenza propria | Barattoli, sacchi, casseforti, cartelli, bandiere, piedistalli, mensole, lino… Richiede Moonlight. Piccole sovrapposizioni: corda (FD, Farm & Charm), lino. Build di un giorno fa: tenere d'occhio. Amendments resta fuori (da verificare con Reactive Alchemy, che usa il calderone vanilla) |
| **Handcrafted** 4.0.3 | Terrarium | Mobili in stile vanilla per tutti i legni, compresi piani e pensili da cucina (scelta al posto di Another Furniture) |
| **Rechiseled** 1.2.6 (13/9/2026) | ARR | Scalpello per varianti decorative dei blocchi, con texture collegate (Fusion). Alternative non scelte: Chisel Reborn, Chipped |
| **Construction Sticks** 1.5.0 | MIT | Bacchette che allungano una superficie di una fila di blocchi |
| **XP Tome** v2.4 | MIT | Libro che contiene ~1400 punti esperienza (configurabile), per portarli in giro; nessuna dipendenza. Banca fissa: Experience Hatch di Create: Enchantment Industry (5.11) |

### 4.20 Piccole e utili (approvate il 17/10/2026)

| Mod | Licenza | Note |
|---|---|---|
| **Just Enough Breeding** 3.3.1 | MIT | Mostra in EMI il cibo per far accoppiare ogni animale, anche modded |
| **Just Enough Professions** 4.0.5 | MIT | Mostra in EMI i blocchi di lavoro dei villager (passa da JEI) |
| **NetherPortalFix** 21.1.1 | ARR | Al ritorno dal Nether ti riporta al portale da cui sei entrato. Richiede Balm |
| **AllTheLeaks** 1.1.13 (22/9/2026) | MIT | Corregge perdite di memoria di molte mod. **Solo CurseForge**: da aggiungere a mano. Nel sorgente si dichiara incompatibile solo con versioni vecchie di GeckoLib, Entity Culling, AmbientSounds e Occultism: le nostre sono più nuove |
| **SeasonHud** 2.0.10 | MIT | Mostra la stagione di Serene Seasons sotto la minimappa di Xaero |
| **Smarter Farmers** 2.2.4 | ARR | I villager contadini ripiantano il seme giusto, anche delle colture modded. Richiede Moonlight |
| **Open Together** 21.1.2 | MPL-2.0 | Le porte doppie si aprono insieme. Richiede Puzzles Lib |

## 5. Mod opzionali 👀 (per tema)

### 5.1 Cucina e bevande

**Addon FD — seconda ondata** (ricerca Modrinth del 17/10/2026, valutazione in 5.13): su Modrinth per 1.21.1 NeoForge ci sono Ocean's Delight, Rustic Delight, Corn Delight, Seed Delight (ultima build 2024), End's Delight, Aquaculture Delight (2025, richiede Aquaculture), My Nether's Delight, Chef's Delight; build esatta e compatibilità con FD da verificare prima di aggiungerle. Non trovate su Modrinth: Cocktails Delight, Bountiful Harvest, Delightful (solo 1.20.1).

### 5.2 Botany Pots

| Mod | Note |
|---|---|
| **BotanyCompatLayer** (datapack) | Colture e terreni di Aether, End's Delight, Rustic Delight, Oritech, mod Let's Do e altre. Pubblicato da poche settimane. Va nella cartella `datapacks` del mondo |
| **Botany Pots Ore Planting** | Coltiva minerali (lingotto come seme, blocco come terreno), supporta Create e Mekanism. Molto "cheese" |

### 5.3 Natura, erbe e pozioni

| Mod | Licenza | Note |
|---|---|---|
| **Just Another Witchery Remake** 0.5.22 (16/10/2026, vedi 5.10) | dichiara LGPL-3.0 ma nessun sorgente pubblico | Remake di Witchery, rituali data-driven, aggiornata di continuo. ⚠️ WIP e instabile; la 0.4→0.5 rompe i mondi |
| **Nature's Aura** 41.x | MIT | Aura in ogni chunk: altare naturale, Rituale della Foresta, generatori che "mangiano" fiori; se la consumi troppo la terra si ammala, se ne produci in eccesso la vegetazione cresce. Richiede Patchouli (già presente) |

### 5.4 Tech e storage

- **BBL Routers** — trasporto oggetti wireless
- **Create Contraption Terminals** — terminali di Tom's Simple Storage su contraption e treni di Create

### 5.5 Equipaggiamento e incantamenti

| Mod | Note |
|---|---|
| **Better Combat** 2.4.x | Combattimento in stile Minecraft Dungeons (animazioni, combo, hitbox reali); supporto integrato in Miapi. Cambia parecchio il feeling del combattimento |
| **Apothic Combat** | Compat Better Combat × Apotheosis, solo se entra Better Combat |
| **Truly Modular: Next Level** | Addon ufficiale di leveling degli attrezzi (XP → upgrade data-driven). Repo su GitHub, non trovato su Modrinth |
| **Apotheotic Creations** | Filtri di Create che riconoscono gear con affissi e gemme (port NeoForge recente e poco scaricato) |

### 5.6 Strutture

| Mod | Note |
|---|---|
| **WDA: Seven Seas** 1.0.4 | Navi e strutture in mare |
| **Explorify** 1.6.5 **oppure** **Moog's Voyager Structures** | Strutture "filler" sparse; sceglierne **una sola** |
| **Moog's Nether Structures** | Strutture per il Nether |
| **Structory** 1.3.17 | Rovine e piccole strutture d'atmosfera |
| **YUNG's Better Caves** 3.1.6 | Grotte rifatte |
| **Nature's Compass** | Bussola che trova i biomi |
| **Repurposed Structures** 7.5.22 | LGPL, ha un datapack di compat FD. Solo **al posto di** Towns and Towers |

### 5.7 Dimensioni

| Mod | Note |
|---|---|
| **Eternal Starlight** 0.9.1 | MIT. Dimensione con boss |
| **The Bumblezone** 7.16.1 | Dimensione delle api; Resourceful Lib |
| **Create: Northstar Redux** 0.6.6 | Beta, MIT. Lo spazio con Create |
| **Nether Depths Upgrade** 3.3 | Pesci e fondali dei mari di lava del Nether |
| **End Remastered** 6.3.0 | Cambia gli occhi di Ender e la ricerca dell'End |
| **Tectonic** | Solo menzione: rilievi più spettacolari, va d'accordo con un solo mod di biomi |

### 5.8 Boss e nemici

| Mod | Note |
|---|---|
| **Bosses of Mass Destruction** 1.3.3 | Port non ufficiale, LGPL |
| **Aquamirae** 7.2.12 | Boss e mob degli oceani ghiacciati; licenza custom, richiede GeckoLib e Fragmentum |
| **Legendary Monsters** 2.2.3 **oppure** **Bosses'Rise** | Sceglierne uno solo. Legendary Monsters: ARR, circa 15 boss tra early e late game |
| **Wither's Wrath** | Scontro con il Wither potenziato |
| **It Takes a Pillage Continuation** | Port non ufficiale; più varietà nei pillager |
| **Alex's Mobs Continued** + il suo Delight | Port non ufficiale (CodxLib) |
| **Naturalist** 2.0.5 · **Critters and Companions** | Animali, non nemici |
| **In Control!** · **Enhanced AI** | Strumenti di difficoltà: regole di spawn e IA più furba (Enhanced AI al posto di Improved Mobs) |

### 5.9 Grandi aggiunte dal confronto con i modpack famosi — da decidere con calma

Pack confrontati il 16/10/2026 (tutti 1.21.1): ATM10 v8.2, Craftoria 1.37.0, FTB Evolution 1.45.1, FTB StoneBlock 4 1.23.0, All of Create 2.6, Create Chronicles: The Endventure 2.0.0, Better MC (BMC5), Fresh & Smooth. Tutte le altre proposte del confronto sono state approvate (sezione 4) o scartate (6.10).

| Mod | Licenza | Note |
|---|---|---|
| ✅ Biomi: **Regions Unexplored** scelta il 17/10/2026 (→ 4.19); ⛔ Oh The Biomes We've Gone | ARR / MIT | Unica grande categoria assente. Usano TerraBlender (già presente per Deep Aether). BWG è nei pack più famosi e in BMC5 convive con Serene Seasons e Aether; Regions Unexplored è open source. Da decidere **prima** di creare il mondo; poi generare i datapack di Botany Pots per gli alberi nuovi |
| **Geophilic** 3.7 · **YUNG's Cave Biomes** 3.1.1 | ARR | Ritocco dei biomi vanilla (pensato per BWG); biomi di grotta YUNG |
| ✅ Decorazione (17/10/2026, → 4.19): **Supplementaries** + **Handcrafted** + **Construction Sticks** (+ **Rechiseled**); non scelte Another Furniture, Chisel Reborn, Chipped; Amendments da valutare | custom / Terrarium / custom / MIT | Barattoli, sacchi, cartelli, vasi; mobili; bacchetta da costruzione. Amendments resta fuori (conflitto con il calderone di Toil and Trouble) |
| ~~**Ars Nouveau**~~ | — | ✅ Approvata il 16/10/2026 → 4.18 (Iron's Spells resta l'alternativa, vedi 5.10) |
| Trasporti: **Create Aeronautics** 1.3.2 **oppure** **Immersive Aircraft** 1.5.0 | custom / GPL-3.0 | Aeronavi e veicoli costruiti con Create (grande novità 2026, pesante) oppure biplani e dirigibili semplici |
| ~~**Artifacts**~~ | — | ✅ Approvata il 16/10/2026 → 4.18 |
| **Mekanism Tools** 10.7.19 | MIT | Ufficiale: attrezzi e armature in osmio, bronzo, acciaio. Si sovrappone a Truly Modular |

**Archivio — confronti già decisi**

**Zaino — confronto**

| | Sophisticated Backpacks | Traveler's Backpack | Backpacked 3 |
|---|---|---|---|
| NeoForge 1.21.1 | 3.26.12 (13/10/2026) + Sophisticated Core | 10.1.39 (29/08/2026) | 3.0.5 (03/04/2026), richiede Framework |
| Licenza | ARR (era GPL-3.0 fino a febbraio 2025) | LGPL-3.0 | LGPL-2.1 |
| Sviluppo | Release ogni pochi giorni | Circa mensile | Lento, molte issue aperte |
| Capienza | Da 27 a 120 slot, 1–7 upgrade (cuoio → netherite) | Da 27 a 99 slot, 2–6 upgrade + slot attrezzi | 9 slot, ampliabili spendendo XP |
| Funzioni | Magnete, raccolta, auto-alimentazione, rifornimento, scambio attrezzi, crafting, fornaci, incudine, serbatoi, batteria, compattazione, cestino… | Magnete, raccolta, auto-alimentazione, crafting, fornaci, serbatoi, cestino, sacco a pelo integrato, varianti a tema | Potenziamenti in stile vanilla: raccolta, semina, torce, riparazione; niente crafting né serbatoi |
| Dove si indossa | Slot del petto oppure slot schiena (Curios/Accessories) | Slot schiena (Curios/Accessories) | Slot proprio |
| Integrazioni | EMI, Mouse Tweaks, wrench di Create, chiavi di Storage Drawers; addon Create (zaini sui contraption) | EMI, backup degli zaini persi | — |
| Problemi noti | Duplicazione piazzandolo (#1719) | Crash se piazzato su una tramoggia (#1595) | Crash premendo Esc (#309); morte gestita solo con YIGD |

Consiglio: **Sophisticated Backpacks** (+ Core, eventualmente l'addon Create), indossato nello slot schiena per lasciare libero il pettorale. È il più completo e il più curato, e i suoi upgrade si sposano con Create, Mekanism e il cibo FD. Prezzo: licenza ARR (conta solo se un giorno si redistribuisce il pack o si vuole tutto open). Alternativa open: **Traveler's Backpack** (meno upgrade; il sacco a pelo integrato fa doppione con Comforts). Con Tombstone: provare una morte con lo zaino nello slot schiena.

Zaini dentro zaini (verificato nel codice, 16/10/2026):
- **Sophisticated dentro Sophisticated**: solo con l'**Inception Upgrade** (e lo zaino interno non deve averne uno a sua volta). Shulker box ammesse di default
- **Traveler's dentro Traveler's**: mai, è bloccato nel codice. Shulker box e altri oggetti con inventario solo attivando `allowShulkerBoxes` nella config
- **Traveler's dentro Sophisticated**: sì, di default
- **Sophisticated dentro Traveler's**: solo con `allowShulkerBoxes = true` nella config di Traveler's

Tenerli **entrambi** è possibile (l'utente ci sta pensando): lo slot schiena è uno solo, quindi uno si indossa (Traveler's si vede sulla schiena) e l'altro va nello slot del petto o resta nell'inventario (gli upgrade di Sophisticated funzionano anche da lì). Entrambi aprono con **B** → cambiare il tasto di uno.

**Ordinamento inventario — confronto**

| | Inventory Essentials | Client Sort | Inventory Profiles Next |
|---|---|---|---|
| NeoForge 1.21.1 | 21.1.20 (02/10/2026) | 3.89.2 (26/09/2026) | 2.2.5 (25/03/2026) |
| Licenza | ARR (sorgente visibile) | Apache-2.0 | AGPL-3.0 |
| Sviluppo | Molto attivo | Molto attivo | Ramo 1.21.1 fermo da marzo |
| Dipendenze | Balm (già presente) | Cloth Config | Kotlin for Forge + libIPN |
| Come si ordina | Click centrale | Pulsanti + click centrale | Pulsanti + tasto R |
| Ricarica attrezzi e stack | Sì | No | Sì (anche armature) |
| Slot bloccati / set di equipaggiamento | No (hotbar e armatura mai toccate) | Slot ignorati per contenitore | Sì / sì |
| Note | Stesso autore di Crafting Tweaks; disattivare `enableShiftDrag` (doppione di Mouse Tweaks) | Default già pensati per toolbox di Create, terminali di Tom's, Traveler's Backpack | La più completa ma la più macchinosa; da verificare con le versioni recenti di Kotlin for Forge |

Consiglio: **Inventory Essentials** (leggera, zero config, ricarica gli attrezzi, aggiornata spesso). Se conta più la licenza: **Client Sort** (open source, pulsanti visibili, ma niente ricarica). IPN solo se servono slot bloccati e set di equipaggiamento. Uno solo: usano tutti il click centrale. Sophisticated Backpacks ha già un suo ordinamento interno.

**Esito (16/10/2026)**: approvati il doppio zaino (Sophisticated + Traveler's) e Inventory Essentials → sezione 4.

### 5.10 Magia — mappa e proposte (16/10/2026)

✅ **Approvate**: **Ars Nouveau** con 8 addon e **Artifacts**; poi **Occultism** (+ Ars Ocultas, Occult Delight), **Reactive Alchemy**, **Psi**, **Scriptor Magicae** (→ 4.18). ⛔ Ars Technica (→ 6.11). ⭐ **Malum: la più papabile per il futuro** (scelta dell'utente), da rivalutare all'uscita della 1.9 (oggi ferma da 10 mesi, la 1.9 toglie alcuni blocchi: meglio entrare in un mondo nuovo). Ancora da decidere: Nature's Aura, Iron's Spells (doppione di Ars), Wisp & Willow, Starbunclemania, addon di Psi (Magical Psi: Revival, PsiTweaks).

**Addon di Ars Nouveau e Artifacts — proposte (16/10/2026)** · ✅ approvati tutti tranne Ars Technica ⛔ e Starbunclemania (non decisa)

| Addon | Versione · licenza | Cosa fa | Utilità nel pack |
|---|---|---|---|
| ✅ **Ars Delight** (Flavors & Delight) | 2.2.5 (6/10/2026) · LGPL-2.1 | 49+ cibi con ingredienti di Ars per Farmer's Delight | ⭐ Alta: entra nel filone FD |
| ✅ **Ars Creo** | 5.4.0 (24/5/2026) · stesso autore di Ars | Torrette di incantesimi sui contraption di Create, ruota degli Starbuncle (energia rotazionale) | ⭐ Alta: ponte con Create |
| ⛔ ~~**Ars Technica**~~ | 2.7.6 (18/2/2026) · GPL/LGPL · solo CurseForge | Glifi a tema Create (pressa, frullino, imballaggio), Source Motor. Segnalata funzionante con Ars 5.13.3 e Create 6.0.10 | ⭐ Alta/media: completa Ars Creo |
| ✅ **Ars Mekanica** | 1.3.0 (27/7/2026) · LGPL-2.1 | Source Dynamo (energia magica → FE), legno di Ars nella segheria di Mekanism | Media: ponte con Mekanism |
| ✅ **Ars Elemental** | 0.7.10.4 (4/10/2026) · LGPL-3.0 · solo CurseForge | Il grande addon di contenuti: glifi elementali, foci, armature, braccialetti (slot Curios propri, nessun conflitto) | Media/alta: più profondità magica |
| ✅ **Ars QOL** | 1.2.1 (5/10/2026) · MIT | Slot Curios per il libro degli incantesimi con tasto rapido | Media: comodo, ma progetto piccolo e nuovo |
| ✅ **Ars Unification** | 1.2.19 · LGPL-3.0 | I glifi Frantuma/Taglia usano le ricette di Mekanism e del tagliere di FD; va d'accordo con AlmostUnified | Media: integrazione fine |
| ✅ **Not Enough Glyphs** | 4.6.x · LGPL-3.0 | Glifi extra e SpellBinder (sostituisce Too Many Glyphs) | Media/bassa |
| ✅ **Ars Controle** | 1.6.16 (10/9/2026) · LGPL-3.0 | Prisma di teletrasporto, collegamenti di scrutamento, filtri | Media/bassa |
| **Starbunclemania** | 1.5.9 (24/9/2026) · licenza non dichiarata · solo CurseForge | Starbuncle che trasportano fluidi, energia e gas | Bassa: doppione dei tubi (Pipez) |

Scartati: **Create Ars Nouveau** (doppione di Ars Technica e Ars Creo) · **Ars Additions** (ferma su Ars 5.11) · **Ars Elixirum** (doppione di Aspect Alchemy e HerbalBrews) · **Too Many Glyphs, Ars Omega, Ars Instrumentum, Ars Scalaes** (niente 1.21.1) · **Ars Ocultas, Ars 'n Spells, Ars Energistique, Reliquified Ars** (le mod base non sono nel pack). Nessun addon trovato per Ars ↔ Apotheosis, Hexalia/Hexerei, Twilight o Aether.

**Artifacts**: nessun addon necessario. Scartati **Artifacts crafting** e **Artifacts Merging** (tolgono il senso dell'esplorazione); **Compat Artifacts** (100+ artefatti a tema Ars, Create, FD, boss…) è curioso ma ha licenza mista e nessun codice pubblico. Il bottino nelle strutture modded è nel datapack del pack (3.3 e 3.4).

**Cosa c'è già**: stregoneria e erboristeria popolare (Hexalia, Hexerei), pozioni e alchimia (Aspect Alchemy, HerbalBrews, alambicco vanilla, Mixing Cauldron di Hexerei), incantamenti (Apotheosis + Create: Enchantment Industry).
**Cosa manca**: incantesimi da lanciare, energia magica del mondo, magia "tecnologica" collegata a Create/Mekanism, oggetti magici da trovare esplorando, un lato oscuro/occulto.

Tutti i candidati sotto hanno una build NeoForge 1.21.1 ufficiale e, se usano una libreria accessori, usano **Curios** (già presente).

**Proposta consigliata — "strega verde" estesa**

| Mod | Versione · licenza | Cosa porta | Sovrapposizione col pack |
|---|---|---|---|
| **Ars Nouveau** | 5.13.3 (3/10/2026) · codice LGPL-3.0, grafica ARR · molto attiva | Incantesimi componibili (forma + effetti + potenziamenti), tono naturalistico: fonti di energia alimentate anche dalla crescita delle colture, famigli, rituali. Progressione lunga | Bassa (4/5) |
| ↳ **Ars Nouveau's Flavors & Delight** | 2.2.5 (6/10/2026) · LGPL-2.1 | 49+ cibi e meccaniche Ars per Farmer's Delight | — |
| ↳ **Ars Creo** | 5.4.0 (24/5/2026) · ARR · dello sviluppatore di Ars | Ars ↔ Create: Starbuncle e rituali sui contraption, energia magica dalla rotazione (Create 6.0.9+) | — |
| ↳ **Ars Mekanica** | lug. 2026 · LGPL-2.1 | Ars ↔ Mekanism: Source Dynamo (energia magica → FE), segheria Mekanism per il legno di Ars | — |
| **Nature's Aura** | 41.10 (4/9/2026) · MIT · attiva | Energia naturale in ogni chunk: alberi e fiori la producono, macchine e rituali la consumano; se la sfrutti troppo la terra si ammala. Compatta. Già "in valutazione" | Media (3/5): qualche rituale simile a Hexalia |
| **Artifacts** | 13.2.5 (2/9/2026) · MIT · attiva | Ninnoli magici da trovare (accampamenti, mimic, casse). Supporta sia Curios sia Accessories | Nessuna: Apotheosis non mette affissi sugli accessori |

**Alternative e aggiunte di gusto**
- **Iron's Spells 'n Spellbooks** (3.16.3, ARR, permesso nei modpack): incantesimi da combattimento in stile RPG, 2 boss e strutture, compatibilità Apotheosis già integrata; addon FD **Farmer's Spell 'n Spell Book** (MIT). Più pesante. **In alternativa ad Ars, non insieme** (salvo il ponte Ars 'n Spells)
- ✅ **Occultism** (1.224.5, MIT, attivissima): il "lato oscuro" pratico, con spiriti evocati che fanno da magazzino e minatori; compatibile con Apothic Enchanting e Create; Botany Pots ne supporta la Datura. Addon: **Occult Delight** (pentola FD che prende ingredienti dal magazzino), **Create: Occult Engineering** (beta), **Ars Ocultas** (se c'è anche Ars). ⚠️ Il magazzino degli spiriti fa un po' da doppione di Tom's Simple Storage
- ✅ **Psi** (1.21.1-110, licenza Psi, sorgente visibile) e **Scriptor Magicae** (2.0.14, CC0): magia "programmabile" (Psi: incantesimi come circuiti; Scriptor: incantesimi scritti in una lingua da decifrare, diversa in ogni mondo)
- ✅ **Reactive Alchemy** (10.2.1, CC-BY-NC-4.0): esperimenti alchemici nel mondo, con "poteri" che reagiscono diversamente in ogni mondo. Vicina come idea ad Aspect Alchemy
- ⭐ **Malum** (1.8.2, LGPL-3.0+; papabile per il futuro): magia oscura delle anime, profonda, già compatibile con FD e Create; rilasci rari, effetti grafici pesanti
- **Wisp & Willow** (1.3.3, CC-BY-4.0): spiriti della natura, piccola e senza sorgente pubblico

**Da tenere d'occhio**: **Botania** (port ufficiale 1.21.1 in corso, nessuna release; esiste solo "Botania Revived", non ufficiale) · **Roots 4** (tema perfetto, ma alpha) · **Hex Casting** (ufficiale solo per 1.20.1; la 0.12 per 1.21 è in sviluppo) · **Just Another Witchery Remake** (0.5.22, 4 release in 48 ore, nessun sorgente pubblico, si sovrappone a Hexerei)

**Approfondimento (16/10/2026)** — verificato su sorgenti e pagine ufficiali
- **Psi** 1.21.1-110 (1/9/2026, release, licenza Psi, sorgente pubblico): incantesimi programmati su una griglia 9×9 (selettori, operatori, vettori, condizioni), caricati su proiettili-incantesimo in un CAD assemblato a pezzi; energia Psi del giocatore; progressione dai componenti del CAD; armatura Exosuit e attrezzi in psimetallo. Richiede Patchouli. Solo JEI. ⚠️ Tasto principale **C** come "apri libro" di Ars → cambiarne uno. ⚠️ Issue aperta #853: particelle di altre mod corrotte, peggio con Sodium. Addon 1.21.1: Magical Psi: Revival (riveste Psi a tema magia), PsiTweaks (beta, integrazione Mekanism, richiede Curios). Phi fermo alla 1.19.4
- **Scriptor Magicae** 2.0.14 (17/9/2026, release, CC0): un incantesimo è una frase (soggetto + azione + descrittori) in una lingua con parole e ordine casuali per ogni mondo, da imparare con tomi antichi; si lancia scrivendolo in chat, da libri, pergamene, leggii automatici, incisioni col gesso o su oggetti all'incudine. Niente mana: costo = tempo di ricarica (addon Mana Mode per chi vuole il mana). Richiede Unfocused e **Kotlin for Forge** (già nel pack). EMI e JEI. Struttura simile ai glifi di Ars, ma gioco diverso (enigma linguistico, potenza da vanilla). Da provare: incisione all'incudine con Apothic Enchanting
- **Psi + Scriptor**: nessun conflitto noto tra loro né con Ars, Apotheosis, Curios
- **Reactive Alchemy** 10.2.1 (27/9/2026, release, CC-BY-NC-4.0, sorgente pubblico, ~1 mln download): il calderone vanilla, con una pergamena, diventa un Crogiolo; gli oggetti si sciolgono in "poteri" che reagiscono tra loro con regole mescolate in base al seme del mondo. Risultati: effetti nell'area (levitazione, fulmini, crescita, esplosioni…), trasmutazione dei metalli, 6 bastoni del potere, portale di teletrasporto. Richiede Patchouli; JEI (EMI tramite JEI). Sovrapposizione: bassa con Aspect Alchemy (solo il tema; Aspect fa pozioni vanilla da una lista fissa), nulla con Hexerei, Hexalia, HerbalBrews; media con Ars solo nei risultati (teletrasporto, gravità, cura). Riconosce già le erbe di Hexerei/Hexalia e gli oggetti di Ars come fonti di potere. Nessun conflitto di calderoni (Toil and Trouble è stata tolta)
- **Occultism vs Malum**: Occultism 1.224.5 (11/10/2026, MIT, attivissima; ramo 1.21.1 ormai solo correzioni) = spiriti evocati con rituali: lavoratori (frantumatore, fornace, taglialegna, contadino, trasportatore), magazzino dimensionale, miniera dimensionale, famigli. EMI e JEI, compat Apotheosis. ⚠️ Frantumatore fino a 6 polveri per minerale (configurabile) → scavalca Create e Mekanism; magazzino doppione di Tom's. Malum 1.8.2 (dic 2025, ultima release da 10 mesi; 1.9 in sviluppo che **toglie alcuni blocchi** → rischio aggiornando a mondo avviato; licenza ambigua: LGPL sui siti, "All Rights Reserved" nel codice): spiriti estratti dalle anime dei mob uccisi con la falce, altare di infusione, riti a totem, equipaggiamento e ninnoli, endgame oscuro. Compat FD e Create, solo JEI, effetti grafici pesanti (Lodestone). Insieme non confliggono: Occultism = automazione, Malum = combattimento
- **Integrazioni con Ars (1.21.1)**: **Ars Ocultas** 2.6.1 (6/8/2026, LGPL-3.0, mantenuta, compatibile con Ars 5.13.3 e Occultism 1.224.5): spiriti di Occultism dentro i barattoli di contenimento di Ars (lavorano in 7×7, ricevono oggetti da tubi e Starbuncle), Altare sacrificale. Ars ↔ Malum, Ars ↔ Psi, Ars ↔ Reactive: **nessun ponte** in 1.21.1
- **Addon di Occultism**: Occult Delight 1.0.0 (31/7/2026, MIT, pentola FD che pesca dal magazzino degli spiriti; una sola release) · ⛔ Create: Occult Engineering 0.13.1 (tolta; **beta**, 3/8/2026, richiede Create ≥ 6.0.8, ok con 6.0.10) · Occultism Delight (ferma da marzo 2025)

---

### 5.11 Esperienza: deposito e farm (verificato nei sorgenti, 17/10/2026)

**Già possibile senza aggiunte**
- **Create: Enchantment Industry**: esperienza liquida (1 mB = 1 punto) in qualsiasi serbatoio di Create o Mekanism, mossa con tubi e Pipez. **Experience Hatch** su un serbatoio = banca XP (click per depositare, accovacciato per prelevare, quantità da 10 a 1000 punti o "tutto"). **Experience Lantern** risucchia le sfere entro 10 blocchi (⚠️ succhia anche il giocatore che la tocca). Macina meccanica: pepite e blocchi di esperienza e gemme di Ars → liquido; Item Drain: bottiglie d'incantesimo → 10 mB; Spout: liquido → bottiglie
- **Uccisioni automatiche**: il Deployer con spada dà XP grazie a CEI (in pepite nel suo inventario); le seghe e le altre uccisioni non da giocatore non danno XP (regola vanilla)
- **Apothic Spawners**: spawner prendibili con Tocco di velluto e potenziabili (ritardo, numero, ignora giocatori, nessuna IA, controllo redstone, silenziosi, frammento di eco = XP × fino a 4). La Mega Torcia blocca solo gli spawn naturali, non gli spawner
- **Occultism**: Campo di battaglia dimensionale (rituale dell'Afrit) simula le uccisioni da un mob catturato e dà bottino + 1 bottiglia d'incantesimo ogni 10 XP
- **Ars Nouveau**: gemme dell'esperienza (3 e 12 punti, impilabili) dalla henge del Drygmy e dal Rituale di disintegrazione
- **Sophisticated Backpacks**: l'upgrade Pompa XP (con upgrade Serbatoio) accetta solo i fluidi `c:experience` (20 mB per punto) e **non** il liquido di CEI. Non unirli via tag: rapporto 1 contro 20 → guadagni o perdite di XP
- Altro: ricompense XP dei Gateways; zaino Lapis di Traveler's (15% di XP doppia); Knowledge of the Ages di Apothic Enchanting (bottino → XP, solo uccisioni del giocatore)

**Candidate (build ufficiali NeoForge 1.21.1)**
| Mod | Versione · licenza | Cosa fa | Sovrapposizione |
|---|---|---|---|
| **XP Tome** | 2.4 (ottobre 2024) · MIT | Libro che contiene 1395 punti (configurabile), portatile | Piccola |
| **Global XP** | 1.12 (agosto 2024) · MIT | Blocco banca XP quasi infinita, raccoglie le sfere vicine | Hatch + serbatoio di CEI |
| **Mob Grinding Utils** | 1.1.10 (luglio 2025) · ARR · **solo CurseForge** | Kit classico per farm: Mob Masher (conta come giocatore), tramoggia che assorbe XP, serbatoi, rubinetto XP, spawner. Fluido `c:experience` → abilita la pompa XP degli zaini (mantieni livello) | Deployer + CEI, Apothic Spawners |
| **Cognition** (ex Experience Obelisk) | 2.4.13 (luglio 2026) · MIT | Obelisco da ~1000 livelli + molto altro | CEI; tanti contenuti estranei |
| **Bottle Your Xp** | 3.6 · ARR | Imbottiglia XP col click | Lo Spout di CEI lo fa già |
| **Easy Mob Farm** | 11.0.0 · MIT | Blocchi farm da mob catturati, XP solo come bottiglie (1 su 5) | Campo di battaglia di Occultism |

Escluse: Ender IO (solo beta), Cyclic (enorme, contenuti estranei).
✅ **XP Tome** approvato il 17/10/2026 (→ 4.19). Il resto non serve. Mob Grinding Utils solo se si vuole la pompa "mantieni livello" degli zaini.

### 5.12 Secondo confronto con i modpack (17/10/2026)

Pack analizzati: **grandi 1.21.1 NeoForge** (ATM10, Better MC 5, Craftoria, All of Create Aeronautics, Create Chronicles, FTB Evolution, Farmopolis) e **a tema** cozy/stregoneria/avventura (Society: Sunlit Valley, Farming Experience, Farming Crossing 5/6, Cottage Witch, CottageCore Dream Life, Homestead, Mayview, Create: Perfect World, WitchHazel, MMC5, Prominence II). Tutte le candidate hanno una build NeoForge 1.21.1 verificata.

**Piccole e utili (nessuna sovrapposizione)** — ✅ tutte approvate il 17/10/2026 (→ 4.20)
| Mod | Dove | Versione · licenza | Cosa fa |
|---|---|---|---|
| Just Enough Breeding | 5 grandi + FE | 3.3.1 · MIT | Cibo per far accoppiare ogni animale, in EMI |
| Just Enough Professions | 4 grandi | 4.0.5 · MIT | Blocchi di lavoro dei villager, in EMI (via JEI) |
| NetherPortalFix | 7 grandi su 7 | 21.1.1 · ARR (Balm ✓) | Riporta al portale da cui sei entrato |
| AllTheLeaks | 7 grandi su 7 | 1.1.13 · MIT · **solo CurseForge** | Corregge perdite di memoria |
| SeasonHud | SSV | 2.0.10 · MIT | Mostra la stagione di Serene Seasons sotto la minimappa |
| Smarter Farmers | FE | 2.2.4 · ARR (Moonlight ✓) | I villager contadini ripiantano il seme giusto, anche modded |
| Open Together | FC5 | 21.1.2 · MPL-2.0 (Puzzles ✓) | Le porte doppie si aprono insieme |

**Contenuti a tema (da scegliere)**
| Mod | Versione · licenza | Cosa fa | Note |
|---|---|---|---|
| Farming for Blockheads | 21.1.14 · ARR (Balm ✓) | Mercato di semi e alberelli, irrigatori, fertilizzanti, nido per galline | La sua mangiatoia doppia Animal Feeding Trough. Addon Fertiliser for Blockheads per Botany Pots |
| Create Confectionery | 1.1.3.b · MIT | Cioccolato e dolci con Create | — |
| Overweight Farming | 2.2.0 · ARR | Raccolti giganti rari | — |
| Macaw's Roofs (+ Paths, Bridges, Windows) | Roofs 2.3.2 · ARR (Paths MIT) | Tetti, sentieri, ponti, finestre | Copre ciò che Handcrafted e Supplementaries non fanno |
| Every Compat | 2.11.52 · ARR (Moonlight ✓) | Varianti dei blocchi di Handcrafted, Storage Drawers, Botany Pots ecc. per i legni modded | Tanti blocchi in più, caricamento più lento |
| Diagonal Fences / Walls / Windows | MPL-2.0 (Puzzles ✓) | Recinti e muri in diagonale | Snow! Real Magic! ha già la compatibilità |
| Better Archeology | 1.3.8 · MIT | Fossili, reperti e siti di scavo | ⚠️ genera strutture → prima del mondo vero |
| Exposure | 1.9.19 · MIT | Macchine fotografiche e foto da sviluppare | — |
| Chimes | 2.1.1 · ARR | Campane a vento | — |
| Personality | 5.0.2 · Abnormals (Blueprint ✓) | Sedersi ovunque, strisciare | — |
| Small Ships / Paragliders | 2.0.2 ARR / 21.1.5 GPL-3.0 | Navi a vela / parapendio | Paragliders genera statue → prima del mondo vero |
| Goblin Traders / Guard Villagers | 1.11.2 MIT (+Framework) / 2.4.12 | Mercanti goblin / guardie dei villaggi | — |
| Autochef's Delight | 2.0.3 · ARR | Ingredienti impilati nella pentola di FD, aiuta l'automazione | — |
| Copycats+ · Create: Bells & Whistles · Create: Hypertubes | ARR · GPL · Apache | Blocchi copia di Create, accessori per treni, tubi di trasporto | Bells & Whistles: build di marzo 2025 |
| Creeper Overhaul · Variants & Ventures | ARR · CC-BY-NC-ND | Varianti dei mob | — |
| Ribbits · Aures Farmers Structures · Formations · Villages & Pillages · Vanilla Backport | — | Villaggi delle rane, strutture a tema FD, strutture, villaggi, contenuti delle versioni nuove | Il pack ha già molte strutture; ⚠️ tutte da decidere prima del mondo vero |

**Visti spesso ma non per noi**: shader (Iris), quest da scrivere (FTB Quests), mod da server, KubeJS, menu personalizzati; Cooking for Blockheads (seconda cucina), Sophisticated Storage (doppione di Tom's e Drawers), mobili alternativi (Handcrafted c'è), Aquaculture e altre pesche (alternative a Starcatcher, vedi 5.13), Relics (Artifacts), Quality Food (rompe gli stack), Just Enough Resources (EMI Loot/Ores), Loot Integrations (c'è il nostro datapack), Building/Mining Gadgets, Mystical Agriculture, suite tech. Amendments torna nei pack a tema: resta da provare con Reactive Alchemy.

### 5.13 Valutazione d'insieme delle opzionali (17/10/2026)

Legenda: 🟢 sta bene nel pack · 🟡 dipende o da provare · 🔴 poco adatta · ⏸️ non disponibile ora · ⭐ scelta per il futuro. ⚠️ = genera mondo o strutture → decidere **prima del mondo vero**.

**Cucina e bevande** (già 18 mod: entra solo ciò che copre un buco)
- 🟢 My Nether's Delight — cucina e ingredienti del Nether, oggi senza piatti
- 🟢 Chef's Delight — villager cuoco e chef che commerciano cibi FD
- 🟢 Create Confectionery — cioccolato e dolci prodotti con Create
- 🟡 Rustic Delight — peperoni, caffè, cotone e piatti rustici: carina, ma tanti ingredienti in più
- 🟡 Ocean's Delight — piatti di mare (calamari, guardiani, alghe); il pesce è già coperto da Starcatcher's Delight
- 🟡 Autochef's Delight — ingredienti impilati nella pentola FD; Create: Central Kitchen automatizza già
- 🔴 End's Delight — doppione di Ender's Delight
- 🔴 Corn Delight — il mais c'è già (Cultural Delights)
- 🔴 Seed Delight — ultima build settembre 2024
- ⏸️ Aquaculture Delight — messa da parte con Aquaculture (vedi "Pesca" sotto)
- ⏸️ Cocktails Delight, Bountiful Harvest, Delightful — non trovate per 1.21.1 su Modrinth

**Agricoltura e Botany Pots**
- 🟢 BotanyCompatLayer — datapack: colture di Aether e mod Let's Do nei vasi; va con Paxi; controllare cosa copre già Botany Pots
- 🟡 Farming for Blockheads — mercato di semi e alberelli di tutte le mod, irrigatori, nido; mangiatoia doppione di Animal Feeding Trough
- 🟡 Overweight Farming — rare colture giganti, decorative
- 🔴 Botany Pots Ore Planting — minerali dai vasi: scavalca Create e Mekanism

**Magia** (già 16 mod: saturo)
- ⭐ Malum — magia oscura delle anime; aspettare la 1.9 e un mondo nuovo
- 🟡 Nature's Aura — in tema "strega verde", ma sarebbe il settimo sistema magico
- 🟡 Magical Psi: Revival · PsiTweaks — solo se Psi piace dopo la prova (PsiTweaks beta)
- 🟡 Wisp & Willow — spiriti della natura, piccola, senza sorgente pubblico
- 🔴 Starbunclemania — doppione di Pipez, solo CurseForge
- 🔴 Iron's Spells 'n Spellbooks — doppione di Ars
- 🔴 Just Another Witchery Remake — WIP, rompe i mondi, doppione di Hexerei
- ⏸️ Botania, Roots 4, Hex Casting — nessuna release ufficiale stabile per 1.21.1

**Tech e trasporti**
- 🟢 Copycats+ — blocchi "copia" di Create; Create: Connected ha già la compatibilità
- 🟡 Create Aeronautics **oppure** Immersive Aircraft — aeronavi Create (spettacolare, pesante) / aerei semplici
- 🟡 Small Ships — navi a vela
- 🟡 Paragliders ⚠️ — parapendio con stamina, genera statue
- 🟡 Create Contraption Terminals — terminali di Tom's su treni e contraption, nicchia
- 🟡 Create: Hypertubes — tubi che trasportano il giocatore
- 🟡 Create: Bells & Whistles — accessori per treni, build ferma a marzo 2025
- 🔴 BBL Routers — doppione di Pipez e Mekanism

**Equipaggiamento e combattimento**
- 🟡 Better Combat (+ Apothic Combat) — combo e animazioni stile Dungeons, Miapi lo supporta; cambia molto il gioco, da provare
- 🟡 Truly Modular: Next Level — attrezzi che salgono di livello; solo su GitHub
- 🔴 Apotheotic Creations — nicchia, poco scaricata
- 🔴 Mekanism Tools — doppione di Truly Modular

**Strutture** (già 17 mod: tutte ⚠️)
- 🟢 Moog's Nether Structures — il Nether oggi è spoglio; stesso autore delle End Structures
- 🟢 Aures Farmers Structures — strutture a tema Farmer's Delight
- 🟢 Better Archeology — fossili, reperti, siti di scavo
- 🟡 Ribbits — villaggi di rane nelle paludi
- 🟡 WDA: Seven Seas — navi e strutture in mare; ha senso con Small Ships
- 🟡 Structory — rovine d'atmosfera, leggere
- 🟡 Formations — piccole strutture sparse
- 🟡 Explorify **oppure** Moog's Voyager — strutture riempitive, una sola
- 🟡 YUNG's Better Caves — grotte rifatte, da provare con Regions Unexplored
- 🔴 Villages & Pillages — sovrapposta a Towns and Towers
- 🔴 Repurposed Structures — solo al posto di Towns and Towers

**Dimensioni** (già 7)
- 🟡 Eternal Starlight — dimensione con boss, curata ma grande
- 🟡 The Bumblezone — dimensione delle api, piccola
- 🟡 Nether Depths Upgrade — pesci e fondali dei mari di lava; verificare con Starcatcher
- 🔴 End Remastered — stravolge la strada verso l'End
- 🔴 Create: Northstar Redux — beta

**Boss, nemici e animali** (già 9)
- 🟢 Aquamirae — boss e mob degli oceani ghiacciati, zona oggi vuota
- 🟢 Creeper Overhaul — creeper diversi per bioma
- 🟢 Naturalist · Critters and Companions — animali selvatici d'atmosfera
- 🟡 Legendary Monsters **oppure** Bosses'Rise — tanti boss sparsi, uno solo
- 🟡 Bosses of Mass Destruction — 4 boss, port non ufficiale
- 🟡 Variants & Ventures — varianti dei mob, licenza restrittiva
- 🟡 Enhanced AI — mob più furbi, se serve difficoltà
- 🔴 Alex's Mobs Continued (+ Delight) — enorme, port non ufficiale, sovrapposta a Mowzie e Born in Chaos
- 🔴 It Takes a Pillage — doppione di Illager Invasion
- 🔴 Wither's Wrath — Cataclysm copre già il fine gioco
- 🔴 In Control! — regole di spawn da scrivere a mano

**Mondo e biomi** (tutte ⚠️)
- 🟡 Tectonic — rilievi spettacolari, da provare con Regions Unexplored
- 🟡 YUNG's Cave Biomes — biomi di grotta; RU ne ha già
- 🔴 Geophilic — pensata per BWG
- 🔴 Vanilla Backport — contenuti delle versioni successive, rischi con RU

**Decorazione e costruzione**
- 🟢 Macaw's Roofs (+ Paths, Bridges, Windows) — completa Handcrafted e Supplementaries
- 🟢 Diagonal Fences / Walls / Windows — Snow! Real Magic! li supporta
- 🟢 Chimes — campane a vento
- 🟢 Exposure — fotografia con camera oscura
- 🟡 Every Compat — varianti per tutti i legni modded; molti blocchi, avvio più lento
- 🟡 Amendments — rifiniture a Supplementaries e vanilla; da provare con Reactive Alchemy

**Pesca — alternativa a Starcatcher** (messa da parte il 17/10/2026; nel pack resta Starcatcher)
- ⏸️ **Aquaculture 2** — ARR, build NeoForge 1.21.1 (giugno 2026): oltre 30 pesci legati al bioma (nuotano anche nel mondo), canne con amo, esca, lenza e galleggiante, cassetta degli attrezzi, filetti, attrezzi e armatura in Neptunium dal bottino di pesca. Doppione di Starcatcher, non insieme
- ⏸️ Espansioni: **Aquaculture Delight** (FD, ultima build febbraio 2025), **Aquaculture 2: Lava Fishing Addon** (pesca nella lava), **Aquacompat** (patch: semi modded su terra bagnata, taglio dei pesci, bonus dei coltelli)

**Villager e comodità**
- 🟢 Goblin Traders — mercanti goblin rari
- 🟡 Guard Villagers — guardie nei villaggi, meno sfida
- 🟡 Personality — sedersi ovunque, strisciare

**Esperienza**: già deciso (5.11), le altre non servono.

## 6. Mod scartate ⛔ (per tema)

### 6.1 Cucina e bevande

| Mod | Motivo |
|---|---|
| Farmer's Respite (Unofficial Port) | Port non ufficiale, non convince |
| Respiteful | Esiste solo fino alla 1.20.1 |

### 6.2 Botany Pots

| Mod | Motivo |
|---|---|
| Botany Pots – Mystical Agriculture Compat | Serve solo con Mystical Agriculture (non nel pack) |
| Datapack "Rich Soil compat", "More Crop Compatibility", "Botany Trees x Farmer's Expanded" | Testati su Fabric, dipendono da Farmer's Delight Refabricated |
| "Botany Pots with more recipes" (Go Eevee) | Fork della mod originale orientato a Cobblemon: rischio conflitto |
| "Botany Pots Trees" (datapack) | Solo alberi vanilla, ridondante con Botany Trees |

### 6.3 Tech, storage e trasporto

| Mod | Motivo |
|---|---|
| Powah! (Rearchitected) | Scelto Mekanism Generators |
| Oritech | Sovrapposta a Mekanism |
| Thermal Series | Port 1.21.1 incerto |
| Ender IO 8.1 (beta) | Tech mod intera sovrapposta a Mekanism; non risolve la pompa |
| Applied Energistics 2 / Refined Storage | Per ora: più complessi, Tom's copre lo stesso bisogno |
| EnderTanks | Non necessaria, Ender Storage copre |
| Ranged Pumps (port 1.21.1) | Port non ufficiale di provenienza dubbia |
| SourceBlock, Small Progressions | Non necessari: la lava la copre Create |

### 6.4 Equipaggiamento

| Mod | Motivo |
|---|---|
| Tetra | ARR; release recenti solo per 1.20.1 |
| Tinkers' Construct | Ufficiale fermo alla 1.20.1; sulla 1.21.1 solo un port non ufficiale |
| Create: Truly Modular | Solo 1.20.1 Forge/Fabric |
| Truly Modular x Epic Fight (Unofficial) | Serve Epic Fight (non nel pack) |
| Back Weapon Slot MI, TFC Modular | Solo Forge / pensate per TerraFirmaCraft |

### 6.5 Strutture

| Mod | Motivo |
|---|---|
| Dungeons Enhanced, Dungeons Plus | Nessuna build 1.21.1 |
| Integrated Dungeons Arise | In conflitto con When Dungeons Arise e vieta le mod di spacing |
| Integrated Dungeons and Structures, Integrated Villages | Richiedono Quark + Supplementaries + Amendments; Integrated Villages disattiva i villaggi vanilla |
| Overhaul di Dungeons and Taverns | Doppioni di YUNG's |
| Structure Essentials | Fa anche spacing e anti-sovrapposizione: ne basta una (Sparse Structures) |
| Più di due mod di villaggi / più di una mod di spacing | Mondo affollato e conflitti |

### 6.6 Dimensioni

| Mod | Motivo |
|---|---|
| Aether Redux, Lost Aether Content, Blue Skies, The Midnight | Nessuna build 1.21.1 |
| Aether Villages | Beta abbandonata |
| Ad Astra, Stellaris | Si sovrappongono a Mekanism |
| BetterEnd, BetterNether | Solo port non ufficiali "New Dawn" |
| Incendium | Ancora in alpha |
| Nullscape | Ridondante con Unusual End |

### 6.7 Boss e nemici

| Mod | Motivo |
|---|---|
| Ice and Fire CE | Non ufficiale, pesante, beta instabile |
| Mutant More, Dungeons Mobs | Nessuna build 1.21.1 |
| Improved Mobs | Si somma ad Apotheosis; mob che rompono blocchi e rubano oggetti |
| The Graveyard (port), Grim & Bleak | Si sovrappongono a Born in Chaos; di The Graveyard esistono solo port non ufficiali |
| Goety | Si sovrappone a Hexalia e Hexerei |
| Alex's Caves | Fuori tema come mod di nemici; da riconsiderare solo come mod di esplorazione |

### 6.8 Villager

| Mod | Motivo |
|---|---|
| Trade Refresh, Traderoller, Easy Trades | Non necessarie: coperte da Easy Villagers + Easy Auto Cycler |

### 6.9 Utilità, interfaccia e performance

| Mod | Motivo |
|---|---|
| Lootr | Pensata per il multiplayer |
| Create: Wrench Multitools | Solo per Create |
| Wrenched | Alpha; cicla gli stati dei blocchi, non è una wrench multi-mod |
| TooManyRecipeViewers | Non necessaria con EMI + JEI |
| JourneyMap | Valida, ma basta una mappa (Xaero's) |
| Shader (Iris…) | Scelta dell'utente. Se un giorno servissero: Iris ≥ 1.8.13 + una sola tra Colorwheel e Iris Flywheel Compat per i contraption di Create |
| Embeddium | Non serve più: Sodium esce ufficialmente per NeoForge |

### 6.10 Dal confronto con i modpack famosi (16/10/2026)

| Mod | Motivo |
|---|---|
| FTB Ultimine, Create Ultimine, Veinminer | Scavare un'intera vena in un colpo non piace |
| Toil and Trouble | Era la mod più vicina a Hexerei: il Mixing Cauldron di Hexerei, se scaldato, fa già le pozioni dell'alambicco. Si perdono solo le pozioni senza combustibile nel calderone vanilla e i calderoni di latte, miele e slime; via anche la libreria MRU e l'unica modifica al calderone vanilla |
| Let's Do EMI Compat | Nata per chi usa EMI senza JEI; nel pack JEI c'è e Vinery e Farm & Charm hanno plugin EMI nativi → creerebbe categorie doppie |
| Dynamic Surroundings | Doppione di AmbientSounds, con un riverbero che si sovrappone a Sound Physics |
| Inventory Tweaks Refoxed | Fermo da metà 2025, bug aperto con Sophisticated Backpacks |
| Client Sort, Inventory Profiles Next | Scelta Inventory Essentials (Client Sort non rimpiazza gli attrezzi; IPN macchinoso e fermo da marzo su 1.21.1) |
| Backpacked | Sviluppo lento, molte issue aperte, morte gestita solo con YIGD |
| Sodium Dynamic Lights | Port non ufficiale di LambDynamicLights, fermo a gennaio 2025 → sostituito dall'originale |
| Enhanced Celestials 2 (Core + Default Lunar Events) | Riscrittura divisa in libreria + addon, molto meno diffusa; scelta la mod originale |
| FTB Quests | Bisognerebbe scriversi le quest da soli |
| FTB Chunks | Doppione di Xaero's e Chunk Loaders |
| Corpse | Doppione di Corail Tombstone |
| Create: Steam 'n' Rails | Su 1.21.1 esistono solo port non ufficiali |
| Create: New Age | Doppione dell'elettricità di Crafts & Additions |
| Mystical Agriculture, Productive Bees/Trees | Doppioni di Botany Pots |
| Pam's HarvestCraft 2 | Doppione di Farmer's Delight |
| ChoiceTheorem's Overhauled Village | Doppione di Towns and Towers |
| Immersive Engineering, Industrial Foregoing, PneumaticCraft, Draconic Evolution… | Altre tech suite, fuori tema |
| MineColonies | Sistema enorme, fuori tema |
| Visuality / Particular / Wakes Reforged e mod Fabric via Sinytra Connector | Port non ufficiali o solo Fabric |
| Mod solo multiplayer (Simple Voice Chat, Open Parties and Claims, mod di chat…) | Gioco single player |

### 6.11 Magia (16/10/2026)

| Mod | Motivo |
|---|---|
| Blood Magic, Embers | Nessuna build ufficiale 1.21.1 (solo port o riscritture di terzi) |
| Eidolon: Repraised | Port non ufficiale (lo dichiara); crogiolo e bracieri ricalcano Hexalia |
| Enchanted: Witchcraft | Remake di Witchery: doppione di Hexerei e Hexalia |
| Enigmatic Legacy+ | Port di terzi "non ufficialmente autorizzato" |
| Theurgy | Duplica i minerali, come già fa Mekanism |
| Forbidden & Arcanus | Sviluppo spostato su 26.1, ramo 1.21.1 fermo da agosto 2025 |
| Glimmering Tales | Ferma da 18 mesi |
| Mekanism Magic | Troppo giovane |
| Ars Technica | Non piace all'utente (glifi a tema Create); il ponte con Create resta Ars Creo |
| Create: Occult Engineering | Tolta dall'utente (beta; automazione di Occultism con Create) |

---

## 7. Log decisioni

- **14/10/2026** — Scelti MC 1.21.1 + NeoForge + Prism Launcher. Confermati Farmer's Delight (+ addon) e Botany Pots. Tech, strutture e dimensioni in fase di proposta.
- **14/10/2026** — Tech confermata: Create + Crafts & Additions + Mekanism con **Mekanism Generators** + Pipez (Powah scartata). Gioco **single player**. Botany Pots: confermati Botany Trees e Botany Pots Tiers; BotanyPotsAdditions e BotanyCompatLayer opzionali. Aggiunto **Farmer's Respite** (port 1.21.1) per i tè.
- **14/10/2026** — **Farmer's Respite scartato** (il port non ufficiale non convince). Alternative per i tè: HerbalBrews (consigliata), Roaster's Delight (nuova, da tenere d'occhio), Delightful Fares.
- **14/10/2026** — Piacciono HerbalBrews e Roaster's Delight. Verificate le licenze: solo HerbalBrews ha il codice open source (MIT, asset ARR); Roaster's Delight e Delightful Fares sono ARR. Nell'ecosistema FD sono MIT anche Farmer's Delight e Brewin' And Chewin'.
- **16/10/2026** — Tè: confermate **entrambe** (HerbalBrews + Roaster's Delight). Armi: Tetra scartata (ARR, niente 1.21.1); proposta **Truly Modular** (Miapi + Arsenal/Archery/Armory), licenza PolyForm Shield. Tinkers' Construct scartato (solo port non ufficiale su 1.21.1).
- **16/10/2026** — Confermati Truly Modular + **Arsenal, Archery e Armory**. Mappato l'ecosistema Miapi: addon di terze parti pochi e per lo più non per NeoForge 1.21.1; interessanti Better Combat (compat dedicata, opzionale) e il Material Helper.
- **16/10/2026** — Approvati **Apotheosis** (8.7.x, con moduli Apothic) e il **Material Helper**. In osservazione: Better Combat e Next Level.
- **16/10/2026** — Nuovo filone **natura, erbe, tè, decotti e pozioni** (grande interesse). Proposte: Hexalia, Toil and Trouble, Nature's Aura (tutte MIT), Let's Do Vinery/Meadow/Farm & Charm, Serene Seasons, Bountiful Fares; alternative Hexerei e Aspect Alchemy; Witchery Remake in osservazione.
- **16/10/2026** — Approvati **Hexalia, Hexerei, Toil and Trouble, Let's Do Vinery/Meadow/Farm & Charm, Serene Seasons**. In valutazione: Witchery Remake e Nature's Aura. Bountiful Fares e Aspect Alchemy ancora da decidere.
- **16/10/2026** — Approvati anche **Bountiful Fares** e **Aspect Alchemy** (MIT).
- **16/10/2026** — Approvato **Delightful Fares** (ponte FD ↔ Bountiful Fares).
- **16/10/2026** — Nuovo tema: semplificare le farm di villager / reroll dei bibliotecari. Proposte Easy Villagers + Easy Auto Cycler; alternative Trade Refresh e Traderoller. Notato che Apotheosis (biblioteca + tavolo a statistiche) riduce già il bisogno di bibliotecari.
- **16/10/2026** — Approvati **Easy Villagers + Easy Auto Cycler**; Trade Refresh, Traderoller ed Easy Trades non necessari.
- **16/10/2026** — RAM del PC: 32 GB (→ 8 GB all'istanza). Storage: confermato **Storage Drawers**; proposto **Tom's Simple Storage** (probabile mod "con i beacon" ricordata dall'utente); AE2/RS accantonati.
- **16/10/2026** — Approvati **Tom's Simple Storage** (accanto a Storage Drawers) e **BotanyPotsAdditions** (da testare subito).
- **16/10/2026** — Nuovi temi: chunk loader (proposta Chunk Loaders di SuperMartijn642), morte (Corail Tombstone), lava farm (Hose Pulley di Create, senza mod extra).
- **16/10/2026** — Approvati **Chunk Loaders**, **Corail Tombstone** ed **Ender Storage**. Lava: Hose Pulley nel Nether → Ender Tank → base → Pipez. EnderTanks, Ender IO e Ranged Pumps scartati.
- **16/10/2026** — Compatibilità: approvati **Akashic Tome** (libro unico) e **OmniTools** (wrench universale per Create e Mekanism).
- **16/10/2026** — Base tecnica: proposta aggiornata (EMI+JEI, Jade, AppleSkin, Polymorph, stack performance con Sodium 0.8.12/Lithium/FerriteCore/ModernFix/ImmediatelyFast/Entity Culling, shader opzionali, mappa da scegliere).
- **16/10/2026** — Base tecnica approvata. **Niente shader.** Mappa: **Xaero's Minimap + World Map** (JourneyMap scartata).
- **16/10/2026** — Aggiunti **Waystones** e l'addon di compatibilità Xaero ↔ Waystones.
- **16/10/2026** — Ricerca su strutture, dimensioni, boss e nemici: proposte core/opzionali/scartate. Scoperto che il crash Miapi ↔ Accessories riguarda anche Hexalia; workaround Forgified Fabric API da testare.
- **16/10/2026** — Approvati **core e utility** di strutture, dimensioni e boss/nemici (Aether + Deep Aether + Aether's Delight condizionati al test Miapi/Accessories); aggiunta **Forgified Fabric API** come fix da testare. Opzionali in osservazione, scartate con motivo. Documento riorganizzato: lista mod → da fare/controllare → approvate / opzionali / scartate per tema.
- **16/10/2026** — Verificata nel codice la causa del crash: Accessories 1.1.0-beta.53 chiama Fabric Loader da codice comune. **Forgified Fabric API** consigliata a prescindere (fornisce la classe mancante); il test in 3.2 resta per conferma.
- **16/10/2026** — **Forgified Fabric API approvata**: fissa nel pack, a prescindere da Truly Modular.
- **16/10/2026** — Confronto con 8 modpack 1.21.1 famosi (ATM10, Craftoria, FTB Evolution, StoneBlock 4, All of Create, Create Chronicles, BMC5, Fresh & Smooth). Proposte in 5.9 (comodità, temi, atmosfera, grandi aggiunte), scartate in 6.10. Nessun doppione di metalli.
- **16/10/2026** — Approvati: **AlmostUnified** (per sicurezza e mod future); comodità (**Mouse Tweaks, Controlling, Crafting Tweaks, Simple Backups, Torchmaster, Comforts, RightClickHarvest, FallingTree, Leaves Be Gone**); temi (**Spice of Life: Carrot Edition, Seasonal Let's Do + compat, Create: Central Kitchen, Enchantment Industry, Integrated Farming, Mekanism: Ponders, Snow! Real Magic!, EMI Loot, EMI Ores, Gateways to Eternity**); atmosfera (**Sound Physics Remastered, AmbientSounds, Subtle Effects, Particle Rain, Sodium Dynamic Lights, Enhanced Celestials, Travelers Titles, Not Enough Animations, EMF + ETF + Fresh Animations**). Su richiesta aggiunto **Carry On**. Vein mining scartato (non piace). Zaino e ordinamento: confronti in 5.9, da decidere. Grandi aggiunte rimandate.
- **16/10/2026** — Zaini: Sophisticated piace ma ha un po' stufato; l'utente valuta di tenere **sia Sophisticated sia Traveler's**. Verificate nel codice le regole degli zaini dentro zaini (5.9). Ordinamento: consigliata Inventory Essentials.
- **16/10/2026** — Approvati il **doppio zaino** (**Sophisticated Backpacks** + Create Integration per la parte tecnica, **Traveler's Backpack** per l'avventura), **Inventory Essentials** e le altre proposte: **Create: Connected, Enchantment Descriptions, Starcatcher + Starcatcher's Delight, Animal Pens, Animal Feeding Trough, Shoulder Surfing Reloaded, YUNG's Menu Tweaks, Pick Up Notifier**. Pack a circa 142 mod. Restano da decidere solo le grandi aggiunte (5.9).
- **16/10/2026** — **Verifica formale delle versioni NeoForge 1.21.1**: 148 voci, 0 senza build (✅ 119, ⚠️ 29 per beta o rami conclusi). Sostituiti Sodium Dynamic Lights → **LambDynamicLights** ed Enhanced Celestials 2 → **Enhanced Celestials** originale. Aggiornate le versioni (Sodium 0.8.13, Apotheosis 8.9.0, Miapi 2.3.9…) e fissate le release dove le ultime sono beta. Tabella completa in `verifica-versioni.md`.
- **16/10/2026** — Revisione delle sovrapposizioni (3.7). Proposti da togliere: Animal Feeding Trough, Let's Do EMI Compat, Comforts. Da valutare: Farm & Charm, Toil and Trouble, Hexerei, Slice & Dice. Aggiunte config per strutture di palude, lune di sangue e increspature della pioggia.
- **16/10/2026** — L'utente tiene **Animal Feeding Trough** e **Comforts**. Let's Do EMI Compat verificata nel codice: nata per chi usa EMI senza JEI; nel pack è superflua (JEI presente, plugin EMI nativi in Vinery e Farm & Charm) e crea categorie doppie → proposta di non installarla. Restano da valutare Farm & Charm, Toil and Trouble, Hexerei, Slice & Dice.
- **16/10/2026** — **Let's Do EMI Compat tolta** (141 mod). **Farm & Charm tenuta** come secondo orto e seconda cucina: verificato che Let's Do Addon Compat converte le ricette tra la pentola di F&C e quella di FD in entrambe le direzioni, e che le colture sono intercambiabili via tag; restano separati impasto e farina (proposto un datapack di tag). Restano da valutare Toil and Trouble, Hexerei, Slice & Dice.
- **16/10/2026** — Scrittura del datapack in pausa. Approvato **Paxi** per caricare i datapack in tutti i mondi (142 mod). Analisi approfondita dei sei calderoni (3.7): la coppia più vicina è Hexerei–Toil and Trouble; proposta di togliere Toil and Trouble e tenere Hexerei; Aspect Alchemy usa solo oggetti vanilla fissati nel codice. Valutazione dei livelli di integrazione (3.8): tag con AlmostUnified subito, ricette via datapack solo mirate, niente KubeJS per ora.
- **16/10/2026** — **Toil and Trouble tolta** (141 mod), dopo aver verificato nel codice come modifica il calderone vanilla. Il gruppo magia resta: Hexalia (progressione), Hexerei (vita da strega), Aspect Alchemy (laboratorio), HerbalBrews (tè e fiaschette).
- **16/10/2026** — Tenuta **Create Slice & Dice**. Preparati i file di configurazione (3.4): `tags.json` di AlmostUnified (farina, impasto, sale, mais, limone, formaggi intercambiabili), `sparsestructures.json5` (1.4, villaggi 1; Dungeons and Taverns di palude a 3 da completare coi nomi), datapack `matteo_tweaks` caricato da Paxi (luna di sangue 5% e ×2, super luna ×4). Decisioni dell'utente: strutture di palude di DnT tenute ma più rare; lune di sangue molto più rare.
- **16/10/2026** — Nuovo tema **magia**: mappa di cosa c'è e cosa manca, ricerca su ~30 mod per 1.21.1 (5.10). Proposta consigliata: Ars Nouveau (+ Flavors & Delight, Ars Creo, Ars Mekanica), Nature's Aura, Artifacts. Alternative: Iron's Spells (al posto di Ars), Occultism (lato oscuro), Psi o Scriptor Magicae (magia programmabile). Da tenere d'occhio: Botania, Roots 4, Hex Casting. Scartate in 6.11.
- **16/10/2026** — Approvati **Ars Nouveau** e **Artifacts** (143 mod). Ricerca addon (5.10): proposti Ars Delight, Ars Creo, Ars Technica, Ars Mekanica, Ars Elemental, Ars QOL, Ars Unification e altri minori; per Artifacts nessun addon necessario. Config: Artifacts solo su Curios (`enableAccessoriesCompat = false`). Da fare: colture di Ars in Botany Pots e bottino di Artifacts nelle strutture modded via datapack.
- **16/10/2026** — Approvati 8 addon di Ars: **Ars Delight, Ars Creo, Ars Mekanica, Ars Elemental, Ars QOL, Ars Unification, Not Enough Glyphs, Ars Controle** (151 mod). **Ars Technica scartata** (non piace). Datapack `matteo_tweaks` ampliato: 14 modificatori di bottino portano gli artefatti in 65 tabelle di casse di 10 mod di strutture e dimensioni (livello di rarità preso dalla struttura vanilla più simile; casse di scorte escluse); colture di Ars (Magebloom, Sourceberry) in Botany Pots. Da completare in gioco: tabelle di When Dungeons Arise, Dungeons and Taverns, Mowzie's Mobs, Born in Chaos, Unusual End.
- **16/10/2026** — Artefatti estesi a **152 tabelle** (15 modificatori): aggiunti When Dungeons Arise e Dungeons and Taverns (nomi da versioni precedenti trovate su GitHub) e Unusual End (sorgente 1.21.1), nuovo livello "relitto" per la nave pirata di WDA. Restano Mowzie's Mobs e Born in Chaos. Alberi di Ars: già coperti da Botany Trees; aggiunti nel datapack i frutti di archwood come colture sui tronchi (come il cacao).
- **16/10/2026** — Approfondite le opzioni di magia (5.10): Psi e Scriptor Magicae convivono (tasto C di Psi da cambiare); Reactive Alchemy quasi tutta nuova (sovrapposizione solo nei risultati con Ars); confronto Occultism vs Malum (Occultism attiva e con ponte Ars Ocultas; Malum ferma da 10 mesi, 1.9 in arrivo); nessun ponte Ars per Malum, Psi o Reactive.
- **16/10/2026** — Approvati **Occultism** con **Ars Ocultas**, **Occult Delight** e **Create: Occult Engineering** (beta), **Reactive Alchemy**, **Psi** e **Scriptor Magicae** (158 mod). Frantumatore di Occultism lasciato di default (decisione dell'utente). **Malum** non entra per ora ma resta la candidata più papabile per il futuro (attendere la 1.9).
- **16/10/2026** — **Create: Occult Engineering tolta** (157 mod). Verificato nel codice che AlmostUnified unifica le polveri del frantumatore di Occultism (escono quelle di Mekanism, l'ossidiana di Create).
- **16/10/2026** — Aggiunti 5 `README.md` dentro il datapack `matteo_tweaks` (generale, artefatti, elenco dei modificatori, lune, vasi) con esempi commentati dei file, regole per modificarli e comandi di prova.
- **16/10/2026** — Generato il pacchetto Modrinth **`modpack-matteo-0.1.0.mrpack`**: 158 mod e resource pack + 36 librerie risolte dalle dipendenze dichiarate su Modrinth, tutte con codici di controllo verificati; config e datapack inclusi. Aether incluso (scelta dell'utente: il test Miapi si fa direttamente nell'istanza). Da aggiungere a mano: 5 mod solo CurseForge.
- **17/10/2026** — Primo avvio dell'istanza (Prism 11.1.1, NeoForge 21.1.262, 198 mod comprese le 5 di CurseForge, Java 21, 8 GB, RTX 5060 Ti usata correttamente): partito in 32 s senza crash. Trovati solo problemi non bloccanti: Apotheosis non legge il tier delle armi Miapi (da testare), Accessories incorporata nell'Aether, plugin Jade di Aspect Alchemy non caricato, conflitto innocuo Lithium/ModernFix su `getTemperature`, alcune animazioni GeckoLib di Ars Nouveau/Ars Elemental, suoni e modelli mancanti (Deep Aether, Cataclysm, Born in Chaos, Aether's Delight). Il log non copre ancora datapack, tag e ricette (si caricano alla creazione del mondo).
- **17/10/2026** — Primo mondo: generato, poi "Connection lost" all'ingresso. Causa verificata nel codice: NeoForge 21.1.261+ ha cambiato `NetworkRegistry.getCodec` (un punto di uscita in più) e il mixin di owo-lib 0.12.15.5 (usata da Accessories dentro l'Aether) colpisce quello sbagliato, quindi il pacchetto `accessories:main` non si codifica. Soluzione: NeoForge **21.1.259** (≥ 21.1.229 richiesta da BotanyPotsAdditions); pacchetto rigenerato come 0.1.1. Dal log del mondo: datapack `matteo_tweaks` caricato senza errori, 19 tag di AlmostUnified applicati (`brewinandchewin:corn` non esiste nella 4.5.0: saltato, si attiverà con un aggiornamento), nessun errore su modificatori di bottino e ricette di Botany Pots. I `README.md` dentro `data/` davano "Invalid path" (maiuscole): rinominati `readme.md`. Errori di ricette delle mod (Unusual End, Let's Do Compat per Ars Delight, B&C pizza, FD melon juice) e modificatori di Veggies/Expanded/Aether's Delight: bug delle mod, non bloccanti.
- **17/10/2026** — Approvati **Regions Unexplored** (biomi; verificato nel codice che non toglie strutture, minerali né colture selvatiche e che DnT/WDA/Hexalia/FD la riconoscono), **Chunky**, **Clumps**, **Supplementaries**, **Handcrafted**, **Rechiseled** e **Construction Sticks** (164 mod; librerie nuove Lithostitched, Fusion, Moonlight). Pacchetto **0.2.0** (204 file). Regions Unexplored va aggiunta prima di creare il mondo vero.
- **17/10/2026** — Datapack: aggiunta la cassaforte del **Galeone** di Supplementaries (`supplementaries:loot/galleon/safe`, verificata nei file della struttura) al livello artefatti "avamposto dei predoni" (25%), come le navi illager di WDA. 153 tabelle. Pacchetto 0.2.1.
- **17/10/2026** — Analisi dell'esperienza (5.11): il pack ha già banca XP (Create: Enchantment Industry), farm automatiche (Deployer + Apothic Spawners, Campo di battaglia di Occultism) e gemme di Ars. Candidate: XP Tome, Global XP, Mob Grinding Utils, Cognition. Attenzione: la pompa XP degli zaini Sophisticated non usa il liquido di CEI.
- **17/10/2026** — Approvato **XP Tome** (165 mod). Pacchetto 0.2.2 (205 file).
- **17/10/2026** — Secondo confronto con 7 pack grandi 1.21.1 NeoForge e 12 pack a tema (5.12): proposte piccole (Just Enough Breeding/Professions, NetherPortalFix, AllTheLeaks, SeasonHud, Smarter Farmers, Open Together) e contenuti a tema da scegliere (Farming for Blockheads, Create Confectionery, Macaw's Roofs, Every Compat…). Segnalate quelle che generano strutture, da decidere prima del mondo vero.
- **17/10/2026** — Approvate tutte le 7 "piccole e utili" di 5.12 (→ 4.20; 172 mod). Pacchetto 0.2.3 (211 file); AllTheLeaks si aggiunge a mano da CurseForge. Le mod a tema restano da scegliere.
- **17/10/2026** — Valutazione d'insieme di tutte le opzionali per categoria (5.13); ricerca Modrinth degli addon FD della seconda ondata (5.1).
- **17/10/2026** — Approvate le 6 di cucina 🟢🟡 di 5.13: My Nether's Delight, Chef's Delight, Create Confectionery, Rustic Delight, Ocean's Delight, Autochef's Delight (verifica in corso). Aquaculture 2 e le sue espansioni messe da parte come alternativa a Starcatcher. Verificata nel codice la compatibilità di Starcatcher con la cucina (4.17).
- **17/10/2026** — Round di decisione su tutte le opzionali concluso (30 mod approvate, vedi `decisioni/2026-10-17-round-opzionali.md`). Ricerche dedicate su Nether, animali con ricette, deposito dell'esperienza e copertura dei vasi (`datapack/conoscenze.md`, `datapack/vasi-copertura.md`). Deciso: niente datapack esterni, tutto nel nostro; repository GitHub pubblico con packwiz (struttura in valutazione).
- **18/10/2026** — Creato il repository pubblico `mango-craft/mango-craft`: una cartella per versione di Minecraft, tag `1.21.1-vX.Y.Z`, nessun ramo stabile. Importata la **0.1.1** in formato packwiz (194 file da Modrinth + 5 mod CurseForge aggiunte dal workflow dedicato), release `1.21.1-v0.1.1` pubblicata (.mrpack con le sole mod Modrinth + zip dei documenti). Workflow: controllo pack, aggiunta mod CurseForge, release (avviabile a mano col tag). `AGENTS.md` per tutti gli agenti, `CLAUDE.md` che lo importa. Prossimo passo: istanza di prova in Prism collegata al tag.
- **18/10/2026** — Piano verso la **1.0.0** (3.0): una versione per tappa (0.2.3 → 0.6.x), pre-release di prova, mondo vero dalla 1.0.0. Nuovo flusso: ramo **`dev`** seguito dall'istanza di prova, `main` avanza per fast-forward solo dopo la prova, tag su `main` (niente pull request). Approvato il **tag del pesce cotto di Starcatcher** (tappa 2). Istruzioni per le mod CurseForge da scaricare a mano (Roaster's Delight) aggiunte a README e `docs/prism.md`.
- **18/10/2026** — Unione di `dev` in `main` con **merge vero** (`--no-ff`) per conservare il grafico dei rami (scelta dell'utente, al posto del fast-forward). Mod, config e datapack su `main` solo con una versione; documenti e workflow anche prima, se su `dev` non c'è una tappa in corso.
- **18/10/2026** — Tappa 0 (strumenti): workflow **Aggiungi mod Modrinth** (sceglie l'ultima release per 1.21.1 + NeoForge, aggiunge con packwiz insieme alle dipendenze), **inventario** automatico dei .jar in `data/inventario/` e **controllo dei nomi** (`check_ids.py`: dipendenze mancanti, nomi del datapack inesistenti) a ogni modifica del pack. Accesso concesso alla cartella `logs` dell'istanza dev: log di riferimento della 0.1.1 su dev senza errori nuovi (417 righe ERROR, tutte di mod note).
- **18/10/2026** — Tappa 1 su `dev` (0.2.3): 17 file da Modrinth con le stesse versioni verificate del vecchio pacchetto 0.2.3 (aggiunti dal workflow, dipendenze già complete) + AllTheLeaks 1.1.13 da CurseForge; cassaforte del Galeone nel datapack (tabella verificata nell'inventario). Controllo dei nomi: 0 errori, 15 avvisi = nomi di casse di When Dungeons Arise e Dungeons and Taverns presi da versioni vecchie che non esistono più (gli artefatti lì non compaiono mai): da correggere nella tappa 5 con i nomi veri dell'inventario. Da provare in gioco.
- **18/10/2026** — **0.2.3 provata** nell'istanza dev (mondo nuovo, 10 minuti di gioco): nessun errore nuovo nel log rispetto alla 0.1.1 (solo l'avviso di Moonlight su Forgified Fabric API, atteso). Merge in `main` e pre-release `1.21.1-v0.2.3`. Aggiunte in 3.0 le tabelle di stato per gruppi (mod, datapack e config).
- **18/10/2026** — Tappa 2 su `dev` (0.3.0): 6 mod di cucina (versioni verificate il 17/10), Farming for Blockheads 21.1.14 e Cognition 2.4.13 (ultime release), nessuna libreria nuova; pesce cotto di Starcatcher in `c:foods/cooked_fish`, `c:foods/cooked_fishes` e `bountifulfares:cooked_fishes`. Il controllo dei nomi ora verifica anche la versione di NeoForge richiesta dalle mod: 0 errori. Da provare in gioco.
