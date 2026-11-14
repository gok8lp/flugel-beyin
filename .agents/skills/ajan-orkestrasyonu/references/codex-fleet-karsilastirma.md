# codex-fleet karşılaştırması

Kaynak: kullanıcı tarafından verilen codex-fleet listesi ve yerel iki skill; [Avenox adresinin](https://avenox.io/codex.md) güncel tam metnine bu oturumda erişilemedi. Bu bir satır satır uzaktan doğrulama değildir. `Var` mevcut yerel metni, `yok` önceden açık kural/otomasyon bulunmamasını, `benimsendi` bu değişikliğin yerel uyarlamasını anlatır; kurulum veya çalışma garantisi değildir.

| Konu | Değişiklik öncesi bizde | Sonuç / bu çalışmada benimsenen davranış |
|---|---|---|
| `codex exec` varsayılanları | **Var:** `--skip-git-repo-check -s read-only`, stdin `/dev/null`; yazmada `-s workspace-write -C <hedef>` | **Var / korundu:** bunlar yerel çağrı politikasıdır, CLI'nin üretici varsayılanları olduğu iddia edilmez. İzin zaten görevde verildiyse yeniden onay isteme; sandbox sınırını aşma. Uzaktaki skill'in tam bayrakları **doğrulanmadı**. |
| Worktree-per-lane ve `OWNS` / `DO-NOT-TOUCH` | **Var:** aynı dosyaya iki yazıcı yasağı; **yok:** zorunlu lane kartı ve worktree yaşam döngüsü | **Benimsendi:** zorunlu açık sahiplik, tek yazıcı; ayrı worktree yalnız izinli işte seçenek. Yerel `codex exec --help` içinde `--worktree` var; bu görevde çalıştırılmadı. Otomatik worktree yaşam döngüsü **yok**; Git yasaksa bu yol kullanılmaz. |
| Canlılık: log büyümüyorsa ölü | **Yok:** genel filo gözetimi | **Benimsendi (uyarlama):** `filo.py durum --takilma-dakika 10` sessizliği `takıldı` diye raporlar. Sessiz log kesin ölüm değil, takılma şüphesidir; otomatik öldürme nedeni süre sınırıdır. |
| “Tamamlanma iddiadır” | **Var:** ayrı taze kontrol ajanı ilkesi | **Benimsendi:** tam yollar + diff özeti + komut ve çıktı; farklı taze ajan kabul/ret/eksik kanıt üretir. |
| Lane'leri 2–5 sn arayla başlatma | **Yok:** açık aralık | **Benimsendi:** lider başlatmaları 2–5 sn arayla kademelendirir; her çağrının kota kapısı ayrıca çalışır. Bu hız sınırını `filo.py` otomatik uygulamaz. |
| Yaklaşık 20 eşzamanlı lane sınırı | **Yok:** genel sayı; görselde en çok 3 vardı | **Benimsendi:** üst sınır 20; mevcut platform/slot, kota, kaynak ve görselde 3 sınırından en düşüğü geçerli. 20 hedef sayı değildir; `filo.py` küresel kota/slot yöneticisi değildir. |
| `caffeinate`; Linux `systemd-inhibit` | **Yok:** Linux için doğrulanmış kullanım | **Benimsendi (koşullu):** uzun gözetimi host'ta gerekliyse `systemd-inhibit --what=sleep --mode=block --why="Ajan filosu" python3 scripts/filo.py bekle --log-dizini <dir>`. Kurulum, polkit izni ve host etkisi ayrıca doğrulanır; sandbox'ta başarı host uyanıklığını kanıtlamaz. |

Bu uyarlamalar gizlilik, kota, OWNS ve sandbox sınırlarını gevşetmez. Filo komutunun çalışması model erişimini ya da ajan tesliminin doğruluğunu kanıtlamaz. Uzaktaki tam metin ulaşılabilir olduğunda yeni bir karşılaştırma yap; şimdiki metni körlemesine değiştirme.
