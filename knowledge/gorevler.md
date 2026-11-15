---
title: "Görev haritası"
type: moc
updated: 2026-11-15
---

# Görev haritası

## Açık

- [[tasks/adguard-dns-temizligi]] — active — `flugelserver` üzerindeki `adguard.gokalpgoksu.com` A kaydının Cloudflare panelinden temizlenip temizlenmediğinin kontrol edilmesini kapsar.
- [[tasks/assignr-yayin-saati-gozlemi]] — active — Cuma–Cumartesi geceleri `assignr` yeni hafta yayın saatinin `duduk-server` loglarından gözlemlenmesini hedefler.
- [[tasks/bolge-ucret-kaydi]] — active — İlk resmi `BÖLGE` yerel lig ödemesi yattığında net maç başı ücretin ilgili Düdük ve tarife notlarına kaydedilmesi görevidir.
- [[tasks/canalp-cli-girisi]] — active — `ai-limitler` kotasının okunabilmesi ve alt ajanların kota kapısından geçebilmesi için Gökalp tarafından Canalp (Claude 2) CLI girişinin yapılmasını bekler.
- [[tasks/duduk-canli-arsiv-yeni-hafta]] — active — Canlı Düdük sunucu arşivinin (`https://duduk.gokalpgoksu.com/v1/stats`) yeni hafta atamalarını yakalamasının izlenmesini içerir.
- [[tasks/tailscale-funnel-karari]] — active — Jellyfin (`:443`) ve Immich (`:10000`) için Tailscale Funnel genel erişiminin kapatılıp kapatılmayacağına dair Gökalp kararını bekler.

## Biten

- [[tasks/sunucu-anahtar-dondurme]] — done — Sır maskelemesinin kaçırdığı Ollama, Guacamole ve tsidp özel anahtarları 2026-11-15'te döndürüldü; eski Ollama anahtarının hesaptan silinip silinmediği açık not olarak bırakıldı.
- [[tasks/sunucu-uygulama-bakimi]] — done — `flugelserver` üzerindeki yeni uygulamalar, Tailscale kimlik kapıları ve Hermes/n8n düzenlemeleri tamamlanarak 2026-11-15'te bitirildi.

## Şablonlar ve companion

- [[📋 Templates/Kisi]] — Yeni kişi notları açılırken beyan, çıkarım ve temas bölümlerini standartlaştıran şablondur.
- [[🔮 850-Companion/Journal]] — Ortak çalışmadan doğan gözlemleri, öğrenimleri ve açık soruları tutan günlük notudur.
- [[🔮 850-Companion/Last-Session]] — Anlamlı çalışma oturumlarının sonuç, gerekçe, açık adım ve kaynak bağlantılarının kaydedildiği oturum özetidir.
- [[🔮 850-Companion/Core]] — Kullanıcının kimlik, çalışma biçimi ve kalıcı tercihlerini barındıran çekirdek companion dosyasıdır.
- [[🔮 850-Companion/Threads]] — Aktif iş akışlarını, sahipliklerini, güncel durumlarını ve sonraki adımları izleyen odak dosyasıdır.
- [[🔮 850-Companion/Kurallar]] — Kullanıcının açıkça belirttiği genel kuralları ve proje bazlı kural işaretçilerini toplayan kalıcı kural dosyasıdır.

Üst harita: [[knowledge/index]]
