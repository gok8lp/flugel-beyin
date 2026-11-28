---
tur: sunucu-durum
guncelleme: 2026-11-28
otomatik: true
---
# flugelserver durumu

Bu dosya `flugel-durum-beyin` tarafından her gün yeniden yazılır; elle düzenleme.

Üretildi: 2026-11-28 08:30 TSİ · up 4 days, 7 hours, 7 minutes

**Özet:** 3 sorun: /mnt/side %90 dolu; /mnt/sidemain %94 dolu; flugel-yedek-kontrol.service başarısız

## Diskler
- `/`: 276G / 437G (66%)
- `/mnt/side`: 389G / 458G (90%) ⚠️
- `/mnt/sidemain`: 848G / 916G (94%) ⚠️

## Bellek
- RAM: 15399 MB toplam, 5718 MB kullanılabilir
- Swap: 2623 / 4095 MB kullanılıyor

## Yedek
- Son başarılı yedek: 2026-11-28 03:42 TSİ
- Son hata: yok

## Konteynerler
- Çalışan: 71 / 74
- İstek üzerine / bilerek kapalı:
  - `guac-db`: Exited (0) 29 hours ago
  - `guacamole`: Exited (143) 29 hours ago
  - `guacd`: Exited (0) 29 hours ago

## Başarısız systemd birimleri
- `flugel-yedek-kontrol.service`
