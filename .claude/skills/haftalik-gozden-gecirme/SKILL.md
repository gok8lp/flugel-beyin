---
name: haftalik-gozden-gecirme
description: 5 adımlı haftalık ikinci beyin bakım becerisi (gelen-kutusu boşaltma, >14 gün bayat projeleri işaretleme, simdi.md yenileme, kararlar/dersler kontrolü ve HARITA.md kırık bağlantı onarımı).
tur: beceri
etiketler:
  - beceri
  - haftalik-gozden-gecirme
  - bakim
olusturma: 2026-11-11
guncelleme: 2026-11-11
---

# Haftalık Gözden Geçirme Becerisi (`/haftalik-gozden-gecirme`)

> Üst bağlantı: [[HARITA]] · Odak: [[simdi]] · Bağlam: [[hafiza]] · Kararlar: [[kararlar]] · Dersler: [[dersler]]

## Amaç
Vault'un dağınıklığını önlemek, bayatlayan projeleri yakalamak ve graf bağlantılarının bütünlüğünü korumak için her hafta düzenli olarak çalıştırılan 5 adımlı standart bakım akışıdır.

## 5 Adımlı Uygulama Akışı

### 1. `gelen-kutusu.md` Dosyasını Boşalt
- [[gelen-kutusu]] (`gelen-kutusu.md`) içindeki hızlı notları ve geçici maddeleri tek tek incele.
- Kalıcı bilgi içeren maddeleri [[kurallar/notlar]] standardına uygun olarak `notlar/` altında tek konulu yeni bir dosyaya taşı veya mevcut ilgili notu (`[[notlar/...]]`) güncelle.
- Görev niteliğindeki maddeleri ilgili proje sayfasındaki (`[[projeler/...]]`) **Sıradaki Adımlar** bölümüne veya [[simdi]] (`simdi.md`) içine aktar.
- İşlenen maddeleri `gelen-kutusu.md` içinden temizle.

### 2. 14 Günden Uzun Süredir Güncellenmeyen Projeleri İşaretle
- `projeler/` altındaki tüm proje dosyalarının ([[projeler/duduk]], [[projeler/flugel-manga]], [[projeler/okul-guz-2026]], [[projeler/hakemlik]], [[projeler/flugel-sunucu-ve-akis]], [[projeler/linux-masaustu-araclari]], [[projeler/siber-guvenlik-ve-sistem-lab]], [[projeler/web-portfolyo]]) `guncelleme` tarihini ve son commit/faaliyet tarihini kontrol et.
- [[kurallar/projeler]] uyarınca **14 günden uzun süredir (`>14 gün`)** güncellenmeyen projeleri tespit et, durumlarını raporla ve kullanıcı onayıyla `durum: arsiv-beklemede` olarak işaretle veya yeni bir sıradaki adım ekle.

### 3. `simdi.md` Odak Dosyasını Yenile
- [[simdi]] (`simdi.md`) içindeki tamamlanmış görevleri (`[x]`) arşivle veya ilgili proje sayfasına işle.
- Önümüzdeki haftanın önceliklerini (sınavlar, hakemlik maç atamaları, aktif geliştirme hedefleri) [[projeler/okul-guz-2026]], [[projeler/hakemlik]] ve [[projeler/duduk]] sayfalarından çekerek `simdi.md` dosyasını ve `wiki/hot.md` özetini yenile.

### 4. Yeni Kararları ve Dersleri Kontrol Et
- Hafta içinde alınan mimari/teknik kararların [[kararlar]] (`kararlar.md`) dosyasına tarih, karar, neden ve alternatifleriyle (bkz. [[sablonlar/karar]]) işlendiğini doğrula.
- Karşılaşılan hataların, tuzakların ve öğrenilen çözümlerin [[dersler]] (`dersler.md`) dosyasına kaydedildiğini kontrol et.

### 5. `HARITA.md` ve Vault Genelinde Kırık Bağlantıları Düzelt
- [[HARITA]] (`HARITA.md`) içindeki tüm `[[wikilink]]` referanslarını ve yeni eklenen `notlar/`, `projeler/`, `kisiler/`, `wiki/` sayfalarını karşılaştır.
- Haritada eksik kalan yeni dosyaları ilgili bölüme ekle.
- `python3 brain.py lint` komutunu çalıştırarak çözülmeyen `[[link]]` veya yetim sayfa (orphan page) kalmadığını doğrula.

## İlgili Sayfalar ve Bağlantılar
- **Kök ve Harita:** [[HARITA]] · [[simdi]] · [[gelen-kutusu]] · [[hafiza]] · [[kararlar]] · [[dersler]]
- **Kurallar ve Şablonlar:** [[kurallar/projeler]] · [[kurallar/notlar]] · [[kurallar/kisiler]] · [[kurallar/guvenlik]] · [[sablonlar/proje]] · [[sablonlar/karar]]
- **Wiki ve Notlar:** [[wiki/ikinci-beyin-sistemi]] · [[wiki/hot]] · [[wiki/index]] · [[notlar/flugelserver-mimari-ozeti]]

> Kaynak: `/home/flugel/Projects/prompt-obsidian-ikinci-beyin-sunucu.md`
