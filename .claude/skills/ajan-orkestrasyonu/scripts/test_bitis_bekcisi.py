"""bitis_bekcisi.py testleri: geçici HOME/durum/DB ile subprocess üzerinden."""
import json
import os
import sqlite3
import subprocess
import sys
import tempfile
import time
import unittest
from datetime import datetime, timezone
from pathlib import Path

BEKCI = Path(__file__).with_name("bitis_bekcisi.py")


class Ortam:
    def __init__(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.kok = self.tmp / "kok"
        self.proje = self.kok / "proje"
        self.proje.mkdir(parents=True)
        self.db = self.tmp / "memory.sqlite3"
        con = sqlite3.connect(self.db)
        con.execute("CREATE TABLE receipts (payload TEXT)")
        con.commit()
        con.close()

    def calistir(self, harness, girdi, ham=False):
        env = dict(os.environ, HOME=str(self.tmp), BITIS_DB=str(self.db),
                   BITIS_KOKLER=str(self.kok))
        veri = girdi if ham else json.dumps(girdi)
        sonuc = subprocess.run(
            [sys.executable, str(BEKCI), "--harness", harness],
            input=veri, capture_output=True, text=True, env=env, timeout=20)
        self.kod = sonuc.returncode
        return json.loads(sonuc.stdout)

    def durum_dosyasi(self, oturum):
        return self.tmp / ".local/state/bitis-bekcisi" / f"{oturum}.json"

    def receipt_yaz(self):
        con = sqlite3.connect(self.db)
        simdi = datetime.now(timezone.utc).isoformat()
        con.execute("INSERT INTO receipts VALUES (?)",
                    (json.dumps({"created_at": simdi}),))
        con.commit()
        con.close()


def codex(olay, cwd, **ek):
    return dict({"hook_event_name": olay, "session_id": "s1", "cwd": str(cwd)}, **ek)


def agy(olay, cwd, **ek):
    return dict({"hookEventName": olay, "conversationId": "c1", "cwd": str(cwd)}, **ek)


class BitisBekcisiTest(unittest.TestCase):
    def setUp(self):
        self.o = Ortam()

    def basla_ve_degistir(self, olusturucu, harness):
        self.o.calistir(harness, olusturucu("SessionStart", self.o.proje))
        time.sleep(0.05)
        (self.o.proje / "yeni.txt").write_text("x")

    def test_session_start_isaret_yazar(self):
        cikti = self.o.calistir("codex", codex("SessionStart", self.o.proje))
        self.assertEqual(cikti, {})
        veri = json.loads(self.o.durum_dosyasi("s1").read_text())
        self.assertEqual(veri["cwd"], str(self.o.proje))
        self.assertIn("start", veri)

    def test_degisiklik_yoksa_izin(self):
        self.o.calistir("codex", codex("SessionStart", self.o.proje))
        self.assertEqual(self.o.calistir("codex", codex("Stop", self.o.proje)), {})

    def test_codex_receiptsiz_degisiklik_engellenir(self):
        self.basla_ve_degistir(codex, "codex")
        cikti = self.o.calistir("codex", codex("Stop", self.o.proje))
        self.assertEqual(cikti["decision"], "block")
        self.assertIn("yeni.txt", cikti["reason"])

    def test_agy_receiptsiz_degisiklik_continue(self):
        self.basla_ve_degistir(agy, "antigravity")
        cikti = self.o.calistir("antigravity", agy("Stop", self.o.proje))
        self.assertEqual(cikti["decision"], "continue")

    def test_agy_workspacepaths_yedegi(self):
        girdi = {"hookEventName": "SessionStart", "conversationId": "c2",
                 "workspacePaths": [str(self.o.proje)]}
        self.o.calistir("antigravity", girdi)
        veri = json.loads(self.o.durum_dosyasi("c2").read_text())
        self.assertEqual(veri["cwd"], str(self.o.proje))

    def test_ikinci_stop_izin_verir(self):
        self.basla_ve_degistir(codex, "codex")
        self.o.calistir("codex", codex("Stop", self.o.proje))
        self.assertEqual(self.o.calistir("codex", codex("Stop", self.o.proje)), {})

    def test_dongu_bayragi_izin_verir(self):
        self.basla_ve_degistir(codex, "codex")
        girdi = codex("Stop", self.o.proje, stop_hook_active=True)
        self.assertEqual(self.o.calistir("codex", girdi), {})

    def test_agy_izin_ciktisi_stop(self):
        self.o.calistir("antigravity", agy("SessionStart", self.o.proje))
        cikti = self.o.calistir("antigravity", agy("Stop", self.o.proje))
        self.assertEqual(cikti, {"decision": "stop"})

    def test_receipt_sonrasi_izin(self):
        self.basla_ve_degistir(codex, "codex")
        self.o.receipt_yaz()
        self.assertEqual(self.o.calistir("codex", codex("Stop", self.o.proje)), {})

    def test_kok_disi_cwd_izin(self):
        disari = self.o.tmp / "disari"
        disari.mkdir()
        self.o.calistir("codex", codex("SessionStart", disari))
        time.sleep(0.05)
        (disari / "a.txt").write_text("x")
        self.assertEqual(self.o.calistir("codex", codex("Stop", disari)), {})

    def test_bozuk_json_izin(self):
        self.assertEqual(self.o.calistir("codex", "{bozuk", ham=True), {})
        self.assertEqual(self.o.kod, 0)
        self.assertEqual(self.o.calistir("antigravity", "", ham=True),
                         {"decision": "stop"})


if __name__ == "__main__":
    unittest.main()
