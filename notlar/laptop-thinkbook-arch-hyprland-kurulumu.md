---
tur: not
etiketler:
  - laptop
  - arch-linux
  - hyprland
  - noctalia
  - kurulum
  - suruculer
olusturma: 2026-11-12
guncelleme: 2026-11-12
---

# Laptop (ThinkBook 16p Gen 4): Arch + Hyprland Kurulum Günlüğü

> **Üst Harita:** [[HARITA]] · [[hafiza]] · [[kararlar]] · [[dersler]] · [[simdi]]
> **İlgili Notlar:** [[notlar/laptop-dux-shell-arayuzu]] · [[notlar/laptop-thinkbook-dosya-agaci]] · [[notlar/pc-arch-hyprland-ve-ubuntu-gnome-analizi]] · [[notlar/flugelserver-uc-disk-ve-klasor-agaci]]
> **İlgili Projeler:** [[projeler/linux-masaustu-araclari]]

Yeni kurulan laptopun 2026-11-12 tarihinde Claude Code ile kullanıma hazırlanma süreci. Eski PC'deki (flugel, Arch + Hyprland + Caelestia/end4) düzen bu makineye taşındı.

> Kaynak: sen, sohbette (Claude Code oturumu), 2026-11-12

---

## 1. Donanım ve Sistem

| Bileşen | Değer |
|---|---|
| Model | Lenovo ThinkBook 16p Gen 4 (21J8) |
| İşlemci | Intel Core i7-13700H |
| Grafik | Intel Iris Xe (i915) + NVIDIA RTX 4060 Max-Q (hibrit, `nvidia-open-dkms 615.78`) |
| RAM | 32 GB (+ 4 GB zram swap, disk swap yok → hibernate yok) |
| Ekran | eDP-1, 2560x1600 @ 60 Hz, ölçek **1.25** |
| Wi-Fi | Intel Raptor Lake CNVi (iwlwifi) |
| Disk | NVMe 466 GB: Windows (BitLocker) + Arch (LUKS → btrfs; alt birimler `@`, `@home`, `@.snapshots`, `@log`, `@pkg`, `@var_tmp`, `@docker`, `@libvirt`), `/boot` 2 GB vfat |
| Çekirdek | `linux-lts` 6.18 (açılış) + `linux` 7.2 (yedek), ikisi için de NVIDIA DKMS derli |
| Kullanıcı / host | `gokalp` @ `laptop` |
| Snapshot | snapper (her pacman işleminde pre/post) |

> Kaynak: `hostnamectl`, `lspci -k`, `lsblk`, `hyprctl monitors` çıktıları, 2026-11-12

---

## 2. Sunucuya Erişim (Tailscale)

- `flugel@192.168.0.15` yalnız **publickey** kabul ediyor; şifreli giriş kapalı, laptopun anahtarı kayıtlı değildi.
- Laptopta yeni anahtar üretildi: `~/.ssh/id_ed25519` (içerik vault'a yazılmaz).
- Çözüm: **Tailscale** kuruldu (`tailscaled` açık), laptop tailnet'e eklendi. `flugelserver` üzerinde **Tailscale SSH** açık olduğundan `ssh flugel@<flugelserver tailscale IP>` anahtarsız çalışıyor.
- Yan etki: laptopun `~/.ssh/authorized_keys` dosyasına kendi anahtarı yanlışlıkla eklendi (zararsız).

> Ders: Sunucu `PasswordAuthentication no` iken `ssh-copy-id` asla çalışmaz; Tailscale SSH bu durumda en kolay giriş yolu. → [[dersler]]

---

## 3. Sürücüler ve Sistem Paketleri

Zaten kurulu gelenler: `nvidia-open-dkms`, `nvidia-utils`, `lib32-nvidia-utils`, `libva-nvidia-driver`, `egl-wayland`, `mesa`, `vulkan-intel`, `intel-media-driver`, `intel-ucode`, `sof-firmware`, `linux-firmware`, PipeWire/WirePlumber, `bluez`, NetworkManager, `power-profiles-daemon`.

Eklenenler:

| Paket / Ayar | Neden |
|---|---|
| `lib32-vulkan-intel` | 32-bit Intel Vulkan (oyun/Steam) |
| `brightnessctl`, `playerctl` | Parlaklık ve medya tuşları |
| `hyprpolkitagent` (user servisi açık) | Yönetici şifre penceresi |
| `nvidia-suspend/hibernate/resume.service` | NVIDIA ile uyku/uyanma |
| `tailscale` | Sunucu erişimi |
| `obsidian` | Bu vault |
| Bluetooth `rfkill unblock` | Bluetooth yazılımsal engelliydi (soft block) |

- NVIDIA kartı boştayken **runtime suspend** ile uyuyor; masaüstü Intel'de çalışıyor (doğru olan, ekran Intel'e bağlı).
- Sistem dili **İngilizce** (`en_US.UTF-8`), klavye **`tr,us`** (Alt+Shift ile geçiş).

---

## 4. Hyprland Config'i (eski PC'den taşındı)

- Kaynak: sunucudaki yedek `/mnt/side/backups/arch-pc-2026-11-12/home/.config/hypr/` + `~/.config/caelestia/hypr-user.lua` ve `hypr-vars.lua`.
- Hyprland **0.57.2** yeni **Lua** config formatını kullanıyor; eski config de Lua olduğu için doğrudan taşındı.
- Yapı: `hyprland.lua` → `hyprland/*.lua` (env, general, input, misc, animations, decoration, group, execs, rules, gestures, keybinds) + `variables.lua` + `user-vars.lua` (eski hypr-vars) + `user.lua` (eski hypr-user) + `monitors.lua`.
- **Arayüz (caelestia/end4/quickshell) bağımlılıkları çıkarıldı**, kişisel ayarlar korundu (NVIDIA video env'leri sonradan kaldırıldı, bkz. §5b): PiP konum hafızası, Alt+Tab (`~/.local/bin/pencere-gec`), Super+Alt+K ses çıkışı (`~/.local/bin/kulaklik-degistir`), 4 parmak çalışma alanı, 5 parmak boş alan jesti, Türkçe klavye için `SUPER + *` boyutlandırma.
- Değiştirilenler: terminal `kitty` (terminator yok), tarayıcı `firefox`, imleç `Adwaita`, uyku `systemctl suspend` (hibernate yok).

### Önemli kısayollar (Noctalia ile)

| Tuş | İşlev |
|---|---|
| SUPER bas-bırak | Uygulama menüsü |
| SUPER+T / W / E | Terminal / tarayıcı / dosya yöneticisi |
| SUPER+Q, ALT+F4 | Pencere kapat |
| SUPER+1…0 · +ALT · +SHIFT | Çalışma alanına git · taşı · sessizce taşı |
| SUPER+S / M / D / R | Özel alanlar (special / music / communication / todo) |
| SUPER+N · SUPER+K | Kontrol merkezi · bildirimler |
| SUPER+V · SUPER+. | Pano · emoji |
| SUPER+L | Kilit (kapak kapanınca da) |
| CTRL+ALT+Delete | Oturum menüsü |
| Print · SUPER+SHIFT+S | Tam ekran · çizimli/bölge ekran görüntüsü |
| SUPER+CTRL+F10 / F11 | Duvar kağıdı / Noctalia ayarları |
| CTRL+SUPER+ALT+R | Noctalia'yı yeniden başlat |

---

## 5. Arayüz (Shell) Denemeleri ve Son Durum

| Sıra | Arayüz | Sonuç |
|---|---|---|
| 1 | Arayüzsüz (wofi + dunst) | Geçici |
| 2 | **Noctalia v5** (5.4.1, resmi depo) | JellyCat dotfiles'tan üst bar, sonra end4 benzeri bar, Türkçe dil, Inter font → hepsi kaldırıldı |
| 3 | **Ambxst** 1.3.15 (Axenide) | Kuruldu, 19 özellik test edildi; 3 yerel hata düzeltmesi gerekti → **tamamen silindi** (127 paket) |
| 4 | **Noctalia v5** (temiz) | 5.4.1 ile kuruldu |
| 5 | **Noctalia 5.5.0** (`noctalia-git`, AUR) | **Şu anki arayüz.** Resmi depoda 5.5 henüz yoktu; ayarlar korundu. Kullanıcı adım adım özelleştirecek |

- Ambxst'te bulunan hatalar (Hyprland Lua ile): kenarlık rengi çift tırnaklanıyordu, şema listesi kaydırılamıyordu, Bluetooth butonu rfkill engelini kaldırmıyordu. → [[dersler]]
- Noctalia notları: ayarlar `~/.local/state/noctalia/settings.toml`; `noctalia msg <komut>` ile kontrol; `margin_ends = "22%"` gibi yüzdeler 5.4.1'de çalışmıyor.
- Bildirimleri Noctalia alsın diye dunst'un D-Bus otomatik başlatması kapatıldı: `~/.local/share/dbus-1/services/org.knopwob.dunst.service`.
- Duvar kağıdı: `~/Pictures/Wallpapers/rezero-d5gg1o.png` (Emilia, eski PC'nin son duvar kağıdı) + 2 Re:Zero daha; sunucuda 149 tane var: `/mnt/sidemain/cloud/nextcloud/flugel/files/Yedekler/Arch PC - 2026-11-12/Pictures/Wallpapers/`.

---

## 5b. Chrome Donanım Video Çözme (eski PC çözümü uygulandı)

- **Sorun:** `user.lua` genel olarak `LIBVA_DRIVER_NAME=nvidia` veriyor; Chrome videoyu NVIDIA'da çözüp Intel'e aktaramıyor (siyah video, NVIDIA uyanık). Doğrulandı: düzeltme öncesi Chrome GPU süreci `nvidia_drv_video.so` yüklüyordu.
- **Çözüm** ([[notlar/pc-arch-hyprland-ve-ubuntu-gnome-analizi]] §3'teki ile birebir):
  - `~/.local/bin/google-chrome-stable` sarmalayıcı: NVIDIA değişkenlerini temizler, `LIBVA_DRIVER_NAME=iHD`, gerekirse `XDG_SESSION_TYPE=wayland`.
  - `~/.config/chrome-flags.conf`: `--enable-features=MiddleClickAutoscroll`, `--disable-features=AcceleratedVideoDecodeLinuxZeroCopyGL`.
  - `~/.local/share/applications/google-chrome.desktop` ve SUPER+W (`user-vars.lua` → `browser`) sarmalayıcıyı çağırır.
- **Doğrulama (2026-11-12):** Chrome 157 GPU süreci `iHD_drv_video.so`, yalnız `renderD128` (Intel); NVIDIA dosyası açık değil.
- **Kural:** Chrome'u asla doğrudan `/usr/bin/google-chrome-stable` ile açma; yeniden başlatırken `hyprctl dispatch 'hl.dsp.exec_cmd(...)'` kullan.
- **Aynı sorun:** Claude masaüstü uygulaması ve Obsidian (Electron) da `nvidia_drv_video.so` yüklüyordu.
- **Kalıcı sistem geneli çözüm (2026-11-12):** `~/.config/hypr/user.lua`'dan `LIBVA_DRIVER_NAME=nvidia`, `__GLX_VENDOR_LIBRARY_NAME=nvidia`, `NVD_BACKEND=direct` **kaldırıldı**; tüm uygulamalar varsayılan olarak Intel'de. Değişkenler başka hiçbir yerde (systemd user env, `/etc/environment`, bash) tanımlı değildi. Etkisi için **oturum kapat/aç veya yeniden başlat** gerekir.
- NVIDIA'da çalıştırmak gerekirse (oyun vb.): `__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia __VK_LAYER_NV_optimus=NVIDIA_only <uygulama>`. Chrome sarmalayıcısı zararsız olarak duruyor.

## 6. Giriş Ekranı (Noctalia Greeter)

- `greetd` 0.10.3 + `noctalia-greeter` 1.7.0 kuruldu; **SDDM kapatıldı**, greetd açık (yeniden başlatınca devreye girer).
- `/etc/greetd/config.toml` → `command = "/usr/bin/noctalia-greeter-session"`, `user = "greeter"`; orijinali `config.toml.yedek-orijinal`.
- Duvar kağıdı/renk senkronu: `noctalia msg greeter-sync` (Noctalia 5.5+, polkit onayı ister) — 2026-11-12'de Emilia duvar kağıdı aktarıldı.
- **Kurtarma:** giriş ekranı açılmazsa CTRL+ALT+F2 → giriş → `sudo systemctl disable greetd && sudo systemctl enable sddm && sudo reboot`

---

## 7. Açık İşler

- [x] `noctalia-git` 5.5.0 kuruldu ve greeter senkronu yapıldı (2026-11-12)
- [ ] Depoya `noctalia` 5.5 gelince `noctalia-git` yerine resmi pakete dön (git sürümü her güncellemede yeniden derlenir)
- [x] Yeniden başlatıldı (2026-11-12): Noctalia Greeter ile giriş çalıştı; Chrome ve Claude GPU süreçleri `iHD_drv_video.so` (Intel), NVIDIA kartı `suspended`; oturumda NVIDIA env değişkeni yok
- [ ] Noctalia'yı adım adım özelleştir (bar, renkler duvar kağıdından)
- [ ] Kasma hissi: kare süresi ölçümü, Hyprland VFR/direct scanout, gereksiz `xe` modülü, 1.25 kesirli ölçek
- [ ] Vault için sunucuyla otomatik eşitleme (Nextcloud) — şu an tek seferlik kopya

---

## 8. Yedekler

| Yol | İçerik |
|---|---|
| `~/eski-hypr/` | Eski PC'nin ham hypr + caelestia dosyaları |
| `~/.config/hypr.yedek-20261112/` | Kurulumun varsayılan config'i |
| `~/.config/hypr.yedek-noctalia-oncesi/`, `-sonrasi/` | Noctalia öncesi/sonrası |
| `~/.config/hypr.yedek-ambxst-oncesi/`, `-sonrasi/` | Ambxst öncesi/sonrası |
| `/etc/greetd/config.toml.yedek-orijinal` | greetd varsayılan ayarı |
