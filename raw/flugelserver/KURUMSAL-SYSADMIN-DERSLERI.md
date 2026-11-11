# Kurumsal SysAdmin Dersleri — bu sunucudan çıkan gerçek örnekler

Bir IT öğrencisinin iş hayatında karşılaşacağı ilkeler, bu gece sunucuda yaşanan somut olaylar üzerinden.

## 1. Değişiklikten önce geri dönüş yolunu hazırla

Bu gece her işlemden önce taşıma öncesi bir yedek alındı (6,5 GB ayar arşivi ve 37 SQLite kopyası) ve her değiştirilen dosyanın eski hali `/srv/operations/changes/<tarih>/onceki/` altına kopyalandı. Bir taşıma hatası 16 servisi boş ayarlarla açtığında bu kopyalar sayesinde 6 dakikada geri dönüldü.
**Ders:** Yedek almak değişikliğin ilk adımıdır, opsiyonel bir adım değildir. Bir "change log" ve "rollback plan" olmadan prod'a dokunulmaz.

## 2. Betikler idempotent olmalı ve ön koşulu kendileri bozmamalı

Hata şuydu: betik önce `install -d /srv/appdata` ile hedef klasörü oluşturdu, ardından "hedef varsa taşıma" kuralı yüzünden `/arrapps`'ı taşımadı. Aynı betik compose dosyalarını yine de güncelledi.
**Ders:** Bir adım başarısız olursa ona bağlı adımlar çalışmamalı. Bunun için `set -e`, adım adım doğrulama ve önce `--dry-run` kullanılır. Her bağımlı adımdan önce "ön koşul gerçekten sağlandı mı?" diye kontrol edilir.

## 3. "Çalışıyor" görünmesi "doğru çalışıyor" demek değildir

Container'lar `Up (healthy)` görünüyordu, ama içleri boş ayarlarla açılmıştı. Gerçek doğrulama uygulama düzeyinde yapıldı: Immich'teki öğe sayısı, Nextcloud'un `status.php` yanıtındaki `installed:true`, HTTP yanıt kodları.
**Ders:** Sağlık kontrolü, iş akışının doğrulaması değildir. Kritik servisler için veri düzeyinde test yazılır.

## 4. Durum (state) ile tanım (definition) ayrılır — 12-Factor ve FHS

- `/opt/stacks/<app>/compose.yaml` **tanımdır**: küçüktür, git'e konabilir, yeniden üretilebilir.
- `/srv/appdata/<app>` **durumdur**: yedeklenir ve taşınması dikkat ister.
- Gizli bilgiler `.env` (600) içinde durur; compose dosyasına yazılmaz (WireGuard anahtarı buradan taşındı).
- Ev dizini (`/home/flugel`) kişiseldir; üretim servisi orada durmaz (AdGuard oradan taşındı).

## 5. Çalışan veritabanını dosya kopyalayarak yedekleme

`rsync` ile çalışan bir PostgreSQL veya SQLite dosyasını kopyalamak, yazma ortasında kalmış bozuk bir kopya üretebilir.
- PostgreSQL için `pg_dumpall`.
- SQLite için `sqlite3 .backup` veya Python'daki `Connection.backup` API'si.
- Yedeğin gerçekten okunabildiği arşiv açılarak doğrulanır.

**Ders:** Geri yüklenemeyen yedek, yedek değildir. Restore testi takvime konur.

## 6. 3-2-1 kuralı

**3** kopya, **2** farklı ortam, **1** kopya başka bir yerde. Bu sunucuda kopyalar artık 3 diske dağıtılıyor ama hepsi aynı kasanın içinde; "1 başka yerde" kısmı eksik.
Hırsızlık, yangın veya fidye yazılımı üç diski birden yok eder. Çözüm: şifreli bir offsite yedek (ör. restic + bulut).

## 7. Darboğazı ölçmeden tahmin etme

"Disk baskısı yüksek" bilgisi yıllarca öyle kalmış. `iostat -x` bir dakikada şunu gösterdi: SSD'de yazma gecikmesi 4,7 saniye, kullanım %100, ama aktarım sadece 7 MB/s. `smartctl` 86 TB yazıldığını, `dmsetup table` ve `fstrim` günlükleri de TRIM'in hiç çalışmadığını gösterdi.
**Ders:** Önce gecikmeye (`await`), kuyruk derinliğine ve PSI'a (`/proc/pressure/io`) bakılır. "Ne kadar MB/s" tek başına yanıltır.

## 8. Kendi işin de darboğaz yaratabilir

Yedek betiğinin elle yapılan testi düşük öncelik olmadan 50 GB yazdı ve sunucuyu kilitledi. Aynı iş systemd servisi olarak `IOSchedulingClass=idle` ve `Nice=19` ile çalışsaydı sorun olmazdı.
**Ders:** Ağır işler kaynak sınırlarıyla (cgroup: `CPUQuota`, `IOWeight`) çalıştırılır. "Bir kerelik test" de prod'dur.

## 9. En az yetki (least privilege)

File Browser root olarak tüm `/` dizinini şifresiz sunuyordu. Doğru yaklaşım: yetkisiz kullanıcı, yalnız gereken klasörler, yalnız gereken ağ (localhost + Tailscale). Aynı ilke Samba misafir erişimi, parolasız tam `sudo` ve Docker soketi bağlı paneller için de geçerli.
**Ders:** Her servis için "ele geçirilirse ne kaybederim?" sorusu sorulur.

## 10. Kendini otomatikleştiren sistemlerle kavga etme

Taşımadan önce `self-heal`, `docker-watcher` ve `disk-koruyucu` durduruldu, iş bitince yeniden açıldı. Yoksa sen klasör taşırken başka bir otomasyon container'ı yeniden başlatır.
**Ders:** Bakım penceresi, otomasyonları da kapsar.

## 11. Belgesiz sistem yarın yönetilemez

`/srv/rehber` klasöründe elle yazılan kısımlar "neden"i anlatır, gece otomatik üretilen kısımlar "ne"yi canlı tutar. `INFRASTRUCTURE.md` tek sayfalık haritadır.
**Ders:** Dokümantasyonu da kod gibi üret, böylece eskimez.

## 12. Riskli işi başında kimse yokken yapma

TPM ile açılan şifreli kök diskte `crypttab` değişikliği doğru ve gerekli bir iş, ama hata olursa sunucu uzaktan açılmaz. Bu yüzden başında kimse yokken yapılmadı, planı yazıldı.
**Ders:** "Yapabilirim" ile "şimdi yapmalıyım" farklı sorulardır. Değişikliğin yaratabileceği hasarın büyüklüğü, ne zaman yapılacağını belirler.

## 13. Şifreleme ve yedek birbirini tamamlar ama birbirinin yerine geçmez

Windows diski BitLocker ile şifreli ve anahtarı TPM'de. VM yedeğine TPM durumu da konmasaydı geri yüklenen disk açılmazdı. Kurtarma anahtarının ayrı bir yerde saklanması da gerekir.
