"""Print registration + key growth/soil logic for given block names in a mod repo.
Usage: python3 -I javainfo.py REPO name1 name2 ...
"""
import os, re, sys

repo = sys.argv[1]
names = sys.argv[2:]
java = {}
for root, dirs, files in os.walk(repo):
    dirs[:] = [d for d in dirs if d not in (".git", "build")]
    for f in files:
        if f.endswith(".java") or f.endswith(".kt"):
            p = os.path.join(root, f)
            try:
                java[p] = open(p, encoding="utf-8", errors="replace").read()
            except Exception:
                pass
by_class = {}
for p, src in java.items():
    for m in re.finditer(r"\b(?:class|record)\s+(\w+)", src):
        by_class.setdefault(m.group(1), p)

KEY = re.compile(r"(mayPlaceOn|canSurvive|getBaseSeedId|getSeed|popResource|AGE\s*=|IntegerProperty|BlockTags\.|is\(Blocks\.|is\(BlockTags|extends\s+\w+|getMaxAge|FluidState|Fluids\.|isFaceSturdy|getRawBrightness|dropResources|getLootTable|LootTable|Items\.|ModItems\.|\w+Items\.\w+|placeOn|PLACE_ON|TagKey|canPlaceOn|getPlant|isValidBonemealTarget)")
shown = set()
for name in names:
    print(f"======== {name}")
    pat = re.compile(r'["\']' + re.escape(name) + r'["\']')
    regs = []
    for p, src in java.items():
        for i, line in enumerate(src.splitlines()):
            if pat.search(line):
                regs.append((p, i, line.strip()))
    for p, i, line in regs[:4]:
        lines = java[p].splitlines()
        ctx = " ".join(l.strip() for l in lines[i:i + 3])
        print(f"  REG {os.path.relpath(p, repo)}:{i+1}: {ctx[:330]}")
        for cm in re.finditer(r"new\s+(\w+)\s*[(<]|(\w+)::new", ctx):
            cls = cm.group(1) or cm.group(2)
            if cls in by_class and cls not in shown and not cls.endswith("Item") and cls not in ("Properties", "BlockItem"):
                shown.add(cls)
                cp = by_class[cls]
                print(f"    CLASS {cls} @ {os.path.relpath(cp, repo)}")
                for j, l in enumerate(java[cp].splitlines()):
                    if KEY.search(l) and not l.strip().startswith("import"):
                        print(f"      {j+1}: {l.strip()[:200]}")
