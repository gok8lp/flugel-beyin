# Tanılama ve doğrulama kılavuzu

Bu komutlar tanılama içindir. Adres ve dosya yolları 28 Ekim 2026 gözlemine aittir; değişiklikten önce doğrula. Süreli SSH kullan, önce hedef hostname'i kontrol et. Parola/anahtar içeriğini loga veya sohbete yazma.

## PC

```bash
hostname
hyprctl version
hyprctl monitors -j
hyprctl configerrors
systemctl --failed --no-pager
systemctl --user --failed --no-pager
wpctl status
free -h
df -h /
qs list --all
```

Hyprland burada Lua kullanıyor. Eski `hyprctl dispatch workspace 9` sözdizimini kopyalama. Önce yerel keybind örneklerini incele; güncel dispatcher türleriyle çalış. Arayüz değişimi için `~/.local/bin/arayuz-sec end4-pC` veya `~/.local/bin/arayuz-sec Caelestia` kullan; GUI ve oturum etkisi olduğu için yalnız ilgili masaüstü görevi sırasında yap.

## Sunucuya bağlanma

```bash
ssh -i ~/.ssh/id_ed25519_homeserver -o IdentitiesOnly=yes -o BatchMode=yes -o ConnectTimeout=8 flugel@192.168.0.15 hostname
```

Private key dosyasının içeriğini hiçbir zaman metin olarak taşıma. Host key değişirse kontrol et; `StrictHostKeyChecking=no` ile geçiştirme. LAN dışında Tailscale hedefi kullanılabilir; auth check çıkarsa bağlantıyı bekletip gerçek kimlik doğrulamasını tamamlat.

Sunucuda kullanılabilecek salt okunur kontroller:

```bash
systemctl --failed --no-pager
docker ps --format '{{.Names}}	{{.Status}}'
docker stats --no-stream
docker system df
df -h / /mnt/side /mnt/sidemain
free -h
cat /proc/pressure/memory
vmstat 1 4
timeout 8 virsh -c qemu:///system list --all
systemctl show vm-bosta-kapat.service -p ActiveState -p Result -p ExecMainStatus
journalctl -u vm-bosta-kapat.service --since '30 minutes ago' --no-pager -n 30
```

Docker inspect'in tüm çıktısını bilgi paketine kopyalama: Env ve healthcheck komutlarında sır olabilir. Sadece imaj, durum, port, mount, restart politikası ve Compose kaynak yolu gibi seçilmiş alanları çıkar.

## Değişiklik kabul ölçütleri

- Önce mevcut değeri ve hedef davranışı kaydet; yapılandırma değişikliğinde tarihli yedek al.
- Bir seferde bir mantıksal değişiklik; syntax/config doğrulaması yap.
- Web servisinde HTTP yanıtı, giriş ve gerçek kullanım senaryosunu ayrı test et. 200 yalnız HTTP seviyesini kanıtlar.
- Docker'da running/healthy, veri kaydı ve restore kanıtı değildir.
- Disk mapper adını fiziksel aygıt sanma. `sdd_crypt` güncel sda üzerinde olabilir.
- Veritabanı yedeği ve mount eşlemesi bilinmeden konteyneri yeniden oluşturma.
- Başarıyı kullanıcıya görünür kanıtla bildir; test edilmeyen kısmı açık tut.

## Bekleyen masaüstü işi

F11/preset/ok tuşu işi tamamlanmadı. Önce mevcut ayar stilini ve hangi panelin açıldığını belirle, videodaki kareyle karşılaştır. Kısayola gerçekten bas; sağ/sol/yukarı/aşağı/Enter/Escape ve eski temaya dönüşü dene. Yalnız IPC komutunun exit 0 dönmesi klavye testinin geçtiği anlamına gelmez.
