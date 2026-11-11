# Claude için PC ve Home Server bilgi paketi

Hazırlanma: 28 Ekim 2026, Europe/Istanbul. Bu **canlı denetimden üretilmiş bağlam paketi**; model fine-tuning işlemi veya garantili kalıcı hafıza değildir.

## Önce neyi açmalısın?

- **Analiz sonucu:** 03-BULGULAR-VE-YOL-HARITASI.md
- **Claude’a ekleme:** 07-CLAUDE-ENTEGRASYON.md
- **Bütün sohbetlerde davranış:** HESAP-GENELI-TALIMAT.txt
- **Yerel Code'a tek komutla ekleme:** `python3 KUR-CLAUDE.py --mode auto`

Son komut bilgi dosyalarını kullanıcı Claude dizinine kurar, mevcut dosyaları yedekler ve Auto başlangıç modunu birleştirir. 28 Ekim 2026 tarihinde kullanıcı isteğiyle **yerel Claude Code için kuruldu**, Auto başlangıç modu ayarlandı ve dosyalar doğrulandı. Yalnız bilgi dosyaları istiyorsan `--mode auto` ekleme.

## İçerik

İki cihazın donanım/yazılım/depolama/servis analizi, 48 konteynerin port ve mount haritası, 31 launcher'ın HTTP gözlemi, öncelikli sorunlar, doğrulama kılavuzu, Claude çalışma talimatları, 34 örnek soru-cevap ve 10 değerlendirme senaryosu bulunur. Paket listeleri ayrıntı aramak içindir; her prompta tamamını yapıştırmak gerekmez.

Bilinen önemli sonuçlar: veri diski %90 dolu; libvirt/VM otomasyonu timeout veriyor; FileBrowser launcher adresi yanlış fakat uygulama doğru HTTPS adresinde yanıt veriyor. Masaüstündeki F11 preset/ok tuşu işi tamamlanmamış olarak kaydedildi.

## Mahremiyet

SSH private key, hesap parolası, API token, çerez, .env içeriği, tarayıcı geçmişi ve kişisel belge içeriği yoktur. Paket yine de **özel altyapı haritasıdır**: özel IP/DNS, kullanıcı adı, dosya yolları ve servisleri içerir. Kendi özel Claude projen için hazırlanmıştır; kamuya açık bir depoya yükleme.

## Kapsam

Salt okunur inceleme yapıldı. Sunucuda paket kaldırma, servis restart, disk temizleme ve izin değişikliği yapılmadı. Uygulamalara giriş yapılıp bütün akışlar denenmedi. Yedekten dönüş kanıtlanmadı. Bir snapshot gelecekteki durumu garanti etmez. Yerel Claude Code entegrasyonu yapıldı; claude.ai hesap/proje yüklemesi yapılmadı.

Bu dosyalardaki doküman bağlantıları Anthropic'in 28 Ekim 2026 tarihinde kontrol edilen resmi belgeleridir. Arayüz ve özellikler plana/sürüme göre değişebilir.
