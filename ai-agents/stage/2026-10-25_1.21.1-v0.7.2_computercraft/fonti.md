# CC: Tweaked e add-on — fonti grezze (25/10/2026)

Ricerca chiesta da Matteo il 25/10/2026 («valutare l'aggiunta per le prossime versioni di computer craft + eventuali add on utili»). Distillato nel tema `1.21.1/theme-knowledge/computercraft.md`. Esame dei jar: `../2026-10-24_1.21.1-v0.7.2_esame-mod/` (workflow Esamina mod, run 40141955312: cc-tweaked, advancedperipherals, cccbridge, toms-peripherals, unlimitedperipheralworks, create-cc-total-logistics, classicperipherals, turtlematic, create-ccbr, cc-terminals).

## Ricerche su Modrinth (API, 25/10/2026, 1.21.1 + NeoForge)

- `query=computercraft`: 21 risultati; `query=peripheral`: 27; `query=cc tweaked`: 37. I più scaricati: cc-tweaked 5.400.923, cccbridge 790.075, advancedperipherals 390.793, toms-peripherals 233.984, cc-sable 224.043, create-ccbr 161.678, unlimitedperipheralworks 140.326, create-avionics 105.774, create-cc-total-logistics 96.922, turtlematic 38.738, classicperipherals 26.656, cc-terminals 21.072.
- Esclusi perché legati a mod non nel pack: create-avionics, cc-sable, cc-wireless-peripheral-sable, simulated-cc-compat, cc-my-peripheral-extender (Create: Simulated / Aeronautics / Sable), cc-cbc, cbcperipheral, cc-cbc-compact-mount (Create Big Cannons), cc-deep-seas, ccpowergridcompat, power-grid-dynamic-motor-w-cc, cc-ballistix-*, cc-synaxis-connector, waterframes-computercraft-compat, modern-industrialization-cc-tweaked-compat, cc-vr, cc_relinked, cc-aeroworks, ccliftlink, universal-keyboard.

## Versioni 1.21.1 NeoForge (API /v2/project/<slug>/version)

| Slug | Ultima | Tipo | Data | Dipendenze (Modrinth) |
|---|---|---|---|---|
| cc-tweaked | 1.120.2 (`1ewzHZYg`) | alpha | 2026-08-08 | — |
| advancedperipherals | 1.21.1-0.8.2a (`fxjzpAbL`) | alpha (21 versioni, nessuna release) | 2026-10-04 | cc-tweaked |
| cccbridge | 1.7.3 (`MKK6cYI5`) | release | 2026-06-11 | cc-tweaked, create; facoltativa McQoy |
| toms-peripherals | 1.21-1.3.1 (`y8svVJBV`) | release | 2026-05-17 | cc-tweaked |
| unlimitedperipheralworks | 1.21.1-1.9.2 (`l84f9GYD`) | alpha | 2026-09-17 | cc-tweaked, kotlin-for-forge |
| create-cc-total-logistics | 0.3.6 (`24hfd7Lg`) | release | 2025-06-14 | cc-tweaked, create, kotlin-for-forge |

Tutte le versioni NeoForge di CC: Tweaked su Modrinth sono `alpha`, anche quelle per 26.1.2 e 26.2 (le 8 più recenti controllate).

## Sorgenti letti (git, clone superficiali)

- **CC: Tweaked** `v1.21.1-1.120.2` (`c7ccc20`): `CommonHooks` aggiunge la tabella `computercraft:treasure_disk` a 10 casse vanilla (dungeon, miniera abbandonata, 3 della roccaforte, piramide del deserto, tempio della giungla, igloo, villa, cartografo del villaggio); metodi generici `AbstractInventoryMethods`, `AbstractFluidMethods`, `AbstractEnergyMethods`; integrazione con Iris (`IrisShaderMod`: testo dei monitor con il vertex sink di Iris, niente monitor nel passaggio delle ombre).
- **Create** `mc1.21.1-6.0.10` (`ac0c444`) e `mc1.21.1/dev` (`7ff2760`): `compat/computercraft/implementation/peripherals/` con 19 periferiche: CreativeMotor, DisplayLink, Frogport, NixieTube, Packager, Postbox, RedstoneRequester, Repackager, SequencedGearshift, Signal, SpeedController, SpeedGauge, Station, Sticker, StockTicker, StressGauge, Synced, TableClothShop, TrackObserver; eventi (KineticsChange, Package, Repackage, SignalStateChange, StationTrainPresence, TrainPass).
- **Mekanism** `v1.21.1-10.7.19.85` (`a00109e`): `integration/computer/computercraft/` (MekanismPeripheral, CCMethodCaller…), compilato contro l'API di CC: Tweaked.
- **Advanced Peripherals** `1.21.1-0.8.2a` (`e3b0c09`): periferiche BlockReader, ChatBox, Chunky, Colony, Compass, DistanceDetector, EnergyDetector, EnvironmentDetector, FluidDetector, GasDetector, GeoScanner, InventoryManager, MEBridge, NBTStorage, PlayerDetector, RSBridge, Saddle, SmartRail, più `metaphysics` (tartarughe automi); 8 potenziamenti per tartarughe e 7 per i computer tascabili; integrazioni in `common/addons/`: ae2, create (Basin, BlazeBurner, FluidTank, filtri, valori a scorrimento), curios (SmartGlasses, InventoryManager), dimstorage, mekanism (radiazioni nell'Environment Detector), minecolonies, powah, refinedstorage, valkyrienskies. `common/village/VillageStructures`: aggiunge le case del Computer Scientist (5 file `structures/villages/scientist_*.nbt`: plains, desert, savanna, snowy, taiga) ai villaggi se `enableVillagerStructures` (vero di serie, peso 10); config `config/Advancedperipherals/world.toml` (COMMON). Requisiti: NeoForge ≥ 21.1.238, CC ≥ 1.119.0; facoltative con versione minima: ae2 19.2.13, minecolonies 1.1.1300, patchouli 1.21-88, mekanism 1.21.1-10.7.15.81.
- **UnlimitedPeripheralWorks** ramo `1.21` (`205d184`, 17/09/2026): integrazioni NeoForge in `projects/forge/.../integrations/`: additionallanterns, ae2, ars_nouveau (sorgente, Mob Jar, Magic Tome, potenziamento tascabile), automobility, create (filtri, Linear Actuator, opzioni a scorrimento, ricette di lavorazione e in sequenza), deepresonance, easy_villagers, embers, emi, extrahnn, fluxnetworks, gtceu, hostilenetworks, integrateddynamics, kubejs, mna, naturescompass, occultism (Golden Sacrificial Bowl, magazzino), powah, projecte, theurgy, toms_storage. Il jar contiene Peripheralium 1.4.6, Broccolium 1.4.6, Tweakium 1.4.9.
- **CC:C Bridge** `v1.7.3-1.21.1` (`73f2efa`): blocchi `source_block` (Source Block), `target_block` (Target Block), `redrouter_block` (RedRouter Block), `scroller_block` (Scroller Pane), `animatronic_block` (Animatronic); più una variante di quadro.

## Pack (25/10/2026)

Create 6.0.10, Mekanism 10.7.19.85 (+ Generators), Create Crafts & Additions 1.6.0, Tom's Storage 2.4.2, Storage Drawers, Sophisticated Backpacks, Occultism, Ars Nouveau, Kotlin for Forge, Curios 9.5.1, Patchouli 1.21.1-93; niente AE2, Refined Storage, Powah, Minecolonies.
