# Tabelle del bottino (`loot_table/`)

Qui stanno tabelle del bottino **nostre** (non i modificatori di bottino, che stanno in `../loot_modifiers/`).

## `tree_drops/bountifulfares/`: raccolti degli alberi nei vasi

Le otto tabelle dei raccolti degli alberi di Bountiful Fares nei vasi di Botany Pots, usate dalle ricette in `../recipe/botanypots/alberi/bountifulfares/`. Sono copiate da **Botany Trees** di Darkhax (`Darkhax-Minecraft/BotanyTrees`, ramo `1.21.1`, commit `eee0890`), licenza **LGPL-2.1**, senza modifiche al contenuto. Come e quando si tolgono: `../recipe/botanypots/readme.md`, sezione «Alberi di Bountiful Fares».

## `artifacts/qualsiasi_40`: un artefatto qualsiasi al 40% (dalla 0.7.5)

La tirano le 5 casse del livello «villa» della toppa degli artefatti ([`../loot_modifiers/artifacts/readme.md`](../loot_modifiers/artifacts/readme.md), sezione «Il livello della villa»): tesoro del tempio della luce di Better Archeology, caveau del labirinto e stanza dell'aurora di Twilight Forest, barili della cittadella di Friends & Foes. Una pool, con la condizione di probabilità di Artifacts (`artifacts:artifact_rarity_adjusted_chance`, `default_probability` 0.4, la stessa della sua tabella della villa), che tira l'elenco completo degli artefatti (`artifacts:artifact`). Si carica solo con Artifacts (`neoforge:conditions`).
