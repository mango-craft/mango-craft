# Nether: research for the 1.21.1 NeoForge pack

_Research date: 17/10/2026 · target: Minecraft 1.21.1, NeoForge 21.1.259, single player._
_Sources: Modrinth API (search, project and versions endpoints), GitHub source (cloned under `scratchpad/repos/`, never executed), project pages. Download counts come from the Modrinth search index, October 2026._

---

## 0. TL;DR

**Recommended combo (3 mods + 1 tiny fix):**

| Role | Pick | Version (1.21.1 NeoForge) | Why |
|---|---|---|---|
| Biomes, terrain, plants, mobs, ambience | **Jaden's Nether Expansion (JNE)** | 2.4.1, release, 22/08/2026 (+ Elysium API 1.21.1-2.0.1, Lodestone 1.8.2) | The only big Nether overhaul for NeoForge 1.21.1 that **ships explicit support for Regions Unexplored 0.6**. Its biome source lists RU's 4 Nether biomes and excludes the removed Redstone Abyss. It redecorates all 5 vanilla biomes and adds sub-biomes, about 7 mobs, 5 structures, crops and fungi, fog, particles and sounds. Both of its worldgen overrides can be switched off in config |
| Structures | **Moog's Nether Structures (MNS)** | 3.1.1, release, 17/09/2026 | 52 structures, from small ruins up to a 207-piece Mega Fortress. LGPL. Its library (Moog's Structure Lib ≥ 3.3.0) is already in the pack through Moog's End Structures. 36 of the 52 use `#minecraft:is_nether`, so they also spawn in RU and JNE biomes. No overlap with YUNG's, and Sparse Structures spaces them too |
| Lava seas | **Nether Depths Upgrade (NDU)** | 3.3, release, 21/09/2026 | Fills the empty lava oceans: crimson/warped kelp and seagrass in every Nether biome, 11 lava fish mobs, a lava fishing rod, lava sponge and lava glass. MIT, GeckoLib is already in the pack. Light |
| Fix for something already broken | **Cataclysm berserker tag** (3-line datapack) or *Cataclysm x YUNG's Better Nether Fortress* 1.0.0 | — | With YUNG's fortresses, Cataclysm's **Ignited Berserkers never spawn**, because they are tied to the `minecraft:fortress` structure tag (verified in source) |

**Optional extras, all compatible:** Eternal Nether (structures and mobs, MIT, Puzzles Lib already in the pack) · Piglin Proliferation (piglin variety) · Gardens of the Dead (2 extra biomes, natively supported by JNE).

**Not recommended:** Incendium (alpha "unsupported port" from Dec 2024; overrides the Nether dimension file, which breaks JNE and thins out RU) · Amplified Nether (good, but redundant with JNE's taller Nether; JNE disables its own terrain when it detects it) · BetterNether: New Dawn (unofficial port that replaces the biome system).

**Key corrections to the pack notes:**
- **RU 0.6.x no longer uses TerraBlender.** 0.6 changelog: "Terrablender has been removed as a dependency, Lithostitched takes it place". **Redstone Abyss was removed** in 0.6, so RU has **4** Nether biomes, not 5. TerraBlender stays in the pack only for other mods (e.g. Deep Aether).
- **Starcatcher × NDU:** the compat class exists in Starcatcher's code, but the call is **commented out** on the 1.21.1 branch (head 16/10/2026). Only Create and Tide compat are active. NDU fish are not in the Starcatcher minigame.

---

## 1. What the pack already puts in the Nether (verified in source unless noted)

| Source | Nether content |
|---|---|
| **Regions Unexplored 0.6.2** (Lithostitched 1.7.9+, *no TerraBlender*) | 4 biomes. Each one **partially replaces one vanilla biome** through Lithostitched `replacePartially` regions (weight 60): Mycotoxic Undergrowth ← Nether Wastes · Glistering Meadow ← Soul Sand Valley · Blackstone Basin ← Crimson Forest · Infernal Holt ← Basalt Deltas. It also adds ash vents to vanilla Basalt Deltas. Redstone Abyss is removed (`REMOVED_REDSTONE_ABYSS`) |
| **YUNG's Better Nether Fortresses** | Its own structure set `betterfortresses:fortress` (`yungsapi:enhanced_random_spread`, spacing 30 / separation 20, kept away from bastions). Jigsaw start at **y 80–100**. Biomes: `#minecraft:is_nether` + `#c:in_nether`, so modded biomes are included |
| **L_Ender's Cataclysm** | **Burning Arena** (Ignis): only `minecraft:nether_wastes`, spacing 80/50 · **Soul Black Smith** (Netherite Monstrosity): crimson_forest, nether_wastes, soul_sand_valley, warped_forest, start y 64, spacing 60/50 · **Ignited Berserker**: added as a spawn override to structures in the `cataclysm:berserker_spawn` tag, which contains only `minecraft:fortress`. **With YUNG's this never fires** (see §3.4) |
| **Friends & Foes 5.0.2** | **Citadel** structure (Wildfire mini-boss) in `#minecraft:is_nether` |
| **Dungeons and Taverns** (base mod, per its page) | Nether Keep (giant tower), Nether Ports (at lava level), Nether Skeleton Towers, Sealing Halls (rarest), Piglin Donjon (crimson forest megastructure); Piglin Camp/Outstation also listed |
| **Born in Chaos** (per its page) | Bone Imp (fire-immune, mainly Nether) and Firelight (Nether and firewells); Phantom Creeper in Warped Forest |
| **Starcatcher** | 10 lava fish restricted to the Nether dimension plus lava (Lava Crab, Embergill, Glowstone Seeker, Magma Fish, Scalding Pike, Cinder Squid, Glowstone Pufferfish, Cerberay…) + Willish (Basalt Deltas only). Being dimension-based, they work in any modded Nether biome |
| **Subtle Effects** | Nether-only flame and smoke geysers |
| **Botany Pots 21.1.x** | Native recipes for vanilla Nether plants and soils (fungi, roots, sprouts, vines, wart, nylium, soul sand/soil, netherrack) **and for RU's Nether plants** (brimsprout, cobalt earlight/roots, dorcel, glister bulb/spire, glistering ivy/sprout/fern/bloom, mycotoxic grass/daisy/mushrooms, bioshrooms; soils brimsprout/cobalt/glistering nylium, mycotoxic moss) |
| WDA, Towns and Towers, Moog's End Structures, Mowzie's, Mutant Monsters, Illager Invasion | Nothing Nether-specific found (WDA's page lists no Nether structures) |

So the Nether already has decent structures (YUNG + DnT + F&F + Cataclysm) and 4 RU biomes. What it lacks: **vanilla biomes still look vanilla**, the **lava seas are empty**, there are **few Nether-native mobs**, and there is little **mid-size filler** between structures.

---

## 2. Recommended combination: details and compatibility verdicts

### 2.1 Jaden's Nether Expansion (JNE), core pick

- **Availability:** NeoForge 1.21.1 only (Fabric dropped). **2.4.1** release 22/08/2026, **2.4.0** "NeoForge 1.21.1 Port" 20/08/2026 (codebase rewritten from scratch), betas since 02/04/2026. Requires **Elysium API ≥ 1.21.1-2.0.1** (GPL-2.0, released 22/08/2026) and **Lodestone** 1.8.2 (rendering lib, also used by Malum). It bundles Biolith (jar-in-jar). Curios is optional. License **CC-BY-NC-ND-4.0** (fine for personal use). 4.08M downloads. Source on GitHub (branch `1.21.1`, head 29/08/2026).
- **What it adds (from the 1.21.1 source):**
  - *Biomes and terrain:* redecorates all 5 vanilla biomes through NeoForge biome modifiers. Examples: quartz crystals in Wastes; weeping ivy, sporeshrooms and crimson sprouts in Crimson; fossil ore, soul magma, ectoplasm lakes, bone pikes and mounds in Soul Sand Valley; pyroclast crusts and siltmarram. Sub-biomes **Black Ice Glaciers** (Biolith) and Sorrowsquash Pastures. The optional *Nether Worldgen Overhaul* pack (on by default) gives multilayered terrain and a **taller Nether**: `dimension_type` min_y −32, height 288, logical height 192. Lava sea stays at y 32.
  - *Biome source:* the **Mosaic** biome source from Elysium API (on by default, labelled **BETA**). It places biomes on a weighted Voronoi grid so many Nether mods don't produce tiny noisy biomes, and it auto-fills from `#minecraft:is_nether`. It ships **explicit entries for RU 0.6** (mycotoxic_undergrowth, glistering_meadow, blackstone_basin, infernal_holt, weight 12, loaded only when RU is present) and **excludes `regions_unexplored:redstone_abyss`**. It also has entries for BetterNether, BOP, Cinderscapes, Gardens of the Dead, Nether Descent, Soulful Nether and Infernal Expansion. Per the 2.4.0 changelog it is compatible with TerraBlender, Biolith and Blueprint biomes.
  - *Mobs:* Wisp, Apparition, Vessel, Ecto Slab, Banshee, Stampede, Carcass (mostly soul sand valleys, plus Gardens of the Dead's Soulblight Forest); damp strider variant.
  - *Structures:* Chapel (its biome tag explicitly includes the 4 RU biomes), Sanctum, Devil's Misfortune, Mega Fossil, Mega Fossil Campsite.
  - *Plants and food:* Sorrowsquash (crop, carved, Ghoul-o'-lantern), Soul Torchflower (crop), Warped Wart, Cerebrage Claret fungus wood set, sporeshrooms, ivies, nether pizza. Huge block palette: soul slate, smooth netherrack, polished basalt, blue nether bricks, netherite plating, bone and skull blocks, gargoyle statues…
  - *Ambience:* per-biome particles (ash, white ash, crimson and warped spores), brighter per-biome Nether fog (configurable, plus an option to keep red Wastes fog), its own ambient sounds and music, geysers.
- **Compatibility verdicts:**
  - **RU 0.6.2: ✅ designed for it.** RU biomes come from two paths: the mosaic entries, and RU's own Lithostitched `replacePartially` injectors. Lithostitched wraps *any* biome source in its `InjectorBiomeSource`; only `add_points` injectors need multi-noise, `replacePartially` does not. Expect *more* RU, not less.
  - **TerraBlender:** Elysium patches TerraBlender's surface-rule category for the mosaic source (`LevelUtilsMixin`), so TB surface rules keep working.
  - **YUNG's fortresses (y 80–100), bastions, Cataclysm structures, DnT, F&F Citadel: ✅.** Vanilla biomes stay in the mosaic list, so Cataclysm's Burning Arena (nether_wastes only) and Soul Black Smith still have their biomes.
  - **Amplified Nether:** JNE detects it and **turns off its own terrain overhaul** (`CompatUtil.AMPLIFIED_NETHER`). The two are compatible but redundant.
  - **Incendium: ❌.** Both override `minecraft:dimension/the_nether.json`, so only one wins.
  - **Pyrellium:** Pyrellium's own code skips its dimension patch when JNE is present ("crashes"). Its biomes then come only through mosaic auto-fill. Avoid.
  - **Mob mods:** no shared entities with Cataclysm or Born in Chaos. More Nether monster types share the same mob cap, so expect a bit fewer vanilla mobs.
  - **Farmer's Delight:** *Jaden's Nether Expansion Delight* (MIT, 1.21.1-1.0.4a, 11/06/2026, 982k downloads) is the bridge. It was built against an older JNE build (CurseForge file 8176209). Two of its recipes reference `netherexp:blue_scale_fungus` / `red_scale_fungus`, which **no longer exist in JNE 2.4**. Expect harmless "unknown item" recipe errors; the rest of its references (hogham, glowcheese, cerebrage, lightspores, frogmist, wisp bottle…) still exist.
  - **Botany Pots:** **no native recipes** for `netherexp`. Use `/botanypots debug … gen_files` for sorrowsquash, soul torchflower, warped wart, cerebrage, sporeshrooms.
  - **Starcatcher:** no interaction. Starcatcher's crimson-forest and Basalt-Deltas fish still have their biomes.
  - **Ambience mods** (AmbientSounds, Particle Rain, Subtle Effects): only cosmetic overlap (extra particles, sounds and geysers on top).
- **Risks:** fresh rewrite (August 2026); the mosaic is BETA; Lodestone adds another rendering library next to Sodium 0.8.12 (Lodestone is widely used on NeoForge 1.21.1, but test it). The `dimension_type` change means **new world only**, at least for the Nether. Other things built for a 128-high roof may look slightly off; for example MNS's Mega Fortress chains are "lengthened to reach the Nether roof".
- **Fallback without uninstalling** (`config/netherexp-startup.toml`, section `packSettings`, needs a game restart): `improvedNetherBiomeSource = false` returns to vanilla multi-noise (RU then works only through Lithostitched); `netherWorldGenOverhaul = false` restores vanilla terrain and height.
- **Performance:** medium. It is content-heavy, adds particles and Lodestone rendering, and the taller Nether costs more chunk generation. No tick-function datapacks.

### 2.2 Moog's Nether Structures (MNS): structures

- **Availability:** 3.1.1 release 17/09/2026 (1.21 → 26.x, NeoForge included). Requires **Moog's Structure Lib ≥ 3.3.0** (latest NeoForge 1.21.1: 3.4.2, 03/10/2026), already pulled in by Moog's End Structures. LGPL-3.0. 4.69M downloads. Server-side worldgen only.
- **Content:** 52 structures in 42 structure sets: bridges (6), wells, houses, fungus "trees", blackstone and nether-brick ruins, lava pools, graveyard, giant skull, sandy skull, sword, train, copper tower, nether tower, nether wart farm, ruined portal, warped dome and pool, soul fire, arenas (small, large, dragon arena, mega arenas), and the **Mega Fortress** (207 pieces, 3.0.0). Vanilla blocks and mobs only.
- **Compatibility:**
  - Biomes: 36 structures use `#minecraft:is_nether` (RU and JNE biomes included); 15 are tied to a specific vanilla biome (6 crimson, 7 warped, 2 soul sand valley, 1 wastes/BYG). All of those biomes still exist with RU and JNE.
  - **YUNG's: ✅.** The Mega Fortress has its own set (spacing 116/76). Its "replace vanilla fortress" option is **off by default**; keep it off, since YUNG's already replaces the fortress.
  - **Sparse Structures: ✅.** Sparse works on the JSON (any placement type except `concentric_rings`), so MNS's custom `moogs_structures:advanced_random_spread` sets get spaced too.
  - Overlap with DnT and F&F Nether structures is thematic only; Sparse Structures handles density.
- **Performance:** light (jigsaw structures; Structure Layout Optimizer helps).

### 2.3 Nether Depths Upgrade (NDU): lava seas

- **Availability:** 3.3 release 21/09/2026 (1.21–1.21.1, NeoForge). Requires GeckoLib (in pack). MIT. 3.34M downloads. Source `Scouter456/Nether_Depths_Upgrade`, branch `nether_depths_upgrade_1.21` (head 23/08/2026).
- **Content:** warped and crimson kelp, seagrass and kelp carpet blocks (added to **all `#minecraft:is_nether` biomes**, so RU and JNE biomes get them too); vents; lava sponge (wet and dry), lava glass; fish **Bonefish, Wither Bonefish, Blazefish, Eyeball Fish, Fortress Grouper, Glowdine, Lava Pufferfish, Magmacubefish, Obsidianfish, Searing Cod, Soulsucker**; a **Lava Fishing Rod** with its own bobber entity (no mixins); one enchantment and one potion; a small fortress-side ruin in `#has_structure/nether_fortress` biomes.
- **Compatibility:**
  - **Starcatcher:** the NDU compat class `DGNetherDepthsUpgradeFishes` exists in Starcatcher, but the call `//DGNetherDepthsUpgradeFishes.bootstrap(context);` is **commented out**, and no NDU JSON is generated. The two systems run side by side. Starcatcher rods in lava give Starcatcher's 10 Nether fish; NDU's Lava Fishing Rod gives NDU fish with its own loot tables. No conflict, just two lava-fishing mechanics.
  - NDU fish *entities* spawn only in vanilla biomes listed in its tags (plus BYG and Infernal Exp IDs), not in RU or JNE-only biomes. Kelp and seagrass go everywhere.
  - **Farmer's Delight:** NDU's FD compat (fish slices) is **commented out** in the 1.21 source. Cooking the fish needs My Nether's Delight or Starcatcher Delight recipes, if they cover them (unverified).
  - **Botany Pots:** no native recipes for NDU kelp or seagrass.
- **Performance:** light.

### 2.4 Cataclysm × YUNG's fortress fix (strongly suggested, no new content)

`CMWorldRegistry.modifyStructure` adds Ignited Berserker to structures in the tag `cataclysm:berserker_spawn` = `["minecraft:fortress"]`. YUNG's replaces the fortress with `betterfortresses:fortress`, so **berserkers are currently lost**. Two options:
- A datapack with `data/cataclysm/tags/worldgen/structure/berserker_spawn.json` = `{"replace": false, "values": ["betterfortresses:fortress"]}`. Zero risk; the tag is evaluated by the NeoForge structure modifier.
- Or the mod **Cataclysm x YUNG's Better Nether Fortress** 1.0.0 (MIT, 31/08/2026, Forge and NeoForge 1.20.1/1.21.1, very few downloads). Its page says it "enables Ignited Berserker spawns in YUNG's fortresses" after Ignis is defeated, so it may add extra gating.

---

## 3. Biome and terrain mods vs RU / Lithostitched / TerraBlender (technical notes)

- **How RU 0.6 places Nether biomes:** `RULithostitched` → `BiomeInjector.replacePartially(target vanilla biome, RU biome, region)`. Lithostitched's `BiomeInjectorManager` wraps whatever biome source the Nether level stem has in an `InjectorBiomeSource`. So RU follows **whatever vanilla biomes the final biome source still produces**, whether that source is vanilla multi-noise, Incendium's custom list or JNE's mosaic.
- **TerraBlender** (1.21.1 branch): for Nether multi-noise sources it takes the dimension's own parameter list as **region 0** and adds other mods' regions next to it. A datapack that replaces the Nether parameter list (like Incendium) therefore becomes "the vanilla region". Lithostitched's `updateParameters` knows about TerraBlender's `uniqueTrees`.
- **Incendium Legacy** (Stardust Labs): its 1.21.x line is **v5.4.4, alpha, 04/12/2024** (mod jar for fabric/forge/neoforge/quilt, plus datapack zip). The changelog says: "This is an unsupported version of Incendium! Use at your own risk… upgrading from this port to the rewrite may not be possible". From 5.5.0 the project was renamed "Incendium Legacy"; a separate rewrite is coming. No dependencies; Sparkles is an optional resource pack. On GitHub, only the 1.20 data (v5.3.5) is public. In that version it:
  - overrides `data/minecraft/dimension/the_nether.json`: multi-noise with 8 Incendium biomes and 5 vanilla ones;
  - overrides many vanilla Nether configured and placed features (glowstone, basalt, deltas, ores, fungi…), **vanilla log loot tables** (Blazing Hatchet → charcoal) and **redstone recipes** (comparator, observer, piston… via a stone tag);
  - runs its mobs and items with **command functions every tick** (`@e[type=#incendium:mobs…]`).
  - **Verdict:** RU biomes *would* still generate, but only inside the smaller share of the map left to vanilla biomes. Cataclysm's Burning Arena (nether_wastes only) becomes rarer. It is incompatible with Amplified Nether (declared) and with JNE (same file). Per-tick function cost. **Not recommended** (the pack notes already discarded it as alpha).
- **Amplified Nether** (Stardust Labs): **1.2.16 release 13/07/2026** (1.21–1.21.11, 26.x; jar for neoforge + datapack). Stardust Labs License, 2.37M downloads. Terrain only: overrides `noise_settings/nether.json` (min_y 0, height 256, custom climate density functions) and some vanilla features and carvers; no new biomes. Its page says it is often compatible with other biome mods, **not with Incendium**, and must not be added to an existing Nether. With RU it works: RU biomes still replace parts of vanilla biomes, and RU prepends its surface rules to whatever noise settings exist. YUNG's fortress (y 80–100) is fine. **Verdict:** a good alternative *instead of* JNE's terrain (JNE auto-yields), but redundant if JNE is used. Heavier Nether chunk generation.

---

## 4. Full candidate list

Legend: ✅ recommended · ➕ good optional extra · 🔁 alternative · ⚠️ risky · ⛔ skip

| Mod | 1.21.1 NeoForge (latest, date) | License · DL | Adds | Compat notes | Perf | Verdict |
|---|---|---|---|---|---|---|
| **Jaden's Nether Expansion** | 2.4.1 rel. 22/08/2026 | CC-BY-NC-ND · 4.08M | See §2.1 | RU explicit ✅; Incendium ❌; BP no; FD via JNE Delight | Medium | ✅ |
| **Moog's Nether Structures** | 3.1.1 rel. 17/09/2026 | LGPL · 4.69M | 52 structures | YUNG ✅, Sparse ✅, MSL in pack | Light | ✅ |
| **Nether Depths Upgrade** | 3.3 rel. 21/09/2026 | MIT · 3.34M | Lava flora and fish | Starcatcher compat disabled; no FD/BP | Light | ✅ |
| Cataclysm x YUNG's BNF | 1.0.0 rel. 31/08/2026 | MIT · tiny | Berserker spawns in YUNG fortresses | Or use the 3-line datapack | None | ✅ (fix) |
| **Eternal Nether** (Fuzs; Bygone Nether continuation) | v21.1.3 rel. 10/07/2025 | MIT · 824k | Piglin Manor (crimson), Citadel (warped), Catacombs (soul sand valley); Piglin Hunter and Prisoner, Warped Enderman, Wither Skeleton Knight and Horse, Wraither, Corpor, Wex; withered blocks; Netherite Bell, Cutlass, Netherite Shield | Needs Puzzles Lib (in pack). Structures use vanilla biomes plus optional Incendium/BYG/BOP. **Overrides vanilla `wither_skeleton` and `blackstone` loot tables.** Its "Citadel" is unrelated to F&F's Citadel | Light–med | ➕ |
| **Piglin Proliferation** (seymourimadeit) | 2.0.16 rel. 09/10/2026 | MIT code / CC-BY-NC-SA assets · 430k | Brute Buckler and charge, zombified variants keep gear, **Piglin Alchemist** and **Piglin Traveler** (Traveler's Compass), Fire Pits, piglin heads | No deps; touches only piglins | Light | ➕ |
| **Gardens of the Dead** | 5.0.2 rel. 08/12/2025 | MIT · 3.56M | 2 spooky biomes (Soulblight Forest, Whistling Woods), plants and blocks | TerraBlender Nether region (TB bundled; fine with Lithostitched). JNE has mosaic entries, mob spawns and structure tags for it | Light | ➕ |
| Formations Nether (SuperMartijn642) | 1.0.5b rel. 11/09/2026 | ARR (modpack use allowed) · 6.59M | 21 small/medium structures (castle, temple, arenas, pillars, ore shards…) | Needs Formations lib (ARR); mostly `#is_nether` | Light | 🔁 to MNS (or alongside it if you want even more filler) |
| Hearths (Everloste) | v1.0.5 rel. 14/10/2025 (mod + datapack) | ARR · 6.53M | Spikes and magma lakes in Wastes; rocks, fallen stems and new huge fungus in Crimson/Warped; Crimson and Warped **Towers** (~100 blocks) | Its page says "not fully compatible" with packs that change the same biome files; it overlaps JNE's redecoration | Light | 🔁 (only if *not* using JNE) |
| Amplified Nether | 1.2.16 rel. 13/07/2026 | Stardust Labs · 2.37M | Terrain only, 256 high | See §3 | Gen-heavy | 🔁 (instead of JNE's terrain) |
| Luminous: Nether | 1.3.3 rel. 12/07/2026 | ARR · 340k | 2 biomes (Fungal Plains, Ash Forest), many mobs incl. Mushlin King / Piglin Executioner / The Furnace, rituals | 1.3.3 moved biome placement from TerraBlender to **Blueprint** (Blueprint is in the pack via Unusual End); GeckoLib. JNE claims Blueprint-biome compatibility, but this stack is untested | Medium | 🔁 ⚠️ |
| Nether Descent (Potion Studios; the former BYG Nether biomes) | 1.0.9 rel. 27/09/2026 | ARR · 16k | 5 biomes (Arisian Undergrowth, Sythian Torrids, Embur Bog, Crimson Gardens, Wailing Garth) with blocks and mobs | Requires Oh The Trees You'll Grow; TerraBlender, Lithostitched or Biolith (optional). JNE has mosaic entries for it. Young project | Medium | 🔁 |
| Pyrellium | 0.4.1 rel. 08/10/2026 | CC-BY-4.0 · 13.6k | 9 biomes | Mixin rewrites the Nether dimension and noise JSON at load; skips the dimension patch when JNE is present ("crashes") | ? | ⚠️ |
| Incendium Legacy | 5.4.4 **alpha** 04/12/2024 | Stardust Labs · 10.5M | 8 biomes, 9+ structures, mobs, boss, 25+ items | See §3: ❌ with JNE and Amplified; thins out RU; per-tick functions; overrides vanilla loot and recipes | Medium (tick) | ⛔ |
| BetterNether: New Dawn (unofficial) | 21.0.28 rel. 14/10/2026 | MIT · 218k | BetterNether + Gloomwood | Needs BCLib/WunderLib/WorldWeaver "New Dawn" ports (own biome-source system) → high risk with RU/Lithostitched; already discarded | Heavy | ⛔ |
| Even Better Nether | (last 19/05/2025) | ARR · 65k | BetterNether remake | Little information, low adoption | ? | ⛔ |
| Nether Weather | **datapack only** for 1.21.1: v1.1.1, 16/06/2024 (the 1.21.1 jar is fabric/forge/quilt) | CC-BY-NC-SA · 134k | Lavafalls, storms and heatblasts (they damage you) | Function-based (1 s clock); install as a world datapack | Light | 🔁 (ambience; old) |
| Nether's Exoticism (MCreator) | 1.2.9 rel. 21/04/2026 | MIT · 78k | 5 fruit trees, one per vanilla biome; Moloch mob; Create and FD-cutting compat | No BP; vanilla biomes only | Light | 🔁 (food theme) |
| My Nether's Delight (already planned) | 1.10.4.1 rel. 11/09/2026 | ARR · 5.2M | FD Nether cooking; wild *Powdery Cannon* patches | No BP natively | Light | (already planned) |
| JNE Delight | 1.21.1-1.0.4a rel. 11/06/2026 | MIT · 982k | 30+ FD foods for JNE | 2 recipes reference items removed in JNE 2.4 (harmless) | Light | ➕ with JNE |
| A Cold Day in the Nether | 1.6.1 rel. 16/11/2024 | MIT · 31k | Everfreeze Cirques frozen biome and mobs | Old; overlaps JNE's Black Ice Glaciers | ? | ⛔ |
| Hellish Trials | 1.0.5 rel. 11/01/2026 | ARR · 89k | Trial chambers in the Nether | — | Light | 🔁 |
| Cult of Azazel | 1.1.4.9a rel. 27/07/2026 | MIT · 133k | Nether mansion with a cult and magic gear | — | Light | 🔁 |
| Medieval Buildings [Nether Edition] | 1.0.2 rel. 08/01/2026 | ARR · 772k | Medieval Nether buildings | — | Light | 🔁 |
| Nether Dungeons | 1.1.0-snapshot5 (marked release) 29/09/2026 | ARR · 218k | "Expands the Nether" | Snapshot naming | ? | ⛔ |
| Bastion Remnant Renovation Project / "Bastion Remnant … Reforged" datapacks | 1.0 rel. 12/01/2026 / July 2025 | GPL / LGPL · ≤ 9k | Bastion facelifts | Datapack overrides of vanilla bastion pools; no YUNG overlap. There is no "YUNG's Better Bastions" | Light | 🔁 (niche) |
| Fortress overhauls: DnT Nether Fortress Overhaul, Bygone Fortress Plus, Updated Nether Fortress, Apocalyptic Fortress (unofficial port) | various | — | Fortress redesigns | **Redundant or conflicting with YUNG's Better Nether Fortresses** | — | ⛔ |
| Nightosphere / Abyssaline Nether / Legacy Nether: Extended | datapacks, 1.21.1 OK | CC-BY-NC-SA / ARR / CC-BY-SA | Terrain tweaks / terrain + 7 biomes / console-era Nether | Terrain packs clash with JNE's terrain and Amplified. Abyssaline: "should not be used with other biome mods" | — | ⛔ |
| Repurposed Structures (NeoForge) | 7.5.x, 1.21.1 | LGPL · 5.4M | Nether pyramid, outposts, shipwrecks, ruins, etc. | Pack notes: only *instead of* Towns and Towers | Light | (see structures section) |
| Explorify | 1.6.5 | ARR · 9.7M | — | **No Nether structures** | — | n/a |
| Kaleidoscope Nether | — | MIT | — | Needs Kaleidoscope Cookery (not in pack) | — | ⛔ |

---

## 5. Not available for 1.21.1 NeoForge

- **BetterNether** (official): Fabric only (21.0.11). Only the unofficial "New Dawn" port exists for NeoForge.
- **Cinderscapes**: Fabric/Quilt only (5.0.4).
- **Infernal Expansion**: Forge ≤ 1.19 on Modrinth; *Infernal Expansion Redux* is 1.20.1 only.
- **Soulful Nether**: no 1.21.1 version.
- **Bygone Nether**: succeeded by **Eternal Nether** (Fuzs).
- **Nether Biomes Compat** (BetterNether/Incendium/RU/Cinderscapes glue): Forge 1.20 only.
- **Nether Weather** as a NeoForge mod: no 1.21.1 NeoForge jar (the datapack works).
- "Better Bastions", "Netherized", "Unusual Nether": no such projects on Modrinth.
- **Oh The Biomes We've Gone**: for reference only. The ex-BYG Nether biomes now ship separately as **Nether Descent** (same studio, same biome names).

---

## 6. Install and test notes

1. **New world** (or at least a never-visited Nether). JNE changes the Nether `dimension_type`, and all worldgen mods want fresh chunks.
2. Install JNE + Elysium API + Lodestone → launch → check the log for Elysium's "MosaicBiomeSource successfully patched surface rules from Terrablender" line (it appears only when TerraBlender is present) and for errors. Then `/locate biome regions_unexplored:infernal_holt`, `…:glistering_meadow`, `netherexp:black_ice_glaciers`.
3. Add MNS (MSL already present) → `/locate structure mns:mega_fortress`, `betterfortresses:fortress`, `cataclysm:burning_arena`, `cataclysm:soul_black_smith`.
4. Add NDU → check kelp in lava seas and test the NDU Lava Fishing Rod next to a Starcatcher rod.
5. Add the berserker datapack to the world `datapacks/` folder. Structure modifiers apply at server start, so restart or re-open the world rather than relying on `/reload`. Then check that Ignited Berserkers appear inside a YUNG fortress (with the mod version, possibly only after Ignis is defeated).
6. If the mosaic misbehaves (odd biome borders, missing RU biomes): set `improvedNetherBiomeSource = false` in `config/netherexp-startup.toml` (needs a restart). If the taller Nether causes problems: `netherWorldGenOverhaul = false`.
7. Botany Pots: run `/botanypots debug` with `gen_files` for JNE plants (and NDU kelp, if wanted).
8. Leave MNS's "replace vanilla fortress with Mega Fortress" option **off** (YUNG's handles fortresses).

---

## 7. Evidence log (sources examined)

- Modrinth API (`/v2/search`, `/v2/project/<slug>`, `/v2/project/<slug>/version?game_versions=["1.21.1"]&loaders=["neoforge"]`) for every project in §4.
- GitHub clones (read only), with commit and branch:
  - `Apollounknowndev/RegionsUnexplored` @ea78a0f (21.1, 16/08/2026): `RULithostitched.java`, `RUCommonConfig.java`, `BiomeTarget.java`, `RUBiomes.java`
  - `Apollounknowndev/lithostitched` @38779fe (21.1, 21/09/2026): `BiomeInjectorManager`, `InjectorBiomeSource`
  - `Glitchfiend/TerraBlender` @c903443 (1.21.1): `LevelUtils`, `MixinParameterList`
  - `Stardust-Labs-MC/Incendium` @fedbebc and `Amplified-Nether` @75f7e7e: default branch 1.20 only; the 1.21 ports are not public
  - `ThatJadenXgamer/Jadens-Nether-Expansion` @7ce1a25 (1.21.1, 29/08/2026): built-in packs, configs, mosaic entries, biome tags, registries
  - `ThatJadenXgamer/Elysium` @928baf6 (1.21.1): `MosaicBiomeSource`, `LevelUtilsMixin`
  - `Chaolux1/NetherExpansionDelight` @62b54b2 (1.21.1-neoforge)
  - `FinnSetchell/MoogsNetherStructures2` @4d4e4c4 (1.21-datapack, 20/09/2026)
  - `Scouter456/Nether_Depths_Upgrade` @0785943 (nether_depths_upgrade_1.21)
  - `wdiscute/starcatcher` @1cdfa153 (1.21.1, 16/10/2026): `DGSCFishProperties`, `DGNetherDepthsUpgradeFishes`, `DGStarcatcherFishes`
  - `lender544` Cataclysm @10e2113 (1.21, 04/10/2026): `CMWorldRegistry`, structure and biome tags
  - `Faboslav/friends-and-foes` 5.0.2; `YUNGs-Better-Fortresses` 1.21.1; `Sparse Structures` 1.21 (`MakeStructuresSparse`)
  - `Fuzss/eternalnether` @466374d (1.21.1); `ochotonida/gardens-of-the-dead` 1.21.x; `Theawsomelamp/pyrellium` 1.21.1-neoforge; `SuperMartijn642/FormationsNether` 1.21
  - Botany Pots 1.21.1 `common/src/main/resources/data/botanypots/recipe/`; Subtle Effects `GeyserType`
- Not verifiable from here: GitHub issue trackers (blocked to the fetcher) and CurseForge pages (proxy refused). The Hearths and DnT Nether contents come from their project pages.
