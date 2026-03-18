#!/usr/bin/env python3
"""
Check GitHub repos listed in docs/*.md for newer releases.
Updates **Release:** lines in-place when a newer version is found.
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
DOCS_DIR = Path(__file__).parent.parent / "docs"

HEADER_RE = re.compile(
    r"^### \[[^\]]+\]\(https://github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)"
)
RELEASE_RE = re.compile(
    r"^\*\*Release:\*\* \[.*?\]\(https://github\.com/[^)]+\)$"
)


def gh_request(path):
    url = f"https://api.github.com{path}"
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "dcs-dev-index/check_releases")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if GITHUB_TOKEN:
        req.add_header("Authorization", f"Bearer {GITHUB_TOKEN}")
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode())


def latest_release(repo):
    try:
        data = gh_request(f"/repos/{repo}/releases/latest")
        return data["tag_name"], data["html_url"]
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None, None
        print(f"  WARNING: HTTP {e.code} for {repo}", file=sys.stderr)
        return None, None
    except Exception as e:
        print(f"  WARNING: {e} for {repo}", file=sys.stderr)
        return None, None


def process_file(path):
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    changed = False
    current_repo = None

    for i, line in enumerate(lines):
        stripped = line.rstrip("\r\n")

        if stripped.startswith("#"):
            current_repo = None
            m = HEADER_RE.match(stripped)
            if m:
                current_repo = m.group(1)
            continue

        if current_repo and RELEASE_RE.match(stripped):
            tag, url = latest_release(current_repo)
            if tag and url:
                new_line = f"**Release:** [{tag}]({url})\n"
                if new_line != line:
                    print(f"  {current_repo}: -> {tag}")
                    lines[i] = new_line
                    changed = True
            current_repo = None

    if changed:
        path.write_text("".join(lines), encoding="utf-8")
    return changed


def main():
    if not DOCS_DIR.is_dir():
        print(f"ERROR: docs/ not found at {DOCS_DIR}", file=sys.stderr)
        return 1

    any_changed = False
    for path in sorted(DOCS_DIR.glob("*.md")):
        print(f"Checking {path.name}...")
        if process_file(path):
            any_changed = True

    if any_changed:
        print("\nRelease links updated.")
    else:
        print("\nAll release links are current.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
