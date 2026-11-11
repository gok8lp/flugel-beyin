# flugelserver Git Depoları Commit Geçmişi, Zamanlayıcılar ve Betikler

Sunucu üzerindeki tüm yerel git depolarının son commit geçmişi, `/usr/local/sbin` ve `/usr/local/bin` bakım betikleri ve systemd zamanlayıcıları.

## 1. Sunucu Üzerindeki Git Depoları ve Son Commitler
### /home/flugel/work/koharia-public
- 75f70ade1 | 2026-10-31 | fix(flugel): use Tailscale addresses and drop embedded server API keys
- 58c974136 | 2026-10-31 | fix(reader,flugel): fix LAN EPUB/PDF novel loading and make Flugel setup plug-and-play
- 715564bce | 2026-10-30 | Flugel: secure personal build, reconnects and signed updates
- 2ed40ac3f | 2026-10-28 | style: apply spotless formatting to LibraryConnectionProfilesScreen (#1)
- df5d324a0 | 2026-10-23 | docs: clarify project purpose, setup and repository naming
- 04d8e34ef | 2026-10-18 | Daha Fazla menusune Manga indir (Tranga) ve Kutuphaneye ekle (yukleme) kisayollari
- 37eb2d40d | 2026-10-18 | Kitaplar sekmesi icin ayri baglanti: Komga ve Kavita ayni anda (Cizgi roman / Kitaplar sekmeleri)
- 593681613 | 2026-10-18 | Komga SSE yolunu duzelt (/sse/v1/events) ve test APK surum etiketini parametre yap
- 761c2fac0 | 2026-10-18 | Prepare Flugel Manga test APK and server setup
- a95a23b0c | 2026-10-06 | fix: 修复升级时重复建表导致的启动崩溃 / Fix upgrade startup migration crash
- 0f287cdf0 | 2026-10-06 | release: 准备 0.7.0，完善文档与墨水屏适配 / Prepare 0.7.0 with docs and E-Ink fixes
- c28ad51fc | 2026-10-06 | feat: 接入 Suwayomi 与网络存储并完善共享阅读功能 / Add Suwayomi and network storage integration
- 6c4560533 | 2026-10-03 | docs: enforce shared provider contracts / 规范跨库通用能力与验证
- 5a4c45a69 | 2026-10-03 | fix: 修复书籍下载并完善 Kavita 书架状态 / Fix book downloads and Kavita shelf status
- 1232f7cef | 2026-10-03 | fix: 修复本地系列与 EPUB 阅读进度 / Fix local series and EPUB reading progress
- a492b9975 | 2026-10-03 | feat: 完善阅读器设置与翻页体验 / Improve reader settings and page-turn behavior
- c7dfde60b | 2026-10-02 | feat: 统一本地系列元数据编辑并修复阅读流程 / Unify local series metadata editing and stabilize reader flows
- 99bddf1c5 | 2026-09-27 | fix(local): improve archive loading and restore entry opening settings
- 17fe06013 | 2026-09-27 | docs: document Kavita support in Chinese and English READMEs
- e62b1674a | 2026-09-27 | fix(ui): use E-Ink aware loading indicators
- fdffa453d | 2026-09-27 | feat(kavita): add native integration and reliable reading sync
- c59e86afd | 2026-09-26 | feat: unify library search and improve reader image handling
- e9fe432ad | 2026-09-24 | feat: prepare 0.6.0 with local library UI and support updates
- 18a787b66 | 2026-09-24 | fix: optimize local library scanning and share chapter display mode
- adb9ea0ba | 2026-09-24 | feat(settings): improve shelf and chapter display controls
- 14a33ed26 | 2026-09-24 | fix(download): improve large-file transfers and retry recovery
- 2f8d90c54 | 2026-09-23 | fix(reader): preserve Markdown code formatting and heading positions
- 73a0d2d36 | 2026-09-23 | Feat/markdown: 支持本地 Markdown 文件阅读 + Markdown 文档大纲导航 (#95)
- f88c7597b | 2026-09-23 | chore(codex): remove project subagent configuration
- c9a04f191 | 2026-09-23 | feat(backup): preserve user data across backup and restore

### /home/flugel/work/koharia-reader
- 75f70ade1 | 2026-10-31 | fix(flugel): use Tailscale addresses and drop embedded server API keys
- 58c974136 | 2026-10-31 | fix(reader,flugel): fix LAN EPUB/PDF novel loading and make Flugel setup plug-and-play
- 715564bce | 2026-10-30 | Flugel: secure personal build, reconnects and signed updates
- 2ed40ac3f | 2026-10-28 | style: apply spotless formatting to LibraryConnectionProfilesScreen (#1)
- df5d324a0 | 2026-10-23 | docs: clarify project purpose, setup and repository naming
- 04d8e34ef | 2026-10-18 | Daha Fazla menusune Manga indir (Tranga) ve Kutuphaneye ekle (yukleme) kisayollari
- 37eb2d40d | 2026-10-18 | Kitaplar sekmesi icin ayri baglanti: Komga ve Kavita ayni anda (Cizgi roman / Kitaplar sekmeleri)
- 593681613 | 2026-10-18 | Komga SSE yolunu duzelt (/sse/v1/events) ve test APK surum etiketini parametre yap
- 761c2fac0 | 2026-10-18 | Prepare Flugel Manga test APK and server setup
- a95a23b0c | 2026-10-06 | fix: 修复升级时重复建表导致的启动崩溃 / Fix upgrade startup migration crash
- 0f287cdf0 | 2026-10-06 | release: 准备 0.7.0，完善文档与墨水屏适配 / Prepare 0.7.0 with docs and E-Ink fixes
- c28ad51fc | 2026-10-06 | feat: 接入 Suwayomi 与网络存储并完善共享阅读功能 / Add Suwayomi and network storage integration
- 6c4560533 | 2026-10-03 | docs: enforce shared provider contracts / 规范跨库通用能力与验证
- 5a4c45a69 | 2026-10-03 | fix: 修复书籍下载并完善 Kavita 书架状态 / Fix book downloads and Kavita shelf status
- 1232f7cef | 2026-10-03 | fix: 修复本地系列与 EPUB 阅读进度 / Fix local series and EPUB reading progress
- a492b9975 | 2026-10-03 | feat: 完善阅读器设置与翻页体验 / Improve reader settings and page-turn behavior
- c7dfde60b | 2026-10-02 | feat: 统一本地系列元数据编辑并修复阅读流程 / Unify local series metadata editing and stabilize reader flows
- 99bddf1c5 | 2026-09-27 | fix(local): improve archive loading and restore entry opening settings
- 17fe06013 | 2026-09-27 | docs: document Kavita support in Chinese and English READMEs
- e62b1674a | 2026-09-27 | fix(ui): use E-Ink aware loading indicators
- fdffa453d | 2026-09-27 | feat(kavita): add native integration and reliable reading sync
- c59e86afd | 2026-09-26 | feat: unify library search and improve reader image handling
- e9fe432ad | 2026-09-24 | feat: prepare 0.6.0 with local library UI and support updates
- 18a787b66 | 2026-09-24 | fix: optimize local library scanning and share chapter display mode
- adb9ea0ba | 2026-09-24 | feat(settings): improve shelf and chapter display controls
- 14a33ed26 | 2026-09-24 | fix(download): improve large-file transfers and retry recovery
- 2f8d90c54 | 2026-09-23 | fix(reader): preserve Markdown code formatting and heading positions
- 73a0d2d36 | 2026-09-23 | Feat/markdown: 支持本地 Markdown 文件阅读 + Markdown 文档大纲导航 (#95)
- f88c7597b | 2026-09-23 | chore(codex): remove project subagent configuration
- c9a04f191 | 2026-09-23 | feat(backup): preserve user data across backup and restore

### /mnt/side/projects/flugel
- 481cad7 | 2026-10-18 | gN: Island v3 yayin kapisi: Hizli izgaralari kart genisligine gore sutun sayisini yeniden hesaplar (560/720 EN tasmasi giderildi), dar kartta medya kapagi 80px
- 2c116ca | 2026-10-18 | Design isolated FLUGEL Cyber Range curriculum
- 9b89808 | 2026-10-18 | Test Island v3 English responsive layout
- 089f98c | 2026-10-18 | gN: Island v3 bildirim + muzik (Codex AI-023): uc fazli esitleyici 2fps, oynatici kapak tonu yok + v3 duzeni, bildirim afisi durum cizgisi/kritik amber, Bildirimler sayfasi okunmamis/kategori gruplama/okundu say/iki adimli temizle (kritik korunur); isinma turu okundu saymaz
- 99036fd | 2026-10-18 | Test Island activity mute and promotion rules
- bc54258 | 2026-10-18 | Design v3 notification and media surfaces
- 159b954 | 2026-10-18 | gN: Island v3.1 canli etkinlik susturma (1 saat/oturum) + onceliklendirme; kritik (gizlilik/panik) susturulamaz; sag tik/Menu tusu satir menusu
- 104edd9 | 2026-10-18 | gN: Island v3.1 kompakt medya ilerleme cizgisi (2px, yalniz gorunurken en cok 1Hz, sure/konum dogrulama)
- 59a823c | 2026-10-18 | gN: Island v3.1 Hizli arac sabitleme: Tumu > Hizliyi duzenle, en cok 4, sira korunur, hizli-araclar ayari
- 5a375d6 | 2026-10-18 | Plan Island v3.1 feature priorities
- 1463d36 | 2026-10-18 | gN: Island Maclar kategori haplari dar kartta iki satira bolunur (sag kenar kesimi giderildi)
- 1f6b384 | 2026-10-18 | gN: Island v3 asama 2: Hizli kisa gorunum + Tumu (4 ayar/4 uygulama/4 arac, hicbir eylem silinmez), v3'te opak mat kart, Izgara yeniden dizme, isinma turu secimi korur, EN ceviriler
- 16cd3be | 2026-10-18 | Document GNOME v3 visual review findings
- 47a2a35 | 2026-10-18 | gN: Island v3 Quiet Orbit asama 1: tasarim=v3, bes grup + ic secim, 4 baslik dugmesi + Daha fazla seridi, en cok 2 canli + N daha, v3 hareketleri (BACK yok, yay 0.33/0.95)
- c73fe7e | 2026-10-18 | Clarify Island v3 wide-card layout
- 9fa9302 | 2026-10-18 | Refine Island v3 from joint design review
- 83cb18c | 2026-10-18 | Prototype Island v3 hover and event motion
- b533e4a | 2026-10-18 | Specify Island v3 motion and reference-inspired interactions
- 7a29ef9 | 2026-10-18 | Design Island v3 Quiet Orbit visual system
- 1c82a93 | 2026-10-17 | gN: Island kart menusu v2 bilgi mimarisi ve uc maket
- 9f5b727 | 2026-10-17 | gN: Island Monochrome Contour tasarimi (AI-010) - opak katman tokenlari, sekme rayi, karo/dugme durumlari, sekme secici 220ms ease-out
- 4ac5abb | 2026-10-17 | gN: Island için hafif monokrom tasarım paketi
- 8cb237e | 2026-10-17 | gN: Island İngilizce çeviri ve dil önceliğini düzelt
- dce83a5 | 2026-10-17 | sunucu: tüm yapı depoda — 37 Docker yığını, servisler, betikler, Cloudflare tüneli, sanal makine tanımları, mullvad-ts masaüstü betikleri; IP/alan adı/gizliler temizle.py ile çıkarıldı (env.ornek), topla.sh guncelle.sh'ye bağlandı
- fd9f347 | 2026-10-17 | gN: Island gecisinde cift blur yukunu kaldir
- 60692a6 | 2026-10-17 | gN: Island performans ve tasarim devrini kaydet
- 9b0df19 | 2026-10-17 | gN: Island blur yukunu azalt ve koyu gorunumu incelt
- 2a31333 | 2026-10-17 | gN: PiP stres testi doğrulamasını devre ekle
- 26ae29d | 2026-10-17 | gN: PiP yük testinde pencere görünürlüğünü doğrula
- 5167ea0 | 2026-10-17 | gN: PiP düzeltmesi devir commitlerini kaydet

### /mnt/side/projects/flugel-cyber-lab
- 025edff | 2026-10-18 | Public yayin oncesi temizlik: test kapsam adresleri ornek adreslerle degistirildi (gercek sunucu IP/alan adi cikarildi), data/ tamamen gitignore
- fb1329e | 2026-10-18 | Savunma odakli icerik: Kullanilabilirlik ve DoS dersi (kavram + savunma, saldiri araci yok) + 5 dayaniklilik bulmacasi (hiz siniri, log patlamasi, SYN cookie, amplifikasyon kavrami, fail open/closed)
- 0adb061 | 2026-10-18 | Arayuz (React/Vite: Ana sayfa, Ogretici, Bulmacalar, Lablar) ve README dokumantasyonu
- b27d50c | 2026-10-18 | Faz 1 iskelet: API (FastAPI/SQLModel), icerik yukleyici, oturum flag (HMAC), dar runner (izin listesi, kapasite, kapsam), ilk lab (linux-permission-leak), 5 ogretici ders, 12 bulmaca, guvenlik politikasi testleri (20 test)

### /mnt/side/projects/flugel-island
- 6d1b10a | 2026-10-18 | 3.0.0 surum notu
- ec78c6b | 2026-10-18 | v3: duyarli Hizli izgaralari, dar kartta 80px kapak
- 551805b | 2026-10-18 | v3 bildirim ve muzik tasarimi
- fa2231b | 2026-10-18 | Document unreleased Quiet Orbit v3
- 0ce9ba2 | 2026-10-18 | v3.1 canli etkinlik susturma ve onceliklendirme
- 2474d7b | 2026-10-18 | v3.1 kompakt medya ilerleme cizgisi
- c0a2a87 | 2026-10-18 | v3.1 Hizli arac sabitleme
- 5ed1b38 | 2026-10-18 | Maclar kategori haplari dar kartta iki satir
- a6fcefb | 2026-10-18 | Island v3 asama 2: Hizli kisa gorunum ve Tumu, opak mat kart, ceviriler
- cea6183 | 2026-10-18 | Island v3 Quiet Orbit asama 1: bes grup gezinme, sade baslik, iki satir canli alan, v3 hareketleri
- aafc29a | 2026-10-17 | Monochrome Contour tasarimi: opak katman tokenlari, sekme rayi, karo/dugme durumlari, sekme secici 220ms ease-out
- 9d019b5 | 2026-10-17 | gN: Island İngilizce çeviri ve dil önceliğini düzelt
- 1fe2003 | 2026-10-17 | gN: Island gecisinde cift blur yukunu kaldir
- 7df2f8a | 2026-10-17 | gN: Island blur yukunu azalt ve koyu gorunumu incelt
- ce471b0 | 2026-10-17 | gN: PiP yük testinde pencere görünürlüğünü doğrula
- 64ccaf9 | 2026-10-17 | gN: PiP aktör yaşam döngüsü ve yük testi
- 6d2c589 | 2026-10-17 | Codex ve Claude icin ortak Island devir kurallari
- 27f3ba3 | 2026-10-17 | Uyku engelle paneli kart kapanınca takılı kalıyordu; ses denetimi kabuk kapanışında yok edilmiş öğelere dokunmuyor
- 5273e72 | 2026-10-16 | FLUGEL Island v2.9.0: Atoll düzeni (medya oynatıcı, pano yöneticisi, renk seçici, canlı izleme) + önceki görünüme dönüş ayarı
- de17a6a | 2026-10-16 | Lint düzeltmesi (hesap ayrıştırıcısı)
- 8e0a818 | 2026-10-16 | FLUGEL Island v2.8.0: hesap makinesi, kronometre, QR, hızlı not, pano dönüştürücüler; ekran görüntüsünde kart görünmez
- ed815ef | 2026-10-16 | FLUGEL Island v2.7.1: hızını koruyan yay animasyonu, daha hafif buzlu cam
- 5aa34e2 | 2026-10-16 | FLUGEL Island v2.7.0: iOS tarzı buzlu cam ve bulanık geçişler, oyun istek listesi + fiyat düşüş / PS Plus / Epic duyuruları, 164 uçtan uca test
- a8f51e3 | 2026-10-15 | FLUGEL Island v2.6.0: siyah bar, Oyunlar sekmesi (PS Plus, ücretsiz, fırsatlar, fiyat arama), kart boyutu düzeltmesi, 148 uçtan uca test
- aa4600e | 2026-10-15 | FLUGEL Island v2.5.1: çentik altındakine yol verir (yazı imleci, sürükleme, Super+Alt+I)
- e4c150b | 2026-10-15 | FLUGEL Island v2.5.0: çentik kipi, Akış sekmesi, düzeltmeler, 130 uçtan uca test
- fb3c995 | 2026-10-15 | FLUGEL Island v2.4.0: Atoll'dan esinlenen medya oynatıcı, güç paneli, zamanlayıcı, pano geçmişi, renk seçici, indirmeler, odak, hava durumu; yeni animasyonlar; 120 uçtan uca test
- 48c3319 | 2026-10-15 | FLUGEL Island v2.3.0: tam ekranda uygulama ile ada birlikte, büyütülmüş pencerede uygulama renginde şerit, 99 uçtan uca test
- baf2492 | 2026-10-15 | FLUGEL Island v2.2.0: ekranı kaplayan pencerede çentik (üst şerit pencerelere bırakıldı), Hızlı sekmesinde ses/parlaklık + uygulama sesleri, ayrıntılı Wi-Fi ve Bluetooth, tepsi adları, 91 uçtan uca test
- df7b12a | 2026-10-15 | FLUGEL Island v2.1.1: dokunmatik yüzeyde kaydırma/kart açılması, canlı maç vurgu zamanlayıcısı, CS2 harita sıfırlama, emoji yerine simgeler, kart CSS yalıtımı, uçtan uca testler (tests/altin)

### /mnt/side/projects/flugel-manga
- 17d127850 | 2026-10-18 | Manga indir aciklamasi: KamiYomu
- 04d8e34ef | 2026-10-18 | Daha Fazla menusune Manga indir (Tranga) ve Kutuphaneye ekle (yukleme) kisayollari
- 37eb2d40d | 2026-10-18 | Kitaplar sekmesi icin ayri baglanti: Komga ve Kavita ayni anda (Cizgi roman / Kitaplar sekmeleri)
- 593681613 | 2026-10-18 | Komga SSE yolunu duzelt (/sse/v1/events) ve test APK surum etiketini parametre yap
- 761c2fac0 | 2026-10-18 | Prepare Flugel Manga test APK and server setup
- a95a23b0c | 2026-10-06 | fix: 修复升级时重复建表导致的启动崩溃 / Fix upgrade startup migration crash
- 0f287cdf0 | 2026-10-06 | release: 准备 0.7.0，完善文档与墨水屏适配 / Prepare 0.7.0 with docs and E-Ink fixes
- c28ad51fc | 2026-10-06 | feat: 接入 Suwayomi 与网络存储并完善共享阅读功能 / Add Suwayomi and network storage integration
- 6c4560533 | 2026-10-03 | docs: enforce shared provider contracts / 规范跨库通用能力与验证
- 5a4c45a69 | 2026-10-03 | fix: 修复书籍下载并完善 Kavita 书架状态 / Fix book downloads and Kavita shelf status
- 1232f7cef | 2026-10-03 | fix: 修复本地系列与 EPUB 阅读进度 / Fix local series and EPUB reading progress
- a492b9975 | 2026-10-03 | feat: 完善阅读器设置与翻页体验 / Improve reader settings and page-turn behavior
- c7dfde60b | 2026-10-02 | feat: 统一本地系列元数据编辑并修复阅读流程 / Unify local series metadata editing and stabilize reader flows
- 99bddf1c5 | 2026-09-27 | fix(local): improve archive loading and restore entry opening settings
- 17fe06013 | 2026-09-27 | docs: document Kavita support in Chinese and English READMEs
- e62b1674a | 2026-09-27 | fix(ui): use E-Ink aware loading indicators
- fdffa453d | 2026-09-27 | feat(kavita): add native integration and reliable reading sync
- c59e86afd | 2026-09-26 | feat: unify library search and improve reader image handling
- e9fe432ad | 2026-09-24 | feat: prepare 0.6.0 with local library UI and support updates
- 18a787b66 | 2026-09-24 | fix: optimize local library scanning and share chapter display mode
- adb9ea0ba | 2026-09-24 | feat(settings): improve shelf and chapter display controls
- 14a33ed26 | 2026-09-24 | fix(download): improve large-file transfers and retry recovery
- 2f8d90c54 | 2026-09-23 | fix(reader): preserve Markdown code formatting and heading positions
- 73a0d2d36 | 2026-09-23 | Feat/markdown: 支持本地 Markdown 文件阅读 + Markdown 文档大纲导航 (#95)
- f88c7597b | 2026-09-23 | chore(codex): remove project subagent configuration
- c9a04f191 | 2026-09-23 | feat(backup): preserve user data across backup and restore
- 2484de18b | 2026-09-22 | feat(smanga): add native server integration and reading support
- dcf5449c1 | 2026-09-22 | docs: refresh README and automate Koharia contributor avatars
- 2830ad847 | 2026-09-22 | feat: improve reader layouts and dual-address server connections
- 933cd1a06 | 2026-09-21 | fix(reader): improve TTS continuity and reader controls

### /mnt/side/projects/home-server
- 77ad2c6 | 2026-10-18 | Record deployed manga catalog location
- 80fe9dc | 2026-10-18 | Clarify pending Kavita rescan verification
- b193059 | 2026-10-18 | Catalog manga series and classify ReZero libraries safely
- cbc2ba8 | 2026-10-18 | Add guarded library organization and rollback plan
- a9f12c4 | 2026-10-17 | telegram-kopru: duz mesaj cevabi ajan gelen kutusuna yonlendirildi
- 7c126fc | 2026-10-17 | Clarify Telegram bridge is not the Claude chat bot
- e3938f5 | 2026-10-17 | Document live desktop gateway and optimization safeguards
- b3db574 | 2026-10-17 | Add scoped Telegram server bridge source
- 5c4a1e4 | 2026-10-17 | Refine dry-run optimization scripts after review
- eb3d1d6 | 2026-10-17 | gN: Sunucu için kuru varsayılan optimizasyon araçları
- 99230c7 | 2026-10-17 | Ayrıntılı belgeler: mimari (şema), ağ ve erişim, depolama, yedekleme, izleme, güvenlik, sanal makineler, uzak masaüstü, kurulum, bakım; otomatik tablolar (yığınlar, servisler, betikler, sanal makineler, tüneller); tüm sistem ayarları ve envanter
- d1df0b7 | 2026-10-17 | home-server: ev sunucusunun tüm yapısı (sistem, Docker yığınları, servisler, betikler, botlar, tüneller, sanal makineler, envanter); gizli ve kişisel bilgiler temizlendi

### /opt/stacks
- Command '['git', '-C', '/opt/stacks', 'log', '-n', '30', '--oneline', '--date=short', '--pretty=format:%h | %ad | %s']' returned non-zero exit status 128.

## 2. Özel Bakım ve Otomasyon Betikleri (/usr/local/sbin & /usr/local/bin)
### /usr/local/sbin
- `/usr/local/sbin/__pycache__`
- `/usr/local/sbin/ai-gozcu.sh`
- `/usr/local/sbin/ai-gozcu.sh.yedek-20261031-claude`
- `/usr/local/sbin/ai-gozcu.sh.yedek-20261104-katman`
- `/usr/local/sbin/ai-saglik-sor`
- `/usr/local/sbin/ai-vm-koruma.sh`
- `/usr/local/sbin/ai-vm-koruma.sh.before-hook`
- `/usr/local/sbin/ai-vm-koruma.sh.before-ramguard`
- `/usr/local/sbin/ai-vm-koruma.sh.yedek-20261028`
- `/usr/local/sbin/ai-vm-koruma.sh.yedek-20261104-katman`
- `/usr/local/sbin/alarm-koprusu.py`
- `/usr/local/sbin/ara-bitir`
- `/usr/local/sbin/aylik-rapor`
- `/usr/local/sbin/db-dokum`
- `/usr/local/sbin/disk-koruyucu.sh`
- `/usr/local/sbin/docker-guvenlik-duvari.sh`
- `/usr/local/sbin/eski-yedek-temizle`
- `/usr/local/sbin/fhs-kontrol.sh`
- `/usr/local/sbin/flugel-geri-yukleme-testi`
- `/usr/local/sbin/flugel-uyari.sh`
- `/usr/local/sbin/flugel-yedek`
- `/usr/local/sbin/gece-yedek`
- `/usr/local/sbin/giris-durum.py`
- `/usr/local/sbin/giris-durum.py.yedek-20261104-ajan`
- `/usr/local/sbin/island-veri.py`
- `/usr/local/sbin/island-veri.py.onceki-2026-10-14_1408`
- `/usr/local/sbin/kaynak-gozcu.sh`
- `/usr/local/sbin/klasor-boyut`
- `/usr/local/sbin/kritik-yedek-ssd.sh`
- `/usr/local/sbin/kritik-yedek.sh`
- `/usr/local/sbin/proje-surum.sh`
- `/usr/local/sbin/rehber-guncelle.py`
- `/usr/local/sbin/savunma-denetim`
- `/usr/local/sbin/suwayomi-sinir`
- `/usr/local/sbin/suwayomi-sinir.yedek-20261104-katman`
- `/usr/local/sbin/taildrop-nextcloud`
- `/usr/local/sbin/taildrop-nextcloud.before-taildraop`
- `/usr/local/sbin/torrent-bekci.sh`
- `/usr/local/sbin/uygulama-katman`
- `/usr/local/sbin/uygulama-katman.yedek-20261104-danisman`
- `/usr/local/sbin/uygulama-yedek.py`
- `/usr/local/sbin/virus-tarama.sh`
- `/usr/local/sbin/vm-bosta-kapat.py`
- `/usr/local/sbin/vm-kapandi.sh`
- `/usr/local/sbin/vm-proje-esitle.sh`
- `/usr/local/sbin/vm-uyandir.sh`
- `/usr/local/sbin/vm-yedek.sh`
- `/usr/local/sbin/vm-yonlendir.sh`
- `/usr/local/sbin/vpn-ip-degistir.sh`
- `/usr/local/sbin/yedek-metrik`
### /usr/local/bin
- `/usr/local/bin/.gpu-release.sh.swp`
- `/usr/local/bin/agy`
- `/usr/local/bin/ai-sohbet`
- `/usr/local/bin/antigravity`
- `/usr/local/bin/bildirim`
- `/usr/local/bin/boot-notify.sh`
- `/usr/local/bin/cloudflared`
- `/usr/local/bin/disk-health-report.sh`
- `/usr/local/bin/disk-keepalive.sh`
- `/usr/local/bin/docker-watcher.sh`
- `/usr/local/bin/emoji-sembol`
- `/usr/local/bin/google-oauthlib-tool`
- `/usr/local/bin/gpu-bind.sh`
- `/usr/local/bin/gpu-release.sh`
- `/usr/local/bin/gpu-to-host.sh`
- `/usr/local/bin/gpu-to-vm.sh`
- `/usr/local/bin/hf`
- `/usr/local/bin/httpx`
- `/usr/local/bin/huggingface-cli`
- `/usr/local/bin/markdown-it`
- `/usr/local/bin/morning-report.sh`
- `/usr/local/bin/pygmentize`
- `/usr/local/bin/self-heal.sh`
- `/usr/local/bin/self-heal.sh.yedek-20261031-claude`
- `/usr/local/bin/self-heal.sh.yedek-20261104-danisman`
- `/usr/local/bin/smartd-gotify.sh`
- `/usr/local/bin/smartd-whatsapp.sh`
- `/usr/local/bin/ssh-login-watcher.sh`
- `/usr/local/bin/swap-flush.sh`
- `/usr/local/bin/telegram-kur`
- `/usr/local/bin/tiny-agents`
- `/usr/local/bin/tqdm`
- `/usr/local/bin/typer`
- `/usr/local/bin/vm`
- `/usr/local/bin/weekly-maintenance.sh`
- `/usr/local/bin/yz`
- `/usr/local/bin/yz.bak`
- `/usr/local/bin/yz.before-library-20261026`
- `/usr/local/bin/yz.yedek-20261031-claude`
- `/usr/local/bin/yz.yedek-20261031-gemini`

## 3. Systemd Zamanlayıcıları (systemctl list-timers)
```
NEXT                                  LEFT LAST                              PASSED UNIT                         ACTIVATES
Wed 2026-11-11 14:51:09 UTC            18s Wed 2026-11-11 14:50:49 UTC       1s ago island-veri.timer            island-veri.service
Wed 2026-11-11 14:51:09 UTC            18s Wed 2026-11-11 14:50:49 UTC       1s ago torrent-bekci.timer          torrent-bekci.service
Wed 2026-11-11 14:51:39 UTC            48s Wed 2026-11-11 14:49:39 UTC 1min 11s ago giris-durum.timer            giris-durum.service
Wed 2026-11-11 14:51:39 UTC            48s Wed 2026-11-11 14:49:39 UTC 1min 11s ago kaynak-gozcu.timer           kaynak-gozcu.service
Wed 2026-11-11 14:51:49 UTC            58s Wed 2026-11-11 14:50:49 UTC       1s ago vm-bosta-kapat.timer         vm-bosta-kapat.service
Wed 2026-11-11 14:52:08 UTC       1min 18s Wed 2026-11-11 14:47:08 UTC 3min 41s ago swap-flush.timer             swap-flush.service
Wed 2026-11-11 14:52:18 UTC       1min 28s Wed 2026-11-11 14:47:18 UTC 3min 31s ago docker-watcher.timer         docker-watcher.service
Wed 2026-11-11 14:52:39 UTC       1min 48s Wed 2026-11-11 14:47:39 UTC 3min 11s ago uyg-bosta.timer              uyg-bosta.service
Wed 2026-11-11 14:52:39 UTC       1min 48s Wed 2026-11-11 14:49:39 UTC 1min 11s ago self-heal.timer              self-heal.service
Wed 2026-11-11 14:54:58 UTC        4min 8s Wed 2026-11-11 14:44:58 UTC     5min ago disk-koruyucu.timer          disk-koruyucu.service
Wed 2026-11-11 14:55:00 UTC        4min 9s Wed 2026-11-11 14:25:00 UTC    25min ago pmproxy_check.timer          pmproxy_check.service
Wed 2026-11-11 14:58:00 UTC           7min Wed 2026-11-11 14:28:00 UTC    22min ago pmie_check.timer             pmie_check.service
Wed 2026-11-11 14:58:10 UTC           7min Wed 2026-11-11 14:28:10 UTC    22min ago pmie_farm_check.timer        pmie_farm_check.service
Wed 2026-11-11 15:00:00 UTC           9min Wed 2026-11-11 14:00:02 UTC    50min ago basket-bot.timer             basket-bot.service
Wed 2026-11-11 15:00:00 UTC           9min Wed 2026-11-11 14:50:02 UTC      47s ago sysstat-collect.timer        sysstat-collect.service
Wed 2026-11-11 15:05:00 UTC          14min Wed 2026-11-11 14:05:02 UTC    45min ago anime-takip.timer            anime-takip.service
Wed 2026-11-11 15:09:00 UTC          18min Wed 2026-11-11 14:39:02 UTC    11min ago phpsessionclean.timer        phpsessionclean.service
Wed 2026-11-11 15:20:00 UTC          29min Wed 2026-11-11 14:50:02 UTC      47s ago pmlogger_check.timer         pmlogger_check.service
Wed 2026-11-11 15:20:10 UTC          29min Wed 2026-11-11 14:50:18 UTC      32s ago pmlogger_farm_check.timer    pmlogger_farm_check.service
Wed 2026-11-11 15:39:31 UTC          48min Tue 2026-11-10 22:40:41 UTC      16h ago apt-daily.timer              apt-daily.service
Wed 2026-11-11 15:48:41 UTC          57min Wed 2026-11-11 14:48:19 UTC 2min 31s ago vpn-ip-degistir.timer        vpn-ip-degistir.service
Wed 2026-11-11 18:10:59 UTC       3h 20min Wed 2026-11-11 05:42:02 UTC       9h ago motd-news.timer              motd-news.service
Thu 2026-11-12 00:00:00 UTC             9h Wed 2026-11-11 00:00:01 UTC      14h ago chkrootkit.timer             chkrootkit.service
Thu 2026-11-12 00:00:00 UTC             9h Wed 2026-11-11 00:00:01 UTC      14h ago dpkg-db-backup.timer         dpkg-db-backup.service
Thu 2026-11-12 00:00:00 UTC             9h Wed 2026-11-11 00:00:01 UTC      14h ago sysstat-rotate.timer         sysstat-rotate.service
Thu 2026-11-12 00:07:00 UTC             9h Wed 2026-11-11 00:07:01 UTC      14h ago sysstat-summary.timer        sysstat-summary.service
Thu 2026-11-12 00:08:00 UTC             9h Wed 2026-11-11 00:08:01 UTC      14h ago pmie_daily.timer             pmie_daily.service
Thu 2026-11-12 00:10:00 UTC             9h Wed 2026-11-11 00:10:01 UTC      14h ago pmlogger_daily.timer         pmlogger_daily.service
Thu 2026-11-12 00:15:00 UTC             9h Wed 2026-11-11 00:15:00 UTC      14h ago pmproxy_daily.timer          pmproxy_daily.service
Thu 2026-11-12 00:33:16 UTC             9h Wed 2026-11-11 00:34:47 UTC      14h ago flugel-yedek.timer           flugel-yedek.service
Thu 2026-11-12 00:40:20 UTC             9h Wed 2026-11-11 00:49:40 UTC      14h ago logrotate.timer              logrotate.service
Thu 2026-11-12 02:30:00 UTC            11h Wed 2026-11-11 02:30:00 UTC      12h ago proje-surum.timer            proje-surum.service
Thu 2026-11-12 06:00:00 UTC            15h Wed 2026-11-11 06:00:02 UTC       8h ago rehber-guncelle.timer        rehber-guncelle.service
Thu 2026-11-12 06:03:11 UTC            15h Wed 2026-11-11 06:00:08 UTC       8h ago apt-daily-upgrade.timer      apt-daily-upgrade.service
Thu 2026-11-12 06:24:51 UTC            15h Wed 2026-11-11 06:22:49 UTC       8h ago imdb-puan.timer              imdb-puan.service
Thu 2026-11-12 09:17:20 UTC            18h Wed 2026-11-11 13:28:37 UTC 1h 22min ago certbot.timer                certbot.service
Thu 2026-11-12 10:38:41 UTC            19h Wed 2026-11-11 10:38:41 UTC 4h 12min ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
Thu 2026-11-12 12:46:21 UTC            21h Wed 2026-11-11 12:46:21 UTC  2h 4min ago etckeeper.timer              etckeeper.service
Thu 2026-11-12 13:00:00 UTC            22h Wed 2026-11-11 13:00:02 UTC 1h 50min ago morning-report.timer         morning-report.service
Sat 2026-11-14 02:00:00 UTC         2 days Sat 2026-11-07 02:00:05 UTC   4 days ago flugel-yedek-kontrol.timer   flugel-yedek-kontrol.service
Sat 2026-11-14 23:00:00 UTC         3 days Sat 2026-11-07 23:00:02 UTC   3 days ago klasor-boyut.timer           klasor-boyut.service
Sun 2026-11-15 03:10:32 UTC         3 days Sun 2026-11-08 03:10:40 UTC   3 days ago e2scrub_all.timer            e2scrub_all.service
Sun 2026-11-15 03:10:51 UTC         3 days Sun 2026-11-08 03:10:47 UTC   3 days ago xfs_scrub_all.timer          xfs_scrub_all.service
Sun 2026-11-15 04:10:00 UTC         3 days Sun 2026-11-08 04:10:01 UTC   3 days ago savunma-denetim.timer        savunma-denetim.service
Sun 2026-11-15 05:00:00 UTC         3 days Sun 2026-11-08 05:00:01 UTC   3 days ago weekly-maintenance.timer     weekly-maintenance.service
Sun 2026-11-15 10:00:00 UTC         3 days Sun 2026-11-08 10:00:01 UTC   3 days ago disk-health.timer            disk-health.service
Mon 2026-11-16 01:28:46 UTC         4 days Mon 2026-11-09 00:07:54 UTC   2 days ago fstrim.timer                 fstrim.service
Wed 2026-11-18 02:00:00 UTC         6 days Wed 2026-11-11 02:00:00 UTC      12h ago virus-tarama.timer           virus-tarama.service
Tue 2026-12-01 06:00:00 UTC 2 weeks 5 days -                                      - aylik-rapor.timer            aylik-rapor.service
-                                        - -                                      - apport-autoreport.timer      apport-autoreport.service
-                                        - -                                      - snapd.snap-repair.timer      snapd.snap-repair.service

51 timers listed.
```
