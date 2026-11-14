---
tur: hafiza
etiketler:
  - hafiza
  - profil
  - ortam
olusturma: 2026-11-11
guncelleme: 2026-11-14
---

# hafiza.md — Kalıcı Tercihler ve Gerçekler

Bağlantılar: [[HARITA]] · [[simdi]] · [[kararlar]] · [[dersler]] · [[kisiler/ahmet-gokalp-goksu]]

## 1. Kimlik ve Tercihler
- **Kullanıcı:** Ahmet Gökalp Göksu (`gok8lp`, MAL: `gokalpgoksu`).
- **Basketbol Hakemliği:** Ankara bölgesi hakemi; `assignr` atama verilerinde tam adı `"AHMET GÖKALP GÖKSU"` olarak geçer.
- **Okul:** Gazi Üniversitesi Elektrik-Elektronik Mühendisliği (2026-2027 Güz dönemi, 3. sınıf — [[projeler/okul-guz-2026]]).
- **Dil ve Üslup:** Her zaman Türkçe konuşulur. Doğrulanmamış şeye "çalışıyor" denmez. Her iş sonunda derleme/test doğrulanır ve git commit atılır.

## 2. Cihazlar ve Sunucu Altyapısı
- **PC:** Arch Linux + Hyprland (ve Ubuntu/GNOME geçmişi), kullanıcı `flugel`.
- **Ev Sunucusu (`flugelserver`):**
  - LAN IP: `192.168.0.15` | Tailscale: `100.86.88.1` / `100.89.254.55` (`flugelserver.tail42f1f4.ts.net`) | Alan adı: `gokalpgoksu.com`.
  - Donanım: AMD Ryzen 5 2600X, GTX 1660 Ti (6 GB), 16 GB RAM.
  - 3 LUKS Disk: `/` (480 GB SSD), `/mnt/side` (500 GB HDD — indirmeler ve yedekler), `/mnt/sidemain` (1 TB — film/dizi, manga/LN, Immich, Nextcloud).
  - Docker Yığınları: `/opt/stacks/<uygulama>/compose.yaml` ve `~/duduk-server/docker-compose.yml`, uygulama verileri `/srv/appdata/<uygulama>/`.
- **Düdük Canlı Uçları:**
  1. Cloudflare Tunnel (`akis.yml`): `https://duduk.gokalpgoksu.com`
  2. Tailscale Serve: `https://flugelserver.tail42f1f4.ts.net:18443`
  3. Doğrudan açık kaynaklar (`assignr`, `ankarabasket`, `TBF`)
- **Düdük Geliştirme Ortamı** (eski `memory.md`'den birleştirildi):
  - Depo: `https://github.com/gok8lp/duduk` (**Private**, sürüm `v0.1.0`), yerel dizin `/home/flugel/Projects/duduk`.
  - Derleme: `cd /home/flugel/Projects/duduk && JAVA_HOME=/usr/lib/jvm/java-17-openjdk ./gradlew :app:assembleDebug :app:testDebugUnitTest`
  - Canlı uç yolları: `/v1/health`, `/v1/bundle`, `/v1/stats`; sunucuda konteyner `duduk-server` → `127.0.0.1:18420` (`~/duduk-server`).
  - Emülatör (`flugelserver`): SDK `/home/flugel/android-sdk`, AVD `duduk_avd` (`system-images;android-35;google_apis;x86_64`).
  - Aktif sezon: `2026-2027`, TBF `seasonId=174`.
  - `sudo`: Bu PC'de (kullanıcı `flugel`/gokalp) **sudo var** (kullanıcı teyidi, 2026-11-14). Ajanlar sudo'yu yalnız kullanıcı görev için açıkça izin verdiğinde kullanır; yedek/geri dönüş/rapor kuralları: `~/Documents/ai_workplace/AGENTS.md`. Eski "sudo yok" notu yanlıştı.

## 3. Güvenlik ve Gizlilik Kuralları
- Parola, token, `.env`, `local.properties` (özellikle `/home/flugel/Projects/koharia-reader/local.properties`), SSH anahtarı veya çerezler **asla** okunmaz, sohbete yazılmaz ve vault'a/git'e kaydedilmez.
- Sunucuda `W11` ve `W11-GPU` sanal makineleri aynı diski (`/var/lib/libvirt/images/w11`) paylaştığı için asla aynı anda açılmaz ve `SIGKILL` ile zorla kapatılmaz.
- `raw/` klasörü salt okunurdur; değişiklikler yalnızca `wiki/` ve `notlar/` üzerinde yapılır ve `python3 brain.py lint` ile doğrulanır.
