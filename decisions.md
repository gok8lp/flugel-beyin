# Karar Günlüğü (Decision Log)

> Neden öyle karar verildiğinin kaydı. [[map]] ile birlikte her zaman odaktadır.

## 2026-11-11 — Düdük Mimari Kararları

1. **Room / KSP / Hilt Kullanmama Kararı (`ArsivDeposu.kt`):**
   - **Karar:** Kalıcılık için SQLite/Room yerine atomik JSON dosyası (`arsiv.json`, `.tmp` + `.bak`) ve `DataStore<Preferences>` seçildi.
   - **Neden:** AGP 9.4.1 + Kotlin 2.3.21 araç zincirinde KSP sürüm uyumsuzluklarını tamamen ortadan kaldırmak, şema göçlerini (`migration`) basitleştirmek ve arşivin insan tarafından okunabilir / yedeklenebilir tek bir JSON olmasını sağlamak.

2. **WorkManager Sürümünü `2.10.5`'te Sabitleme (`libs.versions.toml`):**
   - **Karar:** WorkManager `2.11+`'a yükseltilmedi, `2.10.5`'te tutuldu.
   - **Neden:** WorkManager 2.11+ bazı üretici API 34 cihazlarında `JobScheduler.forNamespace()` çağrısı nedeniyle uygulama açılışında çöküyor (`koharia-reader` projesinde doğrulanmış bulgu).

3. **Birleşik Maç Anahtarı (`matchNumber|date|time`):**
   - **Karar:** Maçların birincil anahtarı yalnız `matchNumber` değil, `matchNumber|date|time` yapıldı.
   - **Neden:** `assignr` üzerinde ertelenen maçlar eski kaydı silinmeden aynı `matchNumber` ile ikinci kez yayınlanıyor (`ANK-U16E-C-2026-153`).

4. **`BÖLGE` Yerel Lig Ücretini `null` ("Ücret Tanımsız") Başlatma (`KazancHesaplayici.kt`):**
   - **Karar:** `BÖLGE` maçlarının varsayılan ücreti `0 TL` değil `null` yapıldı.
   - **Neden:** Resmi TBF Özel Müsabaka Tarifesi yalnızca özel/ticari/okul turnuvalarını kapsıyor; Gençlik ve Spor İl Müdürlüğü bütçesinden ödenen `BÖLGE` resmi lig ücretleri hiçbir açık belgede yer almıyor. Sıfır saymak aylık/sezonluk toplamı yanıltacağı için "ücret tanımsız" olarak ayrı sayaçta gösteriliyor.

5. **`ankarabasket` `/api` Yerine Gömülü Katalog (`assets/katalog/`):**
   - **Karar:** Uygulama çalışma zamanında `ankarabasket.org.tr/api/*` uçlarına istek atmaz; `season-teams`, `clubs`, `tbf-catalog` ve `venues` verileri APK içine gömüldü.
   - **Neden:** `ankarabasket.org.tr/robots.txt` içinde `Disallow: /api` kuralı bulunuyor.

6. **Cloudflare Tunnel İçin `akis.yml` (`cloudflared-akis.service`) Kullanımı:**
   - **Karar:** `duduk.gokalpgoksu.com` yönlendirmesi `flugelserver` üzerindeki `akis.yml` (`6b1b8388-1ab3-46d2-b895-c865bbc1a480`) tüneline eklendi ve CNAME o tünele yönlendirildi.
   - **Neden:** `config.yml` içindeki `1446d4a9...` tüneli Cloudflare Zero Trust konsolundan uzaktan yönetildiği (`remote management`) için yerel `config.yml` değişikliklerini yok sayıyordu; `akis.yml` ise yerel olarak yönetilen aktif tüneldir.
