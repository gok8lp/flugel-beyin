---
title: Mullvad cihazları
tags: [mullvad, vpn, sunucu]
---
# Mullvad cihazları

Hesapta yalnız iki cihaz kalır (kaynak: sen, sohbette, 2026-11-15; `mullvad account list-devices` çıktısı 2026-11-15 16:47):

| Cihaz adı | Ne | Not |
|---|---|---|
| **Useful Dodo** | Bu laptop (ThinkBook, Arch + Hyprland) | 2026-11-15'te `mullvad account login` ile kaydedildi; Mullvad GUI Super+D alanında (communication) açılışta başlar |
| **Warm Ghost** | flugelserver, `gluetun` konteyneri | WireGuard genel anahtarı eşleşmesiyle belirlendi (2026-11-15) |

- Hesap 5 cihaz sınırlıdır; diğer üç eski cihaz (Awake Whale, Amused Hippo, Pretty Bee) 2026-11-15'te kullanıcı tarafından silindi.
- **Warm Ghost silinirse sunucunun VPN'i (gluetun) kopar.** Dokunma.
- Laptopta Mullvad ile Tailscale çakışabilir (2026-11-15'te `/etc/resolv.conf` boşaldı, internet gitti). Çözüm: `sudo nmcli general reload dns-rc`.
- Hesap numarası bilerek bu nota yazılmadı.

Bağlantılı: [[knowledge/sunucu-haritasi]]
