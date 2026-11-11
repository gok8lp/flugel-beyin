# Ev ağı koruma sistemi: güvenlik sertleştirme planı (2026-11-05)

Hedef: flugelserver ev ağının DNS koruma noktası (AdGuard Home) olacak. Kendisi de ağdaki en sıkı
korunan cihaz olmalı. Önkoşul: ilk restic yedeği (`074ea935`, ana, 266 GiB) + geri yükleme testi GEÇTİ.

Sınırlar (YENI-KAPSAM §4, §8, §9):
- DNS filtresi yalnız alan adı düzeyinde çalışır; aynı alan adı içindeki içeriği ayıramaz.
- VPN içerik denetimi değildir. Antivirüs yalnız kötü amaçlı yazılım arar; yasa dışı içerik sınıflandırıcısı değildir.
- Hiçbir katman %100 koruma sağlamaz.

## Canlı denetim bulguları (salt okunur, 18:15–18:40 UTC)
| # | Bulgu | Risk |
|---|---|---|
| B1 | Transmission RPC `[::]:9091`, **parolasız, whitelist kapalı**; LAN, Docker ağları ve tüm tailnet torrent ekleyebilir | Kritik (torrent olayı ile doğrudan ilgili) |
| B2 | Sonarr/Radarr/Prowlarr `AuthenticationRequired=DisabledForLocalAddresses`; socket proxy üzerinden gelen istek "yerel" sayılıyor → LAN'dan parolasız | Yüksek |
| B3 | Bazarr 6767, Lingarr 5575 (auth kapalı), Jackett 9117 da `[::]` üzerinde | Yüksek |
| B4 | İndirme panelleri (torrent/sonarr/radarr/prowlarr/bazarr/jackett/lingarr.gokalpgoksu.com) Cloudflare ile internete açık; önlerinde yalnız nginx basic-auth var, MFA yok | Yüksek |
| B5 | Jackett, Sonarr, Radarr, Bazarr, Lingarr VPN dışından çıkıyor; gluetun `51413` publish; OUTBOUND_SUBNETS geniş | Yüksek |
| B6 | Transmission watch-dir açık, `start-added-torrents=true`; Sonarr/Radarr tamamlanan indirmeyi kütüphaneye otomatik alıyor | Yüksek (§9) |
| B7 | torrent-bekci eşleşmede `--remove-and-delete` (kanıt/inceleme imkânını siliyor) | Orta |
| B8 | ufw `192.168.0.0/16` ve `172.16.0.0/12` için tüm portlar açık (libvirt VM ağı ve Docker köprüleri dahil) | Orta |
| B9 | sshd: `X11Forwarding yes`, `MaxAuthTries 6`, AllowUsers yok (parola girişi zaten kapalı, root kapalı) | Düşük |
| B10 | Tailnet'te 39 cihaz; sunucu portlarına hepsi erişebiliyor (ACL doğrulanmadı) | Orta |
| B11 | Hiçbir konteynerde `no-new-privileges`/`cap_drop` yok; giris, plex, flugel-akis host ağında | Orta |
| B12 | 6 güvenlik güncellemesi bekliyor (unattended-upgrades açık) | Orta |
| B13 | Yedek yalnız aynı kasadaki diskte (`/mnt/side`); root ele geçirilirse veya fidye yazılımı bulaşırsa ikisi de gider | Yüksek (karar gerekli) |
| B14 | Ölü Cloudflare ingress (admin:9090, portainer:9000, tools, pdf, ai, convert, ui, bd): araç geri gelince doğrudan internete çıkar | Yüksek (geri getirmeden önce) |
| B15 | gluetun kontrol API anahtarı oturum çıktısında açığa çıktı; `/opt/stacks` Git geçmişinde DB parolaları var | Orta |
| B16 | wsdd tüm arayüzlerde (Docker köprüleri ve tailscale dahil) | Düşük |
| İyi | ufw varsayılan deny; DOCKER-USER WAN'dan düşürüyor; CrowdSec (nftables bouncer çalışıyor) + fail2ban sshd; AppArmor 122 enforce; sysctl çekirdek ayarları zaten sıkı; Samba `hosts allow` LAN/tailnet ve `valid users`; DB'ler ayrı ağda; indirme araçları fotoğraf/Nextcloud dizinini bağlamıyor | — |

## Uygulama sırası (her adım tek grup, yedek → değişiklik → doğrulama → commit)
**Faz 1: indirme zinciri (torrent olayına doğrudan karşılık)**
1. Otomatik indirme, ekleme ve içe aktarmayı kapat:
   - D1 tetikleri;
   - Sonarr/Radarr *Completed Download Handling* kapalı;
   - Transmission watch-dir kapalı, `start-added-torrents=false`;
   - Suwayomi otomatik bölüm kapalı;
   - `uyg-gece.timer` mask;
   - D2 `docker system prune` cron'u kaldır.
2. Parolasız erişimi kapat (B1–B3):
   - indirme socket'leri yalnız `127.0.0.1` + tailscale IP'ye bağlanır (`FreeBind`); LAN'dan erişim kesilir;
   - *arr için `AuthenticationRequired=Enabled`;
   - Transmission RPC whitelist `127.0.0.1` (tüketiciler: torrent-bekci, Sonarr, Radarr).
3. VPN fail-closed (S1, S2, S3, S5):
   - indirme ve arama araçlarının hepsi gluetun namespace'ine alınır, 51413 publish kaldırılır, gluetun sürümü sabitlenir, API anahtarı yenilenir;
   - testler: VPN kapalıyken çıkış yok, IPv6/DNS sızıntısı yok, DB/fotoğraf/Nextcloud erişimi yok.
4. Karantina akışı:
   - torrent-bekci eşleşmede durdurur, listeden çıkarır ve dosyayı açmadan `/mnt/side/karantina` (700 root) altına taşır, sonra bildirir;
   - tamamlanan indirmeler `clamscan` (kurulu) ile taranır; imza `freshclam` ile güncellenir;
   - içe aktarma yalnız elle.
5. İndirme konteynerleri:
   - `no-new-privileges`, `cap_drop: ALL` + gereken en az yetki;
   - bellek ve pids sınırı;
   - mümkünse read-only rootfs.

**Faz 2: host**
6. ufw daraltma (B8): LAN `/24` ve yalnız gereken portlar; VM ağına yalnız Samba `project`; Docker'dan hosta yalnız gereken portlar.
   - 5 dakikalık otomatik geri alma zamanlayıcısı ve ikinci SSH bağlantısıyla test.
7. sshd drop-in (B9): `AllowUsers flugel`, `X11Forwarding no`, `MaxAuthTries 3`, `LoginGraceTime 30`.
   - Aynı geri alma yöntemi ve ikinci bağlantı testi.
8. Güvenlik güncellemeleri: kademeli (B12); tailscale ve docker ayrı pencerede.
9. wsdd yalnız `enp37s0`; Apache :80 varsayılan sayfa kullanılmıyorsa kapatılır (bağımlılık kontrolü sonrası).
10. Bakım sonunda `90-bakim-gecici` sudoers kaldırılır.

**Faz 3: kimlik ve dış erişim**
11. Ölü Cloudflare ingress satırlarını sil (B14). Araçları geri getirmeden ÖNCE yapılır.
12. Dış erişim kararı (B4): kullanıcı tercihine göre.
13. Tailscale ACL (B10): sunucu yönetim portlarına yalnız sahibin cihazları erişir. Kullanıcı eylemi: admin konsolunda ACL yapıştırma ve bilinmeyen cihazları kaldırma.
14. Sır rotasyonu (B15): gluetun API anahtarı; etckeeper geçmişindeki eski sırlar raporlanır.

**Faz 4: ev ağı DNS koruması (AdGuard Home)**
15. AdGuard Home 7/24 geri gelir:
   - DNS `192.168.0.15:53` + tailnet;
   - yönetim arayüzü yalnız localhost/tailnet;
   - DNSSEC açık, şifreli upstream (DoH/DoT), rebinding koruması.
16. Filtreler (tekrarsız):
   - AdGuard DNS filter;
   - HaGeZi Pro (reklam/izleme);
   - HaGeZi Threat Intelligence (zararlı/oltalama);
   - HaGeZi NSFW (yetişkin);
   - SafeSearch zorunlu;
   - false-positive için izin listesi süreci.
17. Ağ geneline yayma (kullanıcı eylemi):
   - router DHCP'de DNS = `192.168.0.15`;
   - IPv6 RA/RDNSS da aynı adrese ayarlanmalı, yoksa cihazlar ISS DNS'ine kaçar;
   - tarayıcı DoH'u filtreyi atlatabilir (DoH engelleme listesi opsiyonel).
18. Uptime Kuma ile DNS izlenir; sunucu kapanırsa ev ağında DNS çözülmez (tek nokta riski, kullanıcı kararı).

**Faz 5: yedek güvenliği**
19. Bir kopya sunucudan bağımsız olmalı: çevrimdışı USB disk veya şifreli bulut deposu (kullanıcı kararı).

## Bu sunucunun yapamadıkları (açıkça)
- Router değil ve tek NIC'i var. Ev cihazlarının trafiğini satır içi denetleyemez (IDS/firewall). Koruma DNS düzeyindedir.
- Bilerek DoH, VPN veya sabit DNS kullanan cihaz filtreyi atlayabilir.
