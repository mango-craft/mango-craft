# Colorwheel (candidata)

Aggiornata il 19/10/2026 · **non nel pack**: candidata 🟡 (`../lavoro/0601-mod-candidate.md`) · fonti: descrizione su Modrinth, mods.toml e sorgente di Colorwheel 1.3.0 (`colorwheel@8rq5KP4U`, LGPL-3.0), sorgente di Flywheel.

- Con uno shader attivo ridà a Create l'accelerazione di Flywheel (che altrimenti si spegne: scheda `iris.md`). Serve solo usando gli shader con molti macchinari.
- Funziona solo con i pacchetti che la supportano: ufficialmente Complementary Unbound/Reimagined (dalla r5.7), Euphoria Patches, Eclipse, Glimmer, I Like Vanilla, Just Colored Lighting, RenderPearl, Shrimple, Solas, Spooklementary, Steadfast; altri con Colorwheel-Patcher; con i pacchetti non supportati ha un "fallback mode" con problemi di resa. **MakeUp non la supporta.**
- Dipendenza obbligatoria solo Iris/Oculus; senza Flywheel si disattiva. Esclude "Iris & Oculus Flywheel Compat": se ne usa una sola.
- Compilata su Iris 1.8.8 e Sodium 0.6: le 78 funzioni di Iris che usa ci sono tutte nella 1.8.14, ma il funzionamento non è verificato.
