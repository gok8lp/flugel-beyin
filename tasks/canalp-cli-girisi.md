---
{
  "id": "canalp-cli-girisi",
  "status": "active",
  "owner": "Gökalp",
  "priority": "normal",
  "updated_at": "2026-11-14",
  "created_at": "2026-11-14",
  "kind": "task",
  "revision": 1
}
---
# Canalp (Claude 2) CLI girişi

Gökalp yapacak (giriş kodunu ajan girmez). Gerekçe: `ai-limitler` Claude 2 kotasını `~/.claude-canalp` üzerinden okuyor; giriş olmadan kota görünmüyor ve Claude alt ajanları kota kapısından geçemiyor.

```bash
CLAUDE_CONFIG_DIR=~/.claude-canalp ~/.config/Claude-2/claude-code/2.1.321/ded331c1fbf8/claude /login
ai-limitler --yenile   # Claude 2 (Canalp) satırında yüzde görünmeli
```

Gökalp 2026-11-15'te "şimdi yapamam, sonra hatırlat" dedi. Ajanlar: oturum başında bu görev açıksa Gökalp'e bir kez hatırlat.
