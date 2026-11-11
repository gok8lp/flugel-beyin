# GitHub Repo: gok8lp/basketbol-kurallar-calisma

- **URL:** https://github.com/gok8lp/basketbol-kurallar-calisma
- **Görünürlük:** Özel (Private)
- **Ana Dil:** HTML
- **Son Güncelleme:** 2026-10-28T13:40:49Z
- **Açıklama:** Hakemlik sınavı çalışma kopyası: işaretli TBF kural kitabı + FIBA 2026 farkları

## Dosya Ağacı (File Tree)
- `Basketbol-Oyun-Kurallari-2024-isaretli-2026-farklari.pdf` (blob)
- `README.md` (blob)
- `kaynak` (tree)
- `kaynak/build.py` (blob)
- `kaynak/ek.html` (blob)
- `kaynak/marks.py` (blob)

## README İçeriği
# Basketbol Oyun Kuralları – işaretli çalışma kopyası

Kişisel hakemlik sınavı çalışma kopyası.

**[Basketbol-Oyun-Kurallari-2024-isaretli-2026-farklari.pdf](Basketbol-Oyun-Kurallari-2024-isaretli-2026-farklari.pdf)** (103 sayfa)

- **Sayfa 1–97:** TBF *Basketbol Oyun Kuralları 2024* (v1.0a, 1 Ekim 2024'ten itibaren geçerli).
  - Sınav açısından önemli sayılar, süreler ve kurallar **kırmızı** vurgulandı (205 vurgu).
  - 2026'da değişen sayfaların üstünde kırmızı **"2026:"** uyarısı var.
- **Sayfa 98–103:** EK. FIBA *Official Basketball Rules 2026* (v1.1, 1 Ekim 2026'dan itibaren geçerli) kitabında olup Türkçe kitapta olmayanların Türkçe özeti:
  - Madde numarası kayması tablosu (yeni Md. 37 ve 38).
  - Yeni Md. 15 (atış hali), 24.2 (dripling), 36 (Kategori 1/2 teknik faul), 37 (Oyunun Akışını Bozan Faul), 38 (Kasti Faul).
  - Yeni hakem işaretleri ve maç kağıdı işaretleri, D.5.2, IRS eklemeleri.
  - Türkçe kitapta "sportmenlik dışı" geçen her yerin 2026 karşılığı.

Ekteki Türkçe metinler **resmi TBF çevirisi değildir**; kesin metin için FIBA'nın İngilizce kural kitabı esastır.

## Kaynaklar

- TBF Dokümanlar, "Basketbol Oyun Kuralları 2024": https://www.tbf.org.tr/dokuman
- FIBA Resource Hub (Official Basketball Rules 2026, Rule Changes, Interpretations): https://about.fiba.basketball/en/services/resource-hub/downloads

Kural metinlerinin telif hakkı FIBA ve TBF'ye aittir. Bu depo özel (private) tutulmalıdır.

## Yeniden üretme

`kaynak/` klasöründe PyMuPDF betiği (`build.py`), vurgu listesi (`marks.py`) ve ek metni (`ek.html`) var:

```bash
python kaynak/build.py kurallar2024.pdf kaynak/ek.html cikti.pdf
```

