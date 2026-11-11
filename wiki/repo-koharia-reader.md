---
title: GitHub Depo Analizi — gok8lp/koharia-reader
sources: raw/github/koharia-reader.md, raw/github/00-github-envanteri.md, raw/github/01-tum-repolar-commit-gecmisi.md
updated: 2026-11-11
---

# GitHub Depo Analizi: `gok8lp/koharia-reader`

Üst Katalog: [[github-repolar-katalogu]] · [[sunucu-ve-github-commit-gecmisi]] · [[duduk-genel-bakis]] · [[flugelserver-genel-mimari]]

> "GitHub Repo: gok8lp/koharia-reader" - raw/github/koharia-reader.md

> "gok8lp GitHub Depoları Tam Commit Geçmişi" - raw/github/01-tum-repolar-commit-gecmisi.md

## Son Commit Geçmişi (`gok8lp/koharia-reader`)
- `75f70ad` (2026-10-31): fix(flugel): use Tailscale addresses and drop embedded server API keys
- `58c9741` (2026-10-31): fix(reader,flugel): fix LAN EPUB/PDF novel loading and make Flugel setup plug-and-play
- `715564b` (2026-10-29): Flugel: secure personal build, reconnects and signed updates
- `2ed40ac` (2026-10-28): style: apply spotless formatting to LibraryConnectionProfilesScreen (#1)
- `df5d324` (2026-10-22): docs: clarify project purpose, setup and repository naming
- `04d8e34` (2026-10-18): Daha Fazla menusune Manga indir (Tranga) ve Kutuphaneye ekle (yukleme) kisayollari
- `37eb2d4` (2026-10-18): Kitaplar sekmesi icin ayri baglanti: Komga ve Kavita ayni anda (Cizgi roman / Kitaplar sekmeleri)
- `5936816` (2026-10-18): Komga SSE yolunu duzelt (/sse/v1/events) ve test APK surum etiketini parametre yap
- `761c2fa` (2026-10-17): Prepare Flugel Manga test APK and server setup
- `a95a23b` (2026-10-06): fix: 修复升级时重复建表导致的启动崩溃 / Fix upgrade startup migration crash
- `0f287cd` (2026-10-06): release: 准备 0.7.0，完善文档与墨水屏适配 / Prepare 0.7.0 with docs and E-Ink fixes
- `c28ad51` (2026-10-06): feat: 接入 Suwayomi 与网络存储并完善共享阅读功能 / Add Suwayomi and network storage integration
- `6c45605` (2026-10-03): docs: enforce shared provider contracts / 规范跨库通用能力与验证
- `5a4c45a` (2026-10-03): fix: 修复书籍下载并完善 Kavita 书架状态 / Fix book downloads and Kavita shelf status
- `1232f7c` (2026-10-03): fix: 修复本地系列与 EPUB 阅读进度 / Fix local series and EPUB reading progress
- `a492b99` (2026-10-03): feat: 完善阅读器设置与翻页体验 / Improve reader settings and page-turn behavior
- `c7dfde6` (2026-10-02): feat: 统一本地系列元数据编辑并修复阅读流程 / Unify local series metadata editing and stabilize reader flows
- `99bddf1` (2026-09-27): fix(local): improve archive loading and restore entry opening settings
- `17fe060` (2026-09-27): docs: document Kavita support in Chinese and English READMEs
- `e62b167` (2026-09-27): fix(ui): use E-Ink aware loading indicators
- `fdffa45` (2026-09-27): feat(kavita): add native integration and reliable reading sync
- `c59e86a` (2026-09-26): feat: unify library search and improve reader image handling
- `e9fe432` (2026-09-24): feat: prepare 0.6.0 with local library UI and support updates
- `18a787b` (2026-09-24): fix: optimize local library scanning and share chapter display mode
- `adb9ea0` (2026-09-24): feat(settings): improve shelf and chapter display controls
- `14a33ed` (2026-09-24): fix(download): improve large-file transfers and retry recovery
- `2f8d90c` (2026-09-23): fix(reader): preserve Markdown code formatting and heading positions
- `73a0d2d` (2026-09-23): Feat/markdown: 支持本地 Markdown 文件阅读 + Markdown 文档大纲导航 (#95)
- `f88c759` (2026-09-23): chore(codex): remove project subagent configuration
- `c9a04f1` (2026-09-23): feat(backup): preserve user data across backup and restore

## Dosya Ağacı ve README Özeti
# GitHub Repo: gok8lp/koharia-reader

- **URL:** https://github.com/gok8lp/koharia-reader
- **Görünürlük:** Özel (Private)
- **Ana Dil:** Kotlin
- **Son Güncelleme:** 2026-11-04T19:46:59Z
- **Açıklama:** Koharia/Mihon tabanlı kişisel Android okuyucu; Komga, Kavita ve yerel kitaplık bağlantıları.

## Dosya Ağacı (File Tree)
- `.editorconfig` (blob)
- `.gitattributes` (blob)
- `.github` (tree)
- `.github/.java-version` (blob)
- `.github/FUNDING.yml` (blob)
- `.github/ISSUE_TEMPLATE` (tree)
- `.github/ISSUE_TEMPLATE/1_request_feature.yml` (blob)
- `.github/ISSUE_TEMPLATE/2_report_issue.yml` (blob)
- `.github/ISSUE_TEMPLATE/config.yml` (blob)
- `.github/assets` (tree)
- `.github/assets/contributors` (tree)
- `.github/assets/contributors/CurrenWong.svg` (blob)
- `.github/assets/contributors/Mister-album.svg` (blob)
- `.github/assets/logo.png` (blob)
- `.github/assets/screenshots` (tree)
- `.github/assets/screenshots/comic-reader-zh-cn.png` (blob)
- `.github/assets/screenshots/comic-reader.png` (blob)
- `.github/assets/screenshots/epub-reader-zh-cn.png` (blob)
- `.github/assets/screenshots/epub-reader.png` (blob)
- `.github/assets/screenshots/library-zh-cn.png` (blob)
- `.github/assets/screenshots/library.png` (blob)
- `.github/assets/screenshots/series-details-zh-cn.png` (blob)
- `.github/assets/screenshots/series-details.png` (blob)
- `.github/pull_request_template.md` (blob)
- `.github/renovate.json5` (blob)
- `.github/workflows` (tree)
- `.github/workflows/build.yml` (blob)
- `.github/workflows/contributors.yml` (blob)
- `.github/workflows/flugel-test-apk.yml` (blob)
- `.github/workflows/pr_agent.yml` (blob)
- `.github/workflows/rebuild-website.yml` (blob)
- `.github/workflows/release.yml` (blob)
- `.gitignore` (blob)
- `.idea` (tree)
- `.idea/icon.svg` (blob)
- `.pr_agent.toml` (blob)
- `AGENTS.md` (blob)
- `ANDROID_SETUP.md` (blob)
- `CHANGELOG.md` (blob)
- `CODE_OF_CONDUCT.md` (blob)
- `CONTRIBUTING.md` (blob)
- `LICENSE` (blob)
- `NOTICE` (blob)
- `README.md` (blob)
- `README_EN.md` (blob)
- `README_UPSTREAM.zh-CN.md` (blob)
- `app` (tree)
- `app/build.gradle.kts` (blob)
- `app/google-services.json` (blob)
- `app/proguard-android-optimize.txt` (blob)
- `app/proguard-rules.pro` (blob)
- `app/src` (tree)
- `app/src/androidTest` (tree)
- `app/src/androidTest/AndroidManifest.xml` (blob)
- `app/src/androidTest/assets` (tree)
- `app/src/androidTest/assets/reader-animated.gif` (blob)
- `app/src/androidTest/java` (tree)
- `app/src/androidTest/java/eu` (tree)
- `app/src/androidTest/java/eu/kanade` (tree)
- `app/src/androidTest/java/eu/kanade/tachiyomi` (tree)
- `app/src/androidTest/java/eu/kanade/tachiyomi/ui` (tree)
- `app/src/androidTest/java/eu/kanade/tachiyomi/ui/eink` (tree)
- `app/src/androidTest/java/eu/kanade/tachiyomi/ui/eink/EInkMotionDeviceTest.kt` (blob)
- `app/src/androidTest/java/eu/kanade/tachiyomi/ui/reader` (tree)
- `app/src/androidTest/java/eu/kanade/tachiyomi/ui/reader/viewer` (tree)
- `app/src/androidTest/java/eu/kanade/tachiyomi/ui/reader/viewer/ComicResamplingEvidenceDeviceTest.kt` (blob)
- `app/src/androidTest/java/eu/kanade/tachiyomi/ui/reader/viewer/DoubleTapZoomDeviceTest.kt` (blob)
- `app/src/androidTest/java/eu/kanade/tachiyomi/ui/reader/viewer/ReaderPageImageDeviceTest.kt` (blob)
- `app/src/androidTest/java/eu/kanade/tachiyomi/ui/reader/viewer/pager` (tree)
- `app/src/androidTest/java/eu/kanade/tachiyomi/ui/reader/viewer/pager/ComicPageFlipGeometryDeviceTest.kt` (blob)
- `app/src/androidTest/java/eu/kanade/tachiyomi/ui/reader/viewer/pager/DoublePageActionsDeviceTest.kt` (blob)
- `app/src/androidTest/java/eu/kanade/tachiyomi/ui/reader/viewer/pager/MergedPageExportDeviceTest.kt` (blob)
- `app/src/androidTest/java/eu/kanade/tachiyomi/ui/reader/viewer/pager/PagerAccessibilityDeviceTest.kt` (blob)
- `app/src/androidTest/java/eu/kanade/tachiyomi/ui/reader/viewer/pager/PagerSplitDeviceTest.kt` (blob)
- `app/src/androidTest/java/eu/kanade/tachiyomi/ui/reader/viewer/pager/PagerVolumeKeyReadyDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia` (tree)
- `app/src/androidTest/java/koharia/connection` (tree)
- `app/src/androidTest/java/koharia/connection/ConnectionProviderContractTest.kt` (blob)
- `app/src/androidTest/java/koharia/connection/ui` (tree)
- `app/src/androidTest/java/koharia/connection/ui/ConnectionSearchControlsDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/crash` (tree)
- `app/src/androidTest/java/koharia/crash/ReaderCrashRegressionTest.kt` (blob)
- `app/src/androidTest/java/koharia/diagnostics` (tree)
- `app/src/androidTest/java/koharia/diagnostics/ContinuousSwipeReproTest.kt` (blob)
- `app/src/androidTest/java/koharia/diagnostics/KomgaRetryQueueDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/diagnostics/ReaderSettingsOrganizationDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/diagnostics/ReaderStatusStyleDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/diagnostics/SharedConfigMigrationDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/diagnostics/ShelfCacheDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/document` (tree)
- `app/src/androidTest/java/koharia/document/DocumentFontSizeDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/document/MarkdownDocumentRenderingTest.kt` (blob)
- `app/src/androidTest/java/koharia/epub` (tree)
- `app/src/androidTest/java/koharia/epub/EpubContinuousReadingDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/epub/EpubContinuousScrollProgressDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/epub/EpubNotePrepaintDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/epub/EpubPageTransitionDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/epub/EpubTocNavigationDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/importing` (tree)
- `app/src/androidTest/java/koharia/importing/ImageComicImportDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/kavita` (tree)
- `app/src/androidTest/java/koharia/kavita/KavitaLivePublicationDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/lanraragi` (tree)
- `app/src/androidTest/java/koharia/lanraragi/ArchiveReaderDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/lanraragi/ArchiveStreamDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/lanraragi/LanraragiArchiveOpeningDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/lanraragi/LanraragiBrowseDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/lanraragi/LanraragiCategoryTabsDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/lanraragi/LanraragiConnectionDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/lanraragi/LanraragiDraftConnectionDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/lanraragi/LanraragiOfficialDemoTest.kt` (blob)
- `app/src/androidTest/java/koharia/lanraragi/LanraragiPreviewToolbarDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/lanraragi/LanraragiReviewRegressionDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/lanraragi/LanraragiSettingsDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/lanraragi/LanraragiStartupRefreshDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/lanraragi/LanraragiStartupTimingDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/lanraragi/LanraragiTemporarySourceDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/lanraragi/ui` (tree)
- `app/src/androidTest/java/koharia/lanraragi/ui/LocalPreviewRegressionDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/pdf` (tree)
- `app/src/androidTest/java/koharia/pdf/PdfReflowDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/reader` (tree)
- `app/src/androidTest/java/koharia/reader/resampling` (tree)
- `app/src/androidTest/java/koharia/reader/resampling/LongImageTileGridDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/reader/resampling/MitchellReaderDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/reader/resampling/MitchellRegionDecoderDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/reader/resampling/MoireSettingsDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/reader/resampling/MoireThresholdDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/smanga` (tree)
- `app/src/androidTest/java/koharia/smanga/SmangaConnectionSettingsTest.kt` (blob)
- `app/src/androidTest/java/koharia/smanga/SmangaLiveFixture.kt` (blob)
- `app/src/androidTest/java/koharia/smanga/SmangaLiveProtocolTest.kt` (blob)
- `app/src/androidTest/java/koharia/smanga/SmangaLiveReaderTest.kt` (blob)
- `app/src/androidTest/java/koharia/smanga/SmangaPdfCacheTest.kt` (blob)
- `app/src/androidTest/java/koharia/smanga/SmangaPdfTransitionTest.kt` (blob)
- `app/src/androidTest/java/koharia/smanga/SmangaShelfColdStartTest.kt` (blob)
- `app/src/androidTest/java/koharia/smanga/SmangaShelfErrorTest.kt` (blob)
- `app/src/androidTest/java/koharia/source` (tree)
- `app/src/androidTest/java/koharia/source/local` (tree)
- `app/src/androidTest/java/koharia/source/local/LargeLocalArchiveDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/source/local/LocalBookshelfConfigurationDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/source/local/LocalCustomCoverMaintenanceDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/source/local/LocalFileDeletionDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/source/local/LocalFolderDetailUiDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/source/local/LocalFolderLibraryDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/source/local/LocalImportDestinationDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/source/local/LocalLibraryEmulatorScenarioTest.kt` (blob)
- `app/src/androidTest/java/koharia/source/local/LocalLibraryInitialSetupDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/source/local/LocalLibraryItemActionsDeviceTest.kt` (blob)
- `app/src/androidTest/java/koharia/source/local/LocalLibraryRegressionDeviceTest.kt` (blob)

## README İçeriği
# Koharia Reader

Koharia/Mihon tabanlı kişisel Android manga ve kitap okuyucu uyarlaması.
Personal Android reader fork based on [Koharia](https://github.com/Mister-album/Koharia), built on [Mihon](https://github.com/mihonapp/mihon).
Bu depo bu projelerin resmî sürümü değildir; özgün yazarların çalışmaları ve lisansları korunur.

## Ne yapar?

Komga, Kavita ve yerel kitaplık bağlantılarını kullanarak manga ve kitap okuma akışını kişisel sunucu düzenine uyarlar.
Depoda başka sağlayıcılara ait upstream modüller de vardır; modülün bulunması bu uyarlamada uçtan uca doğrulandığı anlamına gelmez.
Kitap, hesap bilgisi veya hazır sunucu erişimi sağlamaz.

## Kullanıcı olarak başlamak

1. Bu deponun [Releases](https://github.com/gok8lp/koharia-reader/releases) bölümünde yayımlanmış bir test APK'si varsa sürüm notlarını oku.
2. Uygulamada kendi Komga/Kavita sunucunu ve hesabını yapılandır.
3. Bağlantı, kitaplık görünümü ve okuma akışını kendi cihazında dene.

Ayrıntılı adımlar: [Android kurulum notları](ANDROID_SETUP.md).
Önceki test APK'leri eski uygulama adını taşıyabilir; kaynak değişikliği mevcut APK'yi yeniden derlemez.

## Kaynaktan derleme

Android Studio, projenin Android SDK/NDK bileşenleri ve Gradle için Java 17 gerekir.
Kesin sürümler `gradle/koharia.versions.toml`, `.github/.java-version` ve build dosyalarında tanımlıdır.

```bash
./gradlew spotlessCheck
./gradlew :app:compileDebugKotlin
./gradlew :app:assembleDebug
```

Windows'ta aynı görevler `gradlew.bat` ile çalıştırılır. APK'ler `app/build/outputs/apk/` altında oluşur.
Yayın imzalama anahtarları depoya eklenmez; debug APK geliştirme içindir.

## Proje haritası

| Dizin | İçerik |
| --- | --- |
| `app/` | Android uygulaması, ekranlar ve bağlantı yönetimi |
| `i18n/` | Ortak ve Türkçe metin kaynakları |
| `data/`, `domain/` | Veri ve iş kuralları |
| `core/`, `presentation-*` | Ortak altyapı ve arayüz bileşenleri |
| `.github/workflows/` | Derleme ve doğrulama iş akışları |

## Kaynak ve lisans

Upstream açıklamalar: [English](README_EN.md) · [简体中文](README_UPSTREAM.zh-CN.md).
Bu belgelerdeki upstream indirme ve destek bağlantıları özgün projeye aittir.
[LICENSE](LICENSE), [NOTICE](NOTICE), [CONTRIBUTING.md](CONTRIBUTING.md) ve üçüncü taraf atıfları korunmuştur.
Koharia, Mihon, Komga veya Kavita'nın resmî ürünü olduğu iddia edilmez.



## İlgili Mimari Sayfaları
- [[github-repolar-katalogu]]
- [[sunucu-ve-github-commit-gecmisi]]
- [[pc-masaustu-hyprland-ve-gnome-araclari]]
- [[koharia-reader-ve-manga-ekosistemi]]
