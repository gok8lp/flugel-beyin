---
{
  "kind": "fact",
  "title": "Paperless AI belge iş akışları",
  "project": "flugel-sunucu-ve-akis",
  "visibility": "internal"
}
---
# Paperless'ta AI belge iş akışları

[[projeler/flugel-sunucu-ve-akis]] · [[knowledge/sunucu-haritasi]]

## Uygulama senaryoları

| İstek | Ajanın yapacağı işlem | Kabul ölçütü |
|---|---|---|
| “Geçen ayın internet faturasını bul” | Paperless'ta tarih, gönderen ve belge türü ile ara. Birden çok yakın eşleşmede kısa aday listesi ver. | Doğru bir belge kimliği ve kullanıcının açabileceği bağlantı. |
| “Bu makbuzu arşivle” | İzinli gelen kutusundan dosyayı al. Aynı dosya özetini kontrol et, uygun belge türüne öner, Paperless içe aktarma işini izle. | Bir belge oluşur, OCR ve etiket sonucu doğrulanır. Yeniden deneme kopya oluşturmaz. |
| “Bu ay gelen sözleşmeleri göster” | Tarih ve belge türüne göre arayıp yalnız gerekli alanları özetle. | Başlık, kimlik ve tarih doğru, erişim bağlantısı çalışır. |
| “Son ödeme tarihi yaklaşan belgeler” | Tarih alanı kayıtlı belgeleri filtrele ve belge bağlantısıyla özetle. Tarihi belirsiz belgeleri açıkça ayır. | Yanlış kesin tarih üretilmez, her tarih kaynağına bağlanır. |
| Telegram'dan dosya isteme | Özel sohbette gönderen ve sohbet kimliklerini doğrula, Paperless veya Nextcloud aramasını isteğe göre kullan, sonuç dosyasını aynı yetkili sohbete gönder. | Yetkili istek doğru dosyayı alır, onaysız sohbet dosya alamaz. |
| Telegram'dan dosya alma | Dosya adını normalleştir. Belge içerikli dosyayı Nextcloud'da sınıflandır ve Paperless'a aktarım isteniyorsa mevcut içe aktarma işini kullandır. | Yol güvenli, dosya kopyalanmış, işlem sonucu ve hedef kaydedilmiş. |

## Ajanlar için veri sınırı

OCR ve indeksleme yerel Paperless'ta yapılır. Belgelerin ham içeriği, kimlik bilgileri ve erişim anahtarları model görevlerine, Telegram günlüklerine veya Beyin notlarına yazılmaz. Eylem kaydı belge kimliğini, zamanı, sonucu ve gerekli kaynak bağlantısını içerir. Bir dosyanın yerini değiştirmeden önce mevcut konumu ve aynı adlı hedefi doğrula.

## Durum — 2026-11-15

Bu sayfa kullanım sözleşmesini kaydeder. Telegram ve Nextcloud belge akışının uçtan uca kabul testi henüz yapılmadı. Hermes servis izleme görevi belge otomasyonundan bağımsızdır.

