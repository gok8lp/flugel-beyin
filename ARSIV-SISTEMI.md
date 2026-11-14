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

> Bu vault PARA mantığıyla düzenlenir, ama klasör adları `CLAUDE.md`, `brain.py`, `hud-uret.py`, hook'lar ve `[[projeler/...]]` / `[[notlar/...]]` biçimindeki yol bağlantıları onlara bağlı olduğu için **numarasız ve Türkçe** kalır. Ayrıntılı içerik dizini için [[HARITA]] kullanılır; bu dosya yalnız *sistemi* tanımlar.

## 1. PARA Eşlemesi

| PARA katmanı | Bu vault'taki karşılığı | Amacı |
|---|---|---|
| Gelen kutusu | `gelen-kutusu.md` | Tasnif edilmemiş hızlı not; haftalık gözden geçirmede boşaltılır |
| **P**rojeler | `projeler/` | Hedefi ve bitişi olan işler (Düdük, okul dönemi, sunucu, manga okuyucu…) |
| **A**lanlar | `kisiler/`, `hafiza.md`, `kurallar/` | Bitişi olmayan sürekli sorumluluklar: kimlik, cihazlar, kişiler, çalışma kuralları |
| **R**esources (Kaynaklar) | `notlar/`, `wiki/`, `raw/` | Konu notları, derlenmiş wiki ve salt okunur ham kaynaklar |
| **A**rşiv | `_arsiv/` | Aktif olmayan ama silinmeyen içerik |

## 2. Klasörler ve Kök Dosyalar

| Yol | Amacı | Dokunma kuralı |
|---|---|---|
| `CLAUDE.md` | Anayasa; oturum başında yüklenir | Kökte kalır, < 200 satır |
| `CLAUDE.local.md` | Yerel makine/sunucu yolları | Kökte kalır, git'e girmez |
| `HARITA.md` | İçerik dizini (her yeni dosya için bir satır) | Kökte kalır, `@import` edilir |
| `simdi.md` | Bu haftanın odağı | Kökte kalır, `@import` edilir |
| `hafiza.md` | Kalıcı gerçekler ve tercihler | Kökte kalır, `@import` edilir |
| `kararlar.md` | Karar tablosu (tarih, karar, neden, alternatifler) | Kökte kalır, `@import` edilir |
| `dersler.md` | Öğrenilen dersler ve tuzaklar | Kökte kalır |
| `gelen-kutusu.md` | Hızlı not kuyruğu | Kökte kalır |
| `ARSIV-SISTEMI.md` | Bu dosya: sistem ve dosyalama kuralları | Kökte kalır |
| `notlar/` | Tek konulu kişisel/teknik notlar (düz klasör, alt klasör yok) | [[kurallar/notlar]] |
| `projeler/` | Proje başına bir dosya (`projeler/<proje>.md`) | [[kurallar/projeler]] |
| `projeler/duduk-derin-referans/` | Düdük derin teknik referansı (eski `Düdük - Side Brain/`) | Dosya adları korunur (ad bazlı bağlantılar) |
| `kisiler/` | Kişi kartları | [[kurallar/kisiler]] |
| `kurallar/` | Yol kapsamlı kurallar | [[kurallar/guvenlik]] |
| `sablonlar/` | Not, proje, kişi, karar şablonları | [[sablonlar/not]] · [[sablonlar/proje]] · [[sablonlar/kisi]] · [[sablonlar/karar]] |
| `raw/` | Ham kaynaklar (`flugelserver/`, `github/`, `yerel-ai/` …) | **Salt okunur**; taşınmaz, yeniden adlandırılmaz (`.brain/manifest.json` yollara bağlı) |
| `wiki/` | `raw/`'dan derlenen kavram sayfaları | Düz klasör; her düzenlemeden sonra `python3 brain.py lint` = `0 problem(s)` |
| `_arsiv/eski/` | Birleştirilmiş eski İngilizce kök dosyalar (`map`, `memory`, `decisions`, `lessons`, `inbox`) ve Obsidian `Welcome.md` | Salt arşiv; yeni bilgi yazılmaz |
| Sistem | `brain.py`, `hud-uret.py`, `second-brain-hud.html`, `.brain/`, `.claude/`, `.obsidian/` | Kökte kalır; yollar betiklere sabit kodlu |

## 3. Yeni Bilgi Nereye? (Karar Sırası)

1. Parola, token, `.env`, anahtar, çerez mi? → **Hiçbir yere yazılmaz**; yalnız yer gösterici ([[kurallar/guvenlik]]).
2. Henüz nereye ait olduğu belli değil mi? → `gelen-kutusu.md`'ye tek madde.
3. Bir karar mı ("X'i Y yerine seçtik, çünkü…")? → `kararlar.md` tablosuna satır.
4. Bir hata/tuzak/ders mi? → `dersler.md` ilgili bölümüne madde.
5. Bu hafta yapılacak iş mi? → `simdi.md`; daha uzun vadeli adım ise ilgili `projeler/<proje>.md` → *Sıradaki Adımlar*.
6. Kalıcı kimlik/cihaz/sunucu gerçeği mi? → `hafiza.md` (200 satır sınırı).
7. Bir kişi hakkında mı? → `kisiler/<ad-soyad>.md`.
8. Hedefi olan bir iş mi? → `projeler/<proje>.md` (yoksa [[sablonlar/proje]] ile aç).
9. Dış kaynak dökümü (sunucu çıktısı, PDF metni, depo README'si) mi? → `raw/<alt-klasör>/` + `/ingest` ile `wiki/` sayfası.
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
- `raw/` ve `wiki/` dosyaları arşive taşınmaz (`brain.py` ve `.brain/manifest.json` yollarına bağlıdır).
