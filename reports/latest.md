# Gemini CLI Upstream Monitor Report

**Generated:** 2026-01-18 00:54 UTC  
**Monitoring:** [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)  
**Period:** 2026-01-11 to 2026-01-18 (7 days)  

---

## Summary

| Metric | Count |
|--------|-------|
| New Releases | 8 |
| Merged PRs | 100 |
| Commits | 0 |
| Open Milestones | 3 |
| Open PRs | 155 |

### Changes by Category

- **ui**: 86 changes
- **models**: 81 changes
- **streaming**: 44 changes
- **hooks**: 43 changes
- **mcp**: 33 changes
- **config**: 33 changes
- **shell**: 30 changes
- **input**: 30 changes
- **agents**: 22 changes
- **sessions**: 17 changes
- **other**: 5 changes

---

## New Releases

### [v0.26.0-nightly.20260115.6cb3ae4e0](https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0-nightly.20260115.6cb3ae4e0) (prerelease)

**Released:** 2026-01-15 | **Categories:** shell, input, streaming, hooks, sessions, models, mcp, agents, ui, config

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
* feat(cli): add install and uninstall commands for skills by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/16377
* feat(ui): use Tab to switch focus between shell and input by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/14332
* feat(core): support shipping built-in skills with the CLI by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/16300
* Collect hardware details telemetry. by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/16119
* feat(agents): i

*[truncated]*

### [v0.24.0-nightly.20260115.c9d6f9b22](https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0-nightly.20260115.c9d6f9b22) (prerelease)

**Released:** 2026-01-15 | **Categories:** models

**Full Changelog**: https://github.com/google-gemini/gemini-cli/compare/v0.25.0-nightly.20260112.15891721a...v0.24.0-nightly.20260115.c9d6f9b22

### [v0.24.0](https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0)

**Released:** 2026-01-14 | **Categories:** shell, input, streaming, hooks, sessions, models, mcp, agents, ui, config

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
* refactor(core): remove deprecated permission aliases from BeforeToolHookOutput by @StoyanD in https://github.com/google-gemini/gemini-cli/pull/14855
* fix: add missing `type` field to MCPServerConfig by @jackwotherspoon in https://github.com/google-gemini/gemini-cli/pull/15465
* Make schema validation errors non-fatal by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/15487
* chore: limit MCP resources display to 10 by default by @jackwotherspoon in https://github.com/google-gemini/gemini-cli/pull/15489
* Add experimental 

*[truncated]*

### [v0.25.0-preview.0](https://github.com/google-gemini/gemini-cli/releases/tag/v0.25.0-preview.0) (prerelease)

**Released:** 2026-01-14 | **Categories:** shell, input, streaming, hooks, sessions, models, mcp, agents, ui, config

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
* Simplify extension settings command by @chrstnb in https://github.com/google-gemini/gemini-cli/pull/16001
* feat(admin): implement extensions disabled by @skeshive in https://github.com/google-gemini/gemini-cli/pull/16024
* Core data structure updates for Rewind functionality by @Adib234 in https://github.com/google-gemini/gemini-cli/pull/15714
* feat(hooks): simplify hook firing with HookSystem wrapper methods by @ved015 in https://github.com/google-gemini/gemini-cli/pull/15982
* Add exp.gws_experiment field to LogEventEntry by @gsquared94 in https

*[truncated]*

### [v0.24.0-preview.3](https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0-preview.3) (prerelease)

**Released:** 2026-01-14 | **Categories:** models

## What's Changed
* fix(patch): cherry-pick eda47f5 to release/v0.24.0-preview.2-pr-16557 [CONFLICTS] by @gemini-cli-robot in https://github.com/google-gemini/gemini-cli/pull/16577


**Full Changelog**: https://github.com/google-gemini/gemini-cli/compare/v0.24.0-preview.2...v0.24.0-preview.3

### [v0.24.0-preview.2](https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0-preview.2) (prerelease)

**Released:** 2026-01-13 | **Categories:** models

## What's Changed
* fix(patch): cherry-pick 356f76e to release/v0.24.0-preview.1-pr-16252 to patch version v0.24.0-preview.1 and create version 0.24.0-preview.2 by @gemini-cli-robot in https://github.com/google-gemini/gemini-cli/pull/16552


**Full Changelog**: https://github.com/google-gemini/gemini-cli/compare/v0.24.0-preview.1...v0.24.0-preview.2

### [v0.24.0-preview.1](https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0-preview.1) (prerelease)

**Released:** 2026-01-13 | **Categories:** models

## What's Changed
* fix(patch): cherry-pick b54e688 to release/v0.24.0-preview.0-pr-16284 to patch version v0.24.0-preview.0 and create version 0.24.0-preview.1 by @gemini-cli-robot in https://github.com/google-gemini/gemini-cli/pull/16466


**Full Changelog**: https://github.com/google-gemini/gemini-cli/compare/v0.24.0-preview.0...v0.24.0-preview.1

### [v0.25.0-nightly.20260112.15891721a](https://github.com/google-gemini/gemini-cli/releases/tag/v0.25.0-nightly.20260112.15891721a) (prerelease)

**Released:** 2026-01-12 | **Categories:** shell, input, streaming, hooks, sessions, models, mcp, agents, ui, config

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
* refactor(core): Extract and integrate ToolExecutor by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/15900
* Fix terminal hang when user exits browser without logging in by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/15748
* fix: avoid SDK warning by not accessing .text getter in logging by @ved015 in https://github.com/google-gemini/gemini-cli/pull/15706
* Make default settings apply by @devr0306 in https://github.com/google-gemini/gemini-cli/pull/15354
* chore: rename smart-edit to edit by @abhipatel12 in https://github.com/google-gem

*[truncated]*

---

## Merged Pull Requests

| PR | Title | Author | Categories | Changes |
|---:|-------|--------|------------|---------|
| [#16932](https://github.com/google-gemini/gemini-cli/pull/16932) | Delete rewind documentation for now | @Adib234 | input, hooks, ui | +0/-0 |
| [#16815](https://github.com/google-gemini/gemini-cli/pull/16815) | fix(core): resolve PKCE length issue and stabilize OAuth red... | @sehoon38 | shell, models, mcp, ui, config | +0/-0 |
| [#16479](https://github.com/google-gemini/gemini-cli/pull/16479) | feat(cli): replace relative keyboard shortcuts link with web... | @imaliabbas | input, hooks, sessions, models, ui | +0/-0 |
| [#16267](https://github.com/google-gemini/gemini-cli/pull/16267) | fix: Show experiment values in settings UI for compressionTh... | @ishaanxgupta | hooks, ui, config | +0/-0 |
| [#16800](https://github.com/google-gemini/gemini-cli/pull/16800) | chore: remove a2a-adapter and bump @a2a-js/sdk to 0.3.8 | @adamfweidman | hooks, models, ui | +0/-0 |
| [#16902](https://github.com/google-gemini/gemini-cli/pull/16902) | Don't commit unless user asks us to. | @gundermanc | hooks, agents, ui | +0/-0 |
| [#16804](https://github.com/google-gemini/gemini-cli/pull/16804) | fix(hooks): enable /hooks disable to reliably stop single ho... | @abhipatel12 | streaming, hooks, sessions, models, ui, config | +0/-0 |
| [#16824](https://github.com/google-gemini/gemini-cli/pull/16824) | refactor(core): foundational truncation refactoring and toke... | @NTaylorMullen | shell, streaming, models, mcp, ui | +0/-0 |
| [#16736](https://github.com/google-gemini/gemini-cli/pull/16736) | feat(agent): enable agent skills by default | @NTaylorMullen | models, mcp, agents, ui, config | +0/-0 |
| [#16828](https://github.com/google-gemini/gemini-cli/pull/16828) | refactor(cli): unify shell confirmation dialogs | @NTaylorMullen | shell, sessions, models, mcp, agents, ui | +0/-0 |
| [#14142](https://github.com/google-gemini/gemini-cli/pull/14142) | feat(settings): rename negative settings to positive naming ... | @afarber | streaming, hooks, models, agents, ui, config | +0/-0 |
| [#16872](https://github.com/google-gemini/gemini-cli/pull/16872) | Remove LRUCache class migrating to mnemoist | @jacob314 | other | +0/-0 |
| [#16882](https://github.com/google-gemini/gemini-cli/pull/16882) | Patch #16730 into v0.25.0 preview | @chrstnb | input, hooks, ui | +0/-0 |
| [#16627](https://github.com/google-gemini/gemini-cli/pull/16627) | feat(admin): implement admin controls polling and restart pr... | @skeshive | input, streaming, sessions, models, mcp, ui, config | +0/-0 |
| [#16876](https://github.com/google-gemini/gemini-cli/pull/16876) | feat(plan): remove `read_many_files` from approval mode poli... | @jerop | streaming, models, mcp, config | +0/-0 |
| [#16873](https://github.com/google-gemini/gemini-cli/pull/16873) | fix(core): surface warnings for invalid hook event names in ... | @sehoon38 | streaming, hooks, models, ui, config | +0/-0 |
| [#16859](https://github.com/google-gemini/gemini-cli/pull/16859) | docs(extensions): add Agent Skills support and mark feature ... | @NTaylorMullen | models, mcp, agents, ui | +0/-0 |
| [#16769](https://github.com/google-gemini/gemini-cli/pull/16769) | fix(core): truncate large telemetry log entries | @sehoon38 | streaming, models, ui | +0/-0 |
| [#16864](https://github.com/google-gemini/gemini-cli/pull/16864) | remove need-triage label from bug_report template | @sehoon38 | input, hooks, ui | +0/-0 |
| [#16866](https://github.com/google-gemini/gemini-cli/pull/16866) | fix(patch): cherry-pick cfdc4cf to release/v0.25.0-preview.0... | @gemini-cli-robot | other | +0/-0 |
| [#16865](https://github.com/google-gemini/gemini-cli/pull/16865) | fix(patch): cherry-pick cfdc4cf to release/v0.24.0-pr-16759 ... | @gemini-cli-robot | other | +0/-0 |
| [#16849](https://github.com/google-gemini/gemini-cli/pull/16849) | feat(plan): enforce strict read-only policy and halt executi... | @jerop | shell, streaming, models, mcp, agents, ui, config | +0/-0 |
| [#16773](https://github.com/google-gemini/gemini-cli/pull/16773) | fix(core): fix PTY descriptor shell leak | @galz10 | shell, hooks, models, ui, config | +0/-0 |
| [#16782](https://github.com/google-gemini/gemini-cli/pull/16782) | perf(ui): optimize text buffer and highlighting for large in... | @NTaylorMullen | shell, input, streaming, hooks, models, ui | +0/-0 |
| [#16638](https://github.com/google-gemini/gemini-cli/pull/16638) | feat(core): Add `generalist` agent. | @joshualitt | models, agents | +0/-0 |
| [#16798](https://github.com/google-gemini/gemini-cli/pull/16798) | cleanup: Organize key bindings | @scidomino | input, hooks, ui | +0/-0 |
| [#16759](https://github.com/google-gemini/gemini-cli/pull/16759) | Fix race condition by awaiting scheduleToolCalls | @chrstnb | shell, input, hooks, sessions, models, mcp, ui | +0/-0 |
| [#16763](https://github.com/google-gemini/gemini-cli/pull/16763) | Steer outer agent to use expert subagents when present | @gundermanc | hooks, models, agents, ui | +0/-0 |
| [#16842](https://github.com/google-gemini/gemini-cli/pull/16842) | skip simple-mcp-server.test.ts | @scidomino | input, models, mcp | +0/-0 |
| [#16818](https://github.com/google-gemini/gemini-cli/pull/16818) | chore(workflows): rename label-workstream-rollup workflow | @bdmorgan | streaming, models, ui | +0/-0 |
| [#16811](https://github.com/google-gemini/gemini-cli/pull/16811) | fix(infra): use GraphQL to detect direct parents in rollup w... | @bdmorgan | streaming, ui | +0/-0 |
| [#16809](https://github.com/google-gemini/gemini-cli/pull/16809) | fix(infra): update maintainer rollup label to 'workstream-ro... | @bdmorgan | shell, streaming, models, ui, config | +0/-0 |
| [#16783](https://github.com/google-gemini/gemini-cli/pull/16783) | fix(patch): cherry-pick 88f1ec8 to release/v0.24.0-pr-16179 ... | @gemini-cli-robot | hooks | +0/-0 |
| [#16721](https://github.com/google-gemini/gemini-cli/pull/16721) | feat(scheduler): add functional awaitConfirmation utility | @abhipatel12 | shell, streaming, models, mcp, ui | +0/-0 |
| [#16753](https://github.com/google-gemini/gemini-cli/pull/16753) | feat(plan): add experimental 'plan' approval mode | @jerop | streaming, models, agents, ui | +0/-0 |
| [#15596](https://github.com/google-gemini/gemini-cli/pull/15596) | Add support for running available commands prior to MCP serv... | @Adib234 | input, streaming, hooks, models, mcp, ui, config | +0/-0 |
| [#16764](https://github.com/google-gemini/gemini-cli/pull/16764) | docs: clarify workspace test execution in GEMINI.md | @mattKorwel | shell, streaming, models, ui | +0/-0 |
| [#16531](https://github.com/google-gemini/gemini-cli/pull/16531) | fix(cli): safely handle /dev/tty access on macOS | @korade-krushna | shell, streaming, hooks, models, ui, config | +0/-0 |
| [#16696](https://github.com/google-gemini/gemini-cli/pull/16696) | fix(cli): prevent OOM crash by limiting file search traversa... | @galz10 | shell, streaming, models, ui, config | +0/-0 |
| [#16762](https://github.com/google-gemini/gemini-cli/pull/16762) | fix(automation): robust label enforcement with permission ch... | @bdmorgan | streaming, models, mcp, ui, config | +0/-0 |
| [#16757](https://github.com/google-gemini/gemini-cli/pull/16757) | fix(cli): add explicit dependency on color-convert | @sehoon38 | streaming, models, ui | +0/-0 |
| [#16548](https://github.com/google-gemini/gemini-cli/pull/16548) | Restricting to localhost | @cocosheng-g | streaming, mcp, config | +0/-0 |
| [#16755](https://github.com/google-gemini/gemini-cli/pull/16755) | Replace relative paths to fix website build | @chrstnb | input, streaming, hooks, ui | +0/-0 |
| [#16752](https://github.com/google-gemini/gemini-cli/pull/16752) | fix(core): prevent ModelInfo event emission on aborted signa... | @sehoon38 | shell, input, streaming, hooks, models, ui | +0/-0 |
| [#16647](https://github.com/google-gemini/gemini-cli/pull/16647) | Make merged settings non-nullable and fix all lints related ... | @jacob314 | streaming, hooks, models, agents, ui, config | +0/-0 |
| [#16751](https://github.com/google-gemini/gemini-cli/pull/16751) | feat(automation): enforce '🔒 maintainer only' and fix bot lo... | @bdmorgan | streaming, models, mcp, ui | +0/-0 |
| [#16670](https://github.com/google-gemini/gemini-cli/pull/16670) | feat(policy): add source tracking to policy rules | @allenhutchison | shell, models, mcp, agents, ui, config | +0/-0 |
| [#16476](https://github.com/google-gemini/gemini-cli/pull/16476) | Add links to supported locations and minor fixes | @g-samroberts | models, ui | +0/-0 |
| [#16746](https://github.com/google-gemini/gemini-cli/pull/16746) | fix(automation): prevent label-enforcer loop by ignoring all... | @bdmorgan | streaming, ui | +0/-0 |
| [#16727](https://github.com/google-gemini/gemini-cli/pull/16727) | fix(automation): correct status/need-issue label matching wi... | @bdmorgan | sessions, models, ui | +0/-0 |
| [#16738](https://github.com/google-gemini/gemini-cli/pull/16738) | chore/release: bump version to 0.26.0-nightly.20260115.6cb3a... | @gemini-cli-robot | other | +0/-0 |
| [#16730](https://github.com/google-gemini/gemini-cli/pull/16730) | fix(core): resolve circular dependency via tsconfig paths | @sehoon38 | streaming, models, ui, config | +0/-0 |
| [#16707](https://github.com/google-gemini/gemini-cli/pull/16707) | chore(automation): enforce 'help wanted' label permissions a... | @bdmorgan | models, ui, config | +0/-0 |
| [#16651](https://github.com/google-gemini/gemini-cli/pull/16651) | feat(scheduler): add SchedulerStateManager for reactive tool... | @abhipatel12 | shell, input, streaming, sessions, models, mcp, ui | +0/-0 |
| [#16709](https://github.com/google-gemini/gemini-cli/pull/16709) | feat(skills): add conflict detection and warnings for skill ... | @NTaylorMullen | streaming, sessions, models, agents, ui | +0/-0 |
| [#16705](https://github.com/google-gemini/gemini-cli/pull/16705) | refactor(core): harden skill frontmatter parsing | @NTaylorMullen | shell, streaming, hooks, models, ui | +0/-0 |
| [#16345](https://github.com/google-gemini/gemini-cli/pull/16345) | fix: Handle colons in skill description frontmatter | @maru0804 | input, hooks, models, ui | +0/-0 |
| [#16657](https://github.com/google-gemini/gemini-cli/pull/16657) | chore(automation): ensure status/need-triage is applied and ... | @bdmorgan | models | +0/-0 |
| [#16587](https://github.com/google-gemini/gemini-cli/pull/16587) | fix: replace 3 consecutive periods with ellipsis character | @Vist233 | models, ui | +0/-0 |
| [#16549](https://github.com/google-gemini/gemini-cli/pull/16549) | feat(cli): add security consent prompts for skill installati... | @NTaylorMullen | models, agents, ui, config | +0/-0 |
| [#16650](https://github.com/google-gemini/gemini-cli/pull/16650) | feat(plan): add experimental plan flag | @jerop | models, mcp, config | +0/-0 |
| [#16667](https://github.com/google-gemini/gemini-cli/pull/16667) | Add timeout for shell-utils to prevent hangs. | @jacob314 | shell, streaming | +0/-0 |
| [#16672](https://github.com/google-gemini/gemini-cli/pull/16672) | cleanup: Improve keybindings | @scidomino | shell, input, hooks, models, ui | +0/-0 |
| [#16225](https://github.com/google-gemini/gemini-cli/pull/16225) | Enable & disable agents | @sehoon38 | input, hooks, models, agents, ui | +0/-0 |
| [#16661](https://github.com/google-gemini/gemini-cli/pull/16661) | feat(config): add 'auto' alias for default model selection | @sehoon38 | input, models, ui, config | +0/-0 |
| [#13507](https://github.com/google-gemini/gemini-cli/pull/13507) | chore: update dependabot configuration | @cosmopax | config | +0/-0 |
| [#13981](https://github.com/google-gemini/gemini-cli/pull/13981) | feat(cli): undeprecate the --prompt flag | @alexaustin007 | models | +0/-0 |
| [#16664](https://github.com/google-gemini/gemini-cli/pull/16664) | Remove sequence binding | @scidomino | input, hooks, ui | +0/-0 |
| [#16659](https://github.com/google-gemini/gemini-cli/pull/16659) | Remove unused rewind key binding | @scidomino | input, hooks, ui | +0/-0 |
| [#16641](https://github.com/google-gemini/gemini-cli/pull/16641) | feat(scheduler): add types needed for event driven scheduler | @abhipatel12 | shell, streaming, models, mcp, ui | +0/-0 |
| [#14953](https://github.com/google-gemini/gemini-cli/pull/14953) | fix(acp): run exit cleanup when stdin closes | @codefromthecrypt | ui, config | +0/-0 |
| [#16652](https://github.com/google-gemini/gemini-cli/pull/16652) | chore(automation): improve scheduled issue triage discovery ... | @bdmorgan | models, mcp | +0/-0 |
| [#16654](https://github.com/google-gemini/gemini-cli/pull/16654) | Simplify paste handling | @scidomino | input, hooks, models, ui | +0/-0 |
| [#16583](https://github.com/google-gemini/gemini-cli/pull/16583) | Docs: Update release notes for 1/13/2026 | @jkcinouye | ui | +0/-0 |
| [#16380](https://github.com/google-gemini/gemini-cli/pull/16380) | refactor(skills): replace 'project' with 'workspace' scope | @NTaylorMullen | models, ui | +0/-0 |
| [#16648](https://github.com/google-gemini/gemini-cli/pull/16648) | chore(automation): remove automated PR size and complexity l... | @bdmorgan | models | +0/-0 |
| [#16394](https://github.com/google-gemini/gemini-cli/pull/16394) | feat: introduce 'skill-creator' built-in skill and CJS manag... | @NTaylorMullen | shell, streaming, sessions, models, mcp, agents, ui | +0/-0 |
| [#16609](https://github.com/google-gemini/gemini-cli/pull/16609) | chore(automation): recursive labeling for workstream descend... | @bdmorgan | shell, streaming, models, mcp, ui | +0/-0 |
| [#16642](https://github.com/google-gemini/gemini-cli/pull/16642) | docs(skills): use body-file in pr-creator skill for better r... | @abhipatel12 | shell, models, agents, ui | +0/-0 |
| [#16646](https://github.com/google-gemini/gemini-cli/pull/16646) | remove unnecessary `\x7f` key bindings | @scidomino | input, hooks, ui | +0/-0 |
| [#16640](https://github.com/google-gemini/gemini-cli/pull/16640) | prefactor: add rootCommands as array so it can be used for p... | @abhipatel12 | ui | +0/-0 |
| [#16541](https://github.com/google-gemini/gemini-cli/pull/16541) | fix(a2a): Don't throw errors for  GeminiEventType Retry and ... | @ehedlund | streaming, hooks, models, mcp, ui | +0/-0 |
| [#15717](https://github.com/google-gemini/gemini-cli/pull/15717) | feat: add Rewind Confirmation dialog and Rewind Viewer compo... | @Adib234 | shell, input, hooks, sessions, models, mcp, ui | +0/-0 |
| [#16506](https://github.com/google-gemini/gemini-cli/pull/16506) | Add an experimental setting for extension config | @chrstnb | input, hooks, ui, config | +0/-0 |
| [#12899](https://github.com/google-gemini/gemini-cli/pull/12899) | docs: Remove .md extension from internal links in architectu... | @medic-code | models, ui, config | +0/-0 |
| [#16570](https://github.com/google-gemini/gemini-cli/pull/16570) | docs: clarify F12 to open debug console | @jackwotherspoon | input, hooks, models, ui | +0/-0 |
| [#16604](https://github.com/google-gemini/gemini-cli/pull/16604) | chore(release): bump version to 0.26.0-nightly.20260114.bb6c... | @gemini-cli-robot | other | +0/-0 |
| [#16527](https://github.com/google-gemini/gemini-cli/pull/16527) | fix: PDF token estimation (#16494) | @korade-krushna | shell, streaming, models, ui | +0/-0 |
| [#16406](https://github.com/google-gemini/gemini-cli/pull/16406) | feat(admin): support admin-enforced settings for Agent Skill... | @NTaylorMullen | shell, models, mcp, agents, ui, config | +0/-0 |
| [#16581](https://github.com/google-gemini/gemini-cli/pull/16581) | Aggregate test results. | @gundermanc | hooks, models, ui | +0/-0 |
| [#16577](https://github.com/google-gemini/gemini-cli/pull/16577) | fix(patch): cherry-pick eda47f5 to release/v0.24.0-preview.2... | @gemini-cli-robot | hooks | +0/-0 |
| [#16047](https://github.com/google-gemini/gemini-cli/pull/16047) | Behavioral evals framework. | @gundermanc | input, hooks, models, mcp, ui, config | +0/-0 |
| [#16565](https://github.com/google-gemini/gemini-cli/pull/16565) | Modernize MaxSizedBox to use <Box maxHeight> and ResizeObser... | @jacob314 | streaming, models, mcp, agents, ui | +0/-0 |
| [#16489](https://github.com/google-gemini/gemini-cli/pull/16489) | feat(core/ui): enhance retry mechanism and UX | @sehoon38 | streaming, sessions, models, ui | +0/-0 |
| [#16561](https://github.com/google-gemini/gemini-cli/pull/16561) |  refactor: clean up A2A task output for users and LLMs | @adamfweidman | streaming, hooks, models, mcp, ui | +0/-0 |
| [#16483](https://github.com/google-gemini/gemini-cli/pull/16483) | feat(ui): highlight persist mode status in ModelDialog | @sehoon38 | sessions, models, ui | +0/-0 |
| [#16557](https://github.com/google-gemini/gemini-cli/pull/16557) | fix(core): Resolve race condition in tool response reporting | @abhipatel12 | shell, streaming, hooks, sessions, models, mcp, ui | +0/-0 |
| [#16556](https://github.com/google-gemini/gemini-cli/pull/16556) | Fix: make ctrl+x use preferred editor | @scidomino | input, hooks, ui | +0/-0 |
| [#16532](https://github.com/google-gemini/gemini-cli/pull/16532) | docs(skills): clarify skill directory structure and file loc... | @NTaylorMullen | models, ui | +0/-0 |
| [#16537](https://github.com/google-gemini/gemini-cli/pull/16537) | fix(cli): fix 'gemini skills install' unknown argument error | @NTaylorMullen | models, ui | +0/-0 |

### PRs by Category

<details><summary><strong>agents</strong> (18 PRs)</summary>

- [#16902](https://github.com/google-gemini/gemini-cli/pull/16902) Don't commit unless user asks us to.
- [#16736](https://github.com/google-gemini/gemini-cli/pull/16736) feat(agent): enable agent skills by default
- [#16828](https://github.com/google-gemini/gemini-cli/pull/16828) refactor(cli): unify shell confirmation dialogs
- [#14142](https://github.com/google-gemini/gemini-cli/pull/14142) feat(settings): rename negative settings to positive naming (disable* -> enable*)
- [#16859](https://github.com/google-gemini/gemini-cli/pull/16859) docs(extensions): add Agent Skills support and mark feature as experimental
- [#16849](https://github.com/google-gemini/gemini-cli/pull/16849) feat(plan): enforce strict read-only policy and halt execution on violation
- [#16638](https://github.com/google-gemini/gemini-cli/pull/16638) feat(core): Add `generalist` agent.
- [#16647](https://github.com/google-gemini/gemini-cli/pull/16647) Make merged settings non-nullable and fix all lints related to that.
- [#16763](https://github.com/google-gemini/gemini-cli/pull/16763) Steer outer agent to use expert subagents when present
- [#16753](https://github.com/google-gemini/gemini-cli/pull/16753) feat(plan): add experimental 'plan' approval mode
- [#16670](https://github.com/google-gemini/gemini-cli/pull/16670) feat(policy): add source tracking to policy rules
- [#16709](https://github.com/google-gemini/gemini-cli/pull/16709) feat(skills): add conflict detection and warnings for skill overrides
- [#16549](https://github.com/google-gemini/gemini-cli/pull/16549) feat(cli): add security consent prompts for skill installation
- [#16565](https://github.com/google-gemini/gemini-cli/pull/16565) Modernize MaxSizedBox to use <Box maxHeight> and ResizeObservers
- [#16225](https://github.com/google-gemini/gemini-cli/pull/16225) Enable & disable agents
- [#16394](https://github.com/google-gemini/gemini-cli/pull/16394) feat: introduce 'skill-creator' built-in skill and CJS management tools
- [#16642](https://github.com/google-gemini/gemini-cli/pull/16642) docs(skills): use body-file in pr-creator skill for better reliability
- [#16406](https://github.com/google-gemini/gemini-cli/pull/16406) feat(admin): support admin-enforced settings for Agent Skills

</details>

<details><summary><strong>config</strong> (29 PRs)</summary>

- [#16815](https://github.com/google-gemini/gemini-cli/pull/16815) fix(core): resolve PKCE length issue and stabilize OAuth redirect port
- [#16267](https://github.com/google-gemini/gemini-cli/pull/16267) fix: Show experiment values in settings UI for compressionThreshold
- [#16804](https://github.com/google-gemini/gemini-cli/pull/16804) fix(hooks): enable /hooks disable to reliably stop single hooks
- [#16736](https://github.com/google-gemini/gemini-cli/pull/16736) feat(agent): enable agent skills by default
- [#14142](https://github.com/google-gemini/gemini-cli/pull/14142) feat(settings): rename negative settings to positive naming (disable* -> enable*)
- [#16627](https://github.com/google-gemini/gemini-cli/pull/16627) feat(admin): implement admin controls polling and restart prompt
- [#16730](https://github.com/google-gemini/gemini-cli/pull/16730) fix(core): resolve circular dependency via tsconfig paths
- [#16876](https://github.com/google-gemini/gemini-cli/pull/16876) feat(plan): remove `read_many_files` from approval mode policies
- [#16873](https://github.com/google-gemini/gemini-cli/pull/16873) fix(core): surface warnings for invalid hook event names in configuration (#16788)
- [#16849](https://github.com/google-gemini/gemini-cli/pull/16849) feat(plan): enforce strict read-only policy and halt execution on violation
- [#16773](https://github.com/google-gemini/gemini-cli/pull/16773) fix(core): fix PTY descriptor shell leak
- [#16647](https://github.com/google-gemini/gemini-cli/pull/16647) Make merged settings non-nullable and fix all lints related to that.
- [#16809](https://github.com/google-gemini/gemini-cli/pull/16809) fix(infra): update maintainer rollup label to 'workstream-rollup'
- [#15596](https://github.com/google-gemini/gemini-cli/pull/15596) Add support for running available commands prior to MCP servers loading
- [#16531](https://github.com/google-gemini/gemini-cli/pull/16531) fix(cli): safely handle /dev/tty access on macOS
- [#16696](https://github.com/google-gemini/gemini-cli/pull/16696) fix(cli): prevent OOM crash by limiting file search traversal and adding timeout
- [#16762](https://github.com/google-gemini/gemini-cli/pull/16762) fix(automation): robust label enforcement with permission checks
- [#16548](https://github.com/google-gemini/gemini-cli/pull/16548) Restricting to localhost
- [#16670](https://github.com/google-gemini/gemini-cli/pull/16670) feat(policy): add source tracking to policy rules
- [#16707](https://github.com/google-gemini/gemini-cli/pull/16707) chore(automation): enforce 'help wanted' label permissions and update guidelines
- [#16549](https://github.com/google-gemini/gemini-cli/pull/16549) feat(cli): add security consent prompts for skill installation
- [#16650](https://github.com/google-gemini/gemini-cli/pull/16650) feat(plan): add experimental plan flag
- [#16661](https://github.com/google-gemini/gemini-cli/pull/16661) feat(config): add 'auto' alias for default model selection
- [#13507](https://github.com/google-gemini/gemini-cli/pull/13507) chore: update dependabot configuration
- [#14953](https://github.com/google-gemini/gemini-cli/pull/14953) fix(acp): run exit cleanup when stdin closes
- [#16506](https://github.com/google-gemini/gemini-cli/pull/16506) Add an experimental setting for extension config
- [#12899](https://github.com/google-gemini/gemini-cli/pull/12899) docs: Remove .md extension from internal links in architecture.md
- [#16406](https://github.com/google-gemini/gemini-cli/pull/16406) feat(admin): support admin-enforced settings for Agent Skills
- [#16047](https://github.com/google-gemini/gemini-cli/pull/16047) Behavioral evals framework.

</details>

<details><summary><strong>hooks</strong> (39 PRs)</summary>

- [#16932](https://github.com/google-gemini/gemini-cli/pull/16932) Delete rewind documentation for now
- [#16479](https://github.com/google-gemini/gemini-cli/pull/16479) feat(cli): replace relative keyboard shortcuts link with web URL
- [#16267](https://github.com/google-gemini/gemini-cli/pull/16267) fix: Show experiment values in settings UI for compressionThreshold
- [#16345](https://github.com/google-gemini/gemini-cli/pull/16345) fix: Handle colons in skill description frontmatter
- [#16800](https://github.com/google-gemini/gemini-cli/pull/16800) chore: remove a2a-adapter and bump @a2a-js/sdk to 0.3.8
- [#16902](https://github.com/google-gemini/gemini-cli/pull/16902) Don't commit unless user asks us to.
- [#16804](https://github.com/google-gemini/gemini-cli/pull/16804) fix(hooks): enable /hooks disable to reliably stop single hooks
- [#14142](https://github.com/google-gemini/gemini-cli/pull/14142) feat(settings): rename negative settings to positive naming (disable* -> enable*)
- [#16882](https://github.com/google-gemini/gemini-cli/pull/16882) Patch #16730 into v0.25.0 preview
- [#16759](https://github.com/google-gemini/gemini-cli/pull/16759) Fix race condition by awaiting scheduleToolCalls
- [#16873](https://github.com/google-gemini/gemini-cli/pull/16873) fix(core): surface warnings for invalid hook event names in configuration (#16788)
- [#16864](https://github.com/google-gemini/gemini-cli/pull/16864) remove need-triage label from bug_report template
- [#16773](https://github.com/google-gemini/gemini-cli/pull/16773) fix(core): fix PTY descriptor shell leak
- [#16782](https://github.com/google-gemini/gemini-cli/pull/16782) perf(ui): optimize text buffer and highlighting for large inputs
- [#16647](https://github.com/google-gemini/gemini-cli/pull/16647) Make merged settings non-nullable and fix all lints related to that.
- [#16798](https://github.com/google-gemini/gemini-cli/pull/16798) cleanup: Organize key bindings
- [#16763](https://github.com/google-gemini/gemini-cli/pull/16763) Steer outer agent to use expert subagents when present
- [#16783](https://github.com/google-gemini/gemini-cli/pull/16783) fix(patch): cherry-pick 88f1ec8 to release/v0.24.0-pr-16179 [CONFLICTS]
- [#15596](https://github.com/google-gemini/gemini-cli/pull/15596) Add support for running available commands prior to MCP servers loading
- [#16531](https://github.com/google-gemini/gemini-cli/pull/16531) fix(cli): safely handle /dev/tty access on macOS
- [#16755](https://github.com/google-gemini/gemini-cli/pull/16755) Replace relative paths to fix website build
- [#16752](https://github.com/google-gemini/gemini-cli/pull/16752) fix(core): prevent ModelInfo event emission on aborted signal
- [#16705](https://github.com/google-gemini/gemini-cli/pull/16705) refactor(core): harden skill frontmatter parsing
- [#16672](https://github.com/google-gemini/gemini-cli/pull/16672) cleanup: Improve keybindings
- [#16225](https://github.com/google-gemini/gemini-cli/pull/16225) Enable & disable agents
- [#16664](https://github.com/google-gemini/gemini-cli/pull/16664) Remove sequence binding
- [#16659](https://github.com/google-gemini/gemini-cli/pull/16659) Remove unused rewind key binding
- [#16654](https://github.com/google-gemini/gemini-cli/pull/16654) Simplify paste handling
- [#16646](https://github.com/google-gemini/gemini-cli/pull/16646) remove unnecessary `\x7f` key bindings
- [#16541](https://github.com/google-gemini/gemini-cli/pull/16541) fix(a2a): Don't throw errors for  GeminiEventType Retry and InvalidStream.
- [#16557](https://github.com/google-gemini/gemini-cli/pull/16557) fix(core): Resolve race condition in tool response reporting
- [#15717](https://github.com/google-gemini/gemini-cli/pull/15717) feat: add Rewind Confirmation dialog and Rewind Viewer component
- [#16506](https://github.com/google-gemini/gemini-cli/pull/16506) Add an experimental setting for extension config
- [#16570](https://github.com/google-gemini/gemini-cli/pull/16570) docs: clarify F12 to open debug console
- [#16581](https://github.com/google-gemini/gemini-cli/pull/16581) Aggregate test results.
- [#16577](https://github.com/google-gemini/gemini-cli/pull/16577) fix(patch): cherry-pick eda47f5 to release/v0.24.0-preview.2-pr-16557 [CONFLICTS]
- [#16047](https://github.com/google-gemini/gemini-cli/pull/16047) Behavioral evals framework.
- [#16561](https://github.com/google-gemini/gemini-cli/pull/16561)  refactor: clean up A2A task output for users and LLMs
- [#16556](https://github.com/google-gemini/gemini-cli/pull/16556) Fix: make ctrl+x use preferred editor

</details>

<details><summary><strong>input</strong> (26 PRs)</summary>

- [#16932](https://github.com/google-gemini/gemini-cli/pull/16932) Delete rewind documentation for now
- [#16479](https://github.com/google-gemini/gemini-cli/pull/16479) feat(cli): replace relative keyboard shortcuts link with web URL
- [#16345](https://github.com/google-gemini/gemini-cli/pull/16345) fix: Handle colons in skill description frontmatter
- [#16882](https://github.com/google-gemini/gemini-cli/pull/16882) Patch #16730 into v0.25.0 preview
- [#16627](https://github.com/google-gemini/gemini-cli/pull/16627) feat(admin): implement admin controls polling and restart prompt
- [#16759](https://github.com/google-gemini/gemini-cli/pull/16759) Fix race condition by awaiting scheduleToolCalls
- [#16864](https://github.com/google-gemini/gemini-cli/pull/16864) remove need-triage label from bug_report template
- [#16782](https://github.com/google-gemini/gemini-cli/pull/16782) perf(ui): optimize text buffer and highlighting for large inputs
- [#16798](https://github.com/google-gemini/gemini-cli/pull/16798) cleanup: Organize key bindings
- [#16842](https://github.com/google-gemini/gemini-cli/pull/16842) skip simple-mcp-server.test.ts
- [#15596](https://github.com/google-gemini/gemini-cli/pull/15596) Add support for running available commands prior to MCP servers loading
- [#16755](https://github.com/google-gemini/gemini-cli/pull/16755) Replace relative paths to fix website build
- [#16752](https://github.com/google-gemini/gemini-cli/pull/16752) fix(core): prevent ModelInfo event emission on aborted signal
- [#16651](https://github.com/google-gemini/gemini-cli/pull/16651) feat(scheduler): add SchedulerStateManager for reactive tool state
- [#16672](https://github.com/google-gemini/gemini-cli/pull/16672) cleanup: Improve keybindings
- [#16225](https://github.com/google-gemini/gemini-cli/pull/16225) Enable & disable agents
- [#16661](https://github.com/google-gemini/gemini-cli/pull/16661) feat(config): add 'auto' alias for default model selection
- [#16664](https://github.com/google-gemini/gemini-cli/pull/16664) Remove sequence binding
- [#16659](https://github.com/google-gemini/gemini-cli/pull/16659) Remove unused rewind key binding
- [#16654](https://github.com/google-gemini/gemini-cli/pull/16654) Simplify paste handling
- [#16646](https://github.com/google-gemini/gemini-cli/pull/16646) remove unnecessary `\x7f` key bindings
- [#15717](https://github.com/google-gemini/gemini-cli/pull/15717) feat: add Rewind Confirmation dialog and Rewind Viewer component
- [#16506](https://github.com/google-gemini/gemini-cli/pull/16506) Add an experimental setting for extension config
- [#16570](https://github.com/google-gemini/gemini-cli/pull/16570) docs: clarify F12 to open debug console
- [#16047](https://github.com/google-gemini/gemini-cli/pull/16047) Behavioral evals framework.
- [#16556](https://github.com/google-gemini/gemini-cli/pull/16556) Fix: make ctrl+x use preferred editor

</details>

<details><summary><strong>mcp</strong> (29 PRs)</summary>

- [#16815](https://github.com/google-gemini/gemini-cli/pull/16815) fix(core): resolve PKCE length issue and stabilize OAuth redirect port
- [#16824](https://github.com/google-gemini/gemini-cli/pull/16824) refactor(core): foundational truncation refactoring and token estimation optimization
- [#16736](https://github.com/google-gemini/gemini-cli/pull/16736) feat(agent): enable agent skills by default
- [#16828](https://github.com/google-gemini/gemini-cli/pull/16828) refactor(cli): unify shell confirmation dialogs
- [#16627](https://github.com/google-gemini/gemini-cli/pull/16627) feat(admin): implement admin controls polling and restart prompt
- [#16759](https://github.com/google-gemini/gemini-cli/pull/16759) Fix race condition by awaiting scheduleToolCalls
- [#16876](https://github.com/google-gemini/gemini-cli/pull/16876) feat(plan): remove `read_many_files` from approval mode policies
- [#16859](https://github.com/google-gemini/gemini-cli/pull/16859) docs(extensions): add Agent Skills support and mark feature as experimental
- [#16849](https://github.com/google-gemini/gemini-cli/pull/16849) feat(plan): enforce strict read-only policy and halt execution on violation
- [#16842](https://github.com/google-gemini/gemini-cli/pull/16842) skip simple-mcp-server.test.ts
- [#16721](https://github.com/google-gemini/gemini-cli/pull/16721) feat(scheduler): add functional awaitConfirmation utility
- [#15596](https://github.com/google-gemini/gemini-cli/pull/15596) Add support for running available commands prior to MCP servers loading
- [#16762](https://github.com/google-gemini/gemini-cli/pull/16762) fix(automation): robust label enforcement with permission checks
- [#16548](https://github.com/google-gemini/gemini-cli/pull/16548) Restricting to localhost
- [#16751](https://github.com/google-gemini/gemini-cli/pull/16751) feat(automation): enforce '🔒 maintainer only' and fix bot loop
- [#16670](https://github.com/google-gemini/gemini-cli/pull/16670) feat(policy): add source tracking to policy rules
- [#16651](https://github.com/google-gemini/gemini-cli/pull/16651) feat(scheduler): add SchedulerStateManager for reactive tool state
- [#16565](https://github.com/google-gemini/gemini-cli/pull/16565) Modernize MaxSizedBox to use <Box maxHeight> and ResizeObservers
- [#16650](https://github.com/google-gemini/gemini-cli/pull/16650) feat(plan): add experimental plan flag
- [#16641](https://github.com/google-gemini/gemini-cli/pull/16641) feat(scheduler): add types needed for event driven scheduler
- [#16652](https://github.com/google-gemini/gemini-cli/pull/16652) chore(automation): improve scheduled issue triage discovery and throughput
- [#16394](https://github.com/google-gemini/gemini-cli/pull/16394) feat: introduce 'skill-creator' built-in skill and CJS management tools
- [#16609](https://github.com/google-gemini/gemini-cli/pull/16609) chore(automation): recursive labeling for workstream descendants
- [#16541](https://github.com/google-gemini/gemini-cli/pull/16541) fix(a2a): Don't throw errors for  GeminiEventType Retry and InvalidStream.
- [#16557](https://github.com/google-gemini/gemini-cli/pull/16557) fix(core): Resolve race condition in tool response reporting
- [#15717](https://github.com/google-gemini/gemini-cli/pull/15717) feat: add Rewind Confirmation dialog and Rewind Viewer component
- [#16406](https://github.com/google-gemini/gemini-cli/pull/16406) feat(admin): support admin-enforced settings for Agent Skills
- [#16047](https://github.com/google-gemini/gemini-cli/pull/16047) Behavioral evals framework.
- [#16561](https://github.com/google-gemini/gemini-cli/pull/16561)  refactor: clean up A2A task output for users and LLMs

</details>

<details><summary><strong>models</strong> (73 PRs)</summary>

- [#16815](https://github.com/google-gemini/gemini-cli/pull/16815) fix(core): resolve PKCE length issue and stabilize OAuth redirect port
- [#16479](https://github.com/google-gemini/gemini-cli/pull/16479) feat(cli): replace relative keyboard shortcuts link with web URL
- [#16345](https://github.com/google-gemini/gemini-cli/pull/16345) fix: Handle colons in skill description frontmatter
- [#16800](https://github.com/google-gemini/gemini-cli/pull/16800) chore: remove a2a-adapter and bump @a2a-js/sdk to 0.3.8
- [#16804](https://github.com/google-gemini/gemini-cli/pull/16804) fix(hooks): enable /hooks disable to reliably stop single hooks
- [#16824](https://github.com/google-gemini/gemini-cli/pull/16824) refactor(core): foundational truncation refactoring and token estimation optimization
- [#16736](https://github.com/google-gemini/gemini-cli/pull/16736) feat(agent): enable agent skills by default
- [#16828](https://github.com/google-gemini/gemini-cli/pull/16828) refactor(cli): unify shell confirmation dialogs
- [#14142](https://github.com/google-gemini/gemini-cli/pull/14142) feat(settings): rename negative settings to positive naming (disable* -> enable*)
- [#16627](https://github.com/google-gemini/gemini-cli/pull/16627) feat(admin): implement admin controls polling and restart prompt
- [#16759](https://github.com/google-gemini/gemini-cli/pull/16759) Fix race condition by awaiting scheduleToolCalls
- [#16730](https://github.com/google-gemini/gemini-cli/pull/16730) fix(core): resolve circular dependency via tsconfig paths
- [#16876](https://github.com/google-gemini/gemini-cli/pull/16876) feat(plan): remove `read_many_files` from approval mode policies
- [#16873](https://github.com/google-gemini/gemini-cli/pull/16873) fix(core): surface warnings for invalid hook event names in configuration (#16788)
- [#16859](https://github.com/google-gemini/gemini-cli/pull/16859) docs(extensions): add Agent Skills support and mark feature as experimental
- [#16769](https://github.com/google-gemini/gemini-cli/pull/16769) fix(core): truncate large telemetry log entries
- [#16849](https://github.com/google-gemini/gemini-cli/pull/16849) feat(plan): enforce strict read-only policy and halt execution on violation
- [#16773](https://github.com/google-gemini/gemini-cli/pull/16773) fix(core): fix PTY descriptor shell leak
- [#16782](https://github.com/google-gemini/gemini-cli/pull/16782) perf(ui): optimize text buffer and highlighting for large inputs
- [#16638](https://github.com/google-gemini/gemini-cli/pull/16638) feat(core): Add `generalist` agent.
- [#16647](https://github.com/google-gemini/gemini-cli/pull/16647) Make merged settings non-nullable and fix all lints related to that.
- [#16763](https://github.com/google-gemini/gemini-cli/pull/16763) Steer outer agent to use expert subagents when present
- [#16842](https://github.com/google-gemini/gemini-cli/pull/16842) skip simple-mcp-server.test.ts
- [#16757](https://github.com/google-gemini/gemini-cli/pull/16757) fix(cli): add explicit dependency on color-convert
- [#16818](https://github.com/google-gemini/gemini-cli/pull/16818) chore(workflows): rename label-workstream-rollup workflow
- [#16809](https://github.com/google-gemini/gemini-cli/pull/16809) fix(infra): update maintainer rollup label to 'workstream-rollup'
- [#16721](https://github.com/google-gemini/gemini-cli/pull/16721) feat(scheduler): add functional awaitConfirmation utility
- [#16753](https://github.com/google-gemini/gemini-cli/pull/16753) feat(plan): add experimental 'plan' approval mode
- [#15596](https://github.com/google-gemini/gemini-cli/pull/15596) Add support for running available commands prior to MCP servers loading
- [#16764](https://github.com/google-gemini/gemini-cli/pull/16764) docs: clarify workspace test execution in GEMINI.md
- [#16531](https://github.com/google-gemini/gemini-cli/pull/16531) fix(cli): safely handle /dev/tty access on macOS
- [#16696](https://github.com/google-gemini/gemini-cli/pull/16696) fix(cli): prevent OOM crash by limiting file search traversal and adding timeout
- [#16762](https://github.com/google-gemini/gemini-cli/pull/16762) fix(automation): robust label enforcement with permission checks
- [#16752](https://github.com/google-gemini/gemini-cli/pull/16752) fix(core): prevent ModelInfo event emission on aborted signal
- [#16751](https://github.com/google-gemini/gemini-cli/pull/16751) feat(automation): enforce '🔒 maintainer only' and fix bot loop
- [#16670](https://github.com/google-gemini/gemini-cli/pull/16670) feat(policy): add source tracking to policy rules
- [#16476](https://github.com/google-gemini/gemini-cli/pull/16476) Add links to supported locations and minor fixes
- [#16727](https://github.com/google-gemini/gemini-cli/pull/16727) fix(automation): correct status/need-issue label matching wildcard
- [#16707](https://github.com/google-gemini/gemini-cli/pull/16707) chore(automation): enforce 'help wanted' label permissions and update guidelines
- [#16651](https://github.com/google-gemini/gemini-cli/pull/16651) feat(scheduler): add SchedulerStateManager for reactive tool state
- [#16709](https://github.com/google-gemini/gemini-cli/pull/16709) feat(skills): add conflict detection and warnings for skill overrides
- [#16705](https://github.com/google-gemini/gemini-cli/pull/16705) refactor(core): harden skill frontmatter parsing
- [#16657](https://github.com/google-gemini/gemini-cli/pull/16657) chore(automation): ensure status/need-triage is applied and never cleared automatically
- [#16537](https://github.com/google-gemini/gemini-cli/pull/16537) fix(cli): fix 'gemini skills install' unknown argument error
- [#16587](https://github.com/google-gemini/gemini-cli/pull/16587) fix: replace 3 consecutive periods with ellipsis character
- [#16549](https://github.com/google-gemini/gemini-cli/pull/16549) feat(cli): add security consent prompts for skill installation
- [#16565](https://github.com/google-gemini/gemini-cli/pull/16565) Modernize MaxSizedBox to use <Box maxHeight> and ResizeObservers
- [#16650](https://github.com/google-gemini/gemini-cli/pull/16650) feat(plan): add experimental plan flag
- [#16672](https://github.com/google-gemini/gemini-cli/pull/16672) cleanup: Improve keybindings
- [#16225](https://github.com/google-gemini/gemini-cli/pull/16225) Enable & disable agents
- [#16661](https://github.com/google-gemini/gemini-cli/pull/16661) feat(config): add 'auto' alias for default model selection
- [#13981](https://github.com/google-gemini/gemini-cli/pull/13981) feat(cli): undeprecate the --prompt flag
- [#16641](https://github.com/google-gemini/gemini-cli/pull/16641) feat(scheduler): add types needed for event driven scheduler
- [#16652](https://github.com/google-gemini/gemini-cli/pull/16652) chore(automation): improve scheduled issue triage discovery and throughput
- [#16654](https://github.com/google-gemini/gemini-cli/pull/16654) Simplify paste handling
- [#16380](https://github.com/google-gemini/gemini-cli/pull/16380) refactor(skills): replace 'project' with 'workspace' scope
- [#16648](https://github.com/google-gemini/gemini-cli/pull/16648) chore(automation): remove automated PR size and complexity labeler
- [#16394](https://github.com/google-gemini/gemini-cli/pull/16394) feat: introduce 'skill-creator' built-in skill and CJS management tools
- [#16609](https://github.com/google-gemini/gemini-cli/pull/16609) chore(automation): recursive labeling for workstream descendants
- [#16642](https://github.com/google-gemini/gemini-cli/pull/16642) docs(skills): use body-file in pr-creator skill for better reliability
- [#16541](https://github.com/google-gemini/gemini-cli/pull/16541) fix(a2a): Don't throw errors for  GeminiEventType Retry and InvalidStream.
- [#16557](https://github.com/google-gemini/gemini-cli/pull/16557) fix(core): Resolve race condition in tool response reporting
- [#15717](https://github.com/google-gemini/gemini-cli/pull/15717) feat: add Rewind Confirmation dialog and Rewind Viewer component
- [#12899](https://github.com/google-gemini/gemini-cli/pull/12899) docs: Remove .md extension from internal links in architecture.md
- [#16570](https://github.com/google-gemini/gemini-cli/pull/16570) docs: clarify F12 to open debug console
- [#16527](https://github.com/google-gemini/gemini-cli/pull/16527) fix: PDF token estimation (#16494)
- [#16406](https://github.com/google-gemini/gemini-cli/pull/16406) feat(admin): support admin-enforced settings for Agent Skills
- [#16581](https://github.com/google-gemini/gemini-cli/pull/16581) Aggregate test results.
- [#16483](https://github.com/google-gemini/gemini-cli/pull/16483) feat(ui): highlight persist mode status in ModelDialog
- [#16047](https://github.com/google-gemini/gemini-cli/pull/16047) Behavioral evals framework.
- [#16489](https://github.com/google-gemini/gemini-cli/pull/16489) feat(core/ui): enhance retry mechanism and UX
- [#16561](https://github.com/google-gemini/gemini-cli/pull/16561)  refactor: clean up A2A task output for users and LLMs
- [#16532](https://github.com/google-gemini/gemini-cli/pull/16532) docs(skills): clarify skill directory structure and file location

</details>

<details><summary><strong>other</strong> (5 PRs)</summary>

- [#16872](https://github.com/google-gemini/gemini-cli/pull/16872) Remove LRUCache class migrating to mnemoist
- [#16866](https://github.com/google-gemini/gemini-cli/pull/16866) fix(patch): cherry-pick cfdc4cf to release/v0.25.0-preview.0-pr-16759 to patch version v0.25.0-preview.0 and create version 0.25.0-preview.1
- [#16865](https://github.com/google-gemini/gemini-cli/pull/16865) fix(patch): cherry-pick cfdc4cf to release/v0.24.0-pr-16759 to patch version v0.24.0 and create version 0.24.1
- [#16738](https://github.com/google-gemini/gemini-cli/pull/16738) chore/release: bump version to 0.26.0-nightly.20260115.6cb3ae4e0
- [#16604](https://github.com/google-gemini/gemini-cli/pull/16604) chore(release): bump version to 0.26.0-nightly.20260114.bb6c57414

</details>

<details><summary><strong>sessions</strong> (13 PRs)</summary>

- [#16479](https://github.com/google-gemini/gemini-cli/pull/16479) feat(cli): replace relative keyboard shortcuts link with web URL
- [#16804](https://github.com/google-gemini/gemini-cli/pull/16804) fix(hooks): enable /hooks disable to reliably stop single hooks
- [#16828](https://github.com/google-gemini/gemini-cli/pull/16828) refactor(cli): unify shell confirmation dialogs
- [#16627](https://github.com/google-gemini/gemini-cli/pull/16627) feat(admin): implement admin controls polling and restart prompt
- [#16759](https://github.com/google-gemini/gemini-cli/pull/16759) Fix race condition by awaiting scheduleToolCalls
- [#16727](https://github.com/google-gemini/gemini-cli/pull/16727) fix(automation): correct status/need-issue label matching wildcard
- [#16651](https://github.com/google-gemini/gemini-cli/pull/16651) feat(scheduler): add SchedulerStateManager for reactive tool state
- [#16709](https://github.com/google-gemini/gemini-cli/pull/16709) feat(skills): add conflict detection and warnings for skill overrides
- [#16394](https://github.com/google-gemini/gemini-cli/pull/16394) feat: introduce 'skill-creator' built-in skill and CJS management tools
- [#16557](https://github.com/google-gemini/gemini-cli/pull/16557) fix(core): Resolve race condition in tool response reporting
- [#15717](https://github.com/google-gemini/gemini-cli/pull/15717) feat: add Rewind Confirmation dialog and Rewind Viewer component
- [#16483](https://github.com/google-gemini/gemini-cli/pull/16483) feat(ui): highlight persist mode status in ModelDialog
- [#16489](https://github.com/google-gemini/gemini-cli/pull/16489) feat(core/ui): enhance retry mechanism and UX

</details>

<details><summary><strong>shell</strong> (26 PRs)</summary>

- [#16815](https://github.com/google-gemini/gemini-cli/pull/16815) fix(core): resolve PKCE length issue and stabilize OAuth redirect port
- [#16824](https://github.com/google-gemini/gemini-cli/pull/16824) refactor(core): foundational truncation refactoring and token estimation optimization
- [#16828](https://github.com/google-gemini/gemini-cli/pull/16828) refactor(cli): unify shell confirmation dialogs
- [#16759](https://github.com/google-gemini/gemini-cli/pull/16759) Fix race condition by awaiting scheduleToolCalls
- [#16849](https://github.com/google-gemini/gemini-cli/pull/16849) feat(plan): enforce strict read-only policy and halt execution on violation
- [#16773](https://github.com/google-gemini/gemini-cli/pull/16773) fix(core): fix PTY descriptor shell leak
- [#16782](https://github.com/google-gemini/gemini-cli/pull/16782) perf(ui): optimize text buffer and highlighting for large inputs
- [#16809](https://github.com/google-gemini/gemini-cli/pull/16809) fix(infra): update maintainer rollup label to 'workstream-rollup'
- [#16721](https://github.com/google-gemini/gemini-cli/pull/16721) feat(scheduler): add functional awaitConfirmation utility
- [#16764](https://github.com/google-gemini/gemini-cli/pull/16764) docs: clarify workspace test execution in GEMINI.md
- [#16531](https://github.com/google-gemini/gemini-cli/pull/16531) fix(cli): safely handle /dev/tty access on macOS
- [#16696](https://github.com/google-gemini/gemini-cli/pull/16696) fix(cli): prevent OOM crash by limiting file search traversal and adding timeout
- [#16752](https://github.com/google-gemini/gemini-cli/pull/16752) fix(core): prevent ModelInfo event emission on aborted signal
- [#16670](https://github.com/google-gemini/gemini-cli/pull/16670) feat(policy): add source tracking to policy rules
- [#16651](https://github.com/google-gemini/gemini-cli/pull/16651) feat(scheduler): add SchedulerStateManager for reactive tool state
- [#16705](https://github.com/google-gemini/gemini-cli/pull/16705) refactor(core): harden skill frontmatter parsing
- [#16667](https://github.com/google-gemini/gemini-cli/pull/16667) Add timeout for shell-utils to prevent hangs.
- [#16672](https://github.com/google-gemini/gemini-cli/pull/16672) cleanup: Improve keybindings
- [#16641](https://github.com/google-gemini/gemini-cli/pull/16641) feat(scheduler): add types needed for event driven scheduler
- [#16394](https://github.com/google-gemini/gemini-cli/pull/16394) feat: introduce 'skill-creator' built-in skill and CJS management tools
- [#16609](https://github.com/google-gemini/gemini-cli/pull/16609) chore(automation): recursive labeling for workstream descendants
- [#16642](https://github.com/google-gemini/gemini-cli/pull/16642) docs(skills): use body-file in pr-creator skill for better reliability
- [#16557](https://github.com/google-gemini/gemini-cli/pull/16557) fix(core): Resolve race condition in tool response reporting
- [#15717](https://github.com/google-gemini/gemini-cli/pull/15717) feat: add Rewind Confirmation dialog and Rewind Viewer component
- [#16527](https://github.com/google-gemini/gemini-cli/pull/16527) fix: PDF token estimation (#16494)
- [#16406](https://github.com/google-gemini/gemini-cli/pull/16406) feat(admin): support admin-enforced settings for Agent Skills

</details>

<details><summary><strong>streaming</strong> (40 PRs)</summary>

- [#16804](https://github.com/google-gemini/gemini-cli/pull/16804) fix(hooks): enable /hooks disable to reliably stop single hooks
- [#16824](https://github.com/google-gemini/gemini-cli/pull/16824) refactor(core): foundational truncation refactoring and token estimation optimization
- [#14142](https://github.com/google-gemini/gemini-cli/pull/14142) feat(settings): rename negative settings to positive naming (disable* -> enable*)
- [#16627](https://github.com/google-gemini/gemini-cli/pull/16627) feat(admin): implement admin controls polling and restart prompt
- [#16730](https://github.com/google-gemini/gemini-cli/pull/16730) fix(core): resolve circular dependency via tsconfig paths
- [#16876](https://github.com/google-gemini/gemini-cli/pull/16876) feat(plan): remove `read_many_files` from approval mode policies
- [#16873](https://github.com/google-gemini/gemini-cli/pull/16873) fix(core): surface warnings for invalid hook event names in configuration (#16788)
- [#16769](https://github.com/google-gemini/gemini-cli/pull/16769) fix(core): truncate large telemetry log entries
- [#16849](https://github.com/google-gemini/gemini-cli/pull/16849) feat(plan): enforce strict read-only policy and halt execution on violation
- [#16782](https://github.com/google-gemini/gemini-cli/pull/16782) perf(ui): optimize text buffer and highlighting for large inputs
- [#16647](https://github.com/google-gemini/gemini-cli/pull/16647) Make merged settings non-nullable and fix all lints related to that.
- [#16757](https://github.com/google-gemini/gemini-cli/pull/16757) fix(cli): add explicit dependency on color-convert
- [#16818](https://github.com/google-gemini/gemini-cli/pull/16818) chore(workflows): rename label-workstream-rollup workflow
- [#16811](https://github.com/google-gemini/gemini-cli/pull/16811) fix(infra): use GraphQL to detect direct parents in rollup workflow
- [#16809](https://github.com/google-gemini/gemini-cli/pull/16809) fix(infra): update maintainer rollup label to 'workstream-rollup'
- [#16721](https://github.com/google-gemini/gemini-cli/pull/16721) feat(scheduler): add functional awaitConfirmation utility
- [#16753](https://github.com/google-gemini/gemini-cli/pull/16753) feat(plan): add experimental 'plan' approval mode
- [#15596](https://github.com/google-gemini/gemini-cli/pull/15596) Add support for running available commands prior to MCP servers loading
- [#16764](https://github.com/google-gemini/gemini-cli/pull/16764) docs: clarify workspace test execution in GEMINI.md
- [#16531](https://github.com/google-gemini/gemini-cli/pull/16531) fix(cli): safely handle /dev/tty access on macOS
- [#16696](https://github.com/google-gemini/gemini-cli/pull/16696) fix(cli): prevent OOM crash by limiting file search traversal and adding timeout
- [#16762](https://github.com/google-gemini/gemini-cli/pull/16762) fix(automation): robust label enforcement with permission checks
- [#16548](https://github.com/google-gemini/gemini-cli/pull/16548) Restricting to localhost
- [#16755](https://github.com/google-gemini/gemini-cli/pull/16755) Replace relative paths to fix website build
- [#16752](https://github.com/google-gemini/gemini-cli/pull/16752) fix(core): prevent ModelInfo event emission on aborted signal
- [#16751](https://github.com/google-gemini/gemini-cli/pull/16751) feat(automation): enforce '🔒 maintainer only' and fix bot loop
- [#16746](https://github.com/google-gemini/gemini-cli/pull/16746) fix(automation): prevent label-enforcer loop by ignoring all bots
- [#16651](https://github.com/google-gemini/gemini-cli/pull/16651) feat(scheduler): add SchedulerStateManager for reactive tool state
- [#16709](https://github.com/google-gemini/gemini-cli/pull/16709) feat(skills): add conflict detection and warnings for skill overrides
- [#16705](https://github.com/google-gemini/gemini-cli/pull/16705) refactor(core): harden skill frontmatter parsing
- [#16565](https://github.com/google-gemini/gemini-cli/pull/16565) Modernize MaxSizedBox to use <Box maxHeight> and ResizeObservers
- [#16667](https://github.com/google-gemini/gemini-cli/pull/16667) Add timeout for shell-utils to prevent hangs.
- [#16641](https://github.com/google-gemini/gemini-cli/pull/16641) feat(scheduler): add types needed for event driven scheduler
- [#16394](https://github.com/google-gemini/gemini-cli/pull/16394) feat: introduce 'skill-creator' built-in skill and CJS management tools
- [#16609](https://github.com/google-gemini/gemini-cli/pull/16609) chore(automation): recursive labeling for workstream descendants
- [#16541](https://github.com/google-gemini/gemini-cli/pull/16541) fix(a2a): Don't throw errors for  GeminiEventType Retry and InvalidStream.
- [#16557](https://github.com/google-gemini/gemini-cli/pull/16557) fix(core): Resolve race condition in tool response reporting
- [#16527](https://github.com/google-gemini/gemini-cli/pull/16527) fix: PDF token estimation (#16494)
- [#16489](https://github.com/google-gemini/gemini-cli/pull/16489) feat(core/ui): enhance retry mechanism and UX
- [#16561](https://github.com/google-gemini/gemini-cli/pull/16561)  refactor: clean up A2A task output for users and LLMs

</details>

<details><summary><strong>ui</strong> (82 PRs)</summary>

- [#16932](https://github.com/google-gemini/gemini-cli/pull/16932) Delete rewind documentation for now
- [#16815](https://github.com/google-gemini/gemini-cli/pull/16815) fix(core): resolve PKCE length issue and stabilize OAuth redirect port
- [#16479](https://github.com/google-gemini/gemini-cli/pull/16479) feat(cli): replace relative keyboard shortcuts link with web URL
- [#16267](https://github.com/google-gemini/gemini-cli/pull/16267) fix: Show experiment values in settings UI for compressionThreshold
- [#16345](https://github.com/google-gemini/gemini-cli/pull/16345) fix: Handle colons in skill description frontmatter
- [#16800](https://github.com/google-gemini/gemini-cli/pull/16800) chore: remove a2a-adapter and bump @a2a-js/sdk to 0.3.8
- [#16902](https://github.com/google-gemini/gemini-cli/pull/16902) Don't commit unless user asks us to.
- [#16804](https://github.com/google-gemini/gemini-cli/pull/16804) fix(hooks): enable /hooks disable to reliably stop single hooks
- [#16824](https://github.com/google-gemini/gemini-cli/pull/16824) refactor(core): foundational truncation refactoring and token estimation optimization
- [#16736](https://github.com/google-gemini/gemini-cli/pull/16736) feat(agent): enable agent skills by default
- [#16828](https://github.com/google-gemini/gemini-cli/pull/16828) refactor(cli): unify shell confirmation dialogs
- [#14142](https://github.com/google-gemini/gemini-cli/pull/14142) feat(settings): rename negative settings to positive naming (disable* -> enable*)
- [#16882](https://github.com/google-gemini/gemini-cli/pull/16882) Patch #16730 into v0.25.0 preview
- [#16627](https://github.com/google-gemini/gemini-cli/pull/16627) feat(admin): implement admin controls polling and restart prompt
- [#16759](https://github.com/google-gemini/gemini-cli/pull/16759) Fix race condition by awaiting scheduleToolCalls
- [#16730](https://github.com/google-gemini/gemini-cli/pull/16730) fix(core): resolve circular dependency via tsconfig paths
- [#16873](https://github.com/google-gemini/gemini-cli/pull/16873) fix(core): surface warnings for invalid hook event names in configuration (#16788)
- [#16859](https://github.com/google-gemini/gemini-cli/pull/16859) docs(extensions): add Agent Skills support and mark feature as experimental
- [#16769](https://github.com/google-gemini/gemini-cli/pull/16769) fix(core): truncate large telemetry log entries
- [#16864](https://github.com/google-gemini/gemini-cli/pull/16864) remove need-triage label from bug_report template
- [#16849](https://github.com/google-gemini/gemini-cli/pull/16849) feat(plan): enforce strict read-only policy and halt execution on violation
- [#16773](https://github.com/google-gemini/gemini-cli/pull/16773) fix(core): fix PTY descriptor shell leak
- [#16782](https://github.com/google-gemini/gemini-cli/pull/16782) perf(ui): optimize text buffer and highlighting for large inputs
- [#16647](https://github.com/google-gemini/gemini-cli/pull/16647) Make merged settings non-nullable and fix all lints related to that.
- [#16798](https://github.com/google-gemini/gemini-cli/pull/16798) cleanup: Organize key bindings
- [#16763](https://github.com/google-gemini/gemini-cli/pull/16763) Steer outer agent to use expert subagents when present
- [#16757](https://github.com/google-gemini/gemini-cli/pull/16757) fix(cli): add explicit dependency on color-convert
- [#16818](https://github.com/google-gemini/gemini-cli/pull/16818) chore(workflows): rename label-workstream-rollup workflow
- [#16811](https://github.com/google-gemini/gemini-cli/pull/16811) fix(infra): use GraphQL to detect direct parents in rollup workflow
- [#16809](https://github.com/google-gemini/gemini-cli/pull/16809) fix(infra): update maintainer rollup label to 'workstream-rollup'
- [#16721](https://github.com/google-gemini/gemini-cli/pull/16721) feat(scheduler): add functional awaitConfirmation utility
- [#16753](https://github.com/google-gemini/gemini-cli/pull/16753) feat(plan): add experimental 'plan' approval mode
- [#15596](https://github.com/google-gemini/gemini-cli/pull/15596) Add support for running available commands prior to MCP servers loading
- [#16764](https://github.com/google-gemini/gemini-cli/pull/16764) docs: clarify workspace test execution in GEMINI.md
- [#16531](https://github.com/google-gemini/gemini-cli/pull/16531) fix(cli): safely handle /dev/tty access on macOS
- [#16696](https://github.com/google-gemini/gemini-cli/pull/16696) fix(cli): prevent OOM crash by limiting file search traversal and adding timeout
- [#16762](https://github.com/google-gemini/gemini-cli/pull/16762) fix(automation): robust label enforcement with permission checks
- [#16755](https://github.com/google-gemini/gemini-cli/pull/16755) Replace relative paths to fix website build
- [#16752](https://github.com/google-gemini/gemini-cli/pull/16752) fix(core): prevent ModelInfo event emission on aborted signal
- [#16751](https://github.com/google-gemini/gemini-cli/pull/16751) feat(automation): enforce '🔒 maintainer only' and fix bot loop
- [#16670](https://github.com/google-gemini/gemini-cli/pull/16670) feat(policy): add source tracking to policy rules
- [#16476](https://github.com/google-gemini/gemini-cli/pull/16476) Add links to supported locations and minor fixes
- [#16746](https://github.com/google-gemini/gemini-cli/pull/16746) fix(automation): prevent label-enforcer loop by ignoring all bots
- [#16727](https://github.com/google-gemini/gemini-cli/pull/16727) fix(automation): correct status/need-issue label matching wildcard
- [#16707](https://github.com/google-gemini/gemini-cli/pull/16707) chore(automation): enforce 'help wanted' label permissions and update guidelines
- [#16651](https://github.com/google-gemini/gemini-cli/pull/16651) feat(scheduler): add SchedulerStateManager for reactive tool state
- [#16709](https://github.com/google-gemini/gemini-cli/pull/16709) feat(skills): add conflict detection and warnings for skill overrides
- [#16705](https://github.com/google-gemini/gemini-cli/pull/16705) refactor(core): harden skill frontmatter parsing
- [#16537](https://github.com/google-gemini/gemini-cli/pull/16537) fix(cli): fix 'gemini skills install' unknown argument error
- [#16587](https://github.com/google-gemini/gemini-cli/pull/16587) fix: replace 3 consecutive periods with ellipsis character
- [#16549](https://github.com/google-gemini/gemini-cli/pull/16549) feat(cli): add security consent prompts for skill installation
- [#16565](https://github.com/google-gemini/gemini-cli/pull/16565) Modernize MaxSizedBox to use <Box maxHeight> and ResizeObservers
- [#16672](https://github.com/google-gemini/gemini-cli/pull/16672) cleanup: Improve keybindings
- [#16225](https://github.com/google-gemini/gemini-cli/pull/16225) Enable & disable agents
- [#16661](https://github.com/google-gemini/gemini-cli/pull/16661) feat(config): add 'auto' alias for default model selection
- [#16664](https://github.com/google-gemini/gemini-cli/pull/16664) Remove sequence binding
- [#16659](https://github.com/google-gemini/gemini-cli/pull/16659) Remove unused rewind key binding
- [#14953](https://github.com/google-gemini/gemini-cli/pull/14953) fix(acp): run exit cleanup when stdin closes
- [#16641](https://github.com/google-gemini/gemini-cli/pull/16641) feat(scheduler): add types needed for event driven scheduler
- [#16654](https://github.com/google-gemini/gemini-cli/pull/16654) Simplify paste handling
- [#16583](https://github.com/google-gemini/gemini-cli/pull/16583) Docs: Update release notes for 1/13/2026
- [#16380](https://github.com/google-gemini/gemini-cli/pull/16380) refactor(skills): replace 'project' with 'workspace' scope
- [#16394](https://github.com/google-gemini/gemini-cli/pull/16394) feat: introduce 'skill-creator' built-in skill and CJS management tools
- [#16609](https://github.com/google-gemini/gemini-cli/pull/16609) chore(automation): recursive labeling for workstream descendants
- [#16642](https://github.com/google-gemini/gemini-cli/pull/16642) docs(skills): use body-file in pr-creator skill for better reliability
- [#16646](https://github.com/google-gemini/gemini-cli/pull/16646) remove unnecessary `\x7f` key bindings
- [#16541](https://github.com/google-gemini/gemini-cli/pull/16541) fix(a2a): Don't throw errors for  GeminiEventType Retry and InvalidStream.
- [#16640](https://github.com/google-gemini/gemini-cli/pull/16640) prefactor: add rootCommands as array so it can be used for policy parsing
- [#16557](https://github.com/google-gemini/gemini-cli/pull/16557) fix(core): Resolve race condition in tool response reporting
- [#15717](https://github.com/google-gemini/gemini-cli/pull/15717) feat: add Rewind Confirmation dialog and Rewind Viewer component
- [#16506](https://github.com/google-gemini/gemini-cli/pull/16506) Add an experimental setting for extension config
- [#12899](https://github.com/google-gemini/gemini-cli/pull/12899) docs: Remove .md extension from internal links in architecture.md
- [#16570](https://github.com/google-gemini/gemini-cli/pull/16570) docs: clarify F12 to open debug console
- [#16527](https://github.com/google-gemini/gemini-cli/pull/16527) fix: PDF token estimation (#16494)
- [#16406](https://github.com/google-gemini/gemini-cli/pull/16406) feat(admin): support admin-enforced settings for Agent Skills
- [#16581](https://github.com/google-gemini/gemini-cli/pull/16581) Aggregate test results.
- [#16483](https://github.com/google-gemini/gemini-cli/pull/16483) feat(ui): highlight persist mode status in ModelDialog
- [#16047](https://github.com/google-gemini/gemini-cli/pull/16047) Behavioral evals framework.
- [#16489](https://github.com/google-gemini/gemini-cli/pull/16489) feat(core/ui): enhance retry mechanism and UX
- [#16561](https://github.com/google-gemini/gemini-cli/pull/16561)  refactor: clean up A2A task output for users and LLMs
- [#16556](https://github.com/google-gemini/gemini-cli/pull/16556) Fix: make ctrl+x use preferred editor
- [#16532](https://github.com/google-gemini/gemini-cli/pull/16532) docs(skills): clarify skill directory structure and file location

</details>

---

## Open Milestones

### [Public OSS](https://github.com/google-gemini/gemini-cli/milestone/1)

**Progress:** 99% (83/84 issues) | Due: 2025-06-25

### [Q3 '2025](https://github.com/google-gemini/gemini-cli/milestone/3)

**Progress:** 76% (52/68 issues) | Due: 2025-09-30

### [GCA - Preview June 23](https://github.com/google-gemini/gemini-cli/milestone/2)

**Progress:** 100% (16/16 issues) | No due date

---

## Upcoming Features (Open PRs)

### Label: `priority/p1` (10 PRs)

- [#16689](https://github.com/google-gemini/gemini-cli/pull/16689) chore(deps): bump google-auth-library from 9.15.1 to 10.5.0 (streaming, hooks, ui)
- [#16599](https://github.com/google-gemini/gemini-cli/pull/16599) fix: migrate BeforeModel and AfterModel hooks to HookSystem (streaming, hooks, models, agents, ui)
- [#16589](https://github.com/google-gemini/gemini-cli/pull/16589) Port integration tests to evals. (input, hooks, ui)
- [#16574](https://github.com/google-gemini/gemini-cli/pull/16574) feat: add `clearContext` to `AfterAgent` hooks (shell, input, streaming, hooks, sessions, agents, ui)
- [#16558](https://github.com/google-gemini/gemini-cli/pull/16558) Add '/agent debug' command (input, hooks, agents, ui)
- [#16542](https://github.com/google-gemini/gemini-cli/pull/16542) fix: refresh agents when extensions are reloaded (input, hooks, agents, ui)
- [#16508](https://github.com/google-gemini/gemini-cli/pull/16508) Add noninteractive auth check to install command (input, hooks, ui)
- [#16486](https://github.com/google-gemini/gemini-cli/pull/16486) feat(core): improve shell redirection transparency and security (shell, models, ui)
- [#16480](https://github.com/google-gemini/gemini-cli/pull/16480) 解决使用自己代理服务器 baseurl 不起作用问题 (input, hooks, ui, config)
- [#16463](https://github.com/google-gemini/gemini-cli/pull/16463) Implement support for 'ask' (hooks, ui)

### Label: `priority/p2` (8 PRs)

- [#16702](https://github.com/google-gemini/gemini-cli/pull/16702) feat: add gemini update command (shell, input, hooks, models, ui, config)
- [#16700](https://github.com/google-gemini/gemini-cli/pull/16700) feat(cli): add /restart command for graceful session restart (input, hooks, sessions, models, mcp, ui)
- [#16680](https://github.com/google-gemini/gemini-cli/pull/16680) chore(deps): bump actions/checkout from 4 to 6 (hooks, ui, config)
- [#16669](https://github.com/google-gemini/gemini-cli/pull/16669) feat(ui): implement output verbosity controls (shell, streaming, hooks, sessions, models, mcp, agents, ui, config)
- [#16653](https://github.com/google-gemini/gemini-cli/pull/16653) chore(deps): bump undici from 7.15.0 to 7.18.2 (streaming, hooks, models, mcp, agents, ui, config)
- [#16580](https://github.com/google-gemini/gemini-cli/pull/16580) fix(ui): strip trailing punctuation from URLs in inline markdown (input, hooks, ui)
- [#16563](https://github.com/google-gemini/gemini-cli/pull/16563) feat(ui): add solid background color option for input prompt (shell, input, hooks, models, ui)
- [#16535](https://github.com/google-gemini/gemini-cli/pull/16535) feat(ui): add bell setting to notify when user input is requested (input, models, ui, config)

### Label: `priority/p3` (2 PRs)

- [#16687](https://github.com/google-gemini/gemini-cli/pull/16687) chore(deps): bump @xterm/headless from 5.5.0 to 6.0.0 (shell, input, streaming, hooks, models, ui)
- [#16487](https://github.com/google-gemini/gemini-cli/pull/16487) Add support for an additional exclusion file besides .gitignore and .geminiignore (models, mcp, ui)

---

## Porting Recommendations

Based on the changes above, consider reviewing:

### Hooks

- [ ] [#16932](https://github.com/google-gemini/gemini-cli/pull/16932) Delete rewind documentation for now
- [ ] [#16479](https://github.com/google-gemini/gemini-cli/pull/16479) feat(cli): replace relative keyboard shortcuts link with web URL
- [ ] [#16267](https://github.com/google-gemini/gemini-cli/pull/16267) fix: Show experiment values in settings UI for compressionThreshold
- [ ] [#16345](https://github.com/google-gemini/gemini-cli/pull/16345) fix: Handle colons in skill description frontmatter
- [ ] [#16800](https://github.com/google-gemini/gemini-cli/pull/16800) chore: remove a2a-adapter and bump @a2a-js/sdk to 0.3.8

### Mcp

- [ ] [#16815](https://github.com/google-gemini/gemini-cli/pull/16815) fix(core): resolve PKCE length issue and stabilize OAuth redirect port
- [ ] [#16824](https://github.com/google-gemini/gemini-cli/pull/16824) refactor(core): foundational truncation refactoring and token estimation optimization
- [ ] [#16736](https://github.com/google-gemini/gemini-cli/pull/16736) feat(agent): enable agent skills by default
- [ ] [#16828](https://github.com/google-gemini/gemini-cli/pull/16828) refactor(cli): unify shell confirmation dialogs
- [ ] [#16627](https://github.com/google-gemini/gemini-cli/pull/16627) feat(admin): implement admin controls polling and restart prompt

### Agents

- [ ] [#16902](https://github.com/google-gemini/gemini-cli/pull/16902) Don't commit unless user asks us to.
- [ ] [#16736](https://github.com/google-gemini/gemini-cli/pull/16736) feat(agent): enable agent skills by default
- [ ] [#16828](https://github.com/google-gemini/gemini-cli/pull/16828) refactor(cli): unify shell confirmation dialogs
- [ ] [#14142](https://github.com/google-gemini/gemini-cli/pull/14142) feat(settings): rename negative settings to positive naming (disable* -> enable*)
- [ ] [#16859](https://github.com/google-gemini/gemini-cli/pull/16859) docs(extensions): add Agent Skills support and mark feature as experimental

### Streaming

- [ ] [#16804](https://github.com/google-gemini/gemini-cli/pull/16804) fix(hooks): enable /hooks disable to reliably stop single hooks
- [ ] [#16824](https://github.com/google-gemini/gemini-cli/pull/16824) refactor(core): foundational truncation refactoring and token estimation optimization
- [ ] [#14142](https://github.com/google-gemini/gemini-cli/pull/14142) feat(settings): rename negative settings to positive naming (disable* -> enable*)
- [ ] [#16627](https://github.com/google-gemini/gemini-cli/pull/16627) feat(admin): implement admin controls polling and restart prompt
- [ ] [#16730](https://github.com/google-gemini/gemini-cli/pull/16730) fix(core): resolve circular dependency via tsconfig paths

### Sessions

- [ ] [#16479](https://github.com/google-gemini/gemini-cli/pull/16479) feat(cli): replace relative keyboard shortcuts link with web URL
- [ ] [#16804](https://github.com/google-gemini/gemini-cli/pull/16804) fix(hooks): enable /hooks disable to reliably stop single hooks
- [ ] [#16828](https://github.com/google-gemini/gemini-cli/pull/16828) refactor(cli): unify shell confirmation dialogs
- [ ] [#16627](https://github.com/google-gemini/gemini-cli/pull/16627) feat(admin): implement admin controls polling and restart prompt
- [ ] [#16759](https://github.com/google-gemini/gemini-cli/pull/16759) Fix race condition by awaiting scheduleToolCalls
