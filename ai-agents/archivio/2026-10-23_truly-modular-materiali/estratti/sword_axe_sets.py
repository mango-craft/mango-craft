import json, glob, os, re
base = '/home/claude/mango-craft/1.21.1/data/inventario/mods/'
for f in sorted(glob.glob(base + '*.json')):
    d = json.load(open(f))
    items = d.get('items') or {}
    swords = {k[:-6] for k in items if k.endswith('_sword')}
    axes = {k[:-4] for k in items if k.endswith('_axe') and not k.endswith('pickaxe')}
    both = sorted(swords & axes)
    if both:
        print(os.path.basename(f), both)
