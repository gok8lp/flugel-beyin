# PC analizi — 28 Ekim 2026

Kaynak: PC01 / DESK01. Bu bir zaman damgalı gözlemdir; her uygulamanın bütün özellikleri, giriş ekranları ve veri kaybı senaryoları test edilmedi.

## Donanım ve disk

Lenovo ThinkBook 16p Gen 4 IRH; Intel Core i7-13700H, 14 fiziksel çekirdek / 20 iş parçacığı; yaklaşık 32 GB RAM. Intel Iris Xe + NVIDIA RTX 4060 Laptop 8 GB hibrit grafik. NVIDIA sürücüsü 615.78.08, gözlem anında 45°C. EndeavourOS, Linux 6.18.58-1-lts.

WD Blue SN5000 500 GB diskin Windows bölümü BitLocker olarak görünüyor. Linux Btrfs bölümü yaklaşık 78 GB: 50 GB kullanılmış, 27 GB boş, %66 dolu. `/`, `/home`, `/var/log`, `/var/cache` aynı dosya sisteminin alt birimleridir; kapasiteleri toplanmamalı. Linux bölümü lsblk'de doğrudan Btrfs görünüyor; buradan Linux şifrelemesi var sonucu çıkarılamaz. Ayrı yaklaşık 37 GB ext4 bölüm bağlı değil; içeriği açılmadı. 8 GB zram swap mevcut.

## Masaüstü

Hyprland 0.56.2; yapılandırma **Lua**. Eski `hyprland.conf` örnekleri doğrudan uygulanmamalı. Ana dosya `~/.config/hypr/hyprland.lua`; kişisel ekler `~/.config/caelestia/hypr-user.lua`. AOC DP-1 laptopun solunda: 1920×1080 60 Hz, x=-1920. Dahili eDP-1: 2560×1600 60 Hz, x=0. Güncel ölçekler: laptop %125 (1.25), AOC %100 (1). Bu ölçekler envanterden sonra kullanıcı isteğiyle güncellendi.

- `~/.config/quickshell/end4-pC`: https://github.com/pctrade/end4-pC, kurulan commit `74813a8`. Qt uyumluluğu ve yerel entegrasyon değişiklikleri var; temiz upstream kopyası değil.
- Caelestia sistem paketleri: shell 2.5.0, CLI 1.1.3.
- Caelestia-AW ayrıca `~/.local/share/caelestia-aw/` ve `~/.config/quickshell/caelestia-aw/` altında kullanıcıya özel derlendi. Sistem Caelestia dosyaları korunuyor.
- `~/.local/bin/arayuz-sec`: iki arayüz arasında geçiş, son seçimi saklama.
- `~/.local/bin/arayuz-ayarlari`: etkin arayüzün ayarlarını açma.
- `~/.local/bin/hareketli-duvar`: ortak resim/video seçici.
- `~/.local/bin/caelestia`: etkin arayüze göre AW CLI veya sistem CLI seçen sarmalayıcı.
- `~/.local/bin/mpvpaper`: oynatıcıyı geçici kullanıcı systemd servisi olarak başlatır; gerçek ikili `~/.local/libexec/mpvpaper`.
- `~/.local/state/arayuz-secimi`: son arayüz. `~/.config/illogical-impulse/config.json`: end4-pC tercihleri. Yerel presetler aynı klasörün `presets/` altındadır.

Kısayollar: Super+Ctrl+F12 arayüz seçimi, Super+Ctrl+F11 ayarlar, Super+Ctrl+F10 duvar kâğıdı. Super Windows tuşudur.

**Açık iş:** F11 hâlâ genel ayarların Quick ekranını açıyor. Videodaki preset ekranını doğrudan açma ve ok tuşlarıyla birebir geçiş önceki iş kesildiğinde tamamlanmamıştı. Kaynak incelemesinde varsayılan ayar penceresinde yukarı/aşağı kaydırma var; sağ/sol preset seçimi doğrulanmadı. “Video ile birebir aynı ve klavye testleri tamamlandı” denmemeli.

## Chrome, ses ve uygulamalar

Chrome 156.0.8078.47 (2 Kasım 2026 güncel, doğrulandı): donanım hızlandırma **açık**. Görüntüyü Intel Iris Xe (renderD129, ANGLE/GL, Wayland) çiziyor; video da Intel'de donanımla çözülüyor (`intel-media-driver`/iHD; H.264, VP9, AV1, 4K dahil). NVIDIA Chrome için hiç uyanmıyor. Eski YouTube boş video sorununun kök nedeni: Hyprland'in tüm uygulamalara verdiği `LIBVA_DRIVER_NAME=nvidia` videoyu NVIDIA'da çözdürüyor, Intel kareleri içe aktaramıyordu (`eglCreateImage 0x3009`). Kalıcı düzen: `~/.local/bin/google-chrome-stable` betiği NVIDIA değişkenlerini temizler, `LIBVA_DRIVER_NAME=iHD` verir ve oturum türü eksikse `XDG_SESSION_TYPE=wayland` ayarlar (yoksa XWayland'e düşüp ölçek bozuluyor). 24 `flugel-*.desktop` web uygulaması ve yerel `com.google.Chrome.desktop` bu betiği kullanır (yedek `~/.local/share/chrome-launcher-yedek-20261102-134555.tgz`). `~/.config/chrome-flags.conf`: `--disable-features=AcceleratedVideoDecodeLinuxZeroCopyGL`; zero-copy açıkken X'te kaydırırken her ~3 karede bir eski kare geri geliyordu, kapatınca kullanıcı düzeldiğini doğruladı. Chrome'u yeniden başlatmak için `systemd-run` değil `hyprctl dispatch "hl.dsp.exec_cmd(...)"` kullan. Yeni web uygulaması kısayolu `/usr/bin/google-chrome-stable` çağırırsa video sorunu geri gelir. PipeWire, WirePlumber ve pipewire-pulse çalışıyor.

Toplam 1720 paket; 21 yabancı/AUR paket, 21 bağımlılık olarak kurulmuş ve artık talep edilmeyen paket. Orphan etiketi gereksiz olduğunun kanıtı değildir; Go/Rust gibi kullanıcı araçları da olabilir. Otomatik kaldırma yapılmadı. Ayrıntılar PC-PAKETLER.tsv'de.

Docker motoru yerelde kurulmuş; gözlemde yerel konteyner yok. Claude Desktop `claude-desktop-deb` paketi 3.6556.2; `claude` terminal komutu PATH'te bulunamadı. Masaüstü Code sekmesi ile CLI kurulu olması farklı şeylerdir. `~/.claude/settings.json` var fakat `permissions` anahtarı yok; mevcut anahtarlar değiştirilmeyecek.

## Sağlık ve sınırlar

Sistem ve kullanıcı failed unit listeleri boş; Hyprland configerrors boş. 26 Ekim'den bir Quickshell SIGSEGV/coredump kaydı var; geçmiş kayıt tek başına güncel arıza kanıtı değil. Snapper zaman çizelgesi/temizlik, Btrfs scrub, fstrim ve paket önbellek temizleme zamanlayıcıları var. Snapshot, aynı diskin bozulmasına karşı ayrı yedek değildir. Root SMART incelemesi yerelde parola istemeyen sudo olmadığı için yapılmadı. Kullanıcının kişisel belgeleri, tarayıcı geçmişi, anahtarları ve parolaları okunmadı.
