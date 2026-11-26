# Threads

## Active Threads
### İkinci beyin: flugel-beyin derlemesi ve V3 geçişi
- **Sahip:** Gökalp (ajanlarla birlikte).
- **Durum (2026-11-27):** Ortak skill ve ajan sistemi kuruldu ve 7 tur sıfırdan ajan testiyle doğrulandı ([[knowledge/kararlar]] 2026-11-26 satırı; rapor `second-brain/raporlar/skill-ve-ajan-sistemi-2026-11-26.md`). Yeni ajan girişi: `~/Documents/ai_workplace/YENI-AJAN.md`. Bilinen eksik: Claude limiti okunamıyor (`claude login` Gökalp'te); `beyin.py` salt okunur sandbox'ta yazma hatası (upstream, `beyin-ara` ile aşılıyor); lint'in `[[receipts/…md|…]]` yanlış alarmı (upstream).
- **Durum (2026-11-15, Claude doctor kontrolü):** V3 sağlıklı: hook yolları ve global köprü ok, scheduled-check ok, güncel sürüm, bekleyen olay 0; 2026-11-15 onarımında lint kırık 0/yetim 0. Kökteki `hafiza`, `simdi`, `gelen-kutusu` yalnız yönlendirme; `kararlar`/`dersler` knowledge/'a taşınmış. Jev modu `on` ve **açık kalacak** (Gökalp kararı, 2026-11-15 19:51).
- **Durum (2026-11-14):** Vault Avenox İkinci Beyin V3.13.0'a geçti ([[knowledge/kararlar]]). Eski çekirdek dosyalar (`hafiza`, `simdi`, `gelen-kutusu`, `kararlar`, `dersler`) companion, `knowledge/` ve `tasks/` yapısına taşındı; arşivlenmeleri lider ajanın kontrolünü bekliyor. Jev: kararlar kaydında "bir hafta gölge modda ölç, sonra `on`" yazıyor, ama 2026-11-14 `doctor` çıktısında Jev modu `on` görünüyor; hangisinin güncel niyet olduğu Gökalp'e sorulmalı.
- **11 Kasım hedefi (simdi.md'den):** 23 GitHub deposu, `flugelserver` Docker/medya/manga arşivleri ve Düdük belgelerinin `raw/` + `wiki/` + `notlar/` + `projeler/` altına eksiksiz derlenmesi ve `python3 brain.py lint` ile 0 problem; `second-brain-hud.html` canlı HUD panosu ve Obsidian Graph View renk kümeleri ([[ikinci-beyin-sistemi]]). Bu hedeflerin bitip bitmediği eski dosyalarda kayıtlı değil.
- **Sonraki adım:** V3 geçişi tamamlandı; açık karar kalmadı. Eski 11 Kasım derleme hedefi (23 GitHub deposu, arşivler) ayrıca istenirse değerlendirilir.

### Hakemlik ve Düdük
- **Sahip:** Gökalp.
- **Durum:** 13 Kasım 2026 Cuma Taha Akgül Spor Salonu maçları (U14 Erkek B ve U18 Erkek B, ikisinde de `referee2`) geçti; sonuç kayıtlı değil. Saat ve eşleşmeler simdi.md ile [[projeler/hakemlik]] arasında farklı yazılmış; ayrıntı [[notes/simdi-2026-11-hafta-2]].
- **Açık işler (tasks/):** canlı sunucu arşivinin (`https://duduk.gokalpgoksu.com/v1/stats`) yeni hafta atamalarını yakalamasını izlemek; `assignr` yeni hafta yayın saatini loglardan gözlemlemek; ilk `BÖLGE` ödemesinde net maç ücretini kaydetmek.
- **Sonraki adım:** 14-20 Kasım atamaları yayımlanınca `/v1/stats` ve değişiklik tespitini kontrol et ([[projeler/duduk]]).
- **2026-11-24:** Basket botu Türkçe metin tarih hatası düzeltildi (yeni atama/sabah hatırlatması gitmiyordu); 24 Kasım 17:30 ve 20:30 maçları görünüyor. Düdük telefonda kasıyor: v0.3.0 debug APK → iOS kalitesi işi Canalp'a devredildi (`second-brain/DEVIR-canalp-duduk.md`, oturumu Gökalp açacak). Gemini basket-bot'a ICS takvim + çakışma uyarısı geliştiriyor (yüklenmedi).

### Gazi EEM 2026 Güz vize dönemi
- **Sahip:** Gökalp.
- **Durum:** EE317 Güç Elektroniği I vizesi 12 Kasım 2026 09:00'da yapıldı (kapsam D1–D4, tristör yok; [[notlar/ee317-vize-calismasi-2026-11-11]]); sonucu kayıtlı değil. simdi.md'deki EE313 ve EE333 "vize tekrarı" maddeleri bayat: [[projeler/okul-guz-2026]] bu iki vizeyi 7 ve 9 Kasım'da tamamlandı olarak gösteriyor.
- **Sonraki adım:** Vize sonuçlarını ve EE346 sınav zamanını [[projeler/okul-guz-2026]] içinde güncelle ([[notlar/gazi-eem-vize-takvimi-ve-ders-notlari]]).

### flugelserver ağ güvenliği
- **Sahip:** Gökalp.
- **Durum (2026-11-26):** Bakım yükü azaltıldı: Cup oto-güncelleme haftalık (pazar 07:30 TSİ), arıza zinciri 10 dk eşik ve beyne yalnız gerçek onarım kaydı, yedek kontrolü günlük, günlük durum notu [[knowledge/sunucu-durum]]. Rapor: `second-brain/raporlar/sunucu-sadelestirme-2026-11-26.md`.
- **Sonraki adım:** Servis azaltma (raporda aday listesi) ve `/mnt/sidemain` %89.
- **Durum (2026-11-15):** Ev ağı entegrasyonu tamamlandı ([[knowledge/concepts/ev-agi-ve-dis-erisim]]): modem ve Tailscale DNS'i AdGuard'a yönlü, evde gokalpgoksu.com doğrudan HTTPS ve `.ev` adları, Mullvad proxy `:8889`, Wi-Fi ayarları, eski Tailscale cihazları silindi. **Funnel bilerek açık kalır** (Gökalp kararı; görev kapandı). `adguard.gokalpgoksu.com` A kaydı hâlâ 178.233.25.73'ü gösteriyor (CGNAT yüzünden işe yaramaz).
- **Durum (2026-11-24):** AdGuard hız sınırı kapatıldı (ev tek istemci sayılıyordu); ölü adların DNS'i yerel akış tüneline alındı (tools/portainer/admin/adguard artık çalışıyor; office/convert/pdf/ai/bd/ui 404). 40+ yeni `*.gokalpgoksu.com` FLUGEL kapısı arkasında; Tailscale istemcileri kapıyı atlar (AdGuard `100.64.0.0/10` kuralı + `127.0.0.1:8198`). Laptop Tailscale `RouteAll: true`; laptop/modem ikinci DNS'e Gökalp isteğiyle dokunulmadı.
- **Sonraki adım:** Cloudflare panelinde eski uzaktan yönetilen tünel rotalarını temizle; internete açık Portainer/Dockge/File Browser için Cloudflare Access ekle. Rapor: `second-brain/raporlar/sunucu-hata-taramasi-2026-11-24.md`.

## Closed Threads
