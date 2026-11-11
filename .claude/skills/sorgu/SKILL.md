---
name: sorgu
description: Vault ve LLM Wiki üzerinde bağlam tasarruflu sorgulama becerisi (önce wiki/hot.md ve HARITA.md, sonra wiki/index.md, ardından yalnızca gereken sayfalar; kaynak gösterimli yanıt ve değerli cevabı yeni wiki/not sayfası olarak kaydetme).
tur: beceri
etiketler:
  - beceri
  - sorgu
  - wiki
  - arama
olusturma: 2026-11-11
guncelleme: 2026-11-11
---

# Bilgi Tabanı Sorgu Becerisi (`/sorgu`)

> Üst bağlantı: [[HARITA]] · Odak: [[simdi]] · Bağlam: [[hafiza]] · Kararlar: [[kararlar]] · Kurallar: [[kurallar/notlar]]

## Amaç
Kullanıcının projeler, dersler, hakemlik veya `flugelserver` mimarisi hakkındaki sorularını tüm vault'u körlemesine bağlama yüklemeden, kademeli okuma sırasıyla ve kanıtlı kaynak gösterimiyle yanıtlamak.

## Kademeli Okuma ve Yanıtlama Akışı

### 1. Önce `wiki/hot.md` ve `HARITA.md` Oku
- Güncel çalışma odağını görmek için önce [[wiki/hot]] (`wiki/hot.md`) ve kişisel bilgi haritası için [[HARITA]] (`HARITA.md`) dosyalarına bak.

### 2. Sonra `wiki/index.md` Kataloğunu Tara
- Sorunun hangi kavram sayfalarıyla ilgili olduğunu bulmak için [[wiki/index]] (`wiki/index.md`) dosyasındaki başlık ve kaynak eşleşmelerini incele.

### 3. Yalnızca Gereken Sayfaları Oku
- Bütün `wiki/` veya `raw/` klasörünü belleğe yükleme; yalnızca `HARITA.md` ve `wiki/index.md` tarafından işaret edilen spesifik sayfaları (ör. [[projeler/duduk]], [[wiki/tbf-eslestirme-algoritmasi]], [[notlar/hakem-kazanc-ve-bolge-kurali]]) oku.
- Genel programlama veya standart kütüphane soruları için wiki'yi gereksiz yere okuma.

### 4. Kaynaklı ve Sayfa Adlı Cevap Ver
- Yanıtta bilginin alındığı sayfa adlarını (`[[wiki/...]]`, `[[projeler/...]]`, `[[notlar/...]]`) açıkça belirt.
- Her somut iddianın altına kaynağını yaz (`dosya yolu` ya da `"sen, sohbette, <tarih>"`).
- Hiçbir dosya konuyu kapsamıyorsa açıkça **"kayıtlı değil"** de; asla tahminle doldurma.

### 5. Değerli Sentezi Kalıcı Sayfa Olarak Kaydet
- Eğer sorgu sonucunda birden fazla kaynağı birleştiren yeni ve kalıcı bir sentez, karşılaştırma veya çözüm ortaya çıktıysa:
  - Kaynak derlemesiyse `wiki/` altında yeni bir kavram sayfası oluşturup `python3 brain.py lint` ve `python3 brain.py index` çalıştır,
  - Kişisel not/karar ise `notlar/` veya [[kararlar]] / [[dersler]] içine kaydet ve [[HARITA]] sayfasına bir satır ekle.

## İlgili Sayfalar ve Bağlantılar
- **Kök ve Harita:** [[HARITA]] · [[simdi]] · [[hafiza]] · [[kararlar]] · [[dersler]]
- **Kurallar:** [[kurallar/notlar]] · [[kurallar/projeler]] · [[kurallar/kisiler]] · [[kurallar/guvenlik]]
- **Wiki ve Notlar:** [[wiki/hot]] · [[wiki/index]] · [[wiki/ikinci-beyin-sistemi]] · [[notlar/assignr-api-yapisi]] · [[notlar/flugelserver-mimari-ozeti]]
- **Projeler:** [[projeler/duduk]] · [[projeler/flugel-manga]] · [[projeler/okul-guz-2026]] · [[projeler/hakemlik]] · [[projeler/flugel-sunucu-ve-akis]]

> Kaynak: `/home/flugel/Projects/prompt-obsidian-ikinci-beyin-sunucu.md`
