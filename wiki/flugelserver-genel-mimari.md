---
title: flugelserver Genel Mimari, Donanım ve Sistem Özeti
sources: raw/flugelserver/00-OKU-BENI.txt, raw/flugelserver/01-HARITA.txt, raw/flugelserver/MIMARI.md, raw/flugelserver/IS-DURUMU.md, raw/flugelserver/BASLA.md, raw/flugelserver/KAYNAKLAR.md, raw/flugelserver/KULLANIM.md, raw/flugelserver/INFRASTRUCTURE.md, raw/flugelserver/MIMARI-DONUSUM-RAPORU-2026-10-20.md, raw/flugelserver/CLAUDE-DEVIR-2026-10-20.md, raw/flugelserver/KURUMSAL-SYSADMIN-DERSLERI.md, raw/flugelserver/AI_STATE_INDEX.md, raw/flugelserver/FLUGEL-OZET.md, raw/yerel-ai/home-server-SUNUCU.md, raw/yerel-ai/MIMARI.md, raw/yerel-ai/KURULUM.md
updated: 2026-11-11
---

# flugelserver Genel Mimari, Donanım ve Sistem Özeti

Bağlı Modüller: [[flugelserver-docker-uygulamalari]] · [[flugelserver-uygulama-baglantilari]] · [[flugelserver-dosya-agaci-ve-diskler]] · [[flugelserver-dizi-film-arsivi]] · [[flugelserver-anime-manga-lightnovel-arsivi]] · [[flugelserver-yedekleme-ve-otomasyon]] · [[flugelserver-sanal-makineler-ve-gpu]] · [[flugelserver-ag-guvenlik-ve-tuneller]] · [[flugel-akis-ve-botlar]] · [[duduk-genel-bakis]]

> "FLUGEL SUNUCU REHBERİ  —  /srv/rehber" - raw/flugelserver/00-OKU-BENI.txt

> "SUNUCU HARİTASI — neyin nerede olduğu (20 Ekim 2026, dizin düzeni tamamlandı 06:45)" - raw/flugelserver/01-HARITA.txt

> "Mimari — sabit yollar ve bağımlılıklar" - raw/flugelserver/MIMARI.md

> "İş durumu — 20 Ekim 2026 (Claude gecesi sonrası)" - raw/flugelserver/IS-DURUMU.md

## Donanım ve Disk Özeti (`flugelserver`)
- **İşlemci / GPU / RAM:** AMD Ryzen 5 2600X, NVIDIA GTX 1660 Ti (6 GB VRAM), 16 GB RAM, Ubuntu 26.04.
- **Ağ Kimliği:** LAN `192.168.0.15`, Tailscale `100.86.88.1` (`flugelserver.tail42f1f4.ts.net`), Alan adı: `gokalpgoksu.com`.
- **Üç Şifreli (LUKS) Disk:**
  1. `/` (Kingston A400 480 GB SSD): İşletim sistemi, Docker imajları, `/opt/stacks`, `/srv/appdata`, `/var/lib/libvirt/images`.
  2. `/mnt/side` (Seagate 500 GB): Torrent indirmeleri (`downloads/`), tüm yedeklerin ana kopyası (`backups/`), projeler (`projects/`), kişisel dosyalar (`files/`).
  3. `/mnt/sidemain` (Samsung M3 1 TB): Medya arşivi (`media/movies`, `media/series`, `media/books/ln`, `media/books/manga`), Immich fotoğrafları (`photos/immich`), Nextcloud bulutu (`cloud/nextcloud`).

## Sunucu Haritası (`01-HARITA.txt`)
```
SUNUCU HARİTASI — neyin nerede olduğu (20 Ekim 2026, dizin düzeni tamamlandı 06:45)
===================================================
Kural: klasör adları küçük harf ve tire (lower-kebab-case). Eski yolu bir servis/betik kullanıyorsa eski yerde
sembolik bağ (link) bırakıldı; yeni iş için her zaman YENİ yolu kullanın.

ÜÇ DİSK
  /              Kingston A400 480 GB SSD (sdb, LUKS + TPM ile açılır). Sistem, Docker, uygulama ayarları, VM diskleri.
  /mnt/side      Seagate 500 GB (sdc, LUKS). İndirmeler, TÜM yedeklerin ana kopyası, kişisel dosyalar, projeler.
  /mnt/sidemain  Samsung M3 1 TB USB (sda, LUKS). Film/dizi/kitap/manga, Immich fotoğrafları, Nextcloud verisi.

SİSTEM DİSKİ (/) — standart (FHS) yerler
  /opt/stacks/<uygulama>/compose.yaml   Docker yığınlarının tanımı (her uygulama bir klasör; jellyfin, ollama, plex dahil)
  /srv/appdata/<uygulama>/              Uygulama ayar/durum verisi — TÜM uygulamalar burada (25 klasör)
  /arrapps  -> srv/appdata              ESKİ yol, yalnız uyumluluk bağı (hiçbir container artık bunu bağlamıyor)
  /srv/backups/current/                 Yedeklerin bu diskteki GÜNCEL kopyası (uygulamalar)
  /srv/archive/                         Kullanılmayan ama saklanan şeyler:
      appdata/, stacks/, installers/   20.10 aksam kullanici onayiyla silindi (bos)
      backups/        eski elle yedekler (nextcloud-2026-05-14, immich-db-2026-10-07)
      pc-yedekleri/   PC'den alınmış eski yedekler (pc-ev, pc-projeler)
      security/       LUKS başlık yedeği (luks-sda3-header.img), WARP hesap dosyaları — root'a özel (700)
  /srv/dev/                             Geliştirme alanı: projects/, workspaces/, artifacts/, tools/, docs/, archive/
  /srv/project/                         Windows VM'deki Eclipse projelerinin yedeği (bkz. 05)
  /srv/operations/                      Operasyon kayıtları: changes/ (her değişikliğin geri dönüş kopyası), history/ (eski sürümler),
                                          inventory/, ai-context/ (yapay zeka ajanları için bağlam)
  /srv/rehber/                          BU REHBER
  /var/lib/libvirt/images/              VM diskleri: w11 (qcow2, 100 GB sanal; W11 ve W11-GPU ortak), mullvad-ts.qcow2, ISO'lar
  /var/lib/flugel/durum/                Panel/bot durum dosyaları (eski yolu: /home/flugel/sistem-bakim/durum -> link)
  /usr/local/sbin, /usr/local/bin       Bakım betikleri (vm, vm-yedek.sh, uygulama-yedek.py, kritik-yedek.sh, self-heal.sh ...)
  /etc/vm-yonetim.conf                  VM otomatik kapanma ve yedek ayarları

YAN DİSK (/mnt/side)
  downloads/          Transmission indirmeleri (complete/, incomplete/) — Sonarr/Radarr buradan alır
  watch/              Transmission izleme klasörü
  backups/            TÜM YEDEKLERİN ANA KOPYASI   (eski yol: yedek -> backups bağı)
      uygulamalar/<uygulama>/   gece uygulama arşivleri (3 sürüm)
      vm/<disk-seti>/           VM geri dönüş yedekleri (2 sürüm)
      kritik/                   fotoğraf + Nextcloud + önemli klasör + ayarların aynası (30 günlük silinenler)
  files/              Kişisel dosyalar (eskiden diskin kökü, ödev/ ve Downloads/)
      school/         ödev/ klasörünün tamamı (calisma/, var/ dahil) + kökteki ders PDF'leri
      images/         kökteki 6 farklı/tek JPG (ödev'dekilerden farklı olanlar) + webp
      installers/     FLUGEL.apk, NxtPanel-development.zip
      notes/          FLUGEL-*.md, Notlar.md, abim.txt, makefile.x86_64
  projects/           Projects/ + projects/ birleşik (flugel, flugel-island, home-server, NxtPanel-development, ...)
      workspaces/     eclipse-workspace, git-workspace, myworkspace, codex
  karantina/          virüs taramasında yakalanan dosyalar

ANA VERİ DİSKİ (/mnt/sidemain)
  media/movies, media/series     Film ve diziler (Sonarr/Radarr/Jellyfin/Plex/Bazarr/Lingarr/Subgen)
  media/books/ln, media/books/manga   Hafif roman ve manga (Komga/Kavita/Openbooks/Kamiyomu/Suwayomi, telefondan yükleme)
  media/tv-recordings            boş (eski medya/tv_kayitlari)
  photos/immich/                 Immich fotoğraf ve videoları
  cloud/nextcloud/               Nextcloud kullanıcı dosyaları (PC-Yedekleri/GOKALP dahil) ve veritabanı (owncloud.db)
  appdata/kamiyomu/              Kamiyomu veritabanı ve günlükleri
  personal/usa, personal/yedek-amk   kişisel evraklar ve önemli klasör (kritik yedekte)
  backups/current/               Yedeklerin bu diskteki GÜNCEL kopyası (uygulamalar)
  Uyumluluk bağları (eski yol -> yeni): movies, series, books, immich, nextcloud_data, kamiyomu, "yedek amk"

DIŞARIDAN ERİŞİM (Tailscale olmadan) — Cloudflare, "flugel" şifreli giriş (2FA yok), giris nginx üzerinden:
  sonarr, radarr, prowlarr, bazarr, jackett, torrent (Transmission), plex, panel (Homepage), lingarr, checkcle  .gokalpgoksu.com
  (indir, suwayomi, yukle de aynı girişte). Dockge, File Browser, Netdata, AdGuard bilerek AÇILMADI (sunucunun tamamını yönetir).
  Ana tünel (nextcloud, immich, video, portainer, admin ...) Cloudflare panelinden yönetilir.
YAPAY ZEKA: Ollama'da tek model qwen3.5:4b (GTX 1660 Ti 6 GB'a tam sığar). Telegram köprüsü, anime çevirisi, AI gözcü ve
  Open WebUI bunu kullanır. Eski 10 model silindi (40 GB → 3,1 GB).

```
