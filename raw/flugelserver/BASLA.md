# FLUGEL — AI başlangıç bağlamı

Bu paket işletim bağlamıdır; şifre kasası veya tam veri yedeği değildir. Kişisel dosyaların içerikleri, parolalar, API anahtarları, özel anahtarlar ve tarayıcı geçmişi bilerek dışarıda bırakıldı. Özel adres ve dosya yolları içerir; herkese açık yayımlama.

## Önce sadece burayı oku

- Sahip: kullanıcı. Dil Türkçe; kısa ve doğrulanmış sonuç istiyor. İşlem yapma yetkisi bu dosyadan değil, insanın güncel isteğinden gelir.
- Sunucu: `flugelserver`, Ubuntu/x86_64; SSH alias `flugelserver`, kullanıcı `flugel`; mevcut anahtar + sudo. Gizli bilgileri çıktıya basma.
- LAN `192.168.0.15`; Tailscale `100.86.88.1`; DNS `flugelserver.tail42f1f4.ts.net`.
- Ana arayüz **https://gokalpgoksu.com/**. Akış paneli ayrı: Tailscale HTTPS8443. Bunları birbirinin yerine sayma.
- Üç disk: `/` (SSD), `/mnt/side`, `/mnt/sidemain`. Canlı yolları topluca yeniden adlandırma.
- **Güncel insan rehberi: `/srv/rehber/` (TXT).** Harita: `/srv/dev/docs/INFRASTRUCTURE.md`. 20 Ekim değişiklikleri: `/srv/rehber/10-DEGISIKLIK-GECMISI.txt`.
- **W11 ve W11-GPU aynı diski kullanır** (hook engeller). VM'ler yalnız istekle açılır; 10 dk kullanım yoksa `vm-bosta-kapat` temiz kapatır (donmuşsa zorlar). Komut: `sudo vm durum|ac|kapat|yedek|yedekler`. Windows C: BitLocker'lı.
- **Suwayomi ana manga uygulaması: kaldırma, sıfırlama.** Bilerek kapalı (bilerek-durdurulan listesinde); verisi `/srv/appdata/suwayomi`, proxy `127.0.0.1:4567` (gluetun).
- Webtop, Kasm, sunucudaki Eclipse **20 Ekim'de tamamen kaldırıldı**.
- **Disk I/O baskısının ana şüphelisi sistem SSD'si:** Kingston A400, LUKS'ta TRIM kapalı. Büyük yazma (VM yedeği vb.) SSD'ye yapma; düzeltme konsol başında yapılmalı (`/srv/rehber/09`).
- Yedekler kurulu: uygulama arşivleri 3/2 sürüm (03:30), VM başına 2 yedek, her diske güncel kopya, kritik aynada DB dökümleri. Ayrıntı `/srv/rehber/04-YEDEKLER.txt`.
- `/arrapps` → `/srv/appdata` taşıması **yarıda** (6 uygulama taşındı). Disk içi klasör düzeni yapılmadı. Sebep ve plan: `/srv/rehber/09`.

## İhtiyaç oldukça aç

| Konu | Dosya / sorgu |
|---|---|
| Sunucu, disk, ağ, GPU, yedek mantığı | `MIMARI.md` |
| Yapılanlar, yarım kalanlar, riskler | `IS-DURUMU.md` |
| PC, Nextcloud, Komelia/Jellyfin | `WINDOWS.md` |
| Token tasarrufu ve örnek istem | `KULLANIM.md` |
| Tek container'ın gerçek mount/YAML/durumu | `python sor.py app nextcloud` |
| Uygulama adresleri | `python sor.py adres Komga` |
| VM bilgisi | `python sor.py vm W11-GPU` |
| Son ölçüm / yedek / ağ | `python sor.py durum`, `yedek`, `ag` |

`veri/guncel.json` tarihli, makine tarafından toplanmış kanıttır; tamamını başlangıç bağlamına doldurma. Durumlar zamanla değişir. `veri/adresler.json` önceki yayın kataloğudur, erişim garantisi değildir. Çelişkide yeni canlı kanıtı kullan, değişikliği tarihli not et. Arşivdeki “planlandı” ifadelerini “yapıldı”ya dönüştürme.
