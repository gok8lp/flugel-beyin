---
title: Android Araç Zinciri, Cam Arayüz ve Sunucu Mimarisi
sources: raw/build.md, raw/devir.md
updated: 2026-11-11
---

# Android Araç Zinciri, Cam Arayüz ve Sunucu Mimarisi

[[duduk-genel-bakis]] uygulaması modern Android araç zinciriyle derlenir ve `flugelserver` üzerindeki Docker arka ucu ile [[yerel-arsiv-ve-senkronizasyon]] katmanını besler.

> "Gradle 9.8.0, AGP 9.4.1, Kotlin 2.3.21, Compose BOM 2026.09.00." - raw/devir.md

> "compileSdk ve targetSdk 37, minSdk 26." - raw/devir.md

## Arayüz ve Glance Widget

> "Alt tarafta Apple tarzı, içeriğin üstünde yüzen, saydam ve arkasını bulanıklaştıran bir gezinme çubuğu olsun. Android 12 ve üstünde gerçek bulanıklık kullan; daha eski sürümlerde yarı saydam renk yeterli." - raw/devir.md

- **5 Ana Sekme:** Maçlarım, Fikstür, Puan, Hakemler, Ben/İstatistik.
- **Alt Ekranlar:** Maç Ayrıntı ekranı, [[hakem-ucret-tarifesi-2026-2027]] düzenleme ekranı, Ayarlar ekranı.
- **Glance Widget:** `SiradakiMacWidget` ana ekranda sıradaki maçı gösterir.

## Sunucu Arka Ucu ve Bağlantı Zinciri

[[assignr-ve-ankarabasket-kaynaklari]] ve [[tbf-eslestirme-algoritmasi]] verileri `flugelserver` üzerinde çalışan `duduk-server` (`127.0.0.1:18420`) tarafından saatlik çekilip arşivlenir:
1. **Cloudflare Tunnel:** `https://duduk.gokalpgoksu.com`
2. **Tailscale Serve:** `https://flugelserver.tail42f1f4.ts.net:18443`
3. **Doğrudan Kaynaklar:** Yedek olarak cihazdan doğrudan çekim.

Bilgi tabanı doğrulaması [[ikinci-beyin-sistemi]] ile yürütülür.
