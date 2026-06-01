#!/usr/bin/env python3
"""Normalize Surge rule lists and remove duplicates.

The script keeps the first occurrence of a rule according to the file order
passed on the command line. Comments and blank lines are ignored in generated
output because these lists are consumed as remote rule sets.
"""

from __future__ import annotations

import argparse
import json
import ipaddress
from pathlib import Path


DOMAIN_RULES = {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD"}
CIDR_RULES = {"IP-CIDR", "IP-CIDR6"}
NAT64_PREFIX = ipaddress.ip_network("64:ff9b::/96")


def normalize_line(raw_line: str) -> str | None:
    line = raw_line.strip()
    if not line or line.startswith("#"):
        return None

    parts = [part.strip() for part in line.split(",")]
    if len(parts) < 2:
        return None

    rule_type = parts[0].upper()
    value = parts[1]

    if not value:
        return None

    if rule_type in DOMAIN_RULES:
        value = value.lower()
        # Surge domain rules must be host names, not IPv6 literals/CIDRs.
        if ":" in value or "/" in value:
            return None

    if rule_type in CIDR_RULES:
        try:
            network = ipaddress.ip_network(value, strict=False)
        except ValueError:
            return None

        if rule_type == "IP-CIDR6" and network == NAT64_PREFIX:
            return None

        value = str(network)
        if network.version == 6:
            rule_type = "IP-CIDR6"
        else:
            rule_type = "IP-CIDR"

    tail = []
    for part in parts[2:]:
        option = part.lower()
        if option and option not in tail:
            tail.append(option)

    return ",".join([rule_type, value, *tail])


def normalize_files(paths: list[Path], global_dedupe: bool) -> None:
    global_seen: set[str] = set()

    for path in paths:
        file_seen: set[str] = set()
        output: list[str] = []

        for raw_line in path.read_text(encoding="utf-8").splitlines():
            normalized = normalize_line(raw_line)
            if normalized is None:
                continue
            if normalized in file_seen:
                continue
            if global_dedupe and normalized in global_seen:
                continue

            file_seen.add(normalized)
            global_seen.add(normalized)
            output.append(normalized)

        path.write_text("\n".join(output) + ("\n" if output else ""), encoding="utf-8")


def write_amnezia_json(input_path: Path, output_path: Path) -> None:
    domains: set[str] = set()

    for raw_line in input_path.read_text(encoding="utf-8").splitlines():
        normalized = normalize_line(raw_line)
        if normalized is None:
            continue

        rule_type, value, *_ = normalized.split(",")
        if rule_type in {"DOMAIN", "DOMAIN-SUFFIX"}:
            domains.add(value)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    payload = [{"hostname": domain, "ip": ""} for domain in sorted(domains)]
    output_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=4) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--global-dedupe", action="store_true")
    parser.add_argument("--amnezia-json", type=Path)
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args()

    if args.amnezia_json:
        if len(args.files) != 1:
            parser.error("--amnezia-json expects exactly one input list")
        write_amnezia_json(args.files[0], args.amnezia_json)
        return

    normalize_files(args.files, args.global_dedupe)


if __name__ == "__main__":
    main()
