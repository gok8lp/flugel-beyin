---
tur: not
etiketler:
  - laptop
  - arch-linux
  - klasor-agaci
  - btrfs
  - luks
olusturma: 2026-11-12
guncelleme: 2026-11-12
---

# Laptop (ThinkBook 16p Gen 4) Disk Düzeni ve Dosya Ağacı

> **Üst Harita:** [[HARITA]] · [[hafiza]]
> **İlgili Notlar:** [[notlar/laptop-thinkbook-arch-hyprland-kurulumu]] · [[notlar/flugelserver-uc-disk-ve-klasor-agaci]]

> Kaynak: `lsblk`, `findmnt` ve ev klasörü taraması, 2026-11-12 (sen, sohbette)

## 1. Disk ve Bölümler (NVMe 466 GB)

```
nvme0n1           465.8G
├─nvme0n1p1         200M  vfat         EFI (muhtemelen Windows)
├─nvme0n1p2          16M               (muhtemelen Microsoft reserved)
├─nvme0n1p3       347.7G  BitLocker    Windows C:
├─nvme0n1p4         922M  ntfs         (muhtemelen Windows kurtarma)
├─nvme0n1p5        37.3G  ext4         (bağlı değil)
├─nvme0n1p6        77.7G  crypto_LUKS  → /dev/mapper/root (btrfs, zstd:3)
│   ├─ @           → /
│   ├─ @home       → /home
│   ├─ @.snapshots → /.snapshots   (snapper)
│   ├─ @log        → /var/log
│   ├─ @pkg        → /var/cache/pacman/pkg
│   ├─ @var_tmp    → /var/tmp
│   ├─ @docker     → /var/lib/docker
│   └─ @libvirt    → /var/lib/libvirt/images
└─nvme0n1p7           2G  vfat         /boot (linux-lts + linux)
zram0                 4G  swap         (disk swap yok → hibernate yok)
```

## 2. Sistem Tarafında Elle Değiştirilen Dosyalar

```
/etc/greetd/config.toml                       Noctalia Greeter oturumu
/etc/greetd/config.toml.yedek-orijinal
/etc/locale.gen                               yalnız en_US.UTF-8 açık
/var/lib/noctalia-greeter/                    greeter ayarları (greeter kullanıcısına ait)
/etc/systemd/system/display-manager.service → greetd.service   (SDDM kapalı)
```

## 3. Ev Klasörü (`/home/gokalp`)

Uygulama önbellekleri ve profil içleri gizlendi; `.ssh` içeriği yazılmadı.

```
~/   (/home/gokalp)
├── .claude/   # Claude Code oturum verisi
├── .config/
│   ├── Claude/   # Claude masaüstü uygulaması verisi
│   ├── dconf/   # GNOME ayar veritabanı
│   ├── ghostty/
│   ├── google-chrome/   # Chrome profili
│   ├── gtk-3.0/
│   ├── gtk-4.0/
│   ├── hypr/
│   │   ├── hyprland/
│   │   │   ├── shellOverrides/
│   │   │   │   └── main.lua
│   │   │   ├── animations.lua
│   │   │   ├── decoration.lua
│   │   │   ├── env.lua
│   │   │   ├── execs.lua
│   │   │   ├── general.lua
│   │   │   ├── gestures.lua
│   │   │   ├── group.lua
│   │   │   ├── input.lua
│   │   │   ├── keybinds.lua
│   │   │   ├── misc.lua
│   │   │   └── rules.lua
│   │   ├── scheme/
│   │   │   ├── current.conf
│   │   │   ├── current.lua
│   │   │   └── default.lua
│   │   ├── utils/
│   │   │   ├── functions.lua
│   │   │   └── json.lua
│   │   ├── hyprland.lua
│   │   ├── monitors.lua
│   │   ├── toggles.json
│   │   ├── user-vars.lua
│   │   ├── user.lua
│   │   └── variables.lua
│   ├── hypr.yedek-20261112/
│   ├── hypr.yedek-ambxst-oncesi/
│   ├── hypr.yedek-ambxst-sonrasi/
│   ├── hypr.yedek-noctalia-oncesi/
│   ├── hypr.yedek-noctalia-sonrasi/
│   ├── kitty/
│   ├── mozilla/   # Firefox profili
│   ├── noctalia/
│   ├── obsidian/   # Obsidian uygulama verisi
│   ├── pulse/   # PulseAudio/PipeWire durum
│   ├── qt5ct/
│   ├── qt6ct/
│   ├── systemd/
│   ├── vesktop/   # Vesktop (Discord) verisi
│   ├── yay/
│   ├── kdeglobals
│   └── mimeapps.list
├── .local/
│   ├── bin/
│   │   ├── kulaklik-degistir
│   │   └── pencere-gec
│   ├── share/
│   │   ├── applications/
│   │   ├── dbus-1/
│   │   ├── flatpak/
│   │   ├── hyprland/
│   │   ├── kio/
│   │   ├── kservices5/
│   │   ├── nautilus/
│   │   ├── pki/
│   │   ├── qalculate/
│   │   ├── sddm/
│   │   └── mimeapps.list
│   └── state/
├── .nv/
│   └── ComputeCache/
├── .ssh/   # SSH anahtarları (içerik yazılmadı)
├── Downloads/
├── eski-hypr/
│   ├── caelestia/
│   ├── custom/
│   ├── hyprland/
│   ├── scheme/
│   ├── utils/
│   ├── hyprland.lua
│   ├── keybinds.lua.copyq-yedek-20261025-232328
│   ├── kulaklik-degistir
│   ├── monitors.lua
│   ├── monitors.lua.yedek-20261030
│   ├── monitors.lua.yedek-20261030b
│   ├── pencere-gec
│   ├── variables.lua
│   ├── variables.lua.yedek-20261031-025338
│   ├── variables.lua.yedek-20261031-025623
│   └── variables.lua.yedek-alttab-20261028
├── Obsidian/
│   └── flugel-beyin/
│       ├── .brain/
│       ├── .claude/
│       ├── .obsidian/
│       ├── drafts/
│       ├── Düdük - Side Brain/
│       ├── kisiler/
│       ├── kurallar/
│       ├── notes/
│       ├── notlar/
│       ├── output/
│       ├── people/
│       ├── projects/
│       ├── projeler/
│       ├── raw/
│       ├── rules/
│       ├── sablonlar/
│       ├── skills/
│       ├── wiki/
│       ├── .gitignore
│       ├── brain.py
│       ├── CLAUDE.local.md
│       ├── CLAUDE.md
│       ├── decisions.md
│       ├── dersler.md
│       ├── gelen-kutusu.md
│       ├── hafiza.md
│       ├── HARITA.md
│       ├── hud-uret.py
│       ├── inbox.md
│       ├── kararlar.md
│       ├── lessons.md
│       ├── map.md
│       ├── memory.md
│       ├── second-brain-hud.html
│       ├── simdi.md
│       └── Welcome.md
├── Pictures/
│   └── Wallpapers/
│       ├── rezero-282vp9.png
│       ├── rezero-57lq91.jpg
│       └── rezero-d5gg1o.png
├── yay-bin/
│   ├── pkg/
│   ├── src/
│   ├── .gitignore
│   ├── .SRCINFO
│   ├── PKGBUILD
│   ├── yay-bin-13.1.0-1-x86_64.pkg.tar.zst
│   ├── yay-bin-debug-13.1.0-1-x86_64.pkg.tar.zst
│   └── yay_13.1.0_x86_64.tar.gz
├── .bash_history
├── .bash_logout
├── .bash_profile
├── .bashrc
├── .claude.json
└── .claude.json.backup
```

## 4. Önemli Yerler

| Yol | Ne |
|---|---|
| `~/.config/hypr/` | Aktif Hyprland (Lua) config'i — bkz. [[notlar/laptop-thinkbook-arch-hyprland-kurulumu]] |
| `~/.local/state/noctalia/settings.toml` | Noctalia arayüz ayarları |
| `~/.local/bin/` | `pencere-gec` (Alt+Tab), `kulaklik-degistir` (Super+Alt+K) |
| `~/.local/share/dbus-1/services/` | dunst'u devre dışı bırakan D-Bus kaydı |
| `~/Obsidian/flugel-beyin/` | Bu vault (sunucudan tek seferlik kopya) |
| `~/Pictures/Wallpapers/` | Re:Zero duvar kağıtları |
| `~/eski-hypr/` | Eski PC'nin ham config yedeği |
| `~/yay-bin/` | yay AUR yardımcısının kurulum artığı (silinebilir) |
