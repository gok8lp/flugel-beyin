---
tur: proje
etiketler:
  - proje
  - siber-guvenlik
  - c
  - java
  - python
  - fastapi
  - react
  - sistem-programlama
durum: arsiv-beklemede
olusturma: 2026-11-11
guncelleme: 2026-11-11
---

# Siber Güvenlik Laboratuvarı ve Sistem Programlama Çalışmaları (C / Java)

> Üst bağlantı: [[HARITA]] · Odak: [[simdi]] · Bağlam: [[hafiza]] · Kararlar: [[kararlar]] · Sorumlu: [[kisiler/ahmet-gokalp-goksu]]

## Genel Bakış
Savunma odaklı siber güvenlik eğitim/laboratuvar prototipi (`cybersecurity-lab`) ile C ve Java dillerinde işletim sistemi süreç yönetimi (`fork`), eşzamanlılık (`Thread`/`synchronized`) ve algoritma pratiklerini içeren 6 depoluk çalışma kümesidir.

## Kapsanan Depolar

1. **`cybersecurity-lab`** (`https://github.com/gok8lp/cybersecurity-lab` — Açık, Python/FastAPI & React/Vite, Son Güncelleme: `2026-10-22T22:53:26Z`)
   - **Amaç:** Savunma odaklı siber güvenlik dersleri, dayanıklılık bulmacaları ve izole laboratuvar prototipi (saldırı aracı içermez).
   - **İçerik:** FastAPI + SQLModel arka ucu, HMAC tabanlı oturum bayrakları (flag), dar kapsamlı ve izin listeli (allowlist) runner, `linux-permission-leak` laboratuvarı, Kullanılabilirlik ve DoS savunma dersi (SYN cookie, hız sınırı, log patlaması, fail open/closed), toplam 6 öğretici ders, 17 bulmaca ve 20 güvenlik politikası testi.
   - **Güvenlik Temizliği:** `025edff` commit'i ile gerçek sunucu IP/alan adları örnek adreslerle değiştirilmiş ve `data/` dizini `.gitignore` içine alınmıştır.
2. **`c-process-tree`** (`https://github.com/gok8lp/c-process-tree` — Açık, C, Son Güncelleme: `2026-10-22T22:53:38Z`)
   - C ve POSIX `fork()` kullanarak ebeveyn/çocuk süreç ağacı oluşturma, süreçler arası dosya iletişimi ve çocuk süreç sonuçlarını toplama (`ab21c8a`) alıştırması.
3. **`java-producer-consumer`** (`https://github.com/gok8lp/java-producer-consumer` — Açık, Java, Son Güncelleme: `2026-10-22T22:53:42Z`)
   - Java `Thread`, `Runnable` ve `synchronized` yapı taşlarıyla klasik üretici-tüketici (producer-consumer) eşzamanlılık alıştırması.
4. **`c-calismalarim`** (`https://github.com/gok8lp/c-calismalarim` — Açık, C, Son Güncelleme: `2026-10-22T22:37:28Z`)
   - C programlama öğrenirken yapılan 1. hafta (`week1`) görevleri, başlık (`header`) dosyaları ve `Makefile` düzenlemeleri (`b75ee56`).
5. **`c-password-generator`** (`https://github.com/gok8lp/c-password-generator` — Açık, C, Son Güncelleme: `2026-10-22T22:53:55Z`)
   - C ile karakter grubu seçerek tekrar etmeyen rastgele dize üretme alıştırması (öğrenme amaçlıdır, üretim parola aracı değildir).
6. **`c-text-shuffler`** (`https://github.com/gok8lp/c-text-shuffler` — Açık, C, Son Güncelleme: `2026-10-22T22:53:52Z`)
   - Girilen metnin karakterlerini C ile rastgele sıralayan küçük algoritma projesi.

## Mevcut Durum (11 Kasım 2026)
- **Durum:** `arsiv-beklemede` (14 gün bayatlık kuralı gereği işaretlendi: tüm depoların son commit tarihi `2026-10-22` olup 20 gündür yeni commit almamıştır).
- Depoların dokümantasyonu, isimlendirmeleri ve gizlilik/güvenlik temizliği 22 Ekim 2026'da tamamlanarak kararlı öğrenme/portfolyo arşivi haline getirilmiştir.

## Sıradaki Adımlar
- [ ] Vize haftası sonrasında `cybersecurity-lab` için Faz 2 izole konteyner laboratuvar senaryolarını değerlendirmek.
- [ ] Eclipse CDT (`~/Documents/eclipse-workspace`) üzerinde yeni C/C++ projeleri açarken `Cross GCC` yerine `Linux GCC` araç takımını standart olarak kullanmak (bkz. [[dersler]]).

## Öne Çıkan Commit Geçmişi
- `cybersecurity-lab` — `d5f2a69` (2026-10-22): `docs: clarify cybersecurity lab and remove display branding`
- `cybersecurity-lab` — `025edff` (2026-10-18): Public yayın öncesi temizlik (örnek IP/alan adları, `data/` gitignore)
- `cybersecurity-lab` — `fb1329e` (2026-10-18): Savunma odaklı DoS dersi + 5 dayanıklılık bulmacası
- `cybersecurity-lab` — `b27d50c` (2026-10-18): Faz 1 iskelet (FastAPI/SQLModel, HMAC flag, dar runner, 20 güvenlik testi)
- `c-process-tree` — `ab21c8a` (2026-10-22): `refactor: name process exercise clearly and fix child result collection`
- `c-calismalarim` — `b75ee56` (2026-10-22): `week1: klasor duzeni, header dosyalari ve makefile duzenlemeleri`

## İlgili Sayfalar ve Bağlantılar
- **Harita ve Kök:** [[HARITA]] · [[simdi]] · [[hafiza]] · [[kararlar]] · [[dersler]]
- **İlgili Projeler ve Kişiler:** [[projeler/okul-guz-2026]] · [[kisiler/ahmet-gokalp-goksu]]
- **Wiki Sayfaları:**
  - [[wiki/repo-cybersecurity-lab]]
  - [[wiki/repo-c-process-tree]]
  - [[wiki/repo-c-password-generator]]
  - [[wiki/repo-c-text-shuffler]]
  - [[wiki/repo-c-calismalarim]]
  - [[wiki/repo-java-producer-consumer]]
  - [[wiki/github-repolar-katalogu]]
- **Bilgi Notları:**
  - [[flugelserver-genel-mimari]]

> Kaynaklar: `raw/github/00-github-envanteri.md`, `raw/github/01-tum-repolar-commit-gecmisi.md`, `raw/flugelserver/FLUGEL-OZET.md`
