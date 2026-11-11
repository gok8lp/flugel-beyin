---
tur: kural
etiketler:
  - kural
  - projeler
  - takip
kapsam: "projeler/**"
olusturma: 2026-11-11
guncelleme: 2026-11-11
---

# Proje Sayfaları Kuralları (`projeler/**`)

> Üst bağlantı: [[HARITA]] · Odak: [[simdi]] · Bağlam: [[hafiza]] · Kararlar: [[kararlar]] · Şablon: [[sablonlar/proje]]

## Kapsam
Bu kural dosyası `projeler/**` dizini altındaki tüm proje takip dosyalarının oluşturulmasında, güncellenmesinde ve haftalık gözden geçirilmesinde geçerlidir.

## Zorunlu Alanlar ve Bölümler
1. **YAML Frontmatter:**
   - `tur: proje`
   - `etiketler`: `proje` ve ilgili teknoloji/alan etiketleri
   - `durum`: `aktif` | `beklemede` | `arsiv-beklemede` | `tamamlandi`
   - `olusturma`: `YYYY-AA-GG`
   - `guncelleme`: `YYYY-AA-GG`
2. **Dosya Adlandırma:** Küçük harf, tireli ve Türkçe karaktersiz (`projeler/duduk.md`, `projeler/okul-guz-2026.md`).
3. **Gövde Bölümleri:**
   - **Genel Bakış ve Amaç:** Projenin ne yaptığı, varsa GitHub depo adresi ve teknoloji yığını.
   - **Mevcut Durum ve Son Güncelleme:** En son ne zaman ve hangi commit/adımla güncellendiği.
   - **Sıradaki Adım (`- [ ]`):** Somut, uygulanabilir bir sonraki görevler listesi.
   - **Bağlantılar (`[[wikilink]]`):** `[[HARITA]]`, `[[simdi]]`, `[[hafiza]]`, `[[kararlar]]` ile ilgili `[[kisiler/...]]`, `[[wiki/...]]` ve `[[notlar/...]]` sayfalarına bağlantılar.

## 14 Gün Bayatlık (Staleness) Kuralı
- Son güncelleme veya son commit tarihinden itibaren **14 günden uzun süredir** (`>14 gün`) güncellenmeyen projeler haftalık gözden geçirmede (`haftalik-gozden-gecirme` becerisi) **bayat / beklemede** olarak işaretlenir.
- Bayatlayan projeler için kullanıcıya:
  1. Yeni bir sıradaki adım belirlenmesi, veya
  2. Projenin `durum: arsiv-beklemede` statüsüne çekilerek `[[simdi]]` odak listesinden çıkarılması önerilir.

## İlgili Sayfalar
- **Kök ve Harita:** [[HARITA]] · [[simdi]] · [[hafiza]] · [[kararlar]]
- **Diğer Kurallar ve Şablonlar:** [[kurallar/kisiler]] · [[kurallar/notlar]] · [[kurallar/guvenlik]] · [[sablonlar/proje]]
- **Projeler:** [[projeler/duduk]] · [[projeler/flugel-manga]] · [[projeler/okul-guz-2026]] · [[projeler/hakemlik]] · [[projeler/flugel-sunucu-ve-akis]] · [[projeler/linux-masaustu-araclari]] · [[projeler/siber-guvenlik-ve-sistem-lab]] · [[projeler/web-portfolyo]]
- **Wiki ve Notlar:** [[wiki/ikinci-beyin-sistemi]] · [[wiki/github-repolar-katalogu]] · [[notlar/flugelserver-mimari-ozeti]]

> Kaynak: `/home/flugel/Projects/prompt-obsidian-ikinci-beyin-sunucu.md`
