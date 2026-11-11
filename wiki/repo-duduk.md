---
title: GitHub Depo Analizi — gok8lp/duduk
sources: raw/github/duduk.md, raw/github/00-github-envanteri.md, raw/github/01-tum-repolar-commit-gecmisi.md
updated: 2026-11-11
---

# GitHub Depo Analizi: `gok8lp/duduk`

Üst Katalog: [[github-repolar-katalogu]] · [[sunucu-ve-github-commit-gecmisi]] · [[duduk-genel-bakis]] · [[flugelserver-genel-mimari]]

> "GitHub Repo: gok8lp/duduk" - raw/github/duduk.md

> "gok8lp GitHub Depoları Tam Commit Geçmişi" - raw/github/01-tum-repolar-commit-gecmisi.md

## Son Commit Geçmişi (`gok8lp/duduk`)
- `18bfbe0` (2026-11-11): 8. Sunucu: hız sınırı, parametre doğrulaması ve güvenlik başlıkları sertleştirmesi
- `7e2ae77` (2026-11-11): 8. Sunucu: __pycache__ temizliği ve .gitignore güncellemesi
- `0287cc6` (2026-11-11): 8. Sunucu arka ucu (Docker servisi): arşivleyici, istatistik hesaplayıcı ve /v1 uçları
- `616281c` (2026-11-11): 6. Glance widget: ana ekranda sıradaki maçım widget'ı ve seçici testi
- `7aad8e0` (2026-11-11): 5. Arayüz: 5 sekme, cam üst/alt çubuklar (glassmorphism), maç ayrıntısı, kazanç/ücret tablosu ve ayarlar
- `1d3d697` (2026-11-11): 4. Senkronizasyon ve bildirimler: WorkManager işleri, bildirim kanalları, hatırlatmalar ve açılış alıcısı
- `59884f1` (2026-11-11): 3. İstatistik ve kazanç hesapları: hakem listesi, kişisel dağılım ve düzenlenebilir ücret tablosu (testleriyle)
- `cc5c9f4` (2026-11-11): 2. Arşiv ve depo: birleştirme, değişiklik tespiti, gömülü katalog ve TBF eşleştirme (%97,9 isabet testi)
- `533eb83` (2026-11-11): 1. Veri modelleri ve ayrıştırıcılar: assignr, ankarabasket days, TBF; hız sınırlı HTTP ve kaynak zinciri; örnek dosyalarla testler
- `9368eb2` (2026-11-11): İskelet: Gradle/AGP yapılandırması, tema, ikon, dokümanlar ve örnek veriler

## Dosya Ağacı ve README Özeti
# GitHub Repo: gok8lp/duduk

- **URL:** https://github.com/gok8lp/duduk
- **Görünürlük:** Özel (Private)
- **Ana Dil:** Kotlin
- **Son Güncelleme:** 2026-11-11T14:10:59Z
- **Açıklama:** Düdük — Ankara basketbol hakem atama, fikstür, puan durumu ve istatistik takip uygulaması

## Dosya Ağacı (File Tree)
- `.gitignore` (blob)
- `BUILD.md` (blob)
- `DEVIR.md` (blob)
- `app` (tree)
- `app/build.gradle.kts` (blob)
- `app/src` (tree)
- `app/src/main` (tree)
- `app/src/main/AndroidManifest.xml` (blob)
- `app/src/main/assets` (tree)
- `app/src/main/assets/katalog` (tree)
- `app/src/main/assets/katalog/clubs.json` (blob)
- `app/src/main/assets/katalog/season-teams.json` (blob)
- `app/src/main/assets/katalog/tbf-catalog.json` (blob)
- `app/src/main/assets/katalog/venues.json` (blob)
- `app/src/main/kotlin` (tree)
- `app/src/main/kotlin/com` (tree)
- `app/src/main/kotlin/com/flugel` (tree)
- `app/src/main/kotlin/com/flugel/duduk` (tree)
- `app/src/main/kotlin/com/flugel/duduk/DudukApp.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/MainActivity.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/data` (tree)
- `app/src/main/kotlin/com/flugel/duduk/data/model` (tree)
- `app/src/main/kotlin/com/flugel/duduk/data/model/Ankarabasket.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/data/model/Arsiv.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/data/model/Assignr.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/data/model/EsnekSerilestiriciler.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/data/model/Tbf.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/data/net` (tree)
- `app/src/main/kotlin/com/flugel/duduk/data/net/Ayristiricilar.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/data/net/Http.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/data/net/Kaynaklar.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/data/repo` (tree)
- `app/src/main/kotlin/com/flugel/duduk/data/repo/DudukDeposu.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/data/repo/Eslestirme.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/data/repo/Normalizasyon.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/data/repo/SalonBulucu.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/data/store` (tree)
- `app/src/main/kotlin/com/flugel/duduk/data/store/ArsivDeposu.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/data/store/AyarlarDeposu.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/data/store/Birlestirici.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/domain` (tree)
- `app/src/main/kotlin/com/flugel/duduk/domain/IstatistikHesaplayici.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/domain/KazancHesaplayici.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/notify` (tree)
- `app/src/main/kotlin/com/flugel/duduk/notify/BildirimYoneticisi.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/notify/HatirlatmaHesaplayici.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/sync` (tree)
- `app/src/main/kotlin/com/flugel/duduk/sync/AcilisAlicisi.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/sync/SenkronIsi.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/ui` (tree)
- `app/src/main/kotlin/com/flugel/duduk/ui/DudukViewModel.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/ui/components` (tree)
- `app/src/main/kotlin/com/flugel/duduk/ui/components/CamBilesenleri.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/ui/nav` (tree)
- `app/src/main/kotlin/com/flugel/duduk/ui/nav/DudukNav.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/ui/screens` (tree)
- `app/src/main/kotlin/com/flugel/duduk/ui/screens/AyrintiVeAyarlarScreens.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/ui/screens/BenVeKazancScreens.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/ui/screens/HomeScreen.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/ui/screens/MaclarVeFiksturScreens.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/ui/screens/PuanVeHakemlerScreens.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/ui/theme` (tree)
- `app/src/main/kotlin/com/flugel/duduk/ui/theme/Color.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/ui/theme/Theme.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/ui/theme/Type.kt` (blob)
- `app/src/main/kotlin/com/flugel/duduk/widget` (tree)
- `app/src/main/kotlin/com/flugel/duduk/widget/SiradakiMacWidget.kt` (blob)
- `app/src/main/res` (tree)
- `app/src/main/res/drawable` (tree)
- `app/src/main/res/drawable/ic_launcher_background.xml` (blob)
- `app/src/main/res/drawable/ic_launcher_foreground.xml` (blob)
- `app/src/main/res/drawable/ic_launcher_monochrome.xml` (blob)
- `app/src/main/res/mipmap-anydpi-v26` (tree)
- `app/src/main/res/mipmap-anydpi-v26/ic_launcher.xml` (blob)
- `app/src/main/res/mipmap-anydpi-v26/ic_launcher_round.xml` (blob)
- `app/src/main/res/values-night` (tree)
- `app/src/main/res/values-night/colors.xml` (blob)
- `app/src/main/res/values-night/themes.xml` (blob)
- `app/src/main/res/values` (tree)
- `app/src/main/res/values/colors.xml` (blob)
- `app/src/main/res/values/strings.xml` (blob)
- `app/src/main/res/values/themes.xml` (blob)
- `app/src/main/res/xml` (tree)
- `app/src/main/res/xml/siradaki_mac_widget_info.xml` (blob)
- `app/src/test` (tree)
- `app/src/test/kotlin` (tree)
- `app/src/test/kotlin/com` (tree)
- `app/src/test/kotlin/com/flugel` (tree)
- `app/src/test/kotlin/com/flugel/duduk` (tree)
- `app/src/test/kotlin/com/flugel/duduk/Ornekler.kt` (blob)
- `app/src/test/kotlin/com/flugel/duduk/ToolchainSmokeTest.kt` (blob)
- `app/src/test/kotlin/com/flugel/duduk/data` (tree)
- `app/src/test/kotlin/com/flugel/duduk/data/net` (tree)
- `app/src/test/kotlin/com/flugel/duduk/data/net/AnkarabasketAyristiriciTest.kt` (blob)
- `app/src/test/kotlin/com/flugel/duduk/data/net/AssignrAyristiriciTest.kt` (blob)
- `app/src/test/kotlin/com/flugel/duduk/data/net/KatalogVeAgTest.kt` (blob)
- `app/src/test/kotlin/com/flugel/duduk/data/net/TbfAyristiriciTest.kt` (blob)
- `app/src/test/kotlin/com/flugel/duduk/data/repo` (tree)
- `app/src/test/kotlin/com/flugel/duduk/data/repo/TbfEslestirmeTest.kt` (blob)
- `app/src/test/kotlin/com/flugel/duduk/data/store` (tree)
- `app/src/test/kotlin/com/flugel/duduk/data/store/BirlestiriciVeArsivTest.kt` (blob)
- `app/src/test/kotlin/com/flugel/duduk/domain` (tree)
- `app/src/test/kotlin/com/flugel/duduk/domain/IstatistikVeKazancTest.kt` (blob)
- `app/src/test/kotlin/com/flugel/duduk/notify` (tree)
- `app/src/test/kotlin/com/flugel/duduk/notify/HatirlatmaTest.kt` (blob)
- `app/src/test/kotlin/com/flugel/duduk/widget` (tree)
- `app/src/test/kotlin/com/flugel/duduk/widget/SiradakiMacSeciciTest.kt` (blob)
- `build.gradle.kts` (blob)
- `docs` (tree)
- `docs/VERI-KAYNAKLARI.md` (blob)
- `docs/samples` (tree)
- `docs/samples/ankarabasket` (tree)
- `docs/samples/ankarabasket/anasayfa-days.json` (blob)
- `docs/samples/ankarabasket/anasayfa.html` (blob)
- `docs/samples/ankarabasket/flight_ayristir.py` (blob)
- `docs/samples/ankarabasket/kulup-ankara-dsi-sk.html` (blob)
- `docs/samples/ankarabasket/payload-access.json` (blob)
- `docs/samples/ankarabasket/payload-clubs.json` (blob)
- `docs/samples/ankarabasket/payload-documents.json` (blob)
- `docs/samples/ankarabasket/payload-fixture-bulletins.json` (blob)
- `docs/samples/ankarabasket/payload-officials.json` (blob)
- `docs/samples/ankarabasket/payload-season-teams.json` (blob)
- `docs/samples/ankarabasket/puan-durumlari-lig22328-sevB.html` (blob)
- `docs/samples/ankarabasket/puan-durumlari.headers.txt` (blob)
- `docs/samples/assignr` (tree)
- `docs/samples/assignr/recent-weeks-masa.json` (blob)
- `docs/samples/assignr/recent-weeks.headers.txt` (blob)
- `docs/samples/assignr/recent-weeks.json` (blob)
- `docs/samples/assignr/venues.json` (blob)
- `docs/samples/lig-eslesme.json` (blob)
- `docs/samples/mac-eslesme-testi.json` (blob)
- `docs/samples/mac-eslesme-testi.py` (blob)
- `docs/samples/tbf` (tree)
- `docs/samples/tbf/filters-results-ankara-2026-2027.json` (blob)
- `docs/samples/tbf/league-info-22328.json` (blob)
- `docs/samples/tbf/league-weeks-22328.json` (blob)
- `docs/samples/tbf/mac-header-350554.json` (blob)
- `docs/samples/tbf/mac-ozet-350554.json` (blob)
- `docs/samples/tbf/matches-22328-all.json` (blob)
- `docs/samples/tbf/matches-22328-week7.json` (blob)
- `docs/samples/tbf/matches-22332-all.json` (blob)
- `docs/samples/tbf/matches.headers.txt` (blob)
- `docs/samples/tbf/standings-22328.json` (blob)
- `docs/samples/tbf/standings-22332.json` (blob)
- `docs/samples/tbf/teams-22332.json` (blob)
- `docs/samples/ucret` (tree)
- `docs/samples/ucret/2026-2027-ozel-musabaka-gorevli-ucretleri.pdf` (blob)
- `docs/samples/ucret/2026-2027-ozel-musabaka-gorevli-ucretleri.txt` (blob)
- `docs/samples/ucret/hakemler-talimati-md29-s19-a.png` (blob)
- `docs/samples/ucret/hakemler-talimati-md29-s19-b.png` (blob)

## README İçeriği
(README dosyası bulunamadı.)


## İlgili Mimari Sayfaları
- [[github-repolar-katalogu]]
- [[sunucu-ve-github-commit-gecmisi]]
- [[pc-masaustu-hyprland-ve-gnome-araclari]]
- [[koharia-reader-ve-manga-ekosistemi]]
