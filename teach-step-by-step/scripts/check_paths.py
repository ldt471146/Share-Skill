#!/usr/bin/env python3
"""Check that local paths referenced from SKILL.md exist."""

from __future__ import annotations

import re
import sys
from pathlib import Path


PATH_RE = re.compile(r"`((?:rules|workflows|references|scripts)/[^`]+)`")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_paths.py <skill-dir>", file=sys.stderr)
        return 2

    skill_dir = Path(sys.argv[1]).resolve()
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        print(f"missing SKILL.md: {skill_md}", file=sys.stderr)
        return 1

    text = skill_md.read_text(encoding="utf-8")
    paths = sorted(set(PATH_RE.findall(text)))
    missing = [p for p in paths if not (skill_dir / p).exists()]

    if missing:
        print("Missing referenced paths:")
        for p in missing:
            print(f"- {p}")
        return 1

    print(f"All {len(paths)} referenced local paths exist.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
