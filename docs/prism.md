# Collegare Prism Launcher al pack

Ogni istanza di Prism scarica il pack da questo repository a ogni avvio, tramite **packwiz-installer**. Cambiando solo l'indirizzo si sceglie quale versione del pack segue l'istanza.

## Le tre istanze tipo

| Istanza | Indirizzo da usare | Cosa succede |
|---|---|---|
| **Prova** | `https://raw.githubusercontent.com/mango-craft/mango-craft/refs/heads/main/1.21.1/pack/pack.toml` | Segue sempre l'ultimo lavoro, anche non ancora rilasciato |
| **Mondo vero** | `https://raw.githubusercontent.com/mango-craft/mango-craft/refs/tags/1.21.1-v0.1.1/1.21.1/pack/pack.toml` | Resta sulla versione indicata dal tag. Per aggiornare: backup del mondo, poi si cambia il tag nell'indirizzo |
| **Archivio** | come il mondo vero, con un tag vecchio, aggiungendo `--bootstrap-no-update` dopo il primo avvio | Congelata per sempre su quella versione |

I tag hanno la forma `1.21.1-vX.Y.Z`: la parte prima di `-v` è la versione di Minecraft, quella dopo la versione del pack. L'elenco è nella pagina [Releases](https://github.com/mango-craft/mango-craft/releases).

## Creare un'istanza

1. **Scarica il bootstrap**: `packwiz-installer-bootstrap.jar` dalle [release ufficiali](https://github.com/packwiz/packwiz-installer-bootstrap/releases). È lo stesso file per tutte le istanze.
2. **Nuova istanza** in Prism: *Aggiungi istanza* → versione di Minecraft **1.21.1** → loader **NeoForge**, versione **21.1.259** (quella indicata nel `CHANGELOG.md` della versione che vuoi usare). Dagli un nome che dica che istanza è, ad esempio "Mango Craft (prova)".
3. **Memoria**: *Modifica* → *Impostazioni* → *Java*: 8 GB di massima.
4. **Il file**: tasto destro sull'istanza → *Cartella*, entra in `minecraft` (o `.minecraft`; se non c'è, avvia una volta l'istanza vanilla o creala) e copia lì `packwiz-installer-bootstrap.jar`.
5. **Il comando**: *Modifica* → *Impostazioni* → *Comandi personalizzati* (Custom commands) → attiva → *Comando prima dell'avvio* (Pre-launch command):
   ```
   "$INST_JAVA" -jar packwiz-installer-bootstrap.jar <indirizzo dalla tabella>
   ```
6. **Avvia**: compare la finestra dell'installer, che la prima volta scarica circa 200 file. Poi parte il gioco.

## Mod di CurseForge da scaricare a mano

Alcuni autori di CurseForge non permettono il download dai launcher esterni (oggi succede con **Roaster's Delight**). L'installer allora si ferma con la finestra **Failed file downloads**:

1. Clicca il nome della mod nell'elenco: a destra compare il messaggio con la pagina e il **percorso esatto** dove salvare il file (la cartella `mods` dell'istanza).
2. Premi **Open missing mods**: si apre la pagina del file giusto su CurseForge. Premi *Download* e aspetta qualche secondo.
3. Sposta il file scaricato in quel percorso, **senza rinominarlo** (attenzione ai doppioni tipo `(1)` nel nome).
4. Torna alla finestra e premi **Continue**: l'installer ricontrolla, trova il file e prosegue.

Se premi *Continue* senza aver messo il file, la finestra ricompare. Succede una volta per istanza, e di nuovo solo se quella mod cambia versione.

## Da sapere

- **NeoForge va impostato a mano**: l'installer non riesce a cambiarlo. Se una nuova versione del pack richiede un NeoForge diverso (lo dice il `CHANGELOG.md`), annulla l'avvio, cambialo nella scheda *Versione* dell'istanza e riavvia.
- **Non gestire le mod dalla scheda *Mod* di Prism** in queste istanze: una mod disattivata lì viene riscaricata al prossimo avvio. Ogni modifica passa dal repository.
- **Le tue modifiche alle config restano** finché il pack non porta una versione nuova di quel file. I file aggiunti da te (salvataggi, screenshot, resource pack tuoi) non vengono mai toccati.
- **Dopo un aggiornamento del repository** aspetta qualche minuto prima di avviare: GitHub tiene i file in cache per circa 5 minuti, e nel frattempo l'installer può dare un errore sull'hash dell'indice. Riprovando dopo un po' passa.
- **Senza internet** l'installer propone di continuare senza aggiornare.
- **Fresh Animations** viene scaricato ma va attivato a mano: *Opzioni* → *Pacchetti di risorse*.
