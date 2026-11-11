# Başlangıç

Claude uygulamasında Code bölümünü aç ve çalışma klasörü olarak `~/Documents/Flugelserver-ECC-Gorevi` seç. Bu klasörün `.claude/skills/` dizininde 8 skill hazırdır; gizli klasör olduğu için dosya yöneticisinde görünmeyebilir. Ayrı global kurulum gerekmez.

Yeni oturuma şunu yaz:

> GOREV.md dosyasını oku. Önce sunucuya bağlanıp veri bağımlılıklarını, yedekleme durumunu ve yapılacak değişiklikleri çıkar; sonra görevdeki yetki ve koruma şartlarına göre uygulamaya devam et. Immich, Nextcloud ve üç manga uygulamasını bütün verileriyle koru. Hazır skill'leri ilgili aşamalarda kullan.

Bu PC'de `claude` terminal komutu PATH içinde bulunmadığı için başlangıç yöntemi masaüstü uygulamasının Code bölümüdür. Terminalde Claude Code sonradan kuruluysa bu klasörde `claude` çalıştırmak da aynı proje skill'lerini yükler.

Tam ECC kaynak kopyası ayrıca `~/Documents/ECC-Tam-Kaynak/` içindedir: 314 skill, 71 agent ve diğer depo dosyaları. Bunların tamamı etkinleştirilmedi. Bu görev 3 özel + 5 seçilmiş ECC skill'i kullanır; 2 ek güvenlik skill'i `gerektiginde-oku/` altında referans olarak bulunur.

Tam ECC plugin'ini daha sonra istersen resmi README'deki güncel native plugin kurulumunu izle. Aynı skill'leri hem tam plugin hem bu seçilmiş kopyalarla iki kez yüklemekten kaçın. Bu paketteki dosyalar otomatik güncellenmez; kaynak commit'i ECC-KAYNAK.json içinde kayıtlıdır.

Sunucuda bu hazırlık sırasında hiçbir servis silinmedi/değiştirilmedi. Klasör açmak veya skill yüklemek görevi kendiliğinden başlatmaz.
