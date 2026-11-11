# İş durumu — 20 Ekim 2026 (Claude gecesi sonrası)

Ayrıntılı ve güncel kayıt sunucuda: `/srv/rehber/10-DEGISIKLIK-GECMISI.txt` ve `/srv/rehber/09-BILINEN-SORUNLAR.txt`. Aşağıdakiler devir bilgisi, yeni işlem emri değil.

## Yapıldığı doğrulananlar (20 Ekim)

- Webtop, Kasm, sunucudaki Eclipse tamamen kaldırıldı (container, imaj, veri, servis, rota, bot komutu, yedek kopyaları).
- VM yönetimi: autostart kapalı; `vm-bosta-kapat.timer` 10 dk kuralı canlı test edildi (donmuş W11-GPU zorla kapatıldı, GPU döndü); VM başına 2 yedek (`/mnt/side/yedek/vm`), ilk W11 yedeği 50 GB.
- Uygulama yedek sistemi `uygulama-yedek.py` (34 uygulama, 1,94 GiB/çalışma, 3 sürüm, 3 diske güncel kopya, pg_dumpall + SQLite .backup). `kritik-yedek.sh` önce DB dökümü alır.
- Güvenlik: File Browser (flugel, kapsam daraltıldı, yalnız localhost/Tailscale), Samba (misafir kapalı, yalnız flugel), Cloudflare yerel dosyası çalışan yapılandırmayla eşitlendi, gluetun anahtarı `.env`, Suwayomi proxy `127.0.0.1:4567`.
- `/srv/project` + Samba `[project]` + Windows eşitleme betiği + gece sürümleme (Windows tarafı henüz çalıştırılmadı).
- Kısmi FHS: adguard, filebrowser, checkcle, guacamole, suwayomi, libreoffice → `/srv/appdata` (eski yollar link); arşivler `/srv/archive`; geçmiş dosyalar `/srv/operations/history`.
- Ana sayfa "Sunucu düzeni" bölümü; rehber `/srv/rehber` (gece yenilenir).

## Bekleyen işler — tamamlandı deme

1. `/arrapps` → `/srv/appdata` taşımasının geri kalanı (izin denetimi engelledi). Betikteki `install -d /srv/appdata` hatası düzeltilmeli.
2. `/mnt/side` ve `/mnt/sidemain` klasör düzeni (Downloads/downloads, Projects/projects çakışmaları).
3. Kök LUKS'ta TRIM (crypttab discard + initramfs + reboot, konsol başında).
4. Sunucu dışı yedek.
5. Windows VM: QEMU konuk ajanı; `eclipse-esitle-kur.ps1` VM içinde bir kez.
6. Karantinadaki boş klasörler incelenip silinebilir: `/srv/operations/changes/2026-10-20-fhs/yanlis-olusan-bos-klasorler`.

## Açık riskler

- Sistem SSD'si darboğaz ve aşınıyor (86 TB yazılmış, TRIM yok).
- sidemain %88, side %77 dolu.
- flugel parolasız tam sudo; self-heal.sh içinde düz metin API anahtarları; Docker soketi bağlı paneller.
