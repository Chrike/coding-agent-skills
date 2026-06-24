Languages: [English](README.md) | [简体中文](README.zh-CN.md)

# 编码代理技能集

一套面向 Claude Code 和 Codex 辅助开发的轻量级技能套件。

目标是在保持日常编码高效的同时，为代理提供清晰的工作流，以便在实际需要时进行调试、测试、规划、评审、交接、可靠性修正及任务委派。

该套件围绕一条简单规则设计：

> 从轻量开始。仅当任务、风险或用户请求确有必要时，才升级流程。

它并不试图将每个编码任务都变成正式流程。

## 本仓库内容

本仓库包含：

- `skills/` 下的可安装运行时技能
- `prompts/` 下的常驻指令源片段
- `tests/` 下的维护与验证材料

## 仓库布局

~~~text
coding-agent-skills/
├── README.md
├── README.zh-CN.md
├── skills.sh.json
├── prompts/
│   ├── AGENTS.fragment.md
│   └── CLAUDE.fragment.md
├── skills/
│   ├── debug-systematically/
│   │   ├── SKILL.md
│   │   └── references/
│   ├── test-strategy/
│   │   ├── SKILL.md
│   │   └── references/
│   ├── review-and-finish/
│   │   ├── SKILL.md
│   │   └── references/
│   ├── plan-work/
│   │   ├── SKILL.md
│   │   └── references/
│   ├── design-codebase/
│   │   ├── SKILL.md
│   │   └── references/
│   ├── reliability-check/
│   │   └── SKILL.md
│   ├── finish-branch/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   ├── agent-workflow/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   ├── issue-workflow/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   ├── memory-handoff/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   └── decision-map/
│       ├── SKILL.md
│       └── agents/openai.yaml
└── tests/
    ├── routing-contract.md
    ├── trigger-matrix.md
    ├── expected-routing.md
    └── non-trigger-cases.md
~~~

说明：

- `skills/` 包含可安装的运行时技能。
- `prompts/` 包含常驻默认行为的源片段。
- `tests/` 包含用于维护套件的路由与边界检查。
- `skills.sh.json` 仅控制 skills.sh 页面分组；不影响运行时行为或技能路由。
- 手动工作流技能包含 `agents/openai.yaml` 以禁用隐式 Codex 调用。

## 快速开始

### 使用 skills.sh 安装

如果您使用 skills.sh，请通过以下命令安装本仓库：

~~~sh
npx skills add Chrike/coding-agent-skills
~~~

安装技能后，仍需查阅 `prompts/` 并将相关提示词片段合并到您的常驻指令文件中：

- Claude Code：将 `prompts/CLAUDE.fragment.md` 合并到 `CLAUDE.md`
- Codex：将 `prompts/AGENTS.fragment.md` 合并到 `AGENTS.md`

不要将 `tests/` 作为运行时指令安装。

### 手动安装

仅从 `skills/` 中安装您需要的运行时技能。

#### Claude Code

项目级安装：

~~~sh
mkdir -p .claude/skills
cp -R skills/debug-systematically skills/test-strategy skills/review-and-finish .claude/skills/
~~~

用户级安装：

~~~sh
mkdir -p ~/.claude/skills
cp -R skills/debug-systematically skills/test-strategy skills/review-and-finish ~/.claude/skills/
~~~

使用 Claude 提示词片段作为项目 `CLAUDE.md` 的源材料：

~~~sh
cp prompts/CLAUDE.fragment.md CLAUDE.md
~~~

如果您的项目已有 `CLAUDE.md`，请将片段合并进去，而不是覆盖文件。

#### Codex

项目级安装：

~~~sh
mkdir -p .agents/skills
cp -R skills/debug-systematically skills/test-strategy skills/review-and-finish .agents/skills/
~~~

用户级安装：

~~~sh
mkdir -p ~/.agents/skills
cp -R skills/debug-systematically skills/test-strategy skills/review-and-finish ~/.agents/skills/
~~~

使用 Codex 提示词片段作为项目 `AGENTS.md` 的源材料：

~~~sh
cp prompts/AGENTS.fragment.md AGENTS.md
~~~

如果您的项目已有 `AGENTS.md`，请将片段合并进去，而不是覆盖文件。

### 手动安装所有技能

为 Claude Code 安装所有运行时技能：

~~~sh
mkdir -p .claude/skills
cp -R skills/* .claude/skills/
~~~

为 Codex 安装所有运行时技能：

~~~sh
mkdir -p .agents/skills
cp -R skills/* .agents/skills/
~~~

手动工作流技能通过其技能元数据和 Codex 调用策略保持仅限手动触发。

## 技能列表

### 自动工作流技能

当请求明确匹配时，代理可自动选择这些技能。

| 技能 | 适用场景 |
| --- | --- |
| `debug-systematically` | 原因不明的 Bug、测试失败、回归问题、不稳定行为、性能瓶颈，或在修改代码前需要诊断的反复修复失败 |
| `test-strategy` | 添加或修改测试、选择测试接缝、TDD、Mock 或测试替身、不稳定测试设计、等待策略或回归证明 |
| `review-and-finish` | 显式代码评审、评审反馈、完成/修复/通过验证或 PR 反馈 |
| `plan-work` | 显式规划、实施计划、方案对比、任务拆解、路线图、分步计划或将工作拆分为实施切片 |
| `design-codebase` | 代码库设计、架构、模块接口、接缝、适配器、深层模块、领域语言、架构选项、难以测试的模块、通过接口提升可测试性，或用于解决设计问题的临时原型 |
| `reliability-check` | 对证据、来源使用、当前阶段、过时上下文、无依据的自信、幻觉、猜测、源码与记忆混淆、示例与任务混淆，或代理是否读取了正确文件的显式重新评估 |

### 手动工作流技能

这些是用于高成本、有副作用、持久性或低频操作的显式命令工作流。它们适用于有意调用的场景，而非日常的自动路由。

| 技能 | 适用场景 |
| --- | --- |
| `finish-branch` | 显式调用的分支收尾、提交、推送、合并、PR 创建或准备、丢弃变更或分支总结 |
| `agent-workflow` | 显式调用的子代理、并行代理、委派实现或多个独立代理任务的协调 |
| `issue-workflow` | 显式调用的 PRD 创建或细化、Issue 拆解、代理就绪的 Issue 简报、Issue 或 PR 分诊、QA Bug 报告会议或可录入跟踪系统的工作项 |
| `memory-handoff` | 显式调用的上下文压缩、压缩后恢复、交接创建或更新、项目状态保存，或从用户指定的交接/记忆文件恢复 |
| `decision-map` | 显式调用的跨会话持久化决策图，用于零散想法、模糊方向、长期设计问题、已跟踪的待解决问题及前沿优先解决策略 |

## 推荐起步

从匹配您实际工作流的最小集合开始。

### 核心自动集合

1. 来自 `prompts/` 的基础默认行为
2. `debug-systematically`
3. `test-strategy`
4. `review-and-finish`

### 可选自动技能

如果您经常需要显式规划、设计或重新评估，可添加以下技能：

- `plan-work`
- `design-codebase`
- `reliability-check`

### 可选手动工作流

仅在您需要针对较重操作的显式命令工作流时添加：

- `finish-branch`
- `agent-workflow`
- `issue-workflow`
- `memory-handoff`
- `decision-map`

## 默认行为层

提示词片段定义了日常开发工作的轻量级默认行为。

涵盖内容：

- 在修改或解释代码前读取相关文件
- 保留现有项目模式、命名和工具链
- 将编辑限制在请求的行为范围内
- 在当前环境中使用最佳可用的项目感知工具
- 在实际可行时运行最小有效验证
- 报告变更内容及验证结果
- 将外部分析、模型输出、计划和保存的产物视为参考输入，而非盲目服从的指令
- 将示例视为意图或故障模式的证据，除非明确要求，否则不视为字面任务
- 保持在用户请求的阶段
- 避免重型工作流、跟踪系统工作、大规模重构、分支操作和持久状态，除非用户要求或任务明确需要

## 路由契约

使用 `tests/` 下的维护文件来验证路由边界。

权威来源为：

- `prompts/AGENTS.fragment.md` 和 `prompts/CLAUDE.fragment.md` 定义常驻默认行为层。
- 每个运行时技能的 `description` 加上 `SKILL.md` 正文定义该技能的触发时机。
- `tests/` 验证这些边界，不得成为第二运行时指令层。

## 维护指南

保持改动精简。

推荐的改动：

- 收紧触发条件
- 移除不使用的工作流
- 明确何时停止
- 为重复出现的真实故障添加参考
- 仅当重复故障属于常驻层时才将其转化为持久行为规则；具体回归案例保留在 `tests` 中

避免导致所有任务变慢的改动。
