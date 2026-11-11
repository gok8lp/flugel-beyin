# Manga ve Light Novel ad denetimi (salt okunur) - 2026-11-04

Kapsam: `/mnt/sidemain/media/books/manga` ve `/mnt/sidemain/media/books/ln` (flugelserver, SSH ile). Sunucuda hicbir sey degistirilmedi/yeniden adlandirilmadi/olusturulmadi; yalniz ls/find/stat benzeri okuma ve cbz/epub dizin okumasi (python zipfile, yazma yok). Re:Zero klasorleri yalniz listelendi, oneri uretilmedi. Oneriler yalnizca oneridir, uygulanmadi.

## Ozet

| Olcut | Deger |
|---|---|
| Manga koku, toplam dosya | 23.898 (23.752 cbz, 68 jpg, 35 json, 22 webp, 14 png, 4 avif, 2 epub, 1 .temp) |
| Ust duzey seri klasoru (kokte) | 43 (41'inde cbz var; 6'si Re:Zero) |
| Suwayomi serisi (`suwayomi/mangas/<Kaynak>/<Seri>`) | 155 seri, 20.421 cbz, 12 kaynak |
| Kamiyomu serisi | 6 seri, 245 cbz (5'i Re:Zero ile ilgili ya da Haimiya/Evangelion) |
| Kokte basibos dosya | 27 (ekran goruntusu/kapak gorselleri, 1 epub) |
| LN koku | 181 dosya (134 epub, 47 pdf); yalniz 1 Re:Zero disi seri (Alya, 9 dosya); gerisi Re:Zero |
| 0 bayt dosya | 0 |
| Bozuk/okunamayan zip (cbz+epub, 23.896 dosya tarandi) | 0 |
| Gorsel sayisi <=2 olan cbz | 197 (cogu yarim bolum/omake, bozuk sayilmadi; 1 gorselliler listelendi) |
| Toplam sorun basligi | 14 (asagidaki tablo) |

Genel durum: dosyalar saglam, format desteklenen (cbz/epub/pdf). Asil sorunlar adlandirma tutarsizligi, ayni serinin birden cok klasorde bulunmasi ve Komga'nin seri algisini bulandiran yapi.

## En onemli sorunlar

| # | Yol (manga kokune gore) | Sorun | Onerilen yeni ad / eylem |
|---|---|---|---|
| 1 | `Oshi no Ko`, `Oshi_no_Ko`, `Oshi_no_Ko_1`, `_Oshi_no_Ko_` (+ `suwayomi/.../MangaKatana (EN)/Oshi no Ko`) | Ayni seri 5 klasorde (101/166/173/101/177 cbz); Komga bunlari 5 ayri seri gosterir | Tek klasor `Oshi no Ko`; digerleri icerik karsilastirilarak birlestirilmeli (silme yalniz onayla) |
| 2 | `Class_De_2_Banme_...Natta`, `..._Natta_1`, `Class_de_2-banme_ni_Kawaii_Onnanoko_to_Tomodachi_ni_Natta` | Ayni seri 3 klasor, 3 farkli buyuk/kucuk harf ve yazim; `_1` icinde 54-55 numarali bolumler eksik | `Class de 2-banme ni Kawaii Onnanoko to Tomodachi ni Natta` (tek) |
| 3 | `Neon_Genesis_Evangelion`, `Shinseiki_Evangelion`, `kamiyomu/Neon Genesis Evangelion` | Ayni seri uc klasorde (99/97/84 cbz) | Tek seri: `Neon Genesis Evangelion` |
| 4 | `The_Angel_Next_Door_Spoils_Me_Rotten_After_The_Rain`, `Otonari_no_Tenshi-sama_..._Sareteita_Ken`, `..._Ken_after_the_rain`, suwayomi `The Angel Next Door Spoils Me Rotten` | Ayni evren/seri 3+1 klasor, Japonca ve Ingilizce baslik karisik; "After the Rain" ayri seri olmali ama adlari tutarsiz | `The Angel Next Door Spoils Me Rotten` ve `The Angel Next Door Spoils Me Rotten - After the Rain` |
| 5 | `Haimiya-senpai [Pixiv Edition]`, `Haimiya-senpai wa Kowakute Kawaii`, `kamiyomu/Haimiya Is Scary Cute`, `kamiyomu/Haimiya-senpai is Scary and Cute`, suwayomi MangaDex `Haimiya Is Scary Cute` | Ayni seri 5 klasor, 3 farkli baslik; `[Pixiv Edition]` etiketi; kokteki ikisi root sahipli ve 777 | `Haimiya-senpai wa Kowakute Kawaii` (tek); Pixiv surumu gerekirse alt etiketsiz ayri seri olarak `Haimiya-senpai wa Kowakute Kawaii - Pixiv` |
| 6 | `Tune_In_To_The_Midnight_Heart` ve `Mayonaka_Heart_Tune` (+ suwayomi Mangahere `Mayonaka Heart Tune`) | Ayni seri Ingilizce/Japonca iki klasor (105 ve 65 cbz) | `Mayonaka Heart Tune` |
| 7 | Kokteki `*_B_l_m_*` dosyalari: `Chainsaw_Man`, `Jujutsu_Kaisen`, `Vagabond`, `Mayonaka_Heart_Tune`, `Oshi_no_Ko`, `Remote_Jugyou_...`, `Ushiro_no_Seki_...`, `..._after_the_rain` (toplam ~1.100 dosya) | Turkce "Bolum" kelimesindeki `o` ve `u` silinmis ("B_l_m"); ad basinda 0 tabanli sira no (`0_B_l_m_1.cbz`, `10_B_l_m_11.cbz`), doldurma yok | `Chainsaw Man - Ch.001.cbz` bicimi; sira oneki kaldirilip bolum numarasi 3 hane doldurulur |
| 8 | Kokteki Mihon/Tachiyomi biçimi: `Class_De_2..`, `Frieren_...`, `Alya_Sometimes_...`, `Yotsuba_to_`, `Neon_...` vb. | `0_Chapter_0.cbz`, `10_Chapter_10_Yuri_Sisters_I_do3.cbz`; alt cizgi ve sira oneki, `chapter/Chapter` buyuk-kucuk karisik, `I_do3` / `I_Do4` gibi bozulmus basliklar; sifir doldurma yok (0,1,10,100) | Tek bicim: `<Seri> - Ch.### - <Baslik>.cbz` (Komga dogal siralama yaptigi icin sirasi bozulmaz, ancak Kavita/dosya yoneticilerinde bozulur) |
| 9 | Suwayomi icindeki kaynak klasorleri (`suwayomi/mangas/<Kaynak>/...`, 12 kaynak, 155 seri) | Komga "Manga" kutuphanesi koku tum Suwayomi ciktisini da seri olarak tarar; ayni seri farkli kaynaklarda tekrar (Bleach: MANGA Plus + Weeb Central; Chainsaw Man, Jujutsu Kaisen, Vagabond, Girls' Last Tour, Bocchi Side Story, Frieren, Alya vb. hem kokte hem Suwayomi'de) | Suwayomi'yi ayri kutuphane/koke tasimak ya da Komga'da `suwayomi` klasorunu dislamak; tekrarlar kaynakla birlestirilmeli |
| 10 | Suwayomi dosya onekleri: `Official_Chapter N.cbz`, `Unknown_Chapter N.cbz`, `www.kakamanga.com_Chapter N.cbz`, `www.natomanga.com_Chapter N.cbz`, `official_Ch. N - (1r0n).cbz`, `<Tarama grubu>_Vol.X Ch.Y.cbz` (MangaDex) | Kaynak/scanlator/site adi dosya adina gomulu; 12 kaynakta 8 farkli kalip; `Vagabond/Unknown_# N.cbz` (327 dosya) bolum sozcugu bile yok; Komga'nin sayi cozumleyicisi ilk sayiyi (`1r0n`, `Vol`) yanlis alabilir | Suwayomi indirme sablonunu `<Seri> - Ch.###.cbz` yapmak; mevcutlari toplu yeniden adlandirma (yalniz oneri) |
| 11 | `suwayomi/.../MangaFire (EN)`, `MangaDex (EN)`, `Mangatown (EN)` vb. | Ayni bolumun birden cok surumu: orn. Komi 1.106 dosya (523 ayri bolum sayisi cakismasi), Go-Toubun no Hanayome 122, Shikimori 196, Nagatoro 192, Haimiya (MangaDex) 49, Yotsuba&! 12, Angel Next Door 21; `(1)` kopyalar (54 dosya: Yotsuba&! 8, Go-Toubun 7, Slam Dunk 7, Promised Neverland 7, Kuroko Replace Plus 11, vb.); Komi'de 13 dosyada cift bosluk | Cakisan numaralari tek surume indirgemek (once icerik karsilastirmasi gerekir); `(1)` kopyalar ayni boyutluysa kopya adaylari |
| 12 | Kok dizin (27 basibos dosya) | `Chainsaw_Man-3.0-15_2025-10-06_1209.avif`, `Class_de_2-b-*.png`, `Frieren_Beyo-79.0-13_*.jpg`, `JoJo_s_Bizar-*.jpg`, `Kaoru_Hana_w-*.avif`, `Otonari_no_T-16.0-*.jpg`, `Re_ZERO_-Sta-*.jpg`, `b3276819-....png` (ekran goruntusu/sayfa kaydi benzeri); 6 dosya `(1)` kopyasi/ayni boyut; bir de `Alya ... Momoco's Art Book [Yen Press].epub` (LN, manga kutuphanesinde) | Gorselleri kutuphane disina (orn. `_ekran-goruntuleri/`) tasimak; epub'u `ln` altina `Alya/` serisine tasimak (Re:Zero gorselleri sadece listelendi) |
| 13 | `Alya/` (manga kokunde, 750 izin) ve `Alya/...Volume 05 [Yen Press][Kobo].epub.temp` (28,9 MB) | Yarim kalmis indirme (`.temp`); klasor LN dosyalariyla manga kutuphanesinde; izin 750 flugel oldugu icin Komga konteyneri okuyamayabilir | `.temp` silinmeden once yeniden indirmeyi dogrula; klasor `ln/books/English/Alya` altina tasinabilir (zaten 9 dosya orada) |
| 14 | `ln/books/English/Alya/` | Cilt adlandirmasi tutarsiz: `... - Volume 03 [Yen Press][Kobo].epub`, `...Volume 04.5...`, `...Volume 07 [Yen Press][Stick].epub`, `Sunsunsun & Momoco - Alya Sometimes Hides Her Feelings in Russian 08.epub`; Vol 05 hem epub hem pdf (`[Kobo_LNWNCentral]`); Vol 01, 02 yok; kutuphane tag'lari `[Yen Press][Kobo]` | `Alya Sometimes Hides Her Feelings in Russian - Volume 08 [Yen Press].epub`; epub/pdf cift ise birini ayri klasore ayirmak; Vol 1-2 eksik |

## Ayrintili bulgular

### 1. Seri klasoru adlari
- Karisik stil: `Haimiya-senpai wa Kowakute Kawaii` (bosluklu), `Oshi_no_Ko` (alt cizgili), `Oshi no Ko` (bosluklu), `_Oshi_no_Ko_` (basta/sonda alt cizgi), `Kaguya-sama_Love_is_War_Colored_Edition_` ve `Ushiro_no_Seki_no_Gal_ni_Sukarete_Shimatta_Mou_Ore_wa_Dame_Kamoshirenai_` ve `Yotsuba_to_` (sonda alt cizgi; orijinal `?`/`!`/`&` karakterinin yerine konmus).
- Alt cizgi, yasakli karakter (`:`, `?`, `'`) yerine kullanilmis: `Frieren_Beyond_Journey_s_End`, `Bocchi_the_Rock_Side_Story_Kikuri_Hiroi_s_Heavy-Drinking_Diary`, `JoJo_s_Bizarre_Adventure_Part_8_JoJolion`.
- Suwayomi'de de ayni durum: `The Angel Next Door Spoils Me Rotten_ After the Rain`, `Konosuba_ An Explosion on This Wonderful World!`, `Trapped in a Dating Sim_ ...` (`:` yerine `_`).
- Windows'ta yasak karakter (`<>:"|?*\`): yalniz `kamiyomu/Re:ZERO...` altinda (Re:Zero, 59+14+6 ad; yalniz not). Windows/SMB uzerinden bu klasorler acilamaz ya da bozuk gorunur.
- Ad uzunlugu: `Otonari_no_Tenshi-sama_ni_Itsunomanika_Dame_Ningen_ni_Sareteita_Ken_after_the_rain` gibi 80+ karakter; dosya adlarinda 255 bayt sinirina yakin olan yok.
- Sonda bosluk/nokta olan klasor yok; dosya adlarinda 16 yerde bos baslik (` - .cbz`), yalniz Re:Zero Dai 3-shou klasorunde.
- Cift bosluk: `Oshi no Ko - Vol.3 Ch.29 - Carbon  Copy.cbz`; MangaFire/Komi 13 dosya; MangaDex JoJolands 1 dosya.
- Etiketli ad: `Haimiya-senpai [Pixiv Edition]`, `Kaguya-sama_Love_is_War_Colored_Edition_` (icinde cbz yok, yalniz `cover.jpg` + `index.json`).

### 2. Cilt/bolum numaralandirma
- Siralama: kokteki serilerde `0.cbz, 1.cbz, 10.cbz, 100.cbz` gibi doldurmasiz sayilar (Yotsuba, Chainsaw, Vagabond...). Komga dogal siralama yapar; Kavita/ham `ls`/SMB ayrimi siralamayi bozar.
- Dolgulu ve dolgusuz karisik: `kamiyomu/Haimiya Is Scary Cute` icinde `Ch.0014.cbz` (4 hane) ve `Ch.014.6.cbz` (3 hane + ondalik) birlikte.
- `Cilt/Vol/Volume/v` karisimi: `Vol.3 Ch.29` (Oshi no Ko), `Volume 05` (Alya), `Vol 2 Ch 6` (Haimiya), `Cilt 26-33` (Turkce LN, Re:Zero), `Quarter/Loss/Song/Episode/#` (Weeb Central).
- Eksik sayi (guvenilir yalniz duzgun serilerde): `Chainsaw_Man` 225; `Class_De_2..._Natta_1` 54-55; `Slam Dunk` bolum 277; `Berserk` 83; `Danjo no Yujou...` 24,30,32,39; `Hokkaido Gals...` 26,56,83,103; `Nee, Mou Isso...` 38,39,54,55; `The Fragrant Flower...` 188-193; `DARLING in the FRANXX` 61-68; `Garbage Time` 107,133,150+. Diger "eksik" hesaplari (JoJo Part 5/6, Delicious in Dungeon, Neon Genesis kamiyomu) bolum numaralandirmasi surekli degil/yarim bolum yuzunden guvenilir degil.
- Yinelenen bolum sayisi (ayni sayi birden cok dosya): MangaFire Komi 523, Go-Toubun 122, Nagatoro 192, Shikimori 196; MangaDex Haimiya 49, Baki-Dou 14, Angel Next Door 21, Bocchi the Rock! 10.
- Weeb Central onekleri: `Official_`, `Unknown_`; `Unknown_Chapter N` sadece kaynak bilinmedigi icin; 327 dosyali Vagabond'un tum dosyalari `Unknown_# N.cbz`.

### 3. Format ve bozukluk
- Desteklenen uzantilar: cbz, epub, pdf; bunun disinda yalniz kapak/metadata (`cover.jpg`, `index.json`, webp/png/avif) ve 1 adet `.temp`.
- 0 bayt dosya yok. 23.896 cbz/epub zip dizini sorunsuz okundu (bozuk yok).
- 197 cbz'de <=2 gorsel var; cogu `.5` yarim bolum/omake. Gerekirse tek gorselli suphelilerden bazilari: `Kimetsu no Yaiba/Chapter 169.5_ Special.cbz`, `Chapter 25.5_ Jump GIGA Special.cbz`, `Legend of the Northern Blade/Ch.130.1.cbz`, `Ch.192.5.cbz`, `Ogami Tsumiki to Kinichijou/Ch.097.1.cbz`, `Chi no Wadachi/Ch.053.cbz`, `DARLING in the FRANXX/73.cbz`, `Komi unofficial_Ch. 464/465`, `Villain with a Crush/Chapter 6.1.cbz`.
- `Alya/*.epub.temp`: tamamlanmamis indirme (yukarida #13).
- Seri klasoru disi basibos dosya: 27 (kok) ve `Alya/` icinde 2 dosya. LN `Yuklenen/` klasoru bos.
- `kamiyomu` ve `suwayomi` her biri bir ust klasor ve alt klasorleri olan "kok" olarak duruyor; `suwayomi/thumbnails/` icinde 42 jpg (Komga'da gorunmemeli).

### 4. Komga seri algisini bozabilecek yapi
- Kok dizinde hem 45 alt klasor hem 27 dosya (`.` satirinda karisim): Komga kokteki dosyalari tek kitaplik "oneshot" seri olarak algilayabilir; epub ve gorseller kutuphaneye bulasir.
- `suwayomi/` ve `kamiyomu/` icinde karisik klasor/dosya yok (yapi temiz: Kaynak -> Seri -> bolum.cbz), ancak Komga icin `Kaynak (EN)` seviyesi bir "koleksiyon"/ara klasor olur; ayni seri adi birden cok kaynakta oldugundan Komga ayni adli bircok seri gosterir.
- `ln/books/` altinda 3 seviye (`English/ReZero/<tur>`, `Turkce/ReZero/...`): Komga yaprak klasorleri seri sayar; Kavita ise klasor yapisini "kutuphane kokunden alt klasor" olarak okur. Re:Zero disi tek seri `English/Alya` (duz, sorun yok).
- Izinler: kokteki bazi klasorler `root:root` (`Oshi no Ko` 755, `Haimiya-senpai ...` x2 777, ReZero... 755), `Alya` 750 flugel; Komga konteyneri farkli bir kullanicidaysa bu klasorler okunamayabilir (konteyner UID'si dogrulanmadi).
- Cok sayida seri icinde yalniz `cover.*` + `index.json` metadata dosyasi bulunuyor (Mihon/Tachiyomi uyumlu); bunlar Komga icin sorun degil ama Kaguya Colored klasoru icin kitap yok, seri bos gorunur.

## Notlar ve sinirlar
- Eksik bolum hesaplari ad-bazli tahmindir; kaynak sitelerin bolum numaralandirmasi (JoJo, Delicious in Dungeon, Komi f2 surumleri) bunu bozar.
- Komga/Kavita'daki gercek seri gruplamasi API ile dogrulanmadi (yalniz dosya sistemi incelendi).
- Re:Zero klasorleri (manga ve ln, kamiyomu, suwayomi) yalniz listelendi, hicbir oneri/degisiklik yapilmadi.
