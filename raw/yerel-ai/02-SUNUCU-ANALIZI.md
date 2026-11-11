# Home server analizi — 28 Ekim 2026

Kaynak: SV01/SV02. Sunucu saat dilimi çıktılarında UTC; kullanıcıya verilen tarihler Europe/Istanbul (+03:00). SSH anahtarıyla salt okunur bağlantı kuruldu. Analizde sunucu ayarı değiştirilmedi, servis/konteyner yeniden başlatılmadı.

## Platform ve erişim

`flugelserver`: Ubuntu 26.04.1 LTS, Linux 7.0.0-38-generic; Ryzen 5 2600X (6 çekirdek / 12 iş parçacığı), yaklaşık 16 GB RAM, GTX 1660 Ti 6 GB (sürücü 580.178.04). Gözlemde GPU 34°C. Docker'da 48 çalışan konteyner; 21 healthy, 27 sağlık denetimi tanımsız, 0 unhealthy. Bu, 48 uygulamanın işlevsel testten geçtiği anlamına gelmez.

LAN bağlantısı `flugel@192.168.0.15`; Tailscale bağlantısı `flugel@flugelserver.tail42f1f4.ts.net`. Yerel kimlik dosyası `~/.ssh/id_ed25519_homeserver` yolunda; anahtarın içeriği pakette yok. LAN bağlantısı bu anahtarla çalıştı. Tailscale SSH oturum doğrulaması istedi; bu kimlik denetimi Claude talimatıyla kaldırılmaz. Sunucuda `sudo -n` denetimi başarılı; PC'de başarısız. Yetkileri cihazlar arasında genelleme.

## Depolama ve veri haritası

| Yer | Boyut / kullanım | İşlev |
|---|---|---|
| `/` | 437 GB; 209 GB kullanılmış, 210 GB boş; %50 | İşletim sistemi, Docker imajları ve uygulama yapılandırmaları |
| `/mnt/side` | 458 GB; 250 GB kullanılmış, 185 GB boş; %58 | İndirmeler, watch klasörü, bazı yedekler |
| `/mnt/sidemain` | 916 GB; 776 GB kullanılmış, 94 GB boş; %90 | Büyük medya, kitap, fotoğraf ve bulut verileri |
| `/opt/stacks` | Compose proje klasörleri | Uygulamaların dağıtım tanımları |
| `/srv/appdata` | Uygulama kalıcı verileri | Veritabanları, ayarlar, AI modelleri |

Sistem diski KINGSTON SA400S3 yaklaşık 447 GiB; LUKS+LVM. Veri diskleri LUKS. Önemli ayrıntı: `/dev/mapper/sdd_crypt` bu gözlemde fiziksel `/dev/sda` üzerinde. Eski mapper adı `/dev/sdd` aygıtının bugün var olduğunu göstermez. Disk işleri için güncel lsblk ve sabit kimlikler doğrulanmalı.

SMART: sdb ve sdc genel sağlık sonucu PASSED. sda için attribute temelli PASSED alındı; denetleyici SMART status yanıtını tam sunmuyor. Tam SMART öznitelikleri, uzun test ve disk ömrü doğrulanmadı. PASSED disk kesin sağlam demek değildir.

Önemli eşlemeler:

- Jellyfin: `/srv/appdata/jellyfin` → `/config`; `/mnt/sidemain/media/movies` → `/movies`; series → `/tv`; `/dev/shm` → transcode.
- Plex de medya sunucusu; iki servisin kullanıcı için gerekliliği ayrıca kararlaştırılmalı.
- Nextcloud: `/srv/appdata/nextcloud` ayarlar; `/mnt/sidemain/cloud/nextcloud` kullanıcı verisi.
- Immich: `/mnt/sidemain/photos/immich` fotoğraflar; PostgreSQL/Redis eşlik ediyor.
- Komga ve Kavita: `/mnt/sidemain/media/books`; Suwayomi indirmeleri bunun manga/suwayomi altına gidiyor.
- Transmission: `/mnt/side/downloads`, `/mnt/side/watch`, `/srv/appdata/transmission`.
- Ollama: `/srv/appdata/ollama`; Open WebUI: `/srv/appdata/open-webui`.
- Özel AI kütüphanesi `/srv/appdata/ai-library`; Telegram köprüsü `/opt/telegram-kopru`; `telegram-kopru.service` ve `yz-tg.socket` aktif. Kütüphane içerikleri okunmadı; tamamının işlenmiş olduğu iddia edilmez.

## İş yükleri

Medya: Jellyfin, Plex, Sonarr, Radarr, Bazarr, Prowlarr, Jackett, Transmission/Gluetun, Subgen, Lingarr. Kitap/manga: Komga, Kavita, Suwayomi, OpenBooks. Kişisel veri: Nextcloud, Immich, FileBrowser. Yönetim: Dockge, Portainer, Cockpit, Dozzle, Beszel, Uptime Kuma, Homepage. Araçlar: ConvertX, Stirling PDF, IT-Tools, Guacamole, PairDrop, BookStack, GLPI. AI: Ollama, Open WebUI, yerel köprü ve kütüphane.

Ollama listesinde `qwen3.5:4b`, `translategemma:4b` ve bir özel llamacpp imaj/model etiketi var. Kurulu model görünmesi, çıkarım kalitesi veya hız testi yapıldığı anlamına gelmez.

Docker imajları 89.51 GB, raporlanan reclaimable 70.87 GB. Bunun tamamını temizlemek güvenli kabul edilmemeli; kullanılan katmanlar, rollback için tutulan imajlar ve build önbelleği ayrılmalı. Analizde prune yapılmadı. Subgen restart sayısı 7; AdGuard ve Cup 1'er. Sayaç geçmişi tek başına güncel crash loop kanıtı değil.

## Otomasyon ve sanallaştırma

50 sistem zamanlayıcısı görünüyor. self-heal, docker-watcher, swap-flush, disk-koruyucu, ai-gozcu, ai-vm-koruma, vm-bosta-kapat gibi özel servisler var. Otomatik yeniden başlatma ve kaynak temizleme kuralları birbirini etkileyebilir; arıza analizinde birden çok otomasyonun eşzamanlı çalışması hesaba katılmalı.

`vm-bosta-kapat.service` tekrar eden `virsh ... timed out after 30 seconds` hatası veriyor. Bağımsız `virsh -c qemu:///system list --all` denemesi de 8 saniyede sonuçlanmadı. libvirtd active; virtqemud inactive. Bu tek başına virtqemud'un yanlış kapalı olduğu anlamına gelmez; kullanılan libvirt daemon düzeni ve soketleri incelenmeli. VM envanteri doğrulanamadı, “VM yok” denmemeli. Bazı unit dosyaları disk üzerinde değişmiş ve systemd reload uyarısı var; analiz kapsamında reload yapılmadı.

RAM tek ölçümde yaklaşık 2.2 GB available'a kadar düştü; başka ölçümde 5.9 GB available görüldü. Swap kullanımı değişken. Bu, zamana bağlı basınç olduğuna işaret eder; tek gözlemden sürekli RAM yetersizliği hükmü verilmez. swap-flush gibi otomasyonlarla birlikte PSI/vmstat izlenmeli.

## Yedekleme ve ağ

uygulama-yedek, kritik-yedek ve vm-yedek-gunluk servislerinin son kaydı success/exit 0. `/mnt/side/backups`, `/mnt/sidemain/backups`, `/srv/backups`, `/srv/archive/backups` gibi dizinler var. İçerik bütünlüğü, harici/offsite kopya ve geri yükleme testi doğrulanmadı. Başarılı script çıkışı yedekten dönülebileceğinin kanıtı değil.

UFW aktif, gelen bağlantı varsayılanı deny; özel ağ ve Tailscale aralıklarına izin veriliyor. Docker DOCKER-USER zincirinde fiziksel enp37s0 arayüzünden LAN'a izin, diğer yeni trafiğe DROP var. Birçok Docker portu 0.0.0.0/:: üzerinde yayımlanıyor; dış internet erişimi yalnız buradan belirlenemez. Router port yönlendirmesi ve dış ağ taraması yapılmadı. SSH root login kapalı, anahtar ve parola girişi açık.

Uptime Kuma, Homepage, Portainer, Cup, Dozzle, Beszel agent ve Dockge Docker socket'ine mount alıyor. Konteynerler privileged görünmüyor; Docker socket erişimi yine yüksek yönetim yetkisidir. İhtiyaç ve read-only proxy seçenekleri ayrı incelenmeli.

## Ek ölçüm

İkinci kısa vmstat ölçümünde RAM available yaklaşık 6.4 GB, swap yaklaşık 3.35 GB kullanılmıştı. Bellek PSI avg60 some=1.31/full=1.22, avg10=0 görüldü. Tek kısa ölçüm ne sürekli sorun ne de tam sorunsuzluk kanıtıdır. FileBrowser loopback HTTP 200, doğru Tailscale HTTPS :26443 adresi 200 verdi.
