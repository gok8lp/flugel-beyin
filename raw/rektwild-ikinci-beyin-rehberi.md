# İkinci Beyin Rehberi: Claude'a Kendini Tekrar Anlatmayı Bırak (Tam Kurulum)

Kaynak: https://x.com/rektwild/status/2119621016339026035 ve https://x.com/rektwild/status/2119624542813319531
Yazar: Rektwild (@rektwild)
Tarih: 9 Kasım 2026

Her Claude oturumu soğuk başlar.
Proje. Kararlar. İnsanlar. Geçen hafta denediğin şey. Hepsini yeniden anlatırsın; akşama kalınca çoğunu kaybetmiş olursun.
Bir ikinci beyin bunu bitirir. Claude, hem okuduğu hem de yazıp güncel tuttuğu düz metin dosyalarından oluşan bir klasörü okur. Sonraki oturum, bir öncekinin kaldığı yerden başlar.

Andrej Karpathy bu kalıbı Nisan 2026'da anlattı. İş bölümü şöyle: Obsidian IDE'dir, LLM programcıdır, wiki kod tabanıdır.

Üç katman:
- raw/: kaynakların. Model okur, asla düzenlemez.
- wiki/: modelin yazdığı ve bakımını yaptığı sayfalar.
- CLAUDE.md: kurallar — gelenekler ve iş akışları.

Üç işlem: ingest (kaynak ekle, model 10–15 sayfaya entegre etsin), query (sor, iyi cevapları geri dosyala), lint (çelişki, bayat iddia, yetim sayfa bul).

Hayatta kalıp kalmayacağını belirleyen isimlendirme kuralları: bir dosya, bir konu. Dosyayı içindekine göre adlandır (tax-policy.md; asla note-12.md değil). Küçük harf, tireli.
Bir proje için Inputs, Process, Outputs ve Feedback klasörleri aç; artı kendi CLAUDE.md'si: ne olduğu, tek hedefi, bitmişin nasıl göründüğü.

Tüm yığındaki en iyi fikir: proje başına ikinci beyin kurma. Her Claude Code projesini aynı vault'a işaret et.
hot.md bir düzine satırdır: ne üzerinde çalıştığın, en son ne değiştiği, açık sorular.

Kontrolü modelin dışına taşı. Bu script'in içinde LLM yok. İçe aktarılan dosyaları hash ile takip eder ve kuralları bozan sayfaları reddeder.

Haritadan dağılanlar:
- notes: bilgileri tutar, her dosyada tek konu
- people: her kişi için bir kart; rolü, nelerden sorumlu olduğu, nasıl ulaşılacağı
- projects: her projenin durumu ve sıradaki adım
- kök klasör: uzun vadeli hafıza, dersler ve neden öyle karar verdiğinin kaydı
- harita: fırtınanın en altında durur, sen bir şey sormadan önce yüklenir
