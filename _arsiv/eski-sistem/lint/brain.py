#!/usr/bin/env python3
"""brain.py - deterministic build tools for a markdown second brain.
status | done <raw> <wiki...> | lint | index
Standard library only."""
import sys, re, json, hashlib, pathlib

ROOT = pathlib.Path(__file__).resolve().parent
RAW, WIKI = ROOT / "raw", ROOT / "wiki"
MANIFEST = ROOT / ".brain" / "manifest.json"
LINK = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")
QUOTE = re.compile(r'^>\s*"(.+?)"\s*[\u2014\u2013-]+\s*(raw/\S+)\s*$', re.M)

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()[:16]
def load():
    return json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
def raws(): return sorted(p for p in RAW.rglob("*") if p.is_file())
def pages(): return sorted(WIKI.rglob("*.md"))
def rel(p): return str(p.relative_to(ROOT))

def status():
    m, todo = load(), []
    for p in raws():
        k = rel(p)
        if k not in m: todo.append(("NEW", k))
        elif m[k]["sha"] != sha(p): todo.append(("CHANGED", k))
    for k in m:
        if not (ROOT / k).exists(): todo.append(("DELETED", k))
    for s, k in todo: print(s, k)
    print(f"pending: {len(todo)}", file=sys.stderr)
    return 0

def done(raw, wiki):
    p = ROOT / raw
    if not p.exists(): print("no such raw file:", raw); return 1
    for w in wiki:
        if not (ROOT / w).exists(): print("no such page:", w); return 1
    m = load(); m[raw] = {"sha": sha(p), "pages": wiki}
    MANIFEST.write_text(json.dumps(m, indent=2, sort_keys=True)); return 0

def frontmatter(text):
    if not text.startswith("---\n"): return None
    end = text.find("\n---", 4)
    if end < 0: return None
    fm = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            a, b = line.split(":", 1); fm[a.strip()] = b.strip()
    return fm

def lint():
    errs, names, text = [], {}, {}
    for p in pages():
        names[p.stem] = p; text[p] = p.read_text()
    inbound = {n: 0 for n in names}
    m = load()
    for p, t in text.items():
        fm = frontmatter(t)
        if p.name in ("index.md", "hot.md", "log.md"): continue
        if fm is None: errs.append(f"{rel(p)}: missing frontmatter"); continue
        for need in ("title", "sources", "updated"):
            if need not in fm: errs.append(f"{rel(p)}: frontmatter lacks '{need}'")
        for src in re.findall(r"raw/[^\s,\]\[]+", fm.get("sources", "")):
            if not (ROOT / src).exists(): errs.append(f"{rel(p)}: source {src} does not exist")
        for l in LINK.findall(t):
            if l in names:
                if names[l] != p: inbound[l] += 1
            else: errs.append(f"{rel(p)}: broken link [[{l}]]")
        for q, src in QUOTE.findall(t):
            f = ROOT / src
            if not f.exists(): errs.append(f"{rel(p)}: quote cites missing {src}")
            elif " ".join(q.split()) not in " ".join(f.read_text().split()):
                errs.append(f"{rel(p)}: QUOTE NOT IN SOURCE -> \"{q[:50]}\" ({src})")
        if "TODO" in t: errs.append(f"{rel(p)}: unresolved TODO")
    for n, c in inbound.items():
        if c == 0 and n not in ("index", "hot", "log"): errs.append(f"{rel(names[n])}: orphan (no inbound links)")
    for k, v in m.items():
        if (ROOT / k).exists() and sha(ROOT / k) != v["sha"]:
            errs.append(f"{k}: changed since ingest, pages stale: {', '.join(v['pages'])}")
    for e in errs: print(e, file=sys.stderr)
    print(f"lint: {len(errs)} problem(s) in {len(text)} pages", file=sys.stderr)
    return 2 if errs else 0

def index():
    rows = []
    for p in pages():
        if p.name in ("index.md", "hot.md", "log.md"): continue
        fm = frontmatter(p.read_text()) or {}
        rows.append(f"- [[{p.stem}]] - {fm.get('title', p.stem)} ({fm.get('updated', '?')})")
    (WIKI / "index.md").write_text("# Index\n\n" + "\n".join(rows) + "\n")
    print(f"index: {len(rows)} pages"); return 0

if __name__ == "__main__":
    c, a = (sys.argv[1] if len(sys.argv) > 1 else ""), sys.argv[2:]
    sys.exit({"status": lambda: status(), "lint": lambda: lint(), "index": lambda: index(),
              "done": lambda: done(a[0], a[1:])}.get(c, lambda: print(__doc__) or 1)())
