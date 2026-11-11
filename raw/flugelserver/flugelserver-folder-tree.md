# flugelserver Canlı Dizin Ağacı (Folder Tree) ve Konteyner Durumu (2026-11-11)

## 1. Çalışan Docker Konteynerleri
```
NAMES                     IMAGE                                                            STATUS                     PORTS
duduk-server              duduk-server-duduk-server                                        Up 27 minutes              127.0.0.1:18420->18420/tcp
suwayomi                  ghcr.io/suwayomi/suwayomi-server:stable                          Up 14 hours                
flugel-akis               python:3.13-alpine                                               Up 5 days (healthy)        
jackett                   lscr.io/linuxserver/jackett:latest                               Up 6 days                  127.0.0.1:19117->9117/tcp
bazarr                    lscr.io/linuxserver/bazarr:latest                                Up 6 days                  127.0.0.1:16767->6767/tcp
radarr                    lscr.io/linuxserver/radarr:latest                                Up 6 days                  127.0.0.1:17878->7878/tcp
sonarr                    lscr.io/linuxserver/sonarr:latest                                Up 6 days                  127.0.0.1:18989->8989/tcp
komga                     gotson/komga:latest                                              Up 6 days                  127.0.0.1:18296->25600/tcp
kavita                    lscr.io/linuxserver/kavita:latest                                Up 6 days                  127.0.0.1:18295->5000/tcp
jellyfin                  lscr.io/linuxserver/jellyfin:latest                              Up 6 days (healthy)        8920/tcp, 127.0.0.1:18096->8096/tcp
flaresolverr              ghcr.io/flaresolverr/flaresolverr:latest                         Up 6 days                  
prowlarr                  lscr.io/linuxserver/prowlarr:latest                              Up 6 days                  
transmission              lscr.io/linuxserver/transmission:latest                          Up 5 days                  
gluetun                   qmcgaw/gluetun                                                   Up 7 minutes (unhealthy)   1080/tcp, 8000/tcp, 1080/udp, 8388/tcp, 8388/udp, 0.0.0.0:51413->51413/tcp, 0.0.0.0:51413->51413/udp, [::]:51413->51413/tcp, [::]:51413->51413/udp, 127.0.0.1:14567->4567/tcp, 127.0.0.1:18889->8888/tcp, 127.0.0.1:19091->9091/tcp, 127.0.0.1:19696->9696/tcp
nextcloud                 lscr.io/linuxserver/nextcloud:latest                             Up 7 days (healthy)        80/tcp, 127.0.0.1:8443->443/tcp, 192.168.0.15:8443->443/tcp
immich_server             ghcr.io/immich-app/immich-server:release                         Up 6 days (healthy)        0.0.0.0:2283->2283/tcp, [::]:2283->2283/tcp
immich_machine_learning   ghcr.io/immich-app/immich-machine-learning:release-cuda          Up 6 days (healthy)        
tsidp                     ghcr.io/tailscale/tsidp:latest                                   Up 7 days                  
nextcloud-db              postgres:17-alpine                                               Up 7 days (healthy)        5432/tcp
plex                      lscr.io/linuxserver/plex:latest                                  Up 7 days (healthy)        
immich_postgres           ghcr.io/immich-app/postgres:14-vectorchord0.3.0-pgvectors0.2.0   Up 6 days (healthy)        5432/tcp
immich_redis              redis:6.2-alpine                                                 Up 6 days                  6379/tcp
giris                     nginx:1.27-alpine                                                Up 6 days                  
```

## 2. Disk ve Bağlama Noktaları (df -h)
```
Filesystem                         Size  Used Avail Use% Mounted on
/dev/mapper/ubuntu--vg-ubuntu--lv  437G  181G  238G  44% /
/dev/mapper/ubuntu--vg-ubuntu--lv  437G  181G  238G  44% /
/dev/mapper/sdc_crypt              458G  295G  140G  68% /mnt/side
/dev/mapper/sdd_crypt              916G  764G  143G  85% /mnt/sidemain
```

## 3. /srv Dizin Ağacı (2 Seviye)
```
/srv
/srv/appdata
/srv/appdata/_kaldirildi-20261104
/srv/appdata/_kaldirildi-20261105
/srv/appdata/adguard
/srv/appdata/ai-library
/srv/appdata/alertmanager
/srv/appdata/backrest
/srv/appdata/bazarr
/srv/appdata/dozzle
/srv/appdata/filebrowser
/srv/appdata/gmail-notifier
/srv/appdata/grafana
/srv/appdata/guacamole
/srv/appdata/immich
/srv/appdata/jackett
/srv/appdata/jellyfin
/srv/appdata/kavita
/srv/appdata/komga
/srv/appdata/nextcloud
/srv/appdata/nextcloud-db
/srv/appdata/ollama
/srv/appdata/plex
/srv/appdata/prometheus
/srv/appdata/prowlarr
/srv/appdata/radarr
/srv/appdata/sonarr
/srv/appdata/suwayomi
/srv/appdata/transmission
/srv/appdata/uptime-kuma
/srv/archive
/srv/archive/appdata
/srv/archive/backups
/srv/archive/pc-yedekleri
/srv/archive/security
/srv/archive/stacks
/srv/backups
/srv/dev
/srv/dev/README.md
/srv/dev/archive
/srv/dev/artifacts
/srv/dev/docs
/srv/dev/projects
/srv/dev/tools
/srv/dev/workspaces
/srv/geri-yukleme
/srv/geri-yukleme/test-20261105-1813
/srv/operations
/srv/operations/ai-context
/srv/operations/audit
/srv/operations/changes
/srv/operations/history
/srv/operations/inventory
/srv/operations/sunucu-kilavuzu
/srv/project
/srv/project/README.txt
/srv/project/docs
/srv/project/gelen
/srv/project/surumler
/srv/project/windows
/srv/rehber
/srv/rehber/00-OKU-BENI.txt
/srv/rehber/01-HARITA.txt
/srv/rehber/02-UYGULAMALAR.txt
/srv/rehber/03-DISKLER-CANLI.txt
/srv/rehber/04-YEDEKLER.txt
/srv/rehber/05-SANAL-MAKINELER.txt
/srv/rehber/06-YEDEK-DURUMU-CANLI.txt
/srv/rehber/07-OTOMASYONLAR.txt
/srv/rehber/08-ERISIM-GUVENLIK.txt
/srv/rehber/09-BILINEN-SORUNLAR.txt
/srv/rehber/10-DEGISIKLIK-GECMISI.txt
/srv/rehber/11-KAYNAK-KORUMA-2026-10-21.txt
/srv/rehber/komutlar
/srv/yedek
/srv/yedek/2026-10-21-claude
/srv/yedek/2026-10-21-codex
/srv/yedek/guvenlik-yamasi-20261025-2002
/srv/yedek/uptime-kuma-v1-20261025-201200.tar.gz
```

## 4. /opt Dizin Ağacı (2 Seviye)
```
/opt
/opt/Antigravity
/opt/Antigravity/LICENSE.electron.txt
/opt/Antigravity/LICENSES.chromium.html
/opt/Antigravity/antigravity
/opt/Antigravity/chrome-sandbox
/opt/Antigravity/chrome_100_percent.pak
/opt/Antigravity/chrome_200_percent.pak
/opt/Antigravity/chrome_crashpad_handler
/opt/Antigravity/icudtl.dat
/opt/Antigravity/libffmpeg.so
/opt/Antigravity/libvk_swiftshader.so
/opt/Antigravity/libvulkan.so.1
/opt/Antigravity/locales
/opt/Antigravity/resources
/opt/Antigravity/resources.pak
/opt/Antigravity/snapshot_blob.bin
/opt/Antigravity/v8_context_snapshot.bin
/opt/Antigravity/version
/opt/Antigravity/vk_swiftshader_icd.json
/opt/Mullvad VPN
/opt/Mullvad VPN/LICENSE.electron.txt
/opt/Mullvad VPN/LICENSES.chromium.html
/opt/Mullvad VPN/chrome-sandbox
/opt/Mullvad VPN/chrome_100_percent.pak
/opt/Mullvad VPN/chrome_200_percent.pak
/opt/Mullvad VPN/chrome_crashpad_handler
/opt/Mullvad VPN/icudtl.dat
/opt/Mullvad VPN/libEGL.so
/opt/Mullvad VPN/libGLESv2.so
/opt/Mullvad VPN/libffmpeg.so
/opt/Mullvad VPN/libvk_swiftshader.so
/opt/Mullvad VPN/libvulkan.so.1
/opt/Mullvad VPN/locales
/opt/Mullvad VPN/mullvad-gui
/opt/Mullvad VPN/mullvad-vpn
/opt/Mullvad VPN/resources
/opt/Mullvad VPN/resources.pak
/opt/Mullvad VPN/snapshot_blob.bin
/opt/Mullvad VPN/v8_context_snapshot.bin
/opt/Mullvad VPN/vk_swiftshader_icd.json
/opt/basket-bot
/opt/basket-bot/__pycache__
/opt/basket-bot/anime_takip.py
/opt/basket-bot/anime_takip.py.onceki-2026-10-14_1417
/opt/basket-bot/anime_takip.py.onceki-2026-10-14_1427
/opt/basket-bot/ayar.json
/opt/basket-bot/basket_bot.py
/opt/basket-bot/imdb_puan.py
/opt/containerd
/opt/containerd/bin
/opt/containerd/lib
/opt/dockge
/opt/dockge/data
/opt/filebrowser
/opt/filebrowser/docker-compose.yml
/opt/filebrowser/filebrowser.db
/opt/flugel-archives
/opt/flugel-archives/Basketbol
/opt/flugel-cyberlab
/opt/flugel-cyberlab/current
/opt/flugel-cyberlab/releases
/opt/gemini-cli
/opt/gemini-cli/node_modules
/opt/gemini-cli/package-lock.json
/opt/gemini-cli/package.json
/opt/nvidia
/opt/nvidia/nsight-compute
/opt/nvidia/nsight-systems
/opt/scripts
/opt/scripts/gmail-auth.py
/opt/scripts/gmail-notifier.py
/opt/stacks
/opt/stacks/_bakim
/opt/stacks/_kaldirildi-20261104
/opt/stacks/_kaldirildi-20261105
/opt/stacks/adguard
/opt/stacks/backrest
/opt/stacks/bazarr
/opt/stacks/cup
/opt/stacks/dozzle
/opt/stacks/flaresolverr
/opt/stacks/giris
/opt/stacks/gluetun
/opt/stacks/guacamole
/opt/stacks/immich_server
/opt/stacks/izleme
/opt/stacks/jackett
/opt/stacks/jellyfin
/opt/stacks/kavita
/opt/stacks/komga
/opt/stacks/nextcloud
/opt/stacks/ollama
/opt/stacks/panel
/opt/stacks/plex
/opt/stacks/prowlarr
/opt/stacks/radarr
/opt/stacks/sonarr
/opt/stacks/subgen
/opt/stacks/suwayomi
/opt/stacks/transmission2
/opt/stacks/tsidp
/opt/stacks/uptime-kuma
/opt/stacks/yukle
/opt/telegram-kopru
/opt/telegram-kopru/__pycache__
/opt/telegram-kopru/kopru.py
/opt/telegram-kopru/kopru.py.bak
```

## 5. /mnt/side ve /mnt/sidemain Dizin Ağacı (2 Seviye)
```
/mnt/side
/mnt/side/arsiv
/mnt/side/backups
/mnt/side/backups/claude-20261031-claude
/mnt/side/backups/guvenlik
/mnt/side/backups/rezero-duzen-20261103-162949.json
/mnt/side/backups/rezero-duzen-20261103-wn-duzeltme.txt
/mnt/side/backups/rezero-ln-20261103
/mnt/side/downloads
/mnt/side/downloads/complete
/mnt/side/downloads/incomplete
/mnt/side/files
/mnt/side/files/images
/mnt/side/files/installers
/mnt/side/files/notes
/mnt/side/files/school
/mnt/side/karantina
/mnt/side/lost+found
/mnt/side/projects
/mnt/side/projects/NxtPanel-development
/mnt/side/projects/NxtPanel-development.zip
/mnt/side/projects/flugel
/mnt/side/projects/flugel-cyber-lab
/mnt/side/projects/flugel-island
/mnt/side/projects/flugel-manga
/mnt/side/projects/flugel-sunucu-app
/mnt/side/projects/home-server
/mnt/side/projects/island-adaylar
/mnt/side/projects/weekly-task
/mnt/side/projects/weekly-tasks
/mnt/side/projects/workspaces
/mnt/side/restic
/mnt/side/watch
/mnt/side/yedek
/mnt/sidemain
/mnt/sidemain/appdata
/mnt/sidemain/backups
/mnt/sidemain/books
/mnt/sidemain/cloud
/mnt/sidemain/cloud/nextcloud
/mnt/sidemain/immich
/mnt/sidemain/kamiyomu
/mnt/sidemain/lost+found
/mnt/sidemain/media
/mnt/sidemain/media/books
/mnt/sidemain/media/movies
/mnt/sidemain/media/series
/mnt/sidemain/media/tv-recordings
/mnt/sidemain/movies
/mnt/sidemain/nextcloud_data
/mnt/sidemain/personal
/mnt/sidemain/personal/usa
/mnt/sidemain/personal/yedek-amk
/mnt/sidemain/photos
/mnt/sidemain/photos/immich
/mnt/sidemain/series
/mnt/sidemain/yedek amk
```

## 6. /home/flugel Dizin Ağacı (2 Seviye)
```
/home/flugel
/home/flugel/Arc 9 - Light of a Nameless Star-20260519T215221Z-3-001.zip.bak
/home/flugel/adguard
/home/flugel/duduk-server
/home/flugel/duduk-server/Dockerfile
/home/flugel/duduk-server/README.md
/home/flugel/duduk-server/app-debug.apk
/home/flugel/duduk-server/app.py
/home/flugel/duduk-server/data
/home/flugel/duduk-server/docker-compose.yml
/home/flugel/duduk-server/ekranlar
/home/flugel/durdurulan-konteynerler-20261104.txt
/home/flugel/flugel-reader-updates
/home/flugel/flugel-reader-updates/latest.json
/home/flugel/flugel-reader-updates/releases
/home/flugel/gokalpgoksu
/home/flugel/gokalpgoksu/islem-kaydi.log
/home/flugel/indirme-rezero
/home/flugel/indirme-rezero/Re:Zero Novel
/home/flugel/izleme-kurulum
/home/flugel/izleme-kurulum/alertmanager
/home/flugel/izleme-kurulum/backrest
/home/flugel/izleme-kurulum/compose.yaml
/home/flugel/izleme-kurulum/db-dokum
/home/flugel/izleme-kurulum/db-dokum.service
/home/flugel/izleme-kurulum/db-dokum.timer
/home/flugel/izleme-kurulum/eski-yedek-temizle
/home/flugel/izleme-kurulum/eski-yedek-temizle.service
/home/flugel/izleme-kurulum/eski-yedek-temizle.timer
/home/flugel/izleme-kurulum/gece-yedek
/home/flugel/izleme-kurulum/gece-yedek.service
/home/flugel/izleme-kurulum/gece-yedek.timer
/home/flugel/izleme-kurulum/grafana
/home/flugel/izleme-kurulum/host
/home/flugel/izleme-kurulum/pano_uret.py
/home/flugel/izleme-kurulum/prometheus
/home/flugel/izleme-kurulum/yama_danisman.py
/home/flugel/izleme-kurulum/yama_katman.py
/home/flugel/sistem-bakim
/home/flugel/sistem-bakim/akis.py.v1-2026-10-09_2246
/home/flugel/sistem-bakim/durum
/home/flugel/sistem-bakim/guac-sifre.sh
/home/flugel/sistem-bakim/islem-kaydi.log
/home/flugel/sistem-bakim/kaynak-siniri.py
/home/flugel/sistem-bakim/komga-adlar.py
/home/flugel/sistem-bakim/komga-bolumler.py
/home/flugel/sistem-bakim/mullvad-sifre.sh
/home/flugel/sistem-bakim/sunucu-optimizasyon.sh
/home/flugel/sistem-bakim/vmroot.sh
/home/flugel/sistem-bakim/w11-kurulum
/home/flugel/sistem-bakim/yedek-etc-2026-10-07_2328
/home/flugel/sistem-bakim/yedek-logind.conf-1792174702
/home/flugel/sistem-bakim/yedek-v2-2026-10-12_2243
/home/flugel/suwayomi-disk-guard.sh
/home/flugel/taildrop-nextcloud-yedek-20261106
/home/flugel/taildrop-nextcloud-yedek-20261106/DERSLER-BILGI.md
/home/flugel/tailscale-serve-yedek-20261105-061248.json
/home/flugel/work
/home/flugel/work/akis-app
/home/flugel/work/android-sdk
/home/flugel/work/avd
/home/flugel/work/bin
/home/flugel/work/build-100007.log
/home/flugel/work/ci.log
/home/flugel/work/ci2.log
/home/flugel/work/ci3.log
/home/flugel/work/ekran1.png
/home/flugel/work/emu-kurulum.log
/home/flugel/work/emu.log
/home/flugel/work/gr-public.sh
/home/flugel/work/gr.sh
/home/flugel/work/gradle-home
/home/flugel/work/home-b
/home/flugel/work/img
/home/flugel/work/keys
/home/flugel/work/keystore.properties.yedek-20261031-claude
/home/flugel/work/koharia-public
/home/flugel/work/koharia-reader
/home/flugel/work/latest-100007.json
/home/flugel/work/lint.log
/home/flugel/work/ln-kategoriler-20261102T145804Z
/home/flugel/work/mega-rezero-20261102
/home/flugel/work/organize_ln_languages.py
/home/flugel/work/out
/home/flugel/work/public-100008.log
/home/flugel/work/public-100008b.log
/home/flugel/work/public-100008c.log
/home/flugel/work/public-100008d.log
/home/flugel/work/public-100009.log
/home/flugel/work/publish.sh
/home/flugel/work/rel.log
/home/flugel/work/rezero-organize-20261102
/home/flugel/work/run.sh
/home/flugel/work/sa.log
/home/flugel/work/st.sh
/home/flugel/yedek
/home/flugel/yedek/bookstack-users-20261025-192727.sql
/home/flugel/yedek/immich-system-config-20261025-221805.json
```
