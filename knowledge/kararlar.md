---
{
  "kind": "fact",
  "title": "Kararlar — Mimari ve Operasyonel Karar Kaydı",
  "visibility": "internal",
  "tags": [
    "kararlar",
    "mimari",
    "ikinci-beyin"
  ],
  "evidence_refs": [
    "kararlar.md"
  ]
}
---
# Kararlar — Mimari ve Operasyonel Karar Kaydı

Bağlantılar: [[HARITA]] · [[Core]] · [[Threads]] · [[knowledge/dersler]]

> 2026-11-14'te kök dizindeki eski `kararlar.md` dosyasından satır satır taşındı (V3 geçişi). Yeni karar eklerken tabloya tarih, karar, neden ve değerlendirilen alternatiflerle yeni satır ekle.

| Tarih | Karar | Neden | Değerlendirilen Alternatifler |
|---|---|---|---|
| **2026-11-15** | **Hermes** (Nous Research ajanı) flugelserver'da çalışıyor: sağlayıcı OpenAI Codex (ChatGPT aboneliği, `gpt-6-luna` medium), Telegram botu **@flugell_bot** (yalnız Gökalp'in ID'si izinli), ikinci beyin `/opt/data/beyin` salt okunur; konteynerde IPv6 kapalı | Telegram üzerinden sunucudaki kişisel asistan; beyni okuyabilsin ama değiştiremesin | Nous Portal (abonelik/kredi yok); Nous'un barındırılan Telegram botu (token Telegram'da yanıtsızdı, token Nous'tan geçiyordu) |
| **2026-11-15** | Eski sistem tamamen kaldırıldı ve arşivlendi (`_arsiv/eski-sistem/`): `brain.py` lint, `post-wiki-edit.sh`, HUD, eski skill'ler (denetle, ingest, sorgu, haftalik-gozden-gecirme); hafiza/simdi/kararlar/dersler/gelen-kutusu V3'e taşındı. Bu, 2026-11-14 kararındaki "lint ve post-wiki-edit korundu" kısmının yerini alır; `raw/` salt okunur kuralı sürüyor | Tam V3 entegrasyonu, tek sistem | Eski sistemi V3 ile paralel tutmak |
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
| **2026-11-15** | Sunucuda **sanal makine çalıştırılmaz**: libvirt üç VM (mullvad-ts, W11, W11-GPU) kaldırıldı, imajları (~72 GB) kalıcı silindi, libvirt devre dışı | Gökalp: "bu sunucuda sanal makine çalışmasın"; `/` diski 55 GB açıldı, ekran kartı ana sistemde kaldı | VM'leri arşivlemek (VM yedeği zaten yoktu; Gökalp silmeyi onayladı) |
| **2026-11-15** | Flugel Manga testi/APK derlemesi **GitHub Actions'ta kalır**; Forgejo yalnız sunucunun altyapı kodunu (`flugel-altyapi`) tutar | Sunucuda Android derlemesi için bellek yok (swap dolu), ayrı test VM'i de kaldırıldı | Forgejo Runner + test VM'i |
| **2026-11-15** | Hermes'e **sınırlı onarım**: `flugel-onarim` kuyruğu (izin listesi, yalnız `restart`, saatte 6); Docker soketi ve sudo verilmez | Prompt injection riski; Hermes yalnız `/opt/data` üzerinden host ile konuşur | Hermes'e Docker/sudo vermek |
| **2026-11-15** | Yeni uygulamalar (17) yalnız Tailscale'den; Funnel eklenmez. Tailscale girişi (`tsidp` OIDC) destekleyenlerde **ek giriş yöntemi**, yerel giriş açık kalır | Kilitlenme riski; kullanıcı "hızlı giriş" istedi | Yerel girişi kapatmak |
| **2026-11-15** | Okul (OBS/ALMS) takip otomasyonu **iptal** | Gökalp iptal etti, sunucuda iz bırakılmadı | — |
| **2026-11-15** | Yeni uygulamalarda yönetici kullanıcı adı `flugel`; parolalar beyne yazılmaz (sunucuda `/opt/stacks/<ad>/.env`, root 600) | Gökalp talimatı; sır değerleri vault'a girmez | Rastgele parolalar (Gökalp değiştirdi) |
| **2026-11-15** | Jellyseerr, Vaultwarden, Audiobookshelf, Changedetection, CyberChef, Homebox, Speedtest Tracker ve Recyclarr **kaldırıldı** (stack/veri `_kaldirildi-20261115` arşivinde); izleme yığını (Prometheus/Grafana/Alertmanager/node-exporter) tekrar durduruldu | Gökalp: "gerekli olmayanları sil"; kullanım yoktu (veri boş), bellek dar (swap dolu), işlev başka uygulamalarla örtüşüyordu | Hepsini tutmak |
| **2026-11-15** | Kalan yeni uygulamalar: Forgejo, Paperless, n8n, SearXNG, Syncthing, IT-Tools, Scrutiny, ntfy | Gerçekten kullanılanlar ya da başka bir şeyin dayandığı olanlar (belge hattı, otomasyon, Hermes araması, bildirim) | — |
| **2026-11-15** | **Tailscale ile giriş**: `giris` nginx'inde kimlik kapısı (`Tailscale-User-Login` = sahip, yoksa 403) 14 uygulamanın önüne eklendi; Paperless/Forgejo/n8n/Dozzle'da bunun üstüne otomatik oturum; OIDC (tsidp) Komga, Kavita, Nextcloud, Immich, Forgejo, Paperless, Dozzle'da | Gökalp "tüm applere hızlı giriş" istedi; nginx kapısı istemci uygulamaları (mobil) bozmaz, ek konteyner gerektirmez | Her uygulamaya ayrı oauth2-proxy |
| **2026-11-15** | Disk: restic'te doğrulanan düz Arch PC kopyaları ve 5 Kasım servis arşivi silindi; indirmedeki sahte film `.scr` dosyası silindi; izlenmiş medya silinmedi (izleme verisi yok), restic saklaması değişmedi (fark sıfır) | Gökalp "kararları yap" dedi; yalnız doğrulanan/zararlı olanlar silindi | Kör silme |

