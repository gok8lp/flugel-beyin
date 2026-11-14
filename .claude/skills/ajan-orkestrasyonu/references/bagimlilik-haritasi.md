# Bağımlılık haritası

2026-11-14 kullanıcı envanteri; aşağıdaki zincirler görevde sağlanmıştır. Bu belge kurulum veya canlı erişim kanıtı değildir. Uçtan uca çalışma, çözülmüş symlink hedefleri ve servis sağlığı bu görevde **doğrulanmadı**. Durdurma, taşıma veya eşitleme öncesi ilgili zinciri salt okunur kontrol et; etkisi belirsiz ortak servisi durdurma.

| Zincir | Bilinen ilişki | Canlı doğrulama / etki |
|---|---|---|
| `beyin-esitle` → sunucu bare repo → `/opt/stacks/hermes/beyin` | Kullanıcının verdiği eşitleme yolu | Bare repo tam yolu, taşıma yöntemi, çalışan tüketiciler: **doğrulanmadı** |
| `ai-limitler` → `codexbar` | Kota kararının veri bağımlılığı | Önbellek yaşı ve sağlayıcı verisinin canlı doğruluğu: **doğrulanmadı** |
| Skill symlink zinciri (aşağıda) | Kullanıcının verdiği ortak kaynak ilişkisi | Her linkin gerçek hedefi ve sağlığı: **doğrulanmadı** |

```text
~/.claude/skills ────────┐
~/.codex/skills ─────────┤
~/.gemini/config/skills ─┼→ ai_workplace/.agents/skills
~/.claude-canalp/skills ─┘              ↓
                           flugel-beyin/.agents/skills
```

`.claude/skills` ve `.kiro` kopyalarının bu göreve ait eşitlemesini lider yapar; bu belge eşitleme yetkisi vermez. Hermes, özel hub, Context7, embedding servisi veya çok kipli indeks yalnız benzer işlev anlatılıyor diye kurulu sayılmaz.

## Yeni bağımlılık kaydı şablonu

```text
Bileşen / tam yol:
Doğrudan bağımlılıklar (A → B = A, B'ye ihtiyaç duyar):
Tüketiciler / etkilenecek lane'ler:
Kaynak ve tarihi (kullanıcı beyanı / dosya:satır / komut çıktısı):
Doğrulama durumu: doğrulandı <kanıt> / doğrulanmadı <eksik>
Salt okunur kontrol komutu ve beklenen sonuç:
Durdurma/değişiklik etkisi, sorumlu ve yetki sınırı:
Geri dönüş / yeniden başlatma önkoşulu:
Sonraki kontrol:
```

Bilinmeyen düğümü hayali bir yolla doldurma; `doğrulanmadı` yaz. Eşitleme hatasını gidermeden önce zincirin hangi halkasının bozulduğunu belirle. Bağımlılık haritası ayrıca ağ erişimi veya sunucu değişikliği izni değildir.
