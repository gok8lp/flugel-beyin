Bağlam devri: "Düdük" Android uygulaması (11 Kasım 2026'da yarıda bırakıldı). Türkçe konuş.

Ben Ahmet Gökalp Göksu, Ankara'da basketbol hakemiyim. Atama verilerinde adım "AHMET GÖKALP GÖKSU" olarak geçiyor. Maçlarımı takip etmek için Maçkolik benzeri, bana özel bir Android uygulaması yaptırıyorum. Proje yarıda kaldı. Senden aşağıdaki işleri sırayla bitirmeni istiyorum. Her adımın sonunda derlemenin ve testlerin geçtiğini gerçekten çalıştırarak doğrula. Çalıştırmadığın şeye "çalışıyor" deme.

## Ortam
- PC: Arch Linux, Hyprland, kullanıcı flugel. Bu PC'de sudo yok, isteme.
- Proje: /home/flugel/Projects/duduk. Git deposu kuruldu (git init) ama henüz commit yok.
- Derleme: `cd /home/flugel/Projects/duduk && JAVA_HOME=/usr/lib/jvm/java-17-openjdk ./gradlew :app:assembleDebug :app:testDebugUnitTest`
  - Bu komut bugün çalıştırıldı ve geçti.
  - APK çıktısı: app/build/outputs/apk/debug/app-debug.apk
  - Ayrıntılar ve sürüm tablosu: BUILD.md
- Sürümler ve SDK:
  - Gradle 9.8.0, AGP 9.4.1, Kotlin 2.3.21, Compose BOM 2026.09.00.
  - compileSdk ve targetSdk 37, minSdk 26.
  - Android SDK yolu: /home/flugel/android-sdk/sdk
- Kullanılacak kütüphaneler build dosyasında zaten var: OkHttp 5, kotlinx-serialization, coroutines, jsoup, navigation-compose, WorkManager 2.10.5, DataStore, Glance.
  - WorkManager bilerek 2.10.5'te tutuluyor; yükseltme.
  - Room, KSP ve Hilt eklenmeyecek. Veriler JSON dosyasında ve DataStore'da saklanacak.
- Paketler (`com.flugel.duduk`): data/{model,net,store,repo}, sync, notify, domain, ui/{theme,nav,screens,components}, widget.
  - İçlerinde şimdilik yalnız Paket.kt yer tutucuları var. Bu dosyaları gerçek kodla değiştir.
  - Hazır olanlar: tema (DudukTheme: açık/koyu tema ve dinamik renk), adaptive ikon ve "Düdük" yazan tek bir HomeScreen.
- Telefon PC'ye bağlı değil, yani uygulama hiçbir cihazda denenmedi. Ekran görünümünü doğruladığını iddia etme.

## Veri kaynakları
docs/VERI-KAYNAKLARI.md dosyasını baştan sona oku. Bütün uçlar orada doğrulanmış halde; örnek yanıtlar docs/samples/ altında. Testlerde bu örnek dosyaları kullan. Özetle:
- **assignr** (girişsiz GET):
  - Hakem atamaları: https://assignr.immensus.io/api/public/assignments/recent-weeks
  - Masa görevlileri: .../recent-weeks/masa
  - Salonlar ve koordinatları: .../api/public/venues
  - Yalnız son 2 haftayı veriyor; geçmiş haftaları almanın yolu yok. Bu yüzden uygulama her çekilen veriyi kendi arşivine eklemeli. Hiçbir şey silinmeyecek; istatistikler bu arşivden hesaplanacak.
  - matchNumber tek başına benzersiz değil, çünkü ertelenen maç iki kez gelebiliyor. Anahtar olarak matchNumber+date+time kullan.
  - groupName farklı biçimlerde gelebiliyor ("F", "Grup D", "-"); normalleştir.
- **ankarabasket.org.tr ana sayfası:** sayfaya gömülü `days` JSON'u bugünden 2 gün öncesiyle 4 gün sonrası arasındaki maçları ve skorları içeriyor. Buradaki `code` alanı assignr'daki matchNumber ile aynı. Günde en az bir kez çekilmeli. Ayrıştırma yöntemi: dokümanın 2.1. bölümü ve samples/ankarabasket/flight_ayristir.py.
- **TBF API:** https://miniappapi.tbf.org.tr/webapi-service
  - Lig kataloğu, sezonun bütün maçları/skorları ve puan durumu buradan geliyor.
  - Skorlar 1-2 gün gecikmeli geliyor ve matchNumber yok; maçlar dokümanın 5. bölümündeki algoritmayla eşleştirilmeli. Denemede isabet %97,9, yanlış eşleşme 0 çıktı.
  - Kimlik alanları kimi zaman "22328.0" biçiminde geliyor; sayıyı Double olarak oku.
  - Oynanmamış maçlarda matchDate tarih yerine "10. Hafta" gibi bir metin olabiliyor.
- Çeyrek skoru ve canlı skor hiçbir kaynakta yok. Uygulama bunları varmış gibi göstermesin.
- ankarabasket'in /api yolu robots.txt'te yasaklı. Lig ve takım kataloğunu çalışma sırasında oradan çekme; samples/'taki season-teams verisini uygulamaya gömülü katalog olarak koy.

## Gereksinimler (benim isteklerim)
1. **Maçlarım:** gelecek ve geçmiş maçlarım. Her maçta tarih, saat, salon (harita bağlantısıyla), lig ve grup, takımlar, birlikte görev yaptığım hakemler, masa görevlileri ve skor. Gelecek maçlarda geri sayım olsun.
2. **Fikstür:** bütün maçlar; lig, gün ve salona göre filtrelenebilsin.
3. **Puan durumu:** takımların durumu. Maç kartında iki takımın sırası ve averajı da görünsün.
4. **Hakemler:** listede her hakemin kaç maça çıktığı, hangi liglerde görev aldığı ve en sık kiminle eşleştiği.
5. **Benim istatistiğim:** toplam maç; liglere ve aylara göre dağılım; 1. ve 2. hakem olarak kaç maç; en sık eşleştiğim hakemler; düdük çaldığım maçlardaki takımların sonuçları.
6. **Kazanç:**
   - Hesap kullanıcının düzenleyebildiği bir ücret tablosuna göre yapılacak, tutarlar koda gömülmeyecek.
   - Başlangıç değerleri docs bölüm 6'dan: il içi altyapı hakem 1.700 TL, masa görevlisi 850 TL; büyükler kategorisinde erkek 3.250 TL, kadın 2.600 TL. Bu tarife özel müsabakalar için.
   - BÖLGE ligi ücreti hiçbir yerde bulunamadı. Bu satırlar boş başlasın ve "ücret tanımsız" diye işaretlensin; sıfır sayılmasın.
   - Aylık ve sezonluk toplam gösterilsin.
7. **Bildirimler** (WorkManager ile düzenli kontrol):
   - Yeni atama haftası yayınlandığında,
   - bana yeni maç atandığında,
   - atamam değiştiğinde ya da kaldırıldığında,
   - maçımdan 1 gün ve 2 saat önce,
   - skor girildiğinde.
   - Telefon yeniden başlatılınca kontrol zamanlaması yeniden kurulsun.
8. **Dinamik yapı:** lig listesi sabit kodlanmayacak. Yeni bir lig, grup veya hafta gelirse uygulama kendiliğinden eklesin. Eşleşmeyen lig adları ayrı bir "tanınmayan" listesinde görünsün.
9. **Arayüz:**
   - Akıcı ve güzel olsun.
   - Alt tarafta Apple tarzı, içeriğin üstünde yüzen, saydam ve arkasını bulanıklaştıran bir gezinme çubuğu olsun. Android 12 ve üstünde gerçek bulanıklık kullan; daha eski sürümlerde yarı saydam renk yeterli.
   - Üst başlık da aynı cam görünümünde olsun.
   - Ekran geçişleri animasyonlu olsun; aşağı çekerek yenileme, yüklenirken iskelet görünüm ve sekme değişiminde hafif titreşim olsun.
   - Büyük başlıklar, yuvarlak köşeli kartlar ve takım logoları kullan.
10. **Ana ekran widget'ı** (Glance): sıradaki maçım.
11. **Bağlantı sırası** (sunucu tarafı yazıldığında):
    1. Önce Cloudflare (planlanan adres duduk.gokalpgoksu.com),
    2. o olmazsa Tailscale (flugelserver.tail42f1f4.ts.net),
    3. o da olmazsa doğrudan açık kaynaklar.
    - İlk sürümde uygulama doğrudan kaynaklardan çalışsın. Sunucu adresi ve anahtarı ayarlardan girilsin; koda gömme.

## Yapılacak işler (sırayla; her biri ayrı commit)
1. **Veri modelleri ve ayrıştırıcılar** (data/model, data/net): assignr, ankarabasket `days` ve TBF için. Her biri için docs/samples dosyalarıyla JVM birim testi yaz.
2. **Arşiv ve depo** (data/store, data/repo):
   - Arşiv JSON dosyası, birleştirme mantığı (eskiyi silmeden üstüne ekleyen) ve değişiklik tespiti (yeni, değişen, kaldırılan atama). Testlerle.
   - TBF eşleştirme algoritması (docs bölüm 5) ve testi. docs/samples/mac-eslesme-testi.json ile isabet oranını doğrula.
3. **İstatistik ve kazanç hesapları** (domain), testleriyle.
4. **Senkronizasyon ve bildirimler** (sync, notify): WorkManager işi, bildirim kanalları, POST_NOTIFICATIONS izin isteği, açılışta yeniden kurulum.
5. **Arayüz** (ui): 5 sekme (Maçlarım, Fikstür, Puan, Hakemler, Ben/İstatistik), maç ayrıntı ekranı, kazanç ve ücret tablosu ekranı, ayarlar.
6. **Glance widget'ı.**
7. **GitHub:**
   - `gh` bu PC'de gok8lp hesabıyla giriş yapmış durumda.
   - Depo **özel (private)** açılacak: gok8lp/duduk.
   - APK'yı depoya ekleme; GitHub Release'e dosya olarak koy (v0.1.0).
   - Göndermeden önce `git ls-files` çıktısını kontrol et: local.properties, *.jks ve herhangi bir anahtar ya da parola depoya girmemeli.
8. **Sunucu arka ucu** (ayrı ve son iş; benim onayımla): flugelserver'da (SSH: `ssh flugelserver`) veriyi düzenli çekip arşivleyen ve istatistiği hesaplayan küçük bir Docker servisi.
   - Önce Tailscale Serve'de boş bir tailnet-içi portta çalıştır.
   - Cloudflare için /etc/cloudflared/config.yml'ye satır eklemek sudo gerektiriyor ve servisi internete açıyor. Bunu yapmadan önce eklenecek satırı bana göster, onayımı bekle ve dosyanın tarihli yedeğini al.
   - Sunucudaki çalışan hiçbir servise, konteynere veya dosyaya dokunma.

## Kurallar
- Gizli bilgileri (local.properties, .env, API anahtarları, parolalar, SSH anahtarları) okuma, sohbete yazma, commit'leme. Özellikle /home/flugel/Projects/koharia-reader/local.properties dosyasını açma.
- Başka projeleri ve kabuk yapılandırmasını (~/.bashrc vb.) değiştirme.
- Kaynak sitelere yavaş istek at; host başına saniyede 1-2 istekten fazla olmasın. Testlerde canlı istek değil, örnek dosyalar kullan.
- Bitince şunları kısaca söyle: ne yapıldı, nasıl doğrulandı (komut ve sonuç), ne kaldı, neyi doğrulayamadın.
