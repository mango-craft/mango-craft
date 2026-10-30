#!/usr/bin/env python3
"""Scansione dei jar per l'archeologia (24/10/2026). Uso: python3 scavi-scansione.py <cartella mods>
Scrive arch.json accanto allo script e stampa un riassunto per jar (vedi scavi-risultati.md)."""
import zipfile, glob, gzip, re, json, os, sys, io
mods = sys.argv[1]
out = {}
for p in sorted(glob.glob(os.path.join(mods, "*.jar"))):
    try:
        z = zipfile.ZipFile(p)
    except Exception:
        continue
    r = {"overrides": [], "json_refs": [], "nbt_refs": [], "class_hits": {}}
    def scan_zip(z, prefix=""):
        for n in z.namelist():
            if n.endswith(".jar"):
                try:
                    scan_zip(zipfile.ZipFile(io.BytesIO(z.read(n))), prefix + n + "!/")
                except Exception:
                    pass
                continue
            if re.match(r"data/minecraft/loot_tables?/archaeology/", n):
                r["overrides"].append(prefix + n)
            if n.endswith(".json") and n.startswith("data/"):
                b = z.read(n)
                if b"archaeology/" in b or b"suspicious_sand" in b or b"suspicious_gravel" in b:
                    r["json_refs"].append(prefix + n)
            elif n.endswith(".nbt") and n.startswith("data/"):
                try:
                    b = gzip.decompress(z.read(n))
                except Exception:
                    b = z.read(n)
                if b"archaeology/" in b:
                    m = sorted(set(re.findall(rb"[a-z0-9_.-]+:archaeology/[a-z0-9_/]+", b)))
                    r["nbt_refs"].append((prefix + n, [x.decode() for x in m][:5]))
            elif n.endswith(".class"):
                b = z.read(n)
                hits = [k.decode() for k in (b"archaeology/", b"BrushableBlockEntity", b"LootTableLoadEvent", b"MODIFY_LOOT_TABLE",
                        b"LootTableEvents", b"LootEvent", b"suspicious_sand", b"SUSPICIOUS_SAND", b"_ARCHAEOLOGY") if k in b]
                if hits:
                    r["class_hits"][prefix + n] = hits
    scan_zip(z)
    if any(r.values()):
        out[os.path.basename(p)] = r
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "arch.json"), "w"), indent=1)
for k, v in out.items():
    keys = sorted({h for hs in v["class_hits"].values() for h in hs})
    print(f"{k}: override={len(v['overrides'])} json={len(v['json_refs'])} nbt={len(v['nbt_refs'])} classi={len(v['class_hits'])} {keys}")
