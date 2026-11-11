# Dosya ve yedek ekosistemi (PC ↔ sunucu ↔ diğer cihazlar)

Taşıma katmanı: **Tailscale** (tüm cihazlar tek ağda). Ek paket kurulmadı.

| İş | Araç | Komut / yer |
|---|---|---|
| PC → sunucu yedek (tarihli, hardlink'li) | rsync | `yedek-sunucu` (kuru: `--kuru`) → `/mnt/side/backups/linux-pc/snap/<tarih>` |
| Yedekten geri dönüş | rsync | `yedek-geri liste`, `yedek-geri geri <yol> [snap] [--uygula]` (üzerine yazılan dosya `~/.local/state/yedek-geri/` altına alınır) |
| Sunucu disklerini klasör gibi kullan | SSHFS | `sunucu-bagla` / `sunucu-bagla ayir` → `~/Sunucu/{side,sidemain,sistem}` |
| Dosyayı başka cihaza yolla | Taildrop | Dolphin sağ tık → "Cihaza gönder" veya `taildrop-gonder dosya...` |
| Sunucudaki dosyayı cihaza yolla (PC'den geçmeden) | Taildrop | `sunucudan-gonder /sunucu/yolu cihaz-adı` |
| Gelen dosyaları al | Taildrop | tek sefer: `tailscale file get ~/Downloads/Taildrop`; sürekli: `systemctl --user enable --now taildrop-al` |
| Fotoğraf / bulut | Immich, Nextcloud | Dolphin yer imleri; Immich'e yükle: sağ tık → Immich (ilk kez `bulut-giris`) |

Ne zaman hangisi (kaynaklar: [Taildrop/Syncthing/LocalSend karşılaştırma tartışmaları](https://www.saashub.com/compare-syncthing-vs-localsend)):
tek seferlik gönderim = Taildrop; aynı klasörü sürekli eşit tutmak = Syncthing (PC'de kurulu, sunucuda yok — gerekirse eklenir);
aynı Wi-Fi'de hızlı telefon aktarımı = LocalSend/PairDrop (sunucuda PairDrop var).

Günlük otomatik yedek için (şu an KAPALI): `systemctl --user enable --now yedek-sunucu.timer`
