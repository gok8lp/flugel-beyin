---
title: flugelserver Tüm Docker Uygulamaları ve Compose YAML Tanımları
sources: raw/flugelserver/02-UYGULAMALAR.txt, raw/flugelserver/docker-compose-yamllar.md, raw/flugelserver/durdurulan-konteynerler-20261104.txt
updated: 2026-11-11
---

# flugelserver Tüm Docker Uygulamaları ve Compose YAML Tanımları

Üst Mimari: [[flugelserver-genel-mimari]] · [[flugelserver-uygulama-baglantilari]] · [[flugelserver-dosya-agaci-ve-diskler]] · [[duduk-genel-bakis]]

> "UYGULAMALAR (Docker) — canli liste, otomatik uretildi: 11.11.2026 06:00" - raw/flugelserver/02-UYGULAMALAR.txt

> "flugelserver Tüm Docker Compose YAML Dosyaları (Gizli Bilgiler Maskelenmiş)" - raw/flugelserver/docker-compose-yamllar.md

## Canlı Uygulama Listesi (`02-UYGULAMALAR.txt`)
```
UYGULAMALAR (Docker) — canli liste, otomatik uretildi: 11.11.2026 06:00
==============================================================================
Her blok bir compose yigini. 'Ayar/veri' = container'in diske yazdigi yerler (bind mount).
Baslat/durdur:  cd <compose klasoru> && sudo docker compose up -d   |   sudo docker compose stop
Gunluk:         sudo docker logs --tail 100 <container>

### /opt/stacks/bazarr
  - bazarr   [running]   imaj: lscr.io/linuxserver/bazarr:latest
      portlar: 127.0.0.1:16767->6767/tcp
      yazilabilir: /mnt/sidemain/media/series  ->  /tv
      yazilabilir: /srv/appdata/bazarr  ->  /config
      yazilabilir: /mnt/sidemain/media/movies  ->  /movies

### /opt/stacks/flaresolverr
  - flaresolverr   [running]   imaj: ghcr.io/flaresolverr/flaresolverr:latest
      portlar: ag: container:be978ccf92e5f90389f9db86e2c6eac4da26e87d72e8211c0f8959b816d1da80 (VPN uzerinden)
      yazilabilir: /var/lib/docker/volumes/9b6ad27b640f1fe77194f920bf6591ef4684959948fd847536013b03ce9883c2/_data  ->  /config

### /opt/stacks/giris
  - giris   [running]   imaj: nginx:1.27-alpine
      portlar: ag: host
      salt-okunur: /opt/stacks/giris/nginx.conf  ->  /etc/nginx/conf.d/default.conf
      salt-okunur: /opt/stacks/giris/htpasswd  ->  /etc/nginx/htpasswd
      salt-okunur: /opt/stacks/giris/html  ->  /usr/share/nginx/html

### /opt/stacks/gluetun
  - gluetun   [running (unhealthy)]   imaj: qmcgaw/gluetun
      portlar: 127.0.0.1:14567->4567/tcp, 0.0.0.0:51413->51413/tcp, 0.0.0.0:51413->51413/udp, 127.0.0.1:18889->8888/tcp, 127.0.0.1:19091->9091/tcp, 127.0.0.1:19696->9696/tcp
      salt-okunur: /opt/stacks/gluetun/auth  ->  /gluetun/auth

### /opt/stacks/immich_server
  - immich_server   [running (healthy)]   imaj: ghcr.io/immich-app/immich-server:release
      portlar: 0.0.0.0:2283->2283/tcp
      yazilabilir: /var/lib/docker/volumes/107b85123b2a39cd1f70d790883c617300b312c3f0b51850aec2d79e170a4148/_data  ->  /data
      yazilabilir: /mnt/sidemain/photos/immich  ->  /usr/src/app/upload
  - immich_machine_learning   [running (healthy)]   imaj: ghcr.io/immich-app/immich-machine-learning:release-cuda
      yazilabilir: /srv/appdata/immich/model-cache  ->  /cache
  - immich_postgres   [running (healthy)]   imaj: ghcr.io/immich-app/postgres:14-vectorchord0.3.0-pgvectors0.2.0
      yazilabilir: /srv/appdata/immich/postgres  ->  /var/lib/postgresql/data
  - immich_redis   [running]   imaj: docker.io/redis:6.2-alpine
      yazilabilir: /var/lib/docker/volumes/67bb95db7f87251b34f14dc3fdeb7c18ef380dc95c14a048a9d221a9ea7d16a7/_data  ->  /data

### /opt/stacks/jackett
  - jackett   [running]   imaj: lscr.io/linuxserver/jackett:latest
      portlar: 127.0.0.1:19117->9117/tcp
      yazilabilir: /srv/appdata/jackett  ->  /config

### /opt/stacks/jellyfin
  - jellyfin   [running (healthy)]   imaj: lscr.io/linuxserver/jellyfin:latest
      portlar: 127.0.0.1:18096->8096/tcp
      yazilabilir: /mnt/sidemain/media/movies  ->  /movies
      yazilabilir: /dev/shm  ->  /transcode
      yazilabilir: /srv/appdata/jellyfin  ->  /config
      yazilabilir: /mnt/sidemain/media/series  ->  /tv

### /opt/stacks/kavita
  - kavita   [running]   imaj: lscr.io/linuxserver/kavita:latest
      portlar: 127.0.0.1:18295->5000/tcp
      yazilabilir: /srv/appdata/kavita  ->  /config
      yazilabilir: /mnt/sidemain/media/books  ->  /data/books

### /opt/stacks/komga
  - komga   [running]   imaj: gotson/komga:latest
      portlar: 127.0.0.1:18296->25600/tcp
      yazilabilir: /srv/appdata/komga  ->  /config
      yazilabilir: /mnt/sidemain/media/books  ->  /data

### /opt/stacks/nextcloud
  - nextcloud   [running (healthy)]   imaj: lscr.io/linuxserver/nextcloud:latest
      portlar: 127.0.0.1:8443->443/tcp, 192.168.0.15:8443->443/tcp
      yazilabilir: /srv/appdata/nextcloud  ->  /config
      yazilabilir: /mnt/sidemain/cloud/nextcloud  ->  /data
      salt-okunur: /mnt/sidemain/photos/immich/library/admin  ->  /immich-originals/Arsiv
      salt-okunur: /mnt/sidemain/photos/immich/upload/27085ce0-8895-482e-8d17-b9aa827997c5  ->  /immich-originals/Yeni Yuklenenler
  - nextcloud-db   [running (healthy)]   imaj: postgres:17-alpine
      yazilabilir: /srv/appdata/nextcloud-db  ->  /var/lib/postgresql/data

### /opt/stacks/panel
  - flugel-akis   [running (healthy)]   imaj: python:3.13-alpine
      portlar: ag: host
      salt-okunur: /opt/stacks/panel/akis/akis.py  ->  /app/akis.py
      salt-okunur: /opt/stacks/panel/akis/web  ->  /app/web
      yazilabilir: /opt/stacks/panel/akis/veri  ->  /veri
      salt-okunur: /var/lib/basket-bot  ->  /basket
      salt-okunur: /var/lib/flugel/durum  ->  /durum
      salt-okunur: /opt/stacks/panel/homepage/services.yaml  ->  /homepage/services.yaml

### /opt/stacks/plex
  - plex   [running (healthy)]   imaj: lscr.io/linuxserver/plex:latest
      portlar: ag: host
      yazilabilir: /srv/appdata/plex  ->  /config
      yazilabilir: /mnt/sidemain/media/movies  ->  /movies
      yazilabilir: /dev/shm  ->  /transcode
      yazilabilir: /mnt/sidemain/media/series  ->  /tv

### /opt/stacks/prowlarr
  - prowlarr   [running]   imaj: lscr.io/linuxserver/prowlarr:latest
      portlar: ag: container:be978ccf92e5f90389f9db86e2c6eac4da26e87d72e8211c0f8959b816d1da80 (VPN uzerinden)
      yazilabilir: /srv/appdata/prowlarr  ->  /config

### /opt/stacks/radarr
  - radarr   [running]   imaj: lscr.io/linuxserver/radarr:latest
      portlar: 127.0.0.1:17878->7878/tcp
      yazilabilir: /mnt/sidemain/media/movies  ->  /movies
      yazilabilir: /mnt/side/downloads  ->  /downloads
      yazilabilir: /srv/appdata/radarr  ->  /config

### /opt/stacks/sonarr
  - sonarr   [running]   imaj: lscr.io/linuxserver/sonarr:latest
      portlar: 127.0.0.1:18989->8989/tcp
      yazilabilir: /srv/appdata/sonarr  ->  /config
      yazilabilir: /mnt/sidemain/media/series  ->  /tv
      yazilabilir: /mnt/side/downloads  ->  /downloads

### /opt/stacks/suwayomi
  - suwayomi   [running]   imaj: ghcr.io/suwayomi/suwayomi-server:stable
      portlar: ag: container:be978ccf92e5f90389f9db86e2c6eac4da26e87d72e8211c0f8959b816d1da80 (VPN uzerinden)
      yazilabilir: /srv/appdata/suwayomi  ->  /home/suwayomi/.local/share/Tachidesk
      yazilabilir: /mnt/sidemain/media/books/manga/suwayomi  ->  /home/suwayomi/.local/share/Tachidesk/downloads

### /opt/stacks/transmission2
  - transmission   [running]   imaj: lscr.io/linuxserver/transmission:latest
      portlar: ag: container:be978ccf92e5f90389f9db86e2c6eac4da26e87d72e8211c0f8959b816d1da80 (VPN uzerinden)
      yazilabilir: /srv/appdata/transmission  ->  /config
      yazilabilir: /mnt/side/downloads  ->  /downloads
      yazilabilir: /mnt/side/watch  ->  /watch

### /opt/stacks/tsidp
  - tsidp   [running]   imaj: ghcr.io/tailscale/tsidp:latest
      yazilabilir: /opt/stacks/tsidp/data  ->  /data


```

## Tüm Docker Compose YAML Dosyaları (`/opt/stacks/*` ve `~/duduk-server`)
# flugelserver Tüm Docker Compose YAML Dosyaları (Gizli Bilgiler Maskelenmiş)

Bu dosya flugelserver üzerindeki tüm `/opt/stacks/*` ve `~/duduk-server` yığınlarının gerçek `compose.yaml` içeriklerini barındırır.

## /home/flugel/duduk-server/docker-compose.yml
```yaml
services:
  duduk-server:
    build: .
    container_name: duduk-server
    restart: unless-stopped
    ports:
      - "127.0.0.1:18420:18420"
    environment:
      - DUDUK_DATA_DIR=/data
      - DUDUK_PORT=18420
      - DUDUK_REFEREE=AHMET GÖKALP GÖKSU
      - DUDUK_POLL_SECONDS=10800
    volumes:
      - ./data:/data
```

## /opt/stacks/adguard/compose.yaml
```yaml
services:
  adguardhome:
    image: adguard/adguardhome
    container_name: adguardhome
    restart: unless-stopped
    mem_limit: 1536m
    ports:
      - 192.168.0.15:53:53/tcp
      - 192.168.0.15:53:53/udp
      - 100.86.88.1:53:53/tcp
      - 100.86.88.1:53:53/udp
      - 0.0.0.0:8888:80/tcp
      - 0.0.0.0:853:853/tcp
      - 0.0.0.0:853:853/udp
    volumes:
      - /srv/appdata/adguard/work:/opt/adguardhome/work
      - /srv/appdata/adguard/conf:/opt/adguardhome/conf
      - /etc/letsencrypt:/etc/letsencrypt:ro
```

## /opt/stacks/backrest/compose.yaml
```yaml
# FLUGEL: Backrest (restic web arayuzu) - Claude 2026-11-04. http://<sunucu>:9898
# Depolar: "yerel" = /mnt/side/restic/yerel (yedek diski), "drive" = Google Drive (rclone, sifreli restic).
# Depo parolalari: /etc/sistem-bakim/restic/*.pass (root 600) ve Backrest ayarinda. Parolayi sunucu disinda da sakla!
# Kaynaklar salt okunur /kaynak altina baglanir. Metrikler: /hooks/metrik.sh -> node_exporter textfile -> Grafana.
services:
  backrest:
    image: garethgeorge/backrest:v1.14.1
    container_name: backrest
    hostname: flugelserver
    restart: unless-stopped
    mem_limit: 1536m
    environment:
      - BACKREST_DATA=/data
      - BACKREST_CONFIG=/config/config.json
      - XDG_CACHE_HOME=/cache
      - TMPDIR=/tmp
      - TZ=Europe/Istanbul
    ports:
      - 9898:9898
    volumes:
      - /srv/appdata/backrest/data:/data
      - /srv/appdata/backrest/config:/config
      - /srv/appdata/backrest/cache:/cache
      - /srv/appdata/backrest/rclone:/root/.config/rclone
      - ./hooks:/hooks:ro
      - /var/lib/node_exporter/textfile:/textfile
      - /mnt/side/restic:/repos
      # yedeklenen kaynaklar (salt okunur)
      - /mnt/sidemain/photos:/kaynak/fotograflar:ro
      - /mnt/sidemain/cloud/nextcloud:/kaynak/nextcloud:ro
      - /mnt/sidemain/personal:/kaynak/kisisel:ro
      - /mnt/sidemain/media/books:/kaynak/kitaplar:ro
      - /srv/appdata:/kaynak/appdata:ro
      - /srv/yedek-dokum:/kaynak/dokum:ro
      - /srv/dev:/kaynak/dev:ro
      - /opt/stacks:/kaynak/stacks:ro
      - /etc:/kaynak/etc:ro
      - /usr/local:/kaynak/usr-local:ro
      # geri yukleme hedefi (yazilabilir)
      - /srv/geri-yukleme:/geri-yukleme
```

## /opt/stacks/bazarr/compose.yaml
```yaml
services:
  bazarr:
    image: lscr.io/linuxserver/bazarr:latest
    mem_limit: 1g   # sistem-bakim v2: makul bellek sınırı
    container_name: bazarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Istanbul
    volumes:
      - /srv/appdata/bazarr:/config:Z
      - /mnt/sidemain/media/movies:/movies:Z
      - /mnt/sidemain/media/series:/tv:Z
    ports:
      - 127.0.0.1:16767:6767   # uygulama-katman: dis port systemd soketinde
    restart: "no"   # uygulama-katman yonetir
```

## /opt/stacks/cup/compose.yaml
```yaml
# Cup: konteyner imajlari icin guncelleme denetimi (yalniz kontrol eder, guncelleme YAPMAZ).
# claude-reddit 2026-10-21. Erisim: Tailscale :50443 (yalniz tailnet). 6 saatte bir kontrol.
services:
  cup:
    image: ghcr.io/sergi0g/cup:v3.5.1
    container_name: cup
    restart: unless-stopped
    mem_limit: 128m
    command: serve
    environment:
      CUP_REFRESH_INTERVAL: "0 0 */6 * * *"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
    ports:
      - 127.0.0.1:9812:8000
```

## /opt/stacks/dozzle/compose.yaml
```yaml
# Dozzle: tarayicidan canli konteyner gunlukleri (salt-okunur, gunluk saklamaz).
# claude-reddit 2026-10-21. Erisim: Tailscale :49443 (yalniz tailnet). Eylem/kabuk ozellikleri kapali.
services:
  dozzle:
    image: amir20/dozzle:v11.3.4
    container_name: dozzle
    restart: unless-stopped
    mem_limit: 128m
    environment:
      DOZZLE_NO_ANALYTICS: "true"
      DOZZLE_HOSTNAME: "flugelserver"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - /srv/appdata/dozzle:/data
    ports:
      - 127.0.0.1:9811:8080
    healthcheck:
      test: ["CMD", "/dozzle", "healthcheck"]
      interval: 60s
      timeout: 10s
      retries: 3
```

## /opt/stacks/flaresolverr/compose.yaml
```yaml
services:
  flaresolverr:
    image: ghcr.io/flaresolverr/flaresolverr:latest
    mem_limit: 1536m   # sistem-bakim v2: makul bellek sınırı
    container_name: flaresolverr
    network_mode: container:gluetun
    user: root
    environment:
      - LOG_LEVEL=info
      - TZ=Europe/Istanbul
    restart: "no"   # uygulama-katman yonetir
```

## /opt/stacks/giris/compose.yaml
```yaml
# FLUGEL: gokalpgoksu.com baslangic sayfasi + sifreli yukleme ve manga yonlendirmeleri.
# Sunucu aginda calisir, yalniz 127.0.0.1:8098 dinler.
services:
  giris:
    image: nginx:1.27-alpine
    container_name: giris
    network_mode: host
    volumes:
      - ./html:/usr/share/nginx/html:ro
      - ./nginx.conf:/etc/nginx/conf.d/default.conf:ro
      - ./htpasswd:<REDACTED>
    restart: unless-stopped
    mem_limit: 32m
```

## /opt/stacks/gluetun/compose.yaml
```yaml
services:
  gluetun:
    image: qmcgaw/gluetun
    mem_limit: 256m   # sistem-bakim v2: makul bellek sınırı
    container_name: gluetun
    cap_add:
      - NET_ADMIN
    network_mode: bridge
    devices:
      - /dev/net/tun:/dev/net/tun
    ports:
      - 127.0.0.1:18889:8888/tcp   # uygulama-katman: dis port systemd soketinde
      - 127.0.0.1:19091:9091/tcp   # uygulama-katman: dis port systemd soketinde
      - 51413:51413/tcp
      - 51413:51413/udp
      - 127.0.0.1:19696:9696/tcp   # uygulama-katman: dis port systemd soketinde
      - 127.0.0.1:14567:4567/tcp   # uygulama-katman: dis port systemd soketinde   # Suwayomi (gluetun ag alaninda); sabit container IP bagimliligi yerine
    volumes:
      - ./auth:<REDACTED>   # Flugel: IP degistirme API anahtari (yalniz vpn/status)
    environment:
      - VPN_SERVICE_PROVIDER=mullvad
      - VPN_TYPE=wireguard
      - WIREGUARD_PRIVATE_KEY=<REDACTED>   # gizli: .env (chmod 600)
      - WIREGUARD_ADDRESSES=${WIREGUARD_ADDRESSES}
      - SERVER_COUNTRIES=Sweden
      - BLOCK_IPV6=on
      - FIREWALL_OUTBOUND_SUBNETS=192.168.0.0/24,172.16.0.0/12   # Claude 2026-10-21: Prowlarr -> Sonarr/Radarr (LAN) erisimi
    restart: "no"   # uygulama-katman yonetir
```

## /opt/stacks/guacamole/compose.yaml
```yaml
# FLUGEL: tarayıcıdan sanal makine masaüstü (Apache Guacamole). Web: 127.0.0.1:8097 (dışarıya Cloudflare tüneliyle).
# guacd sunucu ağında (sanal makine ağına 192.168.122.0/24 erişmek için), sadece docker0 adresinde dinler.
services:
  guacd:
    image: guacamole/guacd:1.6.0
    container_name: guacd
    network_mode: host
    command: ["/opt/guacamole/sbin/guacd", "-b", "172.17.0.1", "-l", "4822", "-L", "info", "-f"]
    restart: "no"   # uygulama-katman yonetir
    mem_limit: 512m
  guac-db:
    image: postgres:16-alpine
    container_name: guac-db
    environment:
      POSTGRES_DB: guacamole
      POSTGRES_USER: guacamole
      POSTGRES_PASSWORD: <REDACTED>
    volumes:
      - /srv/appdata/guacamole/db:/var/lib/postgresql/data
      - ./initdb:/docker-entrypoint-initdb.d:ro
    restart: "no"   # uygulama-katman yonetir
    mem_limit: 256m
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U guacamole -d guacamole"]
      interval: 10s
      retries: 10
  guacamole:
    image: guacamole/guacamole:1.6.0
    container_name: guacamole
    depends_on:
      guac-db:
        condition: service_healthy
    environment:
      GUACD_HOSTNAME: host.docker.internal
      GUACD_PORT: "4822"
      POSTGRESQL_HOSTNAME: guac-db
      POSTGRESQL_DATABASE: guacamole
      POSTGRESQL_USERNAME: guacamole
      POSTGRESQL_PASSWORD: <REDACTED>
      # Cloudflare tuneli docker ag gecidinden gelir: gercek istemci adresi X-Forwarded-For basligindan okunur
      REMOTE_IP_VALVE_ENABLED: "true"
      REMOTE_IP_VALVE_INTERNAL_PROXIES: "192\\.168\\.208\\.1|127\\.0\\.0\\.1"
      REMOTE_IP_VALVE_REMOTE_IP_HEADER: "X-Forwarded-For"
      # giris 1 gun gecerli (dakika)
      API_SESSION_TIMEOUT: "1440"
      # Claude 2026-10-21: TOTP kullanici istegiyle kaldirildi; parola denemesi kilidi sikilastirildi
      BAN_ENABLED: "true"
      BAN_MAX_INVALID_ATTEMPTS: "5"
      BAN_ADDRESS_DURATION: "1800"
      WEBAPP_CONTEXT: ROOT
    extra_hosts:
      - "host.docker.internal:host-gateway"
    ports:
      - "127.0.0.1:18097:8080"   # uygulama-katman: dis port systemd soketinde
    restart: "no"   # uygulama-katman yonetir
    mem_limit: 768m
```

## /opt/stacks/immich_server/compose.yaml
```yaml
services:
  immich-server:
    container_name: immich_server
    extra_hosts:
      - "idp.tail42f1f4.ts.net:100.119.135.23"   # tsidp (tek giriş); kapsayıcı DNS ts.net adını çözemiyor
    image: ghcr.io/immich-app/immich-server:release
    mem_limit: 3g   # sistem-bakim v2: makul bellek sınırı
    runtime: nvidia # Docker'a bu konteynerın NVIDIA kullanacağını doğrudan söyler 🚀
    ports:
      - 2283:2283
    volumes:
      - /mnt/sidemain/photos/immich:/usr/src/app/upload
      - /etc/localtime:/etc/localtime:ro
    environment:
      - DB_HOSTNAME=database
      - DB_USERNAME=postgres
      - DB_PASSWORD=<REDACTED>
      - DB_DATABASE_NAME=immich
      - REDIS_HOSTNAME=redis
    depends_on:
      - redis
      - database
    restart: unless-stopped
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities:
                - gpu
                - video
                - compute
                - utility

  immich-machine-learning:
    container_name: immich_machine_learning
    # CUDA destekli özel imajı kullanıyoruz ✨
    image: ghcr.io/immich-app/immich-machine-learning:release-cuda
    runtime: nvidia
    mem_limit: 2g
    volumes:
      - /srv/appdata/immich/model-cache:/cache
    environment:
      - DB_HOSTNAME=database
      - DB_USERNAME=postgres
      - DB_PASSWORD=<REDACTED>
      - DB_DATABASE_NAME=immich
      - REDIS_HOSTNAME=redis
      # CUDA'yı zorlamak için (opsiyonel):
      - IMMICH_TRITON_ENABLED=false
    restart: unless-stopped
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities:
                - gpu

  redis:
    container_name: immich_redis
    image: docker.io/redis:6.2-alpine
    mem_limit: 256m   # sistem-bakim v2: makul bellek sınırı
    restart: unless-stopped

  database:
    container_name: immich_postgres
    image: ghcr.io/immich-app/postgres:14-vectorchord0.3.0-pgvectors0.2.0
    mem_limit: 1536m   # sistem-bakim v2: makul bellek sınırı
    environment:
      - POSTGRES_PASSWORD=<REDACTED>
      - POSTGRES_USER=postgres
      - POSTGRES_DB=immich
    volumes:
      - /srv/appdata/immich/postgres:/var/lib/postgresql/data
    restart: unless-stopped

networks: {}
```

## /opt/stacks/izleme/compose.yaml
```yaml
# FLUGEL: izleme yigini (Claude 2026-11-04). Prometheus + Alertmanager + node-exporter + Grafana.
# Hepsi host aginda; Grafana disinda her sey yalniz 127.0.0.1'i dinler.
#   Grafana      http://<sunucu>:3020   (kullanici admin, parola: /opt/stacks/izleme/.env)
#   Prometheus   127.0.0.1:9190   Alertmanager 127.0.0.1:9193   node-exporter 127.0.0.1:9100
# Alarmlar -> alarm-koprusu (127.0.0.1:9194, systemd) -> /usr/local/bin/bildirim (Telegram + PC bildirimi).
# Ozel metrikler (yedekler, klasor boyutlari, Suwayomi) /var/lib/node_exporter/textfile altindaki .prom dosyalarindan gelir.
services:
  prometheus:
    image: prom/prometheus:v3.5.0
    container_name: prometheus
    network_mode: host
    restart: unless-stopped
    mem_limit: 768m
    user: "65534:65534"
    command:
      - --config.file=/etc/prometheus/prometheus.yml
      - --storage.tsdb.path=/prometheus
      - --storage.tsdb.retention.time=180d
      - --storage.tsdb.retention.size=8GB
      - --web.listen-address=127.0.0.1:9190
      - --web.enable-lifecycle
    volumes:
      - ./prometheus:/etc/prometheus:ro
      - /srv/appdata/prometheus:/prometheus

  alertmanager:
    image: prom/alertmanager:v0.28.1
    container_name: alertmanager
    network_mode: host
    restart: unless-stopped
    mem_limit: 128m
    command:
      - --config.file=/etc/alertmanager/alertmanager.yml
      - --storage.path=/alertmanager
      - --web.listen-address=127.0.0.1:9193
      - --cluster.listen-address=
    volumes:
      - ./alertmanager:/etc/alertmanager:ro
      - /srv/appdata/alertmanager:/alertmanager

  node-exporter:
    image: prom/node-exporter:v1.9.1
    container_name: node-exporter
    network_mode: host
    pid: host
    restart: unless-stopped
    mem_limit: 128m
    command:
      - --path.rootfs=/host
      - --web.listen-address=127.0.0.1:9100
      - --collector.textfile.directory=/textfile
      - --collector.systemd
      - --collector.systemd.unit-include=(kritik-yedek|kritik-yedek-ssd|uygulama-yedek|docker|nextcloud.*|suwayomi.*|alarm-koprusu|klasor-boyut|aylik-rapor|smartd|tailscaled)\.(service|timer)
      - --collector.filesystem.mount-points-exclude=^/(dev|proc|run|sys|var/lib/docker/.+|var/snap/.+|snap/.+|host/var/lib/docker/.+)($|/)
    volumes:
      - /:/host:ro,rslave
      - /var/lib/node_exporter/textfile:/textfile:ro
      - /run/dbus/system_bus_socket:/var/run/dbus/system_bus_socket:ro

  grafana:
    image: grafana/grafana-oss:12.0.2
    container_name: grafana
    network_mode: host
    restart: unless-stopped
    mem_limit: 384m
    user: "472:0"
    env_file: .env
    environment:
      - GF_SERVER_HTTP_PORT=3020
      - GF_DEFAULT_LOCALE=tr-TR
      - GF_USERS_DEFAULT_LANGUAGE=tr-TR
      - GF_ANALYTICS_REPORTING_ENABLED=false
      - GF_ANALYTICS_CHECK_FOR_UPDATES=false
      - GF_NEWS_NEWS_FEED_ENABLED=false
      - GF_DASHBOARDS_DEFAULT_HOME_DASHBOARD_PATH=/var/lib/grafana/panolar/genel-bakis.json
      - TZ=Europe/Istanbul
    volumes:
      - ./grafana/provisioning:/etc/grafana/provisioning:ro
      - ./grafana/panolar:/var/lib/grafana/panolar:ro
      - /srv/appdata/grafana:/var/lib/grafana
```

## /opt/stacks/jackett/compose.yaml
```yaml
services:
  jackett:
    image: lscr.io/linuxserver/jackett:latest
    mem_limit: 512m   # sistem-bakim v2: makul bellek sınırı
    container_name: jackett
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Istanbul
      - AUTO_UPDATE=true
    volumes:
      - /srv/appdata/jackett:/config:Z
    ports:
      - 127.0.0.1:19117:9117   # uygulama-katman: dis port systemd soketinde
    restart: "no"   # uygulama-katman yonetir
```

## /opt/stacks/jellyfin/compose.yaml
```yaml
services:
  jellyfin:
    container_name: jellyfin
    image: lscr.io/linuxserver/jellyfin:latest
    healthcheck:   # sistem-bakim v2
      test: ["CMD", "curl", "-fsS", "-m", "8", "http://localhost:8096/health"]
      interval: 60s
      timeout: 10s
      retries: 3
      start_period: 120s
    restart: "no"   # uygulama-katman yonetir
    ports:
      - 127.0.0.1:18096:8096   # uygulama-katman: dis port systemd soketinde
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Istanbul
      - VERSION=docker
    volumes:
      - /srv/appdata/jellyfin:/config
      - /mnt/sidemain/media/series:/tv
      - /mnt/sidemain/media/movies:/movies
      - /dev/shm:/transcode
    mem_limit: 2g
    cpus: 2.0
```

## /opt/stacks/kavita/compose.yaml
```yaml
services:
  kavita:
    image: lscr.io/linuxserver/kavita:latest # Resmi ve stabil LinuxServer imajı
    mem_limit: 768m   # sistem-bakim v2: makul bellek sınırı
    container_name: kavita
    extra_hosts:
      - "idp.tail42f1f4.ts.net:100.119.135.23"   # tsidp (tek giriş)
    restart: "no"   # uygulama-katman yonetir
    ports:
      - 127.0.0.1:18295:5000   # uygulama-katman: dis port systemd soketinde
    volumes:
      - /srv/appdata/kavita:/config # Mevcut ayar klasörün aynen kalıyor
      - /mnt/sidemain/media/books:/data/books # Kitap klasörün ve uzantıların güvende
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Istanbul
networks: {}
```

## /opt/stacks/komga/compose.yaml
```yaml
version: "3.8"
services:
  komga:
    image: gotson/komga:latest
    mem_limit: 1536m   # sistem-bakim v2: makul bellek sınırı
    container_name: komga
    extra_hosts:
      - "idp.tail42f1f4.ts.net:100.119.135.23"   # tsidp (tek giriş)
    restart: "no"   # uygulama-katman yonetir
    ports:
      - 127.0.0.1:18296:25600   # uygulama-katman: dis port systemd soketinde # Tarayıcıdan erişim için: http://IP-ADRESINIZ:8296
    volumes:
      # Kitaplarınızın bulunduğu gerçek klasörü buraya bağlayın
      - /mnt/sidemain/media/books:/data
      # Komga ayarlarının (veritabanı vb.) saklanacağı klasör
      - /srv/appdata/komga:/config
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Istanbul
      # Java bellek kullanımı (Sunucunuzun RAM'ine göre artırabilirsiniz)
      - JAVA_OPTS=-Xmx512m
networks: {}
```

## /opt/stacks/nextcloud/compose.yaml
```yaml
services:
  nextcloud:
    image: lscr.io/linuxserver/nextcloud:latest
    mem_limit: 1536m
    healthcheck:
      test:
      - CMD
      - curl
      - -fsSk
      - -m
      - '8'
      - https://localhost/status.php
      interval: 60s
      timeout: 10s
      retries: 3
      start_period: 120s
    container_name: nextcloud
    extra_hosts:
    - idp.tail42f1f4.ts.net:100.119.135.23
    environment:
    - PUID=1000
    - PGID=1000
    - TZ=Europe/Istanbul
    volumes:
    - /srv/appdata/nextcloud:/config
    - /mnt/sidemain/cloud/nextcloud:/data
    - /mnt/sidemain/photos/immich/library/admin:/immich-originals/Arsiv:ro
    - /mnt/sidemain/photos/immich/upload/27085ce0-8895-482e-8d17-b9aa827997c5:/immich-originals/Yeni
      Yuklenenler:ro
    ports:
    - 127.0.0.1:8443:443
    - 192.168.0.15:8443:443
    restart: unless-stopped
    depends_on:
      nextcloud-db:
        condition: service_healthy
  nextcloud-db:
    image: postgres:17-alpine
    container_name: nextcloud-db
    restart: unless-stopped
    mem_limit: 512m
    environment:
    - POSTGRES_DB=nextcloud
    - POSTGRES_USER=nextcloud
    - POSTGRES_PASSWORD=<REDACTED>
    volumes:
    - /srv/appdata/nextcloud-db:/var/lib/postgresql/data
    healthcheck:
      test:
      - CMD-SHELL
      - pg_isready -U nextcloud -d nextcloud
      interval: 10s
      retries: 10
```

## /opt/stacks/ollama/compose.yaml
```yaml
services:
  ollama:
    image: ollama/ollama:latest
    healthcheck:   # sistem-bakim v2
      test: ["CMD", "ollama", "list"]
      interval: 60s
      timeout: 10s
      retries: 3
      start_period: 120s
    container_name: ollama
    restart: "no"   # uygulama-katman yonetir
    runtime: nvidia
    environment:
      - NVIDIA_VISIBLE_DEVICES=all
      - NVIDIA_DRIVER_CAPABILITIES=compute,utility
      - OLLAMA_NUM_PARALLEL=1
      - OLLAMA_KEEP_ALIVE=0
      - OLLAMA_CONTEXT_LENGTH=8192
      - OLLAMA_MAX_LOADED_MODELS=1
      - OLLAMA_FLASH_ATTENTION=1
      - LLAMA_ARG_CACHE_RAM=0          # claude-son 2026-10-21: llama-server istem onbellegi host RAM yemesin (vars. 8 GB)
      - LLAMA_ARG_CTX_CHECKPOINTS=2    # claude-son: qwen3.5 baglam checkpointleri ~110 MB/adet, vars. 32
    volumes:
      - /srv/appdata/ollama:/root/.ollama
    ports:
      - 127.0.0.1:21434:11434   # uygulama-katman: dis port systemd soketinde
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
    mem_limit: 6g
    networks: [default, ai-kumhavuzu]
    memswap_limit: 6g

networks:
  ai-kumhavuzu:
    external: true
```

## /opt/stacks/panel/compose.yaml
```yaml
services:
  homepage:
    image: ghcr.io/gethomepage/homepage:latest
    container_name: homepage
    restart: unless-stopped
    environment:
      HOMEPAGE_ALLOWED_HOSTS: "192.168.0.15:3010,100.86.88.1:3010,flugelserver.tail42f1f4.ts.net:3010,flugelserver.tail42f1f4.ts.net:37443,localhost:3010,127.0.0.1:3010,panel.gokalpgoksu.com"
    volumes:
      - ./homepage:/app/config
      - ./homepage/fontlar:/app/public/fontlar:ro
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - /mnt/side:/mnt/side:ro
      - /mnt/sidemain:/mnt/sidemain:ro
    ports: ["3010:3000"]
    mem_limit: 384m

  # Gundem botu (sistem-bakim): haber/mac/anime/sunucu sorunlari -> JSON + iCal, sadece ic agda (:8090)
  gundem-botu:
    image: python:3.13-alpine
    container_name: gundem-botu
    ports: ["3011:8090"]   # /durum sayfasi + takvim.ics (ic ag / Tailscale)
    restart: unless-stopped
    user: "1000:1000"
    working_dir: /app
    command: ["python", "-u", "/app/gundem_botu.py"]
    environment:
      TZ: Europe/Istanbul
      PYTHONDONTWRITEBYTECODE: "1"
    volumes:
      - ./gundem/gundem_botu.py:/app/gundem_botu.py:ro
      - ./gundem/veri:/veri
      - /var/lib/flugel/durum:/durum:ro
      - /var/lib/basket-bot:/basket:ro
    mem_limit: 128m
    healthcheck:
      test: ["CMD", "python", "-c", "import urllib.request;urllib.request.urlopen(\"http://127.0.0.1:8090/ozet.json\",timeout=5)"]
      interval: 60s
      start_period: 120s

  # FLUGEL Akis (sistem-bakim): kisisel sosyal akis uygulamasi -> http://192.168.0.15:3012
  flugel-akis:
    image: python:3.13-alpine
    healthcheck:   # sistem-bakim v2
      test: ["CMD", "wget", "-qO-", "-T", "8", "http://127.0.0.1:3012/api/istatistik"]
      interval: 60s
      timeout: 10s
      retries: 3
      start_period: 120s
    container_name: flugel-akis
    restart: unless-stopped
    user: "1000:1000"
    working_dir: /app
    command: ["python", "-u", "/app/akis.py"]
    environment:
      TZ: Europe/Istanbul
      PYTHONDONTWRITEBYTECODE: "1"
      PORT: "3012"
      CEVIRI_MODEL: "qwen3.5:4b"   # 2026-10-21 claude-akis: gemma3 kurulu degildi
      SOHBET_MODEL: "qwen3.5:4b"
      AI_KEEP_ALIVE: "2m"
      AI_SESSIZ: "03:30-06:30"     # Lingarr 04:00 gece cevirisi icin arka plan AI durur
      AI_TOPLU_ARALIK: "1800"      # 2026-10-21 claude-ram: arka plan AI 30 dk da bir toplu calisir
      AI_TOPLU_SURE: "900"         # pencere en fazla 15 dk; bitince model bosaltilir
    network_mode: host
    extra_hosts: ["host.docker.internal:127.0.0.1"]
    volumes:
      - ./akis/akis.py:/app/akis.py:ro
      - ./akis/web:/app/web:ro
      - ./akis/veri:/veri
      - /var/lib/basket-bot:/basket:ro
      - /var/lib/flugel/durum:/durum:ro
      - ./homepage/services.yaml:/homepage/services.yaml:ro
    mem_limit: 512m
```

## /opt/stacks/plex/compose.yaml
```yaml
services:
  plex:
    container_name: plex
    image: lscr.io/linuxserver/plex:latest
    healthcheck:   # sistem-bakim v2
      test: ["CMD", "curl", "-fsS", "-m", "8", "http://localhost:32400/identity"]
      interval: 60s
      timeout: 10s
      retries: 3
      start_period: 120s
    network_mode: host
    restart: unless-stopped
    runtime: nvidia
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Istanbul
      - VERSION=docker
      - NVIDIA_VISIBLE_DEVICES=all
      - NVIDIA_DRIVER_CAPABILITIES=compute,video,utility
      - PLEX_CLAIM=claim-Ru6Mrdui-gU-EGHme7vi
    volumes:
      - /srv/appdata/plex:/config
      - /mnt/sidemain/media/series:/tv
      - /mnt/sidemain/media/movies:/movies
      - /dev/shm:/transcode
    devices:
      - /dev/dri:/dev/dri
    group_add:
      - video
    mem_limit: 2g
    memswap_limit: 2g
```

## /opt/stacks/prowlarr/compose.yaml
```yaml
services:
  prowlarr:
    image: lscr.io/linuxserver/prowlarr:latest
    mem_limit: 512m   # sistem-bakim v2: makul bellek sınırı
    container_name: prowlarr
    network_mode: "container:gluetun"
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Istanbul
      - FLARESOLVERR_URL=http://flaresolverr:8191
    volumes:
      - /srv/appdata/prowlarr:/config:Z
    restart: "no"   # uygulama-katman yonetir
    # Arayüz: http://sunucuip:9696
    # FlareSolverr: http://flaresolverr:8191
```

## /opt/stacks/radarr/compose.yaml
```yaml
services:
  radarr:
    image: lscr.io/linuxserver/radarr:latest
    mem_limit: 768m   # sistem-bakim v2: makul bellek sınırı
    container_name: radarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Istanbul
    volumes:
      - /srv/appdata/radarr:/config:Z
      - /mnt/sidemain/media/movies:/movies:Z
      - /mnt/side/downloads:/downloads:Z
    ports:
      - 127.0.0.1:17878:7878   # uygulama-katman: dis port systemd soketinde
    restart: "no"   # uygulama-katman yonetir
```

## /opt/stacks/sonarr/compose.yaml
```yaml
services:
  sonarr:
    image: lscr.io/linuxserver/sonarr:latest
    mem_limit: 768m   # sistem-bakim v2: makul bellek sınırı
    container_name: sonarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Istanbul
    volumes:
      - /srv/appdata/sonarr:/config:Z
      - /mnt/sidemain/media/series:/tv:Z
      - /mnt/side/downloads:/downloads:Z
    ports:
      - 127.0.0.1:18989:8989   # uygulama-katman: dis port systemd soketinde
    restart: "no"   # uygulama-katman yonetir
```

## /opt/stacks/subgen/compose.yaml
```yaml
services:
  subgen:
    image: mccloud/subgen:latest
    container_name: subgen
    restart: "no"   # uygulama-katman yonetir
    runtime: nvidia
    mem_limit: 4g
    environment:
      - WHISPER_MODEL=large-v3-turbo   # Claude 2026-10-21: medium yerine daha dogru ve hizli
      - PREFERRED_AUDIO_LANGUAGES=eng   # MULTi dosyalarda dublaj yerine orijinal ses
      - WHISPER_THREADS=4
      - CONCURRENT_TRANSCRIPTIONS=1   # 2 iken 4 GB sinirini asip OOM oluyordu (sistem-bakim)
      - TRANSCRIBE_OR_TRANSLATE=translate
      - NAMESUBLANG=en
      - OVERWRITE_EXISTINGSUBS=true
      - USE_GPU=true
      - TRANSCRIBE_DEVICE=cuda
      - PLEX_TOKEN=<REDACTED>
      - PLEX_SERVER=http://192.168.0.15:32400
    ports:
      - 127.0.0.1:18091:9000   # uygulama-katman: dis port systemd soketinde
    volumes:
      - /mnt/sidemain/media/series:/tv:Z
      - /mnt/sidemain/media/movies:/movies:Z
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities:
                - gpu
                - compute
                - utility
```

## /opt/stacks/suwayomi/compose.yaml
```yaml
# FLUGEL: Suwayomi - resmi ucretsiz kaynaklar (MANGA Plus, Webtoon). Indirmeler CBZ olarak Komga manga kutuphanesine.
# Yalniz 127.0.0.1:4567; disaridan suwayomi.<alan> giris nginx Basic Auth arkasinda.
services:
  suwayomi:
    image: ghcr.io/suwayomi/suwayomi-server:stable
    container_name: suwayomi
    network_mode: container:gluetun   # Flugel: Mullvad VPN uzerinden; IP saatlik degisir (suwayomi-ip-degistir.timer)
    restart: "no"   # uygulama-katman yonetir
    mem_limit: 2g
    environment:
      - TZ=Europe/Istanbul
      - DOWNLOAD_AS_CBZ=true
      - AUTO_DOWNLOAD_CHAPTERS=false
      - UPDATE_INTERVAL=0
      - EXTENSION_REPOS=["https://raw.githubusercontent.com/keiyoushi/extensions/repo/index.min.json"]
      - FLARESOLVERR_ENABLED=true
      - FLARESOLVERR_URL=http://localhost:8191
      - JAVA_TOOL_OPTIONS=-Xmx1536m
    volumes:
      - /srv/appdata/suwayomi:/home/suwayomi/.local/share/Tachidesk
      - /mnt/sidemain/media/books/manga/suwayomi:/home/suwayomi/.local/share/Tachidesk/downloads
```

## /opt/stacks/transmission2/compose.yaml
```yaml
services:
  transmission:
    image: lscr.io/linuxserver/transmission:latest
    mem_limit: 768m   # sistem-bakim v2: makul bellek sınırı
    container_name: transmission
    network_mode: "container:gluetun"
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Istanbul
    volumes:
      - /srv/appdata/transmission:/config:Z
      - /mnt/side/downloads:/downloads:Z
      - /mnt/side/watch:/watch:Z
    restart: "no"   # uygulama-katman yonetir
```

## /opt/stacks/tsidp/compose.yaml
```yaml
# tsidp — Tailscale kimliğiyle OIDC tek giriş (yalnız tailnet, Funnel kapalı)
# https://github.com/tailscale/tsidp  — v1.0 öncesi, deneysel
services:
  tsidp:
    image: ghcr.io/tailscale/tsidp:latest
    container_name: tsidp
    restart: unless-stopped
    environment:
      - TAILSCALE_USE_WIP_CODE=1
      - TS_STATE_DIR=/data
      - TS_HOSTNAME=idp
    volumes:
      - ./data:/data
```

## /opt/stacks/uptime-kuma/compose.yaml
```yaml
services:
  uptime-kuma:
    image: louislam/uptime-kuma:2
    container_name: uptime-kuma
    volumes:
      - /srv/appdata/uptime-kuma:/app/data:Z
      - /var/run/docker.sock:/var/run/docker.sock # Docker konteynerlerini otomatik bulması için
    mem_limit: 512m
    memswap_limit: 768m
    ports:
      - 3004:3001
    restart: unless-stopped
```
