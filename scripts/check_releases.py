#!/usr/bin/env python3
"""
Check GitHub repos listed in docs/*.md for newer releases.
Updates **Release:** lines in-place when a newer version is found.
Appends a staleness note if the last commit is over 1.5 years old.
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
DOCS_DIR = Path(__file__).parent.parent / "docs"
STALE_DAYS = 548  # ~1.5 years

HEADER_RE = re.compile(
    r"^### \[[^\]]+\]\(https://github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)"
)
RELEASE_RE = re.compile(r"^\*\*Release:\*\* \[")


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


def get_repo_info(repo):
    """Returns (label, url, last_commit_date). Falls back: release -> tag -> commit."""
    label = url = None

    # 1. Try GitHub Releases
    try:
        data = gh_request(f"/repos/{repo}/releases/latest")
        label = data["tag_name"]
        url = data["html_url"]
    except urllib.error.HTTPError as e:
        if e.code != 404:
            print(f"  WARNING: HTTP {e.code} for {repo}", file=sys.stderr)
            return None, None, None
    except Exception as e:
        print(f"  WARNING: {e} for {repo}", file=sys.stderr)
        return None, None, None

    # 2. Fall back to git tags
    if not label:
        try:
            tags = gh_request(f"/repos/{repo}/tags?per_page=1")
            if tags:
                label = tags[0]["name"]
                url = f"https://github.com/{repo}/tree/{label}"
        except Exception as e:
            print(f"  WARNING: tags lookup failed for {repo}: {e}", file=sys.stderr)

    # 3. Get latest commit — used for commit fallback label and staleness check
    commit_date = None
    try:
        commits = gh_request(f"/repos/{repo}/commits?per_page=1")
        if commits:
            date_str = commits[0]["commit"]["committer"]["date"]
            commit_date = datetime.fromisoformat(
                date_str.replace("Z", "+00:00")
            ).date()
            if not label:
                # No release or tag — link to the repo itself, use date as label
                label = str(commit_date)
                url = f"https://github.com/{repo}"
    except Exception as e:
        print(f"  WARNING: commit lookup failed for {repo}: {e}", file=sys.stderr)

    return label, url, commit_date


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
            label, url, commit_date = get_repo_info(current_repo)
            if label and url:
                stale = ""
                if commit_date:
                    today = datetime.now(timezone.utc).date()
                    if (today - commit_date).days > STALE_DAYS:
                        stale = f" · last commit {commit_date}"
                new_line = f"**Release:** [{label}]({url}){stale}\n"
                if new_line != line:
                    print(f"  {current_repo}: -> {label}{stale}")
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
