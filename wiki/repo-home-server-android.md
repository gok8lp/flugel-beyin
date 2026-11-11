---
title: GitHub Depo Analizi — gok8lp/home-server-android
sources: raw/github/home-server-android.md, raw/github/00-github-envanteri.md, raw/github/01-tum-repolar-commit-gecmisi.md
updated: 2026-11-11
---

# GitHub Depo Analizi: `gok8lp/home-server-android`

Üst Katalog: [[github-repolar-katalogu]] · [[sunucu-ve-github-commit-gecmisi]] · [[duduk-genel-bakis]] · [[flugelserver-genel-mimari]]

> "GitHub Repo: gok8lp/home-server-android" - raw/github/home-server-android.md

> "gok8lp GitHub Depoları Tam Commit Geçmişi" - raw/github/01-tum-repolar-commit-gecmisi.md

## Son Commit Geçmişi (`gok8lp/home-server-android`)
- `3577d74` (2026-10-22): docs: clarify project purpose, setup and repository naming
- `abe6e13` (2026-10-17): Fix Android SDK setup in CI
- `c0d68ce` (2026-10-17): Document phone trial for prerelease APK
- `00c5ef7` (2026-10-17): Build verified Android test APK and harden release workflow
- `6e984b3` (2026-10-17): Align server API with live notifications and non-root desktop switch
- `e969dd5` (2026-10-17): Add FLUGEL server Android app and scoped local API

## Dosya Ağacı ve README Özeti
# GitHub Repo: gok8lp/home-server-android

- **URL:** https://github.com/gok8lp/home-server-android
- **Görünürlük:** Açık (Public)
- **Ana Dil:** Kotlin
- **Son Güncelleme:** 2026-10-22T22:53:32Z
- **Açıklama:** Docker ve sanal makine durumunu izlemek için Android istemcisi ve yerel Python API prototipi.

## Dosya Ağacı (File Tree)
- `.github` (tree)
- `.github/workflows` (tree)
- `.github/workflows/android.yml` (blob)
- `.gitignore` (blob)
- `README.md` (blob)
- `app` (tree)
- `app/build.gradle.kts` (blob)
- `app/src` (tree)
- `app/src/main` (tree)
- `app/src/main/AndroidManifest.xml` (blob)
- `app/src/main/java` (tree)
- `app/src/main/java/com` (tree)
- `app/src/main/java/com/flugel` (tree)
- `app/src/main/java/com/flugel/server` (tree)
- `app/src/main/java/com/flugel/server/ApiClient.kt` (blob)
- `app/src/main/java/com/flugel/server/MainActivity.kt` (blob)
- `app/src/main/java/com/flugel/server/SecureStore.kt` (blob)
- `app/src/main/res` (tree)
- `app/src/main/res/drawable` (tree)
- `app/src/main/res/drawable/ic_launcher.xml` (blob)
- `app/src/main/res/values-en` (tree)
- `app/src/main/res/values-en/strings.xml` (blob)
- `app/src/main/res/values` (tree)
- `app/src/main/res/values/strings.xml` (blob)
- `app/src/main/res/xml` (tree)
- `app/src/main/res/xml/backup_rules.xml` (blob)
- `app/src/main/res/xml/data_extraction_rules.xml` (blob)
- `build.gradle.kts` (blob)
- `gradle.properties` (blob)
- `server` (tree)
- `server/api.py` (blob)
- `server/config.example.json` (blob)
- `server/flugel-sunucu-app.service` (blob)
- `server/test_api.py` (blob)
- `settings.gradle.kts` (blob)

## README İçeriği
# Home Server Android

Kişisel ev sunucusu için Kotlin/Jetpack Compose Android istemcisi ve Python kontrol API'si prototipi.
Android dashboard and a local Python API for a personal home server.

## Ne var?

- Sunucu özeti, Docker konteynerleri, sanal makineler, masaüstleri, servis bağlantıları ve bildirim ekranları.
- HTTPS adresi ve erişim tokenı kullanıcı tarafından girilir; kimlik bilgileri kaynakta hazır değildir.
- Android Keystore ile yerel token saklama.
- Python standart kütüphanesiyle API ve izin listesine bağlı start/stop işlemleri.

Bu uygulama genel amaçlı SSH istemcisi değildir. API kurulmadan uygulama sunucu verisi göstermez.
Test APK'sinin bulunması fiziksel cihazda bütün işlevlerin doğrulandığı anlamına gelmez.

## Dizinler

| Dizin | İçerik |
| --- | --- |
| `app/` | Android ekranları, istemci ve yerel güvenli saklama |
| `server/api.py` | Yerel HTTP API |
| `server/config.example.json` | İzin verilen konteyner/VM listeleri için örnek |
| `server/test_api.py` | API testleri |
| `.github/workflows/android.yml` | Debug APK ve lint iş akışı |

## Android derlemesi

Projede Gradle Wrapper yoktur; sistemde uygun Gradle ve Android SDK kurulmalıdır.
CI yapılandırması Gradle 9.6.0, Android 37.0 platform/build tools ve Java kullanır;
kesin ayarlar build dosyalarında ve workflow içinde görülebilir.

```bash
gradle :app:assembleDebug :app:lintDebug
```

APK: `app/build/outputs/apk/debug/`. Hazır test paketleri varsa [Releases](https://github.com/gok8lp/home-server-android/releases) sayfasındadır.
Bu belgeler güncellendiğinde eski APK'lerin görünen adı otomatik değişmez.

## API'yi önce test et

```bash
python3 -m unittest discover -s server -v
```

Kurulumdan önce `server/config.example.json`, `server/api.py` ve systemd birimini incele.
API varsayılan `127.0.0.1:8818` üzerinde çalışır; Android erişimi için yetkilendirilmiş HTTPS katmanı gerekir.
Konteyner/VM izin listelerini kendi ortamına göre doldur; API'yi kimlik doğrulamasız internete açma.
Docker/libvirt yetkileri ve token dosyası izinleri kurulumun parçasıdır. Bu depo değişikliği sunucuda kurulum yapmaz.

## İlgili projeler ve eski teknik adlar

[home-server](https://github.com/gok8lp/home-server): altyapı örnekleri.
[desktop-server-toolkit](https://github.com/gok8lp/desktop-server-toolkit): masaüstü ve veri yardımcıları.
Android paket kimliği, servis dosyası ve yapılandırma yolları mevcut kurulumlarla uyumluluk için korunur.



## İlgili Mimari Sayfaları
- [[github-repolar-katalogu]]
- [[sunucu-ve-github-commit-gecmisi]]
- [[pc-masaustu-hyprland-ve-gnome-araclari]]
- [[koharia-reader-ve-manga-ekosistemi]]
