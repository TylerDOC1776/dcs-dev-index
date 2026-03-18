#!/usr/bin/env python3
"""
Generate gh-pages Jekyll content from docs/ markdown files.
Writes to _pages_build/ — this directory is deployed to the gh-pages branch.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
DOCS = ROOT / "docs"
OUT = ROOT / "_pages_build"

NAV_ORDER = {
    "scripting-frameworks": 1,
    "mission-scripts": 2,
    "mission-generators": 3,
    "server-tools": 4,
    "dev-tools": 5,
    "aircraft-mods": 6,
}

CONFIG = """\
title: DCS Dev Index
description: Curated index of DCS World mods, scripts, and tools for mission designers and server operators.
remote_theme: just-the-docs/just-the-docs
color_scheme: dark
url: https://TylerDOC1776.github.io
baseurl: /dcs-dev-index
search_enabled: true
search:
  heading_level: 3
  previews: 3
footer_content: "Updated weekly by GitHub Actions."
"""


def extract_title(content):
    m = re.match(r"^# (.+)", content)
    return m.group(1) if m else None


def strip_h1(content):
    return re.sub(r"^# .+\n\n?", "", content, count=1)


def build_doc(src, title, nav_order):
    content = src.read_text(encoding="utf-8")
    body = strip_h1(content)
    frontmatter = f"---\ntitle: {title}\nnav_order: {nav_order}\n---\n\n"
    return frontmatter + body


def build_index():
    content = (ROOT / "README.md").read_text(encoding="utf-8")
    # Rewrite docs/X.md links to X.md (flat Jekyll layout)
    content = re.sub(r"\(docs/([^)]+)\)", r"(\1)", content)
    frontmatter = "---\ntitle: Home\nnav_order: 0\n---\n\n"
    return frontmatter + content


def main():
    if not DOCS.is_dir():
        print(f"ERROR: docs/ not found at {DOCS}", file=sys.stderr)
        return 1

    OUT.mkdir(exist_ok=True)

    # Write Jekyll config
    (OUT / "_config.yml").write_text(CONFIG, encoding="utf-8")

    # Write index
    (OUT / "index.md").write_text(build_index(), encoding="utf-8")

    # Process each doc
    count = 0
    for src in sorted(DOCS.glob("*.md")):
        stem = src.stem
        title = extract_title(src.read_text(encoding="utf-8")) or stem.replace("-", " ").title()
        nav_order = NAV_ORDER.get(stem, 99)
        out = OUT / src.name
        out.write_text(build_doc(src, title, nav_order), encoding="utf-8")
        print(f"  {src.name} -> nav_order {nav_order}")
        count += 1

    print(f"\nBuilt {count} pages + index to {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
