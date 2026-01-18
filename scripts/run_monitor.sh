#!/bin/bash
# Quick local runner for upstream monitoring

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"

# Defaults
DAYS_BACK=${1:-7}
INCLUDE_COMMITS=${2:-true}

cd "$REPO_DIR"

# Check for dependencies
if ! python3 -c "import requests" 2>/dev/null; then
    echo "Installing dependencies..."
    pip install requests PyGithub
fi

# Run monitor
echo "Monitoring gemini-cli upstream (last $DAYS_BACK days)..."
DAYS_BACK=$DAYS_BACK INCLUDE_COMMITS=$INCLUDE_COMMITS python3 scripts/monitor_upstream.py

echo ""
echo "=== Report Preview ==="
head -100 reports/latest.md

echo ""
echo "Full report: reports/latest.md"
