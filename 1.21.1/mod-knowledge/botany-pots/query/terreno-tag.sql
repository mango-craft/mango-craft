-- Per ogni terreno, i tag in cui sta: il tag raggiunto, quello il cui file lo elenca davvero (origine),
-- il livello (0 = elencato direttamente) e se l'appartenenza esiste solo grazie al nostro datapack.
SELECT tt.terreno_id,
       g.ambito,
       g.nome                 AS tag,
       d.nome                 AS tag_diretto,
       tt.livello,
       tt.da_noi
FROM TERRENO_TAG tt
JOIN TAG g ON g.tag_id = tt.tag_id
JOIN TAG d ON d.tag_id = tt.tag_diretto_id
ORDER BY tt.terreno_id, g.ambito, g.nome, tt.livello;
