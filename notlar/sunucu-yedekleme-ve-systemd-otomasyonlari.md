---
tur: not
etiketler:
  - flugelserver
  - yedekleme
  - systemd
  - timer
  - otomasyon
  - self-heal
  - ai-gozcu
  - backrest
olusturma: 2026-11-11
guncelleme: 2026-11-11
---

# flugelserver Yedekleme Mimarisi ve Systemd Otomasyon Zamanlayıcıları

> **Üst Harita ve Kök Bağlantılar:** [[HARITA]] · [[hafiza]] · [[kararlar]] · [[dersler]] · [[simdi]]
> **İlgili Wiki Sayfaları:** [[wiki/flugelserver-yedekleme-ve-otomasyon]] · [[wiki/flugelserver-genel-mimari]] · [[wiki/flugelserver-dosya-agaci-ve-diskler]] · [[wiki/sunucu-ve-github-commit-gecmisi]]
> **İlgili Notlar:** [[notlar/flugelserver-uc-disk-ve-klasor-agaci]] · [[notlar/sanal-makineler-w11-gpu-ve-moonlight]] · [[notlar/docker-bulut-ve-fotograf-yigini]] · [[notlar/docker-ag-panel-ve-altyapi-yigini]]
> **İlgili Projeler:** [[projeler/flugel-sunucu-ve-akis]]

---

## 1. Dört Katmanlı Yedekleme Mimarisi

`flugelserver` üzerinde veri kaybını önlemek için uygulama arşivleri, kritik veri aynası, sanal makine imajları ve şifreli Restic/Backrest depolarından oluşan dört katmanlı bir yedekleme yapısı çalışır:

### 1.1. Katman 1: Gece Uygulama Yedekleri (`/usr/local/sbin/uygulama-yedek.py` — `03:30`)
- **Zamanlayıcı:** `uygulama-yedek.timer` (her gece `03:30`, günlük: `/var/log/uygulama-yedek.log`).
- **Yedek Konumları:**
  - **Birincil Arşiv (Ana Kopya):** `/mnt/side/backups/uygulamalar/<uygulama>/<uygulama>_<tarih>.tar.zst` (36 uygulama yığını; ör. `2026-11-02_0334`, `2026-11-03_0335`, `2026-11-04_0334`, toplam `8.41 GiB`).
  - **Güncel Kopyalar:** `/srv/backups/current/uygulamalar/<uygulama>.tar.zst` (SSD) ve `/mnt/sidemain/backups/current/uygulamalar/<uygulama>.tar.zst` (ana veri diski). *Not:* Hedef disk `%90` doluluk sınırını aşacaksa güncel kopya yazımı otomatik olarak `ATLANDI` olarak işaretlenir ve ana kopya `/mnt/side` üzerinde güvende tutulur.
- **Saklama Kuralı:** Uygulama başına **3 sürüm** tutulur. Toplam arşiv boyutu `25 GiB`'ı veya tek bir arşiv `3 GiB`'ı aşarsa otomatik olarak **2 sürüme** düşer.
- **Arşiv İçeriği ve Tutarlı Veritabanı Dökümü:**
  - `/opt/stacks/<uygulama>` compose klasörü + `/srv/appdata/<uygulama>` ayar dizini + Docker volume'ları + `_flugel/BILGI.json`.
  - **PostgreSQL:** Konteyner çalışırken `pg_dumpall` ile tutarlı SQL dökümü (`_flugel/pg-<container>.sql`) alınır.
  - **SQLite:** Parça parça tutarlı `.backup` kopyası alınır (`2026-10-20 06:51` düzeltmesiyle Nextcloud SQLite kilitlenmesi önlenmiştir).
- **Adım Adım Geri Yükleme Prosedürü (`04-YEDEKLER.txt`):**
  ```bash
  sudo docker compose -f /opt/stacks/<uygulama>/compose.yaml stop
  sudo tar --zstd -xpf <arşiv.tar.zst> -C /
  # PostgreSQL varsa:
  tar --zstd -xOf <arşiv.tar.zst> _flugel/pg-<c>.sql | sudo docker exec -i <c> psql -U <kullanıcı> -d postgres
  sudo docker compose -f /opt/stacks/<uygulama>/compose.yaml up -d
  ```

### 1.2. Katman 2: Kritik Veri Aynası (`/usr/local/sbin/kritik-yedek.sh` — `04:30`)
- **Zamanlayıcı:** `kritik-yedek.timer` (her gece `04:30`, ayrıca SSD için `kritik-yedek-ssd.sh`).
- **Hedef:** `/mnt/side/backups/kritik/` (ikinci fiziksel disk).
- **Çalışma Sırası:**
  1. **Tutarlı Veritabanı Dökümleri:** Aynalamadan hemen önce `/mnt/side/backups/kritik/veritabanlari/` altına `pg-immich_postgres.sql`, `pg-guac-db.sql` ve `nextcloud-owncloud.db` dökümleri alınır.
  2. **`rsync -aHAX --delete` Aynalama:**
     - `/mnt/sidemain/photos/immich` (küçük resimler ve yeniden kodlanmış videolar hariç)
     - `/mnt/sidemain/cloud/nextcloud` (Nextcloud kullanıcı dosyaları)
     - `/mnt/sidemain/personal` (`usa`, `yedek-amk`)
     - `/srv/appdata`, `/opt/stacks`, `/etc`, `/srv/dev`
  3. **30 Günlük Silinenler Koruması:** Silinen veya üzerine yazılan her dosya **30 gün** boyunca `/mnt/side/backups/kritik/.silinenler/<tarih>/` altında saklanır.
  4. **Acil Kip (`kritik-yedek.sh --acil`):** `disk-koruyucu.sh` bir diskte kritik SMART/I/O arızası tespit ettiğinde yalnız fotoğrafları ve kişisel belgeleri en hızlı şekilde sağlam diske kaçırmak için kullanılır.

### 1.3. Katman 3: Backrest / Restic Şifreli Yedekleme (`/opt/stacks/backrest` & `flugel-yedek`)
- **Backrest (`:9898`):** Restic tabanlı şifreli yedekleme arayüzüdür.
  - **Yerel Depo:** `/mnt/side/restic/yerel` (ilk tam yedek `074ea935`, `266 GiB` + `/srv/geri-yukleme/test-20261105-1813` geri yükleme testi başarılı).
  - **Bulut Depo (`drive`):** `rclone` üzerinden Google Drive'a şifreli Restic yedeklemesi (sunucu dışı / offsite yedek ihtiyacını karşılar).
  - Depo parolaları `/etc/sistem-bakim/restic/*.pass` (`chmod 600 root`) altında korunur; metrikler `/var/lib/node_exporter/textfile` üzerinden Grafana'ya aktarılır.

### 1.4. Katman 4: Sanal Makine ve Eclipse Proje Yedekleri
- **VM Yedekleri (`/usr/local/sbin/vm-yedek.sh`):** `/mnt/side/backups/vm/{w11,mullvad-ts}/<tarih>/` altında en fazla 2 sürüm tutulur.
- **Eclipse Sürümleri (`/usr/local/sbin/proje-surum.sh` — `02:30`):** `/srv/project/gelen/` altındaki Windows VM projelerini her gece `/srv/project/surumler/<tarih>` altına hardlink ile sürümler.

---

## 2. Kendini Onarma, Gözcü ve Güvenlik Betikleri (`/usr/local/sbin` & `/usr/local/bin`)

### 2.1. `/usr/local/bin/self-heal.sh` (`self-heal.timer` — 3 Dakikada Bir)
- Çöken kritik systemd servislerini ve hata koduyla (`Exited != 0`) çıkan veya 10 dakika boyunca `unhealthy` kalan Docker konteynerlerini otomatik yeniden başlatır.
- **Kritik İyileştirme (`2026-10-20`):** `restart: "no"` olan (`uygulama-katman` tarafından yönetilen) konteynerlere ve `/etc/sistem-bakim/bilerek-durdurulan` listesindeki servislere **dokunmaz**.
- Disk doluluğu `%90`'ı aşarsa otomatik önbellek/günlük temizliği başlatır.

### 2.2. `/usr/local/sbin/ai-gozcu.sh` (`ai-gozcu.timer` — 15 Dakikada Bir)
- Sunucu sağlık metriklerini kontrol eder; yalnız yeni bir sorun tespit edildiğinde veya günlük özette yerel **Ollama (`qwen3.5:4b`, `think` kapalı)** modeline danışarak Türkçe arıza açıklaması ve güvenli çözüm önerisi üretir.
- Bellek veya disk baskısı varsa (`MemAvailable` düşükse veya VM açıksa) Ollama'yı uyandırmaz; iş bitince modeli GPU VRAM'inden anında boşaltır.

### 2.3. Diğer Özel Bakım ve Koruma Betikleri
- **`/usr/local/sbin/kaynak-gozcu.sh` (`kaynak-gozcu.timer` — 2 dk):** Bellek baskısı (PSI), swap, açık VM'ler, GPU sıcaklığı ve OOM olaylarını izler, durum değişiminde bildirim atar.
- **`/usr/local/sbin/ai-vm-koruma.sh` (10 sn + libvirt hook):** VM çalışırken veya boş RAM `< 2500 MB` olduğunda AI konteynerlerini durdurur, RAM `>= 4000 MB` ve VM kapalı olduğunda geri başlatır.
- **`/usr/local/sbin/disk-koruyucu.sh` (`disk-koruyucu.timer` — 10 dk):** SMART hatalarını ve çekirdek I/O hatalarını izler; kritik arızada yazan servisleri durdurup diski salt-okunur yapar ve veriyi sağlam diske kaçırır.
- **`/usr/local/sbin/torrent-bekci.sh` (`torrent-bekci.timer` — 20 sn):** Transmission'daki torrentleri yasaklı terimlere karşı tarar, eşleşenleri durdurup `/mnt/side/karantina` altına alır ve bildirir.
- **`/usr/local/sbin/island-veri.py` (`island-veri.timer` — 20 sn):** CPU, RAM, disk, GPU, konteynerler, VPN, yedekler, VM'ler, basketbol atamaları ve anime takvimini `/var/lib/flugel/durum` altına JSON olarak yazar (`flugel-akis` `/api/island` uç noktası).
- **`/usr/local/sbin/uygulama-katman` & `uyg-bosta.timer` (5 dk):** Systemd soket aktivasyonuyla çalışan konteynerleri istek geldiğinde başlatır, boşta kaldığında durdurarak RAM tasarrufu sağlar.
- **`/usr/local/bin/bildirim`:** Merkezi bildirim aracı; mesajları Telegram'a ve `/var/lib/flugel/durum/bildirimler.log` dosyasına yazar (anahtarlar `/etc/sistem-bakim/bildirim.env` içinde `chmod 600 root` olarak korunur).

---

## 3. Aktif Systemd Zamanlayıcıları Tam Tablosu (`systemctl list-timers`)

Sunucu üzerinde aktif olan **51 systemd zamanlayıcısından** sunucu operasyonuna özel olanların çalışma takvimi:

| Zamanlayıcı (Timer) | Tetiklediği Servis | Çalışma Sıklığı / Saati | Görevi |
| :--- | :--- | :--- | :--- |
| `island-veri.timer` | `island-veri.service` | Her **20 saniye** | FLUGEL Island / Akış için canlı sistem durumu JSON üretimi |
| `torrent-bekci.timer` | `torrent-bekci.service` | Her **20 saniye** | Transmission torrent içerik güvenlik denetimi |
| `vm-bosta-kapat.timer` | `vm-bosta-kapat.service` | Her **1 dakika** | 10 dakika kullanılmayan VM'yi temiz ACPI ile kapatma |
| `giris-durum.timer` | `giris-durum.service` | Her **2 dakika** | Giriş sayfası canlı durum göstergelerini güncelleme |
| `kaynak-gozcu.timer` | `kaynak-gozcu.service` | Her **2 dakika** | RAM PSI, swap, OOM ve GPU sıcaklık denetimi |
| `self-heal.timer` | `self-heal.service` | Her **3 dakika** | Çöken servis ve konteynerleri otomatik onarma |
| `swap-flush.timer` | `swap-flush.service` | Her **5 dakika** | RAM müsait olduğunda swap sayfalarını RAM'e geri çekme |
| `docker-watcher.timer` | `docker-watcher.service` | Her **5 dakika** | Konteyner sağlık/çıkış kodu izleme ve bildirim |
| `uyg-bosta.timer` | `uyg-bosta.service` | Her **5 dakika** | Boşta kalan soket-aktif konteynerleri durdurma |
| `disk-koruyucu.timer` | `disk-koruyucu.service` | Her **10 dakika** | SMART ve I/O hata izleme, ölüm öncesi disk koruma |
| `vpn-ip-degistir.timer` | `vpn-ip-degistir.service` | **Saatlik** (`:48`) | Gluetun Mullvad VPN çıkış IP adresini yenileme |
| `basket-bot.timer` | `basket-bot.service` | **Saatlik** (`:00`) | TBF / Assignr basketbol hakem ve maç verilerini çekme |
| `anime-takip.timer` | `anime-takip.service` | **Saatlik** (`:05`) | Yeni anime bölümlerini takip etme ve `qwen3.5:4b` ile özetleme |
| `flugel-yedek.timer` | `flugel-yedek.service` | Her gece **`00:33` UTC** | Restic / merkezi sistem yedekleme görevi |
| `proje-surum.timer` | `proje-surum.service` | Her gece **`02:30` UTC** | `/srv/project` Windows Eclipse projelerini sürümleme |
| `uygulama-yedek.timer` | `uygulama-yedek.service` | Her gece **`03:30`** | 36 Docker uygulamasının `.tar.zst` ve DB döküm yedeği |
| `kritik-yedek.timer` | `kritik-yedek.service` | Her gece **`04:30`** | Immich, Nextcloud, kişisel belgeler ve ayarların `rsync` aynası |
| `rehber-guncelle.timer` | `rehber-guncelle.service` | Her sabah **`06:00` UTC** | `/srv/rehber` altındaki `CANLI` dokümanları yeniden üretme |
| `imdb-puan.timer` | `imdb-puan.service` | Her sabah **`06:24` UTC** | Medya arşivindeki dizi/filmlerin IMDb puanlarını güncelleme |
| `morning-report.timer` | `morning-report.service` | Her gün **`13:00` UTC** | Günlük sunucu sağlık, RAM, disk ve sıcaklık raporu |
| `virus-tarama.timer` | `virus-tarama.service` | **Çarşamba `02:00` UTC** | ClamAV ile indirmeleri tarama ve `/mnt/side/karantina`'ya alma |
| `flugel-yedek-kontrol.timer` | `flugel-yedek-kontrol.service` | **Cumartesi `02:00` UTC** | Yedek bütünlüğü ve geri yükleme doğrulama testi |
| `klasor-boyut.timer` | `klasor-boyut.service` | **Cumartesi `23:00` UTC** | Disk klasör boyutlarını ölçüp Prometheus `.prom` metriği üretme |
| `savunma-denetim.timer` | `savunma-denetim.service` | **Pazar `04:10` UTC** | Güvenlik duvarı, port ve izin sıkılaştırma denetimi |
| `weekly-maintenance.timer` | `weekly-maintenance.service` | **Pazar `05:00` UTC** | Haftalık paket güncelleme, log temizliği ve SSD TRIM |
| `disk-health.timer` | `disk-health.service` | **Pazar `10:00` UTC** | Haftalık ayrıntılı SMART disk sağlık raporu |
| `aylik-rapor.timer` | `aylik-rapor.service` | **Her ayın 1'i `06:00` UTC** | Aylık kapasite, yedek ve çalışma süresi özeti |
