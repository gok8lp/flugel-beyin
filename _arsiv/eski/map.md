# Harita (Map) — İkinci Beyin Navigasyon Merkezi

> Bu dosya fırtınanın en altında durur. Her sorgudan önce yüklenir; her bilginin tam olarak hangi dosyada yaşadığını gösterir. **Uzun vadeli hafıza (`memory.md`) ve karar günlüğü (`decisions.md`) her zaman odaktadır.**

## 1. Odak Kök Dosyalar (Her Zaman Aktif)
- `memory.md` ([[memory]]): Uzun vadeli hafıza, kullanıcı kimliği (`"AHMET GÖKALP GÖKSU"`), sunucu adresleri, aktif sezon (`2026-2027`, TBF `seasonId=174`).
- `decisions.md` ([[decisions]]): Mimari kararların neden öyle alındığının kaydı (WorkManager `2.10.5`, Room/Hilt kullanmama, `BÖLGE` ücretinin `null` başlaması, `akis` Cloudflare tüneli).
- `lessons.md` ([[lessons]]): Tersine mühendislik ve geliştirme sırasında öğrenilen teknik dersler ve tuzaklar.
- `CLAUDE.md` ([[CLAUDE]]): İletişim kuralları, izinler ve `brain.py` iş akışı.

## 2. Derlenmiş Wiki (`wiki/` — `brain.py lint` ile Doğrulanmış)
- `wiki/hot.md`: Sıcak bağlam önbelleği (12 satır).
- `wiki/index.md`: Otomatik üretilen wiki indeksi.
- `wiki/log.md`: Kronolojik ingest günlüğü.
- `wiki/duduk-genel-bakis.md` ([[duduk-genel-bakis]]): Düdük uygulaması vizyonu ve gereksinimleri.
- `wiki/assignr-ve-ankarabasket-kaynaklari.md` ([[assignr-ve-ankarabasket-kaynaklari]]): `assignr`, `ankarabasket` ve `TBF` uçları ve şema tuzakları.
- `wiki/tbf-eslestirme-algoritmasi.md` ([[tbf-eslestirme-algoritmasi]]): %97,9 isabetli bulanık maç/lig eşleştirme algoritması.
- `wiki/yerel-arsiv-ve-senkronizasyon.md` ([[yerel-arsiv-ve-senkronizasyon]]): Silinmeyen JSON arşiv, değişiklik tespiti ve bildirimler.
- `wiki/hakem-ucret-tarifesi-2026-2027.md` ([[hakem-ucret-tarifesi-2026-2027]]): 2026-2027 görevli ücret tarifesi ve `BÖLGE` kuralı.
- `wiki/android-arac-zinciri-ve-mimari.md` ([[android-arac-zinciri-ve-mimari]]): Gradle 9.8.0 / AGP 9.4.1 / Kotlin 2.3.21, Compose cam arayüz ve sunucu zinciri.
- `wiki/ikinci-beyin-sistemi.md` ([[ikinci-beyin-sistemi]]): Karpathy / `@rektwild` İkinci Beyin mimarisi ve `brain.py`.

## 3. Atomik Notlar (`notes/` — Her Dosyada Tek Konu)
- `notes/assignr-api-yapisi.md` ([[assignr-api-yapisi]]): `assignr` uçları, 2 haftalık pencere ve `matchNumber|date|time` birleşik anahtarı.
- `notes/ankarabasket-rsc-flight-ayristirma.md` ([[ankarabasket-rsc-flight-ayristirma]]): Next.js RSC Flight doğrusal ayrıştırıcısı ve `robots.txt` kuralları.
- `notes/tbf-bulanik-mac-eslestirme.md` ([[tbf-bulanik-mac-eslestirme]]): `SequenceMatcher` + `0.3` slot ödülü formülü.
- `notes/hakem-kazanc-ve-bolge-kurali.md` ([[hakem-kazanc-ve-bolge-kurali]]): `BÖLGE` maçlarının neden `null` ("ücret tanımsız") tutulduğu.
- `notes/cloudflare-ve-tailscale-baglanti-zinciri.md` ([[cloudflare-ve-tailscale-baglanti-zinciri]]): `duduk.gokalpgoksu.com` → `flugelserver.tail42f1f4.ts.net:18443` → Doğrudan kaynaklar.

## 4. Kişiler (`people/`)
- `people/ahmet-gokalp-goksu.md` ([[ahmet-gokalp-goksu]]): Ahmet Gökalp Göksu — rolü, hakem profili, sorumlulukları ve ortam bilgileri.

## 5. Projeler (`projects/`)
- `projects/duduk/CLAUDE.md`: Düdük projesinin tanımı, tek hedefi ve bitmiş kriterleri.
- `projects/duduk/duduk-durum.md` ([[duduk-durum]]): Projenin güncel durumu, doğrulanan adımlar ve sıradaki adımlar.
- `projects/duduk/Inputs/veri-kaynaklari-ve-ornekler.md`: Ham veri kaynakları ve test örnekleri.
- `projects/duduk/Process/mimari-ve-test-sureci.md`: Geliştirme, birim testi ve emülatör doğrulama süreci.
- `projects/duduk/Outputs/apk-github-ve-sunucu-ciktilari.md`: APK, GitHub Release `v0.1.0` ve canlı sunucu uçları.
- `projects/duduk/Feedback/dogrulama-ve-acik-riskler.md`: Emülatör ekran görüntüsü geri bildirimleri ve açık riskler.

## 6. Genişletilmiş Teknik Referans (`Düdük - Side Brain/`)
- `Düdük - Side Brain/00 - Düdük MOC (Ana Merkez).md`
- `Düdük - Side Brain/01 - Veri Kaynakları ve Tersine Mühendislik.md`
- `Düdük - Side Brain/02 - TBF Maç ve Lig Eşleştirme Algoritması.md`
- `Düdük - Side Brain/03 - Yerel Arşiv, Birleştirme ve Değişiklik Tespiti.md`
- `Düdük - Side Brain/04 - Hakem İstatistikleri ve Ücret Tarifesi (2026-2027).md`
- `Düdük - Side Brain/05 - Android Mimari, Senkronizasyon, Bildirimler, Arayüz ve Sunucu Zinciri.md`
- `Düdük - Side Brain/2026-2027 Ankara Lig Eşleşme Tablosu.md`
- `Düdük - Side Brain/Veri Tuzakları ve Uç Durumlar Kataloğu.md`
