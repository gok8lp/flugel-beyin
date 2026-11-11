---
title: 2026-2027 Hakem Ücret Tarifesi ve Kazanç Hesabı
sources: raw/ucret-tarifesi-2026-2027.txt, raw/devir.md
updated: 2026-11-11
---

# 2026-2027 Hakem Ücret Tarifesi ve Kazanç Hesabı

[[duduk-genel-bakis]] uygulamasındaki kazanç modülü (`KazancHesaplayici.kt`), kullanıcının uygulama içinden düzenleyebildiği `UcretTablosu` üzerinden çalışır.

> "Hesap kullanıcının düzenleyebildiği bir ücret tablosuna göre yapılacak, tutarlar koda gömülmeyecek." - raw/devir.md

> "Başlangıç değerleri docs bölüm 6'dan: il içi altyapı hakem 1.700 TL, masa görevlisi 850 TL; büyükler kategorisinde erkek 3.250 TL, kadın 2.600 TL. Bu tarife özel müsabakalar için." - raw/devir.md

## Resmi 2026-2027 Özel Müsabaka Tarifesi (`raw/ucret-tarifesi-2026-2027.txt`)

> "Karşılaşma ücreti hesaplanmaz, seans ücreti alınır. Bir seans en fazla 6 saat olabilir." - raw/ucret-tarifesi-2026-2027.txt

- **İl İçi Altyapı / Kurum / Okul (`AGL`, `OKUL`):** Hakem `1.700 TL`, Masa Görevlisi `850 TL`, Temsilci `1.100 TL`. (MEB / Valilik 18 yaş altı turnuvalarında 1/2 oranı uygulanabilir: `850 TL`).
- **Ticari / Sponsorlu Büyükler (`ABL`, `AA`):** Erkek Hakem `3.250 TL`, Kadın Hakem `2.600 TL`, Masa Görevlisi `1.100 TL`.
- **Federasyon Faaliyetleri:** `BSL` Hakem `14.000 TL`, `KBSL` `9.500 TL`, `TBL` `8.500 TL`, `TKBL` / `TB2L` `5.000 TL`, `BGL` / `EBBL` / `KBBL` `4.250 TL`.

## `BÖLGE` Yerel Lig Ücreti Kuralı

> "BÖLGE ligi ücreti hiçbir yerde bulunamadı. Bu satırlar boş başlasın ve "ücret tanımsız" diye işaretlensin; sıfır sayılmasın." - raw/devir.md

Bu kural gereği [[yerel-arsiv-ve-senkronizasyon]] arşivindeki `BÖLGE` maçları varsayılan olarak `tutarTl = null` ("ücret tanımsız") döner ve toplam kazanca `0 TL` olarak karıştırılmaz; kullanıcı kendi bordrosundaki tutarı [[android-arac-zinciri-ve-mimari]] içindeki Ücret Tablosu ekranından girebilir.
