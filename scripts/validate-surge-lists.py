#!/usr/bin/env python3
"""Validate Surge rule-set files.

This checks for common mistakes that make remote rule sets fail or behave
unexpectedly, such as wildcard values in DOMAIN rules.
"""

from __future__ import annotations

import argparse
from pathlib import Path

VALID_RULE_TYPES = {
    "DOMAIN",
    "DOMAIN-SUFFIX",
    "DOMAIN-KEYWORD",
    "IP-CIDR",
    "IP-CIDR6",
    "IP-ASN",
    "PROCESS-NAME",
    "USER-AGENT",
}


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    for line_no, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        parts = [part.strip() for part in line.split(",")]
        if len(parts) < 2:
            errors.append(f"{path}:{line_no}: expected at least rule type and value: {line}")
            continue

        rule_type, value = parts[0], parts[1]
        if rule_type not in VALID_RULE_TYPES:
            errors.append(f"{path}:{line_no}: unsupported rule type {rule_type!r}: {line}")

        if value.startswith("*."):
            errors.append(
                f"{path}:{line_no}: wildcard host {value!r} should be normalized to DOMAIN-SUFFIX"
            )

        if rule_type == "DOMAIN" and (":" in value or "/" in value):
            errors.append(f"{path}:{line_no}: DOMAIN value is not a host name: {line}")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args()

    errors: list[str] = []
    for path in args.files:
        errors.extend(validate_file(path))

    if errors:
        print("Surge rule validation failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print(f"Validated {len(args.files)} Surge rule-set files")


if __name__ == "__main__":
    main()
