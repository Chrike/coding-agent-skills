# coding-agent-skills 资产职责与生命周期账本

- 日期：2026-07-15
- 阶段：仓库可执行重构收口；Kernel 与 13 个 playbook 的运行时薄化、Lab 归位、profiles/distribution 和 fail-closed lifecycle governance 已实施并提交；真实 outcome 轨道保持 blocked
- 状态：资产映射、协议、静态 seed、conformance check、Kernel/playbook 压缩、唯一 frozen Lab source、evidence-loop reference、Fast/Quality/Lab 非运行时 manifest、显式 installer、lifecycle policy 和空 Archive 边界已建立；三项既有 eval 与新增结构验证通过；真实产品任务规格、独立 acceptance oracle、host/provider/harness、telemetry 和 pricing 仍缺失或不可核验，因此不产生 outcome/lifecycle benefit claim
- 当前基线：`full-suite-v1` → `9a0318a`
- 当前分支：`refactor/kernel-playbooks-thin`
- 最新功能 checkpoint：`5182582`（`Record blocked-invalid evaluation handoff`）；前置 checkpoint 为 `589b3cf`、`beb248a`、`fa0b749`
- 最新交接/冻结 checkpoint：`16e5075`（`Freeze evaluation expansion handoff`）
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
| `kernel.default-behavior` | `prompts/CLAUDE.fragment.md` | always-on | Kernel | `prompts/CLAUDE.fragment.md` | `baseline-runtime` | default/routing 合同；Kernel focused invariant check 通过；无 outcome benchmark | 只有完整恢复门通过并完成单 scenario/provider/host advisory-only smoke proof 后，才考虑建立 scenario/outcome 引用；继续保持具体方法在 playbook/reference，不把它们搬入 Kernel |

Kernel 当前只保留跨任务、可观察、宿主不能确定性保证的默认行为。具体调试、测试、规划、评审和编排方法不在此复制。

### 2.2 Playbooks：运行时 skills

每个 `SKILL.md` 是自身触发边界和方法正文的唯一 owner。`README.md` 只提供能力地图摘要，不能替代 skill 正文；`tests/` 只验证边界，不能成为第二套路由规范。

| asset ID | current path | runtime surface | target layer | canonical owner | lifecycle | validation status | next gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `playbook.debug-systematically` | `skills/debug-systematically/SKILL.md` | automatic | Playbooks | `skills/debug-systematically/SKILL.md` | `baseline-runtime` | routing/方法合同；Kernel-overlap 局部压缩 focused contract 通过；无 outcome benchmark | 继续保持 debug 具体方法与 supporting references 的唯一 owner；完整恢复门通过并完成单 scenario/provider/host advisory-only smoke proof 后，才考虑无 skill/当前 skill/候选精简 skill 对照评测；未有结果前不删除或降级 |
| `playbook.test-strategy` | `skills/test-strategy/SKILL.md` | automatic | Playbooks | `skills/test-strategy/SKILL.md` | `baseline-runtime` | routing/方法合同；Kernel-overlap 局部压缩 focused contract 通过；无 outcome benchmark | 继续保持测试层级、TDD、mock、flaky wait strategy 和 regression seam 的唯一 owner；完整恢复门通过并完成单 scenario/provider/host advisory-only smoke proof 后，才考虑边际 outcome 评测；与 `debug-systematically` 的边界必须继续由两者各自拥有 |
| `playbook.review-and-finish` | `skills/review-and-finish/SKILL.md` | automatic | Playbooks | `skills/review-and-finish/SKILL.md` | `baseline-runtime` | routing/完成验证合同；Kernel-overlap 局部压缩 focused contract 通过；无 outcome benchmark | 继续保持 review、readiness、feedback 和 PASS/BLOCK 判断的唯一 owner；不得因 review 默认推导 branch action；完整恢复门通过并完成单 scenario/provider/host advisory-only smoke proof 后，才考虑评估高风险完成判断价值 |
| `playbook.plan-work` | `skills/plan-work/SKILL.md` | automatic | Playbooks | `skills/plan-work/SKILL.md` | `baseline-runtime` | routing/计划边界合同；Kernel-overlap 局部压缩 focused contract 通过；无 outcome benchmark | 继续保持 planning trigger、依赖/顺序/范围决策和 settled-plan 执行边界的唯一 owner；已确定计划不应重新触发规划；完整恢复门通过并完成单 scenario/provider/host advisory-only smoke proof 后，才考虑评估计划承重价值 |
| `playbook.design-codebase` | `skills/design-codebase/SKILL.md` | automatic | Playbooks | `skills/design-codebase/SKILL.md` | `baseline-runtime` | routing/设计边界合同；Kernel-overlap 局部压缩 focused contract 通过；无 outcome benchmark | 继续保持 architecture/ownership/interface/dependency decision、真实 seam 和 prototype gate 的唯一 owner；不因 skill 激活而自动引入 adapter 或 ADR；完整恢复门通过并完成单 scenario/provider/host advisory-only smoke proof 后，才考虑评估非显而易见的设计决策价值 |
| `playbook.reliability-check` | `skills/reliability-check/SKILL.md` | automatic | Playbooks | `skills/reliability-check/SKILL.md` | `baseline-runtime` | explicit correction contract；Kernel-overlap 局部压缩 focused contract 通过；无 outcome benchmark | 保持显式触发；不得在无可靠性挑战时变成通用 preflight |
| `playbook.agent-workflow` | `skills/agent-workflow/SKILL.md` | automatic | Playbooks | `skills/agent-workflow/SKILL.md` | `baseline-runtime` | orchestration/ownership/verification 合同；Kernel-overlap 局部压缩 focused contract 通过；无 outcome benchmark | 继续作为通用编排 canonical owner；保持 decomposition、evidence handoff、nested-controller 与 stop contracts；adaptive 只提取特有证据状态，不复制通用合同 |
| `playbook.finish-branch` | `skills/finish-branch/SKILL.md` | explicit-intent | Playbooks | `skills/finish-branch/SKILL.md` | `baseline-runtime` | branch-action safety contract；Kernel-overlap 局部压缩 focused contract 通过；无 outcome benchmark | 保持 commit/push/merge/discard/PR 的显式授权边界；不得由 readiness 自动推导 |
| `playbook.issue-workflow` | `skills/issue-workflow/SKILL.md` | explicit-intent | Playbooks | `skills/issue-workflow/SKILL.md` | `baseline-runtime` | tracker-draft/publish boundary；Kernel-overlap 局部压缩 focused contract 通过；无 outcome benchmark | 保持草稿与外部发布分离；不得因任务规模自动创建 issue |
| `playbook.memory-handoff` | `skills/memory-handoff/SKILL.md` | explicit-intent | Playbooks | `skills/memory-handoff/SKILL.md` | `baseline-runtime` | handoff/resume contract；Kernel-overlap 局部压缩 focused contract 通过；无 outcome benchmark | 只承载压缩、交接和恢复状态；不得成为普通任务的默认持久化层 |
| `playbook.markdown-memory` | `skills/markdown-memory/SKILL.md` | explicit-intent | Playbooks | `skills/markdown-memory/SKILL.md` | `baseline-runtime` | project-lesson boundary；Kernel-overlap 局部压缩 focused contract 通过；无 outcome benchmark | 与 host auto memory、handoff、decision map 保持单一职责 |
| `playbook.skill-refactorer` | `skills/skill-refactorer/SKILL.md` | explicit-intent | Playbooks | `skills/skill-refactorer/SKILL.md` | `baseline-runtime` | maintenance/refactor boundary；Kernel-overlap 局部压缩 focused contract 通过；无 outcome benchmark | 维护 prompt/skill 正文；不得把验证材料重新写成运行时指令 |
| `playbook.decision-map` | `skills/decision-map/SKILL.md` | explicit-intent | Playbooks | `skills/decision-map/SKILL.md` | `baseline-runtime` | durable decision-frontier contract；Kernel-overlap 局部压缩 focused contract 通过；无 outcome benchmark | 只处理明确的跨会话决策前沿；路径清楚时不创建第二份决策图 |

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
| `eval.routing-behavior-contract` | `skills/agent-workflow/evals/evals.json` | non-runtime eval | Outcome Evals（routing/behavior subset） | `skills/agent-workflow/evals/evals.json` | `baseline-validation` | 12 组结构化 routing/behavior assertions；不是 outcome benchmark | 继续作为 routing/behavior 维护合同；不得把此文件误报为真实结果收益；真实 outcome 评测保持冻结 |
| `eval.outcome-protocol-v1` | `tests/evals/outcome-protocol.md` | non-runtime protocol | Outcome Evals | `tests/evals/outcome-protocol.md` | `governance-only` | specification-only；定义三臂 paired evaluation、四类证据和 advisory gate；尚未执行 | 只有真实产品任务规格、独立冻结 task oracle、immutable harness、host/provider/tool-policy、隔离、provenance 和 telemetry/pricing 全部可核验后，才先做单 scenario/provider/host advisory-only smoke proof；协议本身不能产生 lifecycle recommendation |
| `scenario.seed-corpus-v1` | `tests/evals/scenario-seeds.json` | non-runtime scenario seed | Scenario Corpus | `tests/evals/scenario-seeds.json` | `baseline-validation` | 6 条 static seed；全部 `outcome_status: unmeasured`、blocked independent oracle；由 `verify-scenario-seeds.js` 做来源/hash conformance check 并通过 | 当前保持 static-seed-only；不得合成产品 fixture/oracle、升级 executable-ready 或把 seed 当 outcome evidence |
| `eval.readiness-slice.test-pos-001` | `tests/evals/scn-tm-test-pos-001-readiness.json`、`scn-tm-test-pos-001-readiness-fixture.js`、`scn-tm-test-pos-001-readiness-oracle.js`、`verify-scn-tm-test-pos-001-readiness.js` | non-runtime readiness self-check | Outcome Evals（readiness only） | `tests/evals/scn-tm-test-pos-001-readiness.json` + independent oracle module | `baseline-validation` | fixture/oracle hash、静态 seed 引用、6 条 readiness criteria、重复稳定性和 fixed-sleep negative control 通过；无 model/host/A-B/outcome claim | 当前保持 non-runtime readiness；只有真实产品任务规格、独立 task acceptance oracle 和完整恢复门具备后，才可考虑 executable scenario；不改变 static seed 或 outcome 状态 |
| `eval.blocked-invalid-semantics-v1` | `tests/evals/blocked-invalid-semantics.json`、`tests/evals/verify-blocked-invalid-semantics.js` | non-runtime metadata-only conformance | Outcome Evals（terminal semantics only） | `tests/evals/outcome-protocol.md` §5.4.1/§5.5 + synthetic manifest/verifier | 9 synthetic records、7 paired sets；blocked/invalid reason code、attempt boundary、metric wrapper、terminal pointer、preservation、paired propagation、raw/paired denominator 和 attrition 通过；`outcome_denominator: 0`；无 runtime/A-B/outcome claim | 只读 inventory 已确认真实产品任务 fixture、独立 task acceptance oracle、outcome runner、三臂隔离 harness、model/provider matrix、真实 telemetry 或 pinned pricing 均缺失或不可核验；当前保持 metadata-only dormant conformance。前置条件全部具备后，才先做单 scenario/provider/host advisory-only smoke proof；此前不实现 runner、A/B、model matrix 或 telemetry stack |

当前没有 `tests/scenarios/`、outcome runner、模型矩阵、成本采集器或自动 promotion/demotion/archive 系统。readiness slice 只验证独立 fixture/oracle 的确定性自检，blocked/invalid slice 只验证终态 metadata 合同；两者都不改变 `scenario-seeds.json` 的 static-seed-only、unmeasured 边界，也不改变这一事实。

### 2.5 Lab：adaptive pilot

| asset ID | current path | runtime surface | target layer | canonical owner | lifecycle | validation status | next gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `lab.adaptive-long-horizon` | `experiments/workflows/adaptive-long-horizon.js` | explicit saved-workflow source；需复制到明确宿主目标后调用 | Lab | `experiments/workflows/adaptive-long-horizon.js` | `frozen-lab` | 已有候选/验证证据边界、预算和停止合同；唯一 source path；无 live outcome/A-B | 保持 frozen；结构归位不等于 outcome promotion；只有真实 outcome 条件具备时才考虑是否恢复或归档 |
| `lab.workflow-boundary` | `experiments/README.md` | non-runtime source/install contract | Lab（实验治理） | `experiments/README.md` | `governance-only` | 已核对显式、只读、有界 pilot 边界和非 sandbox 声明 | 保持 source/install/revision/README/test 合同；不得扩展为通用 workflow 平台 |

adaptive 的通用委派、worker brief、leaf/controller 和集成原则仍由 `skills/agent-workflow/SKILL.md` 负责；adaptive 自己只拥有候选/验证 evidence schema、路径/版本校验、预算、contradiction/no-progress 与 pilot 只读限制。

### 2.6 分发、安装与说明元数据

这些资产影响展示、安装识别或维护说明，但不拥有运行时行为。

| asset ID | current path | runtime surface | target layer | canonical owner | lifecycle | validation status | next gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `distribution.profile-manifest` | `profiles/manifest.json` | non-runtime profile/install metadata | Distribution（非运行时类别） | `profiles/manifest.json` | `distribution-only` | Fast/Quality/Lab 精确集合、Quality policy default、Lab explicit-only；不影响路由；由 profile conformance 验证 | 只维护 source/install selection；不得变成 runtime router 或 outcome claim |
| `distribution.profile-installer` | `scripts/install-profile.js` | explicit distribution tool | Distribution（非运行时类别） | `scripts/install-profile.js` | `distribution-only` | explicit target、dry-run、apply、conflict-safe、no-delete；不写 CLAUDE.md/settings/tests/evals | 继续保持 host-owned policy boundary；不声称 host enforcement 或 provider identity |
| `distribution.skills-sh` | `skills.sh.json` | non-runtime distribution metadata | Distribution（非运行时类别） | `skills.sh.json` | `distribution-only` | 仅页面分组；不影响路由 | 物理 skill 迁移时同步路径和分组；不得让它成为第二套路由 |
| `distribution.skills-lock` | `skills-lock.json` | non-runtime install/version metadata | Distribution（非运行时类别） | `skills-lock.json` | `distribution-only` | source/path/hash lock；不记录生命周期；当前 ignored/stale，不作为 profile source | 只有明确的 source/install 路径变更且建立 canonical lock 合同时更新；不得用 lock 文件替代 ledger |
| `governance.lifecycle-policy` | `governance/lifecycle-policy.json` | non-runtime lifecycle policy | Governance（非运行时类别） | `governance/lifecycle-policy.json` | `governance-only` | blocked、advisory-only、自动 action=false；真实 outcome 前置条件完整列出 | 只在真实前置条件或维护决策改变时更新；不自动执行动作 |
| `governance.archive-boundary` | `archive/README.md` | non-runtime archive boundary | Archive（非运行时类别） | `archive/README.md` | `governance-only` | 当前无归档资产；需 decision-grade evidence + maintainer approval | 不复制正文、不自动归档 |
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
4. `experiments/workflows/<name>.js` 唯一拥有 Lab saved-workflow 实现；`experiments/README.md` 只拥有 source/install/pilot 边界说明。
5. `tests/`、`evals/` 和未来 scenario/outcome 文件只拥有验证资产；它们不得成为运行时 instruction layer。
6. `skills.sh.json` 和 `skills-lock.json` 只拥有分发/版本元数据；它们不得定义触发或生命周期。
7. 本账拥有资产身份、目标层、生命周期和迁移门槛的索引元数据，但不拥有任何运行时规则正文。
8. 外部分析文件没有 canonical owner；它们不能通过被放入仓库而自动取得指令权。

## 4. 单一路线的迁移顺序

### 已完成：冻结、事实盘点与仓库结构收口

- 使用 `full-suite-v1` / `9a0318a` 作为比较基线。
- 确认现有源目录、宿主落点、显式 workflow 复制边界和测试/评测边界。
- 冻结 adaptive 的现有只读、有界能力，不继续扩展状态机。

### 已完成：运行时薄化与唯一映射

- 本账为每个运行时资产和主要非运行时资产分配稳定 ID、唯一 owner、目标层和生命周期。
- 当前路径是唯一有效 source path；迁移后的 `experiments/workflows/adaptive-long-horizon.js` 已取代旧路径，未保留第二入口。
- Kernel 与 13 个高价值 playbook 已完成局部薄化；每个切片均保持具体方法、supporting references（如有）和触发边界。
- 已完成 profiles/distribution、Lab source relocation 和 lifecycle governance 的仓库可执行部分；不创建第二套路由、不改变现有 skill 触发语义。

### 当前：仓库结构已收口，真实 outcome 与生命周期证据保持冻结

- 当前工作模式是“运行时薄化、Lab 归位、profiles/distribution、evidence-loop reference 和 fail-closed governance 已完成；真实 outcome/A-B 与 evidence-backed lifecycle 仍 blocked”；不是重新审查既定路线，也不是继续扩大 synthetic verifier。首个产品任务 fixture/oracle 设计门仍为 `blocked-awaiting-product-task-spec`。现有评测资产保留为 dormant 的非运行时完整性检查，不 archive。
- `SCN-TM-TEST-POS-001` 已有 readiness manifest、纯 Node deterministic fixture、fixture behavior oracle 和 conformance self-check；该 slice 仍属于 non-runtime validation，不是独立产品 acceptance oracle 或 executable outcome scenario。
- readiness self-check 的 6 条 criteria、3 次重复稳定性、missing-readiness timeout 和 fixed-sleep negative control 已通过；blocked/invalid metadata conformance 的 9 条 records、7 个 paired sets 也已通过，`outcome_denominator: 0`；未执行模型、host routing、三臂 A/B、cost/latency telemetry 或 lifecycle action。
- 评测恢复前置条件必须全部具备：真实产品任务规格、独立且预先冻结的 task acceptance oracle、immutable harness、可核验 host/provider/tool-policy contract、fresh isolation、provenance/attempt metadata、telemetry 和 pinned pricing；当前结构性收口已完成，在这些条件自然具备前不扩展真实 outcome 轨道。

### 已完成：阶段 1 验收与阶段 2 协议/静态输入

1. 已核对每个 skill 的 supporting reference 由父 `SKILL.md` 直接链接；未重写方法正文。
2. 已建立 `tests/evals/outcome-protocol.md`，定义无 skill、当前完整 skill、候选精简 skill 三个条件臂，以及 routing、trajectory、outcome、cost/latency 四层证据。
3. 已建立 `tests/evals/scenario-seeds.json` 和 `verify-scenario-seeds.js`；6 条静态 seed 的来源、哈希、基线 revision 和未测量状态已通过 conformance check。
4. README、experiments README、profiles、governance、tests 和 evals 仍保持非运行时边界；账本不参与宿主路由。

### 当前冻结：真实产品任务与真实执行材料不存在

1. `SCN-TM-TEST-POS-001` 的 readiness behavior oracle 只验证 synthetic fixture 的确定性行为；canonical trigger row 只有路由意图，没有产品 surface、输入/状态迁移、预期功能结果、回归边界或可观察验收，因此不能据此编造产品 task fixture 或独立 task acceptance oracle。
2. 首个产品任务 fixture/oracle 设计门仍为 `blocked-awaiting-product-task-spec`：仓库没有真实产品代码或产品域语义；`scenario-seeds.json` 继续保持 `static-seed`、`outcome_status: unmeasured` 和 blocked oracle。当前不补造这些材料。
3. 只读 host/provider/harness/provenance inventory 仍确认没有 outcome runner、immutable task harness、模型/provider 矩阵、成本/Token/工具/延迟采集器或可核验 host execution substrate；profile manifest 和 installer 只提供仓库-owned distribution，不证明 host contract、provider 身份、worker 隔离或 tool-policy snapshot。
4. 仓库结构性收口已完成：profiles/distribution、Lab source relocation、evidence-loop reference、lifecycle policy 和 empty Archive 已落盘并有验证器；真实 outcome/A-B、promotion/demotion/archive 仍保持 blocked，不把这些缺失材料转成用户待办。

### 已完成：仓库结构、分发与治理收口

1. `profiles/manifest.json` 已定义 Fast、Quality、Lab 三个非运行时 distribution profile；Quality 是 policy default，Lab 仅 explicit-only；profile 不改变自然语言路由。
2. `scripts/install-profile.js` 已提供显式 target、dry-run、apply、冲突保护、幂等复制和不删除边界；不写 `CLAUDE.md`、settings、tests/evals 或治理文件。
3. `adaptive-long-horizon` 已唯一归位到 `experiments/workflows/adaptive-long-horizon.js`，旧 source path 已删除；`experiments/README.md` 保留 frozen Lab 和 host sandbox 非证明边界。
4. `skills/agent-workflow/references/evidence-loop.md` 已提取可复用的 candidate/verified evidence、最小 carry-forward、contradiction/no-progress、预算和 leaf/verifier 原则；不复制 adaptive 状态机。
5. `governance/lifecycle-policy.json` 和 `archive/README.md` 已建立 blocked、advisory-only、维护者审阅和空 Archive 边界；不自动 promotion、demotion、archive 或 profile/path/install mutation。

### 证据依赖的后续（不是当前待办）

真实 outcome/A-B 仍只在完整恢复门全部自然具备后恢复：真实产品任务规格、独立冻结 acceptance oracle、immutable harness、可核验 host/provider/tool-policy、fresh isolation、provenance/attempt metadata、provider telemetry 和 pinned pricing。恢复时最多先做一个 immutable scenario × provider × host 的 advisory-only 三臂 smoke proof；否则保持 blocked。该条件不要求用户创造材料。

在真实 outcome 证据自然具备前，不创建产品 fixture/oracle、broad runner、model matrix、telemetry/pricing platform，不声称 Quality/adaptive outcome benefit，不执行 promotion/demotion/archive，也不进行新的物理 runtime 迁移。

## 5. 当前明确不做的事

- 不把本账或外部方向文档装入 `prompts/`、`skills/` 或宿主 runtime。
- 不提前创建并行的 `experiments/`、`archive/` 或第二套路由入口来模拟迁移完成。
- `adaptive-long-horizon` 已完成结构性归位到 `experiments/workflows/adaptive-long-horizon.js`；不把该物理归位解释成 outcome promotion、host enforcement 或 lifecycle eligibility。
- 不因为当前 skill 缺少 outcome 数据就删除、压缩或降级它们。
- 不把当前 routing/behavior 合同描述成真实结果收益。
- 不以 `skills-lock.json`、`skills.sh.json` 或 README 摘要代替 canonical source。
- 不推送、合并、删除或清理分支；提交只在用户明确授权或已设置的“验证通过后默认提交”偏好覆盖的普通已验证改动范围内执行。外部方向文档仍不提交。

## 6. 当前结构验收

当前仓库结构收口只有在以下条件全部成立时才算完成：

- 每个当前运行时 source asset 都有且只有一个 canonical owner。
- 每个主要非运行时验证、实验、分发和治理资产都有明确的非运行时归属。
- 目标层、当前路径和生命周期没有混淆；planned 目标没有被写成当前事实。
- `adaptive-long-horizon` 被明确标记为 frozen Lab pilot，而不是默认 workflow 平台。
- 现有 tests/evals 被明确标记为 routing/behavior validation，不被误报为 outcome 评测。
- ledger 不复制任何规则正文、触发条件或执行步骤。
- 迁移顺序明确要求先评测、后生命周期动作，且没有保留相反架构作为并列选项。
