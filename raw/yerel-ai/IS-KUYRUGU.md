# İş kuyruğu (müdür) — 2026-11-05

Roller: **Müdür** (ana oturum): kuyruk, dağıtım, doğrulama, kullanıcı soruları.
**IT lideri**: inceleme, mimari/güvenlik onayı, tek Git operatörü (commit/push).
**Uygulayıcı**: yalnız atanan, sınırları yazılı işler.

Kural: aynı dosya/servis/çalışma ağacına eşzamanlı yazma yok. Çalışan `flugel-yedek` ve
`flugel-ilk-geri-yukleme-testi` birimlerine kimse dokunmaz. Push yalnız kullanıcı hedefi onaylayınca.

## Durum
| # | İş | Atanan | Yazma kapsamı | Durum |
|---|---|---|---|---|
| Q0 | İlk tam restic yedeği + geri yükleme testi | sistem (systemd) | yok | sürüyor |
| L1 | Güvenlik/ağ/yalıtım/VPN fail-closed incelemesi, MFA/OIDC matrisi taslağı | IT lideri | salt okunur | tamam |
| L2 | Git geçmişi sır taraması (/opt/stacks, /usr/local, /etc) + temiz push deposu önerisi | IT lideri | salt okunur | tamam |
| I1 | Geri getirilecek araçların kaynak/veri envanteri; gündem botu, flugel-akis durumu | Uygulayıcı | salt okunur | tamam |
| I2 | Otomatik indirme tetikleri envanteri (Sonarr/Radarr/Prowlarr/Suwayomi/Transmission/timer) | Uygulayıcı | salt okunur | tamam |
| I3 | disk-keepalive/hdparm ölçümü (model, park/standby sayacı, sıcaklık) | Uygulayıcı | salt okunur | tamam |
| M1 | Kullanıcı kararları alındı (aşağıda) | Müdür | — | tamam |
| — | (iptal) Ara stack'leri arşivle/kaldır | — | — | YENİ KAPSAM ile iptal; hiçbir şey kaldırılmadı |

## Kullanıcı kararları (2026-11-05)
- SSD hedefi = `/srv/yedek-ssd` (sda); zaten yok → silinecek bir şey yok; `eski-yedek-temizle.timer/.service` MASKELENECEK.
- Retention: Re:Zero yedekleri (`rezero-ln-20261103`, `rezero-duzen-*`, `claude-20261031-claude`) TUTULUR; `/mnt/side/backups/guvenlik` restic'e alınıp geri yüklemesi doğrulanınca silinir. Restic 7 günlük/4 haftalık/6 aylık.
- GitHub: yeni PRIVATE `gok8lp/flugelserver-infra`, branch `main`; geçmiş taşınmaz, temiz/sanitize içerik; force push yok; /etc geçmişi push edilmez.

## Bekleyen (yedek + test doğrulandıktan sonra)
- Timer'ları etkinleştir; snapshot kimliklerini kaydet.
- `eski-yedek-temizle.timer` maskelenmesi (hedefleri zaten yok).
- Otomatik indirmeleri kapat (I2 sonucuna göre).
- AdGuard Home 7/24 + filtreler; yönetim yalnız LAN/tailnet.
- Uptime Kuma, Dockge, Dozzle, Cup, Guacamole ve 6. bölümdeki araçların geri getirilmesi (I1 sonucuna göre, tek tek).
- Jellyfin/Kavita/Komga 7/24 (uygulama-katman muafiyeti doğrula).
- Ollama + OpenWebUI kaldırma (modeller kullanıcıya bildirilerek).
- VPN fail-closed, ağ yalıtımı, negatif testler (L1 sonucuna göre).
- Compose sertleştirme, healthcheck, limit, sürüm sabitleme — tek grup.
- İki dilli README'ler, uygulama matrisi.
- Bakım sonunda `90-bakim-gecici` sudoers kaldırma (kullanıcı onaylı).

## L1/L2 sonucu → yeni işler (yedek+test sonrası, sırayla, tek grup)
- S1 gluetun kontrol API anahtarı rotasyonu (lider oturum çıktısında açığa çıktı) + tüketici `vpn-ip-degistir`; gluetun namespace üyeleri (transmission, prowlarr, flaresolverr, suwayomi) birlikte yeniden başlatılır.
- S2 `/opt/stacks`: `gluetun/auth/config.toml` takipten çıkar (git rm --cached).
- S3 İndirme fail-closed: jackett, sonarr, radarr, bazarr, lingarr → `network_mode: container:gluetun`; portlar gluetun'a 127.0.0.1; FIREWALL_OUTBOUND_SUBNETS daralt; gluetun sürüm sabitle; 51413 yayımını kaldır.
- S4 Transmission watch-dir otomatik ekleme kapat (mount/ayar), içerik silinmez.
- S5 Negatif testler (DB erişimi, photos/cloud yazma, VPN çıkış IP, IPv6).
- S6 no-new-privileges tüm compose; DB/redis/tsidp/nginx cap_drop (servis servis test).
- S7 tsidp bayat istemciler (Beszel/BookStack/Portainer geri gelecekse KALIR; OpenWebUI, claim-test×2 temizlenir) — yedekle.
- G1 Temiz export deposu `gok8lp/flugelserver-infra` (allowlist betiği, sanitize, gitleaks kurulumu onaylı ayrı adım). /etc ve /opt/stacks geçmişi ASLA push edilmez.
- K1 Funnel (Komga kök, Kavita :10000): KULLANICI KARARI → AÇIK KALIR (raporda risk).

## I1/I2/I3 sonucu → yeni işler
- B0 (ÖNCE, KRİTİK) Yedek kapsamını genişlet: /srv/appdata (tümü; immich/postgres, model-cache, nextcloud-db ham, ollama modelleri ve canlı sqlite'lar hariç), /srv/appdata/_kaldirildi-20261104, portainer_data + lingarr config volume, /opt/dockge. Mevcut çalışma bitince yeni dosya olarak kur (çalışan bash betiğini yerinde düzenleme YOK) ve ek yedek al.
- D1 Otomatik indirmeyi kapat: Sonarr/Radarr RSS=0 + indexer RSS/AutoSearch kapalı; Prowlarr SyncLevel addOnly/disabled; Bazarr wanted/upgrade kapalı; Lingarr automation kapalı; Transmission watch-dir kapalı; Suwayomi env AUTO_DOWNLOAD_CHAPTERS=false + globalUpdateInterval=0; uyg-gece.timer mask; Jackett UpdateDisabled=true. İçerik/ilerleme silinmez.
- D2 root cron `docker system prune -f` kaldır (durmuş korunan konteynerleri siler).
- R* Geri getirme sırası (tek tek, sabit tag, eski veriyle, 127.0.0.1/tailnet): AdGuard → Uptime Kuma → Guacamole → panel(akis+gundem-botu; homepage opsiyonel) → it-merkezi(GLPI+BookStack+mariadb 11.8) → Stirling → ConvertX → IT-Tools → PairDrop → FileBrowser → Beszel → Portainer → Dockge → Dozzle → Cup → Webmin (veri YOK, boş kurulum).
- P1 disk-keepalive: sdc'yi çıkar; sdb için değişken LBA; 24 saat attrlog karşılaştırması (önce/sonra kaydı).
- X1 Ollama+OpenWebUI kaldırma (appdata 6.2G+916M, image 9.4G+6.4G) — kullanıcıya bildirilerek.

## Kullanıcı kararları (2. tur)
- FileBrowser: Quantum geri gelir; `/:/hostfs` kaldırılır, yalnız eski config.yaml'daki gerçek kaynak dizinler bağlanır.
- OpenBooks: gluetun namespace'inde, yalnız elle kullanım, indirme hedefi karantina klasörü (kütüphane değil).
- torrent-bekci: remove-and-delete yerine durdur + listeden çıkar + karantinaya taşı (açmadan, 700) + bildir.

## Koruma listesi (dokunulmaz)
Immich, Nextcloud, Plex, Jellyfin, Kavita, Komga, Suwayomi, tsidp, giris/portal (gokalpgoksu.com), flugel-akis,
gündem botu, AdGuard, Uptime Kuma, Guacamole(+guacd, guac-db) ve 6. bölüm araçları.
Re:Zero: `/mnt/sidemain/media/books/manga/ReZero kara Hajimeru*`, `/mnt/side/backups/rezero-ln-20261103`,
`/mnt/side/backups/rezero-duzen-20261103-*`, `/mnt/side/backups/claude-20261031-claude` (ReZero epub içeriyor);
tam liste I1/manifestle genişletilecek.

## Koruma sistemi sertleştirme (kullanıcı isteği 2026-11-05 akşam) → `KORUMA-SISTEMI-PLANI.md`
Kullanıcı kararları (3. tur):
- Dış erişim: torrent/sonarr/radarr/prowlarr/bazarr/jackett/lingarr Cloudflare hostname'leri KALDIRILIR → yalnız tailnet. Portal, Immich, Nextcloud, ln/manga, video değişmez.
- DNS: AdGuard ev ağının TEK DNS'i (router'a ikinci DNS yok); Uptime Kuma DNS alarmı zorunlu.
- Bağımsız (offsite) yedek: şimdilik YOK → raporda kalan risk.
- Tailnet: yönetim portları yalnız sahibin cihazlarına → ACL taslağı hazırlanır, kullanıcı cihazları onaylayıp konsola yapıştırır.
Sıra: Faz1 indirme zinciri (H1 otomasyon kapat, H2 parolasız erişim kapat, H3 VPN fail-closed, H4 karantina, H5 konteyner sertleştirme) → Faz2 host (H6 ufw, H7 sshd, H8 güncelleme, H9 wsdd/apache, H10 sudoers) → Faz3 (H11 ölü ingress, H12 indirme hostname'leri kaldır, H13 ACL, H14 sır rotasyonu) → Faz4 AdGuard → Faz5 rapor.
- torrent-bekci (kullanıcı teyidi, bulundurma/delil riski açıklandıktan sonra): MOD=karantina KALIR. Karantina /mnt/side/karantina (700 root), yedek/Samba/kütüphane dışı, içerik açılmaz/kopyalanmaz, bildirimde ad yok. Taslak: scratchpad/h4/torrent-bekci.sh.

## Kullanıcı kararları (4. tur, 2026-11-05 ~19:00 UTC)
- X1 genişledi: Ollama + OpenWebUI + **Lingarr** KALDIRILIR (appdata/volume arşivlenir; medya klasörlerindeki mevcut altyazılar SİLİNMEZ). H1'de Lingarr automation yine kapatılır (kaldırılana kadar güvenli).
- Parolasız araçlar (Transmission RPC, Bazarr, Jackett; Lingarr kaldırılacak): rastgele parola sunucuda üretilir, `/etc/sistem-bakim/uygulama-parolalari/` (700/600 root), sohbete/Git'e düşmez; Sonarr/Radarr/Prowlarr bağlantıları ve torrent-bekci otomatik güncellenir.
- LAN: Apache :80 ve flugel-akis :3012 LAN'a KAPANIR (H6 ufw). akis.gokalpgoksu.com (cloudflared → localhost:3012) değişmez. Akış koduna/konteynerine dokunulmaz.
- Tailnet ACL: medya (Jellyfin/Plex/Kavita/Komga) tüm sahibin cihazlarına; yönetim panelleri yalnız yönetim cihazlarına (cihaz seçimi kullanıcıdan).

## Durum güncellemesi ~19:05 UTC
- H1 TAMAM (kullanıcı onayı + kullanıcı terminalinden; `hepsi dogrula` rc=0). Lider commit'leyecek.
- Kullanıcı kararları (5. tur): X1 daraltıldı → **Ollama KALIR** (flugel-akis kullanıyor; yalnız istek gelince, dışa kapalı). **OpenWebUI + Lingarr kaldırılır**. Bazarr çevirisi **kapatılır** (Lingarr'a bağlı translator kaldırılır, hazır altyazı indirme sürer — otomatik arama zaten H1 ile kapalı).
- Olay: lider Bazarr Gemini API anahtarını bir araç çıktısında açık metin gördü → kullanıcıya rotasyon önerisi (Bazarr çevirisi kapanacağı için anahtar Bazarr'dan da kaldırılabilir).
- H4 v2 lider incelemesinde (4 bloklayıcı giderildi); kurulum `h4/kur.sh` hazırlanıyor.
