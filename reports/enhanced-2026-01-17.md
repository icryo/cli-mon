# Gemini CLI Upstream Monitor - Enhanced Report

**Generated:** 2026-01-18 01:08 UTC  
**Repository:** [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)  
**Period:** 2026-01-11 to 2026-01-18  

## Quick Summary

| Priority | Count | Action |
|----------|-------|--------|
| Breaking Changes | 23 | **REVIEW IMMEDIATELY** |
| Core Code Changes | 6 | Review for porting |
| Dependency Updates | 0 | Check compatibility |
| Other Changes | 1 | Low priority |
| New Releases | 8 | Check release notes |

---

## BREAKING CHANGES

#### [#16932](https://github.com/google-gemini/gemini-cli/pull/16932) Delete rewind documentation for now **[BREAKING]**

**Author:** @Adib234 | **Changes:** +0/-51 | **Categories:** other

#### [#16815](https://github.com/google-gemini/gemini-cli/pull/16815) fix(core): resolve PKCE length issue and stabilize OAuth redirect port **[BREAKING]**

**Author:** @sehoon38 | **Changes:** +195/-7 | **Categories:** mcp

#### [#16479](https://github.com/google-gemini/gemini-cli/pull/16479) feat(cli): replace relative keyboard shortcuts link with web URL **[BREAKING]**

**Author:** @imaliabbas | **Changes:** +5/-1 | **Categories:** ui

**Priority files changed:**

- `~` `packages/cli/src/ui/components/Help.tsx` - +2 -1 lines
- `~` `packages/cli/src/ui/constants.ts` - +3 -0 lines

#### [#16267](https://github.com/google-gemini/gemini-cli/pull/16267) fix: Show experiment values in settings UI for compressionThreshold **[BREAKING]**

**Author:** @ishaanxgupta | **Changes:** +34/-5 | **Categories:** config, other, ui

**Priority files changed:**

- `~` `packages/cli/src/ui/components/SettingsDialog.tsx` - +9 -3 lines

#### [#16345](https://github.com/google-gemini/gemini-cli/pull/16345) fix: Handle colons in skill description frontmatter **[BREAKING]**

**Author:** @maru0804 | **Changes:** +166/-9 | **Categories:** other

#### [#16800](https://github.com/google-gemini/gemini-cli/pull/16800) chore: remove a2a-adapter and bump @a2a-js/sdk to 0.3.8 **[BREAKING]** **[DEPS]**

**Author:** @adamfweidman | **Changes:** +7/-229 | **Categories:** dependencies, agents, other

**Priority files changed:**

- `~` `packages/core/src/agents/a2a-client-manager.ts`

#### [#16902](https://github.com/google-gemini/gemini-cli/pull/16902) Don't commit unless user asks us to. **[BREAKING]**

**Author:** @gundermanc | **Changes:** +76/-0 | **Categories:** other

#### [#16804](https://github.com/google-gemini/gemini-cli/pull/16804) fix(hooks): enable /hooks disable to reliably stop single hooks **[BREAKING]**

**Author:** @abhipatel12 | **Changes:** +96/-58 | **Categories:** config, hooks

**Priority files changed:**

- `~` `packages/cli/src/ui/commands/hooksCommand.ts`

#### [#16824](https://github.com/google-gemini/gemini-cli/pull/16824) refactor(core): foundational truncation refactoring and token estimation optimization **[BREAKING]**

**Author:** @NTaylorMullen | **Changes:** +170/-252 | **Categories:** other

#### [#16736](https://github.com/google-gemini/gemini-cli/pull/16736) feat(agent): enable agent skills by default **[BREAKING]**

**Author:** @NTaylorMullen | **Changes:** +216/-9 | **Categories:** config, other, ui

#### [#16828](https://github.com/google-gemini/gemini-cli/pull/16828) refactor(cli): unify shell confirmation dialogs **[BREAKING]**

**Author:** @NTaylorMullen | **Changes:** +102/-446 | **Categories:** tools, hooks, ui

**Priority files changed:**

- `~` `packages/cli/src/ui/AppContainer.tsx`
- `~` `packages/cli/src/ui/components/DialogManager.tsx` - +0 -6 lines
- `-` `packages/cli/src/ui/components/ShellConfirmationDialog.tsx`
- `~` `packages/cli/src/ui/components/messages/ToolConfirmationMessage.tsx` - +17 -3 lines
- `~` `packages/cli/src/ui/contexts/UIStateContext.tsx` - +0 -2 lines
- `~` `packages/cli/src/ui/hooks/slashCommandProcessor.ts`
- `~` `packages/cli/src/ui/types.ts` - +0 -9 lines
- `~` `packages/core/src/tools/tools.ts` - +1 -0 lines

#### [#14142](https://github.com/google-gemini/gemini-cli/pull/14142) feat(settings): rename negative settings to positive naming (disable* -> enable*) **[BREAKING]**

**Author:** @afarber | **Changes:** +785/-243 | **Categories:** config, other, hooks, ui

**Priority files changed:**

- `~` `packages/cli/src/ui/components/Composer.tsx` - +2 -2 lines
- `~` `packages/cli/src/ui/hooks/useAtCompletion.ts` - +2 -2 lines
- `~` `packages/cli/src/ui/utils/updateCheck.ts` - +1 -1 lines

#### [#16882](https://github.com/google-gemini/gemini-cli/pull/16882) Patch #16730 into v0.25.0 preview **[BREAKING]**

**Author:** @chrstnb | **Changes:** +5/-1 | **Categories:** other

#### [#16759](https://github.com/google-gemini/gemini-cli/pull/16759) Fix race condition by awaiting scheduleToolCalls **[BREAKING]**

**Author:** @chrstnb | **Changes:** +86/-52 | **Categories:** hooks

**Priority files changed:**

- `~` `packages/cli/src/ui/hooks/useGeminiStream.ts` - +2 -2 lines
- `~` `packages/cli/src/ui/hooks/useReactToolScheduler.ts` - +2 -2 lines

#### [#16730](https://github.com/google-gemini/gemini-cli/pull/16730) fix(core): resolve circular dependency via tsconfig paths **[BREAKING]**

**Author:** @sehoon38 | **Changes:** +5/-1 | **Categories:** other

#### [#16873](https://github.com/google-gemini/gemini-cli/pull/16873) fix(core): surface warnings for invalid hook event names in configuration (#16788) **[BREAKING]**

**Author:** @sehoon38 | **Changes:** +65/-3 | **Categories:** hooks

**Priority files changed:**

- `~` `packages/core/src/hooks/hookRegistry.ts` - +9 -2 lines
- `~` `packages/core/src/hooks/types.ts` - +5 -0 lines

#### [#16859](https://github.com/google-gemini/gemini-cli/pull/16859) docs(extensions): add Agent Skills support and mark feature as experimental **[BREAKING]**

**Author:** @NTaylorMullen | **Changes:** +101/-6 | **Categories:** tools, other

#### [#16769](https://github.com/google-gemini/gemini-cli/pull/16769) fix(core): truncate large telemetry log entries **[BREAKING]**

**Author:** @sehoon38 | **Changes:** +247/-1 | **Categories:** other

#### [#16864](https://github.com/google-gemini/gemini-cli/pull/16864) remove need-triage label from bug_report template **[BREAKING]**

**Author:** @sehoon38 | **Changes:** +0/-2 | **Categories:** other

#### [#16849](https://github.com/google-gemini/gemini-cli/pull/16849) feat(plan): enforce strict read-only policy and halt execution on violation **[BREAKING]**

**Author:** @jerop | **Changes:** +179/-8 | **Categories:** config, other

#### [#16773](https://github.com/google-gemini/gemini-cli/pull/16773) fix(core): fix PTY descriptor shell leak **[BREAKING]**

**Author:** @galz10 | **Changes:** +171/-5 | **Categories:** services, other

**Priority files changed:**

- `~` `packages/core/src/services/shellExecutionService.ts`

#### [#16782](https://github.com/google-gemini/gemini-cli/pull/16782) perf(ui): optimize text buffer and highlighting for large inputs **[BREAKING]**

**Author:** @NTaylorMullen | **Changes:** +469/-76 | **Categories:** other, ui

**Priority files changed:**

- `~` `packages/cli/src/ui/components/shared/text-buffer.ts`
- `~` `packages/cli/src/ui/constants.ts` - +1 -0 lines
- `~` `packages/cli/src/ui/utils/highlight.ts` - +24 -1 lines
- `~` `packages/cli/src/ui/utils/textUtils.ts`

#### [#16798](https://github.com/google-gemini/gemini-cli/pull/16798) cleanup: Organize key bindings **[BREAKING]**

**Author:** @scidomino | **Changes:** +162/-181 | **Categories:** config, other

---

## Core Code Changes (Priority Files)

These PRs modified files in: `hooks/`, `agents/`, `mcp/`, `services/`, `tools/`

### Hooks

#### [#16866](https://github.com/google-gemini/gemini-cli/pull/16866) fix(patch): cherry-pick cfdc4cf to release/v0.25.0-preview.0-pr-16759 to patch version v0.25.0-preview.0 and create version 0.25.0-preview.1

**Author:** @gemini-cli-robot | **Changes:** +86/-52 | **Categories:** hooks

**Priority files changed:**

- `~` `packages/cli/src/ui/hooks/useGeminiStream.ts` - +2 -2 lines
- `~` `packages/cli/src/ui/hooks/useReactToolScheduler.ts` - +2 -2 lines

#### [#16865](https://github.com/google-gemini/gemini-cli/pull/16865) fix(patch): cherry-pick cfdc4cf to release/v0.24.0-pr-16759 to patch version v0.24.0 and create version 0.24.1

**Author:** @gemini-cli-robot | **Changes:** +86/-52 | **Categories:** hooks

**Priority files changed:**

- `~` `packages/cli/src/ui/hooks/useGeminiStream.ts` - +2 -2 lines
- `~` `packages/cli/src/ui/hooks/useReactToolScheduler.ts` - +2 -2 lines

### Mcp

#### [#16647](https://github.com/google-gemini/gemini-cli/pull/16647) Make merged settings non-nullable and fix all lints related to that.

**Author:** @jacob314 | **Changes:** +964/-744 | **Categories:** mcp, other, agents, config, ui, hooks

**Priority files changed:**

- `~` `packages/cli/src/ui/AppContainer.tsx`
- `~` `packages/cli/src/ui/auth/AuthDialog.tsx` - +5 -5 lines
- `~` `packages/cli/src/ui/auth/useAuth.ts` - +3 -3 lines
- `~` `packages/cli/src/ui/commands/aboutCommand.ts` - +1 -1 lines
- `~` `packages/cli/src/ui/commands/agentsCommand.ts` - +3 -13 lines
- `~` `packages/cli/src/ui/commands/hooksCommand.ts` - +2 -4 lines
- `~` `packages/cli/src/ui/components/AppHeader.tsx` - +2 -2 lines
- `~` `packages/cli/src/ui/components/Composer.tsx` - +2 -4 lines
- `~` `packages/cli/src/ui/components/EditorSettingsDialog.tsx` - +3 -3 lines
- `~` `packages/cli/src/ui/components/Footer.tsx` - +5 -6 lines
- *... and 13 more files*

### Other

#### [#16872](https://github.com/google-gemini/gemini-cli/pull/16872) Remove LRUCache class migrating to mnemoist

**Author:** @jacob314 | **Changes:** +13/-115 | **Categories:** other, ui

**Priority files changed:**

- `~` `packages/cli/src/ui/components/shared/text-buffer.ts` - +3 -3 lines
- `~` `packages/cli/src/ui/utils/highlight.ts` - +2 -2 lines
- `~` `packages/cli/src/ui/utils/textUtils.ts` - +3 -3 lines

#### [#16638](https://github.com/google-gemini/gemini-cli/pull/16638) feat(core): Add `generalist` agent.

**Author:** @joshualitt | **Changes:** +283/-32 | **Categories:** other, config, agents

**Priority files changed:**

- `+` `packages/core/src/agents/generalist-agent.ts` - +71 -0 lines
- `~` `packages/core/src/agents/registry.ts`
- `~` `packages/core/src/agents/types.ts` - +1 -0 lines

---

## Releases

### [v0.26.0-nightly.20260115.6cb3ae4e0](https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0-nightly.20260115.6cb3ae4e0) *(prerelease)*

Released: 2026-01-15

## What's Changed
* docs: Fix formatting issue in memport documentation by @wanglc02 in https://github.com/google-gemini/gemini-cli/pull/14774
* fix(policy): enhance shell command safety and parsing by @allenhutchison in https://github.com/google-gemini/gemini-cli/pull/15034
* fix(core): avoid 'activate_skill' re-registration warning by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/16398
* perf(workflows): optimize PR triage script for faster execution by @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/16355
* feat(admin): prompt user to restart the CLI if they change auth to oauth mid-session or don't have auth type selected at start of session by @skeshive in https://github.com/google-gemini/gemini-cli/pull/16426
* Update cli-help agent's system prompt in sub-agents section by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/16441
* Revert "Update extension examples" by @chrstnb in https://github.com/google-gemini/gemini-cli/pull/16442
* Fix: add back fastreturn support by @scidomino in https://github.com/google-gemini/gemini-cli/pull/16440
* feat(a2a): Introduce /memory command for a2a server by @cocosheng-g in https://github.com/google-gemini/gemini-cli/pull/14456
* docs: fix broken internal link by using relative path by @Gong-Mi in https://github.com/google-gemini/gemini-cli/pull/15371
* migrate yolo/auto-edit keybindings by @scidomino in https://github.com/google-gemini/gemini-cli/pull/16457
* feat(cli): add install and u

*[truncated - see full notes]*

### [v0.24.0-nightly.20260115.c9d6f9b22](https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0-nightly.20260115.c9d6f9b22) *(prerelease)*

Released: 2026-01-15

**Full Changelog**: https://github.com/google-gemini/gemini-cli/compare/v0.25.0-nightly.20260112.15891721a...v0.24.0-nightly.20260115.c9d6f9b22

### [v0.25.0-preview.0](https://github.com/google-gemini/gemini-cli/releases/tag/v0.25.0-preview.0) *(prerelease)*

Released: 2026-01-14

## What's Changed
* feat(core): improve activate_skill tool and use lowercase XML tags by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/16009
* Add initiation method telemetry property by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/15818
* chore(release): bump version to 0.25.0-nightly.20260107.59a18e710 by @gemini-cli-robot in https://github.com/google-gemini/gemini-cli/pull/16048
* Hx support by @kevinfjiang in https://github.com/google-gemini/gemini-cli/pull/16032
* [Skills] Foundation: Centralize management logic and feedback rendering by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/15952
* Introduce GEMINI_CLI_HOME for strict test isolation by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/15907
* [Skills] Multi-scope skill enablement and shadowing fix by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/15953
* policy: extract legacy policy from core tool scheduler to policy engine by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/15902
* Enhance TestRig with process management and timeouts by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/15908
* Update troubleshooting doc for UNABLE_TO_GET_ISSUER_CERT_LOCALLY by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/16069
* Add keytar to dependencies by @chrstnb in https://github.com/google-gemini/gemini-cli/pull/15928
* Simplify extension settings command by @chrstnb in http

*[truncated - see full notes]*

### [v0.24.0](https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0)

Released: 2026-01-14

## What's Changed
* chore(core): refactor model resolution and cleanup fallback logic by @adamfweidman in https://github.com/google-gemini/gemini-cli/pull/15228
* Add Folder Trust Support To Hooks by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/15325
* Record timestamp with code assist metrics. by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/15439
* feat(policy): implement dynamic mode-aware policy evaluation by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/15307
* fix(core): use debugLogger.debug for startup profiler logs by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/15443
* feat(ui): Add security warning and improve layout for Hooks list by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/15440
* fix #15369, prevent crash on unhandled EIO error in readStdin cleanup by @ElecTwix in https://github.com/google-gemini/gemini-cli/pull/15410
* chore: improve error messages for --resume by @jackwotherspoon in https://github.com/google-gemini/gemini-cli/pull/15360
* chore: remove clipboard file by @jackwotherspoon in https://github.com/google-gemini/gemini-cli/pull/15447
* Implemented unified secrets sanitization and env. redaction options by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/15348
* feat: automatic `/model` persistence across Gemini CLI sessions by @niyasrad in https://github.com/google-gemini/gemini-cli/pull/13199
* refactor(core): remove deprecated permissi

*[truncated - see full notes]*

### [v0.24.0-preview.3](https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0-preview.3) *(prerelease)*

Released: 2026-01-14

## What's Changed
* fix(patch): cherry-pick eda47f5 to release/v0.24.0-preview.2-pr-16557 [CONFLICTS] by @gemini-cli-robot in https://github.com/google-gemini/gemini-cli/pull/16577


**Full Changelog**: https://github.com/google-gemini/gemini-cli/compare/v0.24.0-preview.2...v0.24.0-preview.3

### [v0.24.0-preview.2](https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0-preview.2) *(prerelease)*

Released: 2026-01-13

## What's Changed
* fix(patch): cherry-pick 356f76e to release/v0.24.0-preview.1-pr-16252 to patch version v0.24.0-preview.1 and create version 0.24.0-preview.2 by @gemini-cli-robot in https://github.com/google-gemini/gemini-cli/pull/16552


**Full Changelog**: https://github.com/google-gemini/gemini-cli/compare/v0.24.0-preview.1...v0.24.0-preview.2

### [v0.24.0-preview.1](https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0-preview.1) *(prerelease)*

Released: 2026-01-13

## What's Changed
* fix(patch): cherry-pick b54e688 to release/v0.24.0-preview.0-pr-16284 to patch version v0.24.0-preview.0 and create version 0.24.0-preview.1 by @gemini-cli-robot in https://github.com/google-gemini/gemini-cli/pull/16466


**Full Changelog**: https://github.com/google-gemini/gemini-cli/compare/v0.24.0-preview.0...v0.24.0-preview.1

### [v0.25.0-nightly.20260112.15891721a](https://github.com/google-gemini/gemini-cli/releases/tag/v0.25.0-nightly.20260112.15891721a) *(prerelease)*

Released: 2026-01-12

## What's Changed
* Agent Skills: Unify Representation & Centralize Loading by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/15833
* Unify shell security policy and remove legacy logic by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/15770
* feat(core): restore MessageBus optionality for soft migration (Phase 1) by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/15774
* feat(core): Standardize Tool and Agent Invocation constructors (Phase 2) by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/15775
* feat(core,cli): enforce mandatory MessageBus injection (Phase 3 Hard Migration) by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/15776
* Agent Skills: Extension Support & Security Disclosure by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/15834
* feat(hooks): implement granular stop and block behavior for agent hooks by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/15824
* Agent Skills: Add gemini skills CLI management command by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/15837
* refactor: consolidate EditTool and SmartEditTool by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/15857
* fix(cli): mock fs.readdir in consent tests for Windows compatibility by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/15904
* refactor(core): Extract and integrate ToolExecutor by @abhipatel12 in https://gi

*[truncated - see full notes]*

---

## Other Changes (Low Priority)

<details><summary>1 PRs with non-priority file changes</summary>

- [#16876](https://github.com/google-gemini/gemini-cli/pull/16876) feat(plan): remove `read_many_files` from approval mode policies (other)

</details>

---

## Porting Checklist

- [ ] [#16932](https://github.com/google-gemini/gemini-cli/pull/16932) Delete rewind documentation for now (other) **[BREAKING]**
- [ ] [#16815](https://github.com/google-gemini/gemini-cli/pull/16815) fix(core): resolve PKCE length issue and stabilize OAuth red (mcp) **[BREAKING]**
- [ ] [#16479](https://github.com/google-gemini/gemini-cli/pull/16479) feat(cli): replace relative keyboard shortcuts link with web (ui) **[BREAKING]**
- [ ] [#16267](https://github.com/google-gemini/gemini-cli/pull/16267) fix: Show experiment values in settings UI for compressionTh (config, other) **[BREAKING]**
- [ ] [#16345](https://github.com/google-gemini/gemini-cli/pull/16345) fix: Handle colons in skill description frontmatter (other) **[BREAKING]**
- [ ] [#16800](https://github.com/google-gemini/gemini-cli/pull/16800) chore: remove a2a-adapter and bump @a2a-js/sdk to 0.3.8 (dependencies, agents) **[BREAKING]**
- [ ] [#16902](https://github.com/google-gemini/gemini-cli/pull/16902) Don't commit unless user asks us to. (other) **[BREAKING]**
- [ ] [#16804](https://github.com/google-gemini/gemini-cli/pull/16804) fix(hooks): enable /hooks disable to reliably stop single ho (config, hooks) **[BREAKING]**
- [ ] [#16824](https://github.com/google-gemini/gemini-cli/pull/16824) refactor(core): foundational truncation refactoring and toke (other) **[BREAKING]**
- [ ] [#16736](https://github.com/google-gemini/gemini-cli/pull/16736) feat(agent): enable agent skills by default (config, other) **[BREAKING]**
- [ ] [#16828](https://github.com/google-gemini/gemini-cli/pull/16828) refactor(cli): unify shell confirmation dialogs (tools, hooks) **[BREAKING]**
- [ ] [#14142](https://github.com/google-gemini/gemini-cli/pull/14142) feat(settings): rename negative settings to positive naming  (config, other) **[BREAKING]**
- [ ] [#16882](https://github.com/google-gemini/gemini-cli/pull/16882) Patch #16730 into v0.25.0 preview (other) **[BREAKING]**
- [ ] [#16759](https://github.com/google-gemini/gemini-cli/pull/16759) Fix race condition by awaiting scheduleToolCalls (hooks) **[BREAKING]**
- [ ] [#16730](https://github.com/google-gemini/gemini-cli/pull/16730) fix(core): resolve circular dependency via tsconfig paths (other) **[BREAKING]**
