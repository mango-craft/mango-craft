# Artifacts

Aggiornata il 19/10/2026 · nel pack dalla 0.1.1, versione 13.2.5 (`../docs/0403-distinta-mod.md`; ruolo e licenza in `../docs/0301-mod.md`) · fonti: sorgente (ochotonida/artifacts @7cf7dc42), inventario del pack, controllo dei nomi. Materiale grezzo: `../../ai-agents/stage/2026-10-19_1.21.1-v0.6.0_config-mod/` e `_riconteggio/`.

## Config

`config/artifacts/general.toml` (un solo file, letto con night-config dalla mod: le chiavi mancanti prendono il valore di serie): `[slots] enableAccessoriesCompat` e `enableCuriosCompat`, entrambi `true` di serie, entrambi con riavvio; `artifactRarity` 1.0. Decisione del 16/10: `enableAccessoriesCompat = false`, `enableCuriosCompat = true`, **prima di creare il mondo vero**, così Artifacts e Ars Nouveau condividono un'unica interfaccia Curios, non si possono indossare due copie dello stesso artefatto e Artifacts non passa mai per Accessories. Funziona con overlay di dati nel `pack.mcmeta` della mod (`overlay_disable_accessories` svuota le etichette degli slot di Accessories). Nel pack dalla 0.6.0 (`../lavoro/versioni/v0.6.0.md`).

Slot contesi con Ars Nouveau (testa, collana, cintura, 1 slot ciascuno): se diventano stretti si aumentano con un file di slot Curios nel datapack, formato da verificare (tema aperto, `../lavoro/0503-temi-aperti.md`).

## Artefatti nelle casse delle strutture modded (nostro datapack)

Artifacts mette i suoi oggetti solo nelle casse vanilla (si aggancia ai nomi come `minecraft:chests/abandoned_mineshaft`), e NeoForge applica i modificatori di bottino solo alla tabella "radice" scritta nella cassa. Il nostro datapack ha **15 file** in `data/matteo_tweaks/loot_modifiers/artifacts/`, uno per livello di rarità: ognuno applica una tabella di Artifacts (già bilanciata e soggetta alla sua config) a un elenco di casse modded, 153 in tutto (readme nella cartella). Copertura: 40 tabelle di When Dungeons Arise e 41 di Dungeons and Taverns (`nova_structures`), più Twilight Forest, Unusual End, il Galeone di Supplementaries e altre.

Stato al 19/10 (B01, B03; lavoro in `v0.6.0.md`):
- 15 nomi nei nostri file non esistono più: sono nomi vecchi di strutture coperte già con il nome nuovo (forte degli illager, palazzo Shiraz, templi, case e miniera dei funghi, torri dei banditi e di Thornborn); `desert_city_big` non ha più una struttura.
- Casse "tesoro" esistenti e non ancora nei file: When Dungeons Arise `kisegi_sanctuary/kisegi_sanctuary_treasure`, `mechanical_nest/mechanical_nest_treasure`, `mining_complex/mining_complex_treasure`; Dungeons and Taverns `ruin_loot_master`, `hamlet/hamlet_tresure`, `desert_ruins/desert_ruin_lesser_treasure`, `illager_hideout_lesser_tresure`, `shrine/shrine_lesser_treasure` (i nomi con "tresure" sono della mod). Le tabelle `vault` (ricompense dei blocchi "caveau") non sono casse.
- Mowzie's Mobs: `mowziesmobs:chests/monastery_chest`, `umvuthana_grove_chest`. Born in Chaos: 7 tabelle scritte con il namespace `minecraft` (`minecraft:chests/basic_chest`, `chest_level_1/2/3`, `farm_drop`, `firewell_d`, `shater`): da controllare quali usano le sue strutture.
- Inventario: 141 tabelle di casse di When Dungeons Arise, 119 di Dungeons and Taverns.
- Metodo: per ogni struttura la cassa del "tesoro", non tutte.
