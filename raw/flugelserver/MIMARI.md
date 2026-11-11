# Mimari — sabit yollar ve bağımlılıklar

Kaynak: 18–20 Ekim denetimleri + `veri/guncel.json`. Değişken durum için snapshot tarihine bak.

## Dosya yerleşimi

- `/opt/stacks/<uygulama>/compose.yaml`: çoğu Compose stack'i. Bazılarında dosya adı `docker-compose.yml`; kesin yol için `sor.py app` kullan.
- `/arrapps/compose`: Jellyfin, Ollama/Plex gibi eski Compose tanımları. `/arrapps/<app>` çoğunlukla config/DB; tek başına tüm içerik değildir.
- `/mnt/sidemain/books`: Komga/Kavita kitap-manga kaynağı. Suwayomi indirmeleri `books/manga/suwayomi`, KamiYomu `books/manga/kamiyomu`, Openbooks `books/ln`.
- `/mnt/sidemain/{movies,series}`: büyük medya. `/mnt/sidemain/immich`: fotoğraf yüklemeleri; `/mnt/sidemain/nextcloud_data`: Nextcloud kullanıcı verisi.
- `/mnt/side/downloads`: indirme alanı. `/mnt/side/yedek/kritik`: mevcut kritik rsync yedeği.
- `/srv/dev/{projects,workspaces,artifacts,tools,docs,archive}`: yeni geliştirme düzeni. Canlı uygulamalar topluca buraya taşınmadı.
- `/srv/operations/{changes,inventory,sunucu-kilavuzu}`: geri dönüş kopyaları, denetimler, durum notu. Henüz eksiksiz sunucu kılavuzu değil.
- `/var/lib/libvirt/images/w11`: W11 ve W11-GPU'nun ORTAK diski. `mullvad-ts.qcow2`: ayrı Linux VM. NVRAM yollarını snapshot'tan al.
- `named volume` kaynakları `veri/guncel.json` içinde. Container içindeki `/config` ile host yolunu karıştırma.

## Ağ

- Tailscale Serve: özel HTTPS uçlarını localhost/container upstream'lere taşır. HTTPS portu ile container portu aynı şey değildir.
- Önceden mevcut Funnel443 -> Jellyfin8096 ve10000 -> Immich2283 publicti. Güncel Serve JSON'unu kontrol et; bütün Tailscale uçlarına “özel” deme.
- Cloudflare hostname'leri mevcut ingress üzerinden yayınlanır; alternatif link bulunması korumanın/oturumun test edildiği anlamına gelmez.
- Gluetun, Mullvad çıkışı sağlar. Suwayomi, Transmission/Prowlarr gibi uygulamalar bu ağla ilişkili. Suwayomi proxy hedefi172.17.0.2:4567 olarak kurulmuştu; container IP değişebilir. Doğrulamadan sabit IP'yi kalıcı gerçek kabul etme.
- Guacamole HTTPS11443; guacd host networking. Windows VNC bağlantısı localhost5900'e kuruldu. Libvirt VNC autoport nedeniyle yeniden başlatınca `virsh domdisplay` tekrar doğrulanmalı.

## GPU

- GTX1660 Ti, PCI29:00.x. `/etc/libvirt/hooks/qemu` GPU'yu VM/host arasında geçirir; `/usr/local/bin/self-heal.sh` ile birlikte değerlendirilir.
- Hook listesi: ollama, plex, immich_machine_learning, subgen. Liste bütün GPU bağımlılıklarını kapsıyor diye varsayma; örneğin Immich server'ın DeviceRequests alanını da kontrol et.
- Jellyfin CPU moduna geçirildi; Windows VM ile beraber çalışabilir. Donanım transcode kapalı, gerçek medya oynatma testi tamamlanmadı.
- Hook'un varlığı başarılı rollback/yeniden başlatma testi değildir. GPU'lu VM'ye zorla managedsave/shutdown uygulama.

## Yedekler

- `/usr/local/sbin/kritik-yedek.sh`, `kritik-yedek.timer`: günlük rsync, `/mnt/side/yedek/kritik`. Değişen/silinenler `.silinenler/<tarih>` altında30gün tutulacak şekilde yazılmış.
- Immich/Nextcloud kullanıcı verisi, ayarlar ve `/srv/dev` (tools/artifacts hariç) kapsanacak şekilde düzenlenmişti. Güncel script ve son çalışmayı doğrula.
- Bu yapı DB-tutarlılığı/uygulama başına3 sürüm/VM snapshot/üç diske kopya garantisi değildir. Gerçek geri yükleme testi yapılmadı.
- `/srv/dev/archive/code-server-20261020` ve `tranga-20261020`: kaldırılan uygulamaların korunan ayar/verileri; tek yedek olarak kabul etme.
- Bütün medyanın her diske sığacağı doğrulanmadı. Kopyalama öncesi kapasite, rezerv alan ve uygulama-tutarlı yöntem belirlenmeli.
