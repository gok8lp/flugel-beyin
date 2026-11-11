---
tur: proje
etiketler:
  - proje
  - linux
  - hyprland
  - gnome
  - pipewire
  - wayland
  - masaustu
durum: aktif
olusturma: 2026-11-11
guncelleme: 2026-11-11
---

# Linux Masaüstü, Hyprland ve GNOME Araçları

> Üst bağlantı: [[HARITA]] · Odak: [[simdi]] · Bağlam: [[hafiza]] · Kararlar: [[kararlar]] · Sorumlu: [[kisiler/ahmet-gokalp-goksu]]

## Genel Bakış
Kişisel iş istasyonu (**Lenovo ThinkBook 16p Gen 4**, RTX 4060, Arch Linux + Hyprland ve Ubuntu 26.04 + GNOME 50 Wayland kurulumları) üzerinde günlük üretkenliği, ses işleme kalitesini, çoklu monitör PiP pencere yönetimini, pano (clipboard) akışını ve donanım uyumluluğunu iyileştirmek için geliştirilen 8 açık kaynaklı masaüstü aracı ve kabuk eklentisi grubudur.

## Kapsanan Depolar ve Bileşenler

| Depo Adı | Dil | Son Güncelleme | Açıklama ve Öne Çıkan Özellikler |
|---|---|---|---|
| **`headset-surround-linux`** | Shell | `2026-10-31` | PipeWire üzerinde herhangi bir kulaklık için tek komutla sanal 7.1 surround, Dolby benzeri Sinema modu ve Bass Boost çıkışı (`bd9c465`). |
| **`end4-pC`** | QML | `2026-10-30` | Hyprland/Caelestia masaüstü ayarları, yerel araçlar, yalnızca Discord için Mullvad ayrık tüneli, PiP monitör konum tercihi (`3c34956`) ve Türkçe geri yükleme belgeleri içeren kişisel çatal (fork). |
| **`ubuntu-tam-guncelle`** | Shell | `2026-10-29` | Ubuntu sistemini (`apt`, `snap`, `flatpak` ve `fwupd` aygıt yazılımı kontrolü) tek komutla güvenli biçimde güncelleyen MIT lisanslı betik (`2a355a5`). |
| **`chrome-orta-tik-kaydirma`** | Shell | `2026-10-29` | Linux'ta Google Chrome'a orta tuşla otomatik kaydırma (autoscroll) ekleyen ve `--test-type` ile uyarı çubuğunu gizleyen aç/kapat betikleri (`83945af`). |
| **`gnome-pip-konum`** | JS | `2026-10-29` | Chrome Resim İçinde Resim (PiP) pencerelerini ilk açılışta sağ altta, sonrasında son bırakılan konum ve boyutta açan çoklu monitör destekli ve 3 sanal monitörlü ekransız (headless) testli GNOME eklentisi (`0ac08da`). |
| **`k380s-ubuntu-fn`** | Shell | `2026-10-29` | Logitech Pebble Keys 2 K380s klavyenin üst sıra F4-F9 tuşlarını Ubuntu GNOME/Wayland altında Solaar kurallarıyla (masaüstü, arama, geri, mikrofon sustur, emoji, ekran görüntüsü) tam işlevli yapan paket (`c403efc`). |
| **`clipline-linux`** | JS | `2026-10-28` | ClipBoardLine Electron sürümünün Wayland/Hyprland uyarlaması; `wl-copy` pano yazımı (`4ef9524`) ve `hyprctl` katman odaklama (`0991be1`) ile klavye öncelikli pano rafları. |
| **`gnome-island`** | JS | `2026-10-22` | GNOME Shell 50 için bildirim, medya oynatıcı, pano geçmişi, hızlı araçlar, oyun fırsatları (PS Plus/Epic) ve sistem izlemeyi tek kapsülde toplayan **Quiet Orbit v3 / v3.1** eklentisi (164+ uçtan uca test). |

## Mevcut Durum (11 Kasım 2026)
- `headset-surround-linux`, `end4-pC`, `ubuntu-tam-guncelle`, `chrome-orta-tik-kaydirma`, `gnome-pip-konum`, `k380s-ubuntu-fn` ve `clipline-linux` depoları son 14 gün içinde (28–31 Ekim 2026) güncellenmiş olup **aktif** durumdadır.
- **Bayatlık Notu (>14 Gün Kuralı):** `gnome-island` deposunun son GitHub commit'i `2026-10-22` (20 gün önce) tarihindedir; v3.1 sürümü kararlıdır ancak yeni özellik eklemesi yapılmamıştır.

## Sıradaki Adımlar
- [ ] `clipline-linux` içinde `README`'de belgelenen açık yapıştırma/klavye odaklama (paste/keyboard focus) uç durumunu Hyprland üzerinde çözmek.
- [ ] `end4-pC` üzerindeki Hyprland/Caelestia iş istasyonu ayarlarını güncel Arch Linux paketleriyle senkron tutmak.
- [ ] Lenovo UEFI açılış logosu (`lenovo-logo-flugel.bmp`) değişimi için EFI değişkeni risk değerlendirmesini tamamlayıp karar vermek.

## Öne Çıkan Commit Geçmişi
- `headset-surround-linux` — `bd9c465` (2026-10-31): `Add Bass Boost output`
- `end4-pC` — `3c34956` (2026-10-30): `chore(desktop): preserve saved PiP monitor placement preference`
- `end4-pC` — `c7f9b57` (2026-10-30): `chore(desktop): archive effective workstation settings and restore notes`
- `ubuntu-tam-guncelle` — `2a355a5` (2026-10-29): Tek komutla tam sistem güncelleme betiği
- `chrome-orta-tik-kaydirma` — `83945af` (2026-10-29): Uyarı çubuğunu `--test-type` ile gizle
- `gnome-pip-konum` — `0ac08da` (2026-10-29): 3 sanal monitörlü ekransız test ekle
- `k380s-ubuntu-fn` — `c403efc` (2026-10-29): Solaar tuş kuralları: F4-F9 için GNOME karşılıkları
- `clipline-linux` — `4ef9524` (2026-10-28): `Write the clipboard through wl-copy`
- `gnome-island` — `6d1b10a` (2026-10-18): `3.0.0 surum notu` (Quiet Orbit v3, duyarlı Hızlı ızgaraları, canlı etkinlik susturma)

## İlgili Sayfalar ve Bağlantılar
- **Harita ve Kök:** [[HARITA]] · [[simdi]] · [[hafiza]] · [[kararlar]] · [[dersler]]
- **İlgili Projeler ve Kişiler:** [[projeler/flugel-sunucu-ve-akis]] · [[kisiler/ahmet-gokalp-goksu]]
- **Wiki Sayfaları:**
  - [[wiki/pc-masaustu-hyprland-ve-gnome-araclari]]
  - [[wiki/repo-end4-pc]]
  - [[wiki/repo-gnome-island]]
  - [[wiki/repo-gnome-pip-konum]]
  - [[wiki/repo-headset-surround-linux]]
  - [[wiki/repo-clipline-linux]]
  - [[wiki/repo-k380s-ubuntu-fn]]
  - [[wiki/repo-chrome-orta-tik-kaydirma]]
  - [[wiki/repo-ubuntu-tam-guncelle]]
- **Bilgi Notları:**
  - [[notlar/arch-hyprland-ve-gnome-masaustu-araclari]]
  - [[notlar/flugelserver-mimari-ozeti]]

> Kaynaklar: `raw/github/00-github-envanteri.md`, `raw/github/01-tum-repolar-commit-gecmisi.md`, `raw/flugelserver/FLUGEL-OZET.md`
