# Prova di uscita della 0.7.2: i nomi delle 5 famiglie in lista nera esistono nel gioco (passo 8 della checklist).
# Se un nome fosse sbagliato, questa funzione non si carica (errore nel log all'avvio o dopo /reload) oppure dà un errore in chat.
tellraw @s {"text":"── Nomi della lista nera (0.7.2) ──","color":"gold","bold":true}
give @s minecraft:potion[potion_contents={potion:"apothic_attributes:flying"}]
give @s minecraft:potion[potion_contents={potion:"reactive:no_gravity"}]
give @s minecraft:potion[potion_contents={potion:"bountifulfares:bountifulfares.acidic"}]
give @s minecraft:potion[potion_contents={potion:"bountifulfares:bountifulfares.stupor"}]
give @s minecraft:potion[potion_contents={potion:"unusualend:serenity_potion"}]
tellraw @s {"text":"Devi avere 5 pozioni con un nome vero (Flying, Weightlessness, Acidity, Stupor, Serenity), non «Uncraftable Potion».","color":"yellow"}
