Languages: [English](README.md) | [简体中文](README.zh-CN.md)

# 编码代理技能集

一套面向 Claude Code 辅助开发的轻量级技能套件。

目标是在保持日常编码高效的同时，为代理提供清晰的工作流，以便在实际需要时进行调试、测试、规划、评审、交接、可靠性修正及任务委派。

## 仓库内容

本仓库包含：

- 位于 `skills/` 下的运行时技能源码目录
- 位于 `prompts/` 下的常驻默认行为提示词源码
- 位于 `workflows/` 下的显式选择 saved-workflow 源码
- 位于 `tests/` 下的维护与验证材料

该套件围绕一条简单规则设计：

> 从轻量开始。仅当任务、风险或用户请求确有必要时，才升级流程。

它并不试图将每个编码任务都变成正式流程。

## 能力边界

本套件按运行时角色分层，而不是按某个能力最初来自哪里分层。

- `prompts/` 承载面向日常开发工作的常驻默认行为层。
- `skills/` 承载具名工作流边界，只有当请求明确需要时才应加载。
- `workflows/` 承载显式选择的 saved-workflow 源码，不是宿主发现目录，也不参与普通 skill 路由。
- 显式意图工作流应从清晰的自然语言意图路由，而不是要求用户记住 skill 名称后手动调用。
- 高风险副作用、持久化工件和破坏性动作，应在所属 skill 内部做保护，而不是再堆一层运行时路由。
- `tests/` 负责验证维护中的边界，不能变成第二套运行时指令层。
- 外部分析、审查记录、迁移说明及其他参考材料可以帮助维护判断，但除非用户明确指定它们是当前指令源，否则它们不应变成主动运行时指令。
- bundled `/code-review` 命令仍由宿主负责；不应在项目 review skill 中再建立一条重复的评审路径。
- 维护中的 prompt 是面向模型的指导，不是确定性 enforcement；如果某个动作必须可靠地阻止或要求确认，应使用宿主 permissions 或 `PreToolUse` hooks。

## 技能列表

### 自动工作流技能

当请求明确匹配时，代理可自动选择这些技能。

| 技能                   | 适用场景                                                     |
| ---------------------- | ------------------------------------------------------------ |
| `debug-systematically` | 原因不明的 Bug、不稳定行为、回归问题、性能瓶颈、反复修复失败 |
| `test-strategy`        | 测试设计、TDD、Mock、不稳定测试、回归覆盖，或非显而易见的测试层级/接缝/验收信号 |
| `review-and-finish`    | 代码评审、评审反馈、完成/修复/通过验证、PR 反馈，或行为风险高的完成变更的聚焦就绪证据 |
| `plan-work`            | 规划、方案对比、路线图、任务拆解、垂直切片，或实现请求中无法安全推断的方法/依赖/顺序/迁移/兼容性/范围决策 |
| `design-codebase`      | 架构、接缝、接口、适配器、领域语言、原型设计，或被非显而易见的架构/所有权/接口/依赖边界决策阻塞的实现 |
| `reliability-check`    | 针对幻觉、猜测、过时上下文、方向错误、无依据的自信、源码与记忆混淆、示例与任务混淆的显式重新评估 |
| `agent-workflow`       | 面向独立切片的协调式多代理拆分、证据、验证与集成方法         |

### 显式意图工作流技能

这些技能面向不属于日常编码流的请求，但仍应从清晰的自然语言意图路由，而不是要求用户先记住 skill 名称再手动调用。

| 技能                | 适用场景                                                     |
| ------------------- | ------------------------------------------------------------ |
| `finish-branch`     | 显式提交、推送、合并、PR 准备、丢弃变更、分支收尾            |
| `issue-workflow`    | PRD、Issue 草稿、可录入跟踪系统的工作项、跟踪系统发布/更新、分诊 |
| `memory-handoff`    | 上下文压缩、交接、检查点更新、状态恢复                       |
| `markdown-memory`   | 显式项目版本化、共享或可审阅的 Markdown lessons              |
| `skill-refactorer`  | prompt/skill 维护、迁移、过时脚手架清理                      |
| `decision-map`      | 跨会话持久化决策图                                           |

## 安装

仅安装 `skills/` 中实际需要的运行时技能目录。

在本仓库中，`skills/`、`prompts/` 与 `workflows/` 都是源码目录，而不是宿主运行时路径。

已确认的宿主落点：

- Claude Code 运行时技能：项目级 `.claude/skills/` 或用户级 `~/.claude/skills/`
- Claude Code saved workflows：项目级 `.claude/workflows/` 或用户级 `~/.claude/workflows/`

Saved workflow 采用显式选择：将审阅过的源码文件复制到一个明确选择的落点，再调用其已安装名称。它不替代 skill 路由，也不会因为任务长或文件多而自动激活。

将 `prompts/CLAUDE.fragment.md` 作为宿主常驻指令文件的维护源码。对 Claude Code，这意味着整理到 `CLAUDE.md` 体系。

将 `tests/` 保留为维护与验证材料，而不是运行时技能。
不要将 `tests/` 复制到 `.claude/`、`.agents/` 或其他运行时安装目录中。

### 推荐的宿主 skill 可见性配置

当完整安装本 skill suite，并以宿主多代理工作流作为主要执行载体时，建议在 Claude Code 的宿主本地设置中，将可能重叠的 bundled skills 设为仅用户可调用：

```json
{
  "skillOverrides": {
    "batch": "user-invocable-only",
    "code-review": "user-invocable-only",
    "simplify": "user-invocable-only",
    "loop": "user-invocable-only"
  }
}
```

`user-invocable-only` 会让 Claude 不再自动选择这些 skill，但仍保留在 `/` 菜单中供用户明确调用。保持 `/debug` 的宿主默认可见性：Claude Code 自身运行时问题继续走 bundled debug，项目产品行为调试继续走 `debug-systematically`。

这是完整 suite 的推荐宿主配置，不是对所有安装强制写入仓库的设置。

## 仓库分层

- `skills/` 存放本仓库中的运行时技能源码目录。
- `skills.sh.json` 只控制 skills.sh 页面分组展示，不影响运行时行为或 skill 路由。
- `prompts/` 存放宿主常驻默认行为文件的维护源码。
- `workflows/` 存放显式 saved-workflow 源码；调用前将审阅过的文件复制到 `.claude/workflows/` 或 `~/.claude/workflows/`。
- `tests/` 存放用于维护本套件的路由与边界检查。
- 外部参考 skill 仅作为比较输入，不属于 runtime 安装面，任何维护或运行时边界决策都应先完成评估。
- 维护运行时 prompt 时，原则上让每条规则只承载一个紧密相关的决策族；新行为应有对应的正向或负向回归案例；解释性文字不进入运行时层；Skill 已完整拥有的程序不在全局重复；删除内容应记录为合并、迁移到所属 Skill/维护文档，或无独立行为价值。这些是维护检查，不是运行时指令。
- 如果摘要说明与维护中的 prompt 文件或技能正文漂移，应更新摘要，而不是在 README 中再写一套规范。

## 能力地图

当前运行时表面的组织方式如下：

- `prompts/CLAUDE.fragment.md` 定义常驻默认行为层。
- `debug-systematically`、`test-strategy` 与 `review-and-finish` 覆盖核心编码执行工作流。
- `agent-workflow` 在存在真正独立切片时覆盖多代理编排方法。
- `workflows/` 存放面向有界、会话内程序化执行试点的显式 saved-workflow 源码；它不是普通 skill 路由层。
- `plan-work` 与 `design-codebase` 覆盖显式规划与架构决策，以及存在未解决、承重的规划或设计决策的实现请求。
- `reliability-check` 与 `memory-handoff` 负责纠偏式重新评估与恢复态连续性。
- `finish-branch`、`issue-workflow`、`markdown-memory`、`skill-refactorer` 与 `decision-map` 覆盖分支动作、持久化工件与维护类的显式意图请求。

## 推荐起步

从匹配您实际工作流的最小集合开始。

### 核心自动集合

1. 由 `prompts/CLAUDE.fragment.md` 组装到宿主常驻指令文件中的基础默认行为
2. `debug-systematically`
3. `test-strategy`
4. `review-and-finish`

### 可选自动技能

如果您经常需要显式规划、设计、重新评估或多代理编排，可添加以下技能：

- `plan-work`
- `design-codebase`
- `reliability-check`
- `agent-workflow`

### 可选显式意图工作流

如果您希望分支动作、持久化工件、维护或校准类工作可以通过自然语言路由，而不要求用户记住 skill 名称，可添加以下技能：

- `finish-branch`
- `issue-workflow`
- `memory-handoff`
- `markdown-memory`
- `skill-refactorer`
- `decision-map`

## 自定义

保持改动精简。

推荐的改动：

- 收紧触发条件
- 移除不使用的工作流
- 明确何时停止
- 为重复出现的真实故障添加参考
- 只有当重复故障确实属于常驻层时，才将其沉淀为稳定行为规则；具体回归案例应保留在 `tests/`

避免导致所有任务变慢的改动。
