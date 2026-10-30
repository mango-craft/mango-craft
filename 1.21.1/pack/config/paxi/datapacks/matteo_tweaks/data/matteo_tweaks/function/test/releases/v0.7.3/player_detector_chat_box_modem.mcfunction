# Prova di uscita della 0.7.3: Player Detector e Chat Box di Advanced Peripherals, prima attaccati al computer e poi tramite modem e cavi (lavoro/versioni/v0.7.3.md, sezione 5).
tellraw @s {"text":"── Prova Player Detector e Chat Box (0.7.3) ──","color":"gold","bold":true}
give @s computercraft:computer_advanced
give @s advancedperipherals:player_detector
give @s advancedperipherals:chat_box
give @s computercraft:wired_modem 2
give @s computercraft:cable 8
tellraw @s {"text":"Metti il computer con il Player Detector e la Chat Box attaccati ai lati. Nel computer scrivi «lua» e Invio, poi incolla (Ctrl+V) la riga qui sotto e Invio.","color":"yellow"}
tellraw @s {"text":"[clic per copiare] peripheral.find('chat_box').sendMessage('Vicini: ' .. table.concat(peripheral.find('player_detector').getPlayersInRange(16), ', '))","color":"aqua","clickEvent":{"action":"copy_to_clipboard","value":"peripheral.find('chat_box').sendMessage('Vicini: ' .. table.concat(peripheral.find('player_detector').getPlayersInRange(16), ', '))"}}
tellraw @s {"text":"In chat arriva un messaggio della Chat Box con il tuo nome.","color":"yellow"}
tellraw @s {"text":"Poi sposta la Chat Box a qualche blocco: un modem sul computer e uno sulla Chat Box, uniti dai cavi; clic destro sul modem della Chat Box: in chat «Peripheral \"chat_box_0\" connected to network». Rilancia la riga (freccia su): il messaggio arriva lo stesso.","color":"yellow"}
