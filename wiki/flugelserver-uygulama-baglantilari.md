---
title: flugelserver Uygulamalarının Birbiriyle Bağlantı Topolojisi
sources: raw/flugelserver/02-UYGULAMALAR.txt, raw/flugelserver/MIMARI.md, raw/yerel-ai/dosya-ekosistemi.md, raw/yerel-ai/sunucu-entegrasyon-fikirleri.md, raw/yerel-ai/kisayol-karsilastirma.md
updated: 2026-11-11
---

# flugelserver Uygulamalarının Birbiriyle Bağlantı Topolojisi

Bağlı Sayfalar: [[flugelserver-genel-mimari]] · [[flugelserver-docker-uygulamalari]] · [[flugelserver-dizi-film-arsivi]] · [[flugelserver-anime-manga-lightnovel-arsivi]] · [[flugelserver-ag-guvenlik-ve-tuneller]] · [[koharia-reader-ve-manga-ekosistemi]]

> "Dosya ve yedek ekosistemi (PC ↔ sunucu ↔ diğer cihazlar)" - raw/yerel-ai/dosya-ekosistemi.md

## 1. VPN ve İndirme Zinciri (`Gluetun` Merkezli)
- **`gluetun` (Mullvad WireGuard VPN):** Dış ağa güvenli tünel açar.
- **`transmission` (`network_mode: container:gluetun`):** Tüm torrent trafiği Gluetun VPN üzerinden çıkar; `/mnt/side/downloads` klasörüne yazar.
- **`prowlarr` & `flaresolverr` & `jackett`:** İndeksleyicileri tarar, Cloudflare korumasını `flaresolverr` ile aşar ve `sonarr`/`radarr` ile senkronize olur.
- **`suwayomi` (`network_mode: container:gluetun`):** Manga kaynaklarından bölümleri VPN üzerinden `/mnt/sidemain/media/books/manga/suwayomi` dizinine indirir.

## 2. Dizi, Film ve Altyazı Otomasyon Zinciri (`*arr` -> Medya Sunucuları)
- **`sonarr` (`127.0.0.1:18989`) & `radarr` (`127.0.0.1:17878`):** `prowlarr`/`jackett` üzerinden buldukları dizi/anime ve filmleri `transmission`'a gönderir; tamamlananları `/mnt/side/downloads` içinden alıp `/mnt/sidemain/media/series` ve `/mnt/sidemain/media/movies` altına taşır.
- **`bazarr` (`127.0.0.1:16767`) & `subgen`:** Aynı medya klasörlerini izleyerek eksik Türkçe/İngilizce altyazıları indirir veya ses izinden üretir.
- **`jellyfin` (`127.0.0.1:18096`) & `plex` (`host`):** `/mnt/sidemain/media/movies` ve `/mnt/sidemain/media/series` klasörlerini sunarak TV, PC ve telefondan izlenmesini sağlar.

## 3. Manga ve Light Novel Zinciri (`Suwayomi` / `Komga` / `Kavita` -> `Koharia Reader`)
- **`suwayomi`:** `/mnt/sidemain/media/books/manga/suwayomi` dizinine manga indirir.
- **`komga` (`127.0.0.1:18296`) & `kavita` (`127.0.0.1:18295`):** `/mnt/sidemain/media/books` (`manga/` ve `ln/` — Re:Zero vb.) arşivini OPDS ve REST API üzerinden sunar.
- **[[koharia-reader-ve-manga-ekosistemi]] (Android):** Telefondan Komga, Kavita ve Suwayomi'ye bağlanarak okuma ilerlemesini senkronize eder.

## 4. Fotoğraf ve Bulut Depolama Zinciri (`Immich` <-> `Nextcloud`)
- **`immich_server` (`:2283`) + `immich_machine_learning` (CUDA) + `immich_postgres` + `immich_redis`:** Telefondan yüklenen fotoğrafları `/mnt/sidemain/photos/immich` içine kaydeder ve GPU üzerinde yüz/nesne tanıma yapar.
- **`nextcloud` (`:8443`) + `nextcloud-db` (Postgres 17):** `/mnt/sidemain/cloud/nextcloud` üzerinde bulut dosyalarını tutar VE `/mnt/sidemain/photos/immich` dizinini salt-okunur (`read-only`) bağlayarak Immich fotoğraflarını Nextcloud içinde de gösterir.

## 5. Kişisel Bilgi, Hakemlik ve Panel Zinciri (`FLUGEL Akış` + `basket-bot` + `duduk-server`)
- **`/opt/basket-bot` (`basket_bot.py` & `anime_takip.py`):** `/var/lib/basket-bot/maclar.json` ve `anime.json` üretir.
- **`flugel-akis` (`/opt/stacks/panel/akis/akis.py`):** 61 RSS/YouTube kaynağını, `/var/lib/basket-bot`, `/var/lib/flugel/durum` ve yerel `ollama` (`qwen3.5:4b`) modelini birleştirerek `https://flugelserver.tail42f1f4.ts.net:8443` adresinde sunar.
- **`duduk-server` (`~/duduk-server`, `:18420`):** `assignr`, `ankarabasket` ve `TBF` verilerini saatlik çekip arşivler; `https://duduk.gokalpgoksu.com` ve `https://flugelserver.tail42f1f4.ts.net:18443` üzerinden [[duduk-genel-bakis]] Android uygulamasını besler.
