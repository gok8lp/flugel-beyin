# FLUGEL — Şimdiye kadar yapılan her şey (ayrıntılı özet)

> Bu metni yeni bir oturumda Claude'a bağlam olarak ver. Gizli bilgi (şifre/token/anahtar) içermez.
> Kod deposu: https://github.com/gok8lp/flugel (herkese açık) · Yerel kopya: `~/Projects/flugel`
> İşlem kayıtları: PC `~/sistem-bakim/islem-kaydi.log`, sunucu `~/sistem-bakim/islem-kaydi.log`

## 0. Ben ve makinelerim
- **Ben:** Gökalp (Ahmet Gökalp Göksu), Ankara'da öğrenci ve basketbol hakemi; MAL kullanıcı adım `gokalpgoksu`, GitHub `gok8lp`. Türkçe konuşurum. İlgi alanlarım: PlayStation/konsol oyunları, PC donanımı, yapay zekâ, telefonlar, anime/manga (özellikle Re:Zero), Linux.
- **Kurallar:** Şifremi/token'ımı Claude girmez, ben girerim. Lisanssız yayın sitelerine (AnimeciX, OpenAnime) link konmaz. Sunucuda VM'ler asla zorla (SIGKILL) kapatılmaz. Değişiklikten önce yedek al, işlem kaydına yaz.
- **PC "flugelubuntu":** Lenovo ThinkBook 16p Gen 4, RTX 4060 (NVIDIA 595 sürücü), Ubuntu 26.04, GNOME 50 Wayland, btrfs (@ / @home) + Timeshift. Ekran 2560x1600@60. Klavyeler: dizüstü klavyesi (dokunma) + Logitech **Pebble K380s** (Bluetooth). Fare Logitech G305.
- **Sunucu "flugelserver":** 192.168.0.15 · Tailscale 100.86.88.1 / `flugelserver.tail42f1f4.ts.net` · Ryzen 2600X, GTX 1660 Ti, 15 GB RAM · Ubuntu 26.04 · Docker yığınları `/opt/stacks` ve `/arrapps/compose` · Cloudflare Tunnel "homeserver" (alan adı gokalpgoksu.com, tünel Cloudflare panelinden yönetiliyor; `/etc/cloudflared/config.yml` eski/kullanılmıyor).
- SSH: PC'den `ssh flugelserver` (önce LAN, olmazsa Tailscale). Her iki makinede geçici NOPASSWD sudo var (`/etc/sudoers.d/90-bakim-gecici`).

## 1. PC (flugelubuntu)
### Temel kurulum
- Güncellemeler; Eclipse (snap, C/C++ CDT) + çalışma alanı `~/Documents/eclipse-workspace` (projeler: hafta1, project). gcc/g++ 15, make, gdb, cmake kurulu. Not: `project` "Cross GCC" araç takımıyla açılmış; yeni projelerde "Linux GCC" seçilmeli.
- Sunucu entegrasyonu: sshfs bağlamaları `/mnt/flugelserver/*`, PC yedekleri, sunucu bildirim izleyici, bot yedekleri (systemd kullanıcı birimleri `~/.config/systemd/user`).
- Kitty terminali. Uygulama ızgarası klasörlere ayrıldı (Sunucu, Ofis ve Okul, İnternet, Medya-Oyun, Geliştirme, Araçlar, Sistem); 27 sunucu servisi için `sunucu-*.desktop` kısayolları ve düzeltilmiş simgeler.
- Kurulan uygulamalar: WhatsApp (ZapZap, flatpak), LocalSend (flatpak; ufw'de 53317 tcp/udp sadece 192.168.0.0/24), Moonlight (flatpak), Smile (emoji seçici), evtest, JDK 21, Ubuntu Android araçları (aapt, dalvik-exchange, apksigner, zipalign, android-sdk-platform-23).

### GNOME eklentisi `flugel-panel@flugel` (üst çubuk) — `~/.local/share/gnome-shell/extensions/`
- Siyah-beyaz `*-mono.svg` simgeler (dikkat: `-symbolic.svg` adı kullanılmaz, dolu daireye dönüşüyor). Etiketler kısa tutulur (sağ kutu dar).
- Sol: Eclipse · Terminal · Chrome · Dosyalar · kurukafa (zorla kapat) · panik (gizle/sustur/kilitle) · kripto (BTC/ETH/USD/EUR anlık). Orta: saat. Sağ: basketbol atamaları · anime geri sayım · PC+sunucu durumu · **sanal makine menüsü** (W11-GPU, W11, Ubuntu/mullvad-ts: aç/bağlan/kapat) · ekran görüntüsü · ekran kaydı · kısayollar · Re:Zero ekibi (chibi SVG'ler `karakter-ciz.py`, 9 sn'de bir değişir).
- Quick Settings'te "Pil Tasarrufu" anahtarı (`~/.local/bin/pil-modu` + pil-modu.service: fişten çekince parlaklık 40, power-saver, ekran 3 dk).
- **Arka plan uygulamaları tepsisi** ("‹" ok, AppIndicator simgelerini toplar), simgelerin üzerine gelince açıklama balonu, uygulama sağ tık menüsünde "Masaüstüne ekle", Chrome resim-içinde-resim pencereleri hep üstte + tüm çalışma alanlarında.
- Veri yardımcısı `~/.local/bin/ust-panel-veri` (canli/kripto/pc/sunucu/basket/anime → JSON).
### Kilit ekranı `flugel-kilit@flugel`
- Düz siyah zemin, saatin üstünde Cinzel fontuyla "FLUGEL" (U ile, Ü değil), altında cam kartlar: kripto, sıradaki anime bölümü, pil, sunucu + göz kırpan Re:Zero karakteri. (Kullanıcı manzara arka planı istemedi; sadece yazı.)
### Açılış/giriş
- Plymouth teması "FLUGEL": harfler sırayla yükselir, ışık dalgası, altında yükleme çubuğu (`~/sistem-bakim/acilis-flugel/`).
- GDM giriş ekranı: alttaki Ubuntu logosu yerine FLUGEL logosu (`/usr/share/pixmaps/flugel-gdm-logo.png`), kullanıcı resmi "F" monogramı.
- Lenovo UEFI logosunu değiştirme: BMP hazır (`~/sistem-bakim/acilis-flugel/lenovo-logo-flugel.bmp`), **benim kararım bekleniyor** (EFI değişkeni yazımı riskli).
### Kısayollar
- Pencere kapat: **Super+X** (Alt+F4 de çalışır). Kitty: Super+Z ve Ctrl+Alt+T açar.
- K380s simge modunda (Fn+Esc ile geçiş) Windows kombinasyonları gönderir; eşlemeler: F4 masaüstü (Super+D), F5 arama, F6 geri, **F7 mikrofon sustur** (Super+H; pencere küçültme kısayolu kaldırıldı), **F8 emoji** (Smile), **F9 ekran görüntüsü** (Super+Shift+S). Dizüstü tuşlarına dokunulmadı.
- Chrome: otomatik resim-içinde-resim + orta tekerlek otomatik kaydırma bayrakları (`~/.local/share/applications/google-chrome.desktop` ve `~/.local/bin/google-chrome`).
### Tuzaklar
- Wayland'da eklenti değişikliği için oturumu kapatıp açmak gerekir. Test: `dbus-run-session -- gnome-shell --headless --virtual-monitor 1920x1080 --wayland --no-x11 --unsafe-mode` (uygulama başlatma; bitince `systemctl --user restart xdg-document-portal`, yoksa flatpak uygulamaları açılmaz).

## 2. Sunucu (flugelserver)
- **İzleme ve bakım** (`/usr/local/sbin`, `/usr/local/bin`, systemd zamanlayıcıları): AI gözcü (`ai-gozcu.sh`, 15 dk; yeni sorunları yerel LLM'e açıklatır, günlük özet, `~/sistem-bakim/durum/` HTML), self-heal (3 dk), docker-watcher, disk koruyucu (disk ölüm koruması), kritik yedek, torrent CSAM bekçisi, virüs taraması, docker güvenlik duvarı, smartd/disk raporu. Bildirimler `/usr/local/bin/bildirim` → **Telegram** (@flugels_bot; WhatsApp kapatıldı).
- GPU'lu VM açıkken bilerek durdurulan GPU konteynerleri (ollama, jellyfin, plex, immich_machine_learning, subgen) artık "çöktü" sayılmıyor (self-heal, ai-gozcu, docker-watcher düzeltildi). Haftalık `docker system prune` durmuş konteynerleri sildiği için `image+builder prune` yapıldı; silinen it-tools, stirling-pdf, libreoffice geri kuruldu.
- **Botlar** `/opt/basket-bot`: `basket_bot.py` (saatlik, ankarabasket bültenlerinde adımı arar → hakem atamaları `/var/lib/basket-bot/maclar.json`), `anime_takip.py` (MAL listem + AniList → `anime.json`). PC'de yedekleri var.
- **Homepage paneli** http://192.168.0.15:3010 (`/opt/stacks/panel`): açık grafit animasyonlu tema, FLUGEL başlığı, "Bugün" sekmesi (sunucu durumu, maçlar, takvim, haber kutuları) + "Uygulamalar" sekmesi, Ankara hava durumu, telefona uyumlu. Not: ayar değişince `curl http://192.168.0.15:3010/api/revalidate`.
- `gundem-botu` konteyneri (:3011, `/durum` sayfası, takvim.ics, maç/sorun JSON).
- **Cloudflare tünelleri:** Portainer, Cockpit (admin), Nextcloud, ai, ui, bd → Cloudflare Access (e-posta kodu) korumalı; Immich, Kavita, Komga, Jellyfin, ConvertX kendi girişleriyle açık. `adguard.gokalpgoksu.com` A kaydı ev IP'sini gösteriyor → silinmeli (yapılmadı).
- **Tailscale Funnel AÇIK:** Jellyfin (`https://flugelserver.tail42f1f4.ts.net`) ve Immich (`:10000`) herkese açık internette → **kapatma kararı bekleniyor**. FLUGEL Akış ise `tailscale serve` ile sadece tailnet: `:8443`.
- Immich 100 MB sorunu (Cloudflare limiti): telefondaki Immich'te otomatik URL değiştirme — ev Wi-Fi `http://192.168.0.15:2283`, dışarıda `http://100.86.88.1:2283` (Tailscale).
- Webmin servisi sürekli yeniden başlıyor (port 10000 dolu) → bakılmadı, karar bekleniyor.

## 3. Sanal makineler + Moonlight
- VM'ler: **W11-GPU** (8 vCPU/4 GB, GTX 1660 Ti passthrough, 192.168.122.50), **W11** (GPU'suz, aynı disk, .51), **mullvad-ts** (Ubuntu, 1 GB).
- Düzeltilenler: takılı olmayan USB passthrough (startupPolicy optional), disk `type='volume'` → `type='file'` (AppArmor izni), hook GPU kimliği 10de:2182, Windows güncellemesi sonrası UEFI takılması (sadece vCPU0 %100 + disk 0 → destroy+start güvenli; bekçi `~/sistem-bakim/araclar/w11-bekci.sh`).
- Windows içinde **Apollo** (Sunshine çatalı, sanal monitörlü) servis; PC'de **Moonlight** eşleşti. `/usr/local/sbin/vm-yonlendir.sh` hook ile portları LAN + Tailscale'den VM'e yönlendirir.
- PC komutları: `w11-gpu baslat|kapat|durum` (evde 2560x1600 50 Mbps, dışarıda 1080p 15 Mbps), `vm liste|baslat|baglan|kapat AD`.
- Windows'a uzaktan giriş PIN'i benim; Claude girmez.

## 4. FLUGEL Akış — kişisel X tarzı sosyal akış (ana proje)
- Adres: **https://flugelserver.tail42f1f4.ts.net:8443** (tailnet) · evde http://192.168.0.15:3012 · PC'de "FLUGEL" uygulaması (`~/.local/bin/flugel-akis`, Chrome --app).
- Kod: sunucuda `/opt/stacks/panel/akis/` (`akis.py` Python stdlib, `web/` index.html + app.css + app.js, çerçeve yok), konteyner `flugel-akis`, veritabanı SQLite `akis/veri/akis.db`.
- **Kaynaklar (61):** 36 RSS (Türkçe ağırlıklı oyun/teknoloji/gündem; PlayStation Blog/Push Square/PS LifeStyle; IGN/VGC/Eurogamer/GameSpot/Polygon/Kotaku/Xbox/Nintendo; anime ANN/Crunchyroll/MAL/Anime Corner; Japonya アニメ！アニメ！; Beyazperde) + 25 YouTube kanalı (teknoloji, oyun, anime stüdyoları, Netflix/Prime/Disney+ TR, IMDb). Önemliler **1 dk**, diğerleri 3 dk, YouTube 5 dk (ETag'li). Arayüz 20 sn'de bir yeni gönderiyi canlı ekler.
- **Sayfalar:** Sana özel · 🔥 Öne çıkanlar · 🔔 Takip · Gündem · Oyun (PlayStation, Steam öneri/çok satan/yeni) · Teknoloji · Anime & Manga (listem, bu sezon, haberler, 🇯🇵 Japonya, manga; kapaklar 3B eğim animasyonlu, canlı geri sayım, **yasal** izleme linkleri: Crunchyroll/Netflix/Disney+..., fragman, IMDb) · YouTube · Fragmanlar · Film & Dizi (TVmaze + IMDb puanı) · Oyun fiyatları (Steam TR arama, CheapShark fırsatlar, Epic ücretsiz) · Maçlar (hafta sonu: Süper Lig, 5 büyük lig, UCL/UEL, NBA + hakemlik görevlerim) · Uygulamalar (sunucu servisleri canlı durum) · Kaydedilenler · Sunucu (kaynak tazelik tablosu) · Takip & ayarlar.
- **Yerel AI (Ollama gemma3, sunucuda):** EN/JA → TR çeviri (özel isimler çevrilmez), haberlere 0–100 önem puanı + etiket, aynı haberleri tek gönderide toplama ("+N kaynak"), haber özetleme, FLUGEL AI sohbeti (sadece bağlamdaki gerçek veriyle; tarih + maçlar satır satır verilmezse uyduruyor). GPU VM açıkken AI durur.
- **Takip kelimeleri** (Re:Zero, GTA 6, PlayStation Plus, Elden Ring...) → uygulamada uyarı + Telegram (`/usr/local/sbin/flugel-uyari.sh` + `flugel-uyari.path`).
- **Android APK:** `~/sistem-bakim/flugel-apk` (`derle.sh`, Ubuntu araçlarıyla, targetSdk 34, sadece INTERNET izni, sadece tailnet adresini açar). İmza anahtarı `anahtar/` klasöründe — **silinmemeli, depoya girmez**. İndirme: uygulama → Takip & ayarlar.
- CSS tuzakları: `.orta` genel yerleşim sınıfı → skor rozetleri `s-iyi/s-orta/s-kotu`; oyun kartı `.oyunk`.

## 5. GitHub deposu
- https://github.com/gok8lp/flugel (**herkese açık**), İngilizce ayrıntılı README + `README.tr.md` (Türkçesi henüz kısa) + ekran görüntüleri `docs/ekran/`.
- Güncelleme: `~/Projects/flugel/guncelle.sh "açıklama"` → PC ve sunucudan dosyaları toplar, gizli değerleri depo dışındaki `~/.config/flugel-depo/gizli.txt` listesine göre yer tutucuyla değiştirir (`<TELEFON>`, `<CALLMEBOT_APIKEY>`, `<GOTIFY_TOKEN>`), tarar, bulursa göndermez, commit + push yapar. Commit kimliği GitHub noreply e-postası.
- Depoda görünen kişisel bilgiler: ad-soyad, MAL kullanıcı adı, Tailscale sunucu adı (bilerek kabul edildi).

## 6. Bekleyen işler / kararlar
1. Tailscale Funnel'ı kapat (Jellyfin + Immich herkese açık) — karar bekliyor.
2. `adguard.gokalpgoksu.com` DNS kaydını sil (Cloudflare paneli gerekir; Claude in Chrome eklentisi bağlı değildi).
3. Türkçe README'yi İngilizce kadar ayrıntılı yap; istersen lisans ekle.
4. Webmin yeniden başlama döngüsü.
5. Lenovo UEFI açılış logosu (BMP hazır).
6. X (@gokalpgoksu_) takip listesi: otomatik okunamıyor; hesap adlarını verirsem YouTube/site kaynakları eklenebilir.
7. W11 yeniden başlatma takılmasının kök nedeni (AVIC/hyperv ayarları şüpheli).
8. FLUGEL Akış için gerçek haber gecikmesini ölç (Sunucu sayfasındaki tablo).
