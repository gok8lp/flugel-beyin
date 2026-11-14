---
tur: not
etiketler:
  - flugelserver
  - docker
  - medya
  - sonarr
  - radarr
  - jellyfin
  - plex
  - gluetun
  - transmission
olusturma: 2026-11-11
guncelleme: 2026-11-11
---

# Docker Medya, İndirme ve *arr Yığını Yapılandırması

> **Üst Harita ve Kök Bağlantılar:** [[HARITA]] · [[hafiza]] · [[kararlar]] · [[dersler]] · [[simdi]]
> **İlgili Wiki Sayfaları:** [[wiki/flugelserver-docker-uygulamalari]] · [[wiki/flugelserver-uygulama-baglantilari]] · [[wiki/flugelserver-dizi-film-arsivi]] · [[wiki/flugelserver-ag-guvenlik-ve-tuneller]]
> **İlgili Notlar:** [[notlar/docker-uygulama-baglanti-topolojisi]] · [[notlar/flugelserver-uc-disk-ve-klasor-agaci]] · [[notlar/sunucu-dizi-ve-film-arsivi-envanteri]] · [[notlar/sunucu-yedekleme-ve-systemd-otomasyonlari]]
> **İlgili Projeler:** [[projeler/flugel-sunucu-ve-akis]]

---

## 1. Medya ve *arr Konteynerleri Özet Tablosu

`flugelserver` üzerindeki medya otomasyon zinciri `/opt/stacks/` altında her servis için ayrı birer klasörde tutulur. Bellek tüketimini sınırlamak amacıyla `sistem-bakim v2` kapsamında her konteynere `mem_limit` tanımlanmış ve pek çok servis `restart: "no"` yapılarak `uygulama-katman` (systemd soket aktivasyonu / boşta durdurma) yönetimine bağlanmıştır.

| Konteyner | İmaj | Ağ Modu & Port Eşlemesi | Bellek Sınırı | Kalıcı Disk Bağlamaları (Volumes) | Restart Politikası |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`gluetun`** | `qmcgaw/gluetun` | `bridge`<br>`127.0.0.1:18889->8888`<br>`127.0.0.1:19091->9091`<br>`127.0.0.1:19696->9696`<br>`127.0.0.1:14567->4567`<br>`0.0.0.0:51413->51413/tcp,udp` | `256m` | `./auth:/gluetun/auth:ro`<br>Cihaz: `/dev/net/tun` (`NET_ADMIN`) | `"no"` (`uygulama-katman`) |
| **`transmission`** | `lscr.io/linuxserver/transmission:latest` | `container:gluetun`<br>(Port `19091->9091` gluetun'da) | `768m` | `/srv/appdata/transmission:/config:Z`<br>`/mnt/side/downloads:/downloads:Z`<br>`/mnt/side/watch:/watch:Z` | `"no"` (`uygulama-katman`) |
| **`prowlarr`** | `lscr.io/linuxserver/prowlarr:latest` | `container:gluetun`<br>(Port `19696->9696` gluetun'da) | `512m` | `/srv/appdata/prowlarr:/config:Z` | `"no"` (`uygulama-katman`) |
| **`flaresolverr`** | `ghcr.io/flaresolverr/flaresolverr:latest` | `container:gluetun`<br>(İç port `8191`) | `1536m` | Docker anonim volume (`/config`) | `"no"` (`uygulama-katman`) |
| **`jackett`** | `lscr.io/linuxserver/jackett:latest` | `bridge`<br>`127.0.0.1:19117->9117/tcp` | `512m` | `/srv/appdata/jackett:/config:Z` | `"no"` (`uygulama-katman`) |
| **`sonarr`** | `lscr.io/linuxserver/sonarr:latest` | `bridge`<br>`127.0.0.1:18989->8989/tcp` | `768m` | `/srv/appdata/sonarr:/config:Z`<br>`/mnt/sidemain/media/series:/tv:Z`<br>`/mnt/side/downloads:/downloads:Z` | `"no"` (`uygulama-katman`) |
| **`radarr`** | `lscr.io/linuxserver/radarr:latest` | `bridge`<br>`127.0.0.1:17878->7878/tcp` | `768m` | `/srv/appdata/radarr:/config:Z`<br>`/mnt/sidemain/media/movies:/movies:Z`<br>`/mnt/side/downloads:/downloads:Z` | `"no"` (`uygulama-katman`) |
| **`bazarr`** | `lscr.io/linuxserver/bazarr:latest` | `bridge`<br>`127.0.0.1:16767->6767/tcp` | `1g` | `/srv/appdata/bazarr:/config:Z`<br>`/mnt/sidemain/media/movies:/movies:Z`<br>`/mnt/sidemain/media/series:/tv:Z` | `"no"` (`uygulama-katman`) |
| **`subgen`** | `mccloud/subgen:latest` | `bridge` (`runtime: nvidia`)<br>`127.0.0.1:18091->9000/tcp` | `4g` | `/mnt/sidemain/media/series:/tv:Z`<br>`/mnt/sidemain/media/movies:/movies:Z` | `"no"` (`uygulama-katman`) |
| **`jellyfin`** | `lscr.io/linuxserver/jellyfin:latest` | `bridge` (`cpus: 2.0`)<br>`127.0.0.1:18096->8096/tcp` | `2g` | `/srv/appdata/jellyfin:/config`<br>`/mnt/sidemain/media/series:/tv`<br>`/mnt/sidemain/media/movies:/movies`<br>`/dev/shm:/transcode` | `"no"` (`uygulama-katman`) |
| **`plex`** | `lscr.io/linuxserver/plex:latest` | `host` (`runtime: nvidia`)<br>Doğrudan `:32400` | `2g`<br>(`swap: 2g`) | `/srv/appdata/plex:/config`<br>`/mnt/sidemain/media/series:/tv`<br>`/mnt/sidemain/media/movies:/movies`<br>`/dev/shm:/transcode`<br>Cihaz: `/dev/dri:/dev/dri` | `unless-stopped` |

---

## 2. Servis Bazlı Compose ve Mimari Detayları

### 2.1. Gluetun, Transmission, Prowlarr ve FlareSolverr (VPN Kümesi)
- **Gluetun (`/opt/stacks/gluetun/compose.yaml`):**
  - Sağlayıcı olarak **Mullvad VPN** (`VPN_TYPE=wireguard`, `SERVER_COUNTRIES=Sweden`, `BLOCK_IPV6=on`) kullanır.
  - WireGuard özel anahtarı güvenlik sıkılaştırması (`2026-10-20`) kapsamında compose dosyasından çıkarılıp `/opt/stacks/gluetun/.env` (`chmod 600`) dosyasına taşınmıştır.
  - `FIREWALL_OUTBOUND_SUBNETS=192.168.0.0/24,172.16.0.0/12` ayarı sayesinde Prowlarr, VPN içinden yerel Docker ve LAN ağındaki Sonarr/Radarr'a erişebilir.
- **Transmission (`/opt/stacks/transmission2/compose.yaml`):**
  - `network_mode: "container:gluetun"` ile tüm torrent trafiği zorunlu olarak Mullvad WireGuard tünelinden geçer.
  - İndirmeler ikinci fiziksel disk olan `/mnt/side/downloads` dizinine yazılır; böylece sistem SSD'si (`/`) ve ana medya diski (`/mnt/sidemain`) yoğun torrent G/Ç yükünden korunur.
  - `/usr/local/sbin/torrent-bekci.sh` (`torrent-bekci.timer`, 20 saniyede bir) Transmission kuyruğunu ve dosya listelerini yasaklı terimlere karşı denetler.
- **Prowlarr (`/opt/stacks/prowlarr/compose.yaml`) & FlareSolverr (`/opt/stacks/flaresolverr/compose.yaml`):**
  - Prowlarr `FLARESOLVERR_URL=http://flaresolverr:8191` ortam değişkeniyle Cloudflare korumalı tracker'ları çözer.
  - Jackett (`/opt/stacks/jackett/compose.yaml`, `127.0.0.1:19117->9117`, `AUTO_UPDATE=true`) ek Torznab kaynakları için yedek/yardımcı indexer olarak çalışır.

### 2.2. Sonarr, Radarr, Bazarr ve Subgen (*arr ve Altyazı Kümesi)
- **Sonarr (`/opt/stacks/sonarr/compose.yaml`) & Radarr (`/opt/stacks/radarr/compose.yaml`):**
  - Her iki servis `PUID=1000`, `PGID=1000`, `TZ=Europe/Istanbul` ve `mem_limit: 768m` ile sınırlandırılmıştır.
  - `127.0.0.1:18989:8989` (Sonarr) ve `127.0.0.1:17878:7878` (Radarr) portları host üzerinde `uygulama-katman` systemd soketleri tarafından dinlenir; dışarıdan `sonarr.gokalpgoksu.com` ve `radarr.gokalpgoksu.com` adresleri `giris` nginx Basic Auth arkasından yönlendirilir.
- **Bazarr (`/opt/stacks/bazarr/compose.yaml`):**
  - `127.0.0.1:16767:6767` portunda çalışır (`mem_limit: 1g`). Hem `/mnt/sidemain/media/movies:/movies:Z` hem de `/mnt/sidemain/media/series:/tv:Z` dizinlerine yazma yetkisi vardır.
- **Subgen (`/opt/stacks/subgen/compose.yaml`):**
  - Yapay zeka tabanlı ses-metin (Whisper) altyazı üreticisidir.
  - `WHISPER_MODEL=large-v3-turbo`, `USE_GPU=true`, `TRANSCRIBE_DEVICE=cuda`, `PREFERRED_AUDIO_LANGUAGES=eng`, `TRANSCRIBE_OR_TRANSLATE=translate`, `NAMESUBLANG=en` ayarlarıyla çalışır.
  - Bellek taşmasını (OOM) önlemek için `CONCURRENT_TRANSCRIPTIONS=1` ve `mem_limit: 4g` uygulanmıştır (`2` olduğunda 4 GB sınırını aşıp OOM oluyordu).
  - `W11-GPU` sanal makinesi açıldığında libvirt kancası (`/etc/libvirt/hooks/qemu` ve `ai-vm-koruma.sh`) tarafından otomatik olarak durdurulur.

### 2.3. Jellyfin ve Plex (Medya Sunucuları)
- **Jellyfin (`/opt/stacks/jellyfin/compose.yaml`):**
  - `127.0.0.1:18096:8096` portunda, `mem_limit: 2g` ve `cpus: 2.0` sınırı ile **CPU modunda** çalışır; bu sayede `W11-GPU` sanal makinesi ekran kartını devraldığında bile Jellyfin kesintisiz hizmet vermeye devam eder.
  - Sağlık denetimi: `curl -fsS -m 8 http://localhost:8096/health` (`interval: 60s`).
  - Geçici kod çözme (transcode) dosyaları SSD ömrünü tüketmemek için RAM diske (`/dev/shm:/transcode`) yazılır.
- **Plex (`/opt/stacks/plex/compose.yaml`):**
  - `network_mode: host` ve `runtime: nvidia` (`NVIDIA_DRIVER_CAPABILITIES=compute,video,utility`, `/dev/dri:/dev/dri`) ile doğrudan GTX 1660 Ti donanım hızlandırmasını kullanır.
  - Sağlık denetimi: `curl -fsS -m 8 http://localhost:32400/identity`.
  - Hem Jellyfin hem de Plex aynı `/mnt/sidemain/media/series` ve `/mnt/sidemain/media/movies` kütüphanelerini paylaşır.
