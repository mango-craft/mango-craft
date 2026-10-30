-- Bottino (0.7.5): le casse «radice» (non nominate da un'altra tabella) caricabili senza nessuna fonte di reliquie
-- (né Relics, né un nostro modificatore, né una voce di Artifacts), per file. Tema theme-knowledge/archeologia.md.
SELECT t.fonte,
       count(*)                                                        AS casse,
       GROUP_CONCAT(substr(t.tabella_id, instr(t.tabella_id, ':') + 1), ' ') AS tabelle
FROM BOTTINO_TABELLA_VINCENTE t
WHERE t.categoria = 'casse' AND t.caricabile AND t.dentro IS NULL
  AND NOT EXISTS (SELECT 1 FROM BOTTINO_SOTTOTABELLA s WHERE s.tabella_id = t.tabella_id)
  AND NOT EXISTS (SELECT 1 FROM BOTTINO_RELIQUIA r WHERE r.tabella_id = t.tabella_id)
GROUP BY t.fonte
ORDER BY casse DESC, t.fonte;
