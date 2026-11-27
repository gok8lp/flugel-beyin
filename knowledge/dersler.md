---
{
  "kind": "fact",
  "title": "Dersler — Öğrenilen Dersler ve Teknik Tuzaklar",
  "visibility": "internal",
  "tags": [
    "dersler",
    "tuzaklar",
    "deneyim"
  ],
  "evidence_refs": [
    "dersler.md"
  ]
}
---
# Dersler — Öğrenilen Dersler ve Teknik Tuzaklar

Bağlantılar: [[HARITA]] · [[Core]] · [[knowledge/kararlar]] · [[Veri Tuzakları ve Uç Durumlar Kataloğu]]

> 2026-11-14'te kök dizindeki eski `dersler.md` dosyasından madde madde taşındı (V3 geçişi).

## 1. İkinci Beyin ve Claude Code Dersleri
- **Path Kuralları (`settings.json`):** `.claude/settings.json` içindeki `permissions.deny` kuralları yalnızca `Edit(...)` ve `Read(...)` için çalışır; `Write(raw/**)` kuralı sessizce yok sayılır. `raw/` klasörünü korumak için `Edit(/raw/**)` kullanılır ([[ikinci-beyin-sistemi]]).
- **Bellek Sınırı:** Claude Code otomatik belleği `CLAUDE.md` / `MEMORY.md` dosyasının yalnız ilk **200 satırını (veya 25 KB'ını)** yükler. Bu yüzden `CLAUDE.md` ve `wiki/hot.md` kısa tutulmalı, büyük `wiki/index.md` asla `@import` edilmemelidir.
- **Model Kendi Yazdığı Hatayı Görmez:** Wiki sayfasındaki inandırıcı ama kaynakta olmayan bir iddiayı LLM denetimi kaçırır; `brain.py lint` içindeki birebir alıntı kontrolü (`QUOTE NOT IN SOURCE`) bunu sıfır token ile milisaniyede yakalar.

## 2. Düdük ve Veri Kaynakları Dersleri
- **Java Regex `StackOverflowError`:** Next.js RSC Flight (`self.__next_f.push`) verisi 50 KB'ı geçtiğinde Java regex motoru `("(?:[^"\\]|\\.)*")` üzerinde çöker; doğrusal karakter tarayıcı (`AnkarabasketAyristirici.flight`) kullanılmalıdır ([[assignr-ve-ankarabasket-kaynaklari]]).
- **TBF Şema Tuzakları:** TBF API'de tam sayı kimlikler `"22328.0"` (Double) olarak, oynanmamış maçların `matchDate` alanı ise `"10. Hafta"` metni olarak gelebilir ([[tbf-eslestirme-algoritmasi]]).
- **Atama Kaldırılma Tespiti (`ATAMA_KALDIRILDI`):** Haftanın ilk günündeki maç silindiğinde yalnızca `minTarih..maxTarih` penceresine bakmak o maçı kaçırır; maçın `week` etiketinin (`"10. Hafta"`) aktif haftalar kümesinde olup olmadığına da bakılmalıdır ([[yerel-arsiv-ve-senkronizasyon]]).
- **Yüzen Cam Başlık (`CamUstBaslik`) Üst Boşluğu:** `statusBarsPadding()` + `88.dp` yüksekliğindeki yüzen üst başlık altında ilk kartın kesilmemesi için liste `contentPadding(top = 140.dp)` olmalıdır ([[android-arac-zinciri-ve-mimari]]).

## 3. Sunucu (`flugelserver`) Dersleri
- **GPU Passthrough ve Docker İzleme:** `W11-GPU` açıkken GTX 1660 Ti VM'e geçtiği için `ollama`, `plex`, `immich_machine_learning`, `subgen` konteynerleri bilerek durdurulur; `self-heal.sh` ve `ai-gozcu.sh` bunları "çöktü" saymamalıdır ([[flugelserver-sanal-makineler-ve-gpu]]).
- **Cloudflare Uzaktan Yönetilen Tünel (`remote management`):** `cloudflared` tüneli Zero Trust panelinden yönetiliyorsa yerel `/etc/cloudflared/config.yml` içindeki `ingress` kuralları yok sayılır; yerel yönetilen `akis.yml` (`cloudflared-akis.service`) tüneli kullanılmalıdır ([[notlar/cloudflare-ve-tailscale-baglanti-zinciri]]).
- **Haftalık Docker Prune Tuzağı:** `docker system prune` durdurulmuş konteynerleri sildiği için yalnızca `docker image prune` + `builder prune` kullanılmalıdır ([[flugelserver-genel-mimari]]).

- **Adrese sabitlenmiş APK kabukları:** Eski `FLUGEL.apk` yalnız Tailscale `:8443` adresini açıyordu; erişim yolu değişince uygulama işe yaramaz hâle geldi. Kabuk APK'larda adres tek sabitte tutulmalı ve yol değişince yeni sürüm derlenmeli ([[notlar/flugel-akis-mobil-uygulama]]).
- **İmza anahtarı kaybı:** 1.0'ın anahtarı (`flugel.jks`) 2026-11-11'de ne PC'de ne sunucuda (`~/sistem-bakim/flugel-apk/anahtar/`, `~/Projects/desktop-server-toolkit/android/` ve ev dizinleri) bulundu; 2.0 yeni anahtar ve **farklı paket adıyla** çıktı. Yeni anahtar sunucuda `~/work/keys/flugel-akis.jks`; silinirse güncelleme üstüne kurulamaz ([[notlar/flugel-akis-mobil-uygulama]]).
- **Konteyner kaldırırken tünel satırı da gider:** 4 Kasım sadeleştirmesinde `flugel-akis` hem `docker rm` ile hem de `akis.yml` ingress'inden çıkarılmıştı; geri açarken ikisi birlikte geri alınmalı ([[notlar/flugel-akis-mobil-uygulama]]).

## 4. Ders Çalışma ve Çoklu Ajan Dersleri
- **Ekranda açma doğrulanmalı:** Okular'a açma komutu göndermek pencerenin görünür olduğunu kanıtlamaz; 11 Kasım'da pencereler kapanmıştı. `hyprctl clients -j` ile doğrula ([[notlar/claude-hafizasi]]).
- **Ortak dosya çakışması:** Claude ve Codex aynı `YOL_HARITASI.md` dosyasını üst üste yazdı; ortak dosyalara yalnız sona ekleme yapılır, yazmadan önce yeniden okunur ([[notlar/claude-hafizasi]]).

## 5. Laptop Kurulum Dersleri (2026-11-12)
- **Anahtarsız sunucuya giriş:** `flugelserver` yalnız publickey kabul ediyor; yeni makineden `ssh-copy-id` çalışmaz. Tailscale'e katıl ve Tailscale SSH ile bağlan ([[notlar/laptop-thinkbook-arch-hyprland-kurulumu]]).
- **Hyprland Lua + shell'ler:** Hyprland 0.57 Lua config'inde bazı shell'ler (Ambxst 1.3.15) renk değerlerini çift tırnaklıyor ve yeni kısayolları mevcutlarla çakıştırıyor; aynı tuşa iki bağ olunca **ikisi birden** çalışır. Kurulumdan sonra `hyprctl configerrors` ve kısayol çakışması kontrol edilmeli.
- **Bluetooth butonu çalışmıyorsa** önce `rfkill list` bak; soft block varken `bluetoothctl power on` başarısız olur.
- **Hermes'in terminal aracı konteynerde değil, sunucuda `hermes-ops` olarak çalışır** (`TERMINAL_SSH_USER=hermes-ops`): `/opt/data/.ssh/config` gibi konteyner yolları orada yoktur ("Hermes konteynerinde olan dosya terminalde yok" hatası). `agy` girişi `flugel` kullanıcısındadır; doğru çağrı `cd /tmp && sudo -n -u flugel -H /home/flugel/.local/bin/agy --model <model> --dangerously-skip-permissions -p="…"` (`/home/flugel` hermes-ops'a kapalı, `/tmp`'den çalıştır). Oturum açıkken talimat dosyası değişse de yeni oturum (`/new`) gerekir. Kaynak: `second-brain/raporlar/hermes-varsayilan-hydrogen-2026-11-15.md`.
- **Hermes talimatına "şu yol YOK" diye hata cümlesi yazma:** Luna uyarıyı kendi hata mesajı sanıp komutu denemeden aynısını tekrarladı; yalnız çalışan komutu yaz. Küçük model (Luna) araçlı işte güvenilmez; Hermes'e görev bırakılacaksa Sol ve üstü. Hermes'e bir bilgi öğretmek için o bilginin yerini (Komga/Kavita DB yolları, `saglik-ozet.json`) bir beceriye yaz; "bilgi yok" cevabının nedeni çoğu zaman bilginin yerini bilmemesidir. Kaynak: `second-brain/raporlar/hermes-varsayilan-hydrogen-2026-11-15.md`.
- **sudo şifresi sekme başınadır:** Bir terminal sekmesinde `sudo -v` yapmak başka sekmeye/ajana geçmez.
- **Hibrit laptopta global NVIDIA env yok:** Ekran Intel'e bağlıyken `LIBVA_DRIVER_NAME=nvidia` gibi genel değişkenler Chrome/Electron'u NVIDIA'da video çözmeye zorlar → siyah video + uyanık NVIDIA. NVIDIA yalnız gereken uygulamaya PRIME değişkenleriyle verilir ([[notlar/laptop-thinkbook-arch-hyprland-kurulumu]]).
- **Hyprland 0.57 Lua özel layout (`hl.layout.register`) hedef çoğaltması:** Çalışma alanı kuralıyla `dwindle` → `lua:...` geçişi yapıldığında `ctx.targets` listesinde aynı pencere birden fazla hedef olarak gelebilir; `recalculate(ctx)` içinde hedefler pencere adresine göre tekilleştirilmeli ve yeniden hesaplama için `dwindle`'a dönmek yerine iki Lua layout adı (`a`/`b`) arasında geçiş yapılmalı ([[notlar/laptop-dux-ozellestirme-oturumu-2026-11-13]]).
- **Hyprland eklentisi ve hyprgraphics/Qt güncellemeleri (2026-11-27):** Hyprland sürümü aynı kalsa bile bağımlılık (hyprgraphics 0.6→0.7) güncellenince elle derlenmiş eklenti "version mismatch" verip açılışta sağ üstte hata gösterir; `hyprctl plugin load <so>` hatayı yazar. Aynı şekilde Arch'taki Quickshell, Qt yama sürümü değişince "built against Qt" uyarısı verir; resmi PKGBUILD ile `pkgrel` artırılıp yerelde derlenir. Laptopta eklenti `~/.local/bin/hypr-eklenti-derle` ile kendini onarır.
- **Döşeme zorlaması ile eski yüzen yerleşim betikleri çarpışır:** Tüm pencereleri `float=false` yapan kanca (`yuzmeyi_kapat`) aktifken arka planda `float=on` + sabit boyut veren `alan-yerlesim` / `pencere-duzenle` çalıştırılırsa `dwindle` bölünme oranları bozulup pencereler ince şeritlere (`39px`, `29px`) sıkışır; tüm yerleşim betikleri döşeme tabanlı olmalıdır.

## 6. AI ekibi, skill ve sunucu dersleri (2026-11-26)
- **Codex ücretsiz planda yalnız `gpt-6-luna` çalışır:** `gpt-6.1-sol` ve `gpt-6-astra` "not supported when using Codex with a ChatGPT account" hatasıyla iş başlamadan biter; `~/.codex/config.toml` varsayılanı sol olduğu için `-m` verilmeyen her çağrı boşa gidiyordu. Varsayılan luna'ya çekildi, `ai-limitler --sec` planı hesaba katıyor. Kaynak: `second-brain/raporlar/skill-ve-ajan-sistemi-2026-11-26.md`.
- **agy headless komut izni:** çalıştırılacak komut allow listesinde kalıbıyla yoksa (`"command(ls *)"` gibi) otomatik reddedilir ve ajan rc=0 ile boş döner; boş çıktı başarı değildir.
- **Claude hook'unda alt ajan ayrımı:** PreToolUse girdisinde ana ajan için `agent_id` null, `Agent` aracıyla açılan alt ajan için dolu gelir (2026-11-26 testi). Lider bekçisi bunu kullanır.
- **Sahte arıza alarmı = güncelleme penceresi:** Arıza zinciri "durmuş" konteyneri ilk yoklamada olay sayıyordu; Cup oto-güncellemesi her sabah Gluetun grubunu ~1 dk durdurduğu için 10 günde 38 sahte kayıt oluştu. Durum alarmında ardışık eşik şart. Kaynak: `second-brain/raporlar/sunucu-sadelestirme-2026-11-26.md`.
- **Test geri yüklemesinde kapsamı dar tut:** `restic restore --include <klasör>` tüm Immich kütüphanesini /tmp'ye açmaya başladı (7,6 GB'ta durduruldu). Tek tek dosya seç; `pkill -f <desen>` kendi ssh kabuğunu da öldürür, PID ile durdur. Kaynak: `second-brain/raporlar/sunucu-yedek-denetim-2026-11-26.md`.
- **Alt ajanın "yedek aldım" iddiası doğrulanır:** 2026-11-26 skill sistemi işinde bir alt ajan yedek klasörü yazdığını söyledi ama klasör yoktu, bir diğeri yedeği atladı. Lider, değişiklik lane'inden sonra yedek yolunu `ls` ve `sha256sum -c` ile kontrol eder; eksikse son durumu hemen yedekler. Kaynak: `second-brain/raporlar/skill-ve-ajan-sistemi-2026-11-26.md`.
- **Sıfırdan ajan testi + bağımsız hakem işe yarıyor:** Test ajanlarının kendi verdiği puan (58–82) gürültülü; gizli ölçütle puanlayan taze hakem gerçek ilerlemeyi gösterdi (Claude 87→94, Gemini 92→98) ve şikayetleri sistem sorunu / test sınırı / ortam eksikliği diye ayırdı. Yeni ve görülmemiş senaryo eklemek ezberi önler.
- **Beyin köprüsü dış projede kabukla yazılan dosyayı görmez:** `beyin.py bridge` Stop kontrolü yalnız `apply_patch`/`Edit` düzenlemesini sayar; Codex ve agy çoğu dosyayı kabukla yazdığı için receipt hatırlatması gelmiyordu. Çözüm: dosya mtime'ına bakan `bitis_bekcisi.py`. Codex hook'ları ayrıca ilk etkileşimli açılışta "Trust all and continue" onayı ister; onaysız hiç çalışmaz (agy istemez). Kaynak: `second-brain/raporlar/beyin-otonomi-2026-11-27.md`.


## 7. Şifre kasası ve döndürme dersleri (2026-11-27)
- `rbw` Vaultwarden 1.37'ye kayıt **ekleyemez** (422, `encryptedFor` eksik); okuma çalışır. Yazma için resmi `bw` (npm `@bitwarden/cli`; Arch paketi nodejs-lts ile çakışır).
- Syncthing REST `basic auth` CSRF yüzünden hep 403 döner; şifre doğrulaması `POST /rest/noauth/auth/password` (204/403). GUI kökü basic auth başarılıysa `sessionid` çerezi verir (Tailscale kapısından otomatik giriş bununla).
- `immich-admin reset-admin-password` borudan girdi almaz, takılır → Postgres `"user".password` bcrypt.
- linuxserver Nextcloud `occ` sarmalayıcısı `-e OC_PASS`'ı geçirmez → `docker exec -u abc ... php /app/www/public/occ`.
- Paperless `/api/` yanlış basic auth'a 302 döner; test için Django `check_password` kullan. Actual Budget argon2id (konteynerin argon2 modülü), Speedtest SQLite `$2y$`.
- Jellyfin 10.11'de DB'ye PBKDF2 yazmak da, geçici API anahtarıyla `/Users/{id}/Password` da tutmadı (nedeni bulunmadı).
- `grep -E '...(USER|NAME)...='` gibi geniş desen `LD_SUPERUSER_PASSWORD` satırını da yakalar; .env taramasında `PASS` içeren satırları önce dışla.
- `pkill -f <desen>` aynı komut satırında desen geçiyorsa kendi kabuğunu öldürür.
- 2026-11-27: Laptopta `yay --sudoloop` `sudo -v` çağırır ve NOPASSWD olsa da parola ister; arka planda AUR kurulumu için `yay --sudoflags -n` kullan.
