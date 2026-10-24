# Tema: computer (CC: Tweaked e add-on)

Aggiornata il 25/10/2026 · stato: **ricerca iniziale**, nessuna decisione (richiesta di Matteo del 25/10: «valutare l'aggiunta per le prossime versioni») · mod coinvolte: CC: Tweaked e i suoi add-on (candidati), Create, Mekanism e le mod con inventari, liquidi o energia (già nel pack) · fonti: API di Modrinth; esame dei jar (`../../ai-agents/stage/2026-10-24_1.21.1-v0.7.2_esame-mod/`); sorgenti di CC: Tweaked, Create, Mekanism, Advanced Peripherals, UnlimitedPeripheralWorks e CC:C Bridge alle versioni esaminate (riferimenti in `../../ai-agents/stage/2026-10-25_1.21.1-v0.7.2_computercraft/fonti.md`).

## Cos'è

**CC: Tweaked** aggiunge computer programmabili in Lua: computer, monitor, tartarughe (robot che scavano, costruiscono, coltivano), computer tascabili, modem con e senza fili, stampanti, altoparlanti. Un computer legge e comanda i blocchi accanto o in rete (le «periferiche»).

## Cosa si collega già, senza add-on

- **Qualsiasi inventario, serbatoio o batteria** (metodi generici di CC: Tweaked): casse, Storage Drawers, Tom's Storage, Sophisticated, fornaci di Iron Furnaces e FurnaceMk2, vasche e serbatoi di Create, macchine di Mekanism… Si contano gli oggetti, si spostano tra inventari, si legge l'energia.
- **Create 6.0.10**, integrazione sua (19 periferiche): Display Link, misuratori di velocità e di stress, Speed Controller, Sequenced Gearshift, Creative Motor, Nixie Tube, treni (stazioni, segnali, Track Observer) e **tutta la logistica nuova**: Stock Ticker, Packager, Repackager, Frogport, Postbox, Redstone Requester, Table Cloth Shop.
- **Mekanism 10.7.19**, integrazione sua: le macchine e i multiblocchi diventano periferiche.
- **Shader**: CC: Tweaked ha un'integrazione con Iris (il testo dei monitor passa da Iris; niente monitor nell'ombra).

## Cosa porta nel mondo

- **CC: Tweaked**: i «dischi del tesoro» (programmi Lua) in 10 casse vanilla (dungeon, miniera abbandonata, roccaforte, piramide del deserto, tempio della giungla, igloo, villa, cartografo del villaggio). È bottino, non generazione: non tocca le nostre casse né la toppa delle reliquie.
- **Advanced Peripherals**: le **case del Computer Scientist** nei villaggi (5 strutture, una per tipo di villaggio) e il suo mestiere. ⚠️ Cambia la generazione: va deciso **prima del mondo vero** (si spengono con `enableVillagerStructures` in `config/Advancedperipherals/world.toml`, file COMMON che il pack può portare).
- Gli altri add-on esaminati non hanno strutture né generazione.

## Add-on valutati

| Add-on | Versione 1.21.1 | Cosa aggiunge | Con il pack | Giudizio |
|---|---|---|---|---|
| **CC: Tweaked** (CCPL) | 1.120.2, 08/2026 | la base | NeoForge [21.1.9, 21.2) ✅ | 🟢 Tutte le versioni NeoForge su Modrinth sono segnate alpha, anche quelle per i Minecraft più nuovi; 5,4 milioni di download, aggiornata |
| **CC:C Bridge** (Apache-2.0) | 1.7.3 release, 06/2026 | Source Block e Target Block (dati tra computer e Display Link di Create), Scroller Pane, RedRouter (redstone a distanza), Animatronic (pupazzo programmabile) | vuole **Create [6.0.10, 7.0)**: la nostra 6.0.10 va bene, ma blocca Create sotto la 7 | 🟢 Il ponte con Create più usato (790.000 download) |
| **Advanced Peripherals** (Apache-2.0) | 0.8.2a, **solo alpha**, 10/2026 | Player Detector, Chat Box, Environment Detector, Energy/Fluid/Gas Detector, Inventory Manager (inventario del giocatore e Curios), Geo Scanner (minerali vicini), Block Reader, NBT Storage, Distance Detector, Compass, Smart Rail; potenziamenti per tartarughe e tascabili, tartarughe «automi», occhiali smart (Curios). Ponti AE2 e Refined Storage (non nel pack) | NeoForge ≥ 21.1.238 ✅; Create (bacino, Blaze Burner, serbatoi, filtri), Mekanism ≥ 10.7.15 ✅, Curios ✅, Patchouli ≥ 1.21-88 ✅ (1.21.1-93) | 🟡 Il più completo, ma alpha e con le case nei villaggi |
| **UnlimitedPeripheralWorks** (MIT) | 1.9.2, **alpha**, 09/2026 | molte periferiche e integrazioni; contiene Peripheralium, Broccolium e Tweakium | integrazioni con mod **nostre**: Ars Nouveau (sorgente, Mob Jar), Occultism (Golden Sacrificial Bowl, magazzino), Tom's Storage, Create, EMI, Nature's Compass, KubeJS | 🟡 Interessante per collegare la magia; tre librerie nuove, in parte doppione di Advanced Peripherals |
| **Turtlematic** (MIT) | 1.4.10 release, 08/2026 | potenziamenti per le tartarughe | stesse tre librerie di UnlimitedPeripheralWorks | 🟡 Solo se si usano molto le tartarughe; ha senso insieme a UnlimitedPeripheralWorks |
| **Tom's Peripherals** (MIT) | 1.3.1 release, 05/2026 | GPU e monitor ad alta risoluzione (anche 3D, immagini PNG), tastiera, Redstone Port, watchdog | ✅ | 🟡 Per chi vuole grafica sui monitor |
| **Create: CC Better Recipes** (MIT) | 1.2.0 release, 11/2025 | 20 ricette di CC: Tweaked con materiali di Create (pressa, banco meccanico) | ✅ | 🟡 Lega i computer alla progressione di Create: da decidere con le ricette a tappe |
| **Create: CC Total Logistics** (LGPL-3.0) | 0.3.6, 06/2025 | ponte con la logistica di Create | Create [6.0.4, 6.1) | 🔴 Doppione: Create 6 ha già le periferiche della logistica; ferma da più di un anno |
| Classic Peripherals, CC: Terminals | release | periferiche varie; terminali con interfaccia | ✅ | non approfondite |

Scartati perché servono mod che non abbiamo: gli add-on per Create: Simulated / Aeronautics / Sable, Create Big Cannons, Create: Deep Seas, Power Grid, BallistiX, Modern Industrialization, Vivecraft.

## Da tenere a mente

- **Create bloccato**: CC:C Bridge vuole Create da 6.0.10 a sotto 7.0; il giro di aggiornamenti (0.8.0) deve guardarlo.
- **Alpha**: Advanced Peripherals e UnlimitedPeripheralWorks esistono solo come alpha per la 1.21.1; CC: Tweaked è segnata alpha su tutte le versioni.
- **Internet dai computer**: con l'API `http` (accesa di serie, chiave `http.enabled` della config di CC: Tweaked) i computer scaricano programmi (`wget`, `pastebin`); in single player è comodo, e si può spegnere.
- **Geo Scanner** di Advanced Peripherals: elenca i blocchi (e quindi i minerali) attorno, fino a 8 blocchi senza costo e fino a 16 con un costo, una scansione ogni 2 secondi (`SphereOperation.SCAN_BLOCKS`): un aiuto forte per l'esplorazione; si spegne con `enableGeoScanner`.
