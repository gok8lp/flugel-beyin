# Model tablosu (tek kaynak)

Tarih: 2026-11-26. Plan ya da model değişince yalnız bu dosya güncellenir; diğer skill'ler buraya bağlanır.
Her zaman önce `ai-limitler --sec <tur>`; betik bu tabloyla uyumludur.

## Şu an geçerli
| Sağlayıcı | Çalışan model | Not |
|---|---|---|
| Codex (`codex exec`) | `gpt-6-luna` (effort `low`/`medium`/`high`) | Hesap ChatGPT ücretsiz plan. `gpt-6.1-sol`, `gpt-6.1-terra`, `gpt-6-astra` "not supported" verir; plan yükselirse tabloyu güncelle. |
| Gemini (`agy --model`) | `gemini-4-hydrogen-high` | Alt ajan varsayılanı: ağır okuma/yazma. |
| Gemini | `gemini-4-hydrogen-medium` | Hafif iş. |
| Gemini | `gemini-4-argon` | Zor karar/hakem; haftalık limitli, idareli kullan. |
| Gemini | `gemini-3.8-flash-*` | Artık varsayılan değil. |
| Claude (`Agent` aracı) | `haiku`, `sonnet`, `opus`, `fable` | Claude limiti okunamıyorsa yalnız kısa iş ver. |

## Görev → model
| Görev | Model |
|---|---|
| Basit / okuma | Codex luna low ya da Gemini hydrogen-medium |
| Orta kod / test | Codex luna high ya da Claude sonnet |
| Ağır / mimari | Claude opus ya da Gemini argon |
| Kontrol | Uygulayandan farklı model |

Bilinmeyen model adı uydurma; liste: `agy models`, `~/.codex/models_cache.json`.
