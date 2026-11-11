# CLAUDE.md — İkinci Beyin Anayasası (< 200 Satır)

@HARITA.md
@simdi.md
@hafiza.md
@kararlar.md

---

## 1. Bilgiler Nerede Durur (`where things live`)
- **`HARITA.md`** ([[HARITA]]): En üst giriş noktası. Her bilgi türünün hangi klasörde/dosyada yaşadığını gösterir.
- **`simdi.md`** ([[simdi]]): Bu hafta odaktaki aktif işler ve sıradaki adımlar.
- **`hafiza.md`** ([[hafiza]]): Kalıcı tercihler, cihazlar, sunucu ve kimlik gerçekleri.
- **`kararlar.md`** ([[kararlar]]): Tarih, karar, neden ve alternatifler.
- **`dersler.md`** ([[dersler]]): Öğrenilen teknik dersler ve hatalar.
- **`gelen-kutusu.md`** ([[gelen-kutusu]]): Hızlı notlar; haftalık gözden geçirmede uygun yere taşınır.
- **`notlar/`**: Kişisel ve teknik bilgi notları (her dosyada tek konu).
- **`kisiler/`**: Kişi kartları (rol, sorumluluk alanı, iletişim yolu, ilgili projeler).
- **`projeler/`**: Her projede durum, sıradaki adım ve bağlantılar.
- **`kurallar/`**: Yol kapsamlı kurallar (`kurallar/kisiler.md`, `kurallar/projeler.md`, `kurallar/notlar.md`, `kurallar/guvenlik.md`).
- **`sablonlar/`**: Kişi, proje, karar ve not için Obsidian şablonları (`sablonlar/*.md`).
- **`raw/`**: Ham kaynaklar. Model yalnızca okur, **asla düzenlemez** (`Edit(/raw/**)` yasaklı).
- **`wiki/`**: `raw/` kaynaklarından derlenen kavram sayfaları (`title`, `sources`, `updated` frontmatter + `> "birebir metin" - raw/<dosya>` alıntı satırı zorunlu).
- **`wiki/hot.md`**: En fazla ~15 satırlık sıcak bağlam önbelleği.
- **`wiki/index.md`**: `python3 brain.py index` ile otomatik üretilen wiki indeksi.

## 2. Nasıl Cevap Verilir (`how to answer`)
1. Önce `HARITA.md` ve `wiki/hot.md` dosyalarına bak; cevabı haritanın gösterdiği dosyadan ver ve dosya adını açıkça belirt.
2. Her iddianın altına kaynağını yaz: dosya yolu (`notlar/...`, `wiki/...`, `raw/...`) ya da `"sen, sohbette, <tarih>"`.
3. Hiçbir dosya konuyu kapsamıyorsa **"kayıtlı değil"** de, tahminle boşluk doldurma.
4. Yeni bilgi kalıcıysa:
   - Tek konulu yeni dosya aç veya ilgili dosyayı güncelle,
   - `HARITA.md` dosyasına bir satır ekle,
   - Kararları `kararlar.md`'ye, dersleri `dersler.md`'ye işle.
5. Parola, token, `.env` içeriği, `local.properties`, SSH anahtarı veya oturum çerezi vault'a **ASLA** yazılmaz. Gerekirse `"parola X yöneticisinde"` gibi yer gösterici yaz.

## 3. İsimlendirme ve Bağlantı Kuralları (`naming`)
- Dosya adları: içeriği anlatan, **küçük harf, tireli, Türkçe karaktersiz** (ör. `gazi-eem-vize-takvimi-ve-ders-notlari.md`; asla `not-12.md` değil).
- Bağlantılar: Obsidian `[[wikilink]]` kullan. Her not en az bir ilgili nota ve `[[HARITA]]`'ya bağlansın.
- `wiki/` altındaki her düzenlemeden sonra `python3 brain.py lint` çalıştırılır (`0 problem(s)` zorunlu).

## 4. Her Zaman Odakta (`always in focus`)
- Her oturum başında `@HARITA.md`, `@simdi.md`, `@hafiza.md`, `@kararlar.md` ve `wiki/hot.md` (`SessionStart` hook'u ile) bağlama yüklenir.
- Büyük `wiki/index.md` dosyasını `@import` etme; yalnız gerektiğinde oku.
- Genel kodlama soruları için `wiki/` dizinini okuma.
