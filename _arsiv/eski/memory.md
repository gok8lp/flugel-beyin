# Uzun Vadeli Hafıza (Memory)

> Bu dosya 200 satırın / 25 KB'ın altında tutulur; her oturumda [[map]] ile birlikte odaktadır.

## Kullanıcı ve Ortam
- **Kullanıcı:** Ahmet Gökalp Göksu ([[ahmet-gokalp-goksu]])
- **Hakem Kayıt Adı:** `"AHMET GÖKALP GÖKSU"` (Ankara bölgesi basketbol hakemi)
- **Yerel Makine:** Arch Linux, Hyprland, kullanıcı `flugel` (`sudo` yok)
- **Uzak Sunucu:** `flugelserver` (`ssh flugelserver`, Tailscale FQDN: `flugelserver.tail42f1f4.ts.net`, IP: `100.89.254.55`)

## Aktif Proje: Düdük (`/home/flugel/Projects/duduk`)
- **Depo:** `https://github.com/gok8lp/duduk` (**Private**, sürüm `v0.1.0`)
- **Derleme Komutu:** `cd /home/flugel/Projects/duduk && JAVA_HOME=/usr/lib/jvm/java-17-openjdk ./gradlew :app:assembleDebug :app:testDebugUnitTest`
- **Canlı Sunucu Uçları:**
  1. **Cloudflare Tunnel (`akis`):** `https://duduk.gokalpgoksu.com` (`/v1/health`, `/v1/bundle`, `/v1/stats`)
  2. **Tailscale Serve (`tailnet only`):** `https://flugelserver.tail42f1f4.ts.net:18443`
  3. **Yerel Docker Konteyneri (`flugelserver`):** `127.0.0.1:18420` (`~/duduk-server`, `duduk-server` konteyneri)
- **Emülatör Doğrulama Ortamı (`flugelserver`):**
  - SDK yolu: `/home/flugel/android-sdk`
  - AVD: `duduk_avd` (`system-images;android-35;google_apis;x86_64`)

## Sabit Kurallar
- Gizli dosyalar (`local.properties`, `.env`, anahtarlar, özellikle `/home/flugel/Projects/koharia-reader/local.properties`) asla okunmaz, yazılmaz, commit'lenmez.
- `raw/` klasörü salt okunurdur; yalnızca yeni kaynak eklenir, mevcut ham kaynaklar düzenlenmez.
- Her `wiki/` düzenlemesinden sonra `python3 brain.py lint` çalıştırılır ve `0 problem(s)` doğrulanır.
