---
tur: proje
etiketler:
  - proje
  - flugelserver
  - home-server
  - flugel-akis
  - docker
  - tailscale
  - android
durum: aktif
olusturma: 2026-11-11
guncelleme: 2026-11-11
---

# Flugel Sunucu, Araç Takımı ve Kişisel Sosyal Akış (`flugelserver` & `flugel-akis`)

> Üst bağlantı: [[HARITA]] · Odak: [[simdi]] · Bağlam: [[hafiza]] · Kararlar: [[kararlar]] · Sorumlu: [[kisiler/ahmet-gokalp-goksu]]

## Genel Bakış ve Kapsanan Depolar
Ev sunucusu **flugelserver** (Ryzen 2600X, GTX 1660 Ti, 15 GB RAM, Ubuntu 26.04, LAN `192.168.0.15`, Tailscale `100.86.88.1` / `flugelserver.tail42f1f4.ts.net`) üzerindeki 37 Docker yığınını, KVM/libvirt sanal makinelerini (`W11-GPU`, `W11`, `mullvad-ts`), otonom bakım/izleme betiklerini, Android sunucu istemcisini ve X tarzı kişisel haber/medya platformu **FLUGEL Akış**'ı kapsayan bütünleşik altyapı projesidir.

1. **`desktop-server-toolkit`** (`https://github.com/gok8lp/desktop-server-toolkit` — Açık, JavaScript/Python/Shell, Güncelleme: `2026-10-29T19:34:16Z`)
   - Linux masaüstü ve ev sunucusu için GNOME eklentileri, 37 Docker yığını yapılandırması, Cloudflare tünel tanımları, sanal makine şemaları, kişisel haber akışı ve `temizle.py` ile kişisel verilerden arındırılmış bakım araçları.
2. **`home-server`** (`https://github.com/gok8lp/home-server` — Açık, Python/Shell, Güncelleme: `2026-10-22T22:53:35Z`)
   - Ev sunucusu mimari belgeleri, Docker yığınları, systemd zamanlayıcıları (`self-heal`, `ai-gozcu`, `docker-watcher`, yedekleme), ağ/erişim ve sanal makine yapılandırma örnekleri.
3. **`home-server-android`** (`https://github.com/gok8lp/home-server-android` — Açık, Kotlin/Python, Güncelleme: `2026-10-22T22:53:32Z`)
   - Docker konteynerlerini, canlı bildirimleri ve sanal makine durumlarını (root gerektirmeyen masaüstü/VM geçişleriyle) izlemek için Android istemcisi ve kapsamlı yerel Python API prototipi.
4. **`flugel-akis` (FLUGEL Akış)** (`/opt/stacks/panel/akis/`, `:3012` LAN ve `:8443` Tailscale Serve)
   - Python standart kütüphanesi (`akis.py`), SQLite (`akis.db`) ve çerçevesiz (vanilla) web arayüzüyle çalışan kişisel sosyal akış.
   - **61 Kaynak:** 36 RSS (oyun, teknoloji, gündem, PlayStation, anime/manga) + 25 YouTube kanalı.
   - **Yerel AI (Ollama `gemma3`):** EN/JA → TR çeviri, 0-100 önem puanı, tekrar eden haberleri "+N kaynak" altında birleştirme ve gerçek bağlamlı sohbet.
   - **Modüller:** Anime & Manga (yasal izleme linkleri, 3B eğimli kapaklar, geri sayım), Oyun fiyatları (Steam TR, CheapShark, Epic), Maçlar (Süper Lig, Avrupa ligleri, NBA ve [[projeler/hakemlik]] görevleri), Sunucu tazelik tablosu ve özel Android WebView APK'sı (`~/sistem-bakim/flugel-apk`).

## Mevcut Durum (11 Kasım 2026)
- **Sunucu ve Akış:** Aktif olarak çalışıyor. GPU VM (`W11-GPU`) açıkken GPU kullanan konteynerlerin (`ollama`, `jellyfin`, `plex`, `immich_machine_learning`, `subgen`) bilerek durdurulması `self-heal` ve `ai-gozcu` tarafından hata sayılmayacak şekilde düzeltildi.
- **Bayatlık Notu (>14 Gün Kuralı):** `home-server` ve `home-server-android` depolarının son GitHub commit tarihi `2026-10-22` olup 14 günü aşmıştır (20 gün); `desktop-server-toolkit` ise `2026-10-29` (13 gün) ile günceldir.

## FLUGEL Akış Herkese Açık + Mobil Uygulama 2.0 (5 Kasım 2026)
- Akış yeniden açıldı ve **https://akis.gokalpgoksu.com** üzerinden şifresiz, Tailscale'siz erişilebilir (`cloudflared-akis` → `localhost:3012`).
- Yeni Android kabuğu `FLUGEL-Akis.apk` 2.0 (`com.flugel.akis.app`): eski 1.0 yalnız Tailscale `:8443` adresini açıyordu ve çalışmıyordu.
- AI özellikleri (özet, sohbet, çeviri) Ollama kaldırıldığı için kapalı.
- Ayrıntı, derleme, imza anahtarı yeri ve geri alma: [[notlar/flugel-akis-mobil-uygulama]].

## Sıradaki Adımlar ve Açık Kararlar
- [ ] **FLUGEL-Akis.apk telefonda dene:** Emülatörde doğrulandı, gerçek telefonda henüz kayıtlı test yok.
- [ ] **Tailscale Funnel Kararı:** Jellyfin ve Immich (`:10000`) üzerinde açık olan Tailscale Funnel'ın kapatılıp yalnızca Tailnet/Cloudflare üzerinden erişime sınırlandırılması (kullanıcı onayı bekliyor).
- [ ] **DNS Temizliği:** `adguard.gokalpgoksu.com` A kaydının Cloudflare panelinden silinmesi.
- [ ] **Servis Bakımı:** Port 10000 çakışması nedeniyle yeniden başlayan `webmin` servisinin incelenmesi ve `W11` yeniden başlatma UEFI takılmasının (AVIC/Hyper-V) kök neden analizi.
- [ ] **Akış İyileştirmesi:** FLUGEL Akış Sunucu sayfasındaki gerçek haber gecikmesi ölçümlerinin doğrulanması ve Türkçe README'nin genişletilmesi.

## Öne Çıkan Commit Geçmişi
- `desktop-server-toolkit` — `9eb5961` (2026-10-22): `docs: introduce desktop and server toolkit`
- `desktop-server-toolkit` — `dce83a5` (2026-10-17): `sunucu: tüm yapı depoda — 37 Docker yığını, servisler, betikler, Cloudflare tüneli, sanal makine tanımları, mullvad-ts masaüstü betikleri; IP/alan adı/gizliler temizle.py ile çıkarıldı`
- `home-server` — `19ce8e0` (2026-10-22): `docs: clarify project purpose, setup and repository naming`
- `home-server` — `99230c7` (2026-10-17): Ayrıntılı mimari, ağ, depolama, yedekleme, izleme, güvenlik ve sanal makine belgeleri
- `home-server-android` — `3577d74` (2026-10-22): `docs: clarify project purpose, setup and repository naming`
- `home-server-android` — `00c5ef7` (2026-10-17): Doğrulanmış Android test APK'sı ve sertleştirilmiş sürüm iş akışı
- `home-server-android` — `6e984b3` (2026-10-17): Canlı bildirimler ve root gerektirmeyen masaüstü geçişi için sunucu API uyumu

## İlgili Sayfalar ve Bağlantılar
- **Harita ve Kök:** [[HARITA]] · [[simdi]] · [[hafiza]] · [[kararlar]] · [[dersler]]
- **İlgili Projeler ve Kişiler:** [[projeler/duduk]] · [[projeler/flugel-manga]] · [[projeler/linux-masaustu-araclari]] · [[kisiler/ahmet-gokalp-goksu]]
- **Wiki Sayfaları:**
  - [[wiki/flugelserver-genel-mimari]]
  - [[wiki/flugelserver-docker-uygulamalari]]
  - [[wiki/flugelserver-uygulama-baglantilari]]
  - [[wiki/flugelserver-dosya-agaci-ve-diskler]]
  - [[wiki/flugelserver-yedekleme-ve-otomasyon]]
  - [[wiki/flugelserver-sanal-makineler-ve-gpu]]
  - [[wiki/flugelserver-ag-guvenlik-ve-tuneller]]
  - [[wiki/flugel-akis-ve-botlar]]
  - [[wiki/repo-desktop-server-toolkit]]
  - [[wiki/repo-home-server]]
  - [[wiki/repo-home-server-android]]
- **Bilgi Notları:**
  - [[notlar/cloudflare-ve-tailscale-baglanti-zinciri]]
  - [[flugelserver-genel-mimari]]
  - [[notlar/flugel-akis-mobil-uygulama]]

> Kaynaklar: `raw/flugelserver/FLUGEL-OZET.md`, `raw/github/00-github-envanteri.md`, `raw/github/01-tum-repolar-commit-gecmisi.md`
