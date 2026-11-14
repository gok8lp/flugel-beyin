#!/usr/bin/env python3
"""Linux/POSIX lane gözetimi; yalnız Python 3 standart kütüphanesi.

Her lane'in ayrık gözeticisi çıkış kodunu atomik JSON'a yazar. Takılma bir
şüphedir: log yazmayan sağlıklı süreç kendiliğinden öldürülmez. Zaman aşımı
başlatmadan itibaren işler; bekle açık olmasa da gözetici süreyi uygular.
Lider komut normal bitse de grupta kalan alt süreçler TERM/KILL ile temizlenir;
liderin doğal çıkış kodu korunur, temizlik bitmeden lane bitmiş sayılmaz.
"""
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import json
import math
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import tempfile
import time
import uuid

POLL = 0.1
TERM_GRACE = 1.0


def atomic(path, value):
    fd, name = tempfile.mkstemp(prefix='.' + path.name + '.', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as stream:
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.write('\n')
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
        dirfd = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(dirfd)
        finally:
            os.close(dirfd)
    finally:
        if os.path.exists(name):
            os.unlink(name)


@contextmanager
def locked(directory, name):
    with (directory / ('.' + name + '.lock')).open('a') as stream:
        fcntl.flock(stream, fcntl.LOCK_EX)
        yield


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def identity(pid):
    """PID yeniden kullanımını /proc başlangıç sayacıyla ayırt et."""
    try:
        fields = Path('/proc', str(pid), 'stat').read_text().rsplit(')', 1)[1].split()
        if fields[0] == 'Z':
            return None
        return fields[19]
    except (OSError, IndexError, TypeError):
        return None


def alive(pid, token):
    return pid is not None and token is not None and identity(pid) == token


def terminate(proc):
    # Komut ayrı bir session/process group lideridir; alt süreçler de durur.
    try:
        os.killpg(proc.pid, signal.SIGTERM)
    except ProcessLookupError:
        pass
    deadline = time.monotonic() + TERM_GRACE
    # Lider bitse bile TERM'i yok sayan alt süreçlere de süre tanı.
    while time.monotonic() < deadline:
        proc.poll()
        try:
            os.killpg(proc.pid, 0)
        except ProcessLookupError:
            break
        time.sleep(POLL)
    try:
        os.killpg(proc.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    proc.wait()


def supervise(directory, name, run_id):
    path = directory / (name + '.json')
    control = directory / ('.' + name + '.control.json')
    with locked(directory, name):
        record = read(path)
        if record['run_id'] != run_id:
            return
        # Başlatıcının kaydettiği gözeticiyle aynı süreç olduğumuzu doğrula.
        if record['supervisor_pid'] != os.getpid():
            return
    proc = None
    rc = 127
    reason = 'başlatılamadı'
    with open(record['log'], 'ab', buffering=0) as log:
        try:
            proc = subprocess.Popen(record['command'], stdin=subprocess.DEVNULL,
                                    stdout=log, stderr=subprocess.STDOUT,
                                    start_new_session=True)
            with locked(directory, name):
                record.update(pid=proc.pid, pid_start=identity(proc.pid), state='running')
                atomic(path, record)
            while True:
                rc = proc.poll()
                if rc is not None:
                    # Liderin sonucu korunur; arka planda bıraktığı alt süreçler
                    # lane yaşam döngüsünden ve süre sınırından kaçamaz.
                    terminate(proc)
                    reason = 'bitti'
                    break
                # Monotonic saat aynı host/boot içinde duvar saati değişiminden etkilenmez.
                if time.monotonic() >= record['deadline_monotonic']:
                    terminate(proc)
                    rc, reason = 124, 'zaman aşımı'
                    break
                if control.exists():
                    request = read(control)
                    if request.get('run_id') == run_id:
                        terminate(proc)
                        rc, reason = 143, 'durduruldu'
                        break
                time.sleep(POLL)
        except Exception as exc:
            log.write(('Gözetici hatası: ' + str(exc) + '\n').encode())
            if proc is not None:
                terminate(proc)
            rc, reason = 127, 'başlatılamadı/gözetici hatası'
        finally:
            with locked(directory, name):
                record.update(state='finished', rc=rc, reason=reason,
                              finished_at=datetime.now(timezone.utc).isoformat())
                atomic(path, record)


def start(args, directory):
    command = args.command
    if command and command[0] == '--':
        command = command[1:]
    if not command:
        raise ValueError('-- sonrasında bir komut gerekli')
    path = directory / (args.ad + '.json')
    with locked(directory, args.ad):
        # Geçmiş kayıtların yanlışlıkla ezilmesini de engelle.
        if path.exists():
            raise ValueError('Lane kaydı zaten var; yeni bir --ad veya --log-dizini kullan')
        now = time.time()
        record = dict(name=args.ad, run_id=uuid.uuid4().hex, state='starting', pid=None,
                      started_at=datetime.now(timezone.utc).isoformat(), started_epoch=now,
                      timeout_seconds=args.zaman_asimi,
                      deadline_monotonic=time.monotonic() + args.zaman_asimi,
                      log=str(directory / (args.ad + '.log')), command=command,
                      supervisor_pid=None, supervisor_start=None, rc=None)
        Path(record['log']).touch(exist_ok=False)
        atomic(path, record)
        try:
            supervisor = subprocess.Popen(
                [sys.executable, str(Path(__file__).resolve()), '_go', '--ad', args.ad,
                 '--log-dizini', str(directory), '--run-id', record['run_id']],
                stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL, start_new_session=True, close_fds=True)
            record.update(supervisor_pid=supervisor.pid,
                          supervisor_start=identity(supervisor.pid))
            atomic(path, record)
        except OSError:
            record.update(state='finished', rc=127, reason='gözetici başlatılamadı')
            atomic(path, record)
            raise
    # PID'nin raporda mevcut olması için kısa hazır olma el sıkışması.
    deadline = time.monotonic() + 5
    while time.monotonic() < deadline:
        record = read(path)
        if record['state'] != 'starting':
            break
        time.sleep(POLL)
    print(json.dumps(record, ensure_ascii=False))


def records(directory):
    for path in sorted(directory.glob('*.json')):
        if not path.name.startswith('.'):
            # Başlatma kaydı ile gözetici kimliği aynı kilit altında yayımlanır.
            # Ara 'starting/pid=None' görüntüsünü kayıp süreç sanma.
            with locked(directory, path.stem):
                record = read(path)
            yield record


def status(record, stale_minutes):
    if record['state'] == 'finished':
        if record['rc'] == 124:
            return 'zaman aşımı (rc=124)'
        return 'bitti(rc={}) — {}'.format(record['rc'], record.get('reason', ''))
    if not alive(record['supervisor_pid'], record['supervisor_start']):
        return 'bitti(rc=bilinmiyor) — gözetici kayıp; süreç ayrıca incelenmeli'
    if record['state'] == 'starting':
        return 'çalışıyor (başlatılıyor)'
    if time.monotonic() >= record['deadline_monotonic']:
        return 'zaman aşımı (durduruluyor)'
    age = max(0, time.time() - Path(record['log']).stat().st_mtime)
    if age >= stale_minutes * 60:
        return 'takıldı (log {:.1f} dakikadır büyümedi; şüphe)'.format(age / 60)
    return 'çalışıyor'


def stop(args, directory):
    path = directory / (args.ad + '.json')
    with locked(directory, args.ad):
        record = read(path)
        if record['state'] == 'finished':
            print(args.ad + ': ' + status(record, 10))
            return 0
        if not alive(record['supervisor_pid'], record['supervisor_start']):
            raise ValueError('Gözetici kayıp; PID tekrar kullanımı riski nedeniyle sinyal gönderilmedi')
        atomic(directory / ('.' + args.ad + '.control.json'), {'run_id': record['run_id']})
    deadline = time.monotonic() + TERM_GRACE + 5
    while time.monotonic() < deadline:
        record = read(path)
        if record['state'] == 'finished':
            print(args.ad + ': ' + status(record, 10))
            return 0
        time.sleep(POLL)
    raise ValueError('Durdurma onaylanamadı; gözeticiyi incele')


def positive(value):
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError('sonlu, sıfırdan büyük sayı gerekli')
    return number


def lane(value):
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,79}', value):
        raise argparse.ArgumentTypeError('lane: 1–80 harf/rakam/_/-; ilk karakter harf/rakam')
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    for action in ('baslat', 'durum', 'bekle', 'durdur', '_go'):
        item = sub.add_parser(action, help={'baslat': 'arka planda başlat',
            'durum': 'lane durumlarını göster', 'bekle': 'hepsi bitene kadar bekle',
            'durdur': 'SIGTERM ile durdur', '_go': 'iç gözetici (elle çağırma)'}[action])
        item.add_argument('--log-dizini', required=True, type=Path)
        if action in ('baslat', 'durdur', '_go'):
            item.add_argument('--ad', required=True, type=lane)
        if action == 'baslat':
            item.add_argument('--zaman-asimi', required=True, type=positive, metavar='SN')
            item.add_argument('command', nargs=argparse.REMAINDER)
        if action == 'durum':
            item.add_argument('--takilma-dakika', type=positive, default=10, metavar='N',
                              help='log sessizliği şüphe eşiği (varsayılan: 10 dakika)')
        if action == '_go':
            item.add_argument('--run-id', required=True)
    args = parser.parse_args()
    try:
        directory = args.log_dizini.resolve()
        if args.action == 'baslat':
            directory.mkdir(parents=True, exist_ok=True)
            start(args, directory)
        elif not directory.is_dir():
            raise ValueError('log dizini mevcut değil')
        elif args.action == '_go':
            supervise(directory, args.ad, args.run_id)
        elif args.action == 'durum':
            for record in records(directory):
                print(record['name'] + ': ' + status(record, args.takilma_dakika))
        elif args.action == 'durdur':
            return stop(args, directory)
        else:
            while True:
                current = list(records(directory))
                lost = [r for r in current if r['state'] != 'finished' and
                        not alive(r['supervisor_pid'], r['supervisor_start'])]
                if lost:
                    raise ValueError('Gözetici kayıp: ' + ', '.join(r['name'] for r in lost))
                if all(r['state'] == 'finished' for r in current):
                    for record in current:
                        print(record['name'] + ': ' + status(record, 10))
                    return 1 if any(r['rc'] != 0 for r in current) else 0
                time.sleep(POLL)
    except (OSError, ValueError, KeyError) as exc:
        print('Hata: ' + str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
