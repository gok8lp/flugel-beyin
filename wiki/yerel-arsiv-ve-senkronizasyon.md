---
title: Yerel Arşiv, Birleştirme ve Bildirim Sistemi
sources: raw/devir.md, raw/build.md
updated: 2026-11-11
---

# Yerel Arşiv, Birleştirme ve Bildirim Sistemi

[[duduk-genel-bakis]] uygulamasında Room veya KSP kullanılmaz; tüm veriler atomik JSON dosyasında (`arsiv.json`) ve `DataStore` üzerinde saklanır.

> "Room, KSP ve Hilt eklenmeyecek. Veriler JSON dosyasında ve DataStore'da saklanacak." - raw/devir.md

> "WorkManager 2.10.5'te tutuldu (2.11+ bazı üretici API 34 cihazlarında açılışta çöküyor)." - raw/build.md

## Birleştirme ve Değişiklik Tespiti (`Birlestirici.kt`)

[[assignr-ve-ankarabasket-kaynaklari]] ve [[tbf-eslestirme-algoritmasi]] üzerinden gelen veriler `Birlestirici.birlestir` ile mevcut arşive hiçbir kaydı silmeden eklenir (`upsert`) ve şu olayları üretir:

1. `YENI_HAFTA`: Yeni atama haftası yayınlandığında.
2. `YENI_ATAMA`: Kullanıcının (`"AHMET GÖKALP GÖKSU"`) adını taşıyan yeni bir maç eklendiğinde.
3. `ATAMA_DEGISTI`: Kullanıcının maçında saat, salon veya görevli değiştiğinde.
4. `ATAMA_KALDIRILDI`: Aktif hafta içinde kullanıcının maçı listeden düştüğünde veya hakem listesinden çıkarıldığında.
5. `SKOR_GIRILDI`: Kullanıcının görev aldığı maça ilk kez skor yazıldığında.

## Hatırlatmalar ve Yeniden Başlatma

> "Telefon yeniden başlatılınca kontrol zamanlaması yeniden kurulsun." - raw/devir.md

`AcilisAlicisi` (`BOOT_COMPLETED` ve `MY_PACKAGE_REPLACED`) periyodik WorkManager işini yeniden kurar. `HatirlatmaHesaplayici` maçtan **1 gün (24 saat)** ve **2 saat** önce bildirim tetikler. Arşivlenen maçlar üzerinden [[hakem-ucret-tarifesi-2026-2027]] hesaplamaları yapılır ve [[android-arac-zinciri-ve-mimari]] arayüzünde gösterilir.
