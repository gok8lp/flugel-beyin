---
name: sudo
description: Kullanici /sudo yazdiginda 2 saatlik gecici NOPASSWD sudo izni acmasi icin komutu verir. Ajan sudoers'a kendisi yazmaz, parola girmez.
---

# /sudo — 2 saatlik gecici sudo

Ajan sudoers dosyasini DEGISTIRMEZ ve parola girmez (guvenlik ayari + AGENTS.md bolum 1). Bu skill sadece kullaniciya komutu verir.

1. Kullaniciya su tek satirlik komutu kendi terminalinde calistirmasini soyle (parolayi o yazar):

```bash
sudo-2saat
```

2. Bitince `sudo -n true && echo OK` ile izni dogrula. Calisiyorsa kullanicinin o gorev icin verdigi sudo iznine gore devam et.
3. Is bitince veya 2 saat dolmadan kapatmak icin: `sudo-kapat` (sure dolunca kendiliginden de silinir; yeniden baslatma zamanlayiciyi siler, o durumda sudo-kapat calistir).
4. Izin gorev bazlidir; acma/kapama kaydi `yedekler/sudo-izin.log` icindedir. Raporda belirt.
