# Kullanıcının düzeltmeleri

Açık kullanıcı düzeltmelerini tarihiyle, her kuralı bir iki satırda kaydet; uzun gerekçe ve olayın anlatımı ayrı bir nota gider. Tek bir projeye ya da alana ait kural `projects/<proje>/Kurallar.md` (şablonda `🏰 300-Projects/<proje>/Kurallar.md`) dosyasına gider, burada yalnız `[kapsam: <proje>]` etiketli tek satırlık işaretçi kalır. Geçici istekleri kalıcı kurala dönüştürme.

## Her işte geçerli kurallar
2026-11-14'te [[hafiza]] dosyasından taşındı (kaynak tarihleri 2026-11-11 – 2026-11-14).

- Her zaman Türkçe konuş.
- Doğrulanmamış şeye "çalışıyor" deme. Her iş sonunda derleme/test doğrulanır ve git commit atılır.
- Parola, token, `.env`, `local.properties` (özellikle `/home/flugel/Projects/koharia-reader/local.properties`), SSH anahtarı veya çerezler **asla** okunmaz, sohbete yazılmaz ve vault'a/git'e kaydedilmez. Ayrıntı: [[kurallar/guvenlik]].
- `raw/` klasörü salt okunurdur; mevcut insan notları yerinde korunur, yeni kalıcı bilgi `knowledge/`, işler `tasks/`, odak `🔮 850-Companion/Threads.md`, hızlı notlar V3 Yakala (`📥 000-Inbox/Yakala`) içinde tutulur. Kaynak bağlantıları ve değişiklikler doğrulanır; eski wiki lint kaldırılmıştır.
- sudo (2026-11-14): Bu PC'de sudo var; ajanlar sudo'yu yalnız kullanıcı görev için açıkça izin verdiğinde kullanır. Yedek / geri dönüş / rapor kuralları: `~/Documents/ai_workplace/AGENTS.md`.

## Proje kuralları (işaretçiler)
- [kapsam: flugel-sunucu-ve-akis] Sunucu ve sanal makine işinde önce [[projeler/flugel-sunucu-ve-akis]] içindeki "Kurallar" bölümünü oku (W11 / W11-GPU).
