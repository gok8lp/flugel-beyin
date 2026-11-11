# Sunucu entegrasyon fikirleri (28 Ekim 2026 canlı gözlem; parola/anahtar İÇERMEZ)

Sunucu: Ubuntu 26.04, Ryzen 5 2600X, 16 GB RAM (boşta ~4 GB), GTX 1660 Ti (boşta), 48 konteyner çalışıyor, 0 sağlıksız, 0 başarısız servis.
Diskler: `/` %50, `/mnt/side` %59, **`/mnt/sidemain` %90 (94 GB boş)**. Ağ: LAN 192.168.0.15 + Tailscale.

1. Yerel yapay zekâ: Ollama (11434) GPU'su boşta → PC'den `OLLAMA_HOST=http://192.168.0.15:11434`; Open WebUI hazır.
2. Medya: Jellyfin/Plex PC'de `jellyfin-mpv-shim` ile; Komga/Kavita ile kitap/manga.
3. İndirme: PC'deki qBittorrent yerine sunucudaki Transmission+Gluetun (VPN'li); magnet bağlantısını RPC ile ilet, dosyayı `~/Sunucu/side/downloads` üzerinden al.
4. Yedek: yapıldı (rsync snapshot). Sonraki: Immich'e Pictures klasörünü otomatik yükleme, Nextcloud istemcisiyle Documents eşitleme.
5. İzleme: Beszel agent'ı PC'ye, Uptime Kuma'ya "yedek-sunucu başarılı" push heartbeat'i, Homepage panosuna PC kartı.
6. Uzaktan erişim: Guacamole + wayvnc ile PC masaüstü; tsidp ile Tailscale kimliğiyle tek oturum; sunucu çıkış düğümü.
7. Bildirimler: Uptime Kuma/Telegram köprüsü olayları PC'de `notify-send` olarak.
8. Ağır işler: Docker'ı `docker -H ssh://flugel@192.168.0.15` ile uzakta derleme; Android SDK/Gradle (14 GB) için paylaşımlı önbellek.
9. Dayanıklılık: `/mnt/sidemain` %90 — temizlik/genişletme planı; RAM baskısı için konteyner limitleri; Jellyfin–Plex birini seç.

Parolalar bu belgede YOK. Öneri: KeePassXC/`pass`/KWallet ve Tailscale SSH + anahtar tabanlı giriş.

## Derin tarama bulguları (28 Ekim 2026, salt okunur)

**1) libvirtd kilitlenmesi (en önemli).** `W11-GPU` VM'inin başlatılması 17 saattir `prepare begin` hook'unda takılı.
Hook → `ai-vm-koruma.sh --pause` → satır 14 `virsh list --state-running` (zaman aşımı YOK) → libvirtd'den yanıt bekliyor, libvirtd de hook'u bekliyor (kilitlenme).
Sonuçlar: `virsh` donuyor; `vm-bosta-kapat` (1024 hata/24s) ve `guac-rdp-mullvad-ts` (326 hata/24s) sürekli düşüyor; libvirtd 4414 kez "Input/output error" yazıyor.
Önerilen onarım (henüz UYGULANMADI): hook'taki virsh çağrısına `timeout 5` eklemek veya çalışan VM'leri `/run/libvirt/qemu/*.pid`'den okumak; kilitli hook sürecini sonlandırmak.

**2) `mullvad-ts` bir VM** (192.168.122.75, RDP/Guacamole, isteğe bağlı uyandırılır). Mullvad+Tailscale birlikteliği için kurulan sistem büyük olasılıkla budur; bu PC'deki Mullvad–Tailscale çakışması ayrıdır (PC'de nft istisnası yok).

**3) Bellek:** 6 OOM kaydı, hepsi `subgen` konteynerinde (python3). RAM'in çoğunu immich_server, komga, stirling-pdf, open-webui, adguardhome kullanıyor. Ollama modelleri (3 × 3.3 GB) diskte; GPU boşta.

**4) Güvenlik:** UFW aktif, fail2ban + crowdsec aktif, root girişi kapalı, **SSH parola girişi hâlâ açık**, otomatik güvenlik güncellemesi açık, 2 paket güncellenebilir, reboot gerekmiyor.

**5) Disk:** `/mnt/sidemain` %90. Klasör bazlı `du` taraması çok yavaş olduğu için yarıda kesildi; sunucuda benim başlattığım bir `du` süreci hâlâ çalışıyor olabilir (kendiliğinden biter, I/O baskısı yaratır).

## Keşif raporu (28 Ekim 2026, salt okunur; sırlar, kişisel dosyalar ve veritabanları OKUNMADI)

- **Donanım:** MSI MS-7A38, Ryzen 5 2600X (6C/12T), 15 GB RAM (swap 3.7/4 GB dolu), GTX 1660 Ti.
- **Diskler:** sdb Kingston A400 SSD (LUKS+LVM, `/`), sdc 500 GB HDD (`/mnt/side`), **sda = Seagate "M3 Portable" USB 1 TB (`/mnt/sidemain`, %90)** — kendi rehberine göre 18 Ekim'de USB reset + I/O hatası; sistem SSD'sinde TRIM kapalı (86 TB yazılmış).
- **Ağ:** 192.168.0.15 + Tailscale; Docker köprüleri; `warp` (Cloudflare WARP) arayüzü; cloudflared iki tünel; UFW + DOCKER-USER yalnız LAN/Tailscale; Postfix :25, Samba, Cockpit :9090, Webmin, Apache :80 (yalnız varsayılan sayfa).
- **Konteyner:** 48, hepsi çalışıyor; 38 compose projesi `/opt/stacks` altında.
- **Kullanıcılar:** yalnız `root` ve `flugel`; flugel parolasız tam sudo (`/etc/sudoers.d/90-bakim-gecici`, 7 Ekim'den kalan "geçici" dosya); 4 yetkili SSH anahtarı.
- **Zamanlanmış:** root crontab'ında haftalık `docker system prune -f`; ~30 özel systemd timer (ai-gozcu, ai-vm-koruma, kritik-yedek, disk-health, vm-bosta-kapat, docker-watcher...).
- **Sunucunun kendi rehberi:** `/srv/rehber/*.txt` (00-OKU-BENI … 11) ve `/srv/dev/docs`. Rehber de "sunucu dışında yedek yok" diyor → PC yedekleri dahil her şey aynı kasada; harici/uzak kopya önerisi geçerli.
- **Kritik bulgular:** (1) libvirt hook kilitlenmesi — `ai-vm-koruma.sh` 14. satır `timeout 5` ile DÜZELTİLDİ (yedek: `*.yedek-20261028`), takılı süreç henüz sonlanmadı; (2) USB veri diski sağlığı; (3) swap dolu/OOM (`subgen`); (4) geçici sudoers + düz metin anahtar uyarısı (rehber madde 10).

## Onarım kaydı (28 Ekim 2026)
- Takılı libvirt hook zinciri (PID 3229383/400/406/407) sonlandırıldı; `virsh` yanıt veriyor; W11-GPU açılışı iptal oldu, GPU `nvidia`ya döndü.
- `ai-vm-koruma.sh` 14. satır düzeltildi (yedek: `*.yedek-20261028`); hook yedeği `/etc/libvirt/hooks/qemu.yedek-20261028-onar`.
- Kuyruktaki Guacamole isteği `mullvad-ts` VM'ini açtı; koruma betiği tasarımı gereği AI konteynerlerini durdurdu → VM boşta kapanınca (10 dk kuralı) kendiliğinden geri gelir.
- AdGuard bellek sınırı 1g → 1536m (canlı `docker update` + `/opt/stacks/adguard/compose.yaml`, yedek `.yedek-20261028`); DNS kesilmedi.
- SSH parola girişi kapatıldı: `/etc/ssh/sshd_config.d/00-sadece-anahtar.conf` (geri almak için bu dosyayı silip `sudo systemctl reload ssh`).
- `sidemain` boyut taraması düşük öncelikli çalışıyor → `/var/tmp/sidemain-du.txt` ("bitti" satırı gelince hazır).
- Gerçek kullanılmayan Docker imajı ≈2.2 GB (koharia-build, eclipse-temurin, 2× cyberlab/exercises, curl); silinmedi. "70 GB geri kazanılabilir" rakamı yanıltıcı.
- `subgen` OOM'u: 4 GB sınırını büyük transkripsiyon işleri aşıyor; sınır değiştirilmedi.
