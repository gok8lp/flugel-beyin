---
remote_allowed: false
title: flugelserver Ağ, Cloudflare Tunnel, Tailscale Serve ve Güvenlik Denetimi
sources: raw/flugelserver/08-ERISIM-GUVENLIK.txt, raw/flugelserver/09-BILINEN-SORUNLAR.txt, raw/flugelserver/10-DEGISIKLIK-GECMISI.txt, raw/flugelserver/savunma-2026-11-08.txt, raw/yerel-ai/AG-VE-ERISIM.md, raw/yerel-ai/GUVENLIK.md
updated: 2026-11-11
---

# flugelserver Ağ, Cloudflare Tunnel, Tailscale Serve ve Güvenlik Denetimi

Bağlı Sayfalar: [[flugelserver-genel-mimari]] · [[flugelserver-uygulama-baglantilari]] · [[duduk-genel-bakis]]

> "ERİŞİM VE GÜVENLİK (20 Ekim 2026)" - raw/flugelserver/08-ERISIM-GUVENLIK.txt

> "BİLİNEN SORUNLAR VE ÖNERİLEN SONRAKİ ADIMLAR (20 Ekim 2026)" - raw/flugelserver/09-BILINEN-SORUNLAR.txt

> "[fd7a:115c:a1e0::8435:5801]%tailscale0:10000" - raw/flugelserver/savunma-2026-11-08.txt

## Erişim ve Güvenlik (`08-ERISIM-GUVENLIK.txt`)
```
ERİŞİM VE GÜVENLİK (20 Ekim 2026)
================================

Yollar
  Tailscale (özel ağ)   https://flugelserver.tail42f1f4.ts.net:<port>   — yalnız tailnet cihazları. Port listesi: Akış paneli / 02.
  Cloudflare (internet) *.gokalpgoksu.com — iki tünel:
     ana tünel "homeserver": rotalar Cloudflare PANELİNDEN yönetilir (Zero Trust > Tunnels). /etc/cloudflared/config.yml
        artık çalışan yapılandırmanın birebir kopyasıdır (belge). Yerel dosyayı değiştirmek rotaları DEĞİŞTİRMEZ.
     akış tüneli: /etc/cloudflared/akis.yml (yerel yönetilir) — akis, status, masaustu, gokalpgoksu.com, indir, suwayomi
  Tailscale Funnel (internet): 10000 → Immich, 443 → Jellyfin 8096 (önceden açılmış; Cloudflare Access korumaz)

20 Ekim sıkılaştırmaları
  File Browser   ÖNCE: root (0:0), tüm "/" yazılabilir, kimlik doğrulama YOK (noauth), 0.0.0.0:8085 → ağdaki herkes sunucunun
                       tamamına root olarak yazabiliyordu.
                 SONRA: flugel (1000) kullanıcısı; yalnız /mnt/side, /mnt/sidemain, /srv/dev; port yalnız 127.0.0.1 →
                       erişim yalnız Tailscale: https://flugelserver.tail42f1f4.ts.net:26443
                 Not: uygulamanın kendi girişi hâlâ kapalı (noauth); koruma Tailscale kimliğidir.
  Samba          ÖNCE: guest ok + 0777, herkes parolasız yazabiliyordu; bozuk satırlı yapılandırma.
                 SONRA: yalnız "flugel" (mevcut Samba parolası), misafir kapalı, 0664/0775, yalnız ev ağı + VM ağı + Tailscale,
                       SMB2.1+, şifreleme tercihli. Paylaşımlar: side, sidemain, project. Parola: sudo smbpasswd flugel
  Gluetun        Mullvad WireGuard özel anahtarı compose dosyasından /opt/stacks/gluetun/.env'e (600) taşındı.
  Suwayomi       Sabit Docker IP (172.17.0.2) bağımlılığı kaldırıldı: gluetun 127.0.0.1:4567 yayınlar;
                 Tailscale 45443 ve nginx (suwayomi.gokalpgoksu.com) buraya bakar.
  Webtop/Kasm    tamamen kaldırıldı (container, imaj, veri, servis, rota, Telegram komutu, ana sayfa).

Açık kalan riskler (bkz. 09): flugel için parolasız tam sudo, Docker soketi bağlı yönetim araçları, Cloudflare'de
portainer/admin(Cockpit)/office alt alan adları, Funnel yolları, self-heal.sh içinde düz metin API anahtarları.

```

## Bilinen Sorunlar (`09-BILINEN-SORUNLAR.txt`)
```
BİLİNEN SORUNLAR VE ÖNERİLEN SONRAKİ ADIMLAR (20 Ekim 2026)
==========================================================
Önem sırasıyla.

1) SİSTEM SSD'Sİ DARBOĞAZ — TRIM KAPALI  (en önemli performans bulgusu)
   Kingston A400 (DRAM'siz). LUKS katmanında discard yok → haftalık fstrim kök diski HİÇ kırpmıyor. 18.025 saat, 86 TB yazılmış,
   ömrün %22'si gitmiş. Ölçüm (20.10 00:20): saniyede 7–9 MB yazarken gecikme 4,7 sn, %100 doluluk, I/O baskısı %94, yük 84.
   Öneri (bakım penceresinde, konsol başında): /etc/crypttab'ta dm_crypt-0 satırına ",discard" ekle → sudo update-initramfs -u →
   yeniden başlat → sudo fstrim -v /. TPM ile açılan kök diskte yapıldığı için uzaktan/gözetimsiz YAPILMADI.
   Orta vade: VM diskini ve Docker'ı ayrı/iyi bir SSD'ye almak; swap'ı (4 GB, sık dolu) zram ile desteklemek.

2) ÇÖZÜLDÜ (20.10 06:07) — /arrapps → /srv/appdata taşıması tamamlandı. 19 uygulama klasörü taşındı (mv, aynı disk),
   compose'lar güncellendi, yalnız etkilenen container'lar tek tek yeniden oluşturuldu ve doğrulandı (Immich 14.866 öğe,
   Nextcloud kurulu, *arr/Jellyfin/Plex/Ollama yanıt veriyor). Kullanılmayan 23 klasör → /srv/archive/appdata; jellyfin/ollama/plex
   compose'ları → /opt/stacks/<uygulama>/compose.yaml. /arrapps artık /srv/appdata'ya bağ. Hiçbir container /arrapps bağlamıyor.
   Eski boş klasör karantinası hâlâ duruyor (incelenip silinebilir): /srv/operations/changes/2026-10-20-fhs/yanlis-olusan-bos-klasorler
   Kayıt ve betikler: /srv/operations/changes/2026-10-20-fhs-tamamla (islem.log, appdata-tasi.sh, grup-tasi.sh, onceki/).

3) ÇÖZÜLDÜ (20.10 06:37) — /mnt/side ve /mnt/sidemain lower-kebab düzenine alındı (bkz. 01-HARITA). Hiçbir dosya silinmedi
   (side dosya sayısı önce/sonra 307.913). Downloads → downloads/manual, Projects+projects+workspaces → projects/.
   Kökteki 11 dosya ödev/ ile bayt bayt aynıydı → /mnt/side/archive/duplicates-2026-10-20 (incelenip silinebilir);
   farklı/tek 6 JPG → files/images. Servislerin kullandığı eski yollarda bağ bırakıldı (side/yedek; sidemain/movies, series, books,
   immich, nextcloud_data, kamiyomu, "yedek amk"). Kökteki 15 dosya ile downloads/manual içindekiler hâlâ ikişer kopya (679 MB).
   Windows/SMB eşlemeleri eski alt klasörleri (Downloads, Projects, ödev, eclipse-workspace ...) gösteriyorsa yeni yola güncellenmeli.

4) SUNUCU DIŞINDA YEDEK YOK — tüm kopyalar aynı kasada. Harici disk veya bulut (ör. restic + B2/Hetzner) önerilir.
5) sidemain %88 dolu — VM yedeğinin güncel kopyası buraya sığmıyor. Medya temizliği veya yeni disk gerekli.
6) side %77 dolu — 2. W11 yedeği (+50 GB) eklendiğinde ~%88 olur. İndirmeler aynı diskte.
7) sidemain USB diski: 18 Ekim USB reset + I/O hatası; side: tarihsel CRC. Kablo/kutu/güç yolu kontrol edilmeli.
8) Windows C: BitLocker — kurtarma anahtarının sunucu dışında saklandığını doğrulayın; TPM durumu VM yedeklerinde var.
9) W11-GPU 18 Ekim'den beri donmuştu (VNC siyah) — kök neden bilinmiyor; QEMU konuk ajanı kurulması önerilir.
10) Güvenlik: flugel için parolasız tam sudo (/etc/sudoers.d/90-bakim-gecici), self-heal.sh içinde düz metin WhatsApp/Gotify
    anahtarları, Docker soketi bağlı Portainer/Dockge/Homepage/Kuma/Netdata, Cloudflare'de portainer/admin/office alt alan adları
    (Access kuralı panelden doğrulanmalı), File Browser'ın kendi girişi kapalı (yalnız Tailscale ile korunuyor).
11) Sunucudaki Eclipse (webtop) kaldırıldı; Oomph/Kate sorunu bu yüzden düzeltilmedi. Eclipse VM'de kullanılacak.
12) Yeniden başlatma testi (tam sunucu reboot) gözetimsiz yapılmadı; container'ların hepsinde restart politikası var.

13) Nextcloud SQLite + kritik-yedek çakışması: 20.10 06:38'deki elle kritik-yedek çalışmasında (DB dökümü + aynı USB diskte
    rsync) Nextcloud'un 5 php-fpm işçisinin hepsi owncloud.db'de bekledi ve status.php ~5 dk yanıt vermedi; yedek bitince de
    toparlamadı, container yeniden başlatılınca düzeldi. Gece 04:30'da da olabilir (günlükte 00:07'den beri "Slow session_start").
    Öneri: Nextcloud'u SQLite'tan MariaDB/PostgreSQL'e taşımak; kritik-yedek sonrası status.php kontrolü.
    20.10 18:35 hafifletme: /srv/appdata/nextcloud/php/www2.conf → pm.max_children=10, request_terminate_timeout=120s
    (takılan işçi 2 dk sonra öldürülür, site tamamen düşmez). Kök çözüm (veritabanı taşıma) hâlâ yapılmadı.

EK (20 Ekim sabah) — SİZİN ÇALIŞTIRMANIZ GEREKENLER (Claude'un izin denetimi bu işlemleri engelledi)
  A) YAPILDI (20.10 18:32) — LUKS başlığına kalıcı allow-discards eklendi (başlık yedeği: /srv/archive/security/luks/ ve
     /mnt/side/backups/guvenlik/). 18:38'de LVM tablosu yenilendi ve ilk fstrim 209,7 GiB kırptı;
     artık haftalık fstrim.timer otomatik çalışır.
  B) YAPILDI (20.10 18:34) — 9 betikteki WhatsApp/Gotify anahtarları /etc/sistem-bakim/bildirim.env (root, 600) dosyasına taşındı;
     betikler bu dosyayı yükler. Anahtar içeren .bak kopyaları /srv/operations/changes/2026-10-20-anahtarlar (700) altına alındı.
     YAPMANIZ GEREKEN: CallMeBot anahtarı ve telefon 20.10 akşamı bir Claude oturum kaydında göründü → CallMeBot'ta anahtarı yenileyin
     ve yalnız bildirim.env'i güncelleyin. /opt/scripts/gmail-notifier.py'de de eski CallMeBot anahtarı duruyor (kullanılmıyor).
  C) flugel parolasız sudo (/etc/sistem-bakim değil, /etc/sudoers.d/90-bakim-gecici): uzaktan kilitlenme riski nedeniyle
     dokunulmadı. flugel parolanızı bildiğinizden emin olduktan sonra NOPASSWD'yi yalnız gereken komutlarla sınırlayın.
  D) Sunucu dışı yedek: bir hedef seçilmeli (harici USB disk, Backblaze B2, Hetzner Storage Box vb.); hesap/anahtar sizden gelmeli.
  E) Windows VM içinde: \\192.168.122.1\project\windows\eclipse-esitle-kur.ps1 (bir kez) ve QEMU konuk ajanı (virtio-win ISO).
  F) BEKLİYOR — *arr çıkış trafiği Mullvad'dan (kullanıcı seçti): gluetun'da şifreli HTTP proxy açıp Sonarr/Radarr/Bazarr/Jackett/
     Lingarr'ı ona yönlendirmek. Hazır betik: /tmp/vpn-proxy.sh değil → /srv/operations/changes/2026-10-20-vpn-proxy (henüz çalışmadı).
     Claude'un otomatik modu gluetun'u yeniden oluşturmayı engelledi (Transmission/Prowlarr/Suwayomi kısa süre kesilir).
  G) BEKLİYOR — BT entegrasyonları (kullanıcı seçti): Authelia tek giriş (2FA yok), Vaultwarden şifre kasası, Prometheus+Grafana
     izleme ve Telegram uyarısı, Diun güncelleme bildirimi + otomatik güvenlik güncellemeleri.


```

## Değişiklik Geçmişi (`10-DEGISIKLIK-GECMISI.txt`)
```
DEĞİŞİKLİK GEÇMİŞİ — 19/20 Ekim 2026 gecesi (Claude)
===================================================
Her işlemin geri dönüş kopyası: /srv/operations/changes/2026-10-20-*/  (onceki/ = değiştirilmeden önceki dosyalar)

22:31  Webtop, Kasm, sunucudaki Eclipse tamamen kaldırıldı: container, imaj (8,5 GB), ağ, 3 systemd birimi, masaüstü anahtarı,
       nginx/Cloudflare/Tailscale rotaları, ana sayfa kartları, Akış/Homepage kayıtları, Telegram /webtop /kasm komutları, veriler
       (/opt/stacks/kasm 27 GB dahil) ve yedekteki kopyaları. Kazanç: / 35,7 GB, /mnt/side 26,6 GB.   → changes/2026-10-20-masaustu-kaldirma
22:58  VM yönetimi: 10 dk boşta kapatma, VM başına 2 yedek, autostart kapalı, vm komutu, libvirt kancası.   → changes/2026-10-20-vm-yonetim
23:00  Taşıma öncesi güvenlik yedeği (/mnt/side/yedek/tasima-oncesi-2026-10-20).
23:16  W11-GPU (donmuş) zorla kapatıldı; 23:27 ilk W11 yedeği (50 GB).
23:47  Kök dizin düzeni (kısmi): adguard, filebrowser, checkcle, guacamole, suwayomi, libreoffice verileri → /srv/appdata (eski yola link);
       durum klasörü → /var/lib/flugel/durum; kullanılmayan yığınlar/kurulum dosyaları/eski yedekler → /srv/archive;
       ev dizini ve sistem-bakim eski dosyaları → /srv/operations/history; /W11, /downloads ve libvirt "downloads" havuzu kaldırıldı;
       crontab "docker system prune" → image/builder prune.   → changes/2026-10-20-fhs (manifest.tsv = tüm taşımalar)
23:48–23:54 HATA ve GERİ ALMA: 16 container ~4 dk boş ayar klasörüyle açıldı; geri alındı, veri kaybı yok (bkz. 09 madde 2).
00:20  Güvenlik: File Browser, Samba, Cloudflare yerel dosyası, gluetun gizli anahtarı, Suwayomi proxy.   → changes/2026-10-20-guvenlik
00:30  Uygulama yedek sistemi + kritik-yedek'e DB dökümleri; ilk tam çalışma hatasız (34 uygulama).   → changes/2026-10-20-yedek-sistemi
00:42  /srv/project + Samba [project] + Windows eşitleme betiği + gece sürümleme.
00:50  Ana sayfa: "Sunucu düzeni" bölümü, File Browser açıklaması; Akış kataloğu Suwayomi hedefi.   → changes/2026-10-20-anasayfa
       Bu rehber (/srv/rehber), /srv/dev/docs/INFRASTRUCTURE.md.

20 Ekim sabah — dizin standardı tamamlandı (Claude)   → changes/2026-10-20-fhs-tamamla (islem.log + onceki/)
05:59  self-heal, docker-watcher, disk-koruyucu zamanlayıcıları durduruldu (06:39'da geri açıldı).
06:00–06:07  /arrapps → /srv/appdata: her yığın ayrı ayrı (durdur → mv → doğrula → compose → yalnız etkilenen servis yeniden oluştur
       → HTTP/uygulama kontrolü). convertx, bazarr, jackett, lingarr, kavita, komga, sonarr, radarr, prowlarr, transmission,
       uptime-kuma, stirling-pdf (başlatılmadı), nextcloud, immich (DB temiz kapatıldı; 14.866 öğe aynı), jellyfin, plex,
       ollama + open-webui (başlatılmadı). jellyfin/ollama/plex compose → /opt/stacks. gmail-notifier → /srv/appdata.
       23 kullanılmayan klasör → /srv/archive/appdata; /arrapps/compose kalanı → /srv/archive/stacks/arrapps-compose; /arrapps → bağ.
06:20–06:24  /mnt/side düzeni: ödev → files/school; kök dosyalar → files/{school,images,installers,notes}; Downloads → downloads/manual;
       Projects/projects/çalışma alanları → projects/; kaldirilanlar → archive/removed-2026-10-18; yedek → backups (+bağ).
06:27–06:36  /mnt/sidemain düzeni (grup grup, container'lar durdurulup yeniden oluşturuldu): movies/series → media/, books → media/books,
       kamiyomu → appdata/kamiyomu, immich → photos/immich, nextcloud_data → cloud/nextcloud, USA/yedek amk → personal/,
       tranga/downloads/sda_backup.img → archive/. Suwayomi bilerek "Created" bırakıldı; W11-GPU başlatılmadı.
06:37  Yollar güncellendi: kritik-yedek.sh, virus-tarama.sh, uygulama-yedek.py (kamiyomu önek kuralı dahil), /etc/vm-yonetim.conf,
       rehber-guncelle.py, vm-bosta-kapat.py, flugel-yukle.service, yukle.py, 19 compose dosyası.
06:38  kritik-yedek düzeltmesi: 04:30 çalışması "$H/srv/appdata" oluşturulamadığı için HATA vermişti → betiğe mkdir eklendi,
       eski ayna (kritik/arrapps) kritik/srv/appdata'ya taşındı; elle çalıştırma BAŞARILI (06:43).
06:45  Nextcloud yanıt vermiyordu (SQLite kilidi, bkz. 09 madde 13) → container yeniden başlatıldı, düzeldi.



20 Ekim gündüz/akşam (Claude, ana oturum)
  06:20  mullvad-ts (Ubuntu) için yeni yedek: /mnt/side/yedek/vm/mullvad-ts/2026-10-20_0620 (6,5 GB)
  06:28  Boşta kapatma: sunucudan VM'ye açık SSH/RDP/Guacamole bağlantıları da kullanım sayılıyor
  06:31  W11 otomatik VM yedekleri kapatıldı (/etc/vm-yonetim.conf: YEDEK_HARIC="w11"); elle yedek: sudo vm yedek W11-GPU
  06:33  Abinin eğitim planı yol haritası: /srv/project/docs/ABIMIN-PLANI-YOL-HARITASI.md
  06:35  Yer: hata karantinası silindi, journald 300 MB sınır, PCP arşivi 7 gün (~1,5 GB)
  06:51  Uygulama/kritik yedek: SQLite kopyası parça parça (Nextcloud kilitlenmesi düzeltildi)
  06:55  Suwayomi, Stirling-PDF, Open WebUI başlatıldı (bilerek-durdurulan listesinden çıkarıldı); CheckCle compose ile yeniden oluşturuldu
  07:00  Tailscale SSH açık: Tailscale hesabıyla şifresiz/anahtarsız giriş (check modu, tarayıcı onayı)
  07:05  Şifre sıfırlama betiği (kullanıcı çalıştırır): /srv/rehber/komutlar/sifre-sifirla.sh
  21:30  vm-bosta-kapat: ayar dosyasındaki satır sonu yorumları artık doğru okunuyor (MUAF önce bu yüzden yok sayılmıştı)
  21:40  Ana sayfa: Terminal kartı (Guacamole SSH), "Dosya paylaş", "Ubuntu geliştirme", "C/C++ projesi", "Yapay zekâ sohbeti" kartları;
         internete açık olmayan uygulamalarda pasif Cloudflare butonu yerine "yalnız Tailscale" etiketi
  Bekleyen: Ubuntu VM kurulumu (sunucunun VM'ye SSH anahtarıyla girebilmesi için kullanıcı ssh-copy-id çalıştırmalı), W11 yedeğinin silinmesi (kullanıcı onayı)

20 Ekim akşam — kalan işler (Claude)
18:32  TRIM: LUKS (sdb3) kalıcı allow-discards; başlık yedeği alındı. / için kırpma ilk yeniden başlatmadan sonra (09 EK-A).
       → changes/2026-10-20-trim
18:34  Bildirim anahtarları düz metinden /etc/sistem-bakim/bildirim.env'e (600) taşındı; 9 betik; self-heal, docker-watcher test edildi,
       ssh-login-watcher yeniden başlatıldı.   → changes/2026-10-20-anahtarlar
18:35  Nextcloud php-fpm: pm.max_children 5→10, request_terminate_timeout 120s; container yeniden başlatıldı, status.php OK.
       → changes/2026-10-20-nextcloud-php
       Yapılmayanlar: C (sudo sınırlama — uzaktan kilitlenme riski), D (sunucu dışı yedek — hesap gerekli), E (Windows VM içi adımlar).
18:38  TRIM tamamlandı: LVM tablosu yenilendi (kullanıcı onayı), fstrim / → 209,7 GiB kırpıldı.
18:41  Temizlik (kullanıcı 4 grubu onayladı, kalıcı silme): /srv/archive/{appdata,stacks,installers}, side/archive (yinelenenler,
       removed-2026-10-18), downloads/manual, chatgpt/chrome .deb, manga içindeki 1 GB .exe, sidemain/archive (tranga, openbooks,
       sda_backup.img), backups/flugelubuntu, backups/tasima-oncesi-2026-10-20. Kazanç ~37 GB.   → changes/2026-10-20-temizlik/silinenler.log
18:44  Cloudflare (akış tüneli) + giris nginx şifreli giriş: sonarr, radarr, prowlarr, bazarr, jackett, torrent, plex, panel, lingarr,
       checkcle .gokalpgoksu.com. sonarr'ın eski A kaydı (192.168.0.15, dışarıdan çalışmıyordu) tünel CNAME'iyle değiştirildi.
       Hepsi şifresiz 401 veriyor (doğrulandı). giris container'ı yeniden başlatıldı (tek dosya bağlama eski inode'u görüyordu).
       → changes/2026-10-20-cloudflare
18:55  Yapay zeka: qwen3.5:4b indirildi; telegram-kopru, anime_takip, ai-gozcu ona geçirildi (think kapalı); eski 10 Ollama modeli
       silindi (40 GB → 3,1 GB).   → changes/2026-10-20-ai-model
       Bekleyen: *arr trafiğinin Mullvad'a alınması ve BT entegrasyonları (09 EK F, G) — otomatik mod izin denetimi engelledi.


```
