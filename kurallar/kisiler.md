---
tur: kural
etiketler:
  - kural
  - kisiler
  - gizlilik
kapsam: "kisiler/**"
olusturma: 2026-11-11
guncelleme: 2026-11-11
---

# Kişi Kartları Kuralları (`kisiler/**`)

> Üst bağlantı: [[HARITA]] · Odak: [[simdi]] · Bağlam: [[hafiza]] · Kararlar: [[kararlar]] · Şablon: [[sablonlar/kisi]]

## Kapsam
Bu kural dosyası yalnızca `kisiler/**` dizini altındaki kişi kartları oluşturulurken veya güncellenirken geçerlidir (Claude Code `.claude/rules/` mantığı).

## Zorunlu Alanlar ve Yapı
1. **YAML Frontmatter:** Her kişi kartında şu alanlar zorunludur:
   - `tur: kisi`
   - `etiketler`: En az `kisi` etiketi ve ilgili bağlam (`hakem`, `gazi-eem`, `gelistirici` vb.)
   - `olusturma`: `YYYY-AA-GG`
   - `guncelleme`: `YYYY-AA-GG`
2. **Dosya Adlandırma:** Küçük harf, tireli ve Türkçe karaktersiz (`kisiler/ahmet-gokalp-goksu.md`).
3. **Kart İçeriği (Zorunlu Bölümler):**
   - **Rol ve Kimlik:** Kişinin unvanı, görevi veya resmi sistemlerdeki (ör. TBF/Assignr, OBS) kayıtlı adı.
   - **Sorumluluk Alanı:** Hangi ders, proje, sistem veya организаsyon kapsamında yer aldığı.
   - **İletişim Yolu / Profiller:** Yalnızca doğrulanmış açık profiller (GitHub, kurumsal sayfa vb.) veya kullanıcının bizzat eklediği iletişim kanalı.
   - **İlgili Projeler ve Bağlantılar:** En az `[[HARITA]]` ve ilişkili `[[projeler/...]]`, `[[wiki/...]]`, `[[notlar/...]]` sayfalarına `[[wikilink]]` bağlantıları.

## Kesin Kişisel Veri Kuralı (Asla Uydurma!)
- **Telefon numarası, kişisel e-posta adresi, ev adresi, T.C. kimlik numarası veya özel iletişim bilgileri yapay zekâ tarafından ASLA tahmin edilmez, uydurulmaz ve dış kaynaklardan izinsiz çekilmez.**
- Bu tür kişisel verileri karta **yalnızca kullanıcı bizzat kendisi** ekleyebilir.
- Bilgi mevcut değilse ilgili alana açıkça `"Kayıtlı değil (yalnızca kullanıcı tarafından eklenir)"` yazılır.

## İlgili Sayfalar
- **Kök ve Harita:** [[HARITA]] · [[hafiza]] · [[kararlar]] · [[simdi]]
- **Diğer Kurallar ve Şablonlar:** [[kurallar/guvenlik]] · [[kurallar/projeler]] · [[kurallar/notlar]] · [[sablonlar/kisi]]
- **Örnek Kişi Kartı:** [[kisiler/ahmet-gokalp-goksu]]
- **Wiki ve Notlar:** [[wiki/ikinci-beyin-sistemi]] · [[notlar/gazi-eem-2026-guz-dersleri]]

> Kaynak: `/home/flugel/Projects/prompt-obsidian-ikinci-beyin-sunucu.md`
