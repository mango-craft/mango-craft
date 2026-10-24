# Tema: fornaci a livelli

Aggiornata il 24/10/2026 · stato: **Iron Furnaces, FurnaceMk2 e Jumbo Furnace nel pack dalla 0.7.1** (decisioni del 24/10: tutto Iron Furnaces, ricette e valori originali; `../lavoro/versioni/v0.7.1.md`) (idea di Matteo del 23/10: una progressione delle fornaci che non passi da Create o Mekanism, `../lavoro/0503-temi-aperti.md`) · fonti: ricerca su Modrinth (24/10); jar delle candidate letti dal workflow Esamina mod (`../../ai-agents/stage/2026-10-24_1.21.1-v0.6.3_esame-mod/`); sorgente di Jumbo Furnace (ramo `1.21.1`, commit `915c310`); sorgente di FurnaceMk2 e VapourWare (scheda `../mod-knowledge/furnacemk2.md`); inventario del pack. Schede vicine: `strumenti.md` (la stessa scala dei materiali), `piante.md` (rarità e monete del mercato).

## Cosa c'è già nel pack

- **Mekanism**: fabbriche di fusione a quattro livelli (base, avanzata, élite, definitiva) e il fonditore energizzato: è già una progressione a livelli, ma tecnologica (energia), quindi fuori dall'idea.
- **Create**: la ventola con lava o fuoco fonde in blocco tutto ciò che le passa davanti, senza combustibile. Dopo Create la velocità di una fornace conta poco: le fornaci a livelli servono soprattutto **prima** di Create, o come scelta per chi non vuole macchine.
- **Fornaci per lo zaino**: Sophisticated Backpacks (fusione, altoforno e affumicatoio, anche automatici) e Traveler's Backpack (fornace e altoforno).
- **Fornaci a tema**: fornace e affumicatoio di holystone e altoforno di arkenium (Aether's Delight), fornace di cenere di Twilight Forest; i forni da cucina di Cultural Delights, Handcrafted e Hexalia.
- **Dal datapack, senza mod**: si possono cambiare solo i tempi di cottura delle singole ricette; i livelli sono blocchi e richiedono una mod.

## Le candidate (24/10/2026)

| Mod | Cosa fa | Pro | Contro | Giudizio |
|---|---|---|---|---|
| **Iron Furnaces** (Apache-2.0, 4.3.2 del 26/09/2025, nessuna dipendenza) | 9 livelli: rame, ferro, argento, oro, diamante, smeraldo, cristallo, ossidiana, netherite, più la fornace arcobaleno («million») di fine gioco; potenziamenti sul posto senza rompere il blocco; accessori (velocità, combustibile, altoforno, affumicatoio, fabbrica a più slot, generatore di energia) | la più diffusa (10 milioni di download, in All The Mods 10); **ricette di livelli e potenziamenti nel datapack** (si riscrivono con i nostri materiali, anche quelli delle dimensioni); velocità e livello di ogni fornace nella config; l'argento c'è già (Occultism) | il sorgente per la 1.21.1 non è pubblico (GitHub arriva alla 1.20.1); l'accessorio generatore produce energia (un po' tecnologico, si può togliere dalle ricette); i livelli di All The Mods si spengono da soli (condizione `mod_loaded`) | 🟢 |
| **Iron Smelters** (MIT, di Jared, l'autore di CraftTweaker e Clumps) | fornace, altoforno e affumicatoio in 5 livelli (rame, ferro, oro, diamante, ossidiana), potenziamenti sul posto | leggera, tutti e tre i tipi a livelli, ricette nel datapack | poco diffusa (26.000 download); un solo moltiplicatore di velocità per tipo nella config | 🟡 |
| **Jumbo Furnace** (MIT, solo CurseForge, in Craftoria) | multiblocco 3×3×3 fatto con 27 fornaci: cuoce molte cose **in parallelo** (fino a 65 ricette con i potenziamenti, che sono altre Jumbo Furnace), tempi di cottura delle ricette | un'altra strada: quantità, non velocità; ricette proprie nel datapack; l'oggetto potenziamento è un'etichetta (si può cambiare) | solo CurseForge | 🟡 complementare |
| Better Furnaces Reforged (MIT) | 10 livelli fino a ×200, «forge» da 3 oggetti, potenziamenti | molti potenziamenti | **beta** ferma ad aprile 2025, libreria nuova (`factory_api`); i potenziamenti di **raddoppio e quadruplicazione dei minerali** scavalcano la lavorazione di Create, Mekanism e Occultism | 🔴 |
| Compressed Furnace (MIT) | fabbriche a 3 livelli, frantumatore, generatore, versioni a energia | — | sorgente non pubblico; il frantumatore raddoppia i minerali; tecnologica | 🔴 |
| Iron Furnace: Reburn (GPL-3.0) | fork di Iron Furnaces con fornaci definite nei dati | proprio il modello «data driven» | 2.000 download, librerie proprie, molto giovane | 🔴 per ora (da rivedere se cresce) |
| **FurnaceMk2** (MIT, sorgente pubblico; scheda `../mod-knowledge/furnacemk2.md`) | una sola fornace migliore, in stile vanilla: ×2 di velocità, tre nuclei (velocità ×4, combustibile, esperienza ×2,5), riserva di combustibile che non si spreca, 4 slot di uscita, esperienza raccolta in un cristallo | la raccolta dell'esperienza e il combustibile senza sprechi; ricette e valori nel datapack e nella config; il nucleo di velocità chiede il Nether | due gradini soli, non una scala; solo ricette di fusione (niente altoforno e affumicatoio); piccola (circa 1.000 download del file 1.21.1), libreria dello stesso autore (VapourWare) | 🟡 |
| Brick Furnace (MIT) | fornaci di mattoni d'argilla, uguali alle vanilla | — | non è una progressione | — |

**Correzione del 24/10**: nella prima stesura FurnaceMk2 era scartata come «beta, sorgente non pubblico». Il sorgente è pubblico su GitHub e il file 1.21.1 è una release (è la pagina della mod a dirsi in beta): rivalutata a 🟡 dopo la lettura del sorgente.

**Iron Furnaces e FurnaceMk2.** Sono due idee diverse: Iron Furnaces è una **scala** (9 livelli, accessori), FurnaceMk2 **un gradino** fatto bene (velocità, combustibile ed esperienza, con tre nuclei). **Decisione di Matteo del 24/10: entrambe nel pack**, usate in punti diversi delle sue automazioni (Iron Smelters quindi non serve: in `0602`). Jumbo Furnace aggiunta anche lei il 24/10 («scenica e fa ridere»).

## Energia in Iron Furnaces (verificato il 24/10)

Dal codice della 1.20.1 (`Qelifern/IronFurnaces`, ramo `1.20.1` @`6e0e292`; quello della 1.21.1 non è pubblico, ma ricette e nomi della config nel jar 4.3.2 coincidono). Tre parti usano energia (FE):
- **Accessorio generatore**: la fornace smette di cuocere e produce energia bruciando combustibile; con l'accessorio altoforno brucia invece gli oggetti delle ricette `ironfurnaces:generator_blasting` (nel jar: rame e redstone 10.000 FE, ferro 20.000, oro, lapislazzuli, quarzo, ametista e prismarino 40.000, smeraldo 125.000, diamante 500.000, netherite 750.000, stella del Nether 1.000.000); con l'affumicatoio brucia cibo (durata = nutrimento × 800). Energia al tick per livello (valori di serie della 1.20.1): rame e ferro 40, argento 100, oro 160, diamante 240, smeraldo 320, cristallo 360, ossidiana 500, netherite 1.000, arcobaleno 2.000.
- **Accessorio fabbrica**: la fornace cuoce più oggetti insieme (2, 4 o 6 slot secondo il livello) **a energia** (tempo di cottura × 20 FE per oggetto).
- **Riscaldatore** (blocco `heater` + oggetto `item_heater` collegato): l'oggetto nello slot del combustibile fa andare la fornace con l'energia del blocco (2.000 FE per carica) invece che a combustibile.
- Ogni fornace ha una riserva di energia (config `energy.tier_0/1/2`: 80.000, 200.000, 1.000.000 FE).

Quindi togliere il generatore non toglie l'energia dalla mod: fabbrica e riscaldatore restano e prendono energia da fuori (Mekanism).

## Jumbo Furnace in dettaglio (sorgente, ramo `1.21.1` @`915c310`)

- Si costruisce con **27 blocchi** dell'etichetta `c:player_workstations/furnaces` in un cubo 3×3×3 (nel pack, verificato sull'inventario della 0.7.1: solo la fornace vanilla e la fornace di holystone di Aether's Delight; le fornaci di Iron Furnaces e la FurnaceMk2 **non** valgono); diventa un blocco solo.
- **9 slot di ingresso, 9 di combustibile, 9 di uscita** e uno per i potenziamenti; con tramogge e tubi.
- Cuoce **1 + il numero di potenziamenti** ricette insieme, ognuna con il suo tempo normale; il potenziamento di serie è un'altra Jumbo Furnace (etichetta `jumbofurnace:multiprocessing_upgrade`), fino a 64: **65 ricette alla volta**.
- Usa le ricette della fornace normale più ricette sue a più ingredienti (`jumbofurnace:jumbo_smelting`, scrivibili nel datapack); raccoglie l'esperienza.
- Config: solo `shearable` (smontarla con le cesoie). Solo CurseForge, MIT.
- Fa lo stesso lavoro della ventola di Create, delle fabbriche di Mekanism e della fabbrica di Iron Furnaces: la differenza è che non chiede né energia né Create.

## Come si legherebbe al resto

Con Iron Furnaces la scala delle fornaci si scrive **nel datapack**, come i vasi e il mercato: le ricette dei livelli e dei potenziamenti si riscrivono allo stesso percorso usando una **scala dei materiali** comune agli strumenti a tappe (`strumenti.md`), e i livelli alti possono chiedere i materiali delle dimensioni già scelti per il mercato (frammenti di netherite, gravitite incantata, regalium, steeleaf…). Le velocità si fissano nella config, portata completa nel pack. Le due cose (fornaci e strumenti) condividono la stessa tabella dei materiali: conviene farle una dopo l'altra.
