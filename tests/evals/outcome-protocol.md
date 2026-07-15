# Outcome Evaluation Protocol v1

- 状态：specification-only；尚未执行
- 性质：非运行时评测合同，不参与 skill 路由、安装、宿主配置或生命周期自动变更
- 当前基线：`full-suite-v1` → `9a0318a`
- 适用范围：一次评测只研究一个指定 skill 的边际价值；不把整个 suite、模型标签或 adaptive pilot 混为一个结论
- 维护关联：[`coding-agent-skills-asset-lifecycle-ledger.md`](../../coding-agent-skills-asset-lifecycle-ledger.md)

## 1. 当前状态和声明边界

本仓库当前没有 outcome runner、任务 harness、模型矩阵、成本采集器或自动 promotion/demotion/archive 系统。仓库现在有 `profiles/manifest.json` 与 `scripts/install-profile.js`，但它们只提供显式、非运行时的 distribution metadata 和复制工具，不提供 host/provider/harness、隔离或 outcome 证据。因此，本文件完成后只能声明：

- outcome/A-B 的测量合同已经定义；
- 现有 routing/behavior 合同可以作为 scenario seed；
- 尚未证明任何 skill 的结果收益、成本收益或生命周期资格。

以下内容不能由本文件推出：

- 某个 skill 已经优于无 skill 或当前 baseline；
- adaptive workflow 已经优于 `agent-workflow`；
- 某个模型需要更多或更少永久规则；
- 某条规则应被 promotion、demotion 或 archive；
- 宿主已经提供了 worker 隔离、工具禁用或路径沙箱。

## 2. 评测对象和条件臂

### 2.1 一次只评一个目标 skill

初始第一批目标固定为：

1. `debug-systematically`
2. `test-strategy`
3. `agent-workflow`

之后的 `design-codebase`、`review-and-finish`、`plan-work` 另行评测。不要把多个目标 skill 的结果池化为一个 suite 结论。

### 2.2 三个条件臂

| arm | 内容 | 目标 skill 路由评分 |
| --- | --- | --- |
| `base-only` | 当前常驻 prompt 的 base behavior；不加载目标 repository skill。宿主基础工具和 bundled 能力保持一致。 | 目标 skill 激活是 `not_applicable/design-control`，不是 false negative。 |
| `baseline` | 当前目标 `SKILL.md` 与其当前 supporting references，固定到明确 source revision/hash；除目标 skill 外，其余 repository skill 不作为本次 treatment。 | 按 scenario 的 expected route 与实际激活结果评分。 |
| `candidate` | 候选目标 skill，固定 `candidate_id`、正文/reference revision/hash；必须保持 baseline 的触发边界，除非另行登记为 routing study。 | 按与 baseline 相同的 route oracle 评分。 |

`base-only`、`baseline`、`candidate` 的非 treatment 输入必须相同：任务快照、验收 oracle、模型/provider、宿主/harness、工具权限、预算、超时、初始上下文、仓库 revision、外部状态和重试政策都必须固定。

候选改变触发边界时，不能与本协议的内容边际评测混合；应单独建立 routing 评测，不能把 route 变化解释为方法正文收益。

### 2.3 不纳入初始比较的内容

- `adaptive-long-horizon` 不是本协议的默认 arm；它仍是位于 `experiments/workflows/adaptive-long-horizon.js` 的显式、只读、有界 frozen Lab pilot。
- `Fast`、`Quality`、`Lab` 现在有 `profiles/manifest.json` 和显式复制工具，但它们只决定 distribution/install selection，不是三个运行时 router；本协议不把 profile 选择解释成 outcome treatment。
- 不比较“轻量模型版”和“旗舰模型版”永久规则。模型比较必须在固定 skill treatment 之外单独分层分析。

## 3. Scenario 来源和身份

现有下列文件只能提供 scenario seed，不是 outcome 证明：

- `tests/routing-contract.md`
- `tests/trigger-matrix.md`
- `tests/non-trigger-cases.md`
- `skills/agent-workflow/evals/evals.json`

建议使用稳定、可追溯的 ID：

- `SCN-RT-*`：routing contract
- `SCN-TM-*`：trigger matrix
- `SCN-NT-*`：non-trigger cases
- `SCN-AW-*`：agent-workflow static evals

Scenario 记录必须保存：

- `scenario_id`、`scenario_revision`、`classification`；
- `source.path`、`source.locator`、`source.revision`；
- exact prompt/fixture 及其 hash；
- canonical `rule_refs` 和 `negative_rule_refs`，不得复制规则正文；
- independently authored `acceptance_oracle`；
- `seed_status`：`static-seed`、`executable-ready` 或 `blocked`。

静态 seed 没有可执行任务 fixture 和可用的独立 acceptance oracle 时，只能用于 routing/trajectory 研究，`outcome` 必须为 `unmeasured`；记录应明确 `eligible_for_routing_screen`，并将 `outcome_execution_eligible` 固定为 `false`。`acceptance_oracle.status: blocked` 表示 oracle 尚不可用，`independence_required: true` 表示未来 oracle 的独立性要求，不表示当前已有独立 oracle。

### 3.1 第一轮隔离筛选集

第一轮只用于验证协议和观察目标 skill 的局部信号，不用于生命周期变更。每个目标 skill 使用一个正向触发 scenario 和一个 base-only 负向 scenario：

| target skill | positive seed | base-only negative seed |
| --- | --- | --- |
| `debug-systematically` | `This test is flaky; diagnose it.`（`tests/trigger-matrix.md` 的 debug case） | `Fix this small TypeScript error.`（普通 base case） |
| `test-strategy` | `This test depends on sleep and flakes in CI. Fix the wait strategy.`（`tests/trigger-matrix.md` 的 test case） | `Fix this small TypeScript error.`（普通 base case） |
| `agent-workflow` | `Investigate these independent subsystems in parallel.`（`tests/trigger-matrix.md` 的 orchestration case） | `This multi-file change is still one coherent owner scope.`（`tests/non-trigger-cases.md` 的 negative case） |

推荐的第一轮屏幕是 3 个目标 × 2 个 scenario × 3 次重复；每个 scenario/repetition 是一个 paired set，包含三个 arm，因此总计 18 个 paired sets、54 个 arm runs。这个屏幕不满足生命周期决策门槛。

跨 skill 边界案例，例如 debug 与 test-strategy 的互斥路由、agent-workflow 与单 focused delegation 的区分，另列为 interaction scenarios，不与上述单 skill 边际结果合并。

## 4. Paired execution 合同

一个 `paired_set` 是同一 scenario 实例和同一 repetition 下的完整三臂集合，不是单个 arm run。

每个 paired set 必须满足：

1. 所有 arm 使用同一个不可变任务快照和同一个 acceptance oracle。
2. 每个 arm 使用 fresh session/context、fresh workspace 和隔离的外部状态。
3. 每个 arm 固定相同的 model/provider、host/runtime、OS/environment、tool policy、budget 和 timeout。
4. source revision、prompt hash、skill/reference hash、installed-copy identity 和 workflow revision 都被记录；无法核验时填写 `not_installed`、`unverified` 或 `ineligible`，不得留空或猜测。
5. arm 顺序在每个 repetition 中随机或 counterbalance，并记录 seed 与 order index。
6. 不允许跨 arm 共享 memory、handoff、缓存、产物、工具结果或人工提示。
7. 不允许未登记的 retry、prompt 修改、额外用户纠偏或工具权限变化；每次 retry 都是一个新 run，并保留原 run 记录。
8. 任务、oracle、treatment、环境或关键 provenance 不一致时，paired set 为 `invalid`，不能静默丢弃。

当前没有 runner 时，允许 `collection_mode: manual` 的探索性记录，但必须记录不可收集字段和原因；手工记录不能产生生命周期建议。

## 5. 结果维度

四类证据分开记录，不使用一个 composite score 让路由命中或成本抵消正确性失败。

### 5.1 Routing

记录：

- expected route；
- observed route 和 activated skills；
- route evidence pointer；
- route contract status；
- target activation status。

`base-only` 对目标 skill 激活为 `not_applicable/design-control`。负向 scenario 必须使用可观察的宿主激活或读取证据；回答中没有出现 skill 名称不能证明未触发。

### 5.2 Trajectory / constraint coverage

只记录可观察的合同项，不接受代理自述作为唯一证据。每项包含：

- `item_id`；
- `applicable`；
- `satisfied`：`true|false|unknown`；
- evidence pointer；
- canonical source path/section。

覆盖率不能替代任务 outcome。adaptive 的 candidate/verified evidence 或 `status: complete` 也不能自动成为任务成功。

### 5.3 Outcome

Outcome 必须来自独立于候选 skill 的 acceptance oracle。每个 criterion 记录：

- `criterion_id`；
- observable acceptance；
- evidence kind：`test|artifact|runtime_observation|user_visible_result`；
- evidence pointer；
- evaluator/method；
- status：`pass|fail|unknown`。

必需同时记录：

- acceptance pass/fail；
- correctness verdict 和证据；
- regression count、severity 和证据；
- failure category；
- user correction count、类型、发生轮次和是否为必要纠偏；
- safety events、forbidden side effects 和 changed paths（适用时）。

`unknown` 出现在必需 criterion 时，整个 outcome 不能判定为 pass。

### 5.4 Cost / latency

每个指标都使用带状态的包装，而不是空值或零填充：

```text
{ value, unit, status, reason }
```

`status` 至少支持：`measured`、`not_collected`、`not_applicable`、`unavailable`、`invalid`。

指标包括：

- input/output/total tokens；
- total tool calls、failed tool calls、tool names/counts；
- delegated agent count、parallel groups（适用时）；
- monotonic wall time、latency；
- cost 和 pricing source/version。

没有 provider telemetry 或 pinned pricing 时，记录不可用原因，不自行计算或填零。

#### 5.4.1 Metric wrapper conformance

每个 metric wrapper 都必须是一个只包含 `value`、`unit`、`status`、`reason` 四个字段的对象。`status` 只能是 `measured`、`not_collected`、`not_applicable`、`unavailable` 或 `invalid`；`unit` 和 `reason` 必须是非空字符串。

- `measured` 要求 `value` 为有限、非负数；不能用字符串、`null`、`NaN`、`Infinity` 或未声明的单位替代实际测量。
- 其他状态要求 `value: null`。`0` 不是“没有收集”的合法替代；`unavailable`、`not_collected`、`not_applicable` 和 `invalid` 都必须说明原因。
- `invalid` metric wrapper 表示该指标记录本身不可用于聚合；它不能被降级为 `not_collected`，也不能被静默删除。若指标在一次已尝试的 collection/execution 中违反 wrapper contract，run 应为 `invalid`，并将对应 metric JSON pointer 放入 `terminal_fields`。
- metadata-only conformance 可以验证 wrapper 形状和状态语义，但不能把 wrapper 的 `measured` 值解释成真实 telemetry。

## 5.5 Terminal status、尝试边界和关键 provenance

`terminal_status` 是 run 的终止分类，而不是 outcome 质量分数。它必须是 `completed`、`blocked` 或 `invalid` 之一；不能以 `unknown`、`inconclusive` 或空值替代 run 终止状态。

每个 run 必须记录事实性的 `execution_attempted` 和 `collection_attempted` 两个布尔字段；它们不能由 `terminal_status` 反推，也不能省略。两者的组合、终止状态和稳定 reason-code 由第 6.2.1 节固定。

- 在 collection/execution 尚未开始且 prerequisite 不可用或不可核验时，只能产生 `blocked`；不能把缺少材料伪装成 `invalid`。
- 已经尝试 collection/execution 后发现合同、provenance、pairing、environment 或 metric wrapper 违反要求时，必须产生 `invalid`；不能回写为 `blocked`。
- 如果尝试字段缺失、互相矛盾或无法判断，记录本身应为 `invalid`，使用 `terminal-semantics-ambiguous`，保留原始记录而不是猜测为 `blocked`。

每个 non-completed run 必须同时包含来自固定 registry 的 `terminal_reason_code`、非空的维护者可读 `terminal_reason`、非空的 canonical `terminal_fields`，以及 `record_preserved: true`。`terminal_fields` 必须是相对于该 run record 根、以 `/` 开头的 JSON Pointer；数组去重并按稳定顺序排列，且必须指向实际缺失、不可核验、不一致或违反 contract 的字段，不能只写 `/terminal_reason` 掩盖根因。paired set 的 propagation fields 以 paired-set record 根为准，并使用 `/members/<record_id>/terminal_status` 等稳定 member pointer。

`blocked` 只表达 prerequisite/attempt 尚未成立，不表达任务失败；`invalid` 表达已经尝试但记录或执行违反了可审计合同。两者都不是 complete outcome，不能进入 complete denominator。原始 run 的 terminal counts 与 paired set 的 complete denominator 必须分开报告，避免一个 paired set 中已完成的成员掩盖另一成员的 blocked/invalid 状态。`raw_run_counts` 必须按 `terminal_status` 和 `terminal_reason_code` 分层；`paired_set_counts` 必须按 propagated paired-set status 分层；`complete_paired_denominator` 只能统计所有成员均为 `completed` 的 paired set，不能用已完成 member run 数代替。被 blocked/invalid paired set 中的 completed member 可以保留在 raw run counts，但不能贡献 paired outcome numerator、paired delta 或 complete paired denominator。

reason-code registry 使用本节定义的连字符形式作为唯一 canonical spelling：`prerequisite-unavailable`、`critical-field-unverifiable`、`contract-field-missing`、`provenance-mismatch`、`pairing-mismatch`、`environment-mismatch`、`metric-wrapper-invalid`、`terminal-semantics-ambiguous`。别名、下划线形式和自由文本不得作为聚合键。`terminal_fields` 的 pointer 也必须使用已登记 schema path；通用 run record 至少包括 `/acceptance_oracle_ref`、`/scenario_revision`、`/prompt_sha256`、`/skill_source/revision`、`/installed_copy/hash`、`/host/runtime_revision`、`/profile/tool_permission_snapshot`、`/pairing/arm_order` 和 `/environment/tool_policy`。metadata-only conformance 可以用 manifest 的 `terminal_field_registry` 冻结其合成 record 的具体嵌套路径，但该 registry 必须是已登记 run-schema path 的明确子集，不能建立第二套终态语义。

## 6. 记录格式

### 6.1 Scenario record

```json
{
  "schema_version": "outcome-evaluation-v1",
  "scenario_id": "SCN-TM-001",
  "scenario_revision": 1,
  "classification": "routing-positive",
  "source": {
    "path": "tests/trigger-matrix.md",
    "locator": "Workflow Skill Cases > ...",
    "revision": "9a0318a"
  },
  "prompt_fixture": "...",
  "prompt_sha256": "...",
  "rule_refs": ["rule.playbook.debug-systematically.trigger"],
  "negative_rule_refs": [],
  "acceptance_oracle": {
    "revision": "...",
    "hash": "...",
    "criteria": [
      {
        "id": "A1",
        "observable": "...",
        "evidence_kind": "test|artifact|runtime_observation|user_visible_result"
      }
    ]
  },
  "seed_status": "static-seed|executable-ready|blocked"
}
```

Acceptance oracle 必须在 arm assignment 前冻结，并由候选 treatment 之外的评估者维护。候选不能生成、修改或解释自己的 oracle。

### 6.2 Run record

每个 run 至少包含：

```text
schema_version
record_id / run_id / paired_set_id
scenario_id / scenario_revision
exact task input + prompt hash
acceptance_oracle_ref + oracle hash
target_skill + arm + candidate ID/hash
repo revision
prompt source revision/hash
skill/reference source revision/hash
installed-copy path/revision/hash/status
model/provider/version
host/runtime/SDK/OS/environment
profile/config/tool-permission snapshot
budget/timeout
repetition index / randomization seed / arm order
fresh context/workspace IDs / state reset status
collection_mode: static|manual|automated
started_at / ended_at
terminal_status: completed|blocked|invalid + reason
route result and evidence
trajectory coverage and evidence
outcome criteria, correctness, regressions, corrections, safety events
metrics with value/status/reason wrappers
retries / manual interventions
provenance / evaluator version / limitations
```

任何 critical 字段缺失时，run 必须为 `invalid` 或 `blocked`，并记录原因；不能用零、空字符串或模型自述补齐。

#### 6.2.1 Terminal status application

Apply the terminal-status, attempt-boundary, reason-code, terminal-field, record-preservation, metric-wrapper, denominator, attrition, and paired-set propagation rules defined in §5.4.1 and §5.5. Do not create a second run-record terminal registry in this section.

### 6.3 Aggregate record

聚合必须按 scenario、target skill、arm、model/provider、host/runtime、profile 和 source revision 分层，不把不同环境混成一个结论。至少记录：

- complete、invalid、blocked run 数和 attrition；
- acceptance/correctness/regression 结果；
- coverage、corrections、tools、tokens、wall time、cost 的 mean/median 与 sample SD 或 IQR；
- baseline 与 candidate、baseline 与 base-only 的 paired delta；
- uncertainty interval 或 exact permutation/bootstrap interval；
- scenario-family、holdout 和 sensitivity 结果；
- evidence gaps、contradictions 和 scope；
- aggregate status：`exploratory|inconclusive|decision-grade|blocked`。

失败、超时和 invalid 不得当作零，也不得只保留有利 run。

## 7. 证据门槛和生命周期约束

### 7.1 Claim ladder

| 已完成事项 | 允许的声明 |
| --- | --- |
| 仅创建协议 | 测量合同已定义；没有执行或收益结论。 |
| 一个完整 paired set | 该任务、该环境、该 revision 下的观察和方向性假设。 |
| 多次 paired runs | 受 scenario、model、host、revision 和 protocol scope 限定的经验结果。 |
| lifecycle recommendation | 只有决策级重复证据、无回归、安全门槛、成本门槛和完整 provenance 后，才可给维护者审阅。 |

### 7.2 决策级重复证据的默认门槛

在收集前预先冻结以下门槛：

- 至少 2 个独立 batch；
- 至少 20 个完整 paired scenario instances；
- 至少 4 个 scenario families，每个至少 2 个 instance；
- 至少 3 个未用于调参的 holdout instances；
- 各 arm 观测数相等；
- 报告 paired effect 和 uncertainty；
- 报告 family-level、holdout、invalid/blocked 和 attrition；
- 主要 acceptance/correctness 不能出现 material regression；
- 不能出现 material safety regression；
- cost/latency 只能作为次要门槛，必须在质量底线通过后比较；
- 结果必须明确限定到评测的 model/provider、host/runtime、profile、repository/source revision 和 scenario corpus。

如果目标范围只覆盖一个模型或一个 profile，必须将 recommendation scope 限定在那里，不得写成全局规则。

### 7.3 允许的 recommendation

协议只能输出以下 advisory 状态：

- `inconclusive`
- `retain-current`
- `candidate-for-human-review`
- `blocked`

协议不得输出或自动执行 `promote`、`demote`、`archive`，不得修改 manifest、安装目标、路由、source path、分支或 Git 状态。任何生命周期动作都必须经过维护者审阅，并引用具体 run/batch IDs、source/install hashes、effect、uncertainty、成本、缺口和 rollback condition。

推荐规则：

- 质量不变或改善、约束覆盖不掉、无安全回归、并满足预先声明的实际成本门槛，才可进入 `candidate-for-human-review`。
- 只在命名 scenario family 获益时，保持当前 skill 并考虑将具体内容缩小到 reference；不能只凭 route/coverage 做 outcome promotion。
- 结果混合、方差高、样本不足、telemetry 缺失或环境不一致时，返回 `inconclusive`，保留当前 baseline。
- Archive 需要更高证据门槛、明确缺乏独特安全/路由价值、持续净负收益和维护者明确批准；不能由 runner 自动决定。

## 8. 反污染和可复现约束

- Scenario、oracle、ledger、run metadata 和 evaluator schema 留在 tests/eval 维护面，不进入宿主 runtime 安装目标。
- 评测 harness 不能把 scenario/rubric/ledger prose 作为动态 workflow 的隐式 system instruction；传入 worker 的内容必须是显式用户任务或已 allowlist、已 pin 的 canonical method capsule。
- 模型产生的 evidence/state 是不可信数据，不得直接满足 lifecycle gate；任务 outcome 必须由独立 oracle 复核。
- `targetPaths`、声明的 version/location 或 evidence status 不能证明宿主实际读取沙箱或工具隔离。
- 决策级 run 需要 immutable repository/source tree 和可核验 installed-copy hash；unversioned worktree、alias model、缺失 host revision 或未核验 tool policy 只能标为 exploratory/ineligible。
- 冻结 arm、scenario set、primary metric、阈值、retry/invalid policy 和停止规则后再收集；记录所有尝试、失败、重试和排除。
- 不允许 optional stopping、cherry-picking、只重试有利 arm、跨 arm 共享缓存/记忆/工件或未登记人工介入。
- 本协议本身不是 controller、router、persistent state store 或 workflow platform；不得隐式启动 agent、修改宿主 skill visibility 或创建 nested/sibling orchestration。

## 9. 明确不在本协议范围内

- 不创建第二套运行时架构、profile router 或 source of truth；`profiles/manifest.json` 只拥有非运行时 distribution metadata。
- 不把 `experiments/workflows/adaptive-long-horizon.js` 的结构归位解释成 outcome promotion；它仍是 frozen Lab pilot。
- 不把显式 installer 解释成 global deployment、host enforcement、provider identity、worker isolation 或 outcome runner。
- 不实现 outcome runner、model matrix、telemetry/pricing platform、自动 routing、write-enabled pilot、nested controller 或 lifecycle controller。
- 不因一次成功、静态 assertion、trigger hit、token 下降、reviewer confidence 或 verifier `complete` 而改变生命周期。
- 不把当前 source roots 改成第二套永久 source of truth，也不保留 adaptive old/new 双入口。
- 不执行 promotion、demotion、archive、产品 outcome/A-B 或未经维护者审阅的生命周期动作。

## 10. 协议验收

本协议在以下条件成立前不得进入实际结果采集：

- 三个 arm、treatment isolation 和 target activation 的评分语义已固定；
- scenario source、stable ID、exact fixture 和独立 acceptance oracle 可追溯；
- routing、trajectory、outcome、cost/latency 四类证据不会互相替代；
- 缺失、invalid、blocked、retry 和人工介入有明确处理；
- source/install/model/host/environment provenance 可记录；
- paired set、随机顺序、fresh state 和不污染约束已固定；
- 样本、holdout、质量底线、成本门槛和 uncertainty 规则已在收集前冻结；
- 输出只能是 advisory recommendation，不能自动改变生命周期；
- 当前没有 runner 的事实和所有未执行限制已明确记录。
