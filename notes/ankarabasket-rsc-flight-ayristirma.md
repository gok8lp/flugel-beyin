# ankarabasket Next.js RSC Flight Ayrıştırma ve Gömülü Katalog

Bağlantılar: [[map]] · [[lessons]] · [[decisions]] · [[assignr-ve-ankarabasket-kaynaklari]] · [[01 - Veri Kaynakları ve Tersine Mühendislik]] · [[Veri Tuzakları ve Uç Durumlar Kataloğu]]

## `self.__next_f.push` Doğrusal Karakter Tarayıcısı
- `https://www.ankarabasket.org.tr/` ana sayfasında bugün-2 ile bugün+4 arasındaki maçlar ve skorlar Next.js RSC Flight parçaları içinde gömülü `days` JSON dizisinde bulunur.
- `code` alanı `assignr` `matchNumber` ile birebir aynıdır (`ANK-U14E-A-2026-44`).
- Büyük RSC dizgilerinde Java Regex `StackOverflowError` hatasını önlemek için `AnkarabasketAyristirici.flight()` doğrusal karakter tarayıcısı ve dengeli köşeli parantez (`[...]`) çıkarımı kullanır.

## `robots.txt` Uyumluluğu
- `/api` yolu `robots.txt` içinde yasaklı (`Disallow: /api`) olduğu için `season-teams`, `clubs`, `tbf-catalog` ve `venues` verileri `app/src/main/assets/katalog/` altına gömülmüştür.
