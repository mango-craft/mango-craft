# Accessories: niente artefatti nei suoi slot (dalla 0.7.0)

Fino alla 0.6.3 la config di Artifacts (`enableAccessoriesCompat = false`) teneva gli artefatti solo negli slot di **Curios**. Con **Reliquified Artifacts** la config di Artifacts non viene più letta, e il jar di Artifacts mette i suoi slot nelle etichette di Accessories (`accessories:belt`, `hand`, `hat`, `necklace`, `shoes`): gli artefatti finirebbero anche nel menu di Accessories.

I file in [`tags/item/`](tags/item/) **tolgono** dalle etichette di Accessories le etichette degli slot di Artifacts, con il campo `remove` di NeoForge (`"required": false`: senza Artifacts non danno errore). È la stessa correzione di All The Mods 10 (`kubejs/server_scripts/Tweaks/tags.js`).

| Etichetta di Accessories | Etichette di Artifacts tolte |
|---|---|
| `accessories:belt` | `#artifacts:slot/belt` |
| `accessories:hand` | `#artifacts:slot/hands` |
| `accessories:hat` | `#artifacts:slot/head`, `#artifacts:slot/face`, `#artifacts:slot/all` |
| `accessories:necklace` | `#artifacts:slot/necklace` |
| `accessories:shoes` | `#artifacts:slot/feet` |
