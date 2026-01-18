#!/usr/bin/env python3
"""
Generate implementation specification from upstream Gemini CLI.

Fetches actual code, extracts types/interfaces, and produces
a porting-focused document with code snippets.
"""

import os
import re
import base64
import requests
from datetime import datetime
from pathlib import Path
from typing import Optional

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
REPO = "google-gemini/gemini-cli"
BRANCH = "main"

HEADERS = {"Accept": "application/vnd.github+json"}
if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"

# Paths to fetch for each feature
FEATURE_PATHS = {
    "skills": [
        "packages/core/src/skills/skillLoader.ts",
        "packages/core/src/skills/skillManager.ts",
        "packages/cli/src/commands/skills/list.ts",
        "packages/cli/src/commands/skills/install.ts",
    ],
    "agents": [
        "packages/core/src/agents/types.ts",
        "packages/core/src/agents/registry.ts",
        "packages/core/src/agents/local-executor.ts",
        "packages/core/src/agents/codebase-investigator.ts",
    ],
    "hooks": [
        "packages/core/src/hooks/types.ts",
        "packages/core/src/hooks/hookRegistry.ts",
        "packages/core/src/hooks/hookRunner.ts",
        "packages/core/src/hooks/hookSystem.ts",
    ],
    "sessions": [
        "packages/cli/src/sessions/sessionUtils.ts",
        "packages/cli/src/sessions/sessions.ts",
        "packages/cli/src/ui/hooks/useSessionBrowser.ts",
    ],
}


def fetch_file(path: str) -> Optional[str]:
    """Fetch file content from GitHub."""
    url = f"https://api.github.com/repos/{REPO}/contents/{path}?ref={BRANCH}"
    resp = requests.get(url, headers=HEADERS)
    if resp.status_code != 200:
        return None
    data = resp.json()
    if data.get("encoding") == "base64":
        return base64.b64decode(data["content"]).decode("utf-8", errors="replace")
    return None


def extract_interfaces(content: str) -> list[dict]:
    """Extract TypeScript interfaces and types."""
    interfaces = []

    # Match interface definitions
    interface_pattern = r'(?:export\s+)?interface\s+(\w+)(?:<[^>]+>)?\s*(?:extends\s+[^{]+)?\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}'
    for match in re.finditer(interface_pattern, content, re.DOTALL):
        name = match.group(1)
        body = match.group(2).strip()
        interfaces.append({"type": "interface", "name": name, "body": body})

    # Match type definitions
    type_pattern = r'(?:export\s+)?type\s+(\w+)(?:<[^>]+>)?\s*=\s*([^;]+);'
    for match in re.finditer(type_pattern, content):
        name = match.group(1)
        body = match.group(2).strip()
        interfaces.append({"type": "type", "name": name, "body": body})

    # Match enums
    enum_pattern = r'(?:export\s+)?enum\s+(\w+)\s*\{([^}]+)\}'
    for match in re.finditer(enum_pattern, content, re.DOTALL):
        name = match.group(1)
        body = match.group(2).strip()
        interfaces.append({"type": "enum", "name": name, "body": body})

    return interfaces


def extract_classes(content: str) -> list[dict]:
    """Extract class definitions with key methods."""
    classes = []

    # Match class definitions
    class_pattern = r'(?:export\s+)?class\s+(\w+)(?:<[^>]+>)?(?:\s+(?:extends|implements)\s+[^{]+)?\s*\{'
    for match in re.finditer(class_pattern, content):
        name = match.group(1)
        start = match.end()

        # Find key method signatures (simplified)
        methods = []
        method_pattern = r'(?:async\s+)?(\w+)\s*\([^)]*\)\s*(?::\s*[^{]+)?\s*\{'
        # Look ahead ~2000 chars for methods
        class_body = content[start:start+3000]
        for m in re.finditer(method_pattern, class_body):
            method_name = m.group(1)
            if not method_name.startswith('_') and method_name not in ['constructor', 'if', 'for', 'while']:
                methods.append(method_name)

        if methods:
            classes.append({"name": name, "methods": methods[:10]})

    return classes


def extract_constants(content: str) -> list[dict]:
    """Extract important constants."""
    constants = []

    # Match const with string/number values
    const_pattern = r'(?:export\s+)?const\s+([A-Z_][A-Z0-9_]*)\s*(?::\s*\w+)?\s*=\s*([^;]+);'
    for match in re.finditer(const_pattern, content):
        name = match.group(1)
        value = match.group(2).strip()
        if len(value) < 100:  # Skip long values
            constants.append({"name": name, "value": value})

    return constants


def generate_feature_spec(feature: str, paths: list[str]) -> str:
    """Generate specification for a feature."""
    lines = [f"## {feature.title()}\n"]

    all_interfaces = []
    all_classes = []
    all_constants = []
    code_samples = []

    for path in paths:
        content = fetch_file(path)
        if not content:
            continue

        filename = Path(path).name
        lines.append(f"### Source: `{filename}`\n")

        # Extract types
        interfaces = extract_interfaces(content)
        if interfaces:
            all_interfaces.extend(interfaces)
            for iface in interfaces[:5]:  # Limit per file
                lines.append(f"```typescript")
                if iface["type"] == "interface":
                    lines.append(f"interface {iface['name']} {{")
                    lines.append(f"  {iface['body'][:500]}...")
                    lines.append("}")
                elif iface["type"] == "enum":
                    lines.append(f"enum {iface['name']} {{")
                    lines.append(f"  {iface['body'][:300]}")
                    lines.append("}")
                else:
                    lines.append(f"type {iface['name']} = {iface['body'][:200]}")
                lines.append("```\n")

        # Extract classes
        classes = extract_classes(content)
        if classes:
            all_classes.extend(classes)
            for cls in classes[:3]:
                lines.append(f"**Class `{cls['name']}`** - Methods: `{', '.join(cls['methods'][:5])}`\n")

        # Extract constants
        constants = extract_constants(content)
        if constants:
            all_constants.extend(constants)

    # Summary section
    if all_constants:
        lines.append("### Key Constants\n")
        lines.append("```typescript")
        for const in all_constants[:10]:
            lines.append(f"const {const['name']} = {const['value']};")
        lines.append("```\n")

    return "\n".join(lines)


def generate_full_spec():
    """Generate complete implementation specification."""
    now = datetime.now()

    lines = [
        "# Gemini CLI Implementation Specification (Auto-Generated)\n",
        f"**Generated:** {now.strftime('%Y-%m-%d %H:%M')}",
        f"**Source:** [{REPO}](https://github.com/{REPO}) @ `{BRANCH}`\n",
        "---\n",
    ]

    for feature, paths in FEATURE_PATHS.items():
        print(f"Processing {feature}...")
        spec = generate_feature_spec(feature, paths)
        lines.append(spec)
        lines.append("\n---\n")

    return "\n".join(lines)


def main():
    print("Generating implementation specification...")

    spec = generate_full_spec()

    output_dir = Path("reports")
    output_dir.mkdir(exist_ok=True)

    # Save dated version
    date_str = datetime.now().strftime("%Y-%m-%d")
    output_file = output_dir / f"spec-{date_str}.md"
    output_file.write_text(spec)
    print(f"Saved: {output_file}")

    # Save as latest
    latest_file = output_dir / "spec-latest.md"
    latest_file.write_text(spec)
    print(f"Latest: {latest_file}")


if __name__ == "__main__":
    main()
