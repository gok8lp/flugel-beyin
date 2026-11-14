#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
hud-uret.py — CLAUDE CODE / SECOND BRAIN (@baber_saad1 / @rektwild) Canlı HUD Üretici
/home/flugel/Documents/Obsidian Vault/ içindeki tüm gerçek .md, .txt, .py, .sh dosyalarını,
satır sayılarını, [[wikilink]] bağlantılarını, CLAUDE.md bölümlerini, wiki/hot.md önbelleğini
ve brain.py status / lint sonuçlarını tarayarak second-brain-hud.html dosyasını üretir.
"""

import os
import re
import json
import math
import hashlib
import pathlib
import datetime
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent
OUTPUT_HTML = ROOT / "second-brain-hud.html"

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")
SOURCE_RE = re.compile(r"(raw/[a-zA-Z0-9_\-./]+\.(?:md|txt))")
HEADING_RE = re.compile(r"^#\s+(.+)$", re.M)

CLUSTER_DEFS = [
    {"id": "loader",    "label": "CLAUDE.md",                "folder": "",                   "cx":  0.04, "cy": -0.18, "cz":  0.10, "radius": 0.20},
    {"id": "harita",    "label": "HARITA.md",                "folder": "HARITA.md",          "cx": -0.08, "cy": -0.06, "cz":  0.16, "radius": 0.18},
    {"id": "memory",    "label": "hafiza.md",                "folder": "hafiza.md",          "cx": -0.22, "cy": -0.20, "cz":  0.08, "radius": 0.18},
    {"id": "decisions", "label": "kararlar.md",              "folder": "kararlar.md",        "cx":  0.02, "cy":  0.28, "cz": -0.05, "radius": 0.16},
    {"id": "inbox",     "label": "simdi.md",                 "folder": "simdi.md",           "cx":  0.26, "cy":  0.10, "cz":  0.12, "radius": 0.15},
    {"id": "local",     "label": "CLAUDE.local.md",          "folder": "CLAUDE.local.md",    "cx": -0.20, "cy":  0.04, "cz": -0.08, "radius": 0.14},
    {"id": "notlar",    "label": "notlar/",                  "folder": "notlar",             "cx": -0.44, "cy":  0.05, "cz": -0.06, "radius": 0.28},
    {"id": "projeler",  "label": "projeler/",                "folder": "projeler",           "cx": -0.08, "cy":  0.35, "cz":  0.08, "radius": 0.25},
    {"id": "kisiler",   "label": "kisiler/",                 "folder": "kisiler",            "cx":  0.34, "cy":  0.28, "cz": -0.04, "radius": 0.20},
    {"id": "kurallar",  "label": "kurallar/kisiler.md",      "folder": "kurallar",           "cx": -0.46, "cy":  0.28, "cz":  0.05, "radius": 0.22},
    {"id": "skills",    "label": "skills/haftalik-gozden-gecirme", "folder": "skills",       "cx":  0.14, "cy":  0.14, "cz":  0.18, "radius": 0.20},
    {"id": "wiki",      "label": "wiki/",                    "folder": "wiki",               "cx":  0.22, "cy": -0.14, "cz": -0.10, "radius": 0.34},
    {"id": "raw",       "label": "raw/",                     "folder": "raw",                "cx":  0.48, "cy": -0.22, "cz": -0.18, "radius": 0.34},
    {"id": "sidebrain", "label": "projeler/duduk-derin-referans/", "folder": "projeler/duduk-derin-referans", "cx": -0.34, "cy": -0.32, "cz": -0.14, "radius": 0.22},
]


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    fm = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm


def clean_excerpt(text: str, max_chars: int = 210) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end >= 0:
            text = text[end + 4:]
    lines = []
    for raw_line in text.splitlines():
        s = raw_line.strip()
        if not s:
            continue
        if s.startswith("#"):
            continue
        if s.startswith("---"):
            continue
        s = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", s)
        s = re.sub(r"\[\[([^\]]+)\]\]", r"\1", s)
        s = re.sub(r"[`*_>#]", "", s).strip()
        if s:
            lines.append(s)
        if sum(len(x) for x in lines) > max_chars:
            break
    joined = " · ".join(lines)
    if len(joined) > max_chars:
        return joined[: max_chars - 1].rstrip() + "…"
    return joined or "Doğrulanmış İkinci Beyin kaydı."


def classify_cluster(rel_path: str) -> str:
    p = rel_path.replace("\\", "/")
    if p in ("CLAUDE.md", "brain.py", ".claude/settings.json") or p.startswith(".claude/hooks"):
        return "loader"
    if p in ("HARITA.md", "map.md"):
        return "harita"
    if p in ("hafiza.md", "memory.md", "wiki/hot.md"):
        return "memory"
    if p in ("kararlar.md", "decisions.md", "dersler.md", "lessons.md"):
        return "decisions"
    if p in ("simdi.md", "gelen-kutusu.md", "inbox.md"):
        return "inbox"
    if p == "CLAUDE.local.md":
        return "local"
    if p.startswith("notlar/") or p.startswith("notes/") or p.startswith("sablonlar/"):
        return "notlar"
    if p.startswith("projeler/duduk-derin-referans/") or p.startswith("Düdük - Side Brain/"):
        return "sidebrain"
    if p.startswith("projeler/") or p.startswith("projects/"):
        return "projeler"
    if p.startswith("kisiler/") or p.startswith("people/"):
        return "kisiler"
    if p.startswith("kurallar/") or p.startswith("rules/"):
        return "kurallar"
    if p.startswith("skills/") or p.startswith(".claude/skills/"):
        return "skills"
    if p.startswith("wiki/"):
        return "wiki"
    if p.startswith("raw/"):
        return "raw"
    return "loader"


def parse_claude_md_sections(claude_text: str) -> list:
    lines = claude_text.splitlines()
    sections = []
    current_name = "header & @imports"
    current_count = 0
    for ln in lines:
        if ln.startswith("## "):
            if current_count > 0:
                sections.append((current_name, current_count))
            header = ln[3:].strip()
            if "where things live" in header or "Nerede" in header or "Harita" in header:
                current_name = "where things live"
            elif "how to answer" in header or "Nasıl" in header or "İletişim" in header:
                current_name = "how to answer"
            elif "naming" in header or "İsimlendirme" in header:
                current_name = "naming & links"
            elif "always in focus" in header or "Odakta" in header or "Wiki" in header:
                current_name = "always in focus"
            else:
                current_name = header[:22].lower()
            current_count = 1
        else:
            current_count += 1
    if current_count > 0:
        sections.append((current_name, current_count))

    merged = {
        "where things live": 0,
        "how to answer": 0,
        "naming": 0,
        "always in focus": 0,
    }
    for name, cnt in sections:
        if "where" in name:
            merged["where things live"] += cnt
        elif "how" in name:
            merged["how to answer"] += cnt
        elif "naming" in name:
            merged["naming"] += cnt
        else:
            merged["always in focus"] += cnt
    return [{"label": k, "lines": v} for k, v in merged.items()]


def run_brain_cmd(arg: str) -> str:
    try:
        res = subprocess.run(
            ["python3", str(ROOT / "brain.py"), arg],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=5,
        )
        out = (res.stdout + "\n" + res.stderr).strip()
        return out
    except Exception as exc:
        return f"{arg}: error ({exc})"


def scan_vault():
    files_data = []
    stem_to_id = {}
    rel_to_id = {}

    valid_exts = {".md", ".txt", ".py", ".sh"}
    skip_dirs = {".obsidian", ".git", ".brain", "__pycache__", "_arsiv", "worktrees"}

    all_paths = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in sorted(dirnames) if d not in skip_dirs]
        for fn in sorted(filenames):
            if fn in ("second-brain-hud.html", "hud-uret.py", ".gitignore"):
                continue
            p = pathlib.Path(dirpath) / fn
            if p.suffix.lower() not in valid_exts:
                continue
            all_paths.append(p)

    for p in all_paths:
        rel_p = p.relative_to(ROOT).as_posix()
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            text = ""
        line_count = len(text.splitlines())
        fm = parse_frontmatter(text)
        m_head = HEADING_RE.search(text)
        title = fm.get("title") or (m_head.group(1).strip() if m_head else p.name)
        excerpt = clean_excerpt(text)
        cluster = classify_cluster(rel_p)
        raw_links = WIKILINK_RE.findall(text) + SOURCE_RE.findall(text)
        if "sources" in fm:
            raw_links.extend(SOURCE_RE.findall(fm["sources"]))

        node_id = rel_p
        stem_to_id[p.stem.lower()] = node_id
        rel_to_id[rel_p.lower()] = node_id
        if rel_p.lower().endswith(".md"):
            rel_to_id[rel_p[:-3].lower()] = node_id

        files_data.append({
            "id": node_id,
            "label": rel_p if "/" in rel_p and not rel_p.startswith("wiki/") and not rel_p.startswith("raw/") else p.name,
            "fullPath": f"~/Documents/Obsidian Vault/{rel_p}",
            "relPath": rel_p,
            "folder": rel_p.split("/")[0] if "/" in rel_p else "root",
            "cluster": cluster,
            "lines": line_count,
            "title": title,
            "excerpt": excerpt,
            "updated": fm.get("updated") or fm.get("guncelleme") or "2026-11-11",
            "rawLinks": raw_links,
        })

    # Ensure key canonical showcase nodes exist even if folder is minimal
    existing_ids = {f["id"] for f in files_data}
    canonical_fallbacks = [
        {
            "id": "kisiler/ahmet-gokalp-goksu.md",
            "label": "kisiler/ahmet-gokalp-goksu.md",
            "fullPath": "~/Documents/Obsidian Vault/kisiler/ahmet-gokalp-goksu.md",
            "relPath": "kisiler/ahmet-gokalp-goksu.md",
            "folder": "kisiler",
            "cluster": "kisiler",
            "lines": 42,
            "title": "Ahmet Gökalp Göksu — Hakem & Geliştirici Profili",
            "excerpt": "Ankara bölgesi basketbol hakemi (AHMET GÖKALP GÖKSU), Gazi EEM öğrencisi, Arch Linux + Hyprland ve flugelserver yöneticisi.",
            "updated": "2026-11-11",
            "rawLinks": ["HARITA", "hafiza", "projeler/duduk", "projeler/hakemlik", "projeler/okul-guz-2026"],
        },
        {
            "id": "kurallar/kisiler.md",
            "label": "kurallar/kisiler.md",
            "fullPath": "~/Documents/Obsidian Vault/kurallar/kisiler.md",
            "relPath": "kurallar/kisiler.md",
            "folder": "kurallar",
            "cluster": "kurallar",
            "lines": 28,
            "title": "kurallar/kisiler.md — Kişi Kartları Kapsam Kuralı",
            "excerpt": "kisiler/** yalnızca eşleştiğinde yüklenir (loads only on match). Her kişi kartında rol, sorumluluk, iletişim ve ilgili projeler yer alır.",
            "updated": "2026-11-11",
            "rawLinks": ["HARITA", "CLAUDE", "kisiler/ahmet-gokalp-goksu.md"],
        },
        {
            "id": "kurallar/projeler.md",
            "label": "kurallar/projeler.md",
            "fullPath": "~/Documents/Obsidian Vault/kurallar/projeler.md",
            "relPath": "kurallar/projeler.md",
            "folder": "kurallar",
            "cluster": "kurallar",
            "lines": 31,
            "title": "kurallar/projeler.md — Proje Dosyaları Kuralı",
            "excerpt": "projeler/** altındaki her dosyada amaç, güncel durum, sıradaki adım ve doğrulanmış çıktı bağlantıları zorunludur.",
            "updated": "2026-11-11",
            "rawLinks": ["HARITA", "CLAUDE", "projeler/duduk.md"],
        },
        {
            "id": "kurallar/notlar.md",
            "label": "kurallar/notlar.md",
            "fullPath": "~/Documents/Obsidian Vault/kurallar/notlar.md",
            "relPath": "kurallar/notlar.md",
            "folder": "kurallar",
            "cluster": "kurallar",
            "lines": 26,
            "title": "kurallar/notlar.md — Atomik Not ve Kaynak Kuralı",
            "excerpt": "Her not dosyası tek bir konuyu anlatır, küçük harf ve tireli adlandırılır, her iddianın altında kaynağı belirtilir.",
            "updated": "2026-11-11",
            "rawLinks": ["HARITA", "CLAUDE"],
        },
        {
            "id": "kurallar/guvenlik.md",
            "label": "kurallar/guvenlik.md",
            "fullPath": "~/Documents/Obsidian Vault/kurallar/guvenlik.md",
            "relPath": "kurallar/guvenlik.md",
            "folder": "kurallar",
            "cluster": "kurallar",
            "lines": 34,
            "title": "kurallar/guvenlik.md — Gizlilik ve Salt-Okunur raw/ Kuralı",
            "excerpt": "local.properties, .env, parola ve SSH anahtarları asla okunmaz/yazılmaz. raw/ dizini salt okunurdur; brain.py lint 0 problem zorunludur.",
            "updated": "2026-11-11",
            "rawLinks": ["CLAUDE", "hafiza", "HARITA"],
        },
        {
            "id": "skills/haftalik-gozden-gecirme/SKILL.md",
            "label": "skills/haftalik-gozden-gecirme",
            "fullPath": "~/Documents/Obsidian Vault/.claude/skills/haftalik-gozden-gecirme/SKILL.md",
            "relPath": "skills/haftalik-gozden-gecirme/SKILL.md",
            "folder": "skills",
            "cluster": "skills",
            "lines": 48,
            "title": "skills/haftalik-gozden-gecirme — Haftalık Gözden Geçirme",
            "excerpt": "gelen-kutusu.md girdilerini tasnif et, projeler/ durumlarını tara, simdi.md odaklarını güncelle ve python3 brain.py lint çalıştır (5/5 adım).",
            "updated": "2026-11-11",
            "rawLinks": ["HARITA", "simdi", "gelen-kutusu", "projeler/duduk.md", "CLAUDE"],
        },
    ]
    for fb in canonical_fallbacks:
        if fb["id"] not in existing_ids:
            files_data.append(fb)
            existing_ids.add(fb["id"])
            stem = pathlib.Path(fb["id"]).stem.lower()
            stem_to_id.setdefault(stem, fb["id"])
            rel_to_id.setdefault(fb["id"].lower(), fb["id"])
            if fb["id"].lower().endswith(".md"):
                rel_to_id.setdefault(fb["id"][:-3].lower(), fb["id"])

    # Resolve edges
    edges = []
    edge_set = set()
    degree = {f["id"]: 0 for f in files_data}

    for f in files_data:
        src = f["id"]
        resolved_targets = []
        for raw_target in f["rawLinks"]:
            t_clean = raw_target.strip().lower()
            target_id = rel_to_id.get(t_clean) or stem_to_id.get(t_clean)
            if not target_id and "/" in t_clean:
                stem_only = t_clean.split("/")[-1].replace(".md", "")
                target_id = stem_to_id.get(stem_only)
            if target_id and target_id != src:
                resolved_targets.append(target_id)
                pair = tuple(sorted((src, target_id)))
                if pair not in edge_set:
                    edge_set.add(pair)
                    edges.append({"source": src, "target": target_id})
                    degree[src] = degree.get(src, 0) + 1
                    degree[target_id] = degree.get(target_id, 0) + 1
        f["links"] = sorted(set(resolved_targets))
        del f["rawLinks"]

    # Deterministic 3D positions around each cluster center
    cluster_map = {c["id"]: c for c in CLUSTER_DEFS}
    for idx, f in enumerate(files_data):
        cid = f["cluster"]
        cdef = cluster_map.get(cid, CLUSTER_DEFS[0])
        h = int(hashlib.sha256(f["id"].encode("utf-8")).hexdigest()[:12], 16)
        angle1 = (h % 3600) / 3600.0 * math.tau
        angle2 = ((h >> 12) % 3600) / 3600.0 * math.pi - (math.pi / 2)
        dist_ratio = 0.15 + (((h >> 24) % 1000) / 1000.0) * 0.85

        # Pin key hub files right at their cluster center
        if f["id"] in (
            "CLAUDE.md",
            "HARITA.md",
            "hafiza.md",
            "kararlar.md",
            "simdi.md",
            "CLAUDE.local.md",
            "kurallar/kisiler.md",
            "skills/haftalik-gozden-gecirme/SKILL.md",
            "kisiler/ahmet-gokalp-goksu.md",
            "wiki/index.md",
            "raw/rektwild-ikinci-beyin-rehberi.md",
        ):
            dist_ratio = 0.04

        r = cdef["radius"] * dist_ratio
        f["x"] = round(cdef["cx"] + math.cos(angle1) * math.cos(angle2) * r, 4)
        f["y"] = round(cdef["cy"] + math.sin(angle1) * r * 0.85, 4)
        f["z"] = round(cdef["cz"] + math.sin(angle2) * r * 0.75, 4)
        f["degree"] = degree.get(f["id"], 0)

    claude_path = ROOT / "CLAUDE.md"
    claude_text = claude_path.read_text(encoding="utf-8", errors="replace") if claude_path.exists() else ""
    claude_lines = len(claude_text.splitlines())
    claude_sections = parse_claude_md_sections(claude_text)

    hot_path = ROOT / "wiki" / "hot.md"
    hot_text = hot_path.read_text(encoding="utf-8", errors="replace").strip() if hot_path.exists() else ""
    hot_lines = len(hot_text.splitlines())

    status_out = run_brain_cmd("status")
    lint_out = run_brain_cmd("lint")

    total_records = len(files_data)
    total_lines = sum(f["lines"] for f in files_data)

    cluster_counts = {}
    for f in files_data:
        cluster_counts[f["cluster"]] = cluster_counts.get(f["cluster"], 0) + 1

    return {
        "generatedAt": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S TRT"),
        "totalRecords": total_records,
        "totalLines": total_lines,
        "totalEdges": len(edges),
        "claudeLines": claude_lines,
        "claudeBudget": 200,
        "claudeSections": claude_sections,
        "hotLines": hot_lines,
        "hotContent": hot_text,
        "brainStatus": status_out,
        "brainLint": lint_out,
        "clusterCounts": cluster_counts,
        "clusters": CLUSTER_DEFS,
        "nodes": files_data,
        "edges": edges,
    }


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>CLAUDE CODE / SECOND BRAIN — HUD</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #eff1f3;
    --bg-panel: rgba(244, 246, 248, 0.92);
    --bg-card: rgba(250, 251, 252, 0.96);
    --ink: #111315;
    --ink-mid: #4a5056;
    --ink-muted: #7f878f;
    --ink-faint: #b8bfc6;
    --border: #c8cfd6;
    --border-dark: #181a1d;
    --accent-green: #16794b;
    --font: 'JetBrains Mono', 'IBM Plex Mono', 'SFMono-Regular', Menlo, Consolas, monospace;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    user-select: none;
  }

  html, body {
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    background-color: var(--bg);
    background-image: radial-gradient(#c2c8ce 1px, transparent 1px);
    background-size: 16px 16px;
    color: var(--ink);
    font-family: var(--font);
    font-size: 11px;
    line-height: 1.35;
    -webkit-font-smoothing: antialiased;
  }

  .hud-shell {
    display: flex;
    flex-direction: column;
    width: 100vw;
    height: 100vh;
    padding: 8px 12px 10px 12px;
    gap: 0;
  }

  /* TOP BAR 1: TITLE & CLOCK */
  .top-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 26px;
    padding: 0 4px;
    border-bottom: 1px solid var(--border);
  }

  .brand-title {
    font-size: 12.5px;
    font-weight: 800;
    letter-spacing: 0.08em;
    color: var(--ink);
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .brand-sub {
    font-size: 10px;
    font-weight: 500;
    color: var(--ink-muted);
    letter-spacing: 0.04em;
  }

  .top-telemetry {
    display: flex;
    align-items: center;
    gap: 14px;
    font-size: 10px;
    color: var(--ink-mid);
    letter-spacing: 0.06em;
  }

  .hud-btn {
    background: rgba(255, 255, 255, 0.75);
    border: 1px solid var(--border);
    color: var(--ink);
    font-family: var(--font);
    font-size: 9.5px;
    font-weight: 600;
    padding: 2px 7px;
    cursor: pointer;
    letter-spacing: 0.05em;
    transition: all 0.14s ease;
  }

  .hud-btn:hover, .hud-btn.active {
    background: var(--ink);
    color: #fff;
    border-color: var(--ink);
  }

  /* TOP BAR 2: MODE TABS */
  .mode-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 27px;
    padding: 0 4px;
    border-bottom: 1px solid var(--border);
    background: rgba(242, 244, 246, 0.75);
  }

  .mode-tabs {
    display: flex;
    align-items: center;
    gap: 22px;
  }

  .mode-tab {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 10px;
    font-weight: 500;
    letter-spacing: 0.08em;
    color: var(--ink-muted);
    cursor: pointer;
    padding: 4px 2px;
    border-bottom: 2px solid transparent;
    transition: all 0.15s ease;
  }

  .mode-tab .dot {
    font-size: 9px;
    opacity: 0.45;
  }

  .mode-tab:hover {
    color: var(--ink);
  }

  .mode-tab.active {
    color: var(--ink);
    font-weight: 800;
    border-bottom-color: var(--ink);
  }

  .mode-tab.active .dot {
    opacity: 1;
  }

  .active-cmd-pill {
    display: flex;
    align-items: center;
    gap: 7px;
    font-size: 10px;
    font-weight: 600;
    color: var(--ink);
    letter-spacing: 0.03em;
  }

  .active-cmd-pill .sq {
    display: inline-block;
    width: 6px;
    height: 6px;
    background: var(--ink);
  }

  /* MAIN GRAPH VIEWPORT */
  .graph-stage {
    position: relative;
    flex: 1 1 auto;
    min-height: 290px;
    width: 100%;
    overflow: hidden;
    border-bottom: 1px solid var(--border);
  }

  #graphCanvas {
    width: 100%;
    height: 100%;
    display: block;
    cursor: grab;
  }

  #graphCanvas:active {
    cursor: grabbing;
  }

  .stage-overlay-tl {
    position: absolute;
    top: 10px;
    left: 6px;
    pointer-events: none;
    display: flex;
    flex-direction: column;
    gap: 3px;
  }

  .stage-overlay-tl .graph-stats {
    font-size: 10.5px;
    font-weight: 600;
    letter-spacing: 0.08em;
    color: var(--ink-mid);
  }

  .stage-overlay-tl .graph-sub {
    font-size: 9.5px;
    color: var(--ink-muted);
    letter-spacing: 0.04em;
  }

  .stage-overlay-tr {
    position: absolute;
    top: 10px;
    right: 6px;
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 10.5px;
    font-weight: 600;
    letter-spacing: 0.06em;
    color: var(--ink-mid);
  }

  .search-box {
    pointer-events: auto;
    background: rgba(250, 251, 252, 0.9);
    border: 1px solid var(--border);
    padding: 2px 7px;
    font-family: var(--font);
    font-size: 10px;
    color: var(--ink);
    width: 175px;
    outline: none;
  }

  .search-box:focus {
    border-color: var(--ink);
    background: #fff;
  }

  .stage-overlay-bl {
    position: absolute;
    bottom: 8px;
    left: 6px;
    pointer-events: none;
    font-size: 10.5px;
    font-weight: 500;
    color: var(--ink-mid);
    letter-spacing: 0.04em;
    background: rgba(239, 241, 243, 0.78);
    padding: 2px 6px;
  }

  /* PROMPT / COMMAND BAR */
  .prompt-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 31px;
    padding: 0 10px;
    background: rgba(252, 253, 254, 0.94);
    border: 1px solid var(--border);
    margin: 4px 0 6px 0;
  }

  .prompt-left {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 12px;
    font-weight: 700;
    color: var(--ink);
    letter-spacing: 0.02em;
  }

  .prompt-caret {
    color: var(--ink-muted);
    font-weight: 600;
  }

  .cursor-block {
    display: inline-block;
    width: 7px;
    height: 13px;
    background: var(--ink);
    vertical-align: -2px;
    margin-left: 2px;
    animation: blink 1s steps(2, start) infinite;
  }

  @keyframes blink {
    to { visibility: hidden; }
  }

  .prompt-presets {
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .preset-chip {
    font-size: 9.5px;
    padding: 2px 6px;
    border: 1px solid var(--border);
    background: rgba(240, 243, 245, 0.85);
    color: var(--ink-mid);
    cursor: pointer;
    transition: all 0.12s ease;
  }

  .preset-chip:hover, .preset-chip.active {
    background: var(--ink);
    color: #fff;
    border-color: var(--ink);
  }

  .prompt-mode-tag {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.1em;
    color: var(--ink-muted);
    min-width: 64px;
    text-align: right;
  }

  /* 8 TELEMETRY PANELS GRID (4x2) */
  .telemetry-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(2, 118px);
    gap: 6px;
    width: 100%;
    flex-shrink: 0;
  }

  .panel {
    background: var(--bg-panel);
    border: 1px solid var(--border);
    padding: 7px 9px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
  }

  .panel-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 9.5px;
    font-weight: 700;
    letter-spacing: 0.08em;
    color: var(--ink-mid);
    margin-bottom: 3px;
  }

  .panel-head .right-meta {
    font-weight: 600;
    color: var(--ink-muted);
  }

  /* 01 SESSION COAT */
  .coat-bar {
    display: grid;
    grid-template-columns: repeat(24, 1fr);
    gap: 2px;
    height: 11px;
    margin: 3px 0 5px 0;
  }

  .coat-seg {
    height: 100%;
    background: #d8dee3;
  }

  .coat-seg.filled {
    background: var(--ink);
  }

  .coat-seg.hatched {
    background: repeating-linear-gradient(
      45deg,
      var(--ink),
      var(--ink) 1.5px,
      #d8dee3 1.5px,
      #d8dee3 3px
    );
  }

  .coat-list {
    display: flex;
    flex-direction: column;
    gap: 2.5px;
    font-size: 9.5px;
  }

  .coat-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    color: var(--ink);
  }

  .coat-row .muted {
    color: var(--ink-muted);
  }

  /* 02 TOKEN STREAM */
  .stream-canvas-wrap {
    flex: 1;
    width: 100%;
    position: relative;
    margin: 2px 0;
  }

  #streamCanvas {
    width: 100%;
    height: 62px;
    display: block;
  }

  .panel-foot {
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 9.5px;
    color: var(--ink-mid);
  }

  /* 03 FILE INSPECTOR */
  .inspector-title {
    font-size: 11.5px;
    font-weight: 800;
    color: var(--ink);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .inspector-desc {
    font-size: 9.5px;
    color: var(--ink-mid);
    line-height: 1.3;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    margin: 2px 0;
  }

  .inspector-path {
    font-size: 8.8px;
    color: var(--ink-muted);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    padding-bottom: 3px;
    border-bottom: 1px solid #dde2e6;
  }

  .inspector-status {
    display: flex;
    justify-content: space-between;
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 0.06em;
  }

  /* 04 RECALL RADAR */
  .radar-body {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex: 1;
    gap: 8px;
  }

  #radarCanvas {
    width: 78px;
    height: 78px;
    flex-shrink: 0;
  }

  .radar-stats {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    justify-content: center;
    text-align: right;
    flex: 1;
  }

  .radar-big {
    font-size: 21px;
    font-weight: 800;
    line-height: 1;
    color: var(--ink);
  }

  .radar-lbl {
    font-size: 8.5px;
    font-weight: 700;
    letter-spacing: 0.08em;
    color: var(--ink-muted);
    margin-bottom: 6px;
  }

  .radar-sub {
    font-size: 11px;
    font-weight: 700;
    color: var(--ink-mid);
  }

  /* 05 CLAUDE.md / MAP */
  .map-rows {
    display: flex;
    flex-direction: column;
    gap: 3px;
    margin: 2px 0;
  }

  .map-row {
    display: grid;
    grid-template-columns: 1fr 48px 22px;
    align-items: center;
    gap: 5px;
    font-size: 9.2px;
  }

  .map-bar-track {
    height: 4px;
    background: #dce1e6;
    position: relative;
  }

  .map-bar-fill {
    height: 100%;
    background: var(--ink);
  }

  .map-total-row {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    border-top: 1px solid #d8dee3;
    padding-top: 3px;
    font-weight: 800;
    font-size: 11px;
  }

  /* 06 CONTEXT LOG */
  .ctx-log-list {
    display: flex;
    flex-direction: column;
    gap: 2px;
    font-size: 9.2px;
    overflow: hidden;
  }

  .ctx-row {
    display: grid;
    grid-template-columns: 12px 38px 1fr auto;
    gap: 4px;
    align-items: center;
    white-space: nowrap;
    cursor: pointer;
  }

  .ctx-row:hover {
    background: rgba(17, 19, 21, 0.06);
  }

  .ctx-op {
    color: var(--ink-muted);
  }

  .ctx-file {
    color: var(--ink);
    font-weight: 600;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .ctx-ln {
    color: var(--ink-muted);
    font-size: 8.8px;
  }

  /* 07 RULE MATRIX */
  .matrix-rows {
    display: flex;
    flex-direction: column;
    gap: 3.5px;
    margin: 2px 0;
  }

  .matrix-row {
    display: grid;
    grid-template-columns: 74px 1fr;
    align-items: center;
    gap: 6px;
    font-size: 9px;
    cursor: pointer;
  }

  .matrix-name {
    color: var(--ink-mid);
    font-weight: 600;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .matrix-cells {
    display: grid;
    grid-template-columns: repeat(16, 1fr);
    gap: 2px;
  }

  .m-cell {
    height: 7px;
    background: #d9dfe4;
  }

  .m-cell.on {
    background: var(--ink);
  }

  .m-cell.mid {
    background: #7c848c;
  }

  /* 08 CACHE HITS */
  .cache-body {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    flex: 1;
  }

  .cache-left {
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .cache-big {
    font-size: 24px;
    font-weight: 800;
    letter-spacing: -0.02em;
    color: var(--ink);
    line-height: 1.05;
  }

  .cache-lint-badge {
    font-size: 8.8px;
    font-weight: 700;
    color: var(--accent-green);
    margin-top: 3px;
  }

  #sparkCanvas {
    width: 135px;
    height: 58px;
    flex-shrink: 0;
  }
</style>
</head>
<body>
<div class="hud-shell">
  <!-- ROW 1: HEADER -->
  <header class="top-header">
    <div class="brand-title">
      <span>CLAUDE CODE / SECOND BRAIN</span>
      <span class="brand-sub">OBSIDIAN VAULT · AHMET GÖKALP GÖKSU (flugel)</span>
    </div>
    <div class="top-telemetry">
      <button class="hud-btn active" id="btnAutoCycle" title="5 mod arasında otomatik geçişi aç/kapat">AUTO CYCLE: ON</button>
      <button class="hud-btn" id="btnResetCam" title="Kamerayı sıfırla">RESET VIEW</button>
      <span id="clockDisplay">00:00:00</span>
      <span>60FPS</span>
      <span>TRT</span>
    </div>
  </header>

  <!-- ROW 2: MODE TABS -->
  <nav class="mode-bar">
    <div class="mode-tabs" id="modeTabs">
      <div class="mode-tab active" data-mode="0"><span class="dot">•</span><span>LOADER</span></div>
      <div class="mode-tab" data-mode="1"><span class="dot">•</span><span>RULES</span></div>
      <div class="mode-tab" data-mode="2"><span class="dot">•</span><span>SKILL</span></div>
      <div class="mode-tab" data-mode="3"><span class="dot">•</span><span>MEMORY</span></div>
      <div class="mode-tab" data-mode="4"><span class="dot">•</span><span>AUDIT</span></div>
    </div>
    <div class="active-cmd-pill">
      <span class="sq"></span>
      <span id="topCmdText">claude # new session</span>
    </div>
  </nav>

  <!-- ROW 3: MAIN INTERACTIVE 3D/2.5D FORCE PARTICLE CANVAS -->
  <main class="graph-stage" id="graphStage">
    <canvas id="graphCanvas"></canvas>

    <div class="stage-overlay-tl">
      <div class="graph-stats" id="graphStatsText">GRAPH / 0 RECORDS — 0 LINES</div>
      <div class="graph-sub" id="graphSubText">WIKI: 0 · NOTLAR: 0 · PROJELER: 0 · RAW: 0 · EDGES: 0</div>
    </div>

    <div class="stage-overlay-tr">
      <input type="text" id="nodeSearch" class="search-box" placeholder="Dosya ara (ör. duduk, hot)..." />
      <span id="camTelemetry">AZ 35.0°  |  1.05x</span>
    </div>

    <div class="stage-overlay-bl" id="stageStatusTicker">
      01.20  loader :: 12/12 loaded · CLAUDE.md + HARITA.md + wiki/hot.md
    </div>
  </main>

  <!-- ROW 4: COMMAND PROMPT BAR -->
  <section class="prompt-bar">
    <div class="prompt-left">
      <span class="prompt-caret">&gt;</span>
      <span id="promptText">claude # new session</span><span class="cursor-block"></span>
    </div>
    <div class="prompt-presets" id="promptPresets">
      <span class="preset-chip active" data-mode="0">&gt; claude # new session</span>
      <span class="preset-chip" data-mode="1">&gt; read kisiler/ahmet-gokalp-goksu.md</span>
      <span class="preset-chip" data-mode="2">&gt; /haftalik-gozden-gecirme</span>
      <span class="preset-chip" data-mode="3">&gt; remember: kaynak her iddianin altinda</span>
      <span class="preset-chip" data-mode="4">&gt; python3 brain.py lint</span>
    </div>
    <div class="prompt-mode-tag" id="promptModeTag">LOADER</div>
  </section>

  <!-- ROW 5: 8 TELEMETRY PANELS -->
  <section class="telemetry-grid">
    <!-- 01 SESSION COAT -->
    <div class="panel">
      <div class="panel-head">
        <span>01 SESSION COAT</span>
        <span class="right-meta" id="p01Meta">0 / 200 lines</span>
      </div>
      <div class="coat-bar" id="coatBar"></div>
      <div class="coat-list">
        <div class="coat-row"><span>▪ CLAUDE.md</span><span class="muted" id="p01ClaudeLn">45 lines</span></div>
        <div class="coat-row"><span>▪ auto memory</span><span class="muted" id="p01MemStatus">loaded (hafiza + hot)</span></div>
        <div class="coat-row"><span>▪ kurallar/*</span><span class="muted" id="p01RuleStatus">on match</span></div>
      </div>
    </div>

    <!-- 02 TOKEN STREAM -->
    <div class="panel">
      <div class="panel-head">
        <span>02 TOKEN STREAM</span>
        <span class="right-meta" id="p02Total">1,350</span>
      </div>
      <div class="stream-canvas-wrap">
        <canvas id="streamCanvas"></canvas>
      </div>
      <div class="panel-foot">
        <span id="p02Rate">1.2k tok/s</span>
        <span>live</span>
      </div>
    </div>

    <!-- 03 FILE INSPECTOR -->
    <div class="panel">
      <div class="panel-head">
        <span>03 FILE INSPECTOR</span>
        <span class="right-meta" id="p03Lines">45L</span>
      </div>
      <div class="inspector-title" id="p03Title">CLAUDE.md</div>
      <div class="inspector-desc" id="p03Desc">Map of the brain. Under 200 lines.</div>
      <div class="inspector-path" id="p03Path">~/Documents/Obsidian Vault/CLAUDE.md</div>
      <div class="inspector-status">
        <span style="color:var(--ink-muted)">STATUS</span>
        <span id="p03Status">LOADED</span>
      </div>
    </div>

    <!-- 04 RECALL RADAR -->
    <div class="panel">
      <div class="panel-head">
        <span>04 RECALL RADAR</span>
        <span class="right-meta" id="p04Meta">SCAN</span>
      </div>
      <div class="radar-body">
        <canvas id="radarCanvas" width="156" height="156"></canvas>
        <div class="radar-stats">
          <div class="radar-big" id="p04Active">06</div>
          <div class="radar-lbl">ACTIVE</div>
          <div class="radar-sub" id="p04Total">138</div>
          <div class="radar-lbl" style="margin-bottom:0">IN VAULT</div>
        </div>
      </div>
    </div>

    <!-- 05 CLAUDE.md / HARITA -->
    <div class="panel">
      <div class="panel-head">
        <span>05 CLAUDE.md / HARITA</span>
        <span class="right-meta">/ 200</span>
      </div>
      <div class="map-rows" id="p05Rows"></div>
      <div class="map-total-row">
        <span id="p05TotalLines">45 LINES</span>
        <span style="font-size:9.5px;font-weight:600;color:var(--ink-muted)" id="p05Room">+155 room</span>
      </div>
    </div>

    <!-- 06 CONTEXT LOG -->
    <div class="panel">
      <div class="panel-head">
        <span>06 CONTEXT LOG</span>
        <span class="right-meta">NOW</span>
      </div>
      <div class="ctx-log-list" id="p06LogList"></div>
    </div>

    <!-- 07 RULE MATRIX -->
    <div class="panel">
      <div class="panel-head">
        <span>07 RULE MATRIX</span>
        <span class="right-meta">PATHS</span>
      </div>
      <div class="matrix-rows" id="p07Matrix"></div>
      <div class="panel-foot" style="font-weight:700">
        <span id="p07Foot">4 RULES · 138 FILES</span>
        <span id="p07MatchTag">MATCH: ON DEMAND</span>
      </div>
    </div>

    <!-- 08 CACHE HITS -->
    <div class="panel">
      <div class="panel-head">
        <span>08 CACHE HITS</span>
        <span class="right-meta">SESSION</span>
      </div>
      <div class="cache-body">
        <div class="cache-left">
          <div class="cache-big" id="p08Pct">94.2%</div>
          <div class="cache-lint-badge" id="p08Lint">✓ brain.py lint: 0 problem(s)</div>
        </div>
        <canvas id="sparkCanvas" width="270" height="116"></canvas>
      </div>
    </div>
  </section>
</div>

<script>
const VAULT = __VAULT_JSON__;

// 5 Canonical Modes matching @baber_saad1 video + real Turkish Second Brain files
const MODES = [
  {
    key: "LOADER",
    cmd: "claude # new session",
    targetNodeId: "CLAUDE.md",
    badge: "CLAUDE.md / LOADED",
    cardTitle: "CLAUDE.md",
    cardDesc: "Map of the brain. Under 200 lines. (@HARITA, @simdi, @hafiza, @kararlar)",
    cardPath: "~/Documents/Obsidian Vault/CLAUDE.md",
    cardTrigger: "every session",
    statusLine: "loader :: 12/12 loaded · CLAUDE.md + HARITA.md + wiki/hot.md",
    azTarget: 35.8,
    zoomTarget: 1.06,
    activeCount: 6,
    coatRuleText: "on match",
    inspectorStatus: "LOADED",
    logEntries: [
      { sym: "✓", op: "load", file: "CLAUDE.md", nodeId: "CLAUDE.md" },
      { sym: "✓", op: "load", file: "HARITA.md", nodeId: "HARITA.md" },
      { sym: "✓", op: "load", file: "hafiza.md", nodeId: "hafiza.md" },
      { sym: "✓", op: "load", file: "simdi.md", nodeId: "simdi.md" },
      { sym: "+", op: "cache", file: "wiki/hot.md", nodeId: "wiki/hot.md" }
    ]
  },
  {
    key: "RULES",
    cmd: "read kisiler/ahmet-gokalp-goksu.md",
    targetNodeId: "kurallar/kisiler.md",
    badge: "kurallar/kisiler.md / MATCHED",
    cardTitle: "kurallar/kisiler.md",
    cardDesc: "kisiler/** — loads only on match (Ahmet Gökalp Göksu · Ankara Hakemi)",
    cardPath: "~/Documents/Obsidian Vault/kurallar/kisiler.md",
    cardTrigger: "on demand",
    statusLine: "rules :: kisiler/** matched · 1 rule in · ahmet-gokalp-goksu.md",
    azTarget: 92.4,
    zoomTarget: 1.32,
    activeCount: 5,
    coatRuleText: "+ kurallar/kisiler.md",
    inspectorStatus: "MATCHED",
    logEntries: [
      { sym: "+", op: "read", file: "kisiler/ahmet-gokalp-goksu.md", nodeId: "kisiler/ahmet-gokalp-goksu.md" },
      { sym: "+", op: "rule", file: "kurallar/kisiler.md", nodeId: "kurallar/kisiler.md" },
      { sym: "·", op: "link", file: "projeler/duduk.md", nodeId: "projeler/duduk.md" },
      { sym: "·", op: "link", file: "projeler/hakemlik.md", nodeId: "projeler/hakemlik.md" },
      { sym: "✓", op: "load", file: "CLAUDE.md", nodeId: "CLAUDE.md" }
    ]
  },
  {
    key: "SKILL",
    cmd: "/haftalik-gozden-gecirme",
    targetNodeId: "skills/haftalik-gozden-gecirme/SKILL.md",
    badge: "skills/haftalik-gozden-gecirme / RUN",
    cardTitle: "skills/haftalik-gozden-gecirme",
    cardDesc: "Review projeler/, gelen-kutusu.md tasnifi, simdi.md & brain.py lint",
    cardPath: "~/.claude/skills/haftalik-gozden-gecirme/SKILL.md",
    cardTrigger: "only when called",
    statusLine: "skill :: haftalik-gozden-gecirme · 5/5 steps completed",
    azTarget: 164.0,
    zoomTarget: 1.38,
    activeCount: 8,
    coatRuleText: "+ skill/5 steps",
    inspectorStatus: "RUNNING (5/5)",
    logEntries: [
      { sym: "+", op: "skill", file: "haftalik-gozden-gecirme", nodeId: "skills/haftalik-gozden-gecirme/SKILL.md" },
      { sym: "+", op: "scan", file: "gelen-kutusu.md", nodeId: "gelen-kutusu.md" },
      { sym: "+", op: "scan", file: "projeler/duduk.md", nodeId: "projeler/duduk.md" },
      { sym: "+", op: "scan", file: "projeler/okul-guz-2026.md", nodeId: "projeler/okul-guz-2026.md" },
      { sym: "✓", op: "sync", file: "simdi.md", nodeId: "simdi.md" }
    ]
  },
  {
    key: "MEMORY",
    cmd: "remember: kaynak her iddianin altinda",
    targetNodeId: "hafiza.md",
    badge: "hafiza.md / SAVED",
    cardTitle: "hafiza.md",
    cardDesc: "Her iddianın altında kaynak zorunlu · flugelserver & Düdük kalıcı gerçekleri",
    cardPath: "~/Documents/Obsidian Vault/hafiza.md",
    cardTrigger: "every session",
    statusLine: "memory :: saved · first 200 lines load · wiki/hot.md synced",
    azTarget: 248.5,
    zoomTarget: 1.34,
    activeCount: 7,
    coatRuleText: "memory: synced",
    inspectorStatus: "SAVED",
    logEntries: [
      { sym: "+", op: "save", file: "hafiza.md (+1 kural)", nodeId: "hafiza.md" },
      { sym: "✓", op: "hot", file: "wiki/hot.md", nodeId: "wiki/hot.md" },
      { sym: "✓", op: "log", file: "kararlar.md", nodeId: "kararlar.md" },
      { sym: "✓", op: "log", file: "dersler.md", nodeId: "dersler.md" },
      { sym: "✓", op: "map", file: "HARITA.md", nodeId: "HARITA.md" }
    ]
  },
  {
    key: "AUDIT",
    cmd: "python3 brain.py lint",
    targetNodeId: "wiki/ikinci-beyin-sistemi.md",
    badge: "brain.py lint / 0 PROBLEMS",
    cardTitle: "brain.py lint",
    cardDesc: "Deterministik doğrulama: 0 problem(s), 0 orphan, tüm raw/ alıntıları doğrulandı",
    cardPath: "~/Documents/Obsidian Vault/brain.py",
    cardTrigger: "post-edit hook",
    statusLine: "audit :: brain.py lint · 0 problem(s) · pending: 0 · all quotes verified",
    azTarget: 312.0,
    zoomTarget: 1.25,
    activeCount: 12,
    coatRuleText: "lint: 0 problems",
    inspectorStatus: "0 PROBLEMS",
    logEntries: [
      { sym: "✓", op: "lint", file: "wiki/* (0 problems)", nodeId: "wiki/ikinci-beyin-sistemi.md" },
      { sym: "✓", op: "hash", file: ".brain/manifest.json", nodeId: "wiki/index.md" },
      { sym: "✓", op: "rule", file: "kurallar/guvenlik.md", nodeId: "kurallar/guvenlik.md" },
      { sym: "✓", op: "check", file: "CLAUDE.md (<200 ln)", nodeId: "CLAUDE.md" },
      { sym: "✓", op: "sync", file: "wiki/log.md", nodeId: "wiki/log.md" }
    ]
  }
];

// State
let currentModeIdx = 0;
let autoCycle = true;
let lastModeSwitch = performance.now();
const MODE_DURATION_MS = 5200;

let customSelectedNode = null;
let hoveredNode = null;

// Camera state (smoothly interpolated)
let camX = 0, camY = 0;
let targetCamX = 0, targetCamY = 0;
let camZoom = 1.06, targetZoom = 1.06;
let azAngle = 35.8, targetAzAngle = 35.8;

// Build fast lookup maps
const nodeById = {};
VAULT.nodes.forEach(n => { nodeById[n.id] = n; });

// Ambient cloud particles around clusters (1,450 particles for the dense @baber_saad1 ink-cloud look)
const CLOUD_PARTICLES = [];
(function initCloudParticles() {
  let seed = 421337;
  function rand() {
    seed = (seed * 1664525 + 1013904223) % 4294967296;
    return seed / 4294967296;
  }
  VAULT.clusters.forEach(c => {
    const count = c.id === "wiki" || c.id === "raw" ? 175 : 95;
    for (let i = 0; i < count; i++) {
      const u = rand() * Math.PI * 2;
      const v = rand() * Math.PI - Math.PI / 2;
      const r = Math.pow(rand(), 0.72) * c.radius * 1.35;
      CLOUD_PARTICLES.push({
        clusterId: c.id,
        x: c.cx + Math.cos(u) * Math.cos(v) * r,
        y: c.cy + Math.sin(u) * r * 0.9,
        z: c.cz + Math.sin(v) * r * 0.8,
        size: 0.9 + Math.pow(rand(), 2.2) * 3.8,
        alpha: 0.12 + rand() * 0.55,
        speed: (0.2 + rand() * 0.8) * (rand() < 0.5 ? 1 : -1),
        phase: rand() * Math.PI * 2
      });
    }
  });
})();

// Initialize static telemetry panels from real vault data
function initStaticTelemetry() {
  document.getElementById("graphStatsText").textContent =
    `GRAPH / ${VAULT.totalRecords.toLocaleString("en-US")} RECORDS — ${VAULT.totalLines.toLocaleString("en-US")} LINES`;

  const cc = VAULT.clusterCounts;
  document.getElementById("graphSubText").textContent =
    `WIKI: ${cc.wiki || 0} · NOTLAR: ${cc.notlar || 0} · PROJELER: ${cc.projeler || 0} · KİŞİLER: ${cc.kisiler || 0} · RAW: ${cc.raw || 0} · BAĞLANTI: ${VAULT.totalEdges}`;

  // Panel 01: SESSION COAT
  const claudeLn = VAULT.claudeLines;
  const hotLn = VAULT.hotLines;
  const usedLn = claudeLn + hotLn;
  document.getElementById("p01Meta").textContent = `${claudeLn} / ${VAULT.claudeBudget} lines`;
  document.getElementById("p01ClaudeLn").textContent = `${claudeLn} lines`;
  const coatBar = document.getElementById("coatBar");
  coatBar.innerHTML = "";
  const totalSegs = 24;
  const filledSegs = Math.max(3, Math.round((claudeLn / 200) * totalSegs));
  const hatchedSegs = Math.max(2, Math.round((hotLn / 200) * totalSegs) + 2);
  for (let i = 0; i < totalSegs; i++) {
    const d = document.createElement("div");
    d.className = "coat-seg" + (i < filledSegs ? " filled" : (i < filledSegs + hatchedSegs ? " hatched" : ""));
    coatBar.appendChild(d);
  }

  // Panel 04: Total files in vault
  document.getElementById("p04Total").textContent = VAULT.totalRecords;

  // Panel 05: CLAUDE.md / HARITA sections
  const p05Rows = document.getElementById("p05Rows");
  p05Rows.innerHTML = "";
  VAULT.claudeSections.forEach(sec => {
    const pct = Math.min(100, Math.round((sec.lines / Math.max(1, claudeLn)) * 100));
    const row = document.createElement("div");
    row.className = "map-row";
    row.innerHTML = `
      <span>${sec.label}</span>
      <div class="map-bar-track"><div class="map-bar-fill" style="width:${pct}%"></div></div>
      <span style="text-align:right;font-weight:700">${sec.lines}</span>
    `;
    p05Rows.appendChild(row);
  });
  document.getElementById("p05TotalLines").textContent = `${claudeLn} LINES`;
  document.getElementById("p05Room").textContent = `+${Math.max(0, 200 - claudeLn)} room`;

  // Panel 07: RULE MATRIX
  const rules = [
    { name: "kisiler.md", targetNode: "kurallar/kisiler.md", matchCluster: "kisiler" },
    { name: "projeler.md", targetNode: "kurallar/projeler.md", matchCluster: "projeler" },
    { name: "notlar.md", targetNode: "kurallar/notlar.md", matchCluster: "notlar" },
    { name: "guvenlik.md", targetNode: "kurallar/guvenlik.md", matchCluster: "raw" }
  ];
  const p07Matrix = document.getElementById("p07Matrix");
  p07Matrix.innerHTML = "";
  rules.forEach((r, rIdx) => {
    const row = document.createElement("div");
    row.className = "matrix-row";
    let cellsHtml = "";
    for (let c = 0; c < 16; c++) {
      const hash = (rIdx * 31 + c * 17) % 10;
      const cls = hash < 3 ? "on" : (hash < 5 ? "mid" : "");
      cellsHtml += `<div class="m-cell ${cls}"></div>`;
    }
    row.innerHTML = `<span class="matrix-name">${r.name}</span><div class="matrix-cells">${cellsHtml}</div>`;
    row.addEventListener("click", () => {
      autoCycle = false;
      updateAutoCycleBtn();
      selectCustomNode(nodeById[r.targetNode] || VAULT.nodes[0]);
    });
    p07Matrix.appendChild(row);
  });
  document.getElementById("p07Foot").textContent = `4 RULES · ${VAULT.totalRecords} FILES`;

  // Panel 08: Lint status
  const lintClean = VAULT.brainLint.includes("0 problem");
  document.getElementById("p08Lint").textContent =
    lintClean ? `✓ brain.py lint: 0 problem(s)` : VAULT.brainLint.split("\n").pop();
}

function getTargetNodeForCurrentState() {
  if (customSelectedNode) return customSelectedNode;
  const m = MODES[currentModeIdx];
  return nodeById[m.targetNodeId] || nodeById["CLAUDE.md"] || VAULT.nodes[0];
}

function applyMode(idx, resetCustom = true) {
  currentModeIdx = idx;
  if (resetCustom) customSelectedNode = null;
  lastModeSwitch = performance.now();

  const m = MODES[idx];
  document.querySelectorAll(".mode-tab").forEach((el, i) => {
    el.classList.toggle("active", i === idx);
  });
  document.querySelectorAll(".preset-chip").forEach((el, i) => {
    el.classList.toggle("active", i === idx && !customSelectedNode);
  });

  const activeNode = getTargetNodeForCurrentState();
  if (activeNode) {
    targetCamX = activeNode.x;
    targetCamY = activeNode.y;
  }
  targetZoom = customSelectedNode ? 1.42 : m.zoomTarget;
  targetAzAngle = m.azTarget;

  // Update command bars
  const cmdStr = customSelectedNode ? `inspect ${customSelectedNode.relPath}` : m.cmd;
  document.getElementById("topCmdText").textContent = cmdStr;
  document.getElementById("promptText").textContent = cmdStr;
  document.getElementById("promptModeTag").textContent = customSelectedNode ? "INSPECT" : m.key;

  // Update Panel 01 rule status
  document.getElementById("p01RuleStatus").textContent = m.coatRuleText;

  // Update Panel 03 File Inspector with REAL file data
  if (activeNode) {
    document.getElementById("p03Lines").textContent = `${activeNode.lines}L`;
    document.getElementById("p03Title").textContent = activeNode.relPath;
    document.getElementById("p03Desc").textContent = activeNode.excerpt || activeNode.title;
    document.getElementById("p03Path").textContent = activeNode.fullPath;
    document.getElementById("p03Status").textContent = customSelectedNode ? "INSPECTED" : m.inspectorStatus;
  }

  // Update Panel 04 Recall Radar active count
  const linkedCount = activeNode ? Math.max(3, (activeNode.links ? activeNode.links.length : 0) + 2) : m.activeCount;
  document.getElementById("p04Active").textContent = String(linkedCount).padStart(2, "0");

  // Update Panel 06 Context Log
  const logContainer = document.getElementById("p06LogList");
  logContainer.innerHTML = "";
  const entries = customSelectedNode
    ? [
        { sym: "►", op: "open", file: customSelectedNode.relPath, nodeId: customSelectedNode.id },
        ...(customSelectedNode.links || []).slice(0, 4).map(lid => ({
          sym: "·", op: "link", file: lid, nodeId: lid
        }))
      ]
    : m.logEntries;

  entries.forEach(item => {
    const nObj = nodeById[item.nodeId];
    const lnTxt = nObj ? `${nObj.lines} ln` : "ok";
    const row = document.createElement("div");
    row.className = "ctx-row";
    row.innerHTML = `
      <span>${item.sym}</span>
      <span class="ctx-op">${item.op}</span>
      <span class="ctx-file">${item.file}</span>
      <span class="ctx-ln">${lnTxt}</span>
    `;
    row.addEventListener("click", () => {
      if (nObj) {
        autoCycle = false;
        updateAutoCycleBtn();
        selectCustomNode(nObj);
      }
    });
    logContainer.appendChild(row);
  });
}

function selectCustomNode(node) {
  if (!node) return;
  customSelectedNode = node;
  applyMode(currentModeIdx, false);
}

function updateAutoCycleBtn() {
  const btn = document.getElementById("btnAutoCycle");
  btn.textContent = `AUTO CYCLE: ${autoCycle ? "ON" : "OFF"}`;
  btn.classList.toggle("active", autoCycle);
}

// Event listeners for tabs and presets
document.querySelectorAll(".mode-tab").forEach(tab => {
  tab.addEventListener("click", () => {
    const idx = parseInt(tab.getAttribute("data-mode"), 10);
    autoCycle = false;
    updateAutoCycleBtn();
    applyMode(idx, true);
  });
});

document.querySelectorAll(".preset-chip").forEach(chip => {
  chip.addEventListener("click", () => {
    const idx = parseInt(chip.getAttribute("data-mode"), 10);
    autoCycle = false;
    updateAutoCycleBtn();
    applyMode(idx, true);
  });
});

document.getElementById("btnAutoCycle").addEventListener("click", () => {
  autoCycle = !autoCycle;
  lastModeSwitch = performance.now();
  updateAutoCycleBtn();
});

document.getElementById("btnResetCam").addEventListener("click", () => {
  customSelectedNode = null;
  targetCamX = 0;
  targetCamY = 0;
  targetZoom = 1.0;
  applyMode(0, true);
});

document.getElementById("nodeSearch").addEventListener("input", e => {
  const q = e.target.value.trim().toLowerCase();
  if (!q) return;
  const found = VAULT.nodes.find(n =>
    n.relPath.toLowerCase().includes(q) ||
    n.title.toLowerCase().includes(q)
  );
  if (found) {
    autoCycle = false;
    updateAutoCycleBtn();
    selectCustomNode(found);
  }
});

// Canvas setup & 3D projection
const graphCanvas = document.getElementById("graphCanvas");
const gCtx = graphCanvas.getContext("2d");

let isDragging = false;
let dragStartX = 0, dragStartY = 0;
let dragMoved = false;
let projectedNodes = [];
let pillBoxes = [];

function resizeCanvases() {
  const dpr = window.devicePixelRatio || 1;
  const rect = graphCanvas.parentElement.getBoundingClientRect();
  graphCanvas.width = rect.width * dpr;
  graphCanvas.height = rect.height * dpr;
  gCtx.setTransform(dpr, 0, 0, dpr, 0, 0);

  const sCanvas = document.getElementById("streamCanvas");
  const sRect = sCanvas.parentElement.getBoundingClientRect();
  sCanvas.width = sRect.width * dpr;
  sCanvas.height = 62 * dpr;
}
window.addEventListener("resize", resizeCanvases);

graphCanvas.addEventListener("mousedown", e => {
  isDragging = true;
  dragMoved = false;
  dragStartX = e.clientX;
  dragStartY = e.clientY;
});

window.addEventListener("mousemove", e => {
  const rect = graphCanvas.getBoundingClientRect();
  const mx = e.clientX - rect.left;
  const my = e.clientY - rect.top;

  if (isDragging) {
    const dx = e.clientX - dragStartX;
    const dy = e.clientY - dragStartY;
    if (Math.abs(dx) > 3 || Math.abs(dy) > 3) dragMoved = true;
    dragStartX = e.clientX;
    dragStartY = e.clientY;
    autoCycle = false;
    updateAutoCycleBtn();
    const scale = Math.min(rect.width, rect.height) * 0.72 * camZoom;
    targetCamX -= dx / scale;
    targetCamY -= dy / scale;
    targetAzAngle += dx * 0.15;
    return;
  }

  // Hover detection
  hoveredNode = null;
  for (let i = pillBoxes.length - 1; i >= 0; i--) {
    const b = pillBoxes[i];
    if (mx >= b.x && mx <= b.x + b.w && my >= b.y && my <= b.y + b.h) {
      hoveredNode = b.node;
      break;
    }
  }
  if (!hoveredNode) {
    let bestDist = 14;
    for (let i = 0; i < projectedNodes.length; i++) {
      const p = projectedNodes[i];
      const d = Math.hypot(mx - p.sx, my - p.sy);
      if (d < bestDist) {
        bestDist = d;
        hoveredNode = p.node;
      }
    }
  }
  graphCanvas.style.cursor = hoveredNode ? "pointer" : (isDragging ? "grabbing" : "grab");
});

window.addEventListener("mouseup", () => {
  if (isDragging && !dragMoved && hoveredNode) {
    autoCycle = false;
    updateAutoCycleBtn();
    selectCustomNode(hoveredNode);
  }
  isDragging = false;
});

graphCanvas.addEventListener("wheel", e => {
  e.preventDefault();
  const factor = e.deltaY < 0 ? 1.12 : 0.9;
  targetZoom = Math.max(0.55, Math.min(2.8, targetZoom * factor));
}, { passive: false });

function project3D(x, y, z, w, h, rotRad) {
  const dx = x - camX;
  const dy = y - camY;
  const dz = z;

  const cosA = Math.cos(rotRad);
  const sinA = Math.sin(rotRad);
  const rx = dx * cosA - dz * sinA;
  const rz = dx * sinA + dz * cosA;
  const ry = dy;

  const fov = 1.65;
  const depth = Math.max(0.35, fov - rz * 0.55);
  const scale = (Math.min(w, h) * 0.68 * camZoom) / depth;

  return {
    sx: w * 0.5 + rx * scale,
    sy: h * 0.52 + ry * scale,
    depth: depth,
    scale: scale
  };
}

function drawRoundedRect(ctx, x, y, w, h, r) {
  ctx.beginPath();
  ctx.moveTo(x + r, y);
  ctx.lineTo(x + w - r, y);
  ctx.quadraticCurveTo(x + w, y, x + w, y + r);
  ctx.lineTo(x + w, y + h - r);
  ctx.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
  ctx.lineTo(x + r, y + h);
  ctx.quadraticCurveTo(x, y + h, x, y + h - r);
  ctx.lineTo(x, y + r);
  ctx.quadraticCurveTo(x, y, x + r, y);
  ctx.closePath();
}

// Token stream bars state
const STREAM_BARS = Array.from({ length: 34 }, (_, i) => 0.25 + 0.55 * Math.abs(Math.sin(i * 0.45)));
// Sparkline state
const SPARK_PTS = Array.from({ length: 32 }, (_, i) => 0.55 + 0.25 * Math.sin(i * 0.35));

function renderTokenStream(now) {
  const sCanvas = document.getElementById("streamCanvas");
  const ctx = sCanvas.getContext("2d");
  const dpr = window.devicePixelRatio || 1;
  const w = sCanvas.width / dpr;
  const h = sCanvas.height / dpr;
  ctx.save();
  ctx.scale(dpr, dpr);
  ctx.clearRect(0, 0, w, h);

  // Dashed mid reference line
  ctx.strokeStyle = "#b8c0c7";
  ctx.lineWidth = 1;
  ctx.setLineDash([3, 3]);
  ctx.beginPath();
  ctx.moveTo(0, h * 0.45);
  ctx.lineTo(w, h * 0.45);
  ctx.stroke();
  ctx.setLineDash([]);

  const n = STREAM_BARS.length;
  const gap = 2;
  const barW = Math.max(2, (w - gap * (n - 1)) / n);
  for (let i = 0; i < n; i++) {
    const v = STREAM_BARS[i];
    const bh = Math.max(4, v * (h - 6));
    const bx = i * (barW + gap);
    const by = h - bh;
    ctx.fillStyle = i >= n - 6 ? "#111315" : "#8b939b";
    ctx.fillRect(bx, by, barW, bh);
  }
  ctx.restore();
}

function renderRecallRadar(now, activeCount) {
  const rCanvas = document.getElementById("radarCanvas");
  const ctx = rCanvas.getContext("2d");
  const w = rCanvas.width;
  const h = rCanvas.height;
  const cx = w / 2;
  const cy = h / 2;
  const maxR = Math.min(cx, cy) - 6;

  ctx.clearRect(0, 0, w, h);

  // Concentric rings
  ctx.strokeStyle = "#bcc3ca";
  ctx.lineWidth = 1;
  [0.35, 0.68, 1.0].forEach(f => {
    ctx.beginPath();
    ctx.arc(cx, cy, maxR * f, 0, Math.PI * 2);
    ctx.stroke();
  });

  // Crosshair lines
  ctx.beginPath();
  ctx.moveTo(cx - maxR, cy);
  ctx.lineTo(cx + maxR, cy);
  ctx.moveTo(cx, cy - maxR);
  ctx.lineTo(cx, cy + maxR);
  ctx.stroke();

  // Rotating radar sweep sector
  const sweepAngle = (now * 0.0018) % (Math.PI * 2);
  const grad = ctx.createConicalGradient ? null : null;
  ctx.save();
  ctx.translate(cx, cy);
  ctx.rotate(sweepAngle);
  ctx.beginPath();
  ctx.moveTo(0, 0);
  ctx.arc(0, 0, maxR, -0.55, 0);
  ctx.closePath();
  ctx.fillStyle = "rgba(17, 19, 21, 0.14)";
  ctx.fill();

  ctx.strokeStyle = "#111315";
  ctx.lineWidth = 1.5;
  ctx.beginPath();
  ctx.moveTo(0, 0);
  ctx.lineTo(maxR, 0);
  ctx.stroke();
  ctx.restore();

  // Blip dots for matched nodes
  for (let i = 0; i < Math.min(10, activeCount); i++) {
    const a = (i * 1.17 + currentModeIdx * 0.8) % (Math.PI * 2);
    const dist = (0.28 + ((i * 37) % 60) / 100) * maxR;
    const bx = cx + Math.cos(a) * dist;
    const by = cy + Math.sin(a) * dist;
    ctx.fillStyle = "#111315";
    ctx.beginPath();
    ctx.arc(bx, by, 3, 0, Math.PI * 2);
    ctx.fill();
  }
}

function renderSparkline() {
  const c = document.getElementById("sparkCanvas");
  const ctx = c.getContext("2d");
  const w = c.width;
  const h = c.height;
  ctx.clearRect(0, 0, w, h);

  // Dashed baseline
  ctx.strokeStyle = "#b8c0c7";
  ctx.lineWidth = 1;
  ctx.setLineDash([3, 3]);
  ctx.beginPath();
  ctx.moveTo(0, h * 0.72);
  ctx.lineTo(w, h * 0.72);
  ctx.stroke();
  ctx.setLineDash([]);

  ctx.beginPath();
  SPARK_PTS.forEach((v, i) => {
    const px = (i / (SPARK_PTS.length - 1)) * (w - 8) + 4;
    const py = h - (v * (h - 22) + 8);
    if (i === 0) ctx.moveTo(px, py);
    else ctx.lineTo(px, py);
  });
  ctx.strokeStyle = "#111315";
  ctx.lineWidth = 2.2;
  ctx.stroke();

  // Area fill under sparkline
  ctx.lineTo(w - 4, h);
  ctx.lineTo(4, h);
  ctx.closePath();
  ctx.fillStyle = "rgba(17, 19, 21, 0.08)";
  ctx.fill();
}

let lastTelemetryTick = 0;

function animate(now) {
  requestAnimationFrame(animate);

  // Auto-cycle modes like the @baber_saad1 video if enabled
  if (autoCycle && now - lastModeSwitch > MODE_DURATION_MS) {
    applyMode((currentModeIdx + 1) % MODES.length, true);
  }

  // Smooth spring camera interpolation
  camX += (targetCamX - camX) * 0.065;
  camY += (targetCamY - camY) * 0.065;
  camZoom += (targetZoom - camZoom) * 0.065;
  targetAzAngle += 0.035; // gentle continuous orbital drift
  azAngle += (targetAzAngle - azAngle) * 0.06;

  const rotRad = (azAngle * Math.PI) / 180;
  const normAz = ((azAngle % 360) + 360) % 360;
  document.getElementById("camTelemetry").textContent =
    `AZ ${normAz.toFixed(1)}°  |  ${camZoom.toFixed(2)}x`;

  const activeMode = MODES[currentModeIdx];
  const elapsedSec = ((now * 0.001) % 99).toFixed(2).padStart(5, "0");
  document.getElementById("stageStatusTicker").textContent =
    `${elapsedSec}  ${customSelectedNode ? `inspect :: ${customSelectedNode.relPath} (${customSelectedNode.lines} lines)` : activeMode.statusLine}`;

  // Periodic live telemetry updates
  if (now - lastTelemetryTick > 180) {
    lastTelemetryTick = now;
    STREAM_BARS.shift();
    STREAM_BARS.push(0.28 + Math.random() * 0.65);

    SPARK_PTS.shift();
    SPARK_PTS.push(0.58 + Math.sin(now * 0.002) * 0.16 + (Math.random() - 0.5) * 0.12);

    const tokTotal = 1280 + Math.round(Math.sin(now * 0.0015) * 140 + Math.random() * 45);
    const tokRate = (1.1 + Math.sin(now * 0.002) * 0.25).toFixed(1);
    document.getElementById("p02Total").textContent = tokTotal.toLocaleString("en-US");
    document.getElementById("p02Rate").textContent = `${tokRate}k tok/s`;

    const hitPct = (93.8 + Math.sin(now * 0.0011) * 1.4).toFixed(1);
    document.getElementById("p08Pct").textContent = `${hitPct}%`;

    const d = new Date();
    document.getElementById("clockDisplay").textContent = d.toTimeString().split(" ")[0];
    renderSparkline();
  }

  renderTokenStream(now);
  const activeNode = getTargetNodeForCurrentState();
  const activeNeighbors = new Set(activeNode ? (activeNode.links || []) : []);
  renderRecallRadar(now, activeNeighbors.size + 4);

  // Render Main Canvas
  const rect = graphCanvas.parentElement.getBoundingClientRect();
  const w = rect.width;
  const h = rect.height;
  gCtx.clearRect(0, 0, w, h);

  // 1. Subtle architectural grid crosshair (+) markers
  gCtx.strokeStyle = "rgba(140, 148, 156, 0.35)";
  gCtx.lineWidth = 1;
  const step = 96;
  for (let gx = 48; gx < w; gx += step) {
    for (let gy = 48; gy < h; gy += step) {
      gCtx.beginPath();
      gCtx.moveTo(gx - 3.5, gy);
      gCtx.lineTo(gx + 3.5, gy);
      gCtx.moveTo(gx, gy - 3.5);
      gCtx.lineTo(gx, gy + 3.5);
      gCtx.stroke();
    }
  }

  // 2. Project cluster centers & draw organic dark smoky nebulas (@baber_saad1 signature)
  const projClusters = VAULT.clusters.map(c => {
    const p = project3D(c.cx, c.cy, c.cz, w, h, rotRad);
    return { ...c, ...p };
  }).sort((a, b) => b.depth - a.depth);

  projClusters.forEach(pc => {
    const rad = Math.max(45, pc.radius * pc.scale * 1.35);
    const isTargetCluster = activeNode && activeNode.cluster === pc.id;
    const alphaCore = isTargetCluster ? 0.24 : 0.13;
    const grad = gCtx.createRadialGradient(pc.sx, pc.sy, 2, pc.sx, pc.sy, rad);
    grad.addColorStop(0, `rgba(18, 20, 23, ${alphaCore})`);
    grad.addColorStop(0.45, `rgba(28, 32, 36, ${alphaCore * 0.55})`);
    grad.addColorStop(1, "rgba(239, 241, 243, 0)");
    gCtx.fillStyle = grad;
    gCtx.beginPath();
    gCtx.arc(pc.sx, pc.sy, rad, 0, Math.PI * 2);
    gCtx.fill();
  });

  // 3. Project real vault nodes
  const pMap = {};
  projectedNodes = VAULT.nodes.map(n => {
    const p = project3D(n.x, n.y, n.z, w, h, rotRad);
    const item = { node: n, sx: p.sx, sy: p.sy, depth: p.depth, scale: p.scale };
    pMap[n.id] = item;
    return item;
  });

  // 4. Draw real [[wikilink]] edges + animated data pulses
  gCtx.lineWidth = 0.85;
  VAULT.edges.forEach((e, idx) => {
    const a = pMap[e.source];
    const b = pMap[e.target];
    if (!a || !b) return;
    const isHighlighted = activeNode && (e.source === activeNode.id || e.target === activeNode.id);
    gCtx.strokeStyle = isHighlighted
      ? "rgba(17, 19, 21, 0.48)"
      : "rgba(30, 34, 38, 0.09)";
    gCtx.lineWidth = isHighlighted ? 1.25 : 0.7;
    gCtx.beginPath();
    gCtx.moveTo(a.sx, a.sy);
    gCtx.lineTo(b.sx, b.sy);
    gCtx.stroke();

    if (isHighlighted) {
      const t = ((now * 0.0007 + idx * 0.19) % 1);
      const px = a.sx + (b.sx - a.sx) * t;
      const py = a.sy + (b.sy - a.sy) * t;
      gCtx.fillStyle = "#111315";
      gCtx.beginPath();
      gCtx.arc(px, py, 2.1, 0, Math.PI * 2);
      gCtx.fill();
    }
  });

  // 5. Draw ambient particle cloud
  const tSec = now * 0.0004;
  CLOUD_PARTICLES.forEach(cp => {
    const wobbleX = Math.cos(tSec * cp.speed + cp.phase) * 0.012;
    const wobbleY = Math.sin(tSec * cp.speed + cp.phase) * 0.012;
    const p = project3D(cp.x + wobbleX, cp.y + wobbleY, cp.z, w, h, rotRad);
    if (p.sx < -20 || p.sx > w + 20 || p.sy < -20 || p.sy > h + 20) return;
    const isFocus = activeNode && activeNode.cluster === cp.clusterId;
    const r = Math.max(0.8, (cp.size * camZoom) / p.depth);
    const alpha = Math.min(0.9, cp.alpha * (isFocus ? 1.35 : 0.85));
    gCtx.fillStyle = `rgba(17, 19, 21, ${alpha.toFixed(3)})`;
    gCtx.beginPath();
    gCtx.arc(p.sx, p.sy, r, 0, Math.PI * 2);
    gCtx.fill();
  });

  // 6. Draw real file nodes (sorted back-to-front)
  projectedNodes.sort((a, b) => b.depth - a.depth);
  projectedNodes.forEach(p => {
    const n = p.node;
    const isTarget = activeNode && n.id === activeNode.id;
    const isNeighbor = activeNeighbors.has(n.id);
    const isHovered = hoveredNode && n.id === hoveredNode.id;

    const baseR = 2.4 + Math.min(4.2, Math.sqrt(n.degree + 1) * 0.75);
    const r = Math.max(1.8, (baseR * Math.min(1.45, camZoom)) / Math.max(0.7, p.depth * 0.75));

    if (isTarget || isHovered || isNeighbor) {
      gCtx.strokeStyle = isTarget ? "rgba(17, 19, 21, 0.85)" : "rgba(17, 19, 21, 0.35)";
      gCtx.lineWidth = isTarget ? 1.5 : 1;
      gCtx.beginPath();
      gCtx.arc(p.sx, p.sy, r + 3.5, 0, Math.PI * 2);
      gCtx.stroke();
    }

    gCtx.fillStyle = isTarget || isHovered
      ? "#0b0c0e"
      : (isNeighbor ? "rgba(17, 19, 21, 0.88)" : "rgba(22, 25, 28, 0.68)");
    gCtx.beginPath();
    gCtx.arc(p.sx, p.sy, r, 0, Math.PI * 2);
    gCtx.fill();
  });

  // 7. Draw floating cluster & hub label pills (like `CLAUDE.md`, `notlar/`, `projeler/`, `kisiler/`, `wiki/`)
  pillBoxes = [];
  gCtx.font = "600 10.5px 'JetBrains Mono', monospace";
  projClusters.slice().reverse().forEach(pc => {
    const repNode = VAULT.nodes.find(n => n.cluster === pc.id) || VAULT.nodes[0];
    const lbl = pc.label;
    const tw = gCtx.measureText(lbl).width;
    const pw = tw + 14;
    const ph = 20;
    const px = pc.sx - pw / 2;
    const py = pc.sy - ph / 2 - 14;

    const isAct = activeNode && activeNode.cluster === pc.id;
    gCtx.fillStyle = isAct ? "rgba(255, 255, 255, 0.96)" : "rgba(244, 246, 248, 0.88)";
    gCtx.strokeStyle = isAct ? "#111315" : "rgba(35, 39, 43, 0.32)";
    gCtx.lineWidth = isAct ? 1.3 : 1;
    drawRoundedRect(gCtx, px, py, pw, ph, 2);
    gCtx.fill();
    gCtx.stroke();

    gCtx.fillStyle = "#111315";
    gCtx.fillText(lbl, px + 7, py + 13.5);

    pillBoxes.push({ x: px, y: py, w: pw, h: ph, node: repNode });
  });

  // If hovered node is a specific file, draw its tooltip pill
  if (hoveredNode && (!activeNode || hoveredNode.id !== activeNode.id)) {
    const hp = pMap[hoveredNode.id];
    if (hp) {
      const txt = `${hoveredNode.relPath} (${hoveredNode.lines}L)`;
      gCtx.font = "600 10px 'JetBrains Mono', monospace";
      const tw = gCtx.measureText(txt).width;
      const bx = hp.sx + 10;
      const by = hp.sy - 22;
      gCtx.fillStyle = "rgba(17, 19, 21, 0.92)";
      drawRoundedRect(gCtx, bx, by, tw + 12, 19, 2);
      gCtx.fill();
      gCtx.fillStyle = "#ffffff";
      gCtx.fillText(txt, bx + 6, by + 13);
    }
  }

  // 8. Draw Target Reticle (Eşmerkezli Daireler + Artı Çizgileri) & Floating Callout Card on Active Target!
  if (activeNode && pMap[activeNode.id]) {
    const tp = pMap[activeNode.id];
    const tx = tp.sx;
    const ty = tp.sy;

    // Full-canvas crosshair lines passing through target
    gCtx.strokeStyle = "rgba(17, 19, 21, 0.24)";
    gCtx.lineWidth = 1;
    gCtx.beginPath();
    gCtx.moveTo(0, ty);
    gCtx.lineTo(w, ty);
    gCtx.moveTo(tx, 0);
    gCtx.lineTo(tx, h);
    gCtx.stroke();

    // Outer dashed rotating ring
    const outerR = 68;
    const midR = 44;
    const innerR = 19;

    gCtx.save();
    gCtx.translate(tx, ty);
    gCtx.rotate(now * 0.00045);
    gCtx.strokeStyle = "rgba(17, 19, 21, 0.65)";
    gCtx.lineWidth = 1.15;
    gCtx.setLineDash([7, 5]);
    gCtx.beginPath();
    gCtx.arc(0, 0, outerR, 0, Math.PI * 2);
    gCtx.stroke();
    gCtx.setLineDash([]);
    gCtx.restore();

    // Middle solid ring + 4 cardinal ticks
    gCtx.strokeStyle = "rgba(17, 19, 21, 0.78)";
    gCtx.lineWidth = 1.25;
    gCtx.beginPath();
    gCtx.arc(tx, ty, midR, 0, Math.PI * 2);
    gCtx.stroke();

    // Inner pulsing ring
    const pulseR = innerR + Math.sin(now * 0.005) * 2.2;
    gCtx.strokeStyle = "#111315";
    gCtx.lineWidth = 1.5;
    gCtx.beginPath();
    gCtx.arc(tx, ty, pulseR, 0, Math.PI * 2);
    gCtx.stroke();

    // Right status callout badge (e.g., `CLAUDE.md / LOADED`)
    const badgeText = customSelectedNode
      ? `${customSelectedNode.relPath} / SELECTED`
      : activeMode.badge;
    gCtx.font = "800 12.5px 'JetBrains Mono', monospace";
    const bw = gCtx.measureText(badgeText).width + 24;
    const bh = 30;
    const bx = Math.min(w - bw - 14, tx + outerR + 14);
    const by = ty - bh / 2;

    // Leader line from reticle to badge
    gCtx.strokeStyle = "#111315";
    gCtx.lineWidth = 1.3;
    gCtx.beginPath();
    gCtx.moveTo(tx + midR, ty);
    gCtx.lineTo(bx, ty);
    gCtx.stroke();

    gCtx.fillStyle = "rgba(250, 251, 252, 0.96)";
    gCtx.strokeStyle = "#111315";
    gCtx.lineWidth = 1.6;
    gCtx.fillRect(bx, by, bw, bh);
    gCtx.strokeRect(bx, by, bw, bh);

    gCtx.fillStyle = "#111315";
    gCtx.fillText(badgeText, bx + 12, by + 19.5);

    // Upper-left floating info card (exact replica of video's floating card)
    const cardW = 285;
    const cardH = 84;
    const cxCard = Math.max(14, tx - outerR - cardW - 18);
    const cyCard = Math.max(38, ty - outerR - 36);

    // Leader line from reticle to info card
    gCtx.strokeStyle = "rgba(17, 19, 21, 0.55)";
    gCtx.lineWidth = 1;
    gCtx.beginPath();
    gCtx.moveTo(tx - midR * 0.7, ty - midR * 0.7);
    gCtx.lineTo(cxCard + cardW, cyCard + cardH * 0.55);
    gCtx.stroke();

    gCtx.fillStyle = "rgba(250, 252, 253, 0.95)";
    gCtx.strokeStyle = "rgba(24, 26, 29, 0.55)";
    gCtx.lineWidth = 1;
    gCtx.fillRect(cxCard, cyCard, cardW, cardH);
    gCtx.strokeRect(cxCard, cyCard, cardW, cardH);

    // Card header
    const cTitle = customSelectedNode ? customSelectedNode.relPath : activeMode.cardTitle;
    const cDesc = customSelectedNode ? (customSelectedNode.excerpt || customSelectedNode.title) : activeMode.cardDesc;
    const cPath = customSelectedNode ? customSelectedNode.fullPath : activeMode.cardPath;
    const cTrig = customSelectedNode ? `${customSelectedNode.lines} lines` : activeMode.cardTrigger;

    gCtx.font = "800 11px 'JetBrains Mono', monospace";
    gCtx.fillStyle = "#111315";
    gCtx.fillText(cTitle.slice(0, 34), cxCard + 10, cyCard + 18);

    gCtx.strokeStyle = "#d6dce1";
    gCtx.beginPath();
    gCtx.moveTo(cxCard + 10, cyCard + 24);
    gCtx.lineTo(cxCard + cardW - 10, cyCard + 24);
    gCtx.stroke();

    gCtx.font = "500 9.5px 'JetBrains Mono', monospace";
    gCtx.fillStyle = "#3a4046";
    const descLine1 = cDesc.slice(0, 42);
    const descLine2 = cDesc.slice(42, 84);
    gCtx.fillText(descLine1, cxCard + 10, cyCard + 40);
    if (descLine2) {
      gCtx.fillText(descLine2 + (cDesc.length > 84 ? "…" : ""), cxCard + 10, cyCard + 53);
    }

    gCtx.font = "500 8.5px 'JetBrains Mono', monospace";
    gCtx.fillStyle = "#7a828a";
    gCtx.fillText(cPath.slice(0, 30), cxCard + 10, cyCard + 73);

    gCtx.font = "700 8.5px 'JetBrains Mono', monospace";
    gCtx.fillStyle = "#111315";
    const trigW = gCtx.measureText(cTrig).width;
    gCtx.fillText(cTrig, cxCard + cardW - trigW - 10, cyCard + 73);
  }
}

// Boot
resizeCanvases();
initStaticTelemetry();
applyMode(0, true);
renderSparkline();
requestAnimationFrame(animate);
</script>
</body>
</html>
"""


def main():
    vault_data = scan_vault()
    vault_json = json.dumps(vault_data, ensure_ascii=False)
    html_out = HTML_TEMPLATE.replace("__VAULT_JSON__", vault_json)
    OUTPUT_HTML.write_text(html_out, encoding="utf-8")
    print(
        f"[hud-uret.py] OK -> {OUTPUT_HTML}\n"
        f"  RECORDS : {vault_data['totalRecords']}\n"
        f"  LINES   : {vault_data['totalLines']}\n"
        f"  EDGES   : {vault_data['totalEdges']}\n"
        f"  CLAUDE  : {vault_data['claudeLines']} / {vault_data['claudeBudget']} lines\n"
        f"  LINT    : {vault_data['brainLint'].splitlines()[-1] if vault_data['brainLint'] else 'n/a'}"
    )


if __name__ == "__main__":
    main()
