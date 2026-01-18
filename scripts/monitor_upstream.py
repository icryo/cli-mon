#!/usr/bin/env python3
"""
Gemini CLI Upstream Monitor

Tracks releases, PRs, commits, and milestones from google-gemini/gemini-cli
and generates categorized reports for feature porting decisions.
"""

import os
import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional
import requests

UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "google-gemini/gemini-cli")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
DAYS_BACK = int(os.getenv("DAYS_BACK", "7"))
INCLUDE_COMMITS = os.getenv("INCLUDE_COMMITS", "true").lower() == "true"
LITE_MODE = os.getenv("LITE_MODE", "false").lower() == "true"  # Skip detailed PR fetching

REPORTS_DIR = Path("reports")
STATE_FILE = REPORTS_DIR / ".monitor_state.json"

# Feature categories for classification
FEATURE_CATEGORIES = {
    "shell": ["pty", "shell", "terminal", "bash", "powershell", "cmd", "exec"],
    "input": ["keyboard", "mouse", "key", "input", "keypress", "alt+", "ctrl+"],
    "streaming": ["stream", "json", "event", "delta", "chunk"],
    "hooks": ["hook", "before", "after", "middleware", "intercept"],
    "sessions": ["session", "history", "resume", "browser", "conversation"],
    "models": ["model", "gemini", "thinking", "budget", "router", "flash", "pro"],
    "mcp": ["mcp", "tool", "server", "discovery", "protocol"],
    "agents": ["agent", "subagent", "codebase", "investigator", "autonomous"],
    "ui": ["ui", "render", "display", "ink", "react", "component"],
    "config": ["config", "settings", "permission", "trust", "sandbox"],
}

HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}
if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"


def api_get(endpoint: str, params: Optional[dict] = None, retries: int = 3) -> dict | list:
    """Make GitHub API request with rate limit handling."""
    import time
    url = f"https://api.github.com/{endpoint}"

    for attempt in range(retries):
        resp = requests.get(url, headers=HEADERS, params=params)

        # Check rate limit
        remaining = int(resp.headers.get("X-RateLimit-Remaining", 1))
        if remaining == 0:
            reset_time = int(resp.headers.get("X-RateLimit-Reset", 0))
            wait = max(reset_time - int(time.time()), 1)
            if wait < 300:  # Wait up to 5 min
                print(f"  Rate limited, waiting {wait}s...")
                time.sleep(wait + 1)
                continue
            else:
                raise Exception(f"Rate limited. Reset in {wait}s. Use GITHUB_TOKEN for higher limits.")

        if resp.status_code == 403 and "rate limit" in resp.text.lower():
            if attempt < retries - 1:
                time.sleep(5)
                continue
            raise Exception("Rate limited. Set GITHUB_TOKEN env var for higher limits.")

        resp.raise_for_status()
        return resp.json()

    raise Exception("Max retries exceeded")


def load_state() -> dict:
    """Load previous monitoring state."""
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"last_run": None, "seen_releases": [], "seen_prs": [], "last_commit": None}


def save_state(state: dict):
    """Save monitoring state."""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2))


def classify_change(title: str, body: str = "") -> list[str]:
    """Classify a change into feature categories."""
    text = f"{title} {body}".lower()
    categories = []
    for cat, keywords in FEATURE_CATEGORIES.items():
        if any(kw in text for kw in keywords):
            categories.append(cat)
    return categories or ["other"]


def get_releases(since: datetime) -> list[dict]:
    """Fetch releases since date."""
    releases = api_get(f"repos/{UPSTREAM_REPO}/releases", {"per_page": 50})
    result = []
    for rel in releases:
        published = datetime.fromisoformat(rel["published_at"].replace("Z", "+00:00"))
        if published >= since:
            result.append({
                "tag": rel["tag_name"],
                "name": rel["name"],
                "published": rel["published_at"],
                "body": rel["body"] or "",
                "url": rel["html_url"],
                "prerelease": rel["prerelease"],
                "categories": classify_change(rel["name"], rel["body"] or ""),
            })
    return result


def get_merged_prs(since: datetime) -> list[dict]:
    """Fetch merged PRs since date."""
    # Search for merged PRs
    since_str = since.strftime("%Y-%m-%d")
    query = f"repo:{UPSTREAM_REPO} is:pr is:merged merged:>={since_str}"
    search = api_get("search/issues", {"q": query, "per_page": 100, "sort": "updated"})

    result = []
    for pr in search.get("items", []):
        pr_num = pr["number"]

        # In lite mode, skip detailed PR fetching to avoid rate limits
        if LITE_MODE:
            result.append({
                "number": pr_num,
                "title": pr["title"],
                "merged_at": pr.get("pull_request", {}).get("merged_at"),
                "author": pr["user"]["login"],
                "url": pr["html_url"],
                "body": pr.get("body") or "",
                "labels": [l["name"] for l in pr.get("labels", [])],
                "files_changed": 0,
                "additions": 0,
                "deletions": 0,
                "categories": classify_change(pr["title"], pr.get("body") or ""),
            })
        else:
            # Get PR details for more info
            try:
                pr_detail = api_get(f"repos/{UPSTREAM_REPO}/pulls/{pr_num}")
                result.append({
                    "number": pr_num,
                    "title": pr["title"],
                    "merged_at": pr_detail.get("merged_at"),
                    "author": pr["user"]["login"],
                    "url": pr["html_url"],
                    "body": pr.get("body") or "",
                    "labels": [l["name"] for l in pr.get("labels", [])],
                    "files_changed": pr_detail.get("changed_files", 0),
                    "additions": pr_detail.get("additions", 0),
                    "deletions": pr_detail.get("deletions", 0),
                    "categories": classify_change(pr["title"], pr.get("body") or ""),
                })
            except Exception as e:
                print(f"  Warning: Could not fetch PR #{pr_num}: {e}")
                # Fall back to basic info
                result.append({
                    "number": pr_num,
                    "title": pr["title"],
                    "merged_at": None,
                    "author": pr["user"]["login"],
                    "url": pr["html_url"],
                    "body": pr.get("body") or "",
                    "labels": [l["name"] for l in pr.get("labels", [])],
                    "files_changed": 0,
                    "additions": 0,
                    "deletions": 0,
                    "categories": classify_change(pr["title"], pr.get("body") or ""),
                })
    return result


def get_commits(since: datetime, branch: str = "main") -> list[dict]:
    """Fetch commits since date."""
    since_str = since.isoformat()
    commits = api_get(
        f"repos/{UPSTREAM_REPO}/commits",
        {"sha": branch, "since": since_str, "per_page": 100}
    )

    result = []
    for c in commits:
        commit = c["commit"]
        result.append({
            "sha": c["sha"][:7],
            "message": commit["message"].split("\n")[0],  # First line only
            "author": commit["author"]["name"],
            "date": commit["author"]["date"],
            "url": c["html_url"],
            "categories": classify_change(commit["message"]),
        })
    return result


def get_milestones() -> list[dict]:
    """Fetch open milestones."""
    milestones = api_get(f"repos/{UPSTREAM_REPO}/milestones", {"state": "open"})
    result = []
    for m in milestones:
        result.append({
            "title": m["title"],
            "description": m.get("description") or "",
            "due_on": m.get("due_on"),
            "open_issues": m["open_issues"],
            "closed_issues": m["closed_issues"],
            "url": m["html_url"],
            "progress": round(m["closed_issues"] / max(m["open_issues"] + m["closed_issues"], 1) * 100),
        })
    return result


def get_open_prs_by_label() -> dict[str, list]:
    """Get open PRs grouped by label for tracking upcoming features."""
    prs = api_get(f"repos/{UPSTREAM_REPO}/pulls", {"state": "open", "per_page": 100})
    by_label = {}
    for pr in prs:
        labels = [l["name"] for l in pr.get("labels", [])]
        for label in labels or ["unlabeled"]:
            if label not in by_label:
                by_label[label] = []
            by_label[label].append({
                "number": pr["number"],
                "title": pr["title"],
                "author": pr["user"]["login"],
                "url": pr["html_url"],
                "created": pr["created_at"],
                "categories": classify_change(pr["title"], pr.get("body") or ""),
            })
    return by_label


def generate_report(
    releases: list,
    prs: list,
    commits: list,
    milestones: list,
    open_prs: dict,
    since: datetime
) -> str:
    """Generate markdown report."""
    now = datetime.now(timezone.utc)

    lines = [
        f"# Gemini CLI Upstream Monitor Report",
        f"",
        f"**Generated:** {now.strftime('%Y-%m-%d %H:%M UTC')}  ",
        f"**Monitoring:** [{UPSTREAM_REPO}](https://github.com/{UPSTREAM_REPO})  ",
        f"**Period:** {since.strftime('%Y-%m-%d')} to {now.strftime('%Y-%m-%d')} ({DAYS_BACK} days)  ",
        f"",
        f"---",
        f"",
    ]

    # Summary
    lines.extend([
        f"## Summary",
        f"",
        f"| Metric | Count |",
        f"|--------|-------|",
        f"| New Releases | {len(releases)} |",
        f"| Merged PRs | {len(prs)} |",
        f"| Commits | {len(commits)} |",
        f"| Open Milestones | {len(milestones)} |",
        f"| Open PRs | {sum(len(v) for v in open_prs.values())} |",
        f"",
    ])

    # Category breakdown
    all_categories = {}
    for item in releases + prs + commits:
        for cat in item.get("categories", []):
            all_categories[cat] = all_categories.get(cat, 0) + 1

    if all_categories:
        lines.extend([
            f"### Changes by Category",
            f"",
        ])
        for cat, count in sorted(all_categories.items(), key=lambda x: -x[1]):
            lines.append(f"- **{cat}**: {count} changes")
        lines.append("")

    # Releases
    if releases:
        lines.extend([
            f"---",
            f"",
            f"## New Releases",
            f"",
        ])
        for rel in sorted(releases, key=lambda x: x["published"], reverse=True):
            prerelease = " (prerelease)" if rel["prerelease"] else ""
            cats = ", ".join(rel["categories"])
            lines.extend([
                f"### [{rel['tag']}]({rel['url']}){prerelease}",
                f"",
                f"**Released:** {rel['published'][:10]} | **Categories:** {cats}",
                f"",
            ])
            if rel["body"]:
                # Truncate long release notes
                body = rel["body"][:2000]
                if len(rel["body"]) > 2000:
                    body += "\n\n*[truncated]*"
                lines.extend([body, ""])

    # Merged PRs
    if prs:
        lines.extend([
            f"---",
            f"",
            f"## Merged Pull Requests",
            f"",
            f"| PR | Title | Author | Categories | Changes |",
            f"|---:|-------|--------|------------|---------|",
        ])
        for pr in sorted(prs, key=lambda x: x["merged_at"] or "", reverse=True):
            cats = ", ".join(pr["categories"])
            changes = f"+{pr['additions']}/-{pr['deletions']}"
            title = pr["title"][:60] + "..." if len(pr["title"]) > 60 else pr["title"]
            lines.append(
                f"| [#{pr['number']}]({pr['url']}) | {title} | @{pr['author']} | {cats} | {changes} |"
            )
        lines.append("")

        # Detailed PR breakdown by category
        lines.extend([
            f"### PRs by Category",
            f"",
        ])
        pr_by_cat = {}
        for pr in prs:
            for cat in pr["categories"]:
                if cat not in pr_by_cat:
                    pr_by_cat[cat] = []
                pr_by_cat[cat].append(pr)

        for cat in sorted(pr_by_cat.keys()):
            lines.append(f"<details><summary><strong>{cat}</strong> ({len(pr_by_cat[cat])} PRs)</summary>")
            lines.append("")
            for pr in pr_by_cat[cat]:
                lines.append(f"- [#{pr['number']}]({pr['url']}) {pr['title']}")
            lines.extend(["", "</details>", ""])

    # Commits (optional)
    if INCLUDE_COMMITS and commits:
        lines.extend([
            f"---",
            f"",
            f"## Recent Commits",
            f"",
            f"<details><summary>Show {len(commits)} commits</summary>",
            f"",
            f"| SHA | Message | Author | Date |",
            f"|-----|---------|--------|------|",
        ])
        for c in commits[:50]:  # Limit to 50
            msg = c["message"][:70] + "..." if len(c["message"]) > 70 else c["message"]
            msg = msg.replace("|", "\\|")
            lines.append(
                f"| [{c['sha']}]({c['url']}) | {msg} | {c['author']} | {c['date'][:10]} |"
            )
        lines.extend(["", "</details>", ""])

    # Milestones
    if milestones:
        lines.extend([
            f"---",
            f"",
            f"## Open Milestones",
            f"",
        ])
        for m in sorted(milestones, key=lambda x: x.get("due_on") or "9999"):
            due = f"Due: {m['due_on'][:10]}" if m["due_on"] else "No due date"
            lines.extend([
                f"### [{m['title']}]({m['url']})",
                f"",
                f"**Progress:** {m['progress']}% ({m['closed_issues']}/{m['open_issues'] + m['closed_issues']} issues) | {due}",
                f"",
            ])
            if m["description"]:
                lines.extend([m["description"], ""])

    # Open PRs by label (upcoming features)
    if open_prs:
        lines.extend([
            f"---",
            f"",
            f"## Upcoming Features (Open PRs)",
            f"",
        ])
        priority_labels = ["priority", "enhancement", "feature", "breaking"]
        for label in sorted(open_prs.keys()):
            if any(p in label.lower() for p in priority_labels):
                prs_list = open_prs[label]
                lines.append(f"### Label: `{label}` ({len(prs_list)} PRs)")
                lines.append("")
                for pr in prs_list[:10]:
                    cats = ", ".join(pr["categories"])
                    lines.append(f"- [#{pr['number']}]({pr['url']}) {pr['title']} ({cats})")
                lines.append("")

    # Porting recommendations
    lines.extend([
        f"---",
        f"",
        f"## Porting Recommendations",
        f"",
        f"Based on the changes above, consider reviewing:",
        f"",
    ])

    # Prioritize by category relevance
    priority_cats = ["hooks", "mcp", "agents", "streaming", "sessions"]
    for cat in priority_cats:
        cat_items = [p for p in prs if cat in p["categories"]]
        if cat_items:
            lines.append(f"### {cat.title()}")
            lines.append("")
            for pr in cat_items[:5]:
                lines.append(f"- [ ] [#{pr['number']}]({pr['url']}) {pr['title']}")
            lines.append("")

    return "\n".join(lines)


def main():
    print(f"Monitoring {UPSTREAM_REPO} for changes...")

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    state = load_state()

    since = datetime.now(timezone.utc) - timedelta(days=DAYS_BACK)

    print(f"Fetching releases since {since.date()}...")
    releases = get_releases(since)
    print(f"  Found {len(releases)} releases")

    print(f"Fetching merged PRs...")
    prs = get_merged_prs(since)
    print(f"  Found {len(prs)} merged PRs")

    commits = []
    if INCLUDE_COMMITS:
        print(f"Fetching commits...")
        commits = get_commits(since)
        print(f"  Found {len(commits)} commits")

    print(f"Fetching milestones...")
    milestones = get_milestones()
    print(f"  Found {len(milestones)} open milestones")

    print(f"Fetching open PRs...")
    open_prs = get_open_prs_by_label()
    total_open = sum(len(v) for v in open_prs.values())
    print(f"  Found {total_open} open PRs")

    # Generate dated report
    report = generate_report(releases, prs, commits, milestones, open_prs, since)

    # Save to dated file
    date_str = datetime.now().strftime("%Y-%m-%d")
    report_file = REPORTS_DIR / f"upstream-{date_str}.md"
    report_file.write_text(report)
    print(f"\nReport saved to {report_file}")

    # Also save as latest
    latest_file = REPORTS_DIR / "latest.md"
    latest_file.write_text(report)
    print(f"Latest report: {latest_file}")

    # Update state
    state["last_run"] = datetime.now(timezone.utc).isoformat()
    if releases:
        state["seen_releases"] = list(set(state.get("seen_releases", []) + [r["tag"] for r in releases]))
    if prs:
        state["seen_prs"] = list(set(state.get("seen_prs", []) + [p["number"] for p in prs]))
    if commits:
        state["last_commit"] = commits[0]["sha"]
    save_state(state)

    print("\nDone!")


if __name__ == "__main__":
    main()
