---
tur: not
etiketler:
  - flugelserver
  - docker
  - manga
  - light-novel
  - suwayomi
  - komga
  - kavita
  - kamiyomu
  - koharia-reader
olusturma: 2026-11-11
guncelleme: 2026-11-11
---

# Docker Manga, Light Novel Yığını ve Koharia Reader Entegrasyonu

> **Üst Harita ve Kök Bağlantılar:** [[HARITA]] · [[hafiza]] · [[kararlar]] · [[dersler]] · [[simdi]]
> **İlgili Wiki Sayfaları:** [[wiki/koharia-reader-ve-manga-ekosistemi]] · [[wiki/repo-koharia-reader]] · [[wiki/flugelserver-anime-manga-lightnovel-arsivi]] · [[wiki/flugelserver-docker-uygulamalari]]
> **İlgili Notlar:** [[notlar/docker-uygulama-baglanti-topolojisi]] · [[notlar/sunucu-anime-manga-ve-rezero-arsivi]] · [[notlar/flugelserver-uc-disk-ve-klasor-agaci]]
> **İlgili Projeler:** [[projeler/koharia-reader-flugel-manga]] · [[projeler/flugelserver-ev-sunucusu]]

---

## 1. Manga ve Kitap Sunucuları Karşılaştırma Tablosu

`flugelserver` üzerinde manga (`.cbz`) ve Light Novel (`.epub`, `.pdf`) koleksiyonunu indirmek, indekslemek ve sunmak için dört sunucu bileşeni ve bunlara bağlanan özel Android istemcisi (**Koharia Reader / Flugel Manga**) birlikte çalışır:

| Servis / Bileşen | İmaj / Konum | Port & Ağ Modu | Bellek Sınırı | Disk Bağlamaları (Volumes) | Rolü |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`suwayomi`** | `ghcr.io/suwayomi/suwayomi-server:stable` (`/opt/stacks/suwayomi`) | `container:gluetun`<br>`127.0.0.1:14567->4567/tcp` (Gluetun üzerinden) | `2g`<br>(`-Xmx1536m`) | `/srv/appdata/suwayomi:/home/suwayomi/.local/share/Tachidesk`<br>`/mnt/sidemain/media/books/manga/suwayomi:/home/suwayomi/.local/share/Tachidesk/downloads` | Ana manga kaynak tarayıcısı ve CBZ indiricisi (12 kaynak, 155 seri, 20.421 CBZ) |
| **`komga`** | `gotson/komga:latest` (`/opt/stacks/komga`) | `bridge`<br>`127.0.0.1:18296->25600/tcp`<br>(Dış port: `:8296`) | `1536m`<br>(`-Xmx512m`) | `/mnt/sidemain/media/books:/data`<br>`/srv/appdata/komga:/config` | Manga ve çizgi roman kütüphane sunucusu (OPDS, REST API, SSE `/sse/v1/events`) |
| **`kavita`** | `lscr.io/linuxserver/kavita:latest` (`/opt/stacks/kavita`) | `bridge`<br>`127.0.0.1:18295->5000/tcp`<br>(Dış port: `:8295`) | `768m` | `/srv/appdata/kavita:/config`<br>`/mnt/sidemain/media/books:/data/books` | Light Novel (EPUB/PDF — Re:Zero, Alya) ve kitap okuma/senkronizasyon sunucusu |
| **`kamiyomu`** | `marcoscostadev/kamiyomu:latest` (Eski/Arşiv) | Arşivlendi (Verisi korundu) | — | `/mnt/sidemain/appdata/kamiyomu` (DB)<br>`/mnt/sidemain/media/books/manga/kamiyomu` (6 seri, 245 CBZ) | Önceki manga indirme aracı; indirdiği Re:Zero, Evangelion ve Haimiya arşivleri Komga tarafından sunulur |
| **`yukle`** | `/opt/stacks/yukle` (`flugel-yukle.service`) | Host / `giris` nginx arkasında (`yukle.gokalpgoksu.com`) | — | `/mnt/sidemain/media/books/ln/books/Yuklenen` ve manga dizinleri | Telefondan / Koharia Reader içinden doğrudan sunucuya EPUB/PDF/CBZ yükleme servisi |

---

## 2. Sunucu Yapılandırma Detayları

### 2.1. Suwayomi (`/opt/stacks/suwayomi/compose.yaml`)
- **VPN ve IP Rotasyonu:** `network_mode: container:gluetun` ile tüm manga indirme ve kaynak sorguları Mullvad WireGuard VPN üzerinden çıkar. `vpn-ip-degistir.timer` (saatlik) ile çıkış IP'si düzenli değiştirilir.
- **Kritik Ortam Değişkenleri:**
  - `DOWNLOAD_AS_CBZ=true`: İndirilen tüm bölümler sıkıştırılmış `.cbz` arşivi olarak kaydedilir; böylece Komga ve Kavita doğrudan okuyabilir.
  - `AUTO_DOWNLOAD_CHAPTERS=false` ve `UPDATE_INTERVAL=0`: Diskin kontrolsüz dolmasını önlemek için otomatik bölüm indirme kapatılmıştır (`/usr/local/sbin/suwayomi-sinir` ve `/home/flugel/suwayomi-disk-guard.sh` ek koruma sağlar).
  - `EXTENSION_REPOS=["https://raw.githubusercontent.com/keiyoushi/extensions/repo/index.min.json"]`: Keiyoushi eklenti deposu tanımlıdır.
  - `FLARESOLVERR_ENABLED=true` ve `FLARESOLVERR_URL=http://localhost:8191`: Aynı Gluetun ağ uzayındaki FlareSolverr üzerinden Cloudflare engellerini aşar.
- **Erişim:** Sabit Docker IP (`172.17.0.2`) bağımlılığı kaldırılmış olup Gluetun üzerinde `127.0.0.1:14567->4567` olarak yayınlanır. Tailscale üzerinden `:45443` ve Cloudflare üzerinden `suwayomi.gokalpgoksu.com` (`giris` nginx Basic Auth arkasında) ile erişilir.

### 2.2. Komga (`/opt/stacks/komga/compose.yaml`)
- **Kütüphane Bağlaması:** `/mnt/sidemain/media/books:/data` bağlamasıyla tüm `manga/` ve `ln/` klasörlerini görür.
- **Bellek ve Kimlik:** `JAVA_OPTS=-Xmx512m` ve `mem_limit: 1536m` ile sınırlandırılmıştır. `extra_hosts` içinde `idp.tail42f1f4.ts.net:100.119.135.23` (`tsidp`) tanımlıdır.
- **Yardımcı Bakım Betikleri:** `/home/flugel/sistem-bakim/komga-adlar.py` ve `komga-bolumler.py` betikleriyle Komga seri/bölüm meta verileri düzenlenir.

### 2.3. Kavita (`/opt/stacks/kavita/compose.yaml`)
- **Kütüphane Bağlaması:** `/mnt/sidemain/media/books:/data/books` bağlamasını kullanır; özellikle `/mnt/sidemain/media/books/ln/books/{English,Türkçe}` altındaki **Re:Zero** ve **Alya** EPUB/PDF hafif romanlarının okuma ilerlemesini (sayfa ve bölüm bazında) senkronize etmek için birincil sunucudur.
- **Kaynak Sınırı:** `mem_limit: 768m`, `127.0.0.1:18295->5000` (`uygulama-katman` systemd soketiyle yönetilir).

---

## 3. Koharia Reader (Flugel Manga) İstemci-Sunucu Mimarisi

Sunucu üzerinde `/home/flugel/work/koharia-reader` ve `/home/flugel/work/koharia-public` (ayrıca `/mnt/side/projects/flugel-manga`) dizinlerinde geliştirilen **Koharia Reader (Flugel Manga)** Android uygulaması, bu üç sunucuyla özel bir entegrasyona sahiptir:

1. **Çift Sunucu Sekme Mimarisi (`37eb2d40d`):**
   - **Çizgi Roman / Manga Sekmesi:** Doğrudan **Komga** sunucusuna bağlanır. Komga'nın gerçek zamanlı etkinlik akışı (`/sse/v1/events`, commit `593681613`) üzerinden kütüphane güncellemelerini dinler.
   - **Kitaplar (Light Novel) Sekmesi:** Aynı anda **Kavita** sunucusuna bağlanır (`fdffa453d`, `58c974136`). LAN ve Tailscale üzerinden EPUB/PDF romanların indirilmesini ve okuma ilerlemesinin çift yönlü senkronize edilmesini sağlar.
2. **Suwayomi ve Ağ Depolama Entegrasyonu (`c28ad51fc`):**
   - Koharia Reader içinden doğrudan Suwayomi kaynaklarına göz atılabilir ve ortak okuma/indirme tetiklenebilir.
3. **Kütüphaneye Ekle ve Manga İndir Kısayolları (`04d8e34ef`, `17d127850`):**
   - Uygulamanın "Daha Fazla" menüsünde sunucudaki `yukle` servisine (Kütüphaneye ekle) ve manga indirme arayüzüne doğrudan kısayollar yer alır.
4. **Güvenli Kişisel Derleme ve OTA Güncelleme (`715564bce`, `75f70ade1`):**
   - Koda gömülü API anahtarları kaldırılmış, Tailscale adresleriyle tak-çalıştır (`plug-and-play`) profil yapısı kurulmuştur.
   - Yeni sürümler `/home/flugel/work/publish.sh` ile derlenip imzalanır ve `/home/flugel/flugel-reader-updates/latest.json` üzerinden uygulama içi otomatik güncellemeyle dağıtılır.
