---
title: GitHub Depo Analizi — gok8lp/chrome-orta-tik-kaydirma
sources: raw/github/chrome-orta-tik-kaydirma.md, raw/github/00-github-envanteri.md, raw/github/01-tum-repolar-commit-gecmisi.md
updated: 2026-11-11
---

# GitHub Depo Analizi: `gok8lp/chrome-orta-tik-kaydirma`

Üst Katalog: [[github-repolar-katalogu]] · [[sunucu-ve-github-commit-gecmisi]] · [[duduk-genel-bakis]] · [[flugelserver-genel-mimari]]

> "GitHub Repo: gok8lp/chrome-orta-tik-kaydirma" - raw/github/chrome-orta-tik-kaydirma.md

> "gok8lp GitHub Depoları Tam Commit Geçmişi" - raw/github/01-tum-repolar-commit-gecmisi.md

## Son Commit Geçmişi (`gok8lp/chrome-orta-tik-kaydirma`)
- `10717d2` (2026-10-29): README: klonlama adresini ekle
- `83945af` (2026-10-29): Uyarı çubuğunu --test-type ile gizle
- `14795e6` (2026-10-29): MIT lisansı ekle
- `c5b2b11` (2026-10-29): README: kullanım ve uyarının anlamı
- `5b38f5d` (2026-10-29): Chrome orta tık kaydırmayı aç/kapat betikleri

## Dosya Ağacı ve README Özeti
# GitHub Repo: gok8lp/chrome-orta-tik-kaydirma

- **URL:** https://github.com/gok8lp/chrome-orta-tik-kaydirma
- **Görünürlük:** Açık (Public)
- **Ana Dil:** Shell
- **Son Güncelleme:** 2026-10-29T21:49:52Z
- **Açıklama:** Linux'ta Chrome'a orta tuşla otomatik kaydırma ekler, uyarı çubuğunu gizler

## Dosya Ağacı (File Tree)
- `LICENSE` (blob)
- `README.md` (blob)
- `kaldir.sh` (blob)
- `kur.sh` (blob)

## README İçeriği
# Chrome Orta Tık Kaydırma · Linux

Windows'ta Chrome'da orta tuşa basıp fareyi oynatınca sayfa kayar. Linux'ta Chrome bunu varsayılan olarak yapmaz.
Bu proje özelliği tek komutla açar veya kapatır ve Chrome'un bu ayar için gösterdiği uyarı çubuğunu gizler.

## Kurulum

```bash
git clone https://github.com/gok8lp/chrome-orta-tik-kaydirma.git && cd chrome-orta-tik-kaydirma
./kur.sh
```

Sonra Chrome'u **tamamen** kapatıp aç (arka planda açık kalıyorsa sistem tepsisinden "Çık").

## Kapatma

```bash
./kaldir.sh
```

## Bilinmesi gerekenler

- Özellik Chrome'un `--enable-blink-features=MiddleClickAutoscroll` ayarıyla açılır. Ayar, kullanıcıya ait
  `~/.local/share/applications/google-chrome.desktop` başlatıcısına eklenir; sistem dosyasına dokunulmaz.
- Chrome bu ayar açıkken normalde üstte şu uyarıyı gösterir:
  *"You are using an unsupported command-line flag … Stability and security will suffer."*
  Google bu ayarı resmi olarak desteklemediği için çıkan genel bir uyarıdır; bu ayar bir güvenlik açığı oluşturmaz.
- `kur.sh` uyarı çubuğunu gizlemek için `--test-type` ayarını da ekler. Bu, Chrome'un kendi testleri için kullandığı,
  resmi olarak desteklenmeyen bir ayardır ve başka hangi davranışları değiştirdiği belgelenmemiştir.
  Bir tuhaflık görürsen `./kaldir.sh` ile ikisini birden kapat.
- Yalnızca bu başlatıcıdan (uygulama menüsü, dock) açılan Chrome'da çalışır; terminalden `google-chrome` ile açarsan ayar gelmez.
- Eski AutoScroll eklentisi 2018'den beri güncellenmediği için yeni Chrome sürümlerinde çalışmayabilir; bu yüzden ayar yolu kullanıldı.
- Her işlemde başlatıcının önceki hâli `google-chrome.desktop.yedek` olarak saklanır.

## Lisans

[MIT](LICENSE)



## İlgili Mimari Sayfaları
- [[github-repolar-katalogu]]
- [[sunucu-ve-github-commit-gecmisi]]
- [[pc-masaustu-hyprland-ve-gnome-araclari]]
- [[koharia-reader-ve-manga-ekosistemi]]
