# coding-agent-skills 资产职责与生命周期账本

- 日期：2026-07-14
- 阶段：阶段 2 评测基础已启动；Kernel 与首批 playbook 运行时切片已实施
- 状态：资产映射、协议、静态 seed、conformance check、Kernel 压缩与首批 playbook 局部压缩已建立；真实 runner/物理迁移尚未开始
- 当前基线：`full-suite-v1` → `9a0318a`
- 决策依据：[`coding-agent-skills-refactor-review-decision.md`](coding-agent-skills-refactor-review-decision.md)
- 本文性质：非运行时治理索引。本文不承载 prompt、skill、workflow 或测试正文，不增加路由，不改变安装面，也不替代任何 canonical source。

## 1. 使用规则

这份账本只回答四个问题：资产现在在哪里、谁是唯一 canonical owner、目标上应属于哪一层、什么证据允许它进入下一生命周期。规则正文、触发边界、执行方法和验证合同仍只由账本引用的源文件负责。

### 1.1 字段约束

- `asset ID`：稳定的资产身份；不随物理目录迁移改变。
- `current path`：当前事实路径；不把未来路径写成当前事实。
- `runtime surface`：当前是否常驻、自动路由、显式调用或完全非运行时。
- `target layer`：目标架构中的唯一归属。`Governance` 和 `Distribution` 只表示非运行时元数据类别，不是新的运行时层。
- `canonical owner`：拥有正文、触发边界或执行语义的唯一文件/目录。一个资产不得有两个并列 owner。
- `lifecycle`：当前生命周期状态，不表示结果收益已经被证明。
- `validation status`：当前证据强度。现有 routing/behavior 合同不能填写为 outcome 已证明。
- `next gate`：允许下一步迁移、升降级或归档的明确条件。

### 1.2 生命周期值

| 值 | 含义 |
| --- | --- |
| `baseline-runtime` | 当前运行时基线，继续承担现有职责；尚无足够 outcome 数据支持升降级。 |
| `baseline-supporting` | 当前运行时资产的按需 supporting/reference 内容；不独立路由。 |
| `baseline-validation` | 当前维护与验证基线；不进入运行时上下文。 |
| `frozen-lab` | 显式实验资产；只读、有界，不参与普通自动路由。 |
| `governance-only` | 维护、决策或说明材料；不属于运行时控制面。 |
| `distribution-only` | 安装、展示或版本锁定元数据；不定义行为。 |
| `external-reference` | 外部分析输入；不能作为本项目的指令或 canonical source。 |
| `planned` | 目标层已确定，但物理资产尚未创建或迁移。 |
| `archived` | 明确停止维护但保留历史；当前没有资产因本账自动进入此状态。 |

## 2. 当前资产映射

### 2.1 常驻 Kernel

| asset ID | current path | runtime surface | target layer | canonical owner | lifecycle | validation status | next gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kernel.default-behavior` | `prompts/CLAUDE.fragment.md` | always-on | Kernel | `prompts/CLAUDE.fragment.md` | `baseline-runtime` | default/routing 合同；Kernel focused invariant check 通过；无 outcome benchmark | 在阶段 2 对高代价跨任务规则建立 scenario/outcome 引用；继续保持具体方法在 playbook/reference，不把它们搬入 Kernel |

Kernel 当前只保留跨任务、可观察、宿主不能确定性保证的默认行为。具体调试、测试、规划、评审和编排方法不在此复制。

### 2.2 Playbooks：运行时 skills

每个 `SKILL.md` 是自身触发边界和方法正文的唯一 owner。`README.md` 只提供能力地图摘要，不能替代 skill 正文；`tests/` 只验证边界，不能成为第二套路由规范。

| asset ID | current path | runtime surface | target layer | canonical owner | lifecycle | validation status | next gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `playbook.debug-systematically` | `skills/debug-systematically/SKILL.md` | automatic | Playbooks | `skills/debug-systematically/SKILL.md` | `baseline-runtime` | routing/方法合同；Kernel-overlap 局部压缩 focused contract 通过；无 outcome benchmark | 继续保持 debug 具体方法与 supporting references 的唯一 owner；阶段 2 以无 skill/当前 skill/候选精简 skill 对照评测；未有结果前不删除或降级 |
| `playbook.test-strategy` | `skills/test-strategy/SKILL.md` | automatic | Playbooks | `skills/test-strategy/SKILL.md` | `baseline-runtime` | routing/方法合同；Kernel-overlap 局部压缩 focused contract 通过；无 outcome benchmark | 继续保持测试层级、TDD、mock、flaky wait strategy 和 regression seam 的唯一 owner；与 `debug-systematically` 的边界必须继续由两者各自拥有 |
| `playbook.review-and-finish` | `skills/review-and-finish/SKILL.md` | automatic | Playbooks | `skills/review-and-finish/SKILL.md` | `baseline-runtime` | routing/完成验证合同；Kernel-overlap 局部压缩 focused contract 通过；无 outcome benchmark | 继续保持 review、readiness、feedback 和 PASS/BLOCK 判断的唯一 owner；不得因 review 默认推导 branch action；评估高风险完成判断价值 |
| `playbook.plan-work` | `skills/plan-work/SKILL.md` | automatic | Playbooks | `skills/plan-work/SKILL.md` | `baseline-runtime` | routing/计划边界合同；Kernel-overlap 局部压缩 focused contract 通过；无 outcome benchmark | 继续保持 planning trigger、依赖/顺序/范围决策和 settled-plan 执行边界的唯一 owner；已确定计划不应重新触发规划；评估计划承重价值 |
| `playbook.design-codebase` | `skills/design-codebase/SKILL.md` | automatic | Playbooks | `skills/design-codebase/SKILL.md` | `baseline-runtime` | routing/设计边界合同；无 outcome benchmark | 评估非显而易见的 ownership/interface 决策价值；不因 skill 激活而自动引入 adapter 或 ADR |
| `playbook.reliability-check` | `skills/reliability-check/SKILL.md` | automatic | Playbooks | `skills/reliability-check/SKILL.md` | `baseline-runtime` | explicit correction contract；无 outcome benchmark | 保持显式触发；不得在无可靠性挑战时变成通用 preflight |
| `playbook.agent-workflow` | `skills/agent-workflow/SKILL.md` | automatic | Playbooks | `skills/agent-workflow/SKILL.md` | `baseline-runtime` | orchestration/ownership/verification 合同；Kernel-overlap 局部压缩 focused contract 通过；无 outcome benchmark | 继续作为通用编排 canonical owner；保持 decomposition、evidence handoff、nested-controller 与 stop contracts；adaptive 只提取特有证据状态，不复制通用合同 |
| `playbook.finish-branch` | `skills/finish-branch/SKILL.md` | explicit-intent | Playbooks | `skills/finish-branch/SKILL.md` | `baseline-runtime` | branch-action safety contract；无 outcome benchmark | 保持 commit/push/merge/discard/PR 的显式授权边界；不得由 readiness 自动推导 |
| `playbook.issue-workflow` | `skills/issue-workflow/SKILL.md` | explicit-intent | Playbooks | `skills/issue-workflow/SKILL.md` | `baseline-runtime` | tracker-draft/publish boundary；无 outcome benchmark | 保持草稿与外部发布分离；不得因任务规模自动创建 issue |
| `playbook.memory-handoff` | `skills/memory-handoff/SKILL.md` | explicit-intent | Playbooks | `skills/memory-handoff/SKILL.md` | `baseline-runtime` | handoff/resume contract；无 outcome benchmark | 只承载压缩、交接和恢复状态；不得成为普通任务的默认持久化层 |
| `playbook.markdown-memory` | `skills/markdown-memory/SKILL.md` | explicit-intent | Playbooks | `skills/markdown-memory/SKILL.md` | `baseline-runtime` | project-lesson boundary；无 outcome benchmark | 与 host auto memory、handoff、decision map 保持单一职责 |
| `playbook.skill-refactorer` | `skills/skill-refactorer/SKILL.md` | explicit-intent | Playbooks | `skills/skill-refactorer/SKILL.md` | `baseline-runtime` | maintenance/refactor boundary；无 outcome benchmark | 维护 prompt/skill 正文；不得把验证材料重新写成运行时指令 |
| `playbook.decision-map` | `skills/decision-map/SKILL.md` | explicit-intent | Playbooks | `skills/decision-map/SKILL.md` | `baseline-runtime` | durable decision-frontier contract；无 outcome benchmark | 只处理明确的跨会话决策前沿；路径清楚时不创建第二份决策图 |

这些 skills 当前全部保留在运行时基线中。`baseline-runtime` 不表示它们已经证明具有稳定 outcome 增益，只表示在完成对照评测前不擅自改变当前行为。

### 2.3 References：skill supporting 内容

以下 supporting 文件按父 skill 归属；它们不是独立路由入口。父 `SKILL.md` 必须继续直接说明何时读取、解决什么问题以及谁负责读取后的决策。

| asset ID | current path | runtime surface | target layer | canonical owner | lifecycle | validation status | next gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `reference.debug-systematically` | `skills/debug-systematically/references/*` | on-demand supporting | References | `skills/debug-systematically/SKILL.md` | `baseline-supporting` | parent-link 可核对；无 outcome benchmark | 核对每个 reference 的直接链接和触发分支；未有证据前不合并回主 skill |
| `reference.test-strategy` | `skills/test-strategy/references/*` | on-demand supporting | References | `skills/test-strategy/SKILL.md` | `baseline-supporting` | parent-link 可核对；无 outcome benchmark | 同上；具体测试方法不压缩成空泛 Kernel 规则 |
| `reference.plan-work` | `skills/plan-work/references/*` | on-demand supporting | References | `skills/plan-work/SKILL.md` | `baseline-supporting` | parent-link 可核对；无 outcome benchmark | 同上 |
| `reference.design-codebase` | `skills/design-codebase/references/*` | on-demand supporting | References | `skills/design-codebase/SKILL.md` | `baseline-supporting` | parent-link 可核对；无 outcome benchmark | 同上 |
| `reference.agent-workflow` | `skills/agent-workflow/references/*` | on-demand supporting | References | `skills/agent-workflow/SKILL.md` | `baseline-supporting` | parent-link 可核对；无 outcome benchmark | 只让通用编排 reference 由 `agent-workflow` 拥有；adaptive 不复制整套正文 |
| `reference.review-and-finish` | `skills/review-and-finish/references/*` | on-demand supporting | References | `skills/review-and-finish/SKILL.md` | `baseline-supporting` | parent-link 可核对；无 outcome benchmark | 同上 |
| `reference.skill-refactorer` | `skills/skill-refactorer/references/*` | on-demand supporting | References | `skills/skill-refactorer/SKILL.md` | `baseline-supporting` | parent-link 可核对；无 outcome benchmark | 同上 |

### 2.4 Scenario Corpus 与 Outcome Evals 的现有种子

现有验证资产暂不移动。它们为目标层提供种子，但不因此变成运行时指令。

| asset ID | current path | runtime surface | target layer | canonical owner | lifecycle | validation status | next gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `scenario.routing-contract` | `tests/routing-contract.md` | non-runtime maintenance contract | Scenario Corpus（seed） | `tests/routing-contract.md` | `baseline-validation` | 路由/组合合同；不是 outcome 数据 | 阶段 2 将可复用案例结构化为 scenario 记录，保留本文件作为当前边界合同，避免复制规则正文 |
| `scenario.trigger-matrix` | `tests/trigger-matrix.md` | non-runtime maintenance contract | Scenario Corpus（seed） | `tests/trigger-matrix.md` | `baseline-validation` | 正负触发案例；不是 outcome 数据 | 同上；scenario 记录引用 canonical skill/section，不重写路由规范 |
| `scenario.non-trigger-cases` | `tests/non-trigger-cases.md` | non-runtime maintenance contract | Scenario Corpus（seed） | `tests/non-trigger-cases.md` | `baseline-validation` | 非触发和防漂移案例；不是 outcome 数据 | 同上 |
| `eval.routing-behavior-contract` | `skills/agent-workflow/evals/evals.json` | non-runtime eval | Outcome Evals（routing/behavior subset） | `skills/agent-workflow/evals/evals.json` | `baseline-validation` | 12 组结构化 routing/behavior assertions；不是 outcome benchmark | 阶段 2 新增独立 outcome protocol/runner；不得把此文件误报为真实结果收益 |
| `eval.outcome-protocol-v1` | `tests/evals/outcome-protocol.md` | non-runtime protocol | Outcome Evals | `tests/evals/outcome-protocol.md` | `governance-only` | specification-only；定义三臂 paired evaluation、四类证据和 advisory gate；尚未执行 | 在存在可核验 host execution substrate 后实现 runner；协议本身不能产生 lifecycle recommendation |
| `scenario.seed-corpus-v1` | `tests/evals/scenario-seeds.json` | non-runtime scenario seed | Scenario Corpus | `tests/evals/scenario-seeds.json` | `baseline-validation` | 5 条 initial-screen static seed + 1 条 static eval reference；全部 outcome unmeasured；由 `verify-scenario-seeds.js` 做来源/hash conformance check | 为每条可执行 scenario 补独立 acceptance oracle 和 fixture；不得把 seed 直接当 outcome evidence |

当前没有 `tests/scenarios/`、outcome runner、模型矩阵、成本采集器或自动 promotion/demotion/archive 系统。`tests/evals/outcome-protocol.md` 和 `tests/evals/scenario-seeds.json` 只完成协议与静态输入定义，不改变这一事实。

### 2.5 Lab：adaptive pilot

| asset ID | current path | runtime surface | target layer | canonical owner | lifecycle | validation status | next gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `lab.adaptive-long-horizon` | `workflows/adaptive-long-horizon.js` | explicit saved-workflow source；需复制到明确宿主目标后调用 | Lab | `workflows/adaptive-long-horizon.js`（迁移前） | `frozen-lab` | 已有候选/验证证据边界、预算和停止合同；无 live outcome/A-B | 先完成阶段 2/3 的评测与配置协议；随后单次迁移到 `experiments/workflows/adaptive-long-horizon.js`，不保留两个自动发现入口 |
| `lab.workflow-boundary` | `workflows/README.md` | non-runtime source/install contract | Lab（实验治理） | `workflows/README.md` | `governance-only` | 已核对显式、只读、有界 pilot 边界 | 物理迁移时同步更新 source/install/revision/README/test 合同；不得扩展为通用 workflow 平台 |

adaptive 的通用委派、worker brief、leaf/controller 和集成原则仍由 `skills/agent-workflow/SKILL.md` 负责；adaptive 自己只拥有候选/验证 evidence schema、路径/版本校验、预算、contradiction/no-progress 与 pilot 只读限制。

### 2.6 分发、安装与说明元数据

这些资产影响展示、安装识别或维护说明，但不拥有运行时行为。

| asset ID | current path | runtime surface | target layer | canonical owner | lifecycle | validation status | next gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `distribution.skills-sh` | `skills.sh.json` | non-runtime distribution metadata | Distribution（非运行时类别） | `skills.sh.json` | `distribution-only` | 仅页面分组；不影响路由 | 物理 skill 迁移时同步路径和分组；不得让它成为第二套路由 |
| `distribution.skills-lock` | `skills-lock.json` | non-runtime install/version metadata | Distribution（非运行时类别） | `skills-lock.json` | `distribution-only` | source/path/hash lock；不记录生命周期 | 只有 source/install 路径变更时更新；不得用 lock 文件替代 ledger |
| `governance.readme-en` | `README.md` | non-runtime documentation | Governance（非运行时类别） | `README.md` | `governance-only` | 当前职责、安装和能力摘要；不拥有正文规则 | 物理迁移或配置实现后同步摘要；正文漂移时回到 canonical source 修正 |
| `governance.readme-zh` | `README.zh-CN.md` | non-runtime documentation | Governance（非运行时类别） | `README.zh-CN.md` | `governance-only` | 中文说明；不拥有运行时规则 | 与英文 README 同步，但不创建第三套规范 |
| `governance.refactor-decision` | `coding-agent-skills-refactor-review-decision.md` | non-runtime decision/handoff | Governance（非运行时类别） | `coding-agent-skills-refactor-review-decision.md` | `governance-only` | 已确定唯一目标路线和阶段边界 | 只在路线、阶段或用户约束改变时更新；不复制规则正文 |

`.claude/settings.local.json` 是宿主本地配置，不是本仓库 skill suite 的 canonical source，也不纳入运行时资产迁移。它只能作为宿主配置事实被单独核对。

### 2.7 外部参考材料

| asset ID | current path | runtime surface | target layer | canonical owner | lifecycle | validation status | next gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `reference.external-refactor-direction` | `coding-agent-skills-high-value-refactor-direction.md` | non-runtime external analysis | external reference（非运行时类别） | 无；不得成为本项目 canonical source | `external-reference` | 已审查；其中事实、建议和依据已与仓库证据分开 | 只在维护决策需要时作为参考；任何采用内容必须先转化为本账、canonical source 或独立 eval |

## 3. 唯一 canonical owner 规则

1. `prompts/CLAUDE.fragment.md` 唯一拥有常驻默认行为；README、tests、ledger 和外部文档不得复制并列版本。
2. 每个 `skills/<name>/SKILL.md` 唯一拥有该 skill 的触发边界和核心方法；同目录 `references/` 只由它按需加载。
3. `agent-workflow` 唯一拥有通用多代理委派、证据交接、leaf/controller 和停止边界；adaptive 不拥有通用副本。
4. `workflows/<name>.js` 唯一拥有 saved-workflow 实现；`workflows/README.md` 只拥有 source/install/pilot 边界说明。
5. `tests/`、`evals/` 和未来 scenario/outcome 文件只拥有验证资产；它们不得成为运行时 instruction layer。
6. `skills.sh.json` 和 `skills-lock.json` 只拥有分发/版本元数据；它们不得定义触发或生命周期。
7. 本账拥有资产身份、目标层、生命周期和迁移门槛的索引元数据，但不拥有任何运行时规则正文。
8. 外部分析文件没有 canonical owner；它们不能通过被放入仓库而自动取得指令权。

## 4. 单一路线的迁移顺序

### 已完成：冻结和事实盘点

- 使用 `full-suite-v1` / `9a0318a` 作为比较基线。
- 确认现有源目录、宿主落点、显式 workflow 复制边界和测试/评测边界。
- 冻结 adaptive 的现有只读、有界能力，不继续扩展状态机。

### 当前：建立唯一映射

- 本账为每个运行时资产和主要非运行时资产分配稳定 ID、唯一 owner、目标层和生命周期。
- 当前路径仍是唯一有效 source path；目标路径只表示迁移方向。
- 不移动目录、不创建第二套路由、不改变现有 skill 触发语义。

### 已完成：阶段 1 验收与阶段 2 协议/静态输入

1. 已核对每个 skill 的 supporting reference 由父 `SKILL.md` 直接链接；未重写方法正文。
2. 已建立 `tests/evals/outcome-protocol.md`，定义无 skill、当前完整 skill、候选精简 skill 三个条件臂，以及 routing、trajectory、outcome、cost/latency 四层证据。
3. 已建立 `tests/evals/scenario-seeds.json` 和 `verify-scenario-seeds.js`；6 条静态 seed 的来源、哈希、基线 revision 和未测量状态已通过 conformance check。
4. README、workflow README、tests 和 evals 仍保持非运行时边界；账本不参与宿主路由。

### 当前阻塞：独立 oracle 与可核验执行 substrate

1. 现有 seed 仍缺少可执行任务 fixture 和独立 acceptance oracle，因此不能产生 outcome 结果。
2. 仓库没有 outcome runner、任务 harness、模型矩阵、成本采集器或可核验 host execution substrate；不能凭空实现或宣称 A/B。
3. 在这些依赖具备前，不执行批量删除、合并、降级、promotion、archive、profile manifest 或物理迁移。

### 再随后：阶段 3 到阶段 5

1. 定义 Fast、Quality、Lab manifest、安装目标、覆盖和冲突规则；Quality 是推荐默认，Lab 只显式启用。
2. 只有在评测协议和配置边界可用后，将 adaptive 单次迁移到 `experiments/workflows/adaptive-long-horizon.js`，同时更新 source/install/README/test 合同；不保留旧、新两套自动入口。
3. 根据结果决定 skill 核心、reference、script/hook、Lab 或 Archive 归属，并实施物理目录迁移。
4. 迁移验收覆盖安装目标、命令名、路径链接、source/install revision 和当前测试合同。

## 5. 阶段 1 不做的事

- 不把本账或外部方向文档装入 `prompts/`、`skills/` 或宿主 runtime。
- 不提前创建并行的 `experiments/`、`archive/` 或第二套路由入口来模拟迁移完成。
- 不移动 `adaptive-long-horizon.js`，因为其迁移依赖阶段 2 的 outcome 协议和阶段 3 的 Lab 安装语义。
- 不因为当前 skill 缺少 outcome 数据就删除、压缩或降级它们。
- 不把当前 routing/behavior 合同描述成真实结果收益。
- 不以 `skills-lock.json`、`skills.sh.json` 或 README 摘要代替 canonical source。
- 不提交、推送、合并、删除或清理分支；本轮只建立治理索引并做文档级验证。

## 6. 阶段 1 验收

阶段 1 只有在以下条件全部成立时才算完成：

- 每个当前运行时 source asset 都有且只有一个 canonical owner。
- 每个主要非运行时验证、实验、分发和治理资产都有明确的非运行时归属。
- 目标层、当前路径和生命周期没有混淆；planned 目标没有被写成当前事实。
- `adaptive-long-horizon` 被明确标记为 frozen Lab pilot，而不是默认 workflow 平台。
- 现有 tests/evals 被明确标记为 routing/behavior validation，不被误报为 outcome 评测。
- ledger 不复制任何规则正文、触发条件或执行步骤。
- 迁移顺序明确要求先评测、后生命周期动作，且没有保留相反架构作为并列选项。
