# FLUGEL Server — Infrastructure Map

Snapshot: 20 October 2026. Server copy: `/srv/dev/docs/INFRASTRUCTURE.md`. Human-readable Turkish guide: `/srv/rehber/`.
Live, auto-generated details (containers, mounts, ports, backup status) are in `/srv/rehber/02-*`, `03-*` and `06-*`, regenerated nightly.

## 1. Host

| Item | Value |
|---|---|
| Hostname | `flugelserver` — Ubuntu 26.04.1 LTS, kernel 7.0, x86_64 |
| Access | SSH alias `flugelserver` (user `flugel`, key auth); LAN `192.168.0.15`; Tailscale `100.86.88.1` / `flugelserver.tail42f1f4.ts.net` |
| RAM / swap | 15 GiB / 4 GiB swap file on the system SSD |
| GPU | GTX 1660 Ti — shared between host containers and the `W11-GPU` VM (VFIO hand-over via libvirt hook) |

## 2. Storage

| Mount | Device | Size | Role |
|---|---|---|---|
| `/` | Kingston A400 SSD (`sdb`), LUKS (TPM2 unlock) + LVM | 437 GiB | OS, Docker, app config, VM disks |
| `/mnt/side` | Seagate 500 GB (`sdc`), LUKS (keyfile) | 458 GiB | downloads, **primary backup target**, personal files |
| `/mnt/sidemain` | Samsung M3 1 TB USB (`sda`), LUKS (keyfile) | 916 GiB | media, photos (Immich), Nextcloud data |

Known constraint: discard/TRIM is **not** enabled on the root LUKS mapping, so `fstrim` never trims `/`. This is the main suspected cause of the chronic I/O pressure (see section 9).

## 3. Filesystem layout (target standard and current state)

| Path | Purpose | State |
|---|---|---|
| `/opt/stacks/<app>/compose.yaml` | Deployment definition (one dir per Compose project; secrets in `.env`, mode 600) | 30 stacks; `jellyfin`, `ollama` and `plex` still live in `/arrapps/compose/` |
| `/srv/appdata/<app>/` | Persistent app state (target) | `adguard`, `checkcle`, `filebrowser`, `guacamole`, `libreoffice`, `suwayomi` (old paths are symlinks) |
| `/arrapps/<app>/` | Persistent app state (legacy) | All other apps; 23 unused dirs still here. **Migration incomplete.** |
| `/srv/backups/current/` | On-disk "latest" copy of backups | app archives |
| `/srv/archive/` | Retired but retained material | stacks, installers, old backups, PC backups, security (mode 700) |
| `/srv/dev/` | Development area (`projects`, `workspaces`, `artifacts`, `tools`, `docs`, `archive`) | in use |
| `/srv/project/` | Windows-VM Eclipse projects (`gelen/` incoming, `surumler/` versions) | ready, Windows side not installed yet |
| `/srv/operations/` | `changes/` (rollback copies per change), `history/`, `inventory/`, `ai-context/` | in use |
| `/srv/rehber/` | Operator guide (TXT) | in use |
| `/var/lib/flugel/durum/` | Panel/bot status data (was `~/sistem-bakim/durum`) | symlink left |
| `/var/lib/libvirt/images/` | VM disks: `w11` (qcow2, shared by W11 and W11-GPU), `mullvad-ts.qcow2` | — |

## 4. Services (Docker Compose)

| Group | Apps |
|---|---|
| Files and photos | Nextcloud (SQLite), Immich (+PostgreSQL, Redis, ML), File Browser |
| Media | Jellyfin (CPU), Plex (GPU), Sonarr, Radarr, Bazarr, Lingarr, Subgen (GPU) |
| Download (via Gluetun/Mullvad, SE exit) | Transmission, Prowlarr, Suwayomi (main manga app, intentionally stopped), plus Jackett and FlareSolverr |
| Books and manga | Komga, Kavita, Openbooks, KamiYomu |
| Tools | LibreOffice, ConvertX, IT-Tools, Stirling-PDF (stopped), Open WebUI (stopped), Ollama (GPU) |
| Remote desktop | Guacamole (+guacd, PostgreSQL) |
| Portal and monitoring | giris (nginx, gokalpgoksu.com), Akış panel, gündem-botu, Homepage, Uptime Kuma, Netdata, CheckCle |
| Management | Portainer, Dockge |
| Network | AdGuard Home (LAN + Tailscale DNS) |

Removed on 20 Oct: Webtop, Kasm (and its 8 inner containers), server-side Eclipse, code-server, Tranga.

## 5. Network ingress

```
Internet ──Cloudflare tunnel "homeserver" (dashboard-managed, remote config v40)──► nextcloud, immich, tools, pdf, ai, convert,
         │                                                                        ui, ln, manga, office, bd, portainer, admin, video
         ├─Cloudflare tunnel "akis" (/etc/cloudflared/akis.yml)──► akis, status, masaustu, gokalpgoksu.com, indir, suwayomi ──► nginx giris
         └─Tailscale Funnel ──► :10000 Immich, :443 Jellyfin
Tailnet  ──Tailscale Serve https://flugelserver…ts.net:<8443-45443> ──► one port per app (admin tools tailnet-only)
LAN      ──192.168.0.15 (AdGuard DNS, Samba side/sidemain/project — user flugel only)
VM NAT   ──192.168.122.0/24 (W11-GPU .50, W11 .51, mullvad-ts .75); Moonlight ports DNAT'ed to the running Windows VM
```

## 6. Virtual machines

| VM | Disk | Autostart | Idle policy |
|---|---|---|---|
| W11-GPU | `w11` (shared) + GPU passthrough | off | 10 min without activity → ACPI shutdown → force-off only if fully inactive (hung) |
| W11 | `w11` (shared) | off | same; cannot run alongside W11-GPU (hook) |
| mullvad-ts | `mullvad-ts.qcow2` | off | same |

Activity means at least 256 KiB/min of network traffic, at least 32 MiB/min of disk I/O, or a VNC/console client attached. The tool is `vm` (`durum`/`ac`/`kapat`/`yedek`/`yedekler`/`geri-yukle`) and the config is `/etc/vm-yonetim.conf`.

## 7. Backup architecture

| Layer | Schedule | Primary copy | Other disks | Retention |
|---|---|---|---|---|
| App archives (config + volumes + `pg_dumpall` + consistent SQLite) | 03:30 | `/mnt/side/yedek/uygulamalar/` | `/srv/backups/current/`, `/mnt/sidemain/backups/current/` | 3 versions; 2 if total > 25 GiB or archive > 3 GiB |
| VM rollback (qcow2 zstd + XML + NVRAM + TPM) | on shutdown + 05:15 | `/mnt/side/yedek/vm/<set>/` | sidemain only if ≤ 90 % full (currently skipped) | 2 per disk set |
| Critical data mirror (photos, Nextcloud, configs) + DB dumps | 04:30 | `/mnt/side/yedek/kritik/` | — | 30-day deleted-file history |
| Eclipse projects | 02:30 | `/srv/project/surumler/` | (in app archives) | 30 snapshots |

Gap: no off-site copy.

## 8. Automation

`self-heal` (3 min), `docker-watcher` (5 min), `disk-koruyucu` (10 min), `swap-flush`, `ai-gozcu` (15 min), `vm-bosta-kapat` (1 min), the backup timers above, `rehber-guncelle` (06:00), and bots (`basket`, `anime`, `imdb`, Telegram bridge). Notifications go through `/usr/local/bin/bildirim` to Telegram.

## 9. Open items (priority order)

1. Enable discard on root LUKS (crypttab + initramfs + reboot, from the console), then `fstrim /`.
2. Finish the `/arrapps` → `/srv/appdata` migration; archive the 23 unused dirs; move the jellyfin, ollama and plex compose files.
3. Reorganise the `/mnt/side` and `/mnt/sidemain` trees (case collisions: `Downloads`/`downloads`, `Projects`/`projects`).
4. Add an off-site backup.
5. Plan capacity: sidemain is at 88 %, side at 77 %.
6. Narrow `flugel` NOPASSWD sudo, move plaintext API keys out of `self-heal.sh`, review Cloudflare Access for `portainer`, `admin` and `office`.
7. Install the QEMU guest agent in Windows; run the Eclipse sync installer inside the VM.
