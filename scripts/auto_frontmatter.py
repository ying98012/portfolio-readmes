#!/usr/bin/env python3
"""Add Pages CMS front matter to pure Markdown files under _projects/."""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS_DIR = ROOT / "_projects"
HEADING_RE = re.compile(r"^#\s+(.+)$")


def has_front_matter(text: str) -> bool:
    return text.startswith("---\n") or text.startswith("---\r\n")


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def extract_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        match = HEADING_RE.match(line.strip())
        if match:
            return match.group(1).strip()
    return fallback


def ensure_front_matter(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if has_front_matter(text):
        return False

    slug = path.stem
    title = extract_title(text, slug)
    front_matter = (
        "---\n"
        f"title: {yaml_quote(title)}\n"
        f"slug: {yaml_quote(slug)}\n"
        f"updatedAt: {date.today().isoformat()}\n"
        "---\n\n"
    )
    path.write_text(front_matter + text.lstrip("\n"), encoding="utf-8", newline="\n")
    return True


def main() -> int:
    if not PROJECTS_DIR.is_dir():
        print(f"Missing directory: {PROJECTS_DIR}", file=sys.stderr)
        return 1

    changed = []
    for path in sorted(PROJECTS_DIR.glob("*.md")):
        if ensure_front_matter(path):
            changed.append(path.relative_to(ROOT).as_posix())

    if changed:
        print("Added front matter to:")
        for item in changed:
            print(f"  - {item}")
    else:
        print("No pure Markdown files needed front matter.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
