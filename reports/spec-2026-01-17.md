# Gemini CLI Implementation Specification (Auto-Generated)

**Generated:** 2026-01-17 20:20
**Source:** [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) @ `main`

---

## Skills

### Source: `skillLoader.ts`

```typescript
interface SkillDefinition {
  /** The unique name of the skill. */
  name: string;
  /** A concise description of what the skill does. */
  description: string;
  /** The absolute path to the skill's source file on disk. */
  location: string;
  /** The core logic/instructions of the skill. */
  body: string;
  /** Whether the skill is currently disabled. */
  disabled?: boolean;
  /** Whether the skill is a built-in skill. */
  isBuiltin?: boolean;...
}
```

### Source: `skillManager.ts`

**Class `SkillManager`** - Methods: `clearSkills, setAdminSettings, isAdminEnabled, discoverSkills, discoverBuiltinSkills`

### Source: `list.ts`

### Source: `install.ts`

```typescript
interface InstallArgs {
  source: string;
  scope?: 'user' | 'workspace';
  path?: string;
  consent?: boolean;...
}
```

### Key Constants

```typescript
const FRONTMATTER_REGEX = /^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n([\s\S]*))?/;
```


---

## Agents

### Source: `types.ts`

```typescript
interface OutputObject {
  result: string;
  terminate_reason: AgentTerminateMode;...
}
```

```typescript
interface SubagentActivityEvent {
  isSubagentActivityEvent: true;
  agentName: string;
  type: 'TOOL_CALL_START' | 'TOOL_CALL_END' | 'THOUGHT_CHUNK' | 'ERROR';
  data: Record<string, unknown>;...
}
```

```typescript
interface BaseAgentDefinition {
  /** Unique identifier for the agent. */
  name: string;
  displayName?: string;
  description: string;
  experimental?: boolean;
  inputConfig: InputConfig;
  outputConfig?: OutputConfig<TOutput>;...
}
```

```typescript
interface LocalAgentDefinition {
  kind: 'local';

  // Local agent required configs
  promptConfig: PromptConfig;
  modelConfig: ModelConfig;
  runConfig: RunConfig;

  // Optional configs
  toolConfig?: ToolConfig;

  /**
   * An optional function to process the raw output from the agent's final tool
   * call into a string format.
   *
   * @param output The raw output value from the `complete_task` tool, now strongly typed with TOutput.
   * @returns A string representation of the final output.
   */
  processOutput?: (output...
}
```

```typescript
interface RemoteAgentDefinition {
  kind: 'remote';
  agentCardUrl: string;...
}
```

### Source: `registry.ts`

**Class `AgentRegistry`** - Methods: `initialize, reload, dispose, loadAgents`

### Source: `local-executor.ts`

```typescript
type ActivityCallback = (activity: SubagentActivityEvent) => void
```

```typescript
type AgentTurnResult = | {
      status: 'continue'
```

### Source: `codebase-investigator.ts`

### Key Constants

```typescript
const TASK_COMPLETE_TOOL_NAME = 'complete_task';
const GRACE_PERIOD_MS = 60 * 1000;
```


---

## Hooks

### Source: `types.ts`

```typescript
interface CommandHookConfig {
  type: HookType.Command;
  command: string;
  name?: string;
  description?: string;
  timeout?: number;
  source?: ConfigSource;...
}
```

```typescript
interface HookDefinition {
  matcher?: string;
  sequential?: boolean;
  hooks: HookConfig[];...
}
```

```typescript
interface HookInput {
  session_id: string;
  transcript_path: string;
  cwd: string;
  hook_event_name: string;
  timestamp: string;...
}
```

```typescript
interface HookOutput {
  continue?: boolean;
  stopReason?: string;
  suppressOutput?: boolean;
  systemMessage?: string;
  decision?: HookDecision;
  reason?: string;
  hookSpecificOutput?: Record<string, unknown>;...
}
```

```typescript
interface McpToolContext {
  server_name: string;
  tool_name: string; // Original tool name from the MCP server

  // Connection info (mutually exclusive based on transport type)
  command?: string; // For stdio transport
  args?: string[]; // For stdio transport
  cwd?: string; // For stdio transport

  url?: string; // For SSE/HTTP transport

  tcp?: string; // For WebSocket transport...
}
```

**Class `DefaultHookOutput`** - Methods: `isBlockingDecision, shouldStopExecution, getEffectiveReason, applyLLMRequestModifications, applyToolConfigModifications`

**Class `BeforeToolHookOutput`** - Methods: `getModifiedToolInput, getSyntheticResponse, applyLLMRequestModifications, applyToolConfigModifications, getModifiedResponse`

**Class `BeforeModelHookOutput`** - Methods: `getSyntheticResponse, applyLLMRequestModifications, applyToolConfigModifications, getModifiedResponse`

### Source: `hookRegistry.ts`

```typescript
interface HookRegistryEntry {
  config: HookConfig;
  source: ConfigSource;
  eventName: HookEventName;
  matcher?: string;
  sequential?: boolean;
  enabled: boolean;...
}
```

**Class `HookRegistry`** - Methods: `initialize, getHooksForEvent, getAllHooks, setHookEnabled, getHookName`

### Source: `hookRunner.ts`

**Class `HookRunner`** - Methods: `executeHook, catch, warn`

### Source: `hookSystem.ts`

**Class `HookSystem`** - Methods: `initialize, getEventHandler, getRegistry, setHookEnabled, getAllHooks`

### Key Constants

```typescript
const HOOKS_CONFIG_FIELDS = ['enabled', 'disabled', 'notifications'];
const DEFAULT_HOOK_TIMEOUT = 60000;
const EXIT_CODE_SUCCESS = 0;
const EXIT_CODE_BLOCKING_ERROR = 2;
const EXIT_CODE_NON_BLOCKING_ERROR = 1;
```


---

## Sessions

### Source: `useSessionBrowser.ts`


---
