---
tur: harita
etiketler:
  - harita
  - moc
  - ikinci-beyin
olusturma: 2026-11-11
guncelleme: 2026-11-14
---

# HARITA.md — İkinci Beyin Ana Haritası

> **Fırtınanın Merkezi:** Her oturumda ilk bu dosya okunur. Bilgi nerede yaşar, dosyalar nasıl adlandırılır ve sorular nasıl yanıtlanır burada tanımlıdır. Klasör sistemi ve "yeni bilgi nereye?" kuralları: [[ARSIV-SISTEMI]]. Odak dosyaları: [[simdi]] · [[hafiza]] · [[kararlar]] · [[dersler]] · [[gelen-kutusu]] · [[CLAUDE]].

---

## 1. Bilgi Türleri ve Klasör Haritası (`where things live`)

| Klasör / Dosya | Amacı | Kapsam Kuralı |
|---|---|---|
| **`HARITA.md`** | Tüm bilgi ağının tek merkezi indeks haritası | Her yeni dosya eklendiğinde buraya bir satır eklenir |
| **`simdi.md`** ([[simdi]]) | Bu hafta odaktaki aktif işler ve sıradaki adımlar | Her oturum başında `CLAUDE.md` ile yüklenir |
| **`hafiza.md`** ([[hafiza]]) | Kalıcı tercihler, makineler, sunucu ve kimlik gerçekleri | 200 satırın altında tutulur |
| **`kararlar.md`** ([[kararlar]]) | Tarih, karar, neden ve değerlendirilen alternatifler | Mimari/operasyonel her karar buraya işlenir |
| **`dersler.md`** ([[dersler]]) | Öğrenilen teknik dersler, veri tuzakları ve hatalar | Tekrarlanmaması gereken hatalar |
| **`gelen-kutusu.md`** ([[gelen-kutusu]]) | Hızlı notlar ve tasnif bekleyen girdiler | Haftalık gözden geçirmede ilgili klasöre taşınır |
| **`notlar/`** | Kişisel ve teknik bilgi notları (her dosyada tek konu) | [[kurallar/notlar]] |
| **`kisiler/`** | Kişi kartları (rol, sorumluluk, iletişim yolu, projeler) | [[kurallar/kisiler]] |
| **`projeler/`** | Her projenin durumu, sıradaki adımı ve bağlantıları | [[kurallar/projeler]] |
| **`kurallar/`** | Yol kapsamlı çalışma ve güvenlik kuralları | [[kurallar/guvenlik]] |
| **`sablonlar/`** | Kişi, proje, karar ve not şablonları | [[sablonlar/not]], [[sablonlar/proje]], [[sablonlar/kisi]], [[sablonlar/karar]] |
| **`raw/`** | Ham kaynaklar (`flugelserver`, `github`, `yerel-ai`, `duduk`) | **Salt okunur** (`Edit(/raw/**)` yasaklı) |
| **`wiki/`** | `raw/` kaynaklarından derlenen doğrulanmış wiki sayfaları | `python3 brain.py lint` ile denetlenir (`0 problem`) |
| **`projeler/duduk-derin-referans/`** | Düdük için uzun, modüler derin teknik referans (eski `Düdük - Side Brain/`) | Dosya adları korunur; giriş: [[00 - Düdük MOC (Ana Merkez)]] |
| **`_arsiv/`** | Artık aktif olmayan, ama silinmeyen içerik (`_arsiv/eski/`: eski İngilizce kök dosyalar) | Salt arşiv; yeni bilgi yazılmaz. Kurallar: [[ARSIV-SISTEMI]] |

---

## 2. Kişiler (`kisiler/`)
- [[kisiler/ahmet-gokalp-goksu]] — Ahmet Gökalp Göksu (Ankara basketbol hakemi `"AHMET GÖKALP GÖKSU"`, Gazi EEM öğrencisi, `flugelserver` ve `gok8lp` geliştiricisi)

---

## 3. Projeler (`projeler/`)
- [[projeler/duduk]] — **Düdük** Android hakem takip uygulaması ve `flugelserver` Docker arka ucu (`gok8lp/duduk`, `v0.1.0`)
  - **Düdük Derin Teknik Referans (`projeler/duduk-derin-referans/`):** [[00 - Düdük MOC (Ana Merkez)]] · [[01 - Veri Kaynakları ve API Analizi]] · [[02 - TBF Maç ve Lig Eşleştirme Algoritması]] · [[03 - Yerel Arşiv, Birleştirme ve Değişiklik Tespiti]] · [[04 - Hakem İstatistikleri ve 2026-2027 Ücret Tarifesi]] · [[05 - Android Mimari, Senkronizasyon, Bildirimler ve Arayüz]] · [[2026-2027 Ankara Lig Eşleşme Tablosu]] · [[Veri Tuzakları ve Uç Durumlar Kataloğu]]
- [[projeler/flugel-manga]] — **Flugel Manga (`koharia-reader`)** Android manga okuyucu (`Komga`, `Kavita`, `Suwayomi` entegrasyonu)
- [[projeler/okul-guz-2026]] — **Gazi EEM 2026 Güz Dönemi** (`EE313 Elektrik Makinaları I`, `EE333 Endüstriyel Otomasyon`, vize çalışma planı)
- [[projeler/hakemlik]] — **2026-2027 Ankara Basketbol Hakemliği** (atamalar, TBF/FIBA 2026 kuralları, görevli ücretleri)
- [[projeler/flugel-sunucu-ve-akis]] — **flugelserver & FLUGEL Akış** (`home-server`, `home-server-android`, `desktop-server-toolkit`, `flugel-akis`)
- [[projeler/linux-masaustu-araclari]] — **Linux Masaüstü & Hyprland / GNOME Araçları** (`end4-pC`, `gnome-island`, `gnome-pip-konum`, `headset-surround-linux`, `clipline-linux`, `k380s-ubuntu-fn`, `chrome-orta-tik-kaydirma`, `ubuntu-tam-guncelle`)
- [[projeler/siber-guvenlik-ve-sistem-lab]] — **Siber Güvenlik ve Sistem Programlama** (`cybersecurity-lab`, `c-process-tree`, `c-password-generator`, `c-text-shuffler`, `c-calismalarim`, `java-producer-consumer`)
- [[projeler/web-portfolyo]] — **Kişisel Web ve Portfolyo** (`gok8lp.github.io`, `wix-anilist-portfolio`, `gok8lp`)

---

## 4. Bilgi Notları (`notlar/`)
- [[notlar/flugelserver-uc-disk-ve-klasor-agaci]] — `flugelserver` 3 LUKS disk (`/`, `/mnt/side`, `/mnt/sidemain`) ve tam klasör ağacı
- [[notlar/docker-uygulama-baglanti-topolojisi]] — Tüm Docker servislerinin birbirine bağlanma topolojisi (`Gluetun`, `*arr`, `Immich`, `Nextcloud`, `Komga`, `FLUGEL Akış`, `duduk-server`)
- [[notlar/docker-medya-ve-arr-yigini]] — `Sonarr`, `Radarr`, `Bazarr`, `Prowlarr`, `Jackett`, `FlareSolverr`, `Transmission`, `Gluetun`, `Jellyfin`, `Plex`
- [[notlar/docker-manga-ve-kitap-yigini]] — `Suwayomi`, `Komga`, `Kavita`, `Kamiyomu` ve `Koharia Reader`
- [[notlar/docker-bulut-ve-fotograf-yigini]] — `Nextcloud`, `Nextcloud-DB`, `Immich Server`, `Immich CUDA ML`, `Postgres`, `Redis`
- [[notlar/docker-ag-panel-ve-altyapi-yigini]] — `giris` (nginx), `flugel-akis`, `duduk-server`, `tsidp`, `adguard`, `guacamole`, `uptime-kuma`, `ollama`
- [[notlar/sunucu-dizi-ve-film-arsivi-envanteri]] — `/mnt/sidemain/media/movies` ve `/mnt/sidemain/media/series` tam envanteri
- [[notlar/sunucu-anime-manga-ve-rezero-arsivi]] — `/mnt/sidemain/media/books/ln` (Re:Zero) ve `/mnt/sidemain/media/books/manga` tam envanteri
- [[notlar/sanal-makineler-w11-gpu-ve-moonlight]] — `W11`, `W11-GPU`, `GTX 1660 Ti` passthrough ve `Apollo`/`Moonlight`
- [[notlar/sunucu-yedekleme-ve-systemd-otomasyonlari]] — `uygulama-yedek.py`, `kritik-yedek.sh`, `self-heal.sh`, `ai-gozcu.sh` ve systemd zamanlayıcıları
- [[notlar/pc-arch-hyprland-ve-ubuntu-gnome-analizi]] — PC donanım, Hyprland/GNOME masaüstü ve AI çalışma alanı analizi
- [[notlar/laptop-thinkbook-arch-hyprland-kurulumu]] — Laptop (ThinkBook 16p G4) Arch + Hyprland kurulum günlüğü: sürücüler, Tailscale, taşınan config, Noctalia/Ambxst denemeleri, greeter
- [[notlar/laptop-thinkbook-dosya-agaci]] — Laptop disk düzeni (LUKS + btrfs alt birimleri) ve ev klasörü ağacı
- [[notlar/laptop-dux-shell-arayuzu]] — Laptop arayüzü: Dux Modular Shell kurulumu, Caelestia benzeri çerçeve/dock, özel önizleme yaması
- [[notlar/laptop-dux-ozellestirme-oturumu-2026-11-13]] — Laptop Dux/Hyprland özelleştirme oturumu (12-13 Kasım 2026): yapılanlar, dosya haritası, pencere sistemi ve sol-panel düzeltmeleri, bekleyen işler
- [[notlar/gazi-eem-vize-takvimi-ve-ders-notlari]] — Gazi EEM Güz 2026 dersleri ve vize çalışma takvimi
- [[notlar/tbf-basketbol-kurallari-ve-fiba-2026]] — TBF kural kitabı ve FIBA 2026 değişiklikleri
- [[notlar/ee317-vize-calismasi-2026-11-11]] — EE317 Güç Elektroniği I vizesi (12 Kasım 2026): kapsam D1–D4, dosyalar, H01–H10 konumları, ilerleme
- [[notlar/claude-hafizasi]] — Claude Code belleğinin aktarımı: ders çalışma tercihleri, Claude–Codex ortak klasör düzeni
- [[notlar/flugel-akis-mobil-uygulama]] — FLUGEL Akış `akis.gokalpgoksu.com` (şifresiz, Tailscale'siz) ve Android kabuğu `FLUGEL-Akis.apk` 2.0: derleme, imza, dağıtım, geri alma
- [[notlar/assignr-api-yapisi]] · [[notlar/ankarabasket-rsc-flight-ayristirma]] · [[notlar/tbf-bulanik-mac-eslestirme]] · [[notlar/hakem-kazanc-ve-bolge-kurali]] · [[notlar/cloudflare-ve-tailscale-baglanti-zinciri]]

---

## 5. Derlenmiş Wiki (`wiki/` — `brain.py lint` ile Doğrulanmış 48 Sayfa)
- **Giriş ve Özet:** [[wiki/hot]] · [[wiki/index]] · [[wiki/log]] · [[ikinci-beyin-sistemi]]
- **Düdük Çekirdeği:** [[duduk-genel-bakis]] · [[assignr-ve-ankarabasket-kaynaklari]] · [[tbf-eslestirme-algoritmasi]] · [[yerel-arsiv-ve-senkronizasyon]] · [[hakem-ucret-tarifesi-2026-2027]] · [[android-arac-zinciri-ve-mimari]]
- **flugelserver Mimari ve Arşivler:** [[flugelserver-genel-mimari]] · [[flugelserver-docker-uygulamalari]] · [[flugelserver-uygulama-baglantilari]] · [[flugelserver-dizi-film-arsivi]] · [[flugelserver-anime-manga-lightnovel-arsivi]] · [[flugelserver-dosya-agaci-ve-diskler]] · [[flugelserver-yedekleme-ve-otomasyon]] · [[flugelserver-sanal-makineler-ve-gpu]] · [[flugelserver-ag-guvenlik-ve-tuneller]] · [[flugel-akis-ve-botlar]] · [[sunucu-ve-github-commit-gecmisi]]
- **GitHub 23 Depo Kataloğu:** [[github-repolar-katalogu]] · [[koharia-reader-ve-manga-ekosistemi]] · [[pc-masaustu-hyprland-ve-gnome-araclari]] · [[ee313-ve-hakemlik-calisma-plani]]
  - [[repo-duduk]] · [[repo-koharia-reader]] · [[repo-basketbol-kurallar-calisma]] · [[repo-headset-surround-linux]] · [[repo-end4-pc]] · [[repo-ubuntu-tam-guncelle]] · [[repo-chrome-orta-tik-kaydirma]] · [[repo-gnome-pip-konum]] · [[repo-k380s-ubuntu-fn]] · [[repo-clipline-linux]] · [[repo-cybersecurity-lab]] · [[repo-c-password-generator]] · [[repo-c-text-shuffler]] · [[repo-gok8lp-github-io]] · [[repo-wix-anilist-portfolio]] · [[repo-java-producer-consumer]] · [[repo-c-process-tree]] · [[repo-home-server]] · [[repo-home-server-android]] · [[repo-gnome-island]] · [[repo-desktop-server-toolkit]] · [[repo-c-calismalarim]] · [[repo-gok8lp]]

---

## 6. Arşiv (`_arsiv/`)
- `_arsiv/eski/` — 2026-11-14 yeniden yapılandırmasında Türkçe karşılıklarına birleştirilen eski İngilizce kök dosyalar: [[_arsiv/eski/map|map]] (→ [[HARITA]]), [[_arsiv/eski/memory|memory]] (→ [[hafiza]]), [[_arsiv/eski/decisions|decisions]] (→ [[kararlar]]), [[_arsiv/eski/lessons|lessons]] (→ [[dersler]]), [[_arsiv/eski/inbox|inbox]] (→ [[gelen-kutusu]]) ve Obsidian varsayılan `Welcome.md`.
