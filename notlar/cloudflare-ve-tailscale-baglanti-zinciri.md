# Cloudflare Tunnel ve Tailscale Serve Bağlantı Zinciri

Bağlantılar: [[HARITA]] · [[hafiza]] · [[kararlar]] · [[CLAUDE.local]] · [[android-arac-zinciri-ve-mimari]] · [[05 - Android Mimari, Senkronizasyon, Bildirimler ve Arayüz]]

## 3 Kademeli Bağlantı Sırası (`Kaynaklar.kt` & `DudukDeposu.kt`)
1. **Cloudflare Tunnel (`duduk.gokalpgoksu.com`):**
   - `flugelserver` üzerindeki `cloudflared-akis.service` (`/etc/cloudflared/akis.yml`, yedek: `akis.yml.yedek-20261111-1728`) üzerinden `http://localhost:18420` adresine yönlendirilir.
   - Sağlık kontrolü: `https://duduk.gokalpgoksu.com/v1/health` (`200 OK`).
2. **Tailscale Serve (`flugelserver.tail42f1f4.ts.net:18443`):**
   - Tailnet içi HTTPS (`tailnet only`) üzerinden `http://127.0.0.1:18420` servisine bağlanır.
   - Sağlık kontrolü: `https://flugelserver.tail42f1f4.ts.net:18443/v1/health` (`200 OK`).
3. **Doğrudan Açık Kaynaklar:**
   - Sunuculara ulaşılamazsa uygulama doğrudan `assignr`, `ankarabasket` ve `TBF` uçlarından saniyede en fazla 1–2 istek (`HostHizSinirlayici(minAralikMs = 650L)`) atarak veriyi çeker.
