# Prova di uscita della 0.7.4: il bottino delle creature con Saccheggio, cambiato in NeoForge 21.1.263-265 (lavoro/versioni/v0.7.4.md, sezione 5).
tellraw @s {"text":"── Prova Saccheggio (0.7.4) ──","color":"gold","bold":true}
give @s minecraft:netherite_sword[enchantments={levels:{"minecraft:looting":3}}]
give @s minecraft:cow_spawn_egg 5
tellraw @s {"text":"Fai comparire le mucche e uccidile con la spada (Saccheggio III): cadono carne e cuoio, spesso più di 3 pezzi. Nessun errore in chat.","color":"yellow"}
