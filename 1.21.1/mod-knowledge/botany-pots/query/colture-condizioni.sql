-- Per ogni coltura vincente: fonte, seme, tempo, i tag che accetta (ne basta uno) e quanti terreni la servono.
SELECT c.coltura_id,
       c.strato,
       GROUP_CONCAT(DISTINCT s.seme)                           AS semi,
       c.tempo,
       c.resa_base,
       GROUP_CONCAT(DISTINCT g.ambito || ' ' || g.nome || CASE WHEN ct.implicito THEN ' (implicito)' ELSE '' END) AS tag_ammessi,
       (SELECT COUNT(DISTINCT k.terreno_id) FROM POTS_COMPATIBILITA k WHERE k.coltura_id = c.coltura_id) AS terreni
FROM POTS_COLTURA c
JOIN POTS_COLTURA_SEME s ON s.ricetta_id = c.ricetta_id AND s.fonte = c.fonte
JOIN POTS_COLTURA_TAG ct ON ct.ricetta_id = c.ricetta_id AND ct.fonte = c.fonte
JOIN TAG g ON g.tag_id = ct.tag_id
WHERE c.vincente = 1
GROUP BY c.ricetta_id, c.fonte
ORDER BY c.coltura_id;
