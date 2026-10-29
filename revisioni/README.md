# Revisioni

Il lavoro sul **repository** che non è una versione del pack: struttura e regole dei documenti, script e workflow, ambiente degli agenti. Una revisione ha un inizio e una fine: la valutazione, le decisioni di Matteo, le modifiche che le applicano. Riguarda tutte le versioni di Minecraft, per questo sta nella radice. Regole generali in [`AGENTS.md`](../AGENTS.md), sezione 4.

**Revisione o versione?** Ciò che cambia il gioco (mod, config, datapack, generatori e le loro regole) va sempre in una versione del pack (`<versione>/lavoro/versioni/vX.Y.Z.md`), anche quando nasce da una revisione. Una revisione cambia solo ciò che non finisce nel gioco.

## Come è fatta una revisione

Una cartella `AAAA.MM-NN/`: anno e mese, più un numero che ricomincia da 01 ogni mese. L'argomento sta nel titolo dei file e nell'elenco qui sotto. Dentro, sempre due file:

| File | Contiene | Quando si aggiorna |
|---|---|---|
| `piano.md` | obiettivo, decisioni (una riga datata ciascuna), lavoro da spuntare, prove, punti aperti, esito | quando si completa un passo e quando il piano cambia |
| `diario.md` | il racconto in ordine di tempo: cosa è stato fatto, i controlli, le deviazioni dal piano, le decisioni nuove; ogni voce dice agente e modello (`claude-code (claude-opus-5-5)`) | a ogni passo concluso e ogni volta che si cambia idea |

## Le regole

- **Il piano si può cambiare, mai in silenzio**: ogni modifica ha una voce nel diario con il motivo. Una decisione cambiata è una riga nuova, come nei file delle versioni.
- **Alla chiusura** le regole nuove vanno in `AGENTS.md`, le procedure in [`docs/0201-sviluppo.md`](../docs/0201-sviluppo.md); il piano riceve l'**Esito** e la cartella resta come storico. Le revisioni non si cancellano.
- **Quando va su `main`**: come i documenti e i workflow (`AGENTS.md`, sezione 5), con un merge vero, solo se su `dev` non c'è una tappa in corso; altrimenti aspetta la versione.
- I punti aperti non bloccanti restano nel piano, sezione «Aperto»: si guardano prima di proporre lavoro nuovo.

## Elenco

| Revisione | Argomento | Stato |
|---|---|---|
| [2026.10-01](2026.10-01/piano.md) | lavoro in locale con Claude Code: sessione, permessi e sandbox, contesto locale, stage fuori da git, revisioni, autonomia dell'agente | 🔧 aperta il 29/10/2026 |
