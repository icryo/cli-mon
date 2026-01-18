#!/usr/bin/env python3
"""
Compare two Gemini CLI releases to identify changes for porting.

Usage:
    python compare_releases.py v0.17.0 v0.19.0
    python compare_releases.py v0.15.0  # Compare to latest
"""

import sys
import os
import requests
from datetime import datetime

UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "google-gemini/gemini-cli")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")

HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}
if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"


def api_get(endpoint: str, params=None):
    url = f"https://api.github.com/{endpoint}"
    resp = requests.get(url, headers=HEADERS, params=params)
    resp.raise_for_status()
    return resp.json()


def get_release_info(tag: str) -> dict:
    """Get release information by tag."""
    try:
        return api_get(f"repos/{UPSTREAM_REPO}/releases/tags/{tag}")
    except:
        # Try without 'v' prefix
        if not tag.startswith("v"):
            return api_get(f"repos/{UPSTREAM_REPO}/releases/tags/v{tag}")
        raise


def get_latest_release() -> dict:
    """Get latest release."""
    return api_get(f"repos/{UPSTREAM_REPO}/releases/latest")


def compare_commits(base: str, head: str) -> dict:
    """Compare two refs."""
    return api_get(f"repos/{UPSTREAM_REPO}/compare/{base}...{head}")


def get_prs_between(base_date: str, head_date: str) -> list:
    """Get PRs merged between two dates."""
    query = f"repo:{UPSTREAM_REPO} is:pr is:merged merged:{base_date}..{head_date}"
    result = api_get("search/issues", {"q": query, "per_page": 100, "sort": "updated"})
    return result.get("items", [])


def main():
    if len(sys.argv) < 2:
        print("Usage: python compare_releases.py <from_version> [to_version]")
        print("       python compare_releases.py v0.17.0 v0.19.0")
        print("       python compare_releases.py v0.15.0  # to latest")
        sys.exit(1)

    from_version = sys.argv[1]
    to_version = sys.argv[2] if len(sys.argv) > 2 else None

    print(f"Fetching release info...")

    from_release = get_release_info(from_version)
    if to_version:
        to_release = get_release_info(to_version)
    else:
        to_release = get_latest_release()
        to_version = to_release["tag_name"]

    from_date = from_release["published_at"][:10]
    to_date = to_release["published_at"][:10]

    print(f"\nComparing {from_version} ({from_date}) -> {to_version} ({to_date})")
    print("=" * 60)

    # Get commit comparison
    print(f"\nFetching commit diff...")
    comparison = compare_commits(from_release["tag_name"], to_release["tag_name"])

    print(f"\n## Commit Statistics")
    print(f"- Total commits: {comparison['total_commits']}")
    print(f"- Ahead by: {comparison['ahead_by']} commits")
    print(f"- Behind by: {comparison['behind_by']} commits")

    # File changes
    files = comparison.get("files", [])
    print(f"\n## Changed Files ({len(files)} files)")

    # Group by directory
    by_dir = {}
    for f in files:
        path = f["filename"]
        dir_name = path.split("/")[0] if "/" in path else "root"
        if dir_name not in by_dir:
            by_dir[dir_name] = []
        by_dir[dir_name].append({
            "path": path,
            "additions": f["additions"],
            "deletions": f["deletions"],
            "status": f["status"],
        })

    for dir_name in sorted(by_dir.keys()):
        files_in_dir = by_dir[dir_name]
        total_add = sum(f["additions"] for f in files_in_dir)
        total_del = sum(f["deletions"] for f in files_in_dir)
        print(f"\n### {dir_name}/ (+{total_add}/-{total_del})")
        for f in files_in_dir[:10]:
            print(f"  - {f['path']} ({f['status']}: +{f['additions']}/-{f['deletions']})")
        if len(files_in_dir) > 10:
            print(f"  ... and {len(files_in_dir) - 10} more")

    # PRs
    print(f"\nFetching merged PRs...")
    prs = get_prs_between(from_date, to_date)

    print(f"\n## Merged Pull Requests ({len(prs)} PRs)")
    for pr in prs:
        labels = [l["name"] for l in pr.get("labels", [])]
        label_str = f" [{', '.join(labels)}]" if labels else ""
        print(f"- #{pr['number']}: {pr['title']}{label_str}")

    # Release notes
    print(f"\n## Release Notes")
    print(f"\n### {to_version}")
    print(to_release.get("body", "No release notes") or "No release notes")

    # Key files to review
    print(f"\n## Key Files to Review for Porting")
    priority_paths = ["hooks", "agents", "mcp", "services", "tools"]
    for p in priority_paths:
        matching = [f for f in files if f["filename"].startswith(f"packages/") and p in f["filename"]]
        if matching:
            print(f"\n### {p}/")
            for f in matching[:5]:
                print(f"  - {f['filename']}")


if __name__ == "__main__":
    main()
