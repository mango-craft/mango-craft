# Enhanced Celestials 2: Core (enhanced-celestials-2-core)

File generato da `scripts/esamina.py` (workflow "Esamina mod"): la mod **non** è nel pack. Non modificarlo a mano.

- Versione: **2.0.3.3-neoforge** (release, 2026-09-07), file `Enhanced-Celestials-2-Core-NeoForge-1.21.1-2.0.3.3.jar`, id versione `CWaaEX5L`
- Licenza su Modrinth: LicenseRef-All-Rights-Reserved · download: 66767
- Filtro dei valori: `enhancedcelestials|lunar|moon` · filtro dei testi del codice: `(?i)translat|config|\.json5?$|\.toml$|^ecc$|prompt|modpack`

## Mod nel file e dipendenze dichiarate

- `enhancedcelestials2core` 2.0.3.3
  - required: `neoforge` [21,)
  - required: `minecraft` [1.21.1,)
  - required: `corgilib` [5.0.0.9,)
  - required: `dataanchor` [2.0.0.16,)
  - incompatible: `enhancedcelestials` *

## Cartelle di dati (file .json)

- `enhancedcelestials2core:append_loot_tables/minecraft/chests`: 16
- `enhancedcelestials2core:enhancedcelestials2core/lunar/event`: 1
- `enhancedcelestials2core:tags/enhancedcelestials2core/lunar/event`: 1
- `minecraft:enhancedcelestials2core/lunar/dimension_settings`: 1

## Valori dei file filtrati


### `assets/enhancedcelestials2core/lang/en_us.json`

- `enhancedcelestials2core.command.time.set` = "Set time to %s for the next day. You are now on day %s. Raw daytime is now %s."
- `enhancedcelestials2core.command.time.set.reset` = "Reset daytime to %s from %s. You are now on day %s. You were on day %s."
- `enhancedcelestials2core.commands.disabled` = "Enhanced Celestials' lunar events are disabled for this world!"
- `enhancedcelestials2core.commands.dumpmodifiers.empty` = "%s has no modifiers."
- `enhancedcelestials2core.commands.dumpmodifiers.header` = "Modifiers for %s:"
- `enhancedcelestials2core.commands.lunarevent_missing` = "\"%s\" is not a valid lunar event!"
- `enhancedcelestials2core.commands.scheduleevent.insert_failed` = "Could not schedule lunar event..."
- `enhancedcelestials2core.commands.scheduleevent.inserted` = "Scheduled lunar event \"%s\" %s day(s) from today."
- `enhancedcelestials2core.commands.scheduleevent.remove_day_not_found` = "No lunar event is scheduled %s day(s) from today!"
- `enhancedcelestials2core.commands.scheduleevent.remove_event_not_found` = "No scheduled lunar events match \"%s\"!"
- `enhancedcelestials2core.commands.scheduleevent.removed_day` = "Removed the lunar event scheduled %s day(s) from today."
- `enhancedcelestials2core.commands.scheduleevent.removed_events` = "Removed %s scheduled lunar event(s) matching \"%s\"."
- `enhancedcelestials2core.commands.scheduleevent.too_far_in_advance` = "Lunar events can only be scheduled up to %s day(s) in advance!"
- `enhancedcelestials2core.commands.setlunarevent.empty_tag` = "Invalid lunar event tag \"%s\"!"
- `enhancedcelestials2core.commands.setlunarevent.failed` = "Could not start Lunar Event..."
- `enhancedcelestials2core.commands.setlunarevent.requires_clear_skies` = "Lunar events can only be started during clear skies!"
- `enhancedcelestials2core.commands.setlunarevent.unknown_tag` = "Invalid lunar event tag."
- `enhancedcelestials2core.config.configure` = "Configure Lunar Events & Lunar Dimension Settings"
- `enhancedcelestials2core.config.support` = "Support Corgi Taco"
- `enhancedcelestials2core.config.support.tooltip` = "Help Support the Developer Of Enhanced Celestials 2!"
- `enhancedcelestials2core.config.title` = "Enhanced Celestials 2 Config"
- `enhancedcelestials2core.config.translation_settings` = "Translation Settings"
- `enhancedcelestials2core.debug.blend` = "Blend: %s"
- `enhancedcelestials2core.debug.changed_this_tick` = "Changed This Tick: %s"
- `enhancedcelestials2core.debug.current_event` = "Current Event: %s"
- `enhancedcelestials2core.debug.day_time` = "Day Time: %s"
- `enhancedcelestials2core.debug.dimension` = "Dimension: %s"
- `enhancedcelestials2core.debug.event_active` = "Event Active: %s"
- `enhancedcelestials2core.debug.last_event` = "Last Event: %s"
- `enhancedcelestials2core.debug.moon_phase` = "Moon Phase: %s"
- `enhancedcelestials2core.debug.next_event` = "Next Event: %s"
- `enhancedcelestials2core.debug.side_client` = "Client"
- `enhancedcelestials2core.debug.side_server` = "Server"
- `enhancedcelestials2core.debug.unbound` = "Unbound"
- `enhancedcelestials2core.description.none` = "none"
- `enhancedcelestials2core.drop_settings.entry` = "%s x%s"
- `enhancedcelestials2core.drop_settings.group` = "%s on stacks of %s or more"
- `enhancedcelestials2core.lunar_event_modifier.anvil_cost` = "Amplifies Anvil Cost by %s"
- `enhancedcelestials2core.lunar_event_modifier.beacon_radius` = "Amplifies Beacon Radius by %s"
- `enhancedcelestials2core.lunar_event_modifier.block_item_drop` = "Modifies block drops with %s"
- `enhancedcelestials2core.lunar_event_modifier.block_sleeping` = "Blocks sleeping when %s"
- `enhancedcelestials2core.lunar_event_modifier.disable_biome_spawn_settings` = "Ignores biome spawn settings"
- `enhancedcelestials2core.lunar_event_modifier.enchantment_cost` = "Amplifies Enchantment Cost by %s"
- `enhancedcelestials2core.lunar_event_modifier.entity_drop` = "Modifies entity drops: %s"
- `enhancedcelestials2core.lunar_event_modifier.entity_drop.entry` = "%s when %s"
- `enhancedcelestials2core.lunar_event_modifier.existing_mob_equipment` = "Equips already-alive mobs with: %s"
- `enhancedcelestials2core.lunar_event_modifier.experience` = "Amplifies Experience by %s"
- `enhancedcelestials2core.lunar_event_modifier.force_surface_spawning` = "Forces mobs to spawn on the surface"
- `enhancedcelestials2core.lunar_event_modifier.glow_color` = "Sets glow color to #%s with intensity %s"
- `enhancedcelestials2core.lunar_event_modifier.mob_effects` = "Applies mob effects: %s"
- `enhancedcelestials2core.lunar_event_modifier.mob_effects.entry` = "%s when %s"
- `enhancedcelestials2core.lunar_event_modifier.mob_equipment.entry` = "%s when %s (%s%% chance)"
- `enhancedcelestials2core.lunar_event_modifier.mob_equipment.set` = "[%s] (weight %s)"
- `enhancedcelestials2core.lunar_event_modifier.mob_equipment.slot` = "%s: %s x%s"
- `enhancedcelestials2core.lunar_event_modifier.mob_spawn_distances` = "Sets mob spawn distances to %s"
- `enhancedcelestials2core.lunar_event_modifier.mob_spawn_equipment` = "Equips freshly spawned mobs with: %s"
- `enhancedcelestials2core.lunar_event_modifier.mob_spawn_settings` = "Overrides mob spawn settings with %s"
- `enhancedcelestials2core.lunar_event_modifier.moon_size` = "Sets moon size to %s"
- `enhancedcelestials2core.lunar_event_modifier.moon_texture` = "Sets moon texture to %s"
- `enhancedcelestials2core.lunar_event_modifier.moon_texture_color` = "Sets moon texture color to #%s"
- `enhancedcelestials2core.lunar_event_modifier.name_color` = "Sets name color to %s"
- `enhancedcelestials2core.lunar_event_modifier.sky_light_color` = "Sets sky light color to #%s"
- `enhancedcelestials2core.lunar_event_modifier.slimes_spawn_everywhere` = "Allows slimes to spawn everywhere"
- `enhancedcelestials2core.lunar_event_modifier.sound_track` = "Sets soundtrack to %s"
- `enhancedcelestials2core.lunar_event_modifier.spawn_category_multiplier` = "Multiplies mob spawn rates by %s"
- `enhancedcelestials2core.lunar_event_modifier.text_components` = "Overrides text components with %s"
- `enhancedcelestials2core.lunar_event_modifier.village_siege_probability` = "Sets Village Siege Probability to %s"
- `enhancedcelestials2core.lunar_text_components` = "Rise: %s | Set: %s"
- `enhancedcelestials2core.lunar_text_components.notification` = "%s notification: %s"
- `enhancedcelestials2core.lunarforecast.days_left` = "(in %sd)"
- `enhancedcelestials2core.lunarforecast.empty` = "No upcoming lunar events."
- `enhancedcelestials2core.lunarforecast.header` = "Current Lunar forecast:\n%s"
- `enhancedcelestials2core.lunarforecast.recompute` = "Lunar forecast was recomputed!"
- `enhancedcelestials2core.missing_addon.curseforge` = "Download from CurseForge"
- `enhancedcelestials2core.missing_addon.default_lunar_events.continue_without` = "Continue Without Default Lunar Events"
- `enhancedcelestials2core.missing_addon.default_lunar_events.prompt` = "Enhanced Celestials 2: Default Lunar Events isn't installed! Run %s to add a curated set of lunar events out of the box. Modpack developers: ship a config/enhancedcelestials2core/dle-prompt.json file with your pack to hide this prompt."
- `enhancedcelestials2core.missing_addon.default_lunar_events.subtitle` = "Enhanced Celestials 2: Default Lunar Events isn't installed"
- `enhancedcelestials2core.missing_addon.default_lunar_events.title` = "Missing Default Lunar Events"
- `enhancedcelestials2core.missing_addon.modrinth` = "Download from Modrinth"
- `enhancedcelestials2core.missing_addon.shaders.continue_without` = "Continue Without Shader Support"
- `enhancedcelestials2core.missing_addon.shaders.prompt` = "You're running a shader mod, but Enhanced Celestials 2: Shader Support isn't installed! Run %s to get lunar events working correctly with your shaders. Modpack developers: ship a config/enhancedcelestials2core/shaders-prompt.json file with your pack to hide this prompt."
- `enhancedcelestials2core.missing_addon.shaders.subtitle` = "Iris was detected without Enhanced Celestials 2: Shader Support"
- `enhancedcelestials2core.missing_addon.shaders.title` = "Missing Shader Support"
- `enhancedcelestials2core.mob_effect_instance` = "%s (amplifier %s, %s ticks)"
- `enhancedcelestials2core.sleep.fail` = "You may not rest now because the current lunar event prevents it."
- `enhancedcelestials2core.translation.incomplete` = "Your selected language's Enhanced Celestials 2 translations are incomplete! Run %s to help translate."
- `enhancedcelestials2core.translation.not_configured` = "Enhanced Celestials 2 translation settings not yet configured. Use %s to set up these rules. Modpack developers: once these settings are created ship them with your modpack to hide this prompt from showing again."
- `enhancedcelestials2core.translation_config.cancel.tooltip` = "Discard any changes and return without saving."
- `enhancedcelestials2core.translation_config.done.tooltip` = "Save these translation settings and return."
- `enhancedcelestials2core.translation_config.mode` = "Translation Mode"
- `enhancedcelestials2core.translation_config.mode.automatic` = "Automatic"
- `enhancedcelestials2core.translation_config.mode.disabled` = "Disabled"
- `enhancedcelestials2core.translation_config.mode.manual` = "Manual"
- `enhancedcelestials2core.translation_config.mode.tooltip` = "Click to Cycle\n\nAutomatic: downloads and applies community translations automatically.\n\nManual: downloaded translations are never applied automatically.\n\nDisabled: never downloads or applies community translations."
- `enhancedcelestials2core.translation_config.override_existing` = "Override Existing Translations"
- `enhancedcelestials2core.translation_config.override_existing.tooltip` = "When on, downloaded translations replace existing translation strings for keys you already have. When off, they only fill in keys that are missing."
- `enhancedcelestials2core.translation_config.prompt_incomplete` = "Prompt When Incomplete"
- `enhancedcelestials2core.translation_config.prompt_incomplete.tooltip` = "Ask you to help translate when your selected language is missing translation strings."
- `enhancedcelestials2core.translation_config.title` = "Translation Settings"
- `lunar.event.enhancedcelestials2core.default` = "Normal Moon"

### `assets/enhancedcelestials2core/lang/fr_fr.json`

- `enhancedcelestials2core.commands.disabled` = "Les événements lunaires célestes améliorés sont désactivés pour ce monde !"
- `enhancedcelestials2core.commands.lunarevent_missing` = "\"%s\" n'est pas un événement lunaire valide !"
- `enhancedcelestials2core.lunarforecast.days_left` = "(%s jours jusqu'à)"
- `enhancedcelestials2core.lunarforecast.empty` = "Aucun événement lunaire à venir."
- `enhancedcelestials2core.lunarforecast.header` = "Prévisions lunaires actuelles :\n%s"
- `enhancedcelestials2core.sleep.fail` = "Vous ne pouvez pas vous reposer maintenant car l'événement lunaire actuel l'empêche."

### `assets/enhancedcelestials2core/lang/ja_jp.json`

- `enhancedcelestials2core.commands.disabled` = "このワールドにおけるEnhanced Celestialsの月イベントが無効化されました！"
- `enhancedcelestials2core.commands.lunarevent_missing` = "\"%s\" は有効な月イベントではありません！"
- `enhancedcelestials2core.lunarforecast.days_left` = "(あと %sd 後)"
- `enhancedcelestials2core.lunarforecast.empty` = "今後月イベントは発生しません"
- `enhancedcelestials2core.lunarforecast.header` = "現在の月予報:\n%s"
- `enhancedcelestials2core.lunarforecast.recompute` = "月予報が再計算されました！"
- `enhancedcelestials2core.sleep.fail` = "特別な月が昇っている。休むことはできない"

### `assets/enhancedcelestials2core/lang/ru_ru.json`

- `enhancedcelestials2core.commands.disabled` = "Лунные события отключены для этого мира!"
- `enhancedcelestials2core.commands.lunarevent_missing` = "'%s' не является лунным событием!"
- `enhancedcelestials2core.lunarforecast.days_left` = "(через %s дней)"
- `enhancedcelestials2core.lunarforecast.empty` = "Нет предстоящих лунных событий."
- `enhancedcelestials2core.lunarforecast.header` = "Текущий лунный прогноз:\n%s"
- `enhancedcelestials2core.lunarforecast.recompute` = "Лунный прогноз пересчитан."
- `enhancedcelestials2core.sleep.fail` = "Сейчас вы не можете поспать, так как лунное событие этому препятствует."

### `assets/enhancedcelestials2core/lang/uk_ua.json`

- `enhancedcelestials2core.commands.disabled` = "Місячні явища Enhanced Celestials вимкненні для цього світу!"
- `enhancedcelestials2core.commands.lunarevent_missing` = "\"%s\" не є коректним місячним явищем!"
- `enhancedcelestials2core.lunarforecast.days_left` = "(через %sднів)"
- `enhancedcelestials2core.lunarforecast.empty` = "Немає майбутніх місячних подій."
- `enhancedcelestials2core.lunarforecast.header` = "Поточний місячний прогноз:\n%s"
- `enhancedcelestials2core.lunarforecast.recompute` = "Місячний прогноз оновлено!"
- `enhancedcelestials2core.sleep.fail` = "Ви не можете спати зараз через заборону поточним місячним явищем."

### `assets/enhancedcelestials2core/lang/zh_cn.json`

- `enhancedcelestials2core.sleep.fail` = "你现在不能休息, 当前月相为 \"血月\""

### `data/enhancedcelestials2core/append_loot_tables/minecraft/chests/abandoned_mineshaft.json`

- `type` = "minecraft:chest"
- `pools[0].rolls` = 0
- `pools[0].bonus_rolls` = 1
- `pools[0].entries[0].name` = "minecraft:diamond"
- `pools[0].entries[0].type` = "minecraft:item"
- `pools[0].entries[0].weight` = 15
- `pools[0].entries[0].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[0].functions[0].count.min` = 2.0
- `pools[0].entries[0].functions[0].count.max` = 5.0
- `pools[0].entries[0].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[1].name` = "minecraft:iron_ingot"
- `pools[0].entries[1].type` = "minecraft:item"
- `pools[0].entries[1].weight` = 20
- `pools[0].entries[1].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[1].functions[0].count.min` = 4.0
- `pools[0].entries[1].functions[0].count.max` = 10.0
- `pools[0].entries[1].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[2].type` = "minecraft:item"
- `pools[0].entries[2].weight` = 5
- `pools[0].entries[2].functions[0].function` = "minecraft:enchant_randomly"
- `pools[0].entries[2].name` = "minecraft:book"
- `pools[0].entries[3].name` = "minecraft:diamond_pickaxe"
- `pools[0].entries[3].type` = "minecraft:item"
- `pools[0].entries[3].weight` = 5
- `pools[0].entries[3].functions[0].function` = "minecraft:enchant_randomly"
- `pools[0].entries[4].type` = "minecraft:empty"
- `pools[0].entries[4].weight` = 60

### `data/enhancedcelestials2core/append_loot_tables/minecraft/chests/buried_treasure.json`

- `type` = "minecraft:chest"
- `pools[0].rolls` = 0
- `pools[0].bonus_rolls` = 1
- `pools[0].entries[0].name` = "minecraft:diamond"
- `pools[0].entries[0].type` = "minecraft:item"
- `pools[0].entries[0].weight` = 5
- `pools[0].entries[0].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[0].functions[0].count.min` = 2.0
- `pools[0].entries[0].functions[0].count.max` = 5.0
- `pools[0].entries[0].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[1].name` = "minecraft:iron_ingot"
- `pools[0].entries[1].type` = "minecraft:item"
- `pools[0].entries[1].weight` = 10
- `pools[0].entries[1].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[1].functions[0].count.min` = 4.0
- `pools[0].entries[1].functions[0].count.max` = 10.0
- `pools[0].entries[1].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[2].name` = "minecraft:emerald"
- `pools[0].entries[2].type` = "minecraft:item"
- `pools[0].entries[2].weight` = 10
- `pools[0].entries[2].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[2].functions[0].count.min` = 2.0
- `pools[0].entries[2].functions[0].count.max` = 8.0
- `pools[0].entries[2].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[3].name` = "minecraft:gold_ingot"
- `pools[0].entries[3].type` = "minecraft:item"
- `pools[0].entries[3].weight` = 10
- `pools[0].entries[3].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[3].functions[0].count.min` = 2.0
- `pools[0].entries[3].functions[0].count.max` = 8.0
- `pools[0].entries[3].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[4].name` = "minecraft:gold_ingot"
- `pools[0].entries[4].type` = "minecraft:item"
- `pools[0].entries[4].weight` = 10
- `pools[0].entries[4].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[4].functions[0].count.min` = 2.0
- `pools[0].entries[4].functions[0].count.max` = 8.0
- `pools[0].entries[4].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[5].type` = "minecraft:item"
- `pools[0].entries[5].weight` = 5
- `pools[0].entries[5].functions[0].function` = "minecraft:enchant_randomly"
- `pools[0].entries[5].name` = "minecraft:book"
- `pools[0].entries[6].name` = "minecraft:diamond_axe"
- `pools[0].entries[6].type` = "minecraft:item"
- `pools[0].entries[6].weight` = 10
- `pools[0].entries[6].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[6].functions[0].damage.min` = 0.6
- `pools[0].entries[6].functions[0].damage.max` = 0.9
- `pools[0].entries[6].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[6].functions[1].levels.min` = 5.0
- `pools[0].entries[6].functions[1].levels.max` = 10.0
- `pools[0].entries[6].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[7].type` = "minecraft:empty"
- `pools[0].entries[7].weight` = 40

### `data/enhancedcelestials2core/append_loot_tables/minecraft/chests/desert_pyramid.json`

- `type` = "minecraft:chest"
- `pools[0].rolls` = 0
- `pools[0].bonus_rolls` = 1
- `pools[0].entries[0].name` = "minecraft:diamond"
- `pools[0].entries[0].type` = "minecraft:item"
- `pools[0].entries[0].weight` = 5
- `pools[0].entries[0].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[0].functions[0].count.min` = 2.0
- `pools[0].entries[0].functions[0].count.max` = 5.0
- `pools[0].entries[0].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[1].name` = "minecraft:iron_ingot"
- `pools[0].entries[1].type` = "minecraft:item"
- `pools[0].entries[1].weight` = 20
- `pools[0].entries[1].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[1].functions[0].count.min` = 4.0
- `pools[0].entries[1].functions[0].count.max` = 10.0
- `pools[0].entries[1].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[2].type` = "minecraft:item"
- `pools[0].entries[2].weight` = 5
- `pools[0].entries[2].functions[0].function` = "minecraft:enchant_randomly"
- `pools[0].entries[2].name` = "minecraft:book"
- `pools[0].entries[3].type` = "minecraft:empty"
- `pools[0].entries[3].weight` = 70

### `data/enhancedcelestials2core/append_loot_tables/minecraft/chests/igloo_chest.json`

- `type` = "minecraft:chest"
- `pools[0].rolls` = 0
- `pools[0].bonus_rolls` = 1
- `pools[0].entries[0].name` = "minecraft:iron_ingot"
- `pools[0].entries[0].type` = "minecraft:item"
- `pools[0].entries[0].weight` = 20
- `pools[0].entries[0].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[0].functions[0].count.min` = 0.0
- `pools[0].entries[0].functions[0].count.max` = 10.0
- `pools[0].entries[0].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[1].type` = "minecraft:item"
- `pools[0].entries[1].weight` = 5
- `pools[0].entries[1].functions[0].function` = "minecraft:enchant_randomly"
- `pools[0].entries[1].name` = "minecraft:book"
- `pools[0].entries[2].name` = "minecraft:leather_leggings"
- `pools[0].entries[2].type` = "minecraft:item"
- `pools[0].entries[2].weight` = 2
- `pools[0].entries[2].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[2].functions[0].damage.min` = 0.1
- `pools[0].entries[2].functions[0].damage.max` = 0.4
- `pools[0].entries[2].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[2].functions[1].levels.min` = 10.0
- `pools[0].entries[2].functions[1].levels.max` = 30.0
- `pools[0].entries[2].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[3].name` = "minecraft:leather_chestplate"
- `pools[0].entries[3].type` = "minecraft:item"
- `pools[0].entries[3].weight` = 2
- `pools[0].entries[3].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[3].functions[0].damage.min` = 0.1
- `pools[0].entries[3].functions[0].damage.max` = 0.4
- `pools[0].entries[3].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[3].functions[1].levels.min` = 10.0
- `pools[0].entries[3].functions[1].levels.max` = 30.0
- `pools[0].entries[3].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[4].name` = "minecraft:leather_boots"
- `pools[0].entries[4].type` = "minecraft:item"
- `pools[0].entries[4].weight` = 2
- `pools[0].entries[4].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[4].functions[0].damage.min` = 0.1
- `pools[0].entries[4].functions[0].damage.max` = 0.4
- `pools[0].entries[4].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[4].functions[1].levels.min` = 10.0
- `pools[0].entries[4].functions[1].levels.max` = 30.0
- `pools[0].entries[4].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[5].name` = "minecraft:iron_shovel"
- `pools[0].entries[5].type` = "minecraft:item"
- `pools[0].entries[5].weight` = 4
- `pools[0].entries[5].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[5].functions[0].damage.min` = 0.3
- `pools[0].entries[5].functions[0].damage.max` = 0.6
- `pools[0].entries[5].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[5].functions[1].levels.min` = 10.0
- `pools[0].entries[5].functions[1].levels.max` = 30.0
- `pools[0].entries[5].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[6].type` = "minecraft:empty"
- `pools[0].entries[6].weight` = 40

### `data/enhancedcelestials2core/append_loot_tables/minecraft/chests/jungle_temple.json`

- `type` = "minecraft:chest"
- `pools[0].rolls` = 0
- `pools[0].bonus_rolls` = 1
- `pools[0].entries[0].name` = "minecraft:diamond"
- `pools[0].entries[0].type` = "minecraft:item"
- `pools[0].entries[0].weight` = 15
- `pools[0].entries[0].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[0].functions[0].count.min` = 2.0
- `pools[0].entries[0].functions[0].count.max` = 5.0
- `pools[0].entries[0].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[1].name` = "minecraft:iron_ingot"
- `pools[0].entries[1].type` = "minecraft:item"
- `pools[0].entries[1].weight` = 20
- `pools[0].entries[1].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[1].functions[0].count.min` = 4.0
- `pools[0].entries[1].functions[0].count.max` = 10.0
- `pools[0].entries[1].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[2].type` = "minecraft:item"
- `pools[0].entries[2].weight` = 5
- `pools[0].entries[2].functions[0].function` = "minecraft:enchant_randomly"
- `pools[0].entries[2].name` = "minecraft:book"
- `pools[0].entries[3].name` = "minecraft:chainmail_helmet"
- `pools[0].entries[3].type` = "minecraft:item"
- `pools[0].entries[3].weight` = 2
- `pools[0].entries[3].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[3].functions[0].damage.min` = 0.1
- `pools[0].entries[3].functions[0].damage.max` = 0.4
- `pools[0].entries[3].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[3].functions[1].levels.min` = 10.0
- `pools[0].entries[3].functions[1].levels.max` = 30.0
- `pools[0].entries[3].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[4].name` = "minecraft:chainmail_chestplate"
- `pools[0].entries[4].type` = "minecraft:item"
- `pools[0].entries[4].weight` = 2
- `pools[0].entries[4].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[4].functions[0].damage.min` = 0.1
- `pools[0].entries[4].functions[0].damage.max` = 0.4
- `pools[0].entries[4].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[4].functions[1].levels.min` = 10.0
- `pools[0].entries[4].functions[1].levels.max` = 30.0
- `pools[0].entries[4].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[5].name` = "minecraft:chainmail_leggings"
- `pools[0].entries[5].type` = "minecraft:item"
- `pools[0].entries[5].weight` = 2
- `pools[0].entries[5].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[5].functions[0].damage.min` = 0.1
- `pools[0].entries[5].functions[0].damage.max` = 0.4
- `pools[0].entries[5].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[5].functions[1].levels.min` = 10.0
- `pools[0].entries[5].functions[1].levels.max` = 30.0
- `pools[0].entries[5].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[6].name` = "minecraft:chainmail_boots"
- `pools[0].entries[6].type` = "minecraft:item"
- `pools[0].entries[6].weight` = 2
- `pools[0].entries[6].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[6].functions[0].damage.min` = 0.1
- `pools[0].entries[6].functions[0].damage.max` = 0.4
- `pools[0].entries[6].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[6].functions[1].levels.min` = 10.0
- `pools[0].entries[6].functions[1].levels.max` = 30.0
- `pools[0].entries[6].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[7].type` = "minecraft:empty"
- `pools[0].entries[7].weight` = 52

### `data/enhancedcelestials2core/append_loot_tables/minecraft/chests/pillager_outpost.json`

- `type` = "minecraft:chest"
- `pools[0].rolls` = 0
- `pools[0].bonus_rolls` = 1
- `pools[0].entries[0].name` = "minecraft:iron_ingot"
- `pools[0].entries[0].type` = "minecraft:item"
- `pools[0].entries[0].weight` = 20
- `pools[0].entries[0].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[0].functions[0].count.min` = 4.0
- `pools[0].entries[0].functions[0].count.max` = 10.0
- `pools[0].entries[0].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[1].name` = "minecraft:iron_helmet"
- `pools[0].entries[1].type` = "minecraft:item"
- `pools[0].entries[1].weight` = 2
- `pools[0].entries[1].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[1].functions[0].damage.min` = 0.4
- `pools[0].entries[1].functions[0].damage.max` = 0.8
- `pools[0].entries[1].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[1].functions[1].levels.min` = 10.0
- `pools[0].entries[1].functions[1].levels.max` = 30.0
- `pools[0].entries[1].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[2].name` = "minecraft:iron_chestplate"
- `pools[0].entries[2].type` = "minecraft:item"
- `pools[0].entries[2].weight` = 2
- `pools[0].entries[2].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[2].functions[0].damage.min` = 0.4
- `pools[0].entries[2].functions[0].damage.max` = 0.8
- `pools[0].entries[2].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[2].functions[1].levels.min` = 10.0
- `pools[0].entries[2].functions[1].levels.max` = 30.0
- `pools[0].entries[2].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[3].name` = "minecraft:iron_leggings"
- `pools[0].entries[3].type` = "minecraft:item"
- `pools[0].entries[3].weight` = 2
- `pools[0].entries[3].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[3].functions[0].damage.min` = 0.4
- `pools[0].entries[3].functions[0].damage.max` = 0.8
- `pools[0].entries[3].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[3].functions[1].levels.min` = 10.0
- `pools[0].entries[3].functions[1].levels.max` = 30.0
- `pools[0].entries[3].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[4].name` = "minecraft:iron_boots"
- `pools[0].entries[4].type` = "minecraft:item"
- `pools[0].entries[4].weight` = 2
- `pools[0].entries[4].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[4].functions[0].damage.min` = 0.4
- `pools[0].entries[4].functions[0].damage.max` = 0.8
- `pools[0].entries[4].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[4].functions[1].levels.min` = 10.0
- `pools[0].entries[4].functions[1].levels.max` = 30.0
- `pools[0].entries[4].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[5].name` = "minecraft:crossbow"
- `pools[0].entries[5].type` = "minecraft:item"
- `pools[0].entries[5].weight` = 5
- `pools[0].entries[5].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[5].functions[0].damage.min` = 0.4
- `pools[0].entries[5].functions[0].damage.max` = 0.8
- `pools[0].entries[5].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[5].functions[1].levels.min` = 10.0
- `pools[0].entries[5].functions[1].levels.max` = 30.0
- `pools[0].entries[5].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[6].type` = "minecraft:empty"
- `pools[0].entries[6].weight` = 67

### `data/enhancedcelestials2core/append_loot_tables/minecraft/chests/ruined_portal.json`

- `type` = "minecraft:chest"
- `pools[0].rolls` = 0
- `pools[0].bonus_rolls` = 1
- `pools[0].entries[0].name` = "minecraft:obsidian"
- `pools[0].entries[0].type` = "minecraft:item"
- `pools[0].entries[0].weight` = 5
- `pools[0].entries[0].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[0].functions[0].count.min` = 2.0
- `pools[0].entries[0].functions[0].count.max` = 5.0
- `pools[0].entries[0].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[1].name` = "minecraft:iron_ingot"
- `pools[0].entries[1].type` = "minecraft:item"
- `pools[0].entries[1].weight` = 20
- `pools[0].entries[1].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[1].functions[0].count.min` = 4.0
- `pools[0].entries[1].functions[0].count.max` = 10.0
- `pools[0].entries[1].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[2].name` = "minecraft:ancient_debris"
- `pools[0].entries[2].type` = "minecraft:item"
- `pools[0].entries[2].weight` = 1
- `pools[0].entries[2].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[2].functions[0].count.min` = 0.0
- `pools[0].entries[2].functions[0].count.max` = 1.0
- `pools[0].entries[2].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[3].type` = "minecraft:empty"
- `pools[0].entries[3].weight` = 75

### `data/enhancedcelestials2core/append_loot_tables/minecraft/chests/shipwreck_supply.json`

- `type` = "minecraft:chest"
- `pools[0].rolls` = 0
- `pools[0].bonus_rolls` = 1
- `pools[0].entries[0].name` = "minecraft:diamond_axe"
- `pools[0].entries[0].type` = "minecraft:item"
- `pools[0].entries[0].weight` = 2
- `pools[0].entries[0].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[0].functions[0].damage.min` = 0.6
- `pools[0].entries[0].functions[0].damage.max` = 0.9
- `pools[0].entries[0].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[0].functions[1].levels.min` = 5.0
- `pools[0].entries[0].functions[1].levels.max` = 10.0
- `pools[0].entries[0].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[1].name` = "minecraft:diamond_sword"
- `pools[0].entries[1].type` = "minecraft:item"
- `pools[0].entries[1].weight` = 1
- `pools[0].entries[1].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[1].functions[0].damage.min` = 0.6
- `pools[0].entries[1].functions[0].damage.max` = 0.9
- `pools[0].entries[1].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[1].functions[1].levels.min` = 1.0
- `pools[0].entries[1].functions[1].levels.max` = 5.0
- `pools[0].entries[1].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[2].name` = "minecraft:iron_axe"
- `pools[0].entries[2].type` = "minecraft:item"
- `pools[0].entries[2].weight` = 5
- `pools[0].entries[2].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[2].functions[0].damage.min` = 0.6
- `pools[0].entries[2].functions[0].damage.max` = 0.9
- `pools[0].entries[2].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[2].functions[1].levels.min` = 1.0
- `pools[0].entries[2].functions[1].levels.max` = 25.0
- `pools[0].entries[2].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[3].name` = "minecraft:iron_sword"
- `pools[0].entries[3].type` = "minecraft:item"
- `pools[0].entries[3].weight` = 5
- `pools[0].entries[3].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[3].functions[0].damage.min` = 0.6
- `pools[0].entries[3].functions[0].damage.max` = 0.9
- `pools[0].entries[3].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[3].functions[1].levels.min` = 1.0
- `pools[0].entries[3].functions[1].levels.max` = 25.0
- `pools[0].entries[3].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[4].name` = "minecraft:iron_helmet"
- `pools[0].entries[4].type` = "minecraft:item"
- `pools[0].entries[4].weight` = 2
- `pools[0].entries[4].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[4].functions[0].damage.min` = 0.4
- `pools[0].entries[4].functions[0].damage.max` = 0.8
- `pools[0].entries[4].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[4].functions[1].levels.min` = 10.0
- `pools[0].entries[4].functions[1].levels.max` = 30.0
- `pools[0].entries[4].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[5].name` = "minecraft:iron_chestplate"
- `pools[0].entries[5].type` = "minecraft:item"
- `pools[0].entries[5].weight` = 2
- `pools[0].entries[5].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[5].functions[0].damage.min` = 0.4
- `pools[0].entries[5].functions[0].damage.max` = 0.8
- `pools[0].entries[5].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[5].functions[1].levels.min` = 10.0
- `pools[0].entries[5].functions[1].levels.max` = 30.0
- `pools[0].entries[5].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[6].name` = "minecraft:iron_leggings"
- `pools[0].entries[6].type` = "minecraft:item"
- `pools[0].entries[6].weight` = 2
- `pools[0].entries[6].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[6].functions[0].damage.min` = 0.4
- `pools[0].entries[6].functions[0].damage.max` = 0.8
- `pools[0].entries[6].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[6].functions[1].levels.min` = 10.0
- `pools[0].entries[6].functions[1].levels.max` = 30.0
- `pools[0].entries[6].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[7].name` = "minecraft:iron_boots"
- `pools[0].entries[7].type` = "minecraft:item"
- `pools[0].entries[7].weight` = 2
- `pools[0].entries[7].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[7].functions[0].damage.min` = 0.4
- `pools[0].entries[7].functions[0].damage.max` = 0.8
- `pools[0].entries[7].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[7].functions[1].levels.min` = 10.0
- `pools[0].entries[7].functions[1].levels.max` = 30.0
- `pools[0].entries[7].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[8].type` = "minecraft:empty"
- `pools[0].entries[8].weight` = 79

### `data/enhancedcelestials2core/append_loot_tables/minecraft/chests/shipwreck_treasure.json`

- `type` = "minecraft:chest"
- `pools[0].rolls` = 0
- `pools[0].bonus_rolls` = 1
- `pools[0].entries[0].name` = "minecraft:diamond"
- `pools[0].entries[0].type` = "minecraft:item"
- `pools[0].entries[0].weight` = 5
- `pools[0].entries[0].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[0].functions[0].count.min` = 2.0
- `pools[0].entries[0].functions[0].count.max` = 5.0
- `pools[0].entries[0].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[1].name` = "minecraft:iron_ingot"
- `pools[0].entries[1].type` = "minecraft:item"
- `pools[0].entries[1].weight` = 10
- `pools[0].entries[1].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[1].functions[0].count.min` = 4.0
- `pools[0].entries[1].functions[0].count.max` = 10.0
- `pools[0].entries[1].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[2].name` = "minecraft:emerald"
- `pools[0].entries[2].type` = "minecraft:item"
- `pools[0].entries[2].weight` = 5
- `pools[0].entries[2].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[2].functions[0].count.min` = 2.0
- `pools[0].entries[2].functions[0].count.max` = 8.0
- `pools[0].entries[2].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[3].name` = "minecraft:gold_ingot"
- `pools[0].entries[3].type` = "minecraft:item"
- `pools[0].entries[3].weight` = 10
- `pools[0].entries[3].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[3].functions[0].count.min` = 2.0
- `pools[0].entries[3].functions[0].count.max` = 8.0
- `pools[0].entries[3].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[4].type` = "minecraft:empty"
- `pools[0].entries[4].weight` = 70

### `data/enhancedcelestials2core/append_loot_tables/minecraft/chests/simple_dungeon.json`

- `type` = "minecraft:chest"
- `pools[0].rolls` = 0
- `pools[0].bonus_rolls` = 1
- `pools[0].entries[0].name` = "minecraft:diamond"
- `pools[0].entries[0].type` = "minecraft:item"
- `pools[0].entries[0].weight` = 15
- `pools[0].entries[0].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[0].functions[0].count.min` = 2.0
- `pools[0].entries[0].functions[0].count.max` = 5.0
- `pools[0].entries[0].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[1].name` = "minecraft:iron_ingot"
- `pools[0].entries[1].type` = "minecraft:item"
- `pools[0].entries[1].weight` = 20
- `pools[0].entries[1].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[1].functions[0].count.min` = 4.0
- `pools[0].entries[1].functions[0].count.max` = 10.0
- `pools[0].entries[1].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[2].name` = "minecraft:diamond_sword"
- `pools[0].entries[2].type` = "minecraft:item"
- `pools[0].entries[2].weight` = 1
- `pools[0].entries[2].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[2].functions[0].damage.min` = 0.3
- `pools[0].entries[2].functions[0].damage.max` = 0.9
- `pools[0].entries[2].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[2].functions[1].levels.min` = 1.0
- `pools[0].entries[2].functions[1].levels.max` = 14.0
- `pools[0].entries[2].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[3].type` = "minecraft:item"
- `pools[0].entries[3].weight` = 5
- `pools[0].entries[3].functions[0].function` = "minecraft:enchant_randomly"
- `pools[0].entries[3].name` = "minecraft:book"
- `pools[0].entries[4].type` = "minecraft:empty"
- `pools[0].entries[4].weight` = 60

### `data/enhancedcelestials2core/append_loot_tables/minecraft/chests/stronghold_corridor.json`

- `type` = "minecraft:chest"
- `pools[0].rolls` = 0
- `pools[0].bonus_rolls` = 1
- `pools[0].entries[0].name` = "minecraft:diamond"
- `pools[0].entries[0].type` = "minecraft:item"
- `pools[0].entries[0].weight` = 15
- `pools[0].entries[0].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[0].functions[0].count.min` = 1.0
- `pools[0].entries[0].functions[0].count.max` = 5.0
- `pools[0].entries[0].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[1].name` = "minecraft:iron_ingot"
- `pools[0].entries[1].type` = "minecraft:item"
- `pools[0].entries[1].weight` = 20
- `pools[0].entries[1].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[1].functions[0].count.min` = 4.0
- `pools[0].entries[1].functions[0].count.max` = 10.0
- `pools[0].entries[1].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[2].type` = "minecraft:item"
- `pools[0].entries[2].weight` = 5
- `pools[0].entries[2].functions[0].function` = "minecraft:enchant_randomly"
- `pools[0].entries[2].name` = "minecraft:book"
- `pools[0].entries[3].type` = "minecraft:empty"
- `pools[0].entries[3].weight` = 60

### `data/enhancedcelestials2core/append_loot_tables/minecraft/chests/stronghold_crossing.json`

- `type` = "minecraft:chest"
- `pools[0].rolls` = 0
- `pools[0].bonus_rolls` = 1
- `pools[0].entries[0].name` = "minecraft:diamond"
- `pools[0].entries[0].type` = "minecraft:item"
- `pools[0].entries[0].weight` = 2
- `pools[0].entries[0].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[0].functions[0].count.min` = 1.0
- `pools[0].entries[0].functions[0].count.max` = 5.0
- `pools[0].entries[0].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[1].name` = "minecraft:iron_ingot"
- `pools[0].entries[1].type` = "minecraft:item"
- `pools[0].entries[1].weight` = 20
- `pools[0].entries[1].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[1].functions[0].count.min` = 4.0
- `pools[0].entries[1].functions[0].count.max` = 10.0
- `pools[0].entries[1].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[2].name` = "minecraft:ender_pearl"
- `pools[0].entries[2].type` = "minecraft:item"
- `pools[0].entries[2].weight` = 20
- `pools[0].entries[2].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[2].functions[0].count.min` = 1.0
- `pools[0].entries[2].functions[0].count.max` = 4.0
- `pools[0].entries[2].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[3].type` = "minecraft:empty"
- `pools[0].entries[3].weight` = 58

### `data/enhancedcelestials2core/append_loot_tables/minecraft/chests/stronghold_library.json`

- `type` = "minecraft:chest"
- `pools[0].rolls` = 0
- `pools[0].bonus_rolls` = 1
- `pools[0].entries[0].type` = "minecraft:item"
- `pools[0].entries[0].weight` = 5
- `pools[0].entries[0].functions[0].function` = "minecraft:enchant_randomly"
- `pools[0].entries[0].name` = "minecraft:book"
- `pools[0].entries[1].type` = "minecraft:empty"
- `pools[0].entries[1].weight` = 95

### `data/enhancedcelestials2core/append_loot_tables/minecraft/chests/underwater_ruin_big.json`

- `type` = "minecraft:chest"
- `pools[0].rolls` = 0
- `pools[0].bonus_rolls` = 1
- `pools[0].entries[0].name` = "minecraft:diamond"
- `pools[0].entries[0].type` = "minecraft:item"
- `pools[0].entries[0].weight` = 10
- `pools[0].entries[0].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[0].functions[0].count.min` = 2.0
- `pools[0].entries[0].functions[0].count.max` = 5.0
- `pools[0].entries[0].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[1].name` = "minecraft:iron_ingot"
- `pools[0].entries[1].type` = "minecraft:item"
- `pools[0].entries[1].weight` = 20
- `pools[0].entries[1].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[1].functions[0].count.min` = 4.0
- `pools[0].entries[1].functions[0].count.max` = 10.0
- `pools[0].entries[1].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[2].type` = "minecraft:item"
- `pools[0].entries[2].weight` = 5
- `pools[0].entries[2].functions[0].function` = "minecraft:enchant_randomly"
- `pools[0].entries[2].name` = "minecraft:book"
- `pools[0].entries[3].type` = "minecraft:empty"
- `pools[0].entries[3].weight` = 70

### `data/enhancedcelestials2core/append_loot_tables/minecraft/chests/underwater_ruin_small.json`

- `type` = "minecraft:chest"
- `pools[0].rolls` = 0
- `pools[0].bonus_rolls` = 1
- `pools[0].entries[0].name` = "minecraft:diamond"
- `pools[0].entries[0].type` = "minecraft:item"
- `pools[0].entries[0].weight` = 10
- `pools[0].entries[0].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[0].functions[0].count.min` = 2.0
- `pools[0].entries[0].functions[0].count.max` = 5.0
- `pools[0].entries[0].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[1].name` = "minecraft:iron_ingot"
- `pools[0].entries[1].type` = "minecraft:item"
- `pools[0].entries[1].weight` = 20
- `pools[0].entries[1].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[1].functions[0].count.min` = 4.0
- `pools[0].entries[1].functions[0].count.max` = 10.0
- `pools[0].entries[1].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[2].type` = "minecraft:item"
- `pools[0].entries[2].weight` = 5
- `pools[0].entries[2].functions[0].function` = "minecraft:enchant_randomly"
- `pools[0].entries[2].name` = "minecraft:book"
- `pools[0].entries[3].type` = "minecraft:empty"
- `pools[0].entries[3].weight` = 70

### `data/enhancedcelestials2core/append_loot_tables/minecraft/chests/woodland_mansion.json`

- `type` = "minecraft:chest"
- `pools[0].rolls` = 0
- `pools[0].bonus_rolls` = 1
- `pools[0].entries[0].name` = "minecraft:diamond"
- `pools[0].entries[0].type` = "minecraft:item"
- `pools[0].entries[0].weight` = 5
- `pools[0].entries[0].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[0].functions[0].count.min` = 2.0
- `pools[0].entries[0].functions[0].count.max` = 5.0
- `pools[0].entries[0].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[1].name` = "minecraft:totem_of_undying"
- `pools[0].entries[1].type` = "minecraft:item"
- `pools[0].entries[1].weight` = 3
- `pools[0].entries[1].functions[0].function` = "minecraft:set_count"
- `pools[0].entries[1].functions[0].count.min` = 1.0
- `pools[0].entries[1].functions[0].count.max` = 1.0
- `pools[0].entries[1].functions[0].count.type` = "minecraft:uniform"
- `pools[0].entries[2].name` = "minecraft:iron_axe"
- `pools[0].entries[2].type` = "minecraft:item"
- `pools[0].entries[2].weight` = 10
- `pools[0].entries[2].functions[0].function` = "minecraft:set_damage"
- `pools[0].entries[2].functions[0].damage.min` = 0.6
- `pools[0].entries[2].functions[0].damage.max` = 0.9
- `pools[0].entries[2].functions[1].function` = "minecraft:enchant_with_levels"
- `pools[0].entries[2].functions[1].levels.min` = 1.0
- `pools[0].entries[2].functions[1].levels.max` = 35.0
- `pools[0].entries[2].functions[1].levels.type` = "minecraft:uniform"
- `pools[0].entries[3].type` = "minecraft:empty"
- `pools[0].entries[3].weight` = 67

### `data/enhancedcelestials2core/tags/enhancedcelestials2core/lunar/event/moon.json`

- `values` = ["enhancedcelestials2core:default"]

### `data/minecraft/enhancedcelestials2core/lunar/dimension_settings/overworld.json`

- `day_length` = 24000
- `default` = "enhancedcelestials2core:default"
- `max_days_between_all_events` = 98
- `min_days_between_all_events` = 3
- `night_start_time` = 12500
- `requires_clear_skies` = true
- `tracked_past_events_max_count` = 100
- `year_length_in_days` = 100

## Testi nel codice


### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/DropSettings.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarEvent.class`

- "getTranslationKey"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarForecast.class`

- "customTranslationTextComponent"
- "()Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;"
- "dev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent"
- "translatable"
- "getTranslationKey"
- "translationKey"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarTextComponents$Notification.class`

- "customTranslationTextComponent"
- "Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;"
- "dev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent"
- "translatable"
- "(Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarTextComponents$NotificationType;)V"
- "()Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;"
- "(Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarTextComponents$Notification;)Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;"
- "(Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarTextComponents$NotificationType;)Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarTextComponents$Notification;"
- "customTranslationTextComponent;notificationType"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarTextComponents.class`

- "(Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarTextComponents$NotificationType;)V"
- "translatable"
- "(Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;)V"
- "Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/MobEffectInstanceBuilder.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/AnvilCostModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/BeaconRadiusModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/BlockItemDropModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/BlockSleepingModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/DisableBiomeSpawnSettingsModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/EnchantmentCostModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/EntityDropModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/ExperienceModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/ForceSurfaceSpawningModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/GlowColorModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MobEffectsModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MobEquipment.class`

- "translatable"
- "translationKey"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MobSpawnDistancesModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MobSpawnSettingsModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MoonSizeModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MoonTextureColorModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MoonTextureModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/NameColorModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/SkyLightColorModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/SlimesSpawnEverywhereModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/SoundTrackModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/SpawnCategoryMultiplierModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/TextComponentsModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/VillageSiegeProbabilityModifier.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/client/AddonPrompts.class`

- "dev/corgitaco/enhancedcelestials2core/util/Translations$Config"
- "notifyIfUnconfigured"
- "dev/corgitaco/enhancedcelestials2core/client/AddonPrompts"
- "dev/corgitaco/enhancedcelestials2core/util/AddonPrompt"
- "enhancedcelestials2core.missing_addon.shaders.prompt"
- "sendPrompt"
- "enhancedcelestials2core.missing_addon.default_lunar_events.prompt"
- "translatable"
- "SHADER_SUPPORT_PROMPT_ID"
- "DEFAULT_LUNAR_EVENTS_PROMPT_ID"
- "Ldev/corgitaco/enhancedcelestials2core/client/AddonPrompts;"
- "sentTranslations"
- "AddonPrompts.java"
- "dev/corgitaco/enhancedcelestials2core/util/Translations"
- "Config"

### `dev/corgitaco/enhancedcelestials2core/client/EC2ClientCommands.class`

- "ecc"
- "config"
- "translate"
- "dev/corgitaco/enhancedcelestials2core/util/Translations"
- "dev/corgitaco/enhancedcelestials2core/client/screen/TranslationConfigScreen"
- "translatable"
- "dev/corgitaco/enhancedcelestials2core/client/AddonPrompts"
- "dev/corgitaco/enhancedcelestials2core/util/AddonPrompt"
- "dev/corgitaco/enhancedcelestials2core/client/screen/EC2ConfigScreen"

### `dev/corgitaco/enhancedcelestials2core/client/screen/ConfigureAction.class`

- "dev/corgitaco/enhancedcelestials2core/client/screen/ConfigureAction"
- "Ldev/corgitaco/enhancedcelestials2core/client/screen/ConfigureAction;"
- "ConfigureAction.java"

### `dev/corgitaco/enhancedcelestials2core/client/screen/EC2ConfigScreen.class`

- "enhancedcelestials2core.config.title"
- "translatable"
- "dev/corgitaco/enhancedcelestials2core/client/screen/EC2ConfigScreen"
- "enhancedcelestials2core.config.configure"
- "enhancedcelestials2core.config.translation_settings"
- "dev/corgitaco/enhancedcelestials2core/client/screen/ConfigureAction"
- "(Ldev/corgitaco/enhancedcelestials2core/client/screen/EC2ConfigScreen;)Lnet/minecraft/client/gui/components/Button$OnPress;"
- "enhancedcelestials2core.config.support"
- "dev/corgitaco/enhancedcelestials2core/client/screen/TranslationConfigScreen"
- "CONFIGURE_URL"
- "Ldev/corgitaco/enhancedcelestials2core/client/screen/EC2ConfigScreen;"
- "configureText"
- "translationText"
- "configurePress"
- "EC2ConfigScreen.java"

### `dev/corgitaco/enhancedcelestials2core/client/screen/MissingAddonScreen.class`

- "translatable"
- "enhancedcelestials2core.config.support"

### `dev/corgitaco/enhancedcelestials2core/client/screen/TranslationConfigScreen.class`

- "enhancedcelestials2core.translation_config.title"
- "translatable"
- "dev/corgitaco/enhancedcelestials2core/client/screen/TranslationConfigScreen"
- "dev/corgitaco/enhancedcelestials2core/util/Translations$Config"
- "()Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config;"
- "config"
- "Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config;"
- "dev/corgitaco/enhancedcelestials2core/util/Translations$Config$TranslationMode"
- "()[Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config$TranslationMode;"
- "Translation_Mode"
- "Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config$TranslationMode;"
- "enhancedcelestials2core.translation_config.mode"
- "(Ldev/corgitaco/enhancedcelestials2core/client/screen/TranslationConfigScreen;)Lnet/minecraft/client/gui/components/CycleButton$OnValueChange;"
- "Prompt_Language_When_Translation_Incomplete"
- "enhancedcelestials2core.translation_config.prompt_incomplete"
- "override_existing_translations"
- "enhancedcelestials2core.translation_config.override_existing"
- "(Ldev/corgitaco/enhancedcelestials2core/client/screen/TranslationConfigScreen;)Lnet/minecraft/client/gui/components/Button$OnPress;"
- "enhancedcelestials2core.translation_config.done.tooltip"
- "enhancedcelestials2core.translation_config.cancel.tooltip"
- "enhancedcelestials2core.config.support"
- "(Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config;)V"
- "enhancedcelestials2core.translation_config.override_existing.tooltip"
- "enhancedcelestials2core.translation_config.prompt_incomplete.tooltip"
- "enhancedcelestials2core.translation_config.mode.tooltip"
- "Ldev/corgitaco/enhancedcelestials2core/client/screen/TranslationConfigScreen;"
- "(Lnet/minecraft/client/gui/components/CycleButton;Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config$TranslationMode;)V"
- "(Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config$TranslationMode;)Lnet/minecraft/client/gui/components/Tooltip;"
- "(Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config$TranslationMode;)Lnet/minecraft/network/chat/Component;"
- "TranslationConfigScreen.java"
- "enhancedcelestials2core.translation_config.mode.\u0001"
- "dev/corgitaco/enhancedcelestials2core/util/Translations"
- "Config"
- "TranslationMode"

### `dev/corgitaco/enhancedcelestials2core/client/screen/widget/SupportButton.class`

- "enhancedcelestials2core.config.support.tooltip"
- "translatable"

### `dev/corgitaco/enhancedcelestials2core/config/EC2MixinConfig.class`

- "dev/corgitaco/enhancedcelestials2core/config/EC2MixinConfig"
- "./config/enhancedcelestials2core/mixins.properties"
- "Ldev/corgitaco/enhancedcelestials2core/config/EC2MixinConfig;"
- "EC2MixinConfig.java"

### `dev/corgitaco/enhancedcelestials2core/mixin/EnhancedCelestialsMixinPlugin.class`

- "dev/corgitaco/enhancedcelestials2core/config/EC2MixinConfig"
- "mixinConfig"
- "Ldev/corgitaco/enhancedcelestials2core/config/EC2MixinConfig;"
- "org/spongepowered/asm/mixin/extensibility/IMixinConfigPlugin"
- "getRefMapperConfig"

### `dev/corgitaco/enhancedcelestials2core/mixin/LivingEntityMixin.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/mixin/client/LanguageMixin.class`

- "dev/corgitaco/enhancedcelestials2core/util/Translations"

### `dev/corgitaco/enhancedcelestials2core/neoforge/EnhancedCelestialsNeoForge.class`

- "registerConfigScreen"

### `dev/corgitaco/enhancedcelestials2core/neoforge/client/EnhancedCelestialsNeoForgeClient.class`

- "dev/corgitaco/enhancedcelestials2core/client/AddonPrompts"
- "net/neoforged/neoforge/client/gui/IConfigScreenFactory"
- "()Lnet/neoforged/neoforge/client/gui/IConfigScreenFactory;"
- "dev/corgitaco/enhancedcelestials2core/client/screen/EC2ConfigScreen"
- "registerConfigScreen"
- "lambda$registerConfigScreen$0"

### `dev/corgitaco/enhancedcelestials2core/neoforge/platform/ForgePlatformHelper.class`

- "CONFIGDIR"
- "configDir"

### `dev/corgitaco/enhancedcelestials2core/platform/services/IPlatformHelper.class`

- "configDir"

### `dev/corgitaco/enhancedcelestials2core/server/commands/DumpModifiersCommand.class`

- "translatable"
- "getTranslationKey"

### `dev/corgitaco/enhancedcelestials2core/server/commands/LunarForecastCommand.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/server/commands/ScheduleLunarEventCommand.class`

- "translatable"
- "getTranslationKey"

### `dev/corgitaco/enhancedcelestials2core/server/commands/SetLunarEventCommand.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/util/AddonPrompt.class`

- "dev/corgitaco/enhancedcelestials2core/util/AddonPrompt"
- "Ldev/corgitaco/enhancedcelestials2core/util/AddonPrompt;"
- "AddonPrompt.java"
- "{\n  \"_comment\": \"This file's presence hides the '\u0001' addon prompt. Ship it with your modpack to hide the prompt for players.\"\n}"
- "./config/enhancedcelestials2core/\u0001-prompt.json"

### `dev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent.class`

- "dev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent"
- "(Ljava/lang/String;Lnet/minecraft/network/chat/Style;[Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;)V"
- "translationKey"
- "translatable"
- "[Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;"
- "Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;"
- "Lcom/mojang/serialization/Codec<Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;>;"
- "Ljava/util/List<Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;>;"
- "(Ljava/lang/String;[Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;)V"
- "(Ljava/lang/String;Lnet/minecraft/network/chat/Style;Ljava/util/List<Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;>;)V"
- "(Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;)Lnet/minecraft/network/chat/Component;"
- "customTranslationTextComponent"
- "(Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;)Ljava/util/List;"
- "(Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;)Lnet/minecraft/network/chat/Style;"
- "(Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;)Ljava/lang/String;"
- "CustomTranslationTextComponent.java"
- "(Ljava/lang/String;Lnet/minecraft/network/chat/Style;Ljava/util/List;)Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;"

### `dev/corgitaco/enhancedcelestials2core/util/TimeCommandUtil.class`

- "translatable"

### `dev/corgitaco/enhancedcelestials2core/util/Translations$Cache.class`

- "config"
- "translations-cache"
- "dev/corgitaco/enhancedcelestials2core/util/Translations$Cache"
- "translations"
- "dev/corgitaco/enhancedcelestials2core/util/Translations"
- "Failed to read cached translations for {}/{}"
- "Failed to write cached translations for {}/{}"
- "Ldev/corgitaco/enhancedcelestials2core/util/Translations$Cache;"
- "Translations.java"
- "\u0001.json"

### `dev/corgitaco/enhancedcelestials2core/util/Translations$Config$TranslationMode.class`

- "dev/corgitaco/enhancedcelestials2core/util/Translations$Config$TranslationMode"
- "Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config$TranslationMode;"
- "[Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config$TranslationMode;"
- "()[Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config$TranslationMode;"
- "(Ljava/lang/String;)Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config$TranslationMode;"
- "Ljava/lang/Enum<Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config$TranslationMode;>;"
- "Translations.java"
- "dev/corgitaco/enhancedcelestials2core/util/Translations"
- "dev/corgitaco/enhancedcelestials2core/util/Translations$Config"
- "Config"
- "TranslationMode"

### `dev/corgitaco/enhancedcelestials2core/util/Translations$Config.class`

- "dev/corgitaco/enhancedcelestials2core/util/Translations$Config$TranslationMode"
- "Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config$TranslationMode;"
- "dev/corgitaco/enhancedcelestials2core/util/Translations$Config"
- "Translation_Mode"
- "Prompt_Language_When_Translation_Incomplete"
- "override_existing_translations"
- "dev/corgitaco/enhancedcelestials2core/util/Translations"
- "/ecc translate config"
- "enhancedcelestials2core.translation.not_configured"
- "translatable"
- "./config/enhancedcelestials2core/translations.json"
- "Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config;"
- "()Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config;"
- "config"
- "(Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config;)V"
- "notifyIfUnconfigured"
- "Translations.java"
- "Config"
- "TranslationMode"

### `dev/corgitaco/enhancedcelestials2core/util/Translations$Contribution.class`

- "dev/corgitaco/enhancedcelestials2core/util/Translations$Contribution"
- "dev/corgitaco/enhancedcelestials2core/util/Translations"
- "./config/enhancedcelestials2core/translation-contribution.json"
- "Ldev/corgitaco/enhancedcelestials2core/util/Translations$Contribution;"
- "Translations.java"

### `dev/corgitaco/enhancedcelestials2core/util/Translations.class`

- "dev/corgitaco/enhancedcelestials2core/util/Translations"
- "injectTranslations"
- "promptContributeIfIncomplete"
- "dev/corgitaco/enhancedcelestials2core/util/Translations$Contribution"
- "dev/corgitaco/enhancedcelestials2core/util/Translations$Config"
- "()Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config;"
- "Prompt_Language_When_Translation_Incomplete"
- "/ecc translate contribute"
- "enhancedcelestials2core.translation.incomplete"
- "translatable"
- "Translation_Mode"
- "Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config$TranslationMode;"
- "dev/corgitaco/enhancedcelestials2core/util/Translations$Config$TranslationMode"
- "(Ljava/lang/String;Ljava/util/Set;Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config;)Ljava/util/function/Consumer;"
- "Failed to inject translations for {}/{}"
- "override_existing_translations"
- "dev/corgitaco/enhancedcelestials2core/util/Translations$Cache"
- "https://translations.corgitaco.dev/"
- "Ldev/corgitaco/enhancedcelestials2core/util/Translations;"
- "localTranslations"
- "config"
- "Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config;"
- "lambda$injectTranslations$8"
- "lambda$injectTranslations$7"
- "(Ljava/lang/String;Ljava/util/Set;Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config;Lcom/google/gson/JsonObject;)V"
- "Translations.java"
- "https://translations.corgitaco.dev/\u0001/get/\u0001.json"
- "https://translations.corgitaco.dev/\u0001/contribute"
- "Config"
- "TranslationMode"
