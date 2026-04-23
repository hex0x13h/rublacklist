Этот репозиторий содержит набор правил с доменами, заблокированными в России, и связанных списков обхода.

Структура:

- `rules/aggregates/all-bypass.list`
  Итоговый объединенный список правил обхода.

- `rules/services/`
  Отдельные списки по сервисам.

- `rules/categories/`
  Общие и смешанные подборки, которые не относятся к одному сервису.

- `sources/antifilter-domains.list`
  Исходный внешний список из `https://antifilter.download/`.

- `Amnezia/bypass.json`
  JSON-версия списка для Amnezia.

Переименование файлов:

- `bypass.list` -> `rules/aggregates/all-bypass.list`
- `claude.list` -> `rules/services/service-claude.list`
- `google.list` -> `rules/services/service-google.list`
- `openai.list` -> `rules/services/service-openai.list`
- `snapchat.list` -> `rules/services/service-snapchat.list`
- `spotify.list` -> `rules/services/service-spotify.list`
- `telegram.list` -> `rules/services/service-telegram.list`
- `udemy.list` -> `rules/services/service-udemy.list`
- `whatsapp.list` -> `rules/services/service-whatsapp.list`
- `x.list` -> `rules/services/service-x.list`
- `youtube.list` -> `rules/services/service-youtube.list`
- `rule.list` -> `rules/categories/category-general-services.list`
- `ros.list` -> `rules/categories/category-civil-society-and-privacy.list`
- `san.list` -> `rules/categories/category-manual-misc.list`
- `uncategorized.list` -> `rules/categories/category-uncategorized.list`
- `antifilter/domains.list` -> `sources/antifilter-domains.list`

Удалено:

- `merged_bypass_list/merged_bypass.list`
  Полный дубликат `bypass.list`.

Источники:

- `https://antifilter.download/`
- `https://iplist.opencck.org/`
