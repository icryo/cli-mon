#!/usr/bin/env python3
"""
Enhanced Gemini CLI Upstream Monitor

Features:
- File-level diff summaries for key directories
- Smart filtering (ignores docs/tests/workflows)
- Code change categorization and impact assessment
"""

import os
import json
import re
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional
from collections import defaultdict
import requests

UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "google-gemini/gemini-cli")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
DAYS_BACK = int(os.getenv("DAYS_BACK", "7"))

REPORTS_DIR = Path("reports")
STATE_FILE = REPORTS_DIR / ".monitor_state.json"

# Directories to focus on (high priority)
PRIORITY_DIRS = [
    "packages/core/src/hooks",
    "packages/core/src/agents",
    "packages/core/src/tools/mcp",
    "packages/core/src/services",
    "packages/core/src/tools",
    "packages/cli/src/hooks",
    "packages/cli/src/agents",
    "packages/cli/src/sessions",
    "packages/cli/src/ui",
]

# Directories to ignore
IGNORE_PATTERNS = [
    r"^\.github/",
    r"^docs/",
    r"^website/",
    r"/__tests__/",
    r"/test/",
    r"\.test\.",
    r"\.spec\.",
    r"\.md$",
    r"^README",
    r"^CHANGELOG",
    r"^LICENSE",
    r"\.json$",  # Config files (package.json tracked separately)
    r"\.lock$",
    r"\.yaml$",
    r"\.yml$",
]

# Special tracking for breaking changes
BREAKING_INDICATORS = [
    r"BREAKING",
    r"breaking change",
    r"removed.*deprecated",
    r"rename.*export",
    r"change.*signature",
    r"remove.*function",
    r"delete.*api",
]

HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}
if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"


def api_get(endpoint: str, params: Optional[dict] = None) -> dict | list:
    """Make GitHub API request with rate limit handling."""
    url = f"https://api.github.com/{endpoint}"

    for attempt in range(3):
        resp = requests.get(url, headers=HEADERS, params=params)

        remaining = int(resp.headers.get("X-RateLimit-Remaining", 100))
        if remaining < 10:
            print(f"  [Rate limit: {remaining} remaining]")

        if remaining == 0:
            reset_time = int(resp.headers.get("X-RateLimit-Reset", 0))
            wait = max(reset_time - int(time.time()), 1)
            if wait < 120:
                print(f"  Rate limited, waiting {wait}s...")
                time.sleep(wait + 1)
                continue
            raise Exception(f"Rate limited. Reset in {wait}s.")

        if resp.status_code == 403 and "rate limit" in resp.text.lower():
            time.sleep(5)
            continue

        resp.raise_for_status()
        return resp.json()

    raise Exception("Max retries exceeded")


def should_ignore_file(path: str) -> bool:
    """Check if file should be ignored."""
    for pattern in IGNORE_PATTERNS:
        if re.search(pattern, path, re.IGNORECASE):
            return True
    return False


def is_priority_file(path: str) -> bool:
    """Check if file is in a priority directory."""
    for dir_path in PRIORITY_DIRS:
        if path.startswith(dir_path):
            return True
    return False


def get_file_category(path: str) -> str:
    """Categorize a file by its path."""
    path_lower = path.lower()

    if "/hooks/" in path_lower or "hook" in path_lower:
        return "hooks"
    if "/agents/" in path_lower or "agent" in path_lower:
        return "agents"
    if "/mcp/" in path_lower:
        return "mcp"
    if "/services/" in path_lower:
        return "services"
    if "/tools/" in path_lower:
        return "tools"
    if "/sessions/" in path_lower:
        return "sessions"
    if "/ui/" in path_lower:
        return "ui"
    if "/config/" in path_lower:
        return "config"
    if "package.json" in path_lower:
        return "dependencies"

    return "other"


def check_breaking_change(text: str) -> bool:
    """Check if text indicates a breaking change."""
    for pattern in BREAKING_INDICATORS:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False


def get_pr_files(pr_number: int) -> list[dict]:
    """Fetch files changed in a PR."""
    try:
        files = api_get(f"repos/{UPSTREAM_REPO}/pulls/{pr_number}/files", {"per_page": 100})
        return files
    except Exception as e:
        print(f"  Warning: Could not fetch files for PR #{pr_number}: {e}")
        return []


def analyze_pr_diff(pr: dict) -> dict:
    """Analyze a PR's file changes in detail."""
    pr_number = pr["number"]
    files = get_pr_files(pr_number)

    analysis = {
        "number": pr_number,
        "title": pr["title"],
        "author": pr["user"]["login"],
        "url": pr["html_url"],
        "merged_at": pr.get("merged_at"),
        "labels": [l["name"] for l in pr.get("labels", [])],
        "is_breaking": check_breaking_change(pr["title"] + " " + (pr.get("body") or "")),
        "priority_files": [],
        "other_files": [],
        "ignored_files": [],
        "categories": set(),
        "total_additions": 0,
        "total_deletions": 0,
        "dependency_changes": False,
    }

    for f in files:
        path = f["filename"]
        file_info = {
            "path": path,
            "status": f["status"],  # added, removed, modified, renamed
            "additions": f["additions"],
            "deletions": f["deletions"],
            "category": get_file_category(path),
        }

        analysis["total_additions"] += f["additions"]
        analysis["total_deletions"] += f["deletions"]
        analysis["categories"].add(file_info["category"])

        if "package.json" in path:
            analysis["dependency_changes"] = True

        if should_ignore_file(path):
            analysis["ignored_files"].append(file_info)
        elif is_priority_file(path):
            analysis["priority_files"].append(file_info)
            # Fetch patch for priority files if small enough
            if f.get("patch") and len(f["patch"]) < 2000:
                file_info["patch_summary"] = summarize_patch(f["patch"])
        else:
            analysis["other_files"].append(file_info)

    analysis["categories"] = list(analysis["categories"])
    return analysis


def summarize_patch(patch: str) -> str:
    """Create a brief summary of a patch."""
    lines = patch.split("\n")
    added = [l[1:] for l in lines if l.startswith("+") and not l.startswith("+++")]
    removed = [l[1:] for l in lines if l.startswith("-") and not l.startswith("---")]

    # Look for key changes
    summary_parts = []

    # Function/class additions
    new_funcs = [l for l in added if re.match(r'\s*(export\s+)?(async\s+)?function\s+\w+', l)]
    if new_funcs:
        names = [re.search(r'function\s+(\w+)', f).group(1) for f in new_funcs[:3] if re.search(r'function\s+(\w+)', f)]
        if names:
            summary_parts.append(f"Added functions: {', '.join(names)}")

    # Interface/type additions
    new_types = [l for l in added if re.match(r'\s*(export\s+)?(interface|type|enum)\s+\w+', l)]
    if new_types:
        names = [re.search(r'(interface|type|enum)\s+(\w+)', t).group(2) for t in new_types[:3] if re.search(r'(interface|type|enum)\s+(\w+)', t)]
        if names:
            summary_parts.append(f"Added types: {', '.join(names)}")

    # Removed exports
    removed_exports = [l for l in removed if "export" in l and ("function" in l or "const" in l or "class" in l)]
    if removed_exports:
        summary_parts.append(f"Removed {len(removed_exports)} export(s)")

    if not summary_parts:
        summary_parts.append(f"+{len(added)} -{len(removed)} lines")

    return "; ".join(summary_parts)


STABLE_ONLY = os.getenv("STABLE_ONLY", "true").lower() == "true"

def get_releases_with_diff(since: datetime) -> list[dict]:
    """Fetch releases with comparison info."""
    releases = api_get(f"repos/{UPSTREAM_REPO}/releases", {"per_page": 50})
    result = []

    for rel in releases:
        # Skip prereleases if STABLE_ONLY is set
        if STABLE_ONLY and rel["prerelease"]:
            continue

        # Skip nightly/preview tags
        tag = rel["tag_name"].lower()
        if STABLE_ONLY and ("nightly" in tag or "preview" in tag or "alpha" in tag or "beta" in tag or "rc" in tag):
            continue

        published = datetime.fromisoformat(rel["published_at"].replace("Z", "+00:00"))
        if published >= since:
            result.append({
                "tag": rel["tag_name"],
                "name": rel["name"],
                "published": rel["published_at"],
                "body": rel["body"] or "",
                "url": rel["html_url"],
                "prerelease": rel["prerelease"],
                "is_breaking": check_breaking_change(rel["body"] or ""),
            })

    return result


def get_merged_prs_analyzed(since: datetime, limit: int = 30) -> list[dict]:
    """Fetch and analyze merged PRs."""
    since_str = since.strftime("%Y-%m-%d")
    query = f"repo:{UPSTREAM_REPO} is:pr is:merged merged:>={since_str}"
    search = api_get("search/issues", {"q": query, "per_page": min(limit, 100), "sort": "updated"})

    analyzed = []
    items = search.get("items", [])[:limit]

    for i, pr in enumerate(items):
        print(f"  Analyzing PR {i+1}/{len(items)}: #{pr['number']}")

        # Get full PR details
        pr_detail = api_get(f"repos/{UPSTREAM_REPO}/pulls/{pr['number']}")
        pr_detail["labels"] = pr.get("labels", [])

        analysis = analyze_pr_diff(pr_detail)

        # Only include if it has priority files or is breaking
        if analysis["priority_files"] or analysis["is_breaking"] or analysis["dependency_changes"]:
            analyzed.append(analysis)
        elif not analysis["ignored_files"] or analysis["other_files"]:
            # Has some non-ignored, non-priority changes
            analysis["_relevance"] = "low"
            analyzed.append(analysis)

    return analyzed


def generate_enhanced_report(releases: list, prs: list, since: datetime) -> str:
    """Generate enhanced markdown report with diff summaries."""
    now = datetime.now(timezone.utc)

    # Separate high-priority PRs
    breaking_prs = [p for p in prs if p["is_breaking"]]
    priority_prs = [p for p in prs if p["priority_files"] and not p["is_breaking"]]
    dep_prs = [p for p in prs if p["dependency_changes"] and p not in breaking_prs]
    other_prs = [p for p in prs if p not in breaking_prs and p not in priority_prs and p not in dep_prs]

    lines = [
        f"# Gemini CLI Upstream Monitor - Enhanced Report",
        f"",
        f"**Generated:** {now.strftime('%Y-%m-%d %H:%M UTC')}  ",
        f"**Repository:** [{UPSTREAM_REPO}](https://github.com/{UPSTREAM_REPO})  ",
        f"**Period:** {since.strftime('%Y-%m-%d')} to {now.strftime('%Y-%m-%d')}  ",
        f"",
    ]

    # Quick summary box
    lines.extend([
        f"## Quick Summary",
        f"",
        f"| Priority | Count | Action |",
        f"|----------|-------|--------|",
        f"| Breaking Changes | {len(breaking_prs)} | {'**REVIEW IMMEDIATELY**' if breaking_prs else 'None'} |",
        f"| Core Code Changes | {len(priority_prs)} | Review for porting |",
        f"| Dependency Updates | {len(dep_prs)} | Check compatibility |",
        f"| Other Changes | {len(other_prs)} | Low priority |",
        f"| New Releases | {len(releases)} | Check release notes |",
        f"",
    ])

    # Breaking changes section (highest priority)
    if breaking_prs:
        lines.extend([
            f"---",
            f"",
            f"## BREAKING CHANGES",
            f"",
        ])
        for pr in breaking_prs:
            lines.extend(format_pr_analysis(pr, detailed=True))

    # Core code changes
    if priority_prs:
        lines.extend([
            f"---",
            f"",
            f"## Core Code Changes (Priority Files)",
            f"",
            f"These PRs modified files in: `hooks/`, `agents/`, `mcp/`, `services/`, `tools/`",
            f"",
        ])

        # Group by category
        by_category = defaultdict(list)
        for pr in priority_prs:
            primary_cat = pr["categories"][0] if pr["categories"] else "other"
            by_category[primary_cat].append(pr)

        for cat in ["hooks", "agents", "mcp", "services", "tools", "sessions", "ui", "other"]:
            if cat in by_category:
                lines.append(f"### {cat.title()}")
                lines.append("")
                for pr in by_category[cat]:
                    lines.extend(format_pr_analysis(pr, detailed=True))

    # Dependency changes
    if dep_prs:
        lines.extend([
            f"---",
            f"",
            f"## Dependency Changes",
            f"",
            f"These PRs modified `package.json` - check for version bumps or new dependencies.",
            f"",
        ])
        for pr in dep_prs:
            lines.extend(format_pr_analysis(pr, detailed=False))

    # Releases
    if releases:
        lines.extend([
            f"---",
            f"",
            f"## Releases",
            f"",
        ])
        for rel in releases:
            breaking_badge = " **[BREAKING]**" if rel["is_breaking"] else ""
            prerelease = " *(prerelease)*" if rel["prerelease"] else ""
            lines.extend([
                f"### [{rel['tag']}]({rel['url']}){prerelease}{breaking_badge}",
                f"",
                f"Released: {rel['published'][:10]}",
                f"",
            ])
            if rel["body"]:
                # Extract key points from release notes
                body = rel["body"][:1500]
                if len(rel["body"]) > 1500:
                    body += "\n\n*[truncated - see full notes]*"
                lines.extend([body, ""])

    # Other changes (collapsed)
    if other_prs:
        lines.extend([
            f"---",
            f"",
            f"## Other Changes (Low Priority)",
            f"",
            f"<details><summary>{len(other_prs)} PRs with non-priority file changes</summary>",
            f"",
        ])
        for pr in other_prs[:20]:
            cats = ", ".join(pr["categories"][:3]) if pr["categories"] else "misc"
            lines.append(f"- [#{pr['number']}]({pr['url']}) {pr['title']} ({cats})")
        if len(other_prs) > 20:
            lines.append(f"- *... and {len(other_prs) - 20} more*")
        lines.extend(["", "</details>", ""])

    # Porting checklist
    lines.extend([
        f"---",
        f"",
        f"## Porting Checklist",
        f"",
    ])

    all_priority = breaking_prs + priority_prs
    if all_priority:
        for pr in all_priority[:15]:
            cats = ", ".join(pr["categories"][:2])
            breaking = " **[BREAKING]**" if pr["is_breaking"] else ""
            lines.append(f"- [ ] [#{pr['number']}]({pr['url']}) {pr['title'][:60]} ({cats}){breaking}")
    else:
        lines.append("*No high-priority changes to port this period.*")

    lines.append("")

    return "\n".join(lines)


def format_pr_analysis(pr: dict, detailed: bool = True) -> list[str]:
    """Format a single PR analysis for the report."""
    lines = []

    breaking = " **[BREAKING]**" if pr["is_breaking"] else ""
    deps = " **[DEPS]**" if pr["dependency_changes"] else ""

    lines.extend([
        f"#### [#{pr['number']}]({pr['url']}) {pr['title']}{breaking}{deps}",
        f"",
        f"**Author:** @{pr['author']} | **Changes:** +{pr['total_additions']}/-{pr['total_deletions']} | **Categories:** {', '.join(pr['categories'])}",
        f"",
    ])

    if detailed and pr["priority_files"]:
        lines.append("**Priority files changed:**")
        lines.append("")
        for f in pr["priority_files"][:10]:
            status_icon = {"added": "+", "removed": "-", "modified": "~", "renamed": ">"}.get(f["status"], "?")
            summary = f.get("patch_summary", "")
            summary_text = f" - {summary}" if summary else ""
            lines.append(f"- `{status_icon}` `{f['path']}`{summary_text}")

        if len(pr["priority_files"]) > 10:
            lines.append(f"- *... and {len(pr['priority_files']) - 10} more files*")
        lines.append("")

    return lines


def main():
    if not GITHUB_TOKEN:
        print("WARNING: No GITHUB_TOKEN set. Rate limits will be restrictive.")
        print("Set GITHUB_TOKEN environment variable for full functionality.")
        print("")

    print(f"Enhanced monitoring for {UPSTREAM_REPO}...")
    print(f"Focus directories: {', '.join(d.split('/')[-1] for d in PRIORITY_DIRS[:5])}...")

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    since = datetime.now(timezone.utc) - timedelta(days=DAYS_BACK)

    print(f"\nFetching releases since {since.date()}...")
    releases = get_releases_with_diff(since)
    print(f"  Found {len(releases)} releases")

    print(f"\nFetching and analyzing merged PRs...")
    prs = get_merged_prs_analyzed(since, limit=30)
    print(f"  Analyzed {len(prs)} relevant PRs")

    # Count priority items
    breaking = sum(1 for p in prs if p["is_breaking"])
    priority = sum(1 for p in prs if p["priority_files"])
    print(f"  - {breaking} breaking changes")
    print(f"  - {priority} with priority file changes")

    # Generate report
    report = generate_enhanced_report(releases, prs, since)

    # Save reports
    date_str = datetime.now().strftime("%Y-%m-%d")
    report_file = REPORTS_DIR / f"enhanced-{date_str}.md"
    report_file.write_text(report)
    print(f"\nReport saved to {report_file}")

    latest_file = REPORTS_DIR / "enhanced-latest.md"
    latest_file.write_text(report)
    print(f"Latest: {latest_file}")

    print("\nDone!")


if __name__ == "__main__":
    main()
