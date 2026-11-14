---
tur: not
etiketler:
  - ikinci-beyin
  - avenox
  - yapay-zeka
olusturma: 2026-11-14
guncelleme: 2026-11-14
---

# Avenox İkinci Beyin serisi: öğrenimler ve kurulum özeti

Bağlantılar: [[HARITA]] · [[kararlar]] · [[ikinci-beyin-sistemi]] · [[hafiza]]

## Kaynak videolar (Avenox, YouTube)
1. Tek komutla ikinci beyin ([İsim]OS), V1: https://www.youtube.com/watch?v=a-vO-Re4UqY
2. 130 gündür kendi hafızasını yazıyor, V2: https://www.youtube.com/watch?v=sRCTOxc4658
3. İkinci Beyin V3 kurulumu: https://www.youtube.com/watch?v=NpzqWvKR_iw
4. Jev ile güncelleme: https://www.youtube.com/watch?v=EY_ta3P9fQc

Transkriptler alınamadı (YouTube IP engeli, 2026-11-14). Notlar video açıklamaları ve resmi belgelerden çıkarıldı. Ayrıntılı çalışma dosyaları vault dışında: `~/Documents/ai_workplace/second-brain/` (her video için `NOTLAR.md`, `OGRENIMLER.md`, `DERS-KITABI.md`, `TERIMLER.md`, `AVENOXBEYIN-NASIL-CALISIR.md`, `raporlar/`).

## On ilke
1. Hafıza modelde değil dosyada; Markdown tek doğruluk kaynağı.
2. Ajanı dosya sistemi erişimiyle (Claude Code) kullan; sohbet penceresi hafızayı yönetemez.
3. Yazmayı otomatiğe al ama denetlenebilir tut (V2 akşam derleyicisi V3'te kaldırıldı).
4. Her hatıranın kaynağı olmalı; kaynaksız bilgi potansiyel halüsinasyondur.
5. Kaydet → yeni oturumda geri sor; doğrulamadan "çalışıyor" deme.
6. Bağlam kalitesi miktardan önemli.
7. Deterministik iş kodda, yargı modelde; model yazma/onay yetkisi almaz.
8. Yeni bileşeni önce gölgede ölç (off → shadow → on).
9. Gizlilik katmanlı: `private`, `remote_allowed: false`; anahtarlar ortam değişkeninde ya da `env_file`'da.
10. Resmi paket + checksum + `--plan` + yedek + rollback.

## Bu vault'ta yapılanlar (2026-11-14)
- Avenox V3.13.0 kuruldu; eski `session-start.sh` emekliye ayrıldı; `raw/`, `brain.py`, `post-wiki-edit.sh` korundu ([[kararlar]]).
- `_arsiv` aramadan çıkarıldı (`preferences --index-exclude-dir _arsiv`).
- Hassas notlara `remote_allowed: false` eklendi; `.beyin-projects.json` ile proje kapsamı (`duduk`, `shared_unscoped`).
- Jev gölge modda; anahtar `~/.config/beyin/typesafe.env` dosyasında (600 izin, vault dışında). İlk testte "hakemlere ne kadar para veriliyor" sorusunda kelime araması alakasız notlar getirdi, Jev doğru üç notu seçti.
- Yakala kısayolu: Hyprland `Ctrl+Alt+B` (`~/.config/hypr/user.lua`); `tk` paketi gerekiyor.

## Açık konular
- Jev'i bir hafta gölgede ölçüp `jev on` kararı.
- Global köprü (`~/Projects`) kurulumu Gökalp'te.
- Codex ve Antigravity güven onayı.
- İleride: flugelserver Ollama ile yerel anlam araması (Jev alternatifi).
