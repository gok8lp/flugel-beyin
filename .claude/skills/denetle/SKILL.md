---
name: denetle
description: Vault ve wiki sayfalarındaki çelişkileri, eskimiş iddiaları, yetim sayfaları ve sayfası olmayan kavramları tespit eden salt-okunur denetim becerisi (yalnızca rapor üretir, otomatik düzeltme yapmaz).
tur: beceri
etiketler:
  - beceri
  - denetle
  - lint
  - kalite
  - rapor
olusturma: 2026-11-11
guncelleme: 2026-11-11
---

# Bilgi Tabanı Denetleme Becerisi (`/denetle`)

> Üst bağlantı: [[HARITA]] · Odak: [[simdi]] · Bağlam: [[hafiza]] · Kararlar: [[kararlar]] · Kurallar: [[kurallar/notlar]] · [[kurallar/projeler]]

## Çalışma Kuralı (Yalnız Rapor, Düzeltme Yok!)
`/denetle` becerisi **salt okunur (read-only)** bir kalite ve tutarlılık denetimidir. Hiçbir dosyayı doğrudan düzenlemez (`Edit` veya `Write` yapmaz); yalnızca bulguları yapılandırılmış bir rapor olarak kullanıcıya sunar.

## Denetim Adımları ve Kontrol Listesi

### 1. Yapısal Denetim (`brain.py status` ve `brain.py lint`)
- `python3 brain.py status` ve `python3 brain.py lint` komutlarını çalıştırarak:
  - İşlenmemiş (`NEW`) veya ingest sonrası değişmiş (`MODIFIED`) `raw/` kaynaklarını ve bunlara bağlı bayat `wiki/` sayfalarını,
  - Eksik frontmatter alanlarını, kırık `[[wikilink]]` bağlantılarını, kalmış `TODO` notlarını ve kaynakta birebir geçmeyen alıntıları tespit et.

### 2. Çelişki Tespiti (Contradictions)
- `wiki/`, `notlar/`, `projeler/` ve kök dosyalar ([[HARITA]], [[simdi]], [[hafiza]], [[kararlar]]) arasında aynı konu hakkında birbiriyle çelişen tarih, saat, salon, IP/port, sürüm numarası veya mimari iddiaları (ör. taslak sınav saatleri, konteyner durumları, depo görünürlükleri) karşılaştır.

### 3. Eskimiş İddialar ve Bayat Projeler (Stale Claims)
- Geçmişte kalmış sınav/maç tarihlerini hâlâ "gelecek" gibi anlatan ifadeleri tespit et.
- [[kurallar/projeler]] uyarınca `projeler/` altında 14 günden uzun süredir güncellenmeyen ancak `durum: aktif` görünen projeleri listele.

### 4. Yetim Sayfalar (Orphan Pages)
- [[HARITA]] (`HARITA.md`), [[wiki/index]] (`wiki/index.md`) veya diğer notlar tarafından hiçbir gelen bağlantısı (`[[wikilink]]`) bulunmayan yetim sayfaları belirle.

### 5. Sayfası Olmayan Kavramlar (Missing Concept Pages)
- Metinlerde sıkça geçen veya `[[olmayan-sayfa]]` şeklinde referans verilen ancak henüz `wiki/` ya da `notlar/` altında müstakil bir dosyası açılmamış önemli kavramları listele.

## Çıktı Biçimi
Raporu şu 5 başlık altında madde madde ve dosya/satır referanslarıyla sun:
1. **Linter ve Kaynak Durumu (`brain.py`)**
2. **Tespit Edilen Çelişkiler**
3. **Eskimiş İddialar ve >14 Gün Bayat Projeler**
4. **Yetim Sayfalar**
5. **Sayfası Olmayan / Eksik Kavramlar ve Önerilen Eylemler**

## İlgili Sayfalar ve Bağlantılar
- **Kök ve Harita:** [[HARITA]] · [[simdi]] · [[hafiza]] · [[kararlar]] · [[dersler]]
- **Kurallar:** [[kurallar/notlar]] · [[kurallar/projeler]] · [[kurallar/kisiler]] · [[kurallar/guvenlik]]
- **Wiki ve Notlar:** [[wiki/ikinci-beyin-sistemi]] · [[wiki/index]] · [[wiki/hot]] · [[notlar/assignr-api-yapisi]] · [[flugelserver-genel-mimari]]
- **Projeler:** [[projeler/duduk]] · [[projeler/okul-guz-2026]] · [[projeler/hakemlik]] · [[projeler/flugel-sunucu-ve-akis]]

> Kaynak: `/home/flugel/Projects/prompt-obsidian-ikinci-beyin-sunucu.md`
