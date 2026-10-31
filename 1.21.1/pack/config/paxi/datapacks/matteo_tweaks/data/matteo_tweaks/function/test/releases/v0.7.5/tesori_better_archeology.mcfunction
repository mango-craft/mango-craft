# Prova di uscita della 0.7.5: le casse del tesoro di Better Archeology danno artefatti (lavoro/versioni/v0.7.5.md, sezione 5).
tellraw @s {"text":"── Prova tesori di Better Archeology (0.7.5) ──","color":"gold","bold":true}
# Prima fila: 10 casse del tempio della luce (40%, un artefatto qualsiasi: matteo_tweaks:artifacts/qualsiasi_40).
execute rotated ~ 0 run setblock ^-9 ^ ^3 minecraft:chest{LootTable:"betterarcheology:archeology/chest_light_temple_treasure"}
execute rotated ~ 0 run setblock ^-7 ^ ^3 minecraft:chest{LootTable:"betterarcheology:archeology/chest_light_temple_treasure"}
execute rotated ~ 0 run setblock ^-5 ^ ^3 minecraft:chest{LootTable:"betterarcheology:archeology/chest_light_temple_treasure"}
execute rotated ~ 0 run setblock ^-3 ^ ^3 minecraft:chest{LootTable:"betterarcheology:archeology/chest_light_temple_treasure"}
execute rotated ~ 0 run setblock ^-1 ^ ^3 minecraft:chest{LootTable:"betterarcheology:archeology/chest_light_temple_treasure"}
execute rotated ~ 0 run setblock ^1 ^ ^3 minecraft:chest{LootTable:"betterarcheology:archeology/chest_light_temple_treasure"}
execute rotated ~ 0 run setblock ^3 ^ ^3 minecraft:chest{LootTable:"betterarcheology:archeology/chest_light_temple_treasure"}
execute rotated ~ 0 run setblock ^5 ^ ^3 minecraft:chest{LootTable:"betterarcheology:archeology/chest_light_temple_treasure"}
execute rotated ~ 0 run setblock ^7 ^ ^3 minecraft:chest{LootTable:"betterarcheology:archeology/chest_light_temple_treasure"}
execute rotated ~ 0 run setblock ^9 ^ ^3 minecraft:chest{LootTable:"betterarcheology:archeology/chest_light_temple_treasure"}
# Seconda fila: una cassa per ciascuno degli altri 8 tesori.
execute rotated ~ 0 run setblock ^-7 ^ ^5 minecraft:chest{LootTable:"betterarcheology:archeology/chest_jungle_temple_treasure"}
execute rotated ~ 0 run setblock ^-5 ^ ^5 minecraft:chest{LootTable:"betterarcheology:archeology/chest_catacombs_golden"}
execute rotated ~ 0 run setblock ^-3 ^ ^5 minecraft:chest{LootTable:"betterarcheology:archeology/chest_sculk_sword"}
execute rotated ~ 0 run setblock ^-1 ^ ^5 minecraft:chest{LootTable:"betterarcheology:archeology/chest_mott"}
execute rotated ~ 0 run setblock ^1 ^ ^5 minecraft:chest{LootTable:"betterarcheology:archeology/chest_buried_ruins_sand"}
execute rotated ~ 0 run setblock ^3 ^ ^5 minecraft:chest{LootTable:"betterarcheology:archeology/chest_mesa_ruins"}
execute rotated ~ 0 run setblock ^5 ^ ^5 minecraft:chest{LootTable:"betterarcheology:archeology/chest_tumulus"}
execute rotated ~ 0 run setblock ^7 ^ ^5 minecraft:chest{LootTable:"betterarcheology:archeology/chest_underwater"}
tellraw @s {"text":"Davanti a te due file di casse. Prima fila: 10 tesori del tempio della luce, circa 4 su 10 hanno un artefatto, di tipi diversi (non quasi sempre il chorus totem); nessuno su 10 = la prova non va. Seconda fila: gli altri 8 tesori, con il loro bottino normale e a volte un artefatto. Nessun errore in chat.","color":"yellow"}
