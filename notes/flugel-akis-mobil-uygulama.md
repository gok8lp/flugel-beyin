---
tur: not
etiketler:
  - flugel-akis
  - android
  - cloudflare
  - flugelserver
olusturma: 2026-11-11
guncelleme: 2026-11-11
---

# FLUGEL Akış: Herkese Açık Adres ve Mobil Uygulama (FLUGEL-Akis.apk 2.0)

Bağlantılar: [[HARITA]] · [[projeler/flugel-sunucu-ve-akis]] · [[flugel-akis-ve-botlar]] · [[notes/cloudflare-ve-tailscale-baglanti-zinciri]] · [[kararlar]] · [[dersler]]

> Kaynak: sen, sohbette, 2026-11-05 ("sunucuda flugel akışı açıp bana mobil appini yapar mısın"). Durum 2026-11-11 15:02 UTC'de sunucuda yeniden doğrulandı.

## Özet
- **Adres:** https://akis.gokalpgoksu.com — **şifresiz, herkese açık** (kullanıcı kararı: "şifre olsa ne yarar zaten aç hemen", 2026-11-05).
- **Mobil uygulama:** `FLUGEL-Akis.apk` 2.0. Tailscale **gerekmez**, okulda ve evde aynı adrese bağlanır.
- **Neden yeniden yapıldı:** Eski `FLUGEL.apk` (1.0) yalnız `https://flugelserver.tail42f1f4.ts.net:8443` (Tailscale serve/funnel) adresini açıyordu. O yol artık çalışmıyor.

## 1. Sunucu Tarafı (flugelserver, 192.168.0.15)

| Parça | Değer |
|---|---|
| Konteyner | `flugel-akis` (`python:3.13-alpine`, `network_mode: host`, port `3012`) |
| Compose | `/opt/stacks/panel/compose.yaml` → servis `flugel-akis` |
| Kod | `/opt/stacks/panel/akis/akis.py` + `web/` (index.html, app.js, app.css, sw.js, manifest) |
| Veri | `/opt/stacks/panel/akis/veri/akis.db` (SQLite, ~130 MB) |
| Yeniden başlatma | `restart: unless-stopped` → sunucu açılınca kendiliğinden kalkar |
| Uygulama katmanı | `/etc/sistem-bakim/uygulama-katmanlari.conf` içinde **yok** → "hep açık" sayılır, boşta kapatılmaz |
| Sağlık testi | `wget http://127.0.0.1:3012/api/istatistik` (60 sn) |

### Ne oldu (zaman sırası)
1. **2026-11-04:** Sunucu yalnız izleme/depolama için sadeleştirilirken `flugel-akis` konteyneri `docker rm` ile kaldırıldı (veri ve compose kaldı). Liste: `/etc/sistem-bakim/ara-20261104/kaldirilan-konteynerler.txt`. Aynı gün `akis.gokalpgoksu.com` satırı tünel ayarından çıkarıldı.
2. **2026-11-05:** `cd /opt/stacks/panel && docker compose up -d flugel-akis` ile yeniden açıldı. Yerel test `127.0.0.1:3012/api/istatistik` → 200.
3. **2026-11-05:** Tünel satırı geri eklendi (aşağıda).

### Cloudflare yolu
- Tünel: `cloudflared-akis.service`, ayar dosyası `/etc/cloudflared/akis.yml` (yerel yönetilen tünel; ana "homeserver" tüneli panelden yönetilir, ona dokunulmadı).
- Eklenen satır (ingress listesinin başına):
  ```yaml
  - hostname: akis.gokalpgoksu.com
    service: http://localhost:3012
  ```
- Doğrudan `localhost:3012`'ye gider; **giris nginx'ten (basic auth) geçmez**. Diğer alt alanlar (plex, suwayomi, *arr, torrent) `localhost:8098` → giris → şifreli.
- Yedekler: `akis.yml.onceki-20261105-175806` (bu değişiklikten önceki hâl), `akis.yml.yedek-20261104-ajan` (sadeleştirmeden önceki hâl). Sonradan başka bir oturum `duduk.gokalpgoksu.com` ekledi (`akis.yml.yedek-20261111-1728`); akış satırı hâlâ yerinde.
- Doğrulama: `cloudflared tunnel --config /etc/cloudflared/akis.yml ingress validate` → OK.

### Doğrulama (2026-11-11)
| Adres | Sonuç |
|---|---|
| `https://akis.gokalpgoksu.com/` | 200 |
| `https://akis.gokalpgoksu.com/api/istatistik` | 200 |
| `https://akis.gokalpgoksu.com/indir/FLUGEL.apk` | 200, 41 736 bayt |
| `flugel-akis` konteyneri | Up 5 days (healthy) |
| `https://plex.gokalpgoksu.com/` (karşılaştırma) | 401 (şifre istiyor, beklenen) |

İstatistik anlık görüntüsü: 221 632 gönderi, 1000 kaynak, 6 sorunlu / 4 ölü kaynak, 711 çeviri bekliyor.

## 2. Mobil Uygulama

| Alan | Değer |
|---|---|
| Ad | FLUGEL |
| Paket | `com.flugel.akis.app` (eskisi `com.flugel.akis`; **farklı paket**, yan yana kurulabilir) |
| Sürüm | versionCode 2 / versionName 2.0 |
| SDK | minSdk 23, targetSdk 34, derleme platformu android-37.0 |
| İzin | Yalnız `INTERNET`; servis, alıcı, takip yok |
| Boyut | 41 736 bayt |
| SHA-256 (dosya) | `611bca0c8bb0527832cca5786f0be70c661cf8233628aa09ea49d75d99baad16` |
| İmza sertifikası SHA-256 | `e7c904d57380105e25d6f1e2ed1696f13191c9ec13eab84ec2556086b0abc0eb` |

### Nasıl çalışır
- Tek `Activity` (`com.flugel.akis.Ana`) içinde tam ekran siyah **WebView**; açılışta `https://akis.gokalpgoksu.com/#/ana` yüklenir.
- `akis.gokalpgoksu.com` dışındaki linkler (haber siteleri, YouTube vb.) telefonun tarayıcısında açılır.
- YouTube tam ekran desteği (`onShowCustomView`), geri tuşu sayfa geçmişinde geri gider.
- Bağlantı yoksa siyah "FLUGEL — Sunucuya ulaşılamadı. İnternet bağlantını kontrol et." sayfası ve **Tekrar dene** düğmesi.
- Güvenlik: dosya/içerik erişimi kapalı, karışık içerik (HTTP) yasak, `usesCleartextTraffic=false`, `allowBackup=false`.

### Kaynak ve derleme
- Asıl kaynak: `~/Projects/desktop-server-toolkit/android/` (eski, Tailscale adresli 1.0 sürümü; **bu repoda değiştirilmedi**).
- 2.0 kopyası: sunucuda `~/work/akis-app/` (laptopta geçici kopya scratchpad'deydi). Değişenler:
  - `Ana.java`: `EV = "akis.gokalpgoksu.com"`, `ADRES = "https://" + EV + "/#/ana"`, hata metnindeki "Tailscale açık mı?" → "İnternet bağlantını kontrol et."
  - `AndroidManifest.xml`: paket `com.flugel.akis.app`, sürüm 2 / 2.0, activity tam adla `com.flugel.akis.Ana`.
  - Yeni derleme betiği `derle-docker.sh` (Gradle'sız): `aapt2 compile/link` → `javac -source 8` → `d8` → `jar uf0M` ile `classes.dex` ekleme → `zipalign` → `apksigner`.
- Derleme komutu (sunucuda):
  ```bash
  docker run --rm -u 1000:1000 -v ~/work/akis-app:/src -v ~/work/android-sdk:/sdk:ro -v ~/work/keys:/anahtar koharia-build bash /src/derle-docker.sh
  ```
  Çıktı: `~/work/akis-app/bin/FLUGEL-Akis.apk`. İmaj `koharia-build` (eclipse-temurin:21, Flugel Manga ile ortak), SDK `~/work/android-sdk` (build-tools 36.0.0).
- **İmza anahtarı:** sunucuda `~/work/keys/flugel-akis.jks`; parolası aynı klasörde 600 izinli ayrı dosyada (değeri buraya yazılmaz). **Silinmemeli**: sonraki sürümler ancak bu anahtarla imzalanırsa üstüne kurulur.

### Test
- Sunucudaki emülatörde (`flugel-test` AVD, `adb -s emulator-5554`) kuruldu ve açıldı. "Sana özel" akışı resimli kartlarla yüklendi; alt menü, sekmeler ve AI düğmesi göründü. Ardından emülatör kapatıldı.
- **Gerçek telefonda kullanıcı tarafından denenmedi** (bu not yazıldığında kayıtlı değil).

### Dağıtım yerleri (hepsi aynı SHA-256)
- Sunucu indirme: `https://akis.gokalpgoksu.com/indir/FLUGEL.apk` (dosya `/opt/stacks/panel/akis/web/indir/FLUGEL.apk`; eski 1.0 yanında `FLUGEL.apk.eski-tailscale-20261105` olarak duruyor). Uygulama içinde **Takip & ayarlar → indir** bağlantısı da buraya gider.
- Nextcloud: `flugel` kullanıcısının ana klasöründe `FLUGEL-Akis.apk` (`occ files:scan` ile tarandı).
- Laptop: `~/Documents/FLUGEL-sunucu/FLUGEL-Akis.apk`.
- Sohbette dosya olarak da gönderildi.

### Kurulum
1. APK'yı telefonda aç, "bilinmeyen kaynaklardan yükleme" iznini ver.
2. Eski FLUGEL (1.0, `com.flugel.akis`) çakışmaz; istersen sonra kaldır.

## 3. Bilinen Sınırlar
- **AI özellikleri çalışmaz:** "Özetle", ✦ FLUGEL AI sohbeti, Japonca → Türkçe çeviri ve önem puanlama Ollama'ya bağlı. Ollama 2026-11-04'te kaldırıldı (sunucu yalnız izleme/depolama modunda). `/api/istatistik` → `"son": "Ollama'ya ulaşılamadı"`. Akışın kendisi, kaynak toplama, resimler, anime/oyun/dizi/maç sayfaları normal.
- **Şifresiz açık:** Adresi bilen herkes akışı görebilir, kaydet/takip gibi POST uçlarını kullanabilir. Bilerek seçildi (bkz. [[kararlar]]).
- Uygulama yalnız bir kabuktur; içerik ve arayüz güncellemeleri sunucudaki `web/` dosyalarından gelir, APK yeniden kurmak gerekmez. Yalnız adres veya kabuk davranışı değişirse yeni APK gerekir.

## 4. Geri Alma
- Herkese açık erişimi kapatmak: `/etc/cloudflared/akis.yml` içinden `akis.gokalpgoksu.com` iki satırını sil → `sudo systemctl restart cloudflared-akis`.
- Akışı durdurmak: `cd /opt/stacks/panel && docker compose stop flugel-akis`.
- Eski APK'ya dönmek: `FLUGEL.apk.eski-tailscale-20261105` dosyasını `FLUGEL.apk` adıyla geri koy (Tailscale yolu çalışmadığı için anlamsız).
