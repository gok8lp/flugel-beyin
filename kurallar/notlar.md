---
tur: kural
etiketler:
  - kural
  - notlar
  - wiki
  - kaynak
kapsam: "notlar/**, wiki/**"
olusturma: 2026-11-11
guncelleme: 2026-11-11
---

# Bilgi Notları ve Wiki Sayfaları Kuralları (`notlar/**` ve `wiki/**`)

> Üst bağlantı: [[HARITA]] · Odak: [[simdi]] · Bağlam: [[hafiza]] · Kararlar: [[kararlar]] · Şablon: [[sablonlar/not]]

## Kapsam
Bu kural dosyası kişisel bilgi notlarını barındıran `notlar/**` dizini ile ham kaynaklardan (`raw/**`) derlenen kavram sayfalarını barındıran `wiki/**` dizininde geçerlidir.

## Temel Kurallar
1. **Tek Konu İlkesi (Atomiklik):** Her dosya yalnızca **tek bir konuyu, kavramı veya teknik bileşeni** ele alır. Birden fazla bağımsız konu tek dosyada birleştirilmez; gerekirse ayrı dosyalara bölünüp `[[wikilink]]` ile bağlanır.
2. **Dosya Adlandırma Standardı:**
   - İçeriği doğrudan anlatan, **küçük harf**, **tireli (`-`)** ve **Türkçe karaktersiz** (`c, g, i, o, s, u`) dosya adları kullanılır (ör. `notlar/tbf-bulanik-mac-eslestirme.md`, `wiki/hakem-ucret-tarifesi-2026-2027.md`).
3. **YAML Frontmatter:**
   - **`notlar/**` için:** `tur: not`, `etiketler`, `olusturma`, `guncelleme` alanları zorunludur (bkz. [[sablonlar/not]]).
   - **`wiki/**` için:** Karpathy LLM Wiki standardı ve `brain.py lint` denetimi gereği `title`, `sources` (liste halinde `raw/...` yolları) ve `updated` (`YYYY-AA-GG`) alanları zorunludur.
4. **Kaynak Gösterme ve Birebir Alıntı Kuralı:**
   - Hiçbir iddia kaynaksız bırakılmaz; kaynakta olmayan bilgi tahminle doldurulmaz ("kayıtlı değil" denir).
   - **`notlar/**` sayfalarında:** Her iddianın veya bölümün altında kaynak dosya yolu ya da `"sen, sohbette, <tarih>"` belirtilir.
   - **`wiki/**` sayfalarında:** Somut her iddia kaynak dosyada birebir geçen metinle şu formatta doğrulanır:
     `> "birebir metin" - raw/<dosya>`
   - `wiki/` altındaki her düzenlemeden sonra `python3 brain.py lint` çalıştırılarak alıntıların kaynak dosyada birebir geçtiği ve kırık `[[link]]` olmadığı doğrulanır.
5. **Graf Bağlantısı:** Her not en az bir ilgili nota/projeye ve `[[HARITA]]` sayfasına `[[wikilink]]` ile bağlanır; yetim sayfa (orphan page) bırakılmaz.

## İlgili Sayfalar
- **Kök ve Harita:** [[HARITA]] · [[simdi]] · [[hafiza]] · [[kararlar]]
- **Diğer Kurallar ve Şablonlar:** [[kurallar/kisiler]] · [[kurallar/projeler]] · [[kurallar/guvenlik]] · [[sablonlar/not]]
- **Wiki ve Notlar:** [[wiki/ikinci-beyin-sistemi]] · [[wiki/index]] · [[notlar/assignr-api-yapisi]] · [[notlar/tbf-bulanik-mac-eslestirme]]

> Kaynak: `/home/flugel/Projects/prompt-obsidian-ikinci-beyin-sunucu.md`
