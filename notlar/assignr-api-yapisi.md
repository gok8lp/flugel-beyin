# assignr API Yapısı ve Birleşik Maç Anahtarı

Bağlantılar: [[HARITA]] · [[hafiza]] · [[kararlar]] · [[assignr-ve-ankarabasket-kaynaklari]] · [[yerel-arsiv-ve-senkronizasyon]] · [[01 - Veri Kaynakları ve API Analizi]]

## Uç Noktalar
- Hakem atamaları: `https://assignr.immensus.io/api/public/assignments/recent-weeks`
- Masa görevlileri: `https://assignr.immensus.io/api/public/assignments/recent-weeks/masa`
- Salonlar ve koordinatlar: `https://assignr.immensus.io/api/public/venues`

## Neden Birleşik Anahtar (`matchNumber|date|time`)?
- `assignr` yalnızca son 2 haftanın verisini döndürür ve ertelenen bir maçı aynı `matchNumber` ile ikinci kez yayınlayabilir (`ANK-U16E-C-2026-153`).
- Bu nedenle `MacAnahtari.olustur(matchNumber, date, time)` ile `matchNumber|date|time` birincil anahtar olarak kullanılır ve `Birlestirici` eski kaydı silmeden `yerineGelen` alanıyla yeni maça bağlar.
