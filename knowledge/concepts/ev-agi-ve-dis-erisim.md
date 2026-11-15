---
{
  "kind": "fact",
  "title": "Ev ağı ve dış erişim düzeni (flugelserver + NetMASTER)",
  "project": "flugel-sunucu-ve-akis",
  "visibility": "internal",
  "updated_at": "2026-11-15"
}
---
# Ev ağı ve dış erişim düzeni

2026-11-15'te Claude (Opus 5.5) tarafından kuruldu ve doğrulandı. Ayrıntılı adım/yedek/geri dönüş kaydı: `~/Documents/ai_workplace/second-brain/raporlar/ev-agi-entegrasyon-2026-11-15.md` (vault dışında).

## Temel gerçekler
- Modem: Türksat Kablonet NetMASTER DOCSIS 3.0 ("Residential Gateway"), `http://192.168.0.1`. Paket 200/20 Mbps; hat sağlıklı (24 DS kanal, SNR 40–43 dB, düzeltilemeyen hata 0).
- **CGNAT:** modemin WAN adresi 100.88.x; evde genel IPv4 yok, IPv6 internet yok. Port yönlendirme/DMZ/DDNS/UPnP dışarıdan erişim sağlamaz. Dış erişim yalnız Cloudflare Tunnel, Tailscale Funnel ve Tailscale ile. Genel IP ancak Türksat'tan istenerek alınabilir.
- Sunucu LAN adresi 192.168.0.15 (modemde statik), Tailscale 100.86.88.1; sunucu `192.168.0.0/24`'ü Tailscale alt ağ rotası olarak yayınlar (telefon/Windows varsayılan kullanır, Linux `--accept-routes` ister).

## Yollar ve kim kullanır
| Yol | Ne için | Not |
|---|---|---|
| Cloudflare Tunnel (`*.gokalpgoksu.com`) | Tailscale'siz cihazlar (başka PC) | Değişmedi. Nextcloud Cloudflare Access arkasında |
| Tailscale Funnel | Mobil uygulamalar (manga/Komga, Nextcloud, Kavita) | **Bilerek açık (Gökalp, 2026-11-15):** `:443` Komga, `:8443` reader güncellemeleri + `/nextcloud`, `:10000` Kavita |
| Tailscale | Gökalp'in cihazları, her yerden | İnternet hızı değiştiği için Cloudflare ve Funnel ile birlikte tercih ediliyor |
| Evde `*.gokalpgoksu.com` | AdGuard bu adları yalnız ev ağı/Tailscale istemcilerine 192.168.0.15 olarak çözer; `giris` nginx `192.168.0.15:443` cloudflared ingress'inin aynısını sunar | Let's Encrypt wildcard `gokalpgoksu-ev` (dns-cloudflare, `/root/.cloudflare.ini`); evde Cloudflare 100 MB sınırı yok |
| Evde `*.ev` | `http://ev/` portal + `jellyfin.ev`, `immich.ev` vb. (`giris` `lan.conf`, 192.168.0.15:80) | n8n.ev/git.ev Tailscale adreslerine yönlenir. Apache masklendi |

## DNS
- Modem DHCP'si istemcilere DNS olarak 192.168.0.15 (AdGuard), ikincil 1.1.1.1 dağıtır.
- Tailscale admin DNS: global ad sunucuları 100.86.88.1 + 1.1.1.1, **Override DNS servers açık**. Laptop `accept-dns` kapalı, flugelserver `CorpDNS false`.
- AdGuard bridge ağında; ev ve Tailscale istemcilerini **172.18.0.1** olarak görür (docker-proxy). Cihaz bazında istatistik yok. gokalpgoksu.com kuralları `client=192.168.0.0/24|172.18.0.1` ile sınırlı.
- AdGuard Ebeveyn Denetimi **kapalı** (Gökalp isteği, 2026-11-15). Reklam/zararlı/oltalama/kumar listeleri açık; SafeSearch kapalı.
- DNS filtresi alan adı düzeyindedir: sosyal medya akışını dil/konu bazında süzemez.

## Mullvad proxy
- gluetun `HTTPPROXY=on`, kimliksiz; dış port `8889` (systemd soketi, `uyg-medya-indirme-p8889`), drop-in ile yalnız 192.168.0.0/24, 100.64.0.0/10, 127/8, 172.16/12.
- Kullanım: `192.168.0.15:8889` (evde) veya `100.86.88.1:8889` (Tailscale). Çıkış Mullvad İsveç; ölçülen ~34 Mbit/s. Dışarıda Tailscale üzerinden evin 20 Mbit/s yüklemesiyle sınırlı.
- Tailscale açık olmak trafiği VPN'den geçirmez; yalnız DNS ve ev ağı trafiği tünelden gider.
- NetMASTER'ın VPN'i yalnız IPsec; Mullvad IPsec sunmadığı için modeme eklenemez.

## Wi-Fi (NetMASTER)
2,4 GHz kanal 6 (eskiden otomatik → 1, kalabalık), 5 GHz kanal 36/80 sabit (otomatik DFS 52'ye kaçıyordu), Airtime Fairness açık, PMF iki bantta Capable, misafir ağı 2,4 GHz açık (192.168.10.x, Gökalp ara sıra kendisi için kullanıyor; parolayı kendisi belirledi). WPS, uzaktan yönetim, UPnP kapalı.

## Sınırlar / açık
- ufw `192.168.0.0/16` izni misafir ağını da kapsar; modem misafirleri ana ağa geçiriyor mu test edilmedi (Gökalp: misafir ağı yalnız kendisi için, sorun değil).
- Cloudflare'de arkasında servis olmayan rotalar: tools, pdf, ai, convert, ui, bd, portainer, admin.

Kaynaklar: Gökalp'in sohbetteki kararları (2026-11-15); canlı doğrulamalar ve yedekler yukarıdaki rapordadır.
