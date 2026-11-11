# Bulgular ve yol haritası

Öncelik, doğrulanan etki ve yapılacak iş birlikte yazılmıştır. Bu dosyadaki öneriler uygulanmadı.

| Öncelik | Bulgular / kanıt | Sonraki iş ve başarı ölçütü |
|---|---|---|
| P1 | `/mnt/sidemain` %90 dolu, 94 GB boş (SV01) | En büyük klasörleri salt okunur ölç; saklama kurallarını kullanıcıyla belirle. Fotoğraf, Nextcloud ve kitap verisini otomatik silme. Başarı: kapasite payı ve büyüme tahmini belgeli. |
| P1 | VM otomasyonu `virsh` zaman aşımıyla tekrar hata veriyor (SV02) | Libvirt soketleri, oturum URI'si ve bloklanan sorguyu incele; çalışan VM'leri kesmeden düzelt. Başarı: süre sınırlı listeleme ve en az 3 timer çevrimi başarılı. |
| P1 | Yedekler success ama restore bilinmiyor (SV02) | Ayrı hedefe kontrollü geri yükleme ve checksum testi; offsite kapsamını belirle. Üretim verisinin üstüne yazma. |
| P2 | FileBrowser launcher `http://...:8085` bağlantısı reddediliyor; konteyner loopback'e bağlı (HTTP01/SV01) | Kısayolu mevcut Tailscale HTTPS proxy adresi `https://flugelserver.tail42f1f4.ts.net:26443/` ile düzelt. Bu adres GET 200 verdi; uygulama oturum testi yapılmadı. |
| P2 | Jackett launcher kök adresi GET 400, HEAD 405 (HTTP01) | Doğru UI yolu ve proxy Host ayarını incele. API token gerektiren özel ayarları pakete koyma. |
| P2 | 27 konteynerde healthcheck tanımlı değil (SV01) | Her servis için gerçek readiness uç noktası ekle; 401 gereken yerde beklenen sonuç sayılabilir. Yanlış probe ile restart döngüsü oluşturma. |
| P2 | RAM/swap dalgalanıyor, çok sayıda özel timer var (SV01/SV02) | PSI, vmstat ve servis zaman çizelgesini korele et; swap-flush/self-heal çakışmalarını gözden geçir. |
| P2 | Docker imajları 89.51 GB (SV01) | Kullanılan ve rollback için gereken imajları ayırarak temizlik planla. Otomatik `docker system prune -a --volumes` kullanma. |
| P2 | F11 Quick açıyor; videodaki preset/ok tuşu akışı tamamlanmadı (DESK01) | Doğru profile/preset panelini hedefle; fiziksel kısayol, oklar, Enter, Escape ve geri dönüşü ekranla doğrula. |
| P3 | Geçmiş Quickshell SIGSEGV kaydı; Lua/Qt yerel yamaları (PC01) | Güncel sürümle tekrarlanabilirlik ara; yamaları patch dosyasıyla koru, güncelleme sonrası smoke test yap. |
| P3 | AUR ve orphan paketler (PC01) | İhtiyaç listesi çıkar; kullanıcı tercihini bilmeden kaldırma. |

## Kapsam ve güven düzeyi

31 sunucu uygulama kısayoluna HTTP HEAD denendi; bazıları GET ile tekrar denendi. 401, oturum/API anahtarı gereksinimi olabilir; tek başına arıza değildir. Transmission HEAD 501 fakat GET 200. Sunucu Durumu HEAD 404 fakat GET 200. FileBrowser uygulamasının kendisi hem loopback hem HTTPS proxy üzerinden yanıt veriyor; yanlış olan launcher adresi. Uçtan uca oturum açma, dosya yükleme, fotoğraf indeksleme, altyazı üretimi, torrent indirme ve bütün UI akışları test edilmedi.

## Yapılacakların sırası

1. Depolama ve yedek güvencesini netleştir.
2. Libvirt timeout ve otomasyon çakışmalarını düzelt.
3. Kısayol/adres hatalarını düzelt; salt okunur erişim testini tekrarla.
4. Uygun healthcheck ve izleme eşiklerini ekle.
5. Masaüstü preset/klavye akışını bitir.
6. İhtiyaç duyulmayan uygulamalar için kullanıcı tercihine dayalı sadeleştirme yap.

Bu analiz sırasında otomatik onarım, paket kaldırma, disk temizleme, servis restart veya Claude hesap ayarı değişikliği yapılmadı.
