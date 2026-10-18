# Enhanced Celestials 2: Core (enhanced-celestials-2-core)

File generato da `scripts/esamina.py` (workflow "Esamina mod"): la mod **non** è nel pack. Non modificarlo a mano.

- Versione: **2.0.3.3-neoforge** (release, 2026-09-07), file `Enhanced-Celestials-2-Core-NeoForge-1.21.1-2.0.3.3.jar`, id versione `CWaaEX5L`
- Licenza su Modrinth: LicenseRef-All-Rights-Reserved · download: 66767
- Filtro dei valori: `enhancedcelestials|lunar|moon` · filtro dei testi del codice: `(?i)^(automatic|manual|disabled)$|gson|getSerializedName|getAsString|getAsBoolean|JsonObject|fromJson|toJson|translations\.json|Translation_Mode|override_existing|Prompt_Language|codec`

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

- "DROP_ENHANCER_CODEC"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/codecs/RecordCodecBuilder;"
- "com/mojang/serialization/codecs/RecordCodecBuilder$Instance"
- "hashedCodec"
- "(Lnet/minecraft/resources/ResourceKey;)Lcom/mojang/serialization/Codec;"
- "codec"
- "(Lcom/mojang/serialization/Codec;Lcom/mojang/serialization/Codec;)Lcom/mojang/serialization/Codec;"
- "TARGET_CODEC"
- "Lcom/mojang/serialization/codecs/PrimitiveCodec;"
- "(Lcom/mojang/serialization/Codec;Lcom/mojang/serialization/Codec;)Lcom/mojang/serialization/codecs/UnboundedMapCodec;"
- "MULTIPLIERS_CODEC"
- "(II)Lcom/mojang/serialization/Codec;"
- "()Lcom/mojang/serialization/Codec;"
- "DROP_ENHANCER_ENTRY_CODEC"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/Codec;"
- "LEGACY_DROP_ENHANCER_CODEC"
- "com/mojang/serialization/codecs/RecordCodecBuilder"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/Codec;"
- "CODEC"
- "Lcom/mojang/serialization/Codec<Lcom/mojang/datafixers/util/Either<Lnet/minecraft/tags/TagKey<Lnet/minecraft/world/item/Item;>;Lnet/minecraft/resources/ResourceKey<Lnet/minecraft/world/item/Item;>;>;>;"
- "Lcom/mojang/serialization/Codec<Ljava/util/Map<Lcom/mojang/datafixers/util/Either<Lnet/minecraft/tags/TagKey<Lnet/minecraft/world/item/Item;>;Lnet/minecraft/resources/ResourceKey<Lnet/minecraft/world/item/Item;>;>;Ljava/lang/Double;>;>;"
- "Lcom/mojang/serialization/Codec<Lcom/mojang/datafixers/util/Pair<Ljava/lang/Integer;Ljava/util/Map<Lcom/mojang/datafixers/util/Either<Lnet/minecraft/tags/TagKey<Lnet/minecraft/world/item/Item;>;Lnet/minecraft/resources/ResourceKey<Lnet/minecraft/world/item/Item;>;>;Ljava/lang/Double;>;>;>;"
- "Lcom/mojang/serialization/Codec<Ljava/util/List<Lcom/mojang/datafixers/util/Pair<Ljava/lang/Integer;Ljava/util/Map<Lcom/mojang/datafixers/util/Either<Lnet/minecraft/tags/TagKey<Lnet/minecraft/world/item/Item;>;Lnet/minecraft/resources/ResourceKey<Lnet/minecraft/world/item/Item;>;>;Ljava/lang/Double;…"
- "Lcom/mojang/serialization/Codec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/DropSettings;>;"
- "(Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;)Lcom/mojang/datafixers/kinds/App;"
- "Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarDimensionSettings.class`

- "codec"
- "(Lnet/minecraft/resources/ResourceKey;)Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/codecs/RecordCodecBuilder;"
- "Lcom/mojang/serialization/codecs/PrimitiveCodec;"
- "com/mojang/serialization/codecs/PrimitiveCodec"
- "(Ljava/lang/Object;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/codecs/RecordCodecBuilder$Instance"
- "com/mojang/serialization/codecs/RecordCodecBuilder"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/Codec;"
- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "Lcom/mojang/serialization/Codec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarDimensionSettings;>;"
- "(Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;)Lcom/mojang/datafixers/kinds/App;"
- "Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarEvent$SpawnRequirements.class`

- "com/mojang/serialization/Codec"
- "Lcom/mojang/serialization/codecs/PrimitiveCodec;"
- "com/mojang/serialization/codecs/PrimitiveCodec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/codecs/RecordCodecBuilder;"
- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "dev/corgitaco/enhancedcelestials2core/util/CodecUtil"
- "(Lnet/minecraft/resources/ResourceKey;Lcom/mojang/serialization/Codec;)Lcom/mojang/serialization/Codec;"
- "()Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/codecs/RecordCodecBuilder$Instance"
- "com/mojang/serialization/codecs/RecordCodecBuilder"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/Codec;"
- "Lcom/mojang/serialization/Codec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarEvent$SpawnRequirements;>;"
- "(Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;)Lcom/mojang/datafixers/kinds/App;"
- "Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarEvent.class`

- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "dev/corgitaco/enhancedcelestials2core/util/CodecUtil"
- "(Lnet/minecraft/resources/ResourceKey;Lcom/mojang/serialization/Codec;)Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "()Lcom/mojang/serialization/Codec;"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/codecs/RecordCodecBuilder;"
- "com/mojang/serialization/codecs/RecordCodecBuilder$Instance"
- "com/mojang/serialization/codecs/RecordCodecBuilder"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/Codec;"
- "BASE_CODEC"
- "DIRECT_CODEC"
- "Lcom/mojang/serialization/Codec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarEvent;>;"
- "(Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;)Lcom/mojang/datafixers/kinds/App;"
- "Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarEventProbabilities$DimensionProbability.class`

- "com/mojang/serialization/Codec"
- "Lcom/mojang/serialization/codecs/PrimitiveCodec;"
- "com/mojang/serialization/codecs/PrimitiveCodec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/codecs/RecordCodecBuilder;"
- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/codecs/RecordCodecBuilder$Instance"
- "com/mojang/serialization/codecs/RecordCodecBuilder"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/Codec;"
- "Lcom/mojang/serialization/Codec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarEventProbabilities$DimensionProbability;>;"
- "(Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;)Lcom/mojang/datafixers/kinds/App;"
- "Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarEventProbabilities.class`

- "codec"
- "(Lnet/minecraft/resources/ResourceKey;)Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/codecs/RecordCodecBuilder;"
- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "(Lcom/mojang/serialization/Codec;Lcom/mojang/serialization/Codec;)Lcom/mojang/serialization/codecs/UnboundedMapCodec;"
- "com/mojang/serialization/codecs/UnboundedMapCodec"
- "com/mojang/serialization/codecs/RecordCodecBuilder$Instance"
- "com/mojang/serialization/codecs/RecordCodecBuilder"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/Codec;"
- "Lcom/mojang/serialization/Codec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarEventProbabilities;>;"
- "(Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;)Lcom/mojang/datafixers/kinds/App;"
- "Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarForecast.class`

- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "()Lcom/mojang/serialization/Codec;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarTextComponents$Notification.class`

- "getSerializedName"
- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/codecs/RecordCodecBuilder;"
- "com/mojang/serialization/codecs/RecordCodecBuilder$Instance"
- "com/mojang/serialization/codecs/RecordCodecBuilder"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/Codec;"
- "Lcom/mojang/serialization/Codec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarTextComponents$Notification;>;"
- "(Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;)Lcom/mojang/datafixers/kinds/App;"
- "Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarTextComponents$NotificationType.class`

- "(Ljava/util/function/Supplier;)Lnet/minecraft/util/StringRepresentable$EnumCodec;"
- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "Lcom/mojang/serialization/Codec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarTextComponents$NotificationType;>;"
- "getSerializedName"
- "net/minecraft/util/StringRepresentable$EnumCodec"
- "EnumCodec"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarTextComponents.class`

- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/lang/Object;)Lcom/mojang/serialization/MapCodec;"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/codecs/RecordCodecBuilder;"
- "com/mojang/serialization/codecs/RecordCodecBuilder$Instance"
- "com/mojang/serialization/codecs/RecordCodecBuilder"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/Codec;"
- "Lcom/mojang/serialization/Codec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/LunarTextComponents;>;"
- "(Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;)Lcom/mojang/datafixers/kinds/App;"
- "Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/MobEffectInstanceBuilder.class`

- "dev/corgitaco/enhancedcelestials2core/util/CodecUtil"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/codecs/RecordCodecBuilder;"
- "Lcom/mojang/serialization/codecs/PrimitiveCodec;"
- "com/mojang/serialization/codecs/PrimitiveCodec"
- "com/mojang/serialization/codecs/RecordCodecBuilder$Instance"
- "com/mojang/serialization/codecs/RecordCodecBuilder"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/Codec;"
- "CODEC"
- "Lcom/mojang/serialization/Codec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/MobEffectInstanceBuilder;>;"
- "(Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;)Lcom/mojang/datafixers/kinds/App;"
- "Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/AnvilCostModifier.class`

- "com/mojang/serialization/Codec"
- "Lcom/mojang/serialization/codecs/PrimitiveCodec;"
- "com/mojang/serialization/codecs/PrimitiveCodec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "CODEC"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/AnvilCostModifier;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/BeaconRadiusModifier.class`

- "com/mojang/serialization/Codec"
- "Lcom/mojang/serialization/codecs/PrimitiveCodec;"
- "com/mojang/serialization/codecs/PrimitiveCodec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "CODEC"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/BeaconRadiusModifier;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/BlockItemDropModifier.class`

- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/BlockItemDropModifier;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/BlockSleepingModifier.class`

- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/BlockSleepingModifier;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/DisableBiomeSpawnSettingsModifier.class`

- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Supplier;)Lcom/mojang/serialization/MapCodec;"
- "CODEC"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/DisableBiomeSpawnSettingsModifier;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/EnchantmentCostModifier.class`

- "com/mojang/serialization/Codec"
- "Lcom/mojang/serialization/codecs/PrimitiveCodec;"
- "com/mojang/serialization/codecs/PrimitiveCodec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "CODEC"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/EnchantmentCostModifier;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/EntityDropModifier.class`

- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "codec"
- "()Lcom/mojang/serialization/Codec;"
- "(Lcom/mojang/serialization/Codec;Lcom/mojang/serialization/Codec;)Lcom/mojang/serialization/Codec;"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/EntityDropModifier;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/EquipmentSet.class`

- "CODEC"
- "Lnet/minecraft/util/StringRepresentable$EnumCodec;"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "(Lcom/mojang/serialization/Codec;Lcom/mojang/serialization/Codec;)Lcom/mojang/serialization/codecs/UnboundedMapCodec;"
- "com/mojang/serialization/codecs/UnboundedMapCodec"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/Codec;"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/Codec;"
- "DIRECT_CODEC"
- "Lcom/mojang/serialization/Codec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/EquipmentSet;>;"
- "net/minecraft/util/StringRepresentable$EnumCodec"
- "EnumCodec"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/ExistingMobEquipmentModifier.class`

- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "()Lcom/mojang/serialization/Codec;"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/codecs/RecordCodecBuilder;"
- "com/mojang/serialization/codecs/RecordCodecBuilder$Instance"
- "com/mojang/serialization/codecs/RecordCodecBuilder"
- "mapCodec"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/ExistingMobEquipmentModifier;>;"
- "(Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;)Lcom/mojang/datafixers/kinds/App;"
- "Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/ExperienceModifier.class`

- "com/mojang/serialization/Codec"
- "Lcom/mojang/serialization/codecs/PrimitiveCodec;"
- "com/mojang/serialization/codecs/PrimitiveCodec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "CODEC"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/ExperienceModifier;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/ForceSurfaceSpawningModifier.class`

- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Supplier;)Lcom/mojang/serialization/MapCodec;"
- "CODEC"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/ForceSurfaceSpawningModifier;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/GlowColorModifier.class`

- "FLEXIBLE_COLOR_CODEC"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/codecs/RecordCodecBuilder;"
- "Lcom/mojang/serialization/codecs/PrimitiveCodec;"
- "com/mojang/serialization/codecs/PrimitiveCodec"
- "(Ljava/lang/String;Ljava/lang/Object;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/codecs/RecordCodecBuilder$Instance"
- "com/mojang/serialization/codecs/RecordCodecBuilder"
- "mapCodec"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "CODEC"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/GlowColorModifier;>;"
- "(Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;)Lcom/mojang/datafixers/kinds/App;"
- "Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/LunarEventModifierType.class`

- "codec"
- "()Lcom/mojang/serialization/MapCodec;"
- "()Lcom/mojang/serialization/MapCodec<TT;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/LunarEventModifierTypes.class`

- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "codec"
- "(Lcom/mojang/serialization/MapCodec;)Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/LunarEventModifierType;"
- "byNameCodec"
- "()Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "(Ljava/lang/String;Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/Codec;"
- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "Lcom/mojang/serialization/MapCodec;"
- "(Ljava/lang/String;Lcom/mojang/serialization/MapCodec;)Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/LunarEventModifierType;"
- "(Lcom/mojang/serialization/MapCodec;)Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/Codec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/LunarEventModifier;>;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/BlockItemDropModifier;>;"
- "(Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/BlockItemDropModifier;>;)Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/BlockItemDropModifier;>;"
- "settingsCodec"
- "Lcom/mojang/serialization/MapCodec<TT;>;"
- "<T::Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/LunarEventModifier;>(Ljava/lang/String;Lcom/mojang/serialization/MapCodec<TT;>;)Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/LunarEventModifierType<TT;>;"
- "()Lcom/mojang/serialization/MapCodec;"
- "(Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/LunarEventModifierType;)Lcom/mojang/serialization/MapCodec;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MobEffectsModifier.class`

- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "codec"
- "()Lcom/mojang/serialization/Codec;"
- "(Lcom/mojang/serialization/Codec;Lcom/mojang/serialization/Codec;)Lcom/mojang/serialization/Codec;"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MobEffectsModifier;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MobEquipment$EquipmentCombination.class`

- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/codecs/RecordCodecBuilder;"
- "(FF)Lcom/mojang/serialization/Codec;"
- "(Ljava/lang/String;Ljava/lang/Object;)Lcom/mojang/serialization/MapCodec;"
- "DIRECT_CODEC"
- "dev/corgitaco/enhancedcelestials2core/util/CodecUtil"
- "(Lnet/minecraft/resources/ResourceKey;Lcom/mojang/serialization/Codec;)Lcom/mojang/serialization/Codec;"
- "wrappedCodecAllowingEmpty"
- "(Lcom/mojang/serialization/Codec;)Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/codecs/RecordCodecBuilder$Instance"
- "com/mojang/serialization/codecs/RecordCodecBuilder"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/Codec;"
- "Lcom/mojang/serialization/Codec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MobEquipment$EquipmentCombination;>;"
- "(Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;)Lcom/mojang/datafixers/kinds/App;"
- "Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MobEquipment$EquipmentEntry.class`

- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/codecs/RecordCodecBuilder;"
- "NON_NEGATIVE_CODEC"
- "(Ljava/lang/String;Ljava/lang/Object;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/codecs/RecordCodecBuilder$Instance"
- "com/mojang/serialization/codecs/RecordCodecBuilder"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/Codec;"
- "Lcom/mojang/serialization/Codec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MobEquipment$EquipmentEntry;>;"
- "(Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;)Lcom/mojang/datafixers/kinds/App;"
- "Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MobSpawnDistancesModifier.class`

- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "Lcom/mojang/serialization/codecs/PrimitiveCodec;"
- "(Lcom/mojang/serialization/Codec;Lcom/mojang/serialization/Codec;)Lcom/mojang/serialization/codecs/UnboundedMapCodec;"
- "com/mojang/serialization/codecs/UnboundedMapCodec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MobSpawnDistancesModifier;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MobSpawnEquipmentModifier.class`

- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "()Lcom/mojang/serialization/Codec;"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/codecs/RecordCodecBuilder;"
- "com/mojang/serialization/codecs/RecordCodecBuilder$Instance"
- "com/mojang/serialization/codecs/RecordCodecBuilder"
- "mapCodec"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MobSpawnEquipmentModifier;>;"
- "(Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;)Lcom/mojang/datafixers/kinds/App;"
- "Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MobSpawnSettingsModifier.class`

- "CODEC"
- "Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MobSpawnSettingsModifier;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MoonSizeModifier.class`

- "com/mojang/serialization/Codec"
- "Lcom/mojang/serialization/codecs/PrimitiveCodec;"
- "com/mojang/serialization/codecs/PrimitiveCodec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "CODEC"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MoonSizeModifier;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MoonTextureColorModifier.class`

- "COLOR_CODEC"
- "Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "CODEC"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MoonTextureColorModifier;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MoonTextureModifier.class`

- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/MoonTextureModifier;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/NameColorModifier.class`

- "COLOR_CODEC"
- "Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "CODEC"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/NameColorModifier;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/SkyLightColorModifier.class`

- "COLOR_CODEC"
- "Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "CODEC"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/SkyLightColorModifier;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/SlimesSpawnEverywhereModifier.class`

- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Supplier;)Lcom/mojang/serialization/MapCodec;"
- "CODEC"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/SlimesSpawnEverywhereModifier;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/SoundTrackModifier.class`

- "DIRECT_CODEC"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "CODEC"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/SoundTrackModifier;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/SpawnCategoryMultiplierModifier.class`

- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "Lcom/mojang/serialization/codecs/PrimitiveCodec;"
- "(Lcom/mojang/serialization/Codec;Lcom/mojang/serialization/Codec;)Lcom/mojang/serialization/codecs/UnboundedMapCodec;"
- "com/mojang/serialization/codecs/UnboundedMapCodec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/SpawnCategoryMultiplierModifier;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/TextComponentsModifier.class`

- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/TextComponentsModifier;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/VillageSiegeProbabilityModifier.class`

- "com/mojang/serialization/Codec"
- "Lcom/mojang/serialization/codecs/PrimitiveCodec;"
- "com/mojang/serialization/codecs/PrimitiveCodec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "CODEC"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/modifier/VillageSiegeProbabilityModifier;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/spawnrule/LunarEventSpawnRuleType.class`

- "codec"
- "()Lcom/mojang/serialization/MapCodec;"
- "()Lcom/mojang/serialization/MapCodec<TT;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/spawnrule/LunarEventSpawnRuleTypes.class`

- "com/mojang/serialization/MapCodec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "codec"
- "(Lcom/mojang/serialization/MapCodec;)Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/spawnrule/LunarEventSpawnRuleType;"
- "byNameCodec"
- "()Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "(Ljava/lang/String;Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/Codec;"
- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "Lcom/mojang/serialization/MapCodec;"
- "(Ljava/lang/String;Lcom/mojang/serialization/MapCodec;)Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/spawnrule/LunarEventSpawnRuleType;"
- "Lcom/mojang/serialization/Codec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/spawnrule/LunarEventSpawnRule;>;"
- "settingsCodec"
- "Lcom/mojang/serialization/MapCodec<TT;>;"
- "<T::Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/spawnrule/LunarEventSpawnRule;>(Ljava/lang/String;Lcom/mojang/serialization/MapCodec<TT;>;)Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/spawnrule/LunarEventSpawnRuleType<TT;>;"
- "(Lcom/mojang/serialization/MapCodec;)Lcom/mojang/serialization/MapCodec;"
- "()Lcom/mojang/serialization/MapCodec;"
- "(Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/spawnrule/LunarEventSpawnRuleType;)Lcom/mojang/serialization/MapCodec;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/spawnrule/MinNightsBetweenRule.class`

- "com/mojang/serialization/Codec"
- "Lcom/mojang/serialization/codecs/PrimitiveCodec;"
- "com/mojang/serialization/codecs/PrimitiveCodec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "CODEC"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/spawnrule/MinNightsBetweenRule;>;"

### `dev/corgitaco/enhancedcelestials2core/api/lunarevent/spawnrule/ValidMoonPhaseRule.class`

- "com/mojang/serialization/Codec"
- "(II)Lcom/mojang/serialization/Codec;"
- "(Lcom/mojang/serialization/Codec;)Lcom/mojang/serialization/Codec;"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/MapCodec;"
- "CODEC"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/MapCodec<Ldev/corgitaco/enhancedcelestials2core/api/lunarevent/spawnrule/ValidMoonPhaseRule;>;"

### `dev/corgitaco/enhancedcelestials2core/client/screen/TranslationConfigScreen.class`

- "Translation_Mode"
- "Prompt_Language_When_Translation_Incomplete"
- "override_existing_translations"
- "enhancedcelestials2core.translation_config.override_existing"
- "enhancedcelestials2core.translation_config.override_existing.tooltip"

### `dev/corgitaco/enhancedcelestials2core/lunarevent/LunarEventInstance.class`

- "net/minecraft/resources/RegistryFixedCodec"
- "(Lnet/minecraft/resources/ResourceKey;)Lnet/minecraft/resources/RegistryFixedCodec;"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/codecs/RecordCodecBuilder;"
- "com/mojang/serialization/Codec"
- "Lcom/mojang/serialization/codecs/PrimitiveCodec;"
- "com/mojang/serialization/codecs/PrimitiveCodec"
- "(Ljava/lang/String;Ljava/lang/Object;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/codecs/RecordCodecBuilder$Instance"
- "com/mojang/serialization/codecs/RecordCodecBuilder"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/Codec;"
- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "Lcom/mojang/serialization/Codec<Ldev/corgitaco/enhancedcelestials2core/lunarevent/LunarEventInstance;>;"
- "(Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;)Lcom/mojang/datafixers/kinds/App;"
- "Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;"

### `dev/corgitaco/enhancedcelestials2core/neoforge/ECModBusEventsHandler.class`

- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "(Lnet/minecraft/resources/ResourceKey;Lcom/mojang/serialization/Codec;Lcom/mojang/serialization/Codec;)V"
- "DIRECT_CODEC"

### `dev/corgitaco/enhancedcelestials2core/neoforge/datagen/ECDataGen.class`

- "addCodec"
- "(Lnet/minecraft/resources/ResourceKey;Lcom/mojang/serialization/Codec;)Lnet/minecraft/core/Cloner$Factory;"
- "(Lnet/minecraft/resources/ResourceKey;Lcom/mojang/serialization/Codec;)V"

### `dev/corgitaco/enhancedcelestials2core/neoforge/platform/NeoForgeRegistrationService.class`

- "com/mojang/serialization/Codec"
- "(Lnet/minecraft/resources/ResourceKey;Lcom/mojang/serialization/Codec;)V"
- "codec"
- "Ljava/util/function/Supplier<Lcom/mojang/serialization/Codec<TT;>;>;"
- "<T:Ljava/lang/Object;>(Lnet/minecraft/resources/ResourceKey<Lnet/minecraft/core/Registry<TT;>;>;Ljava/util/function/Supplier<Lcom/mojang/serialization/Codec<TT;>;>;)V"

### `dev/corgitaco/enhancedcelestials2core/platform/services/RegistrationService.class`

- "<T:Ljava/lang/Object;>(Lnet/minecraft/resources/ResourceKey<Lnet/minecraft/core/Registry<TT;>;>;Ljava/util/function/Supplier<Lcom/mojang/serialization/Codec<TT;>;>;)V"

### `dev/corgitaco/enhancedcelestials2core/util/CodecUtil$1.class`

- "dev/corgitaco/enhancedcelestials2core/util/CodecUtil$1"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/Codec"
- "(Lcom/mojang/serialization/Codec;Lnet/minecraft/resources/ResourceKey;Lcom/mojang/serialization/Codec;)V"
- "Ldev/corgitaco/enhancedcelestials2core/util/CodecUtil$1;"
- "Ljava/lang/Object;Lcom/mojang/serialization/Codec<Lnet/minecraft/core/Holder<TE;>;>;"
- "CodecUtil.java"
- "dev/corgitaco/enhancedcelestials2core/util/CodecUtil"
- "(Lnet/minecraft/resources/ResourceKey;Lcom/mojang/serialization/Codec;)Lcom/mojang/serialization/Codec;"

### `dev/corgitaco/enhancedcelestials2core/util/CodecUtil$LazyCodec.class`

- "dev/corgitaco/enhancedcelestials2core/util/CodecUtil$LazyCodec"
- "com/mojang/serialization/Codec"
- "(Ldev/corgitaco/enhancedcelestials2core/util/CodecUtil$LazyCodec;)Ljava/lang/String;"
- "(Ldev/corgitaco/enhancedcelestials2core/util/CodecUtil$LazyCodec;)I"
- "(Ldev/corgitaco/enhancedcelestials2core/util/CodecUtil$LazyCodec;Ljava/lang/Object;)Z"
- "Ljava/util/function/Supplier<Lcom/mojang/serialization/Codec<TTYPE;>;>;"
- "Ldev/corgitaco/enhancedcelestials2core/util/CodecUtil$LazyCodec;"
- "Ldev/corgitaco/enhancedcelestials2core/util/CodecUtil$LazyCodec<TTYPE;>;"
- "(Ljava/util/function/Supplier<Lcom/mojang/serialization/Codec<TTYPE;>;>;)V"
- "()Ljava/util/function/Supplier<Lcom/mojang/serialization/Codec<TTYPE;>;>;"
- "<TYPE:Ljava/lang/Object;>Ljava/lang/Record;Lcom/mojang/serialization/Codec<TTYPE;>;"
- "CodecUtil.java"
- "dev/corgitaco/enhancedcelestials2core/util/CodecUtil"
- "LazyCodec"

### `dev/corgitaco/enhancedcelestials2core/util/CodecUtil.class`

- "net/minecraft/resources/RegistryFileCodec"
- "(Lnet/minecraft/resources/ResourceKey;Lcom/mojang/serialization/Codec;)Lnet/minecraft/resources/RegistryFileCodec;"
- "com/mojang/serialization/Codec"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/Codec;"
- "dev/corgitaco/enhancedcelestials2core/util/CodecUtil$1"
- "(Lcom/mojang/serialization/Codec;Lnet/minecraft/resources/ResourceKey;Lcom/mojang/serialization/Codec;)V"
- "CODEC"
- "Lcom/mojang/serialization/Codec;"
- "dev/corgitaco/enhancedcelestials2core/util/CodecUtil"
- "CLICK_EVENT_ACTION_CODEC"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/codecs/RecordCodecBuilder;"
- "Lcom/mojang/serialization/codecs/PrimitiveCodec;"
- "com/mojang/serialization/codecs/PrimitiveCodec"
- "com/mojang/serialization/codecs/RecordCodecBuilder$Instance"
- "createLoggedExceptionRegistryCodec"
- "(Lnet/minecraft/core/Registry;)Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/codecs/RecordCodecBuilder"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/Codec;"
- "CLICK_EVENT_CODEC"
- "STYLE_CODEC"
- "Lcom/mojang/serialization/Codec<Lnet/minecraft/world/effect/MobEffect;>;"
- "Lcom/mojang/serialization/Codec<Lnet/minecraft/world/entity/EntityType<*>;>;"
- "Lcom/mojang/serialization/Codec<Lnet/minecraft/network/chat/ClickEvent$Action;>;"
- "Lcom/mojang/serialization/Codec<Lnet/minecraft/network/chat/ClickEvent;>;"
- "Lcom/mojang/serialization/Codec<Lnet/minecraft/network/chat/Style;>;"
- "Ldev/corgitaco/enhancedcelestials2core/util/CodecUtil;"
- "(Lnet/minecraft/resources/ResourceKey;Lcom/mojang/serialization/Codec;)Lcom/mojang/serialization/Codec;"
- "elementCodec"
- "Lcom/mojang/serialization/Codec<TE;>;"
- "Lcom/mojang/serialization/Codec<Lnet/minecraft/core/Holder<TE;>;>;"
- "<E:Ljava/lang/Object;>(Lnet/minecraft/resources/ResourceKey<+Lnet/minecraft/core/Registry<TE;>;>;Lcom/mojang/serialization/Codec<TE;>;)Lcom/mojang/serialization/Codec<Lnet/minecraft/core/Holder<TE;>;>;"
- "<T:Ljava/lang/Object;>(Lnet/minecraft/core/Registry<TT;>;)Lcom/mojang/serialization/Codec<TT;>;"
- "lambda$createLoggedExceptionRegistryCodec$3"
- "lambda$createLoggedExceptionRegistryCodec$2"
- "(Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;)Lcom/mojang/datafixers/kinds/App;"
- "Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;"
- "CodecUtil.java"
- "dev/corgitaco/enhancedcelestials2core/util/CodecUtil$LazyCodec"
- "LazyCodec"

### `dev/corgitaco/enhancedcelestials2core/util/ColorUtil.class`

- "com/mojang/serialization/Codec"
- "(II)Lcom/mojang/serialization/Codec;"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/codecs/RecordCodecBuilder;"
- "com/mojang/serialization/codecs/RecordCodecBuilder$Instance"
- "Lcom/mojang/serialization/codecs/PrimitiveCodec;"
- "com/mojang/serialization/codecs/PrimitiveCodec"
- "(Ljava/util/function/Function;Ljava/util/function/Function;)Lcom/mojang/serialization/Codec;"
- "NAMED_OR_HEX_CODEC"
- "Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/codecs/RecordCodecBuilder"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/Codec;"
- "RGB_CODEC"
- "(Lcom/mojang/serialization/Codec;Lcom/mojang/serialization/Codec;)Lcom/mojang/serialization/Codec;"
- "FLEXIBLE_COLOR_CODEC"
- "COLOR_CODEC"
- "Lcom/mojang/serialization/MapCodec;"
- "Lcom/mojang/serialization/Codec<Ljava/lang/Integer;>;"
- "Lcom/mojang/serialization/MapCodec<Ljava/lang/Integer;>;"
- "(Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;)Lcom/mojang/datafixers/kinds/App;"
- "Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;"

### `dev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent.class`

- "com/mojang/serialization/Codec"
- "Lcom/mojang/serialization/codecs/PrimitiveCodec;"
- "com/mojang/serialization/codecs/PrimitiveCodec"
- "(Ljava/lang/String;)Lcom/mojang/serialization/MapCodec;"
- "com/mojang/serialization/MapCodec"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/codecs/RecordCodecBuilder;"
- "dev/corgitaco/enhancedcelestials2core/util/CodecUtil"
- "STYLE_CODEC"
- "Lcom/mojang/serialization/Codec;"
- "(Ljava/lang/String;Ljava/lang/Object;)Lcom/mojang/serialization/MapCodec;"
- "dev/corgitaco/enhancedcelestials2core/util/CodecUtil$LazyCodec"
- "()Lcom/mojang/serialization/Codec;"
- "com/mojang/serialization/codecs/RecordCodecBuilder$Instance"
- "CODEC"
- "com/mojang/serialization/codecs/RecordCodecBuilder"
- "(Ljava/util/function/Function;)Lcom/mojang/serialization/Codec;"
- "Lcom/mojang/serialization/Codec<Ldev/corgitaco/enhancedcelestials2core/util/CustomTranslationTextComponent;>;"
- "(Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;)Lcom/mojang/datafixers/kinds/App;"
- "Lcom/mojang/serialization/codecs/RecordCodecBuilder$Instance;"
- "LazyCodec"

### `dev/corgitaco/enhancedcelestials2core/util/Translations$Cache.class`

- "com/google/gson/JsonParser"
- "(Ljava/lang/String;)Lcom/google/gson/JsonElement;"
- "com/google/gson/JsonElement"
- "getAsJsonObject"
- "()Lcom/google/gson/JsonObject;"
- "com/google/gson/JsonObject"
- "(Ljava/lang/String;)Lcom/google/gson/JsonObject;"
- "(Ljava/lang/String;Lcom/google/gson/JsonElement;)V"
- "(Ljava/lang/String;Ljava/lang/String;)Lcom/google/gson/JsonObject;"
- "Lcom/google/gson/JsonObject;"
- "(Ljava/lang/String;Ljava/lang/String;Lcom/google/gson/JsonObject;)V"

### `dev/corgitaco/enhancedcelestials2core/util/Translations$Config$TranslationMode.class`

- "AUTOMATIC"
- "MANUAL"
- "DISABLED"

### `dev/corgitaco/enhancedcelestials2core/util/Translations$Config.class`

- "AUTOMATIC"
- "Translation_Mode"
- "Prompt_Language_When_Translation_Incomplete"
- "override_existing_translations"
- "GSON"
- "Lcom/google/gson/Gson;"
- "com/google/gson/Gson"
- "fromJson"
- "toJson"
- "./config/enhancedcelestials2core/translations.json"
- "com/google/gson/GsonBuilder"
- "()Lcom/google/gson/GsonBuilder;"
- "()Lcom/google/gson/Gson;"

### `dev/corgitaco/enhancedcelestials2core/util/Translations$Contribution.class`

- "GSON"
- "Lcom/google/gson/Gson;"
- "com/google/gson/Gson"
- "toJson"
- "fromJson"
- "com/google/gson/GsonBuilder"
- "()Lcom/google/gson/GsonBuilder;"
- "()Lcom/google/gson/Gson;"

### `dev/corgitaco/enhancedcelestials2core/util/Translations.class`

- "com/google/gson/JsonObject"
- "com/google/gson/JsonElement"
- "getAsString"
- "(Ljava/lang/String;Lcom/google/gson/JsonElement;)V"
- "Prompt_Language_When_Translation_Incomplete"
- "Translation_Mode"
- "AUTOMATIC"
- "override_existing_translations"
- "(Ljava/lang/String;Ljava/lang/String;Lcom/google/gson/JsonObject;)V"
- "(Lcom/google/gson/JsonObject;Ljava/util/Map;)Lcom/google/gson/JsonObject;"
- "com/google/gson/JsonParser"
- "(Ljava/lang/String;)Lcom/google/gson/JsonElement;"
- "getAsJsonObject"
- "()Lcom/google/gson/JsonObject;"
- "(Ljava/lang/String;Ljava/lang/String;)Lcom/google/gson/JsonObject;"
- "(Ljava/lang/String;Ljava/lang/String;Ljava/util/Map<Ljava/lang/String;Ljava/lang/String;>;)Ljava/util/concurrent/CompletableFuture<Lcom/google/gson/JsonObject;>;"
- "Lcom/google/gson/JsonObject;"
- "Ljava/util/Map$Entry<Ljava/lang/String;Lcom/google/gson/JsonElement;>;"
- "(Lcom/google/gson/JsonObject;Ljava/util/Map<Ljava/lang/String;Ljava/lang/String;>;)Lcom/google/gson/JsonObject;"
- "(Ljava/lang/String;Ljava/util/Set;Ldev/corgitaco/enhancedcelestials2core/util/Translations$Config;Lcom/google/gson/JsonObject;)V"
- "(Ljava/lang/String;Ljava/lang/String;Ljava/util/Map;Lcom/google/gson/JsonObject;)Ljava/util/concurrent/CompletionStage;"
- "(Ljava/lang/String;Ljava/lang/String;Lcom/google/gson/JsonObject;)Lcom/google/gson/JsonObject;"
- "(Ljava/util/Map;Lcom/google/gson/JsonObject;)Lcom/google/gson/JsonObject;"
- "(Ljava/lang/String;)Lcom/google/gson/JsonObject;"
- "(Lcom/google/gson/JsonObject;)Ljava/util/concurrent/CompletionStage;"
- "(Lcom/google/gson/JsonObject;)V"
- "(Lcom/google/gson/JsonObject;)Lcom/google/gson/JsonObject;"
