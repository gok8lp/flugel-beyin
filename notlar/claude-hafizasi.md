---
tur: not
etiketler:
  - claude
  - hafiza
  - calisma-tercihleri
olusturma: 2026-11-11
guncelleme: 2026-11-11
kaynak: /home/flugel/.claude/projects/-home-flugel-Documents/memory/
---

# Claude hafızası (aktarım)

Bağlantılar: [[HARITA]] · [[hafiza]] · [[dersler]] · [[ee317-vize-calismasi-2026-11-11]]

Bu not, Claude Code'un `~/Documents` projesindeki otomatik belleğinin (`memory/`) Obsidian'a aktarılmış kopyasıdır. Claude yeni bir bellek yazdığında buraya da ekler. Sistem envanteri (PC + flugelserver, 28 Ekim 2026 tarihli) ayrıca `~/.claude/knowledge/flugel-sistem/` altındadır; kopyalanmadı, sunucu bilgisi zaten [[hafiza]] ve `wiki/` içinde.

## 1. Ders çalışma tercihleri (feedback · 11 Kasım 2026)
- Her konu adımı **önce konu, sonra soru** sırasıyla işlenir.
- Hocanın slaytları **sayfa sırasıyla** izlenir; kendi sıralamayla "karışık" gidilmez.
- **Bir konu anlaşılmadan diğerine geçilmez.** Her parçadan sonra "anladın mı?" sorulur, cevap gelmeden yeni konuya/soruya geçilmez.
- Her adımın başında kısa **DEFTERE** kutusu (en fazla ~6 madde) ve **ÇİZ:** satırı verilir; kullanıcı anlatılanları deftere yazarak ilerliyor.
- Formüller sohbette düz metin olarak değil, **düzgün dizilmiş** (KaTeX) gösterilir.
- Devre ve grafikler mümkünse **ekranda** (Okular) gösterilir; token tasarrufu sağlar. Ekranda iki pencere: solda hocanın orijinal slaytı, sağda Codex'in hazırladığı PDF.
- Ara aritmetik sınavı istemiyor; genel formül → yerine koyma → sonuç biçiminde doğrudan çözüm tercih ediyor.

**Neden:** EE317 vize gecesi (11 Kasım 2026) kullanıcı bu tercihleri açıkça ve tekrar tekrar belirtti.

## 2. Claude–Codex ortak klasör düzeni (proje)
- Ders çalışmalarında Claude, Codex (ChatGPT masaüstü uygulaması) ve bazen Antigravity (Gemini) `<Ders>/Ortak_Calisma/` klasöründe dosyayla haberleşir.
- Dosyalar: `CLAUDE_DAN_CODEX_E.md` (CL-xxx), `CODEX_TEN_CLAUDE_A.md` (CX-xxx), `ANTIGRAVITY_DAN.md` (AG-xxx) — yalnız sona ekleme; `BASLANGIC.md`, `YOL_HARITASI.md`, `ILERLEME.md`; `EKRANDA_AC.json` + `ekran_izleyici.py` (Okular'da iki pencere açar).
- Örnekler: EE319 Lab (10 Kasım 2026), EE317 (11 Kasım 2026).
- Roller: Codex görsel/PDF üretimi ve sayısal doğrulama; Claude anlatım ve kontrol.

**Ders (çakışma):** 11 Kasım'da `YOL_HARITASI.md` iki ajan tarafından üst üste yazıldı. Ortak dosyalara yalnız sona bölüm eklenir, yazmadan hemen önce yeniden okunur. Kullanıcıya iç iletişim uzun anlatılmaz, derse odaklanılır.

**Ders (ekran):** Okular `--unique` ile açılan pencereler kapanmıştı ve "açtım" denen sayfalar görünmüyordu. Açma komutunun gönderilmesi pencerenin görünür olduğunu kanıtlamaz; `hyprctl clients -j` ile doğrulanmalı.

## 3. Obsidian aynası (feedback · 11 Kasım 2026)
- Kullanıcı Claude belleğinin bu kasaya da yazılmasını istedi. Claude yeni bellek yazınca bu nota ekler; ders/iş ilerlemesini ilgili nota (ör. [[ee317-vize-calismasi-2026-11-11]]) işler. Kasa kurallarına uyar (yalnız ekleme, HARITA satırı, lint).
