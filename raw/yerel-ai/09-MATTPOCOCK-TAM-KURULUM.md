# Matt Pocock tam depo kurulumu

28 Ekim 2026 tarihinde, yerel Claude Code için kuruldu.

- Depodaki **38 becerinin tamamı**, destek dosyaları ve MIT lisansıyla kurulu. Resmi plugin manifestinin 27 becerisiyle sınırlı değil.
- Kategoriler: 20 engineering, 7 productivity, 4 misc ve 7 in-progress.
- Dört özel home server/masaüstü becerin korundu: toplam **42 kişisel beceri**.
- Kaynak deponun tamamı `~/.local/share/claude-skill-sources/mattpocock-skills` altında Git kopyası olarak saklanıyor.
- Commit: `59db609eb1e18aaf59b63284d0e52255aff0c63c`.
- Keşfedilen beceriler `~/.claude/skills/<ad>/SKILL.md` altında. Çift kurulum olmaması için aynı beceriler ayrıca plugin olarak kaydedilmedi.
- Dosyaların kaynakla aynı olduğu, YAML ön bilgileri ve üç shell yardımcısının sözdizimi doğrulandı. Beceri iş akışlarının tamamı gerçek projelerde çalıştırılmış değildir.
- Mevcut Auto izin modu ve kişisel bilgi paketi korundu. Kurulum git hook'larını etkinleştirmedi, uygulama/deploy/PR akışlarını başlatmadı.

## Kullanım

Yeni yerel Claude Code sohbetinde `/` menüsünü aç. Örnekler: `/grill-me`, `/to-spec`, `/tdd`, `/code-review`, `/diagnosing-bugs`, `/implement`, `/handoff`. Bazı beceriler kaynakta explicit-only olduğu için yalnız kullanıcı çağırdığında yüklenir.

Bir kod projesinde engineering akışlarını ilk defa kullanırken o projenin klasöründe `/setup-matt-pocock-skills` çalıştır; issue tracker ve domain belgelerini projeye göre kurar. Beceri kurulumu bu proje ayarlarının yapılmış olduğu anlamına gelmez. `in-progress` klasöründekiler upstream'in geliştirme aşaması olarak işaretlediği becerilerdir.

Bunlar laptopun yerel Code oturumlarına kuruldu. Web hesabına, cloud oturumuna veya home server'daki ayrı Claude kullanıcısına otomatik kopyalanmadı.

| Komut | Kategori | Çağrılma |
|---|---|---|
| /ask-matt | engineering | Elle çağrılır |
| /code-review | engineering | İlgili görevde otomatik veya elle |
| /codebase-design | engineering | İlgili görevde otomatik veya elle |
| /diagnosing-bugs | engineering | İlgili görevde otomatik veya elle |
| /domain-modeling | engineering | İlgili görevde otomatik veya elle |
| /grill-with-docs | engineering | Elle çağrılır |
| /implement | engineering | Elle çağrılır |
| /implement-spec | engineering | Elle çağrılır |
| /improve-codebase-architecture | engineering | Elle çağrılır |
| /pr | engineering | İlgili görevde otomatik veya elle |
| /prototype | engineering | İlgili görevde otomatik veya elle |
| /research | engineering | İlgili görevde otomatik veya elle |
| /retro | engineering | Elle çağrılır |
| /setup-matt-pocock-skills | engineering | Elle çağrılır |
| /tdd | engineering | İlgili görevde otomatik veya elle |
| /to-spec | engineering | Elle çağrılır |
| /to-tickets | engineering | Elle çağrılır |
| /triage | engineering | Elle çağrılır |
| /wayfinder | engineering | Elle çağrılır |
| /wizard | engineering | İlgili görevde otomatik veya elle |
| /chief-of-staff | in-progress | Elle çağrılır |
| /claude-handoff | in-progress | Elle çağrılır |
| /loop-me | in-progress | Elle çağrılır |
| /setup-ts-deep-modules | in-progress | Elle çağrılır |
| /writing-beats | in-progress | Elle çağrılır |
| /writing-fragments | in-progress | Elle çağrılır |
| /writing-shape | in-progress | Elle çağrılır |
| /git-guardrails-claude-code | misc | İlgili görevde otomatik veya elle |
| /migrate-to-shoehorn | misc | İlgili görevde otomatik veya elle |
| /scaffold-exercises | misc | İlgili görevde otomatik veya elle |
| /setup-pre-commit | misc | İlgili görevde otomatik veya elle |
| /grill-me | productivity | Elle çağrılır |
| /grilling | productivity | İlgili görevde otomatik veya elle |
| /handoff | productivity | Elle çağrılır |
| /teach | productivity | Elle çağrılır |
| /to-questionnaire | productivity | Elle çağrılır |
| /wait-what | productivity | Elle çağrılır |
| /writing-for-agents | productivity | İlgili görevde otomatik veya elle |
