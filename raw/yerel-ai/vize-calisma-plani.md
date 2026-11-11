# 2026-2027 Güz vize çalışma planı (EEM, Gazi TF)

Hazırlanma: 31 Ekim 2026. Kaynaklar: OBS ders programı ekran görüntüsü (30 Ekim) ve fakültenin 16 Ekim tarihli **taslak** ara sınav programı. Final sürüm yayımlanmadı. Duyuruya göre 23 Ekim'den sonra değişiklik yapılmayacak.

## 1. Sınav takvimi (senin şubelerin)

| Tarih | Saat | Ders | Şube / Hoca | Salon |
|---|---|---|---|---|
| Cmt 7.11 | 13:30 | EE215 Elektromanyetik Alan Teorisi | 2 – Erol Kurt | D5-D8 |
| Cmt 7.11 | 15:00 | EE333 Endüstriyel Otomasyon Sistemleri | 1 – Mahir Dursun | D3 |
| Pzt 9.11 | 09:00 | EE313 Elektrik Makinaları 1 | 3 – Orhan Kaplan | D6 |
| Pzt 9.11 | 15:00 | EE315 Elektrik Makinaları Lab 1 | 5 – Orhan Kaplan | D4 |
| Sal 10.11 | 09:00 | İSG302 İş Sağlığı ve Güvenliği 2 | 1 – Seyfettin Vadi | – |
| Sal 10.11 | 12:00 | EE346 Mesleki Yazılım Uyg. ⚠ | Ayşe Demirhan | D5 |
| Çar 11.11 | 09:00 | EE319 Güç Elektroniği Lab 1 | 1 – Erdal Bekiroğlu | D6 |
| Per 12.11 | 09:00 | EE317 Güç Elektroniği 1 | 3 – Seyfettin Vadi | D6-D8 |

⚠ EE346 taslakta iki kez geçiyor: Sal 10.11 12:00 (D5) ve Per 12.11 18:00 (D5, D8). Hangisi geçerli, hocaya veya bölüme sor.

## 2. Kaynak durumu (31.10 15:00 güncellemesi: GUZEM indirildi, Taildrop derslere göre klasörlendi)

| Ders | Elindeki kaynak | Durum |
|---|---|---|
| EE333 Otomasyon | "Kumanda Teknikleri ve PLC" kitabından 23 sayfa fotoğraf (kumanda soruları, PLC, zamanlayıcı, sayıcı, karşılaştırma, RTC, analog, PTO/PWM) | 🟠 Konu listesi ve soru var. Hocanın slaytları hâlâ yok |
| EE346 Mesleki Yazılım | GUZEM'den 6 sunum: MATLAB diziler, string, fonksiyonlar, nargin/nargout, if-else | 🟢 Yeterli. Pratik için MATLAB veya Octave kullan |
| EE315 / EE319 Lab | GUZEM'den tüm deney föyleri, değerlendirme kriterleri ve simülatörler | 🟢 Yeterli |
| EE215 EM Alan | Cheng (TR çeviri, taranmış, 512 s.), el yazısı notlar ve ödev | 🟠 Çözümlü soru kaynağı zayıf. Öneri: Schaum's Electromagnetics (Edminister) veya hocanın eski vize soruları |
| EE317 Güç Elk. | 9 slayt + konu anlatımı/formül özeti | 🟡 Slaytlarda çözümlü örnek az. Sen (2014) kitabındaki doğrultucu bölümü ek soru kaynağı olabilir |
| EE313 Makinalar | Chapman 4. baskı ve çözümleri, Sen, Andebili DC soru kitabı, Kaplan 4-5. hafta slaytları | 🟢 Yeterli |
| İSG302 | Yok | ⚪ Düşük öncelik, ders notu yeter |

## 3. Matematiksel model

**Talep (gereken saat).** Her ders için ağırlık `w = Zorluk (1-5) × Hazırlık açığı (1-5)`. Kaynağı olmayan dersin açığı yüksek tutuldu.

| Ders | Z | A | w | Saat ≈ w × 68/75 |
|---|---|---|---|---|
| EE215 | 5 | 4 | 20 | 18 |
| EE333 | 3 | 4 | 12 | 11 → 13.5** |
| EE313 | 4 | 3 | 12 | 11 |
| EE317 | 4 | 3 | 12 | 11 |
| EE346 | 2 | 3 | 6 | 5.5 → 3* |
| EE315 | 2 | 2 | 4 | 3.5 |
| EE319 | 2 | 2 | 4 | 3.5 |
| İSG302 | 1 | 2 | 2 | 2 |

**Kapasite (OBS ders saatleri düşülmüş varsayım).** Cmt 5, Paz 8, Pzt 5, Sal 3, Çar 8, Per 3, Cum 3, 7.11 sabahı 3 saat. Sınav haftasında sınav aralarına göre toplam ≈ **68 saat**. Ders saatleri dışındaki gerçek boş vaktine göre bu sayıları değiştir; yöntem aynı kalır.

**Kural 1 – En erken teslim önce (EDF) uygulanabilirlik koşulu.** Her sınav tarihi `d` için şu koşul sağlanmalı: `Σ(o tarihe kadarki sınavların talebi) ≤ o tarihe kadarki kapasite`.

| Sınav anına kadar | Kümülatif talep | Kümülatif kapasite | Boşluk |
|---|---|---|---|
| 7.11 13:30 (EE215+EE333) | 31.5 | 38 | +6.5 |
| 9.11 09:00 (+EE313) | 42.5 | 49 | +6.5 |
| 9.11 15:00 (+EE315) | 46 | 52 | +6 |
| 10.11 12:00 (+İSG, EE346) | 51 | 56 | +5 |
| 11.11 09:00 (+EE319) | 54.5 | 61 | +6.5 |
| 12.11 09:00 (+EE317) | 65.5 | 68 | **+2.5** ← en dar |

**Sonuç.** En dar pencere EE317'de. Bu yüzden ilk haftadaki 6.5 saatlik boşluk **EE317 ve EE313'e önceden yüklenir**. Son günlere iş yığmak matematiksel olarak riskli; bir gün kaybedersen plan çöker.

**Kural 2 – Aralıklı tekrar.** Her ders en az iki ayrı günde çalışılır. Son tekrar sınavdan önceki 24 saat içinde yapılır. Sınav sabahı yalnız formül kâğıdı ve 2-3 soru.

**Kural 3 – Serpiştirme.** Günde en çok 2-3 ders, 50 dk çalışma + 10 dk mola blokları. Zor ders (EE215) günün ilk bloğuna konur.

\* EE346 içeriği artık belli (MATLAB temel programlama, 6 sunum). 3 saat yeterli; pratik ağırlıklı çalış. Sınav 12.11 18:00 çıkarsa 11.11 akşamına +1 saat ekle.

\*\* EE333'ün açığı kaynak bulununca 5'ten 4'e indi (w = 12, ≈ 11 saat). Takvim yine 13.5 saatte bırakıldı: kitap sayfaları çok sayıda ladder sorusu içeriyor ve aradaki 2.5 saatlik fark ilk sınava kadarki boşluk içinde kalıyor (31.5 ≤ 38).

## 4. Gün gün, konu konu plan

### Cmt 31.10 – 5 sa
- **EE215 (3 sa):** Vektör analizi. Kartezyen/silindirik/küresel koordinatlar; gradyan, diverjans, rotasyonel; diverjans ve Stokes teoremleri (Cheng Böl. 2, notların s. "Vektör Analizi").
- **EE333 (2 sa):** Kaynak edinme (sınıf grubu, hoca). Otomasyon temelleri; röle, kontaktör ve buton sembolleri.

### Paz 1.11 – 8 sa
- **EE215 (3.5 sa):** Coulomb yasası, nokta/çizgi/yüzey yük dağılımlarının E alanı, Gauss yasası (Cheng 3.1-3.4). Ödev Q2-Q3'ü tekrar çöz.
- **EE333 (3 sa):** Sensörler (endüktif, kapasitif, optik, limit switch). Kumanda devreleri: mühürleme, kilitleme, yön değiştirme.
- **EE317 (1.5 sa):** Ortalama/RMS, tepe değer, faz. İdeal diyot, diyot türleri, ters toparlanma, kayıplar (formül özeti §1-2, slayt 1 ve 9).

### Pzt 2.11 – 5 sa
- **EE215 (3 sa):** Elektrik potansiyeli V, iş `W = Q·V_AB`. İletken/dielektrik, sınır koşulları, `R = L/(σS)`. Poisson/Laplace denklemleri.
- **EE333 (2 sa):** PLC yapısı, giriş-çıkış, tarama çevrimi, ladder temel komutları (NO/NC, bobin, set/reset).

### Sal 3.11 – 3 sa
- **EE215 (2 sa):** Biot-Savart; Ampère yasası (sonsuz tel, koaksiyel kablo: ödev Q5), solenoid ve toroid alanı.
- **EE333 (1 sa):** Zamanlayıcı (TON/TOF) ve sayıcı ladder örnekleri.

### Çar 4.11 – 8 sa
- **EE215 (3 sa):** Lorentz kuvveti `F = q(E + v×B)`, akım taşıyan tele kuvvet `dF = I dl×B`, manyetik enerji `W = ½LI²`, endüktans, Maxwell denklemleri tablosu.
- **EE333 (3 sa):** Ladder soru çözümü: start-stop, yön değiştirme, yıldız-üçgen, sayıcılı uygulama. Müfredatta varsa pnömatik.
- **EE317 (2 sa):** Yarım dalga doğrultucu R ve R-L; serbest dolaşım diyodu (özet §3-5, slayt 2).

### Per 5.11 – 3 sa
- **EE215 (2 sa):** Karma deneme, süre tutarak 4-5 soru (Cheng örnekleri ve notlar).
- **EE313 (1 sa):** Manyetik devreler: relüktans, B-H eğrisi, histerezis ve girdap kayıpları (Chapman Böl. 1).

### Cum 6.11 – 3 sa
- **EE215 (1.5 sa):** Yanlış yaptığın sorular. Tek sayfa formül kâğıdı.
- **EE333 (1.5 sa):** Sembol ve komut özeti, karma soru.

### Cmt 7.11 – sabah 3 sa → 13:30 EE215, 15:00 EE333
- Sabah: **EE215** formül kâğıdı + 2 soru (1.5 sa), **EE333** özet (1 sa), mola.
- Akşam (3 sa) **EE313:** Elektromekanik dönüşüm ve lineer makine. DA makine temelleri: dönen çerçevede endüklenen gerilim, `Ea = Kφω`, `τ = KφIa`, komütasyon, armatür reaksiyonu (Kaplan 4. hafta, Chapman Böl. 8).

### Paz 8.11 – 8 sa
- **EE313 (6 sa):** DA generatörler: yabancı uyartımlı, şönt (gerilim oluşumu, mıknatıslanma eğrisi), seri, kompund. Güç akışı, kayıplar, verim (Kaplan 4-5. hafta, Chapman Böl. 9). Soru kaynağı: Chapman çözümleri ve Andebili. Ödevdeki güç akışı sorularını tekrar çöz.
- **EE315 (2 sa):** DA makine deney föyleri: boşta ve yükte karakteristikler, ölçüm bağlantıları.

### Pzt 9.11 → 09:00 EE313, 15:00 EE315
- 10:30-14:30: **EE315** (1.5 sa) tekrar.
- Akşam (3 sa): **İSG302** (1.5 sa), **EE346** (1.5 sa).

### Sal 10.11 → 09:00 İSG302, 12:00 EE346
- 10:30-11:30: **EE346** son tekrar.
- Akşam (5 sa): **EE319** (2 sa) doğrultucu deney föyleri; EE317 ile aynı konular. **EE317** (3 sa) tam dalga doğrultucu R ve R-L, C filtre, Fourier (özet §8-9, slayt 3).

### Çar 11.11 → 09:00 EE319
- 10:30 sonrası (7 sa) **EE317:** 3 faz altı darbeli köprü (özet §10, slayt 4); kontrollü doğrultucular: yarım dalga, tam dalga, 3 faz (slayt 5-7); çok darbeli doğrultucular (slayt 8). Son 1.5 saat karma soru ve formül kâğıdı.

### Per 12.11 → 09:00 EE317
- Sabah yalnız formül kâğıdı.

## 5. Hemen yapılacaklar
1. EE333: Elindeki kitap sayfalarındaki SORULAR bölümlerini çöz. Hocanın slaytları bulunursa konu listesini karşılaştır.
2. EE346'nın sınav günü: hoca veya bölüm (10.11 12:00 mı, 12.11 18:00 mı?).
3. EE215 için eski vize soruları veya Schaum's.
4. EE313 ve EE317 için GUZEM boş; derste paylaşılan ek materyal varsa sınıf grubundan iste.

Dosyaların yeri: `~/Downloads/Taildrop/<ders klasörü>`. Ayrıntılı döküm: `~/Downloads/Taildrop/DERSLER-BILGI.md`.
