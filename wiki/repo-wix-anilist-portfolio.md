---
title: GitHub Depo Analizi — gok8lp/wix-anilist-portfolio
sources: raw/github/wix-anilist-portfolio.md, raw/github/00-github-envanteri.md, raw/github/01-tum-repolar-commit-gecmisi.md
updated: 2026-11-11
---

# GitHub Depo Analizi: `gok8lp/wix-anilist-portfolio`

Üst Katalog: [[github-repolar-katalogu]] · [[sunucu-ve-github-commit-gecmisi]] · [[duduk-genel-bakis]] · [[flugelserver-genel-mimari]]

> "GitHub Repo: gok8lp/wix-anilist-portfolio" - raw/github/wix-anilist-portfolio.md

> "gok8lp GitHub Depoları Tam Commit Geçmişi" - raw/github/01-tum-repolar-commit-gecmisi.md

## Son Commit Geçmişi (`gok8lp/wix-anilist-portfolio`)
- `d292048` (2026-10-22): docs: clarify project purpose, setup and repository naming
- `e35a6eb` (2025-07-11): Initial commit

## Dosya Ağacı ve README Özeti
# GitHub Repo: gok8lp/wix-anilist-portfolio

- **URL:** https://github.com/gok8lp/wix-anilist-portfolio
- **Görünürlük:** Açık (Public)
- **Ana Dil:** JavaScript
- **Son Güncelleme:** 2026-10-22T22:53:45Z
- **Açıklama:** Wix Velo kişisel site denemesi; AniList verisi ve sayfa kodları. Tam site dışa aktarımı değildir.

## Dosya Ağacı (File Tree)
- `.eslintrc.json` (blob)
- `.gitignore` (blob)
- `README.md` (blob)
- `package.json` (blob)
- `src` (tree)
- `src/backend` (tree)
- `src/backend/README.md` (blob)
- `src/backend/permissions.json` (blob)
- `src/pages` (tree)
- `src/pages/About.a4nu4.js` (blob)
- `src/pages/Contact.u9b9y.js` (blob)
- `src/pages/Hobies.ch7ux.js` (blob)
- `src/pages/Home.k42v9.js` (blob)
- `src/pages/Projects.ctbjf.js` (blob)
- `src/pages/README.md` (blob)
- `src/pages/masterPage.js` (blob)
- `src/public` (tree)
- `src/public/README.md` (blob)
- `wix.config.json` (blob)
- `wix.lock` (blob)

## README İçeriği
# Wix AniList Portfolio

Wix Velo üzerinde kişisel site ve AniList verisi gösterme denemesi.
Page-code experiments for a Wix portfolio with AniList integration.

Bu depo **tam bir statik web sitesi dışa aktarımı değildir**. Sayfa tasarımları ve Wix editöründeki öğeler
Wix tarafında bulunur; yalnızca bu dosyaları açmak siteyi çalıştırmaz.

## İçerik

| Yol | Görev |
| --- | --- |
| `src/pages/masterPage.js` | AniList GraphQL sorgusu ve ortak sayfa denemesi |
| `src/pages/Hobies.ch7ux.js` | Hobi sayfasındaki AniList denemesi |
| `src/pages/*.js` | Diğer sayfaların Velo kodları ve başlangıç şablonları |
| `src/backend/` | Wix arka uç izinleri |
| `wix.config.json` | Bağlı Wix projesi yapılandırması |

## Geliştirme

Bağlı Wix sitesine erişim, Node.js ve projenin desteklediği Wix CLI gerekir.
`package.json` içindeki `dev` ve `lint` komutları kullanılır. Bağımlılık kurulumu `wix sync-types`
çağıran bir postinstall işlemi içerir ve Wix hesabına/siteye erişim gerektirebilir.

```bash
npm install
npm run dev
```

Bu komutlar site erişimi olan geliştirme ortamı içindir; GitHub Pages üzerinde çalışmaz.

## Mevcut durum

Öğrenme prototipidir. Bazı sayfalar başlangıç şablonudur; hobi sayfasında import satırı callback içine
konulduğundan düzeltilmeden standart JavaScript olarak ayrıştırılamaz. Site çalışır/dağıtıma hazır diye sunulmaz.
AniList kullanıcı adını, sorgu alanlarını ve Wix öğe kimliklerini kendi sayfana göre uyarlamalısın.
Kişisel statik site ayrı depodadır: [gok8lp.github.io](https://github.com/gok8lp/gok8lp.github.io).



## İlgili Mimari Sayfaları
- [[github-repolar-katalogu]]
- [[sunucu-ve-github-commit-gecmisi]]
- [[pc-masaustu-hyprland-ve-gnome-araclari]]
- [[koharia-reader-ve-manga-ekosistemi]]
