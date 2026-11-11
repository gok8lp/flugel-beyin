# GitHub Repo: gok8lp/cybersecurity-lab

- **URL:** https://github.com/gok8lp/cybersecurity-lab
- **Görünürlük:** Açık (Public)
- **Ana Dil:** Python
- **Son Güncelleme:** 2026-10-22T22:53:26Z
- **Açıklama:** FastAPI ve React ile siber güvenlik dersleri, bulmacalar ve izole laboratuvar prototipi.

## Dosya Ağacı (File Tree)
- `.gitignore` (blob)
- `README.md` (blob)
- `apps` (tree)
- `apps/api` (tree)
- `apps/api/cyberlab` (tree)
- `apps/api/cyberlab/__init__.py` (blob)
- `apps/api/cyberlab/content.py` (blob)
- `apps/api/cyberlab/flags.py` (blob)
- `apps/api/cyberlab/main.py` (blob)
- `apps/api/cyberlab/models.py` (blob)
- `apps/api/cyberlab/puzzles.py` (blob)
- `apps/web` (tree)
- `apps/web/index.html` (blob)
- `apps/web/package-lock.json` (blob)
- `apps/web/package.json` (blob)
- `apps/web/src` (tree)
- `apps/web/src/Uygulama.tsx` (blob)
- `apps/web/src/api.ts` (blob)
- `apps/web/src/main.tsx` (blob)
- `apps/web/src/stil.css` (blob)
- `apps/web/tsconfig.json` (blob)
- `apps/web/tsconfig.tsbuildinfo` (blob)
- `apps/web/vite.config.ts` (blob)
- `content` (tree)
- `content/challenges.yaml` (blob)
- `content/lessons` (tree)
- `content/lessons/00-baslarken.md` (blob)
- `content/lessons/01-kapsam-etik.md` (blob)
- `content/lessons/02-linux-izinleri.md` (blob)
- `content/lessons/03-kodlama-sifreleme-ozet.md` (blob)
- `content/lessons/04-http-temelleri.md` (blob)
- `content/lessons/05-kullanilabilirlik-dos.md` (blob)
- `content/puzzles.yaml` (blob)
- `docs` (tree)
- `docs/CLAUDE_BUILD_ORDER.md` (blob)
- `docs/CURRICULUM.md` (blob)
- `docs/MASTER_SPEC.md` (blob)
- `labs` (tree)
- `labs/linux-permission-leak` (tree)
- `labs/linux-permission-leak/Dockerfile` (blob)
- `labs/linux-permission-leak/baslat.sh` (blob)
- `labs/linux-permission-leak/compose.yaml` (blob)
- `labs/linux-permission-leak/verify.sh` (blob)
- `labs/scope-guard` (tree)
- `labs/scope-guard/README.md` (blob)
- `pytest.ini` (blob)
- `runner` (tree)
- `runner/__init__.py` (blob)
- `runner/kapasite.py` (blob)
- `runner/kapsam.py` (blob)
- `runner/runner.py` (blob)
- `tests` (tree)
- `tests/bulmaca_kaynak.yaml` (blob)
- `tests/test_api.py` (blob)
- `tests/test_guvenlik_politikasi.py` (blob)
- `tests/test_runner.py` (blob)
- `tools` (tree)
- `tools/bulmaca_derle.py` (blob)

## README İçeriği
# Siber Güvenlik Laboratuvarı

Kişisel siber güvenlik eğitim laboratuvarı: **öğretici dersler**, **tarayıcıda çözülen bulmacalar** ve
**tek kullanımlık, internete kapalı lab görevleri**. Her saldırı görevinin eşlenmiş bir savunma görevi vardır.

> Durum: geliştirme prototipi. Dersler, bulmacalar ve API kodu bulunur; Docker runner ve sunucu kurulumu ayrı doğrulama gerektirir.
> English: a personal cybersecurity learning lab built with FastAPI, React and isolated container exercises.

## İçindekiler

- [Ne var?](#ne-var)
- [Hızlı başlangıç (yerel)](#hızlı-başlangıç-yerel)
- [Nasıl kullanılır](#nasıl-kullanılır)
- [Mimari](#mimari)
- [Güvenlik sınırları](#güvenlik-sınırları)
- [İçerik ekleme](#içerik-ekleme)
- [Testler](#testler)
- [Yol haritası](#yol-haritası)

## Ne var?

| Bölüm | İçerik |
|---|---|
| Öğretici | 6 ders: Başlarken, Kapsam ve etik, Linux izinleri, Kodlama/şifreleme/özet, HTTP ve güvenlik başlıkları, Kullanılabilirlik ve DoS (savunma) |
| Bulmacalar | 17 bulmaca, 7 kategori: kodlama, özet (hash), dosya izinleri, HTTP, güvenli kod, dayanıklılık (DoS savunması), log |
| Lablar | `linux-permission-leak` (fazla izinli yedek: saldırı + savunma), `scope-guard` (kapsam koruması) |
| Puan | XP, tamamlanan bulmacalar; ipucu kademeleri (2. ipucu −%10, 3. ipucu −%25) |

## Hızlı başlangıç (yerel)

Gereken: Python 3.12+, Node 20+. Lab konteynerlerini çalıştırmak için ayrıca Docker gerekir.

```bash
git clone https://github.com/gok8lp/cybersecurity-lab.git
cd cybersecurity-lab
python3 -m venv .venv
.venv/bin/pip install fastapi==0.115.6 uvicorn==0.34.0 sqlmodel==0.0.22 pyyaml==6.0.2 pytest==8.3.4 httpx==0.28.1
```

API:

```bash
CYBERLAB_AUTO=1 CYBERLAB_DATA=./data PYTHONPATH=apps/api .venv/bin/uvicorn cyberlab.main:app --host 127.0.0.1 --port 8000
```

Arayüz (ayrı terminal):

```bash
cd apps/web && npm install && npx vite --host 127.0.0.1 --port 5173
```

Tarayıcıda: <http://127.0.0.1:5173>

## Nasıl kullanılır

1. **Ana sayfa:** "Bugünün üçlüsü" (1 ders, 1 bulmaca, 1 lab), ilerleme ve lab durumu.
2. **Öğretici:** dersler sırayla; her dersin sonunda "Sonraki ders". Önce *Başlarken* ve *Kapsam ve etik* okunmalı.
3. **Bulmacalar:** kategoriye göre süz; cevabı yaz ya da seçeneği seç. Takılırsan ipuçlarını sırayla aç.
   Doğru cevaptan sonra kısa bir açıklama çıkar ve XP eklenir (aynı bulmaca ikinci kez XP vermez).
4. **Lablar:** "Lab başlat" sana özel, internete kapalı bir hedef açar. Bulduğun `FLG{...}` değerini gönder,
   ardından savunma adımında açığı kapat. Lab servisi (runner) çalışmıyorsa ya da sunucu meşgulse neden yazılır.

## Mimari

```text
tarayıcı ── React (apps/web) ── /api ── FastAPI (apps/api)
                                           │  SQLite (data/cyberlab.db), içerik (content/)
                                           └── runner (Unix soket, yalnız izin listesi)
                                                  └── docker compose: labs/<görev>/compose.yaml
                                                       (internal ağ, tek kullanımlık)
```

| Dizin | Görev |
|---|---|
| `apps/api/cyberlab/` | `main.py` uç noktalar, `content.py` ders/görev yükleyici, `puzzles.py` bulmaca motoru, `flags.py` oturum bayrağı, `models.py` veri modeli |
| `apps/web/src/` | `Uygulama.tsx` sekmeler, `api.ts` istemci, `stil.css` koyu tema |
| `runner/` | `kapsam.py` hedef koruması, `kapasite.py` kaynak eşiği, `runner.py` başlat/durdur |
| `content/` | `lessons/*.md` dersler, `challenges.yaml` görevler, `puzzles.yaml` (üretilir) |
| `labs/<görev>/` | Dockerfile, `compose.yaml`, doğrulayıcı |
| `tests/` | API, runner ve güvenlik politikası testleri; `bulmaca_kaynak.yaml` |
| `tools/` | `bulmaca_derle.py` |
| `docs/` | Codex'in tasarım belgeleri (MASTER_SPEC, CURRICULUM, CLAUDE_BUILD_ORDER) |

## Güvenlik sınırları

- Gerçek ev sunucusu, ev ağı, modem, Cloudflare, VM'ler ve üretim konteynerleri **asla hedef değildir**.
- Lab ağları `internal: true`: internete ve ev ağına çıkamaz. Hedef portları hiçbir yere yayımlanmaz.
- Her lab konteyneri: salt okunur kök, `cap_drop: [ALL]`, `no-new-privileges`, bellek/CPU/süreç sınırı, sağlık kontrolü.
- `privileged`, `network_mode: host`, host PID/IPC, `docker.sock` ve host dizini bağlamak yasak; testler bunu denetler.
- API Docker'a dokunmaz; yalnız runner, izin listesindeki görevleri `docker compose` argv ile açar (shell yok).
- Runner, sunucuda boş bellek < 4 GiB, disk baskısı ≥ %20 ya da yük yüksekse lab başlatmaz.
- Bayraklar imajda yok: oturum başında HMAC ile üretilir, veritabanında yalnız özeti tutulur; başka oturumda geçmez.
- Bulmaca cevapları içerikte açık değil: `sha256(normalize(cevap))`.

## İçerik ekleme

**Ders:** `content/lessons/NN-ad.md` dosyası, başında ön bilgi bloğu:

```markdown
---
slug: yeni-ders
module: web
title: Başlık
type: theory
minutes: 10
prerequisites: [baslarken]
---
# İçerik (Markdown)
```

Önkoşul döngüsü ya da bilinmeyen önkoşul yükleme hatası verir.

**Bulmaca:** `tests/bulmaca_kaynak.yaml` dosyasına ekle (cevap burada açık), sonra:

```bash
.venv/bin/python tools/bulmaca_derle.py
```

Bu komut `content/puzzles.yaml` dosyasını cevap özetleriyle yeniden üretir.

**Lab görevi:** `content/challenges.yaml` kaydı + `labs/<slug>/compose.yaml` (güvenlik testlerinden geçmeli).

## Testler

```bash
.venv/bin/python -m pytest -q
cd apps/web && npx tsc -b && npx vite build
```

20 test: API (bayrak tekrar kullanımı, bulmaca cevapları, XP), runner (kapsam dışı hedef reddi, kapasite eşiği,
izin listesi, argv), güvenlik politikası (yasaklı ayarlar, lab sertleştirme).

## Yol haritası

| Faz | Durum |
|---|---|
| 0 Keşif | tamam |
| 1 Güvenli iskelet | tamam |
| 2 İçerik ve puan motoru | kısmen: 6 ders, 17 bulmaca |
| 3 Runner (Unix soket servisi, 20 döngü testi) | iskelet |
| 4 İlk dört görev | 1/4 (`linux-permission-leak` dosyaları hazır, sunucuda denenmedi) |
| 5 C/C++ yolu | bekliyor |
| 6 Tarayıcı terminali, erişilebilirlik | bekliyor |
| 7 Sunucuya kurulum | kullanıcı onayı bekler (port, alan adı, erişim politikası gösterilecek) |

