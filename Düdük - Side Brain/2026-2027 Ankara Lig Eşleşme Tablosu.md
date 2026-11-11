---
title: "2026-2027 Ankara Lig Eşleşme Tablosu"
aliases:
  - "Lig Eşleşme Tablosu"
  - "Ankara Lig Kataloğu"
  - "lig-eslesme"
tags:
  - duduk
  - referans
  - lig-eslesme
  - tbf
  - ankara
created: 2026-11-11
status: active
---

# 🏆 2026-2027 Ankara Lig ve Grup Eşleşme Tablosu

⬅️ **Üst Merkez:** [[00 - Ana Merkez (MOC)]]
➡️ **İlgili Modüller:** [[01 - Veri Kaynakları ve Tersine Mühendislik]] · [[02 - TBF Maç ve Lig Eşleştirme Algoritması]]

Kaynak veri: `/home/flugel/Projects/duduk/docs/samples/lig-eslesme.json` (**81 grup/lig satırı**: **59 `eslesti`**, **7 `kismi`**, **15 `eslesmedi`**; TBF Sezon ID: `174`).

---

## 🏛️ 1. TBF 2026-2027 Ankara Faaliyet Kataloğu (`filters-results`)

| TBF `faaliyetId` | TBF Faaliyet Adı | `assignr` Karşılığı (`league`) | Maç Kaydı | Puan Tablosu Grupları | Eşleşme Durumu |
|---|---|---|---|---|---|
| **`22320`** | Ankara Büyük Erkekler | `BÜYÜK ERKEK A` | 84 | 1 grup (`ANKARA BÜYÜK ERKEKLER A LİGİ`) | ✅ `eslesti` |
| **`22321`** | Ankara Büyük Kadınlar | `BÜYÜK KADIN` | 55 (tamamı tarihsiz, statü 19) | Boş (0 grup) | ⚠️ `kismi` |
| **`22322`–`22327`** | Ankara U10 / U11 / U12 Erkek & Kız | — (`AGL` özel turnuva olarak oynanıyor) | 0 | Boş | ❌ `eslesmedi` |
| **`22328`** | Ankara U14 Erkekler | `U 14 ERKEK A`, `U 14 ERKEK B`, `U 14 ERKEK C` | 488 | **22 grup** (A: 2, B: 8, C: 12) | ✅ `eslesti` |
| **`22329`** | Ankara U14 Kızlar | `U 14 KIZ A`, `U 14 KIZ B` | 125 | **5 grup** (A: 1 tek grup, B: 4 grup) | ✅ `eslesti` |
| **`22330`** | Ankara U16 Erkekler | `U 16 ERKEK A`, `U 16 ERKEK B`, `U 16 ERKEK C` | 356 | **16 grup** (A: 2, B: 8, C: 6) | ✅ `eslesti` |
| **`22331`** | Ankara U16 Kızlar | `U 16 KIZ A`, `U 16 KIZ` (B seviyesi) | 123 | **4 grup** (A: 1 tek grup, B: 3 grup) | ✅ `eslesti` |
| **`22332`** | Ankara U18 Erkekler | `U 18 ERKEK A`, `U 18 ERKEK B`, `U 18 ERKEK C` | 267 | **9 grup** (A: 1, B: 4, C: 4) | ✅ `eslesti` |
| **`22333`** | Ankara U18 Kızlar | `U 18 KIZ A`, `U 18 KIZ B` | 111 | **2 grup** (`U18 KIZ A LİGİ`, `U18 KIZ B LİGİ`) | ✅ `eslesti` |
| **`22334`, `22335`, `22337`** | U21 Erkek / U21 Kadın / Ümit Kadın | — | 0 | Boş | — |
| **`22336`** | Ankara Ümit Erkekler | `U 21 ERKEK` (Grup A, B) | 56 | Boş (`mac-header` içinde `U 21 ERKEK A GRUBU`) | ⚠️ `kismi` |
| **`23542`** | Ankara U16 Erkekler Seri A Ön Eleme | `U 16 ERKEK ÖN ELEME` (Grup A, B) | 19 | Boş (Ön eleme tamamlandı) | ⚠️ `kismi` |
| **`23543`** | Ankara U18 Erkekler Seri A Ön Eleme | `U 18 ERKEK ÖN ELEME` (Grup A, B) | 18 | Boş (Ön eleme tamamlandı) | ⚠️ `kismi` |

---

## ✅ 2. Tam Eşleşen (`eslesti`) 59 Lig / Grup Özeti (`BÖLGE`)

| `assignrLeague` | Seviye (`sev`) | Gruplar (`groupLetter`) | Grup Sayısı | TBF `faaliyetId` | TBF Grup Adı Kalıbı | Özel Not |
|---|---|---|---|---|---|---|
| `BÜYÜK ERKEK A` | `A` | `A` | 1 | `22320` | `ANKARA BÜYÜK ERKEKLER A LİGİ` | Tek grup; TBF adında grup harfi yok |
| `U 14 ERKEK A` | `A` | `A`, `B` | 2 | `22328` | `U 14 ERKEK A LİGİ <G> GRUBU` | — |
| `U 14 ERKEK B` | `B` | `A` .. `H` | 8 | `22328` | `U 14 ERKEK B LİGİ <G> GRUBU` | Kullanıcının 13 Kasım maçı (`F` grubu) burada |
| `U 14 ERKEK C` | `C` | `A` .. `L` | 12 | `22328` | `U 14 ERKEK C LİGİ <G> GRUBU` | — |
| `U 14 KIZ A` | `A` | `A` | 1 | `22329` | `U 14 KIZ A LİGİ GRUBU` | Tek grup; TBF adında `A GRUBU` harfi yok |
| `U 14 KIZ B` | `B` | `A` .. `D` | 4 | `22329` | `U 14 KIZ B LİGİ <G> GRUBU` | — |
| `U 16 ERKEK A` | `A` | `A`, `B` (`Grup A/B`) | 2 | `22330` | `U 16 ERKEK A LİGİ <G> GRUBU` | — |
| `U 16 ERKEK B` | `B` | `A` .. `H` | 8 | `22330` | `U 16 ERKEK B LİGİ <G> GRUBU` | — |
| `U 16 ERKEK C` | `C` | `A` .. `F` | 6 | `22330` | `U 16 ERKEK C LİGİ <G> GRUBU` | — |
| `U 16 KIZ A` | `A` | `A` | 1 | `22331` | `U16 KIZ A` | Tek grup; `U` ile `16` arasında boşluk yok |
| `U 16 KIZ` | `B` (çıkarım) | `A`, `B`, `C` | 3 | `22331` | `U 16 KIZ B LİGİ <G> GRUBU` | `season-teams`'te seviye harfsiz |
| `U 18 ERKEK A` | `A` | `A` (`Grup A`) | 1 | `22332` | `U 18 ERKEK A LİGİ A GRUBU` | — |
| `U 18 ERKEK B` | `B` | `A` .. `D` (`Grup A..D`) | 4 | `22332` | `U 18 ERKEK B LİGİ <G> GRUBU` | Kullanıcının 13 Kasım maçı (`ANK-U18E-B-2026-088`) burada |
| `U 18 ERKEK C` | `C` | `A` .. `D` (`Grup A..D`) | 4 | `22332` | `U 18 ERKEK C LİGİ <G> GRUBU` | `ANK-U18E-C-2026-070` maçında B↔C grup farkı |
| `U 18 KIZ A` | `A` | `A` | 1 | `22333` | `U18 KIZ A LİGİ` | Tek grup; TBF adında grup harfi yok |
| `U 18 KIZ B` | `B` | `A` | 1 | `22333` | `U18 KIZ B LİGİ` | Tek grup; TBF adında grup harfi yok |

---

## ⚠️ 3. Kısmi Eşleşen (`kismi`) 7 Lig / Grup (`BÖLGE`)

1. **`BÜYÜK KADIN` (Grup A)** → TBF `22321` (*Ankara Büyük Kadınlar*): 55 maç kaydının tamamı `matchStatusId = 19` (tarihsiz), puan tablosu boş.
2. **`U 16 ERKEK ÖN ELEME` (Grup A, B — 2 grup)** → TBF `23542` (*Ankara U16 Erkekler Seri A Ön Eleme*): 19 maç oynanmış, eleme turu olduğu için puan tablosu boş.
3. **`U 18 ERKEK ÖN ELEME` (Grup A, B — 2 grup)** → TBF `23543` (*Ankara U18 Erkekler Seri A Ön Eleme*): 18 maç oynanmış, puan tablosu boş.
4. **`U 21 ERKEK` (Grup A, B — 2 grup)** → TBF `22336` (*Ankara Ümit Erkekler*): 56 maç kaydı var, puan tablosu henüz boş.

---

## ❌ 4. Eşleşmeyen / Tanınmayan (`eslesmedi`) 15 Lig (`OKUL`, `AGL`, `ABL`, `AA`)

Bu 15 lig/turnuva resmi TBF yerel ligi (`BÖLGE`) olmadığı için TBF veya `ankarabasket.org.tr` üzerinde puan durumu ya da resmi skor API'si **bulunmamaktadır** (`DinamikLigKaydedici` tarafından `LigDurumu.TANINMAYAN` olarak işaretlenir):

| `matchType` | `assignrLeague` | `assignr` Maç Sayısı (2 Haftada) | Açıklama ve Kaynak Durumu |
|---|---|---|---|
| **`AA`** | `AA` (Grup `AA`) | 8 | **Anadolu Ajansı Turnuvası** (3x3 / kurum turnuvası); fikstür Google Sheet'te, skor API'si yok. |
| **`ABL`** | `ABL` (Grup `-`) | 2 | **SkorAltyapı Ankara Basketbol Ligi** (özel yetişkin ligi); fikstür Google Sheet'te, skor API'si yok. |
| **`AGL`** | `U10 ELİT`, `U10 PREMİUM`, `U10 SÜPER`<br>`U11 ELİT`, `U11 PREMİUM`, `U11 SÜPER`<br>`U12 ELİT`, `U12 PREMIUM`, `U12 SÜPER` (9 lig) | 22 | **Pizza Bulls Ankara Gelişim Ligi** (özel altyapı turnuvası); TBF `22322–22327` faaliyetleri boş, skor API'si yok. |
| **`OKUL`** | `GENÇ ERKEKLER A`, `GENÇ KIZLAR A`<br>`YILDIZ ERKEKLER`, `YILDIZ KIZLAR` (4 lig) | 31 | **MEB Okul Sporları** müsabakaları; fikstür OneDrive bültenlerinde, TBF/ankarabasket üzerinde puan ve skor yok. |
