# Gemini CLI Implementation Specification

**Version Delta:** v0.14.0 → v0.24.0
**Features:** Skills, Agents, Hooks, Sessions
**Source:** [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) (Apache-2.0)

---

## Part 1: Skills System (v0.17.0+)

### 1.1 Core Types

```typescript
// skillLoader.ts
interface SkillDefinition {
  name: string;           // Unique skill identifier
  description: string;    // What the skill does
  location: string;       // Absolute path to SKILL.md
  body: string;           // Core instructions/logic
  disabled?: boolean;     // Runtime disable flag
  isBuiltin?: boolean;    // Built-in vs user skill
}
```

### 1.2 Skill File Format

Skills are defined as `SKILL.md` files with YAML frontmatter:

```markdown
---
name: code-reviewer
description: Reviews code for best practices and security issues
---

When reviewing code, check for:
1. Security vulnerabilities (injection, XSS, etc.)
2. Performance issues
3. Code style violations
...
```

### 1.3 Discovery Precedence

```
builtin → extension → user → workspace (highest priority wins)
```

**Search Paths:**
- `packages/cli/src/skills/` (builtin)
- Extension directories
- `~/.gemini/skills/` (user)
- `.gemini/skills/` (workspace)

### 1.4 Loader Implementation

```typescript
// Discovery pattern - searches for SKILL.md files
const FRONTMATTER_REGEX = /^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n([\s\S]*))?/;

async function loadSkillsFromDir(dir: string): Promise<SkillDefinition[]> {
  const skillFiles = await glob(['SKILL.md', '*/SKILL.md'], {
    cwd: dir,
    absolute: true,
    nodir: true,
  });

  return Promise.all(skillFiles.map(loadSkillFromFile));
}

async function loadSkillFromFile(filePath: string): Promise<SkillDefinition | null> {
  const content = await fs.readFile(filePath, 'utf-8');
  const match = content.match(FRONTMATTER_REGEX);
  if (!match) return null;

  const frontmatter = yaml.load(match[1]);
  return {
    name: frontmatter.name,
    description: frontmatter.description,
    location: filePath,
    body: match[2]?.trim() ?? '',
  };
}
```

### 1.5 Manager API

```typescript
// skillManager.ts - Key methods
class SkillManager {
  async loadSkills(): Promise<void>;
  getActiveSkills(): SkillDefinition[];
  enableSkill(name: string): void;
  disableSkill(name: string): void;
  getSkillByName(name: string): SkillDefinition | undefined;
}
```

### 1.6 CLI Commands

| Command | File | Purpose |
|---------|------|---------|
| `gemini skills list` | `commands/skills/list.ts` | Show all available skills |
| `gemini skills enable <name>` | `commands/skills/enable.ts` | Activate a skill |
| `gemini skills disable <name>` | `commands/skills/disable.ts` | Deactivate a skill |
| `gemini skills install <path>` | `commands/skills/install.ts` | Install from path/URL |
| `gemini skills uninstall <name>` | `commands/skills/uninstall.ts` | Remove installed skill |

---

## Part 2: Agent Framework (v0.15.0+)

### 2.1 Core Types

```typescript
// agents/types.ts
enum AgentTerminateMode {
  ERROR = 'ERROR',
  TIMEOUT = 'TIMEOUT',
  GOAL = 'GOAL',
  MAX_TURNS = 'MAX_TURNS',
  ABORTED = 'ABORTED',
  ERROR_NO_COMPLETE_TASK_CALL = 'ERROR_NO_COMPLETE_TASK_CALL',
}

interface OutputObject {
  result: string;
  terminate_reason: AgentTerminateMode;
}

interface BaseAgentDefinition<TOutput extends z.ZodTypeAny = z.ZodUnknown> {
  name: string;
  displayName?: string;
  description: string;
  experimental?: boolean;
  inputConfig: InputConfig;
  outputConfig?: OutputConfig<TOutput>;
}

// Local agents run in-process
interface LocalAgentDefinition<TOutput> extends BaseAgentDefinition<TOutput> {
  kind: 'local';
  promptConfig: PromptConfig;
  modelConfig: ModelConfig;
  runConfig: RunConfig;
  toolConfig?: ToolConfig;
  processOutput?: (output: z.infer<TOutput>) => string;
}

// Remote agents use A2A protocol
interface RemoteAgentDefinition<TOutput> extends BaseAgentDefinition<TOutput> {
  kind: 'remote';
  agentCardUrl: string;  // URL to agent card JSON
}
```

### 2.2 Configuration Interfaces

```typescript
interface PromptConfig {
  systemPrompt?: string;        // Supports ${input_name} templating
  initialMessages?: Content[];  // Few-shot examples
  query?: string;               // Initial task prompt
}

interface RunConfig {
  maxTimeMinutes: number;  // Timeout
  maxTurns?: number;       // Max conversation turns
}

interface InputConfig {
  inputs: Record<string, {
    description: string;
    type: 'string' | 'number' | 'boolean' | 'integer' | 'string[]' | 'number[]';
    required: boolean;
  }>;
}

interface ToolConfig {
  tools: Array<string | FunctionDeclaration | AnyDeclarativeTool>;
}
```

### 2.3 Local Executor Loop

```typescript
// local-executor.ts - Simplified execution loop
class LocalAgentExecutor<TOutput extends z.ZodTypeAny> {
  private readonly TASK_COMPLETE_TOOL_NAME = 'complete_task';
  private readonly GRACE_PERIOD_MS = 60 * 1000;  // 60s recovery window

  async run(inputs: AgentInputs, signal: AbortSignal): Promise<OutputObject> {
    const timeoutController = new AbortController();
    setTimeout(() => timeoutController.abort(), maxTimeMinutes * 60 * 1000);

    const combinedSignal = AbortSignal.any([signal, timeoutController.signal]);

    while (true) {
      // Check termination conditions
      const reason = this.checkTermination(startTime, turnCounter);
      if (reason) break;

      // Execute turn
      const turnResult = await this.executeTurn(chat, currentMessage, turnCounter++, combinedSignal);

      if (turnResult.status === 'stop') {
        terminateReason = turnResult.terminateReason;
        finalResult = turnResult.finalResult;
        break;
      }

      currentMessage = turnResult.nextMessage;
    }

    // Recovery attempt on non-fatal termination
    if (terminateReason !== AgentTerminateMode.GOAL &&
        terminateReason !== AgentTerminateMode.ABORTED) {
      const recoveryResult = await this.executeFinalWarningTurn(chat, turnCounter, terminateReason, signal);
      if (recoveryResult) {
        terminateReason = AgentTerminateMode.GOAL;
        finalResult = recoveryResult;
      }
    }

    return { result: finalResult, terminate_reason: terminateReason };
  }
}
```

### 2.4 Built-in Agents

| Agent | File | Purpose |
|-------|------|---------|
| `CodebaseInvestigator` | `codebase-investigator.ts` | Deep code analysis |
| `CliHelp` | `cli-help-agent.ts` | CLI usage assistance |
| `Generalist` | `generalist-agent.ts` | General-purpose tasks |

### 2.5 Agent Registry

```typescript
// registry.ts
class AgentRegistry {
  private agents: Map<string, AgentDefinition> = new Map();

  registerAgent(definition: AgentDefinition): void;
  getAgent(name: string): AgentDefinition | undefined;
  getAllAgents(): AgentDefinition[];

  // Model config routing for subagents
  getModelConfigAlias(definition: LocalAgentDefinition): string;
}

// Built-in registration
registry.registerAgent({
  name: 'codebase-investigator',
  kind: 'local',
  description: 'Investigates codebase structure and patterns',
  // ...
});
```

### 2.6 Subagent Activity Events

```typescript
interface SubagentActivityEvent {
  isSubagentActivityEvent: true;
  agentName: string;
  type: 'TOOL_CALL_START' | 'TOOL_CALL_END' | 'THOUGHT_CHUNK' | 'ERROR';
  data: Record<string, unknown>;
}
```

---

## Part 3: Hook System (v0.13.0+)

### 3.1 Event Types

```typescript
// hooks/types.ts
enum HookEventName {
  BeforeTool = 'BeforeTool',
  AfterTool = 'AfterTool',
  BeforeAgent = 'BeforeAgent',
  AfterAgent = 'AfterAgent',
  SessionStart = 'SessionStart',
  SessionEnd = 'SessionEnd',
  PreCompress = 'PreCompress',
  BeforeModel = 'BeforeModel',
  AfterModel = 'AfterModel',
  BeforeToolSelection = 'BeforeToolSelection',
  Notification = 'Notification',
}

enum ConfigSource {
  Project = 'project',   // .gemini/settings.json (highest priority)
  User = 'user',         // ~/.gemini/settings.json
  System = 'system',     // System defaults
  Extensions = 'extensions',
}
```

### 3.2 Hook Configuration

```typescript
interface CommandHookConfig {
  type: 'command';
  command: string;       // Shell command to execute
  name?: string;         // Display name
  description?: string;
  timeout?: number;      // Default: 60000ms
  source?: ConfigSource;
}

interface HookDefinition {
  matcher?: string;      // Regex to match tool/context names
  sequential?: boolean;  // Run hooks in sequence vs parallel
  hooks: HookConfig[];
}
```

### 3.3 Hook Input/Output Protocol

Hooks receive JSON on stdin, output JSON on stdout:

```typescript
// Base input (all events)
interface HookInput {
  session_id: string;
  transcript_path: string;
  cwd: string;
  hook_event_name: string;
  timestamp: string;
}

// BeforeTool specific
interface BeforeToolInput extends HookInput {
  tool_name: string;
  tool_input: Record<string, unknown>;
  mcp_context?: McpToolContext;  // Present for MCP tools
}

// Base output
interface HookOutput {
  continue?: boolean;          // false = STOP_EXECUTION
  stopReason?: string;
  suppressOutput?: boolean;
  systemMessage?: string;
  decision?: 'ask' | 'block' | 'deny' | 'approve' | 'allow';
  reason?: string;
  hookSpecificOutput?: Record<string, unknown>;
}
```

### 3.4 Exit Code Semantics

```
0 = Success (allow/approve)
1 = Non-blocking error (warn but continue)
2 = Blocking error (deny/block)
```

### 3.5 Hook Runner

```typescript
// hookRunner.ts
class HookRunner {
  async executeHook(hookConfig: HookConfig, eventName: HookEventName, input: HookInput): Promise<HookExecutionResult> {
    // Security: Block project hooks in untrusted folders
    if (hookConfig.source === ConfigSource.Project && !this.config.isTrustedFolder()) {
      return { success: false, error: new Error('Security: Blocked in untrusted folder') };
    }

    const child = spawn(shellConfig.executable, [...shellConfig.argsPrefix, command], {
      env: { ...sanitizedEnv, GEMINI_PROJECT_DIR: input.cwd },
      cwd: input.cwd,
      stdio: ['pipe', 'pipe', 'pipe'],
    });

    // Send input as JSON
    child.stdin.write(JSON.stringify(input));
    child.stdin.end();

    // Parse stdout as JSON output
    // ...
  }

  async executeHooksParallel(hooks: HookConfig[], eventName: HookEventName, input: HookInput): Promise<HookExecutionResult[]>;
  async executeHooksSequential(hooks: HookConfig[], eventName: HookEventName, input: HookInput): Promise<HookExecutionResult[]>;
}
```

### 3.6 Registry Source Priority

```typescript
// hookRegistry.ts
private getSourcePriority(source: ConfigSource): number {
  switch (source) {
    case ConfigSource.Project: return 1;     // Highest
    case ConfigSource.User: return 2;
    case ConfigSource.System: return 3;
    case ConfigSource.Extensions: return 4;  // Lowest
    default: return 999;
  }
}
```

### 3.7 Settings Configuration

```json
{
  "hooks": {
    "enabled": true,
    "disabled": ["hook-name-to-disable"],
    "BeforeTool": [
      {
        "matcher": "shell_execute",
        "sequential": true,
        "hooks": [
          {
            "type": "command",
            "name": "security-check",
            "command": "python ~/.gemini/hooks/security.py"
          }
        ]
      }
    ]
  }
}
```

---

## Part 4: Session Management (v0.15.0+)

### 4.1 Core Types

```typescript
// sessionUtils.ts
interface SessionInfo {
  id: string;              // UUID
  file: string;            // Filename without .json
  fileName: string;        // Full filename
  startTime: string;       // ISO timestamp
  lastUpdated: string;     // ISO timestamp
  messageCount: number;
  displayName: string;     // Summary or first message
  firstUserMessage: string;
  isCurrentSession: boolean;
  index: number;           // 1-based display index
  summary?: string;        // AI-generated summary
  fullContent?: string;    // For search
  matchSnippets?: TextMatch[];  // Search results
}

interface SessionSelectionResult {
  sessionPath: string;
  sessionData: ConversationRecord;
  displayInfo: string;
}

type SessionErrorCode = 'NO_SESSIONS_FOUND' | 'INVALID_SESSION_IDENTIFIER';
```

### 4.2 Session Selector

```typescript
// sessionUtils.ts
class SessionSelector {
  constructor(private config: Config) {}

  async listSessions(): Promise<SessionInfo[]> {
    const chatsDir = path.join(this.config.storage.getProjectTempDir(), 'chats');
    return getSessionFiles(chatsDir, this.config.getSessionId());
  }

  async findSession(identifier: string): Promise<SessionInfo> {
    const sessions = await this.listSessions();

    // Try UUID first
    const byUuid = sessions.find(s => s.id === identifier);
    if (byUuid) return byUuid;

    // Try numeric index (1-based)
    const index = parseInt(identifier, 10);
    if (!isNaN(index) && index > 0 && index <= sessions.length) {
      return sessions[index - 1];
    }

    throw SessionError.invalidSessionIdentifier(identifier);
  }

  async resolveSession(resumeArg: string): Promise<SessionSelectionResult> {
    if (resumeArg === 'latest') {
      const sessions = await this.listSessions();
      return this.selectSession(sessions[sessions.length - 1]);
    }
    return this.selectSession(await this.findSession(resumeArg));
  }
}
```

### 4.3 Session Browser Hook (React)

```typescript
// useSessionBrowser.ts
const useSessionBrowser = (config: Config, onLoadHistory: Function) => {
  const [isSessionBrowserOpen, setIsSessionBrowserOpen] = useState(false);

  return {
    isSessionBrowserOpen,
    openSessionBrowser: useCallback(() => setIsSessionBrowserOpen(true), []),
    closeSessionBrowser: useCallback(() => setIsSessionBrowserOpen(false), []),

    handleResumeSession: useCallback(async (session: SessionInfo) => {
      const conversation = JSON.parse(await fs.readFile(sessionPath, 'utf8'));
      config.setSessionId(conversation.sessionId);

      const historyData = convertSessionToHistoryFormats(conversation.messages);
      onLoadHistory(historyData.uiHistory, historyData.clientHistory, { conversation, filePath });
      setIsSessionBrowserOpen(false);
    }, [config, onLoadHistory]),

    handleDeleteSession: useCallback((session: SessionInfo) => {
      config.getGeminiClient()?.getChatRecordingService()?.deleteSession(session.file);
    }, [config]),
  };
};
```

### 4.4 History Conversion

```typescript
// Converts stored messages to UI and client formats
function convertSessionToHistoryFormats(messages: ConversationRecord['messages']): {
  uiHistory: HistoryItemWithoutId[];
  clientHistory: Array<{ role: 'user' | 'model'; parts: Part[] }>;
} {
  // Map message types
  for (const msg of messages) {
    // UI history: USER, GEMINI, INFO, ERROR, WARNING, tool_group
    // Client history: user/model roles with parts

    // Handle tool calls specially
    if (msg.toolCalls?.length > 0) {
      // Add function calls to model message
      // Add function responses to user message
    }
  }
}
```

### 4.5 CLI Commands

| Command | Purpose |
|---------|---------|
| `--list-sessions` | List all sessions |
| `--resume latest` | Resume most recent |
| `--resume <uuid>` | Resume by UUID |
| `--resume <n>` | Resume by index |
| `--delete-session <n>` | Delete session |

### 4.6 Storage Format

```
~/.gemini/projects/<project-hash>/chats/
├── session-1736000000000-abc12345.json
├── session-1736100000000-def67890.json
└── session-1736200000000-ghi13579.json
```

```json
{
  "sessionId": "abc12345-1234-5678-9abc-def012345678",
  "startTime": "2025-01-01T00:00:00.000Z",
  "lastUpdated": "2025-01-01T01:00:00.000Z",
  "summary": "Implemented user authentication feature",
  "messages": [
    { "type": "user", "content": "Help me add login" },
    { "type": "gemini", "content": "...", "toolCalls": [...] }
  ]
}
```

---

## Part 5: Package Dependencies

### 5.1 Core Dependencies

```json
{
  "@google/genai": "^0.x.x",
  "zod": "^3.x.x",
  "zod-to-json-schema": "^3.x.x",
  "glob": "^10.x.x",
  "js-yaml": "^4.x.x"
}
```

### 5.2 CLI Dependencies

```json
{
  "react": "^18.x.x",
  "ink": "^4.x.x"
}
```

---

## Part 6: File Structure Reference

```
packages/core/src/
├── agents/
│   ├── types.ts              # AgentDefinition, InputConfig, etc.
│   ├── registry.ts           # AgentRegistry
│   ├── local-executor.ts     # LocalAgentExecutor
│   ├── local-invocation.ts   # Invocation wrapper
│   ├── remote-invocation.ts  # A2A remote agent support
│   ├── a2a-client-manager.ts # A2A protocol client
│   ├── codebase-investigator.ts
│   ├── cli-help-agent.ts
│   └── generalist-agent.ts
├── hooks/
│   ├── types.ts              # HookEventName, HookConfig, etc.
│   ├── hookSystem.ts         # Main orchestrator
│   ├── hookRegistry.ts       # Load/validate hooks
│   ├── hookRunner.ts         # Execute command hooks
│   ├── hookPlanner.ts        # Schedule by matcher
│   ├── hookAggregator.ts     # Combine results
│   ├── hookTranslator.ts     # SDK ↔ Hook format
│   └── trustedHooks.ts       # Folder trust management
├── skills/
│   ├── skillLoader.ts        # SKILL.md discovery/parsing
│   └── skillManager.ts       # Activation, precedence
└── sessions/                 # (in packages/cli)
    ├── sessionUtils.ts       # SessionSelector, SessionInfo
    ├── sessions.ts           # CLI commands
    └── useSessionBrowser.ts  # React hook for UI
```

---

## Part 7: Migration Notes from v0.14.0

### Breaking Changes

1. **Settings Rename:** All `disable*` → `enable*` (inverted)
2. **MessageBus Required:** Tool/Agent constructors require MessageBus injection
3. **Hook Events Added:** `BeforeToolSelection`, `AfterModel`
4. **Agent Tool:** `complete_task` is now mandatory termination

### New Dependencies

- `zod` for agent output validation
- `zod-to-json-schema` for schema generation
- `glob` for skill discovery

### Config Schema Additions

```json
{
  "skills": {
    "enabled": true,
    "disabled": []
  },
  "agents": {
    "enabled": ["codebase-investigator", "generalist"],
    "disabled": []
  },
  "hooks": {
    "enabled": true,
    "BeforeToolSelection": [...]
  }
}
```
