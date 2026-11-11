# Hakem Kazanç Hesabı ve BÖLGE Ücreti Kuralı

Bağlantılar: [[map]] · [[decisions]] · [[hakem-ucret-tarifesi-2026-2027]] · [[04 - Hakem İstatistikleri ve 2026-2027 Ücret Tarifesi]]

## Düzenlenebilir Ücret Tablosu (`KazancHesaplayici.kt`)
- Hiçbir tutar koda sabit gömülmemiştir; `ucret_tablosu.json` içinde saklanır ve uygulama içinden düzenlenebilir.
- Özel müsabaka başlangıç değerleri (2026-2027 TBF Özel Müsabaka Tarifesi):
  - İl içi altyapı / okul (`AGL`, `OKUL`): Hakem `1.700 TL`, Masa Görevlisi `850 TL`.
  - Büyükler özel turnuva (`ABL`, `AA`): Erkek Hakem `3.250 TL`, Kadın Hakem `2.600 TL`.
- **`BÖLGE` Kuralı:** Resmi il ligi (`BÖLGE`) ücretleri açık kaynaklarda yer almadığından `tutarTl = null` ("ücret tanımsız") başlar; kesinlikle `0 TL` sayılmaz ve `tanimsizMacSayisi` olarak ayrı raporlanır.
