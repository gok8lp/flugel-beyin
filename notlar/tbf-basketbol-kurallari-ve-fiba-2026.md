---
tur: not
etiketler:
  - basketbol
  - hakemlik
  - tbf
  - fiba-2026
  - oyun-kurallari
  - duduk
  - assignr
  - ankarabasket
olusturma: 2026-11-11
guncelleme: 2026-11-11
---

# TBF Basketbol Oyun Kuralları, FIBA 2026 Farkları ve Hakemlik Hazırlık Rehberi

> **Üst Harita ve Kök Bağlantılar:** [[HARITA]] · [[hafiza]] · [[kararlar]] · [[dersler]] · [[simdi]]
> **İlgili Wiki Sayfaları:** [[wiki/repo-basketbol-kurallar-calisma]] · [[wiki/duduk-genel-bakis]] · [[wiki/hakem-ucret-tarifesi-2026-2027]] · [[wiki/assignr-ve-ankarabasket-kaynaklari]] · [[wiki/tbf-eslestirme-algoritmasi]] · [[wiki/ee313-ve-hakemlik-calisma-plani]]
> **İlgili Notlar:** [[notlar/gazi-eem-vize-takvimi-ve-ders-notlari]] · [[notlar/docker-ag-panel-ve-altyapi-yigini]] · [[notlar/docker-uygulama-baglanti-topolojisi]]
> **İlgili Projeler:** [[projeler/duduk-hakem-uygulamasi]] · [[projeler/basketbol-hakemligi]]

---

## 1. İşaretli Çalışma Kitabı ve FIBA 2026 Kural Farkları (`gok8lp/basketbol-kurallar-calisma`)

Özel GitHub deposu (`https://github.com/gok8lp/basketbol-kurallar-calisma`, commit `8465a3f`) ve `~/Downloads/Taildrop/_Ders_Disi/` altında hakemlik sınavları ve sezon içi tazeleme için üretilen **`Basketbol-Oyun-Kurallari-2024-isaretli-2026-farklari.pdf` (103 sayfa)** çalışma kopyası yer alır.

- **Üretim Hattı (`kaynak/build.py`, `marks.py`, `ek.html`):**
  ```bash
  python kaynak/build.py kurallar2024.pdf kaynak/ek.html cikti.pdf
  ```
- **Yapısı:**
  1. **Sayfa 1–97 (TBF *Basketbol Oyun Kuralları 2024*, v1.0a — 1 Ekim 2024 yürürlük):**
     - Sınav açısından kritik sayılar, süreler, ölçüler ve yaptırımlar **205 kırmızı vurgu** ile işaretlenmiştir.
     - 2026'da değişen kuralların bulunduğu sayfaların üst kısmına kırmızı **`"2026:"`** uyarısı eklenmiştir.
  2. **Sayfa 98–103 (EK — FIBA *Official Basketball Rules 2026*, v1.1 — 1 Ekim 2026 yürürlük):**
     - TBF'nin Türkçe 2024 kitabında henüz yer almayan **FIBA 2026** değişikliklerinin madde madde Türkçe özeti ve karşılaştırma tablolarını içerir.

---

## 2. FIBA 2026 Resmi Oyun Kuralları Değişiklikleri Özeti (Sayfa 98–103)

1 Ekim 2026 itibarıyla yürürlüğe giren FIBA *Official Basketball Rules 2026* (v1.1) ile TBF 2024 kitabı arasındaki temel farklar:

| Madde / Konu | TBF 2024 Karşılığı | FIBA 2026 (v1.1) Yeni Kural ve Farkı |
| :--- | :--- | :--- |
| **Madde Numarası Kayması (Yeni Md. 37 ve 38)** | Md. 37: Sportmenlik Dışı Faul (`Unsportsmanlike Foul`)<br>Md. 38: Diskalifiye Edici Faul | Terminoloji ve sınıflandırma yeniden yapılandırıldı: **Yeni Md. 37 (Oyunun Akışını Bozan Faul)** ve **Yeni Md. 38 (Kasti Faul)** ayrımı getirildi; Türkçe kitapta *"sportmenlik dışı"* geçen her yerin 2026 karşılığı ek tabloda eşleştirildi. |
| **Madde 15 — Atış Hali (*Act of Shooting*)** | Standart atış hali ve gather step tanımı | Atış halinin başlangıcı, **gather step** (topu kontrol altına alma adımı) ve pas/şut ayrımındaki temas anı kriterleri netleştirildi. |
| **Madde 24.2 — Dripling (*Dribbling*)** | Topun elden çıkması ve yürüme (traveling) | Dripling başlangıcında topun elden çıkışı ile pivot ayağının yerden kalkışı arasındaki sınır ve top kontrolü tanımları güncellendi. |
| **Madde 36 — Teknik Faul (*Kategori 1 / Kategori 2*)** | Tek tip Teknik Faul (Md. 36) | Teknik faullerde **Kategori 1** ve **Kategori 2** ayrımı ve davranışsal/idari ihlal derecelendirmesi tanımlandı. |
| **Madde 37 — Oyunun Akışını Bozan Faul** | Sportmenlik Dışı Faul (C1–C5 kriterleri) | Hızlı hücumu ve oyunun doğal akışını topa oynama niyeti olmaksızın kesen taktiksel temaslar **Oyunun Akışını Bozan Faul** altında yapılandırıldı. |
| **Madde 38 — Kasti Faul** | Sportmenlik Dışı Faul (sert/aşırı temas, C2/C3) | Aşırı, sert veya doğrudan oyuncuya yönelik kasti temaslar **Md. 38 Kasti Faul** olarak ayrıştırıldı. |
| **Hakem İşaretleri, Maç Kağıdı ve IRS / D.5.2** | 2024 hakem sinyalleri ve klasman kuralları | Yeni faul türleri için **yeni hakem el işaretleri**, maç kağıdı (scoresheet) kısaltmaları, **Ek D.5.2** takım sınıflandırma detayları ve **IRS (Instant Replay System)** inceleme kapsamı eklendi. |

---

## 3. 13 Kasım 2026 Cuma Maç Atamaları ve Saha Hazırlık Planı (`devir-hakem-vize-13kasim.md`)

- **Hakem:** **AHMET GÖKALP GÖKSU** (Ankara İl Hakemi — 4 aylık aradan sonra ilk maç günü).
- **Salon ve Tarih:** **13 Kasım 2026 Cuma**, **TAHA AKGÜL SPOR SALONU**.
- **Görev ve Partner:** Her iki maçta da **2. Hakem (Yardımcı Hakem)**; **1. Hakem (Başhakem): ONUR UĞUR ÇİÇEKDENK**.

| Saat | Maç Kodu | Lig ve Grup | Ev Sahibi (A Takımı) | Deplasman (B Takımı) | Puan Durumu ve Maç Analizi (TBF `10.11` Verisi) |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **`17:30`** | `ANK-U14E-B-2026-113` | **U14 Erkek B — F Grubu** (`lig=22328`) | **BAŞKENT İZ SK (B)**<br>*(3. sıra, 3G–1M, Averaj: +41)* | **ÇAYYOLU AKADEMİ SK (A)**<br>*(1. sıra, 4G–0M, Averaj: +134)* | **Isınma Maçı:** Çayyolu Akademi net favori (+134 averaj). Pozisyon alma, net sinyal mekaniği ve masa iletişimi ritmi kazanmak için ideal. |
| **`19:00`** | `ANK-U18E-B-2026-088` | **U18 Erkek B — D Grubu** (`lig=22332`) | **ANKARA SPOR AKADEMİSİ SK**<br>*(2. sıra, 2G–1M, Averaj: +53)* | **BAŞKENT İZ SK (A)**<br>*(4. sıra, 1G–1M, Averaj: +49)* | **Ana / Zorlu Maç:** Çok dengeli iki takım. Temas çizgisi ilk 3–4 dakikada net belirlenmeli ve 40 dakika tutarlı korunmalı; son çeyrek gerginliğine hazırlıklı olunmalı. |

### 3.1. Maç Öncesi ve Maç Günü Kontrol Listesi
1. **Günlük Kural ve Mekanik Tazeleme (15+15+5 dk):**
   - **Kural (15 dk):** 24/14 saniye sıfırlama kuralları, son 2 dakikada mola sonrası oyuna sokma yeri (ileri sahadaki oyuna sokma çizgisi vs. geri saha), gather step / yürüme ve yeni Md. 36/37/38 faul kriterleri.
   - **Video (15–20 dk):** BSL veya FIBA maçında topu değil yalnız hakemlerin **ikili mekaniğini (Lead / Trail pozisyonları, rotasyon, açık açı bulma)** izle.
   - **Ayna Karşısında Sinyal (5 dk):** *Düdük → Durdur (el havada) → Faul/İhlal Sinyali → Masaya Raporlama (Numara → Faul Türü → Atış/Yön)*.
2. **Maç Günü (`13.11.2026` Cuma):**
   - Salonda en geç **`16:45`**'te hazır bulun ve fiziksel ısınmayı tamamla.
   - **Başhakem Onur Uğur Çiçekdenk ile Ön Görüşme (Pre-game Conference):** 4 aydır maça çıkmadığını paylaş; Lead/Trail birincil sorumluluk alanlarını, ikili sıkıştırma (trap) ve dip çizgi dışarı çıkma pozisyonlarında göz temasını, mola ve oyuncu değişikliği yönetimini netleştir.
   - İki maç arasındaki 15–20 dakikalık arada su tüket, hafif karbonhidrat al ve kasları soğutmadan sıcak tut.

---

## 4. 2026–2027 Sezonu Hakem Ücret Tarifesi ve "Düdük" Uygulaması Kuralı

`raw/ucret-tarifesi-2026-2027.txt` resmi TBF Yönetim Kurulu kararına ve **Düdük** (`com.flugel.duduk`) Android uygulamasının kazanç modülüne göre 2026–2027 sezonu özel müsabaka görevli ücretleri:

| Kategori / Faaliyet Türü | Hakem Ücreti | Masa Görevlisi | Temsilci | İstatistik Görevlisi |
| :--- | :---: | :---: | :---: | :---: |
| **BSL (Basketbol Süper Ligi)** | `14.000 TL` | `1.700 TL` | `4.250 TL` | `1.700 TL` |
| **KBSL (Kadınlar Basketbol Süper Ligi)** | `9.500 TL` | `1.700 TL` | `3.750 TL` | `1.700 TL` |
| **TBL (Türkiye Basketbol Ligi — 1. Lig)** | `8.500 TL` | `1.400 TL` | `3.750 TL` | `1.400 TL` |
| **TKBL / TB2L (Kadınlar 1. Lig / Erkekler 2. Lig)** | `5.000 TL` | `1.400 TL` | `3.250 TL` | `1.400 TL` |
| **BGL / EBBL / KBBL (Gençler ve Bölgesel Lig)** | `4.250 TL` | `1.400 TL` | `3.250 TL` | `1.400 TL` |
| **İl İçi Büyükler (Şirketler / Ticari — Erkek)** | `3.250 TL` | `1.100 TL` | `1.400 TL` | — |
| **İl İçi Büyükler (Şirketler / Ticari — Kadın)** | `2.600 TL` | `1.100 TL` | `1.250 TL` | — |
| **İl İçi Kulüp Altyapı / Üniversite / Okul / STK** | **`1.700 TL`** | **`850 TL`** | `1.100 TL` | — |
| **MEB / Valilik / Kaymakamlık 18 Yaş Altı Turnuvaları** | `850 TL` *(1/2 tarife)* | `425 TL` *(1/2 tarife)* | `550 TL` *(1/2 tarife)* | — |
| **Açıkhava Turnuvaları (Seans Ücreti — En fazla 6 saat)** | `4.250 TL / Seans` | `2.600 TL / Seans` | `3.500 TL / Seans` | — |
| **Resmi İl İçi `BÖLGE` Ligi Müsabakaları** | **`Ücret Tanımsız (`null`)`** *(Resmi bordro tutarı tarifede yazmadığı için Düdük uygulamasında `0 TL` sayılmaz, "ücret tanımsız" olarak işaretlenir ve ayarlardan girilir)* | | | |
