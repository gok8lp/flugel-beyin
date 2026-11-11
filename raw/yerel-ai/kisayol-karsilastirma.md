# Kısayol karşılaştırması — Caelestia (referans) ↔ end4-pC

Test: 2026-10-28 02:45:06, ydotool ile gerçek tuş basımı; fark = basılınca ortaya çıkan katman/pencere. (Kilit/uyku/kayıt kısayolları güvenlik nedeniyle basılmadı.)

## 1) Caelestia (referans)

Super (tek basış: başlatıcı) | YENİ: — | KAYBOLAN: —
Ctrl+Alt+Delete (oturum menüsü) | YENİ: — | KAYBOLAN: —
Super+N (yan panel) | YENİ: — | KAYBOLAN: —
Super+K (paneller) | YENİ: — | KAYBOLAN: —
Print (ekran görüntüsü) | YENİ: — | KAYBOLAN: —
Super+Shift+S (dondur+bölge) | YENİ: caelestia-area-picker  | KAYBOLAN: —
Super+Shift+Alt+S (bölge) | YENİ: caelestia-area-picker  | KAYBOLAN: —
Super+V (pano) | YENİ: launcher  | KAYBOLAN: —
Super+Alt+V (pano sil) | YENİ: launcher  | KAYBOLAN: —
Super+. (emoji, fiziksel 52) | YENİ: — | KAYBOLAN: —
Super+. (emoji, fiziksel 53) | YENİ: launcher  | KAYBOLAN: —
Ses + (XF86AudioRaiseVolume) | YENİ: — | KAYBOLAN: —
Ses − (XF86AudioLowerVolume) | YENİ: — | KAYBOLAN: —
Parlaklık + (XF86MonBrightnessUp) | YENİ: — | KAYBOLAN: —
Parlaklık − (XF86MonBrightnessDown) | YENİ: — | KAYBOLAN: —
Ctrl+Alt+C (bildirimleri temizle) | YENİ: — | KAYBOLAN: —
Super+Shift+C (renk seçici) | YENİ: hyprpicker  | KAYBOLAN: —
Super+A (uygulama ızgarası) | YENİ: app-izgara  | KAYBOLAN: —
Super+H (kısayol rehberi) | YENİ: kisayol-rehberi  | KAYBOLAN: —
Super+Tab (pencere ara) | YENİ: launcher  | KAYBOLAN: —

## 2) end4-pC (düzeltme ÖNCESİ)

Super (tek basış: başlatıcı) | YENİ: quickshell:overview  | KAYBOLAN: —
Ctrl+Alt+Delete (oturum menüsü) | YENİ: quickshell:session  | KAYBOLAN: —
Super+N (yan panel) | YENİ: quickshell:sidebarRight  | KAYBOLAN: —
Super+K (paneller) | YENİ: quickshell:sidebarRight  | KAYBOLAN: —
Print (ekran görüntüsü) | YENİ: quickshell:notificationPopup  | KAYBOLAN: —
Super+Shift+S (dondur+bölge) | YENİ: — | KAYBOLAN: —
Super+Shift+Alt+S (bölge) | YENİ: — | KAYBOLAN: quickshell:notificationPopup 
Super+V (pano) | YENİ: launcher  | KAYBOLAN: —
Super+. (emoji, fiziksel 53) | YENİ: launcher  | KAYBOLAN: —
Ses + (XF86AudioRaiseVolume) | YENİ: — | KAYBOLAN: —
Ses − (XF86AudioLowerVolume) | YENİ: — | KAYBOLAN: —
Parlaklık + (XF86MonBrightnessUp) | YENİ: — | KAYBOLAN: —
Parlaklık − (XF86MonBrightnessDown) | YENİ: — | KAYBOLAN: —
Ctrl+Alt+C (bildirimleri temizle) | YENİ: — | KAYBOLAN: —
Super+Shift+C (renk seçici) | YENİ: hyprpicker  | KAYBOLAN: —
Super+A (uygulama ızgarası) | YENİ: app-izgara  | KAYBOLAN: —
Super+H (kısayol rehberi) | YENİ: kisayol-rehberi  | KAYBOLAN: —
Super+Tab (pencere ara) | YENİ: launcher  | KAYBOLAN: —

## 3) end4-pC (düzeltme SONRASI)

Super+K (paneller) | YENİ: quickshell:overview quickshell:sidebarRight  | KAYBOLAN: —
Super+Shift+S (dondur+bölge) | YENİ: quickshell:regionSelector  | KAYBOLAN: —
Super+Shift+Alt+S (bölge) | YENİ: quickshell:regionSelector  | KAYBOLAN: —

## 4) Sonuç (Caelestia = referans)

| Kısayol | Caelestia | end4-pC önce | end4-pC şimdi |
|---|---|---|---|
| Super (tek basış) | başlatıcı (bu makinede ekranda görünür bir pencere üretmedi) | arama + 10 çalışma alanı ızgarası | **yalnız arama/başlatıcı** (ızgara kaldırıldı; ızgara `search workspacesToggle` ile hâlâ erişilebilir) |
| Ctrl+Alt+Delete | oturum menüsü (sağda dikey düğmeler) | oturum menüsü | aynı işlev |
| Super+N | sağ yan panel | sağ yan panel | aynı |
| Super+K | tüm paneller (pano/başlatıcı + yan panel) | yalnız yan panel | **arama + yan panel birlikte** |
| Print | ekran görüntüsü + "Screenshot taken" bildirimi | aynı | aynı |
| Super+Shift+S / +Alt+S | alan seçici | hiçbir şey | **bölge seçici (regionSelector)** |
| Ctrl+Alt+C | bildirimleri temizle | çalışmıyordu | **temizliyor, zil sayacı 0** |
| Super+V / Super+Alt+V / Super+. | fuzzel pano / pano sil / emoji | aynı | aynı |
| Ses/parlaklık tuşları | kenarda OSD hapı | OSD (kısa süre) | aynı |
| Super+Shift+C | hyprpicker | aynı | aynı |
| Kilit, uyku, ekran kaydı | **basılmadı** (kilidi açmak parola ister; kayıt dosya üretir) | — | — |

Değişen dosyalar: `~/.local/bin/arayuz-komut`, `~/.config/hypr/hyprland/keybinds.lua`, end4-pC `services/Notifications.qml`, `modules/ii/overview/Overview.qml` (hepsinin `.yedek-20261028*` kopyası yanında).
