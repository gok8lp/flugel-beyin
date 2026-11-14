# Lane kartı (başlatmadan önce zorunlu)

Her bağımsız iş için bu kartı doldur. Boş sahiplik veya kabul ölçütüyle ajan başlatma.

```text
Lane adı: <benzersiz kısa ad>
Gönderen / neden: <lider, kullanıcı isteği>
Hedef: <tek, gözlenebilir sonuç>
Girdiler: <kaynak tam yolları, ilgili bölümler ve sürüm/tarih>
Çalışma dizini: <tam yol; dış proje kodu vault dışında>
OWNS: <yalnız yazılabilen tam dosya/klasör yolları>
DO-NOT-TOUCH: <yasak yollar; diğer lane'lerin dosyaları dahil>
Yalıtım: <tek yazıcı / izinli ayrı worktree; oluşturmayı kim yapar>
Bağımlılıklar: <önce bitmesi gereken lane veya doğrulanacak servis>
Kabul ölçütleri: <her biri komut ve beklenen davranışla ölçülebilir>
Model ve kota: <çağrıdan hemen önce ai-limitler --sec ... çıktısı>
Süre sınırı: <saniye; ilerleme kontrol aralığı ve durma koşulu>
Çalışma kimliği / PID: <filo.py baslat çıktısı>
Log / rapor: <tam yollar; izinli log dizini>
Teslim: <references/rapor-semasi.md; yaklaşık en çok 30 satır>
Kontrol ajanı: <uygulayandan farklı, taze bağlamlı ajan; ayrıca kota kapısı>
Devir: <süre/engel durumunda devir-sablonu.md ve V3 görevi>
```

- Başlatmadan önce OWNS kümelerini karşılaştır. Kesişen dosya varsa tek yazıcı seç; diğer lane salt okunur öneri üretir. Worktree kullanımı dosya sahipliği zorunluluğunu kaldırmaz.
- Başlangıç ve teslim dosya listelerini/diff özetini karşılaştır. Sınır dışı değişiklik kabulü durdurur; başka lane'in işini silerek düzeltme. Lider yeniden bölüştürür.
- Kapsam bitince dur; yeni iş üretme. Süre aşımı, erişim engeli veya kapsam değişikliği başarı değildir.
- Yetki zaten bu görev için açıkça verilmişse tekrar isteme; sandbox engelini başka ajan veya sağlayıcıyla aşma.
- **Dış modele veri göndermeden önce içerik sır taraması zorunlu.** Codex/Gemini'ye gidecek her paket, gönderimden önce `grep -E "PRIVATE KEY-----|\"d\"\s*:\s*\"[A-Za-z0-9_-]{16,}|(api[_-]?key|token|secret|password)\s*[:=]\s*[^*\s]"` gibi bir içerik taramasından geçer. Eşleşme varsa paket gönderilmez, maskelenir. Yalnız dosya adına dayalı sır tespiti yetmez (2026-11-15: `id_ed25519`, `oidc-key.json`, `server-ed25519` bu yüzden sızdı).
