---
tur: proje
etiketler:
  - proje
  - android
  - kotlin
  - manga
  - epub
  - komga
  - kavita
  - suwayomi
durum: aktif
olusturma: 2026-11-11
guncelleme: 2026-11-11
---

# Flugel Manga (`koharia-reader`) — Kişisel Android Manga ve Kitap Okuyucu

> Üst bağlantı: [[HARITA]] · Odak: [[simdi]] · Bağlam: [[hafiza]] · Kararlar: [[kararlar]] · Sorumlu: [[kisiler/ahmet-gokalp-goksu]]

## Genel Bakış ve Amaç
**Flugel Manga** (`gok8lp/koharia-reader`), Koharia ve Mihon üzerine inşa edilmiş kişisel Android manga, çizgi roman, EPUB/PDF ve hafif roman (light novel) okuyucu uyarlamasıdır. `flugelserver` üzerindeki **Komga**, **Kavita**, **Suwayomi** ve **Tranga** servisleriyle ve cihazdaki yerel kitaplıkla bütünleşik çalışacak biçimde özelleştirilmiştir.

- **GitHub Deposu:** `https://github.com/gok8lp/koharia-reader` (Özel / Private, Kotlin)
- **Son Güncelleme:** `2026-11-04T19:46:59Z` (Son commit: `2026-10-31`)
- **Temel Özellikler:**
  - **Çift Sunucu Sekmesi:** Çizgi roman / manga için Komga ve kitaplar / EPUB için Kavita bağlantılarının aynı anda ayrı sekmelerde çalışması (`37eb2d4`).
  - **Sunucu Entegrasyonu:** Suwayomi ve ağ depolama desteği (`c28ad51`), Komga `/sse/v1/events` canlı etkinlik yolu (`5936816`), Daha Fazla menüsünden doğrudan Tranga ile manga indirme ve kütüphaneye ekleme kısayolları (`04d8e34`).
  - **Güvenli Tailscale Yapılandırması:** Gömülü API anahtarları kaldırılarak Tailscale adresleri üzerinden tak-çalıştır (plug-and-play) güvenli bağlantı ve imzalı güncelleme akışı (`75f70ad`, `715564b`).
  - **Okuyucu İyileştirmeleri:** LAN üzerinden EPUB/PDF roman yükleme düzeltmesi (`58c9741`), yerel Markdown okuma ve başlık gezinmesi (`73a0d2d`), E-Ink ekran uyumu (`0f287cd`, `e62b167`).

## Mevcut Durum (11 Kasım 2026)
Proje **aktif** durumdadır (son commit 31 Ekim 2026; 14 günlük güncellik eşiği içindedir). Gömülü sunucu anahtarları temizlenmiş, Tailscale ve LAN üzerinden Komga/Kavita/Suwayomi bağlantıları kararlı hale getirilmiştir.

## Sıradaki Adımlar
- [ ] Tailscale üzerinden Komga SSE (`/sse/v1/events`) ve Kavita okuma ilerlemesi eşitlemesini uzun süreli oturumlarda gözlemlemek.
- [ ] Yeni EPUB ve hafif roman (light novel) arşivlerinde sayfa geçiş ve içindekiler (TOC) performansını doğrulamak.
- [ ] İmzalı kişisel APK güncellemelerini GitHub Actions iş akışı (`flugel-test-apk.yml`) üzerinden sürdürmek.

## Öne Çıkan Commit Geçmişi
- `75f70ad` (2026-10-31): `fix(flugel): use Tailscale addresses and drop embedded server API keys`
- `58c9741` (2026-10-31): `fix(reader,flugel): fix LAN EPUB/PDF novel loading and make Flugel setup plug-and-play`
- `715564b` (2026-10-29): `Flugel: secure personal build, reconnects and signed updates`
- `2ed40ac` (2026-10-28): `style: apply spotless formatting to LibraryConnectionProfilesScreen (#1)`
- `df5d324` (2026-10-22): `docs: clarify project purpose, setup and repository naming`
- `04d8e34` (2026-10-18): Daha Fazla menüsüne Manga indir (Tranga) ve Kütüphaneye ekle (yükleme) kısayolları
- `37eb2d4` (2026-10-18): Kitaplar sekmesi için ayrı bağlantı: Komga ve Kavita aynı anda (Çizgi roman / Kitaplar sekmeleri)
- `5936816` (2026-10-18): Komga SSE yolunu düzelt (`/sse/v1/events`) ve test APK sürüm etiketini parametre yap
- `761c2fa` (2026-10-17): `Prepare Flugel Manga test APK and server setup`
- `c28ad51` (2026-10-06): Suwayomi ve ağ depolama entegrasyonu, paylaşımlı okuma işlevleri

## İlgili Sayfalar ve Bağlantılar
- **Harita ve Kök:** [[HARITA]] · [[simdi]] · [[hafiza]] · [[kararlar]]
- **İlgili Projeler ve Kişiler:** [[projeler/flugel-sunucu-ve-akis]] · [[kisiler/ahmet-gokalp-goksu]]
- **Wiki Sayfaları:**
  - [[wiki/repo-koharia-reader]]
  - [[wiki/koharia-reader-ve-manga-ekosistemi]]
  - [[wiki/flugelserver-anime-manga-lightnovel-arsivi]]
  - [[wiki/flugelserver-docker-uygulamalari]]
  - [[wiki/android-arac-zinciri-ve-mimari]]
- **Bilgi Notları:**
  - [[notlar/cloudflare-ve-tailscale-baglanti-zinciri]]
  - [[flugelserver-genel-mimari]]

> Kaynaklar: `raw/github/00-github-envanteri.md`, `raw/github/01-tum-repolar-commit-gecmisi.md`, `raw/github/koharia-reader.md`
