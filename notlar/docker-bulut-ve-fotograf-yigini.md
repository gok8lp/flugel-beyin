---
tur: not
etiketler:
  - flugelserver
  - docker
  - nextcloud
  - immich
  - postgres
  - redis
  - cuda
  - bulut
olusturma: 2026-11-11
guncelleme: 2026-11-11
---

# Docker Bulut Depolama (Nextcloud) ve Fotoğraf (Immich CUDA) Yığını

> **Üst Harita ve Kök Bağlantılar:** [[HARITA]] · [[hafiza]] · [[kararlar]] · [[dersler]] · [[simdi]]
> **İlgili Wiki Sayfaları:** [[wiki/flugelserver-docker-uygulamalari]] · [[wiki/flugelserver-uygulama-baglantilari]] · [[wiki/flugelserver-dosya-agaci-ve-diskler]] · [[wiki/ikinci-beyin-sistemi]]
> **İlgili Notlar:** [[notlar/docker-uygulama-baglanti-topolojisi]] · [[notlar/flugelserver-uc-disk-ve-klasor-agaci]] · [[notlar/sunucu-yedekleme-ve-systemd-otomasyonlari]] · [[notlar/sanal-makineler-w11-gpu-ve-moonlight]]
> **İlgili Projeler:** [[projeler/flugel-sunucu-ve-akis]] · [[ikinci-beyin-sistemi]]

---

## 1. Bulut ve Fotoğraf Konteynerleri Özet Tablosu

`flugelserver` üzerindeki en kritik kişisel veriler (fotoğraflar, videolar, belgeler, ders notları ve Obsidian ikinci beyin vault'u) `/mnt/sidemain` diski üzerinde çalışan **Nextcloud** ve **Immich** yığınlarında barındırılır:

| Konteyner | İmaj | Port Eşlemesi | Bellek & GPU Sınırı | Kalıcı Disk Bağlamaları (Volumes) | Sağlık Denetimi (Healthcheck) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`nextcloud`** | `lscr.io/linuxserver/nextcloud:latest` | `127.0.0.1:8443->443/tcp`<br>`192.168.0.15:8443->443/tcp` | `1536m` (CPU) | `/srv/appdata/nextcloud:/config`<br>`/mnt/sidemain/cloud/nextcloud:/data`<br>`/mnt/sidemain/photos/immich/library/admin:/immich-originals/Arsiv:ro`<br>`/mnt/sidemain/photos/immich/upload/27085ce0-8895-482e-8d17-b9aa827997c5:/immich-originals/Yeni Yuklenenler:ro` | `curl -fsSk -m 8 https://localhost/status.php` (`60s`) |
| **`nextcloud-db`** | `postgres:17-alpine` | İç ağ (`5432/tcp`) | `512m` (CPU) | `/srv/appdata/nextcloud-db:/var/lib/postgresql/data` | `pg_isready -U nextcloud -d nextcloud` (`10s`) |
| **`immich_server`** | `ghcr.io/immich-app/immich-server:release` | `0.0.0.0:2283->2283/tcp` | `3g` + NVIDIA GPU (`gpu, video, compute, utility`) | `/mnt/sidemain/photos/immich:/usr/src/app/upload`<br>`/etc/localtime:/etc/localtime:ro` | Yerleşik HTTP sağlık kontrolü (`healthy`) |
| **`immich_machine_learning`** | `ghcr.io/immich-app/immich-machine-learning:release-cuda` | İç ağ | `2g` + NVIDIA GPU (`gpu`, CUDA) | `/srv/appdata/immich/model-cache:/cache` | Yerleşik ML sağlık kontrolü (`healthy`) |
| **`immich_postgres`** | `ghcr.io/immich-app/postgres:14-vectorchord0.3.0-pgvectors0.2.0` | İç ağ (`5432/tcp`) | `1536m` (CPU) | `/srv/appdata/immich/postgres:/var/lib/postgresql/data` | Yerleşik Postgres sağlık kontrolü (`healthy`) |
| **`immich_redis`** | `docker.io/redis:6.2-alpine` | İç ağ (`6379/tcp`) | `256m` (CPU) | Docker volume (`/data`) | `running` |

---

## 2. Nextcloud Yapılandırması (`/opt/stacks/nextcloud/compose.yaml`)

### 2.1. Mimari ve Veritabanı Geçişi
- **PostgreSQL 17 Entegrasyonu:** Geçmişte (`2026-10-20`) Nextcloud SQLite (`owncloud.db`) kullanırken gece `04:30`'daki `kritik-yedek.sh` çalışması sırasında 5 `php-fpm` işçisinin tamamı veritabanı kilidinde (`Slow session_start`) takılıp `status.php`'nin 5 dakika yanıt vermemesine yol açmıştı.
- İlk aşamada `/srv/appdata/nextcloud/php/www2.conf` içinde `pm.max_children=10` ve `request_terminate_timeout=120s` yapılarak kilitlenme hafifletilmiş, ardından compose yığınına `nextcloud-db` (`postgres:17-alpine`, `service_healthy` bağımlılığıyla) eklenmiştir.
- **Kullanıcı Dosyaları ve OCC Tarama Kuralı:**
  - Kullanıcı dosyaları `/mnt/sidemain/cloud/nextcloud/flugel/files` altında bulunur (`Notes`, `Dersler`, `Basketbol`, `Okul`, `Belgeler`, `Yedekler`, `PC-Yedekleri/GOKALP`).
  - Sunucu diskine SSH veya `taildrop-nextcloud` servisiyle doğrudan dosya yazıldığında Nextcloud veritabanının haberdar olması için şu komut çalıştırılır:
    ```bash
    sudo docker exec -u abc nextcloud php /app/www/public/occ files:scan --path="flugel/files/<klasör>"
    ```
- **Immich Salt-Okunur Köprüsü:**
  - Nextcloud konteyneri, Immich'in iki ana fotoğraf klasörünü (`library/admin` ve `upload/27085ce0-8895-482e-8d17-b9aa827997c5`) kendi içine `/immich-originals/Arsiv:ro` ve `/immich-originals/Yeni Yuklenenler:ro` olarak **salt-okunur** bağlar. Böylece Nextcloud üzerinden fotoğraflar silinemez/bozulamaz ama tüm arşive klasör yapısıyla erişilebilir.
- **Tek Giriş (`tsidp`):** `extra_hosts` altında `idp.tail42f1f4.ts.net:100.119.135.23` tanımlıdır.

---

## 3. Immich ve CUDA Makine Öğrenmesi Yapılandırması (`/opt/stacks/immich_server/compose.yaml`)

### 3.1. Donanım Hızlandırma (GTX 1660 Ti 6 GB)
- **`immich-server`:** `runtime: nvidia` ve `capabilities: [gpu, video, compute, utility]` ile videoların donanımsal kodlamasını (NVENC/NVDEC) gerçekleştirir (`mem_limit: 3g`). Envanterde **14.866+** fotoğraf/video öğesi barındırdığı doğrulanmıştır.
- **`immich-machine-learning`:** Özel `release-cuda` imajını kullanır (`runtime: nvidia`, `mem_limit: 2g`, `IMMICH_TRITON_ENABLED=false`). Yüz tanıma, CLIP akıllı arama (vektör gömme) ve nesne sınıflandırma modelleri `/srv/appdata/immich/model-cache:/cache` üzerinde saklanır.
- **VM / GPU Koruması (`11-KAYNAK-KORUMA-2026-10-21.txt`):**
  - `W11-GPU` sanal makinesi başlatıldığında `/etc/libvirt/hooks/qemu` ve `/usr/local/sbin/ai-vm-koruma.sh` devreye girerek GTX 1660 Ti kartını serbest bırakmak için `immich_machine_learning` ve `immich_server` konteynerlerini geçici olarak durdurur; VM kapandığında otomatik yeniden başlatır.
  - Tüm VM'ler kapalı olsa bile sunucuda boş RAM (`MemAvailable`) `2500 MB` altına düşerse `immich_machine_learning` durdurulur ve RAM `4000 MB` üstüne çıktığında tekrar başlatılır.

### 3.2. Vektör Veritabanı (`immich_postgres`) ve Önbellek (`immich_redis`)
- **PostgreSQL 14 + VectorChord / pgvectors:** `ghcr.io/immich-app/postgres:14-vectorchord0.3.0-pgvectors0.2.0` imajı, CLIP görsel arama vektörlerini indekslemek için kullanılır (`mem_limit: 1536m`, veri yolu: `/srv/appdata/immich/postgres`).
- **Yedekleme Stratejisi:**
  - Veritabanı her gece `03:30` (`uygulama-yedek.py` -> `_flugel/pg-immich_postgres.sql`) ve `04:30` (`kritik-yedek.sh` -> `/mnt/side/backups/kritik/veritabanlari/pg-immich_postgres.sql`) zamanlayıcılarıyla tutarlı SQL dökümü olarak yedeklenir.
  - Fotoğraf dosyaları (`/mnt/sidemain/photos/immich`) hem `kritik-yedek.sh` ile `/mnt/side/backups/kritik/immich` dizinine (`rsync -aHAX --delete`, 30 günlük `.silinenler/` korumasıyla) hem de **Backrest (Restic)** ile `/mnt/side/restic` ve Google Drive depolarına yedeklenir.
