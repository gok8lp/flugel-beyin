# Flugelserver'ı düzenleme, onarma ve güvenli hâle getirme görevi

Sunucum dağınık. Sadece öneri raporu verme: mevcut durumu incele, uygulanabilir hedef düzeni belirle, gerekli düzeltmeleri yap ve sonucu doğrula. İşi aşamalı yürüt; sorunları gizleyen geçici çözümler yerine anlaşılır, bakımı kolay bir sistem bırak.

## Bağlantı ve skill'ler

Bu PC'den mevcut `flugelserver` SSH tanımını kullan. Skill dosyaları `~/Documents/Claude-Sunucu-Skills/` altında; kurulu değillerse önce `sunucuna-ozel/` altındaki üç klasörü `~/.claude/skills/` altına mevcut dosyaları ezmeden kopyala. Bu oturumda henüz keşfedilmiyorlarsa SKILL.md dosyalarını doğrudan oku:

- flugel-backup-recovery
- flugel-compose-maintenance
- flugel-network-access

Hazır medya skill'lerini yalnızca korunacak bir işlev için gerçekten gerektiğinde kullan. `istege-bagli/` içindekileri otomatik olarak kurma; R2 veya Ansible kullanma kararını ihtiyaca göre ver. Skill kurulumu yeni oturum gerektirirse bunu açıkça belirt ve görev metnini yeni oturumda devam ettirebileceğim şekilde bırak.

5 Kasım 2026 ön incelemesi Ubuntu 26.04, `/opt/stacks` altında Docker Compose, libvirt, Tailscale, Cloudflare Tunnel, Mullvad/Gluetun ve çok sayıda özel systemd görevi gösterdi. Bunlar başlangıç ipuçlarıdır; mevcut durumu yeniden doğrula. Bazı yedek timer'ları devre dışıydı; bu durumun sebebini ve alternatif yedekleri araştır.

## Mutlaka korunacaklar

1. **Immich ve bütün fotoğraf/video arşivi.** Orijinaller, dış kütüphaneler, kullanıcılar, albümler, metaveri, veritabanları, gerekli eklentiler, depolama eşlemeleri ve erişim ayarları korunacak. Önizleme/ML gibi yeniden üretilebilir içerikleri bile kaynak ve bağımlılıklarını doğrulamadan silme.
2. **Nextcloud ve tüm kullanıcı dosyaları.** Veritabanı, config, hesaplar, paylaşımlar, uygulamaların gerekli durum verileri ve depolama eşlemeleri korunacak. Senkronizasyonu bozacak yeni/boş bir kurulumla değiştirme.
3. **Manga okuma uygulamaları ve bütün manga/çizgi roman içeriği.** Envanterde Komga, Kavita ve Suwayomi vardı; kullanıcı aksini belirtmedikçe üçünü de koru. Kütüphaneler, indirmeler, okuma ilerlemesi, kullanıcılar, veritabanları, kaynak/eklenti ayarları ve kapak/metaveri dosyaları korunacak.
4. Bu hizmetlerin çalışması için gereken ortak bağımlılıklar da korunacak veya doğrulanmış bir alternatifle kontrollü biçimde değiştirilecek: PostgreSQL, gerekli Redis/worker/ML bileşenleri, Docker volume/bind mount'ları, dosya sahiplikleri, disk bağlama ve şifre çözme düzeni, gerekli GPU sürücüleri ve erişim yolları.

**Korumayı klasör adından tahmin etme.** Gerçek Compose dosyaları, mount'lar, symlink'ler, harici diskler ve uygulama ayarlarından veri bağımlılık haritası çıkar. Paylaşılan bir dizinde korunacak içerik varsa dizini topluca silme. LUKS anahtarları, crypttab/fstab, SSH erişimi, sertifikalar ve gerekli kimlik bilgilerini kaybetme. Sırları sohbet veya rapora yazma.

## Kaldırma ve değişiklik yetkisi

Yukarıda korunması istenen uygulamalar, veriler ve bunların gerekli altyapısı dışında kalan gereksiz uygulamaları, eski projeleri, artık konteynerleri, kullanılmayan VM'leri, çakışan görevleri ve gereksiz verileri kaldırmana izin veriyorum. Bu yetki, korunacak verilerle ilişkisi belirsiz dosyaları silme veya işletim sistemi/diskleri körlemesine sıfırlama yetkisi değildir. Disk formatlama ya da OS yeniden kurulumu gerekiyorsa somut taşıma/kurtarma planını sun ve bu ayrı işlem için onay iste.

Örneğin Plex, Jellyfin, Sonarr/Radarr, indirme servisleri, eski botlar ve deneysel laboratuvarlar kaldırma adayı olabilir; sadece adlarına bakarak kullanılmadıklarına karar verme. Korunacak manga hizmetlerinin bunlara bağımlı olup olmadığını doğrula. Kullanıcı dosyaları, fotoğraflar veya kitapların yer aldığı ortak depolamayı silme.

Silmeden önce gerçek hedefleri, boyutlarını, bağımlılık gerekçelerini ve korunacak veriyle çakışmadıklarını içeren bir kaldırma manifesti oluştur ve kısa bir özetini göster. Kesin olarak kapsam içinde kalan bağımsız bileşenler için tekrar tekrar izin isteme; kapsamı belirsiz veya korunacak veriye temas eden hedefleri bırakıp tek bir toplu soru sor. Kullanılabilir alan uygunsa geri alınabilir kaldırmayı tercih et. Hangi verilerin gerçekten kalıcı silindiğini açıkça kaydet; bir taşıma işlemini silme olarak raporlama.

## Önce kurtarılabilirliği doğrula

Değişikliklerden önce korunacak sistemin tutarlı yedeğini al veya mevcut yedeğini doğrula. Veritabanı için uygulama sürümüne uygun yöntem kullan; çalışan PostgreSQL dizinini kopyalamayı tek başına tutarlı yedek sayma. Ayrı geçici konumda geri yükleme doğrulaması yap. Yerel bir dizinin başka diskte ya da bağımsız yedek olduğunu varsayma.

Yedek için yeterli kapasite/erişim yoksa mevcut güvenli salt okunur inceleme ve bağımsız düşük riskli düzeltmelere devam et; korunan veri üzerinde geri dönüşsüz işlem yapmadan önce eksik kapasite/konum kararını sor. Bulut hesabı açma veya ücretli depolama satın alma.

## Hedef düzen

- Çalışan ve tekrar başlatıldığında düzgün açılan Immich, Nextcloud, Komga, Kavita ve Suwayomi.
- Açıkça tanımlanmış Compose projeleri, veri dizinleri ve dosya izinleri. Yalnız estetik bir klasör düzeni için büyük veri taşıma yapma.
- Çakışan self-heal/watchdog/otomatik güncelleme işleri yerine anlaşılır, asgari otomasyon. Önce her görevin ne yaptığını incele; gerekli görevi kaybetme.
- Gerçek uygulama sağlık kontrolleri, makul kaynak sınırları, log rotasyonu ve disk doluluk takibi.
- Uygulama sürümleriyle uyumlu güncelleme yolu; hareketli image etiketleri yerine mümkün olduğunca izlenebilir sürümler. Geri dönüş için önceki image digest'lerini ve DB geçişlerinin sınırlarını kaydet.
- Zamanlanmış, hata bildiren ve geri yüklenmesi doğrulanmış yedekleme. Retention hedefini mevcut alan ve veri önceliklerine göre belirle.

## Güvenlik iyileştirmeleri

Önce gerçek dışa açıklığı, host ve Docker portlarını, yönetim yollarını, DNS ve VPN akışını incele. Gereksiz yayımlanan portları kapat; veritabanlarını internete açma. Gerekli web erişiminde HTTPS ve uygulama kimlik doğrulamasını doğrula. Cloudflare/Tailscale bulunduğu için her servisin zaten korunduğunu varsayma.

SSH anahtarlı erişimi, sudo yetkilerini, servis kullanıcılarını, Compose yetkilerini ve secret dosya izinlerini değerlendir. Root/privileged/container socket erişimini yalnız gerekliyse bırak; gerekli GPU ve uygulama işlevlerini test et. Mevcut CrowdSec/Fail2ban/firewall araçlarını incele; birbirini tekrarlayan yeni güvenlik yazılımları ekleme. Docker'ın yayımladığı portların host firewall kurallarıyla ilişkisini ayrıca kontrol et.

Yönetim bağlantısını kesebilecek ağ/firewall/SSH değişikliklerini geri alma yöntemi ve ikinci bağlantıyla doğrulama olmadan uygulama. Gerekli şifre/token değişimlerini tüketici servisleriyle birlikte yönet; mevcut oturumları veya entegrasyonları habersiz bozma. 2FA gibi kullanıcının kayıt/kurtarma kodu alması gereken adımlarda gereken kullanıcı eylemini açıkça belirt.

## Standart araçlar

Gereken, bakımı süren araçları dağıtımın güvenilir kaynaklarından kur; mevcut eşdeğer varsa onu kullan. Örneğin curl, jq, git, rsync, SMART araçları ve seçilen yedekleme aracı gerçekten ihtiyaç varsa uygundur. "Standart uygulamalar" ifadesi yeni medya servisleri, kontrol panelleri veya rastgele büyük paket koleksiyonları kurma isteği değildir. Kurulacak ek araçların amacını belirt. Immich/Nextcloud/manga uygulamalarını değiştiren alternatif ürünler kurma.

## Git kayıtları, ilerleme takibi ve geri dönüş

İşe başlamadan önce mevcut Git depolarını ve çalışma ağacındaki kullanıcı değişikliklerini kontrol et. Kullanıcının değişikliklerini kendi değişikliklerinle aynı commit'e katma. Var olan uygun altyapı deposu varsa onu kullan; yoksa sunucuda mevcut verilerle çakışmayan, yalnız bu bakımın sır içermeyen yapılandırma ve dokümantasyonunu tutacak bir yerel depo oluştur. Bütün `/`, `/srv` veya `/opt` dizinini Git deposuna çevirme. Depo konumunu, branch adını ve salt okunur ilerleme izleme komutlarını kullanıcıya bildir. Uzak depoya push veya yeni GitHub deposu oluşturma bu talimatın kapsamında değildir.

Değişiklik yapmadan önce başlangıç durumunu sır içermeyen bir envanter ve uygun yapılandırma kopyalarıyla kaydet; `checkpoint: başlangıç envanteri` commit'i oluştur. Git'e fotoğraf, manga, Nextcloud kullanıcı dosyaları, veritabanı dump'ları, volume içerikleri, loglar, özel anahtar, `.env`, parola, API token veya sır içeren yapılandırma ekleme. Compose/systemd dosyalarında gömülü sır varsa Git'e yalnız sırlardan arındırılmış şablon ve referans koy; gerçek dosyayı izinleri kısıtlı ayrı yedekte tut. `.gitignore` tek başına yeterli kontrol değildir: her commit öncesi sahnelenen diff'i sırlar ve kapsam dışı dosyalar açısından incele. Sır taramasının çıktısında da sırları gösterme.

Commit sıklığı: her tamamlanmış ve doğrulanmış anlamlı aşamadan sonra commit oluştur (örneğin yedekleme doğrulaması, tek uygulamanın Compose düzeltmesi, ağ erişim kontrolü veya gereksiz bir bileşenin kaldırılması). Aktif çalışma uzarsa yaklaşık 20–30 dakikada bir uygun kontrol noktasını değerlendir; değişiklik yoksa boş commit oluşturma. Süre doldu diye yarım veya doğrulanmamış işi başarılı olarak kaydetme. Gereken ara WIP kaydını açıkça WIP ve doğrulanmamış olarak işaretle. Özellikle riskli değişikliklerden hemen önce geri dönüş için gerekli önceki durumun kaydedildiğini doğrula.

Her aşamada `ILERLEME.md` dosyasını güncelle: tamamlanan işler, devam eden iş, doğrulama sonucu, sıradaki adım ve mevcut engeller. `DEGISIKLIK-GUNLUGU.md` içinde tarih/saat ve saat dilimi, yapılan değişiklik, etkilenen servis/dosya, test sonucu ve geri alma yöntemi olsun. Bu dosyaları ilgili commit'e dahil et. Commit hash'ini commit tamamlandıktan sonra kullanıcıya kısa güncellemede bildir; bir commit'in kendi hash'ini aynı commit'in içindeki dosyada tutmaya çalışma. Mesajlar anlaşılır ve aşamaya özgü olsun: örneğin `fix(nextcloud): sağlık kontrolünü düzelt` veya `chore(backup): geri yükleme testini belgele`.

Git commit'i canlı sunucunun snapshot'ı veya yedeği değildir. Veritabanı migration'ı, dosya silme, Docker volume değişimi, paket kaldırma ve ağ kuralı değişikliğini yalnız `git revert` ile geri alınabilir diye sunma. Bu işlemler için ilgili yedek/snapshot, önceki image digest'i, paket sürümü, ağ kuralı çıktısı veya geri alma komutlarını ayrı belirle. Fotoğraf/manga/veritabanını Git'e koyarak bu açığı kapatmaya çalışma.

Bir değişiklik doğrulamayı bozarsa sonraki aşamaya geçme: kanıtı kaydet, nedeni araştır ve güvenliyse son doğrulanmış çalışır duruma dön. Geri dönüşü de uygula ve doğrula; yalnız dosyayı geri almakla servis geri dönmüş sayılmaz. Geri alma korunan veriyi kaybettirecekse ya da güvenli olduğu kanıtlanamıyorsa o işlemde durup eksik kararı kullanıcıdan iste; bağımsız güvenli işlere devam edebilirsin. Ortak geçmişte `git reset --hard` veya geçmişi silmek yerine uygun düzeltme/revert commit'i kullan; kullanıcının önceki değişikliklerine dokunma.

Son teslimde başlangıç ve son commit kimliklerini, aşama commit'lerinin kısa listesini, başarısızlık ve geri dönüşleri ve mevcut bekleyen değişiklikleri bildir. Kullanıcının `git log --oneline --decorate -20`, `git status --short` ve `git show --stat <commit>` ile takip edebilmesi için gerçek depo yoluyla örnek komutlar ver. Git kayıtlarını otomatik bir yedek sistemi gibi tanıtma.

## Doğrulama ve teslim

Aşamalar boyunca ne bulunduğunu, ne değiştiğini ve neyin sırada olduğunu kısa Türkçe güncellemelerle bildir. Sonuç raporunda şunları ver:

- Korunan uygulamalar ve gerçek veri yolları; kaldırılan bileşenler ve kalıcı silinen veri özeti.
- Her uygulama için giriş/erişim, mevcut içerik ve ilgili işlev testleri. Immich'te mevcut fotoğrafı görüntüleme, Nextcloud'da mevcut dosyayı indirme/senkronizasyon durumu, manga uygulamalarında kitap açma ve mevcut okuma ilerlemesi. Hesapla UI testi yapamadıysan yapılmış gibi gösterme.
- Başlangıç bağımlılıkları ve otomatik açılışın kontrolü; gerçek reboot testi gerekiyorsa beklenen kesintiyi bildir, yapılmadıysa bunu belirt.
- Yedekleme zamanı/konumu, geri yükleme testinin sonucu, yeni bakım ve güvenlik düzeni.
- Devam eden sorunlar, kullanıcıdan gereken eylemler ve geri alma yönergeleri.

Sunucuda uygun bir dokümantasyon konumunda sır içermeyen kısa işletim rehberi bırak. İşin bittiğini yalnızca container "running" durumuna bakarak söyleme. Korunacak veriler ve hizmetler doğrulanmadan yedekleri veya eski çalışır yapılandırmayı temizleme.
