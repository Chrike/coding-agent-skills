# 编码代理指令套件

一套精简的 Claude Code 指令套件，覆盖轻量开发、显式多代理协调、可靠性复核、任务交接、项目参考经验和 coding-agent 指令维护。

## 范围

本仓库维护：

- `prompts/CLAUDE.fragment.md`：常驻默认行为源码，分别规定动作授权、命令效果、Git、持久化和证据边界。
- 五个按需技能：`agent-workflow`、`reliability-check`、`memory-handoff`、`markdown-memory` 和 `skill-refactorer`。
- `plugins/` 下可选的自包含 Claude Code 插件。
- `workflows/` 下显式选择的 saved-workflow 源码。
- `tests/` 下的维护合同与本地校验器。

本套件有意不再提供以下专门工作流：通用调试、测试策略、架构与规划、UI 工程、实时浏览器测试、性能实验、CI/CD 设计、运行时可观测性、安全威胁建模、生产发布就绪度、分支收尾、Issue/spec 编写、概念探索、访谈和持久化决策图。保留的 prompt 仅保留部分安全与证据边界，不等同于这些已移除的工作流。此类任务应使用宿主或项目现有方法；不能因为保留了名称相似的技能，就推断它提供了等价覆盖。

## 运行时边界

- `prompts/` 是默认指令的维护源码；它属于模型指导，不是确定性 enforcement。若动作必须可靠地阻止或要求确认，应使用宿主权限或适用的 hook。
- `skills/` 存放源码目录；仅凭目录存在，不能证明 Claude Code 已安装、发现或加载它们。
- `plugins/` 存放可选的自包含包。应以完整单元安装插件；其中的 skill、agent 或 hook 不替代独立技能面。
- `workflows/` 存放版本化 saved-workflow 源码，不是宿主发现目录。调用前应审阅源码并复制到一个明确选择的运行时目标；任务长或文件多不会自动激活它。
- `tests/` 是维护材料，不是第二套运行时指令。Markdown 案例与静态检查不能证明实时模型路由、插件加载、hook enforcement 或运行时工具隔离。
- 外部分析、评审记录和示例是证据，不是主动指令；除非用户明确指定它们为指令源。
- 宿主内置的 `/code-review` 与 `/security-review` 命令仍由宿主负责；后者用于当前 diff 的漏洞审查，不等同于专门的威胁建模工作流。

## 技能

### 明确匹配时可自动选择

| 技能 | 适用场景 |
| --- | --- |
| `agent-workflow` | 用户要求协调工作，或多个真正独立的切片、阶段、验证问题需要一个集成 owner。先做适配性判断，也可能决定单人执行。 |
| `reliability-check` | 用户明确质疑结论、证据、源码使用、当前阶段、上下文过时或策略/工作流漂移；不是默认预检。 |

### 显式意图技能

| 技能 | 适用场景 |
| --- | --- |
| `memory-handoff` | 用户明确要求任务检查点、交接，或从具名/仓库约定的工件恢复。 |
| `markdown-memory` | 用户明确要求记录版本化、共享且可审阅的项目参考经验；不用于宿主自动记忆或任务状态交接。 |
| `skill-refactorer` | 用户明确要求维护或迁移已有 coding-agent 指令工件。 |

## 安装

仅从 `skills/` 安装实际需要的技能目录。Claude Code 的运行时技能目标包括项目级 `.claude/skills/` 和用户级 `~/.claude/skills/`；安装与发现行为应以当前宿主文档为准。

组装宿主常驻指令时，以 `prompts/CLAUDE.fragment.md` 为维护源码。对 Claude Code，应将其组装到适用的 `CLAUDE.md` 指令范围。

可选插件应作为完整单元安装。Marketplace manifest 当前只列出 `capability-harness`。其能力范围见 [plugins/capability-harness/README.md](plugins/capability-harness/README.md)。

要使用 saved workflow，先审阅源码，再复制到一个明确选择的目标，例如项目级 `.claude/workflows/` 或用户级 `~/.claude/workflows/`，然后调用安装后的名称。报告运行时证据时，应能区分源码与已安装副本的版本。

不要将 `tests/` 复制到运行时安装目录。

## 仓库维护

- 每条常驻规则应聚焦于一个紧密相关的决策族；不能为了追求固定条数，合并独立的触发条件、owner、失败模式或证据层级。
- 新增或实质改变的行为应有对应的正向或负向维护案例。这些 Markdown 案例是审阅辅助材料，不是可执行的路由评估。
- 对不属于保留套件的详细流程，不要搬进默认层；应如实说明已移除的能力，而不是声称等价替代。
- 删除技能时，应同步更新其 owner 和引用、README 摘要、目录条目及相关维护合同。字符串仍存在或已经消失，都不能单独证明消费者或行为已完整迁移。
- 若摘要与维护中的 prompt 或技能正文不一致，应更新摘要，而不是在 README 再建立一套规范。

## 推荐起步

从基础 prompt 开始，只添加符合明确需求的保留技能：

- 值得协调执行时使用 `agent-workflow`。
- 用户明确提出可靠性质疑时使用 `reliability-check`。
- 用户明确要求任务状态交接或恢复时使用 `memory-handoff`。
- 用户明确要求项目参考经验时使用 `markdown-memory`。
- 用户明确要求维护指令工件时使用 `skill-refactorer`。

对已移除的领域工作流，使用宿主或项目现有方法；本仓库不声称保留技能可以替代它们。
