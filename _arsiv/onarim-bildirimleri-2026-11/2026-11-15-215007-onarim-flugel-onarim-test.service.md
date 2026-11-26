---
tur: onarim-raporu
olay_id: z1794768607
servis: service:flugel-onarim-test.service
durum: basarisiz
acilis: 2026-11-15 21:50:07
kapanis: 2026-11-15 21:51:07
yapan: flugel-ariza-zinciri (tespit, dogrulama) + flugel-onarim (restart)
etiketler: [flugelserver, onarim, hermes]
---
# Onarım raporu: flugel-onarim-test.service

**Sonuç:** Onarım reddedildi/başarısız: ayni hedef icin 15 dk bekleme suresi

## Zaman çizelgesi (TSİ)
- 2026-11-15 21:50:07 — Arıza tespit edildi (3 ardışık yoklama): systemd failed
- 2026-11-15 21:50:07 — Onarım kuyruğuna restart isteği bırakıldı.
- 2026-11-15 21:51:07 — Kapandı: Onarım reddedildi/başarısız: ayni hedef icin 15 dk bekleme suresi

## Ayrıntı
- Arıza belirtisi: systemd failed
- Uygulanan adım: yok (yalnız bildirim)
- Doğrulama: -
- Dosya değişikliği: yok (yalnız yeniden başlatma). Yetki ve sınırlar: `/usr/local/sbin/flugel-onarim`.
