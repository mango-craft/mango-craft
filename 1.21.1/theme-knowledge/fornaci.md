# Tema: fornaci a livelli

Aggiornata il 24/10/2026 · stato: **valutazione iniziale**, nessuna decisione (idea di Matteo del 23/10: una progressione delle fornaci che non passi da Create o Mekanism, `../lavoro/0503-temi-aperti.md`) · fonti: ricerca su Modrinth (24/10); jar delle candidate letti dal workflow Esamina mod (`../../ai-agents/stage/2026-10-24_1.21.1-v0.6.3_esame-mod/`); sorgente di Jumbo Furnace (ramo `1.21.1`, commit `915c310`); inventario del pack. Schede vicine: `strumenti.md` (la stessa scala dei materiali), `piante.md` (rarità e monete del mercato).

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
| FurnaceMk2 (MIT) | una fornace migliore con un cristallo d'esperienza | — | beta, libreria in più, sorgente non pubblico | 🔴 |
| Brick Furnace (MIT) | fornaci di mattoni d'argilla, uguali alle vanilla | — | non è una progressione | — |

## Come si legherebbe al resto

Con Iron Furnaces la scala delle fornaci si scrive **nel datapack**, come i vasi e il mercato: le ricette dei livelli e dei potenziamenti si riscrivono allo stesso percorso usando una **scala dei materiali** comune agli strumenti a tappe (`strumenti.md`), e i livelli alti possono chiedere i materiali delle dimensioni già scelti per il mercato (frammenti di netherite, gravitite incantata, regalium, steeleaf…). Le velocità si fissano nella config, portata completa nel pack. Le due cose (fornaci e strumenti) condividono la stessa tabella dei materiali: conviene farle una dopo l'altra.
