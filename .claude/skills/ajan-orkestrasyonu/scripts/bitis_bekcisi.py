#!/usr/bin/env python3
"""Bitiş bekçisi: dosya değişti ama ikinci beyne receipt yok ise oturumu bir kez geri çevirir.

Codex ve Gemini/Antigravity Stop hook'u olarak çalışır. Hata olursa izin verir.
"""
import argparse
import json
import os
import re
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

VARSAYILAN_KOKLER = "/home/gokalp/Documents/ai_workplace:/home/gokalp/Projects"
VARSAYILAN_DB = "~/.local/state/beyin-v3/00de12d3aee6e8f1/memory.sqlite3"
ATLANAN = {".git", "node_modules", "build", ".gradle", "__pycache__", ".venv"}
EN_COK_DOSYA, EN_COK_SANIYE, KAC_YOL = 20000, 2.0, 5
YONERGE = "/home/gokalp/Documents/ai_workplace/YENI-AJAN.md"
BEYIN = "/home/gokalp/Documents/ai_workplace/flugel-beyin"


def alan(veri, *adlar):
    for ad in adlar:
        if veri.get(ad):
            return veri[ad]
    return None


def olay_adi(veri):
    return alan(veri, "hook_event_name", "hookEventName")


def oturum_kimligi(veri):
    ham = str(alan(veri, "session_id", "conversationId") or "bilinmeyen")
    return re.sub(r"[^A-Za-z0-9_.-]", "_", ham)


def calisma_klasoru(veri):
    cwd = alan(veri, "cwd")
    yollar = veri.get("workspacePaths") or []
    return cwd or (yollar[0] if yollar else None)


def dongu_mu(veri):
    return bool(alan(veri, "stop_hook_active", "continuationActive"))


def durum_dosyasi(oturum):
    return Path.home() / ".local/state/bitis-bekcisi" / f"{oturum}.json"


def durum_oku(oturum):
    try:
        return json.loads(durum_dosyasi(oturum).read_text())
    except (OSError, ValueError):
        return None


def durum_yaz(oturum, durum):
    dosya = durum_dosyasi(oturum)
    dosya.parent.mkdir(parents=True, exist_ok=True)
    dosya.write_text(json.dumps(durum))


def kokler():
    ham = os.environ.get("BITIS_KOKLER", VARSAYILAN_KOKLER)
    return [Path(k).resolve() for k in ham.split(":") if k]


def kok_icinde_mi(cwd):
    yol = Path(cwd).resolve()
    return any(yol == k or k in yol.parents for k in kokler())


def degisenler(cwd, baslangic):
    bulunan, sayac = [], 0
    son = time.monotonic() + EN_COK_SANIYE
    for dizin, altlar, dosyalar in os.walk(cwd):
        altlar[:] = [a for a in altlar if a not in ATLANAN]
        for ad in dosyalar:
            sayac += 1
            if sayac > EN_COK_DOSYA or time.monotonic() > son:
                return bulunan
            yol = os.path.join(dizin, ad)
            if mtime(yol) > baslangic and len(bulunan) < KAC_YOL:
                bulunan.append(yol)
    return bulunan


def mtime(yol):
    try:
        return os.lstat(yol).st_mtime
    except OSError:
        return 0.0


def zaman_damgasi(iso):
    zaman = datetime.fromisoformat(iso)
    if zaman.tzinfo is None:
        zaman = zaman.replace(tzinfo=timezone.utc)
    return zaman.timestamp()


def receipt_var_mi(baslangic):
    """DB yoksa ya da hata varsa True döner (fail open)."""
    yol = Path(os.environ.get("BITIS_DB", VARSAYILAN_DB)).expanduser()
    if not yol.exists():
        return True
    try:
        con = sqlite3.connect(f"file:{yol}?mode=ro", uri=True)
        try:
            satirlar = con.execute("SELECT payload FROM receipts").fetchall()
        finally:
            con.close()
        return any(yeni_receipt(s[0], baslangic) for s in satirlar)
    except Exception:
        return True


def yeni_receipt(payload, baslangic):
    try:
        return zaman_damgasi(json.loads(payload)["created_at"]) >= baslangic
    except Exception:
        return False


def hatirlatma(harness, oturum, yollar):
    return (
        f"Bitiş bekçisi: bu oturumda dosyalar değişti ({', '.join(yollar)}) ama ikinci beyne kayıt yok. "
        f"{YONERGE} 'Bitiş' adımlarını uygula (anlamlı işse rapor + knowledge/ai-workplace-raporlar.md "
        "satırı + Threads + Last-Session kartı) ve en son receipt yaz: "
        f"python3 {BEYIN}/beyin.py --vault {BEYIN} receipt --harness {harness} "
        f"--session {oturum[:24]} --event-id <kisa-ad> --summary \"<ne yapıldı>\" "
        "--ref knowledge/ai-workplace-raporlar.md. Test/deneme dosyasıysa ya da sandbox yazmaya "
        "izin vermiyorsa bunu tek cümleyle söyle ve bitir."
    )


def izin(harness):
    return {} if harness == "codex" else {"decision": "stop"}


def engel(harness, neden):
    karar = "block" if harness == "codex" else "continue"
    return {"decision": karar, "reason": neden}


def oturum_basladi(veri, oturum):
    if durum_oku(oturum) is None:
        durum_yaz(oturum, {"start": time.time(), "cwd": calisma_klasoru(veri)})


def durdurulabilir_mi(veri, durum):
    """Engellenecekse değişen yolları, değilse None döner."""
    if dongu_mu(veri) or durum is None or durum.get("hatirlatildi"):
        return None
    cwd = calisma_klasoru(veri) or durum.get("cwd")
    if not cwd or not kok_icinde_mi(cwd):
        return None
    yollar = degisenler(cwd, durum["start"])
    if not yollar or receipt_var_mi(durum["start"]):
        return None
    return yollar


def durdur(veri, harness, oturum):
    durum = durum_oku(oturum)
    yollar = durdurulabilir_mi(veri, durum)
    if not yollar:
        return izin(harness)
    durum["hatirlatildi"] = True
    durum_yaz(oturum, durum)
    return engel(harness, hatirlatma(harness, oturum, yollar))


def isle(harness):
    try:
        veri = json.loads(sys.stdin.read())
        oturum = oturum_kimligi(veri)
        if olay_adi(veri) == "SessionStart":
            oturum_basladi(veri, oturum)
        elif olay_adi(veri) == "Stop":
            return durdur(veri, harness, oturum)
    except Exception:
        pass
    return izin(harness)


def main():
    kur = argparse.ArgumentParser()
    kur.add_argument("--harness", choices=["codex", "antigravity"], required=True)
    harness = kur.parse_args().harness
    print(json.dumps(isle(harness), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
