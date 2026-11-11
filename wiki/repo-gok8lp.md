---
title: GitHub Depo Analizi — gok8lp/gok8lp
sources: raw/github/gok8lp.md, raw/github/00-github-envanteri.md, raw/github/01-tum-repolar-commit-gecmisi.md
updated: 2026-11-11
---

# GitHub Depo Analizi: `gok8lp/gok8lp`

Üst Katalog: [[github-repolar-katalogu]] · [[sunucu-ve-github-commit-gecmisi]] · [[duduk-genel-bakis]] · [[flugelserver-genel-mimari]]

> "GitHub Repo: gok8lp/gok8lp" - raw/github/gok8lp.md

> "gok8lp GitHub Depoları Tam Commit Geçmişi" - raw/github/01-tum-repolar-commit-gecmisi.md

## Son Commit Geçmişi (`gok8lp/gok8lp`)
- `3e4c3e3` (2026-10-31): Profile: drop intro text, add home server section
- `2516681` (2026-10-31): Profile README: banner, featured projects, bilingual intro

## Dosya Ağacı ve README Özeti
# GitHub Repo: gok8lp/gok8lp

- **URL:** https://github.com/gok8lp/gok8lp
- **Görünürlük:** Açık (Public)
- **Ana Dil:** Belirtilmemiş
- **Son Güncelleme:** 2026-10-31T00:16:54Z
- **Açıklama:** Profile README

## Dosya Ağacı (File Tree)
- `README.md` (blob)
- `assets` (tree)
- `assets/avatar.png` (blob)
- `assets/banner.svg` (blob)

## README İçeriği
<a href="https://gokalpgoksu.com"><img src="assets/banner.svg" alt="Gökalp Göksu" width="100%"></a>

## Home server · Ev sunucusu

<p>
  <img src="https://img.shields.io/badge/Ubuntu_26.04-1a1a1d?style=flat-square&logo=ubuntu&logoColor=E95420" alt="Ubuntu 26.04">
  <img src="https://img.shields.io/badge/Docker-1a1a1d?style=flat-square&logo=docker&logoColor=2496ED" alt="Docker">
  <img src="https://img.shields.io/badge/KVM_·_VFIO-1a1a1d?style=flat-square&logo=qemu&logoColor=FF6600" alt="KVM · VFIO">
  <img src="https://img.shields.io/badge/Tailscale-1a1a1d?style=flat-square&logo=tailscale&logoColor=white" alt="Tailscale">
  <img src="https://img.shields.io/badge/Cloudflare_Tunnel-1a1a1d?style=flat-square&logo=cloudflare&logoColor=F38020" alt="Cloudflare Tunnel">
  <img src="https://img.shields.io/badge/systemd-1a1a1d?style=flat-square&logo=linux&logoColor=white" alt="systemd">
</p>

**Ryzen 5 2600X · 15 GB RAM · GTX 1660 Ti · SSD + 2 external disks**

| | |
|---|---|
| **Docker** | 36 stacks: Nextcloud, Immich, Komga, Kavita, AdGuard, n8n, Uptime Kuma, Netdata, Gotify, code-server, Stirling-PDF… |
| **Virtual machines** | Windows VM with GTX 1660 Ti passthrough (handed back to the host on shutdown) · Mullvad VPN + dev desktop VM |
| **Remote desktop** | Guacamole (RDP, TOTP from the internet) · Webtop · Kasm, from the browser |
| **Network** | Tailscale + two Cloudflare Tunnels · ufw · one start page for every service |
| **Storage** | 3 LUKS-encrypted disks · disk spin-down · SMART monitoring |
| **Backups** | Nightly critical backup · 30-day deleted-file retention |
| **Monitoring** | Self-healing services · Docker/disk/SSH watchers · AI-assisted issue summaries · Telegram / WhatsApp / Gotify alerts |

The whole setup lives in **[home-server](https://github.com/gok8lp/home-server)** as sanitized config,
and **[home-server-android](https://github.com/gok8lp/home-server-android)** monitors and controls it from my phone.

## Projects · Projeler

| | |
|---|---|
| [headset-surround-linux](https://github.com/gok8lp/headset-surround-linux) | Virtual 7.1 surround + Cinema mode for any headset (PipeWire) |
| [desktop-server-toolkit](https://github.com/gok8lp/desktop-server-toolkit) | GNOME integrations, news feed and maintenance tools for desktop + server |
| [gnome-island](https://github.com/gok8lp/gnome-island) | Notifications, media and system tools in one capsule for GNOME Shell 50 |
| [clipline-linux](https://github.com/gok8lp/clipline-linux) | Wayland/Hyprland port of ClipBoardLine |
| [koharia-reader](https://github.com/gok8lp/koharia-reader) | Android reader with Komga, Kavita and local libraries |
| [end4-pC](https://github.com/gok8lp/end4-pC) | My Hyprland/Caelestia desktop setup |

<details>
<summary><b>Small Linux tools · Küçük Linux araçları</b></summary>
<br>

| | |
|---|---|
| [ubuntu-tam-guncelle](https://github.com/gok8lp/ubuntu-tam-guncelle) | apt, snap, flatpak and firmware updates in one command |
| [chrome-orta-tik-kaydirma](https://github.com/gok8lp/chrome-orta-tik-kaydirma) | Middle-click autoscroll for Chrome on Linux |
| [gnome-pip-konum](https://github.com/gok8lp/gnome-pip-konum) | Chrome picture-in-picture remembers its position |
| [k380s-ubuntu-fn](https://github.com/gok8lp/k380s-ubuntu-fn) | Logitech K380s top-row keys on GNOME/Wayland |

</details>

<details>
<summary><b>Learning projects · Öğrenme projeleri</b></summary>
<br>

| | |
|---|---|
| [cybersecurity-lab](https://github.com/gok8lp/cybersecurity-lab) | Security lessons and an isolated lab · FastAPI + React |
| [c-process-tree](https://github.com/gok8lp/c-process-tree) | Process trees with POSIX `fork` |
| [java-producer-consumer](https://github.com/gok8lp/java-producer-consumer) | Producer/consumer with Java threads |
| [c-calismalarim](https://github.com/gok8lp/c-calismalarim) · [c-text-shuffler](https://github.com/gok8lp/c-text-shuffler) · [c-password-generator](https://github.com/gok8lp/c-password-generator) | C exercises |
| [gok8lp.github.io](https://github.com/gok8lp/gok8lp.github.io) · [wix-anilist-portfolio](https://github.com/gok8lp/wix-anilist-portfolio) | Personal site experiments |

</details>



## İlgili Mimari Sayfaları
- [[github-repolar-katalogu]]
- [[sunucu-ve-github-commit-gecmisi]]
- [[pc-masaustu-hyprland-ve-gnome-araclari]]
- [[koharia-reader-ve-manga-ekosistemi]]
