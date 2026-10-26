# Funzioni di prova (dalla 0.7.2)

Comandi del gioco messi in fila, per non doverli incollare uno a uno durante le prove di uscita. Richiesta di Matteo del 25/10/2026.

## Come si usano

In gioco (mondo con i trucchi attivi): `/function matteo_tweaks:test/releases/v0.7.2/` e **Tab** per scegliere la funzione. Ogni funzione dà gli oggetti della prova e scrive in chat cosa controllare. Dopo aver cambiato un file: `/reload`.

## Regole

- **Percorso**: `test/releases/v<versione>/`, una cartella per release, con le prove di tutte le versioni che escono in quella release (la 0.7.2 contiene anche le fornaci della 0.7.1).
- **Nome del file**: corto, ma dice cosa c'è dentro (quali mod, quali pozioni): `fornaci_iron_mk2_jumbo`, `amuleto_flying_vs_visione`, `lista_nera_5_pozioni`; `tutte_le_prove` chiama tutte le altre della cartella. I dettagli li dicono la riga di commento in testa e la chat quando la lanci.
- Una riga di commento in testa rimanda alla sezione 5 del file della versione (`lavoro/versioni/vX.Y.Z.md`), dove stanno le prove.
- **Senza condizione di caricamento**, eccezione voluta alla regola del datapack: le funzioni non ne hanno. Se un nome non esiste (mod tolta o aggiornata), quella funzione non si carica e lascia un errore nel log; il resto del datapack non cambia. Per questo `scripts/check_ids.py` controlla oggetti, pozioni e funzioni chiamate in ogni `.mcfunction`.
- Le funzioni delle release vecchie restano come storia; si tolgono solo se danno errori dopo un aggiornamento.
