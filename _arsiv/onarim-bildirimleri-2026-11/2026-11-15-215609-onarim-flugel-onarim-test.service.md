---
tur: onarim-raporu
olay_id: z1794768969
servis: service:flugel-onarim-test.service
durum: dogrulandi
acilis: 2026-11-15 21:56:09
kapanis: 2026-11-15 22:00:11
yapan: flugel-ariza-zinciri (tespit, dogrulama) + flugel-onarim (restart)
etiketler: [flugelserver, onarim, hermes]
---
# Onarım raporu: flugel-onarim-test.service

**Sonuç:** Restart sonrası servis sağlıklı; onarım doğrulandı.

## Zaman çizelgesi (TSİ)
- 2026-11-15 21:56:09 — Arıza tespit edildi (3 ardışık yoklama): systemd failed
- 2026-11-15 21:56:09 — Onarım kuyruğuna restart isteği bırakıldı.
- 2026-11-15 21:56:09 — flugel-onarim: restart başarılı.
- 2026-11-15 22:00:11 — Kapandı: Restart sonrası servis sağlıklı; onarım doğrulandı.

## Ayrıntı
- Arıza belirtisi: systemd failed
- Uygulanan adım: restart (flugel-onarim)
- Doğrulama: 3 ardışık sağlıklı yoklama (systemd ok)
- Dosya değişikliği: yok (yalnız yeniden başlatma). Yetki ve sınırlar: `/usr/local/sbin/flugel-onarim`.
