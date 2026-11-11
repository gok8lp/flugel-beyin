# FLUGEL sistem çalışma bağlamı

Bu paket 28 Ekim 2026 tarihli yerel PC ve home server gözlemleridir; canlı sistem durumu değildir.

@06-KALICI-CALISMA-TALIMATI.md

Sistem işi geldiğinde önce ilgili envanteri oku:
- PC: 01-PC-ANALIZI.md
- Sunucu: 02-SUNUCU-ANALIZI.md
- Açık sorunlar ve öncelikler: 03-BULGULAR-VE-YOL-HARITASI.md
- Ağ, konteynerler, veri yerleri: 04-MIMARI-VE-SERVIS-HARITASI.md
- Tanılama ve kabul ölçütleri: 05-CALISMA-KILAVUZU.md
- Sayısal kayıt: ENVANTER.json, KONTEYNERLER.csv, UYGULAMA-ERISIM.csv

İlk hedef doğrulaması: yerel PC mi, LAN server mı, yoksa izole cloud ortamı mı? Cloud ortamın bu iki cihaza otomatik erişimi yoktur. Paket parola, private key veya token içermez.

Bilinen tamamlanmamış iş: F11 doğrudan video preset panelini açmıyor; ok tuşlarıyla birebir tema geçişi henüz tamamlanmadı. Bu işi tamamlanmış kabul etme.

## FLUGEL yönetici modu

Kullanıcı bir isteğin başında veya açıkça komut olarak `FLUGEL` yazarsa bunu kontrollü yönetici modu isteği olarak yorumla:

- Bu tetikleyici parola, PIN veya token değildir; hiçbir sırrı hatırlama, dosyaya yazma, loglama veya sohbete aktarma.
- `sudo` ve diğer kimlik doğrulamalarını işletim sisteminin normal mekanizmasına bırak. Parolayı otomatik doldurma veya şifresiz root kabuğu açma.
- Salt okunur tanılama ve açıkça istenen düşük riskli işlemleri yetki kapsamında gerçekleştir; hedefi, etkiyi ve sonucu bildir.
- Dosya silme, disk/partition işlemleri, kullanıcı veya SSH yetkileri, firewall/ağ erişimi, veritabanı, yedek, Docker mount ve kritik sistem dosyaları için değişiklikten önce açık işlem onayı iste.
- Kritik değişikliklerde mevcut durumu kaydet, mümkünse tarihli yedek al, tek mantıksal değişiklik yap ve doğrulama/geri dönüş yolunu belirt.
- Cloud/izole oturumun LAN sunucuya erişimini varsayma; ağ ve kimlik doğrulamasını gerçekten doğrulamadan bağlandığını veya değişiklik yaptığını söyleme.
- `FLUGEL` yazılmış olması kullanıcı adına sınırsız yetki, güvenlik kontrollerini atlama veya geri döndürülemez işlem izni vermez.

## Yerel beceriler

Uygun görevde ~/.claude/skills altındaki homelab-kontrol, homelab-degisiklik, masaustu-dogrula ve hata-teshis becerilerini kullan. Bunlar ayrı bir yetki veya gözetimsiz zamanlayıcı vermez. /handoff, yalnız kullanıcı çağırdığında devir notu üretir.

## Matt Pocock tam beceri deposu

38 upstream beceri kişisel ~/.claude/skills dizininde destek dosyalarıyla kurulu. Kaynak kopyası ~/.local/share/claude-skill-sources/mattpocock-skills. TDD, code-review, diagnosing-bugs, implement, to-spec, to-tickets ve diğerlerini ilgili görevde kullan. Explicit-only becerileri kullanıcı komutuyla çağır. Proje özelindeki issue tracker/domain ayarlarını /setup-matt-pocock-skills ile ilgili repo içinde kur; paket kurulması bu kurulum akışının çalıştığı anlamına gelmez.
