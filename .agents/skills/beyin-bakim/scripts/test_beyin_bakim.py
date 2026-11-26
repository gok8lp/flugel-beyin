import importlib.machinery, importlib.util, os, tempfile, unittest
from datetime import date
from pathlib import Path

HERE = Path(__file__).parent
loader = importlib.machinery.SourceFileLoader("bakim", str(HERE / "beyin-bakim"))
bakim = importlib.util.module_from_spec(importlib.util.spec_from_loader("bakim", loader))
loader.exec_module(bakim)

BUGUN = date(2026, 11, 27)
THREADS = """# Threads

## Active Threads
### Eski konu
- Durum (2026-10-01): bir şey. Sonra 2026-10-05 notu.
- gizli ayrıntı satırı

### Yeni konu
- Durum (2026-11-25): güncel.
"""


def task(title, status, extra=""):
    return f'---\n{{\n  "title": "{title}",\n  "status": "{status}"{extra}\n}}\n---\ngövde\n'


class BakimTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.v = Path(self.tmp.name) / "vault"
        (self.v / "🔮 850-Companion").mkdir(parents=True)
        (self.v / "tasks").mkdir()
        (self.v / "knowledge").mkdir()
        (self.v / "🔮 850-Companion/Threads.md").write_text(THREADS)
        self.rap = Path(self.tmp.name) / "raporlar"
        self.rap.mkdir()
        os.environ["BEYIN_BAKIM_BEYIN_PY"] = ""

    def tearDown(self):
        self.tmp.cleanup()

    def test_bayat_thread_tek_soru_basliktan_ibaret(self):
        sorular = bakim.stale_threads(self.v, BUGUN)
        self.assertEqual(len(sorular), 1)
        self.assertIn("Eski konu: en son 2026-10-05 güncellendi.", sorular[0])
        self.assertNotIn("gizli", sorular[0])

    def test_bayat_gorev_yalniz_acik_ve_eski(self):
        eski = BUGUN.toordinal() - 20
        for ad, durum in [("a", "active"), ("b", "done")]:
            p = self.v / "tasks" / f"{ad}.md"
            p.write_text(task(f"Görev {ad}", durum))
            t = date.fromordinal(eski)
            os.utime(p, (
                __import__("time").mktime(t.timetuple()),) * 2)
        (self.v / "tasks/c.md").write_text(task("Görev c", "active"))
        sorular = bakim.stale_tasks(self.v, BUGUN)
        self.assertEqual(sorular, ["Görev a: hâlâ geçerli mi, bitti mi?"])

    def test_indekslenmemis_rapor(self):
        (self.rap / "var.md").write_text("x")
        (self.rap / "yok.md").write_text("x")
        (self.v / "knowledge/ai-workplace-raporlar.md").write_text("`raporlar/var.md`")
        self.assertEqual(bakim.unindexed(self.rap, self.v), ["yok.md"])

    def test_lint_yanlis_alarm_ayrilir(self):
        (self.v / "receipts").mkdir()
        (self.v / "receipts/x.md").write_text("r")
        lint = {"orphan_count": 2, "broken_links_count": 2, "broken_links": [
            {"source": "a.md", "target": "receipts/x.md"},
            {"source": "b.md", "target": "yok/y.md"}]}
        gercek, yanlis = bakim.split_broken(self.v, lint)
        self.assertEqual((len(gercek), yanlis), (1, 1))

    def test_beyin_py_yoksa_okunamadi_ve_cikti(self):
        md, nq, nw = bakim.build(self.v, BUGUN, self.rap)
        self.assertEqual(nq, 1)
        self.assertIn("okunamadı", md)
        self.assertIn("tur: beyin-bakim", md)
        self.assertIn("## Gökalp'e sorular", md)

    def test_soru_yoksa_soru_yok(self):
        (self.v / "🔮 850-Companion/Threads.md").write_text("### Yeni\n2026-11-26\n")
        md, nq, _ = bakim.build(self.v, BUGUN, self.rap)
        self.assertEqual(nq, 0)
        self.assertIn("Soru yok", md)


if __name__ == "__main__":
    unittest.main()
