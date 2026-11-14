---
tur: harita
etiketler:
  - arsiv-sistemi
  - ikinci-beyin
  - kurallar
olusturma: 2026-11-14
guncelleme: 2026-11-14
---

# ARSIV-SISTEMI.md — Klasör Sistemi ve Dosyalama Kuralları

Bağlantılar: [[HARITA]] · [[CLAUDE]] · [[kurallar/notlar]] · [[kurallar/projeler]] · [[kurallar/kisiler]] · [[kurallar/guvenlik]]

> Bu vault Avenox Beyin V3 ile çalışır; PARA eşlemesi dosyalama rehberidir. Mevcut `projeler/`, `notlar/`, `kisiler/`, `kurallar/` adları ve `[[projeler/...]]` / `[[notlar/...]]` yol bağlantıları korunur; V3 ise companion, `tasks/`, `knowledge/`, `notes/` ve Yakala alanlarını kullanır. `brain.py`, `hud-uret.py` ve eski HUD arşivdedir; oturum bağlamını V3 hook’ları verir. Ayrıntılı içerik dizini için [[HARITA]] kullanılır; bu dosya yalnız *sistemi* tanımlar.

## 1. PARA Eşlemesi

| PARA katmanı | Bu vault'taki karşılığı | Amacı |
|---|---|---|
| Gelen kutusu | V3 Yakala (`📥 000-Inbox/Yakala`) | Tasnif edilmemiş hızlı not; Ctrl+Alt+B ile yakalanır, “yakalananları işle” ile işlenir |
| **P**rojeler | `projeler/`, `tasks/`, `🔮 850-Companion/Threads.md` | Hedefi ve bitişi olan projeler (Düdük, okul dönemi, sunucu, manga okuyucu…); somut işler `tasks/`, aktif odak Threads içinde |
| **A**lanlar | `kisiler/`, `🔮 850-Companion/Core.md`, `🔮 850-Companion/Kurallar.md`, `kurallar/` | Bitişi olmayan sürekli sorumluluklar: kimlik, cihazlar, kişiler, çalışma kuralları |
| **R**esources (Kaynaklar) | `notlar/`, `wiki/`, `raw/` | Konu notları, derlenmiş wiki ve salt okunur ham kaynaklar |
| **A**rşiv | `_arsiv/` | Aktif olmayan ama silinmeyen içerik |

## 2. Klasörler ve Kök Dosyalar

| Yol | Amacı | Dokunma kuralı |
|---|---|---|
| `CLAUDE.md` | Anayasa; oturum başında yüklenir | Kökte kalır, < 200 satır |
| `CLAUDE.local.md` | Yerel makine/sunucu yolları | Kökte kalır, git'e girmez |
| `HARITA.md` | İçerik dizini (her yeni dosya için bir satır) | Kökte kalır, `@import` edilir |
| `🔮 850-Companion/Threads.md`, `tasks/` | Aktif odak konuları ve yapılacak işler | Odak companion bağlamında yüklenir; işler `tasks/` içinde tutulur; kökteki `simdi.md` yalnız yönlendirmedir |
| `🔮 850-Companion/Core.md`, `🔮 850-Companion/Kurallar.md` | Kalıcı gerçekler, tercihler ve her işte geçerli kurallar | V3 hook’ları bağlamı verir; kökteki `hafiza.md` yalnız yönlendirmedir |
| `knowledge/kararlar.md` | Karar tablosu (tarih, karar, neden, alternatifler) | V3 kalıcı bilgi alanı; eski çekirdek `_arsiv/eski-sistem/cekirdek/*-eski.md` altında |
| `knowledge/dersler.md` | Öğrenilen dersler ve tuzaklar | V3 kalıcı bilgi alanı; eski çekirdek `_arsiv/eski-sistem/cekirdek/*-eski.md` altında |
| V3 Yakala (`📥 000-Inbox/Yakala`) | Hızlı not kuyruğu | Ctrl+Alt+B / “yakalananları işle”; kökteki `gelen-kutusu.md` yalnız yönlendirmedir |
| `ARSIV-SISTEMI.md` | Bu dosya: sistem ve dosyalama kuralları | Kökte kalır |
| `notlar/` | Tek konulu kişisel/teknik notlar (düz klasör, alt klasör yok) | [[kurallar/notlar]] |
| `projeler/` | Proje başına bir dosya (`projeler/<proje>.md`) | [[kurallar/projeler]] |
| `projeler/duduk-derin-referans/` | Düdük derin teknik referansı (eski `Düdük - Side Brain/`) | Dosya adları korunur (ad bazlı bağlantılar) |
| `kisiler/` | Kişi kartları | [[kurallar/kisiler]] |
| `kurallar/` | Yol kapsamlı kurallar | [[kurallar/guvenlik]] |
| `sablonlar/` | Not, proje, kişi, karar şablonları | [[sablonlar/not]] · [[sablonlar/proje]] · [[sablonlar/kisi]] · [[sablonlar/karar]] |
| `raw/` | Ham kaynaklar (`flugelserver/`, `github/`, `yerel-ai/` …) | **Salt okunur**; taşınmaz, yeniden adlandırılmaz (`.brain/manifest.json` yollara bağlı) |
| `wiki/` | `raw/`’dan derlenmiş eski kavram sayfaları | Mevcut referanslar korunur; wiki lint kaldırıldı, yeni kalıcı bilgi `knowledge/` içine kaynak bağlantısıyla yazılır |
| `_arsiv/eski/` | Birleştirilmiş eski İngilizce kök dosyalar (`map`, `memory`, `decisions`, `lessons`, `inbox`) ve Obsidian `Welcome.md` | Salt arşiv; yeni bilgi yazılmaz |
| Sistem | Aktif: `beyin.py`, V3 hook’ları, `.agents/`, `.claude/`, `.obsidian/`; arşiv: `brain.py`, `hud-uret.py`, `second-brain-hud.html`, eski `denetle`, `ingest`, `sorgu`, `haftalik-gozden-gecirme` skill’leri | Aktif V3 yolları korunur; eski sistem `_arsiv/eski-sistem/` altında yalnız referanstır |

## 3. Yeni Bilgi Nereye? (Karar Sırası)

1. Parola, token, `.env`, anahtar, çerez mi? → **Hiçbir yere yazılmaz**; yalnız yer gösterici ([[kurallar/guvenlik]]).
2. Henüz nereye ait olduğu belli değil mi? → V3 Yakala (`📥 000-Inbox/Yakala`) alanına tek madde; “yakalananları işle” ile tasnif et.
3. Bir karar mı ("X’i Y yerine seçtik, çünkü…")? → `knowledge/kararlar.md` tablosuna kaynak bağlantılı satır.
4. Bir hata/tuzak/ders mi? → `knowledge/dersler.md` ilgili bölümüne kaynak bağlantılı madde.
5. Bu hafta yapılacak iş mi? → `tasks/`; aktif odak → `🔮 850-Companion/Threads.md`; daha uzun vadeli adım ayrıca ilgili `projeler/<proje>.md` → *Sıradaki Adımlar* ile ilişkilendirilir.
6. Kalıcı kimlik/cihaz/sunucu gerçeği mi? → `🔮 850-Companion/Core.md`; her işte geçerli çalışma kuralı → `🔮 850-Companion/Kurallar.md`.
7. Bir kişi hakkında mı? → `kisiler/<ad-soyad>.md`.
8. Hedefi olan bir iş mi? → `projeler/<proje>.md` (yoksa [[sablonlar/proje]] ile aç).
9. Dış kaynak dökümü (sunucu çıktısı, PDF metni, depo README’si) mi? → Mevcut `raw/<alt-klasör>/` yalnız okunur; yeni kaynak V3 not/yakalama akışında saklanır, kaynak bağlantılı kalıcı sentez `knowledge/` içine yazılır. Eski `/ingest` kullanılmaz.
10. Kendi bilgin/özetin mi? → `notlar/<konu>.md` ([[sablonlar/not]]).
11. Artık güncel değil ama silinmemeli mi? → `_arsiv/` (gerekirse `_arsiv/<yil>/` alt klasörü) ve [[HARITA]]'daki satırı arşiv bölümüne taşı.

Her yeni kalıcı dosyadan sonra: [[HARITA]]'ya bir satır, dosyada en az bir ilgili nota ve `[[HARITA]]`'ya bağlantı.

## 4. İsimlendirme Kuralı

- Dosya adı içeriği anlatır; **küçük harf, tireli, Türkçe karaktersiz** (`ç→c, ğ→g, ı→i, ö→o, ş→s, ü→u`): `gazi-eem-vize-takvimi-ve-ders-notlari.md`. Asla `not-12.md`.
- Tarihe bağlı notlarda tarih sonda, ISO biçiminde: `ee317-vize-calismasi-2026-11-11.md`.
- Klasör adları Türkçe, küçük harf, numarasız. Yeni üst klasör açmadan önce bu dosya ve [[HARITA]] güncellenir.
- Dosya adları vault genelinde **benzersiz** tutulur (Obsidian ad bazlı çözer); bu sayede dosya taşımak bağlantı kırmaz.
- İstisna: `projeler/duduk-derin-referans/` içindeki eski başlık biçimli adlar (`00 - Düdük MOC (Ana Merkez).md` …) çok sayıda ad bazlı bağlantı nedeniyle korunmuştur.
- Yol bağlantılarında (`[[notlar/...]]`, `[[projeler/...]]`) klasör adı da yazılır; klasör yeniden adlandırılırsa bu bağlantılar toplu güncellenmelidir.

## 5. Arşivleme Kuralı

- Hiçbir not kalıcı silinmez; ya ilgili dosyayla **birleştirilir** ya da `_arsiv/` altına `git mv` ile taşınır.
- Birleştirmede kaybolacak benzersiz satır bırakılmaz; kaynak dosya arşive taşınır ve hedef dosyada "eski `X.md`'den birleştirildi" notu düşülür.
- `raw/` salt okunurdur; dosyaları model taşımaz, düzenlemez veya silmez. `wiki/` mevcut kaynak bağlantıları için korunur; eski `brain.py` / `.brain/manifest.json` bağımlılığı ve wiki lint artık aktif sistem kuralı değildir.
