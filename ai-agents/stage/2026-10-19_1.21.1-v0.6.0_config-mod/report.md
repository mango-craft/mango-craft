# Config research for the planned 0.6.0 settings (Minecraft 1.21.1 NeoForge)

Raw report of a research agent, 19/10/2026, for pack version 0.6.0 (in design). Kept as it was delivered; the Italian distillate is in `1.21.1/mod-knowledge/` (one sheet per mod) and in `1.21.1/lavoro/versioni/v0.6.0.md`.

Source clones were under the agent's scratch folder (`agent-config/src/`), not in the repository.

## Corrections to 0302 and the brief

1. **Jaden's: the planned file is wrong.** `netherWorldGenOverhaul` and `improvedNetherBiomeSource` live in `config/netherexp-common.toml`, section `[worldSettings]`. They are not in `netherexp-startup.toml [packSettings]`, which only holds `soulCampfireSoulSoil`.
2. **Server configs on NeoForge 1.21.1** are global: `config/<modid>-server.toml`. A copy in `saves/<world>/serverconfig/` overrides it for that world. `defaultconfigs/` is not used for this.
   - Source: NeoForge branch `1.21.1` @e0e7ab5, `ServerLifecycleHooks.java` L68-96: `loadConfigs(SERVER, CONFIGDIR, <world>/serverconfig)`. Same code at commit 5700ea2 (2024-08-01). FML `ConfigTracker.resolveBasePath`.
3. **Every Compat: all 12 modules active in the pack are on the "keep" list.** They are create, farmersdelight, friendsandfoes, handcrafted, mcwbridges, mcwpaths, mcwroofs, mcwwindows, rechiseled, regions_unexplored, storagedrawers and twilightforest.
   - There is no Botany Pots module. The only Botany Pots code is a helper for Quark hedges, and Quark is not in the pack.
   - So "turn off useless modules" removes nothing. B22 can only shrink by dropping or cutting Rechiseled, or by blacklisting wood types.
4. **Sparse Structures: a partial file is NOT safe** (details in section 8).

## General rule for NeoForge TOML (applies wherever it says "NeoForge TOML" below)

- A partial file works. Missing keys get their default. An invalid value is reset to its default one key at a time. Unknown keys are removed.
- When it corrects a file, NeoForge makes a backup and rewrites it. The whole file is only recreated if it can't be parsed.
- Source: FML branch `1.21.1` @44982c6, `ConfigTracker.loadConfig` L160-196; NeoForge `ModConfigSpec.correct` L204-283.
- Advice: ship complete files. A partial file gets "corrected" on first launch (backup, rewrite, log warning), which is the kind of message already listed in B14.

## 1. Every Compat 2.11.54 + Moonlight 3.7.2

Sources: WoodGood @bdb551e8 ("CHANGELOG - v2.11.54", 2026-10-17, same day as the Modrinth release) and Moonlight @1a3802e8 (the 3.7.2 version bump).

File names come from `ModConfigHolder` L86 (`namespace-path.toml`). The files are written by `ForgeConfigHolder` as COMMON or CLIENT configs in `config/`, so they behave like NeoForge TOML (partial OK).

| file | side | key | default | planned / option | partial OK? |
|---|---|---|---|---|---|
| `everycomp-hazardous.toml` | common | `[module] blacklist` | `[]` | e.g. `["rechiseled"]`. Exact mod id, no regex. | yes |
| same | common | `[entryset] blacklist` | `[]` | Regex on `modid:entry`, e.g. `"rechiseled:.*_connecting"` | yes |
| same | common | `[woodtype] blacklist` / `[leavestype] blacklist` | `[]` | Regex on the wood id, e.g. `"deep_aether:.*"` | yes |
| same | common | `[block] blacklist` | `[]` | Regex on `module/woodNamespace/block` | yes |
| same | common | `[other] include_all_wood_modules` | `true` | `false` turns off every module | yes |
| `everycomp-entries.toml` | common | `[types.wood_type.<ns>] <wood> = true`, `[entries.wood_type.<modid>] <entry> = true` | all `true` | Hides only (see below) | yes |
| `everycomp-client.toml` | client | `[general] dynamic_assets_generation_mode` | `"ALWAYS"` | NEVER / RUN_ONCE / CACHED / CACHED_ZIPPED / ALWAYS | yes |
| `everycomp-common.toml` | common | `[general] server_assets_generation_mode` | `"ALWAYS"` | same choices; needs a world reload | yes |
| same | common | `[general] generate_blocktype_tags` | `true` | `false`: the source says it "can make pack a bit faster" | yes |
| `moonlight-common.toml` | common (synced) | `[general] multi_threaded_generation` / `faster_cache_search` | `true` / `true` | leave | yes |
| `moonlight-client.toml` | client | `[general] merge_dynamic_resource_packs` | `true` | leave | yes |

**Which file actually removes blocks**
- Only `hazardous` stops registration. The module blacklist is checked in `EveryCompat.addModule/addOptionalModule` (L233-280). The other lists are checked in `HardcodedBlockType` L31-37, which `SimpleEntrySet` L150-153 calls before it registers anything.
- Disabling a module this way removes its blocks for good. In an existing world they should turn to air (vanilla behaviour, not checked in source).
- The `entries` file, in its own comment, "only hide[s] stuff from tabs and disable[s] their recipes". Assets are still generated for every block (`ResourcesUtils` L80/197: `if (true || …)`). It does not help B22.
- The hazardous file warns "modpack makers DO NOT use it", but the reason is joining servers with a different config. That does not apply to a single-player pack where client and server read the same file.

**Rechiseled module size**
- It has 37 block entries × 3 (block, slab, stairs) = 111 per wood type.
- 54 of those are `_connecting` variants. `[entryset] blacklist = ["rechiseled:.*_connecting"]` would roughly halve the module.

**The log line `REGEN_ON_EVERY_RELOAD`**
- This is Every Compat's own `ALWAYS` mode (`ECConfigs.GenMode.pickStrategy`). Moonlight has no cache-strategy setting of its own.
- `RUN_ONCE`: generates once per session and skips regeneration on F3+T or resource reloads. This is relevant to B33.
- `CACHED` / `CACHED_ZIPPED`: write to `dynamic-resource-pack-cache/` and `dynamic-data-pack-cache/` in the instance. They regenerate only when the fingerprint changes (`GlobalCachedStrategy`).
  - The fingerprint is the list of mods with versions plus the non-mod resource packs.
  - Every Compat's options never call `affectsDynamicPacks()`, so hand-editing its TOML does not invalidate the cache. Those two folders must be deleted after each Every Compat config change.
- Every Compat 2.11.54 has 64 module ids in total (`EveryCompatCommon.addModules` and `EveryCompatForge.addModules`). Other mods can also register modules through `EveryCompatAPI`; I found none in the inventory.

## 2. Artifacts 13.2.5

Source: ochotonida/artifacts @7cf7dc42 ("Update 13.2.5").

| file | side | key | default | planned | partial OK? |
|---|---|---|---|---|---|
| `config/artifacts/general.toml` | one common file, both sides | `[slots] enableAccessoriesCompat` | `true` | `false` | yes |
| same | same | `[slots] enableCuriosCompat` | `true` | `true` | yes |
| same | same | `artifactRarity` (top level) | `1.0` | — | yes |

- Both slot keys are `requiresRestart`.
- They work through data overlays in `pack.mcmeta`: `overlay_disable_accessories` empties the `accessories` slot tags (`GeneralConfig.java`, `neoforge/src/main/resources/pack.mcmeta`).
- The file is not a NeoForge config. It is read with night-config by Artifacts' own `ConfigManager`, which adds missing keys with defaults, so a partial file works.

## 3. Jaden's Nether Expansion 2.4.1

Source: branch 1.21.1 @0e5a1ea ("2.4.1"). Files: `JNEConfigImpl.java` L30, L474-505, L825-831; `NetherExp.java` L21-22.

| file | side | key | default | planned (fallback only) | partial OK? |
|---|---|---|---|---|---|
| `config/netherexp-common.toml` | COMMON | `[worldSettings] netherWorldGenOverhaul` | `true` | `false` | yes (NeoForge TOML) |
| same | COMMON | `[worldSettings] improvedNetherBiomeSource` | `true` | `false` | yes |

- Both need a game restart (`gameRestart()`).
- They switch the built-in datapacks `netherexp:nether_worldgen_overhaul` and `netherexp:nether_mosaic_biome_source` on or off (`JNEBuiltinPacks.java` L41-60).
- `netherexp-startup.toml` contains only `startupSettings` (splash texts, profanity, developerMode) and `packSettings.soulCampfireSoulSoil`.

## 4. Smaller mods

| mod | file | side | key | default | planned | partial OK? | source |
|---|---|---|---|---|---|---|---|
| Carry On 2.2.6 | `config/carryon-common.toml` | COMMON | `[settings] pickupAllBlocks` | `false` | `true` | yes (NeoForge TOML) | Tschipp/CarryOn 1.21.1 @9f1cf66, `CarryConfig.java` L31-110, `ConfigLoaderImpl.java` L45-52 |
| FallingTree 1.21.1.11 | `config/fallingtree.json` (Gson) | read on both sides; the server syncs it to the client | `sneakMode` | `"SNEAK_DISABLE"` | `"SNEAK_ENABLE"`: fells only while sneaking (`IGNORE` = always) | yes, if the JSON is valid: classes have no-arg constructors, missing fields keep defaults, the file is rewritten | RakambdaOrg/FallingTree minecraft/1.21.1 @15173b7, `Configuration.java` L34/L68, `SneakMode.java` |
| Inventory Essentials 21.1.20 | `config/inventoryessentials-common.toml` | COMMON | `enableShiftDrag` (top level) | `true` | `false` | yes (NeoForge TOML via Balm 21.0.66) | tag v21.1.20 `InventoryEssentialsConfigData.java`; Balm v21.0.66 `NeoForgeBalmConfig.java` L276-289; legacy `@Config` maps to `:common` |
| Traveler's Backpack 10.1.39 | `config/travelersbackpack-server.toml` (per-world override in `saves/<w>/serverconfig/`) | SERVER | `[server.backpackSettings] allowShulkerBoxes` | `false` | `true` if wanted | yes | 1.21-neoforge @a913d503, `TravelersBackpackConfig.java` L28-33, L279-281 |
| Subtle Effects 1.15.0 | `config/subtle_effects/blocks.toml` (Fzzy Config 0.7.7) | CLIENT only | `rainWaterRipples` (+ `rainWaterRipplesDensity` 0.35) | `true` | `false` only if ripples double up | yes: Fzzy logs "missing" and rewrites the full file | SubtleEffects main @39c079dd, `ModBlockConfigs.java` L154-155, `ModConfigs.register` (CLIENT); fzzy neo/1.21 @274e61c, `ValidatedBoolean()` = true, `ConfigApiImpl` L290-312 |
| Sound Physics Remastered 1.5.1 | `config/sound_physics_remastered/soundphysics.properties` | client | quality keys below | see below | lower if CPU-heavy | yes: a missing key gets its default | henkelmax/sound-physics-remastered 1.21.1 @f0037e3, `SoundPhysicsConfig.java` L118-160, `SoundPhysicsMod.java` L41; config-builder `AbstractConfigEntry.reload()` |
| Cognition 2.4.13 | `config/cognition-common.toml` | COMMON | `["Allowed Experience Fluids"] AllowedFluids` | list of 6: mob_grinding_utils:fluid_xp, cofh_core:experience, industrialforegoing:essence, sophisticatedcore:xp_still, enderio:fluid_xp_juice_still, reliquary:xp_still | leave unchanged, no file needed | yes | Experience-Obelisk 1.21.1-neoforge @02edb80, `Config.java` L55-69, `Cognition.java` L27 |

Notes on these mods:
- **Carry On:** the default blacklist does contain `create:*`, `enderstorage:*`, `create_enchantment_industry:*`, `mekanismgenerators:wind_generator` and `heat_generator`, as 0302 says.
- **Traveler's Backpack:** the open key **B** is a vanilla keybinding (`key.travelersbackpack.inventory`, `GLFW_KEY_B`, `ModClientEventHandler.java` L55). It is stored in `options.txt`, not in a mod config, so it can only be changed in-game or by shipping `options.txt`. That would clash with the decision not to ship video settings.
  - With `allowShulkerBoxes` on, any item whose `canFitInsideContainerItems()` is false is allowed. Traveler's backpacks and the `travelersbackpack:blacklisted_items` tag stay excluded (`BackpackSlotItemHandler` L27).
- **Subtle Effects:** it detects Particle Rain only for its mist particle. There is no automatic handling of ripples.
- **Sound Physics quality keys** (default, allowed range):
  - `environment_evaluation_ray_count` 32 (8–64)
  - `environment_evaluation_ray_bounces` 4 (2–64)
  - `max_occlusion_rays` 16 (1–128)
  - `strict_occlusion` false
  - `sound_direction_evaluation` true
  - `redirect_non_occluded_sounds` true
  - `update_moving_sounds` false
  - `sound_update_interval` 5
  - `max_sound_processing_distance` 512
  - `evaluate_ambient_sounds` false
- **Cognition:** `isFluidValid` only checks whether the fluid is in the list. The comment "must be tagged" is not enforced, which supports the 0303 rule never to add the Create liquid there (`ExperienceObeliskEntity.java` L292-298).

## 8. Sparse Structures 3.0

| file | side | key | default (shipped template) | planned | partial OK? |
|---|---|---|---|---|---|
| `config/sparsestructures.json5` | both (read during worldgen registry load) | `spreadFactor`, `idBasedSalt`, `customSpreadFactors: [{ "structure": "<set or structure id>", "factor": n }]` | 2, true, mansion 2 | pack: 1.4 / villages 1 / mansion 2 (+ D&T 3, WDA 2) | **NO** |

- **Why a partial file breaks:** Gson reads it into a class with no no-arg constructor. A missing `spreadFactor` becomes 0, which turns off all structures. A missing `customSpreadFactors` becomes null and crashes the loader.
- The pack's file has all three keys.
- Format confirmed as `structure`/`factor`; the Modrinth description, which says `name`, is wrong.
- First match wins and replaces the global factor; it is not multiplied. Factor 0 sets frequency 0. Concentric-ring sets (strongholds) are skipped. A trailing comma in the list becomes a null entry, which is skipped.
- Source: MaxenceDC/sparsestructures tag v3.0 @6cc5bf6. That is the 1.21.5 port: `SparseStructuresCommon.java`, `SparseStructuresConfig.java`, `neoforge/.../MakeStructuresSparse.java`, `Constants.java` L13-15.

## 9. Moog's Nether Structures 3.1.1 (+ Moog's Structure Lib 3.4.2)

| file | side | key | default | planned | partial OK? |
|---|---|---|---|---|---|
| `config/moogs_structures.json` (global, written by the Lib) | common | `presets.mns.replace_nether_fortress` | `false` (`default_enabled` from MNS) | keep `false` | yes: missing keys get defaults, file rewritten |

- The preset is declared in MNS at `data/mns/moogs_structures/replace_vanilla.json` (tag `3.1.1-1.21` @e353f0a).
- The Lib reads and merges it in `MslConfig.loadAndSync` and `ReplaceVanillaManager` (MoogsStructureLib tag 3.4.2-neoforge @6d45e5f).
- With the preset off, the mega fortress still generates as its own rarer set (`mns:mega_fortress`, spacing 116 / separation 76 before the Lib's ×1.65). The preset only adds the tighter "when replacing" spacing in place of the vanilla fortress (`AdvancedRandomSpread` L118-146).

## Could not verify

- **Exact release commits.** These repos have no tags for the shipped builds, so I picked commits by version bump or Modrinth date:
  - Every Compat: @bdb551e8.
  - Moonlight 3.7.2: the bump commit is dated 2026-10-14, but Modrinth published 2026-10-10.
  - Carry On build .13, FallingTree, Cognition, Traveler's Backpack.
  - Sparse Structures: the 1.21.1 port has no public source. I read the 1.21.5 v3.0 tag.
- **NeoForge 21.1.259 / its FML version.** The repo has no tag for it; I read the `1.21.1` branch heads.
- **Every Compat at runtime:** per-module block counts and the list of wood types in the pack can't be computed here. The `everycomp-entries.toml` generated in the dev instance lists every wood type and entry.
- **Removed Every Compat blocks becoming air** in an existing world: expected vanilla behaviour, not checked in source.
- **packwiz-installer:** whether it re-downloads a shipped config after the game rewrites it.
- **Sound Physics:** which config-builder version is bundled in the jar; I read master from 2025-08-19.
- **Subtle Effects + Particle Rain:** whether ripples really double up.
- **Sophisticated backpacks inside Traveler's:** whether `allowShulkerBoxes` lets them in depends on Sophisticated's code, which I didn't check.
- **Moog's Structure Lib frequency multipliers** (`frequency.*`) stacking with Sparse Structures on Moog's sets: not analysed.
