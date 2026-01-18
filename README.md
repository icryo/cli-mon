# cli-mon

CLI feature tracker for porting upstream changes to forks.

## Gemini CLI

Tracking [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) for porting to forks.

## Tracked Features

| Feature | Files | Description |
|---------|-------|-------------|
| **Skills** | 7 | New extensibility system - discover, load, activate skills |
| **Agents** | 15 | Agent registry, subagents, A2A, model routing |
| **Hooks** | 11 | Event system - before/after tool, session, agent hooks |
| **Sessions** | 8 | Session browser, resume, cleanup |

## Structure

```
code/                    # Source extracted from upstream (Apache 2.0)
├── skills/
│   ├── core/            skillManager.ts, skillLoader.ts
│   └── commands/        install, uninstall, enable, disable, list
├── agents/
│   └── core/            registry.ts, local-executor.ts, generalist-agent.ts,
│                        codebase-investigator.ts, a2a-client-manager.ts...
├── hooks/
│   ├── core/            hookSystem.ts, hookRunner.ts, hookRegistry.ts...
│   └── commands/        migrate.ts
└── sessions/            useSessionBrowser.ts, sessions.ts, sessionUtils.ts...

scripts/                 # Monitoring tools
├── monitor_focused.py   # Track Skills/Agents/Hooks/Sessions
├── monitor_enhanced.py  # Full PR analysis with diffs
└── compare_releases.py  # Compare specific versions

reports/                 # Generated tracking reports
```

## Usage

```bash
# Set GitHub token (public_repo scope)
export GITHUB_TOKEN="ghp_..."

# Track features (last 30 days, comparing to v0.14.0)
FORK_VERSION=v0.14.0 DAYS_BACK=30 python3 scripts/monitor_focused.py

# Compare specific versions
python3 scripts/compare_releases.py v0.14.0 v0.24.0
```

## Key Files

### Skills (`code/skills/`)
- `skillManager.ts` - Discovery (builtin → extension → user → workspace precedence), activation, conflict detection
- `skillLoader.ts` - YAML frontmatter parsing, skill definition loading

### Agents (`code/agents/`)
- `registry.ts` - Agent registration, built-in agents (CodebaseInvestigator, CliHelp, Generalist), model config routing
- `local-executor.ts` - Turn loop execution with timeout/max_turns
- `a2a-client-manager.ts` - Remote agent (A2A protocol) support

### Hooks (`code/hooks/`)
- `hookSystem.ts` - Main orchestrator, fires session/agent/tool events
- `hookRegistry.ts` - Load hooks from config, enable/disable
- `hookRunner.ts` - Execute command-based hooks with JSON stdin/stdout
- `hookPlanner.ts` - Schedule hooks based on context matchers

### Sessions (`code/sessions/`)
- `useSessionBrowser.ts` - React hook for session browser UI, resume/delete
- `sessions.ts` - Session listing, metadata extraction
- `sessionSummaryService.ts` - Conversation summarization

## GitHub Actions

Daily monitoring at 6 AM UTC - see `.github/workflows/monitor-upstream.yml`

## License

- `scripts/` - MIT
- `code/` - Apache 2.0 (Google LLC) - extracted from [gemini-cli](https://github.com/google-gemini/gemini-cli)
