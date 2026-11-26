#!/usr/bin/env python3
"""Lider bekcisi (Claude Code hook'u), 2026-11-26.

Sorun: "Sen ana ajansin, alttakilere is ver" denen Claude bir iki is dagittiktan sonra
kendisi kod yazmaya basliyor. Bu hook o kaymayi mekanik olarak durdurur.

- UserPromptSubmit: istemde lider ifadesi gecerse bu oturum icin lider modunu acar;
  "lider modu kapat" gecerse kapatir.
- PreToolUse (Edit|Write|NotebookEdit): lider modundaki ANA ajan izinli yerler disinda
  dosya duzenlerse engeller. Alt ajanlar (girdide agent_id olan cagrilar) serbesttir.
Izinli yerler: raporlar, planlar, beyin companion/tasks/knowledge, Claude bellegi, gecici klasorler.
"""
import json
import os
import re
import sys
import time

DURUM = os.path.expanduser("~/.local/state/lider-bekci")
SURE = 12 * 3600
AC = re.compile(r"(ana ajans[ıi]n|lider(\s+modu)?\s*(ol|sen|ac|aç)|sen\s+lider|alt(taki)?(lere|\s+ajanlara)\s+(i[sş]|g[öo]rev)\s+ver|orkestre\s+et|ekip\s+lideri)", re.I)
KAPAT = re.compile(r"lider\s+modu(nu)?\s+kapat", re.I)
IZINLI = [
    "/second-brain/raporlar/", "/second-brain/planlar/", "/.claude/projects/", "/tmp/",
    "/flugel-beyin/🔮 850-Companion/", "/flugel-beyin/tasks/", "/flugel-beyin/knowledge/",
    "/flugel-beyin/receipts/", "/plans/", "/scratchpad/",
]
LOG = os.path.join(DURUM, "olaylar.log")


def bayrak(oturum):
    return os.path.join(DURUM, re.sub(r"[^A-Za-z0-9_-]", "", oturum or "yok") + ".acik")


def kaydet(metin):
    os.makedirs(DURUM, exist_ok=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(time.strftime("%F %T ") + metin + "\n")


def istem(girdi):
    metin, yol = girdi.get("prompt") or "", bayrak(girdi.get("session_id"))
    if KAPAT.search(metin):
        if os.path.exists(yol):
            os.remove(yol)
        kaydet(f"kapandi {girdi.get('session_id')}")
    elif AC.search(metin):
        os.makedirs(DURUM, exist_ok=True)
        open(yol, "w").close()
        kaydet(f"acildi {girdi.get('session_id')}")
        print("LİDER MODU AÇIK: Kod/dosya düzenleme işlerini alt ajanlara ver (ajan-orkestrasyonu). "
              "Ana ajan yalnız plan, rapor ve beyin notu yazar; düzenleme denemesi engellenir.")
    return 0


def acik_mi(oturum):
    yol = bayrak(oturum)
    return os.path.exists(yol) and time.time() - os.path.getmtime(yol) < SURE


def arac(girdi):
    if girdi.get("agent_id") or not acik_mi(girdi.get("session_id")):
        return 0
    ti = girdi.get("tool_input") or {}
    yol = ti.get("file_path") or ti.get("notebook_path") or ""
    if any(p in yol for p in IZINLI):
        return 0
    kaydet(f"engellendi {girdi.get('session_id')} {girdi.get('tool_name')} {yol}")
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": "deny",
        "permissionDecisionReason": (
            f"Lider modu açık: '{yol}' dosyasını ana ajan düzenleyemez. Bu işi bir lane kartıyla alt ajana ver "
            "(Agent aracı, codex exec ya da agy; model için önce `ai-limitler --sec <tur>`). "
            "Kullanıcı açıkça 'lider modu kapat' derse kapanır.")}}, ensure_ascii=False))
    return 0


def main():
    try:
        girdi = json.load(sys.stdin)
    except ValueError:
        return 0
    if "--test-kayit" in sys.argv:
        kaydet("girdi " + json.dumps({k: girdi.get(k) for k in ("hook_event_name", "session_id", "agent_id", "agent_type", "tool_name")}))
    olay = girdi.get("hook_event_name")
    if olay == "UserPromptSubmit":
        return istem(girdi)
    if olay == "PreToolUse":
        return arac(girdi)
    return 0


if __name__ == "__main__":
    sys.exit(main())
