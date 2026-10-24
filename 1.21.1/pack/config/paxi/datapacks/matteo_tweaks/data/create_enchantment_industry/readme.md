# Create: Enchantment Industry (0.6.3)

`data_maps/fluid/unit/experience.json` aggiunge alla tabella delle unità di Create: Enchantment Industry il cognitium di Cognition, a **20 mB per punto**: così l'Experience Hatch e le parti di Create che leggono la tabella capiscono il liquido dell'Obelisco. L'incantatore no: accetta solo il liquido di Create, che si ottiene con il Mescolatore (`data/matteo_tweaks/recipe/create/mixing/experience/`).

Il file **si aggiunge** a quello della mod con lo stesso percorso, non lo sostituisce: NeoForge legge le mappe di dati di tutti i pacchetti e le unisce (`DataMapLoader`, `listMatchingResourceStacks`; `replace` è falso se manca). La condizione si scrive per valore (`neoforge:conditions` + `neoforge:value`), come fa la mod nel suo file. Dettagli: `1.21.1/theme-knowledge/esperienza.md`.
