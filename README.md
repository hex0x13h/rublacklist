# rublacklist

Surge-compatible rule lists for services and domains that should be routed through a bypass/proxy policy.

## Surge usage

Use the raw GitHub URLs with `RULE-SET` in your Surge profile. Replace `"♻️ 手动切换"` with the policy or policy group you want to use.

### Aggregate list

```ini
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/aggregates/all-bypass.list,"♻️ 手动切换"
```

### Service lists

```ini
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

### Category and ASN lists

```ini
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/asn/asn-facebook.list,"♻️ 手动切换"
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/categories/category-civil-society-and-privacy.list,"♻️ 手动切换"
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/categories/category-general-services.list,"♻️ 手动切换"
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/categories/category-manual-misc.list,"♻️ 手动切换"
RULE-SET,https://raw.githubusercontent.com/itworksig/rublacklist/refs/heads/main/rules/categories/category-uncategorized.list,"♻️ 手动切换"
```

## Rule format

Lists are plain Surge rule-set files. Typical entries:

```ini
DOMAIN-SUFFIX,example.com
DOMAIN,exact.example.com
DOMAIN-KEYWORD,keyword
IP-CIDR,203.0.113.0/24,no-resolve
IP-CIDR6,2001:db8::/32,no-resolve
IP-ASN,32934,no-resolve
```

Do **not** write wildcard domains as `DOMAIN,*.example.com`. The normalization script converts those to `DOMAIN-SUFFIX,example.com`, because Surge `DOMAIN` is exact-match only.

## Maintenance

Run the same normalization/merge/validation flow locally:

```bash
{
  find rules/services -name "*.list" | sort
  find rules/asn -name "*.list" | sort
  find rules/categories -name "*.list" | sort
  find sources -name "*.list" | sort
} > rule-files.txt

python3 scripts/normalize-surge-lists.py --global-dedupe $(cat rule-files.txt)
cat $(cat rule-files.txt) | sort -u > bypass.list
cp bypass.list rules/aggregates/all-bypass.list
python3 scripts/validate-surge-lists.py $(cat rule-files.txt) bypass.list rules/aggregates/all-bypass.list
rm -f rule-files.txt
```

The GitHub Action also normalizes, validates, and rebuilds aggregate outputs on pushes to `main`.

## Legacy README

The original Russian README is kept as [`README.txt`](README.txt).
