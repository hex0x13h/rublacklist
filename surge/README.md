# Surge snippets

Copy one of these snippets into the `[Rule]` section of your Surge profile.

## Aggregate bypass/proxy list

Use this if you want every rule in the repository to use one policy group:

```ini
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/aggregates/all-bypass.list,"♻️ 手动切换"
```

## Split service/category lists

Use this if you want separate policy groups for OpenAI or Netflix:

```ini
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/asn/asn-facebook.list,"♻️ 手动切换"
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/categories/category-civil-society-and-privacy.list,"♻️ 手动切换"
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/categories/category-general-services.list,"♻️ 手动切换"
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/categories/category-manual-misc.list,"♻️ 手动切换"
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/categories/category-uncategorized.list,"♻️ 手动切换"
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/services/service-youtube.list,"♻️ 手动切换"
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/services/service-x.list,"♻️ 手动切换"
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/services/service-whatsapp.list,"♻️ 手动切换"
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/services/service-udemy.list,"♻️ 手动切换"
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/services/service-telegram.list,"♻️ 手动切换"
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/services/service-spotify.list,"♻️ 手动切换"
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/services/service-snapchat.list,"♻️ 手动切换"
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/services/service-reddit.list,"♻️ 手动切换"
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/services/service-openai.list,"🧲 OpenAI"
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/services/service-google.list,"♻️ 手动切换"
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/services/service-claude.list,"🧲 OpenAI"
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/services/service-netflix.list,"🎬 Netflix"
```
