# Son oturum

## 2026-11-15 19:44 · ev ağı entegrasyonu · f86c5534
- **Ne yaptık:** flugelserver uygulamaları NetMASTER modem ("Residential Gateway") üzerinden ev ağına entegre edildi: modem DNS → AdGuard, evde gokalpgoksu.com doğrudan HTTPS + `.ev` adları, Tailscale DNS → AdGuard, Mullvad HTTP proxy `:8889`, Wi-Fi (kanal 6 / 36, Airtime, PMF, misafir ağı), AdGuard Ebeveyn Denetimi kapalı, 13 eski Tailscale cihazı silindi. Ayrıntı: [[knowledge/concepts/ev-agi-ve-dis-erisim]].
- **Karar:** Funnel, Cloudflare ve Tailscale birlikte kalır; Funnel bilerek açık (mobil uygulamalar).
- **Karar:** +18 engeli kaldırıldı; Tailscale DNS AdGuard, yedek 1.1.1.1.
- **Belirsizlik:** AdGuard istemcileri 172.18.0.1 olarak görüyor; ileride tailnet DNS'i değişirse gokalpgoksu.com kuralları yeniden ele alınmalı.
- **Açık:** Cloudflare'de adguard A kaydı ve servissiz rotalar; Jev modu kararı.
- **Kaynak:** `~/Documents/ai_workplace/second-brain/raporlar/ev-agi-entegrasyon-2026-11-15.md`

Henüz bir çalışma sonucu kaydedilmedi. Anlamlı çalışma sonunda sonuç, gerekçe, açık kalan adım ve kaynak bağlantılarını `## YYYY-MM-DD HH:MM · <etiket> · <session_id[:8]>` başlığıyla buraya yaz. Tarih ve saati kartı yazdığın turdaki hook bağlamının `now=` değerinden al; o turda verilmediyse yerel sistem saatini oku, tahmin etme. Paralel oturumlarda yalnız kendi kartını düzenle, başka oturumların kartlarını ezme.
