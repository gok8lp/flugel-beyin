---
tur: proje
etiketler:
  - proje
  - android
  - kotlin
  - basketbol
  - hakemlik
  - flugelserver
  - docker
durum: aktif
olusturma: 2026-11-11
guncelleme: 2026-11-26
---

# Düdük — Ankara Basketbol Hakem Atama, Fikstür ve İstatistik Uygulaması

> Üst bağlantı: [[HARITA]] · Odak: [[simdi]] · Bağlam: [[hafiza]] · Kararlar: [[kararlar]] · Sorumlu: [[kisiler/ahmet-gokalp-goksu]]

## Genel Bakış ve Amaç
**Düdük** (`gok8lp/duduk`), Ankara basketbol il temsilciliği bünyesindeki hakem ve masa görevlisi atamalarını, lig fikstürlerini, puan durumlarını, hakem istatistiklerini ve 2026-2027 sezonu görevli ücretlerini takip etmek için geliştirilen kişisel bir Android uygulaması (`com.flugel.duduk`) ve `flugelserver` üzerinde çalışan Docker tabanlı arka uç servisidir.

- **GitHub Deposu:** `https://github.com/gok8lp/duduk` (Özel / Private, Kotlin)
- **Son Güncelleme:** `2026-11-11T14:10:59Z`
- **Veri Kaynakları Zinciri:**
  1. `assignr.immensus.io` JSON uçları (hakem ve masa görevlisi haftalık atamaları, salon listesi)
  2. `ankarabasket.org.tr` Next.js RSC Flight yükleri (`anasayfa-days`, kulüpler, duyurular, sezon takımları)
  3. `tbf.org.tr` API ve lig sayfaları (resmî maç sonuçları, puan durumu, lig/hafta eşleştirmesi)
  4. `flugelserver` `/v1` arka uç servisi (arşivleyici, istatistik hesaplayıcı, önbellek ve hız sınırlı API)

## Mevcut Durum (11 Kasım 2026)
Proje **aktif** ve 8 ana geliştirme aşaması tamamlanmış durumdadır:
- **Veri ve Eşleştirme:** Assignr, Ankarabasket ve TBF ayrıştırıcıları ile %97,9 isabet oranına sahip bulanık TBF maç/lig eşleştirme algoritması (`Eslestirme.kt`, `Normalizasyon.kt`) doğrulandı.
- **Yerel Arşiv ve Birleştirme:** Değişiklik tespiti (hakem, saat, salon değişimi), gömülü katalog (`clubs.json`, `season-teams.json`, `tbf-catalog.json`, `venues.json`) ve yerel birleştirici (`Birlestirici.kt`, `ArsivDeposu.kt`) çalışıyor.
- **İstatistik ve Kazanç:** 2026-2027 özel ve resmî müsabaka ücret tarifesine göre kişisel kazanç ve maç dağılımı hesaplayıcı (`IstatistikHesaplayici.kt`, `KazancHesaplayici.kt`) birim testleriyle tamamlandı.
- **Arka Plan ve Bildirimler:** `WorkManager` senkronizasyon işleri (`SenkronIsi.kt`), açılış alıcısı (`AcilisAlicisi.kt`), maç hatırlatmaları ve atama değişikliği bildirim kanalları kuruldu.
- **Arayüz ve Widget:** 5 sekmeli buzlu cam (glassmorphism) arayüz (`CamBilesenleri.kt`, `HomeScreen.kt`, `MaclarVeFiksturScreens.kt`, `PuanVeHakemlerScreens.kt`, `BenVeKazancScreens.kt`) ve ana ekranda sıradaki maçı gösteren Glance widget (`SiradakiMacWidget.kt`) eklendi.
- **Sunucu Arka Ucu:** `flugelserver` üzerinde Docker servisi olarak çalışan arşivleyici, istatistik hesaplayıcı ve `/v1` uçları hız sınırı (rate limit), parametre doğrulaması ve güvenlik başlıklarıyla sertleştirildi.

## Sıradaki Adımlar
- [ ] Cuma 13 Kasım 2026 Taha Akgül Spor Salonu maçları (U14 Erkek B 17:30 ve U18 Erkek B 19:00) öncesinde gerçek zamanlı bildirim ve Glance widget akışını sahada doğrulamak.
- [ ] 14-20 Kasım 2026 haftası Assignr atamaları yayımlandığında değişiklik tespiti ve arşiv birleştirmesini kontrol etmek.
- [ ] `flugelserver` `/v1` uçlarının Tailscale üzerinden mobil istemciyle uzun süreli senkronizasyon kararlılığını izlemek.

## Geliştirme Ortamı ve Canlı Uçlar
2026-11-14'te [[hafiza]] dosyasından taşındı (o dosyaya eski `memory.md`'den birleştirilmişti).

- **Depo:** `https://github.com/gok8lp/duduk` (**Private**). Kanonik depo bu; `origin/HEAD -> origin/master` (kaynak: `git -C ~/Projects/duduk remote -v` ve `symbolic-ref refs/remotes/origin/HEAD`, 2026-11-26).
- **Yerel dizin:** Laptop (gokalp): `/home/gokalp/Projects/duduk` (doğrulandı; o gün `ad-eslestirme-v0.2.2` dalında, `092421b`). PC/sunucu (flugel): `/home/flugel/Projects/duduk` (11 Kasım notundan kalma yol, bu oturumda doğrulanmadı).
- **Kardeş klasörler (`~/Projects/duduk-*`):** aynı `origin`'e bağlı ayrı çalışma kopyaları, kanonik değil: `duduk-ios-kalite` (dal `ios-kalite`, v0.4.x işi) ve `duduk-lane-{bildirim,dagilim,kartpaylas,kurallar,notlar,siradaki,takvim}` (dal `lane/<ad>`, paralel özellik şeritleri; içlerinde `BIRLESTIRME-NOTU.md` var).
- **Güncel sürüm:** git etiketleri `v0.4.0` (2026-11-24), `v0.3.0`, `v0.2.2`, `v0.2.1`, `v0.2.0` (`git tag --sort=-creatordate`). v0.4.1 etiketsiz, `ios-kalite` dalında `0eeabfc`. En yeni rapor: `/home/gokalp/Documents/ai_workplace/second-brain/raporlar/duduk-ios-kalite-2026-11-24.md` (v0.4.1, 197 test, 0 hata). Diğer raporlar: `duduk-v030-release-2026-11-22.md`, `duduk-ad-eslestirme-2026-11-22.md`, `duduk-elle-duzeltme-takas-2026-11-24.md`, `duduk-hltv-DEVIR-claude1-2026-11-22.md`. (Aşağıdaki "Son Commit Geçmişi" 11 Kasım'a aittir, eskidir.)
- **Derleme/test kuralı:** Android derleme bu PC'de değil, flugelserver'da yapılır: `ssh flugelserver` → `~/ai-sandbox/android-calistir.sh duduk ./gradlew :app:assembleDebug :app:testDebugUnitTest` (kaynak: `/home/gokalp/Documents/ai_workplace/AGENTS.md` bölüm 1). Eski komut (`/home/flugel/Projects/duduk` içinde doğrudan `./gradlew`, 11 Kasım) geçersiz sayılır.
- **Canlı uç yolları:** `/v1/health`, `/v1/bundle`, `/v1/stats`; sunucuda konteyner `duduk-server` → `127.0.0.1:18420` (`~/duduk-server`, Compose: `~/duduk-server/docker-compose.yml`).
- **Canlı uçlar:**
  1. Cloudflare Tunnel (`akis.yml`): `https://duduk.gokalpgoksu.com`
  2. Tailscale Serve: `https://flugelserver.tail42f1f4.ts.net:18443`
  3. Doğrudan açık kaynaklar (`assignr`, `ankarabasket`, `TBF`)
- **Emülatör (`flugelserver`):** SDK `/home/flugel/android-sdk`, AVD `duduk_avd` (`system-images;android-35;google_apis;x86_64`).
- **Aktif sezon:** `2026-2027`, TBF `seasonId=174`.

## Son Commit Geçmişi
- `18bfbe0` (2026-11-11): 8. Sunucu: hız sınırı, parametre doğrulaması ve güvenlik başlıkları sertleştirmesi
- `7e2ae77` (2026-11-11): 8. Sunucu: `__pycache__` temizliği ve `.gitignore` güncellemesi
- `0287cc6` (2026-11-11): 8. Sunucu arka ucu (Docker servisi): arşivleyici, istatistik hesaplayıcı ve `/v1` uçları
- `616281c` (2026-11-11): 6. Glance widget: ana ekranda sıradaki maçım widget'ı ve seçici testi
- `7aad8e0` (2026-11-11): 5. Arayüz: 5 sekme, cam üst/alt çubuklar (glassmorphism), maç ayrıntısı, kazanç/ücret tablosu ve ayarlar
- `1d3d697` (2026-11-11): 4. Senkronizasyon ve bildirimler: WorkManager işleri, bildirim kanalları, hatırlatmalar ve açılış alıcısı
- `59884f1` (2026-11-11): 3. İstatistik ve kazanç hesapları: hakem listesi, kişisel dağılım ve düzenlenebilir ücret tablosu (testleriyle)
- `cc5c9f4` (2026-11-11): 2. Arşiv ve depo: birleştirme, değişiklik tespiti, gömülü katalog ve TBF eşleştirme (%97,9 isabet testi)
- `533eb83` (2026-11-11): 1. Veri modelleri ve ayrıştırıcılar: assignr, ankarabasket days, TBF; hız sınırlı HTTP ve kaynak zinciri; örnek dosyalarla testler
- `9368eb2` (2026-11-11): İskelet: Gradle/AGP yapılandırması, tema, ikon, dokümanlar ve örnek veriler

## İlgili Sayfalar ve Bağlantılar
- **Harita ve Kök:** [[HARITA]] · [[simdi]] · [[hafiza]] · [[kararlar]] · [[dersler]]
- **İlgili Projeler ve Kişiler:** [[projeler/hakemlik]] · [[projeler/flugel-sunucu-ve-akis]] · [[kisiler/ahmet-gokalp-goksu]]
- **Wiki Sayfaları:**
  - [[wiki/repo-duduk]]
  - [[wiki/duduk-genel-bakis]]
  - [[wiki/assignr-ve-ankarabasket-kaynaklari]]
  - [[wiki/tbf-eslestirme-algoritmasi]]
  - [[wiki/yerel-arsiv-ve-senkronizasyon]]
  - [[wiki/hakem-ucret-tarifesi-2026-2027]]
  - [[wiki/android-arac-zinciri-ve-mimari]]
- **Bilgi Notları:**
  - [[notlar/assignr-api-yapisi]]
  - [[notlar/ankarabasket-rsc-flight-ayristirma]]
  - [[notlar/tbf-bulanik-mac-eslestirme]]
  - [[notlar/hakem-kazanc-ve-bolge-kurali]]

> Kaynaklar: `raw/github/00-github-envanteri.md`, `raw/github/01-tum-repolar-commit-gecmisi.md`, `raw/github/duduk.md`
