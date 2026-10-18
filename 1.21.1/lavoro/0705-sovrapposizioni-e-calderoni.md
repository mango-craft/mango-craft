# Sovrapposizioni e calderoni — revisione del 16/10/2026

> **Documento storico**: fotografia del momento in cui è stato scritto, non si aggiorna. Lo stato attuale è nei documenti vivi (vedi il README della cartella).

Revisione delle mod che si sovrappongono (verificata sui sorgenti, sui file di lingua, tag e ricette) e analisi dei sei calderoni. Gli esiti sono nelle righe delle mod (`../docs/0301-mod.md`) e tra le scartate (`0602-mod-scartate.md`).

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
  - **Restano separati**: impasto e farina (F&C usa i tag vecchi `c:dough` e `c:flour`, FD `c:foods/dough`, Create `c:flours`) → sistemabili con un piccolo datapack di tag (vedi 0302)
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
- Subtle Effects, Particle Rain, Snow! Real Magic!: unico doppione le increspature della pioggia (vedi 0302)
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

## Appendice: note della ricerca (in inglese)

**1. Slice & Dice vs Central Kitchen: KEEP BOTH (S&D is the optional one).** Not a superset. Central Kitchen (CK) converts FD cutting-board recipes to Sawing/Deploying, lets Packagers/Arms feed real Cooking Pots (plus kegs, ovens, many FD addons) with boiler-heater speedup. S&D adds the Slicer, pot recipes as heated basin mixing, and the Sprinkler (liquid fertilizer). Overlap is cutting and pot automation only. Neither source references the other; no incompatibility declared; "wet air/oven" is not an S&D feature. Create Food Factories (Modrinth) ships both. Test for duplicate recipe categories in EMI.

**2. Hexalia vs Hexerei: OPTIONAL (keep both or pick by taste).** Shared: herb jar, mortar and pestle, cauldron brewing, willow wood, swamp structures. Hexerei only: brooms, crows/owls, candles/candelabra, herb drying racks, coffers, courier/post office, covens. Hexalia only: rituals (table, brazier, salt), censer, enchanted crops, silk moths, accessory gear. Separate namespaces, no conflict found (tags unchecked). Hexerei 1.21.1 is beta 0.5.0.3 (Apr 2025), rituals "planned"; Hexalia 1.3.6 is active (Aug 2026). If only one: Hexalia for maintenance, Hexerei for broom/decor.

**3. Toil and Trouble vs Aspect Alchemy: OPTIONAL (T&T is the removable one).** T&T upgrades the vanilla cauldron to brew vanilla/modded brewing-stand recipes. Aspect Alchemy is a different system: a separate crafted Aspect Cauldron (cauldron+gold+copper), heating, hidden aspects (effect needs 2+ ingredients), multi-sip bottles. No conflict: Aspect blocks extend `Block`, no mixins, while T&T hooks only vanilla cauldron states. With Hexerei/Hexalia you have four cauldron systems. Aspect Alchemy is one release (2.0.0), no integrations.

**4. Botany Pots Tiers vs BotanyPotsAdditions: KEEP BOTH.** Different axes. Tiers: Elite/Ultra/Creative at x2/x6/x10 speed and output. Additions: double/quad slots, greenhouse (+50% yield), FE+water sprinkler pots, hopper pots. Separate blocks. Whether Additions variants stack with Tiers is unverified. Power creep is the only cost; Tiers is the easier cut.

**5. Comforts vs Traveler's Backpack bag: OPTIONAL (lean drop).** TB's bag uses vanilla bed sleep rules; `enableSleepingBagSpawnPoint` defaults false, so spawn is never set. That covers Comforts' bag. Comforts only adds hammocks (sleep through day), standalone bags, colors.

**6. Animal Pens vs Feeding Trough: KEEP Animal Pens, drop the trough.** Pens store animals as data and breed them when fed; there are no free entities to walk to a trough. The trough only helps open pastures. Last 1.21.1 build 1.1.2 is 22 Sep 2024 (confirmed).

**7. Let's Do EMI Compat: OPTIONAL (likely drop).** EMI states that with JEI installed they "share recipes". Farm & Charm, HerbalBrews, Meadow and Vinery all ship JEI+REI plugins. Vinery 1.5.5+ and Farm & Charm HEAD also ship native EMI plugins; HerbalBrews and Meadow have none. The compat mod fills EMI gaps but shows no guard against native plugins, so duplicates are possible (unverified). Remove, then check Meadow/HerbalBrews stations in EMI.

**8. Gateways to Eternity: KEEP.** Apotheosis 8.4+ has first-party integration (optional dep gateways >=5.1.0): four tiered gateways (frontier to pinnacle) plus the Endless Gateway of Apothic Invaders (wave 100 gives Sigil of Supremacy). Tier progression does not require them. They are player-summoned wave arenas, complementary to world bosses; datapack-tunable.

**9. Chunk Loaders vs Mekanism: KEEP.** Chunk Loaders: no power, 1/3x3/5x5/7x7; Basic is iron+obsidian+ender pearl (early-mid), Ultimate adds diamond and ender eye. Mekanism's Dimensional Stabilizer needs atomic alloy, Ultimate circuit, refined obsidian, diamond block; 5x5 at 5,000 J/chunk/tick (late, powered). Anchor Upgrade is cheap (infused alloy, diamond dust) but only on Digital Miner, Entangloporter, Teleporter.

**10. Storage: KEEP Tom's + Create; QIO is just Mekanism.** Tom's: chest-network terminal (mid: connector needs diamond+ender pearl). Create 6 Stock Ticker (glass+Stock Link+gold) is logistics: orders go through a Stock Keeper and arrive as physical packages, not instant. QIO: Ultimate circuit/teleportation core, late. Overlap is "request items remotely"; feel and timing differ.

**11. Mob density: no removal, tune.** No reports found for this exact stack (unverified). Biggest multiplier: Enhanced Celestials blood moon x2.25 monster cap (10%/night, 4+ nights apart; super x4.5), using biome spawns so it scales every mod. Mutant Monsters default 5% of vanilla weight. Born in Chaos escalates (night 3, night 10). Illager Invasion is structure/raid-bound; F&F spawn rules unverified. Apotheosis invaders 1.8-3.0% per spawn. Levers: EC datapack `spawn_category_multiplier`, Mutant weights, Born In Configuration/gamerules, Apotheosis `invader_spawn_rules`, Torchmaster.

**12. Witch structures: yes, overlap; fix by datapack, not removal.** Swamps: Hexerei witch hut (20/8 chunks) + dark coven (29/11), Hexalia hut (32/20, swamp), YUNG's huts (replace vanilla), D&T Witch Villa/Swamp Villages (spacing unverified). Keep YUNG's; empty D&T and Hexalia `structure_set` files; Sparse Structures also helps.

**13. Subtle Effects / Particle Rain / Snow! Real Magic!: KEEP ALL.** Only real overlap: rain water ripples (SE `rainWaterRipples`, PR ripples). SE detects Particle Rain (blocklists its mist). Snow! Real Magic! is block snow layers and accumulation, not weather particles. If ripples double, disable SE's.

**Removal ranking:** 1) Animal Feeding Trough. 2) Let's Do EMI Compat (test first). 3) Comforts. 4) Toil and Trouble. 5) Slice & Dice. 6) Hexerei or Hexalia (taste). 7) Botany Pots Tiers.

**Sources:** github.com/PssbleTrngle/SliceAndDice; github.com/DragonsPlusMinecraft/CreateCentralKitchen (1.21.1/6.0.0-dev); moddex.gg/modpack/create-food-factories-mr-um7VgdHH; github.com/GrapeStudios/Hexalia; github.com/JoeFoxe/Hexerei-1.19 (1.21.1); github.com/cassiancc/Toil-and-Trouble; github.com/NezerX/Aspect-Alchemy; curseforge.com/minecraft/mc-mods/botanypotsadditions; modrinth.com/mod/botany-pots-tiers; github.com/Tiviacz1337/Travelers-Backpack (1.21-neoforge); modrinth.com/mod/animalpens; modrinth.com/mod/animal_feeding_trough; github.com/Pandaismyname1/Let-s-Do-EMI-Compat; modrinth.com/mod/emi; github.com/Let-s-Do-Collection; github.com/Shadows-of-Fire/Apotheosis; github.com/Shadows-of-Fire/GatewaysToEternity; github.com/SuperMartijn642/ChunkLoaders (forge-1.21); github.com/mekanism/Mekanism (1.21.x); github.com/tom5454/Toms-Storage; github.com/Creators-of-Create/Create; github.com/CorgiTaco-MC/Enhanced-Celestials; github.com/Fuzss/mutantmonsters; github.com/Fuzss/illagerinvasion; modrinth.com/mod/borninchaos; modrinth.com/mod/yungs-better-witch-huts; modrinth.com/datapack/dungeons-and-taverns; github.com/MincraftEinstein/SubtleEffects; modrinth.com/mod/particle-rain; modrinth.com/mod/snow-real-magic.
