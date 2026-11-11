# Kaynaklar ve gözlem kapsamı

## Yerel kanıtlar

PC01: hostname/lscpu/free/lsblk/df, seçilmiş paket envanteri, GPU, systemd, Hyprland ve ses servisi çıktıları. SV01: aynı kolektörün flugelserver üzerinde SSH anahtarıyla çalışması; Docker inspect'ten sadece seçilmiş güvenli alanlar. SV02: süreli libvirt sorgusu, ilgili unit hata kaydı, SMART genel sağlık sonuçları, yedek servis sonuçları, DOCKER-USER kuralları, Ollama model listesi. HTTP01: launcher URL'lerine HEAD ve seçilmiş GET denemeleri; FileBrowser doğru HTTPS adresine ek GET. DESK01: mevcut Lua dosyaları ve yerel kabuk yardımcıları. AUTH01: Tailscale oturum doğrulaması gereksinimi ve LAN anahtar girişinin başarılı olması.

Ham inceleme dosyaları work/audit altında tutuldu; kullanıcıya sunulan envanter özel cihaz tanımlayıcıları azaltılarak üretildi. Paket kişisel dosya içeriklerini veya hesap sırlarını içermez.

## Resmi Claude belgeleri

- https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features
- https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/permissions
- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/settings
- https://code.claude.com/docs/en/desktop

## Masaüstü kaynakları

- https://github.com/pctrade/end4-pC
- https://github.com/AdiAmbassador/caelestia-aw
- https://github.com/AdiAmbassador/caelestia-shell-aw
- https://github.com/AdiAmbassador/caelestia-cli-aw
- https://github.com/GhostNaN/mpvpaper
