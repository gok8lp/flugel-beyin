---
title: GitHub Depo Analizi — gok8lp/k380s-ubuntu-fn
sources: raw/github/k380s-ubuntu-fn.md, raw/github/00-github-envanteri.md, raw/github/01-tum-repolar-commit-gecmisi.md
updated: 2026-11-11
---

# GitHub Depo Analizi: `gok8lp/k380s-ubuntu-fn`

Üst Katalog: [[github-repolar-katalogu]] · [[sunucu-ve-github-commit-gecmisi]] · [[duduk-genel-bakis]] · [[flugelserver-genel-mimari]]

> "GitHub Repo: gok8lp/k380s-ubuntu-fn" - raw/github/k380s-ubuntu-fn.md

> "gok8lp GitHub Depoları Tam Commit Geçmişi" - raw/github/01-tum-repolar-commit-gecmisi.md

## Son Commit Geçmişi (`gok8lp/k380s-ubuntu-fn`)
- `17a9f17` (2026-10-29): README: klonlama adresini ekle
- `6cc71de` (2026-10-29): MIT lisansı ekle
- `a2d6f7c` (2026-10-29): README: tuş haritası ve kullanım
- `3c1b24d` (2026-10-29): Tek komutla kurma ve kaldırma betikleri
- `c403efc` (2026-10-29): Solaar tuş kuralları: F4-F9 için GNOME karşılıkları

## Dosya Ağacı ve README Özeti
# GitHub Repo: gok8lp/k380s-ubuntu-fn

- **URL:** https://github.com/gok8lp/k380s-ubuntu-fn
- **Görünürlük:** Açık (Public)
- **Ana Dil:** Shell
- **Son Güncelleme:** 2026-10-29T21:49:38Z
- **Açıklama:** Logitech Pebble Keys 2 K380s üst sıra tuşlarını Ubuntu'da (GNOME, Wayland) Solaar ile tam işlevli yapar

## Dosya Ağacı (File Tree)
- `LICENSE` (blob)
- `README.md` (blob)
- `kaldir.sh` (blob)
- `kur.sh` (blob)
- `rules.yaml` (blob)

## README İçeriği
# Pebble Keys 2 K380s · Ubuntu Fn Tuşları

Logitech Pebble Keys 2 K380s klavyenin üst sıra tuşlarını Ubuntu'da (GNOME, Wayland) eksiksiz çalıştırır.
Logitech'in Logi Options+ uygulaması Linux'ta yok; bu proje aynı işi açık kaynak [Solaar](https://github.com/pwr-Solaar/Solaar) ile yapar.

## Kurulum

```bash
git clone https://github.com/gok8lp/k380s-ubuntu-fn.git && cd k380s-ubuntu-fn
./kur.sh
```

Klavye Bluetooth ile bağlı olmalı. Betik `sudo` ister (Solaar kurulumu ve aygıt izinleri için).

## Tuş haritası

Harita klavyenin kendisinden (`solaar show`) okunmuştur.

| Tuş | Klavyedeki işlev | Ubuntu'da |
| --- | --- | --- |
| Fn + Esc | Fn Lock | Medya tuşları ↔ F1–F12 |
| F1 / F2 / F3 | Easy-Switch | 1., 2., 3. cihaza geçer |
| F4 | Show Desktop | Masaüstünü gösterir (Super+D) |
| F5 | Search | Etkinlikler araması (Super) |
| F6 | Back | Geri (Alt+Sol) |
| F7 | Dictation | Mikrofonu kapatır/açar (Linux'ta dikte yok) |
| F8 | Emoji | Emoji seçici (Super+.) |
| F9 | Screen Capture | GNOME ekran görüntüsü aracı (Print) |
| F10 – F12, sonraki tuş | Oynat/Duraklat, Sessiz, Ses −, Ses + | Aynı |
| Fn + ← → ↑ ↓ | Home, End, PgUp, PgDn | Aynı |

F1–F12'nin varsayılan olarak F tuşu gibi çalışması için Solaar penceresinde **Swap Fx function** ayarını kapat.

## Nasıl çalışır

- `kur.sh` Solaar'ı kurar, `hidraw` ve `uinput` izinlerini yeniler.
- F4–F9 tuşlarını Solaar'a yönlendirir (`divert-keys`), [`rules.yaml`](rules.yaml) bu tuşları GNOME kısayollarına çevirir.
- Solaar oturum açılışında arka planda başlar. **Solaar kapalıyken F4–F9 çalışmaz.**

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
