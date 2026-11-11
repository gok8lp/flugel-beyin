---
title: assignr, ankarabasket ve TBF Veri Kaynakları
sources: raw/veri-kaynaklari.md, raw/devir.md
updated: 2026-11-11
---

# assignr, ankarabasket ve TBF Veri Kaynakları

[[duduk-genel-bakis]] uygulaması üç bağımsız veri kaynağını birleştirir.

> "Tüm uçlar giriş gerektirmeden, yalnız `GET` ile denendi (toplam ~200 istek, host başına ≤ 1-2 istek/sn)." - raw/veri-kaynaklari.md

## 1. assignr.immensus.io Uçları

- Hakem atamaları: `https://assignr.immensus.io/api/public/assignments/recent-weeks`
- Masa görevlileri: `https://assignr.immensus.io/api/public/assignments/recent-weeks/masa`
- Salonlar ve koordinatlar: `https://assignr.immensus.io/api/public/venues`

> "Yalnız son 2 haftayı veriyor; geçmiş haftaları almanın yolu yok. Bu yüzden uygulama her çekilen veriyi kendi arşivine eklemeli. Hiçbir şey silinmeyecek; istatistikler bu arşivden hesaplanacak." - raw/devir.md

> "matchNumber tek başına benzersiz değil, çünkü ertelenen maç iki kez gelebiliyor. Anahtar olarak matchNumber+date+time kullan." - raw/devir.md

Bu arşivleme davranışı [[yerel-arsiv-ve-senkronizasyon]] içinde detaylandırılmıştır.

## 2. ankarabasket.org.tr Ana Sayfa `days` JSON ve robots.txt Kuralı

> "ankarabasket'in /api yolu robots.txt'te yasaklı. Lig ve takım kataloğunu çalışma sırasında oradan çekme; samples/'taki season-teams verisini uygulamaya gömülü katalog olarak koy." - raw/devir.md

Ana sayfadaki Next.js RSC Flight (`self.__next_f.push`) verisi içindeki `days` dizisi, `code == matchNumber` üzerinden yakın maçların skorlarını verir.

## 3. TBF WebAPI (`miniappapi.tbf.org.tr`)

TBF uçları sezonun tüm maçlarını ve puan durumunu sağlar ancak iki önemli şema tuzağı vardır:

> "Kimlik alanları kimi zaman "22328.0" biçiminde geliyor; sayıyı Double olarak oku." - raw/devir.md

> "Oynanmamış maçlarda matchDate tarih yerine "10. Hafta" gibi bir metin olabiliyor." - raw/devir.md

TBF maçlarının `assignr` kayıtlarıyla nasıl bağlandığı [[tbf-eslestirme-algoritmasi]] sayfasında açıklanmıştır.
