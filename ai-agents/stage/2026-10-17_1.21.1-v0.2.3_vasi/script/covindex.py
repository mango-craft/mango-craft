"""Build coverage index from Botany Pots / Botany Trees / datapack / bundled recipe JSONs.
Usage: python3 -I covindex.py OUT.json label=dir [label=dir ...]
Each dir is walked for *.json; recipes with botanypots types are indexed.
"""
import json, os, sys, re

def walk_ids(o, out):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in ("block", "item", "id", "tag") and isinstance(v, str):
                out.append((k, v))
            walk_ids(v, out)
    elif isinstance(o, list):
        for v in o:
            walk_ids(v, out)

def main():
    out_path = sys.argv[1]
    recs = []
    for arg in sys.argv[2:]:
        label, d = arg.split("=", 1)
        for root, dirs, files in os.walk(d):
            dirs[:] = [x for x in dirs if x not in (".git", "build")]
            for f in files:
                if not f.endswith(".json"):
                    continue
                p = os.path.join(root, f)
                try:
                    with open(p, encoding="utf-8") as fh:
                        j = json.load(fh)
                except Exception as e:
                    recs.append({"src": label, "path": p, "error": str(e)})
                    continue
                if not isinstance(j, dict):
                    continue
                t = j.get("type", "")
                if not isinstance(t, str) or not (t.startswith("botanypots:") or t.startswith("botany_pots") or "botany" in p.lower()):
                    continue
                ids = []
                walk_ids(j, ids)
                rec = {"src": label, "path": os.path.relpath(p, d), "type": t,
                       "block": j.get("block"), "input": j.get("input", j.get("seed")),
                       "soil": j.get("soil"), "ids": ids,
                       "conditions": j.get("bookshelf:load_conditions", j.get("conditions", j.get("neoforge:conditions")))}
                recs.append(rec)
    with open(out_path, "w") as fh:
        json.dump(recs, fh, indent=1)
    print(len(recs), "records")

main()
