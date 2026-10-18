# XP banking for the 1.21.1 NeoForge pack (Pipez + Mekanism tanks)

Research date: 2026-10-17. I checked fluid IDs, tags and capabilities in source wherever a repo was available. For XP Obelisk, which ships no source here, I read the bundled jar with `javap`. Download counts are from Modrinth (MR) or from CurseForge (CF) mirrors (moddex/gdlauncher). I could not reach the CF API directly.

## TL;DR

1. **Cognition (formerly Experience Obelisk) 2.4.13**: best fit for "simple + fun + pipes/tanks".
   - The obelisk has a GUI to store or retrieve 1, 10 or all levels, with exact points kept. It soaks up nearby orbs, has an animated GeckoLib model and holds about 1072 levels.
   - It exposes a fluid handler on 5 sides (not the top). The fluid is `cognition:cognitium_source`, tagged `c:experience`, at 20 mB per point.
   - By default it also accepts Sophisticated Backpacks' XP fluid, so the backpack XP pump and magnet can feed it.
   - Fun extras: the Memory Tablet gives remote access and recovers your XP after death; the Fountain spits orbs.
   - Cost: the mod adds a lot of other content (tools, armor, enchanting blocks, Metamorpher, Dispeller). Its only new dependency is GeckoLib, which is already in the pack. MIT licence, about 18.8M CF downloads and used in about 1260 CF modpacks.
2. **No new mod: CEI Experience Lantern as a "deposit pad", then Pipez, then a Mekanism tank, withdrawing with an Experience Hatch on the Mekanism tank.**
   - Everything is already in the pack, and this is the densest storage (1 mB per point, so a Basic Mekanism tank holds about level 101).
   - Downside: withdrawing still uses the Hatch.
   - A Sophisticated backpack with Tank, XP Pump and Magnet upgrades is a good portable companion.
- **Global XP 1.12** is the simplest and cheapest bank, and very charming (a spinning emerald and a level nameplate). It is by the same author as XP Tome, which is already in the pack. It has **no fluid or pipe support**, so it fails the Pipez/Mekanism requirement.

## 1. XP-fluid conventions (the key compatibility facts)

| Fluid id | Mod | mB per XP point | `c:experience` tag? | Notes |
|---|---|---|---|---|
| `create_enchantment_industry:experience` | CEI 2.4.2 / 2.5.4b | **1** | **NO** (CEI tags only `c:dragon_breath`; XP is in `create:bottomless/deny` and its own `infusing/ingredients`) | Blaze Enchanter, Lantern and Printer accept only this fluid. |
| `sophisticatedcore:xp_still` | Sophisticated Core | 20 (`XpHelper.RATIO = 20`) | yes | The XP Pump and Magnet drain or fill any `c:experience` fluid at 20 mB per point. |
| `cognition:cognitium_source` | Cognition | 20 | yes (Cognition's tag file also adds MGU, CoFH, IF, Sophisticated, EnderIO and Reliquary fluids, each `required:false`) | |
| `mob_grinding_utils:fluid_xp` | MGU 1.1.10 | 20 | yes (also `c:xpjuice`; MGU also adds `pneumaticcraft:memory_essence` and `cofh_core:experience` to `c:experience`) | |
| `justdirethings:xp_fluid_source` | Just Dire Things | 20 | yes | |
| `xps:xp_fluid` | XP Obelisk 0.5.0 (Meridanus) | **10** (810 droplets per point ÷ 81 droplets per mB) | **NO**, and it is tagged **`minecraft:water`** | |
| Liquid Experience (closed source) | Liquid Experience 1.0.0 | about 37 (body says 27 XP per bucket) | unknown | |

The NeoForge 1.21.1 `Tags.Fluids.EXPERIENCE` javadoc says: "Standard unit for experience is 20mb per 1 experience". I checked this in NeoForge's 1.21.1 `Tags.java`.

CEI has its own **data map** `create_enchantment_industry:unit/experience`, which gives mB per point for foreign XP fluids. It ships the following entries, each loaded only if that mod is present. The map is identical in 2.4.2 and 2.5.4b:

- `sophisticatedcore:xp_still`: 20
- `mob_grinding_utils:fluid_xp`: 20
- `justdirethings:xp_fluid_source`: 20
- `enderio:xpjuice`: 20
- `industrialforegoing:essence`: 20
- `pneumaticcraft:memory_essence`: 20
- `cyclic:xpjuice`: 20
- `reliquary:xp_juice_still`: 20
- `cofh_core:experience`: 25

**Cognition is not in the map.** It is a one-line datapack fix: `data/create_enchantment_industry/data_maps/fluid/unit/experience.json` with `{"values":{"cognition:cognitium_source":20}}`.

**Duplication and loss analysis (current pack):** it is safe as long as CEI XP stays out of `c:experience`.
- Sophisticated XP Pump, MGU XP Tap and the c:experience tag only touch 20 mB fluids. The CEI Lantern and Blaze Enchanter only touch CEI fluid. Cognition only accepts cognitium plus an explicit allowlist, and its default allowlist (`mob_grinding_utils:fluid_xp`, `cofh_core:experience`, `industrialforegoing:essence`, `sophisticatedcore:xp_still`, `enderio:fluid_xp_juice_still`, `reliquary:xp_still`) does not include CEI.
- A Mekanism tank holds only one fluid, and Pipez only moves fluid. So these networks cannot cross-convert anything.
- **Do NOT** add CEI XP to `c:experience` (no KubeJS, Almost Unified or datapack tag). If you did, the Sophisticated pump would fill a tank that already holds CEI XP at 20 mB per point. That is 20x duplication when you later withdraw through the CEI Hatch. The MGU tap would also read CEI XP at 1/20 of its value.
- **Do NOT** add CEI XP to Cognition's `AllowedFluids`. The obelisk copies mB 1:1 into cognitium, so you would lose 95%.
- CEI Hatch quirk (both 2.4.2 and 2.5.4b): with a *foreign* fluid in its filter and the scroll set to "all" (0), a deposit puts the point count in as mB. Each click therefore stores only 1/20 of your XP. Nothing is duplicated; you just lose up to 19 mB of rounding. Use fixed amounts (10–1000 points) with foreign fluids. CEI's own fluid is exact.
- XP Obelisk (xps) accepts **any** fluid whose id contains `liquid_xp` or `xp_fluid` and values it at 10 mB per point. JDT's 20 mB `xp_fluid_source` would therefore be credited 2x. Neither is in the pack, but don't combine them.
- Clumps is safe. Clumps puts the merged total into `orb.value` (`clumps$resolve`). Global XP and the CEI Lantern read `orb.value`, and Cognition reads Clumps' `clumpedMap` explicitly.

## 2. What the existing pack can already do

Mekanism capacities:
- Basic, Advanced, Elite and Ultimate Fluid Tanks hold 32, 64, 128 and 256 B. They accept any fluid and fill the tank below when full.
- The Dynamic Tank holds **350 B per interior block** (`dynamicTankFluidPerTank = 350 * BUCKET_VOLUME` in GeneralConfig).

| Storage | CEI XP (1 mB per point) | 20 mB XP |
|---|---|---|
| Basic tank (32 B) | 32,000 points, about level 101 | 1,600 points, about level 31 |
| Ultimate tank (256 B) | about level 256 | 12,800 points, about level 69 |
| 3×3×3 Dynamic Tank (1 interior block) | about level 296 | about level 79 |

Pipez:
- Fluid pipes use `Capabilities.FluidHandler.BLOCK` (Pipez 1.21.1-1.2.31), so they move any fluid.
- Filters support tags such as `#c:experience` (you need an Advanced or Ultimate upgrade).

### A. CEI-only bank (0 new mods, densest)
- **Deposit:** the **Experience Lantern** (CEI) drains a player who stands in or against it, 50 points every 10 ticks (`experienceLanternDrainRate`). It pulls orbs within 10 blocks and absorbs them. It glows by fill level and has a 1000 mB buffer. It registers `FluidHandler.BLOCK`, so a Pipez extract pipe takes the fluid into a Mekanism tank.
- **Withdraw:** an **Experience Hatch** placed against the Mekanism tank. The hatch calls `level.getCapability(FluidHandler.BLOCK, tankPos, null)`, so it works on any fluid-handler block, not just Create tanks. You should still try it once on a Mekanism tank or Dynamic Valve in creative.
  - Right-click deposits.
  - Shift-right-click withdraws.
  - The value box sets the amount per click: "all", or 10 to 1000 points.
  - It is exact, with no level rounding.
- Bonus: the same fluid feeds the Blaze Enchanter, Printer and other CEI machines.
- Downside: it is still the Hatch UX, and there is no GUI.

### B. Sophisticated Backpacks (portable bank)
- Install the Tank upgrade (4000 mB per slot row, multiplied by stack upgrades) plus the **XP Pump** upgrade:
  - Modes are input, output, or keep at level N.
  - Buttons store or take N levels, or all.
  - An optional "mend items" setting.
- A **Magnet** upgrade sends XP orbs into the tank automatically.
- A placed backpack exposes `FluidHandler.BLOCK` (`BackpackBlockEntity::getExternalFluidHandler`), so Pipez can drain it into a Mekanism tank. To withdraw at the tank, use an Experience Hatch with a `sophisticatedcore:xp_bucket` filter. The unit (20) is already in CEI's data map; use fixed amounts because of the quirk above.
- It accepts only `c:experience` fluids, so no CEI XP.

### C. XP Tome
- An item that stores 1395 points by default (configurable via `max_xp`). It has no fluid capability.

## 3. Candidates

### Cognition (formerly Experience Obelisk), recommended
- **Version and maintenance:** 2.4.13 for 1.21.1, NeoForge only, released 2026-07-10. The repo's `1.21.1-neoforge` branch was still being committed to on 2026-08-07.
- **Licence and reach:** MIT. MR 124.7k downloads; CF about 18.8M downloads and about 1260 modpacks.
- **Jar size:** 659 KB.
- **Dependencies:** GeckoLib ≥4.7.5.1, required and already in the pack. Curios and JEI are optional. Nothing new.
- **Obelisk (`cognition:experience_obelisk`):**
  - GUI with Store 1 / 10 / all and Retrieve 1 / 10 / all levels, using exact level-to-point maths with partial progress.
  - Settings for absorb radius (default 2.5) and redstone control.
  - Absorbs orbs passively.
  - Capacity 100,000,000 mB, about 1072 levels (configurable).
  - Fluid handler on every side except UP (`getCapability` returns null for `Direction.UP`).
  - `isFluidValid` accepts cognitium plus the `AllowedFluids` config list, and converts input mB 1:1 into cognitium.
  - Output is cognitium (`c:experience`, 20 mB per point), so Pipez can extract to a Mekanism tank, and you can pipe back in either cognitium or `sophisticatedcore:xp_still`.
- **Fun extras:**
  - Memory Tablet: shift-right-click an obelisk to link it. You can then access the obelisk remotely, and after a death (without keepInventory) your full XP is recovered when you return to the obelisk.
  - Experience Fountain: bind it to the obelisk and it dispenses orbs at Slow, Moderate, Fast or Hyper rates.
  - Enlightened Amulet: an orb magnet.
  - Precision Dispeller: disenchanting.
- **Scope creep:** it also adds cognitive tools, armor, a bow and a rod; agar and "infected" bookshelves for enchanting; the Molecular Metamorpher; flasks; jellies; Mending neurogel; and chest-loot modifiers (desert pyramid, ruined portal, mineshaft, stronghold). It adds no world-gen ores. It fits a magic-leaning pack, but it is more than "one block".
- **Recipe path:** an early Nether trip.
  - Cognitive Flux (×4) = quartz + lapis + soul sand or soil. Smelt it into Amalgam.
  - Alloy = 4 Amalgam + copper. Crystal = 4 Amalgam + emerald.
  - Astute Assembly (×2) = 4 Alloy + 2 redstone + Crystal.
  - Obelisk = Crystal + Amalgam + 2 Alloy + Astute Assembly.
  - Total is roughly 9 quartz, 9 lapis, 9 soul sand, 6 copper, 2 emeralds and 2 redstone.
- **Simplest setup:**
  1. Place the obelisk and use the GUI to store and retrieve.
  2. Optionally run a Pipez fluid pipe, extracting from a side or the bottom, into a Mekanism tank as overflow. Note that one Basic tank holds only about level 31 of cognitium; the obelisk itself is the bank.
  3. Optionally place a Sophisticated backpack (Tank + XP Pump + Magnet) next to it and pipe its `xp_still` into the obelisk, which accepts it by default.
  4. Keep CEI XP in a separate tank for the CEI machines.
  5. If you want CEI's Hatch to understand cognitium, add the data-map datapack line from section 1.

### Global XP (bl4ckscor3)
- **Version:** v1.12 for NeoForge 1.21 and 1.21.1, released 2024-08-19. It is the latest 1.21.1 NeoForge build; the project is still updated for newer MC (2026-10-12).
- **Licence and reach:** MIT. MR 120k downloads; CF about 15.4M downloads and about 1395 modpacks.
- **Dependencies:** none. The jar is 45 KB.
- **XP Block:** recipe is 8 iron bars around an emerald.
  - Sneak-right-click with an empty hand stores all your XP. Right-click withdraws until your next level (configurable to all, or a fixed amount).
  - Keeps its contents when broken.
  - Holds up to about 2.1 billion points (int).
  - Picks up orbs within 3 blocks (redstone disables this).
  - Comparator output.
  - Floating nameplate showing levels; supports anvil names.
  - A spinning, bobbing emerald.
  - Optional retrieval percentage, if you want a "fee".
- **No fluid:** no capability or fluid code at all (checked the `neoforge/1.21` branch). It is not pipe- or Mekanism-compatible.
- **Simplest setup:** craft it and click it. It pairs well with XP Tome from the same author.

### Mob Grinding Utils (vadis365 / Flanks255)
- **Version:** 1.1.10+mc1.21.1, released 2025-07-23.
- **Licence and availability:** "All rights reserved". CurseForge only, with about 112–116M total downloads.
- **Dependencies:** only NeoForge.
- **XP blocks:**
  - Singularity Tank: 32 B, about level 31.
  - Jumbo Tank: 1024 B, about level 124.
  - XP Drain Singularity Tank: stand on it and it drains 1 point per tick into itself.
  - XP Tap: attach it to **any** fluid-handler block whose first tank holds a `c:experience` fluid with at least 20 mB. A redstone signal turns it into orbs. This works on a Mekanism tank or on Sophisticated or Cognition XP.
  - Absorption Hopper: vacuums orbs and items over 7×7×7.
  - XP Solidifier and moulds.
- **Fluid:** `mob_grinding_utils:fluid_xp`, 20 mB per point, tagged `c:experience`.
- **Caveats:**
  - Withdrawing gives orbs, so Mending soaks them up first and the amount is not exact.
  - There is no "give me N levels" button.
  - It also adds mob-farm toys (fans, spikes, saw, Mob Masher, dirt spawners, mufflers, chicken feed), which overlap Apothic Spawners and Easy Mob Farm.
  - It cannot go into an `.mrpack` as a download (CF-only, ARR).
  - Its last update was July 2025.
- **Simplest setup:** an XP Drain tank as the deposit pad, then Pipez into a Mekanism tank, with an XP Tap on the Mekanism tank and a lever to withdraw.

### Just Dire Things (Direwolf20)
- **Version:** JustDireThings 1.5.x–1.6.x for 1.21.1 (repo `1.21.1` branch is at mod_version 1.5.7).
- **Licence and reach:** MIT. CF only, about 20.8M downloads.
- **Experience Holder:** GUI to deposit and withdraw levels; collects orbs; effectively unlimited capacity.
- **Fluid:** fluid handler with `justdirethings:xp_fluid_source` (c:experience, 20 mB per point). It accepts c:experience fluids.
- Very good mechanically, but it is a huge mod (4 resource tiers, tools, armor, machines, portals, a time wand). That is far too much scope for "an XP bank".

### XP Obelisk 0.5.0 + XP Obelisk Additions 0.2.0 (Meridanus)
- **Licence and dependencies:** MIT. Requires Architectury, which is in the pack.
- **Availability:**
  - Additions 0.2.0 for NeoForge is on MR (2026-08-29, 80 downloads) and requires XP Obelisk ≥0.5.0.
  - The base mod has **no NeoForge 1.21.1 build on Modrinth** (the MR project is Fabric 1.18–1.19 only). The NeoForge 0.5.0+1.21.1 jar exists in the Additions repo's `depend/` folder, but I could not verify that it is published on CF.
- **Content:** the "XP Storage" block, plus XP berries (a bush that grows XP), XP dust, an XP Rod, an XP Transfer item, lock and key, a Soulcopper set, and a Patchouli handbook (works without Patchouli but shows "Patchouli missing").
- **Fluid:** `xps:xp_fluid` at **10 mB per point**. It is *not* tagged `c:experience` but *is* tagged `minecraft:water`, so it hydrates and acts as water.
- **Fluid handler:** accepts any fluid whose id contains `xp_fluid` or `liquid_xp`, which is a duplication hazard.
- **Additions:** an XP Item Inserter (bottles, berries and buckets into the obelisk) and an XP Enchanter (enchanting that pays from the obelisk).
- **Verdict:** not recommended (odd fluid ratio, water tag, availability).

### Liquid Experience 1.0.0
- **Release:** 2026-06-01, NeoForge 1.21.1 only.
- **Licence and source:** ARR, no source code, 420 downloads.
- **Content:**
  - A bucket holds 27 XP, so roughly 37 mB per point; non-standard.
  - Player Experience Drain: stand-on, with tiers.
  - Experience Repository: placed on a tank. Left-click gains 1 level, right-click deposits 1 level, and crouching makes it 10.
  - Apothic Enchanting stats from a tank under the enchanting table.
- **Dependencies:** relies on Fluidic Tanks (ARR, about 4.4k downloads), listed as an "optional" dependency but described as installed alongside.
- I could not verify the tags or capabilities. **Not recommended.**

### Better Exp Storage 0.1.0-beta
- NeoForge 1.21.1, released 2026-07-28. WTFPL, no source, 335 downloads, alpha/beta.
- Adds Exp Storage Books (tiers), an Exp Hypercube (about 100M XP, stated as 2.1B mB), an Exp Collector and an Exp Generator (FE).
- I could not verify whether it has a fluid handler. Too immature.

### Others (not storage or not suitable)
- **Bottle Your Xp 3.6:** released 2026-10-02, ARR. Needs **Collective**, which is *not* in the pack. Turns your XP into Bottles o' Enchanting. Lossy and item-only, though the bottles can go through an Item Drain into CEI fluid.
- **Easy Mob Farm 11.0.0:** not an XP store. Its Experience Enhancement only makes farms drop Bottles o' Enchanting.
- **Exp Save mod:** ARR, about 340 downloads, closed source. An "Iron Experience Storage Box" that pays out in XP items.
- **XP Crystals, Sculk Vials, XP Tablets, XP Bank, Storable XP:** item-based. No fluid.
- **ExperienceLib:** library only. **Applied Experienced:** needs AE2.
- **EnderIO, Industrial Foregoing, Cyclic, PneumaticCraft, Reliquary:** have XP fluids (all listed in CEI's map) but are huge mods. Not worth it for an XP bank.

## 4. Recommendation

1. **Add Cognition** and use the Experience Obelisk as the XP bank.
   - Pipe cognitium to and from Mekanism tanks with Pipez if you want overflow, or feed it from a Sophisticated backpack (XP Pump + Magnet).
   - Optionally add the one-line CEI data-map datapack so the Hatch also understands cognitium.
   - It offers the best mix of simple GUI clicks, a fun model, Memory Tablet death recovery and full fluid compatibility. Its new dependency (GeckoLib) is already in the pack, and it is MIT and maintained.
2. **Zero-mod alternative:** CEI Experience Lantern (stand-on deposit) → Pipez → Mekanism tank (1 mB per point, densest) → Experience Hatch to withdraw. Keep this line anyway for the CEI machines.

Alternatives, one line each:
- Global XP: simplest and cutest bank block, but no fluids.
- Mob Grinding Utils: XP drain tank and XP Tap work with any c:experience tank; ARR, CF-only, orbs-only withdrawal.
- Just Dire Things: excellent Experience Holder, but a huge mod.
- XP Obelisk (Meridanus): 10 mB per point, water-tagged fluid, NeoForge build not on Modrinth.
- Liquid Experience: ARR, closed source, non-standard ratio.
- Better Exp Storage: beta, closed source.
- Bottle Your Xp: needs Collective; lossy bottles.

## Sources
- Modrinth API (search and project/version endpoints) for global-xp, cognition, bottle-your-xp, xp-obelisk, xp-obelisk-additions, liquid-experience, fluidic-tanks, better-exp-storage, exp-save-mod and experiencelib.
- Source checked:
  - CEI (DragonsPlusMinecraft) 2.5.4b and 2.4.2: `CEIFluids`, `ExperienceHatchBlock` and `ExperienceHatchBehaviour`, `ExperienceHelper`, `ExperienceLanternBlockEntity`, `CEIDataMaps`, `data_maps/fluid/unit/experience.json`, tags.
  - Sophisticated Core (`ModFluids`, `XpHelper`, `XpPumpUpgradeWrapper`, `TankUpgradeConfig`) and Sophisticated Backpacks `ModBlocks`.
  - Cognition `1.21.1-neoforge` branch (`ExperienceObeliskEntity`, `RegisterCapabilities`, `Config`, tags, recipes, `MemoryTabletItem`).
  - Mob Grinding Utils `MC1.21.1` branch.
  - GlobalXP `neoforge/1.21` branch.
  - JustDireThings `1.21.1` branch.
  - XP Obelisk Additions `1.21.1` branch, plus the bundled `xp_obelisk-neoforge-0.5.0+1.21.1.jar` read with javap.
  - Pipez 1.21.1, Mekanism (`GeneralConfig`, `TileEntityFluidTank`), NeoForge 1.21.1 `Tags.java`, Clumps 1.21.1 `MixinExperienceOrb`.
- CurseForge mirrors: https://moddex.gg/mod/mob-grinding-utils, https://gdlauncher.com/mods/curseforge/mob-grinding-utils, https://moddex.gg/mod/cognition-mod, https://moddex.gg/mod/global-xp, https://moddex.gg/mod/just-dire-things
- https://www.mado-hosting.com/minecraft-mods/better-exp-storage, https://www.mado-hosting.com/minecraft-mods/experience-storage, https://moddex.gg/mod/mr-92JGvR9L (XP Extractor, Fabric only)
