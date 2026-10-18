# Animals that come with cooking-integrated foods — MC 1.21.1 NeoForge

Research date: 2026-10-17. Versions come from the Modrinth versions API (and CurseForge where it is the first place a mod is published). Source checks were done on shallow clones under `scratchpad/repos/{abn,am,aq,wn,natd,crab,duck,uw,ad2}`; Naturalist and Critters & Companions were reused from `repos/animals`.

## 0. How the pack's cooking mods consume animal products (verified in source)

I counted references in recipe JSON across the cloned FD addons (FD, Cultural, Veggies, Expanded, B&C, Bountiful Fares, F&C, Meadow, Rustic, Ocean's, MND). The counts are approximate.

| Tag | Approx. uses | Takeaway |
|---|---|---|
| `c:eggs` | ~70 (Cultural 17, B&C 10, Veggies 9, FD 8, Rustic 6, MND 6, Expanded 6, Meadow 3, Ocean's 3, F&C 1) | Any modded egg in `c:eggs` plugs straight into a lot of recipes. |
| `c:foods/raw_chicken` | ~17 (mostly Veggies) | A meat needs this tag to replace chicken. |
| `c:foods/raw_beef` | ~15 | A meat needs this tag to replace beef. |
| `c:foods/safe_raw_fish` | ~15 (FD, Veggies, B&C, Rustic) | FD defines it as `#c:foods/raw_fish` minus pufferfish, so any fish tagged `c:foods/raw_fish` is accepted automatically. |
| `c:foods/raw_meat` | ~9 | FD cabbage rolls and dog food, B&C raw sausage, MND curry and rolls, F&C. |

**Consequence:** an animal mod helps the cooking side when (a) its eggs are in `c:eggs`, (b) its fish are in `c:foods/raw_fish`, and above all (c) its meats are tagged as `raw_chicken` / `raw_beef` / `raw_pork` / `raw_mutton`, not only as `raw_meat`. Dedicated FD cooking-pot and cutting-board recipes come on top of that.

## 1. Recommendation

### Pick 1 — Naturalist 2.0.5 + "Naturalist Delight" (CurseForge) — best integration for the least risk

- **Naturalist** `2.0.5+1.21.1-neoforge` (2026-09-28)
  - Modrinth, 11.6M downloads, no dependencies.
  - License: code MIT, assets ARR.
  - 47 animals. The ones with food drops:
    - duck: duck + duck egg
    - deer: venison
    - turkey and ostrich: drumstick (ostrich also an egg)
    - boar: porkchop + fat
    - capybara, elephant, giraffe, rhino, zebra, komodo: bushmeat
    - mammoth: mammoth meat
    - crab and ray: crab meat
    - clam: clam meat
    - lizard, rat, snake, hedgehog: morsel
    - fish: bass, catfish, piranha, anglerfish, blobfish
  - Tags:
    - `c:foods/raw_meat`: duck, venison, bushmeat, drumstick, crab, clam, mammoth, morsel
    - `c:foods/raw_fish`: the five fish, so they reach FD `safe_raw_fish`
    - `c:eggs`: duck, ostrich, tortoise and alligator eggs
  - **No biomes.** Animals spawn through generic biome tags, so there is no TerraBlender/Regions Unexplored conflict.
- **Naturalist Delight** (slickson77)
  - CurseForge project 1236964 (`curseforge.com/minecraft/mc-mods/naturalist-delight`). Not on Modrinth.
  - File `farmerd_naturalist_compat-0.2-1.21.1.jar` (NeoForge, 2026-08-01). MIT. Source: github.com/Slickson77/FarmerDelight_Naturalist_Compat, branch 1.21.1, checked.
  - **Retags** Naturalist meats into the tags the pack actually uses:
    - duck → `c:foods/raw_chicken` (cooked → `cooked_chicken`)
    - venison and bushmeat → `c:foods/raw_beef` / `cooked_beef`
    - The effect: the ~30 Veggies/Cultural/B&C/Rustic/FD recipes that ask for chicken or beef accept them.
  - **FD cutting-board recipes:**
    - bass → salmon slices
    - catfish → cod slices
    - duck → duck cuts
    - venison and bushmeat → strips, which cut again into FD minced beef
  - **9 new foods:** biltong, deer jerky, bushmeat strip sandwich, bushsteak & potatoes, duck cuts, and others.
  - Naturalist's own cooked-egg smelting recipes are overridden to give FD fried egg instead.
  - **Caveats:**
    - It is early (v0.2, 9 items).
    - Its mods.toml declares no dependency on FD or Naturalist, but the jar needs both (it static-imports FD `FoodValues`). Both are in the pack, so this is fine.
    - Drumstick, crab, clam and mammoth meat are still only in `raw_meat`. A 3-line tag datapack could add drumstick to `raw_chicken` if wanted.
- **New dependencies:** none. **Overlap:** Friends & Foes crab vs Naturalist crab; Meadow cattle (different niche).

### Pick 2 (combinable, or an alternative to Pick 1) — Abnormals set: Environmental + Autumnity + Abnormals Delight, with Upgrade Aquatic optional

This is the only option with real hand-made FD dishes for its animals. All three need only Blueprint and FD, which are already in the pack. Use Blueprint ≥ 8.1.0; the latest is 8.2.0 (2026-09-06).

**Abnormals Delight**
- CurseForge **6.0.3** (2026-09-16) is the newest. Modrinth only has **6.0.2** (2026-04-27); Abnormals Delight publishes to CurseForge first.
- Abnormals License. 24.3M downloads on CurseForge, 1.58M on Modrinth.
- Every recipe is gated on `neoforge:mod_loaded`, so only the installed Abnormals mods activate.
- For Environmental:
  - FD cooking pot: Duck Noodles, Venison with Bamboo Shoots, Slabdish
  - Crafted: Seared Venison, Cherry Cookie
  - Cutting board: duck and venison → duck fillet and venison shanks
  - Knife-kill loot modifiers give feathers and leather
- For Autumnity:
  - FD cooking pot: Escargot (snail goo + onion + milk), Foul Soup, Stuffed Pumpkin
  - Cutting board: turkey → 5 turkey pieces
  - Crafted: Maple-Glazed Bacon, Pumpkin Bread, Maple Cookie
- For Upgrade Aquatic:
  - Cutting board: pike and perch slices
  - FD cooking pot: Perch with Mushrooms, Pike with Beetroot
- New tags: `c:foods/raw_duck|raw_venison|raw_perch|raw_pike` (plus cooked versions), and `minecraft:meat`.

**Environmental 5.0.1** (2025-10-18)
- Animals: duck (duck + **duck egg** in `c:eggs`), deer and reindeer (venison), yak (beef + yak hair), koi (`c:foods/raw_fish`), slabfish, tapir, zebra/zonkey/zorse.
- Pigs dig up **truffles**.
- Meats are in `c:foods/raw_meat` (via raw_duck/raw_venison) and **not** in `raw_chicken`/`raw_beef`.

**Autumnity 6.0.1** (2025-10-17)
- Turkey (`c:foods/raw_meat`, **turkey egg** in `c:eggs`) and snail (snail goo, used by Escargot).
- Also maple syrup and pancakes.

**Upgrade Aquatic 7.0.2** (2026-09-16), optional
- Pike, perch and lionfish in `c:foods/raw_fish`; also nautilus, thrasher, jellyfish.
- Overlaps heavily with Starcatcher's 132 fish. A goose exists in the source repo but is unfinished (empty loot table).

**Worldgen — verified in Blueprint source** (`ModdedBiomeSlicesManager`)
- Abnormals biomes do **not** use TerraBlender. Blueprint wraps whatever biome source exists, which here is TerraBlender/Regions Unexplored, in "modded biome slices". Inside a slice, only some climate cells become Abnormals biomes; the rest is `original_source_marker`, which falls back to Regions Unexplored or vanilla.
- So the two systems **layer rather than crash**, but Abnormals slices take area away from Regions Unexplored. The original-source slice has weight 100. Slice weights:
  - Environmental: marsh 25, blossom 30, pine_barrens 30 (12 biomes)
  - Autumnity: autumn 20 (maple_forest, pumpkin_fields)
  - Neapolitan: strawberry_fields 20
  - Atmospheric: six slices totalling **175** (16 biomes)
- **A slice with weight ≤ 0 is skipped (verified in code).** A worldgen datapack loaded before world creation (e.g. via Paxi) can set Environmental's and Autumnity's slices to `"weight": 0` and keep Regions Unexplored as the only biome provider.
- Environmental animals still spawn in Regions Unexplored biomes, because they use generic tags and Regions Unexplored tags its biomes properly (verified):
  - ducks: `#c:is_swamp` (RU bayou, fen, marsh)
  - deer: `#minecraft:is_forest`
  - reindeer: snowy plains, taiga, grove
  - yak: `#minecraft:is_hill` and stony peaks
- **But Autumnity turkeys and snails spawn only in `#autumnity:is_autumnal`, i.e. its own biomes.** If you disable the slice, add Regions Unexplored's `maple_forest`, `autumnal_maple_forest` and `pumpkin_fields` to `autumnity:has_animal/turkey` and `/snail`. Regions Unexplored already has the same biome themes, so this costs nothing.

**Gameplay caveat (verified)**
- Environmental ships `remove_spawns_inverted` biome modifiers: vanilla cows remain only in plains/savanna, sheep only in plains/savanna/meadow, chickens only in forest/taiga/jungle, pigs only in forest/swamp.
- This applies to Regions Unexplored biomes too.
- To neutralize it, override `environmental:neoforge/biome_modifier/remove_spawn/{cow,sheep,pig,chicken}.json` with `{"type":"neoforge:none"}`.

**Maintenance and overlap**
- Maintenance: Environmental, Autumnity, Neapolitan and Atmospheric have not had a release since Oct 2025, although their repos have commits through Oct 2026. Abnormals Delight and Upgrade Aquatic were released in Sep 2026.
- Overlap with Pick 1: both add duck, deer and turkey. Both together means duplicate species, but every meat still works in recipes. Choose Pick 1 alone if you want no duplicates and no worldgen changes. Choose Pick 2 alone if you want the hand-made dishes.
- Twilight's Flavor & Delight (already in the pack) lists Neapolitan and Blueprint as optional integrations.

### Pick 3 (small add-on, combinable with either) — Crabber's Delight 1.3.1

- 2026-09-28, MIT, 3.37M downloads, requires FD only. Source checked: branch NeoForge-1.21.1.
- One animal (crab) plus crab traps that yield crab, clawster, shrimp and clams.
- 14 FD cooking-pot dishes (bisque, clam chowder, seafood gumbo, crab cakes, shrimp fried rice, turtle stew…) and 9 cutting recipes; built-in Upgrade Aquatic recipes.
- Worldgen: palm trees, seashells and wormy dirt as features only, no biomes.
- Overlaps Friends & Foes crab and Ocean's Delight.
- Pick it only if you want more seafood cooking. It is mostly a cooking mod with one animal.

## 2. Other candidates (one line each)

- **Spawn 4.0.8** (2026-09-14; ARR, closed source; 8.2M; **new dependency Teal Lib**)
  - Content: ~35 mostly coastal/ocean creatures (tuna, herring, bluefish, clam, sea cow, seal, octopus, dodo, booby, snail, hamster…), ~30 foods (sushi rolls with FD cooked rice, canned herring, steamed clams, dodo meat, escargot, date cookie). Only **2 FD cooking-pot recipes** (Clam Chowder, Crab Boil).
  - Worldgen risk: many biomes (Rocky Shore, Seagrass Meadow, Deep Coral Reef, Tide Pools, Octopolis, Ant Gardens, Dragonfly Reeds, Dodo Island). The injection method **can't be verified** because the source is private. Recent changelogs keep fixing worldgen clashes with other biome mods (Biolith, Expanded Ecosphere), so there is real risk with Regions Unexplored.
  - Verdict: overlaps Starcatcher and Ocean's Delight. Not recommended now.
- **[Let's Do] WilderNature 1.1.5** (NeoForge build is **beta**, 2026-07-30; custom license; 4.8M; deps Architectury + Foundation, both already in the pack)
  - Content: bison, deer, turkey, cassowary, boar, hippo, giraffe, lion, squirrel, raccoon, minisheep…
  - Integration is weak: meats are not in any `c:foods` tag and there are no FD or Farm & Charm recipes. Only the turkey egg is in `c:eggs`. It has a truffling mechanic. Farm & Charm counts its turkey as a "chicken" entity.
  - Verdict: fits the pack's style, but needs a tag datapack to be useful.
- **Alex's Mobs Continued 2.2.2** (2026-09-18; GPL-3; 293k; **new dependency CodxLib ≥1.6.0**; no Citadel)
  - Content: 85+ mostly exotic or hostile mobs.
  - Foods: moose ribs, kangaroo meat, lobster tail, catfish, emu egg, banana…
  - Integration: only `c:eggs` (via its forge→c data migration); no `c:foods` meat tags.
  - FD compat needs an addon:
    - **Alex's Delight 1.6**: CurseForge, ARR, 2026-02-12, 48M downloads. Same `alexsmobs` mod id, so it should work with either port, but not verified.
    - **AMC Delight 1.0.1**: 2026-08-21, CC-BY-NC-ND, closed source, ~10k downloads, needs CodxLib; 48 butchery cuts and many dishes.
  - Verdict: big and not very cozy.
- **Alex's Mobs (Unofficial Port, Raguto)** 2026-01-26: GPL, needs the Citadel unofficial port. It is superseded by Continued.
- **Untitled Duck Mod 1.7.0** (2026-08-30; MIT; 2.0M; no deps): duck and goose with raw duck/goose in `c:foods/raw_meat` and `c:foods/raw_duck`, which feeds Abnormals Delight's Duck Noodles. Eggs are in `c:eggs`. Good as a tiny add-on to Pick 2, redundant with Pick 1.
- **Hybrid Aquatic mc1.21.1-1.7.3** (2026-09-22; ARR, public source; 5.0M)
  - Dependencies: **new** — Kotlin for Forge, Lithostitched, Hybrid API, Biolith; already present — Curios, GeckoLib.
  - Content: dozens of fish in `c:foods/raw_fish` (reach FD `safe_raw_fish`); only smelting recipes, no dishes.
  - Worldgen: 14 biomes injected with Lithostitched `replace_partially` over vanilla oceans, rivers and caves (it does not touch Regions Unexplored land).
  - Verdict: overlaps Starcatcher.
- **Critters n' Crawlers 2.2.5** (2025-11-18; ARR, closed source; GeckoLib): elk, goose, turkey, deer, boar, plus cryptids. No documented foods or tags. Stale.
- **Cosy Critters & Creepy Crawlies** (MIT): **client-side ambient** birds, moths and spiders with no drops. Not applicable.
- **Eravern's More Animal Products 3.0.0** (2026-09-23; MIT; no deps): meats for vanilla mobs (horse, camel, frog, squid…). No c tags, smelting only. It **overrides 23 vanilla entity loot tables**, which risks conflicts.
- **Untamed Wilds (Unofficial Port)** (2026-02-15; GPL; Citadel port): bear, cetacean and pachyderm meats and roe, no c tags. Its only FD recipe sits at the old `data/farmersdelight/recipes/` path, so it **won't load on 1.21.1**.
- **Butchery** (2026-10-09; ARR; 1.18M): carcass and butchering mechanic for vanilla mobs, FD food optional. **Butchercraft** (CC-BY-NC-SA) is similar and integrates with Extra Delight, which is not in the pack. Neither adds animals.
- **Compat Delight 1.0.1.1** (2025-09-09; ARR, closed source): claims Naturalist, Friends & Foes, Hexerei and Regions Unexplored food content (~1000 items total). It can't be verified what the 1.21.1 build actually contains, and it has been unmaintained for a year.
- **Neapolitan / Buzzier Bees / Atmospheric**:
  - Neapolitan: food rather than animals (chimpanzee; ice cream, milk bottle in `c:drinks/milk`); adds a strawberry fields slice.
  - Buzzier Bees: moobloom duplicates Friends & Foes; grizzly bear; honey foods.
  - Atmospheric: no meat animals (cochineal, tetra), fruits only, and **adds 16 biomes with slice weight 175**. Skip.
- **Drop the Meat** (custom license): meat for every passive mob, no FD or tag compat documented.
- **Barbeque's Delight**: an FD-based skewer/grill cooking mod; it adds no animals.

## 3. Not available / dead ends

- **No Naturalist FD addon on Modrinth.** "Naturalist Delight" with 1.21.1 support exists only on CurseForge (Slickson). The other "Naturalist Delight" on Modrinth/ModDex is for 1.19/1.20 only.
- The original Alex's Mobs and Untamed Wilds stopped at 1.20.1. On 1.21.1 only unofficial ports exist.
- The **Spawn** source repo (N1nn1/spawn) is private, so its worldgen and tags could not be verified.
- The Upgrade Aquatic goose is not finished.

## 4. Suggested optional datapack tweaks

These are small. Load them via Paxi or another global datapack before creating the world.

1. Pick 2: set Environmental/Autumnity `blueprint/modded_biome_slices/*.json` to `"weight": 0` so Regions Unexplored stays the only biome provider.
2. If you did (1): add Regions Unexplored's autumnal biomes to `autumnity:has_animal/{turkey,snail}`.
3. Pick 2: override Environmental's `remove_spawn/*.json` with `neoforge:none` to keep vanilla livestock everywhere.
4. Optional tag additions for wider recipe use:
   - Pick 1: Naturalist drumstick → `c:foods/raw_chicken`.
   - Pick 2: Environmental/Autumnity duck and turkey → `raw_chicken`, venison → `raw_beef`.
