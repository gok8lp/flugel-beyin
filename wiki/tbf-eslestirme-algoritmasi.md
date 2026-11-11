---
title: TBF Maç ve Lig Eşleştirme Algoritması
sources: raw/veri-kaynaklari.md, raw/devir.md
updated: 2026-11-11
---

# TBF Maç ve Lig Eşleştirme Algoritması

[[assignr-ve-ankarabasket-kaynaklari]] içinde belirtildiği üzere TBF WebAPI yanıtlarında `assignr` `matchNumber` alanı bulunmaz. Bu nedenle [[duduk-genel-bakis]] uygulaması bulanık eşleştirme algoritması kullanır.

> "Skorlar 1-2 gün gecikmeli geliyor ve matchNumber yok; maçlar dokümanın 5. bölümündeki algoritmayla eşleştirilmeli. Denemede isabet %97,9, yanlış eşleşme 0 çıktı." - raw/devir.md

## Algoritma Adımları (`Eslestirme.kt` ve `Normalizasyon.kt`)

1. **Türkçe Karakter Katlama (`katla`):** `İ/ı/i -> I` ve `ÇĞÖŞÜÂÎÛ -> CGOSUAIU`.
2. **Salon Anahtarı (`salonAnahtari`):** `SPOR`, `SALONU`, `KOMPLEKSI`, `ANKARA`, `BESEVLER` sözcükleri atılır.
3. **Takım Anahtarı (`takimAnahtari`):** Sondaki `(A)`/`(B)` takım eki ayrılır; `SK`, `SPOR`, `KULUBU`, `GSK` gibi durak sözcükler çıkarılır; `GB -> GLOBAL BASKETBALL` ve `BASKETBOL -> BASKETBALL` eş안lamlıları uygulanır.
4. **Ratcliff/Obershelp (`SequenceMatcher`) Benzerliği + Slot Ödülü:**
   - İki takımın ortalama benzerliği `s = 0.5 * (sim(teamA, home) + sim(teamB, away))`
   - Saat ve salon anahtarı aynıysa (`slot == true`) `+0.3` ödül eklenir (`sc = s + 0.3`).
   - Kabul eşiği: `s >= 0.70` veya (`slot == true` ve `s >= 0.45`).

## Dinamik Lig Yapısı

> "lig listesi sabit kodlanmayacak. Yeni bir lig, grup veya hafta gelirse uygulama kendiliğinden eklesin. Eşleşmeyen lig adları ayrı bir "tanınmayan" listesinde görünsün." - raw/devir.md

Eşleşen skorlar [[yerel-arsiv-ve-senkronizasyon]] katmanındaki `Arsiv` kayıtlarına yazılır.
