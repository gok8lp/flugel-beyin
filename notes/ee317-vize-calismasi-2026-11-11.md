---
tur: not
etiketler:
  - okul
  - ee317
  - guc-elektronigi
  - vize
olusturma: 2026-11-11
guncelleme: 2026-11-11
---

# EE317 Güç Elektroniği I — vize çalışması (11 Kasım 2026 gecesi)

Bağlantılar: [[HARITA]] · [[claude-hafizasi]] · [[hafiza]]

## Sınav
- **Vize:** Perşembe 12 Kasım 2026, 09:00 (taslak programa göre D6–D8 salonları). Hoca: Doç. Dr. Seyfettin Vadi.
- **Kapsam (kesin):** 4 slayt dosyası, sonuna kadar — D1 diyotlar, D2 yarım dalga, D3 tam dalga, D4 üç faz köprü. **Tristör işlenmedi, kapsam dışı.** Kaynak: sınıf arkadaşıyla WhatsApp yazışması ("o zaman 4'ün sonuna kadar"); resmi duyuru görülmedi.
- Arkadaşın tavsiyesi: "grafiklere iyi çalış", "soruları çöz".

## Dosyalar
- Kök: `/home/flugel/Downloads/Taildrop/EE317_Guc_Elektronigi_1/`
- Hocanın slaytları: `Ders_Slaytlari/1_…diyotlar.pdf`, `2_EE317_YDD.pdf`, `3_EE317_TDD.pdf`, `4_EE317_3faz_TDD.pdf`
- Soru haritası (H01–H10 ve çözüm denetimi): `Calisma_Seti/EE317_Soru_Haritasi_ve_Ders_Devri.md`
- Ortak çalışma (Claude + Codex + Antigravity): `Ortak_Calisma/` — plan `YOL_HARITASI.md` (v5 = slayt sırası), ilerleme `ILERLEME.md`
- **Codex rehberi (sabah tekrarı için tek dosya):** `Ortak_Calisma/gorseller/EE317_Calisma_Rehberi_Yeni.pdf` — 160 sayfa, hocanın slaytları + not şeridi + H01–H10 açıklamalı çözümleri. Sayfa eşlemesi: `Ortak_Calisma/gorseller/yeni_baski/sayfa_haritasi.json`
- Eski ana PDF (arşiv): `Ortak_Calisma/gorseller/EE317_Ana_Calisma.pdf`

## Hocanın soruları (konum)
| Soru | Konu | Slayt |
|---|---|---|
| H01 | Yarım dalga R | D2 s.7 (çözüm 8–11; s.8'deki 53,36 V hatalı, doğrusu 54,02 V) |
| H02 | Yarım dalga RL | D2 s.20 |
| H03 | Serbest dönüşüm diyodu | D2 s.33 |
| H04 | C filtre | D2 s.42 |
| H05 | R+E | D2 s.49 |
| H06 | RLE | D2 s.54 |
| H07 | Tam dalga RL | D3 s.13 |
| H08 | Tam dalga C | D3 s.21 |
| H09 | Üç faz köprü R | D4 s.27 |
| H10 | Üç faz köprü RL | D4 s.31 |

## İlerleme (Claude günceller)
- 17:00 — D1 (diyotlar) tamamı işlendi: anahtar sınıfları, ideal/gerçek diyot, ters toparlanma, 4 diyot türü (genel amaçlı / hızlı / FRD / Schottky), kayıplar.
- 18:00 — D2 parça 2.1 (s.3–6: yarım dalga R, ortalama, RMS, güç) anlatılıyor; anlaşıldığı henüz teyit edilmedi. Sırada H01 (s.7–11).
- 18:09 — Ekran iki pencereye geçti (solda D2 slaytı, sağda Codex rehberi s.22); Claude belleği Obsidian'a aktarıldı. Öğrenci hâlâ D2 parça 2.1a (s.3); anlaşıldı teyidi bekleniyor.

## Sabah tekrarı (öneri)
1. Rehberin içindekiler sayfasından H01–H10'un çözüm sayfalarına bak.
2. Her devre için: hangi diyot ne zaman iletir → vo, io, vD grafiği → Vort, Vrms → P, PF → PIV.
3. Formül tuzakları: güç RMS ile; yarım dalga Vrms = Vm/2; üç faz 1,35 çarpanı hat-hat RMS için; R+E'de kesimde vo = E.
