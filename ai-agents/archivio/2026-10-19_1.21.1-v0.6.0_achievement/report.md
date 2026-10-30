# Achievements research (NeoForge 1.21.1)

Raw report of a research agent, 19/10/2026, during the design of pack version 0.6.0. Kept as it was delivered; the Italian distillate is in `1.21.1/mod-knowledge/tema-achievement.md` and `1.21.1/lavoro/versioni/v0.6.0.md`.

## 1. Mods for the advancement screen and notifications

These are the latest NeoForge 1.21.1 builds according to the Modrinth API.

| Mod (slug) | Latest NF 1.21.1 | Licence · downloads | Deps | What it does / caveats |
|---|---|---|---|---|
| **Better Advancements** (`better-advancements`) | 0.4.3.21 · `FjTYILOi` · **beta** · 2024-10-27 | Dont-Be-a-Jerk (non-commercial) · 27.4M total, 1.9M for this file | none, client-only | Screen fills the window, custom colours, criteria list (config), inventory button. **No search.** The 1.21.1 build is 2 years old and the repo has no 1.21.1 branch. The GitHub issues page for "huge tree" problems was blocked here, so known issues are **not verified**. |
| **Reliable Advancements** (`reliable-advancements`) | 6.3.1+1.21.1-neoforge · `J5weQWAm` · release · 2026-10-15 | MIT · 478k | optional YACL (not in pack, only for the config GUI) | Fork of Better Advancements with all its features, plus free layout, pan and zoom, a criteria view and tab sorting. Has an **in-game editor** (create, edit or delete advancements) that writes plain JSON to `config/reliable_advancements_edits/data/<ns>/advancement/…`. Option `requireRewardClaiming`. Editor is off by default and needs op (cheats on in single player). Listed incompatible with Better Advancements, Clickable Advancements and Advancements Arranged. Moves fast (6.0 to 6.3.1 in about 2 months, many sync fixes), so expect churn. 6.3.1 batches background drawing to speed up large tabs. |
| **Lucid Advancements** (`lucid-advancements`) | 1.2.21 · `ei0eVl2W` · release · 2026-10-11 | GPL-3.0+ · 8.8k | none, client-only | A **list** instead of a tree: one view across all tabs, search with `@modid`, filters, **global and per-tab progress bars**, pin advancements to a HUD tracker. Requirement texts are translated into **Italian**. "Designed with large modpacks in mind". New (June 2026) and small user base. |
| **Advancements Reloaded / AdvancementInfo** (`advancements-reloaded`) | 0.6.1 · `bLJZSBmQ` · beta · 2024-10-22 | MIT · 967k | Cloth Config (in pack) | Larger UI with fixed ordering. Search only arrived in 0.9.0 (MC 1.21.5+), so the **1.21.1 build has no search**. Known issue: may break with other screen mods. Stale. |
| ForgedPaginatedAdvancements | 0.0.2 · `aAD33IiT` · release · 2025-10-20 | MIT · 130k | Cloth Config | Pages through tabs when there are many. Unofficial port. |
| **Advancement Plaques** (`advancement-plaques`) | 1.6.8 · `OWylG33I` · release · 2024-11-15 | CC-BY-NC-ND · 18.2M | **Iceberg** (required, not in pack), Prism lib (optional) | Glowing plaques instead of pop-ups. Config by frame type (task/goal/challenge), screen position and a whitelist. On NeoForge the custom sounds need the server side (fine in single player). |
| **Fancy Toasts** (`fancy-toasts`) | 1.5.0 · `L1OaPVbd` · release · 2026-08-24 | MIT · 1.85M | none | 8 styles, 4 animations, a sound per frame type. Supports FTB Quests and Questlog toasts. Does not work with Toast Control (not in pack). |
| Just Enough Advancements (`jea`) | 21.1.1 · `yslMBOHV` · beta · 2025-11 | Apache · 168k | JEI (in pack) + **LibX** (not in pack), needed on both sides | Advancements become searchable in JEI. Not verified whether this works through EMI. |
| Achievements Optimizer (`achievements-optimizer`) | 2.1.0 · `qHMtEGz4` · release · 2025-08-17 | MIT · 1.2M | none | Speeds up the item-pickup checks behind recipe-unlock advancements. Relevant because the pack has about 10.8k advancement files, mostly recipe unlocks. Alternative: Cerulean 1.0.0 (GPL, needs TxniLib). Use one, not both, and measure first. |
| Advancements Debug | — | — | — | Fabric only, up to 1.19.3: **not usable**. |

## 2. Pack-wide progression: quest mods vs our own datapack

- **FTB Quests** 2101.1.36 (GitHub `1.21.1/main`, 2026-09-15):
  - **CurseForge only**, licence **ARR**.
  - Needs FTB Library and **FTB Teams** (both new) plus Architectury (already in pack).
  - Best in-game editor. 19 task types (including advancement, structure, stat) and 16 reward types (item, XP, loot, choice, command, advancement…).
  - Since 2101.1.31, single-player worlds with cheats off cannot edit the quest book.
  - Already rejected in `0602` ("bisognerebbe scriversi le quest da soli"). 🔴
- **Odyssey Quests (= Heracles)**, slug `odyssey-quests`, 2.0.3 · `DYaRmc9w` · **beta** · 2026-10-18:
  - MIT; needs Resourceful Lib (in pack, 3.0.12).
  - Tree-style quests with an in-game editor; text in Markdown.
  - Quests are JSON under `config/heracles/quests`.
  - 17 task types (advancement, recipe, gather, kill, biome, structure…); rewards are items, loot table, selectable, command, XP.
  - 2.0 is a two-week-old rewrite with 4 fixes in 14 days. 🟡/🔴 for now.
- **Questlog** (`questlog`) 3.3.2 · `Sah2CQqd` · release · 2026-08-01:
  - Apache-2.0; needs Cloth Config (in pack).
  - Quests are JSON in `config/questlog/{quests,chapters}`, with an in-game edit mode.
  - About 30 objective types (including advancement, structure, biome, craft) and rewards (item, XP, loot table, command, choice, random).
  - Book/checklist layout built to explain things to the player, so it also fits the open "Guida del pack" topic (`0503`).
  - GitHub already has 3.4.1, which is not on Modrinth for NF 1.21.1. 🟡
- **Our own advancements in `matteo_tweaks`**:
  - No new mods. Plain JSON, versioned in git and checked by `check_ids.py`.
  - Each file can carry `neoforge:conditions` with `mod_loaded`, so removing a mod causes no errors.
  - Can make our own tab and point parents at modded advancements.
  - Rewards: `experience`, `loot`, `recipes`, `function` (a function can run any command).
  - Limits:
    - Vanilla has no "advancement completed" trigger. Chaining goals, or "do N of these", needs function rewards that grant criteria.
    - No in-game editor unless we add Reliable Advancements, whose editor exports compatible JSON to copy into the datapack (its extra fields such as multi-parent and `better_tab` need checking).
    - Layout is automatic and the vanilla screen is small, so this pairs with a screen mod.
  - Upkeep is low: only IDs can break, and the inventory catches that. 🟢

## 3. How many advancements the pack already has

The inventory stores advancements in `data_counts.advancement` as a single number per jar: no IDs, no split by namespace, and **recipe-unlock files are included**.
- **Total: 10,769 files in 98 mod jars**, plus 1,399 from vanilla (vanilla 1.21.1 has 1,400 files, of which **122 are real** in 5 tabs; checked against misode/mcmeta).
- Two jars still use the old 1.20 folder `advancements/`, which 1.21.1 ignores: animalpens (2 files) and nether-depths-upgrade (4). Harmless.
- To get the real counts I listed the mods' GitHub source trees and dropped `recipes/`. Source totals match the inventory closely for Create, TF, FD, Handcrafted, Deeper Darker and Undergarden. Ars, Bountiful Fares and Deep Aether were read from source branches that may not match the pack's version, so their counts are approximate.

| # | Mod | Inventory files | Real (from source) |
|---|---|---|---|
| 1 | Create | 1150 | **102** (85 visible, 17 hidden) |
| 2 | Occultism | 1131 | **221** (45 visible, 158 hidden until earned, 18 without display; its book does not use them) |
| 3 | Regions Unexplored | 638 | not checked (repo not reachable; 622 of the files match ordinary crafting recipes) |
| 4 | Twilight Forest | 545 | **45** |
| 5 | Bountiful Fares | 408 | ~19 |
| 6 | Undergarden | 377 | 37 |
| 7 | Deep Aether | 377 | ~6 |
| 8 | Ars Nouveau | 344 | ~39 |
| 9 | Aether | 343 | 31 |
| 10 | Supplementaries | 330 | 9 (2 visible) |
| 11 | Handcrafted | 317 | **0** (all recipe unlocks) |
| 12 | Deeper Darker | 264 | 11 |
| 13 | Rustic Delight | 256 | not checked |
| 14 | Corail Tombstone | 238 | not checked (closed source) |
| 15 | Farmer's Delight | 218 | **21** |

Others checked: Mekanism 97 (+4 Generators, all real, no recipe unlocks), Psi 41, Reactive ≥56, Traveler's Backpack 23, Hexalia 20, Starcatcher 0.
- About 780 real advancements are confirmed across 18 mods.
- **My estimate, not verified:** about 1,000–1,500 real modded advancements in total, plus vanilla's 122. Roughly 85–90% of all files are recipe unlocks.

Mods whose trees work as a guide or checklist:
- **Create** (85 visible): andesite, then brass, then trains and logistics.
- **Mekanism** (97).
- **Farmer's Delight** (21, including "master chef" and "plant all crops").
- **Aether** (31), **Ars** (~39), **Undergarden** (37).
- **Twilight Forest uses advancements as a progression lock** (verified in source). Its 9 biome restriction files need `progress_lich`, `progress_knights`, `progress_yeti`, `progress_labyrinth`, `progress_troll` or `progress_merge`. **Never delete or hide these** (with Reliable Advancements' "Delete from Game", Advancement Disable, or the like).

## 4. Mods that reward advancements or show completion %

- **Lucid Advancements** shows a global and per-tab progress bar, filters and pins.
- FTB Quests, Odyssey Quests and Questlog show per-chapter progress and give rewards.
- **Reliable Advancements**: `requireRewardClaiming` plus a Rewards tab in the editor.
- Vanilla rewards in the datapack. FD (3), TF (10) and Deeper Darker (6) already give XP this way.
- Advancements&Rewards (`advancements_rewards` 1.0.1, MIT, 541 downloads, made with MCreator): +2 health and +5% attack damage/speed every 5 advancements. It is **not documented whether recipe unlocks count**, and with about 10k of them that could explode. 🔴
- Achievement attribute rewards (1.0.3, MIT): permanent attributes per advancement, set in a JSON config. 🔴 power creep.
- Advancement Trophies Reforged (1.4.1, MIT): trophy blocks by frame type. 🟡 cosmetic.
- Advancement Count: vanilla advancements only. 🔴

## Recommendation for a first step

- 🟢 **Try one client-side screen mod in the dev instance**:
  - **Reliable Advancements** for the tree view, its later use as the editor for our own tab, and MIT licence.
  - **Lucid Advancements** if search, % and Italian text matter more than the tree.
  - Use one at a time (not verified together). Look at the real trees before writing anything.
- 🟢 **Then** write a small "Mango Craft" tab in `matteo_tweaks` (about 20–40 milestones linking the mods, XP/loot rewards, `mod_loaded` conditions).
- 🟡 Questlog if the pack guide needs text pages.
- 🟡 Achievements Optimizer only if the test shows lag when picking up items.
- 🔴 FTB Quests and the Odyssey Quests 2.0 beta.

Possible improvement (not done): have `scripts/inventory.py` count advancements split into recipe unlocks, visible and hidden, so these numbers come from the inventory directly.

## Sources

- Modrinth API (`/v2/project/<slug>` and `/version?game_versions=["1.21.1"]&loaders=["neoforge"]`, `/v2/version/ei0eVl2W`, search for advancement/advancements/quest/achievement/ftb quests/heracles/advancements debug).
- GitHub sources:
  - FTBTeam/FTB-Quests `1.21.1/main` (gradle.properties, neoforge.mods.toml, CHANGELOG, task and reward classes)
  - terrarium-earth/Heracles `1.21.1`
  - infernalstudios/Questlog `1.21.1` (docs, objectives, rewards)
  - evanbones/Advancement-Enhancement `1.21.1` (docs, ModConfig, ServerAdvancementEditor)
  - TeamTwilight/twilightforest `1.21.1` (`twilight/restrictions/*.json`)
  - misode/mcmeta `1.21.1-data`
  - Advancement source trees of Create, Occultism, FD, Ars, Aether, Mekanism, Undergarden, Supplementaries, Deeper Darker, Traveler's Backpack, Handcrafted, Bountiful Fares, Deep Aether, Hexalia, Starcatcher, Psi, Reactive
- Repo files: `1.21.1/data/inventario/mods/*.json`, `scripts/inventory.py` (COUNT_ONLY), the open-topics and rejected-mods documents.
- Blocked: github.com/way2muchnoise/BetterAdvancements/issues (permission not answered).
