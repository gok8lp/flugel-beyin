---
tur: kararlar
etiketler:
  - kararlar
  - mimari
  - ikinci-beyin
olusturma: 2026-11-11
guncelleme: 2026-11-14
---

# kararlar.md — Mimari ve Operasyonel Karar Kaydı

Bağlantılar: [[HARITA]] · [[hafiza]] · [[dersler]] · [[simdi]]

| Tarih | Karar | Neden | Değerlendirilen Alternatifler |
|---|---|---|---|
| **2026-11-14** | flugel-beyin'i **Avenox İkinci Beyin V3.13.0**'a geçirme: V3 hook'ları oturum açılış bağlamını ve her mesajdaki ilgili notları verir; eski `session-start.sh` emekliye ayrıldı; `raw/` salt okunur kuralı, `brain.py` lint ve `post-wiki-edit.sh` korundu; `_arsiv` aramadan çıkarıldı. Önce `beyin-test` klasöründe denendi, oturumlar arası hafıza doğrulandı | Her yeni oturumda bağlamı elle yüklemek yerine otomatik, kaynaklı hatırlama; Claude, Codex ve Antigravity'nin aynı defteri kullanabilmesi | Kendi sistemini sıfırdan yazmak veya Avenox'u forklamak (Gökalp vazgeçti); Jev: önce kapalıydı; aynı gün TypeSafe anahtarıyla **gölge modda** açıldı, ilk testte doğru notları seçti (karar: bir hafta ölç, sonra `on`) |
| **2026-11-13** | Laptopta **hiçbir pencerenin yüzmemesi** (Chrome video PiP hariç tüm pencereler ve özel alanlar gerçek döşeme ile ekranı böler), özel alanlardan normal alana geçince özel alanın otomatik kapanması ve uygulama taşıma hafızası (`~/.local/state/ozel-alan-hafiza`) ([[notlar/laptop-dux-ozellestirme-oturumu-2026-11-13]]) | Pencerelerin üst üste binmesini önlemek ve Super+Ctrl kısayollarıyla tam uyumlu döşeme sağlamak | Yüzen özel alan pencereleri (bırakıldı) |
| **2026-11-12** | Laptopta Noctalia yerine **Dux Modular Shell** kullanma; Caelestia benzeri çerçeve + alttan açılan dock, dock önizlemesi için güncellemeye dayanıklı yama (`~/.local/share/dux-ozel`) ([[notlar/laptop-dux-shell-arayuzu]]) | Arch `extra` paketi, kendi Lua Hyprland ayarına dokunmadan oturuyor, çerçeve/dock Caelestia görünümüne yakın | end-4 (ayarları ezer), Serpantinum (yeni, ses/gamma daemonlarını değiştirir), Noctalia (bırakıldı) |
| **2026-11-12** | Giriş ekranını Noctalia Greeter yerine **greetd + tuigreet** yapma | Noctalia kaldırılınca greeter da gitti; tuigreet hafif ve resmi depoda | Dux greeter |
| **2026-11-12** | Laptopta arayüz olarak **Noctalia v5** kullanma; Hyprland config'i eski PC'den arayüzsüz taşıma ([[notlar/laptop-thinkbook-arch-hyprland-kurulumu]]) | Resmi Arch deposunda, Hyprland Lua config'ini destekliyor, eklenti sistemiyle güncellemeyi bozmadan özelleştirilebiliyor | Caelestia (sabit dikey bar), Ambxst (Lua uyumsuzluk hataları, 127 bağımlılık; denendi ve silindi), end4 |
| **2026-11-12** | Laptopta giriş ekranını SDDM yerine **greetd + Noctalia Greeter** yapma | Noctalia ile aynı görünüm ve duvar kağıdı/renk senkronu | SDDM'de kalmak |
| **2026-10-20** | `flugelserver` üzerinde tüm uygulama verilerini `/srv/appdata/<uygulama>` ve Compose yığınlarını `/opt/stacks/<uygulama>` altında standartlaştırma ([[flugelserver-genel-mimari]]) | Eski `/arrapps` dağınıklığını bitirmek ve `uygulama-yedek.py` ile tek tip gece yedeği almak | `/arrapps` altında devam etmek (bakımı zor olduğu için reddedildi) |
| **2026-10-20** | Yerel LLM olarak Ollama'da yalnız `qwen3.5:4b` modelini tutma (`40 GB -> 3,1 GB`) | GTX 1660 Ti (6 GB VRAM) belleğine tam sığması ve `flugel-akis` + `ai-gozcu` için hızlı yanıt vermesi | 10 farklı büyük model tutmak (disk ve VRAM darboğazı yarattı) |
| **2026-11-11** | **Düdük** uygulamasında Room/KSP/Hilt yerine atomik JSON (`arsiv.json`) + `DataStore` kullanma ([[yerel-arsiv-ve-senkronizasyon]]) | AGP 9.4.1 + Kotlin 2.3.21 ile KSP uyumsuzluklarını önlemek ve arşivi taşınabilir tutmak | Room SQLite + KSP (reddedildi) |
| **2026-11-11** | **Düdük** uygulamasında WorkManager sürümünü `2.10.5`'te sabitleme ([[android-arac-zinciri-ve-mimari]]) | WorkManager 2.11+ sürümlerinin bazı API 34 cihazlarda `JobScheduler.forNamespace()` nedeniyle açılışta çökmesi | WorkManager 2.11+ (reddedildi) |
| **2026-11-11** | `BÖLGE` yerel lig maç ücretini `0 TL` yerine `null` ("ücret tanımsız") başlatma ([[hakem-ucret-tarifesi-2026-2027]]) | İl Müdürlüğü bordro tutarının açık kaynaklarda yer almaması ve `0 TL` saymanın toplam kazancı bozması | Sabit tahmini tutar gömmek veya `0 TL` saymak (reddedildi) |
| **2026-11-11** | `duduk.gokalpgoksu.com` adresini `flugelserver` üzerinde `akis.yml` (`cloudflared-akis.service`) tüneline bağlama | `config.yml` tünelinin Cloudflare Zero Trust tarafından uzaktan yönetildiği için yerel satırları yok sayması | `config.yml` (uzaktan yönetildiği için çalışmadı) |
| **2026-11-11** | **Düdük** maç birincil anahtarını yalnız `matchNumber` yerine birleşik `matchNumber\|date\|time` yapma ([[notlar/assignr-api-yapisi]]) | `assignr` ertelenen maçları eski kaydı silmeden aynı `matchNumber` ile ikinci kez yayınlıyor (`ANK-U16E-C-2026-153`) | Yalnız `matchNumber` anahtarı (çakışma yarattığı için reddedildi) |
| **2026-11-11** | **Düdük** uygulamasının çalışma zamanında `ankarabasket.org.tr/api/*` uçlarına istek atmaması; `season-teams`, `clubs`, `tbf-catalog`, `venues` verilerini APK içine gömülü katalog (`assets/katalog/`) olarak koyma ([[notlar/ankarabasket-rsc-flight-ayristirma]]) | `ankarabasket.org.tr/robots.txt` içinde `Disallow: /api` kuralı bulunması | Çalışma zamanında `/api` uçlarını çağırmak (robots.txt nedeniyle reddedildi) |
| **2026-11-11** | Tüm projeler için tek bir merkezi **İkinci Beyin Vault'u** (`HARITA.md` + `notlar/kisiler/projeler` + `raw/wiki` + `brain.py`) kurma ve Nextcloud `files/Obsidian/flugel-beyin/` ile eşitleme | Her oturumda bağlamı sıfırdan anlatmayı bitirmek ve model halüsinasyonlarını `brain.py lint` ile deterministik olarak yakalamak | Proje başına ayrı not klasörleri veya yalnız RAG (reddedildi) |
| **2026-11-05** | FLUGEL Akış'ı `akis.gokalpgoksu.com` üzerinden **şifresiz** açma; Android kabuğunu bu adrese bağlama ([[notlar/flugel-akis-mobil-uygulama]]) | Kullanıcı okulda ve evde Tailscale olmadan kullanmak istedi; "şifre olsa ne yarar zaten aç hemen" | giris nginx üzerinden basic auth + APK'ya gömülü kullanıcı (kullanıcı istemedi); Tailscale serve `:8443` (çalışmıyordu) |
