---
title: GitHub Depo Analizi — gok8lp/c-process-tree
sources: raw/github/c-process-tree.md, raw/github/00-github-envanteri.md, raw/github/01-tum-repolar-commit-gecmisi.md
updated: 2026-11-11
---

# GitHub Depo Analizi: `gok8lp/c-process-tree`

Üst Katalog: [[github-repolar-katalogu]] · [[sunucu-ve-github-commit-gecmisi]] · [[duduk-genel-bakis]] · [[flugelserver-genel-mimari]]

> "GitHub Repo: gok8lp/c-process-tree" - raw/github/c-process-tree.md

> "gok8lp GitHub Depoları Tam Commit Geçmişi" - raw/github/01-tum-repolar-commit-gecmisi.md

## Son Commit Geçmişi (`gok8lp/c-process-tree`)
- `ab21c8a` (2026-10-22): refactor: name process exercise clearly and fix child result collection
- `7b718ea` (2025-07-27): Update asdasdsa.c
- `333e67d` (2025-07-27): Add files via upload
- `36ead69` (2025-07-27): Initial commit

## Dosya Ağacı ve README Özeti
# GitHub Repo: gok8lp/c-process-tree

- **URL:** https://github.com/gok8lp/c-process-tree
- **Görünürlük:** Açık (Public)
- **Ana Dil:** C
- **Son Güncelleme:** 2026-10-22T22:53:38Z
- **Açıklama:** C ve POSIX fork ile süreç ağacı, dosya iletişimi ve ebeveyn/çocuk süreç alıştırması.

## Dosya Ağacı (File Tree)
- `README.md` (blob)
- `process_tree.c` (blob)

## README İçeriği
# C Process Tree

C ve POSIX süreçleri üzerine küçük bir öğrenme projesi.
A small learning exercise about process trees using `fork()` and file-based communication.

`process_tree.c`, iki alt süreç oluşturarak bir ağaç kurar. Yaprak süreçler rastgele bir sayıyı
PID adını taşıyan `.txt` dosyasına yazar; ebeveyn süreçler çocukların dosyalarını okuyup toplamayı dener.

## Derleme

Linux veya POSIX `fork()` desteği olan bir ortam ve C derleyicisi gerekir.

```bash
gcc -std=c11 -Wall -Wextra process_tree.c -o process_tree
mkdir -p output
cd output
../process_tree
```

Çalışma dizininde PID isimli dosyalar oluşur; örnek bu yüzden ayrı `output` dizininde çalıştırılır.

## Öğrenilecek konular ve mevcut sınırlar

`fork`, PID, ebeveyn/çocuk süreç, `wait` ve dosya üzerinden veri paylaşımı.
Bu düzenlemede çocuk dosyasının doğru PID ile okunması ve iki çocuğun `waitpid` ile beklenmesi düzeltildi.
Dosya açma/fork hataları hâlâ tam işlenmez; örnek sabit derinlikli bir ders denemesidir.
Üretim amaçlı süreç yönetimi örneği olarak değerlendirilmemelidir.



## İlgili Mimari Sayfaları
- [[github-repolar-katalogu]]
- [[sunucu-ve-github-commit-gecmisi]]
- [[pc-masaustu-hyprland-ve-gnome-araclari]]
- [[koharia-reader-ve-manga-ekosistemi]]
