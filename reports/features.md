# Gemini CLI Feature Tracker

**Updated:** 2026-01-18 01:27 UTC
**Your Fork:** v0.14.0
**Latest Stable:** v0.24.0
**Commits Behind:** 813

---

## Summary (Last 30 Days)

| Feature | Merged PRs | Open PRs | Files Changed Since Fork |
|---------|------------|----------|--------------------------|
| **Skills** | 10 | 1 | 18 |
| **Agents** | 5 | 20 | 28 |
| **Hooks** | 3 | 11 | 3 |

---

## Skills

### Recently Merged (10)

- [#16345](https://github.com/google-gemini/gemini-cli/pull/16345) fix: Handle colons in skill description frontmatter
  - `packages/core/src/skills/skillLoader.test.ts`
  - `packages/core/src/skills/skillLoader.ts`
- [#16736](https://github.com/google-gemini/gemini-cli/pull/16736) feat(agent): enable agent skills by default
  - `packages/cli/src/config/skills-backward-compatibility.test.ts`
  - `packages/cli/src/ui/commands/skillsCommand.test.ts`
- [#16709](https://github.com/google-gemini/gemini-cli/pull/16709) feat(skills): add conflict detection and warnings for skill overrides
  - `packages/core/src/skills/skillManager.test.ts`
  - `packages/core/src/skills/skillManager.ts`
- [#16705](https://github.com/google-gemini/gemini-cli/pull/16705) refactor(core): harden skill frontmatter parsing
  - `packages/core/src/skills/skillLoader.test.ts`
  - `packages/core/src/skills/skillLoader.ts`
- [#16537](https://github.com/google-gemini/gemini-cli/pull/16537) fix(cli): fix 'gemini skills install' unknown argument error
  - `packages/cli/src/commands/skills/disable.test.ts`
  - `packages/cli/src/commands/skills/disable.ts`
  - `packages/cli/src/commands/skills/install.test.ts`
- [#16549](https://github.com/google-gemini/gemini-cli/pull/16549) feat(cli): add security consent prompts for skill installation
  - `packages/cli/src/commands/skills/install.test.ts`
  - `packages/cli/src/commands/skills/install.ts`
  - `packages/cli/src/utils/skillUtils.test.ts`
- [#16380](https://github.com/google-gemini/gemini-cli/pull/16380) refactor(skills): replace 'project' with 'workspace' scope
  - `docs/cli/skills.md`
  - `packages/cli/src/commands/skills/disable.test.ts`
  - `packages/cli/src/commands/skills/disable.ts`
- [#16394](https://github.com/google-gemini/gemini-cli/pull/16394) feat: introduce 'skill-creator' built-in skill and CJS management tools
  - `integration-tests/skill-creator-scripts.test.ts`
  - `integration-tests/skill-creator-vulnerabilities.test.ts`
  - `packages/core/src/skills/builtin/skill-creator/SKILL.md`
- [#16642](https://github.com/google-gemini/gemini-cli/pull/16642) docs(skills): use body-file in pr-creator skill for better reliability
  - `.gemini/skills/pr-creator/SKILL.md`
- [#16406](https://github.com/google-gemini/gemini-cli/pull/16406) feat(admin): support admin-enforced settings for Agent Skills
  - `packages/cli/src/config/extension-manager-skills.test.ts`
  - `packages/cli/src/ui/commands/skillsCommand.test.ts`
  - `packages/cli/src/ui/commands/skillsCommand.ts`

### Coming Soon (1 open)

- [#16822](https://github.com/google-gemini/gemini-cli/pull/16822) feat(cli): align hooks enable/disable with skills and improve completion

### Files Changed Since v0.14.0

- `added` `docs/cli/skills.md` (+188)
- `added` `docs/cli/tutorials/skills-getting-started.md` (+124)
- `added` `.gemini/skills/pr-creator/SKILL.md` (+57)
- `added` `integration-tests/skill-creator-scripts.test.ts` (+0)
- `added` `integration-tests/skill-creator-vulnerabilities.test.ts` (+0)
- `added` `packages/cli/src/commands/skills.test.tsx` (+0)
- `added` `packages/cli/src/commands/skills.tsx` (+0)
- `added` `packages/cli/src/commands/skills/disable.test.ts` (+0)
- `added` `packages/cli/src/commands/skills/disable.ts` (+0)
- `added` `packages/cli/src/commands/skills/enable.test.ts` (+0)
- *... and 8 more*

---

## Agents

### Recently Merged (5)

- [#16800](https://github.com/google-gemini/gemini-cli/pull/16800) chore: remove a2a-adapter and bump @a2a-js/sdk to 0.3.8
  - `packages/a2a-server/package.json`
  - `packages/core/src/agents/a2a-client-manager.test.ts`
  - `packages/core/src/agents/a2a-client-manager.ts`
- [#16638](https://github.com/google-gemini/gemini-cli/pull/16638) feat(core): Add `generalist` agent.
  - `packages/core/src/agents/generalist-agent.test.ts`
  - `packages/core/src/agents/generalist-agent.ts`
  - `packages/core/src/agents/registry.test.ts`
- [#16763](https://github.com/google-gemini/gemini-cli/pull/16763) Steer outer agent to use expert subagents when present
  - `evals/subagents.eval.ts`
  - `packages/core/src/agents/local-executor.ts`
  - `packages/core/src/agents/registry.ts`
- [#16225](https://github.com/google-gemini/gemini-cli/pull/16225) Enable & disable agents
  - `packages/core/src/agents/a2a-client-manager.ts`
  - `packages/core/src/agents/registry.ts`
- [#16541](https://github.com/google-gemini/gemini-cli/pull/16541) fix(a2a): Don't throw errors for  GeminiEventType Retry and InvalidStream.
  - `packages/a2a-server/src/agent/task.test.ts`
  - `packages/a2a-server/src/agent/task.ts`

### Coming Soon (20 open)

- [#16919](https://github.com/google-gemini/gemini-cli/pull/16919) remove fireAgent and beforeAgent hook
- [#16918](https://github.com/google-gemini/gemini-cli/pull/16918) fix(acp): await session/update notifications before returning response
- [#16895](https://github.com/google-gemini/gemini-cli/pull/16895) refactor(core): decouple scheduler into orchestration, policy, and confirmation
- [#16879](https://github.com/google-gemini/gemini-cli/pull/16879) Gundermanc/slash agents
- [#16856](https://github.com/google-gemini/gemini-cli/pull/16856) feat(core): Add initial eval for generalist agent.
- [#16833](https://github.com/google-gemini/gemini-cli/pull/16833) fix return type of fireSessionStartEvent to defaultHookOutput 
- [#16816](https://github.com/google-gemini/gemini-cli/pull/16816) docs(hooks): comprehensive update of hook documentation and specs

### Files Changed Since v0.14.0

- `added` `evals/subagents.eval.ts` (+64)
- `modified` `packages/a2a-server/development-extension-rfc.md` (+0)
- `modified` `packages/a2a-server/package.json` (+0)
- `modified` `packages/a2a-server/src/agent/executor.ts` (+0)
- `modified` `packages/a2a-server/src/agent/task.test.ts` (+0)
- `modified` `packages/a2a-server/src/agent/task.ts` (+0)
- `modified` `packages/a2a-server/src/commands/command-registry.test.ts` (+0)
- `modified` `packages/a2a-server/src/commands/command-registry.ts` (+0)
- `added` `packages/a2a-server/src/commands/extensions.test.ts` (+0)
- `added` `packages/a2a-server/src/commands/extensions.ts` (+0)
- *... and 18 more*

---

## Hooks

### Recently Merged (3)

- [#16828](https://github.com/google-gemini/gemini-cli/pull/16828) refactor(cli): unify shell confirmation dialogs
  - `packages/cli/src/ui/hooks/slashCommandProcessor.test.tsx`
  - `packages/cli/src/ui/hooks/slashCommandProcessor.ts`
- [#16873](https://github.com/google-gemini/gemini-cli/pull/16873) fix(core): surface warnings for invalid hook event names in configuration (#16788)
  - `packages/core/src/hooks/hookRegistry.test.ts`
  - `packages/core/src/hooks/hookRegistry.ts`
  - `packages/core/src/hooks/types.ts`
- [#16647](https://github.com/google-gemini/gemini-cli/pull/16647) Make merged settings non-nullable and fix all lints related to that.
  - `packages/cli/src/commands/hooks/migrate.ts`
  - `packages/cli/src/config/extension-manager-skills.test.ts`
  - `packages/cli/src/ui/hooks/useAlternateBuffer.ts`

### Coming Soon (11 open)

- [#16912](https://github.com/google-gemini/gemini-cli/pull/16912) feat(ui): improve settings consistency and clarity
- [#16878](https://github.com/google-gemini/gemini-cli/pull/16878) Fix hooks exit code.
- [#16870](https://github.com/google-gemini/gemini-cli/pull/16870) feat(core): Ensure all properties in `hooks` object are event names.
- [#16848](https://github.com/google-gemini/gemini-cli/pull/16848) feat: add /new command & list extensions on update failure
- [#16760](https://github.com/google-gemini/gemini-cli/pull/16760) Docs: Marking for experimental features
- [#16740](https://github.com/google-gemini/gemini-cli/pull/16740) fix(ui): handle Ctrl+X external editor and env editor resolution
- [#16719](https://github.com/google-gemini/gemini-cli/pull/16719) fix: pause streaming after tool call requests

### Files Changed Since v0.14.0

- `added` `packages/cli/src/commands/hooks.tsx` (+0)
- `added` `packages/cli/src/commands/hooks/migrate.test.ts` (+0)
- `added` `packages/cli/src/commands/hooks/migrate.ts` (+0)

---

## Recent Stable Releases

- [v0.24.0](https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0) (2026-01-14)
- [v0.23.0](https://github.com/google-gemini/gemini-cli/releases/tag/v0.23.0) (2026-01-07)
- [v0.22.5](https://github.com/google-gemini/gemini-cli/releases/tag/v0.22.5) (2025-12-30)
- [v0.22.4](https://github.com/google-gemini/gemini-cli/releases/tag/v0.22.4) (2025-12-27)
- [v0.22.3](https://github.com/google-gemini/gemini-cli/releases/tag/v0.22.3) (2025-12-26)
