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

    def test_lider_bitince_kalan_alt_surec_temizlenir_rc_korunur(self):
        for native_rc in (0, 7):
            with self.subTest(native_rc=native_rc):
                name = 'yetim' + str(native_rc)
                # Alt süreç TERM'i yok saysın; hazır olmadan lider çıkmasın.
                child_code = ('import signal,time; '
                              'signal.signal(signal.SIGTERM, signal.SIG_IGN); '
                              'print("hazir", flush=True); time.sleep(30)')
                code = ('import subprocess,sys; '
                        'child=subprocess.Popen([sys.executable,"-c",' + repr(child_code) +
                        '],stdout=subprocess.PIPE); child.stdout.readline(); '
                        'print(child.pid,flush=True); sys.exit(' + str(native_rc) + ')')
                self.start(name, 0.3, sys.executable, '-c', code)
                result = self.cli('bekle', check=False)
                self.assertEqual(result.returncode, 0 if native_rc == 0 else 1)
                self.assertEqual(self.record(name)['rc'], native_rc)
                child_pid = int((self.directory / (name + '.log')).read_text().strip())
                stat = Path('/proc', str(child_pid), 'stat')
                # Yetim zombie'yi host init'i toplar; çalışan alt süreç kalmamalı.
                if stat.exists():
                    self.assertEqual(stat.read_text().rsplit(')', 1)[1].split()[0], 'Z')

    def test_baslangic_kaydi_yarisi_kayip_gozetici_sayilmaz(self):
        # İlk atomik JSON ile gözetici kimliği yazımı arasını bir kapıyla sabitle.
        # Rastgele scheduler zamanlamasına güvenmeden gerçek CLI okuyucularını çalıştır.
        marker = self.directory / 'ilk-kayit'
        gate = self.directory / 'devam'
        wrapper = """import pathlib,sys,time
scope={'__name__':'filo_test','__file__':sys.argv[1]}
exec(compile(pathlib.Path(sys.argv[1]).read_text(),sys.argv[1],'exec'),scope)
original=scope['atomic']
log_directory=sys.argv[2]
def delayed(path, record):
    original(path, record)
    if record.get('state')=='starting' and record.get('supervisor_pid') is None:
        pathlib.Path(log_directory,'ilk-kayit').touch()
        while not pathlib.Path(log_directory,'devam').exists(): time.sleep(0.01)
scope['atomic']=delayed
sys.argv=[sys.argv[1],'baslat','--ad','yaris','--zaman-asimi','5',
          '--log-dizini',sys.argv[2],'--','sleep','0.4']
sys.exit(scope['main']())
"""
        starter = subprocess.Popen([sys.executable, '-c', wrapper, str(SCRIPT),
                                    str(self.directory)], stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, text=True)
        readers = []
        try:
            deadline = time.monotonic() + 5
            while not marker.exists() and time.monotonic() < deadline:
                time.sleep(0.01)
            self.assertTrue(marker.exists(), 'başlangıç penceresi kurulamadı')
            self.assertIsNone(self.record('yaris')['supervisor_pid'])
            for action in ('durum', 'bekle'):
                reader = subprocess.Popen([sys.executable, str(SCRIPT), action,
                                           '--log-dizini', str(self.directory)],
                                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                          text=True)
                readers.append(reader)
                # Geçici kaydı görüp rc2/bitti(bilinmiyor) dönmek yerine kilidi bekler.
                with self.assertRaises(subprocess.TimeoutExpired):
                    reader.communicate(timeout=0.25)
        finally:
            gate.touch()
            start_out, start_err = starter.communicate(timeout=10)
            outcomes = [reader.communicate(timeout=10) for reader in readers]
        self.assertEqual(starter.returncode, 0, start_out + start_err)
        for reader, (out, err) in zip(readers, outcomes):
            self.assertEqual(reader.returncode, 0, out + err)
            self.assertNotIn('gözetici kayıp', out + err)
            self.assertNotIn('bilinmiyor', out + err)
        self.assertEqual(self.record('yaris')['rc'], 0)

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
