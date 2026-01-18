#!/usr/bin/env python3
"""
Focused Gemini CLI Monitor

Tracks only: Skills, Agents/Subagents, Hooks
Ignores: UI polish, docs, tests, internal refactoring
"""

import os
import json
import re
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
import requests

UPSTREAM_REPO = "google-gemini/gemini-cli"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
DAYS_BACK = int(os.getenv("DAYS_BACK", "14"))
FORK_VERSION = os.getenv("FORK_VERSION", "v0.14.0")

REPORTS_DIR = Path("reports")

# ONLY these directories matter
WATCH_PATTERNS = {
    "skills": [
        "packages/core/src/skills",
        "packages/cli/src/commands/skills",
        "skill",
    ],
    "agents": [
        "packages/core/src/agents",
        "packages/cli/src/agents",
        "subagent",
        "a2a",
    ],
    "hooks": [
        "packages/core/src/hooks",
        "packages/cli/src/ui/hooks",
        "packages/cli/src/commands/hooks",
        "hookRegistry",
        "hookRunner",
    ],
    "sessions": [
        "packages/cli/src/sessions",
        "packages/cli/src/utils/session",
        "packages/core/src/services/session",
        "useSessionBrowser",
        "useSessionResume",
        "sessionStorage",
    ],
}

HEADERS = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"


def api_get(endpoint, params=None):
    url = f"https://api.github.com/{endpoint}"
    for _ in range(3):
        resp = requests.get(url, headers=HEADERS, params=params)
        if resp.status_code == 403 and "rate limit" in resp.text.lower():
            time.sleep(5)
            continue
        resp.raise_for_status()
        return resp.json()
    raise Exception("Rate limited")


def classify_file(path):
    """Return which feature area a file belongs to, or None."""
    path_lower = path.lower()
    for area, patterns in WATCH_PATTERNS.items():
        for p in patterns:
            if p.lower() in path_lower:
                return area
    return None


def get_stable_releases():
    """Get stable releases only."""
    releases = api_get(f"repos/{UPSTREAM_REPO}/releases", {"per_page": 30})
    stable = []
    for r in releases:
        tag = r["tag_name"].lower()
        if r["prerelease"] or "nightly" in tag or "preview" in tag:
            continue
        stable.append({
            "tag": r["tag_name"],
            "date": r["published_at"][:10],
            "url": r["html_url"],
        })
    return stable


def get_prs_for_features(since_date):
    """Get PRs that touch our watched features."""
    since_str = since_date.strftime("%Y-%m-%d")

    results = {"skills": [], "agents": [], "hooks": []}

    # Search merged PRs
    query = f"repo:{UPSTREAM_REPO} is:pr is:merged merged:>={since_str}"
    search = api_get("search/issues", {"q": query, "per_page": 100, "sort": "updated"})

    for pr in search.get("items", []):
        pr_num = pr["number"]
        title = pr["title"].lower()
        body = (pr.get("body") or "").lower()
        text = f"{title} {body}"

        # Quick keyword check first
        dominated_by = None
        if "skill" in text:
            dominated_by = "skills"
        elif "agent" in text or "subagent" in text or "a2a" in text:
            dominated_by = "agents"
        elif "hook" in text:
            dominated_by = "hooks"

        if not dominated_by:
            continue

        # Get files to confirm
        try:
            files = api_get(f"repos/{UPSTREAM_REPO}/pulls/{pr_num}/files", {"per_page": 50})
        except:
            files = []

        relevant_files = []
        areas_touched = set()
        for f in files:
            area = classify_file(f["filename"])
            if area:
                areas_touched.add(area)
                relevant_files.append({
                    "path": f["filename"],
                    "area": area,
                    "changes": f["additions"] + f["deletions"],
                })

        if not areas_touched:
            continue

        pr_info = {
            "number": pr_num,
            "title": pr["title"],
            "url": pr["html_url"],
            "author": pr["user"]["login"],
            "merged": pr.get("pull_request", {}).get("merged_at", "")[:10],
            "files": relevant_files[:5],
            "total_files": len(relevant_files),
        }

        # Add to primary area
        primary = dominated_by if dominated_by in areas_touched else list(areas_touched)[0]
        results[primary].append(pr_info)

    return results


def get_open_prs_for_features():
    """Get open PRs for watched features (what's coming)."""
    results = {"skills": [], "agents": [], "hooks": []}

    prs = api_get(f"repos/{UPSTREAM_REPO}/pulls", {"state": "open", "per_page": 100})

    for pr in prs:
        title = pr["title"].lower()
        body = (pr.get("body") or "").lower()
        text = f"{title} {body}"

        labels = [l["name"] for l in pr.get("labels", [])]
        priority = next((l for l in labels if l.startswith("priority/")), "")

        area = None
        if "skill" in text:
            area = "skills"
        elif "agent" in text or "subagent" in text:
            area = "agents"
        elif "hook" in text:
            area = "hooks"

        if area:
            results[area].append({
                "number": pr["number"],
                "title": pr["title"],
                "url": pr["html_url"],
                "priority": priority,
                "updated": pr["updated_at"][:10],
            })

    return results


def compare_to_fork():
    """Compare current stable to fork version."""
    try:
        compare = api_get(f"repos/{UPSTREAM_REPO}/compare/{FORK_VERSION}...main")

        changes = {"skills": [], "agents": [], "hooks": []}

        for f in compare.get("files", []):
            area = classify_file(f["filename"])
            if area:
                changes[area].append({
                    "path": f["filename"],
                    "status": f["status"],
                    "changes": f["additions"] + f["deletions"],
                })

        return {
            "commits_behind": compare["ahead_by"],
            "files": changes,
        }
    except Exception as e:
        return {"error": str(e)}


def generate_report(releases, merged_prs, open_prs, fork_diff):
    """Generate focused markdown report."""
    now = datetime.now(timezone.utc)

    lines = [
        f"# Gemini CLI Feature Tracker",
        f"",
        f"**Updated:** {now.strftime('%Y-%m-%d %H:%M UTC')}",
        f"**Your Fork:** {FORK_VERSION}",
        f"**Latest Stable:** {releases[0]['tag'] if releases else 'Unknown'}",
        f"**Commits Behind:** {fork_diff.get('commits_behind', '?')}",
        f"",
        f"---",
        f"",
    ]

    # Summary counts
    total_merged = sum(len(v) for v in merged_prs.values())
    total_open = sum(len(v) for v in open_prs.values())

    lines.extend([
        f"## Summary (Last {DAYS_BACK} Days)",
        f"",
        f"| Feature | Merged PRs | Open PRs | Files Changed Since Fork |",
        f"|---------|------------|----------|--------------------------|",
    ])

    for area in ["skills", "agents", "hooks"]:
        merged = len(merged_prs.get(area, []))
        opened = len(open_prs.get(area, []))
        files = len(fork_diff.get("files", {}).get(area, []))
        lines.append(f"| **{area.title()}** | {merged} | {opened} | {files} |")

    lines.extend(["", "---", ""])

    # Each feature area
    for area in ["skills", "agents", "hooks"]:
        lines.append(f"## {area.title()}")
        lines.append("")

        # Merged PRs
        merged = merged_prs.get(area, [])
        if merged:
            lines.append(f"### Recently Merged ({len(merged)})")
            lines.append("")
            for pr in merged[:10]:
                lines.append(f"- [#{pr['number']}]({pr['url']}) {pr['title']}")
                if pr.get("files"):
                    for f in pr["files"][:3]:
                        lines.append(f"  - `{f['path']}`")
            lines.append("")

        # Open PRs (what's coming)
        opened = open_prs.get(area, [])
        if opened:
            lines.append(f"### Coming Soon ({len(opened)} open)")
            lines.append("")
            for pr in sorted(opened, key=lambda x: x.get("priority", "z"))[:7]:
                prio = f" **[{pr['priority']}]**" if pr.get("priority") else ""
                lines.append(f"- [#{pr['number']}]({pr['url']}) {pr['title']}{prio}")
            lines.append("")

        # Files changed since fork
        files = fork_diff.get("files", {}).get(area, [])
        if files:
            lines.append(f"### Files Changed Since {FORK_VERSION}")
            lines.append("")
            for f in sorted(files, key=lambda x: -x["changes"])[:10]:
                lines.append(f"- `{f['status']}` `{f['path']}` (+{f['changes']})")
            if len(files) > 10:
                lines.append(f"- *... and {len(files) - 10} more*")
            lines.append("")

        lines.append("---")
        lines.append("")

    # Stable releases
    lines.extend([
        f"## Recent Stable Releases",
        f"",
    ])
    for r in releases[:5]:
        lines.append(f"- [{r['tag']}]({r['url']}) ({r['date']})")

    lines.append("")

    return "\n".join(lines)


def main():
    print(f"Focused monitor: Skills, Agents, Hooks")
    print(f"Fork version: {FORK_VERSION}")

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    since = datetime.now(timezone.utc) - timedelta(days=DAYS_BACK)

    print(f"\nFetching stable releases...")
    releases = get_stable_releases()
    print(f"  Latest: {releases[0]['tag'] if releases else 'None'}")

    print(f"\nFetching merged PRs (last {DAYS_BACK} days)...")
    merged_prs = get_prs_for_features(since)
    for area, prs in merged_prs.items():
        print(f"  {area}: {len(prs)} PRs")

    print(f"\nFetching open PRs...")
    open_prs = get_open_prs_for_features()
    for area, prs in open_prs.items():
        print(f"  {area}: {len(prs)} open")

    print(f"\nComparing to {FORK_VERSION}...")
    fork_diff = compare_to_fork()
    if "error" not in fork_diff:
        print(f"  {fork_diff['commits_behind']} commits behind")

    report = generate_report(releases, merged_prs, open_prs, fork_diff)

    report_file = REPORTS_DIR / "features.md"
    report_file.write_text(report)
    print(f"\nReport: {report_file}")


if __name__ == "__main__":
    main()
