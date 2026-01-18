# Major Upgrades: v0.14.0 → v0.24.0

**Fork Point:** v0.14.0 (Nov 12, 2025)
**Current Stable:** v0.24.0 (Jan 14, 2026)
**Delta:** 585 commits, 300 files changed, ~2 months of development

---

## TL;DR - Big Upgrades Worth Porting

| Priority | Feature | Effort | Impact |
|----------|---------|--------|--------|
| **P0** | Agent Skills System | High | New extensibility model |
| **P0** | Policy Engine Refactor | High | Security/confirmation overhaul |
| **P1** | Hook System v2 | Medium | STOP_EXECUTION, agent hooks |
| **P1** | MessageBus Architecture | High | Internal refactor (breaking) |
| **P2** | Remote Agents (A2A) | Medium | Multi-agent support |
| **P2** | Settings Rename | Low | disable* → enable* |
| **P3** | Tool Executor Extract | Medium | Cleaner architecture |

---

## P0: Agent Skills System (NEW)

**What:** Complete new system for "skills" - autonomous agent capabilities that can be activated/deactivated.

**Key PRs:**
- #15698 - Core Skill Infrastructure & Tiered Discovery
- #15725 - Autonomous Activation Tool & Context Injection
- #15728 - Agent Integration and System Prompt Awareness
- #15833 - Unify Representation & Centralize Loading
- #15834 - Extension Support & Security Disclosure
- #15837 - `gemini skills` CLI management command
- #15865 - `/skills reload` command
- #16045 - Built-in Agent Skills support
- #16300 - Shipping built-in skills with CLI
- #16377 - Install/uninstall commands for skills

**Key Files:**
```
packages/core/src/skills/           # NEW directory
packages/cli/src/commands/skills/   # NEW directory
packages/core/src/agents/skill-*.ts
```

**Breaking:** Yes - new config schema, new commands

---

## P0: Policy Engine Refactor

**What:** Complete overhaul of security/confirmation logic. Old per-tool settings replaced with centralized policy engine.

**Key PRs:**
- #15307 - Dynamic mode-aware policy evaluation
- #15601 - Granular shell command allowlisting
- #15626 - Deprecate legacy confirmation settings, enforce Policy Engine
- #15770 - Unify shell security policy, remove legacy logic
- #15977 - Allow 'modes' in user and admin policies

**Key Files:**
```
packages/core/src/policy/           # Heavily modified
packages/core/src/services/shellExecutionService.ts
```

**Breaking:** Yes - old confirmation settings deprecated

---

## P1: Hook System v2

**What:** Major enhancements to hooks - new event types, STOP_EXECUTION support, agent hooks.

**Key PRs:**
- #15325 - Folder Trust Support for Hooks
- #15470 - Project-level hook warnings
- #15552 - Hooks enable-all/disable-all feature
- #15685 - STOP_EXECUTION and enhanced hook decision handling
- #15701 - Deduplicate agent hooks
- #15746 - Context injection via SessionStart hook
- #15824 - Granular stop and block behavior for agent hooks
- #15933 - `hooks.enabled` setting
- #16361 - Other hook wrapper methods

**Key Files:**
```
packages/core/src/hooks/hookRegistry.ts
packages/core/src/hooks/types.ts
packages/cli/src/ui/commands/hooksCommand.ts
```

**Breaking:** Partially - new hook events, some behavior changes

---

## P1: MessageBus Architecture

**What:** Major internal refactor - MessageBus now mandatory for all tool/agent invocations. Cleaner event-driven architecture.

**Key PRs:**
- #15774 - Phase 1: Restore MessageBus optionality (soft migration)
- #15775 - Phase 2: Standardize Tool and Agent Invocation constructors
- #15776 - Phase 3: Enforce mandatory MessageBus injection

**Key Files:**
```
packages/core/src/message-bus/
packages/core/src/tools/tools.ts
packages/core/src/agents/*.ts
```

**Breaking:** Yes - constructor signatures changed

---

## P2: Remote Agents (A2A)

**What:** Support for remote agents via A2A protocol.

**Key PRs:**
- #15437 - Remote agents and multi-agent TOML files
- #15485 - A2A Client Manager
- #15711 - Remote agents in agent registry
- #16013 - Full remote agent support

**Key Files:**
```
packages/core/src/agents/a2a-client-manager.ts
packages/core/src/agents/registry.ts
packages/a2a-server/
```

---

## P2: Settings Rename (Breaking)

**What:** All `disable*` settings renamed to `enable*` (inverted logic).

**Key PRs:**
- #14142 - Rename negative settings to positive naming

**Migration:**
```
disableTelemetry → enableTelemetry (inverted)
disableUpdateCheck → enableUpdateCheck (inverted)
// etc.
```

---

## P3: Tool Executor Extraction

**What:** ToolExecutor extracted from CoreToolScheduler for cleaner separation.

**Key PRs:**
- #15589 - Extract static concerns from CoreToolScheduler
- #15857 - Consolidate EditTool and SmartEditTool
- #15900 - Extract and integrate ToolExecutor
- #15923 - Rename smart-edit to edit

**Key Files:**
```
packages/core/src/tools/tool-executor.ts  # NEW
packages/core/src/scheduler/
```

---

## Other Notable Changes

### UI/UX
- #14332 - Tab to switch focus between shell and input
- #15524 - modifyOtherKeys protocol for tmux
- #15336 - OSC 52 paste support
- #15936 - Settings descriptions in /settings
- #16378 - Dynamic terminal tab titles

### Stability
- #15410 - Fix EIO error crash in readStdin
- #15684 - Exponential back-off retries
- #15748 - Fix terminal hang on browser exit
- #16420 - Fix crash on unicode character
- #16424 - OOM fix with useMemo on history

### Config
- #13199 - Automatic `/model` persistence
- #15354 - Default settings apply correctly
- #16252 - Remove legacy V1 settings migration

---

## Recommended Porting Order

1. **Settings Rename** (P2) - Do this first, it's mechanical but affects everything
2. **Policy Engine** (P0) - Foundation for security model
3. **Hook System v2** (P1) - Builds on policy engine
4. **MessageBus** (P1) - Required for agents
5. **Agent Skills** (P0) - Major new feature, depends on MessageBus
6. **Remote Agents** (P2) - Optional, if you need multi-agent

---

## Files Changed by Category

### Core (packages/core/)
- 131 files in packages/ directory
- Major: agents/, hooks/, policy/, tools/, services/

### CLI (packages/cli/)
- UI components heavily modified
- New commands: skills, agents refresh

### Config Schema
- settings.json schema expanded significantly
- New sections: skills, agents, policy modes
