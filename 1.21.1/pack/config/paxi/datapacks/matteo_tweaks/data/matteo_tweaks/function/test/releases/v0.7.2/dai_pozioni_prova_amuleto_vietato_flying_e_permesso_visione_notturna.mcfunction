# Prova di uscita della 0.7.2: la lista nera degli amuleti di Apotheosis funziona. Passi 6-7 della checklist (lavoro/versioni/v0.7.2.md, sezione 5).
tellraw @s {"text":"── Prova amuleti (0.7.2) ──","color":"gold","bold":true}
give @s minecraft:blaze_powder 12
give @s minecraft:potion[potion_contents={potion:"apothic_attributes:flying"}] 3
give @s minecraft:potion[potion_contents={potion:"minecraft:night_vision"}] 3
tellraw @s {"text":"Banco da lavoro: 3 polveri di blaze in alto, 3 pozioni uguali in mezzo, 3 polveri in basso.","color":"yellow"}
tellraw @s {"text":"Con Flying (in lista nera): nessun risultato. Con Visione notturna: esce l'amuleto.","color":"yellow"}
