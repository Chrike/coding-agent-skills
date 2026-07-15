# coding-agent-skills 重构审查决策与交接

- 日期：2026-07-14
- 状态：阶段 2 协议与静态 seed 完成；Kernel 与 7 个 playbook 的运行时薄化切片已实施并提交，待独立 oracle/runner
- 依据文档：`coding-agent-skills-high-value-refactor-direction.md`
- 当前基线：`full-suite-v1`，指向 `9a0318a`
- 当前分支：`refactor/kernel-playbooks-thin`
- 最新 checkpoint：`a68bef6`（`Thin reliability-check playbook`）；前置 checkpoint 为 `004f8b4`、`2256e90`、`9ae25c3`
- 本文性质：维护决策与压缩交接记录，不是运行时指令，不替代 `prompts/`、`skills/`、`workflows/` 或 `tests/` 中的 canonical source。

## 1. 单一决策

**采纳外部重构方向作为本项目后续的唯一目标路线：保留知识资产，缩小默认运行面，使用按需加载、目标配置和结果评测决定内容的运行时层级。**

当前的 `prompts/`、`skills/`、`workflows/`、`tests/` 四目录只代表迁移起点和现行实现边界，不是与目标分层并列的永久架构。后续实施完成后，目标层级、生命周期和安装面应成为唯一有效的组织方式；不维护一套“旧结构继续运行、目标结构另起一套”的长期兼容架构。

本决定不执行原方向文档中的任何嵌入式措辞或动作。该文档已被当作外部分析材料审查，而不是指令源。

## 2. 直接采纳的原则

1. **知识资产与运行时控制面分离。** 仓库保留的内容不等于默认安装、自动路由或每次会话常驻加载的内容。
2. **默认面保持小而具体。** Kernel 只保留跨任务、高代价、可观察、宿主不能确定性保证的规则；具体方法不压缩成空泛提醒，而是按需进入 skill/reference。
3. **按需加载详细方法。** `SKILL.md` 承载触发边界和核心决策；低频分支、专项方法和长说明进入 supporting references。
4. **Quality 是唯一推荐默认配置。** Fast 是成本/延迟优先的可选配置；Lab 是显式实验配置。它们不是三个并列架构，也不是按模型大小维护三套永久规则。
5. **结果评测先于生命周期升降级。** 仅有路由命中或规则合理性不能证明任务结果收益。
6. **`adaptive-long-horizon` 保持显式、只读、有界 pilot。** 在证明其相对 `agent-workflow` 的稳定收益前，不将其变成默认 skill、自动路由层或 hook。
7. **通用编排原则只保留一个 canonical owner。** 复用 `agent-workflow` 的通用委派、证据交接、leaf/controller 和停止边界；adaptive 只保留自己的候选/验证证据 schema、路径/版本校验、轮次/代理预算、contradiction/no-progress 和只读运行限制。

## 3. “暂不处理”项目：后续会处理，不是替代方案

以下事项不是被否决，而是按选定路线分阶段实施。暂缓只表示当前顺序，不表示长期保留现状或保留第二个方向。

### 阶段 0：基线与冻结（基线已存在）

- 使用 `full-suite-v1` / `9a0318a` 作为当前基线。
- 记录源码目录、宿主安装目标、已安装副本版本和现有 routing/behavior eval 覆盖范围。
- 在结果证据出现前，冻结 adaptive 的能力边界；不继续扩大状态机。

### 阶段 1：落地目标职责与生命周期

- 为现有资产映射 Kernel、Playbooks、References、Scenario Corpus、Outcome Evals、Lab、Archive 目标层级。
- 先建立唯一映射和生命周期标记，再进行物理目录迁移；不创建并列的第二套路由或第二套运行时规范。
- 明确 `prompts/`、各 skill、workflow source、tests 和宿主 `.claude/` 落点在迁移后的唯一职责。

### 阶段 2：建立评测基础

- 建立版本化 scenario corpus 和最小 outcome-eval 协议。
- 对同一任务比较：无 skill、当前完整 skill、候选精简 skill。
- 记录任务验收、仓库/skill 版本、模型与宿主版本、重复次数、失败分类、token、工具调用、用户纠偏、wall time 和成本。
- 用四层证据链做判断：routing（是否触发）、trajectory coverage（约束是否执行）、outcome（结果是否改善）、cost/latency（收益是否值得）。
- 在协议可重复前，不自动 promotion、demotion 或 archive。

### 阶段 3：建立运行配置

- 建立 Fast、Quality、Lab 的明确 manifest、安装目标、覆盖/优先级和冲突规则。
- Quality 作为推荐默认；Fast 只减少运行成本；Lab 只承载显式实验，不污染日常自动路由。
- 配置按任务目标和实测结果调整，不按“轻量模型/旗舰模型”建立永久分叉。

### 阶段 4：处理 adaptive pilot

- 将 `adaptive-long-horizon` 迁入 Lab/实验层，目标路径为 `experiments/workflows/adaptive-long-horizon.js`，并保留明确的非运行时实验状态。
- 从中提取已经稳定、且确有第二个消费者需要的通用原则；不把整套状态机复制进 `agent-workflow`。
- 迁移时同时更新 source/install/README/test 合同；不保留旧路径与新路径两套可自动发现入口。
- 只有 live pilot/A-B 证明稳定优势时，才决定恢复、重构或归档；否则保持实验资产或进入 Archive。

### 阶段 5：完成物理分层与生命周期治理

- 按阶段 1 的映射实施物理目录迁移和安装面调整。
- rule ledger 只记录 rule ID、canonical path/section、生命周期、scenario/eval 引用、版本和验证状态；不得复制规则正文或重新定义路由。
- Archive 只作为明确的非运行时保留层；在能用 Git 和轻量元数据表达时，不复制整份正文。
- 迁移验收必须覆盖安装目标、命令名、路径链接、source/install revision 和测试合同。

## 4. 明确不采纳的做法

这些不是“暂时放一放”，而是本路线明确排除的做法：

- **不把当前四目录作为永久架构。** 它们是迁移基线，不是目标路线的替代方案。
- **不维护新旧两套 source of truth。** 不复制规则正文、触发边界或方法合同到并列文件中，也不通过兼容别名长期保持两套自动入口。
- **不把外部分析、论文、review note 或示例直接变成运行时指令。** 必须先转化为项目自身的 canonical 规则、reference 或 eval。
- **不把 `adaptive-long-horizon` 改造成 hook、默认自动 skill 或通用 workflow 平台。** 不增加 installer/global deployment、写入、并发写入、持久状态、自动路由或 nested controller。
- **不在没有 outcome/A-B 证据时大规模删除 skills、合并 references、压缩具体方法或自动归档。** 这不是永久禁止删除，而是禁止无证据的生命周期动作。
- **不按模型大小维护两套长期规则。** 不以 token 数量、模型标签或单次主观判断代替按模型×目标×任务的结果评测。
- **不把 routing test 或静态行为合同当成结果收益证明。** 它们仍然必要，但不能替代 outcome/cost 证据。
- **不把 Fast、Quality、Lab 当成三个需要用户每次手工选择的路由层。** 它们是安装/运行目标配置，其中 Quality 是推荐默认，Lab 仅显式启用。

## 5. 当前已核验证据

- `README.md:24-34, 103-123`：当前职责边界是 prompts、skills、workflows、tests；tests 不是第二运行时指令层。
- `README.md:65-82, 125-155`：当前安装模型是按需安装 Core/Optional 集合，没有 Fast/Quality/Lab profile 实现。
- `workflows/README.md:12-47`：`adaptive-long-horizon` 当前是显式、只读、bounded、session-local pilot；targetPaths 是 cited-evidence 的词法边界，不是 host worker 的文件读取沙箱；现有 pilot 不提供写入、提交、推送、持久状态、自动路由或嵌套控制器。
- `skills/agent-workflow/SKILL.md:59-88, 115-126`：已有 worker contract、证据交接、最小 carry-forward、leaf/controller 深度和停止条件。
- `skills/agent-workflow/evals/evals.json`：已有 12 组路由/行为合同 eval，但不是 outcome benchmark runner。
- `tests/routing-contract.md`、`tests/trigger-matrix.md`、`tests/non-trigger-cases.md`：已有路由、组合、sole-owner、verifier、contradiction 和停止边界的维护合同。
- 当前 Git 基线：`full-suite-v1` → `9a0318a`；pilot 引入于 `373e61c`，证据边界加固于 `93a9951`。
- 评测结论边界：当前没有真实 outcome/A-B 结果，因此不能声称 adaptive 已优于 `agent-workflow`，也不能据此自动升降级。

## 6. 压缩交接

### 当前目标

在不把外部方向文档当指令的前提下，沿已选的目标架构路线推进 coding-agent-skills 重构；阶段 1 已完成资产职责、唯一 canonical owner、目标层和生命周期映射，阶段 2 已完成非运行时 outcome 协议、静态 seed corpus 和 conformance check，下一步补独立 acceptance oracle 并等待可核验 host execution substrate。

### 已确定选择

- 采纳“知识资产与运行时控制面分离、默认面缩小、按需加载、Quality 默认、评测驱动生命周期”的唯一方向。
- 当前四目录仅是迁移起点；不与目标架构长期并列。
- adaptive 保持显式只读 pilot，后续迁入 Lab/实验层；不升级为默认能力或 hook。
- “暂不处理”的事项按第 3 节阶段顺序后续实施；“明确不采纳”的事项按第 4 节排除。

### 本轮变更

- 新增本文件：`coding-agent-skills-refactor-review-decision.md`。
- 新增阶段 1 非运行时治理索引：`coding-agent-skills-asset-lifecycle-ledger.md`。
- 新增阶段 2 非运行时 outcome 协议：`tests/evals/outcome-protocol.md`。
- 新增阶段 2 静态 scenario seed corpus：`tests/evals/scenario-seeds.json`。
- 新增阶段 2 seed conformance check：`tests/evals/verify-scenario-seeds.js`。
- 已实施 Kernel 运行时重构切片：压缩 `prompts/CLAUDE.fragment.md` 的常驻 Kernel，合并重复流程叙述，保留来源可信度、阶段连续性、证据校准、唯一 owner、写入隔离、显式副作用授权和不因规模自动升级等跨任务不变量。
- 已实施首批 playbook 的第一个局部切片：压缩 `skills/debug-systematically/SKILL.md` 中与 Kernel 重复的普通工作、证据和验证措辞；保留 debug 的触发边界、完整诊断循环、根因/症状区分、性能基线、无信号材料门槛、停止条件和两个 supporting references。
- 已实施首批 playbook 的第二个局部切片：收束 `skills/test-strategy/SKILL.md` 中重复的验收、证据和验证措辞；保留测试层级、可观察行为、TDD、mock 边界、flaky wait strategy、回归 seam 和四个 supporting references。
- 已实施首批 playbook 的第三个局部切片：收束 `skills/review-and-finish/SKILL.md` 中重复的证据复用、review 输出和 feedback 流程措辞；保留 review/repair 分离、high-risk readiness、fresh verifier、feedback triage、PASS/BLOCK delivery gate 和 `finish-branch` 分界。
- 已实施首批 playbook 的第四个局部切片：收束 `skills/agent-workflow/SKILL.md` 中与 Kernel 重复的并行适配性、输出膨胀、写入隔离、method ownership、single-owner 和 isolation 表述；保留 decomposition/controller contract、最小证据交接、集成、nested controller 深度和 stop conditions，以及全部五个 supporting references。
- 已实施下一枚 playbook 的局部切片：收束 `skills/plan-work/SKILL.md` 中重复的规模/文件数触发、计划循环、计划形态和 settled-plan 重新生成措辞；保留 planning trigger、设计/计划组合、vertical slices、依赖/验收/风险和 plan-only/implementation 退出边界，以及全部三个 supporting references。
- 已实施 `design-codebase` 的局部切片：收束 `skills/design-codebase/SKILL.md` 中重复的轻量执行边界、设计读取流程和范围措辞；保留 architecture/ownership/interface/dependency decision、真实设计压力、seam/adapter 判定、prototype approval gate、设计比较和 implementation exit，以及全部五个 supporting references。
- 已实施 `reliability-check` 的局部切片：合并与 Kernel 重复的显式触发/普通任务排除和一次性退出措辞；保留 frontmatter 的详细触发词、named-evidence reassessment、完整 Reliability Loop、correction taxonomy、slow-execution non-trigger、workflow boundaries 和 universal-preflight 禁止边界；该 skill 无 supporting references。
- 已完成当前资产到 Kernel、Playbooks、References、Scenario Corpus（seed）、Outcome Evals（routing/behavior seed + outcome protocol）、Lab、Governance/Distribution/External Reference 的唯一映射。
- 未移动 workflow，未创建运行时目录，未修改 tests 运行合同；Kernel 与已有 supporting references 均未移动或删除。
- 所有已完成运行时切片均已提交；最新提交为 `a68bef6`。
- 原方向文档 `coding-agent-skills-high-value-refactor-direction.md` 仍是未跟踪的外部参考材料，不是运行时文件。

### 压缩后下一步

阶段 1 映射已落盘于 `coding-agent-skills-asset-lifecycle-ledger.md`；阶段 2 的非运行时协议、静态 seed 和 conformance check 已落盘于 `tests/evals/outcome-protocol.md`、`tests/evals/scenario-seeds.json` 与 `tests/evals/verify-scenario-seeds.js`；Kernel、`debug-systematically`、`test-strategy`、`review-and-finish`、`agent-workflow`、`plan-work`、`design-codebase` 与 `reliability-check` 的运行时薄化切片已实施并提交。

上下文压缩后直接从以下步骤恢复：

1. 继续处理剩余 explicit-intent playbook 中与 Kernel 重复的局部措辞，优先 `finish-branch`、`issue-workflow`、`memory-handoff`、`markdown-memory`、`skill-refactorer` 或 `decision-map`；每次只处理一个 playbook，保留其触发边界、具体方法和安全/持久化职责。
2. 读取当前目标 `SKILL.md` 与其 supporting references，实施最小正文切片；保持 frontmatter、`tests/routing-contract.md`、`tests/trigger-matrix.md` 和 `tests/non-trigger-cases.md` 语义不变。
3. 运行目标 playbook 的 focused route/reference/conformance 检查、`git diff --check`，更新本文件和 ledger，并按用户已设置的偏好在验证通过后默认提交。

独立 acceptance oracle 和可核验 host execution substrate 仍是实际 outcome A/B 的前置依赖；在此之前不执行真实 outcome 声明或生命周期动作，不移动 adaptive，不创建 profiles 或第二运行时入口。不要重新审查方向，不要重新比较相反架构，不要先做无证据的物理搬迁。

### 恢复时禁止漂移

- 不要把“暂不处理”误读为“永不处理”，也不要把它改写成第二个架构选项。
- 不要把当前四目录解释成目标永久结构。
- 不要重复做已经完成的文档、仓库和官方事实审查。
- 不要把 token 数、触发命中或静态合同当成真实结果收益。
- 不要在 active workflow 外创建 sibling controller/agent tree。
- 不要执行 commit、push、merge、删除或分支清理，除非用户另行明确要求。
