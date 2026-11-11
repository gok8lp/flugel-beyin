# Mimari Dönüşüm Raporu — FLUGEL sunucusu

19/20 Ekim 2026 gecesi. Hazırlayan: Claude. Sunucudaki ayrıntılı rehber: `/srv/rehber/`. Teknik harita: `/srv/dev/docs/INFRASTRUCTURE.md`.

## Özet

| Hedef | Sonuç |
|---|---|
| Webtop ve Kasm'ı tamamen kaldır | **Tamam.** Container, imaj, veri, servis, rota, bot komutu ve yedek kopyaları kaldırıldı; ~62 GB yer açıldı |
| Sunucudaki Eclipse'i kaldır | **Tamam.** Çalışma alanında proje yoktu |
| VM'ler yalnız istekle açılsın, 10 dk boşta kalınca kapansın | **Tamam ve canlı test edildi** |
| VM başına en fazla 2 geri dönüş yedeği | **Tamam.** W11 için ilk yedek alındı (50 GB) |
| Uygulama başına 3 (yer darsa 2) yedek | **Tamam.** 34 uygulama, 1,94 GB/çalışma |
| Bir yedeği her diske güncel tut | **Uygulamalar için tamam (3 disk).** VM yedeği sidemain'e sığmıyor; SSD'ye bilerek yazılmıyor |
| Çalışan veritabanlarını tutarlı yedekle | **Tamam.** `pg_dumpall` ve SQLite `.backup` |
| Güvenlik: File Browser, Samba, Cloudflare | **Tamam** |
| Suwayomi sabit IP bağımlılığı | **Tamam** |
| Eclipse projelerini sunucuya sürümlü al | **Sunucu tarafı hazır.** Windows'ta kurulum betiğinin bir kez çalıştırılması gerekiyor |
| Kök dizin FHS düzeni | **Kısmi.** 6 uygulama `/srv/appdata`'ya taşındı; geri kalanı `/arrapps`'ta |
| `side`/`sidemain` klasör düzeni | **Yapılmadı.** Taşıma komutları izin denetimince engellendi |
| Rehber, ana sayfa, Telegram | **Tamam** |

## 1. Neyi, nereden nereye, neden?

### 1.1 Kaldırılanlar

- **Kaldırılan bileşenler:**
  - `webtop`, `kasm` ve `eclipse` container'ları ile `lscr.io/linuxserver/{kasm,webtop}` imajları (8,5 GB).
  - `/opt/stacks/{kasm,webtop,eclipse,anahtar}`; `kasm` tek başına 27 GB'tı.
  - `/srv/dev/tools/eclipse` ve `/srv/dev/workspaces/eclipse`.
- **Kaldırılan systemd servisleri:** `flugel-kasm`, `flugel-webtop` ve `flugel-anahtar`. Sonuncusu web üzerinden root `systemctl start` yapabilen bir HTTP servisiydi.
- **Kapatılan erişim yolları:** Tailscale 13443, 36443 ve 40443 portları, nginx'teki Webtop ve Kasm sunucu blokları, Cloudflare'deki `webtop` ve `kasm` alt alan adları, Telegram'daki `/webtop` ve `/kasm` komutları.
- **Neden:** Kasm ayrıcalıklı (privileged) çalışıyor ve kendi içinde Docker barındırıyordu. 1,9 GB RAM tüketiyordu ve sürekli bakım yükü getiriyordu. Eclipse VM'ye taşınacak.

### 1.2 Kök dizin (FHS)

| Nereden | Nereye | Neden |
|---|---|---|
| `/home/flugel/adguard` | `/srv/appdata/adguard` | Üretim DNS'i bir kullanıcının ev dizininde durmamalı |
| `/DATA/AppData/filebrowser` | `/srv/appdata/filebrowser` | Kökte uydurma bir dizin yerine standart yer |
| `/portainer/Files/AppData/Config/checkcle` | `/srv/appdata/checkcle` (+ `/opt/stacks/checkcle/compose.yaml`) | Yığın Portainer'in iç volume'unda gizliydi |
| `/opt/stacks/{guacamole/veri,suwayomi/veri,libreoffice/config}` | `/srv/appdata/<app>` | Tanım (compose) ile durum verisi ayrıldı |
| `~/sistem-bakim/durum` | `/var/lib/flugel/durum` | Servis durum verisi `/var/lib` altına aittir |
| Kullanılmayan 5 yığın, ev dizinindeki 4 eski yığın | `/srv/archive/stacks/` | Silinmedi; arşivlendi |
| `.deb` dosyaları, wgcf | `/srv/archive/installers`, `/srv/archive/security` (700) | Kurulum dosyaları yığın klasöründe durmamalı |
| LUKS başlık yedeği (`~/backups`) | `/srv/archive/security/luks/` (700) | Kritik kurtarma dosyası korumalı bir yerde olmalı |
| Ev dizinindeki eski yedekler (Nextcloud Mayıs, Immich DB) | `/srv/archive/backups/` | 4 birebir kopya tespit edilip silindi (önce `cmp` ile karşılaştırıldı) |
| `~/yedek` (PC yedekleri) | `/srv/archive/pc-yedekleri` | Sağlıklı SSD'de kaldı |
| `~/sistem-bakim` ve yığınlardaki ~70 eski sürüm/yedek dosyası | `/srv/operations/history/` | Çalışan klasörler temizlendi; geçmiş korundu |
| `/W11`, `/downloads` (boş) ve libvirt `downloads` havuzu | — | Boş ve kullanılmıyordu |

Her taşıma aynı dosya sistemi içinde anlık bir yeniden adlandırmaydı (`mv`); veri kopyalanmadı. Eski yollara sembolik link bırakıldı. Tam liste `/srv/operations/changes/2026-10-20-fhs/manifest.tsv` dosyasında.

### 1.3 Yedekleme mimarisi (yeni)

Önceden tek bir `rsync` aynası vardı. Bu ayna çalışan veritabanlarını dosya düzeyinde kopyalıyordu; bu yüzden geri yükleme garantisi yoktu. Şimdi katmanlı bir yapı var:

1. **Uygulama arşivi (gece 03:30).** Her Compose projesi için tek `.tar.zst` dosyası alınıyor. PostgreSQL için `pg_dumpall`, SQLite için tutarlı `.backup` kopyası arşivde dosyanın orijinal yolunda duruyor; geri yüklemek için `tar -x -C /` yetiyor. Saklama 3 sürüm; bütçe aşılırsa otomatik olarak 2'ye düşüyor. En yeni arşiv 3 diske de yazılıyor; her diske yazmadan önce %90 doluluk sınırı kontrol ediliyor.
2. **VM geri dönüş yedeği.** VM kapalıyken alınıyor, yani tutarlı. Disk, XML, UEFI NVRAM ve TPM durumu birlikte saklanıyor. BitLocker anahtarı TPM'de olduğu için TPM yedeklenmeseydi geri yüklenen disk açılmazdı. Saklama 2 sürüm.
3. **Kritik ayna.** Mevcut yapı korundu; aynalamadan önce tutarlı veritabanı dökümleri alınıyor.
4. **Eclipse projeleri.** Windows'tan gelen veri `/srv/project/gelen`'e düşüyor, gece hardlink'li sürüm alınıyor.

### 1.4 Güvenlik

- **File Browser:**
  - Önce: kimlik doğrulama yoktu (`noauth`), root olarak tüm `/` yazılabilirdi ve servis `0.0.0.0`'da yayındaydı. Yani yerel ağdaki herhangi bir cihaz sunucuyu tamamen ele geçirebilirdi.
  - Şimdi: `flugel` kullanıcısıyla çalışıyor, yalnız veri diskleri ve `/srv/dev` görünüyor, port yalnız `127.0.0.1`'de. Erişim yalnız Tailscale üzerinden.
- **Samba:** Misafir erişimi ve `0777` izinleri kaldırıldı; yalnız `flugel` girebiliyor. Bağlantı yalnız LAN, VM ağı ve Tailscale'den kabul ediliyor. Yapılandırma dosyasındaki bozuk satır (`nano /etc/samba/smb.conf[print$]`) da temizlendi.
- **Cloudflare:** Yerel `config.yml` dosyası artık çalışan uzak yapılandırmanın birebir kopyası. Rotaların panelden yönetildiği dosyada açıkça yazıyor; eski `code`, `plex` ve `files` kayıtları kaldırıldı.
- **Gluetun:** WireGuard özel anahtarı compose dosyasından `.env`'e (600) taşındı (12-Factor: yapılandırmayı ortamda tut).
- **Suwayomi:** `172.17.0.2` sabit IP'si yerine gluetun'un yalnız localhost'a yayınladığı `127.0.0.1:4567` kullanılıyor. Container IP'si değişse de bağlantı kopmuyor.
- **Cron:** Haftalık `docker system prune -f` durmuş container'ları da siliyordu (Suwayomi dahil). Yerine yalnız imaj ve önbellek temizliği koyuldu.

### 1.5 Sanal makineler

- **Otomatik açılış:** Hiçbir VM sunucu açılışında başlamıyor; `mullvad-ts`'in otomatik açılışı da kapatıldı.
- **Boşta izleme:** Dakikalık izleme ağ, disk ve konsol bağlantısına bakıyor. CPU bilerek sayılmıyor, çünkü donmuş bir Windows bir çekirdeği boşa döndürür.
- **Canlı test:** W11-GPU 18 Ekim'den beri donmuştu ve 4 GB RAM ile GPU'yu boşuna tutuyordu. Sistem iki ACPI isteği gönderdi, yanıt alamayınca VM'yi zorla kapattı. GPU ana makineye döndü, GPU uygulamaları sağlıklı başladı, kullanılabilir RAM 1,2 GB'tan 6,7 GB'a çıktı ve ilk yedek alındı.

## 2. Hatalar ve dürüst kayıt

1. **Taşıma betiği hatası (23:47).** Betik `/srv/appdata` klasörünü taşımadan önce kendisi oluşturdu; bu yüzden `/arrapps` taşınmadı ama compose dosyaları yeni yolu gösterdi. 16 container yaklaşık 4 dakika boş ayar klasörüyle çalıştı. Fark edildi ve geri alındı:
   - Compose dosyaları taşıma öncesi haline döndürüldü.
   - Servisler gerçek verileriyle yeniden başlatıldı. Doğrulama: Immich'te 15.101 öğe ve 3 kullanıcı, Nextcloud `installed:true`, *arr servisleri yanıt veriyor.
   - Bu sürede yanlışlıkla oluşan klasörler silinmedi, karantinaya alındı.

   Veri kaybı yok.
2. **Disk darboğazına benim yol açtığım an.** Yedek testi, 50 GB'lık VM kopyasını düşük öncelik olmadan SSD'ye yazdı ve sunucu yükü 84'e çıktı. Kopya durduruldu; SSD artık VM kopyası için hedef değil.
3. **Uzak komut tırnaklama hataları.** Birkaç komut yanlış tırnaklandı. Bir kontrol betiği `r` ile biten satırların son harfini sildi; etkilenen dosyalar yeniden kuruldu ve doğrulandı.
4. **İzin denetimi.** Taşıma komutları iki kez engellendi. Engeli aşmaya çalışılmadı; sistem tutarlı bir ara durumda bırakıldı.

## 3. Yapılamayanlar ve nedenleri

- **`/arrapps` → `/srv/appdata` taşımasının geri kalanı ve disk içi klasör düzeni:** izin denetimi bu tür işlemleri engelledi. Hazır betik ve plan `/srv/rehber/09-BILINEN-SORUNLAR.txt` dosyasında.
- **TRIM düzeltmesi:** Şifreli kök diskte `crypttab` + `initramfs` değişikliği ve yeniden başlatma gerekiyor. Başında kimse yokken yapılacak bir hata sunucuyu uzaktan açılmaz hale getirebilir; bu yüzden yapılmadı.
- **VM'den sunucuya çevrimdışı proje eşitlemesi:** Windows C: sürücüsü BitLocker ile şifreli, sunucu bu diski okuyamıyor. Yerine VM içinden çalışacak bir eşitleme kuruldu.
- **Eclipse Oomph/Kate sorunu:** Sunucudaki Eclipse kaldırıldığı için düzeltilmedi.
- **Tam sunucu yeniden başlatma testi:** Gözetimsiz yapılmadı.

## 4. En önemli bulgu

Sunucunun kronik "disk I/O baskısı"nın en güçlü açıklaması sistem SSD'si:
- Disk DRAM'siz bir Kingston A400 ve LUKS katmanında TRIM kapalı.
- 18.025 saat çalışmış, 86 TB yazılmış, ömrünün %22'si gitmiş.
- Uzun yazmalarda saniyede 7–9 MB'a düşüp 4,7 saniye gecikmeyle %100 kullanıma kilitlendiği ölçüldü.

Bu düzeltilmeden "hiçbir darboğaz olmasın" hedefi karşılanamaz.
