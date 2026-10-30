# Installazione e istanze di Prism

Ogni istanza di Prism scarica il pack da questo repository a ogni avvio, tramite **packwiz-installer**. Cambiando solo l'indirizzo si sceglie quale versione del pack segue l'istanza. Vale per ogni versione di Minecraft del repository: negli esempi `<MC>` è la cartella della versione (oggi `1.21.1`).

## Le tre istanze tipo

| Istanza | Indirizzo da usare | Cosa succede |
|---|---|---|
| **Prova** | `https://raw.githubusercontent.com/mango-craft/mango-craft/refs/heads/dev/<MC>/pack/pack.toml` | Segue il ramo `dev`: l'ultimo lavoro, anche non ancora provato. Qui si provano le tappe prima di rilasciarle |
| **Mondo vero** | `https://raw.githubusercontent.com/mango-craft/mango-craft/refs/tags/<MC>-vX.Y.Z/<MC>/pack/pack.toml` | Resta sulla versione indicata dal tag: la prima è la 0.x con cui si crea il mondo vero (`AGENTS.md`, sezione 5). Per aggiornare: backup del mondo, poi si cambia il tag nell'indirizzo |
| **Archivio** | come il mondo vero, con un tag vecchio, aggiungendo `--bootstrap-no-update` dopo il primo avvio | Congelata per sempre su quella versione |

I tag hanno la forma `<MC>-vX.Y.Z` (es. `1.21.1-v0.3.0`): la parte prima di `-v` è la versione di Minecraft, quella dopo la versione del pack. L'elenco è nella pagina [Releases](https://github.com/mango-craft/mango-craft/releases); le 0.x sono segnate come *pre-release*.

**Scorciatoia**: se hai già un'istanza del pack, tasto destro → *Copia*, poi cambia solo l'indirizzo nel comando prima dell'avvio (passo 5). Le mod già scaricate restano e l'installer scarica solo le differenze.

## Creare un'istanza

1. **Scarica il bootstrap**: `packwiz-installer-bootstrap.jar` dalle [release ufficiali](https://github.com/packwiz/packwiz-installer-bootstrap/releases). È lo stesso file per tutte le istanze.
2. **Nuova istanza** in Prism: *Aggiungi istanza* → la versione di Minecraft e il loader con la versione indicati nel changelog della versione del pack che vuoi usare (`<MC>/docs/0401-changelog.md`; per l'ultima versione anche nel `README.md` del repository). Dagli un nome che dica che istanza è, ad esempio "Mango Craft (prova)".
3. **Memoria**: *Modifica* → *Impostazioni* → *Java* → *Memoria massima*: **12 GB** (12288 MB; il PC ha 32 GB). Con 8 GB il gioco parte, ma un ricaricamento delle risorse in gioco (F3+T, mipmap, resource pack) può finire la memoria e chiudere il gioco (bug B33 della 1.21.1, 19/10/2026). Assegnarne molta di più non aiuta e può allungare le pause del garbage collector.
4. **Il file**: tasto destro sull'istanza → *Cartella*, entra in `minecraft` (o `.minecraft`; se non c'è, avvia una volta l'istanza vanilla o creala) e copia lì `packwiz-installer-bootstrap.jar`.
5. **Il comando**: *Modifica* → *Impostazioni* → *Comandi personalizzati* (Custom commands) → attiva → *Comando prima dell'avvio* (Pre-launch command):
   ```
   "$INST_JAVA" -jar packwiz-installer-bootstrap.jar <indirizzo dalla tabella>
   ```
6. **Avvia**: compare la finestra dell'installer, che la prima volta scarica tutte le mod (per la 1.21.1 oltre 200 file). Poi parte il gioco.

## Mod di CurseForge da scaricare a mano

Alcuni autori di CurseForge non permettono il download dai launcher esterni (nella 1.21.1 succede con **Roaster's Delight**). L'installer allora si ferma con la finestra **Failed file downloads**:

1. Clicca il nome della mod nell'elenco: a destra compare il messaggio con la pagina e il **percorso esatto** dove salvare il file (la cartella `mods` dell'istanza).
2. Premi **Open missing mods**: si apre la pagina del file giusto su CurseForge. Premi *Download* e aspetta qualche secondo.
3. Sposta il file scaricato in quel percorso, **senza rinominarlo** (attenzione ai doppioni tipo `(1)` nel nome).
4. Torna alla finestra e premi **Continue**: l'installer ricontrolla, trova il file e prosegue.

Se premi *Continue* senza aver messo il file, la finestra ricompare. Succede una volta per istanza, e di nuovo solo se quella mod cambia versione.

## Da sapere

- **NeoForge va impostato a mano**: l'installer non riesce a cambiarlo. Se una nuova versione del pack richiede un NeoForge diverso (lo dice il changelog della versione), annulla l'avvio, cambialo nella scheda *Versione* dell'istanza e riavvia.
- **Non gestire le mod dalla scheda *Mod* di Prism** in queste istanze: una mod disattivata lì viene riscaricata al prossimo avvio. Ogni modifica passa dal repository.
- **Le tue modifiche alle config restano** finché il pack non porta una versione nuova di quel file. I file aggiunti da te (salvataggi, screenshot, resource pack tuoi) non vengono mai toccati.
- **Dopo un aggiornamento del repository** aspetta qualche minuto prima di avviare: GitHub tiene i file in cache per circa 5 minuti, e nel frattempo l'installer può dare un errore sull'hash dell'indice. Riprovando dopo un po' passa.
- **Senza internet** l'installer propone di continuare senza aggiornare.
- **Errore `403` su `api.github.com/repos/comp500/packwiz-installer`** all'avvio: a ogni avvio il bootstrap chiede a GitHub se esiste una versione nuova dell'installer, e GitHub concede circa 60 di queste richieste all'ora per rete. Superato il limite risponde 403. In un'istanza che ha già il file `packwiz-installer.jar` nella cartella `minecraft` non succede niente: l'avviso si chiude e si continua. In un'istanza **nuova** invece il file non c'è ancora e l'avvio fallisce (`ClassNotFoundException`). Soluzione: copiare `packwiz-installer.jar` dalla cartella `minecraft` di un'altra istanza del pack (oppure scaricarlo dalle [release dell'installer](https://github.com/packwiz/packwiz-installer/releases)), o riprovare dopo un'ora. Creando le istanze per copia il problema non si presenta.
- **Resource pack** (nella 1.21.1: Fresh Animations): vengono scaricati ma vanno attivati a mano, *Opzioni* → *Pacchetti di risorse*.
- **Shader** (facoltativi; nella 1.21.1 dalla 0.5.2): il pack scarica nella cartella `shaderpacks` dell'istanza due pacchetti (nella 1.21.1: Complementary Reimagined e MakeUp - Ultra Fast), **spenti**. Per usarne uno: in gioco, impostazioni video → sezione degli shader di Iris → scegli il pacchetto (lì si sceglie anche il profilo di qualità). Puoi aggiungerne altri nella stessa cartella (Prism ha una scheda apposita nella modifica dell'istanza): sono file tuoi, l'installer non li tocca. Con uno shader attivo il gioco è più pesante e alcuni effetti delle mod possono vedersi male (scheda `1.21.1/theme-knowledge/shader.md`).
