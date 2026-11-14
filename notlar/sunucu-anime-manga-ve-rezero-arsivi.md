---
tur: not
etiketler:
  - flugelserver
  - rezero
  - light-novel
  - manga
  - anime
  - suwayomi
  - komga
  - kavita
  - kamiyomu
olusturma: 2026-11-11
guncelleme: 2026-11-11
---

# flugelserver Anime, Manga ve Re:Zero (Light Novel / Web Novel) Arşivi Tam Envanteri

> **Üst Harita ve Kök Bağlantılar:** [[HARITA]] · [[hafiza]] · [[kararlar]] · [[dersler]] · [[simdi]]
> **İlgili Wiki Sayfaları:** [[wiki/flugelserver-anime-manga-lightnovel-arsivi]] · [[wiki/koharia-reader-ve-manga-ekosistemi]] · [[wiki/repo-koharia-reader]] · [[wiki/flugelserver-dizi-film-arsivi]]
> **İlgili Notlar:** [[notlar/docker-manga-ve-kitap-yigini]] · [[notlar/sunucu-dizi-ve-film-arsivi-envanteri]] · [[notlar/flugelserver-uc-disk-ve-klasor-agaci]]
> **İlgili Projeler:** [[projeler/flugel-manga]] · [[projeler/flugel-sunucu-ve-akis]]

---

## 1. Kütüphane Genel İstatistikleri (`2026-11-04` Denetimi ve `2026-11-11` Canlı Ağacı)

`/mnt/sidemain/media/books` dizini hem **Komga** (`/data`) hem **Kavita** (`/data/books`) hem de **Suwayomi** (`/mnt/sidemain/media/books/manga/suwayomi`) tarafından kullanılan devasa bir manga ve hafif roman (Light Novel) arşividir:

| Ölçüt | Değer / Durum |
| :--- | :--- |
| **Manga Kökü Toplam Dosya (`/mnt/sidemain/media/books/manga`)** | **23.898 dosya** (`23.752` `.cbz`, `68` `.jpg`, `35` `.json`, `22` `.webp`, `14` `.png`, `4` `.avif`, `2` `.epub`, `1` `.temp`) |
| **Manga Kökü Üst Düzey Seri Klasörü** | **43 klasör** (41'inde `.cbz` var; 6'sı doğrudan **Re:Zero** manga uyarlaması) |
| **Suwayomi Serileri (`suwayomi/mangas/<Kaynak>/<Seri>`)** | **12 kaynakta 155 seri**, toplam **20.421 `.cbz`** dosyası |
| **Kamiyomu Serileri (`kamiyomu/<Seri>`)** | **6 seri**, toplam **245 `.cbz`** dosyası (3'ü **Re:Zero**, 2'si *Haimiya*, 1'i *Neon Genesis Evangelion*) |
| **Light Novel Kökü (`/mnt/sidemain/media/books/ln`)** | **181 dosya** (`134` `.epub`, `47` `.pdf`) — *Alya* (9 dosya) dışındaki tüm koleksiyon (**172 dosya**) **Re:Zero** evrenine aittir |
| **Arşiv Sağlığı** | `0` bayt dosya yok; taranan `23.896` `.cbz`/`.epub` ZIP arşivinde **bozuk dosya sayısı: 0** |

---

## 2. Light Novel ve Re:Zero Arşivi (`/mnt/sidemain/media/books/ln`)

Light Novel arşivi `/home/flugel/work/organize_ln_languages.py` betiği ve `2026-11-02` / `2026-11-03` düzenlemeleriyle (`rezero-ln-20261103` yedeği `/mnt/side/backups/` altında korunarak) **İngilizce** ve **Türkçe** olarak iki ana dil dalına ayrılmıştır:

### 2.1. İngilizce Light Novel & Web Novel Koleksiyonu (`ln/books/English/`)
1. **`books/English/Alya` (9 dosya — EPUB & PDF):**
   - `Alya Sometimes Hides Her Feelings in Russian - Volume 03 [Yen Press][Kobo].epub`
   - `Alya Sometimes Hides Her Feelings in Russian - Volume 04 [Yen Press][Kobo].epub`
   - `Alya Sometimes Hides Her Feelings in Russian - Volume 04.5 [Yen Press][Kobo].epub`
   - `Alya Sometimes Hides Her Feelings in Russian - Volume 05 [Yen Press][Kobo].epub` ve `[Kobo_LNWNCentral].pdf`
   - Volume 06, 07 (`[Yen Press][Stick].epub`), 08 (`Sunsunsun & Momoco - ... 08.epub`) + manga kökünde `Momoco's Art Book [Yen Press].epub`.
2. **`books/English/ReZero` (6 Alt Kategori — Arc 1–9 ve Cilt 1–27+ Tam Koleksiyon):**
   - `Light Novel/`: Resmi İngilizce Light Novel ciltleri (Cilt 1–27+ EPUB/PDF serisi).
   - `Web Novel/`: Arc 1'den **Arc 9 (*Light of a Nameless Star*)** dahil derlenmiş İngilizce Web Novel ciltleri (ayrıca `/home/flugel/Arc 9 - Light of a Nameless Star-20260519T215221Z-3-001.zip.bak` ve `/home/flugel/indirme-rezero/Re:Zero Novel` yedekleri mevcuttur).
   - `EX/`: Re:Zero EX yan roman ciltleri (Crusch/abisi, Wilhelm, Thearesia vb. geçmiş hikayeleri).
   - `IF Stories/`: Yazar Tappei Nagatsuki'nin alternatif rota (Ayamatsu/Pride, Oboreru/Wrath, Kasimatsu/Greed, Tsugihagu/Gluttony, Rem/Sloth, Lust) hikayeleri.
   - `Short Stories/`: Yan hikayeler ve dükkan özel öykü derlemeleri.
   - `Extras/`: Ek materyaller ve rehber kitaplar.

### 2.2. Türkçe Re:Zero Koleksiyonu (`ln/books/Türkçe/ReZero/`)
Türkçe Re:Zero arşivi çevirmen gruplarına ve formatlarına göre **9 özel alt klasöre** ayrılmıştır:
1. `Re Zero - EX` (Türkçe EX yan ciltleri)
2. `Re Zero - IF Rotaları` (Türkçe alternatif IF hikayeleri)
3. `Re Zero - Light Novel (Eraxy)` (Eraxy çevirisi EPUB/PDF ciltleri)
4. `Re Zero - Light Novel (TimeOfMortally PDF)` (TimeOfMortally PDF çevirileri)
5. `Re Zero - Light Novel 21-25 (PDF, çevirmen belirsiz)` (Arc 6 — Cilt 21–25 Türkçe PDF seti)
6. `Re Zero - Web Novel` (Arc bazlı Türkçe Web Novel bölümleri, Cilt 26–33 / Arc 7–9 karşılıkları dahil)
7. `Re Zero - Web Novel (Epik Novel, tek dosya)` (Epik Novel toplu derleme)
8. `Re Zero - Web Novel (TimeOfMortally PDF)` (TimeOfMortally Web Novel PDF ciltleri)
9. `Re Zero - Yan Hikâyeler` (Türkçeye çevrilmiş Short Stories / Tanpenshuu öyküleri)

---

## 3. Manga Kök Dizini Serileri (`/mnt/sidemain/media/books/manga`)

Manga kök dizininde doğrudan yer alan 43 seri klasörü ve dosya sayıları:

### 3.1. Re:Zero Manga Uyarlamaları (Kök + Kamiyomu + Suwayomi)
- **Kök Dizin Re:Zero Mangaları:**
  1. `ReZero kara Hajimeru Isekai Seikatsu Dai 1-shouOuto no Ichinichi-hen` (**12 dosya** — Arc 1: Başkentte Bir Gün)
  2. `Re_Zero_kara_Hajimeru_Isekai_Seikatsu_Dai_1-shou_Outo_no_Ichinichi-hen` (**13 dosya** — Arc 1)
  3. `ReZero kara Hajimeru Isekai Seikatsu Dai 3-shouTruth of Zero` (**35 dosya** — Arc 3: Truth of Zero)
  4. `Re_Zero_kara_Hajimeru_Isekai_Seikatsu_Dai_3-shou_Truth_of_Zero` (**36 dosya** — Arc 3)
  5. `Re_zero_Kara_Hajimeru_Isekai_Seikatsu_Dai_4-Shou_Seiiki_To_Gouyoku_No_Majo` (**73 dosya** — Arc 4: Sığınak ve Açgözlülük Cadısı)
  6. `Re_Zero_kara_Hajimeru_Isekai_Seikatsu_Dai_5-shou_Mizu_no_Miyako_to_Eiyuu_no_Uta` (**20 dosya** — Arc 5: Su Şehri Priestella ve Kahramanların Şarkısı)
  7. `Re_Zero_kara_Hajimeru_Isekai_Seikatsu_Hyouketsu_no_Kizuna` (**6 dosya** — *The Frozen Bond* / Emilia & Puck OVA Manga Uyarlaması)
  8. `Re_Zero_kara_Hajimeru_Isekai_Seikatsu_Koushiki_Anthology_Comic` (**9 dosya** — Resmi Antoloji Çizgi Romanı)
- **Kamiyomu Altındaki Re:Zero Mangaları (`manga/kamiyomu/`):**
  - `Re:ZERO - Starting Life in Another World - Chapter 1: A Day in the Capital` (**13 dosya**)
  - `Re:ZERO -Starting Life in Another World-, The Frozen Bond` (**58 dosya**)
  - `Re:Zero Kara Hajimeru Isekai Seikatsu Official Anthology` (**5 dosya**)
- **Suwayomi Altındaki Re:Zero Mangaları (`manga/suwayomi/mangas/`):**
  - `MangaFire (EN)`: `Kenki Renka_ Re_Zero kara Hajimeru Isekai Seikatsu † Shinmeitan` (Wilhelm & Theresia — Kılıç Şeytanı Aşk Şarkısı) ve `Re_Zero Kara Hajimeru Isekai Seikatsu Official Anthology`
  - `MangaHub (EN)`: `Re_zero Kara Hajimeru Isekai Seikatsu Dai 4-Shou - Seiiki To Gouyoku No Majo`
  - `Mangahere (EN)`: `Re_Zero kara Hajimeru Isekai Seikatsu - Daigoshou - Mizu no Miyako to Eiyuu no Uta`

### 3.2. Kök Dizindeki Diğer Tüm Manga Serileri
| Seri Klasör Adı | Dosya Sayısı | Notlar |
| :--- | :--- | :--- |
| `Vagabond` | 329 `.cbz` | Türkçe (`Bölüm 001.cbz`...) |
| `Jujutsu_Kaisen` | 275 `.cbz` | Türkçe (`Bölüm 001.cbz`...) |
| `Chainsaw_Man` | 228 `.cbz` | Türkçe (`Bölüm 001.cbz`...) |
| `Oshi_no_Ko_1` / `Oshi_no_Ko` / `_Oshi_no_Ko_` / `Oshi no Ko` | 175 / 168 / 103 / 102 `.cbz` | Farklı kaynaklardan Türkçe ve İngilizce sürümler |
| `Frieren_Beyond_Journey_s_End` | 147 `.cbz` | İngilizce (`0_The_End_of_the_Adventure.cbz`...) |
| `Yotsuba_to_` | 124 `.cbz` | *Yotsuba&!* |
| `JoJo_s_Bizarre_Adventure_Part_8_JoJolion` | 109 `.cbz` | *JoJolion* |
| `Tune_In_To_The_Midnight_Heart` & `Mayonaka_Heart_Tune` | 105 & 67 `.cbz` | İngilizce (105) ve Türkçe (67) sürümler |
| `Otonari_no_Tenshi-sama_ni_Itsunomanika_Dame_Ningen_ni_Sareteita_Ken` | 103 `.cbz` | *The Angel Next Door Spoils Me Rotten* |
| `The_Angel_Next_Door_Spoils_Me_Rotten_After_The_Rain` & `..._after_the_rain` | 85 & 6 `.cbz` | *After the Rain* yan serisi (EN & TR) |
| `Neon_Genesis_Evangelion` & `Shinseiki_Evangelion` & `kamiyomu/Neon Genesis Evangelion` | 101 & 99 & 84 `.cbz` | *Evangelion* manga serisi |
| `Alya_Sometimes_Hides_Her_Feelings_In_Russian` & `Alya` | 78 & 2 dosya | *Roshidere* mangası ve Momoco Art Book |
| `Haimiya-senpai wa Kowakute Kawaii` & `[Pixiv Edition]` & `kamiyomu/Haimiya...` | 74 & 13 & 73 & 12 `.cbz` | Ana seri ve Pixiv sürümleri |
| `Class_de_2-banme_ni_Kawaii_Onnanoko_to_Tomodachi_ni_Natta` (3 klasör) | 60 / 58 / 56 `.cbz` | *I Made Friends with the Second Prettiest Girl in My Class* |
| `Girls_Last_Tour_Official_Anthology_Comic` & `Girls_Last_Tour` | 58 & 49 `.cbz` | *Shoujo Shuumatsu Ryokou* + Antoloji |
| `Kusunoki-san_wa_Koukou_Debut_ni_Shippai_Shite_Iru` | 52 `.cbz` | İngilizce |
| `Tonari_no_Neko_to_Koi_Shirazu` | 47 `.cbz` | İngilizce |
| `Ushiro_no_Seki_no_Gal_ni_Sukarete_Shimatta_Mou_Ore_wa_Dame_Kamoshirenai_` | 24 `.cbz` | Türkçe (`Bölüm 001.cbz`...) |
| `Remote_Jugyou_ni_Nattara_Class_1_no_Bishoujo_to_Doukyo_suru_Koto_ni_Natta` | 23 `.cbz` | Türkçe (`Bölüm 001.cbz`...) |
| `Bocchi_The_Rock_Anthology_Comic` / `..._Kikuri_Hiroi_s_Heavy-Drinking_Diary` / `..._Epigraph` | 18 / 17 / 1 `.cbz` | *Bocchi the Rock!* yan serileri |
| `Laid-Back_Camp` & `Kaguya-sama_Love_is_War_Colored_Edition_` | 1 `.cbz` & 2 meta | *Yuru Camp* ve Kaguya kapak/indeks |

---

## 4. Suwayomi Kaynak Bazlı Manga Envanteri (`manga/suwayomi/mangas/`)

Suwayomi altında **12 İngilizce kaynakta toplam 155 seri (20.421 `.cbz`)** bulunmaktadır:

1. **MANGA Plus by SHUEISHA (EN):** *Bleach*
2. **MangaDex (EN):** *Akame ga KILL!*, *Baki-Dou*, *Bocchi the Rock!*, *Bocchi the Rock! Epigraph*, *Classroom of the Elite*, *Cosmic Princess Kaguya!*, *Fullmetal Alchemist*, *Haimiya Is Scary Cute*, *I Made Friends with the Second Prettiest Girl in My Class*, *Itoshi no Ko, Charlotte*, *JoJo's Bizarre Adventure Part 9 - The JOJOLands*, *JoJo's Bizarre Adventure: Part 7 – Steel Ball Run*, *Lycoris Recoil Koushiki Comic Anthology: React*, *Lycoris Recoil: Official Comic Anthology - Reload*, *Lycoris Recoil: Recollect*, *More than a Married Couple, but Not Lovers*, *My Senpai is Annoying*, *Studio Cabana*, *The Angel Next Door Spoils Me Rotten*, *The Drifting Classroom*
3. **MangaFire (EN):** *1-nen A-gumi no Monster*, *Akira*, *Death Note Tanpenshuu*, *Go-Toubun no Hanayome*, *Ijiranaide, Nagatoro-san*, *Innocent*, *Italia-jin no Onnanoko ga Isourou Suru Koto ni Natta*, *JoJo Part 1: Phantom Blood*, *JoJo Part 2: Sentou Chouryuu*, *JoJo Part 3: Stardust Crusaders*, *JoJo Part 5: Ougon no Kaze*, *JoJo Part 6: Stone Ocean*, *Karakai Jouzu no (Moto) Takagi-san*, *Kenki Renka: Re:Zero kara Hajimeru Isekai Seikatsu † Shinmeitan*, *Komi Can't Communicate*, *Kuroko no Basket - Replace Plus*, *My Dress-Up Darling*, *NANA*, *Re:Zero Official Anthology*, *Shikanoko Nokonoko Koshitantan*
4. **MangaFox (EN):** *Blue Period*, *Chi no Wadachi*, *Girls' Last Tour Official Anthology Comic*, *Legend of the Northern Blade*, *Ogami Tsumiki to Kinichijou*, *Yamada-kun to Lv999 no Koi wo Suru*
5. **MangaHub (EN):** *5toubun no Hanayome*, *Azumanga Daioh*, *Kuroiwa Medaka ni Watashi no Kawaii ga Tsuujinai*, *Mob Psycho 100*, *Oyasumi Punpun*, *Re:Zero Dai 4-Shou - Seiiki To Gouyoku No Majo*, *Slam Dunk*, *The Promised Neverland*, *Tokidoki Bosotto Roshiago de Dereru Tonari no Alya-san (Novel)*
6. **MangaKatana (EN):** *Attack on Titan*, *Grand Blue*, *Is This Hero for Real?*, *Kaguya-sama wa Kokurasetai*, *Kimetsu no Yaiba*, *KonoSuba! Megumin Anthology Aka*, *Kusuriya no Hitorigoto*, *Oshi no Ko*
7. **MangaPill (EN):** *Fetiple*, *Hochiya-san wa Amari Aru*, *Hunter x Hunter*, *JoJo Part 4: Diamond Is Unbreakable*, *Kaguya-sama wo Kataritai*, *Shiotaiou no Satou-san ga Ore ni dake Amai*, *Watashi ni xx Shinasai!*, *Yuru Camp△*
8. **Mangahere (EN):** *Bakemonogatari*, *Boku no Hero Academia*, *Death Note*, *Mayonaka Heart Tune*, *Re:Zero Daigoshou - Mizu no Miyako to Eiyuu no Uta*, *Spy X Family*, *Tokidoki Bosotto Roshiago de Dereru Tonari no Alya-san*, *Tsumi to Kai*
9. **Mangakakalot (EN):** *Billy Bat*, *Danjo No Yujou Wa Seiritsu Suru? (Iya, Shinai!!)*, *Delicious in Dungeon*, *Frieren: Beyond Journey's End*, *Hokkaido Gals Are Super Adorable!*, *JoJolion*, *Nee, Mou Isso Tsukiacchau? Osananajimi no Bishoujo ni Tanomarete, Camo Kareshi Hajimemashita*, *Rikei ga Koi ni Ochita no de Shoumei shitemita*, *She Is In Love With The Mob*, *The Fragrant Flower Blooms With Dignity*
10. **Manganato (EN):** *Blame!*, *Garbage Time*, *Liar Game*, *One Punch Man*, *Redo Of Healer*, *Seishun Buta Yarou wa Siscon Idol no Yume o Minai*, *Toradora!*, *Villain with a Crush*
11. **Mangatown (EN):** *Ansatsu Kyoushitsu*, *Beck*, *Claymore*, *DARLING in the FRANXX*, *Fire Punch*, *Horimiya*, *Kuroko no Basket*, *Yofukashi no uta*
12. **Weeb Central (EN):** *20th Century Boys*, *Adabana*, *Another*, *Bakuman*, *Before You Go Extinct*, *Berserk*, *Bleach*, *Bocchi the Rock! Side Story - Kikuri Hiroi’s Heavy-Drinking Diary*, *Cat-Eyed Boy*, *Chainsaw Man*, *Dandadan*, *Days with My Stepsister*, *Girls' Last Tour*, *Goodbye, Eri*, *I Want to Love You Till Your Dying Day*, *Ibitsu*, *Jujutsu Kaisen*, *Jumyou wo Kaitotte Moratta. Ichinen ni Tsuki, Ichimanen de*, *Kagurabachi*, *Konosuba: An Explosion on This Wonderful World!*
