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
