# Sıcak Bağlam (Hot Context Cache)

- **Aktif Proje:** [[duduk-genel-bakis]] (`/home/flugel/Projects/duduk`) — Ankara basketbol hakemi Ahmet Gökalp Göksu (`"AHMET GÖKALP GÖKSU"`) için kişisel maç, istatistik ve kazanç takip uygulaması.
- **Son Değişiklik (2026-11-11):** Android APK (`v0.1.0`) derlendi, 22 birim testi geçti, `gok8lp/duduk` özel GitHub deposuna ve Release'e yüklendi; `flugelserver` üzerinde Docker arka ucu hem Tailscale (`https://flugelserver.tail42f1f4.ts.net:18443`) hem Cloudflare (`https://duduk.gokalpgoksu.com`) üzerinden canlıya alındı; sunucuda Android 15 emülatör kurulup 5 sekme doğrulandı.
- **Mimari Özet:** [[android-arac-zinciri-ve-mimari]], [[assignr-ve-ankarabasket-kaynaklari]], [[tbf-eslestirme-algoritmasi]], [[yerel-arsiv-ve-senkronizasyon]], [[hakem-ucret-tarifesi-2026-2027]], [[ikinci-beyin-sistemi]].
- **Açık Sorular / İzlenecekler:**
  1. `BÖLGE` yerel lig maç ücreti resmi açık kaynaklarda yer almadığı için kullanıcı ilk bordrosundan sonra uygulama içi Ücret Tablosu ekranından girecek.
  2. `assignr` yeni hafta yayın günü/saati (Cuma gecesi mi Cumartesi mi) `flugelserver` saatlik arşiv döngüsüyle gözlenecek.
