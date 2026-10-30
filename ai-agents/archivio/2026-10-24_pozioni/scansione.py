#!/usr/bin/env python3
"""Scansione di pozioni ed effetti nei .jar del pack (24/10/2026). Si lancia nella cartella `mods` dell'istanza
di prova, in sola lettura: python3 scansione.py > pozioni.json

Per ogni jar, dalla traduzione inglese (`assets/*/lang/en_us.json`):
- effects: le chiavi `effect.<ns>.<nome>` (nome dell'effetto) e le descrizioni `effect.<ns>.<nome>.desc[ription]`
  (scritte dalle mod per Just Enough Effect Descriptions e per i tooltip di Apothic Attributes);
- potions: le chiavi `item.minecraft.potion.effect.<nome>`: una pozione registrata (anche le varianti lunghe e forti).
Dal codice compilato, senza eseguirlo (si cercano solo i nomi nelle classi):
- brew_classes: le classi che nominano `RegisterBrewingRecipesEvent`, `PotionBrewing$Builder` o `addMix`, cioè le mod
  che aggiungono ricette all'alambicco. Le librerie (Bookshelf, Puzzles Lib, YUNG's API, Lithium, ModernFix) compaiono
  come falsi positivi.
Le durate, i livelli e le ricette dell'alambicco stanno nel codice: qui non ci sono (si leggono in gioco con EMI).
L'uscita completa del 24/10 (57 KB, 53 jar) non è stata copiata qui: si rigenera con questo script; il distillato
è nella scheda `1.21.1/theme-knowledge/pozioni.md`.
"""
import glob
import json
import re
import zipfile

out = {}
for p in sorted(glob.glob("*.jar")):
    try:
        z = zipfile.ZipFile(p)
    except Exception:
        continue
    names = z.namelist()
    r = {"effects": {}, "desc": {}, "potions": [], "brew_classes": []}
    for n in names:
        if n.endswith("/lang/en_us.json"):
            try:
                d = json.loads(z.read(n).decode("utf-8", "ignore"))
            except Exception:
                continue
            for k, v in d.items():
                if not isinstance(v, str):
                    continue
                m = re.match(r"^effect\.([a-z0-9_.-]+)\.([a-z0-9_/.-]+)$", k)
                if m:
                    r["effects"][m.group(1) + ":" + m.group(2)] = v
                m = re.match(r"^effect\.([a-z0-9_.-]+)\.([a-z0-9_/-]+)\.desc(ription)?$", k)
                if m:
                    r["desc"][m.group(1) + ":" + m.group(2)] = v[:200]
                m = re.match(r"^item\.minecraft\.potion\.effect\.([a-z0-9_.-]+)$", k)
                if m:
                    r["potions"].append(m.group(1))
    for n in names:
        if n.endswith(".class"):
            b = z.read(n)
            if b"RegisterBrewingRecipesEvent" in b or b"PotionBrewing$Builder" in b or b"addMix" in b:
                r["brew_classes"].append(n.split("/")[-1])
    if any(r[k] for k in ("effects", "potions", "brew_classes")):
        r["brew_classes"] = r["brew_classes"][:6]
        out[p] = r
print(json.dumps(out, ensure_ascii=False))
