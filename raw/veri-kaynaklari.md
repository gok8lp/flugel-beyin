# Düdük — Veri Kaynakları (doğrulanmış)

Gözlem zamanı: **11 Kasım 2026, ~10:45–11:00 TRT**. Tüm uçlar giriş gerektirmeden, yalnız `GET` ile denendi (toplam ~200 istek, host başına ≤ 1-2 istek/sn).
Ham yanıtlar `docs/samples/` altında. Bu doküman bir anlık görüntüdür; id, şema ve davranışlar değişebilir.

İşaretler: **[Ç]** = bizzat çalıştırıp yanıtını gördüm · **[Ç-kod]** = sitenin JS kodundan okudum, çağrıyı ayrıca denedim · **[Çıkarım]** = kanıta dayalı tahmin · **[Yok]** = aradım, bulamadım.

---

## 0. Özet: hangi veri nereden

| İhtiyaç | Birincil kaynak | Yedek / tamamlayıcı |
|---|---|---|
| Kullanıcının atamaları (hakem) | assignr `recent-weeks` (§1.1) | — |
| Masa görevlileri | assignr `recent-weeks/masa` (§1.2) | — |
| Salon koordinatı | assignr `venues` (§1.3) | — |
| Yakın fikstür (bugün−2 … bugün+4), **matchNumber ile skor** | ankarabasket ana sayfa gömülü `days` JSON (§2.1) | — |
| Eski maç skorları (sezon başından beri) | TBF `get-all-matches-for-filter` (§3.3) — matchNumber YOK, eşleştirme gerekir (§5) | ankarabasket kulüp sayfası (§2.3, kulüp başına son 6 sonuç, matchNumber var) |
| Puan durumu | TBF `get-standings-table` JSON (§3.4) | ankarabasket `/puan-durumlari` HTML (§2.2; aynı TBF verisinin önbelleği) |
| Lig kataloğu (id'ler) | TBF `filters-results` (§3.1) | ankarabasket Payload `season-teams` (§2.4) |
| Lig/grup ↔ takım (assignr adlarıyla) | ankarabasket Payload `season-teams` + `clubs` (§2.4) | — |
| Takım logoları | ankarabasket `/api/media/file/<slug>.png` (§2.5) | TBF `teamLogoUrl` |
| Hakem listesi / klasman | ankarabasket Payload `officials` (§2.4) | — |
| Ücret tarifesi | Özel müsabaka tarifesi PDF (§6) | Yerel lig (BÖLGE) tutarı: **bulunamadı** |

En önemli mimari sonuç: **üç ayrı sistem var** — assignr (atama, immensus), ankarabasket.org.tr (portal, immensus; assignr `matchNumber`'ını `code` olarak taşır ve skoru gösterir), TBF (resmî skor/puan; kendi `matchId`/`matchCode`'u var, assignr numarasını bilmez).

---

## 1. assignr.immensus.io

Sunucu: Spring Boot (404 yanıtı `application/problem+json`, "No static resource …"), Cloudflare arkasında. Sayfa: `https://assignr.immensus.io/assignments.html` (tek satır içi script; yalnız aşağıdaki üç ucu çağırır **[Ç]**).

### 1.1 Hakem atamaları

- **Uç:** `GET https://assignr.immensus.io/api/public/assignments/recent-weeks`
- **Yöntem:** Düz GET, başlık gerekmez. Sayfanın kendisi `city` parametresi **göndermiyor**; `?city=ankara`, `?city=istanbul`, `?city=izmir` aynı bayt-özdeş yanıtı verdi (md5 aynı) → parametre yok sayılıyor **[Ç]**.
- **Şema:** JSON dizi (11 Kasım: 301 kayıt, 128 KB; `Accept-Encoding: br` ile 10 KB).

  | Alan | Tip | Not |
  |---|---|---|
  | `week` | string | `"7-13 Kasım 2026"`, `"31 Ekim - 6 Kasım 2026"` (biçim tutarsız; ay değişince tire etrafında boşluk var). Sıralama için kullanma; `date` kullan. |
  | `matchType` | string | `BÖLGE`, `OKUL`, `AGL`, `AA`, `ABL` (bkz. §7) |
  | `date` | `YYYY-MM-DD` | TR yerel tarihi |
  | `time` | `HH:MM` | TR yerel saati (UTC+3, DST yok) |
  | `hall` | string | BÜYÜK HARF; AA'da karışık harf |
  | `league` | string | `"U 14 ERKEK B"`, `"BÜYÜK ERKEK A"`, `"GENÇ ERKEKLER A"`, `"U11 PREMİUM"`, `"U12 PREMIUM"` (İ/I tutarsız), `"AA"`, `"ABL"` |
  | `groupName` | string | `"F"`, `"Grup D"`, `"-"`, `"AA"`. Görülen küme: `- A AA B C D E F G H I J K L "Grup A".."Grup D"`. Baştaki `Grup ` atılarak normalize edilmeli. |
  | `matchNumber` | string | BÖLGE: `ANK-U14E-B-2026-113` (kalıcı). Diğerleri: `OKUL-20261109-1300-f442`, `AGL-20261107-1500-328b`, `ABL-…`, `AA-29`. |
  | `teamA`, `teamB` | string | Ev sahibi / deplasman |
  | `referee1..3` | string \| null | `referee3` çoğunlukla `""`, bazen `null`. Ad BÜYÜK HARF: `"AHMET GÖKALP GÖKSU"`. `referee1` = başhakem **[Çıkarım: ABL Google Sheet'inde sütun sırası "BAŞ HAKEM, 1. YARDIMCI, 2. YARDIMCI" ile aynı kişiler aynı sırada]**. |
  | `tableOfficial1..4` | null | Bu uçta hep `null` |

- **Örnek dosya:** `samples/assignr/recent-weeks.json`, başlıklar `samples/assignr/recent-weeks.headers.txt`
- **Tuzaklar:**
  - **Yalnız son 2 hafta** döner (şu an 31 Ekim–6 Kasım ve 7–13 Kasım). Geçmişi uygulama **kendisi biriktirmek zorunda** (bkz. §1.4).
  - **`matchNumber` tekil değil:** `ANK-U16E-C-2026-153` aynı yanıtta iki kez var (7 Kasım 17:00 Altındağ ve 8 Kasım 12:30 Taha Akgül; hakemler farklı) — ertelenen/yeniden atanan maçın eski kaydı silinmiyor. Yerel birincil anahtar `matchNumber + date + time` olmalı; aynı numaranın en ileri tarihli kaydı güncel kabul edilebilir **[Çıkarım]**.
  - BÖLGE dışı `matchNumber` içindeki saat, `time` alanıyla uyuşmayabiliyor (`OKUL-20261109-1300-f442` kaydının `time` değeri `10:30`) → numara oluşturulma anındaki saati taşıyor, saat değişince güncellenmiyor.
  - Hafta Cumartesi başlıyor (Cmt–Cuma).
  - Kullanıcının adı için eşleştirme: `tr-TR` büyük harfe çevirip tam eşitlik. (11 Kasım'da kullanıcı 2 maçta `referee2`: `ANK-U14E-B-2026-113`, `ANK-U18E-B-2026-088`, ikisi de 13 Kasım.)
- **Koşullu istek:** **ETag yok, Last-Modified yok**; `Cache-Control: no-cache, no-store, max-age=0, must-revalidate`, `Expires: 0`. `If-Modified-Since`/`If-None-Match` gönderildiğinde yine `200` + tam gövde **[Ç]**. Uygulama gövdenin SHA-256'sını saklayıp değişimi kendisi algılamalı.
- **Önerilen yenileme sıklığı:** Uygulama açılışında + arka planda 3–6 saatte bir (WorkManager); maç günü 1 saatte bir. ~15 dakika arayla iki çekimde gövde bayt-özdeşti; gerçek değişim sıklığı **ölçülemedi** (bkz. §8). Brotli/gzip'i açık bırak (OkHttp varsayılanı gzip).

### 1.2 Masa görevlisi atamaları

- **Uç:** `GET https://assignr.immensus.io/api/public/assignments/recent-weeks/masa`
- **Şema:** §1.1 ile aynı; `tableOfficial1..4` dolu, `referee1..3` = `null`. 311 kayıt.
- **Örnek dosya:** `samples/assignr/recent-weeks-masa.json`
- **Tuzaklar:** Kayıt kümesi hakem ucuyla **aynı değil**: masa ucunda ayrıca `TBL`, `KBSL`, `TKBL`, `TB2L`, `BSL`, `Eurocup`, `Tekerlekli Sandalye Süper Ligi` türleri ve `DEP-20261102-1800-454e` biçimli numaralar var (18 kayıt yalnız masada), `AA` maçları ise masada yok (8 kayıt yalnız hakemde). İki ucu `matchNumber+date+time` ile birleştir, eksik tarafı boş bırak.
- **Önerilen yenileme sıklığı:** §1.1 ile birlikte.

### 1.3 Salonlar

- **Uç:** `GET https://assignr.immensus.io/api/public/venues`
- **Şema:** `[{ "name": String, "aliases": [String], "lat": Double, "lng": Double }]` — 13 salon.
- **Örnek dosya:** `samples/assignr/venues.json`
- **Tuzaklar:** Sayfa eşleştirmeyi `trim → tr büyük harf → çoklu boşluğu teke indir` ile `name` ve `aliases` üzerinden yapıyor; aynısını uygula. `SİNCAN SPOR KOMPLEKSİ` ve `GİMSA PARK AVM SS` listede **yok** (koordinatsız kalır). `ANKARA SPOR SALONU KÜÇÜK` → `ANKARA SPOR SALONU` takma adıyla eşleşir.
- **Önerilen yenileme sıklığı:** Haftada bir; uygulamaya gömülü kopya ile başla.

### 1.4 Başka uç / geçmiş hafta var mı? — **Yok**

Denenen ve sonuç **[Ç]**:

| Deneme | Sonuç |
|---|---|
| `recent-weeks?weeks=6`, `?week=24-30 Ekim 2026`, `?from=&to=`, `?startDate=&endDate=`, `?season=2026`, `?count=&limit=&page=` | Hepsi 200, **parametresiz yanıtla bayt-özdeş** (yok sayılıyor) |
| `/api/public/assignments`, `/assignments/weeks`, `/assignments/all`, `/assignments/history`, `/assignments/archive`, `/assignments/week/2026-10-24`, `/assignments/recent-weeks/hakem` | 404 |
| `/api/public/weeks`, `/referees`, `/officials`, `/matches`, `/leagues`, `/cities`, `/scores`, `/seasons`, `/stats`, `/api/public` | 404 |

- Skor, hakem listesi, hafta listesi ucu **yok**. Sayfadaki "Hafta" seçici yalnız dönen 2 haftayı istemci tarafında süzüyor.
- **Wayback Machine:** `archive.org/wayback/available?url=assignr.immensus.io/api/public/assignments/recent-weeks` → `"archived_snapshots": {}` (anlık görüntü yok) **[Ç]**. CDX sorgusu iki denemede "Temporarily Offline" döndü; CDX ile ayrıca doğrulanamadı.
- Sonuç: **geçmiş haftalara ulaşmanın herkese açık yolu yok.** Hakem istatistikleri için uygulama her çekimi Room'a `upsert` edip kendi arşivini oluşturmalı; 31 Ekim öncesi atamalar bu uçlardan geri getirilemez. (BÖLGE fikstür bültenleri ankarabasket'te Google Drive klasörü olarak duruyor — §2.4 `fixture-bulletins` — ama makinece okunur değil, incelenmedi.)

---

## 2. ankarabasket.org.tr (Next.js + Payload CMS)

`robots.txt` **[Ç]**: `Allow: /`, `Allow: /api/media/file/`, `Allow: /api/files/file/`, **`Disallow: /api`**, `Disallow: /r/`. Yani HTML sayfaları ve medya dosyaları serbest; Payload REST uçları (§2.4) teknik olarak açık ama robots ile tarayıcılara kapatılmış. Tüm sayfalarda `Cache-Control: private, no-cache, no-store`; ETag/Last-Modified yok.

Sitede istemci tarafı veri çağrısı **yok**: JS yalnız `POST /api/hit` (sayaç) ve `POST/DELETE /api/push` (web push aboneliği) çağırıyor **[Ç-kod]**. Tüm veri sunucuda render edilip HTML'e ve `self.__next_f.push(...)` (RSC flight) yüküne gömülüyor. `RSC: 1` başlığıyla istek `307 → …&_rsc` yönlendirmesi verdi; ayrı RSC ucu kullanmaya gerek yok, HTML yeterli.

### 2.1 Ana sayfa "Maçlar — Sonuçlar ve Program" (**matchNumber + skor**)

- **Uç:** `GET https://www.ankarabasket.org.tr/`
- **Yöntem:** HTML'i indir; `self.__next_f.push([1,"…"])` parçalarını birleştir; içinden `"days":[ … ]` JSON dizisini çıkar.
- **Şema [Ç]:**
  ```json
  [{ "dateKey": "2026-11-10", "label": "10 Kasım Salı", "isToday": false, "isPast": true,
     "matches": [{
       "league": "U 14 KIZ A", "group": "A", "time": "17:00",
       "venue": "ANKARA SPOR SALONU KÜÇÜK",
       "code": "ANK-U14K-A-2026-023",
       "home": "GALLARDO SK", "away": "ÇANKAYA ÜNİVERSİTESİ SK (B)",
       "homeLogo": "/api/media/file/gallardo-sk.png", "awayLogo": "/api/media/file/cankaya-universitesi-sk.png",
       "score": { "home": 76, "away": 52 },
       "forfeit": false }] }]
  ```
  `score` oynanmamış maçta yok/`null`. `code` = assignr `matchNumber`; `league`/`group`/`venue`/takım adları assignr yazımıyla aynı.
- **Kapsam [Ç]:** 7 gün = **bugün−2 … bugün+4** (11 Kasım'da: 9–15 Kasım). Yalnız `BÖLGE` (yerel lig) maçları; OKUL/AGL/ABL/AA yok. 9–13 Kasım için maç sayısı assignr BÖLGE sayısıyla birebir (13/13/12/13/8). **14–15 Kasım maçları (34 maç) assignr'da henüz yokken burada vardı** → gelecek haftanın fikstürü atamadan önce buradan görülebilir.
- **Skor gecikmesi [Ç]:** 10 Kasım Salı akşamı oynanan 13 maçın 13'ünde skor 11 Kasım ~10:45'te mevcuttu; aynı anda TBF'de bu maçların skoru yoktu. Ana sayfa "Takımının skoru girildiği anda tarayıcı bildirimi al" diyor → skor maç sonrası elle giriliyor **[Çıkarım]**; dakika cinsinden gecikme ölçülmedi.
- **Örnek dosya:** `samples/ankarabasket/anasayfa.html`, çıkarılmış hali `samples/ankarabasket/anasayfa-days.json`, referans ayrıştırıcı `samples/ankarabasket/flight_ayristir.py`
- **Kotlin tarifi:**
  ```kotlin
  // 1) parçaları topla: her push argümanı bir JSON string literalidir
  val re = Regex("""self\.__next_f\.push\(\[1,("(?:[^"\\]|\\.)*")\]\)""")
  val flight = buildString { re.findAll(html).forEach { append(Json.decodeFromString<String>(it.groupValues[1])) } }
  // 2) "days":[ ... ] dizisini köşeli parantez dengeleyerek kes (string içindeki [ ] ve \" kaçışlarına dikkat)
  val start = flight.indexOf("\"days\":[") + 7
  val end = matchingBracket(flight, start)            // elle yazılacak küçük tarayıcı
  val days = Json { ignoreUnknownKeys = true }.decodeFromString<List<Day>>(flight.substring(start, end + 1))

  @Serializable data class Day(val dateKey: String, val label: String, val isToday: Boolean, val isPast: Boolean, val matches: List<M>)
  @Serializable data class M(val league: String, val group: String, val time: String, val venue: String, val code: String,
      val home: String, val away: String, val homeLogo: String? = null, val awayLogo: String? = null,
      val score: Score? = null, val forfeit: Boolean = false)
  @Serializable data class Score(val home: Int, val away: Int)
  ```
- **Tuzaklar:** Belgelenmemiş, sitenin iç render biçimi; bileşen adı (`MatchBoardTabs`) veya prop adı (`days`) değişirse kırılır → ayrıştırma hatasında sessizce TBF yoluna (§3.3 + §5) düş. Tarih penceresini değiştiren bir sorgu parametresi kodda **görülmedi**. Pencere dışına düşen maçın skoru buradan bir daha alınamaz → **her gün en az bir kez çekilmeli** (2 günlük geri pencere).
- **Önerilen yenileme sıklığı:** Günde 2–4 kez; kullanıcının maçı olan gün maç bitişinden sonra 30–60 dakikada bir, skor gelene kadar (en çok ~48 saat).

### 2.2 Puan durumu (HTML tablo; TBF verisinin önbelleği)

- **Uç:** `GET https://www.ankarabasket.org.tr/puan-durumlari?lig=<tbfFaaliyetId>&sev=<A|B|C>`
  - `lig`: 22320 (Büyük Erkekler), 22328 (U14 E), 22329 (U14 K), 22330 (U16 E), 22331 (U16 K), 22332 (U18 E), 22333 (U18 K) — **bunlar TBF faaliyet id'leri**. `sev` verilmezse A. 22320'de `sev` yok.
- **Şema:** Her grup `<div class="stand-group" id="grup-N">` içinde `<h3>U 14 ERKEK B LİGİ F GRUBU<span class="stand-week"> · 4. hafta</span></h3>` + `<table class="stand-table">`; sütunlar `# | Takım | O | G | M | A | Y | Av | P`. Sayfada "TBF verisi · Son güncelleme: 10 Kasım 17:28" ve "Kaynak: Türkiye Basketbol Federasyonu" yazıyor; grup adları ve takım adları TBF yazımıyla (assignr yazımıyla **değil**).
- **Örnek dosya:** `samples/ankarabasket/puan-durumlari-lig22328-sevB.html`
- **Kotlin tarifi (Jsoup):** `doc.select("div.stand-group")` → `h3.ownText()` grup adı, `span.stand-week` hafta; `table.stand-table tbody tr` → `td` metinleri; takım adı `td.team span.team-in > span`, logo `img.fx-logo[src]`.
- **Tuzaklar:** TBF'den periyodik kopya (son güncelleme damgası ~17 saat eskiydi). Doğrudan TBF JSON'u (§3.4) hem daha taze hem ayrıştırması kolay → **bunu yalnız yedek olarak kullan**. Tek artısı: satırlarda ankarabasket logo yolu var.
- **Önerilen yenileme sıklığı:** Yalnız TBF başarısız olursa.

### 2.3 Kulüp sayfası (kulüp başına gelecek maçlar + son 6 sonuç)

- **Uç:** `GET https://www.ankarabasket.org.tr/kulupler/<slug>` (slug: Payload `clubs.slug`, ör. `ankara-dsi-sk`)
- **Şema:** HTML. "2026/27 Sezonu" tablosu (Kategori, Lig, Grup, Takım), "Gelecek Maçları", "Son Sonuçlar" (`table.res-table`: Tarih `DD.MM.YYYY`, Rakip + `İç Saha`/`Deplasman` etiketi, Skor `35 – 48`). `matchNumber` HTML'de görünmez ama flight yükünde satırın React anahtarı olarak durur: `"10.11.2026-ANK-U18K-A-2026-031"` **[Ç]**.
- **Örnek dosya:** `samples/ankarabasket/kulup-ankara-dsi-sk.html`
- **Tuzaklar:** Son sonuç sayısı 6 ile sınırlı görünüyor (tek kulüpte gözlendi). Skorun "ev – deplasman" mı "kulüp – rakip" mi olduğu **doğrulanmadı** (kazanılan satırda `rt-team win` sınıfı var; onunla çapraz kontrol edilebilir). 127 kulüp × istek pahalı; yalnız tek maç için hedefli kullan (kullanıcının yönettiği maçın takımları).
- **Önerilen yenileme sıklığı:** İstek üzerine (ana sayfa penceresini kaçırmış maçın skoru için).

### 2.4 Payload REST uçları (robots.txt'te `Disallow`, ama girişsiz 200 dönüyor)

- **Uç:** `GET https://www.ankarabasket.org.tr/api/<collection>?limit=1000&depth=0` — standart Payload: `{ docs: [...], totalDocs, limit, page, totalPages, hasNextPage, ... }`. `where[alan][equals]=…`, `depth=1` (ilişkileri açar) standart Payload sözdizimi **[depth=0 ve limit denendi; where denenmedi]**.
- `GET /api/access` herkese açık okunabilir koleksiyonları listeliyor **[Ç]** (`samples/ankarabasket/payload-access.json`):

  | Koleksiyon | Kayıt | Alanlar | Kullanım |
  |---|---|---|---|
  | `season-teams` | 455 | `club`(id), `season`("2026/27"), `ageCategory`(`yildiz`=U14, `genc`=U16, `u18`, `buyuk`), `gender`(`erkek`/`kadin`), `league`("U 14 ERKEK B"), `group`("F"), `teamName`("A Takımı"), `placeholder` | **Lig/grup kataloğu, assignr adlarıyla** |
  | `clubs` | 127 | `name`, `slug`, `logo`(media id), `district`, `address`, `lat`, `lng`, `ageGroups`, `venues`, iletişim | Takım → logo/slug |
  | `officials` | 234 | `name`("Egehan Sert"), `photo`, `group`(`referee` 69 / `classification-referee` 28 / `table-official` 137), `classification`(`il`,`a`,`b`,`c`), `hidden` | Hakem listesi/klasman |
  | `fixture-bulletins` | 13 | `title`, `season`, `month`, `year`, `bulletinNo`, `status`, `competitionType`(`local-league`,`away-league`,`preparation`,`school`,`threexthree`,`other`), `customCompetitionType`, `externalUrl` | Bülten bağlantıları (Drive/Sheets/OneDrive) |
  | `documents`, `files`, `media`, `news`, `pages`, `ads` | — | — | Mevzuat PDF'leri vb. |

  **Maç/skor/puan koleksiyonu yok** (`/api/standings` → 404). Maç verisi sunucu tarafında başka bir yerden (büyük olasılıkla assignr'ın kapalı arka ucu) geliyor **[Çıkarım]**.
- **Örnek dosya:** `samples/ankarabasket/payload-{season-teams,clubs,officials,fixture-bulletins,documents,access}.json`
- **Tuzaklar:** robots.txt bu yolu yasaklıyor → uygulamada **sık çağırma; tercihen uygulamaya gömülü statik katalog** (sezon başında bir kez elle güncellenir) ya da haftada 1 istek. `season-teams` kulüp beyanına dayanıyor; TBF puan tablosuyla takım sayıları 20 grupta ±1-2 farklı (bkz. `lig-eslesme.json` notları).
- **Önerilen yenileme sıklığı:** Sezonda birkaç kez / haftada en çok 1.

### 2.5 Logo URL kalıbı **[Ç]**

- ankarabasket: `https://www.ankarabasket.org.tr/api/media/file/<kulüp-slug>.png` (ör. `ankara-dsi-sk.png`; bazıları `baskent-iz-sk-480x479.webp`). 127 kulübün 104'ünde logo var; kesin dosya adı için ana sayfa `homeLogo`/`awayLogo` ya da `clubs?depth=1` → `logo.url` kullan, slug'dan **tahmin etme**. Bu yol robots'ta `Allow`.
- TBF: maç kaydındaki `homeTeam.logoUrl` → `https://tbf.org.tr/res/<guid>_<ad>.png`. Boş string olabilir; dosya adında **boşluk** olabilir (`…_an kavra sk.png`) → URL-encode et.
- Hakem fotoğrafları: `/api/media/file/<AD SOYAD>-480x320.webp` (ad NFD ayrışık Unicode ile kodlanmış; URL'yi HTML'den/`officials?depth=1`'den olduğu gibi al).

---

## 3. TBF (tbf.org.tr) — resmî skor ve puan durumu JSON API'si

`www.tbf.org.tr` bir Nuxt uygulaması; HTML'deki `window.__NUXT__.config.public.apiBaseUrl = "https://miniappapi.tbf.org.tr/webapi-service"` **[Ç]**. Uç yolları sitenin JS paketlerinden okundu, sonra doğrudan `curl` ile çağrıldı. `apiHashing` yapılandırması şu an kapalı (yer tutucu `$(ENABLE_API_HASHING)`); açılırsa yollar `/api/h<base64>` biçimine döner ve bu bölüm kırılır.

- **Taban:** `https://miniappapi.tbf.org.tr/webapi-service`
- **Başlık:** Gerekmedi (kimlik, Origin, Referer yok). `Accept-Encoding: br` destekli (396 KB → küçük). ETag/Last-Modified/Cache-Control **yok**.
- **Zarf:** `{ "data": …, "isSuccess": true, "message": "Success", "problemDetails": null }`; listelerde ayrıca `count, pageNumber, pageCount, hasPreviousPage, hasNextPage`. Hata: HTTP 400 + `problemDetails.detail`.
- **GENEL TUZAK — sayı biçimi:** Aynı uç farklı çağrılarda id'leri kâh `22328` kâh `22328.0` olarak döndürdü (`takimIslemId: 269615` ↔ `269615.0`) **[Ç]**. Kotlin'de bu alanları `Double` (ya da `JsonPrimitive` → `.double.toLong()`) oku; `Int`/`Long` olarak bildirirsen ara sıra patlar. Skorlar **string** (`"52"`, boş `""`).

### 3.1 Lig kataloğu

- **Uç:** `GET /api/Altyapilar/filters-results?CityNameForLocalLeague=ANKARA&Season=2026-2027&Page=1&PageSize=300` **[Ç]** (ops. `AgeGroup`, `Gender` **[Ç-kod]**). Süzgeç değerleri: `GET /api/Altyapilar/local-league-filters` **[Ç-kod; yanıtı sayfa yükünde görüldü]** → `seasons` (2016-2017 … 2026-2027), `ageGroups`, `genders`, `city`.
- **Şema:** `data[]: { faaliyetId, sezonAdi, seasonId, faaliyetAdi, yasGrubu, cinsiyet, il, basTarih, bitTarih, durum }`
- **2026-2027 Ankara (seasonId = 174) [Ç]:**

  | faaliyetId | Ad | Maç kaydı | Puan tablosu |
  |---|---|---|---|
  | 22320 | Ankara Büyük Erkekler | 84 | 1 grup |
  | 22321 | Ankara Büyük Kadınlar | 55 (hepsi tarihsiz) | boş |
  | 22322–22327 | U10/U11/U12 Erkek-Kız | 0 | boş |
  | 22328 | Ankara U14 Erkekler | 488 | 22 grup (A:2, B:8, C:12) |
  | 22329 | Ankara U14 Kızlar | 125 | 5 grup |
  | 22330 | Ankara U16 Erkekler | 356 | 16 grup |
  | 22331 | Ankara U16 Kızlar | 123 | 4 grup |
  | 22332 | Ankara U18 Erkekler | 267 | 9 grup |
  | 22333 | Ankara U18 Kızlar | 111 | 2 grup |
  | 22334, 22335, 22337 | U21 Erkek / U21 Kadın / Ümit Kadın | 0 | boş |
  | 22336 | Ankara Ümit Erkekler (= "U 21 ERKEK") | 56 | boş |
  | 23542, 23543 | U16 / U18 Erkekler Seri A Ön Eleme | 19 / 18 | boş |

- **Örnek dosya:** `samples/tbf/filters-results-ankara-2026-2027.json`, `samples/tbf/league-info-22328.json`
- **"sev" ve grup:** TBF'de ayrı alan değil; puan tablosundaki `grup` metninde gömülü: `"U 14 ERKEK B LİGİ F GRUBU"`. ankarabasket'in `sev=A|B|C` parametresi bu metindeki lig harfi.
- **Önerilen yenileme sıklığı:** Sezonda bir (gömülü sabit + elle güncelleme yeterli).

### 3.2 Hafta listesi

- **Uç:** `GET /api/League/get-league-weeks?leagueId=22328&seasonId=174` (ikisi de zorunlu; yoksa 400) **[Ç]**
- **Şema:** `data[]: { sezon_Hafta: "7", devre_ID: 1, devre_Deger: null, display_Text: "Hafta 7", isCurrentWeek: true }`
- **Örnek dosya:** `samples/tbf/league-weeks-22328.json`

### 3.3 Maçlar ve skorlar

- **Uç:** `GET /api/Match/get-all-matches-for-filter?ActivityId=<faaliyetId>&Page=1&PageSize=-1&WeekFilter=*` **[Ç]**
  - `WeekFilter=*` tüm sezon; `WeekFilter=7` tek hafta **[Ç]**. `WeekFilter` hiç verilmezse **boş** liste döner **[Ç]**. Ops. `TeamId`, `HalfValue` **[Ç-kod]**.
- **Şema [Ç]:**
  ```json
  { "matchId": 350958, "activityName": "Ankara U14 Erkekler 2026-2027", "activityId": 22328.0,
    "activityCode": "tbf", "seasonId": 174.0, "season": "2026-2027",
    "matchDate": "2026-09-26T09:30:00", "matchDateOnly": "2026-09-26", "matchTime": "09:30",
    "week": "1. Hafta", "halfValue": "1",
    "homeTeam": { "id": 272566.0, "name": "ANKARA DSİ (B)", "logoUrl": "https://tbf.org.tr/res/….png", "score": "52", "isHome": true },
    "awayTeam": { "id": 272573.0, "name": "GENÇ MAGİC HANDS (B)", "logoUrl": "…", "score": "36", "isHome": false },
    "matchStatusId": 1.0, "salonAdi": "MEB Beşevler Spor Salonu", "matchCode": "BRZ4933",
    "genuisId": "", "hasUzatma": false, "il": "ANKARA", "cinsiyet": "Erkek",
    "youtubeLink": "", "broadcastChannel": "", "isFavorite": false, "activityDisplayName": "" }
  ```
- **`matchStatusId` anlamları** (`/api/Match/mac-header` yanıtındaki `matchStatus` metninden) **[Ç]**:

  | id | Metin | Skor |
  |---|---|---|
  | 1 | Oynandı | dolu |
  | 6 | Tatil Edildi | boş |
  | 8 | Oynandı \| A Takım Hükmen Mağlup | `0`–`20` |
  | 9 | Oynandı \| B Takım Hükmen Mağlup | `20`–`0` |
  | 13 | Oynandı \| A Takımı Ligden Çekildi / İhraç | `0`–`20` |
  | 14 | Oynandı \| B Takımı Ligden Çekildi / İhraç | `20`–`0` |
  | 19 | Fikstür / Tarih ve Saat Atanmadı | boş |
  | 20 | Ertelendi / Tarih ve Saat Atanmadı | boş |

- **Örnek dosya:** `samples/tbf/matches-22328-all.json` (488 maç), `matches-22328-week7.json`, `matches-22332-all.json`, başlıklar `matches.headers.txt`
- **Tuzaklar (kritik):**
  - **Maçta grup alanı yok.** Grup: `homeTeam.id` = puan tablosundaki `takimIslemId` (800 tarihli maçın 799'unda eşleşti) → `grup`. Ya da tek maç için `mac-header.leagueName`.
  - **Gelecek maçların tarihi yok:** statü 19/20'de `matchDate`, `matchDateOnly` ve `matchTime` alanlarının üçü de ISO tarih yerine **hafta metni** taşıyor (`"10. Hafta"`), `salonAdi = "Atanmadı"`. 1702 kaydın 902'si böyle. Yani TBF **fikstür takvimi olarak kullanılamaz**; tarih ancak maç oynanıp sonuç girilince doluyor. Ayrıştırırken `matchDate` ISO değilse `null` say.
  - Statüye körü körüne güvenme: 1 kayıtta statü 19 olduğu halde tarih, salon ve skor doluydu (U14 E, 6 Kasım, `ANKARA DTY SK` 30-…). "Oynandı" ölçütü olarak `homeTeam.score` ve `awayTeam.score` dolu + `matchDate` ISO koşulunu kullan.
  - 13/14 (çekilme) kayıtlarında saat `T00:00:00`, salon gerçek salon olmayabilir ("Büyük Kolej Spor Salonu").
  - assignr `matchNumber` **yok**; `matchCode` (`BRZ4933`) TBF'nin kendi kodu. Eşleştirme §5.
  - **Skor gecikmesi [Ç]:** 11 Kasım ~10:45'te 9 Kasım (Pzt) maçlarının 13'ü skorluydu; 10 Kasım (Sal) akşam maçlarının hiçbiri yoktu (yalnız 1 çekilme kaydı). Yani TBF **≥ ~14 saat, tipik olarak 1–2 gün** geriden geliyor; ankarabasket (§2.1) daha hızlı.
- **Önerilen yenileme sıklığı:** Lig başına günde 1 (gece). Yalnız kullanıcının hakemlik yaptığı liglerin `ActivityId`'leri çekilsin (tipik 2–4 lig). İlk kurulumda `WeekFilter=*`, sonra yalnız güncel hafta ±1.

### 3.4 Puan durumu

- **Uç:** `GET /api/League/get-standings-table?leagueId=<faaliyetId>` (güncel hafta) **[Ç]**; `&hafta=3` geçmiş hafta **[Ç]**
- **Şema [Ç]:** `data[]` = grup listesi:
  ```json
  { "grup": "U 14 ERKEK B LİGİ F GRUBU", "weeksByGroup": ["4","3","2","1"],
    "standings": [{ "takimIslemId": 269615, "faaliyetAltAlanId": 22328, "takimAdi": "ÇAYYOLU AKADEMİ (A)",
       "grup": "…", "hafta": 4, "sira": 1, "o": 4, "g": 4, "m": 0, "a": 247, "y": 113, "puan": 8,
       "icP": "0", "icA": "0", "toA": "134", "ihrac": 0, "teamLogo": "", "tiedRows": [] }] }
  ```
  `o`=oynanan, `g`/`m`=galibiyet/mağlubiyet, `a`/`y`=atılan/yenen, `toA`=toplam averaj (string), `icP`/`icA`=ikili puan/averaj, `ihrac`≠0 ihraç.
- **Örnek dosya:** `samples/tbf/standings-22328.json`, `standings-22332.json`
- **Tuzaklar:** Grup adı biçimi tutarsız: `"U 14 KIZ A LİGİ GRUBU"`, `"U16 KIZ A"`, `"U18 KIZ A LİGİ"`, `"ANKARA BÜYÜK ERKEKLER A LİGİ"` (tek gruplu liglerde harf yok, U ile sayı arasında boşluk bazen yok). `teamLogo` çoğunlukla boş. Gruplar arası hafta farklı olabilir (A ligi 7. hafta, C ligi 3. hafta).
- **Önerilen yenileme sıklığı:** Günde 1; ekran açılışında 6 saatten eskiyse.

### 3.5 Maç ayrıntısı, çeyrek skoru, canlı skor

- `GET /api/Match/mac-header?matchId=<id>` **[Ç]** → `matchDateTime`, `leagueName` (**grup adı**), `homeTeam{teamId,teamName,logo}`, `homeTeamScore`(int), `location`, `mainReferee`, `firstAssistantReferee`, `secondAssistantReferee`, `temsilciAdi`, `matchStatusId`, `matchStatus`, `matchCode`, `hasUzatma`. Yerel lig maçında hakem alanları **boş string**. Örnek: `samples/tbf/mac-header-350554.json`
- `GET /api/Match/mac-ozet?matchId=` **[Ç]** → `homeTeamScore: []`, `awayTeamScore: []` (çeyrek dizileri) yerel lig maçında **boş**. Örnek: `samples/tbf/mac-ozet-350554.json`
- `mac-istatistik`, `mac-leader`, `get-match-report-with-players`, `game-flow` **[Ç]** → yerel lig maçında hepsi boş/sıfır.
- **Çeyrek skoru: YOK.** **Canlı skor: YOK.** Kanıt: 1702 Ankara maç kaydının 1702'sinde `genuisId` boş (canlı istatistik sağlayıcı bağlantısı yok), `game-flow.events` boş, `hasUzatma` hepsinde `false`; ankarabasket yalnız final skor + `forfeit` taşıyor; assignr'da skor alanı yok. (TBF'de bir SignalR `…/hub` ucu var ama üst ligler için **[Çıkarım]**; denenmedi.)
- `GET /api/Team/get-teams-by-leauge?leaugeId=<id>` **[Ç]** (yazım hatası uçta aynen var) → `teamProcessId, teamId, teamName, teamLogoUrl, hexRenkKodu1/2`. Örnek: `samples/tbf/teams-22332.json`
- `GET /api/Match/get-daily-matches?Date=…&City=…` → boş döndü; doğru parametre adları **bulunamadı**.

### 3.6 Kotlin iskeleti (TBF)

```kotlin
@Serializable data class TbfEnvelope<T>(val data: T? = null, val isSuccess: Boolean = false, val message: String? = null)
@Serializable data class TbfTeam(val id: Double, val name: String, val logoUrl: String = "", val score: String = "", val isHome: Boolean)
@Serializable data class TbfMatch(
    val matchId: Double, val activityId: Double, val matchDate: String, val matchDateOnly: String, val matchTime: String,
    val week: String, val halfValue: String? = null, val homeTeam: TbfTeam, val awayTeam: TbfTeam,
    val matchStatusId: Double, val salonAdi: String = "", val matchCode: String = "") {
  val dateTime: LocalDateTime? get() = runCatching { LocalDateTime.parse(matchDate) }.getOrNull()   // "10. Hafta" -> null
  val homeScore: Int? get() = homeTeam.score.toIntOrNull()
  val isForfeit get() = matchStatusId.toInt() in setOf(8, 9, 13, 14)
}
val json = Json { ignoreUnknownKeys = true; isLenient = true; coerceInputValues = true }
```

---

## 4. Lig kataloğu ve assignr ↔ TBF eşlemesi

Makinece okunur tablo: **`samples/lig-eslesme.json`** (81 satır: 59 `eslesti`, 7 `kismi`, 15 `eslesmedi`).

**Kural [Ç — 188 eşleşen maçın tamamında lig/grup bu kuralla doğrulandı, 1 istisna aşağıda]:**

1. assignr `league` = `"<taban> <sev>"` → son harf `sev` (A/B/C). Taban → TBF faaliyet id:
   `U 14 ERKEK`→22328, `U 14 KIZ`→22329, `U 16 ERKEK`→22330, `U 16 KIZ`→22331, `U 18 ERKEK`→22332, `U 18 KIZ`→22333, `BÜYÜK ERKEK`→22320.
2. assignr `groupName` → baştaki `"Grup "` at → harf.
3. TBF grup adı = `"<taban> <sev> LİGİ <harf> GRUBU"`. Karşılaştırmadan önce iki tarafta da `U\s*(\d+)` → `U$1` yap, `ANKARA ` ve `LİGİ`/`GRUBU` sözcüklerini at.
4. Tek gruplu ligler (harf TBF adında yok): `BÜYÜK ERKEK A/A` → `ANKARA BÜYÜK ERKEKLER A LİGİ`; `U 14 KIZ A/A` → `U 14 KIZ A LİGİ GRUBU`; `U 16 KIZ A/A` → `U16 KIZ A`; `U 18 KIZ A/A` → `U18 KIZ A LİGİ`; `U 18 KIZ B/A` → `U18 KIZ B LİGİ`.

**Eşleşmeyen / kısmi (açıkça):**

| assignr | Durum |
|---|---|
| `OKUL` (`GENÇ ERKEKLER A`, `GENÇ KIZLAR A`, `YILDIZ ERKEKLER`, `YILDIZ KIZLAR`; grup `-`) | **Eşleşmedi.** TBF/ankarabasket'te puan durumu ve skor yok. |
| `AGL` (`U10/U11/U12` × `PREMİUM/PREMIUM/ELİT/SÜPER`) | **Eşleşmedi.** TBF 22322–22327 boş. Skor kaynağı yok. |
| `ABL`, `AA` | **Eşleşmedi.** Skor kaynağı yok. |
| `BÜYÜK KADIN / A` | Kısmi: TBF 22321 var ama 55 maçın hepsi tarihsiz, tablo boş. |
| `U 21 ERKEK / A,B` | Kısmi: TBF 22336 "Ümit Erkekler" (`leagueName` = "U 21 ERKEK A GRUBU") seçildi **[Çıkarım]**; tablo boş. |
| `U 16/U 18 ERKEK ÖN ELEME / A,B` | Kısmi: TBF 23542 / 23543; tablo yok (eleme bitti). |
| `U 16 KIZ / A,B,C` (season-teams'te sev harfsiz) | TBF `U 16 KIZ B LİGİ A/B/C GRUBU` ile eşlendi **[Çıkarım]** — assignr'da bu ligden maç 2 haftalık pencerede görülmedi, assignr'ın bu ligi nasıl adlandırdığı doğrulanmadı. |
| `U 18 ERKEK C / Grup B` (`ANK-U18E-C-2026-070`) | Veri tutarsızlığı: aynı maçın takımı TBF'de `C GRUBU`'nda. Tek örnek. |

Listeleyen uçlar: TBF `filters-results` (§3.1, faaliyet id'leri) + ankarabasket `season-teams` (§2.4, assignr adlarıyla lig/grup/takım). ankarabasket `/puan-durumlari` sayfası yalnız 7 lig id'sini bağlıyor.

---

## 5. Maç eşleştirme (assignr/ankarabasket ↔ TBF)

- **ankarabasket ana sayfa ↔ assignr:** doğrudan `code == matchNumber`. 9–13 Kasım'daki 58 maçın 58'i assignr'da var **[Ç]**. → **Yakın tarihli skor için eşleştirme gerekmez.**
- **TBF ↔ assignr:** TBF'de `matchNumber` **yok** **[Ç]**. Anahtar: **faaliyet id + tarih + (saat + salon) + takım adı benzerliği**.

### 5.1 Yazım farkları (gerçek örnekler) **[Ç]**

| assignr | TBF |
|---|---|
| `ANKARA MAGIC HANDS SK` | `ANKARA MAGIC HANDS` |
| `GENÇ MAGIC HANDS SK (A)` | `GENÇ MAGİC HANDS (A)` (I ↔ İ) |
| `SPORTS A ACADEMY SK (B)` | `SPORTSA ACADEMY  (B)` (boşluk, çift boşluk) |
| `ANKARA DİNAMİK SK` | `DİNAMİK SPOR` |
| `ANKARA MAVİ BİRLİK SK` | `MAVİBİRLİK` |
| `OGM ORMAN SK (B)` | `OGM ORMANSPOR (B)` |
| `BAŞKENT ANKA SK` | `BAŞKENT ANKASPOR` |
| `ÇAĞDAŞ BATI SK (A)` | `ÇAĞDAŞ BATI İHTİSAS (A)` |
| `GB ACADEMY SK (B)` | `GLOBAL BASKETBALL ACADEMY SPOR (B)` / `GLOBAL BASKETBOL ACADEMY SK (B)` |
| `TÜRK TELEKOM ANKARA SK` | `ANKARA TÜRK TELEKOM` (sözcük sırası) |
| `ANKARA ÜNİVERSİTESİ GELİŞTİRME VAKFI ÖZEL OKULLARI SK` | `ANKARA ÜNİVERİTESİ GEL. VAK. Ö.O. SK` |
| `ŞEHİT CENGİZ POLAT SK (B)` | `ŞEHİT CENGİZ POLAT İMAM HATİP ORTA OKULU  (B)` |
| `ERYAMAN YILDIZLARI BASKETBOL SK` | `ERYAMAN YILDIZLARI  (B)` (takım eki bir tarafta yok) |
| Salon `MEB SPOR SALONU` | `MEB Beşevler Spor Salonu` |
| Salon `SİNCAN SPOR KOMPLEKSİ` | `Sincan Spor Salonu` |
| Salon `ANKARA SPOR SALONU KÜÇÜK` | `Ankara Spor Salonu (Küçük)` |
| Salon `TAHA AKGÜL SPOR SALONU` | `Ankara Taha Akgül Spor Salonu` / `Taha Akgül Spor Salonu` |

Ham adların birebir eşit olduğu maç: 192'de yalnız 5.

### 5.2 Önerilen normalizasyon

```
fold(s):      İ,ı,i → I ; büyük harf ; ÇĞÖŞÜ → CGOSU
hallKey(h):   fold → harf/rakam dışını boşluk yap → {SPOR, SALONU, KOMPLEKSI, ANKARA, BESEVLER} sözcüklerini at
              (sonuç: MEB, KUCUK, ALTINDAG, TAHA AKGUL, SINCAN, SINAN SAMIL SAM)
teamKey(n):   fold → sondaki "(A)"/"(B)" ekini ayır (suffix) → noktalama at
              → {SK, SPOR, KULUBU, GSK, S, K} sözcüklerini at
              → takma ad: GB → GLOBAL BASKETBALL ; BASKETBOL → BASKETBALL
              → 6 harften uzun ve SPOR ile biten sözcükten SPOR'u kes (ORMANSPOR → ORMAN)
              → boşluksuz birleştir
sim(a,b):     suffix'ler ikisi de dolu ve farklı → 0
              key'ler eşit → 1.0 ; biri diğerini içeriyor (≥4 harf) → ≥0.85
              değilse Ratcliff/Obershelp (difflib) ya da normalize Levenshtein oranı
              suffix yalnız bir tarafta varsa −0.15 ceza
```

### 5.3 Algoritma

1. assignr `league` → TBF `ActivityId` (§4). Adaylar = o faaliyette `matchDateOnly == date` olan tarihli maçlar.
2. Her aday için `s = min(sim(teamA, home), sim(teamB, away))`; `slot = (matchTime == time && hallKey eşit)`; skor = `s + 0.3·slot`.
3. En iyi adayı kabul et, eğer `s ≥ 0.70` **veya** (`slot` ve `s ≥ 0.45`). Yoksa "eşleşmedi" (kullanıcıya elle seçtir / ertesi gün yeniden dene).
4. Kabul edilen `matchNumber ↔ tbfMatchId` çiftini kalıcı sakla (bir daha eşleştirme yapma).

Kotlin'de benzerlik için kütüphane gerekmez; 30 satırlık Levenshtein yeterli. Türkçe büyük harf için `uppercase(Locale("tr"))` **kullanma** — önce elle `İ/ı/i → I` çevir, sonra `Locale.ROOT`.

### 5.4 Gerçek deneme sonucu **[Ç]**

Betik: `samples/mac-eslesme-testi.py`, çıktı: `samples/mac-eslesme-testi.json` (188 eşleşme; her satırda assignr + TBF alanları, skor, `teamSim`, `slotEqual`, `tbfGroup`).

| Küme (BÖLGE, tarihi ≤ 9 Kasım olan = oynanmış) | Maç | Slot+takım | Yalnız takım (saat/salon farklı) | Kaçan | İsabet |
|---|---|---|---|---|---|
| **7–13 Kasım haftası** (7, 8, 9 Kasım) | 78 | 76 | 0 | 2 | **%97,4** |
| 31 Ekim–6 Kasım haftası | 114 | 109 | 3 | 2 | %98,2 |
| Toplam | 192 | 185 | 3 | 4 | %97,9 |

- Yalnız "tarih+saat+salon" anahtarıyla (takım adına bakmadan) isabet 182/192 (%94,8) ve **6 yanlış eşleşme riski** (aynı salonda saatleri yer değiştirmiş maçlar) → takım benzerliği şart.
- Kaçan 4 maç: 3'ünde bir takım ligden çekilmiş/maç oynanmamış (TBF'de başka tarihte `13/14` statüsüyle ya da hiç yok), 1'i assignr'da çift kayıtlı ertelenen maçın eski kaydı. Yani **gerçekten oynanmış maçlarda yanlış/eksik eşleşme görülmedi**; yanlış pozitif 0 (188 eşleşmenin en düşük benzerliği 0,65, elle kontrol edildi).
- "Yalnız takım" 3 maç: saat TBF'de farklı girilmiş (14:00↔16:00) veya aynı salonda iki maçın saati takas edilmiş.

---

## 6. Ücret tarifesi (2026-2027)

### 6.1 Bulunan resmî belge: "2026-2027 Sezonu Basketbol Özel Müsabakalarında Uygulanacak Görevli Ücretleri"

- **Kaynak:** `https://www.ankarabasket.org.tr/mevzuat` → "2026-2027 Sezonu Özel Müsabaka Görevli Ücretleri" → `https://www.ankarabasket.org.tr/api/files/file/56BC342B4D7948E1BEDF65D9D831A050_ozel-musabaka-ucretleri.pdf` **[Ç — indirildi, metni okundu]**. Aynı adlı belge TBF'de "Merkez Hakem Kurulu" doküman kategorisinde de listeli (`…/dokuman/12D0852D375C43E0BE711F76F121EB00_ozel-musabaka-ucretleri.pdf`; içeriği ayrıca karşılaştırılmadı).
- **Tarih:** PDF oluşturma damgası **10 Temmuz 2026**. Belgenin altındaki "… tarih ve … no'lu TBF Yönetim Kurulu Toplantısı Kararı" satırında tarih/sayı **boş bırakılmış**.
- **Örnek dosya:** `samples/ucret/2026-2027-ozel-musabaka-gorevli-ucretleri.pdf` ve `.txt`
- **B. İl içi faaliyetler (maç başı):**

  | Görevli | Büyükler (18+), şirketler arası / reklam / sponsorlu — Erkek | — Kadın | Kulüp altyapı takımları (E/K) | Üniversite ve okullar arası, kamu yararına kurum / STK sosyal sorumluluk (E/K) |
  |---|---|---|---|---|
  | Hakemler | 3.250 TL | 2.600 TL | 1.700 TL | 1.700 TL * |
  | Masa görevlileri | 1.100 TL | 1.100 TL | 850 TL | 850 TL * |
  | Temsilci ** | 1.400 TL | 1.250 TL | 1.100 TL | 1.100 TL * |

  \* "Valilik, Kaymakamlık ve Milli Eğitim'in düzenlediği 18 yaş altı karşılaşma ve turnuvalarda tüm görevlilere yukarıdaki tarifenin **1/2'si** ödenir." → hakem 850 TL, masa 425 TL.
  \** Yalnız turnuvalarda görevlendirilir.
- **A. Federasyon faaliyetleri** (özel maç/turnuva): Hakem BSL 14.000 / KBSL 9.500 / TBL 8.500 / TKBL 5.000 / TB2L 5.000 / BGL 4.250 / EBBL-KBBL 4.250 TL; masa görevlisi 1.700 (BSL, KBSL) / 1.400 TL (diğer). Not: farklı lig takımları arasında üst lig rayici; il dışından gelen hakemin yol-konaklaması ev sahibi kulübe ait.
- **C. Açık hava turnuvaları:** seans (≤ 6 saat) başına hakem 4.250, masa 2.600, temsilci 3.500 TL.
- **Belgede olmayanlar:** Başhakem / yardımcı hakem ayrımı **yok** (tek "Hakemler" satırı). Yaş kategorisi (U18/U16/U14/U12) ayrımı **yok** (tek "Kulüp Altyapı Takımları" sütunu). İl içi ulaşım ödeneği, stopaj/kesinti **yok**.

### 6.2 matchType → tarife eşlemesi

| matchType | Uygulanabilir satır | Tutar (hakem / masa) | Güven |
|---|---|---|---|
| **BÖLGE** (resmî yerel lig: Büyükler, U18, U16, U14) | Bu tarife **kapsamıyor** | **bulunamadı** | — |
| **AGL** (özel turnuva, U10–U12 kulüp altyapı) | "Kulüp Altyapı Takımları" | 1.700 / 850 TL | [Çıkarım] — bültende "Özel Turnuva (AGL)" olarak etiketli; organizasyonun fiilen bu tarifeyi ödediği doğrulanmadı |
| **ABL** (özel turnuva, yetişkin, sponsor adlı) | "Büyükler … sponsorluk alınan" Erkek | 3.250 / 1.100 TL | [Çıkarım] |
| **AA** (kurum turnuvası) | Büyükler şirketler arası (3.250 / 1.100) **ya da** kamu yararına kurum (1.700 / 850) | belirsiz | [Çıkarım] — hangisi olduğu doğrulanmadı; maçlar 35 dk aralıklı (3x3 olabilir) |
| **OKUL** (MEB okul maçları) | Özel müsabaka sayılırsa: okullar arası × ½ = 850 / 425 TL | belirsiz | [Çıkarım] — okul sporları resmî GSB faaliyeti olarak İl Müdürlüğü'nce ödeniyor olabilir; **doğrulanmadı** |

### 6.3 BÖLGE (resmî yerel lig) ücreti — **bulunamadı**

- **Kim öder (resmî dayanak) [Ç — taranmış PDF'ten gözle okundu]:** TBF **Hakemler Talimatı** (TBF mevzuat listesinde yürürlük 09.07.2025; `https://www.tbf.org.tr/sitefiny-tbf-media/dokuman/BB68C718D5804F8ABF7236BD995452D2_hakemler-talimati.pdf`) **Madde 29/(4):** "Yerel Lig Faaliyetlerinde görev yapacak müsabaka görevlilerinin müsabaka tazminatları, yol ve konaklama giderleri **Genel Müdürlük mevzuat ve uygulamaları kapsamında İl Müdürlükleri bütçesinden ödenir.** …" (fıkra 20. sayfada devam ediyor; devamı okunmadı). Md. 29/(2): lig/özel müsabaka tazminatları MHK önerisi + TBF Yönetim Kurulu onayıyla **sirkülerle** belirlenir. Sayfa görüntüleri: `samples/ucret/hakemler-talimati-md29-s19-{a,b}.png`.
- Sonuç: BÖLGE maç ücretini TBF değil **Ankara Gençlik ve Spor İl Müdürlüğü** (GSB mevzuatı) belirliyor/ödüyor. 2026-2027 için kategori bazlı (Büyükler/U18/U16/U14, başhakem/yardımcı/masa) **tutar tablosu hiçbir açık kaynakta bulunamadı**: ankarabasket `/mevzuat` (12 belge), TBF `get-mevzuat` (46 talimat), TBF `get-documents` (82 belge), TBF Ankara `dokumanlar`/`sirkulerler`, iki web araması.
- Önceki sezon tutarı da **bulunamadı**. Uydurma rakam yazılmadı.
- **Yol/ulaşım ödeneği:** il içi için **bulunamadı**. (Md. 29/(1): yalnız ikamet edilen il dışına görevlendirmede ulaşım-konaklama karşılanır.)
- **Stopaj/kesinti:** resmî kaynaktan **doğrulanamadı**. Web aramasında ikincil kaynaklar "amatör spor müsabakalarını yöneten hakemlere ödenen ücretlerin gelir vergisinden istisna olduğunu (GVK md. 29), basketbolda en üst ligin istisna dışı olduğunu" yazıyor — birincil metin okunmadı, **doğrulanmamış** sayılmalı.
- **Uygulama tasarımı için öneri:** Ücretler **koddan değil, kullanıcının düzenleyebildiği bir tablodan** gelsin: anahtar `(matchType, yaşKategorisi, rol)`; AGL/ABL/AA/OKUL için §6.2 değerleri "öneri" olarak ön-doldurulsun, BÖLGE satırları boş başlasın ve kullanıcı kendi bordrosundaki tutarı girsin.

---

## 7. Kısaltmalar (`matchType`)

| Değer | Anlam | Kanıt |
|---|---|---|
| `BÖLGE` | Ankara yerel (il) ligi resmî müsabakaları — TBF "İl Ligleri" | ankarabasket bültenleri: "1-30 Kasım 2026 Bölge Fikstürü", `competitionType: local-league` ("YEREL LİG" sekmesi); tüm BÖLGE maçları TBF faaliyetleriyle eşleşiyor **[Ç]** |
| `OKUL` | MEB okul sporları basketbol maçları (Genç/Yıldız, okul takımları) | Bülten: "2026-2027 Sezonu MEB Okul Maçları Fikstürü" (`school`); takım adları lise/ortaokul **[Ç]** |
| `AGL` | **Ankara Gelişim Ligi** ("Pizza Bulls Ankara Gelişim Ligi Minikler", U10–U12; Premium/Elit/Süper kademeleri) | Bülten `customCompetitionType: "Özel Turnuva (AGL)"` **[Ç]** |
| `ABL` | **Ankara Basketbol Ligi** ("SkorAltyapı Ankara Basketbol Ligi") — özel yetişkin ligi | Bülten `"Özel Turnuva (ABL)"`; Google Sheet başlığı "SKORALTYAPI ANKARA BASKETBOL LİGİ" **[Ç]** |
| `AA` | **Anadolu Ajansı Turnuvası** | **[Çıkarım, güçlü]**: bültende "Anadolu Ajansı Turnuvası 2026-2027" (`threexthree` sekmesi) var; AA maçlarının takım adları "Basket AAuthority", "PhotoBulls", "On the Record"; `matchNumber` `AA-29`. Doğrudan "AA = …" yazan bir kaynak görülmedi. |
| (masa ucunda) `TBL`, `KBSL`, `TKBL`, `TB2L`, `BSL`, `Eurocup`, `DEP-…` | Ulusal/deplasmanlı lig ve Avrupa maçlarında Ankara masa görevlileri | TBF ücret belgesindeki lig kısaltmaları; `DEP` = "Deplasmanlı Lig" **[Çıkarım]** |

Not: `ABEL` (matchNumber `ANK-ABEL-A-…`) = "Ankara Büyük Erkekler Ligi" (`league: BÜYÜK ERKEK A`) **[Çıkarım; ankarabasket haberinde "ABEL B Ligi" geçiyor]**.

Ek fikstür kaynağı (skor içermez): AGL/ABL/AA/Ünilig bültenleri herkese açık Google Sheet; `https://docs.google.com/spreadsheets/d/<id>/export?format=csv` girişsiz CSV veriyor **[Ç — ABL ve Ünilig sayfalarında denendi]**. Sütunlar: `LİG, TARİH ("Perşembe, Kasım 12, 2026"), SALON, SAAT, A TAKIMI, B TAKIMI, BAŞ HAKEM, 1. YARDIMCI, 2. YARDIMCI, MASA GÖREVLİSİ…`. Sheet id'leri `fixture-bulletins.externalUrl` içinde. Biçim sayfadan sayfaya değişiyor; uygulama için **önerilmez**.

---

## 8. Doğrulanmayanlar ve riskler

**Doğrulanmayanlar**

1. **assignr verisinin değişim sıklığı:** yalnız ~15 dk arayla iki çekim yapıldı (özdeş). Atamaların haftanın hangi günü/saatinde yayımlandığı, hafta devrinin ne zaman olduğu (Cuma gece mi Cumartesi mi) **gözlenmedi**. İlk hafta sık (saatlik) sorgulayıp gövde hash'i değişim zamanlarını kaydetmek, sonra aralığı ayarlamak gerekir.
2. **Skor giriş gecikmesi (dakika düzeyi):** ankarabasket'te "ertesi sabah mevcut", TBF'de "ertesi sabah yok, 2 gün sonra var" dışında ölçüm yok.
3. **ankarabasket `forfeit: true`** örneği pencerede yoktu; hükmen maçta `score` alanının nasıl geldiği görülmedi.
4. **ankarabasket ana sayfasının tarih penceresi** (bugün−2…+4) tek gözleme dayanıyor; hafta sonu farklı olabilir. Pencereyi kaydıran parametre aranmadı (kodda görülmedi).
5. **Kulüp sayfası skor yönü** (ev–deplasman mı) ve "son 6" sınırı tek kulüpte gözlendi.
6. **BÖLGE maç ücretleri**, il içi yol ödeneği, stopaj: bulunamadı (§6.3). AGL/ABL/AA/OKUL'un özel müsabaka tarifesine tabi olduğu çıkarım.
7. **`referee1` = başhakem** varsayımı dolaylı kanıta dayanıyor.
8. `U 16 KIZ` (harfsiz) ve `U 21 ERKEK` lig eşlemeleri çıkarım (§4). OKUL/AGL/ABL/AA için skor ve puan durumu kaynağı **yok**.
9. Payload `where[...]` süzgeçleri, TBF `TeamId`/`HalfValue`/`AgeGroup`/`Gender` parametreleri koddan okundu, çağrılmadı. TBF `get-daily-matches` parametreleri bulunamadı.
10. Wayback CDX servisi çevrimdışıydı; yalnız `available` API'siyle "anlık görüntü yok" doğrulandı.
11. Playwright bu makinede kurulu değildi (`require('playwright')` başarısız; `/opt/pw-browsers` yok). Ağ izleme yerine JS paketleri okunup uçlar `curl` ile doğrulandı; tarayıcıda yalnız çalışma anında oluşan bir çağrı varsa kaçmış olabilir (ankarabasket JS'inde `fetch` yalnız `/api/hit` ve `/api/push`).

**Riskler**

- **Hiçbiri belgelenmiş/taahhütlü API değil.** assignr ve ankarabasket aynı geliştiriciye ait (immensus); TBF ucu sitenin iç API'si. Şema değişimine karşı: `ignoreUnknownKeys`, her kaynak için ayrı `try/catch`, son başarılı yanıtın diskte saklanması, ayrıştırma hatasında kullanıcıya "veri güncellenemedi (tarih)" gösterimi.
- **TBF `apiHashing`** açılırsa uç yolları değişir (§3). **TBF sayı biçimi** (`22328` ↔ `22328.0`) ve **tarih alanına hafta metni** yazılması en olası çökme nedenleri.
- **ankarabasket flight ayrıştırma** kırılgan (§2.1); Next.js sürüm yükseltmesi biçimi bozabilir.
- **robots.txt:** ankarabasket `/api` (Payload) yasaklı → gömülü katalog tercih et; HTML sayfaları ve `/api/media/file/` serbest. assignr `robots.txt` → 302 (yok). TBF API alt alanının robots'u kontrol edilmedi.
- **Nezaket/oran sınırı:** hiçbir uçta rate-limit başlığı görülmedi; Cloudflare arkasındalar. Uygulama tanımlayıcı bir `User-Agent` göndermeli, eşzamanlı istek atmamalı, üstel geri çekilme uygulamalı. Tek kullanıcı için günlük toplam < 50 istek yeterli.
- **Kişisel veri:** assignr yanıtları tüm hakem ve masa görevlilerinin ad-soyadlarını içeriyor; uygulama yalnız kullanıcının kendi kayıtlarını ve aynı maçtaki ekip arkadaşlarını saklamalı, toplu arşivi cihaz dışına çıkarmamalı.
- **Geçmiş yok:** kurulumdan önceki (ve 2 haftadan eski) atamalar geri getirilemez; istatistikler kurulum tarihinden başlar. Kullanıcıya elle geçmiş maç ekleme ekranı gerekebilir.
- **`matchNumber` çift kayıt** ve BÖLGE dışı numaraların saatle tutarsızlığı (§1.1) yerel anahtar tasarımını etkiler.
