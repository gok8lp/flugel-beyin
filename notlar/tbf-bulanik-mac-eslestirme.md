# TBF Bulanık Maç ve Lig Eşleştirme Formülü

Bağlantılar: [[HARITA]] · [[dersler]] · [[tbf-eslestirme-algoritmasi]] · [[02 - TBF Maç ve Lig Eşleştirme Algoritması]] · [[2026-2027 Ankara Lig Eşleşme Tablosu]]

## Eşleştirme Özeti (`Eslestirme.kt`)
- TBF WebAPI'de (`get-all-matches-for-filter`) `assignr` `matchNumber` alanı yoktur ve takım/salon adları farklı yazılır.
- Aynı tarih (`matchDate.startsWith(assignr.date)`) ve aynı `tbfActivityId` içindeki adaylar arasında:
  - `s = 0.5 * (takimBenzerligi(teamA, home) + takimBenzerligi(teamB, away))`
  - `slot = (matchTime == time && salonAnahtari(salonAdi) == salonAnahtari(hall))`
  - `toplamPuan = s + (if (slot) 0.3 else 0.0)`
- Kabul koşulu: `s >= 0.70 || (slot && s >= 0.45)`.
- Doğrulama: `docs/samples/mac-eslesme-testi.json` üzerinde **188 / 192 maç (%97,91 isabet, 0 yanlış pozitif)**.
