---
title: Düdük Uygulaması Genel Bakış ve Gereksinimler
sources: raw/devir.md, raw/veri-kaynaklari.md
updated: 2026-11-11
---

# Düdük Uygulaması Genel Bakış ve Gereksinimler

**Düdük**, Ankara'da basketbol hakemi olan **Ahmet Gökalp Göksu** için geliştirilen kişisel bir Android maç, fikstür, puan durumu, hakem istatistiği ve kazanç takip uygulamasıdır.

> "Ben Ahmet Gökalp Göksu, Ankara'da basketbol hakemiyim. Atama verilerinde adım "AHMET GÖKALP GÖKSU" olarak geçiyor. Maçlarımı takip etmek için Maçkolik benzeri, bana özel bir Android uygulaması yaptırıyorum." - raw/devir.md

## Temel Modüller ve Bağlantılar

1. **Veri Kaynakları (`assignr`, `ankarabasket`, `TBF`):** Ayrıntılar için [[assignr-ve-ankarabasket-kaynaklari]] sayfasına bakın.
2. **TBF Maç ve Lig Eşleştirme Algoritması:** %97,9 isabetli bulanık eşleştirme için [[tbf-eslestirme-algoritmasi]] sayfasına bakın.
3. **Hiçbir Veriyi Silmeyen Yerel Arşiv ve Bildirimler:** [[yerel-arsiv-ve-senkronizasyon]] içinde açıklanmıştır.
4. **Ücret Tablosu ve Kazanç Hesabı:** [[hakem-ucret-tarifesi-2026-2027]] sayfasında resmi tarife ve `BÖLGE` kuralı yer alır.
5. **Android Araç Zinciri ve Sunucu Bağlantı Sırası:** [[android-arac-zinciri-ve-mimari]] sayfasında belgelenmiştir.
6. **Bilgi Tabanı Mimarisi:** [[ikinci-beyin-sistemi]] kurallarına göre doğrulanmaktadır.

## Canlı Skor ve Çeyrek Skoru Kuralı

> "Çeyrek skoru ve canlı skor hiçbir kaynakta yok. Uygulama bunları varmış gibi göstermesin." - raw/devir.md

## Bağlantı Öncelik Sırası

1. **Cloudflare Tunnel:** `https://duduk.gokalpgoksu.com`
2. **Tailscale Serve:** `https://flugelserver.tail42f1f4.ts.net:18443`
3. **Doğrudan Açık Kaynaklar:** `assignr.immensus.io`, `ankarabasket.org.tr`, `miniappapi.tbf.org.tr`

## Ekosistem Bağlantıları
- [[github-repolar-katalogu]]
- [[flugelserver-genel-mimari]]
- [[flugelserver-docker-uygulamalari]]
- [[flugelserver-uygulama-baglantilari]]
- [[ee313-ve-hakemlik-calisma-plani]]
