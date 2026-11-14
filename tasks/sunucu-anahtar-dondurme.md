---
{
  "id": "sunucu-anahtar-dondurme",
  "status": "active",
  "owner": "Gökalp",
  "updated_at": "2026-11-14",
  "created_at": "2026-11-14",
  "kind": "task",
  "revision": 1
}
---
# Sunucu özel anahtarlarını döndür

2026-11-15 derin taramada sır maskelemesi 3 özel anahtarı kaçırdı ve bunlar Codex (OpenAI) ve Gemini (Google) lane'lerine gitti:
- `/opt/stacks/tsidp/data/oidc-key.json` (tsidp OIDC imzalama anahtarı)
- `/opt/stacks/guacamole/keys/server-ed25519`
- `/srv/appdata/ollama/id_ed25519`

Yapılacak: her anahtarı yeniden üret, servisi yeniden başlat, eski anahtara güvenen yerleri güncelle. Sunucuda değişiklik olduğu için Gökalp onayı gerekir. Maskeleme düzeltildi (sunucu_indeks.py, test 15/15).
