#!/usr/bin/env python3
"""Validate that every row in each data/*.csv has the header's field count.

Catches the two classic hand-edited-CSV bugs:
  - a trailing comma (an extra empty field), and
  - an unquoted comma inside a value (which splits one field into two).

Uses the stdlib csv parser, so commas inside properly *quoted* fields are fine.
Exits non-zero if any row's field count differs from its header's.

Usage:
    scripts/validate_csv.py                # all data/*.csv
    scripts/validate_csv.py data/foo.csv   # specific file(s)
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path


def validate(path: str) -> list[str]:
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    if not rows:
        return [f"{path}: empty file (no header)"]
    expected = len(rows[0])
    errors = []
    for lineno, row in enumerate(rows[1:], start=2):
        if len(row) != expected:
            errors.append(
                f"{path}:{lineno}: expected {expected} fields, found {len(row)} -> {row}"
            )
    return errors


def main(argv: list[str]) -> int:
    repo_root = Path(__file__).resolve().parent.parent
    targets = argv[1:] or sorted(str(p) for p in (repo_root / "data").glob("*.csv"))
    if not targets:
        print("no CSV files found under data/", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    for t in targets:
        errs = validate(t)
        all_errors += errs
        print(f"  {'FAIL' if errs else 'ok  '}  {t}  ({len(errs)} issue(s))")

    if all_errors:
        print("\nField-count mismatches:", file=sys.stderr)
        for e in all_errors:
            print("  " + e, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
