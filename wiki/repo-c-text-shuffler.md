---
title: GitHub Depo Analizi — gok8lp/c-text-shuffler
sources: raw/github/c-text-shuffler.md, raw/github/00-github-envanteri.md, raw/github/01-tum-repolar-commit-gecmisi.md
updated: 2026-11-11
---

# GitHub Depo Analizi: `gok8lp/c-text-shuffler`

Üst Katalog: [[github-repolar-katalogu]] · [[sunucu-ve-github-commit-gecmisi]] · [[duduk-genel-bakis]] · [[flugelserver-genel-mimari]]

> "GitHub Repo: gok8lp/c-text-shuffler" - raw/github/c-text-shuffler.md

> "gok8lp GitHub Depoları Tam Commit Geçmişi" - raw/github/01-tum-repolar-commit-gecmisi.md

## Son Commit Geçmişi (`gok8lp/c-text-shuffler`)
- `5d5d5b0` (2026-10-22): docs: clarify project purpose, setup and repository naming
- `5b13d75` (2025-01-23): Password Generator
- `07f37c5` (2025-01-23): Delete Password Randomizer
- `4eee389` (2025-01-20): Create Password Randomizer
- `a2c8e47` (2025-01-20): Initial commit

## Dosya Ağacı ve README Özeti
# GitHub Repo: gok8lp/c-text-shuffler

- **URL:** https://github.com/gok8lp/c-text-shuffler
- **Görünürlük:** Açık (Public)
- **Ana Dil:** C
- **Son Güncelleme:** 2026-10-22T22:53:52Z
- **Açıklama:** C ile girilen metnin karakterlerini rastgele sıralayan küçük öğrenme projesi.

## Dosya Ağacı (File Tree)
- `README.md` (blob)
- `shuffle_text.c` (blob)

## README İçeriği
# C Text Shuffler

Girilen metnin karakterlerinin sırasını rastgele değiştiren küçük C alıştırması.
A C learning exercise that shuffles the characters of an input word.

Bu program yeni ve bağımsız karakterlerden parola üretmez; kullanıcıdan aldığı karakterleri farklı sıraya koyar.
Bu yüzden depo adı yaptığı işi anlatacak şekilde düzenlenmiştir.

## Derleme ve kullanım

```bash
gcc -std=c11 -Wall -Wextra shuffle_text.c -o shuffle_text
./shuffle_text
```

Bir kelime girilir; program rastgele indeks sırasıyla aynı karakterleri yeniden yazar.
Karakterler girişte tekrar ediyorsa çıktıda da tekrar edebilir.

## Öğrenme konusu ve sınırlar

Dizi, string uzunluğu, rastgele indeks ve kullanılan indeksleri kontrol etme.
Kod bir ilk denemedir: mevcut `scanf("%s", ...)` uzun girdiyi sınırlamaz; bellek taşması riski vardır.
`rand()` kriptografik rastgelelik sağlamaz. Gerçek parola üretimi için kullanılmamalıdır.



## İlgili Mimari Sayfaları
- [[github-repolar-katalogu]]
- [[sunucu-ve-github-commit-gecmisi]]
- [[pc-masaustu-hyprland-ve-gnome-araclari]]
- [[koharia-reader-ve-manga-ekosistemi]]
