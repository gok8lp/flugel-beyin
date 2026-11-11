# Öğrenilen Dersler (Lessons Learned)

Bağlantılar: [[map]] · [[memory]] · [[decisions]] · [[CLAUDE]] · [[duduk-genel-bakis]]

## 1. Veri Kaynakları ve Tersine Mühendislik Dersleri
- **Java Regex Yığın Taşması (`StackOverflowError`):** Next.js RSC Flight (`self.__next_f.push`) dizgileri 50 KB+ olduğunda Java'nın `("(?:[^"\\]|\\.)*")` özyinelemeli düzenli ifadesi `StackOverflowError` fırlatır. Çözüm: `Ayristiricilar.kt` içinde doğrusal karakter tarayıcı (`linear scanner`) kullanmak ([[ankarabasket-rsc-flight-ayristirma]]).
- **TBF `22328.0` Double Kimlik Tuzağı:** TBF WebAPI'de tam sayı olması gereken `activityId`, `takimIslemId` gibi kimlikler bazen `"22328.0"` biçiminde gelir. Çözüm: `EsnekInt` (`toDoubleOrNull()?.toInt()`) serileştiricisi ([[assignr-ve-ankarabasket-kaynaklari]]).
- **TBF `"10. Hafta"` Tarih Tuzağı:** Oynanmamış maçlarda `matchDate` alanı ISO tarih yerine `"10. Hafta"` metni döndürür. Tarih ayrıştırıcısı önce `\d{4}-\d{2}-\d{2}` kontrolü yapmalıdır ([[tbf-bulanik-mac-eslestirme]]).

## 2. Birleştirme ve Bildirim Dersleri
- **Hafta Bazlı Atama Kaldırılma Tespiti (`ATAMA_KALDIRILDI`):** Bir haftadaki en erken maç silindiğinde yalnızca `minTarih..maxTarih` aralığına bakmak o maçı pencere dışında bırakır. Çözüm: `Birlestirici.kt` içinde maçın `week` etiketinin (`"10. Hafta"`) aktif haftalar kümesinde (`hakemHaftalar`) olup olmadığını da kontrol etmek ([[yerel-arsiv-ve-senkronizasyon]]).

## 3. Sunucu ve Arayüz Dersleri
- **Cloudflare Uzaktan Yönetilen Tünel (`remote management`):** `cloudflared` tüneli Zero Trust panelinden yönetiliyorsa yerel `/etc/cloudflared/config.yml` içindeki `ingress` kuralları yok sayılır. Yerel yönetilen `akis.yml` (`cloudflared-akis.service`) tüneli kullanılmalıdır ([[cloudflare-ve-tailscale-baglanti-zinciri]]).
- **Yüzen Cam Başlık (`CamUstBaslik`) Üst Boşluğu:** `statusBarsPadding()` + `88.dp` yüksekliğindeki yüzen üst başlık altında ilk kartın kesilmemesi için liste `contentPadding(top = 140.dp)` olmalıdır ([[android-arac-zinciri-ve-mimari]]).
