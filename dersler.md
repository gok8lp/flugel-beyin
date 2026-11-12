---
tur: dersler
etiketler:
  - dersler
  - tuzaklar
  - deneyim
olusturma: 2026-11-11
guncelleme: 2026-11-11
---

# dersler.md — Öğrenilen Dersler ve Teknik Tuzaklar

Bağlantılar: [[HARITA]] · [[hafiza]] · [[kararlar]] · [[Veri Tuzakları ve Uç Durumlar Kataloğu]]

## 1. İkinci Beyin ve Claude Code Dersleri
- **Path Kuralları (`settings.json`):** `.claude/settings.json` içindeki `permissions.deny` kuralları yalnızca `Edit(...)` ve `Read(...)` için çalışır; `Write(raw/**)` kuralı sessizce yok sayılır. `raw/` klasörünü korumak için `Edit(/raw/**)` kullanılır ([[ikinci-beyin-sistemi]]).
- **Bellek Sınırı:** Claude Code otomatik belleği `CLAUDE.md` / `MEMORY.md` dosyasının yalnız ilk **200 satırını (veya 25 KB'ını)** yükler. Bu yüzden `CLAUDE.md` ve `wiki/hot.md` kısa tutulmalı, büyük `wiki/index.md` asla `@import` edilmemelidir.
- **Model Kendi Yazdığı Hatayı Görmez:** Wiki sayfasındaki inandırıcı ama kaynakta olmayan bir iddiayı LLM denetimi kaçırır; `brain.py lint` içindeki birebir alıntı kontrolü (`QUOTE NOT IN SOURCE`) bunu sıfır token ile milisaniyede yakalar.

## 2. Düdük ve Veri Kaynakları Dersleri
- **Java Regex `StackOverflowError`:** Next.js RSC Flight (`self.__next_f.push`) verisi 50 KB'ı geçtiğinde Java regex motoru `("(?:[^"\\]|\\.)*")` üzerinde çöker; doğrusal karakter tarayıcı (`AnkarabasketAyristirici.flight`) kullanılmalıdır ([[assignr-ve-ankarabasket-kaynaklari]]).
- **TBF Şema Tuzakları:** TBF API'de tam sayı kimlikler `"22328.0"` (Double) olarak, oynanmamış maçların `matchDate` alanı ise `"10. Hafta"` metni olarak gelebilir ([[tbf-eslestirme-algoritmasi]]).
- **Atama Kaldırılma Tespiti (`ATAMA_KALDIRILDI`):** Haftanın ilk günündeki maç silindiğinde yalnızca `minTarih..maxTarih` penceresine bakmak o maçı kaçırır; maçın `week` etiketinin (`"10. Hafta"`) aktif haftalar kümesinde olup olmadığına da bakılmalıdır ([[yerel-arsiv-ve-senkronizasyon]]).

## 3. Sunucu (`flugelserver`) Dersleri
- **GPU Passthrough ve Docker İzleme:** `W11-GPU` açıkken GTX 1660 Ti VM'e geçtiği için `ollama`, `plex`, `immich_machine_learning`, `subgen` konteynerleri bilerek durdurulur; `self-heal.sh` ve `ai-gozcu.sh` bunları "çöktü" saymamalıdır ([[flugelserver-sanal-makineler-ve-gpu]]).
- **Haftalık Docker Prune Tuzağı:** `docker system prune` durdurulmuş konteynerleri sildiği için yalnızca `docker image prune` + `builder prune` kullanılmalıdır ([[flugelserver-genel-mimari]]).

- **Adrese sabitlenmiş APK kabukları:** Eski `FLUGEL.apk` yalnız Tailscale `:8443` adresini açıyordu; erişim yolu değişince uygulama işe yaramaz hâle geldi. Kabuk APK'larda adres tek sabitte tutulmalı ve yol değişince yeni sürüm derlenmeli ([[notes/flugel-akis-mobil-uygulama]]).
- **İmza anahtarı kaybı:** 1.0'ın anahtarı (`flugel.jks`) 2026-11-11'de ne PC'de ne sunucuda (`~/sistem-bakim/flugel-apk/anahtar/`, `~/Projects/desktop-server-toolkit/android/` ve ev dizinleri) bulundu; 2.0 yeni anahtar ve **farklı paket adıyla** çıktı. Yeni anahtar sunucuda `~/work/keys/flugel-akis.jks`; silinirse güncelleme üstüne kurulamaz ([[notes/flugel-akis-mobil-uygulama]]).
- **Konteyner kaldırırken tünel satırı da gider:** 4 Kasım sadeleştirmesinde `flugel-akis` hem `docker rm` ile hem de `akis.yml` ingress'inden çıkarılmıştı; geri açarken ikisi birlikte geri alınmalı ([[notes/flugel-akis-mobil-uygulama]]).

## 4. Ders Çalışma ve Çoklu Ajan Dersleri
- **Ekranda açma doğrulanmalı:** Okular'a açma komutu göndermek pencerenin görünür olduğunu kanıtlamaz; 11 Kasım'da pencereler kapanmıştı. `hyprctl clients -j` ile doğrula ([[notes/claude-hafizasi]]).
- **Ortak dosya çakışması:** Claude ve Codex aynı `YOL_HARITASI.md` dosyasını üst üste yazdı; ortak dosyalara yalnız sona ekleme yapılır, yazmadan önce yeniden okunur ([[notes/claude-hafizasi]]).

## 5. Laptop Kurulum Dersleri (2026-11-12)
- **Anahtarsız sunucuya giriş:** `flugelserver` yalnız publickey kabul ediyor; yeni makineden `ssh-copy-id` çalışmaz. Tailscale'e katıl ve Tailscale SSH ile bağlan ([[notlar/laptop-thinkbook-arch-hyprland-kurulumu]]).
- **Hyprland Lua + shell'ler:** Hyprland 0.57 Lua config'inde bazı shell'ler (Ambxst 1.3.15) renk değerlerini çift tırnaklıyor ve yeni kısayolları mevcutlarla çakıştırıyor; aynı tuşa iki bağ olunca **ikisi birden** çalışır. Kurulumdan sonra `hyprctl configerrors` ve kısayol çakışması kontrol edilmeli.
- **Bluetooth butonu çalışmıyorsa** önce `rfkill list` bak; soft block varken `bluetoothctl power on` başarısız olur.
- **sudo şifresi sekme başınadır:** Bir terminal sekmesinde `sudo -v` yapmak başka sekmeye/ajana geçmez.
- **Hibrit laptopta global NVIDIA env yok:** Ekran Intel'e bağlıyken `LIBVA_DRIVER_NAME=nvidia` gibi genel değişkenler Chrome/Electron'u NVIDIA'da video çözmeye zorlar → siyah video + uyanık NVIDIA. NVIDIA yalnız gereken uygulamaya PRIME değişkenleriyle verilir ([[notlar/laptop-thinkbook-arch-hyprland-kurulumu]]).
- **Hyprland 0.57 Lua özel layout (`hl.layout.register`) hedef çoğaltması:** Çalışma alanı kuralıyla `dwindle` → `lua:...` geçişi yapıldığında `ctx.targets` listesinde aynı pencere birden fazla hedef olarak gelebilir; `recalculate(ctx)` içinde hedefler pencere adresine göre tekilleştirilmeli ve yeniden hesaplama için `dwindle`'a dönmek yerine iki Lua layout adı (`a`/`b`) arasında geçiş yapılmalı ([[notlar/laptop-dux-ozellestirme-oturumu-2026-11-13]]).
- **Döşeme zorlaması ile eski yüzen yerleşim betikleri çarpışır:** Tüm pencereleri `float=false` yapan kanca (`yuzmeyi_kapat`) aktifken arka planda `float=on` + sabit boyut veren `alan-yerlesim` / `pencere-duzenle` çalıştırılırsa `dwindle` bölünme oranları bozulup pencereler ince şeritlere (`39px`, `29px`) sıkışır; tüm yerleşim betikleri döşeme tabanlı olmalıdır.
