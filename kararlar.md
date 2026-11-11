---
tur: kararlar
etiketler:
  - kararlar
  - mimari
  - ikinci-beyin
olusturma: 2026-11-11
guncelleme: 2026-11-11
---

# kararlar.md — Mimari ve Operasyonel Karar Kaydı

Bağlantılar: [[HARITA]] · [[hafiza]] · [[dersler]] · [[simdi]]

| Tarih | Karar | Neden | Değerlendirilen Alternatifler |
|---|---|---|---|
| **2026-10-20** | `flugelserver` üzerinde tüm uygulama verilerini `/srv/appdata/<uygulama>` ve Compose yığınlarını `/opt/stacks/<uygulama>` altında standartlaştırma ([[flugelserver-genel-mimari]]) | Eski `/arrapps` dağınıklığını bitirmek ve `uygulama-yedek.py` ile tek tip gece yedeği almak | `/arrapps` altında devam etmek (bakımı zor olduğu için reddedildi) |
| **2026-10-20** | Yerel LLM olarak Ollama'da yalnız `qwen3.5:4b` modelini tutma (`40 GB -> 3,1 GB`) | GTX 1660 Ti (6 GB VRAM) belleğine tam sığması ve `flugel-akis` + `ai-gozcu` için hızlı yanıt vermesi | 10 farklı büyük model tutmak (disk ve VRAM darboğazı yarattı) |
| **2026-11-11** | **Düdük** uygulamasında Room/KSP/Hilt yerine atomik JSON (`arsiv.json`) + `DataStore` kullanma ([[yerel-arsiv-ve-senkronizasyon]]) | AGP 9.4.1 + Kotlin 2.3.21 ile KSP uyumsuzluklarını önlemek ve arşivi taşınabilir tutmak | Room SQLite + KSP (reddedildi) |
| **2026-11-11** | **Düdük** uygulamasında WorkManager sürümünü `2.10.5`'te sabitleme ([[android-arac-zinciri-ve-mimari]]) | WorkManager 2.11+ sürümlerinin bazı API 34 cihazlarda `JobScheduler.forNamespace()` nedeniyle açılışta çökmesi | WorkManager 2.11+ (reddedildi) |
| **2026-11-11** | `BÖLGE` yerel lig maç ücretini `0 TL` yerine `null` ("ücret tanımsız") başlatma ([[hakem-ucret-tarifesi-2026-2027]]) | İl Müdürlüğü bordro tutarının açık kaynaklarda yer almaması ve `0 TL` saymanın toplam kazancı bozması | Sabit tahmini tutar gömmek veya `0 TL` saymak (reddedildi) |
| **2026-11-11** | `duduk.gokalpgoksu.com` adresini `flugelserver` üzerinde `akis.yml` (`cloudflared-akis.service`) tüneline bağlama | `config.yml` tünelinin Cloudflare Zero Trust tarafından uzaktan yönetildiği için yerel satırları yok sayması | `config.yml` (uzaktan yönetildiği için çalışmadı) |
| **2026-11-11** | Tüm projeler için tek bir merkezi **İkinci Beyin Vault'u** (`HARITA.md` + `notlar/kisiler/projeler` + `raw/wiki` + `brain.py`) kurma ve Nextcloud `files/Obsidian/flugel-beyin/` ile eşitleme | Her oturumda bağlamı sıfırdan anlatmayı bitirmek ve model halüsinasyonlarını `brain.py lint` ile deterministik olarak yakalamak | Proje başına ayrı not klasörleri veya yalnız RAG (reddedildi) |
| **2026-11-05** | FLUGEL Akış'ı `akis.gokalpgoksu.com` üzerinden **şifresiz** açma; Android kabuğunu bu adrese bağlama ([[notes/flugel-akis-mobil-uygulama]]) | Kullanıcı okulda ve evde Tailscale olmadan kullanmak istedi; "şifre olsa ne yarar zaten aç hemen" | giris nginx üzerinden basic auth + APK'ya gömülü kullanıcı (kullanıcı istemedi); Tailscale serve `:8443` (çalışmıyordu) |
