-- Per ogni terreno: stato, bonus di oggi (file vincente), classe di rarità scelta e bonus che avrà,
-- numero di colture servite (tutte e solo quelle originali). Ordinata per colture servite.
SELECT t.terreno_id,
       t.stato,
       p.strato                                   AS file_di,
       COALESCE(p.crescita, 0)                    AS crescita_oggi,
       COALESCE(p.resa, 0)                        AS resa_oggi,
       r.classe,
       s.crescita                                 AS crescita_scelta,
       s.resa                                     AS resa_scelta,
       COUNT(DISTINCT k.coltura_id)               AS colture,
       COUNT(DISTINCT CASE WHEN k.da_noi = 0 THEN k.coltura_id END) AS colture_originali,
       r.motivo
FROM TERRENO t
LEFT JOIN POTS_TERRENO p ON p.terreno_id = t.terreno_id AND p.vincente = 1
LEFT JOIN TERRENO_RARITA r ON r.terreno_id = t.terreno_id
LEFT JOIN RARITA_POTS_SETTINGS s ON s.classe = r.classe
LEFT JOIN POTS_COMPATIBILITA k ON k.terreno_id = t.terreno_id
GROUP BY t.terreno_id
ORDER BY colture DESC, t.terreno_id;
