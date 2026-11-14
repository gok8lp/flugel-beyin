---
tur: not
etiketler:
  - flugelserver
  - docker
  - nginx
  - flugel-akis
  - duduk-server
  - tsidp
  - adguard
  - guacamole
  - uptime-kuma
  - ollama
  - izleme
olusturma: 2026-11-11
guncelleme: 2026-11-11
---

# Docker Ağ, Panel, İzleme, Yerel AI ve Altyapı Yığını

> **Üst Harita ve Kök Bağlantılar:** [[HARITA]] · [[hafiza]] · [[kararlar]] · [[dersler]] · [[simdi]]
> **İlgili Wiki Sayfaları:** [[wiki/flugelserver-ag-guvenlik-ve-tuneller]] · [[wiki/flugelserver-docker-uygulamalari]] · [[wiki/flugel-akis-ve-botlar]] · [[wiki/duduk-genel-bakis]] · [[wiki/repo-duduk]]
> **İlgili Notlar:** [[notlar/docker-uygulama-baglanti-topolojisi]] · [[notlar/flugelserver-uc-disk-ve-klasor-agaci]] · [[notlar/sunucu-yedekleme-ve-systemd-otomasyonlari]] · [[notlar/sanal-makineler-w11-gpu-ve-moonlight]]
> **İlgili Projeler:** [[projeler/flugel-sunucu-ve-akis]] · [[projeler/duduk]]

---

## 1. Ağ, Panel, İzleme ve Yapay Zekâ Konteynerleri Özet Tablosu

| Konteyner | Yığın Konumu | İmaj | Ağ & Portlar | Bellek Sınırı | Temel Görevi |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`giris`** | `/opt/stacks/giris` | `nginx:1.27-alpine` | `host` (`127.0.0.1:8098` ve ters vekil kapıları) | `32m` | `gokalpgoksu.com` ana sayfası + `*.gokalpgoksu.com` Basic Auth (`htpasswd`) ters vekili |
| **`flugel-akis`** | `/opt/stacks/panel` | `python:3.13-alpine` | `host` (`:3012`) | `512m` | Kişisel sosyal akış, AI haber/gündem çevirisi, `/api/island` sunucu durum API'si |
| **`gundem-botu`** | `/opt/stacks/panel` | `python:3.13-alpine` | `3011:8090` | `128m` | Haber, basketbol maçları, anime ve sunucu sorunlarını JSON (`/ozet.json`) ve iCal (`takvim.ics`) olarak sunar |
| **`homepage`** | `/opt/stacks/panel` | `ghcr.io/gethomepage/homepage:latest` | `3010:3000` | `384m` | Sunucu kontrol paneli (`panel.gokalpgoksu.com`) |
| **`duduk-server`** | `/home/flugel/duduk-server` | `duduk-server-duduk-server` | `127.0.0.1:18420:18420` | — | **AHMET GÖKALP GÖKSU** için Assignr, AnkaraBasket ve TBF verilerini 3 saatte bir çekip arşivleyen arka uç |
| **`tsidp`** | `/opt/stacks/tsidp` | `ghcr.io/tailscale/tsidp:latest` | Tailnet (`idp.tail42f1f4.ts.net` / `100.119.135.23`) | — | Tailscale kimliğiyle OIDC tek giriş (SSO) sağlayıcısı |
| **`adguardhome`** | `/opt/stacks/adguard` | `adguard/adguardhome` | `192.168.0.15:53`, `100.86.88.1:53`, `0.0.0.0:8888->80`, `0.0.0.0:853` | `1536m` | Ev ağı ve Tailnet DNS sunucusu, reklam/zararlı/NSFW engelleme, DoH/DoT |
| **`guacamole`** + **`guacd`** + **`guac-db`** | `/opt/stacks/guacamole` | `guacamole/*:1.6.0` + `postgres:16-alpine` | `127.0.0.1:18097->8080` (`guacd`: host `172.17.0.1:4822`) | `768m` + `512m` + `256m` | Tarayıcı üzerinden VM (`mullvad-ts`, `W11`) RDP/SSH uzak masaüstü geçidi (`masaustu.gokalpgoksu.com`) |
| **`uptime-kuma`** | `/opt/stacks/uptime-kuma` | `louislam/uptime-kuma:2` | `3004:3001` | `512m` (`swap: 768m`) | Servis ve Docker konteyner çalışma süresi izleyici (`status.gokalpgoksu.com`) |
| **`ollama`** | `/opt/stacks/ollama` | `ollama/ollama:latest` | `127.0.0.1:21434->11434` (`runtime: nvidia`, `ai-kumhavuzu`) | `6g` (`swap: 6g`) | Yerel LLM çıkarım motoru (**`qwen3.5:4b`** — GTX 1660 Ti 6 GB VRAM'e tam sığar) |
| **`prometheus`** + **`alertmanager`** + **`node-exporter`** + **`grafana`** | `/opt/stacks/izleme` | `prom/*` + `grafana/grafana-oss:12.0.2` | `host` (Grafana `:3020`, Prom `127.0.0.1:9190`, Alert `127.0.0.1:9193`, Node `127.0.0.1:9100`) | `768m` + `128m` + `128m` + `384m` | Sunucu metrikleri, systemd birim durumu, yedek/klasör boyutu izleme ve Telegram alarm köprüsü |
| **`backrest`** | `/opt/stacks/backrest` | `garethgeorge/backrest:v1.14.1` | `9898:9898` | `1536m` | Restic şifreli yedekleme web arayüzü (`/mnt/side/restic` ve Google Drive `rclone`) |
| **`dozzle`** & **`cup`** | `/opt/stacks/dozzle` & `cup` | `amir20/dozzle:v11.3.4` & `ghcr.io/sergi0g/cup:v3.5.1` | `127.0.0.1:9811->8080` (Tailscale `:49443`) & `127.0.0.1:9812->8000` (`:50443`) | `128m` & `128m` | Canlı konteyner günlükleri (Dozzle) ve 6 saatte bir imaj güncelleme denetimi (Cup) |

---

## 2. Kritik Servislerin Mimari ve Yapılandırma Ayrıntıları

### 2.1. `giris` (Nginx Ters Vekil ve Başlangıç Kapısı — `/opt/stacks/giris`)
- `network_mode: host` ve `mem_limit: 32m` ile çalışır; `/opt/stacks/giris/html`, `nginx.conf` ve `htpasswd` dosyalarını salt-okunur (`:ro`) bağlar.
- Cloudflare `akis.yml` tüneli üzerinden gelen dış istekleri (`sonarr`, `radarr`, `prowlarr`, `bazarr`, `jackett`, `torrent`, `plex`, `panel`, `lingarr`, `checkcle`, `indir`, `suwayomi`, `yukle` `.gokalpgoksu.com`) tek noktadan **HTTP Basic Auth (`401 Unauthorized`)** ile korur.
- `Dockge`, `File Browser`, `Netdata` ve `AdGuard` yönetim panelleri güvenlik kararı gereği dış tünelden bilerek **açılmamıştır**.

### 2.2. `panel` Yığını: `flugel-akis`, `gundem-botu` ve `homepage` (`/opt/stacks/panel`)
- **`flugel-akis` (`:3012`):**
  - Sunucunun kişisel sosyal akış ve durum merkezidir. `/var/lib/basket-bot:/basket:ro`, `/var/lib/flugel/durum:/durum:ro` ve `./homepage/services.yaml:/homepage/services.yaml:ro` bağlamalarını okur.
  - **Yapay Zekâ Çeviri ve Özetleme:** `CEVIRI_MODEL="qwen3.5:4b"` ve `SOHBET_MODEL="qwen3.5:4b"` kullanır. RAM ve GPU kullanımını optimize etmek için `AI_KEEP_ALIVE="2m"`, `AI_TOPLU_ARALIK="1800"` (30 dakikada bir toplu çalışır), `AI_TOPLU_SURE="900"` (en fazla 15 dakika çalışıp modeli VRAM'den boşaltır) ve `AI_SESSIZ="03:30-06:30"` (gece yedekleme ve Lingarr çevirisi saatlerinde arka plan AI durur) parametreleriyle yapılandırılmıştır.
- **`gundem-botu` (`3011:8090`):**
  - Haberleri, basketbol hakem atamalarını, anime yayın takvimini ve sunucu uyarılarını birleştirip `/ozet.json` ve iCal takvimi (`/takvim.ics`) olarak yerel ağ ve Tailscale'e sunar.

### 2.3. `duduk-server` (`/home/flugel/duduk-server/docker-compose.yml`)
- **Görev:** Basketbol hakemi **AHMET GÖKALP GÖKSU** için Assignr (`assignr.immensus.io`), `ankarabasket.org.tr` (gömülü `days` RSC Flight JSON'u) ve TBF API (`miniappapi.tbf.org.tr`) verilerini düzenli olarak çeker.
- **Yapılandırma:**
  - `ports: ["127.0.0.1:18420:18420"]`
  - `DUDUK_DATA_DIR=/data` (`./data:/data` kalıcı hacmi; Assignr yalnız son 2 haftayı döndürdüğü için geçmiş haftalar burada silinmeden biriktirilir)
  - `DUDUK_REFEREE=AHMET GÖKALP GÖKSU`
  - `DUDUK_POLL_SECONDS=10800` (3 saatte bir tarama)

### 2.4. `ollama` ve Yerel Yapay Zekâ Optimizasyonu (`/opt/stacks/ollama`)
- **Model Seçimi (`2026-10-20` Kararı):** Eskiden 40 GB yer kaplayan 10 farklı model silinerek GTX 1660 Ti'ın **6 GB VRAM**'ine tam sığan **`qwen3.5:4b`** (3,1 GB) ana model olarak belirlenmiştir. Telegram köprüsü (`/opt/telegram-kopru`), `anime_takip.py`, `ai-gozcu.sh` ve `flugel-akis` bu modeli kullanır.
- **Bellek Koruması (`claude-son 2026-10-21`):**
  - `OLLAMA_NUM_PARALLEL=1`, `OLLAMA_KEEP_ALIVE=0` (iş bitince VRAM anında boşaltılır), `OLLAMA_CONTEXT_LENGTH=8192`, `OLLAMA_MAX_LOADED_MODELS=1`, `OLLAMA_FLASH_ATTENTION=1`.
  - `LLAMA_ARG_CACHE_RAM=0`: `llama-server` istem önbelleğinin varsayılan olarak 8 GB host RAM tüketmesi engellenmiştir.
  - `LLAMA_ARG_CTX_CHECKPOINTS=2`: `qwen3.5` bağlam kontrol noktaları varsayılan 32'den (her biri ~110 MB) 2'ye düşürülerek sistem RAM'i korunmuştur.

### 2.5. `adguardhome`, `guacamole` ve `tsidp`
- **AdGuard Home (`/opt/stacks/adguard`):**
  - Ev ağı (`192.168.0.15:53`) ve Tailscale (`100.86.88.1:53`) üzerinde DNS filtreleme yapar.
  - Ekim 2026'da `768m` sınırında OOM (Out of Memory) yaşadığı için bellek sınırı önce `1 GiB` ardından `1536m`'ye çıkarılmış ve `querylog.size_memory` değeri 1000'den **500** kayda düşürülmüştür.
- **Apache Guacamole (`/opt/stacks/guacamole`):**
  - `guacd` host ağında yalnız Docker köprüsü (`172.17.0.1:4822`) üzerinde dinler ve KVM sanal makine ağına (`192.168.122.0/24`) RDP/SSH bağlantısı kurar.
  - Web arayüzü `127.0.0.1:18097->8080` portundadır; `BAN_MAX_INVALID_ATTEMPTS: "5"` ve `BAN_ADDRESS_DURATION: "1800"` (30 dk engelleme) ile kaba kuvvet saldırılarına karşı korunur; Cloudflare tünelinden gelen gerçek istemci IP'sini `X-Forwarded-For` (`REMOTE_IP_VALVE_ENABLED: "true"`) üzerinden okur.
- **Tailscale OIDC (`tsidp` — `/opt/stacks/tsidp`):**
  - `TS_HOSTNAME=idp` ile Tailnet içinde `idp.tail42f1f4.ts.net` (`100.119.135.23`) adresinde OIDC kimlik sağlayıcısı olarak çalışır (Funnel kapalıdır, yalnız tailnet cihazları erişebilir).
