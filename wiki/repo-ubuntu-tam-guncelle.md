---
title: GitHub Depo Analizi — gok8lp/ubuntu-tam-guncelle
sources: raw/github/ubuntu-tam-guncelle.md, raw/github/00-github-envanteri.md, raw/github/01-tum-repolar-commit-gecmisi.md
updated: 2026-11-11
---

# GitHub Depo Analizi: `gok8lp/ubuntu-tam-guncelle`

Üst Katalog: [[github-repolar-katalogu]] · [[sunucu-ve-github-commit-gecmisi]] · [[duduk-genel-bakis]] · [[flugelserver-genel-mimari]]

> "GitHub Repo: gok8lp/ubuntu-tam-guncelle" - raw/github/ubuntu-tam-guncelle.md

> "gok8lp GitHub Depoları Tam Commit Geçmişi" - raw/github/01-tum-repolar-commit-gecmisi.md

## Son Commit Geçmişi (`gok8lp/ubuntu-tam-guncelle`)
- `d9f5364` (2026-10-29): README: klonlama adresini ekle
- `940d5b6` (2026-10-29): MIT lisansı ekle
- `b19a118` (2026-10-29): README: adımlar ve güvenlik notları
- `2a355a5` (2026-10-29): Tek komutla tam sistem güncelleme betiği

## Dosya Ağacı ve README Özeti
# GitHub Repo: gok8lp/ubuntu-tam-guncelle

- **URL:** https://github.com/gok8lp/ubuntu-tam-guncelle
- **Görünürlük:** Açık (Public)
- **Ana Dil:** Shell
- **Son Güncelleme:** 2026-10-29T21:49:59Z
- **Açıklama:** Ubuntu'yu tek komutla tamamen günceller: apt, snap, flatpak, aygıt yazılımı kontrolü

## Dosya Ağacı (File Tree)
- `LICENSE` (blob)
- `README.md` (blob)
- `guncelle.sh` (blob)

## README İçeriği
# Ubuntu Tam Güncelleme

Ubuntu'yu tek komutla baştan sona günceller.

## Kullanım

```bash
git clone https://github.com/gok8lp/ubuntu-tam-guncelle.git && cd ubuntu-tam-guncelle
./guncelle.sh
```

`sudo` parolası bir kez sorulur.

## Ne yapar

| Adım | Komut |
| --- | --- |
| Paket listelerini yeniler | `apt-get update` |
| Tüm paketleri yükseltir (çekirdek dahil) | `apt-get full-upgrade` |
| Artık paketleri ve eski önbelleği temizler | `apt-get autoremove --purge`, `autoclean` |
| Snap uygulamalarını günceller | `snap refresh` |
| Flatpak uygulamalarını günceller, kullanılmayanları siler | `flatpak update`, `flatpak uninstall --unused` |
| Aygıt yazılımı güncellemelerini listeler (kurmaz) | `fwupdmgr get-updates` |

Sonunda yeniden başlatma gerekip gerekmediğini ve hangi paketlerin istediğini söyler.

## Güvenlik notları

- Senin değiştirdiğin yapılandırma dosyaları korunur (`--force-confold`); paketin yeni sürümü yanına `.dpkg-dist` olarak yazılır.
- Aygıt yazılımı (BIOS vb.) otomatik kurulmaz, yalnızca listelenir. Kurmak için: `fwupdmgr update`.

## Lisans

[MIT](LICENSE)



## İlgili Mimari Sayfaları
- [[github-repolar-katalogu]]
- [[sunucu-ve-github-commit-gecmisi]]
- [[pc-masaustu-hyprland-ve-gnome-araclari]]
- [[koharia-reader-ve-manga-ekosistemi]]
