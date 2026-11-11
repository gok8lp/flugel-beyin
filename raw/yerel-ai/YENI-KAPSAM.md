# Güncel sunucu görevi — kapsam ve ekip düzeni / Updated server scope

Bu dosya kullanıcının 5 Kasım 2026 tarihli yeni talimatıdır. GOREV.md ile çelişen eski kaldırma izinleri ve yalnız yerel commit kısıtı yerine bu kapsam geçerlidir. Mevcut çalışmayı baştan başlatma; çalışan yedeği kesme. Tamamlanan işleri yeniden yapma. Kullanıcının aşağıdaki istekleri henüz uygulanmış sayılmaz.

## 1. Ekip ve karar düzeni

Ana ajan müdür/koordinatördür. Tam iki alt ajan oluştur:

- **IT lideri:** geniş sistem yönetimi bilgisiyle canlı kanıtları, mimariyi, güvenlik ve geri dönüş planını değerlendirir; uygulayıcının değişikliklerini inceler, test sonuçlarını kontrol eder ve onaylanan aşamaları commit edip yetkili GitHub hedefine push eder.
- **Uygulayıcı:** liderin incelediği ve müdürün kendisine verdiği sınırları açık işleri uygular; değişiklik listesini, test ve geri alma kanıtlarını lidere teslim eder. Kendi başına kapsam genişletmez.

Müdür tek iş kuyruğu tutar, görevleri ve yazılabilecek dosya/servisleri açıkça dağıtır. Aynı servis, dosya, Git çalışma ağacı veya ağ ayarları üzerinde eşzamanlı yazma yaptırmaz. Lider inceleme/commit yaparken uygulayıcı o aşamanın dosyalarını değiştirmez. Hatalı işte ilgili aşamayı durdurur, hatayı açıkça bildirir, düzeltmeyi ister ve yeniden doğrulatır. Alt ajanlar belirsiz kararları müdüre iletir; müdür çözülemeyen kullanıcı tercihi, hedef veya yetki belirsizliğini kullanıcıya tek toplu soruda sorar. Sessizlik onay değildir. Açıkça yetkilendirilmiş rutin işleri tekrar tekrar sorma.

İki alt ajan açma olanağı yoksa varmış gibi davranma; durumu bildir ve kullanıcıya mevcut yürütme seçeneğini sor. Daha fazla alt ajan oluşturma. Yalnız gerekli bağlamı aktar; ilgili skill'leri ihtiyaca göre yükle. Kısa Türkçe ilerleme bildir, ayrıntıları dosyalara yaz.

## 2. Öncelik: SSD, keepalive ve eski yedekler

- Kullanıcı, **11 Kasım 2026'da silinmesi planlanan SSD üzerindeki hedefin bugün silinmesini** istiyor. Önce mevcut planı/timer'ı ve gerçek hedefi salt okunur incele. Bunun bütün SSD mi, bir dizin/arşiv mi olduğunu tahmin etme. Disk seri numarası/UUID, mount, tam hedef yol, boyut, içerik ve korunacak uygulamalar/yedeklerle ilişkisini göster. Kullanıcı hedefi bu bilgilerle kesin olarak doğrulayana kadar silme/formatlama yapma. Doğru hedefin bugün kaldırılması tamamlandıktan sonra eski 11 Kasım görevinin başka veri silmesini önle.
- `disk-keepalive` ve ilgili disk güç yönetimini değerlendir. Disk modelini ve HDD/SSD ayrımını doğrula; standby/park sayacı ve sıcaklık değişimini ölç. Her birkaç saniyede yazı yazmayı veya tüm disklerde standby'ı kapatmayı otomatik çözüm sayma. Gerekiyorsa ölçülebilir faydası olan en küçük düzeltmeyi yap ve önce/sonra kaydını tut.
- Yedek diskteki eski yedekleri temizle; ancak önce güncel korunan veri kapsamı ve bağımsız geri yükleme testi başarılı olmalı. Hangi snapshot/arşivlerin tutulup kaldırılacağını tarih, kapsam ve boyutlarıyla listele. Kullanıcının retention tercihi bilinmiyorsa sor; yeni verilerin tek kurtarılabilir kopyasını silme. Restic deposundaki dosyaları `rm` ile temizleme; doğrulanmış retention ve aracın kendi forget/prune sürecini kullan. Repo parola/kurtarma anahtarlarını koru.

## 3. İndirme davranışı

Gece indirmelerini ve saat tabanlı indirme otomasyonunu tamamen kaldır. Kullanıcı istemeden yeni otomatik indirme başlamasın. Sonarr/Radarr/RSS/Suwayomi vb. otomatik arama/izleme/indirme tetiklerini ve cron/systemd işleriyle ilişkilerini incele; gereken otomatik indirme davranışını kapatırken mevcut kitapları, ilerlemeyi ve kayıtları silme. Başlamış indirme/seed işlerini kullanıcıya bildir; içeriği veya yarım dosyaları kendiliğinden silme. İndirmeler yalnız kullanıcının açık talebiyle başlatılacak.

## 4. AdGuard Home ve içerik tercihleri

AdGuard Home sürekli çalışsın; boot, restart, sağlık ve DNS erişimini doğrula. Yönetim ekranını internete açık bırakma. Reklam, takip ve yetişkin içerik filtrelerini güvenilir, bakımı süren listelerle güçlendir; gereksiz tekrarlanan listeleri azalt ve false-positive/izin listesi süreci bırak. Kullanıcı bunu kendi yetişkin içerik kullanımını sınırlamak için istiyor; çocuk hesabı/çocuk cihazı varsayma.

DNS katmanı yalnız alan adını ayırır; aynı X/Twitter alan adı içindeki belirli yetişkin video veya Türkçe paylaşımı seçerek engelleyemez. Tüm reklamların/yetişkin içeriğin her koşulda engellendiğini iddia etme. Yönetilen cihazlarda uygun tarayıcı içerik engelleyici, arama motoru SafeSearch, platformun hassas içerik ayarları ve mümkün olan hesap/cihaz kontrollerini değerlendir. Desteklenen ayarları gerçek oturumda doğrula; hesap oturumu veya kullanıcı eylemi gereken yerde kullanıcıya adımı ver. Kapsam dışı hesap ayarı değişikliği yapma.

Kullanıcı sosyal medyada mümkün olduğunca Türkçe içerik görmemek istiyor. Platformların dil/içerik tercihleri, sessize alma ve takip listesi araçlarıyla azaltma öner/uygula; yüzde yüz dil filtresi vaat etme. Kullanıcının Türkçe içerikleri, dosyaları veya manga/novel kütüphanesini silme. Engelleme politikalarını delme ve kurtarma davranışını belgeleyerek kendi yönetim erişimini koru.

## 5. Uygulamalar ve korunacaklar

Önceki genel kaldırma izni şu uygulamaları artık kapsamıyor: aşağıda tutulması/geri getirilmesi istenenleri kaldırma.

- **Immich ve Nextcloud:** bütün kullanıcı verileri, orijinaller, hesaplar, albümler/paylaşımlar, DB ve gerekli worker/Redis/eklenti bağımlılıkları korunacak. Kurulu sürümün resmi yönetim/yükseltme belgelerini izle. Tutarlı yedek, izole geri yükleme, uygulama işlev testleri, kaynak sınırları ve hata alarmlarıyla dayanıklılığı iyileştir. Hiç çökmez garantisi verme.
- **Fotoğraf gizliliği:** kullanıcı yüklenen verilerin yedeklenmesini ve hangi cihazdan geldiğinin bilinmemesini istiyor. Önce EXIF/GPS/seri/model, dosya adları, yükleme kaydı ve hesap/IP loglarının farklı izler olduğunu açıkla. Mevcut orijinallerin metaverisini topluca ve geri alınamaz biçimde silme. Yeni yükleme/gösterim için uygulanabilir gizlilik seçeneklerini ve işlev kayıplarını sun; orijinal değişikliği için kullanıcı tercihini al. Sırf logları susturarak tam anonimlik iddia etme; güvenlik ve denetim ihtiyacıyla dengeli veri minimizasyonu uygula.
- **Plex:** korunacak; stabilitesini ve erişimini doğrula.
- **Jellyfin:** 7/24 çalışacak; otomatik boşta durdurma varsa bu servis için kaldır, boot/health/restart ve gerçek oynatma yolunu test et.
- **Kavita, Komga:** 7/24 çalışacak. Suwayomi de korunacak. Manga ve novelleri ayrı, anlaşılır kütüphaneler olarak düzenle; seri/cilt adlandırması ve mevcut okuma ilerlemesini koru. Taşıma öncesi eşleme/manifest ve yedek oluştur. **Re:Zero / Re Zero / ReZero içerik ve ayarlarına dokunma**; gerçek yollarını belirleyip koruma listesine al.
- **tsidp:** kimlik sağlayıcı stabilitesi önemli. Her Docker uygulaması için doğal OIDC desteğini, proxy ile koruma seçeneğini veya neden uygulanamadığını matrise yaz. Login/logout, token/session süresi ve mobil/masaüstü istemcilerini ayrı test et; DB/worker gibi web arayüzü olmayan konteynerlere sahte SSO ekleme.
- **Portal:** kullanılan giriş adresi `https://gokalpgoksu.com/`. Homepage yerine bu portalı esas al; adresi ve çalışan yönlendirmeleri koru.
- **flugel-akis / Akış:** henüz bitmemiş ayrı proje; kodunu, verisini ve erişimini koru. Bu bakım sırasında habersiz yeniden yazma veya kaldırma.
- **Gündem botu:** gerçek servis/proje adını keşfet, çalışma/son başarılı iş/hata durumunu incele; sır ve erişimleri koruyarak onar.
- **Uptime Kuma:** temiz, anlaşılır ve eyleme geçirilebilir bildirimler. Durum geçişi, arıza/iyileşme, tekrar bastırma, bakım penceresi ve kanal teslimini doğrula. Sürekli aynı başarı mesajlarını gönderme; kullanıcıya deneme mesajı gönderme gerekiyorsa kapsam ve kanalı belirt.
- **Dockge, Dozzle, Cup:** erişimi kısıtla. Docker socket erişiminin güçlü yetki olduğunu dikkate al; yönetim arayüzlerini yalnız uygun kimlik doğrulama/yönetim ağıyla sun. Salt okunur mount'un Docker API yetkisini kendiliğinden kısıtladığını varsayma. İzleme aracının kendiliğinden güncelleme yapmasına izin verme.
- **Guacamole + guacd + guac-db:** korunacak/geri getirilecek. Windows performansını RDP/display/codec/ağ ve kaynak ölçümleriyle değerlendir. Kullanıcıya bizzat deneyebileceği güvenli erişim ve test adımları ver; kullanıcı testi yapılmış gibi gösterme. Doğrudan terminal açılan bağlantıyı belirle, gereksiz erişimi kapat veya uygun MFA/yetki sınırıyla koru. Terminal ve Windows oturumlarını başka kişilere açma.
- **Ollama ve OpenWebUI:** gereksiz; bağımlılık/veri envanteri sonrası kaldırılabilir. Model dosyaları kullanıcıya bildirilerek kapsam dahilinde temizlenebilir; alternatif yaratıcı kullanım yalnız kısa öneri olsun, yeni local AI servisi kurma.

## 6. Geri getirilecek araçlar

GLPI, BookStack, IT veritabanı, Stirling-PDF, ConvertX, IT-Tools, PairDrop, OpenBooks, FileBrowser, Portainer, Beszel ve Webmin kullanıcının kullandığı araçlar; kaldırılmayacak. Önce önceki Compose/Git/yedek ve korunmuş appdata'yı bul. Mevcut veri ve hesaplarla, sürüm uyumluluğunu gözeterek güvenilir resmi kaynaklardan geri getir. Yeni boş kurulumla eski verinin üzerine yazma. "IT veritabanı" ve "OpenBooks" hangi ürün/depo olduğu belirsizse gerçek önceki kaynaktan doğrula veya sor; isimden rastgele ürün seçme. Bir araç için veri bulunamadıysa bunu açıkça belirt; varmış gibi gösterme.

Portainer ve Dockge gibi örtüşen araçlar isteniyor: kaldırmak yerine rolleri ayır, aynı Compose projesini iki yerden çelişkili yönetme. Yeni admin panellerini doğrudan internete açma. Gerçek kaynak tüketimini ölç; 15 GiB civarı RAM'e tüm ağır araçları sınırsız açma. 7/24 istenmeyen araçlarda isteğe bağlı çalışma önerisini kullanıcıyla netleştir.

## 7. Kimlik, MFA ve güvenilir cihazlar

Etkileşimli kullanıcı/admin arayüzleri için MFA/OIDC desteği envanteri çıkar. Yerel MFA varsa uygun yöntemi kullan; yoksa proxy/IdP katmanı ve erişim kısıtları değerlendir. MFA kaydı, passkey/kurtarma kodu gibi kullanıcı eylemlerini açıkça iste. Ana cihazlarda kolaylık için cihaz kimliği, passkey ve süreli "güvenilir cihaz/oturum" yaklaşımını değerlendir; yalnız LAN IP'sine bakıp herkese MFA muafiyeti verme. Yeni cihaz, hesap kurtarma, kritik yönetim işlemi ve süresi dolmuş oturumda yeniden doğrulama kalsın. Native app/API senkronizasyonunun bozulmadığını test et. tsidp'nin desteklemediği MFA özelliğini var sayma; üst kimlik sağlayıcı zincirini doğrula. Kilitlenmeye karşı güvenli, sırları Git'e gitmeyen kurtarma yolu bırak.

## 8. Konteyner yalıtımı ve güvenlik

Konteynerleri güvenilir birer sanal makine gibi görme; ortak host kernel'i vardır. Uygulamaları gerekmedikçe ayrı ağlar, minimum port ve mount'lar, uygun non-root kullanıcı, capability drop, no-new-privileges, desteklenen AppArmor/seccomp ve read-only alanlarla sınırla. Gereksiz privileged, host network/PID, host dizini ve Docker socket paylaşımını kaldır. Gereken GPU/device erişimini kanıtla ve sınırla.

Nextcloud ve Immich'in DB'lerini host/internet erişimine kapat; veri ağlarını yönetim, indirme ve deneysel servislerden ayır. Bir indirme aracının fotoğraf/Nextcloud dizinine yazamamasını ve DB'ye ulaşamamasını negatif testlerle doğrula. Gerçek gereksinim varsa daha güçlü VM yalıtımını kaynak/maliyet/downtime ile öner; bütün servisleri körlemesine VM'e taşıma. Güvenlik değişikliği uygulamayı bozarsa düzelt veya güvenli geri dön; korumayı topluca kapatma.

## 9. Torrent, VPN ve içerik güvenliği

Gluetun/Mullvad, Transmission (:9091), Sonarr (:8989), Radarr (:7878), Prowlarr (:9696), Jackett (:9117), FlareSolverr, Bazarr, Subgen ve Lingarr'ın ilgili dış trafiklerini kullanıcının VPN şartıyla değerlendir. Suwayomi indirmelerinde de aynı trafik ve güvenlik değerlendirmesini yap. Yerel yönetim/kimlik trafiği için gereken dar istisnaları belgeleyerek indirme ve arama trafiğinde fail-closed VPN çıkışı sağla. Port numaraları keşif ipucudur; canlı konfigürasyonu doğrula.

VPN kapanması, Gluetun yeniden başlatılması, IPv4/IPv6 ve DNS sızıntısı senaryolarını kontrollü test et. VPN yokken indirme devam etmesin; host varsayılan ağına düşmesin. Test yalnız yasal, bilinen bir test içeriği veya zararsız bağlantı kontrolüyle yapılsın. Bağlantı kopması testinin diğer servisleri etkilemesini önle. VPN veya şifreleme için anonimlik, hukuki bağışıklık veya sıfır risk garantisi verme.

Kullanıcının aktardığı olay doğrulanmış teknik/hukuki olgu kabul edilmesin. BitTorrent parça hash doğrulaması, torrent metaverisinin tanımladığı içerikle bütünlüğü denetler; içeriğin yasal veya zararsız olduğunu belirlemez. Hash'e uymayan veri reddedilse de seçilmiş torrent baştan yanlış/zararlı içerik barındırabilir. VPN içerik denetimi değildir. Beklenmeyen içeriğin tamamını yüzde yüz tespit edebilen bir filtre vaat etme. Kaçınma/delil silme yerine güvenilir yasal kaynaklar, açık kullanıcı seçimi, dosya türü/yol sınırlaması, izole indirme/karantina ve uygun kötü amaçlı yazılım taraması uygula. Antivirüsü yasa dışı içerik sınıflandırıcısı gibi sunma. Rastgele başka torrent seçme, otomatik torrent ekleme ve otomatik kütüphane içe aktarma yapma. Şüpheli içeriği incelemek için açma/çoğaltma/yükleme yapma; kullanıcıya zararsız biçimde olay ve gerekli sonraki adımı bildir.

## 10. İngilizce adlar, iki dilli belgeler

Kendi geliştirdiğimiz arayüzlerin görünen metin ve servis adlarını mümkün olduğunca İngilizce yap; örneğin `giris` için `login` önerisi değerlendirilebilir. Renaming öncesi DNS, proxy, OIDC callback, Compose project/volume kimlikleri ve diğer bağımlılıkları çıkar. Ad değişikliği yeni boş volume oluşturmasın; mevcut veri yolunu koru. Akış gibi başka proje adlarını sahibinin niyetini doğrulamadan değiştirme. Üçüncü taraf kaynak/DB/migration dosyalarını topluca yeniden adlandırma.

Yönettiğimiz her uygulama/proje ve bakım dizininde `README.tr.md` ve `README.en.md` veya açık iki dilli açıklama bulunsun: amaç, veri/konfigürasyon yolları, port/erişim, bağımlılıklar, güvenlik/MFA, başlat-durdur, yedek/geri yükleme ve bakım. Git'e girecek belgelerde sır bulunmasın. Her OS/vendor dosyasının yanına çeviri kopyası oluşturma; paket dosyalarını değiştirme. Kullanıcı içeriklerini çevirmeye, çoğaltmaya veya yeniden adlandırmaya kalkma. İki dilde içerik aynı durum ve talimatı yansıtsın.

## 11. Commit ve GitHub

IT lideri her tamamlanmış, test edilmiş anlamlı iş birimini commit etsin; uzun çalışmada 20–30 dakika kontrol noktası değerlendirsin, boş commit oluşturmasın. Müdür commit hash'i ve kısa sonuç bildirsin. Lider tek Git yazarı/operatörü olsun; diğer ajanlar eşzamanlı stage/commit yapmasın. Sadece ilgili dosyaları açıkça stage et; kullanıcıya ait başka değişiklikleri dahil etme.

Kullanıcı bu görevde incelenmiş commit'lerin GitHub'a push edilmesini istiyor; eski "push yapma" talimatı bununla değiştirilmiştir. Önce mevcut remote'u, erişimi, repo görünürlüğünü ve hangi repo/branch'ın hedef olduğunu doğrula. Birden fazla/belirsiz remote, repo yokluğu veya herkese açık hedefte iç altyapı bilgisi bulunması durumunda tam owner/repo, private/public ve branch tercihini kullanıcıdan al. Rastgele depo oluşturma; bilhassa `/etc` deposunun geçmişini kontrolsüz push etme. Daha önce etckeeper geçmişinde sır bulunduğu bildirildi: takipten çıkarmak geçmişi temizlemez. Push edilecek bütün geçmişin ve staged değişikliklerin güvenli olduğunu doğrula; sır içeren eski geçmişi yayımlama. Gerekirse geçmişi taşımayan temiz ve sırları ayıklanmış bakım deposu öner. Token/parola yenilemesini tüketiciler ve eski yedeklere erişimle birlikte yönet. Force push yapma.

Config şablonları, kod, iki dilli belge, manifest ve doğrulama kayıtlarını commit et. Fotoğraf, manga, DB dump, `.env`, LUKS başlığı, özel anahtar ve kurtarma kodlarını commit/push etme. Her küçük shell komutu için commit yerine izlenebilir anlamlı iş birimini kullan. Git yedek yerine geçmez. Paket kaldırma, veri silme, DB değişimi ve firewall için ayrı geri alma kaydı şarttır.

## 12. Bitiş ölçütü

Her uygulama için "mevcut/verisi korundu/başlatıldı/gerçek işlev test edildi/MFA/yalıtım/yedek/alarmlar/bekleyen kullanıcı eylemi" matrisi oluştur. Test edilmemişi başarılı yazma. Kullanıcı denemesi gerektiren Guacamole ve hesap/MFA adımlarını ayır. Re:Zero'nun değişmediğini manifestle doğrula. Güvenli şekilde erişilebilir fakat gereksiz portları kapalı, indirmeleri yalnız talep üzerine yapan ve VPN kaybında indirmeyi durduran bir sistem bırak.

Güvenliği "kusursuz", içeriği "asla görünmez", uygulamayı "çökmez" veya VPN'i "takip edilemez" diye nitelendirme; uygulanan kontrolü, test kanıtını ve kalan sınırı bildir. Ana yedek/geri yükleme devam ediyorsa onu koruyarak salt okunur inceleme ile başla. SSD, eski yedek retention'ı, GitHub hedefi ve cihaz/hesap işlemleri gibi eksik kararları tek kısa listede sor; yanıt gerektirmeyen güvenli bağımsız işleri ilerlet.

Referanslar / References:
- https://www.bittorrent.org/beps/bep_0003.html
- https://adguard-dns.io/kb/general/dns-filtering/
- https://github.com/tailscale/tsidp
