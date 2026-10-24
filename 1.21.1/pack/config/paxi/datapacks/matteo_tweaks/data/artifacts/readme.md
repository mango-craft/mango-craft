# Artifacts: scavi archeologici (dalla 0.7.0)

Artifacts mette un artefatto in **1 scavo su 16** (sabbia e ghiaia sospette) di 5 tabelle vanilla: `minecraft:archaeology/desert_pyramid`, `desert_well`, `ocean_ruin_cold`, `ocean_ruin_warm`, `trail_ruins_rare`. Lo fa con 5 modificatori (`artifacts:inject/archaeology/*`) che **tolgono** l'oggetto normale e mettono l'artefatto (`"replace": true`), perché uno scavo dà un oggetto solo.

Con **Reliquified Artifacts** quel tipo di modificatore toglie l'oggetto normale e poi scarta l'artefatto (è una reliquia): lo scavo non darebbe niente. Per questo, dalla 0.7.0:

1. i 5 modificatori di Artifacts sono riscritti **allo stesso percorso** in [`loot_modifiers/inject/archaeology/`](loot_modifiers/inject/archaeology/): stesso nome, ma tipo `neoforge:add_table` verso `minecraft:empty`, cioè non fanno più niente. Restano nell'elenco di Artifacts (`global_loot_modifiers.json`), quindi i file devono esistere; hanno la condizione `mod_loaded` di Artifacts;
2. gli artefatti li mettono le **5 tabelle vanilla riscritte** in [`../minecraft/loot_table/archaeology/`](../minecraft/loot_table/archaeology/readme.md), con la stessa probabilità di prima (1/16).
