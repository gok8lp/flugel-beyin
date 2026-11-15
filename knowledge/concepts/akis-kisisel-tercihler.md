---
{
  "kind": "fact",
  "title": "Akış kişisel tercih profili",
  "visibility": "internal",
  "project": "flugel-sunucu-ve-akis"
}
---
# Akış kişisel tercih profili

Gökalp’in Flugel Akış isteğindeki açık dil, hobi ve içerik tercihleri. Bu tercihler öğrenilmiş davranış ve Hermes önerilerinden önce gelir. Mevcut el ile takip kelimeleri Akış’ın takip tablosundan okunur.

```json
{
  "schema_version": 1,
  "preferred_languages": [
    "en",
    "tr",
    "ja"
  ],
  "excluded_topics": [
    "siyaset",
    "cinayet",
    "olumsuz yerel haber"
  ],
  "topics": {
    "oyun": 0.75,
    "anime": 0.65,
    "manga": 0.6,
    "müzik": 0.55,
    "hobi": 0.85
  },
  "source_weights": {},
  "tracked_topics": []
}
```

