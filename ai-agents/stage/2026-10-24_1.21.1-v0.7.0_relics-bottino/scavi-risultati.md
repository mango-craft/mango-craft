# Scavi archeologici: chi usa le tabelle vanilla (24/10/2026)

Scansione dei 253 jar dell'istanza di prova (sola lettura, script `scavi-scansione.py`, lanciato sul PC di Matteo nella cartella `mods`), più i sorgenti indicati. Cercati: copie delle tabelle `data/minecraft/loot_table/archaeology/*`, JSON e strutture `.nbt` che nominano `archaeology/`, classi con `archaeology/`, `BrushableBlockEntity`, `LootTableLoadEvent`, `MODIFY_LOOT_TABLE`, `LootTableEvents`, `*_ARCHAEOLOGY`.

## Risultati

- **Nessun jar** contiene una copia delle tabelle `minecraft:archaeology/*`. L'unica mod con modificatori su quelle tabelle è Artifacts (5 file, `"replace": true`, `artifacts:config_value_chance` = `archaeologyChance` 1/16; sorgente `ochotonida/artifacts` @7cf7dc4).
- **Usano le tabelle vanilla come tabella principale** (oggi Artifacts ci mette l'artefatto):
  - Dungeons and Taverns: `nova_structures/worldgen/processor_list/desert_ruins_degradation.json` (`append_loot` → `minecraft:archaeology/desert_pyramid` sulla sabbia sospetta), più processori in `data/minecraft/worldgen/processor_list/` (creeping crypt, ruined town);
  - YUNG's Better Desert Temples (codice: `minecraft:archaeology/desert_pyramid`);
  - YUNG's Extras (`DesertWellProcessor`, `DESERT_WELL_ARCHAEOLOGY`) e Lithostitched (`WellConfig`, `DESERT_WELL_ARCHAEOLOGY`): pozzi del deserto;
  - Towns and Towers: processori con `trail_ruins_common`/`trail_ruins_rare`;
  - **Ars Nouveau, Alakarkinos** (granchio): 6 ricette `alakarkinos_conversion` (sabbia/ghiaia → tabelle vanilla, pesi 100/25); il codice (`SpawnLootState.getLoot`, `baileyholl/Ars-Nouveau` main @7ee8826, 5.13.3) tira la tabella con `getRandomItems` (quindi con i modificatori), giocatore finto `ANFakePlayer` come entità, pausa di 60 secondi dopo ogni bottino.
- **Usano le tabelle vanilla come sotto-tabella** (i modificatori non si applicano alle sotto-tabelle, oggi niente artefatti): **Better Archeology** 1.3.9, `betterarcheology:archeology/desert_sand` (desert_well peso 5, schegge 1), `mesa_red_sand` (trail_ruins_rare 6, schegge 1), `plains_gravel` (desert_pyramid 6, schegge 1), `sussand_underwater` (ocean_ruin_warm 6, schegge 1), `taiga_dirt` (trail_ruins_rare 2, trail_ruins_common 3, schegge 1).
- **Tabelle proprie, non toccate**: Jaden's (`netherexp:archaeology/*`), Cataclysm (`cataclysm:archaeology/cursed_pyramid*`), Moog's End Structures (`mes:archaeology/end_sand`, nelle `.nbt`), YUNG's Better Jungle Temples (`betterjungletemples:archaeology/emerald`), YUNG's Extras (`yungsextras:desert/extra_archeology`), Towns and Towers (`kaisyn:archeology/*`).
- **Codice che modifica tabelle al caricamento**:
  - Corail Tombstone (`LootHelper`, `LootTableLoadEvent`): aggiunge una sua pool (`tombstone:archeology_treasure`) alle tabelle dell'archeologia;
  - Hexalia (`MODIFY_LOOT_TABLE`): solo `JUNGLE_TEMPLE`;
  - Bookshelf `PoolTarget` elenca le tabelle vanilla, ma nessun altro jar lo usa;
  - gli altri utenti di `LootTableLoadEvent` (Create Dragons Plus, Illager Invasion, L'Ender's Delight, Moonlight, owo-lib, Puzzles Lib, Unfocused, Architectury) non nominano tabelle dell'archeologia.
- **NeoForge 1.21.1** (`patches/.../LootDataType.java.patch`, @e0e7ab5): ogni tabella letta dai dati, anche se riscritta da un datapack, passa da `EventHooks.loadLootTable` (quindi Tombstone continua a funzionare); una tabella con `neoforge:conditions` falso diventa `LootTable.EMPTY` (nessun ritorno alla vanilla).
