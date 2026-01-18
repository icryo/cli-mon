# Gemini CLI Intel Report

**Generated:** 2026-01-17
**Your Fork Base:** v0.14.0
**Current Stable:** v0.24.0
**Latest Preview:** v0.26.0-nightly

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Commits since your fork | 585 |
| Features in preview (not stable) | 190 commits ahead |
| Open P1 PRs | 21 |
| Open P0 Issues | 11 |
| Active development areas | Skills, Hooks, Agents |

---

## What's Coming Next (Preview → Stable)

These features are in **v0.26.0-nightly** but not yet in stable v0.24.0:

### High Priority Features in Preview

| Feature | PR | Impact |
|---------|-----|--------|
| **Skills install/uninstall commands** | #16377 | New CLI commands for skill management |
| **Subagent model routing** | #16035 | Route different models to subagents |
| **Extensions disabled admin control** | #16024 | Enterprise admin can disable extensions |
| **Filepath autosuggestion** | #14738 | Better UX for file paths after commands |
| **MCP context in hooks** | - | Hooks get MCP server context |
| **Hook system simplification** | - | HookSystem wrapper methods |

### Key Files Changing

```
+112 packages/cli/src/commands/skills/install.ts (NEW)
+72  packages/cli/src/commands/skills/uninstall.ts (NEW)
+53  packages/cli/src/services/BuiltinCommandLoader.ts
```

---

## Roadmap Analysis

### Milestones

| Milestone | Progress | Due | Notes |
|-----------|----------|-----|-------|
| Q3 '2025 | 76% (52/68) | 2025-09-30 | **16 items still open** |
| Public OSS | 99% (83/84) | 2025-06-25 | Nearly complete |
| GCA Preview | 100% | Done | ✓ |

**Interpretation:** Q3 milestone still has 16 open items - these are likely deferred features or lower priority. Main OSS work is essentially complete.

---

## Priority PRs in Flight

### P1 - High Priority (21 Open)

| PR | Title | Area | Status |
|----|-------|------|--------|
| #7077 | Audio Notifications System | UX | Active |
| #11357 | Block shell redirections outside workspace | Security | Stale |
| #11013 | Remove retries on quota errors | Core | Stale |

**Analysis:** Many P1 PRs are stale (no activity). The team may have deprioritized them or they're blocked.

### P2 - Medium Priority (34 Open)

Focus areas:
- Core improvements (21 PRs)
- Agent enhancements (6 PRs)
- Security hardening (2 PRs)

---

## Development Velocity

### Last 50 commits to main:

| Area | Commits | Trend |
|------|---------|-------|
| Fixes | 21 | High - stabilization phase |
| Features | 13 | Moderate |
| UI | 4 | Low |
| Agents | 4 | Active |
| Hooks | 2 | Maintenance |
| Skills | 2 | New feature bedding in |
| Policy | 2 | Maintenance |
| MCP | 2 | Maintenance |

**Interpretation:** Heavy focus on bug fixes suggests they're in a stabilization phase after the big v0.24.0 release. Agent/Skills work continues.

---

## P0 Issues (Critical Bugs)

| Issue | Title | Notes |
|-------|-------|-------|
| #12657 | VS Code extension v2.57 breaking changes | Cross-product issue |
| #16726, #16724, #16722, #16720 | Nightly release failures | CI/CD issues |

**Analysis:** Most P0s are CI/CD related, not core functionality. VS Code extension issue is external.

---

## Areas to Watch

### 1. Skills System (High Activity)
- `install.ts` and `uninstall.ts` being added
- Built-in skills shipping with CLI
- This is their big bet for extensibility

### 2. Subagent Model Routing
- PR #16035 - preliminary changes
- Will allow different models for different agents
- Could be important for cost optimization

### 3. Hook System Maturation
- Simplification via wrapper methods
- MCP context now available in hooks
- More granular control

### 4. Admin/Enterprise Features
- Extensions can be disabled by admin
- Remote admin settings
- Secure mode enforcement

---

## What This Report is Missing

### Critical Gaps

1. **No automated diff analysis against YOUR fork**
   - We see upstream changes but don't know which you've already ported
   - Need: Mapping of your file paths to upstream paths

2. **No semantic code analysis**
   - We see files changed but not function signatures
   - Breaking API changes could be missed

3. **No dependency vulnerability tracking**
   - package.json changes could introduce vulnerabilities
   - Should track npm audit results

4. **No test coverage comparison**
   - Are they adding tests for features you care about?

5. **No Discord/Slack monitoring**
   - Developer discussions happen outside GitHub
   - Roadmap hints, deprecation warnings

6. **No release notes parsing**
   - Release notes often have upgrade guides
   - Should extract migration instructions

7. **No contributor network analysis**
   - Who are the key maintainers?
   - Whose PRs get merged fastest?

8. **No issue-to-PR linking**
   - What user pain points drive features?

---

## Recommended Actions

### Immediate (This Week)

1. **Port Settings Rename** (`disable*` → `enable*`)
   - Low effort, high compatibility impact
   - Do this before any other porting

2. **Review Policy Engine PRs**
   - Foundation for security model
   - #15307, #15601, #15626, #15770

### Short Term (This Month)

3. **Evaluate Agent Skills**
   - Major new capability
   - Decide: Port it or build your own?

4. **Track v0.25.0 stable release**
   - Currently in preview
   - Will include skills install/uninstall

### Ongoing

5. **Monitor P1 PRs weekly**
   - Especially security-related ones
   - #11357 (shell redirections) affects your fork

---

## Intelligence Quality Assessment

| Aspect | Current | Target | Gap |
|--------|---------|--------|-----|
| Release tracking | ✓ Stable + Preview | ✓ | None |
| PR prioritization | ✓ By label | By impact on fork | Need fork mapping |
| Breaking changes | ✓ Keyword detection | Semantic analysis | Medium |
| Roadmap visibility | ✓ Milestones | Issue clustering | Low |
| Pre-release features | ✓ Compare to stable | ✓ | None |
| Your fork sync state | ✗ Missing | Full diff | **Critical gap** |

---

## Files to Review

### Most Changed Since v0.14.0 (Core Areas)

```
packages/core/src/policy/          # Complete overhaul
packages/core/src/hooks/           # v2 system
packages/core/src/skills/          # NEW
packages/core/src/agents/          # A2A, registry
packages/core/src/message-bus/     # Mandatory injection
packages/cli/src/commands/skills/  # NEW
```

### Your Likely Pain Points

Based on fork age (v0.14.0), these files have diverged significantly:
- `packages/core/src/tools/tools.ts` - MessageBus changes
- `packages/core/src/scheduler/` - ToolExecutor extraction
- `packages/cli/src/ui/` - Heavy UI refactoring
