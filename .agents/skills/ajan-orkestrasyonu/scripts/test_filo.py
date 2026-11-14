#!/usr/bin/env python3
"""Gerçek CLI ve süreçlerle stdlib regresyon testleri: python3 scripts/test_filo.py."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest

SCRIPT = Path(__file__).with_name('filo.py').resolve()


class FiloTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='filo-test-')
        self.directory = Path(self.temp.name)

    def tearDown(self):
        # Başarısız test dahi arka planda sleep bırakmasın.
        for path in self.directory.glob('*.json'):
            if not path.name.startswith('.'):
                try:
                    record = json.loads(path.read_text())
                    if record['state'] != 'finished':
                        self.cli('durdur', '--ad', record['name'], check=False)
                except (OSError, ValueError):
                    pass
        self.temp.cleanup()

    def cli(self, action, *args, check=True):
        result = subprocess.run([sys.executable, str(SCRIPT), action,
                                 '--log-dizini', str(self.directory), *args],
                                capture_output=True, text=True, timeout=12)
        if check:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def start(self, name, seconds, *command):
        return self.cli('baslat', '--ad', name, '--zaman-asimi', str(seconds),
                        '--', *command)

    def record(self, name):
        return json.loads((self.directory / (name + '.json')).read_text())

    def test_baslat_durum_bekle_echo_sleep(self):
        self.start('uyku', 5, 'sleep', '0.5')
        initial = self.record('uyku')
        self.assertIsInstance(initial['pid'], int)
        self.assertTrue(initial['started_at'])
        self.assertEqual(initial['timeout_seconds'], 5)
        self.assertIn('çalışıyor', self.cli('durum').stdout)
        self.start('mesaj', 5, 'echo', 'merhaba filo')
        self.assertIn('bitti(rc=0)', self.cli('bekle').stdout)
        self.assertEqual(self.record('uyku')['rc'], 0)
        self.assertEqual((self.directory / 'mesaj.log').read_text(), 'merhaba filo\n')

    def test_zaman_asimi_ve_surec_sonlanmasi(self):
        self.start('sure', 0.3, 'sleep', '30')
        result = self.cli('bekle', check=False)
        self.assertEqual(result.returncode, 1)
        self.assertIn('zaman aşımı', result.stdout)
        record = self.record('sure')
        self.assertEqual(record['rc'], 124)
        self.assertFalse(Path('/proc', str(record['pid'])).exists())
        self.assertIn('zaman aşımı', self.cli('durum').stdout)

    def test_durdur_ve_tekrar_durdur(self):
        self.start('iptal', 30, 'sleep', '30')
        self.assertIn('durduruldu', self.cli('durdur', '--ad', 'iptal').stdout)
        self.assertEqual(self.record('iptal')['rc'], 143)
        self.cli('durdur', '--ad', 'iptal')
        self.assertEqual(self.record('iptal')['rc'], 143)
        self.assertEqual(self.cli('bekle', check=False).returncode, 1)

    def test_takilma_suphesi_otomatik_durdurmaz(self):
        self.start('sessiz', 30, 'sleep', '30')
        past = time.time() - 180
        os.utime(self.directory / 'sessiz.log', (past, past))
        self.assertIn('takıldı (log 3.', self.cli('durum', '--takilma-dakika', '1').stdout)
        self.assertIn('çalışıyor', self.cli('durum').stdout)  # varsayılan 10 dakika
        self.assertEqual(self.record('sessiz')['state'], 'running')

    def test_rc_korunur_ve_stdin_devnull(self):
        self.start('hata', 5, sys.executable, '-c',
                   "import sys; print(repr(sys.stdin.read())); sys.exit(7)")
        self.assertEqual(self.cli('bekle', check=False).returncode, 1)
        self.assertEqual(self.record('hata')['rc'], 7)
        self.cli('durdur', '--ad', 'hata')
        self.assertEqual(self.record('hata')['rc'], 7)
        self.assertEqual((self.directory / 'hata.log').read_text(), "''\n")

    def test_hizli_bitis_timeout_olmaz(self):
        self.start('hizli', 2, 'echo', 'bitti')
        self.cli('bekle')
        self.cli('durdur', '--ad', 'hizli')
        self.assertEqual(self.record('hizli')['rc'], 0)

    def test_term_direnci_kill_ile_sonlanir(self):
        self.start('direnc', 0.5, sys.executable, '-c',
                   'import signal,time; signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(30)')
        self.assertEqual(self.cli('bekle', check=False).returncode, 1)
        self.assertEqual(self.record('direnc')['rc'], 124)
        self.assertFalse(Path('/proc', str(self.record('direnc')['pid'])).exists())

    def test_timeout_bekle_olmadan_alt_surecleri_durdurur(self):
        code = ("import subprocess,signal,sys,time; "
                "child=subprocess.Popen(['sleep','30']); "
                "signal.signal(signal.SIGTERM, lambda *args: (child.wait(), sys.exit(0))); "
                "print(child.pid, flush=True); time.sleep(30)")
        self.start('agac', 0.5, sys.executable, '-c', code)
        deadline = time.monotonic() + 8
        while self.record('agac')['state'] != 'finished' and time.monotonic() < deadline:
            time.sleep(0.05)
        self.assertEqual(self.record('agac')['rc'], 124)
        child_pid = int((self.directory / 'agac.log').read_text().strip())
        self.assertFalse(Path('/proc', str(child_pid)).exists())

    def test_gecersiz_cagri_ve_mevcut_lane(self):
        for name in ('../kacis', '.sakli', 'iki kelime'):
            self.assertNotEqual(self.cli('baslat', '--ad', name, '--zaman-asimi', '1',
                                        '--', 'echo', 'x', check=False).returncode, 0)
        for value in ('0', '-1', 'nan', 'inf'):
            self.assertNotEqual(self.cli('baslat', '--ad', 'gecersiz', '--zaman-asimi', value,
                                        '--', 'echo', 'x', check=False).returncode, 0)
        self.start('tek', 5, 'echo', 'ilk')
        self.cli('bekle')
        self.assertEqual(self.cli('baslat', '--ad', 'tek', '--zaman-asimi', '5',
                                  '--', 'echo', 'ikinci', check=False).returncode, 2)
        self.assertEqual((self.directory / 'tek.log').read_text(), 'ilk\n')

    def test_komut_bulunamazsa_kalici_rc(self):
        self.start('eksik', 5, '/kesinlikle/olmayan/komut')
        self.assertEqual(self.cli('bekle', check=False).returncode, 1)
        self.assertEqual(self.record('eksik')['rc'], 127)
        self.assertIn('Gözetici hatası', (self.directory / 'eksik.log').read_text())

    def test_es_zamanli_ayni_lane_tek_yazici(self):
        command = [sys.executable, str(SCRIPT), 'baslat', '--log-dizini', str(self.directory),
                   '--ad', 'ortak', '--zaman-asimi', '5', '--', 'echo', 'tek']
        first = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        second = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        first.communicate(timeout=10)
        second.communicate(timeout=10)
        self.assertEqual(sorted([first.returncode, second.returncode]), [0, 2])
        self.cli('bekle')
        self.assertEqual((self.directory / 'ortak.log').read_text(), 'tek\n')

    def test_yardim(self):
        for action in ([], ['baslat'], ['durum'], ['bekle'], ['durdur']):
            result = subprocess.run([sys.executable, str(SCRIPT), *action, '--help'],
                                    capture_output=True, text=True, timeout=5)
            self.assertEqual(result.returncode, 0)
            self.assertIn('usage:', result.stdout)


if __name__ == '__main__':
    unittest.main(verbosity=2)
