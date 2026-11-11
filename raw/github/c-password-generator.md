# GitHub Repo: gok8lp/c-password-generator

- **URL:** https://github.com/gok8lp/c-password-generator
- **Görünürlük:** Açık (Public)
- **Ana Dil:** C
- **Son Güncelleme:** 2026-10-22T22:53:55Z
- **Açıklama:** C ile karakter grubu seçerek rastgele dize üretme alıştırması; üretim amaçlı parola aracı değildir.

## Dosya Ağacı (File Tree)
- `README.md` (blob)
- `password_generator.c` (blob)

## README İçeriği
# C Password Generator Exercise

C ile karakter grubu seçerek rastgele dize üretme alıştırması.
A beginner C exercise for generating strings from selectable character groups.

## Ne yapar?

Kullanıcıdan 8–16 uzunluk ve rakam/harf/sembol seçimi ister; seçilen gruptan karakterler üretir.
Eski depo adındaki "tekrar etmez" iddiası kodun davranışını yansıtmıyordu:
karakter seçiminde tekrar engellenmediği için aynı karakter birden fazla kez gelebilir.

## Derleme

```bash
gcc -std=c11 -Wall -Wextra password_generator.c -o password_generator
./password_generator
```

Kodda ilk öğrenme denemelerinden kalan uyarılar bulunabilir.

## Mevcut eksikler

Bu bir eğitim projesidir, güvenli parola üreticisi olarak sunulmaz.
`rand()`/zaman tabanlı tohumlama, eksik giriş doğrulaması ve bazı karakter havuzu ayırmalarında
sonlandırıcı için yer eksikliği vardır. Bazı seçim akışları ve tekrar üretimde seçenek sıfırlama da geliştirilmeye açıktır.
Gerçek hesap parolaları için kullanılmamalıdır.

## Öğrenilecekler

Fonksiyonlar, koşullar, diziler/stringler, karakter havuzları ve malloc/free kullanımı.
Kaynak kodun özgün öğrenme akışı korunmuştur; bu güncelleme tamamlanmış bir algoritma veya güvenlik düzeltmesi değildir.

