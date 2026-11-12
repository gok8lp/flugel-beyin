---
tur: not
etiketler:
  - laptop
  - hyprland
  - dux-shell
  - arayuz
  - quickshell
olusturma: 2026-11-12
guncelleme: 2026-11-12
---

# Laptop Arayüzü: Dux Modular Shell (Caelestia benzeri düzen)

> **Üst Harita:** [[HARITA]] · [[hafiza]] · [[kararlar]] · [[dersler]] · [[simdi]]
> **İlgili Notlar:** [[notlar/laptop-thinkbook-arch-hyprland-kurulumu]] · [[notlar/pc-arch-hyprland-ve-ubuntu-gnome-analizi]]

2026-11-12'de Noctalia kaldırılıp yerine **Dux Modular Shell** (`dux-shell`, eski adı DankMaterialShell, Quickshell tabanlı) kuruldu. Hedef: eski PC'deki Caelestia'nın görünüşü.

## Neden Dux
- Arch `extra` deposunda paket olarak var (`sudo pacman -S dux-shell`).
- Yalnızca shell; kendi Lua Hyprland ayarına dokunmadan üstüne oturuyor (Hyprland 0.57 Lua destekli).
- Diğer adaylar: end-4 (komple dotfile, ayarları ezer), Serpantinum (yeni, ses/gamma daemon'larını değiştiriyor).

## Kaldırılanlar
- `noctalia-git`, `noctalia-greeter`, `dunst`, `wofi` ve artıkları; `~/eski-hypr` ve `hypr.yedek-*` klasörleri.
- Giriş ekranı **tuigreet** oldu (`/etc/greetd/config.toml`, yedek `config.toml.yedek`).

## Kurulu paketler
`dux-shell dux-gop matugen cava wtype wl-clipboard cliphist qt6ct hyprpicker xdg-desktop-portal-gtk kimageformats cups-pk-helper cups`

## Hyprland bağlantısı
- `dms setup` **kullanılmadı** (hyprland.lua'yı baştan yazar). Yalnızca parçalar üretildi: `~/.config/hypr/dms/`.
- `hyprland.lua` sonunda: `dms.colors`, `dms.cursor`, `dms.windowrules`, `dms.binds-user`. `dms/layout.lua` ve `dms/binds.lua` bilerek dahil değil (kendi boşluk/kısayollar korunuyor).
- Kısayollar `dms ipc call …` komutlarına yönlendirildi (`hyprland/keybinds.lua`): Super = başlatıcı, Super+N kontrol merkezi, Super+K bildirimler, Super+L kilit, Ctrl+Alt+Del güç menüsü, Super+Ctrl+F11 ayarlar, Super+Ctrl+F10 duvar kağıdı, Super+Shift+/ kısayol listesi, Ctrl+Super+Alt+R Dux yeniden başlat.
- Otomatik başlatma: `dms systemd enable` (hyprland-session.target).

## Görünüm ayarları (`~/.config/dms/settings.json`)
- Dil: Türkçe (`~/.local/state/dms/session.json` → `locale: tr`).
- Duvar kağıdı: `~/Pictures/Wallpapers/rezero-d5gg1o.png` (mor Emilia); renkler duvar kağıdından (matugen).
- **Frame (çerçeve)** açık, `connected` mod; renk Caelestia gibi opak yüzey rengi (`surfaceColor: default`). Caelestia videosundan tespit: çerçeve/bar/paneller opak `surface`, vurgular `primary`.
- Alt dock: otomatik gizli, alttan çıkıyor; sıra: sabit uygulamalar (Chrome, Claude, Obsidian, Kitty, Dolphin) → müzik widget'ı → uygulamalar düğmesi (9 nokta). `groupByApp: true`. İkinci alt bar kaldırıldı.
- Animasyon süresi 450 ms; başlatıcı son modu hatırlamıyor (Tümü sekmesinde açılır).

## Özel eklentiler
- **Siyah kavisli ekran köşeleri:** `~/.config/quickshell/ekran-koseleri/` (Quickshell katmanı, `execs.lua`'dan `qs -c ekran-koseleri`). Yarıçap `shell.qml` içinde `yaricap: 22`.
- **Dux yaması (dux-ozel):** `~/.local/share/dux-ozel/`
  - Dock simgesinde ad yerine canlı pencere önizlemesi (`DockWindowPreview.qml`), uygulamalar düğmesinde ipucu yok.
  - `yamalar/01-dock-onizleme.patch`, `yamala.sh`, `baslat.sh`; systemd drop-in `~/.config/systemd/user/dms.service.d/ozel.conf`.
  - Dux güncellenince: ilk açılış orijinal Dux, ~20 sn sonra yama yeni sürüme uygulanır ve bildirim gelir; uymazsa orijinal kalır.
  - Geri almak: `ozel.conf` dosyasını silip `systemctl --user daemon-reload && systemctl --user restart dms`.

## Sonraki geliştirmeler (2026-11-12 akşam)
- Dock önizlemeleri tıklanabilir (pencereye gider); odaktaki uygulamanın simgesine tıklamak pencereyi `special:kucuk` alanına gönderir, tekrar tıklamak geri getirir.
- Dock açılış/kapanış: aynı sönümlü yay (`defaultSpatial`, `popoutAnimationDuration * 1.9`), üzerine gelme zıplaması kapalı; kapanışta dock kendi arka planını da çizer (çerçeve arka planı önden gittiği için boşluk oluyordu).
- Pencere kenarlığı 0, `gaps_out` 10 (`user.lua`); çalışma alanı göstergesi koyu mor `#7c5cbf`.
- **Sağ kenar paneli** `~/.config/quickshell/sag-panel/`: ses/parlaklık dikey çubukları, ortada `~/Pictures/panel-karakter-seffaf.gif` (tıklayınca güç menüsü). Panel açıkken `$XDG_RUNTIME_DIR/sag-panel-durum` = 1 olur ve Dux'un ses/parlaklık OSD'si bastırılır (yama).
- Ekran kaydı: `wf-recorder` kuruldu.

## Açık konular
- Önizleme ve müzik tıklama animasyonu gerçek fareyle test edilmedi; güncelleme yama akışı gerçek güncellemeyle denenmedi.
- Sonraki fikirler: barı Caelestia gibi sol kenarda dikey yapmak, kenarlardan açılan paneller.
