---
name: beyin-bakim
description: Kullanıcı beyin bakımını yap dediğinde ya da oturum başında knowledge/beyin-bakim.md dosyasında açık soru veya ajan işi varken kullan; soruları kullanıcıya tek mesajda sorar, cevapları ilgili notlara işler.
---

# Beyin bakımı

Beyin her pazar kendi bayatlığını bulur (`beyin-bakim`, systemd timer) ve `knowledge/beyin-bakim.md` dosyasına yazar.

1. `beyin-bakim` çalıştır (taze liste üretir). `--kuru` dosya yazmadan gösterir.
2. "Gökalp'e sorular" bölümünü TEK mesajda numaralı sor. Gökalp ara soru sevmez; yalnız bu listeyi sor, başka soru ekleme.
3. Cevapları `python3 beyin.py note-read` / `note-edit` ile Threads, tasks ve proje notlarına işle. Görev durumu için `task-update` kullan ve expected revision ver.
4. "Ajan işleri" bölümünü kendin yap: dizinsiz raporu `knowledge/ai-workplace-raporlar.md` içine satır olarak ekle, gerçek kırık bağlantıyı düzelt, Inbox'u ayıkla.
5. `beyin-bakim` tekrar çalıştır; soru ve iş kalmadığını gör.
6. Receipt yaz (beyin.py receipt akışı); kritik iş ise `second-brain/raporlar/` raporu da yaz.

Kural: bu skill yalnız okur ve tek dosya üretir; düzeltmeler 3-4. adımda, notlara yapılır.
