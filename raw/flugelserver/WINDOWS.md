# Kullanıcının PC'si — sunucu entegrasyonu

Tarihsel kayıt; değişiklikten önce Windows'ta tekrar doğrula.

- Windows kullanıcı dizini `C:\Users\gokal`; SSH alias/anahtar zaten var, yeni anahtar gereksiz. Özel anahtar içeriğini okuma/paylaşma.
- Tailscale kurulu. H/S/M rclone SFTP bağlantıları sunucu kökü/side/sidemain için hazırlanmıştı; çalışan bağlantıları gelişigüzel kesme.
- Nextcloud native istemci kurulu; URL `https://flugelserver.tail42f1f4.ts.net:9443`; VFS kök `C:\Users\gokal\Nextcloud-Flugel`.
- Explorer'da sunucu dosyaları “Available when online” ve bulut simgesiyle GÖRÜLDÜ. Tam arşiv hemen PC'ye indirilmiyor.
- Belgeler `C:\Users\gokal\OneDrive\Belgeler`, İndirilenler `C:\Users\gokal\Downloads`:15dk döngüde rclone COPY -> `PC-Yedekleri/GOKALP`; değişen sürümler `_Surumler`. Kaynak silmeleri bu tek-yönlü yedekte sunucuya yayılmıyor.
- Normal Nextcloud VFS klasöründe silmek ise sunucudan da silebilir. Yer boşaltmak için “Free up space”; bu iki davranışı birbirine karıştırma.
- Yardımcılar `%LOCALAPPDATA%\FlugelServer`; credential DPAPI korumalı. Değerleri bağlama alma. Durum dosyası `nextcloud-backup-status.json`.
- Explorer Nextcloud native CLSID `{22145910-0213-4b12-8b43-243157b34c12}` mevcut; This PC kaydı eklendi, Quick Access pin istendi. Son navigation görünümü teyit edilmedi.
- Aynı klasörü açan `Nextcloud Klasoru.lnk` kullanıcı onayıyla kaldırıldı; `Nextcloud Dosyalarim.lnk` korundu.
- Komelia0.20.0 kurulu; son görülen ekran giriş, eski serverUrl localhost25600. Kurulu olmak oturumunun hazır olduğu anlamına gelmez. Komga Tailscale HTTPS10443 kullanılacak.
- Jellyfin Media Player1.12.0 kuruldu: `C:\Program Files\Jellyfin\Jellyfin Media Player\JellyfinMediaPlayer.exe`; masaüstü `Jellyfin.lnk`. Host alanına HTTPS12443 girildi; bağlantı/oturum/oynatma doğrulanmadı.
- Gereksiz Windows Jellyfin Server kaldırılması onaylandı. Winget kaydı kayboldu fakat Server exe kalmıştı; UAC nedeniyle bitiş doğrulanmadı. Oynatıcı ayrı dizin; uzak Jellyfin'e dokunma.
- Diğer kişisel masaüstü uygulamalarını “gereksiz” diye silme.
