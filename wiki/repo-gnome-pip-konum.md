---
title: GitHub Depo Analizi — gok8lp/gnome-pip-konum
sources: raw/github/gnome-pip-konum.md, raw/github/00-github-envanteri.md, raw/github/01-tum-repolar-commit-gecmisi.md
updated: 2026-11-11
---

# GitHub Depo Analizi: `gok8lp/gnome-pip-konum`

Üst Katalog: [[github-repolar-katalogu]] · [[sunucu-ve-github-commit-gecmisi]] · [[duduk-genel-bakis]] · [[flugelserver-genel-mimari]]

> "GitHub Repo: gok8lp/gnome-pip-konum" - raw/github/gnome-pip-konum.md

> "gok8lp GitHub Depoları Tam Commit Geçmişi" - raw/github/01-tum-repolar-commit-gecmisi.md

## Son Commit Geçmişi (`gok8lp/gnome-pip-konum`)
- `aa541a2` (2026-10-29): README: klonlama adresini ekle
- `745ec03` (2026-10-29): MIT lisansı ekle
- `16eb04e` (2026-10-29): README: kurulum, özellikler, test
- `0ac08da` (2026-10-29): 3 sanal monitörlü ekransız test ekle
- `5abcfa6` (2026-10-29): PiP konum hafızası GNOME eklentisi

## Dosya Ağacı ve README Özeti
# GitHub Repo: gok8lp/gnome-pip-konum

- **URL:** https://github.com/gok8lp/gnome-pip-konum
- **Görünürlük:** Açık (Public)
- **Ana Dil:** JavaScript
- **Son Güncelleme:** 2026-10-29T21:49:46Z
- **Açıklama:** Chrome PiP pencerelerini ilk seferde sağ altta, sonra son konum ve boyutta açan GNOME eklentisi (çoklu monitör destekli)

## Dosya Ağacı (File Tree)
- `LICENSE` (blob)
- `README.md` (blob)
- `kaldir.sh` (blob)
- `kur.sh` (blob)
- `pip-konum@gokalp` (tree)
- `pip-konum@gokalp/extension.js` (blob)
- `pip-konum@gokalp/metadata.json` (blob)
- `test` (tree)
- `test/cdp.mjs` (blob)
- `test/page.html` (blob)
- `test/test.sh` (blob)

## README İçeriği
# PiP Konum Hafızası · GNOME Eklentisi

Chrome'un resim içinde resim (PiP) ve küçük popup pencerelerini ilk seferde **sağ altta** açar.
Sonra pencereyi nereye taşır ve hangi boyuta getirirsen bir sonraki açılışta **orada ve o boyutta** açar.
YouTube, Spotify Web mini oynatıcısı ve diğer PiP pencerelerinde çalışır.

GNOME Wayland'da Chrome pencere konumunu kendisi seçemez; bu eklenti işi pencere yöneticisinin içinde yapar.

## Kurulum

```bash
git clone https://github.com/gok8lp/gnome-pip-konum.git && cd gnome-pip-konum
./kur.sh
```

Sonra **oturumu bir kez kapatıp aç**. Wayland'da GNOME eklenti kodunu yalnızca oturum açılışında yükler.

## Özellikler

- **İlk açılış:** Panel ve dock'u hesaba katarak bulunduğu monitörün sağ alt köşesi.
- **Hafıza:** Konum ve boyut, pencere taşındıkça ve kapanırken `~/.local/share/pip-konum/state.json` dosyasına yazılır.
- **Çoklu monitör:** PiP hangi monitörde bırakıldıysa orada açılır. Monitör düzeni değişirse aynı monitörde ekrana göre aynı oranda bir yere konur. Monitör sökülürse mevcut monitörde sağ alta döner.
- **Sanal masaüstleri:** PiP tüm çalışma alanlarında görünür ve hep üstte kalır.
- **Tanıma:** Chrome PiP penceresi Wayland'da boş uygulama adıyla açılır; eklenti pencereyi ait olduğu süreçten (`/proc/<pid>/comm`) tanır.

Desteklenen GNOME sürümleri: 48–52.

## Test

Eklentiyi ekransız, 3 sanal monitörlü ayrı bir GNOME Shell'de gerçek bir Chrome PiP'iyle dener.
Senin oturumuna, kayıtlı konumuna ve Chrome profiline dokunmaz.

```bash
sudo apt-get install mutter-dev-bin dbus-daemon   # bir kez
./test/test.sh
```

## Sorun giderme

```bash
journalctl --user -b -o cat | grep pip-konum
```

## Kaldırma

```bash
./kaldir.sh
```

## Lisans

[MIT](LICENSE)



## İlgili Mimari Sayfaları
- [[github-repolar-katalogu]]
- [[sunucu-ve-github-commit-gecmisi]]
- [[pc-masaustu-hyprland-ve-gnome-araclari]]
- [[koharia-reader-ve-manga-ekosistemi]]
