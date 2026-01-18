# Implementation Plan: Selective Per-Tool MCP Isolation

**Goal:** Route specific MCP tools to a dedicated subagent for context isolation, configurable per-server and per-tool.

---

## 1. Config Schema Extension

Extend MCP server config to specify which tools run in isolated subagent:

```typescript
// In settings.json or .gemini/settings.json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["@my/db-mcp"],
      "isolatedTools": ["query", "execute", "schema"]  // NEW
    },
    "filesystem": {
      "command": "npx",
      "args": ["@anthropic/fs-mcp"]
      // No isolation - runs in main context
    },
    "external-api": {
      "command": "npx",
      "args": ["@my/api-mcp"],
      "isolated": true  // NEW - isolate ALL tools from this server
    }
  }
}
```

**Config precedence:**
- `isolated: true` → all tools from server run in subagent
- `isolatedTools: [...]` → only listed tools run in subagent
- Neither → tools run in main agent context (default)

---

## 2. Files to Modify

### A. Config Types
**File:** `packages/core/src/config/types.ts` (or equivalent)

```typescript
interface McpServerConfig {
  command?: string;
  args?: string[];
  url?: string;
  // ... existing fields

  // NEW: Isolation config
  isolated?: boolean;           // Isolate all tools
  isolatedTools?: string[];     // Isolate specific tools only
}
```

### B. MCP Tool Context Extension
**File:** `packages/core/src/hooks/types.ts` (lines 375-387)

Already has what we need:
```typescript
interface McpToolContext {
  server_name: string;   // ✓ Can lookup server config
  tool_name: string;     // ✓ Can check against isolatedTools
  command?: string;
  // ...
}
```

### C. Tool Execution Interception
**File:** `packages/core/src/core/nonInteractiveToolExecutor.ts`

This is where `executeToolCall()` lives - the function called at `local-executor.ts:926`.

**Add isolation check before execution:**

```typescript
export async function executeToolCall(
  context: Config,
  requestInfo: ToolCallRequestInfo,
  signal: AbortSignal,
): Promise<ToolCallResult> {
  const toolName = requestInfo.name;

  // Check if this is an MCP tool that should be isolated
  if (toolName.startsWith('mcp__')) {
    const [_, serverName, mcpToolName] = toolName.split('__');
    const serverConfig = context.getMcpServerConfig(serverName);

    if (shouldIsolateTool(serverConfig, mcpToolName)) {
      return executeInIsolatedSubagent(context, requestInfo, signal);
    }
  }

  // Normal execution path
  return executeToolCallDirect(context, requestInfo, signal);
}

function shouldIsolateTool(
  config: McpServerConfig | undefined,
  toolName: string
): boolean {
  if (!config) return false;
  if (config.isolated) return true;
  if (config.isolatedTools?.includes(toolName)) return true;
  return false;
}
```

### D. Isolated Subagent Definition
**File:** `packages/core/src/agents/builtin/mcp-executor.ts` (NEW)

```typescript
import { LocalAgentDefinition } from '../types.js';
import { z } from 'zod';

export const mcpExecutorAgent: LocalAgentDefinition<typeof outputSchema> = {
  name: 'mcp-executor',
  displayName: 'MCP Tool Executor',
  description: 'Executes MCP tools in isolated context',

  inputConfig: {
    schema: z.object({
      serverName: z.string(),
      toolName: z.string(),
      toolInput: z.record(z.unknown()),
    }),
  },

  outputConfig: {
    outputName: 'result',
    schema: z.object({
      success: z.boolean(),
      output: z.unknown(),
      error: z.string().optional(),
    }),
  },

  promptConfig: {
    systemPrompt: `You are a tool executor. Execute the requested MCP tool and return the result.
Do not interpret or process the result - just return it exactly as received.
Call complete_task immediately after executing the tool.`,
    query: 'Execute tool {{toolName}} from server {{serverName}} with input: {{toolInput}}',
  },

  modelConfig: {
    model: 'gemini-2.0-flash',  // Fast model for simple execution
  },

  runConfig: {
    maxTurns: 3,        // Tool call + complete_task + retry
    maxTimeMinutes: 2,
  },

  toolConfig: {
    tools: [],  // Dynamically populated with only the target MCP tool
  },
};
```

### E. Register Builtin Agent
**File:** `packages/core/src/agents/registry.ts`

```typescript
import { mcpExecutorAgent } from './builtin/mcp-executor.js';

// In BUILTIN_AGENTS array:
const BUILTIN_AGENTS = [
  codebaseInvestigatorAgent,
  cliHelpAgent,
  generalistAgent,
  mcpExecutorAgent,  // NEW
];
```

### F. Subagent Invocation Helper
**File:** `packages/core/src/core/nonInteractiveToolExecutor.ts`

```typescript
async function executeInIsolatedSubagent(
  context: Config,
  requestInfo: ToolCallRequestInfo,
  signal: AbortSignal,
): Promise<ToolCallResult> {
  const [_, serverName, mcpToolName] = requestInfo.name.split('__');

  // Get the MCP executor agent definition
  const agentRegistry = context.getAgentRegistry();
  const agentDef = agentRegistry.getAgent('mcp-executor');

  if (!agentDef || agentDef.kind !== 'local') {
    throw new Error('mcp-executor agent not found');
  }

  // Clone and inject only the specific MCP tool
  const isolatedDef = {
    ...agentDef,
    toolConfig: {
      tools: [requestInfo.name],  // Only this MCP tool
    },
  };

  // Create and run executor
  const executor = await LocalAgentExecutor.create(isolatedDef, context);

  const result = await executor.run({
    serverName,
    toolName: mcpToolName,
    toolInput: JSON.stringify(requestInfo.args),
  }, signal);

  // Convert agent output back to tool result format
  return {
    response: {
      responseParts: [{
        functionResponse: {
          name: requestInfo.name,
          id: requestInfo.callId,
          response: JSON.parse(result.result),
        },
      }],
      resultDisplay: result.result,
    },
  };
}
```

---

## 3. Execution Flow

```
┌─────────────────────────────────────────────────────────────┐
│  Main Agent calls: mcp__database__query                     │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  executeToolCall()                                          │
│  ├─ Detect MCP tool (starts with mcp__)                     │
│  ├─ Parse: server=database, tool=query                      │
│  └─ Check: serverConfig.isolatedTools.includes('query')     │
└──────────────────────────┬──────────────────────────────────┘
                           │ YES - isolated
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  executeInIsolatedSubagent()                                │
│  ├─ Get mcp-executor agent definition                       │
│  ├─ Inject ONLY mcp__database__query tool                   │
│  ├─ Create LocalAgentExecutor                               │
│  └─ Run with {serverName, toolName, toolInput}              │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  MCP Executor Subagent (isolated context)                   │
│  ├─ Fresh history (no main agent context)                   │
│  ├─ Only has mcp__database__query tool                      │
│  ├─ Executes tool                                           │
│  └─ Returns via complete_task                               │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  Result returned to main agent                              │
│  └─ Main agent sees tool result, NOT subagent execution     │
└─────────────────────────────────────────────────────────────┘
```

---

## 4. Key Benefits

| Aspect | Main Context | Isolated Subagent |
|--------|--------------|-------------------|
| History | Full conversation | Fresh/empty |
| Tools available | All tools | Only target MCP tool |
| Token usage | Accumulates (50k+) | Bounded (~2k per call) |
| Context pollution | Yes | No |
| Token cost | High (pays for full history) | Low (minimal context) |
| Latency | 1 model call | 2-3 model calls |

**Net effect:** Subagent isolation *reduces* token costs significantly for long conversations, at the expense of slightly higher latency per tool call.

---

## 5. Implementation Order

### Phase 1: Config (Minimal)
1. Add `isolated` and `isolatedTools` to MCP server config type
2. Update config loader to parse new fields

### Phase 2: Detection
3. Add `shouldIsolateTool()` helper
4. Add detection logic in `executeToolCall()`

### Phase 3: Subagent
5. Create `mcp-executor` agent definition
6. Register in `BUILTIN_AGENTS`
7. Implement `executeInIsolatedSubagent()`

### Phase 4: Testing
8. Test with sample MCP server
9. Verify context isolation
10. Benchmark overhead

---

## 6. Alternative: Hook-Based (No Code Changes)

If you want to avoid fork code changes entirely, use BeforeTool hook:

**`~/.gemini/hooks/mcp-isolator.py`**
```python
#!/usr/bin/env python3
import sys, json

ISOLATED = {
    "database": ["query", "execute"],
    "external-api": "*",  # all tools
}

data = json.load(sys.stdin)
tool = data.get("tool_name", "")
mcp_ctx = data.get("mcp_context")

if mcp_ctx:
    server = mcp_ctx.get("server_name")
    mcp_tool = mcp_ctx.get("tool_name")

    rules = ISOLATED.get(server, [])
    if rules == "*" or mcp_tool in rules:
        print(json.dumps({
            "decision": "block",
            "reason": f"Use delegate_to_agent('mcp-executor', {{server: '{server}', tool: '{mcp_tool}', input: <args>}})",
            "continue": True
        }))
        sys.exit(2)

print(json.dumps({"continue": True}))
sys.exit(0)
```

**Tradeoff:** Hook approach requires LLM to interpret the block message and manually call delegate_to_agent. The code approach is automatic and transparent.

---

## 7. Files Summary

| File | Change Type | Purpose |
|------|-------------|---------|
| `config/types.ts` | Modify | Add isolation fields to McpServerConfig |
| `hooks/types.ts` | None | Already has McpToolContext |
| `core/nonInteractiveToolExecutor.ts` | Modify | Add isolation check + subagent dispatch |
| `agents/builtin/mcp-executor.ts` | New | Dedicated subagent definition |
| `agents/registry.ts` | Modify | Register mcp-executor |

**Estimated: ~200 lines of new code**
