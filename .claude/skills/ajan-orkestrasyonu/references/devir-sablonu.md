# Devir ve yarım iş şablonu

%80–90 ilerleme kapanış değildir. Aşağıdaki kartı kaynak bağlantılarıyla doldur; kalan işi V3 `task-create` ile görev yap. Aktif odağı mevcut Threads konusu içinden göreve bağla. Görev/companion yazımı mevcut işin OWNS sınırına girmiyorsa bu işlemleri yetkili lidere devret; sınırı aşma.

```text
Lane / hedef / devralacak sorumlu:
Biten işler: <yalnız kanıtlanan sonuçlar>
Dokunulan dosyalar: <tam yollar ve kısa diff özeti>
Doğrulama: <komut, rc, kısa çıktı ve kanıt yolu>
Kalan kabul ölçütleri: <numaralı, ölçülebilir liste>
Engeller: <neden, kanıt, gereken yetki veya dış koşul>
Sıradaki adım: <tek somut eylem, önkoşul ve süre>
V3 görev: <id, source, revision, durum; açılmadıysa bunu açık yaz>
```

## V3 görevi açma örneği

Mevcut benzer görevi önce ara; varsa yeni kopya yerine `task-update` ve okunan `expected_revision` kullan. Yeni görev için UTF-8 JSON'u geçici bir dosyaya koy; aşağıdaki kimliği, sorumluyu ve kaynakları gerçek devirle değiştir. Görevin açıklaması `text`, frontmatter alanları `metadata` içindedir.

```json
{
  "source": "tasks/ajan-filosu-devir-ornek.md",
  "text": "Biten işler: lane kartı hazır.\nDokunulan dosyalar: .agents/skills/ajan-orkestrasyonu/references/lane-karti.md\nDoğrulama: şablon alanları elle kontrol edildi; süreç testleri henüz koşulmadı.\nKalan kabul: filo testlerinin gerçek çıktısını incele ve teslimi doğrula.\nEngel: bağımsız kontrol bekleniyor.\nSıradaki adım: taze kontrol ajanı testleri çalıştırsın.\nKaynak: [[.agents/skills/ajan-orkestrasyonu/references/lane-karti]]",
  "metadata": {
    "id": "ajan-filosu-devir-ornek",
    "title": "Ajan filosu bağımsız kontrol devri",
    "kind": "task",
    "revision": 1,
    "status": "waiting",
    "owner": "Gökalp",
    "visibility": "internal",
    "project": "ajan-orkestrasyonu",
    "next_action": "Kalan kabul ölçütlerini bağımsız kontrolle doğrula"
  }
}
```

```bash
# Vault kökünde; JSON dosyası bu komuttan önce hazırlanmış olmalı.
python3 beyin.py --vault <vault> task-create --file /tmp/ajan-devir.json
```

Sorumlu örnekte kullanıcıdır; gerçek işi başka biri üstlendiyse onu yaz, sorumlu uydurma. Komutun çıkış koduna ek olarak dönen `source`, `id`, `kind`, `revision`, `status`, `owner` alanlarını istekle karşılaştır. Başarısız kayıt veya engel açık kalır; görev oluşturuldu diye uygulama tamamlandı sayılmaz. Bu örnek bu görevde çalıştırılmamıştır.

Söz dizimi dayanağı (2026-11-14, salt okunur): `beyin.py:908` global vault argümanını CLI'ye iletir; `.claude/scripts/beyin_v3_cli.py:1127,1249,2098` argümanları ve JSON sözleşmesini; `beyin_v3_sync.py:1488` alan doğrulamasını tanımlar. Bu dosyalara yazılmaz.
