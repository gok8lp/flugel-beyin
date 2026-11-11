---
title: flugelserver Yedekleme, Zamanlayıcılar ve Otomasyon Betikleri
sources: raw/flugelserver/04-YEDEKLER.txt, raw/flugelserver/06-YEDEK-DURUMU-CANLI.txt, raw/flugelserver/07-OTOMASYONLAR.txt, raw/flugelserver/11-KAYNAK-KORUMA-2026-10-21.txt, raw/yerel-ai/BAKIM.md, raw/yerel-ai/YEDEKLEME.md, raw/yerel-ai/IZLEME-VE-BILDIRIM.md, raw/yerel-ai/KORUMA-SISTEMI-PLANI.md
updated: 2026-11-11
---

# flugelserver Yedekleme, Zamanlayıcılar ve Otomasyon Betikleri

Bağlı Sayfalar: [[flugelserver-genel-mimari]] · [[flugelserver-dosya-agaci-ve-diskler]] · [[sunucu-ve-github-commit-gecmisi]]

> "YEDEKLER — nerede, ne zaman, nasıl geri yüklenir (20 Ekim 2026)" - raw/flugelserver/04-YEDEKLER.txt

> "OTOMASYONLAR — zamanlanmış görevler (20 Ekim 2026)" - raw/flugelserver/07-OTOMASYONLAR.txt

> "Kritik yedek (her gece 04:30)" - raw/yerel-ai/YEDEKLEME.md

## Yedekleme Sistemi (`04-YEDEKLER.txt`)
```
YEDEKLER — nerede, ne zaman, nasıl geri yüklenir (20 Ekim 2026)
==============================================================

1) UYGULAMA YEDEKLERİ  (her gece 03:30, uygulama-yedek.timer)
   Ana kopya .... /mnt/side/backups/uygulamalar/<uygulama>/<uygulama>_<tarih>.tar.zst
   Güncel kopya . /srv/backups/current/uygulamalar/<uygulama>.tar.zst          (sistem SSD'si)
                  /mnt/sidemain/backups/current/uygulamalar/<uygulama>.tar.zst  (ana veri diski)
   Sürüm ........ uygulama başına 3. Tüm arşivler 25 GiB'ı veya tek arşiv 3 GiB'ı aşarsa 2'ye düşer (otomatik).
                  İlk tam çalışma: 34 uygulama, toplam 1,94 GiB → 3 sürüm geçerli.
   İçerik ....... compose klasörü + ayar/durum klasörleri + Docker volume'ları.
                  PostgreSQL: pg_dumpall dökümü (_flugel/pg-<container>.sql). SQLite: tutarlı .backup kopyası (orijinal yolunda).
                  İçermez: film/dizi/kitap/fotoğraf/Nextcloud dosyaları (bkz. 3), model/önbellek/günlük klasörleri.
   Geri yükleme . 1. sudo docker compose -f /opt/stacks/<uygulama>/compose.yaml stop
                  2. sudo tar --zstd -xpf <arşiv> -C /
                  3. PostgreSQL varsa: tar --zstd -xOf <arşiv> _flugel/pg-<c>.sql | sudo docker exec -i <c> psql -U <kullanıcı> -d postgres
                  4. sudo docker compose -f ... up -d
   Arşivi incele  tar --zstd -tvf <arşiv> | less    |    tar --zstd -xOf <arşiv> _flugel/BILGI.json
   Elle çalıştır  sudo systemctl start uygulama-yedek.service   (günlük: /var/log/uygulama-yedek.log)

2) SANAL MAKİNE GERİ DÖNÜŞ YEDEKLERİ  (her VM kapanışında + her gün 05:15 kontrol)
   Yer .......... /mnt/side/backups/vm/w11/<tarih>/        (W11 ve W11-GPU ortak diski)
                  /mnt/side/backups/vm/mullvad-ts/<tarih>/
   Sürüm ........ disk seti başına en fazla 2. Yeni yedek: son yedek ≥ 3 günlük VE disk değişmişse.
   İçerik ....... disk.qcow2 (zstd sıkıştırılmış), VM XML'leri, UEFI NVRAM, TPM durumu (BitLocker anahtarı TPM'de!), BILGI.txt
   Mevcut ....... w11/2026-10-19_2316 (50 GB, VM kapalıyken alındı), mullvad-ts/2026-10-17_1123 (eski elle kopya)
   Geri dönüş ... sudo vm geri-yukle w11 <tarih> --evet     (VM kapalı olmalı; mevcut disk .geri-yukleme-oncesi-* adıyla saklanır)
   Güncel kopya . sidemain'e: disk %90 sınırını aşacağı için ŞU AN ATLANIYOR. SSD'ye: bilerek yazılmıyor (bkz. 09).

3) KRİTİK VERİ AYNASI  (her gece 04:30, kritik-yedek.timer)
   Yer .......... /mnt/side/backups/kritik/   (immich, nextcloud_data, "yedek amk", srv/appdata, stacks, etc, development)
   Silinen/değişen dosyalar 30 gün: /mnt/side/backups/kritik/.silinenler/<tarih>/
   YENİ: aynalamadan önce tutarlı veritabanı dökümleri alınır → /mnt/side/backups/kritik/veritabanlari/
         (pg-immich_postgres.sql, pg-guac-db.sql, nextcloud-owncloud.db)

4) WINDOWS VM ECLIPSE PROJELERİ  → /srv/project (bkz. 05-SANAL-MAKINELER.txt)

5) TAŞIMA ÖNCESİ GÜVENLİK YEDEĞİ (20 Ekim 2026)
   (20.10 akşam silindi) /mnt/side/backups/tasima-oncesi-2026-10-20/  ayarlar.tar.zst (6,5 GB), db/ (37 SQLite + Immich/Guacamole dökümü), inspect-*.json

ÖNEMLİ SINIR: Tüm yedekler aynı sunucunun içinde. Hırsızlık, yangın, elektrik hasarı veya sunucunun ele geçirilmesine karşı
sunucu DIŞINDA bir kopya yok (bkz. 09).

```

## Otomasyonlar (`07-OTOMASYONLAR.txt`)
```
OTOMASYONLAR — zamanlanmış görevler (20 Ekim 2026)
=================================================
Liste: systemctl list-timers --all      Günlük: journalctl -u <ad>.service

YENİ (20 Ekim)
  vm-bosta-kapat.timer      her dakika   kullanılmayan VM'yi 10 dk sonra temiz kapatır (05-SANAL-MAKINELER.txt)
  vm-yedek-gunluk.timer     05:15        kapalı VM'lerin yedek gerekip gerekmediğini kontrol eder
  vm-kapandi@<VM>.service   VM kapanınca yedek + Eclipse proje eşitleme (libvirt kancası başlatır)
  uygulama-yedek.timer      03:30        34 uygulamanın arşivi, 3/2 sürüm, her diske güncel kopya
  proje-surum.timer         02:30        /srv/project sürümleri
  rehber-guncelle.timer     06:00        bu rehberin CANLI dosyalarını yeniler

ÖNCEDEN VAR OLANLAR
  kritik-yedek.timer        04:30        fotoğraf/Nextcloud/ayar aynası (+ YENİ: önce tutarlı DB dökümleri)
  self-heal.timer           ~3 dk        çöken servis/container'ı yeniden başlatır (restart=no ve bilerek-durdurulanları atlar)
  docker-watcher.timer      ~5 dk        container hata/sağlık izleme ve bildirim
  disk-koruyucu.timer       ~10 dk       SMART/I/O hatası izler; ağır durumda container'ları durdurabilir
  swap-flush.timer          ~5 dk        eşik aşılırsa swap boşaltma
  ai-gozcu.timer            15 dk        sağlık kontrolü + (bellek/disk rahatsa) Ollama özeti
  island-veri / torrent-bekci  ~20 sn    panel durumu / torrent kontrolü
  vpn-ip-degistir.timer     saatlik      gluetun çıkış IP'sini yeniler
  basket-bot, anime-takip, imdb-puan, morning-report, weekly-maintenance, virus-tarama   botlar ve bakım
  root crontab              Pazar 03:00  docker image/builder temizliği
                            (20 Ekim: "docker system prune" kaldırıldı — bilerek durdurulan container'ları siliyordu)

Bilerek kapalı tutulanlar: /etc/sistem-bakim/bilerek-durdurulan (suwayomi, stirling-pdf, open-webui) — self-heal bunlara dokunmaz.
Bildirimler: /usr/local/bin/bildirim → Telegram + /var/lib/flugel/durum/bildirimler.log

```

## Canlı Yedek Durumu (`06-YEDEK-DURUMU-CANLI.txt`)
```
YEDEK DURUMU — canli, otomatik uretildi: 11.11.2026 06:00
==============================================================================
Son uygulama yedegi: 2026-11-04 03:41:00   toplam: 8.41 GiB   kural: 3 (toplam > 25 GiB veya arsiv > 3 GiB ise 2)
Hatalar: yok
Guncel kopya notlari: /srv/backups/current/uygulamalar/jackett.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/giris.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/ollama.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/nextcloud.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/convertx.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/sonarr.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/pairdrop.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/tsidp.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/adguard.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/flaresolverr.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/suwayomi.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/stirling-pdf.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/immich.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/prowlarr.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/subgen.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/portainer.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/openbooks.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/it-merkezi.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/jellyfin.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/gluetun.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/it-tools.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/transmission.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/plex.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/dockge.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/guacamole.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/kavita.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/panel.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/bazarr.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/dozzle.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/lingarr.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/beszel.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/komga.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/filebrowser.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/cup.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/uptime-kuma.tar.zst: ATLANDI (disk %90 sinirini asardi); /srv/backups/current/uygulamalar/radarr.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/jackett.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/giris.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/ollama.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/nextcloud.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/convertx.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/sonarr.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/pairdrop.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/tsidp.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/adguard.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/flaresolverr.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/suwayomi.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/stirling-pdf.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/immich.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/prowlarr.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/subgen.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/portainer.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/openbooks.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/it-merkezi.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/jellyfin.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/gluetun.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/it-tools.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/transmission.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/plex.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/dockge.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/guacamole.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/kavita.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/panel.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/bazarr.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/dozzle.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/lingarr.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/beszel.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/komga.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/filebrowser.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/cup.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/uptime-kuma.tar.zst: ATLANDI (disk %90 sinirini asardi); /mnt/sidemain/backups/current/uygulamalar/radarr.tar.zst: ATLANDI (disk %90 sinirini asardi)

Uygulama basina mevcut surumler (/mnt/side/backups/uygulamalar/<uygulama>/):
  adguard                2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  bazarr                 2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  beszel                 2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  convertx               2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  cup                    2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  dockge                 2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  dozzle                 2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  filebrowser            2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  flaresolverr           2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  giris                  2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  gluetun                2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  guacamole              2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  immich                 2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  it-merkezi             2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  it-tools               2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  jackett                2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  jellyfin               2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  kavita                 2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  komga                  2026-11-03_0335, 2026-11-04_0334
  lingarr                2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  nextcloud              2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  ollama                 2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  openbooks              2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  pairdrop               2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  panel                  2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  plex                   2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  portainer              2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  prowlarr               2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  radarr                 2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  sonarr                 2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  stirling-pdf           2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  subgen                 2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  suwayomi               2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  transmission           2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  tsidp                  2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334
  uptime-kuma            2026-11-02_0334, 2026-11-03_0335, 2026-11-04_0334

VM geri donus yedekleri (/mnt/side/backups/vm/<disk-seti>/):
[w11] (W11 W11-GPU)  -> /mnt/side/backups/vm/w11
[mullvad-ts] (mullvad-ts)  -> /mnt/side/backups/vm/mullvad-ts

Kritik veri aynasi (/mnt/side/backups/kritik): son calisma 2026-11-04 04:42:28

Zamanlayicilar:
NEXT                        LEFT LAST                              PASSED UNIT              ACTIVATES
Thu 2026-11-12 02:30:00 UTC  20h Wed 2026-11-11 02:30:00 UTC 3h 30min ago proje-surum.timer proje-surum.service

1 timers listed.


```
