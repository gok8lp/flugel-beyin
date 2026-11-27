# Threads

## Active Threads
### İkinci beyin: flugel-beyin derlemesi ve V3 geçişi
- **Sahip:** Gökalp (ajanlarla birlikte).
- **Durum (2026-11-27, gece):** Beyin otonomisi: Codex/Gemini bitiş bekçisi (test edildi) ve haftalık `beyin-bakim` (pazar 10:00 → `knowledge/beyin-bakim.md`). Codex hook güven onayı Gökalp'te.
- **Durum (2026-11-27):** Ortak skill ve ajan sistemi kuruldu ve 7 tur sıfırdan ajan testiyle doğrulandı ([[knowledge/kararlar]] 2026-11-26 satırı; rapor `second-brain/raporlar/skill-ve-ajan-sistemi-2026-11-26.md`). Yeni ajan girişi: `~/Documents/ai_workplace/YENI-AJAN.md`. Bilinen eksik: Claude limiti okunamıyor (`claude login` Gökalp'te); `beyin.py` salt okunur sandbox'ta yazma hatası (upstream, `beyin-ara` ile aşılıyor); lint'in `[[receipts/…md|…]]` yanlış alarmı (upstream).
- **Durum (2026-11-15, Claude doctor kontrolü):** V3 sağlıklı: hook yolları ve global köprü ok, scheduled-check ok, güncel sürüm, bekleyen olay 0; 2026-11-15 onarımında lint kırık 0/yetim 0. Kökteki `hafiza`, `simdi`, `gelen-kutusu` yalnız yönlendirme; `kararlar`/`dersler` knowledge/'a taşınmış. Jev modu `on` ve **açık kalacak** (Gökalp kararı, 2026-11-15 19:51).
### Hakemlik ve Düdük
- **Sahip:** Gökalp.
- **Durum (2026-11-27, Düdük arşivinden):** 11 atama (13 Kas–2 Ara): 13 Kas Taha Akgül U14E-B 73-53 ve U18E-B 51-96 (2. hakem), 18 Kas MEB U16E-A 72-60 ve 62-79 (2. hakem), 24 Kas GİMSA U12/U11 AGL (2. hakem); yaklaşan 28 Kas Sincan U16E-C ×3 (1. hakem, Ali Barış Hazinedar), 2 Ara MEB U14K-A ×2 (2. hakem, Kaan Çam). Güncel liste her gün otomatik: [[knowledge/hakem-maclari]].
- **Durum:** 13 Kasım 2026 Cuma Taha Akgül Spor Salonu maçları (U14 Erkek B ve U18 Erkek B, ikisinde de `referee2`) geçti; sonuç kayıtlı değil. Saat ve eşleşmeler simdi.md ile [[projeler/hakemlik]] arasında farklı yazılmış; ayrıntı [[notes/simdi-2026-11-hafta-2]].
- **Açık işler (tasks/):** canlı sunucu arşivinin (`https://duduk.gokalpgoksu.com/v1/stats`) yeni hafta atamalarını yakalamasını izlemek; `assignr` yeni hafta yayın saatini loglardan gözlemlemek; ilk `BÖLGE` ödemesinde net maç ücretini kaydetmek.
- **Sonraki adım:** 14-20 Kasım atamaları yayımlanınca `/v1/stats` ve değişiklik tespitini kontrol et ([[projeler/duduk]]).
- **2026-11-24:** Basket botu Türkçe metin tarih hatası düzeltildi (yeni atama/sabah hatırlatması gitmiyordu); 24 Kasım 17:30 ve 20:30 maçları görünüyor. Düdük telefonda kasıyor: v0.3.0 debug APK → iOS kalitesi işi Canalp'a devredildi (`second-brain/DEVIR-canalp-duduk.md`, oturumu Gökalp açacak). Gemini basket-bot'a ICS takvim + çakışma uyarısı geliştiriyor (yüklenmedi).

### Gazi EEM 2026 Güz dönemi (Teknoloji Fakültesi, Elektrik-Elektronik)
- **Sahip:** Gökalp.
- **Durum (2026-11-27, Gökalp sohbette):** Vize dönemi çoktan bitti. Gökalp Gazi Üniversitesi Teknoloji Fakültesi Elektrik-Elektronik Mühendisliği öğrencisi. Vize sonuçları kayıtlı değil; dönem sonu (final) tarihleri ve kapsamı henüz beyinde yok.
- **Durum:** EE317 Güç Elektroniği I vizesi 12 Kasım 2026 09:00'da yapıldı (kapsam D1–D4, tristör yok; [[notlar/ee317-vize-calismasi-2026-11-11]]); sonucu kayıtlı değil. simdi.md'deki EE313 ve EE333 "vize tekrarı" maddeleri bayat: [[projeler/okul-guz-2026]] bu iki vizeyi 7 ve 9 Kasım'da tamamlandı olarak gösteriyor.
- **Sonraki adım:** Final takvimi açıklanınca [[projeler/okul-guz-2026]] içine işle; vize sonuçları Gökalp söylerse eklenir. (Eski adım: Vize sonuçlarını ve EE346 sınav zamanını [[projeler/okul-guz-2026]] içinde güncelle ([[notlar/gazi-eem-vize-takvimi-ve-ders-notlari]]).

### flugelserver ağ güvenliği
- **Sahip:** Gökalp.
- **Durum (2026-11-26):** Bakım yükü azaltıldı: Cup oto-güncelleme haftalık (pazar 07:30 TSİ), arıza zinciri 10 dk eşik ve beyne yalnız gerçek onarım kaydı, yedek kontrolü günlük, günlük durum notu [[knowledge/sunucu-durum]]. Rapor: `second-brain/raporlar/sunucu-sadelestirme-2026-11-26.md`.
- **Medya istemcileri (2026-11-27):** Laptopa plex-desktop + jellyfin-desktop (AUR) kuruldu. Jellyfin: Tailscale `:12443` / `100.86.88.1:8096`, LAN `192.168.0.15:8096`. Plex: `:44443` / `:32400`, `plex.gokalpgoksu.com`. Funnel 443 artık Jellyfin değil. Rapor: `second-brain/raporlar/plex-jellyfin-istemci-kurulumu-2026-11-27.md`.
- **Şifreler (2026-11-27):** Vaultwarden kasası (yalnız Tailscale kimliği), 21 uygulama + gokalpgoksu.com ortak kapısı benzersiz şifreye döndü (`~/Documents/ai_workplace/sifre-dondur`). Açık: Jellyfin şifresi, Komga/Kavita yerel şifreleri.
- **Sonraki adım:** Jellyfin şifresi; servis azaltma (raporda aday listesi) ve `/mnt/sidemain` %89.
- **Durum (2026-11-15):** Ev ağı entegrasyonu tamamlandı ([[knowledge/concepts/ev-agi-ve-dis-erisim]]): modem ve Tailscale DNS'i AdGuard'a yönlü, evde gokalpgoksu.com doğrudan HTTPS ve `.ev` adları, Mullvad proxy `:8889`, Wi-Fi ayarları, eski Tailscale cihazları silindi. **Funnel bilerek açık kalır** (Gökalp kararı; görev kapandı). `adguard.gokalpgoksu.com` A kaydı hâlâ 178.233.25.73'ü gösteriyor (CGNAT yüzünden işe yaramaz).
- **Durum (2026-11-24):** AdGuard hız sınırı kapatıldı (ev tek istemci sayılıyordu); ölü adların DNS'i yerel akış tüneline alındı (tools/portainer/admin/adguard artık çalışıyor; office/convert/pdf/ai/bd/ui 404). 40+ yeni `*.gokalpgoksu.com` FLUGEL kapısı arkasında; Tailscale istemcileri kapıyı atlar (AdGuard `100.64.0.0/10` kuralı + `127.0.0.1:8198`). Laptop Tailscale `RouteAll: true`; laptop/modem ikinci DNS'e Gökalp isteğiyle dokunulmadı.
- **Sonraki adım:** Cloudflare panelinde eski uzaktan yönetilen tünel rotalarını temizle; internete açık Portainer/Dockge/File Browser için Cloudflare Access ekle. Rapor: `second-brain/raporlar/sunucu-hata-taramasi-2026-11-24.md`.

### Laptop bakımı (ThinkBook, Arch + Hyprland + Dux)
- **Sahip:** Gökalp.
- **Durum (2026-11-27):** Tek çekirdek `linux` 7.3.6 (LTS kaldırıldı, systemd-boot varsayılanı `arch-linux.efi`). Hyprland eklentisi `dynamic-cursors` açılışta `~/.local/bin/hypr-eklenti-derle` ile yüklenir, sürüm uyumsuzsa kendini yeniden derler. Quickshell yerelde Qt 6.12.1 ile derlendi (`0.3.2-1.1`). Kilit ekranı tuş takımı yaması `dux-ozel/yamalar/02-kilit-numpad.patch`; eski `kilit-numlock` servisi arşivde. Rapor: `second-brain/raporlar/2026-11-27-laptop-acilis-cekirdek-kilit.md`.
- **Dolphin + Syncthing (2026-11-27):** Dolphin `/usr/local/bin/dolphin` sarmalayıcısıyla qt6ct + `FlugelSiyah` şemasında açılır (GTK teması açık olduğu için adlar siyah çiziliyordu). Terminal: F4 panel, Ctrl+Alt+T Ghostty (`--gtk-single-instance=false`, yoksa klasör kaçıyor). Syncthing iki uçta algılama 1 sn. Rapor: `second-brain/raporlar/2026-11-27-dolphin-tema-syncthing.md`.
- **Telefon + son dosyalar (2026-11-27):** KDE Connect `kdeconnectd.service` (kullanıcı, enabled) + ufw yalnız LAN/Tailscale; telefonlarda eşleştirme Gökalp'te. Son Dosyalar için `plasma-kactivitymanagerd` servisi. Disk %81: yay önbelleği 11 GB, pacman 8 GB, temizlik onay bekliyor.
- **Sonraki adım:** Yeniden başlatıp `acilis-kontrol` çalıştır; kilit ekranında tuş takımıyla parola dene (elle denenmedi). Giriş ekranında da aynı sorun varsa dux-greeter için çözüm ara.

## Closed Threads
Arşivlenen metin: `🔮 850-Companion/Arşiv/Threads-2026-11.md`
