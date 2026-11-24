# Son oturum

## 2026-11-24 02:30 · sunucu-hata-taramasi-ve-devops · 10f26676
- **Ne yaptık (Claude 1 / Opus 5.5 lider):** "Chrome çalışmıyor" kökü bulundu: AdGuard `ratelimit 20` bütün evi tek istemci sayıyordu (50 sorgudan 40'ı düşüyordu) → `ratelimit 0`. Gece yedeği 18 Kas'tan beri bozuktu (disk adları değişti, `/dev/sda3` sabit) → UUID ile düzeltildi, yeni snapshot alındı. Komga 43 saat kapalıydı (earlyoom öldürmüş) → `unless-stopped` + self-heal katman bekçisi. n8n↔Paperless ALLOWED_HOSTS, uyarı/gece birimleri, Subgen ölü portu, basket botu Türkçe tarih hatası (yeni atama bildirimi/sabah hatırlatması gitmiyordu; 12 test) düzeltildi. Çekirdek 7.0.0-44 + yeniden başlatma doğrulandı.
- **Kurulanlar:** IT/DevOps: Vaultwarden, BookStack, DevDocs, Excalidraw, DevOps Lab (yalıtık Docker + k3d/kind), Forgejo Actions runner (`ci-ornek` yeşil), Kod (C/C++ code-server + 25 GitHub deposu), Actual Budget (geri), Semaphore, RustFS S3, Healthchecks, Beszel, Vikunja, CyberChef, draw.io, Kroki, Swagger, Mailpit, Speedtest, Homebox, PairDrop, Linkding, Siber Lab (kendi deposu). Portal 55 uygulama ("IT ve DevOps" 21). 40+ yeni `*.gokalpgoksu.com` (FLUGEL kapısı); **Tailscale'den gelince kapı atlanır** (127.0.0.1:8198 + AdGuard 100.64.0.0/10).
- **Arka planda:** Gemini 3 hat (`~/Documents/ai_workplace/gemini-gelistirme`: duduk-server, basket-bot, akis; Flash High + Argon inceleme, 9 saat, kota bekçisi %80); sunucuya yükleme lider incelemesinden sonra.
- **Açık:** Canalp oturumu Gökalp açacak (`second-brain/DEVIR-canalp-duduk.md` tek proje; Rust devri `DEVIR-canalp-rust-yonetim.md` beklemede); yeni uygulamalarda ilk yönetici hesapları (Gökalp), Vaultwarden kaydını kapatma; Cloudflare panelinde eski tünel rotaları ve Portainer/Dockge/File Browser için Access önerisi; `/mnt/sidemain` %86; eski çekirdek 7.0.0-42; laptop/modem ikinci DNS'e Gökalp isteğiyle dokunulmadı.
- **Kaynak:** `~/Documents/ai_workplace/second-brain/raporlar/sunucu-hata-taramasi-2026-11-24.md`.

## Önceki oturumlar

Arşivlenen metin: `🔮 850-Companion/Arşiv/Last-Session-2026-11.md`
