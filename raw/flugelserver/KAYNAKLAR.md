# Kaynak ve doğrulama sırası

1. `veri/guncel.json`: tarihli canlı metadata, `tools/collect.py` ile alındı. İçerik/veritabanı/yedek geri yükleme testi değil. Container health çıktısı durmuş container'da eski değer olabilir; önce state'e bak.
2. `IS-DURUMU.md`, `WINDOWS.md`: sohbet içinde yapılan ve yarım kalan işlemler. Sonraki ajan eski işleri kendi kendine sürdürmesin.
3. `veri/adresler.json`: yayın kataloğundan. URL/port eşlemesi, erişilebilirlik veya bant genişliği ölçümü değil.
4. `../CLAUDE-DEVIR-2026-10-20.md`: daha uzun tarihsel devir. Sonradan işi durdurma/kaldırılmadı bilgisi bu pakette daha güncel; çelişkide bu eski belgeyi üstün tutma.
5. `../ekosistem-denetimi-2026-10-19.md`: önceki geniş denetim. Güncel durum değil; yalnız gerektiğinde ilgili başlığı oku.
6. `../filesystem-inventory-2026-10-20.json`: eski bounded filesystem taraması. Bazı du işlemleri timeout nedeniyle kısmidir; “bütün dosyalar tarandı” deme.
7. `../nextcloud-kullanim.md`: önceki Nextcloud kullanım notu.

Yukarıdaki eski dosyalar ZIP'e tekrar konmadı. Ham `server-inventory.json` bütünü sır taramasından geçirilmiş sayılmadığı için bu pakete dahil edilmedi. İhtiyaç halinde yalnız güvenli alanları seçerek oku.

## Bilerek bilinmeyenler

Tüm dosyaların içerikleri, bütün kullanıcı/rol ve uygulama oturumları, bütün bot görevlerinin iş mantığı, bütün DB şemaları, yedeklerin gerçek restore sonucu, uygulama başına dış erişim testi, ağ bant genişliği/ölçülmüş gecikme, VM içindeki Eclipse proje yolu, disk hatalarının kesin nedeni bu pakette eksiksiz bulunmaz. AI bunları tahminle tamamlamasın; ihtiyaç olunca dar kapsamda doğrulasın.
