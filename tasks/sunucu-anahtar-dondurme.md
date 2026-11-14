---
{
  "id": "sunucu-anahtar-dondurme",
  "status": "done",
  "owner": "Gökalp",
  "updated_at": "2026-11-15",
  "created_at": "2026-11-14",
  "kind": "task",
  "revision": 2,
  "facts": {
    "sonuc": "3 anahtar 2026-11-15 01:06-01:09 döndürüldü (Ollama, Guacamole SSH + DB, tsidp OIDC). Eski Guacamole anahtarı SSH'ta reddediliyor; tsidp JWKS yeni kid 7683704046407132635.",
    "rapor": "~/Documents/ai_workplace/second-brain/raporlar/anahtar-dondurme-2026-11-15.md",
    "yedek": "flugelserver:/root/yedek-anahtar-donusumu-20261114-220644/",
    "acik": "Eski Ollama anahtarı ollama.com hesabına eklenmişse oradan silinmeli (doğrulanmadı)."
  }
}
---
# Sunucu özel anahtarlarını döndür

2026-11-15 derin taramada sır maskelemesi 3 özel anahtarı kaçırdı ve bunlar Codex (OpenAI) ve Gemini (Google) lane'lerine gitti:
- `/opt/stacks/tsidp/data/oidc-key.json` (tsidp OIDC imzalama anahtarı)
- `/opt/stacks/guacamole/keys/server-ed25519`
- `/srv/appdata/ollama/id_ed25519`

Yapılacak: her anahtarı yeniden üret, servisi yeniden başlat, eski anahtara güvenen yerleri güncelle. Sunucuda değişiklik olduğu için Gökalp onayı gerekir. Maskeleme düzeltildi (sunucu_indeks.py, test 15/15).
