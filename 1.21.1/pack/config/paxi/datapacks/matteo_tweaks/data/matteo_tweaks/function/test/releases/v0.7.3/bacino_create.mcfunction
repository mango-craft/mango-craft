# Prova di uscita della 0.7.3: Advanced Peripherals legge i serbatoi di un bacino di Create (lavoro/versioni/v0.7.3.md, sezione 5).
tellraw @s {"text":"── Prova bacino di Create (0.7.3) ──","color":"gold","bold":true}
give @s computercraft:computer_advanced
give @s create:basin
give @s minecraft:water_bucket
tellraw @s {"text":"Metti il computer e il bacino attaccato a un lato; versa l'acqua nel bacino (clic destro con il secchio). Nel computer scrivi «lua» e Invio, poi incolla (Ctrl+V) la riga qui sotto e Invio.","color":"yellow"}
tellraw @s {"text":"[clic per copiare] peripheral.find('basin').inputTanks()","color":"aqua","clickEvent":{"action":"copy_to_clipboard","value":"peripheral.find('basin').inputTanks()"}}
tellraw @s {"text":"Deve mostrare un elenco di serbatoi con minecraft:water dentro (anche vuoto risponde, con l'elenco). Un errore «attempt to index a nil value» vuol dire che il computer non vede il bacino.","color":"yellow"}
