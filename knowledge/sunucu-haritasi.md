---
{
  "title": "flugelserver haritası",
  "tags": [
    "sunucu",
    "flugelserver",
    "harita"
  ],
  "remote_allowed": false
}
---
> Bu harita 2026-11-15 anlık kaydıdır; konteyner sayısı ve servisler değişti. Güncel durum: [[knowledge/sunucu-durum]] (günlük otomatik).

> Kaynak: 2026-11-15 sunucu derin taraması (indeks + 20 lane AI ordusu + çapraz kontrol + Codex Astra hakem). Ham raporlar ve sırları maskeli paketler: `~/Documents/ai_workplace/second-brain/raporlar/sunucu-envanter/` (vault dışı). Bu belge anlık durum garantisi değildir; canlı bilgi için `sunucu-indeks` kullan.
> **Güvenlik notu:** İlk taramada 3 özel anahtar (tsidp oidc-key.json, guacamole server-ed25519, ollama id_ed25519) maskelenmeden Codex/Gemini'ye gitti; 2026-11-15'te üçü de döndürüldü (bkz. tasks/sunucu-anahtar-dondurme, done). Bu not `remote_allowed: false`: Jev/TypeSafe'e gönderilmez.

# flugelserver — hakem haritası
Tarih: 15 Kasım 2026. Hazırlayan: Codex (hakem). Kapsam: 20 lane raporu, çapraz kontrol ve yerel kaynak paketler; sunucuya bağlanılmadı. Bu belge anlık canlı durum garantisi değildir.
Kanıt önceliği: tarihli çalışma zamanı/dosya içeriği > yapılandırma > bakım kaydı > lane yorumu. “Çalışıyor” süreç durumudur; “sağlıklı” yalnız healthcheck bulunan kayıtlarda kullanılır.
**P** = /home/gokalp/Documents/ai_workplace/second-brain/raporlar/sunucu-envanter/paketler. P/dosya:satır bu dizindeki kanıta gider.
**X** = /home/gokalp/Documents/ai_workplace/second-brain/raporlar/sunucu-envanter/capraz/x01-capraz.log. P/c04 gibi kısa atıflar, P altındaki aynı lane önekli tek .txt paketini belirtir. Diğer mutlak yollar aksi belirtilmedikçe sunucudadır.

## 1. Genel bakış

- Donanım: Ryzen 2600X, GTX 1660 Ti (6 GB), yaklaşık 16 GB fiziksel RAM; eski ölçümde toplam 15.399 MiB RAM ve 4.095 MiB swap. Ubuntu 26.04/x86_64 bilgisi işletim notundandır; güncel CPU/RAM kullanım ölçümü yok. Kanıt: P/g09-side-proje-dosya.txt:3373 (/mnt/side/files/notes/FLUGEL-OZET.md), P/g02-srv-dev-proje.txt:4286, /srv/rehber/01-HARITA.txt.
- VM tanımları: W11 ve W11-GPU aynı /var/lib/libvirt/images/w11 diskini paylaşır; rehbere göre eşzamanlı açılmayı kanca engeller. mullvad-ts ayrı VM'dir. GPU, host ile W11-GPU arasında geçirilir; güncel VM açık/kapalı durumu verilmemiştir.
- Disk modelleri 20 Ekim rehberinden; doluluklar **14 Kasım 2026 06:00** kaydından alınmıştır. Eski sdX adları güncel mapper adlarıyla birebir eşlenmemelidir.

| Bağlama | Fiziksel disk / rol | Kapasite | Kullanılan / boş | Doluluk |
|---|---|---:|---:|---:|
| / | Kingston A400 480 GB SSD; sistem, appdata, geliştirme, VM | 437G | 182G / 237G | %44 |
| /mnt/side | Seagate 500 GB; restic, indirmeler, proje ve yedekler | 458G | 313G / 122G | %72 |
| /mnt/sidemain | Samsung M3 1 TB USB; medya, fotoğraf, bulut | 916G | 777G / 131G | %86 |

Kanıt: P/g01-srv-arsiv-rehber.txt:3966,4170; /srv/rehber/01-HARITA.txt ve 03-DISKLER-CANLI.txt. LUKS kullanımı belgeli; şifreli disk bağlandığında uygulamalar dosyaları açık olarak okur. Dosya özetlerindeki MB/GB ile df birimleri farklıdır; klasör boyutları tekilleştirilmiş fiziksel kullanım değildir.
- İndeks: **984.771 dosya** = kök bölüm 665.499 + sidemain 184.727 + side 134.545. **319.819 containerd/Docker katman dosyası hariçtir** (görev girdisi). Arama sonucu yokluğu sunucuda dosya yokluğunu kanıtlamaz.
- LAN: enp37s0, 192.168.0.15/24, ağ geçidi 192.168.0.1; Tailscale: 100.86.88.1, flugelserver.tail42f1f4.ts.net. Kanıt: P/c10-ag.txt:407 ve arayüz dökümü.
- **Tailscale Funnel bilerek açık (Gökalp kararı, 2026-11-15; mobil uygulamalar kullanıyor):** `:443` Komga, `:8443` reader güncellemeleri + `/nextcloud`, `:10000` Kavita. Eski "Jellyfin 443 / Immich 10000" eşlemesi geçersiz. Güncel ağ düzeni: [[knowledge/concepts/ev-agi-ve-dis-erisim]].
- İki Cloudflare birimi çalışıyor. Yerel /etc/cloudflared/akis.yml: Akış→3012, Düdük→18420, ana alan adı ve medya/indirme alt alanları→8098 giriş portalı. /etc/cloudflared/config.yml ana tünelin **20 Ekim belge kopyasıdır**; gerçek rotalar panelden yönetilir. Nextcloud→8443, Immich→2283, video→8096, kitap→8295, manga→8296 ve eski yönetim rotaları burada yazılıdır; güncel panel/Access kuralları doğrulanmadı.
- Doğrudan yayın: Docker kaydında Immich 0.0.0.0/[::]:2283, Gluetun 0.0.0.0/[::]:51413 TCP/UDP, Nextcloud LAN ve loopback 8443. Kısmi ss kaydında *:8295,8091,8096,7878,6767, Samba [::]:139, çok arayüzde WSDD 5357 görülür; diğer portların yokluğu çıkarılamaz.
- UFW etkin, gelen/yönlendirilen varsayılan deny; 172.16.0.0/12, 192.168.0.0/16, 100.64.0.0/10 geniş izinli. Docker FORWARD zincirleri ayrıca değerlendirilmelidir; kesilmiş nft dökümü bütün WAN trafiğinin UFW'yi aştığını kanıtlamaz. 5 Kasım notunda DOCKER-USER WAN engeli de kayıtlıdır. Kanıt: P/c10-ag.txt:104–232; P/c04-stacks-diger.txt:3657.

## 2. Servis tablosu

**23 çalışan Docker konteyneri, 19 compose yığını**: P/c09-docker-runtime.txt:8–31 ile P/g01-srv-arsiv-rehber.txt:4031 sonrası bloklar birlikte sayıldı. g01'in “18 yığın” sayımı hatalıdır.
Kısaltmalar: **S**=/opt/stacks, **A**=/srv/appdata, **M**=/mnt/sidemain/media, **L**=127.0.0.1. “c09'da yok”: docker ps -a listesinde yok; silinmiş veya başka biçimde çalışıyor olabileceğinden “durmuş konteyner” denmez.
Ağ sütunu host/VPN dışında tanım düzeyindedir; *_default ağının bulunması üyelik kanıtı değildir. Portlar host yayınıdır; “iç” konteyner portudur, hosttan açık sayılmaz.

| Servis | Ne | Compose yolu | Veri yolu | Port | Ağ | Bağımlılık | Durum |
|---|---|---|---|---|---|---|---|
| plex | Medya sunumu | S/plex/compose.yaml | A/plex; M/movies,series | 32400 | host | GPU, medya | Çalışıyor, sağlıklı |
| jellyfin | Medya sunumu | S/jellyfin/compose.yaml | A/jellyfin; M/movies,series | L:18096→8096; soket 8096 | bridge tanımı | medya, uyg katmanı | Çalışıyor, sağlıklı |
| radarr | Film yönetimi | S/radarr/compose.yaml | A/radarr; M/movies; /mnt/side/downloads | L:17878→7878; soket 7878 | bridge tanımı | Transmission, indeksleyiciler | Çalışıyor |
| sonarr | Dizi yönetimi | S/sonarr/compose.yaml | A/sonarr; M/series; /mnt/side/downloads | L:18989→8989; soket 8989 | bridge tanımı | Transmission, indeksleyiciler | Çalışıyor |
| bazarr | Altyazı | S/bazarr/compose.yaml | A/bazarr; M/movies,series | L:16767→6767; soket 6767 | bridge tanımı | medya/Arr | Çalışıyor |
| jackett | İndeksleyici | S/jackett/compose.yaml | A/jackett | L:19117→9117; soket 9117 | bridge tanımı | dış indeksleyiciler | Çalışıyor |
| prowlarr | İndeksleyici yönetimi | S/prowlarr/compose.yaml | A/prowlarr | Gluetun L:19696→9696; soket 9696 | Gluetun namespace | Gluetun, FlareSolverr | Çalışıyor |
| transmission | Torrent | S/transmission2/compose.yaml | A/transmission; /mnt/side/downloads,watch | Gluetun L:19091→9091; soket 9091; peer 51413 | Gluetun namespace | Gluetun | Çalışıyor |
| flaresolverr | Web doğrulama yardımcısı | S/flaresolverr/compose.yaml | Docker volume /config (g01) | iç 8191 | Gluetun namespace | Gluetun | Çalışıyor |
| gluetun | Mullvad/WireGuard geçidi | S/gluetun/compose.yaml | S/gluetun/auth; .env | 51413 TCP/UDP; L:14567,18889,19091,19696 | VPN + bridge | TUN, NET_ADMIN, Mullvad | Çalışıyor, healthy (2026-11-15 16:07 UTC yeniden oluşturuldu; HTTPPROXY açık, dış port 8889) |
| kavita | Kitap sunumu | S/kavita/compose.yaml | A/kavita; M/books | L:18295→5000; soket 8295 | bridge tanımı | kitaplar, IDP eşlemesi | Çalışıyor |
| komga | Manga/kitap sunumu | S/komga/compose.yaml | A/komga; M/books | L:18296→25600; soket 8296 | bridge tanımı | kitaplar, IDP eşlemesi | Çalışıyor |
| suwayomi | Manga kaynak/indirme | S/suwayomi/compose.yaml | A/suwayomi; M/books/manga/suwayomi | Gluetun L:14567→4567; soket 4567 | Gluetun namespace | Gluetun, FlareSolverr | Çalışıyor; oto-indirme kapatma kaydı var |
| nextcloud | Kişisel bulut | S/nextcloud/compose.yaml | A/nextcloud; /mnt/sidemain/cloud/nextcloud; Immich salt okunur | L ve 192.168.0.15:8443→443 | bridge tanımı | nextcloud-db | Çalışıyor, sağlıklı |
| nextcloud-db | PostgreSQL 17 | S/nextcloud/compose.yaml | A/nextcloud-db | iç 5432 | Nextcloud ağı tanımı | disk | Çalışıyor, sağlıklı |
| immich_server | Fotoğraf/video | S/immich_server/compose.yaml | /mnt/sidemain/photos/immich; ek /data volume'u (g01) | tüm IPv4/IPv6:2283 | bridge tanımı | PG, Redis, GPU | Çalışıyor, sağlıklı |
| immich_machine_learning | Fotoğraf ML | S/immich_server/compose.yaml | A/immich/model-cache | host yayını yok | Immich ağı tanımı | NVIDIA/CUDA | Çalışıyor, sağlıklı |
| immich_postgres | PostgreSQL 14/vector | S/immich_server/compose.yaml | A/immich/postgres | iç 5432 | Immich ağı tanımı | disk | Çalışıyor, sağlıklı |
| immich_redis | Kuyruk/önbellek | S/immich_server/compose.yaml | Docker volume /data (g01) | iç 6379 | Immich ağı tanımı | Immich | Çalışıyor |
| giris | Nginx portal/HUD/proxy | S/giris/compose.yaml | S/giris/html,nginx.conf,htpasswd | L:8098 (tanım) | host | arka uçlar, Basic Auth | Çalışıyor |
| tsidp | OIDC kimlik sağlayıcı | S/tsidp/compose.yaml | S/tsidp/data | host eşlemesi yok | kendi Tailscale kimliği | tailnet, sertifikalar | Çalışıyor |
| flugel-akis | Haber/spor/AI akışı | S/panel/compose.yaml (içerik eksik) | S/panel/akis/veri; /var/lib/basket-bot, /var/lib/flugel/durum | 3012 (rota/kod) | host (g01) | Ollama, dış API'ler | Çalışıyor, sağlıklı |
| duduk-server | TBF/basketbol/hakem takibi | /home/flugel/duduk-server/docker-compose.yml | /home/flugel/duduk-server/data | L:18420 | üyelik belirsiz | Python, dış spor kaynakları | Çalışıyor |
| subgen | Whisper altyazı | S/subgen/compose.yaml | M/series,movies; ayrı model volume'u tanımlı değil | L:18091→9000; soket 8091 | bridge tanımı | NVIDIA, Plex | c09'da yok |
| adguard | DNS filtreleme | S/adguard/compose.yaml | A/adguard/work,conf | LAN/TS:53; tüm:8888,853 (tanım) | bridge tanımı | upstream DNS, TLS | Çalışıyor (2026-11-15; modem ve Tailscale DNS'i buna yönlü) |
| guacamole + guacd + guac-db | Web RDP/SSH ve PostgreSQL | S/guacamole/compose.yaml | A/guacamole/db; S/guacamole/keys | L:18097; 172.17.0.1:4822 | bridge tanımı | DB, 192.168.122.75:3389 | Üçü de c09'da yok |
| cup | İmaj güncelleme kontrolü | S/cup/compose.yaml | kalıcı veri belirsiz | L:9812 | bridge tanımı | Docker socket | c09'da yok |
| ollama | Yerel LLM | S/ollama/compose.yaml | A/ollama (~6,6 GB modeller) | L:21434; ön soket 11434 | ai-kumhavuzu tanımı | NVIDIA, uyg katmanı | c09'da yok; talep üzerine tasarım |
| prometheus | Metrik deposu | S/izleme/compose.yaml | A/prometheus | L:9190 | host tanımı | exporter | c09'da yok |
| alertmanager | Alarm yönlendirme | S/izleme/compose.yaml | A/alertmanager | L:9193 | host tanımı | alarm-koprusu:9194 | c09'da yok |
| node-exporter | Host metrikleri | S/izleme/compose.yaml | /var/lib/node_exporter/textfile | L:9100 | host tanımı | host fs/DBus | c09'da yok |
| grafana | İzleme panosu | S/izleme/compose.yaml | A/grafana | 3020 | host tanımı | Prometheus | c09'da yok |
| uptime-kuma | Erişilebilirlik izleme | S/uptime-kuma/compose.yaml | A/uptime-kuma | 3004→3001 | bridge tanımı | Docker socket | c09'da yok |
| backrest | Restic web yöneticisi | S/backrest/compose.yaml | A/backrest; /mnt/side/restic | 9898 | bridge tanımı | restic, rclone | c09'da yok; doğrudan restic ayrı |
| dozzle | Docker günlük arayüzü | S/dozzle/compose.yaml | A/dozzle | L:9811 | bridge tanımı | Docker socket | c09'da yok |
| filebrowser | Web dosya yönetimi | /opt/filebrowser/docker-compose.yml | /opt/filebrowser/filebrowser.db; host /→/srv | LAN:9876 (bu tanım) | belirsiz | host dosya sistemi | c09'da yok; alternatif eski tanımlar var |
| yukle | Telefon kitap/manga yükleme | compose doğrulanmadı; S/yukle/yukle.py | M/books altındaki Yuklenen dizinleri | L:8105 | host betiği tanımı | giris /yukle/, Komga/Kavita | kod var, süreç kanıtı yok |
| hermes / Homepage | Beyin kasası / pano | S/hermes ve S/panel | S/hermes/beyin; S/panel/homepage | bağımsız port doğrulanmadı | belirsiz | dosyalar/ilgili uygulamalar | bağımsız konteyner yok |

Tablo dayanakları: P/c01–c07 ilgili paketleri (tanım/veri), P/c09 (durum), P/g01 içindeki /srv/rehber/02-UYGULAMALAR.txt (14 Kasım bind/host/VPN eşlemesi), P/c08 (soketler). docker inspect c09'da boş olsa da g01 bazı bağları ayrıca belgeliyor.
Portainer, Beszel, ConvertX, IT-Tools, OpenBooks, PairDrop, Stirling-PDF ve IT merkezi: S/_kaldirildi-20261104; Lingarr/OpenWebUI: 5 Kasım kaldırma kaydı ve /mnt/side/arsiv/kaldirilan-20261105. Aktif sayıya eklenmez. portainer_data volume'u ve Hermes imajı çalışan servis kanıtı değildir.

## 3. Veri haritası

Adetler dosya/klasör sayısıdır; benzersiz eser veya uygulama DB kaydı sayısı değildir. Alt klasörleri üst toplamla yeniden toplamayın.

| Alan | Nerede | Yaklaşık miktar | İçerik / örnek |
|---|---|---|---|
| Dizi/anime | /mnt/sidemain/media/series | **390,59 GB; 4.390 dosya; 13 seri/22 sezon + Specials** | JoJo S1–S6, Westworld S1–S3, Better Call Saul S1–S2, Evangelion, Haruhi, 86, Band of Brothers |
| Filmler | /mnt/sidemain/media/movies | **128,83 GB; 828 dosya; 42 film klasörü** | LOTR, Godfather, Dune; Ghibli, Perfect Blue, Redline, Look Back; metadata/trickplay dahil |
| Manga bütünü | /mnt/sidemain/media/books/manga | **204,92 GB; 25.371 dosya** | kök + 43 doğrudan seri klasörü 31,61 GB; Suwayomi 170,95 GB; Kamiyomu 2,36 GB; Vagabond, Chainsaw Man, Frieren, Oshi no Ko, Re:Zero |
| Suwayomi manga | aynı ağacın suwayomi/ dalı | 21.936 dosya; 21.852 arşiv; ~170,95 GB | kaynaklardan indirilen bölümler; 163 manga/21.892 indirilmiş bölüm ise **5 Kasım uygulama kaydıdır**, indeksle özdeş değil |
| LN/WN | /mnt/sidemain/media/books/ln ve ln-arsiv | 181 + 11 dosya; ~2,09 GB | İngilizce/Türkçe Re:Zero LN/WN, EX/IF/yan hikâyeler; Alya 9 cilt |
| Kitap yan kopyaları | /home/flugel/indirme-rezero; /mnt/side/backups/rezero-ln-20261103 | 42 dosya/292 MB; 120 dosya/916 MB | Re:Zero EPUB/PDF, IF ve Türkçe yan hikâyeler; ana kütüphaneye ek eser sayılmaz |
| Fotoğraf/video | /mnt/sidemain/photos/immich | ~87,43 GB; 45.898 dosya | library 71,13 GB/14.992 dosya; üç kullanıcı dizini, tarihli kişisel arşiv; encoded-video 9,98 GB, thumbs 4,67 GB, upload 306 MB, DB yedekleri 1,35 GB |
| Kişisel bulut | /mnt/sidemain/cloud/nextcloud | **18,27 GB; 107.735 dosya** | flugel/files 17,11 GB/103.771 dosya; kullanıcı dosyaları, önizlemeler, çöp/sürümler. Kesik ağaçta kullanıcı koleksiyonları ayrıntılı görünmüyor |
| Kişisel evrak/aile | /mnt/sidemain/personal | 304 dosya; 422 MB | usa: 7 evrak/görsel; yedek-amk: 2016/2018 telefon-USB arşivi, 287 fotoğraf/10 video |
| Okul/dosyalar | /mnt/side/files | 84 dosya; 170 MB | school: PDF/DOCX deney ve ders belgeleri; images, installers, notes; FLUGEL APK ve NxtPanel arşivi |
| Proje kaynakları | /mnt/side/projects | **458,2 MB; 17.558 dosya** | flugel, home-server, flugel-manga, flugel-island, flugel-cyber-lab, flugel-sunucu-app, NxtPanel, weekly-task(s), Eclipse çalışma alanları |
| Aktif geliştirme | /home/flugel/work; /home/flugel/duduk-server | koharia-reader/public ~5,6 GB; SDK 7,6 GB; Gradle 5 GB | Android okuyucu, Akış, Düdük; emülatörler work/avd ~2,1 GB ve ~/.android/avd ~5,1 GB. Kaynakla derleme/önbellek iç içe |
| Sunucu kodu/bilgi | /opt/stacks/panel/akis; /opt/stacks/hermes/beyin; /opt/flugel-cyberlab; /opt/basket-bot | Akış veri 190 MB; beyin 31 ham/26 not/48 wiki dosyası; Cyberlab 3 release | kişisel akış, Obsidian kasası, lab/bot kodu; /home/flugel/git/flugel-beyin.git bare depo |
| FIBA arşivi | /opt/flugel-archives/Basketbol/FIBA-2026-2026-10-27/FIBA-2026 | 6 dosya; 18,3 MB | kurallar, yorumlar/işaretli PDF, Türkçe not ve kaynak kaydı; başarısız TBF indirmeleri mevcut sayılmaz |
| Eski geliştirme/operasyon | /srv/dev; /srv/project; /srv/operations | 840 MB/3.110 dosya; <0,1 MB/3 dosya; 3,71 GB/430 dosya | code-server/tranga arşivi; Windows eşitleme planı (gelen/surumler boş); değişiklikler, DB yedekleri, eski envanter |
| İndirmeler | /mnt/side/downloads/complete | ~23,2 GB | radarr ~19,66 GB, tv-sonarr ~3,54 GB; film/dizi ve yan dosyalar; watch boş |
| Yedek ve arşivler | /mnt/side/restic/flugel; /mnt/side/backups; /srv/yedek; /srv/archive | restic ~296 GB; Arch home ~12,16 GB; /srv/yedek 624,8 MB/112 dosya | §4; /srv/archive eski uygulama 667 MB, pc-ev 582 MB, pc-projeler 243 MB, güvenlik 33,6 MB |
| Geri yükleme çalışma alanı | /srv/geri-yukleme/test-20261105-1813 | ~15,08 GB; 135.911 dosya | Nextcloud, kitap uygulamaları, DB/LUKS dökümleri, 30 örnek medya; canlı verinin ayrıca kopyası |

Kaynaklar: P/g01–g09 dizin özetleri; P/c04–c07. Hakem, ham özetlerdeki ayrık satırları yeniden topladı: **medya 726.427,8 MB/30.781 dosya**; g06'nın ~696 GB/29.900 iddiası düzeltilmiştir. Satırlar derinlik sınırına kadar doğrudan dosyaları, sınırda alt ağacı içerir; aynı dosya yeniden sayılmadı, içerik/hash tekilleştirmesi yapılmadı. g05 koharia toplamı da ham paketle ~5,63 GB'dır.
/mnt/sidemain altındaki books, movies, series, immich, nextcloud_data, kamiyomu ve "yedek amk" eski uyumluluk yolları olarak belgeli; indeksin [diger] 0 MB kaydı kırık/boş bağ kanıtı değildir. Esas yollar yukarıdadır; güncel bağ hedefleri doğrulanmadı.

## 4. Yedekleme zinciri

- **Yeni doğrudan restic:** /usr/local/sbin/flugel-yedek → /mnt/side/restic/flugel; parola dosyası /etc/sistem-bakim/restic/flugel-yerel.pass, ikinci kurtarma kopyası /mnt/sidemain/.kurtarma/. Değerler bu belgede yoktur.
- 5 Kasım ilk başarı: ana 266,218 GiB ve nextcloud 8,925 GiB mantıksal snapshot; g04 repo ağacında **16 snapshot/~296 GB pack verisi** var. Snapshot dosyası adedi son tarih veya her gün başarı kanıtı değildir.
- Geri yüklemede görülen kapsam: Nextcloud dosyaları+uygulaması, Kavita/Komga, Suwayomi DB, Immich SQL, LUKS başlıkları ve örnek medya. Güncel flugel-yedek betiğinin tüm kaynak/dışlama listesi pakette yok; fotoğraf/manga/projelerin tamamını kapsıyor varsayılmadı.
- **Geri yükleme testi geçtiğine dair kayıt var:** 5 Kasım 42/44 doğrudan kontrol; iki sayım farkı yedek sonrası eklenen kayıtlarla açıklanmış, medya hash örneklemi 30/30. *.err dosyalarının yalnız bulunması başarısızlık değildir. Kanıt: P/c04-stacks-diger.txt:3566–3569; /opt/stacks/_bakim/DEGISIKLIK-GUNLUGU.md. Son haftalık test sonucu bilinmiyor.
- **Backrest ayrı/eski kurulum:** /opt/stacks/backrest/compose.yaml, kur.py, /srv/appdata/backrest/config/config.json; yerel hedef /mnt/side/restic/yerel, bulut hedefi rclone:gdrive:FLUGEL-sunucu-yedek/restic. Bunlar /restic/flugel ile aynı repo değildir. c09'da Backrest konteyneri yok.
- Backrest tanımında fotoğraflar (thumbs/encoded-video hariç), Nextcloud (PC-Yedekleri ve bazı cache/preview hariç), appdata/DB dökümleri, dev, stacks, etc, usr-local ve personal planlıdır; Drive için kitap/manga ek planı vardır. **Plan ve Drive kimlik dosyası, tamamlanmış uzak yedek kanıtı değildir.**
- **Eski arşiv zinciri:** uygulama-yedek.py → /mnt/side/backups/uygulamalar; kritik-yedek.sh → /mnt/side/backups/kritik; VM → /mnt/side/backups/vm. 14 Kasım rehberi bunların son çalışmasını 4 Kasım gösteriyor; yeni restic zincirini raporlamıyor. g04 üst özetinde bu eski hedefler görünmüyor: **mevcut eski kopyalar doğrulanamadı**.
- /srv/backups ve /mnt/sidemain/backups indeks kesitinde boş; eski rehberin “current kopyaları” güncel mevcut yedek sayılmadı. /srv/yedek 21/25 Ekim müdahale kopyalarıdır; /srv/archive/backups daha eski Nextcloud/Immich arşivleridir.
- Immich /mnt/sidemain/photos/immich/backups: 1–14 Kasım arası 14 SQL arşivi/~1,35 GB; yalnız DB yedeğidir, fotoğraf yedeğinin yerini tutmaz. Appdata içinde Kavita 31, Suwayomi 16, Arr/Prowlarr dörder uygulama yedeği bulunur; çoğu kaynakla aynı disktedir.
- Arch PC düz dosya yedeği /mnt/side/backups/arch-pc-2026-11-12; laptop yedekleri /home/flugel/yedekler/laptop-arch (~5,24 GB); proje kopyaları /srv/archive/pc-yedekleri. Varlıkları güncel geri yüklenebilirlik/eksiksizlik kanıtı değildir.
- **Yedeksizliği belgelenen kapsam:** /mnt/side/arsiv/kaldirilan-20261105 arşivinin restic dışında olduğu X1 notunda yazılıdır (P/c04:3868). **Yedek kapsamı doğrulanamayanlar:** tüm film/diziler, personal/usa ve aile arşivinin güncel tam kopyası, /mnt/side/projects, /home/flugel/work ve Düdük, VM diskleri, 8 Docker volume'un tamamı. Bunlar “kesin yedeksiz” diye sunulamaz.
- **Sunucudan bağımsız başarılı yedek gösterilemiyor.** 5 Kasım bakım kaydı offsite/çevrimdışı kopya olmadığını söylüyor; Drive yapılandırması bunu tek başına değiştirmiyor. Aynı kasadaki ayrı disk host ele geçirilmesi/yangın/çalınmaya karşı bağımsız kopya değildir.

## 5. Otomasyon

Kaynak: P/c08-systemd-cron.txt (14 Kasım 21:11 UTC civarı), P/c04 bakım günlüğü, P/c07 betikleri, P/g05 ve g10 envanteri. Timer dökümü UTC'dir (İstanbul +3).

| Birim / betik | Görev ve kanıtlanan durum |
|---|---|
| flugel-yedek.timer/service | Yeni restic; son tetik 14 Kasım 00:35 UTC, sonraki 15 Kasım 00:39 UTC. 00:30 taban saati üzerine gecikme görülüyor; tetik başarı kanıtı değil |
| flugel-yedek-kontrol.timer | Haftalık kontrol; son tetik 14 Kasım 02:00 UTC; /usr/local/sbin/flugel-geri-yukleme-testi bakım kaydında mevcut |
| uyg-*.socket/service, uyg-bosta.timer | Talep gelince uygulama açma/port vekili, boşta kapatma; Jellyfin 8096, Kavita 8295, Komga 8296, indirme portları; restart: no tek başına arıza değil |
| eski-yedek-temizle.*, uyg-gece.* | /dev/null ile maskeli; 5 Kasım H1 kapsamında **bilerek** kapatılmış. Yeni restic saklama/prune davranışı bu maskeden çıkarılamaz |
| torrent-bekci.timer | Dökümde 20 sn; v2 durdur/karantinaya taşıma kaydı var. vm-bosta-kapat.timer **60 sn** aralık; çapraz kontroldeki 10–20 sn genellemesi yanlış |
| self-heal, kaynak-gozcu, disk-koruyucu, disk-health, docker-watcher, swap-flush | Bakım/izleme timer'ları listede; çoğunun ExecStart içeriği pakette yok |
| proje-surum.timer, VM kapanış/yedek birimleri | Proje sürümleme tetikleniyor; VM/eski yedek dosyasının varlığı işin hâlen çalıştığını kanıtlamaz |
| basket-bot.timer, anime-takip.timer, imdb-puan.timer | /opt/basket-bot spor/anime/IMDb işleri; dış API'ler ve bildirim altyapısı |
| telegram-kopru.service | /opt/telegram-kopru/kopru.py; Telegram→Ollama/yz/gelen kutusu; **activating/auto-restart** |
| taildrop-nextcloud.service, giris-durum, island-veri | Dosya aktarımı/panel durum üretimi; Taildrop aktif, diğerleri timer listesinde |
| cloudflared*, tailscaled, wg-quick@warp, snap.lxd | Ağ/tünel/ikinci konteyner altyapısı; aktif birimler var. LXD iş yükleri ayrıca envanterlenmemiş |
| rehber-guncelle, sunucu-indeks, etckeeper | Rehber günlük 06:00 UTC; indeks kodu/unit'leri /home/flugel/sunucu-indeks, timer etkinliği bu kesitte doğrulanmadı; etckeeper timer listede |
| Cron | flugel crontab boş; sistem cron/anacron, certbot, e2scrub, PHP ve güvenlik taramaları var; diğer kullanıcı cron'ları bütünüyle gösterilmedi |
| /opt/scripts/gmail-*.py | Gmail OAuth ve WhatsApp bildirim betikleri var; zamanlama/çalışma durumu kanıtlanmadı |

317 yüklü unit ve 51 timer listeleniyor; tümü aktif/başarılı değildir. webmin.service **not-found/failed**; eski nottaki port çakışması güncel neden olarak kanıtlanmadı. PCP servisleri mevcut; apache2 veya dosya halinde bulunan birimler yalnız envanterden aktif kabul edilmedi.

## 6. Riskler — öncelik sırasıyla

1. **Yüksek — kişisel verinin bağımsız yedeği doğrulanamıyor.** Aynı hosttaki restic ayrı diskte olsa da ortak kayıp alanında; son başarılı snapshot/kapsam belirsiz. Kaynak: /opt/stacks/_bakim/ILERLEME.md, KORUMA-SISTEMI-PLANI.md B13 (P/c04-stacks-diger.txt:3576,3657); /mnt/side/restic/flugel (P/g04-side-yedek-arsiv.txt).
2. **Yüksek — parolasız/yerel muafiyetli indirme yönetimi ve geniş ağ izinleri.** Transmission RPC auth/whitelist kapalı; systemd vekilleri loopback arka uçları LAN'a sunabiliyor, Arr yerel muafiyeti vekil arkasında etkili olabilir. Kaynak: /srv/appdata/transmission/settings.json, /srv/appdata/{radarr,sonarr}/config.xml (P/c06-appdata-n-z.txt); /etc/systemd/system/uyg-* (P/c08-systemd-cron.txt); /opt/stacks/_bakim/KORUMA-SISTEMI-PLANI.md B1–B4; UFW (P/c10-ag.txt:104).
3. **Yüksek — kimlik/özel anahtarların paket ve kopyalarda bulunması.** X ile özel anahtar içeriği doğrulanan örnekler: /opt/stacks/guacamole/keys/server-ed25519, /opt/stacks/tsidp/data/oidc-key.json (P/c03-stacks-ag-guvenlik.txt; X). c06 ayrıca /srv/appdata/ollama/id_ed25519 ve /srv/appdata/plex/Library/Application Support/Plex Media Server/.LocalAdminToken içeriğinin açık olduğunu raporluyor; bu iki içerik hakemce ayrıca açılmadı. Arch düz yedeğinde .claude/.credentials.json, .android/adbkey, .bash_history yolları mevcut (P/g04-side-yedek-arsiv.txt; X); erişebilen hesaplar/ACL bilinmiyor. /etc ve /opt/stacks Git geçmişindeki sırlar bakım kaydında belgeli (P/c04-stacks-diger.txt:3610); rotasyon tamamlanma kanıtı yok.
4. **Yüksek — internet erişimi ve tek faktörlü girişler.** Funnel ana adres/:10000 açık (P/c10-ag.txt:288); medya proxy'si Basic Auth, Guacamole TOTP kaldırma kaydı var (/opt/stacks/guacamole/compose.yaml, P/c03-stacks-ag-guvenlik.txt:1158; X). Guacamole c09'da yok; risk geri açıldığında geçerli. Ana Cloudflare rotaları/Access bilinmiyor; belgede kalan portainer/admin rotaları servis geri gelince maruziyet yaratabilir. Kaynak: /etc/cloudflared/config.yml.
5. **Yüksek — VPN geçidi unhealthy.** Gluetun sağlıksız; Transmission/Prowlarr/Suwayomi/FlareSolverr bu namespace'e bağlı. Kesinti veya korumanın beklenen biçimde çalışmaması riski var; **trafik sızıntısı gözlenmiş değildir**. Kaynak: P/c09-docker-runtime.txt:22; /opt/stacks/gluetun/compose.yaml, /srv/rehber/02-UYGULAMALAR.txt; fail-closed işi bakım planında bekliyor (P/c04-stacks-diger.txt:3596).
6. **Yüksek — doluluk ve disk geçmişi.** sidemain %86, side %72 (14 Kasım); SSD TRIM kapalı/I/O baskısı, USB reset ve CRC hataları **20 Ekim tarihli** bulgulardır, güncel sağlık testi değildir. Kaynak: /srv/rehber/03-DISKLER-CANLI.txt, 09-BILINEN-SORUNLAR.txt (P/g01-srv-arsiv-rehber.txt:4170,4528). Maskeli eski temizleyici, ~15 GB /srv/geri-yukleme/test-20261105-1813 (P/g03-srv-yedekler.txt) ve geliştirme kopyaları kapasite baskısını artırabilir.
7. **Yüksek — yetki yoğunlaşması ve yeniden açılabilecek geniş erişim.** Geçici tam sudo eski rehberde belgeli; /etc/sudoers.d/90-bakim-gecici güncel ağaçta var, içeriği yok (P/g01, P/g10). /opt/filebrowser/docker-compose.yml root ve host / yazılabilir tanımlıyor (P/c07-opt-diger.txt); ayrı noauth ayarı /srv/appdata/filebrowser/config/settings.json (P/c05-appdata-a-m.txt) ile aynı çalışan örnek olduğu kanıtlanmadı. Kuma/Dozzle/CUP compose socket bağları daemon güven sınırına erişir; :ro API'yi salt okunur yapmaz. Bu konteynerler c09'da yok.
8. **Yüksek — medya gibi adlandırılmış çalıştırılabilir dosya.** /mnt/side/downloads/complete/radarr/Michael 2026 1080p HD X264 1080p.scr (P/g09-side-proje-dosya.txt). Uzantı Windows çalıştırılabilir türüne işaret eder; içerik/hash/zararlı analizi yok, “doğrulanmış zararlı” değildir.
9. **Orta — izleme/kimlik köprüsü sürekliliği.** Telegram yeniden başlama döngüsünde, Webmin failed; izleme yığını ve Backrest konteynerleri c09'da yok. Kaynak: P/c08-systemd-cron.txt:87,121; P/c09-docker-runtime.txt; /srv/appdata/uptime-kuma/error.log (P/c06) eski SQLite hataları içeriyor. Alarm kapsamasının yeterliliği bilinmiyor.
10. **Orta — izin kayıtlarında hassas dosyalar genel okunabilir.** /etc/fail2ban/action.d/cloudflare-token.conf, /etc/crowdsec/{local_api_credentials,online_api_credentials}.yaml için .etckeeper 0644 kaydı var (P/g10-etc-genel.txt); güncel stat/ACL ve içerik doğrulanmadı. 0600/0400 anahtar dosyasının varlığı tek başına sızıntı sayılmadı.
11. **Düşük/orta — koleksiyon/proje tutarsızlığı.** /mnt/sidemain/media/books/manga altında aynı adlı varyantlar, Alya/*.epub.temp, yalnız kapak içeren Kaguya klasörü ve /mnt/side/projects/weekly-task/.git/rebase-merge mevcut (P/g06-sidemain-medya-kitap.txt, P/g09-side-proje-dosya.txt). Hash karşılaştırması olmadan “10+ GB gereksiz kopya” veya güvenle silinebilir dosya sonucu yok.

## 7. Bir şeyi nasıl bulurum

Aşağıdaki komutlar kullanıcı için örnektir; bu görevde çalıştırılmadı. Aramanın eşleşme/desen ayrıntıları kesik koddan doğrulanmadı; önce sade ifadelerle başlayın.
~~~bash
ssh flugelserver python3 ~/sunucu-indeks/sunucu_indeks.py ara "<ifade>"
ssh flugelserver python3 ~/sunucu-indeks/sunucu_indeks.py yol "<desen>"
ssh flugelserver python3 ~/sunucu-indeks/sunucu_indeks.py ozet
ssh flugelserver python3 ~/sunucu-indeks/sunucu_indeks.py ara "ReZero"
ssh flugelserver python3 ~/sunucu-indeks/sunucu_indeks.py ara "Vagabond"
ssh flugelserver python3 ~/sunucu-indeks/sunucu_indeks.py ara "duduk"
ssh flugelserver python3 ~/sunucu-indeks/sunucu_indeks.py yol "/mnt/sidemain/photos/immich"
ssh flugelserver python3 ~/sunucu-indeks/sunucu_indeks.py yol "/mnt/side/projects"
~~~
Başlangıç noktaları: eser→M/books veya M/{movies,series}; fotoğraf→photos/immich; belge→cloud/nextcloud/flugel/files ve personal; proje→side/projects veya home/flugel/work; uygulama ayarı→S ve A; yedek→restic/flugel ve tarihli arşivler.
İndeks snapshot'ı, kesilmiş ağaçlar, dışlanan katmanlar ve yanlış pozitif [sir] etiketleri sonuç yorumunu sınırlar; sır içeriğini arama çıktısına/rapora taşımayın.

## 8. Belirsizlikler ve çelişkiler

- **Çözüldü — veri toplamları:** g06 medya 696→726,43 GB, manga 198,2→204,92 GB, dizi 366,8→390,59 GB ve 14→13 seri; g08 Nextcloud 107.662→107.735 dosya; g09 projeler 385→458,2 MB. g02/g03/g05 toplamları da ham özetlerden düzeltildi; yuvarlama dışında kalan lane aritmetik hataları taşınmadı.
- **Çözüldü — servis sayısı/tarihi:** 19 Ekim guncel.json içindeki 34 konteyner güncel değil; 14 Kasım rehberindeki 19 yığın, c09'daki 23 konteynerle tutarlı. g01'in “18” sayısı düzeltilmiştir.
- **Çözüldü — yedekler durmuş iddiası:** 4 Kasım son tarihi eski zincire ait; 5 Kasım restic geçişi ve 14 Kasım tetikleri mevcut. “10 gündür hiçbir yedek yok” reddedildi. Son başarılı restic tarihi/kapsamı ve Drive başarısı belirsiz.
- **Çözüldü — restore başarısız iddiası:** .err adları yeterli değil; 5 Kasım testinin geçtiği ve iki farkın açıklaması günlüğe alınmış. Güncel restore testi sonucu gösterilmedi.
- **Çözüldü — Funnel kapalı iddiası:** tsidp yorumundaki kapalı ayarı host Funnel durumunu anlatmıyor; host çalışma zamanı açık. **8098 kapalı iddiası** da kesik ss nedeniyle kanıtsız.
- **Çözüldü — FHS taşıması:** g02'nin yarım kaldı notu daha eski; 20 Ekim tamamlanma kaydı ve /arrapps→srv/appdata bağı var. **VM timer 10–20 sn** iddiası ham kayıttaki 60 sn ile düzeltildi.
- **Çelişki — disk aygıt adları:** eski rehber sidemain=sda, yeni df sdd_crypt diyor. Model→güncel fiziksel aygıt eşlemesi/SMART/TRIM doğrulanmadı; kararlı harita bağlama yollarıyla verildi.
- **Çelişki — Filebrowser örneği:** eski envanterde :8085/root/tüm disk, sıkılaştırma notunda loopback/dar bağlar, /opt/filebrowser tanımında LAN:9876/root/tüm disk var. c09'da çalışan örnek yok; hangisinin yeniden başlatılacağı belirsiz.
- **Çelişki — restart politikaları:** bazı compose'larda restart: no, 5 Kasım günlüğünde medya-indirme/Suwayomi için unless-stopped var. Boş güncel inspect yüzünden etkin politika belirlenemedi; socket tasarımı ve süreç bilgisi ayrı tutuldu.
- **Çelişki — eski yedek hedeflerinin varlığı:** 14 Kasım rehberi /mnt/side/backups/{uygulamalar,kritik,vm} listesini raporluyor, g04 üst özeti bunları göstermiyor. Yeni restic varlığı açık; eski hedefler mevcut kopya sayılmadı.
- **Kanıt yetersiz:** Cloudflare panel/Access ve Tailscale ACL, tam firewall/Serve, son başarılı yedek, named volume sahiplerinin tamamı, güncel VM durumu ve sudoers içeriği eksik. Kaynaklar farklı zamanlıdır; plan dosyası uygulanmış işlem sayılmaz.
- **Hatalı kesinlikler elendi:** [sir] etiketi/.env adı sızıntı kanıtı değildir; deploy_ed25519.pub, DH parametreleri, token.py, “Secret” adlı CBZ'ler özel anahtar değildir. g04 proje-sirlari/Projects içeriği okunmadı; Arch yedeğinin tüm Samba kullanıcılarına açık olduğu veya LUKS dışında tamamen şifresiz fiziksel diskte bulunduğu kanıtlanmadı.
- **Hatalı kesinlikler elendi:** Immich upload varlığı takılı iş, kullanıcı klasörü sayısı aktif hesap sayısı, kök [diger] girdileri bozuk bağ kanıtı değildir. g06 aynı eser adları hash eşitliği göstermez; g10 Webmin aktif iddiası c08 failed kaydıyla değiştirildi.
- **Kapsam sınırı:** g01–g10 ağaç/metin kesintileri; c09 inspect boş; c10 nft/ss kısmi. Sunucu güncellenmedi; yalnız bu taslak oluşturuldu. Sır değerleri rapora alınmadı.

## 9. Güncelleme — 2026-11-15 geliştirme turu

> Tam rapor: `~/Documents/ai_workplace/second-brain/raporlar/sunucu-gelistirme-2026-11-15.md` (lane raporları, sha256, diff). Sır değerleri bu nota yazılmaz.

- **Yeni uygulamalar (kalanlar, yalnız Tailscale, `https://flugelserver.tail42f1f4.ts.net:<port>`):** Forgejo 55443 (altyapı deposu `flugel/flugel-altyapi`, gece eşitleme), Paperless-ngx 56443 (Türkçe OCR; Syncthing + n8n ile PC/Nextcloud'dan belge), n8n 60443 (4 ntfy akışı + Nextcloud→Paperless), SearXNG 61443 (Hermes `flugel-arama`), Syncthing 62443, IT-Tools 65443, Scrutiny 46443, ntfy 51443. Kaldırılanlar: Jellyseerr, Vaultwarden, Audiobookshelf, Changedetection, CyberChef, Homebox, Speedtest Tracker, Recyclarr; izleme yığını durduruldu.
- **Kaldırılan:** libvirt ve üç sanal makine (imajlar silindi); `telegram-kopru.service` (Hermes aldı); Homepage.
- **Otomasyon:** `flugel-saglik-ozet` (5 dk) → Hermes `saglik-gozcu` (15 dk) → Telegram; `flugel-onarim` kuyruğu; `gluetun-netns-onar` (2 dk); `flugel-arsiv-katalog` (günlük) + Hermes `arsiv_sorgu.py`; `flugel-manga-denetim` (pazar); `flugel-geri-yukleme-testi` (aylık); `flugel-altyapi-esitle` (gece); `bildirim` artık ntfy `flugel` konusuna da yayın yapar.
- **Tailscale ile giriş:** `giris` nginx'inde (`/opt/stacks/giris/nginx.conf`) `Tailscale-User-Login` başlığı sahip değilse 403; Paperless/Forgejo/n8n/Dozzle'da bunun üstüne otomatik oturum (başlık kullanıcı adı `flugel`); kapı eklenenler: SearXNG, IT-Tools, Scrutiny, Syncthing, Cup, Uptime Kuma, Dockge, AdGuard, Sonarr, Radarr, Prowlarr, Bazarr, Jackett, Transmission (geri alma: `/home/flugel/tailscale-kapi-geri-al.sh`). OIDC (tsidp): Komga, Kavita, Nextcloud, Immich, Forgejo, Paperless, Dozzle.
- **Docker ağ havuzu:** `daemon.json` `default-address-pools` genişletildi (yeniden başlatmada etkin); o zamana kadar yeni stack'lerde `network_mode: bridge` ya da açık subnet kullan.
- **Açık:** Cloudflare'da `masaustu.gokalpgoksu.com` genel ana bilgisayar adı ve Nextcloud Access kapısı (Gökalp), disk temizliği kararları (`/mnt/sidemain` %86), manga seri birleştirme, çekirdek `7.0.0-43` yeniden başlatması (Drive aktarımı bitince), ilk yeni-uygulama yedeği (bu gece).
- **Hermes yönlendirme (2026-11-15, güncel):** Hermes modeli `gpt-6-luna` (openai-codex); ajan belirtilmezse Hydrogen'e `agy` ile devreder (becerisi `ai-ekibi-yonlendirici`, `/srv/appdata/hermes/skills/`), `codex`/`argon`/`carbon`/`flash`/`üçünüz` ile seçilir. Terminal aracı sunucuda `hermes-ops` (NOPASSWD sudo) ile çalışır; `agy` çağrısı `sudo -n -u flugel` ile `/tmp`'den yapılır. Tam yetki ayarları: `HERMES_YOLO`, `--accept-hooks`. Raporlar: `second-brain/raporlar/hermes-tam-yetki-ve-ajan-secimi-2026-11-15.md`, `hermes-varsayilan-hydrogen-2026-11-15.md`.
- **Hermes ↔ Antigravity/Codex (2026-11-15):** `agy` ve `codex` sunucuda `/home/flugel/.local/bin` (girişler Gökalp'in kendi terminalinde yapılır; kimlik bilgisi kopyalanmadı). Gemini soru köprüsü (`flugel-gemini-kopru`, araç izni yok, saatte 6) ve PIN onaylı görev köprüsü (`flugel-gorev`: Hermes `gorev-istek` bırakır → ntfy bağlantısı → `:47443` onay sayfası + Gökalp'in PIN'i → ajan `flugel` olarak 30 dk). Koşulsuz sudo verilmedi. Hermes becerileri: `flugel-gemini`, `flugel-gorev`. Açık: PIN, `agy` ve `codex` girişleri Gökalp'te.


