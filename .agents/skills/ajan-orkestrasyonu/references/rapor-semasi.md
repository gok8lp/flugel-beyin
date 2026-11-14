# Alt ajan teslim raporu

Yaklaşık en çok 30 satır kullan. Ham logları taşıma; tam logun izinli dosya yolunu ve gerekli son satırlarını ver. Dosya/satır alanı kanıtın yerini gösterir; dosya dışı kanıtta komut ve log konumu yazılır.

```text
Bulgu: <hedefe göre sonuç; bitti ifadesi kontrol edilene kadar iddia>
Dosya:satır: <değişen/yeni TAM yollar ve ilgili başlangıç satırları>
Diff özeti: <hangi davranış değişti; çıkarılan/eklenen ana parçalar>
Öneri eşlemesi: <öneri no → tam dosya/bölüm; her öneri kapsansın>
Kanıt: <doğrulama komutu; çıkış kodu; kısa gerçek çıktı/son satırlar>
Kabul: <her ölçüt için geçti/kaldı/doğrulanmadı; kanıt bağlantısı>
Karar gerekiyor mu: <hayır / seçenekler, etkileri ve gereken karar>
Belirsizlik: <test edilmeyenler, erişilemeyen kaynak, kalan risk ve açık iş>
```

Birden çok paralel bulgu varsa `Bulgu / Dosya:satır / Kanıt / Karar gerekiyor mu / Belirsizlik` alanlarını kısa maddelerde yinele; ortak diff ve test sonuçlarını tek kez ver. Dosya listesi uzunsa aynı kökü açıkça belirterek birkaç dosyayı bir satırda grupla; tam yollar korunmalı.

## Kabul kapısı

- Uygulayıcı değişen tam yolları, diff özetini, doğrulama komutunu **ve gerçek çıktısını** sunar. Çalıştırılmayan komut kanıt değildir.
- Uygulayandan farklı, taze bağlamlı kontrol ajanı yalnız hedef/kaynaklar/kabul ölçütleriyle başlar; iddia edilen sonucu dosyalardan ve kendi testinden çıkarır. Çağrısı da kota kapısından geçer.
- Kontrol sonucu `kabul`, `ret` veya `eksik kanıt` olur. Hatalı ölçütler ve komut çıktıları iliştirilir. Düzeltme geldiyse ilgili kabul ölçütleri yeniden doğrulanır.
- Log sessizliği veya süreç çıkışı tek başına başarılı teslim sayılmaz; açık kalanlar V3 göreviyle devredilir.
