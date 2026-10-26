# Apotheosis: lista nera degli amuleti di pozione (dalla 0.7.2)

Gli **amuleti di pozione** di Apotheosis si fanno con 3 pozioni uguali e 6 polveri di blaze e danno l'effetto finché sono accesi nell'inventario: 192 usi, poi si rompono; con l'infusione di Apothic Enchanting (eterna 100) diventano **infrangibili**, cioè l'effetto è permanente. Apotheosis accetta qualsiasi pozione con **un solo effetto, non istantaneo**, che non sia nell'etichetta `apotheosis:potion_charm_blacklist` (vuota nella mod). Fatti e fonti: tema `theme-knowledge/pozioni.md`.

## Come

[`tags/potion/potion_charm_blacklist.json`](tags/potion/potion_charm_blacklist.json) aggiunge all'etichetta della mod (niente `replace`) le pozioni che **non** devono diventare amuleti, ognuna con `"required": false`: se una mod sparisce, la sua voce si ignora senza errori.

**Il file è generato**: lo scrive `scripts/pozioni_genera.py` dalla regola in `1.21.1/data/pozioni/pozione_custom.csv`, passando dalla base dati (tabelle `POZIONE`, `POZIONE_CUSTOM`, vista `POZIONE_LISTA_NERA`). **Non si modifica a mano**: si cambia il CSV e si rilancia lo script; il controllo di ogni workflow (`--verifica`) si ferma se file e regola non coincidono.

- Una riga del CSV con `varianti = tutte` vale per tutta la famiglia (normale, lunga, forte: `flying`, `long_flying`, `extra_long_flying`); con `questa` solo per quella pozione.
- I nomi di alcune pozioni (Ars Nouveau, Ars Elemental) sono **dedotti** dalla traduzione, perché nel codice sono costruiti a pezzi: lo script li segnala, e vanno confermati in gioco (suggerimenti del comando `/give @s minecraft:potion[potion_contents={potion:"ars_nouveau:`).
- L'etichetta si ricarica con `/reload`.
