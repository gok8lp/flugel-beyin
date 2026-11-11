# Düdük — derleme

## Ortam

Kabuk yapılandırmasına bir şey eklenmedi; değişkenleri komut satırında ver:

| Değişken | Değer | Not |
|---|---|---|
| `JAVA_HOME` | `/usr/lib/jvm/java-17-openjdk` | Sistem varsayılanı JDK 27; derleme 17 ile yapılır |
| `ANDROID_HOME` | `/home/flugel/android-sdk/sdk` | İsteğe bağlı; Gradle yolu `local.properties` içindeki `sdk.dir`'den alır (bu dosya git'e girmez) |

Kurulu SDK paketleri: `cmdline-tools;latest`, `platform-tools`, `platforms;android-37.0`, `build-tools;37.0.0`.
Emülatör / sistem imajı yok. `adb`: `$ANDROID_HOME/platform-tools/adb`.

## Derleme ve test (tek satır)

```sh
JAVA_HOME=/usr/lib/jvm/java-17-openjdk ./gradlew :app:assembleDebug :app:testDebugUnitTest
```

- APK: `app/build/outputs/apk/debug/app-debug.apk` (`~/.android/debug.keystore` ile imzalı, minify kapalı)
- Test raporu: `app/build/reports/tests/testDebugUnitTest/index.html`
- İş bitince daemon'ı kapat: `./gradlew --stop`

APK doğrulama:

```sh
/home/flugel/android-sdk/sdk/build-tools/37.0.0/aapt2 dump badging app/build/outputs/apk/debug/app-debug.apk | head -5
```

## Sürümler

Tek kaynak: `gradle/libs.versions.toml`.

| Bileşen | Sürüm |
|---|---|
| Gradle (wrapper) | 9.8.0 |
| Android Gradle Plugin | 9.4.1 (yerleşik Kotlin; `kotlin-android` eklentisi yok) |
| Kotlin (compose + serialization eklentileri) | 2.3.21 |
| Compose BOM | 2026.09.00 |
| compileSdk / targetSdk / minSdk | 37 / 37 / 26 |
| Build-Tools | 37.0.0 |
| JDK | 17 |

## Bilinçli kararlar

- Room / KSP / Hilt yok: kalıcılık JSON dosyası + DataStore Preferences ile yapılacak.
- WorkManager 2.10.5'te tutuldu (2.11+ bazı üretici API 34 cihazlarında açılışta çöküyor).
- Release imzası kurulmadı.
