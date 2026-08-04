# agent-skills-main 吸收迁移记录

## 状态、范围与归档边界

- **状态：** 已归档（2026-08-04）。本文件保留为根目录的唯一迁移历史记录；未猜测或新建 `docs/`、`archive/`、`maintenance/`、`history/` 或 `records/` 目录。
- **当前仓库：** `E:\projects\_drafts`，归档前分支为 `migrate-meta-define`，归档前根快照为 `0915a55db2a72ce9bee9d47aaa61024472a82cd8`。迁移基线记录为 `f82a1b2`；target 没有独立 Git 元数据或可确认 revision。
- **来源与比较输入：** `addyosmani/agent-skills`，参考地址为 <https://github.com/addyosmani/agent-skills>；`absorb-agent-skills-master-prompt.md` 与 `agent-skills-main/` 继续是未跟踪的比较输入，不是当前项目运行时指令源。
- **许可限定：** target 的实际 `LICENSE` 观察为 GNU AGPL v3；target manifest 的 `MIT` 字段是观察到的元数据不一致。该事实不构成当前仓库或 current-owned plugin 的许可结论，详见 [`CREDITS.md`](CREDITS.md)。
- **动作边界：** 本次迁移未执行 target scripts、hooks、evals、commands、CI、browser、network、external service、deployment、production、monitoring、rollback 或真实 credentials/secrets；未 push、创建 PR、merge、删除分支、清理或删除 target。

## 归档原则

本记录只保留已确认的 disposition、当前落点、理由、证据入口、实现引用和验证边界。target 文本、fixture、manifest、命令输出和历史评审材料只作为证据；不把它们转成当前运行时指令、普遍 gate、权限或副作用授权。

Outcome 含义如下：

- **absorbed / merged：** 已按当前 owner 改写或合并，并有独立实现 commit。
- **no-op / retained：** 当前能力或边界已经足够，保持现状，不创建重复 owner 或维护层。
- **skipped：** 经确认不引入 target 内容；不表示目标能力故障。
- **deferred / retained：** 只保留边界或未来决策入口，没有创建持续 gate、结果层或新的 runtime surface。

## 已吸收或合并

| 生命周期/面 | Target 条目 → 当前落点 | 实现 commit |
| --- | --- | --- |
| Meta | `using-agent-skills` → `prompts/`、维护 prompt 与 routing contract；未启用 SessionStart meta-router | `5f98042` |
| Define | `interview-me` → `skills/interview-me/`；`idea-refine` → `skills/idea-refine/`；`spec-driven-development` → `skills/issue-workflow/` 的显式 `spec-authoring` 模式 | `aaeedb1`, `edfc886`, `ec2cdac` |
| Plan | `planning-and-task-breakdown` → `skills/plan-work/references/plan-template.md` | `89ed5fb` |
| Build | `incremental-implementation` → `skills/plan-work/references/vertical-slices.md`；`context-engineering` → `skills/context-engineering/`；`doubt-driven-development` → `skills/agent-workflow/references/fresh-context-verification.md`；`frontend-ui-engineering` → `skills/frontend-ui-engineering/`；`api-and-interface-design` → `skills/design-codebase/references/api-and-interface-design.md` | `c1581f0`, `6d8e137`, `ef133f7`, `bdd87b6`, `722e65f` |
| Verify | `browser-testing-with-devtools` → `skills/browser-testing-with-devtools/`，仅提供显式 browser/DevTools evidence owner | `1f32856` |
| Review | `code-review-and-quality` → `skills/review-and-finish/references/review-template.md`；`security-and-hardening` → `skills/security-and-hardening/`；`performance-optimization` → `skills/performance-optimization/` | `3df0e10`, `05cfbf2`, `145eba9` |
| Ship | `git-workflow-and-versioning` → `skills/finish-branch/`；`ci-cd-and-automation` → `skills/ci-cd-and-automation/`；`deprecation-and-migration` → `skills/plan-work/references/deprecation-and-migration.md`；`documentation-and-adrs` → `skills/design-codebase/references/domain-modeling.md`；`observability-and-instrumentation` → `skills/observability-and-instrumentation/`；`shipping-and-launch` → `skills/shipping-and-launch/` | `78afc84`, `4647b11`, `a329d9a`, `ae0ba21`, `5882531`, `d689afb` |
| Infrastructure / agents | `security-auditor` → `security-and-hardening`；`web-performance-auditor` → `performance-optimization` | `0ca2867`, `ec08152` |
| Infrastructure / orchestration | `orchestration-patterns` + `docs/agents.md` → `agent-workflow` references；不复制 command wiring 或第二 orchestration owner | `d5cafaf` |
| Infrastructure / references | `accessibility-checklist` → UI accessibility reference；`observability-checklist` → observability owner；`performance-checklist` → performance owner；`security-checklist` → security owner | `97a9bdf`, `3ff5ece`, `fa5ad2d`, `68ccac7` |
| Infrastructure / hook | `simplify-ignore` protected-block filter/restore → 显式 opt-in `plugins/simplify-protected-blocks/`；不改变 host `/code-simplify` | `e147a4a` |
| Infrastructure / evals | `evals/README.md` → `tests/eval-contract.md`；`scripts/run-evals.js` Tier 2 runner → `tests/check_routing_contract.py`；`scripts/run-evals-test.js` regression scaffold → `tests/test_eval_contract.py`；`scripts/validate-skills.js` validator → `tests/validate_suite.py`；`scripts/lib/skill-lint.js` lint → validator 内 current-owned checks | `332d71b`, `1b4065a`, `37f5ef9`, `03db3b3`, `458d435` |
| Infrastructure / eval corpus | 24 cases / 45 fixtures 的 disposition → `tests/eval-contract.md`；ownerless negative 与 stale-boundary audit → ownership contract；不复制完整 corpus、fixture workspace、headless executor 或 results layer | `c4da121`, `153e9a7` |
| Infrastructure / command | target `/ship` 的 host-controller/merge 形状 → `shipping-and-launch` 与 non-trigger contract；不复制固定 persona fan-out | `34d8ff2` |
| Attribution | source-license clarification → `CREDITS.md`；保留 target LICENSE 与 manifest metadata 的限定性记录 | `dc9f7ef`（迁移记录 `8a1d604`） |

每个条目的来源、保留内容、未保留内容和 GNU AGPL v3 attribution basis 继续由 [`CREDITS.md`](CREDITS.md) 维护；上表 commit 是 ledger cross-reference，不宣称 target 有可复现 source revision。

## No-op、保留现状与延期保留

| Target 条目/范围 | 结果 | 理由与证据入口 |
| --- | --- | --- |
| `debugging-and-error-recovery` | no-op / retained | 保留 `debug-systematically` 作为唯一项目调试 owner；不创建第二 debug owner 或空 commit。 |
| SessionStart meta injection | no-op / retained | material assumptions、technical tradeoffs、source/evidence 与 action-specific boundaries 已由当前 prompt/Skills 覆盖；不启用第二全局 router。 |
| `definition-of-done` | no-op / retained | target 的 standing universal DoD 与当前按 acceptance、risk 和证据缺口升级的轻量方式冲突；不引入普遍完成门。 |
| hidden patch/materialization | no-op / retained | 不复制 patch application、fixture-to-workspace、temporary Git baseline 或 cleanup 行为；静态 patch shape 不能证明 live executor。 |
| fixture realism / 窄 gate（P2） | no-op / retained | 不把 fixture completeness/realism 扩展为 universal gate；按少数 capability/result case 处理。 |
| eval results / CI delivery boundary（P2） | deferred / retained | 保留 deterministic/local evidence boundary；不创建 `evals/results`、hosted CI status、deployment gate、external grader 或 publication path。 |
| Claude/plugin manifest 与多工具范围 | no-op / retained | 保持 current Claude Code-first、自包含 plugin 和 plain-Markdown portability；target manifest/setup text 不证明其他 host discovery、permission、precedence 或 runtime。 |
| adoption/getting-started 与平台 setup docs | no-op / retained | 保留当前 README、README.zh-CN、plugin-local README 和 workflow docs；不承诺未经验证的多平台支持。 |
| 文档/manifest 声称的 validation/CI gates | no-op / retained | current local validators、routing/eval contracts 与 plugin-local tests 只是维护证据，不是 hosted CI、required status 或 release gate。 |
| `.gitattributes`、`.gitignore`（P2） | no-op / retained | 保留当前 metadata state；不复制 target attributes、workflow/generated-file policy 或 cleanup scope。 |

## 跳过的条目

P2 是优先级，不等于自动延期。以下状态按用户确认记录：

| 优先级 | 跳过范围 | 理由 |
| --- | --- | --- |
| P0 | `code-reviewer`、`test-engineer` persona | 分别与 host `/code-review`/`review-and-finish`、`test-strategy` 和按需 verifier 重复；不创建第二 Review/Test owner。 |
| P0 | `source-driven-development`、`code-simplification` | 与 current base、`test-strategy`、`review-and-finish` 和显式 plugin/host boundary 重叠；不复制自动 cleanup、second owner 或 branch action。 |
| P0 | SDD WebFetch cache | prompt-shaped URL/ETag cache、curl/jq、持久化与 network side effects 不能替代 exact current source；不复制或执行 hook。 |
| P1 | `test-driven-development`、`testing-patterns` | current `test-strategy` 已覆盖 TDD mode、fixture、timing、seam 和 acceptance evidence；target examples 不形成独立 owner。 |
| P1 | browser runtime capability gate | 无授权 live browser/DevTools channel；保持 `UNVERIFIED`，不把静态 fixture 当 DOM、console、network 或 screenshot 证据。 |
| P1 | `/spec`、`/plan`、`/planning`、`/build`、`/test`、`/review`、`/code-simplify` | current issue/plan/test/review owners 与 host commands 已覆盖；不复制 target command layer、自动 handoff、固定 gate 或逐任务 commit。 |
| P2 | `/webperf`、`docs/comparison.md` | Performance/browser owner 与当前迁移记录已覆盖需要的边界；没有独立维护价值。 |
| P1 | `validate-commands.js`、Codex/.agents manifests、Antigravity/Gemini wrappers/commands、contributor/anatomy/rule infrastructure | 静态 setup/manifest 不证明 host discovery、permission、command/hook precedence 或 runtime；不扩展当前产品范围。 |

`idea-refine` 虽为 P2，但已完成并列于“已吸收或合并”，不属于延期项目。

## 验证快照与证据层级

- **静态结构/路由证据（2026-08-04）：** `python tests/validate_suite.py` 为 `0 error(s), 0 warning(s)`；`python tests/check_routing_contract.py` 为 `0 error(s), 76 informational overlap(s)`。catalog 覆盖 23/23 个 current Skill，无 duplicate/unknown/missing。
- **仓库内执行证据（2026-08-04）：** `python -m unittest discover -s tests -p 'test_*.py'` 的 16 项 current-owned tests 通过；Capability Harness plugin-local tests 66 项通过；`simplify-protected-blocks` plugin-local tests 3 项通过；`git diff --check` 通过。此前 ledger 中的 Python compile 和各条目 focused checks 仍只作为对应 commit 的历史证据。
- **证据限定：** 上述是当前仓库静态/本地 evidence，不是 live host、model、browser、CI、deployment 或 production proof；plugin-local tests 也不改变 standalone Skill routing。

## 未验证边界

以下事实在本次迁移中没有被证明，不能写成“缺失”或“失败”：

- target scripts、hooks、evals、commands、headless executor、fixture materialization 和 target runtime behavior；
- live host/model/runtime discovery、权限、独立 fresh context、host hook ordering 或 isolation；
- browser/DevTools DOM、console、network、screenshot、focus、accessibility 或 runtime-performance observation；
- network、external services、dependency installation effects、hosted CI、required-status enforcement、deployment、production traffic/health、monitoring、notification、rollout 或 rollback safety；
- persisted-data integrity、migration safety、real credentials、tokens、cookies、keys、secrets，以及 target changed-versus-original state（target 无独立 revision）。

这些限制与 [`README.md`](README.md)、[`CREDITS.md`](CREDITS.md) 和 [`tests/eval-contract.md`](tests/eval-contract.md) 的维护边界一致。`GO`、`BLOCK`、`UNVERIFIED` 仍是证据判断，不是 deploy、rollback、migration、flag、publication、Git 或 cleanup authorization。

## 最终 disposition

- 所有用户批准条目均已完成、no-op、保留现状、跳过或延期保留；没有未记录的批准条目。
- 当前仓库的 runtime surface、owner、routing contract、README 分类、source attribution 和 evidence boundary 保持一致；阶段 7 归档已完成。
- 两个比较输入保持原样：未 staging、未删除、未清理；不把 target 的 `CLAUDE.md`、README、manifest 或其他文本作为当前项目指令。
- 后续若要重新打开 target 范围、改变产品支持范围、配置 live runtime、创建结果/CI gate 或执行外部/分支动作，必须获得新的、动作特定的授权；本记录不预先授予这些动作。
