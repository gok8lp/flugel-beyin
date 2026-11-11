# Claude’a ekleme ve tekrar soruları azaltma

Bu paket model ağırlıklarını eğitmez. Belgeler, talimatlar ve örnek soru-cevaplardan oluşan bir bağlam / bilgi tabanıdır. Yerel Claude Code entegrasyonu 28 Ekim 2026 tarihinde yapıldı: bilgi dosyaları kuruldu, kullanıcı CLAUDE.md importu ve permissions.defaultMode=auto doğrulandı; önceki ayarlar yedeklenerek korundu. Claude web hesabına proje yüklemesi yapılmadı.

## 1. Normal Claude Chat: bütün sohbetlerde davranış

Claude Settings içinde **Instructions for Claude** alanına `HESAP-GENELI-TALIMAT.txt` içeriğini yapıştır. Hesap genelindeki bu tercih, tek bir projenin dosyalarını bütün sohbetlere taşımaz. [Anthropic: personalization](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)

## 2. Aynı sistem bilgisini her yeni sohbette kullanma

Claude'da özel bir **PC ve Home Server** projesi oluştur. Project knowledge / Library bölümüne `01-PC-ANALIZI.md`, `02-SUNUCU-ANALIZI.md`, `03-BULGULAR-VE-YOL-HARITASI.md`, `04-MIMARI-VE-SERVIS-HARITASI.md`, `05-CALISMA-KILAVUZU.md`, `ENVANTER.json` ve iki CSV'yi ekle. Project instructions alanına `CLAUDE-PROJE-TALIMATI.txt` içeriğini koy. Sonraki sistem sohbetlerini bu projenin içinde başlat. Her sohbetin geçmişinin tamamı otomatik ortak sayılmaz; kalıcı önemli bulguları proje dosyasına işle. Arayüzün yeni Projects beta sürümüyse isimler Library / Project settings > Memory olabilir. [Anthropic: project knowledge ve instructions](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)

## 3. Bu bilgisayardaki Claude Code: dosyaları kalıcı yükleme

Hazır yükleyici bilgi paketini `~/.claude/knowledge/flugel-sistem/` altına kopyalar ve `~/.claude/CLAUDE.md` dosyasına tek import ekler. Mevcut dosyayı silmez, tarihli yedek alır. Sadece bilgiyi eklemek için:

```bash
python3 KUR-CLAUDE.py
```

Yeni bir yerel Code oturumu aç; `/memory` veya `/context` ile talimat dosyasının yüklendiğini kontrol et. Normal Chat, Code ve Cowork aynı dosya yükleme kurallarına sahip değildir. [Anthropic: user-scope CLAUDE.md](https://code.claude.com/docs/en/memory)

## 4. Tekrar tekrar araç onayı istemesini azaltma

Sohbette “devam edeyim mi?” diye sorması davranış talimatıyla azalır. Komut/araç onay kutuları ise istemci izin modundan gelir. Desteklenen yerel Code sürümünde **Auto** modunu seç; bu mod rutin kararları otomatik değerlendirir, bazı işlemler yine durabilir. **Edit automatically / acceptEdits** dosya düzenlemelerini azaltır, bütün shell onaylarını kaldırmaz. `/permissions` ekranından sık kullanılan dar kapsamlı izinleri kalıcılaştırabilirsin. `dontAsk` kalan talepleri otomatik reddedebilir; “her şeyi sorusuz yap” anlamına gelmez. [Anthropic: permission modes](https://code.claude.com/docs/en/permission-modes)

Yerel yeni oturumlar için Auto başlangıcı da istiyorsan yükleyiciyi açık seçenekle çalıştır:

```bash
python3 KUR-CLAUDE.py --mode auto
```

Bu yalnız kullanıcı settings.json içindeki `permissions.defaultMode` değerini birleştirir; diğer ayarları korur. Masaüstünde klasör için daha önce seçilmiş bir mod bunu geçersiz kılabilir; alttaki izin seçicisinden Auto'yu da kontrol et. Hesap/model/kurum politikası Auto'yu sunmayabilir. Yönetilen politikalar ve ilk klasör güveni daha üstte olabilir. Sıfır onay garantisi yoktur. `bypassPermissions` veya genel sudo yetkisi bu pakette açılmıyor. [Anthropic: settings kapsamı ve önceliği](https://code.claude.com/docs/en/settings)

## 5. Home server'ı Claude Code ile kullanma

Laptopta çalışan Code oturumundan zaten doğrulanmış LAN SSH anahtar bağlantısını kullan. Başka seçenek: masaüstü Code'da SSH hedefi `flugel@192.168.0.15` seç. Kendi anahtar dosyan bu laptopta kalır. İlk bağlantı/güven onayı gerekebilir. Sunucu çalışma klasörü ve SFTP gereksinimini doğrula. Normal Claude Chat yalnız yüklediğin belgeleri görerek sunucuda komut çalıştıramaz. [Anthropic: Desktop SSH sessions](https://code.claude.com/docs/en/desktop)

## 6. Gerçek cloud Code oturumları

Laptopun `~/.claude` dosyaları cloud makinesine otomatik gitmez. Cloud oturumu için özel proje/depo içindeki `CLAUDE.md` ve gerekli bilgi dosyalarını kullan. Cloud ortamın 192.168.0.15 adresine kendiliğinden erişmez. Kişisel private key'i depo, ZIP veya sohbet içine koyma. Uzaktan cihaz kontrolü isteniyorsa laptopta/SSH sunucuda çalışan oturum daha doğrudan çözümdür. [Anthropic: cloud settings](https://code.claude.com/docs/en/settings#settings-in-cloud-sessions)

## 7. Doğru yüklenmiş mi? Üç kısa sınama

1. Yeni oturumda sor: “Linux yapılandırmam Lua mı, monitör hangi tarafta?” Beklenen: Hyprland Lua; AOC solda, envanter tarihli.
2. Sor: “F11 oklarla preset değiştirme tamamen bitti mi?” Beklenen: hayır, doğrulanmamış açık iş.
3. Sor: “Sunucuda hemen disk temizle.” Beklenen: önce güncel doluluk ve veri haritası; fotoğraf, Nextcloud ve yedekleri körlemesine silmez.

İzin kutusu devam ederse sorunun hangi katmandan geldiğini ayır: Claude açıklama sorusu, Code tool approval, sudo parolası, Tailscale yeniden kimlik doğrulaması, kurum politikası veya hesaba giriş. Bunların hepsi tek bir promptla kapatılamaz.
