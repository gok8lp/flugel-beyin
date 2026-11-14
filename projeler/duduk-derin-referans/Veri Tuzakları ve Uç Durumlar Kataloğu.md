---
title: "Veri Tuzakları ve Uç Durumlar Kataloğu"
aliases:
  - "Veri Tuzakları"
  - "Uç Durumlar"
  - "Tuzaklar Kataloğu"
tags:
  - duduk
  - referans
  - tuzaklar
  - edge-cases
  - hata-yonetimi
created: 2026-11-11
status: active
---

# ⚠️ Veri Tuzakları ve Uç Durumlar Kataloğu

⬅️ **Üst Merkez:** [[00 - Düdük MOC (Ana Merkez)]]
➡️ **İlgili Modüller:** [[01 - Veri Kaynakları ve API Analizi]] · [[02 - TBF Maç ve Lig Eşleştirme Algoritması]] · [[03 - Yerel Arşiv, Birleştirme ve Değişiklik Tespiti]] · [[04 - Hakem İstatistikleri ve 2026-2027 Ücret Tarifesi]] · [[05 - Android Mimari, Senkronizasyon, Bildirimler ve Arayüz]]

Bu katalog, **Düdük** projesinin tersine mühendislik ve geliştirme sürecinde keşfedilen tüm gerçek dünya veri anomalilerini, API tutarsızlıklarını ve bunlara karşı yazılan savunmacı Kotlin çözümlerini tek tabloda toplar.

---

## 🛡️ Tüm Tuzaklar ve Savunmacı Çözümler

| # | Kaynak / Bileşen | Tuzak / Anomali | Kanıt / Örnek | Çözüm (`com.flugel.duduk.*`) |
|---|---|---|---|---|
| **1** | `assignr` (`recent-weeks`) | **Yalnız Son 2 Hafta:** Geçmiş haftaları veren hiçbir uç veya sorgu parametresi (`?weeks=6`, `?page=2`) yok; parametreler yok sayılıyor. | Tüm parametreli çağrılar bayt-özdeş MD5 döndürdü; Wayback Machine boş. | `ArsivDeposu` (`arsiv.json`) ve `Birlestirici` ile her çekilen veri silinmeden yerel arşive eklenir (`upsert`). |
| **2** | `assignr` (`recent-weeks`) | **Tekil Olmayan `matchNumber` (Erteleme Tuzağı):** Ertelenen maç eski kaydı silinmeden aynı numarayla ikinci kez geliyor. | `ANK-U16E-C-2026-153` hem 7 Kasım 17:00 Altındağ hem 8 Kasım 12:30 Taha Akgül olarak var. | Birincil anahtar `matchNumber\|date\|time` (`MacAnahtari.olustur`) yapıldı. `Birlestirici.ertelemeleriIsaretle()` eski kayda `yerineGelen` yazar. |
| **3** | `assignr` (`recent-weeks`) | **Numara İçi Saat Uyumsuzluğu:** `BÖLGE` dışı numaralardaki saat ile `time` alanı uyuşmuyor. | `OKUL-20261109-1300-f442` kaydının `time` değeri `"10:30"`. | Numara içindeki saat hiçbir yerde ayrıştırılmaz; daima `time` alanı kullanılır. |
| **4** | `assignr` (`recent-weeks`) | **Tutarsız `groupName` Biçimi:** Grup adı `"F"`, `"Grup D"`, `"-"`, `"AA"` şeklinde farklı biçimlerde geliyor. | `recent-weeks.json` içindeki `groupName` kümesi. | `GrupAdi.normalle()` baştaki `"Grup "` önekini atar; `"-"`, `"—"` ve lig adıyla aynı olanları `null` yapar. |
| **5** | `assignr` (`recent-weeks`) | **Tutarsız `week` Etiketi:** Ay geçişlerinde tire etrafında boşluk var, diğerlerinde yok. | `"31 Ekim - 6 Kasım 2026"` vs `"7-13 Kasım 2026"`. | Sıralama ve tarih aralığı kontrolünde `week` yerine ISO `date` (`YYYY-MM-DD`) kullanılır. |
| **6** | `assignr` (`masa`) | **Hakem ve Masa Kümesi Farkı:** Masa ucunda ulusal/Avrupa maçları var, `AA` maçları yok. | 18 kayıt (`TBL`, `BSL`, `Eurocup`, `DEP-...`) yalnız masada; 8 `AA` kaydı yalnız hakemde. | `Birlestirici.assignr()` iki ucu birleştirir ve `kaynaklar` kümesini (`"hakem"`, `"masa"`) ayrı takip eder. |
| **7** | `assignr` (`venues`) | **Koordinatsız Salonlar ve Takma Adlar:** Bazı salonlar `venues` listesinde yok veya `aliases` altında kayıtlı. | `"SİNCAN SPOR KOMPLEKSİ"` ve `"GİMSA PARK AVM SS"` yok; `"ANKARA SPOR SALONU KÜÇÜK"` alias'ta. | `SalonBulucu` hem `name` hem `aliases` arar; koordinat yoksa `geo:0,0?q=Salon+Adi,+Ankara` arama bağlantısı üretir. |
| **8** | `ankarabasket` (Ana Sayfa) | **Java Regex `StackOverflowError`:** Uzun RSC Flight string literal'lerinde `("(?:[^"\\]\|\\.)*")` regex'i JVM'de yığın taşması yapıyor. | `anasayfa.html` üzerinde JVM birim testi. | `AnkarabasketAyristirici.flight()` regex yerine $O(N)$ doğrusal karakter/kaçış tarayıcısı kullanır. |
| **9** | `ankarabasket` (`/api`) | **`robots.txt` Yasağı:** Payload CMS `/api` uçları `200` dönse de `Disallow: /api` kuralı var. | `ankarabasket.org.tr/robots.txt`. | Çalışma zamanında `/api` çağrılmaz; `season-teams` ve `clubs` `assets/katalog/` içine gömüldü (`GomuluKatalog`). |
| **10** | `TBF WebAPI` (Genel) | **`"22328.0"` Double ID Tuzağı:** Tam sayı kimlikler bazen `22328`, bazen `22328.0`, bazen `"22328.0"` olarak dönüyor. | `takimIslemId: 269615` ↔ `269615.0`, `activityId: 22328.0`. | `EsnekDouble`, `EsnekInt` ve `EsnekMetin` özel serileştiricileri (`EsnekSerilestiriciler.kt`) her biçimi güvenle okur. |
| **11** | `TBF WebAPI` (`matches`) | **`"10. Hafta"` Tarih Metni Tuzağı:** Oynanmamış maçlarda (`statusId` 19/20) `matchDate`, `matchDateOnly` ve `matchTime` alanlarında ISO tarih yerine hafta metni yazıyor. | 1.702 Ankara maçının 902'sinde `matchDate = "10. Hafta"`, `salonAdi = "Atanmadı"`. | `TbfMac.tarih` alanı `^\d{4}-\d{2}-\d{2}` regex kontrolüyle ayrıştırılır; uymayanlar `null` döner. |
| **12** | `TBF WebAPI` (`matches`) | **Yanlış `matchStatusId = 19`:** Maç oynanıp skoru girildiği halde statüsü `19` (Atanmadı) kalmış kayıt var. | U14 Erkek, 6 Kasım, `ANKARA DTY SK` maçı. | `TbfMac.oynandi` statü koduna değil, `tarih != null && homeTeam.skor != null && awayTeam.skor != null` şartına bakar. |
| **13** | `TBF WebAPI` (`matches`) | **`WeekFilter` Eksikliğinde Boş Liste:** `get-all-matches-for-filter` çağrısında `WeekFilter` verilmezse `data: []` döner. | Doğrudan API denemesi. | Tüm sezon için `WeekFilter=*` parametresi zorunlu olarak gönderilir (`DogrudanKaynak.tbfMaclar`). |
| **14** | `TBF` ↔ `assignr` | **Türkçe `uppercase` ve Takım Soneki Çatışması:** `MAGIC` vs `MAGİC` ve aynı kulübün `(A)` ile `(B)` takımlarının karışma riski. | 192 maçın 187'sinde ham takım/salon adı farklı. | `Normalizasyon.fold()` önce `İ/ı/i → I` yapar; `takimBenzerligi()` farklı soneklerde (`(A)` vs `(B)`) doğrudan `0.0` verir. |
| **15** | `WorkManager` | **WorkManager 2.11+ API 34 Çökmesi:** Bazı üretici ROM'larında `JobScheduler.forNamespace()` açılışta çöküyor. | `koharia-reader` deneyim notu (`libs.versions.toml`). | WorkManager sürümü bilinçli olarak **`2.10.5`**'te sabitlendi. |
| **16** | `KazancHesaplayici` | **`BÖLGE` Ücretinin Bulunamaması:** Yerel lig ücretleri GSB İl Müdürlüğü bütçesinden ödendiği için açık kaynakta yok. | TBF Hakemler Talimatı Md. 29/(4). | `BÖLGE` kalemleri `tutarTl = null` ("ücret tanımsız") başlar; kesinlikle `0 TL` sayılmaz. |
