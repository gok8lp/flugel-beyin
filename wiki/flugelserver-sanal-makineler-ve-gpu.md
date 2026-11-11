---
title: flugelserver Sanal Makineler (W11 / W11-GPU) ve GTX 1660 Ti Passthrough
sources: raw/flugelserver/05-SANAL-MAKINELER.txt, raw/flugelserver/WINDOWS.md, raw/yerel-ai/SANAL-MAKINELER.md, raw/yerel-ai/UZAK-MASAUSTU.md
updated: 2026-11-11
---

# flugelserver Sanal Makineler (W11 / W11-GPU) ve GTX 1660 Ti Passthrough

Bağlı Sayfalar: [[flugelserver-genel-mimari]] · [[flugelserver-docker-uygulamalari]] · [[pc-masaustu-hyprland-ve-gnome-araclari]]

> "SANAL MAKİNELER (20 Ekim 2026)" - raw/flugelserver/05-SANAL-MAKINELER.txt

> "Kullanıcının PC'si — sunucu entegrasyonu" - raw/flugelserver/WINDOWS.md

## Sanal Makineler Rehberi (`05-SANAL-MAKINELER.txt`)
```
SANAL MAKİNELER (20 Ekim 2026)
=============================

VM'ler
  W11-GPU     Windows 11, 8 vCPU, 4 GB, GTX 1660 Ti doğrudan VM'ye verilir. Disk: /var/lib/libvirt/images/w11
  W11         Windows 11, 4 vCPU, 4 GB, GPU'suz. AYNI disk (w11). W11-GPU açıkken açılamaz (ve tersi).
  mullvad-ts  Linux, 4 vCPU, 4 GB. Disk: mullvad-ts.qcow2

Açılış: YALNIZ SİZ İSTEYİNCE
  Sunucu açılışında hiçbir VM otomatik başlamaz (autostart kapalı).
  Aç:  sudo vm ac W11-GPU        Kapat:  sudo vm kapat W11-GPU        Durum:  sudo vm durum
  (Cockpit'ten de açılabilir: https://flugelserver.tail42f1f4.ts.net:39443)

10 dakika kuralı (vm-bosta-kapat.timer, her dakika)
  Kullanım belirtisi = dakikada ≥256 KiB ağ trafiği (Moonlight/RDP/indirme) VEYA ≥32 MiB disk okuma/yazma VEYA bağlı VNC/konsol.
  10 dakika boyunca hiçbiri yoksa → Windows'a guc dugmesi (ACPI) ile TEMİZ KAPATMA istenir.
  5 dk içinde kapanmazsa ikinci istek; 8 dk sonra hâlâ açık ve TAMAMEN etkinliksizse (donmuş) zorla kapatılır + Telegram bildirimi.
  Kapanış sırasında disk yazıyorsa (güncelleme kuruluyor olabilir) zorlanmaz; 30 dk sonra bildirim gider.
  CPU bilerek sayılmaz: donmuş Windows bir çekirdeği boşa döndürür.
  Ayarlar: /etc/vm-yonetim.conf (BOSTA_DAKIKA, eşikler, MUAF listesi). Kayıt: /var/log/vm-yonetim.log
  İlk gerçek test (19.10 23:08–23:16): W11-GPU 18 Ekim'den beri donmuştu; iki ACPI isteğine yanıt vermedi, zorla kapatıldı,
  GPU sunucuya geri döndü, GPU uygulamaları (ollama, plex, immich ML, subgen) sağlıklı başladı, ardından ilk yedek alındı.

Windows'ta "kaydet ve kapat" (hazırda bekletme) neden yok?
  GPU doğrudan VM'ye verildiği için libvirt'in kaydet/geri yükle özelliği güvenilir değil; Windows'un kendi hazırda bekletmesi için
  VM'de QEMU konuk ajanı gerekir (şu an yok). Bu yüzden temiz kapatma seçildi. Açık belgeleri Windows kapanırken kaydetmez.

Geri dönüş yedekleri (en fazla 2): bkz. 04-YEDEKLER.txt bölüm 2.

GPU döngüsü (/etc/libvirt/hooks/qemu)
  W11-GPU başlarken: ollama, plex, immich_machine_learning, subgen durdurulur → kart vfio-pci'ye verilir.
  W11-GPU kapanınca: kart nvidia'ya döner → bu uygulamalar yeniden başlar. Jellyfin CPU modunda; GPU'dan bağımsız.
  Kanca ayrıca: W11/W11-GPU çakışmasını engeller; VM açılırken süren yedeği/eşitlemeyi durdurur (sizin isteğiniz önceliklidir);
  VM kapanınca vm-kapandi@<VM>.service ile yedek + proje eşitlemeyi başlatır; Moonlight portlarını yönlendirir.

Eclipse projeleri → sunucu (/srv/project)
  Windows C: BitLocker ile şifreli (anahtar VM'nin TPM'inde) → sunucu Windows diskini okuyamaz. Bu yüzden eşitlemeyi Windows yapar:
   1. VM içinde \\192.168.122.1\project\windows\eclipse-esitle-kur.ps1 dosyasını bir kez çalıştırın (Samba kullanıcısı: flugel).
   2. Her 15 dk ve oturum açılışında C:\Users\<siz>\eclipse-workspace → /srv/project/gelen/<BİLGİSAYAR>/<alan> (robocopy /MIR).
   3. Sunucu her gece 02:30'da değişiklik varsa /srv/project/surumler/<tarih> sürümü alır (hardlink, en fazla 30).
  Durum: kurulum betiği hazır; Windows tarafında HENÜZ ÇALIŞTIRILMADI (VM içinde sizin yapmanız gerekir).

```
