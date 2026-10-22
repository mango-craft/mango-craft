-- Cosa ha cambiato il nostro datapack: per ogni terreno, colture servite senza di noi e con noi.
SELECT k.terreno_id,
       t.stato,
       COUNT(DISTINCT CASE WHEN k.da_noi = 0 THEN k.coltura_id END) AS colture_originali,
       COUNT(DISTINCT k.coltura_id)                                 AS colture_con_noi,
       COUNT(DISTINCT k.coltura_id) - COUNT(DISTINCT CASE WHEN k.da_noi = 0 THEN k.coltura_id END) AS aggiunte_da_noi
FROM POTS_COMPATIBILITA k
JOIN TERRENO t ON t.terreno_id = k.terreno_id
GROUP BY k.terreno_id
HAVING aggiunte_da_noi > 0
ORDER BY aggiunte_da_noi DESC, k.terreno_id;
