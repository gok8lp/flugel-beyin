---
tur: not
etiketler:
  - flugelserver
  - medya-arsivi
  - filmler
  - diziler
  - anime
  - jellyfin
  - plex
  - sonarr
  - radarr
olusturma: 2026-11-11
guncelleme: 2026-11-11
---

# flugelserver Dizi, Anime ve Film Arşivi Tam Envanteri

> **Üst Harita ve Kök Bağlantılar:** [[HARITA]] · [[hafiza]] · [[kararlar]] · [[dersler]] · [[simdi]]
> **İlgili Wiki Sayfaları:** [[wiki/flugelserver-dizi-film-arsivi]] · [[wiki/flugelserver-anime-manga-lightnovel-arsivi]] · [[wiki/flugelserver-docker-uygulamalari]] · [[wiki/flugelserver-dosya-agaci-ve-diskler]]
> **İlgili Notlar:** [[notlar/docker-medya-ve-arr-yigini]] · [[notlar/sunucu-anime-manga-ve-rezero-arsivi]] · [[notlar/flugelserver-uc-disk-ve-klasor-agaci]] · [[notlar/docker-uygulama-baglanti-topolojisi]]
> **İlgili Projeler:** [[projeler/flugel-sunucu-ve-akis]]

---

## 1. Medya Arşivi Genel Özeti

`flugelserver` üzerindeki tüm sinema filmleri, diziler ve animeler 1 TB kapasiteli LUKS şifreli ana veri diski **`/mnt/sidemain/media/`** altında tutulur. Devam eden ve yeni tamamlanan torrent indirmeleri ise **`/mnt/side/downloads/`** üzerinde yer alır.

- **Sunucu Servisleri:** **Jellyfin** (`127.0.0.1:18096`), **Plex** (`:32400`), **Radarr** (`127.0.0.1:17878`), **Sonarr** (`127.0.0.1:18989`), **Bazarr** (`127.0.0.1:16767`) ve **Subgen** (`127.0.0.1:18091`).
- **IMDb ve Anime Takip Otomasyonu:** `/opt/basket-bot/imdb_puan.py` (`imdb-puan.timer`, her sabah 06:24) ve `/opt/basket-bot/anime_takip.py` (`anime-takip.timer`, her saat başı :05) yeni bölümleri ve puanları takip ederek **FLUGEL Akış** ve **FLUGEL Island** panellerine bildirir.
- **Canlı Envanter Sayıları (`raw/flugelserver/dizi-film-arsivi.md`):**
  - `/mnt/sidemain/media/movies` altında **42 film klasörü** (+ `/mnt/side/downloads/complete/radarr` altında bekleyenlerle birlikte toplam film envanteri)
  - `/mnt/sidemain/media/series` altında **13 ana dizi/anime klasörü** (+ `/mnt/side/downloads/complete/tv-sonarr` ve `anime_takip.py` takip listesi)

---

## 2. Filmler Tam Listesi (`/mnt/sidemain/media/movies`)

Aşağıda `/mnt/sidemain/media/movies` dizininde yer alan tüm filmler alfabetik sırayla, yayın yılları ve kategorileriyle listelenmiştir:

| # | Klasör / Film Adı | Yıl | Kategori / Tür |
| :--- | :--- | :--- | :--- |
| 1 | `100 METERS (2025)` | 2025 | Anime Film (*Hyakuemu*) |
| 2 | `12 Angry Men (1957)` | 1957 | Klasik Drama / Mahkeme |
| 3 | `A Whisker Away (2020)` | 2020 | Anime Film (*Nakitai Watashi wa Neko wo Kaburu*) |
| 4 | `Alien (1979)` | 1979 | Bilim Kurgu / Korku |
| 5 | `Amélie (2001)` | 2001 | Romantik Komedi / Fransız Sineması |
| 6 | `Back to the Future (1985)` | 1985 | Bilim Kurgu / Macera |
| 7 | `Catch Me If You Can (2002)` | 2002 | Biyografi / Suç / Drama |
| 8 | `Django Unchained (2012)` | 2012 | Western / Aksiyon |
| 9 | `Dune (2021)` | 2021 | Bilim Kurgu / Epik |
| 10 | `Dune - Part Two (2024)` | 2024 | Bilim Kurgu / Epik |
| 11 | `Dunkirk (2017)` | 2017 | Savaş / Tarih |
| 12 | `EVANGELION 30th Anniversary Special Screening (2026)` | 2026 | Anime Özel Gösterim (*Evangelion 30. Yıl*) |
| 13 | `Fight Club (1999)` | 1999 | Psikolojik Drama / Kült |
| 14 | `Ghost in the Shell (1995)` | 1995 | Anime Film / Cyberpunk (*Kôkaku Kidôtai*) |
| 15 | `Grave of the Fireflies (1988)` | 1988 | Anime Film / Studio Ghibli (*Hotaru no Haka*) |
| 16 | `Gravity (2013)` | 2013 | Bilim Kurgu / Gerilim |
| 17 | `Howl's Moving Castle (2004)` | 2004 | Anime Film / Studio Ghibli (*Howl no Ugoku Shiro*) |
| 18 | `I Want to Eat Your Pancreas (2018)` | 2018 | Anime Film / Drama (*Kimi no Suizô wo Tabetai*) |
| 19 | `Insomnia (2002)` | 2002 | Gizem / Psikolojik Gerilim |
| 20 | `Jujutsu Kaisen 0 (2021)` | 2021 | Anime Film / Aksiyon |
| 21 | `Look Back (2024)` | 2024 | Anime Film / Tatsuki Fujimoto Uyarlaması |
| 22 | `Memento (2000)` | 2000 | Gizem / Neo-Noir Gerilim |
| 23 | `My Neighbor Totoro (1988)` | 1988 | Anime Film / Studio Ghibli (*Tonari no Totoro*) |
| 24 | `Neon Genesis Evangelion - The End of Evangelion (1997)` | 1997 | Anime Film / Mecha & Psikolojik |
| 25 | `One Battle After Another (2025)` | 2025 | Drama / Suç |
| 26 | `Oshi no Ko -The Final Act- (2024)` | 2024 | Live-Action Film Uyarlaması |
| 27 | `Parasite (2019)` | 2019 | Gerilim / Kara Komedi (*Gisaengchung*) |
| 28 | `Perfect Blue (1998)` | 1998 | Anime Film / Satoshi Kon Psikolojik Gerilim |
| 29 | `Princess Mononoke (1997)` | 1997 | Anime Film / Studio Ghibli (*Mononoke-hime*) |
| 30 | `Redline (2009)` | 2009 | Anime Film / Bilim Kurgu Yarış |
| 31 | `Saving Private Ryan (1998)` | 1998 | Savaş / Tarih |
| 32 | `Spirited Away (2001)` | 2001 | Anime Film / Studio Ghibli (*Sen to Chihiro no Kamikakushi*) |
| 33 | `The Disappearance of Haruhi Suzumiya (2010)` | 2010 | Anime Film (*Suzumiya Haruhi no Shôshitsu*) |
| 34 | `The Godfather (1972)` | 1972 | Suç / Drama (Üçleme 1) |
| 35 | `The Godfather Part II (1974)` | 1974 | Suç / Drama (Üçleme 2) |
| 36 | `The Godfather Part III (1990)` | 1990 | Suç / Drama (Üçleme 3) |
| 37 | `The Intouchables (2011)` | 2011 | Biyografi / Komedi / Drama |
| 38 | `The Lord of the Rings - The Fellowship of the Ring (2001)` | 2001 | Fantastik / Epik (Üçleme 1) |
| 39 | `The Lord of the Rings - The Two Towers (2002)` | 2002 | Fantastik / Epik (Üçleme 2) |
| 40 | `The Lord of the Rings - The Return of the King (2003)` | 2003 | Fantastik / Epik (Üçleme 3) |
| 41 | `The Social Network (2010)` | 2010 | Biyografi / Drama |
| 42 | `The Truman Show (1998)` | 1998 | Bilim Kurgu / Komedi-Drama |

---

## 3. Diziler ve Animeler Tam Listesi (`/mnt/sidemain/media/series`)

`/mnt/sidemain/media/series` dizininde yer alan dizi ve anime serileri:

| # | Klasör / Dizi veya Anime Adı | Tür | Açıklama |
| :--- | :--- | :--- | :--- |
| 1 | `1883` | Western / Tarih | *Yellowstone* ön dizisi (1 Sezon) |
| 2 | `86 - Eighty Six` | Anime | Bilim Kurgu / Mecha / Askeri Drama |
| 3 | `Attack on Titan` | Anime | *Shingeki no Kyojin* (Tam Seri) |
| 4 | `Band of Brothers` | Mini Dizi | II. Dünya Savaşı Tarihsel Drama |
| 5 | `Better Call Saul` | Dizi | Suç / Hukuk Draması |
| 6 | `Black Mirror` | Dizi | Bilim Kurgu / Antoloji |
| 7 | `JoJo's Bizarre Adventure (2012)` | Anime | *JoJo no Kimyou na Bouken* |
| 8 | `Makeine - Too Many Losing Heroines!` | Anime | Romantik Komedi (*Make Heroine ga Oosugiru!*) |
| 9 | `Neon Genesis Evangelion` | Anime | *Shinseiki Evangelion* (Orijinal TV Serisi) |
| 10 | `Regular Show - The Lost Tapes` | Animasyon | Çizgi Dizi |
| 11 | `The Melancholy of Haruhi Suzumiya` | Anime | *Suzumiya Haruhi no Yûutsu* |
| 12 | `Westworld` | Dizi | Bilim Kurgu / Distopya |
| 13 | `Young Sherlock (2026)` | Dizi | Gizem / Dedektiflik (2026) |

---

## 4. İndirme Klasörü Durumu (`/mnt/side/downloads`)

Transmission tarafından indirilen ve Sonarr/Radarr tarafından işlenen/bekleyen medya kalemleri (`raw/flugelserver/dizi-film-arsivi.md`):

- **`/mnt/side/downloads/complete/radarr` (2 dosya):**
  - `Michael [2026] HDTS YG`
- **`/mnt/side/downloads/complete/tv-sonarr`:**
  - `www.UIndex.org    -    Dutton.Ranch.S01E03.1080p.WEB.h264-GRACE`
  - `www.UIndex.org    -    The Sopranos S06E10 Moe n Joe 1080p BluRay 10Bit DDP5 1 H265-d3g`
- **`/mnt/side/downloads/incomplete`:** Boş (`0` dosya).
- **`/mnt/sidemain/media/tv-recordings`:** Boş (eski `medya/tv_kayitlari` klasörünün FHS karşılığı).
