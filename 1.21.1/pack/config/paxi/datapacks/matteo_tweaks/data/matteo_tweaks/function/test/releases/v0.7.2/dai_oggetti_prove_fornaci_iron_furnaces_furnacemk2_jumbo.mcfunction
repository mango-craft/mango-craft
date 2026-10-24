# Prove di uscita della 0.7.1 (fornaci), uscita nella release 0.7.2. Passi 3-5 della checklist (lavoro/versioni/v0.7.1.md, sezione 5).
tellraw @s {"text":"── Prove fornaci (0.7.1) ──","color":"gold","bold":true}
give @s minecraft:furnace 28
give @s minecraft:raw_iron 64
give @s minecraft:coal 64
give @s ironfurnaces:upgrade_iron
give @s ironfurnaces:upgrade_gold
give @s furnacemk2:furnacemk2
give @s furnacemk2:thermal_core
give @s furnacemk2:crystal_gem_item
tellraw @s {"text":"Iron Furnaces: metti 1 fornace, falla cuocere, poi clic destro con il potenziamento di ferro (se non va, da accovacciato), poi con quello d'oro: cambia senza perdere il contenuto e cuoce più veloce.","color":"yellow"}
tellraw @s {"text":"FurnaceMk2: mettila, nucleo (Thermal Magnifier) e cristallo (Attuned Crystal) nei loro slot: cuoce e il cristallo si riempie di esperienza.","color":"yellow"}
tellraw @s {"text":"Jumbo Furnace: cubo 3×3×3 con le altre 27 fornaci: diventa una fornace gigante e cuoce.","color":"yellow"}
