---
title: "agy (Gemini Hydrogen) başsız modda izinler"
type: concept
updated: 2026-11-15
---
# agy (Gemini Hydrogen) başsız modda izinler

- `agy -p` başsız (headless) modda izin soramaz; ajan kabuk komutu (`command`) ya da izinsiz bir klasörde `read_file` isterse sessizce reddedilir ve "no output produced" ile biter. Bazen dosyayı yazdıktan sonra durur (yazma gerçekleşmiş olabilir; logdan değil dosyadan kontrol et).
- `--settings` ile `command(ls*)` gibi izin kalıpları vermek 2026-11-15'te işe yaramadı.
- İşe yarayan yöntem: gereken dosya listesi ve içerik özetini lider önceden çıkarıp prompt'a gömer, ajana "komut çalıştırma, sadece yaz" der; `--mode accept-edits`. Kasa dışı klasör için `--add-dir` ve `read_file(*)` izni gerekir.
- Mullvad uygulaması bağlıyken, Mullvad'dan hariç tutulmuş Claude süreçlerinden başlatılan `agy` ağa çıkamıyor (yanıt vermiyor). VPN kapalıyken Hydrogen yanıtı ~40 sn.

Kaynak: sen, sohbette, 2026-11-15; `second-brain/raporlar/beyin-onarim-2026-11-15.md`. Üst harita: [[knowledge/index]]
