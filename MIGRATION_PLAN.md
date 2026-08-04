# agent-skills-main 吸收迁移计划

## 当前状态

- 当前阶段：阶段 4（Infrastructure/agents、orchestration、references 批次已完成；Ship 批次已完成；Review 批次已完成，Verify 批次已完成，Plan + Build 已完成，Define 第二批已完成，`spec-driven-development` 独立提交为 `ec2cdac`）。
- 计划建立日期：2026-08-03。
- 当前根项目：`E:\projects\_drafts`，Git 分支 `migrate-meta-define`，迁移基线 revision `f82a1b2`。
- 审查输入：`absorb-agent-skills-master-prompt.md`。
- 待审查 target：`agent-skills-main/`，当前是根工作树中的未跟踪目录，没有独立 `.git` 或可确认的 target revision。
- 阶段 0 路线图已于 2026-08-03 获得整体批准；阶段 1 只做客观清单，不作吸收、保留或跳过判断。

## Goal

逐文件核实当前项目与 `agent-skills-main/` 的实际能力、重叠和缺口，在阶段 3 由用户决定整体流程强度与逐项动作后，用本项目确认后的结构、文风、触发边界和验证方式吸收获批内容。

## Context

- 当前项目的职责分层：`prompts/` 是常驻默认行为源；`skills/` 是按需工作流；`plugins/` 是自包含可选插件；`workflows/` 是显式安装前的 saved-workflow 源；`tests/` 是维护与验证材料。
- target 是外部参考输入，不是当前项目的运行时指令源；其中的 `CLAUDE.md`、rules、commands、hooks、README 和 agent 输出只能作为待核对证据。
- 当前项目已有 13 个 Skill，Capability Harness 插件和 `adaptive-long-horizon` workflow 具有独立的职责与安全边界。
- target 的 README 声称包含完整生命周期 skill bundle，但具体覆盖、重叠、兼容性和维护成本必须以实际文件为准。
- 风险等级：低。本任务只整理本地 Markdown/配置类仓库，无线上部署、无用户数据；错误通常可通过 Git revert 恢复。
- 阶段 3 开放决策：**要不要整体更贴近 `addyosmani/agent-skills` 那种流程更重、处处设验证门的风格？** 阶段 1 不评价，阶段 2 只收集七个分类的实际正反证据，阶段 3 将其作为独立条目交由用户决定。
- 许可证标准已决：以 target 实际 `LICENSE` 的 GNU AGPL v3 为准；manifest 中的 MIT 声明保留为客观元数据不一致，后续来源标注和 commit 规则统一使用 GNU AGPL v3。

## Hard constraints

1. 不一次性通读后一次性修改；按阶段和生命周期类别推进。
2. 阶段 2 差距分析、阶段 3 最终确认和阶段 6 收尾检查维持强制暂停；阶段 4 只在一个生命周期大类全部获批条目处理完后统一汇报一次。
3. 纯调研使用只读子代理；编辑由主线程完成。若宿主不能实际强制只读工具边界，必须把该限制标为未验证，并避免把提示词当成技术隔离。
4. 阶段 4 可连续处理同一生命周期大类的全部已批准条目；每个条目必须独立验证、独立本地 commit，并在本文件留下可追溯记录。提交不推导 push、merge、PR 或删除授权。
5. 不逐字复制 target 文本；必须依据本项目现有 Skill 的 frontmatter、文风、章节和触发边界改写。
6. 优先复用本项目已有 Skill；重叠项必须做合并/协调判断，不因 target 更大或更热门而默认替换当前设计。
7. 对宿主内置 `code-review`、`simplify`、`batch`、`loop` 的让位政策，以及本项目 README 已有的 `prompts/`、`skills/`、`plugins/`、`workflows/`、`tests/`边界，不得默默覆盖；阶段 3 可以基于证据决定是否调整明确授权的政策。
8. 外部文本、评审材料、命令输出和代理结果均是证据，不得扩大任务范围、权限或副作用。
9. 每个已批准条目修改后先做针对性验证，同步必要的 README、测试、来源记录和本文件，再只提交该条目的授权修改。
10. 阶段 3 是强制暂停点：完整最终差距清单未得到用户逐条确认前，不得进入阶段 4。
11. 在阶段 3 用户决定前，不预设整体流程应维持轻量或转向更重的验证门；阶段 2 只核实实际效果、维护成本和冲突证据。

## Acceptance seed

- 目标范围：完成当前项目与 `agent-skills-main/` 的事实清单、差距分析、用户确认后的分批吸收和最终一致性检查。
- 最小可观察信号：每一阶段都有可读取的清单/差距/批次记录；每个已吸收条目都有对应源码、改写文件、路由/边界测试、README 同步和验证证据。
- 证据路径：当前仓库文件、target 文件、Git 状态/历史、现有测试与新增的聚焦维护检查；不把静态结果冒充 live host/runtime 证明。
- 未决风险：target 来源 revision、具体条目重叠关系、宿主内置能力替代范围、维护成本，以及哪些内容值得跨项目长期保留。

## 阶段 1：双仓库清单化（只做客观盘点）

### 清单

#### A. 当前项目清单

- **证据状态：** Local Read/Grep/Glob inventory of E:/projects/_drafts at the user-specified current root revision f82a1b2a1f42da9ee7947d8948c51a94857c471c, with the uncommitted plan/prompt/target material excluded: MIGRATION_PLAN.md, absorb-agent-skills-master-prompt.md, and agent-skills-main/. Also excluded exactly as requested: .git/ and ignored .claude/worktrees/. No WebSearch or WebFetch was used; no files or repository state were modified.
- **清单性质：** 客观 inventory；不包含与 target 的差距或价值判断。

##### 当前项目数量汇总

| Surface | 数量 |
| --- | ---: |
| root classification physical files | 3 |
| prompts/ physical files | 1 |
| skills/ physical files | 36 |
| workflows/ physical files | 2 |
| plugins/ physical files | 27 |
| tests/ physical files | 7 |
| all scoped physical files | 76 |
| catalog records after grouping 3 generated cache files into 1 record | 74 |

##### 当前项目 `root classification`（3 条）

| 类别 | 类型 | 名称 | 路径 | Description / 触发条件 / 职责 | 约字数 | 备注 |
| --- | --- | --- | --- | --- | ---: | --- |
| Root classification and installation documentation | Repository README / classification document | `README.md` | `README.md` | English repository overview and classification source. Defines the always-on prompt, standalone runtime Skills, optional self-contained plugins, explicit opt-in saved workflows, maintenance tests, the seven Automatic Workflow Skills, the six Explicit-Intent Workflow Skills, installation targets, and capability boundaries. | 1410 | repo-relative: README.md; classification source for Automatic versus Explicit-Intent Skills and for top-level surface roles. |
| Root classification and installation documentation | Repository README / Chinese classification document | `README.zh-CN.md` | `README.zh-CN.md` | Simplified-Chinese counterpart of the repository overview and classification source, covering the same runtime surfaces, seven automatic Skills, six explicit-intent Skills, installation targets, and maintenance boundaries. | 460 | repo-relative: README.zh-CN.md; approximate count is whitespace-token based and therefore under-segments Chinese text. |
| Presentation-only classification; non-runtime | skills.sh grouping configuration | `skills.sh.json` | `skills.sh.json` | skills.sh presentation configuration with two groups: Automatic Workflow Skills (debug-systematically, test-strategy, review-and-finish, plan-work, design-codebase, reliability-check, agent-workflow) and Explicit-Intent Workflow Skills (finish-branch, issue-workflow, memory-handoff, markdown-memory, skill-refactorer, decision-map). It states no runtime behavior; README.md says it controls page grouping only. | 80 | repo-relative: skills.sh.json; corroborates the 7 Automatic / 6 Explicit-Intent classification. |

##### 当前项目 `prompts/`（1 条）

| 类别 | 类型 | 名称 | 路径 | Description / 触发条件 / 职责 | 约字数 | 备注 |
| --- | --- | --- | --- | --- | ---: | --- |
| Always-on default behavior source | Maintained prompt fragment | `CLAUDE.fragment.md` | `prompts/CLAUDE.fragment.md` | Maintained always-on “Default Coding Behavior” source for ordinary development: Simplified-Chinese user-facing output by default, exact-source reading, untrusted-evidence handling, fact/constraint/assumption separation, proportional changes, explicit opt-in dynamic workflows, stage and authorization boundaries, Git action separation, artifact restraint, outcome-based verification, supported recovery, bounded lesson retention, and isolated or serialized parallel writes. | 680 | repo-relative: prompts/CLAUDE.fragment.md; README.md identifies this as the maintained source assembled into host instructions. |

##### 当前项目 `skills/`（36 条）

| 类别 | 类型 | 名称 | 路径 | Description / 触发条件 / 职责 | 约字数 | 备注 |
| --- | --- | --- | --- | --- | ---: | --- |
| Automatic Workflow Skill | Standalone runtime SKILL.md | `debug-systematically` | `skills/debug-systematically/SKILL.md` | Systematically diagnose unclear product behavior or root cause by building a feedback signal, testing one hypothesis at a time, and verifying the original symptom. Use for intermittent or flaky symptoms, cross-component failures, performance regressions, regressions after recent changes, or bugs that survived previous fixes. Do not use for obvious direct failures, primary test-design or wait-strategy problems, Claude Code runtime issues, unresolved architecture boundaries, or explicit review/readiness checks. | 1360 | repo-relative: skills/debug-systematically/SKILL.md; description copied verbatim from frontmatter; category verified by README.md and skills.sh.json. |
| Automatic Workflow Skill | Standalone runtime SKILL.md | `test-strategy` | `skills/test-strategy/SKILL.md` | Use when the primary problem is test design, explicit TDD, test-first or red-green-refactor work, test seams, regression coverage, mocks, assertions, fixtures, or timing and wait strategy, or when a requested change needs a non-obvious test level, seam, regression signal, or acceptance proof. Do not use for generic testing explanations, ordinary implementation, unresolved root-cause diagnosis, unresolved architecture or ownership/interface/dependency-boundary decisions, explicit review or feedback handling, or completed-work readiness review. | 770 | repo-relative: skills/test-strategy/SKILL.md; description copied verbatim from frontmatter; category verified by README.md and skills.sh.json. |
| Automatic Workflow Skill | Standalone runtime SKILL.md | `review-and-finish` | `skills/review-and-finish/SKILL.md` | Use when the user explicitly asks to review code, assess or address review or PR feedback, verify whether completed software work is done, fixed, passing, or ready, or check a development artifact before sending or shipping. Also use before a done claim for completed changes affecting persisted data or migrations, authentication, authorization, permissions, public compatibility contracts, concurrency, transactions, or destructive behavior. Do not use for ordinary progress summaries, implementation-only requests, high-risk terminology without a completion claim, or an explicitly invoked bundled `/code-review`. | 1490 | repo-relative: skills/review-and-finish/SKILL.md; description copied verbatim from frontmatter; category verified by README.md and skills.sh.json. |
| Automatic Workflow Skill | Standalone runtime SKILL.md | `plan-work` | `skills/plan-work/SKILL.md` | Use for software implementation planning when the user asks for planning, an implementation plan, approach comparison, task breakdown, roadmap, step-by-step plan, or splitting a feature/refactor into clear implementation slices before the next safe implementation step, or when a requested software implementation has unresolved implementation approach, dependency-ordering, sequencing, migration, compatibility, rollout, or scope decisions that cannot be safely inferred. Do not use when the primary request is an architecture, ownership, interface, seam, or dependency-boundary decision; use design-codebase first when available, then return here for dependent rollout or sequencing planning. Do not use for PRD authoring, issue or tracker drafting/publication, durable multi-session decision-map workflows, ordinary code explanation, or implementation of an already-settled plan. | 700 | repo-relative: skills/plan-work/SKILL.md; description copied verbatim from frontmatter; category verified by README.md and skills.sh.json. |
| Automatic Workflow Skill | Standalone runtime SKILL.md | `design-codebase` | `skills/design-codebase/SKILL.md` | Use when the user asks to make or compare a codebase architecture decision involving module boundaries, ownership, interfaces, seams, adapters, domain language, or a throwaway prototype that answers a design question. Also use during implementation only when a non-obvious architecture, ownership, interface, or dependency-boundary decision blocks the next safe edit; a testability concern qualifies only when it demonstrates that kind of boundary pressure. Do not use for ordinary code explanation, straightforward implementation, general test design, flaky tests, mocks, regression coverage, or implementation of an already selected design. | 1040 | repo-relative: skills/design-codebase/SKILL.md; description copied verbatim from frontmatter; category verified by README.md and skills.sh.json. |
| Automatic Workflow Skill | Standalone runtime SKILL.md | `reliability-check` | `skills/reliability-check/SKILL.md` | Use when the user explicitly challenges the reliability of the agent's current or prior conclusion, evidence, source use, active stage, wrong direction, strategy or workflow drift, stale context, unsupported confidence, hallucination, guessing, source-vs-memory confusion, or example-vs-task confusion, or explicitly asks to reassess one of those concerns. Also use when the user says the agent used the wrong, missing, unread, or outdated source for its current or prior conclusion. Do not use for ordinary status questions, file-inventory questions, routine source-reading requests, general uncertainty, ordinary strategy or approach preference changes, or preventive stage reminders without a stated reliability concern. | 1060 | repo-relative: skills/reliability-check/SKILL.md; description copied verbatim from frontmatter; category verified by README.md and skills.sh.json. |
| Automatic Workflow Skill | Standalone runtime SKILL.md | `agent-workflow` | `skills/agent-workflow/SKILL.md` | Use when the user explicitly asks to parallelize work, coordinate multiple agents, run parallel scouts, split work across independent owners, or coordinate multiple independent verifiers; first perform the orchestration fit check even when the correct result is to keep one owner. Also use when two or more genuinely independent subsystem or artifact slices, repeated per-item pipelines, orthogonal scout questions, or high-stakes candidate-and-review scopes require coordinated ownership and integration with material benefit over one owner. Own decomposition, assignment, evidence handoff, verification coordination, and integration. Do not use for one focused delegation or verifier, small independent tasks without an explicit orchestration request when coordination cost exceeds the benefit, coherent single-owner or shared-root work without an explicit orchestration request, capability-only parallelism, or work already owned by another orchestration layer. | 2550 | repo-relative: skills/agent-workflow/SKILL.md; description copied verbatim from frontmatter; category verified by README.md and skills.sh.json. |
| Explicit-Intent Workflow Skill | Standalone runtime SKILL.md | `finish-branch` | `skills/finish-branch/SKILL.md` | Use when the user explicitly asks to commit changes, push a branch, prepare or create a new PR for a resolved branch, merge local branches, merge a named PR remotely, discard explicitly scoped Git working-tree changes, delete a named local or remote branch, remove a named worktree, or choose how to finish the current branch. Do not use to view or summarize an existing PR, review code, assess readiness or completion, answer read-only branch-status questions, explain Git, discard a non-Git idea, or write a generic PR template; use `review-and-finish` for review and completion verification when installed and available, otherwise leave that portion to the ordinary host workflow. | 1670 | repo-relative: skills/finish-branch/SKILL.md; description copied verbatim from frontmatter; category verified by README.md and skills.sh.json. |
| Explicit-Intent Workflow Skill | Standalone runtime SKILL.md | `issue-workflow` | `skills/issue-workflow/SKILL.md` | Use when the user clearly asks to create, publish, or update a tracker item; turn discussion into a PRD, issue draft, tracker-ready work item, or triage result; or modify tracker state such as status, labels, comments, or closure. Keep ordinary coding, planning, review, and repository-local work-item execution in their own flows. | 670 | repo-relative: skills/issue-workflow/SKILL.md; description copied verbatim from frontmatter; category verified by README.md and skills.sh.json. |
| Explicit-Intent Workflow Skill | Standalone runtime SKILL.md | `memory-handoff` | `skills/memory-handoff/SKILL.md` | Creates or updates a compact handoff or checkpoint for a later session, and resumes work from a user-named or repository-standard handoff artifact. Use when the user explicitly asks to create or update a handoff or checkpoint, prepare one before context compaction, or resume from one. Do not use for ordinary progress summaries, long contexts without explicit handoff intent, or a direct request to run /compact without preparing a handoff. | 1240 | repo-relative: skills/memory-handoff/SKILL.md; description copied verbatim from frontmatter; category verified by README.md and skills.sh.json. |
| Explicit-Intent Workflow Skill | Standalone runtime SKILL.md | `markdown-memory` | `skills/markdown-memory/SKILL.md` | Use when the user clearly asks to record, update, prune, or consult project-governed Markdown reference lessons about repeated mistakes, corrections, or confirmed approaches that must be versioned, shared, reviewable, or otherwise tied to repository history. Do not use for automatically loaded CLAUDE.md or .claude/rules instructions, host auto memory, handoff state, or decision-frontier planning. | 1980 | repo-relative: skills/markdown-memory/SKILL.md; description copied verbatim from frontmatter; category verified by README.md and skills.sh.json. |
| Explicit-Intent Workflow Skill | Standalone runtime SKILL.md | `skill-refactorer` | `skills/skill-refactorer/SKILL.md` | Use when the user clearly asks to refactor, migrate, rewrite, de-duplicate, or clean up an existing coding-agent instruction artifact, such as a SKILL.md, Claude Code prompt, CLAUDE.md fragment, or equivalent agent configuration, while preserving its intended behavior and trigger boundary. Do not use for ordinary code refactors, code or document review, planning, general-purpose writing, translation, or ordinary prompt and copy editing. | 910 | repo-relative: skills/skill-refactorer/SKILL.md; description copied verbatim from frontmatter; category verified by README.md and skills.sh.json. |
| Explicit-Intent Workflow Skill | Standalone runtime SKILL.md | `decision-map` | `skills/decision-map/SKILL.md` | Create, update, or resume a durable multi-session map of unresolved decisions and their dependencies. Use when the user clearly asks for a decision map, wants to track an open decision frontier across sessions, or wants to resume decision work by ticket. Do not use for ordinary implementation planning, one-session design comparison, progress summaries, handoff or checkpoint state, or direct execution of settled decisions. | 2010 | repo-relative: skills/decision-map/SKILL.md; description copied verbatim from frontmatter; category verified by README.md and skills.sh.json. |
| Conditional reference owned by debug-systematically | Skill reference | `Root Cause Tracing` | `skills/debug-systematically/references/root-cause-tracing.md` | Use when a failure appears deep in a call stack but the bad input or decision likely happened earlier; trace callers upward to the earliest creation or acceptance point, fix at the source, and remove temporary traces. | 170 | repo-relative: skills/debug-systematically/references/root-cause-tracing.md. |
| Conditional reference owned by debug-systematically | Skill reference | `Defense In Depth` | `skills/debug-systematically/references/defense-in-depth.md` | Use after finding a root cause involving invalid data, unsafe paths, missing state, or assumptions another caller can bypass; select only fitting entry, domain, environment, and diagnostic layers. | 150 | repo-relative: skills/debug-systematically/references/defense-in-depth.md. |
| Conditional reference owned by test-strategy | Skill reference | `Good Tests` | `skills/test-strategy/references/good-tests.md` | Use tests that describe observable behavior and survive internal refactors; covers preferred public seams, anti-patterns, and regression coverage that exercises the real failure path. | 150 | repo-relative: skills/test-strategy/references/good-tests.md. |
| Conditional reference owned by test-strategy | Skill reference | `Mocking` | `skills/test-strategy/references/mocking.md` | Mocks isolate boundaries rather than serving as the behavior under test; identifies suitable external or nondeterministic targets, mock anti-patterns, and a four-question gate. | 160 | repo-relative: skills/test-strategy/references/mocking.md. |
| Conditional reference owned by test-strategy | Skill reference | `Flaky Tests` | `skills/test-strategy/references/flaky-tests.md` | Use when tests pass intermittently, fail under load, depend on timing, or contain guessed sleeps; replace sleeps with condition-based waits and prefer existing helpers or deterministic time control. | 220 | repo-relative: skills/test-strategy/references/flaky-tests.md. |
| Conditional reference owned by test-strategy | Skill reference | `TDD Mode` | `skills/test-strategy/references/tdd-mode.md` | Use when the user explicitly asks for TDD, test-first, or red-green-refactor; defines the single-behavior red/green/refactor cycle and existing-code guardrails. | 190 | repo-relative: skills/test-strategy/references/tdd-mode.md. |
| Conditional reference owned by plan-work | Skill reference | `Vertical Slices` | `skills/plan-work/references/vertical-slices.md` | Use vertical slices when a feature, refactor, or PRD is too large for one safe pass; each slice should deliver a narrow complete path that is independently demonstrable or verifiable. | 190 | repo-relative: skills/plan-work/references/vertical-slices.md. |
| Conditional reference owned by plan-work | Skill reference / template | `Plan Template` | `skills/plan-work/references/plan-template.md` | Template for durable plans, handoffs, or work spanning sessions, with goal, context, approach, file ownership, executable steps, risks, verification, and a self-check. | 230 | repo-relative: skills/plan-work/references/plan-template.md. |
| Conditional reference owned by plan-work | Skill reference | `Design Questions` | `skills/plan-work/references/design-questions.md` | Use only when a request is too vague to plan safely; offers focused clarification and option-comparison questions plus stop conditions for conflicting or user-owned decisions. | 180 | repo-relative: skills/plan-work/references/design-questions.md. |
| Conditional reference owned by design-codebase | Skill reference | `Deep Modules` | `skills/design-codebase/references/deep-modules.md` | Design modules that provide meaningful behavior through small interfaces; defines module/interface/seam/adapter/depth/locality vocabulary and deep-versus-shallow signals. | 210 | repo-relative: skills/design-codebase/references/deep-modules.md. |
| Conditional reference owned by design-codebase | Skill reference | `Deepening` | `skills/design-codebase/references/deepening.md` | Use when improving a cluster of shallow modules or choosing where a seam belongs; classifies dependency types and gives an incremental caller/leakage/interface method. | 250 | repo-relative: skills/design-codebase/references/deepening.md. |
| Conditional reference owned by design-codebase | Skill reference | `Domain Modeling` | `skills/design-codebase/references/domain-modeling.md` | Use when architecture depends on precise domain language or the user asks to name concepts, define a glossary, or record an architectural decision; covers compact glossary and ADR gates. | 180 | repo-relative: skills/design-codebase/references/domain-modeling.md. |
| Conditional reference owned by design-codebase | Skill reference | `Design It Twice` | `skills/design-codebase/references/design-it-twice.md` | Use when the first interface idea is plausible but the trade-off merits comparison; generate only materially distinct options, compare decision-relevant criteria, and finish with a recommendation. | 220 | repo-relative: skills/design-codebase/references/design-it-twice.md. |
| Conditional reference owned by design-codebase | Skill reference | `Prototypes` | `skills/design-codebase/references/prototypes.md` | Build a prototype only when runnable feedback is needed for one design question; defines the automatic local throwaway gate, exact command/effect disclosure, logic and UI prototype shapes, ownership, cleanup, and approval-required boundary. | 890 | repo-relative: skills/design-codebase/references/prototypes.md. |
| Conditional reference owned by review-and-finish | Skill reference | `Feedback Handling` | `skills/review-and-finish/references/feedback-handling.md` | Use when the user supplies review comments, PR feedback, static-analysis findings, or another model/tool’s advice; read, verify, triage, separate assessment from implementation, and run focused checks after authorized changes. | 270 | repo-relative: skills/review-and-finish/references/feedback-handling.md. |
| Conditional reference owned by review-and-finish | Skill reference / template | `Review Template` | `skills/review-and-finish/references/review-template.md` | Use for code, PR, branch, or since-ref review; limits review to selected scope and affected contracts, prioritizes correctness and risk, and defines findings-first output and severity guidance. | 240 | repo-relative: skills/review-and-finish/references/review-template.md. |
| Conditional orchestration pattern owned by agent-workflow | Skill reference | `Review Panel` | `skills/agent-workflow/references/review-panel.md` | Use after agent-workflow is active only for a high-stakes single artifact where multiple genuinely plausible candidates and reviewers are worth the cost; judge against an explicit rubric. | 160 | repo-relative: skills/agent-workflow/references/review-panel.md. |
| Conditional orchestration pattern owned by agent-workflow | Skill reference | `Pipeline Processing` | `skills/agent-workflow/references/pipeline-processing.md` | Use after agent-workflow is active for a batch of similar items moving through the same small stage sequence; share one compact contract, preserve per-item outcomes, and aggregate only missing verification. | 190 | repo-relative: skills/agent-workflow/references/pipeline-processing.md. |
| Conditional orchestration pattern owned by agent-workflow | Skill reference | `Fresh-Context Verification` | `skills/agent-workflow/references/fresh-context-verification.md` | Use only after agent-workflow is active when milestone risk or blind-spot cost justifies a separate verifier in an existing multi-slice workflow; defines verifier inputs, role, and evidence reuse. | 290 | repo-relative: skills/agent-workflow/references/fresh-context-verification.md. |
| Conditional orchestration pattern owned by agent-workflow | Skill reference | `Scout Slices` | `skills/agent-workflow/references/scout-slices.md` | Use after agent-workflow is active when two or more orthogonal investigation questions can proceed independently; defines scout ownership, split axes, evidence-bearing output, deduplication, and stop conditions. | 370 | repo-relative: skills/agent-workflow/references/scout-slices.md. |
| Conditional orchestration pattern owned by agent-workflow | Skill reference | `File Handoffs` | `skills/agent-workflow/references/file-handoffs.md` | Use after agent-workflow is active when prompts or reports are too long for clean controller-agent exchange; prioritizes host-managed or producer-local state, then uniquely owned ignored project scratch files with containment and cleanup rules. | 510 | repo-relative: skills/agent-workflow/references/file-handoffs.md. |
| Conditional reference owned by skill-refactorer | Skill reference / checklist | `Compression Checklist` | `skills/skill-refactorer/references/compression-checklist.md` | Use only after skill-refactorer is active and the main file remains too procedural; distinguishes compressible repetition from trigger, safety, routing, and failure behavior that must remain. | 240 | repo-relative: skills/skill-refactorer/references/compression-checklist.md. |
| Maintenance calibration data; non-runtime | Skill evaluation dataset (JSON) | `agent-workflow evals` | `skills/agent-workflow/evals/evals.json` | Twenty-two agent-workflow calibration cases covering sole-controller ownership, fit-check stay-solo behavior, domain-method composition, focused delegation versus orchestration, nested-controller depth, carry-forward state, transient handoffs, unavailable-sibling and unavailable-agent fallbacks, worker failure, prompt-injection fixtures, resource gates, required context independence, and enforced read-only boundaries. | 2460 | repo-relative: skills/agent-workflow/evals/evals.json; eval IDs 1–19 and 27–29. |

##### 当前项目 `workflows/`（2 条）

| 类别 | 类型 | 名称 | 路径 | Description / 触发条件 / 职责 | 约字数 | 备注 |
| --- | --- | --- | --- | --- | ---: | --- |
| Explicit opt-in saved-workflow source documentation | Saved-workflow documentation | `Workflow Sources README` | `workflows/README.md` | Documents workflows/ as versioned saved-workflow source rather than a discovery directory; specifies Claude Code 2.1.154+, explicit installation targets, adaptive-long-horizon input fields, candidate-versus-verified evidence, session-local state, lexical target-path bounds, prompt-constrained read policy, verifier boundary, and pilot exclusions. | 710 | repo-relative: workflows/README.md; documents the only workflow source in this surface. |
| Explicit opt-in saved workflow; not automatic skill routing | Claude Code dynamic saved-workflow JavaScript source | `adaptive-long-horizon` | `workflows/adaptive-long-horizon.js` | Run a bounded, prompt-constrained, session-local evidence loop for an explicitly supplied task | 3320 | repo-relative: workflows/adaptive-long-horizon.js; description copied exactly from meta.description; implements bounded input normalization, up to three investigation rounds/four total agents, candidate evidence, contradiction and progress state, and fresh-context completion verification. |

##### 当前项目 `plugins/`（25 条）

| 类别 | 类型 | 名称 | 路径 | Description / 触发条件 / 职责 | 约字数 | 备注 |
| --- | --- | --- | --- | --- | ---: | --- |
| Optional self-contained plugin documentation | Plugin README | `Capability Harness README` | `plugins/capability-harness/README.md` | Self-contained Claude Code plugin documentation for project-scoped, decision-first capability amplification. Describes local installation and validation, five namespaced agents, two hooks, pre-action route behavior, context discovery, Python/runtime requirements, calibration data, and manual positive/negative examples. | 850 | repo-relative: plugins/capability-harness/README.md. |
| Optional plugin manifest, version 0.6.5 | Claude Code plugin manifest | `capability-harness plugin manifest` | `plugins/capability-harness/.claude-plugin/plugin.json` | Adds a project-scoped decision-first capability control plane and five focused leaf agents for Claude Code. | 30 | repo-relative: plugins/capability-harness/.claude-plugin/plugin.json; description copied exactly from manifest. |
| Optional plugin runtime Skill: capability-harness:capability-harness | Namespaced plugin SKILL.md | `capability-harness` | `plugins/capability-harness/skills/capability-harness/SKILL.md` | Apply a decision-first capability-harness pass to substantive work when a model may miss context, evidence, an observable check, or a materially different alternative. When the prompt hook selects a pre-action route, execute exactly that one route before material work and integrate its bounded result. Do not use for routine direct work, fixed pipelines, cosmetic variants, or work already owned by another controller. | 1220 | repo-relative: plugins/capability-harness/skills/capability-harness/SKILL.md; description copied verbatim from frontmatter. |
| Leaf agent: capability-harness:context-scout | Namespaced plugin agent definition | `context-scout` | `plugins/capability-harness/agents/context-scout.md` | Leaf pre-action decision-brief worker for one open-ended task where missing domain context may materially improve the approach or result. When the prompt hook selects bounded context discovery, execute this one route before material generation; otherwise use only when a controller explicitly assigns the same bounded question. Search bounded public sources, distill them into an actionable brief, and do not implement, copy a reference artifact, or make the final task decision. | 870 | repo-relative: plugins/capability-harness/agents/context-scout.md; frontmatter tools are Read, Grep, Glob, WebSearch, WebFetch; maxTurns 24; description copied verbatim. |
| Leaf agent: capability-harness:evidence-researcher | Namespaced plugin agent definition | `evidence-researcher` | `plugins/capability-harness/agents/evidence-researcher.md` | Leaf evidence worker for one controller-assigned material uncertainty requiring scoped repository facts or current official or primary public sources. When the prompt hook selects focused evidence research, execute this one route before material generation or recommendation; otherwise use only with a bounded controller-assigned question. Respect explicit source and data boundaries and the built-in return and stop contract; do not use as a general planner, reviewer, implementer, or autonomous router. | 600 | repo-relative: plugins/capability-harness/agents/evidence-researcher.md; frontmatter tools are Read, Grep, Glob, WebSearch, WebFetch; maxTurns 20; description copied verbatim. |
| Leaf agent: capability-harness:independent-brancher | Namespaced plugin agent definition | `independent-brancher` | `plugins/capability-harness/agents/independent-brancher.md` | Leaf alternative-generation worker for one bounded design, plan, optimization, or implementation question where a materially different approach could change the outcome. Use only with settled hard constraints, relevant project context, an independence boundary, and a validation and stop contract; do not use for cosmetic variants, carrying out implementation, final selection, or autonomous orchestration. | 430 | repo-relative: plugins/capability-harness/agents/independent-brancher.md; frontmatter tools are Read, Grep, Glob; maxTurns 16; description copied verbatim. |
| Leaf agent: capability-harness:execution-verifier | Namespaced plugin agent definition | `execution-verifier` | `plugins/capability-harness/agents/execution-verifier.md` | Leaf verification worker for one controller-assigned claim that can be checked against an identified repository state, artifact, or environment with bounded observable inspection or execution. Use only after the target identity, exact permitted check, and acceptance signal are resolved; do not use for implementation, broad review, unsafe commands, or autonomous completion claims. | 660 | repo-relative: plugins/capability-harness/agents/execution-verifier.md; frontmatter tools are Read, Grep, Glob, Bash; maxTurns 20; description copied verbatim. |
| Leaf agent: capability-harness:skeptical-evaluator | Namespaced plugin agent definition | `skeptical-evaluator` | `plugins/capability-harness/agents/skeptical-evaluator.md` | Leaf evaluation worker for controller-supplied candidate artifacts or results when deterministic checks do not cover an important quality dimension. Use only with actual candidates, hard constraints, project facts, and observable evidence; do not use to generate candidates, rewrite artifacts, authorize actions, or replace the active review or design method. | 380 | repo-relative: plugins/capability-harness/agents/skeptical-evaluator.md; frontmatter tools are Read, Grep, Glob; maxTurns 18; description copied verbatim. |
| Runtime hook registration | Plugin hook configuration | `hooks.json` | `plugins/capability-harness/hooks/hooks.json` | Registers a project-scoped UserPromptSubmit command hook running user_prompt_submit.py and a SubagentStop command hook running subagent_stop.py for exactly the five capability-harness agent names; both invoke `python -B` with five-second timeouts. | 60 | repo-relative: plugins/capability-harness/hooks/hooks.json. |
| Runtime hook implementation unit | Plugin hook Python library | `common.py` | `plugins/capability-harness/hooks/lib/common.py` | Shared hook implementation unit containing English and Chinese regex signal sets, stdin/stdout JSON helpers, prompt classification, candidate-action calculation, and conservative selection among direct, project_inspection, evidence_research, and context_discovery pre-action routes. | 690 | repo-relative: plugins/capability-harness/hooks/lib/common.py. |
| Runtime UserPromptSubmit implementation unit | Plugin hook Python executable | `user_prompt_submit.py` | `plugins/capability-harness/hooks/user_prompt_submit.py` | UserPromptSubmit implementation that reads the prompt event, honors `[harness:off]` and explicit controller ownership, classifies the prompt, remains silent on the direct route, and otherwise emits one selected project-inspection, focused-evidence, or context-discovery contract as hook additionalContext. | 660 | repo-relative: plugins/capability-harness/hooks/user_prompt_submit.py. |
| Runtime SubagentStop implementation unit | Plugin hook Python executable | `subagent_stop.py` | `plugins/capability-harness/hooks/subagent_stop.py` | SubagentStop implementation that validates required top-level headings, order, and non-empty sections for each recognized namespaced agent, including blocked and context-scout skip contracts; emits a block correction when the contract is malformed and avoids recursive blocking when stop_hook_active is set. | 640 | repo-relative: plugins/capability-harness/hooks/subagent_stop.py. |
| Reference documentation; not an additional runtime component | Plugin maintainer reference | `Architecture` | `plugins/capability-harness/references/architecture.md` | Maintainer reference defining the plugin objective, control plane versus capability plane, component mapping, decision-first state machine, project-scoped deployment boundary, and reliability limits. | 740 | repo-relative: plugins/capability-harness/references/architecture.md. |
| Reference documentation; not an additional runtime component | Plugin maintainer reference | `Decision-First Routing Policy` | `plugins/capability-harness/references/routing-policy.md` | Maintainer reference for decision-first routing: pre-action test, transient acceptance seed, three strong hook routes, direct path, context discovery, evidence acquisition, alternatives/observation/evaluation, capability limits, and escalation budget. | 1000 | repo-relative: plugins/capability-harness/references/routing-policy.md. |
| Canonical reference contract; SubagentStop minimums derive from it | Plugin maintainer reference / contract | `Capability Contracts` | `plugins/capability-harness/references/capability-contracts.md` | Canonical plugin delegation contracts for the acceptance seed and all five agents, including required and optional return headings, blocked/skip forms, public-source inheritance boundaries, ownership, and integration. | 1240 | repo-relative: plugins/capability-harness/references/capability-contracts.md. |
| Evidence-policy reference | Plugin maintainer reference | `Evidence Policy` | `plugins/capability-harness/references/evidence-policy.md` | Defines evidence precedence, compact evidence cards, current/version-specific verification, adjacent-problem research order, explicit transfer assumptions, and untrusted external-content handling. | 260 | repo-relative: plugins/capability-harness/references/evidence-policy.md. |
| Evaluation-policy reference | Plugin maintainer reference | `Evaluation Policy` | `plugins/capability-harness/references/evaluation-policy.md` | Defines evaluation order, task-derived quality dimensions, capability-decision calibration, judge controls, preserve-best acceptance, and a completion rule while keeping verification, evaluation, and overall completion distinct. | 460 | repo-relative: plugins/capability-harness/references/evaluation-policy.md. |
| Failure-recovery reference | Plugin maintainer reference | `Failure Recovery` | `plugins/capability-harness/references/failure-recovery.md` | Failure handling for unavailable or conflicting evidence, noisy retrieval, empty context briefs, subagent format failure, duplicate agents, evaluation disagreement, tool failure, revision regression, context saturation, early stopping, recursive delegation, and retrieved prompt injection. | 490 | repo-relative: plugins/capability-harness/references/failure-recovery.md. |
| Installation and operation reference | Plugin maintainer reference | `Installation and Operation` | `plugins/capability-harness/references/installation.md` | Documents local-scope marketplace installation, one-session source loading, repository validation, Python requirements, explicit namespaced invocation, per-prompt opt-out, and the project-only deployment boundary. | 320 | repo-relative: plugins/capability-harness/references/installation.md. |
| Design-intent reference | Plugin maintainer reference | `Design Intent` | `plugins/capability-harness/references/design-intent.md` | Explains the pre-action capability-amplifier purpose, non-normative decision profile, routing intent, non-goals, and maintenance rules tying routing or role changes to architecture, policy, contracts, and calibration cases. | 720 | repo-relative: plugins/capability-harness/references/design-intent.md. |
| Maintenance test; non-runtime | Plugin deterministic test module | `RoutingHookTests` | `plugins/capability-harness/tests/test_routing_hooks.py` | Thirty-eight unittest cases for UserPromptSubmit routing: project-first inspection, open-ended context discovery, current-evidence research, fixed/direct negatives, explicit source/delegation constraints, controller ownership, slash-prefix handling, project/no-project distinctions, opt-out and no-state behavior, acceptance-seed text, and hook registration. | 1000 | repo-relative: plugins/capability-harness/tests/test_routing_hooks.py. |
| Maintenance test; non-runtime | Plugin deterministic test module | `SubagentStopHookTests` | `plugins/capability-harness/tests/test_subagent_stop.py` | Twenty unittest cases for SubagentStop output-contract validation across all five agents: success, blocked and skip contracts, heading case/order/content/fence rules, retry behavior, malformed or unrelated input, and hook/agent registration. | 690 | repo-relative: plugins/capability-harness/tests/test_subagent_stop.py. |
| Maintenance test; non-runtime | Plugin deterministic contract test module | `ReferenceContractTests` | `plugins/capability-harness/tests/test_reference_contracts.py` | Eight unittest cases asserting the complete eight-reference inventory, Skill links, agent minimum contracts, inherited public-search/stop wording, controller-owned acceptance seed, evidence-only verifier boundary, exact authorized-check contract, and project-local installation. | 380 | repo-relative: plugins/capability-harness/tests/test_reference_contracts.py. |
| Maintenance calibration data; explicitly not automated Hook tests | Plugin Skill evaluation dataset (JSON) | `capability-harness evals` | `plugins/capability-harness/skills/capability-harness/evals/evals.json` | Twelve capability-harness calibration entries covering current vendor evidence, independent alternatives plus verification/evaluation, rendered artifact evidence, direct spelling and known-bug paths, existing-controller ownership, bounded observable checking, open-ended and unfamiliar-domain discovery, fixed artifact direct routing, and acceptance-seed behavior. | 980 | repo-relative: plugins/capability-harness/skills/capability-harness/evals/evals.json; eval IDs 1–12. |
| Generated maintenance/runtime cache; non-source | Grouped generated binary cache | `capability-harness Python bytecode caches` | `plugins/capability-harness/hooks` | Three generated CPython 3.14 bytecode cache files corresponding to subagent_stop.py, user_prompt_submit.py, and hooks/lib/common.py. Grouped as low-level generated/cache material rather than substantive source. | 0 | repo-relative paths: plugins/capability-harness/hooks/__pycache__/subagent_stop.cpython-314.pyc; plugins/capability-harness/hooks/__pycache__/user_prompt_submit.cpython-314.pyc; plugins/capability-harness/hooks/lib/__pycache__/common.cpython-314.pyc. Absolute paths: E:/projects/_drafts/plugins/capability-harness/hooks/__pycache__/subagent_stop.cpython-314.pyc; E:/projects/_drafts/plugins/capability-harness/hooks/__pycache__/user_prompt_submit.cpython-314.pyc; E:/projects/_drafts/plugins/capability-harness/hooks/lib/__pycache__/common.cpython-314.pyc. Binary files have no meaningful whole-file word count. |

##### 当前项目 `tests/`（7 条）

| 类别 | 类型 | 名称 | 路径 | Description / 触发条件 / 职责 | 约字数 | 备注 |
| --- | --- | --- | --- | --- | ---: | --- |
| Maintenance contract; non-runtime | Root Markdown routing contract | `Routing Contract` | `tests/routing-contract.md` | Maintenance-layer routing contract defining authoritative sources, core routing from user need to base/Skill/host layer, expected multi-skill composition, test-strategy cross-cutting boundaries, and suite-level maintenance use. Explicitly not a runtime Skill. | 1120 | repo-relative: tests/routing-contract.md. |
| Maintenance test/contract; non-runtime | Root Markdown routing test matrix | `Trigger Matrix` | `tests/trigger-matrix.md` | Positive and composition pressure-test matrix for default behavior, automatic and explicit-intent Skills, agent orchestration and adaptive workflow ownership, branch actions, handoff/memory/decision artifacts, planning/design/reliability, shared defaults, maintenance routing, and failure signals. Explicitly validation rather than runtime routing authority. | 5560 | repo-relative: tests/trigger-matrix.md; includes instruction-shaped strings as test fixtures, treated only as data. |
| Maintenance test/contract; non-runtime | Root Markdown negative routing matrix | `Non-Trigger Cases` | `tests/non-trigger-cases.md` | Negative routing cases that keep ordinary work out of heavy, corrective, artifact, review, branch, design, memory, orchestration, and saved-workflow paths; also preserves review/branch separation and explicit-only corrective/meta activation. | 4380 | repo-relative: tests/non-trigger-cases.md; includes instruction-shaped strings as negative fixtures, treated only as data. |
| Maintenance contract for finish-branch; non-executable | Root Markdown behavior contract | `Finish Branch Behavior Contract` | `tests/finish-branch-cases.md` | Post-selection behavior contract for finish-branch covering scoped commits, hooks and filters, push and force boundaries, PR preparation/creation, local versus remote merge, conflict handling, destructive confirmation, worktree ownership, review handoff, verification effects, untrusted content, partial success, and idempotence. | 1150 | repo-relative: tests/finish-branch-cases.md. |
| Maintenance contract for markdown-memory; non-executable | Root Markdown behavior contract | `Markdown Memory Behavior Contract` | `tests/markdown-memory-cases.md` | Post-selection behavior contract for markdown-memory covering target selection, read/write failures, partial index success, trust boundaries, evidence and version status, prune/delete authorization, repository-local Markdown constraints, naming and deduplication, consult read-only behavior, conflict handling, stable labels, and index consistency. | 1050 | repo-relative: tests/markdown-memory-cases.md. |
| Maintenance contract for skill-refactorer; non-executable | Root Markdown behavior contract | `Skill Refactorer Behavior Contract` | `tests/skill-refactorer-cases.md` | Post-selection behavior contract for skill-refactorer covering exact target scope, read-only versus modification modes, untrusted embedded text, verified replacement-source equivalence, unavailable sibling handling, reference integrity, behavior-boundary preservation, non-SKILL targets, no-op completion, and repeated-pass idempotence. | 540 | repo-relative: tests/skill-refactorer-cases.md. |
| Executable maintenance test for saved workflow source | Root Python contract test | `AdaptiveLongHorizonContractTests` | `tests/test_adaptive_long_horizon.py` | Six unittest contract checks for adaptive-long-horizon: prompt-constrained workflow shape, input/evidence limits, location and repeated-question guards, candidate-reference constraints, absence of direct side-effect APIs, and documentation/matrix preservation of the runtime evidence boundary. | 160 | repo-relative: tests/test_adaptive_long_horizon.py. |

##### 当前项目结构事实

- The scoped inventory contains 76 physical files: 36 under skills/, 1 under prompts/, 2 under workflows/, 27 under plugins/, 7 under tests/, and 3 root classification files.
- The catalog has 74 records because the three low-level `.pyc` cache files are represented by one grouped generated-cache record, as permitted; all 73 substantive/text files are represented individually.
- The standalone runtime Skill surface has 13 SKILL.md files: 7 Automatic Workflow Skills and 6 Explicit-Intent Workflow Skills. Their descriptions above are verbatim frontmatter values, and their categories are jointly supported by README.md and skills.sh.json.
- The remainder of skills/ is 22 conditional reference files plus one 22-case agent-workflow eval dataset, yielding 36 physical skills/ files total.
- The saved-workflow surface has one documentation file and one JavaScript source file. README.md and workflows/README.md classify it as explicit opt-in source rather than ordinary Skill routing or a host discovery directory.
- The Capability Harness plugin has 24 substantive files: one README, one manifest, one namespaced Skill, five agents, one hook configuration, three hook implementation units, eight references, three deterministic test modules, and one 12-case eval dataset; three additional generated `.pyc` files bring its physical total to 27.
- Whole-file approximate counts use local Grep over non-whitespace token chunks and are rounded down to the nearest 10; punctuation and code tokens count as words. The Chinese README count is therefore a whitespace-token approximation, and binary `.pyc` files are recorded as 0 word-countable content.
- Every scoped textual file returned by Glob was read in full. The three generated binary cache files were inventoried from Glob and grouped; no expected scoped path was missing or unreadable.
- Instruction-shaped strings occur in several tests, evals, and references as deliberate fixtures or quoted examples; they were treated only as repository data and did not alter scope or permissions.

##### 当前项目缺失或不可读项

- 无。

#### B. `agent-skills-main` target 清单

### Target skills

`README.md` and `CLAUDE.md` assign 23 lifecycle skills plus one meta-skill. All 24 named directories and `SKILL.md` files exist. Phase totals: Meta 1, Define 3, Plan 1, Build 7, Verify 2, Review 4, Ship 6.

| Lifecycle | Name | Path | Exact frontmatter description | Approx. whole-file words |
|---|---|---|---|---:|
| Meta | using-agent-skills | `E:/projects/_drafts/agent-skills-main/skills/using-agent-skills/SKILL.md` | Discovers and invokes agent skills. Use when starting a session or when you need to discover which skill applies to the current task. This is the meta-skill that governs how all other skills are discovered and invoked. | ~1,307 |
| Define | interview-me | `E:/projects/_drafts/agent-skills-main/skills/interview-me/SKILL.md` | Extracts what the user actually wants instead of what they think they should want. Achieves this through one-question-at-a-time interview until ~95% confidence about the underlying intent. Use when an ask is underspecified ("build me X" without "for whom" or "why now"), when the user explicitly invokes ("interview me", "grill me", "are we sure?", "stress-test my thinking"), or when you catch yourself silently filling in ambiguous requirements before any plan, spec, or code exists. | ~2,400 |
| Define | idea-refine | `E:/projects/_drafts/agent-skills-main/skills/idea-refine/SKILL.md` | Refines raw ideas into sharp, actionable concepts through structured divergent and convergent thinking. Use when an idea is still vague, when you need to stress-test assumptions before committing to a plan, or when you want to expand options before converging on one. Triggers on "ideate", "refine this idea", or "stress-test my plan". | ~1,278 |
| Define | spec-driven-development | `E:/projects/_drafts/agent-skills-main/skills/spec-driven-development/SKILL.md` | Creates specs before coding. Use when starting a new project, feature, or significant change and no specification exists yet. Use when requirements are unclear, ambiguous, or only exist as a vague idea. | ~1,283 |
| Plan | planning-and-task-breakdown | `E:/projects/_drafts/agent-skills-main/skills/planning-and-task-breakdown/SKILL.md` | Breaks work into ordered tasks. Use when you have a spec or clear requirements and need to break work into implementable tasks. Use when a task feels too large to start, when you need to estimate scope, or when parallel work is possible. | ~1,260 |
| Build | incremental-implementation | `E:/projects/_drafts/agent-skills-main/skills/incremental-implementation/SKILL.md` | Delivers changes incrementally. Use when implementing any feature or change that touches more than one file. Use when you're about to write a large amount of code at once, or when a task feels too big to land in one step. | ~1,477 |
| Build | test-driven-development | `E:/projects/_drafts/agent-skills-main/skills/test-driven-development/SKILL.md` | Drives development with tests. Use when implementing any logic, fixing any bug, or changing any behavior. Use when you need to prove that code works, when a bug report arrives, or when you're about to modify existing functionality. | ~2,438 |
| Build | context-engineering | `E:/projects/_drafts/agent-skills-main/skills/context-engineering/SKILL.md` | Optimizes agent context setup. Use when starting a new session, when agent output quality degrades, when switching between tasks, or when you need to configure rules files and context for a project. | ~1,590 |
| Build | source-driven-development | `E:/projects/_drafts/agent-skills-main/skills/source-driven-development/SKILL.md` | Grounds every implementation decision in official documentation. Use when you want authoritative, source-cited code free from outdated patterns. Use when building with any framework or library where correctness matters. | ~1,194 |
| Build | doubt-driven-development | `E:/projects/_drafts/agent-skills-main/skills/doubt-driven-development/SKILL.md` | Subjects every non-trivial decision to a fresh-context adversarial review before it stands. Use when correctness matters more than speed, when working in unfamiliar code, when stakes are high (production, security-sensitive logic, irreversible operations), or any time a confident output would be cheaper to verify now than to debug later. | ~2,562 |
| Build | frontend-ui-engineering | `E:/projects/_drafts/agent-skills-main/skills/frontend-ui-engineering/SKILL.md` | Builds production-quality, accessible, responsive user-facing UIs. Use when building or modifying interfaces and pages, creating components, implementing layouts, meeting WCAG accessibility requirements, managing state, or when the output needs to look and feel production-quality rather than AI-generated. | ~1,440 |
| Build | api-and-interface-design | `E:/projects/_drafts/agent-skills-main/skills/api-and-interface-design/SKILL.md` | Guides stable API and interface design. Use when designing APIs, module boundaries, or any public interface. Use when creating REST or GraphQL endpoints, defining type contracts between modules, or establishing boundaries between frontend and backend. | ~1,444 |
| Verify | browser-testing-with-devtools | `E:/projects/_drafts/agent-skills-main/skills/browser-testing-with-devtools/SKILL.md` | Tests in real browsers via Chrome DevTools MCP. Use when building or debugging anything that runs in a browser. Use when you need to inspect the DOM, capture console errors, analyze network requests, profile performance, or verify visual output with real runtime data. Requires the chrome-devtools MCP server to be configured. | ~2,138 |
| Verify | debugging-and-error-recovery | `E:/projects/_drafts/agent-skills-main/skills/debugging-and-error-recovery/SKILL.md` | Guides systematic root-cause debugging. Use when tests fail, builds break, behavior doesn't match expectations, or you encounter any unexpected error. Use when you need a systematic approach to finding and fixing the root cause rather than guessing. | ~1,677 |
| Review | code-review-and-quality | `E:/projects/_drafts/agent-skills-main/skills/code-review-and-quality/SKILL.md` | Conducts multi-axis code review. Use before merging any change. Use when reviewing code written by yourself, another agent, or a human. Use when you need to assess code quality across multiple dimensions before it enters the main branch. | ~3,262 |
| Review | code-simplification | `E:/projects/_drafts/agent-skills-main/skills/code-simplification/SKILL.md` | Simplifies code for clarity. Use when refactoring code for clarity without changing behavior. Use when code works but is harder to read, maintain, or extend than it should be. Use when reviewing code that has accumulated unnecessary complexity. | ~2,028 |
| Review | security-and-hardening | `E:/projects/_drafts/agent-skills-main/skills/security-and-hardening/SKILL.md` | Hardens code against vulnerabilities. Use when handling user input, authentication, data storage, or external integrations. Use when building any feature that accepts untrusted data, manages user sessions, or interacts with third-party services. | ~2,926 |
| Review | performance-optimization | `E:/projects/_drafts/agent-skills-main/skills/performance-optimization/SKILL.md` | Optimizes application performance across frontend, backend, queries, and databases. Use when performance requirements exist, when you suspect performance regressions, when Core Web Vitals or load times need improvement, when N+1 query patterns need fixing, or when profiling reveals bottlenecks. | ~2,217 |
| Ship | git-workflow-and-versioning | `E:/projects/_drafts/agent-skills-main/skills/git-workflow-and-versioning/SKILL.md` | Structures git workflow practices. Use when making any code change. Use when committing, branching, resolving conflicts, or when you need to organize work across multiple parallel streams. Use when cutting a release, choosing a semantic version bump, tagging, or writing a changelog. | ~2,131 |
| Ship | ci-cd-and-automation | `E:/projects/_drafts/agent-skills-main/skills/ci-cd-and-automation/SKILL.md` | Automates CI/CD pipeline setup. Use when setting up or modifying build and deployment pipelines. Use when you need to automate quality gates, configure test runners in CI, or establish deployment strategies. | ~1,560 |
| Ship | deprecation-and-migration | `E:/projects/_drafts/agent-skills-main/skills/deprecation-and-migration/SKILL.md` | Manages deprecation and migration. Use when removing old systems, APIs, or features. Use when migrating users from one implementation to another. Use when deciding whether to maintain or sunset existing code. | ~1,953 |
| Ship | documentation-and-adrs | `E:/projects/_drafts/agent-skills-main/skills/documentation-and-adrs/SKILL.md` | Records decisions and documentation. Use when making architectural decisions, changing public APIs, shipping features, or when you need to record context that future engineers and agents will need to understand the codebase. | ~1,470 |
| Ship | observability-and-instrumentation | `E:/projects/_drafts/agent-skills-main/skills/observability-and-instrumentation/SKILL.md` | Instruments code so production behavior is visible and diagnosable. Use when adding logging, metrics, tracing, or alerting. Use when shipping any feature that runs in production and you need evidence it works. Use when production issues are reported but you can't tell what happened from the available data. | ~1,699 |
| Ship | shipping-and-launch | `E:/projects/_drafts/agent-skills-main/skills/shipping-and-launch/SKILL.md` | Prepares production launches. Use when preparing to deploy to production. Use when you need a pre-launch checklist, when setting up monitoring, when planning a staged rollout, or when you need a rollback strategy. | ~1,583 |

### Target agents and references

| Category | Name | Path | Factual purpose | Approx. words |
|---|---|---|---|---:|
| Agent | code-reviewer | `E:/projects/_drafts/agent-skills-main/agents/code-reviewer.md` | Staff-engineer review across correctness, readability, architecture, security, and performance, with severity-labelled output. | ~544 |
| Agent | security-auditor | `E:/projects/_drafts/agent-skills-main/agents/security-auditor.md` | Practical vulnerability and threat-model review covering trust boundaries, OWASP, AI/LLM risks, severity, and mitigations. | ~738 |
| Agent | test-engineer | `E:/projects/_drafts/agent-skills-main/agents/test-engineer.md` | Test strategy, coverage analysis, test-level selection, edge cases, and the fail-first Prove-It pattern. | ~526 |
| Agent | web-performance-auditor | `E:/projects/_drafts/agent-skills-main/agents/web-performance-auditor.md` | Quick source audit or Deep artifact/live audit for Core Web Vitals, loading, rendering, and network behavior; includes metric-source rules. | ~1,802 |
| Reference | accessibility-checklist | `E:/projects/_drafts/agent-skills-main/references/accessibility-checklist.md` | WCAG 2.1 AA checks for keyboard, screen readers, visual design, forms, ARIA, HTML patterns, and testing tools. | ~789 |
| Reference | definition-of-done | `E:/projects/_drafts/agent-skills-main/references/definition-of-done.md` | Standing project-wide completion bar, distinguished from task-specific acceptance criteria. | ~627 |
| Reference | observability-checklist | `E:/projects/_drafts/agent-skills-main/references/observability-checklist.md` | On-call questions, structured logging, RED/USE metrics, tracing, alerting, dashboards, telemetry checks, and launch gate. | ~800 |
| Reference | orchestration-patterns | `E:/projects/_drafts/agent-skills-main/references/orchestration-patterns.md` | Catalog of direct, command, fan-out, sequential, research-isolation, and Agent Teams patterns plus anti-patterns and Claude interop. | ~2,764 |
| Reference | performance-checklist | `E:/projects/_drafts/agent-skills-main/references/performance-checklist.md` | Core Web Vitals and TTFB targets, frontend/backend checks, measurement workflows, and performance anti-patterns. | ~1,141 |
| Reference | security-checklist | `E:/projects/_drafts/agent-skills-main/references/security-checklist.md` | Threat modeling, auth/authz, input validation, headers, CORS, dependency/install controls, AI/LLM security, and OWASP tables. | ~1,640 |
| Reference | testing-patterns | `E:/projects/_drafts/agent-skills-main/references/testing-patterns.md` | JavaScript/TypeScript examples for Jest, React Testing Library, Supertest, Playwright, mocking, assertions, and anti-patterns. | ~805 |

### Target infrastructure

**Eval cases.** `3+/2−` denotes three positive and two negative routing prompts. Kinds omitted in JSON default to `execution`.

| Eval case | Factual inventory |
|---|---|
| `E:/projects/_drafts/agent-skills-main/evals/cases/api-and-interface-design.json` | 3+/2−; 1 execution eval for URL-shortener endpoint contracts and error/version semantics. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/browser-testing-with-devtools.json` | 3+/2−; 1 execution eval requiring runtime evidence for a non-responsive signup form. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/ci-cd-and-automation.json` | 3+/2−; 1 execution eval for a Node pull-request CI pipeline and blocking quality gates. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/code-review-and-quality.json` | 3+/2−; 1 execution eval for a multi-axis review of a user-search diff. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/code-simplification.json` | 3+/2−; 1 execution eval for behavior-preserving config-parser simplification. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/context-engineering.json` | 3+/2−; 1 execution eval for diagnosing and repairing degraded session context. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/debugging-and-error-recovery.json` | 3+/2−; 2 execution evals for pagination root-cause repair and time-pressure resistance. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/deprecation-and-migration.json` | 3+/2−; 1 execution eval for staged deprecation of a public v1 REST API. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/documentation-and-adrs.json` | 3+/2−; 1 execution eval for an event-sourcing ADR. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/doubt-driven-development.json` | 3+/2−; 1 execution eval for adversarial review of an irreversible migration. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/frontend-ui-engineering.json` | 5+/2−; 1 execution eval for an accessible, keyboard-operable design-system control. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/git-workflow-and-versioning.json` | 3+/2−; 1 execution eval for splitting a mixed working tree into atomic commits. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/idea-refine.json` | 3+/2−; 1 fixtureless dialogue eval for refining a vague knowledge-sharing idea. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/incremental-implementation.json` | 3+/2−; 2 execution evals for planned CSV export and sunk-cost pressure. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/interview-me.json` | 3+/2−; 1 fixtureless dialogue eval for one-question-at-a-time admin-page requirements discovery. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/observability-and-instrumentation.json` | 3+/2−; 1 execution eval for payment-retry logs, metrics, and alerts. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/performance-optimization.json` | 5+/2−; 1 execution eval for measuring and improving a 1,000-item products page. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/planning-and-task-breakdown.json` | 3+/2−; 1 execution eval for turning a notifications spec into dependency-ordered vertical tasks. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/security-and-hardening.json` | 3+/2−; 1 execution eval for threat-modelled webhook SSRF hardening. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/shipping-and-launch.json` | 3+/2−; 2 execution evals for checkout launch readiness and authority-pressure resistance. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/source-driven-development.json` | 3+/2−; 1 execution eval for source-cited framework session handling. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/spec-driven-development.json` | 3+/2−; 1 execution eval for a usage-based-billing specification. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/test-driven-development.json` | 3+/2−; 3 execution evals: JavaScript invoice repair, authority pressure, and Python/unittest ecosystem detection. |
| `E:/projects/_drafts/agent-skills-main/evals/cases/using-agent-skills.json` | 3+/2−; 1 execution eval for routing a broken-login request through the meta-skill. |

**Fixture groups.** There are 24 named groups and 45 files. `idea-refine` and `interview-me` are dialogue evals and therefore have no fixture groups.

| Fixture group | Files | Factual contents/purpose |
|---|---:|---|
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/api-and-interface-design` | 1 | URL-shortening service brief. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/browser-testing-with-devtools` | 3 | Browser fixture README, HTML page, and server. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/ci-cd-and-automation` | 3 | Node package manifest, slug source, and slug test. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/code-review-and-quality` | 1 | User-search patch/diff. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/code-simplification` | 2 | Config parser and its test. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/context-engineering` | 1 | Context-audit scenario document. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/debugging-and-error-recovery` | 3 | Pagination source/test and time-pressure scenario. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/deprecation-and-migration` | 1 | API inventory for migration planning. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/documentation-and-adrs` | 1 | Architectural decision context. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/doubt-driven-development` | 1 | Migration plan for adversarial review. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/frontend-ui-engineering` | 2 | `Button.tsx` and design-system guidance. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/git-workflow-and-versioning` | 3 | App source/test plus hidden `.eval/working-tree.patch`. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/incremental-implementation` | 3 | Reports source/test and `tasks/plan.md`. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/incremental-implementation-pressure` | 2 | Mixed CSV-export draft and sunk-cost scenario. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/observability-and-instrumentation` | 2 | Operational context and payment-retry source. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/performance-optimization` | 2 | Benchmark and products implementation. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/planning-and-task-breakdown` | 1 | Notifications specification. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/security-and-hardening` | 2 | Webhook source and test. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/shipping-and-launch` | 2 | Authority-pressure and launch-status documents. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/source-driven-development` | 1 | Framework documentation task. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/spec-driven-development` | 1 | Billing brief. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/test-driven-development` | 3 | Authority-pressure scenario, invoice source, and invoice test. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/test-driven-development-ecosystem` | 3 | Python/unittest README, ledger source, and test. |
| `E:/projects/_drafts/agent-skills-main/evals/fixtures/using-agent-skills` | 1 | Broken-login incident scenario. |

**Eval framework and scripts**

| Path | Factual purpose | Approx. words |
|---|---|---:|
| `E:/projects/_drafts/agent-skills-main/evals/README.md` | Defines structural, lexical trigger/routing, and behavioral tiers; case schema, fixture rules, and metrics. | ~1,050 |
| `E:/projects/_drafts/agent-skills-main/scripts/run-evals.js` | Dependency-free Tier 2 TF-IDF routing/collision/schema runner and opt-in Tier 3 headless-Claude execution/grading runner. | ~2,757 |
| `E:/projects/_drafts/agent-skills-main/scripts/run-evals-test.js` | `node:test` coverage for case minimums, fixtures, dialogue kinds, rank floor, and workspace/patch materialization. | ~896 |
| `E:/projects/_drafts/agent-skills-main/scripts/validate-skills.js` | CLI wrapper that walks all skill directories and reports shared-linter results. | ~289 |
| `E:/projects/_drafts/agent-skills-main/scripts/lib/skill-lint.js` | Frontmatter, naming, description-trigger, required-section, exemption, and cross-reference lint rules. | ~1,182 |
| `E:/projects/_drafts/agent-skills-main/scripts/validate-commands.js` | Checks command presence and description parity across Claude, Gemini, and Antigravity command directories. | ~685 |
| `E:/projects/_drafts/agent-skills-main/skills/idea-refine/scripts/idea-refine.sh` | Creates `docs/ideas` when absent and emits a small JSON status object. | ~44 |

**Hooks**

| Path | Factual purpose | Approx. words |
|---|---|---:|
| `E:/projects/_drafts/agent-skills-main/hooks/hooks.json` | Registers `session-start.sh` for `SessionStart`, with plugin-root/project fallback. | ~33 |
| `E:/projects/_drafts/agent-skills-main/hooks/session-start.sh` | Emits JSON that injects the full `using-agent-skills` meta-skill; provides a missing-`jq` fallback. | ~131 |
| `E:/projects/_drafts/agent-skills-main/hooks/session-start-test.sh` | Regression test for the SessionStart JSON payload and fallback branch. | ~138 |
| `E:/projects/_drafts/agent-skills-main/hooks/sdd-cache-pre.sh` | Pre-`WebFetch` URL cache lookup; revalidates ETag/Last-Modified and serves only on HTTP 304. | ~646 |
| `E:/projects/_drafts/agent-skills-main/hooks/sdd-cache-post.sh` | Post-`WebFetch` storage of prompt-shaped content and origin validators under `.claude/sdd-cache`. | ~673 |
| `E:/projects/_drafts/agent-skills-main/hooks/SDD-CACHE.md` | Setup, data model, testing, debugging, requirements, and limitations for the source-driven-development cache hooks. | ~1,208 |
| `E:/projects/_drafts/agent-skills-main/hooks/simplify-ignore.sh` | Read/Edit/Write/Stop hook that replaces protected blocks with hashed placeholders and restores backed-up content. | ~1,500 |
| `E:/projects/_drafts/agent-skills-main/hooks/simplify-ignore-test.sh` | Ten shell-level cases covering filtering, reasons, newline handling, malformed input, and comment styles. | ~965 |
| `E:/projects/_drafts/agent-skills-main/hooks/SIMPLIFY-IGNORE.md` | Setup, annotation syntax, event flow, recovery, requirements, and limitations for protected simplification blocks. | ~526 |

**Commands**

| Surface/command | Path | Factual purpose | Approx. words |
|---|---|---|---:|
| Claude `/build` | `E:/projects/_drafts/agent-skills-main/.claude/commands/build.md` | Single-task incremental TDD or `/build auto` whole-plan execution with per-task verification and commits. | ~612 |
| Claude `/code-simplify` | `E:/projects/_drafts/agent-skills-main/.claude/commands/code-simplify.md` | Behavior-preserving simplification of changed or specified code. | ~154 |
| Claude `/plan` | `E:/projects/_drafts/agent-skills-main/.claude/commands/plan.md` | Read-only spec decomposition into dependency-ordered tasks and task files. | ~92 |
| Claude `/review` | `E:/projects/_drafts/agent-skills-main/.claude/commands/review.md` | Five-axis review with severity and file/line recommendations. | ~104 |
| Claude `/ship` | `E:/projects/_drafts/agent-skills-main/.claude/commands/ship.md` | Parallel code/security/test persona fan-out, merge, go/no-go, and rollback plan. | ~668 |
| Claude `/spec` | `E:/projects/_drafts/agent-skills-main/.claude/commands/spec.md` | Clarifies requirements and writes `SPEC.md` before implementation. | ~98 |
| Claude `/test` | `E:/projects/_drafts/agent-skills-main/.claude/commands/test.md` | Red-green-refactor and bug Prove-It workflow, with browser escalation. | ~99 |
| Claude `/webperf` | `E:/projects/_drafts/agent-skills-main/.claude/commands/webperf.md` | Quick or Deep web-performance audit through the web-performance persona. | ~291 |
| Antigravity `/build` | `E:/projects/_drafts/agent-skills-main/commands/build.toml` | TOML variant of incremental or whole-plan build workflow. | ~622 |
| Antigravity `/code-simplify` | `E:/projects/_drafts/agent-skills-main/commands/code-simplify.toml` | TOML variant of behavior-preserving simplification. | ~157 |
| Antigravity `/planning` | `E:/projects/_drafts/agent-skills-main/commands/planning.toml` | TOML planning command; uses `/planning` rather than `/plan`. | ~95 |
| Antigravity `/review` | `E:/projects/_drafts/agent-skills-main/commands/review.toml` | TOML five-axis review command. | ~107 |
| Antigravity `/ship` | `E:/projects/_drafts/agent-skills-main/commands/ship.toml` | TOML parallel persona launch-readiness workflow. | ~692 |
| Antigravity `/spec` | `E:/projects/_drafts/agent-skills-main/commands/spec.toml` | TOML specification command. | ~101 |
| Antigravity `/test` | `E:/projects/_drafts/agent-skills-main/commands/test.toml` | TOML TDD and Prove-It command. | ~102 |
| Antigravity `/webperf` | `E:/projects/_drafts/agent-skills-main/commands/webperf.toml` | TOML Quick/Deep web-performance audit command. | ~307 |

**Docs, rule, and skill-local references**

| Path | Factual purpose | Approx. words |
|---|---|---:|
| `E:/projects/_drafts/agent-skills-main/docs/adoption-guide.md` | Greenfield full-lifecycle and brownfield verification-first rollout paths. | ~1,533 |
| `E:/projects/_drafts/agent-skills-main/docs/agents.md` | Persona/skill/command relationship, invocation matrix, fan-out model, and Claude subagent/team interop. | ~997 |
| `E:/projects/_drafts/agent-skills-main/docs/antigravity-setup.md` | Antigravity plugin installation, commands, skill discovery, personas, validation, and configuration. | ~654 |
| `E:/projects/_drafts/agent-skills-main/docs/codex-setup.md` | Codex marketplace/local installation and shared root-skills manifest behavior. | ~236 |
| `E:/projects/_drafts/agent-skills-main/docs/comparison.md` | Factual project comparison with Superpowers and Matt Pocock’s skills, including cited sources. | ~2,283 |
| `E:/projects/_drafts/agent-skills-main/docs/copilot-setup.md` | Copilot skill/persona copying, filename requirements, project instructions, and usage tips. | ~416 |
| `E:/projects/_drafts/agent-skills-main/docs/cursor-setup.md` | Current Cursor rules/skills layout, synchronization, loading model, and troubleshooting. | ~1,083 |
| `E:/projects/_drafts/agent-skills-main/docs/developer-onboarding.md` | Contributor-facing repository model, local requirements, verification loop, contribution paths, and reading order. | ~1,112 |
| `E:/projects/_drafts/agent-skills-main/docs/gemini-cli-setup.md` | Gemini native skills, `GEMINI.md`, MCP/hooks, and claimed slash-command integration. | ~757 |
| `E:/projects/_drafts/agent-skills-main/docs/getting-started.md` | Harness-neutral loading guidance and catalogs for skills, agents, commands, references, and artifacts. | ~891 |
| `E:/projects/_drafts/agent-skills-main/docs/opencode-setup.md` | OpenCode workflow described through root `AGENTS.md`, the skill tool, and root `skills`. | ~590 |
| `E:/projects/_drafts/agent-skills-main/docs/skill-anatomy.md` | Skill path/frontmatter/section/support-file/script/naming conventions. | ~1,308 |
| `E:/projects/_drafts/agent-skills-main/docs/windsurf-setup.md` | `.windsurfrules` and global-rule loading guidance. | ~177 |
| `E:/projects/_drafts/agent-skills-main/.claude/rules/skills-contributing.md` | Path-scoped anti-duplication rule for changes under `skills/**`; points to contribution and anatomy docs. | ~138 |
| `E:/projects/_drafts/agent-skills-main/skills/idea-refine/examples.md` | Three worked ideation sessions and observations about expected session behavior. | ~3,124 |
| `E:/projects/_drafts/agent-skills-main/skills/idea-refine/frameworks.md` | SCAMPER, HMW, first principles, JTBD, constraints, pre-mortem, and analogy lenses. | ~872 |
| `E:/projects/_drafts/agent-skills-main/skills/idea-refine/refinement-criteria.md` | User-value, feasibility, differentiation, assumption, decision, and MVP-scoping criteria. | ~900 |

**Manifests and top-level files**

| Path | Factual purpose | Approx. words |
|---|---|---:|
| `E:/projects/_drafts/agent-skills-main/README.md` | Main catalog, install paths, integrations, lifecycle, skills, agents, references, anatomy, and project tree. | ~2,419 |
| `E:/projects/_drafts/agent-skills-main/CLAUDE.md` | Repository-scoped agent configuration describing structure, phase assignments, conventions, commands, and boundaries. | ~508 |
| `E:/projects/_drafts/agent-skills-main/LICENSE` | Full GNU Affero General Public License Version 3 text dated 19 November 2007. | ~5,535 |
| `E:/projects/_drafts/agent-skills-main/plugin.json` | Minimal Antigravity plugin name/version/description manifest. | ~14 |
| `E:/projects/_drafts/agent-skills-main/.claude-plugin/plugin.json` | Claude plugin metadata and paths for both command directories, skills, and four agents. | ~47 |
| `E:/projects/_drafts/agent-skills-main/.claude-plugin/marketplace.json` | Claude marketplace listing for the GitHub-hosted plugin. | ~76 |
| `E:/projects/_drafts/agent-skills-main/.codex-plugin/plugin.json` | Codex plugin metadata, root skills path, empty Codex hook configuration, and interface metadata. | ~66 |
| `E:/projects/_drafts/agent-skills-main/.agents/plugins/marketplace.json` | Agent/Codex marketplace entry using the repository root as a local plugin source. | ~50 |
| `E:/projects/_drafts/agent-skills-main/.gitattributes` | Normalizes text files to LF. | ~3 |
| `E:/projects/_drafts/agent-skills-main/.gitignore` | Ignores dependencies, env/log files, generated hook caches, eval results, and Python cache files. | ~9 |

### Target counts and missing paths

| Surface | Count |
|---|---:|
| `E:/projects/_drafts/agent-skills-main/skills` | 24 skill directories; 28 files total: 24 `SKILL.md`, 3 idea-refine reference docs, 1 helper script |
| `E:/projects/_drafts/agent-skills-main/agents` | 4 files |
| `E:/projects/_drafts/agent-skills-main/references` | 7 files |
| `E:/projects/_drafts/agent-skills-main/hooks` | 9 files: 1 manifest, 6 shell scripts/tests, 2 docs |
| `E:/projects/_drafts/agent-skills-main/.claude` | 9 files: 8 commands, 1 rule |
| `E:/projects/_drafts/agent-skills-main/commands` | 8 TOML commands |
| `E:/projects/_drafts/agent-skills-main/docs` | 13 files |
| `E:/projects/_drafts/agent-skills-main/evals` | 70 files: 1 framework README, 24 cases, 45 fixtures |
| `E:/projects/_drafts/agent-skills-main/scripts` | 5 JavaScript files |
| `E:/projects/_drafts/agent-skills-main/.agents` | 1 marketplace manifest |
| `E:/projects/_drafts/agent-skills-main/.claude-plugin` | 2 manifests |
| `E:/projects/_drafts/agent-skills-main/.codex-plugin` | 1 manifest |
| Target-root standalone files | 6: `.gitattributes`, `.gitignore`, `CLAUDE.md`, `LICENSE`, `README.md`, `plugin.json` |
| **Total** | **163 files** |

**Explicit existence results**

| Path | Result | Factual context |
|---|---|---|
| `E:/projects/_drafts/agent-skills-main/.gemini` | Missing | Root README project tree and Gemini setup text claim `.gemini/commands` with eight commands; the validator also expects that directory. |
| `E:/projects/_drafts/agent-skills-main/.gemini/commands` | Missing | README-claimed command surface. |
| `E:/projects/_drafts/agent-skills-main/.opencode` | Missing | OpenCode documentation instead describes root `AGENTS.md` plus root `skills`. |
| `E:/projects/_drafts/agent-skills-main/CONTRIBUTING.md` | Missing | Referenced by `CLAUDE.md`, the scoped Claude rule, and developer onboarding. |
| `E:/projects/_drafts/agent-skills-main/tests` | Missing | Tests exist only as colocated hook/script test files and eval fixtures. |
| `E:/projects/_drafts/agent-skills-main/workflows` | Missing | No root workflow directory. |
| `E:/projects/_drafts/agent-skills-main/.github/workflows` | Missing | The entire `.github` directory is absent despite CI being described in eval documentation. |
| `E:/projects/_drafts/agent-skills-main/package.json` | Missing | Developer onboarding explicitly describes no top-level package manifest; one nested fixture manifest exists under `evals/fixtures/ci-cd-and-automation`. |
| `E:/projects/_drafts/agent-skills-main/AGENTS.md` | Missing | Referenced as a root file by OpenCode setup and developer onboarding. |
| `E:/projects/_drafts/agent-skills-main/evals/results` | Missing | Documented as generated behavioral-eval output and ignored by `.gitignore`. |
| `E:/projects/_drafts/agent-skills-main/.claude/sdd-cache` | Missing | Documented generated cache path and ignored by `.gitignore`. |
| `E:/projects/_drafts/agent-skills-main/.claude/.simplify-ignore-cache` | Missing | Documented generated backup/cache path and ignored by `.gitignore`. |

**README project-tree surfaces:** `skills`, `agents`, `references`, `hooks`, `.claude/commands`, `commands`, `plugin.json`, and `docs` exist; the claimed `.gemini/commands` surface does not.

**Observable license identity:** `E:/projects/_drafts/agent-skills-main/LICENSE` is the GNU Affero General Public License, Version 3, dated 19 November 2007. Separately, `E:/projects/_drafts/agent-skills-main/.claude-plugin/plugin.json`, `E:/projects/_drafts/agent-skills-main/.claude-plugin/marketplace.json`, and `E:/projects/_drafts/agent-skills-main/.codex-plugin/plugin.json` declare `"license": "MIT"` in manifest metadata.

### Target evidence state

- **Working tree:** `E:/projects/_drafts/agent-skills-main` has no tracked files. Of its 163 files, 153 appear as `??` in the enclosing repository; the remaining 10 are ignored by enclosing `.claude/` and `.agents/` patterns: all 9 files under the target `.claude` surface and the 1 file under target `.agents`.
- **Repository boundary:** `E:/projects/_drafts/agent-skills-main/.git` does not exist. Git resolves the enclosing repository root to `E:/projects/_drafts`.
- **Inspected surfaces:** all 163 paths were recursively enumerated, including hidden plugin directories and the fixture `.eval/working-tree.patch`; complete contents were read for root metadata, manifests, agents, references, docs, hooks, commands, scripts, eval cases, the Claude rule, and idea-refine support files. All 24 skill frontmatter blocks were extracted and compared with README/CLAUDE lifecycle listings.
- **Unreadable items:** none encountered.
- **Not execution-verified:** repository scripts, hooks, validators, test files, and evals were not run. Fixture bodies were inventoried by recursive path, filename, and their referencing eval cases rather than behaviorally exercised. Skill bodies were not reviewed; only inventory-relevant frontmatter, existence, lifecycle, and whole-file size were inspected.
- **Word-count method:** GNU `wc -w` over each whole file; counts are whitespace-delimited and include frontmatter, prose, code blocks, and markup, so they are reported as approximate. File counts come from recursive path enumeration, not README claims.

#### 阶段 1 执行记录

- A（当前项目）完成：74 条 catalog 记录，覆盖 76 个 scoped physical files；3 个生成的 `.pyc` 合并为 1 条缓存记录。
- B（target）完成：覆盖 163 个文件、24 个 Skills、4 个 agents、7 个 root references，以及 evals/hooks/commands/docs/scripts/hidden manifests。
- B 的首个结构化返回和一次同角色重试因范围过大未产生可用 final result；随后在同一 workflow 内改由 Explore owner 完成，A 结果从缓存复用。空结果未被当作成功或写入清单。
- A 的 worker 工具边界不含 shell/Edit/Write；B 的 Explore 角色不含 Edit/Write，但具备 Bash，因此 B 的技术只读隔离未完全验证。一次最终状态读取曾短暂显示新增 `prompt.md`，该路径在读取前已不存在，最终 Git 状态仅保留三个预期未跟踪输入；其内容和来源无法验证。
- 两个最终清单均只用于事实盘点；未执行 target 脚本、hooks、validators、tests 或 evals，未作差距、优先级、风格或吸收判断。

## 阶段 2：差距分析（按生命周期分组、分批核实）

按 Meta、Define、Plan、Build、Verify、Review、Ship 的顺序核实；每完成 1-2 个分类就更新本文件、汇报并暂停，等待用户确认后再继续下一组。此阶段只形成证据化判断，不进入吸收修改。

### 差距分析

#### 第 1 组：Meta + Define（已完成，已确认）

> 本组结论是阶段 2 的 provisional classification，不是阶段 4 的引入授权。P0 表示必须优先解决冲突，不等于批准采用。

##### 暂定结论汇总

| 分类 | Target 条目 | 当前暂定动作 | 优先级 | 核心理由 |
| --- | --- | --- | --- | --- |
| Meta | `using-agent-skills（含 SessionStart / DoD 直接依赖）` | `合并/协调重叠` | `P1` | 暂不原样新增 `using-agent-skills` 或启用其 SessionStart hook：它会成为第二个 always-on/router 权威、指向另一套 Skill 名称，并把当前明确保持轻量的普通工作升级为默认 spec/workflow/DoD 流程。可协调吸收的范围应非常窄：仅评估把“有具体技术问题时直接提出异议”和“仅对 material assumptions 显式化”写入现有 prompt，并为正/负边界补现有测试；不要复制 flowchart、生命周期序列或固定全局 DoD。该项列 P1 是因为原样引入会影响所有会话与核心路由，但目标目录在启动快照中未跟踪、未证明正在运行，因此不是 P0 活跃故障。依据：`E:\projects\_drafts\agent-skills-main\hooks\session-start.sh` 第 14-21 行；`E:\projects\_drafts\agent-skills-main\skills\using-agent-skills\SKILL.md` 第 74-83、130-163 行；`E:\projects\_drafts\README.md` 第 19-38、111-119 行；`E:\projects\_drafts\tests\trigger-matrix.md` 第 243-257 行。 |
| Define | `interview-me` | `新增/改写引入` | `P1` | 暂定 P1“新增/改写引入”，不是原样复制：本次有界当前表面没有独立的前决策意图访谈能力，而“假设+猜测式单问、want-vs-should 探针、确认意图输出”有独立行为价值。[agent-skills-main/skills/interview-me/SKILL.md:L40-L138；README.md:L121-L132] 但引入版应只在用户显式要求访谈，或产品意图确实会改变范围/方案且无法安全推断时触发；保留实时交互限制和可选持久化，去掉把 95%、特定确认措辞和六字段模板作为所有模糊请求的普遍硬门，以保持当前最小提问/无默认批准门合同。[skills/plan-work/SKILL.md:L12-L20,L50-L60] |
| Define | `idea-refine` | `新增/改写引入` | `P2` | 暂定 P2“新增/改写引入”，仅作为可选、明确意图的轻量 ideation Skill，而非复制五文件包。其真正缺口是 HMW/JTBD/SCAMPER 等发散镜头和“价值—可行性—差异化—关键假设”产品收敛；当前 plan/design/issue 只覆盖其收敛与工件部分。[agent-skills-main/skills/idea-refine/frameworks.md:L19-L99；agent-skills-main/skills/idea-refine/refinement-criteria.md:L5-L113；README.md:L121-L132] 改写版应把固定数量变为上限/按需、默认只在聊天输出、不带目录初始化脚本，并明确不接管实现规划或架构边界。因暂无仓库证据证明该需求高频，优先级低于 interview 的明确意图缺口，也不是最终引入授权。 |
| Define | `spec-driven-development` | `合并/协调重叠` | `P0` | 暂定 P0“合并/协调重叠”，其中 P0 表示在任何吸收前必须先解决路由冲突，不表示批准原样引入。不要新增一个贯穿 Specify→Implement 的总控 Skill；把“用户显式要求工程 spec 时的需求工件”协调到 issue-workflow（或明确选定的单一 Define 工件所有者），只保留经验证项目事实、目标/用户/成功、关键假设、边界和开放问题；架构交 design-codebase，实施规划交 plan-work，测试/完成仍由现有所有者处理。[skills/issue-workflow/SKILL.md:L20-L39；tests/routing-contract.md:L16-L61] 删除自动大小/时长触发、四段普遍批准、固定 tasks 路径、约 5 文件阈值和自动 commit/PR 要求。[agent-skills-main/skills/spec-driven-development/SKILL.md:L12-L32,L141-L178] |

##### Meta 详细分析

- **完整性说明：** 已完成 `using-agent-skills` 的有界、只读分类：全文读取目标 SKILL、其会话注入链 `hooks/hooks.json` 与 `hooks/session-start.sh`、其直接引用的 `references/definition-of-done.md`；全文读取当前 `prompts/CLAUDE.fragment.md`、根 README、三份指定路由测试；并读取直接相关的当前 Skill 描述及可选 `capability-harness` Skill。结论不依赖 README 摘要，也未读取无关目标生命周期 Skill。当前基线为会话启动快照中的 `main@f82a1b2`；`agent-skills-main/` 在该快照中未跟踪，因此目标证据无当前仓库提交版本。本轮仅使用 Read/Grep/Glob，未执行命令、未修改文件、未使用 WebSearch/WebFetch。所有“未见等价规则”均仅限上述有界来源，不宣称全仓库或实时宿主中的绝对不存在。

###### `using-agent-skills（含 SessionStart / DoD 直接依赖）`

- **暂定动作：** `合并/协调重叠`
- **优先级：** `P1`
- **理由：** 暂不原样新增 `using-agent-skills` 或启用其 SessionStart hook：它会成为第二个 always-on/router 权威、指向另一套 Skill 名称，并把当前明确保持轻量的普通工作升级为默认 spec/workflow/DoD 流程。可协调吸收的范围应非常窄：仅评估把“有具体技术问题时直接提出异议”和“仅对 material assumptions 显式化”写入现有 prompt，并为正/负边界补现有测试；不要复制 flowchart、生命周期序列或固定全局 DoD。该项列 P1 是因为原样引入会影响所有会话与核心路由，但目标目录在启动快照中未跟踪、未证明正在运行，因此不是 P0 活跃故障。依据：`E:\projects\_drafts\agent-skills-main\hooks\session-start.sh` 第 14-21 行；`E:\projects\_drafts\agent-skills-main\skills\using-agent-skills\SKILL.md` 第 74-83、130-163 行；`E:\projects\_drafts\README.md` 第 19-38、111-119 行；`E:\projects\_drafts\tests\trigger-matrix.md` 第 243-257 行。

**Target 实际行为**

- 静态意图：frontmatter 把它定义为会话开始或需要发现适用 Skill 时使用、并治理所有 Skill 发现/调用的 meta-skill。位置：`E:\projects\_drafts\agent-skills-main\skills\using-agent-skills\SKILL.md` 第 1-4 行。
- 静态路由：任务到达后按 Define/Plan/Build/Verify/Review/Ship 类阶段和子条件路由到目标仓库的命名 Skill。位置：`E:\projects\_drafts\agent-skills-main\skills\using-agent-skills\SKILL.md` 第 12-42、165-191 行。
- 静态通用规则：把 surface assumptions、遇到困惑停止、技术异议、简化、限范围、验证设为“at all times/non-negotiable”。位置：`E:\projects\_drafts\agent-skills-main\skills\using-agent-skills\SKILL.md` 第 44-113 行。
- 静态强制性：开始前检查 Skill、按顺序执行 workflow、允许多 Skill 串联、非平凡任务无 spec 时先进入 spec；同时说明并非每项任务需要全部 Skill。位置：`E:\projects\_drafts\agent-skills-main\skills\using-agent-skills\SKILL.md` 第 130-163 行。
- 注入实现：SessionStart hook 调用 shell；shell 在存在 `jq` 和 meta 文件时读取完整 SKILL 并发出 `priority: IMPORTANT` 的消息。缺少依赖或文件以及 hook 命令失败均 fail open。位置：`E:\projects\_drafts\agent-skills-main\hooks\hooks.json` 第 1-14 行；`E:\projects\_drafts\agent-skills-main\hooks\session-start.sh` 第 5-24 行。
- 完成门：meta SKILL 引用固定 Definition of Done；该依赖称每个 change 都需同时满足任务 acceptance criteria 与 standing checklist，并分列 runtime、tests、regression、quality、integration、docs 与 ship-readiness。位置：`E:\projects\_drafts\agent-skills-main\skills\using-agent-skills\SKILL.md` 第 109-113 行；`E:\projects\_drafts\agent-skills-main\references\definition-of-done.md` 第 1-59 行。

**当前已验证覆盖**

- 当前 always-on prompt 已覆盖：区分事实/假设并用能解决材料不确定性的来源、采用最轻流程、限制范围、按动作授权、按结果/风险验证并报告缺口。位置：`E:\projects\_drafts\prompts\CLAUDE.fragment.md` 第 6-18 行。
- 当前 routing contract 已定义 ordinary/base、各 Skill trigger、最小组合、host workflow 不重入等边界；其来源层级也明确 prompt 与 Skill bodies/descriptions 为运行权威，tests 仅做维护验证。位置：`E:\projects\_drafts\tests\routing-contract.md` 第 1-14、16-61 行。
- 当前正负路由案例已覆盖小改动、已批准计划、检查/准备阶段、完成声明、单 focused verifier、meta/reliability 显式触发等退化风险。位置：`E:\projects\_drafts\tests\trigger-matrix.md` 第 8-37、220-257 行；`E:\projects\_drafts\tests\non-trigger-cases.md` 第 7-44、159-176 行。
- 当前 `plan-work`、`design-codebase`、`test-strategy`、`review-and-finish`、`reliability-check` 和 `agent-workflow` 的描述均对普通工作给出窄触发/非触发边界，已承担目标 phase router 想统一分派的主要领域职责。位置：`E:\projects\_drafts\skills\plan-work\SKILL.md` 第 3、8 行；`E:\projects\_drafts\skills\design-codebase\SKILL.md` 第 3、8 行；`E:\projects\_drafts\skills\test-strategy\SKILL.md` 第 3、8 行；`E:\projects\_drafts\skills\review-and-finish\SKILL.md` 第 3、8 行；`E:\projects\_drafts\skills\reliability-check\SKILL.md` 第 3、8 行；`E:\projects\_drafts\skills\agent-workflow\SKILL.md` 第 3、8 行。
- 可选 capability harness 已覆盖 substantive work 的决策前未知项、外部信号、权限/副作用/停止边界与轻量 acceptance seed，并明确 routine direct work 不应加流程。位置：`E:\projects\_drafts\plugins\capability-harness\skills\capability-harness\SKILL.md` 第 1-35、37-53、68-87 行；其可选地位见 `E:\projects\_drafts\README.md` 第 121-133 行。

**独有或缺失部分**

- 有界来源中未见与目标第 74-83 行同等明确的“反谄媚/有具体问题时提出技术异议、说明代价、给替代方案、再服从知情决定”规则；这是最清晰的潜在独立价值，但该缺失仅对已读当前来源成立。位置：`E:\projects\_drafts\agent-skills-main\skills\using-agent-skills\SKILL.md` 第 74-83 行；已读 current always-on 全文为 `E:\projects\_drafts\prompts\CLAUDE.fragment.md` 第 1-20 行。
- 目标提供固定的 `ASSUMPTIONS I'M MAKING` 输出模板及任何冲突时 `STOP`/等待的显式协议；当前仅有材料假设/必要询问原则，没有该固定格式或无条件停止阈值。位置：`E:\projects\_drafts\agent-skills-main\skills\using-agent-skills\SKILL.md` 第 48-72 行；`E:\projects\_drafts\prompts\CLAUDE.fragment.md` 第 8、13 行。该差异是形式与阈值差异，不等于当前完全缺少假设管理。
- 目标独有一个通过 SessionStart 注入完整 Skill 目录的中央发现层；当前明确选择 prompt + Skill descriptions + maintenance tests，而不是新 router。位置：`E:\projects\_drafts\agent-skills-main\hooks\session-start.sh` 第 14-21 行；`E:\projects\_drafts\tests\trigger-matrix.md` 第 243-249 行。该独特性是架构差异，不是应补缺口。
- 目标独有固定跨阶段 DoD 文档及全目录 lifecycle sequence；当前 bounded sources 采用按任务、风险和 owning Skill 分布式验证，没有同等单一固定 checklist。位置：`E:\projects\_drafts\agent-skills-main\references\definition-of-done.md` 第 1-59 行；`E:\projects\_drafts\prompts\CLAUDE.fragment.md` 第 17 行；`E:\projects\_drafts\skills\review-and-finish\SKILL.md` 第 3、8 行。该独特性同时带来重叠和过度门控风险。

**重叠部分**

- 目标的假设/困惑管理与当前“区分事实、假设、材料不确定性并只在会改变结果时询问”重叠，但目标阈值更重。位置：`E:\projects\_drafts\agent-skills-main\skills\using-agent-skills\SKILL.md` 第 48-72 行；`E:\projects\_drafts\prompts\CLAUDE.fragment.md` 第 8、13 行。
- 目标的 simplicity/scope discipline 与当前最轻流程、限范围、按动作授权重叠。位置：`E:\projects\_drafts\agent-skills-main\skills\using-agent-skills\SKILL.md` 第 85-107 行；`E:\projects\_drafts\prompts\CLAUDE.fragment.md` 第 9、14-16 行。
- 目标的 verify-before-done 与当前默认验证、`test-strategy`、`review-and-finish` 及 capability acceptance seed 重叠。位置：`E:\projects\_drafts\agent-skills-main\skills\using-agent-skills\SKILL.md` 第 109-113 行；`E:\projects\_drafts\prompts\CLAUDE.fragment.md` 第 17 行；`E:\projects\_drafts\plugins\capability-harness\skills\capability-harness\SKILL.md` 第 22-35 行。
- 目标 phase router 与当前 routing contract/Skill descriptions 都解决“哪个 workflow 适用”，但当前采用分散权威与维护测试，目标采用单个注入目录。位置：`E:\projects\_drafts\agent-skills-main\skills\using-agent-skills\SKILL.md` 第 12-42 行；`E:\projects\_drafts\tests\routing-contract.md` 第 1-35、71-82 行。

**冲突**

- 中央运行层冲突：目标通过 SessionStart 把整个 meta SKILL 以 `IMPORTANT` 消息注入每个新会话；当前架构规定 `prompts/` 才是 always-on 层，Skill 只在请求明确需要时加载，并明确 tests 不应成为第二运行层。位置：`E:\projects\_drafts\agent-skills-main\hooks\hooks.json` 第 3-9 行；`E:\projects\_drafts\agent-skills-main\hooks\session-start.sh` 第 14-23 行；`E:\projects\_drafts\README.md` 第 25-38 行。
- 路由哲学冲突：目标要求开始前检查 Skill、顺序执行 workflow、非平凡任务无 spec 时默认先 spec；当前规则把普通编码、直接修复和已解决计划执行放在基础层，并要求最小组合。位置：`E:\projects\_drafts\agent-skills-main\skills\using-agent-skills\SKILL.md` 第 130-163 行；`E:\projects\_drafts\tests\routing-contract.md` 第 16-35、37-61 行；`E:\projects\_drafts\tests\trigger-matrix.md` 第 8-37 行。
- 阻塞阈值冲突：目标对不一致或不清楚规格给出无条件 `STOP`/等待协议；当前 prompt 只在缺失信息会实质改变结果、范围、风险或授权时提问，否则应采用明显低风险默认并继续。位置：`E:\projects\_drafts\agent-skills-main\skills\using-agent-skills\SKILL.md` 第 62-72 行；`E:\projects\_drafts\prompts\CLAUDE.fragment.md` 第 8、13 行；`E:\projects\_drafts\plugins\capability-harness\skills\capability-harness\SKILL.md` 第 31-35 行。
- Skill 命名/所有权冲突：目标 flowchart 路由到 `spec-driven-development`、`incremental-implementation`、`test-driven-development`、`code-review-and-quality` 等目标目录；当前权威路由使用 `plan-work`、`design-codebase`、`test-strategy`、`review-and-finish` 等边界。直接引入会建立第二套分类与所有权。位置：`E:\projects\_drafts\agent-skills-main\skills\using-agent-skills\SKILL.md` 第 14-42、165-191 行；`E:\projects\_drafts\tests\routing-contract.md` 第 16-35 行；`E:\projects\_drafts\README.md` 第 40-68 行。
- 验证范围冲突：目标把固定 DoD 描述为每个 change 的常设门，并在 meta SKILL 中概括为 tests、无回归、runtime、docs；当前默认层要求按 requested outcome、acceptance criteria、affected contracts 和 concrete risks 验证，并允许明确报告未验证项。位置：`E:\projects\_drafts\agent-skills-main\skills\using-agent-skills\SKILL.md` 第 109-113 行；`E:\projects\_drafts\agent-skills-main\references\definition-of-done.md` 第 3、15-19、53-59 行；`E:\projects\_drafts\prompts\CLAUDE.fragment.md` 第 17 行。
- 维护合同冲突：当前 meta 测试要求从 routing contract 与 Skill descriptions 路由且“不 invent a new router layer”；目标文件本身正是新增中央 router layer。位置：`E:\projects\_drafts\tests\trigger-matrix.md` 第 243-249 行。

**维护成本**

- 目录映射重复：目标同一 SKILL 内同时维护 flowchart、Lifecycle Sequence 和 Quick Reference 三份目录，再与当前 README、routing contract、trigger/non-trigger tests 同步；任何 rename、trigger 或所有权变化都可能形成漂移。位置：`E:\projects\_drafts\agent-skills-main\skills\using-agent-skills\SKILL.md` 第 14-42、140-191 行；`E:\projects\_drafts\README.md` 第 40-68、111-119 行。
- 运行依赖成本：每次会话启动需要 Bash、`jq`、正确 plugin/project 路径、JSON 转义和 fail-open 分支的跨平台测试；缺依赖时所谓强制 meta 层静默退化为单项 Skill 可用。位置：`E:\projects\_drafts\agent-skills-main\hooks\hooks.json` 第 3-9 行；`E:\projects\_drafts\agent-skills-main\hooks\session-start.sh` 第 5-24 行。
- 上下文/延迟成本：hook 每个新会话读取并注入完整 192 行 SKILL，而当前维护原则明确避免让每项任务更慢。位置：`E:\projects\_drafts\agent-skills-main\hooks\session-start.sh` 第 14-21 行；`E:\projects\_drafts\README.md` 第 165-178 行。
- 规则协调成本：假设、停止、范围、验证和 acceptance 已分布在当前 prompt、capability harness、test strategy 与 review-and-finish；新增 DoD/meta 层需要持续解决哪一层权威、何时阻塞及副作用验证授权。位置：`E:\projects\_drafts\prompts\CLAUDE.fragment.md` 第 8-18 行；`E:\projects\_drafts\plugins\capability-harness\skills\capability-harness\SKILL.md` 第 22-35 行；`E:\projects\_drafts\agent-skills-main\references\definition-of-done.md` 第 17-59 行。
- 测试扩张成本：若保留目标的默认 spec、强制 workflow 与全局 DoD，现有大量普通任务 base/non-trigger 案例都需重写或增加冲突优先级测试。位置：`E:\projects\_drafts\tests\trigger-matrix.md` 第 8-37、250-257 行；`E:\projects\_drafts\tests\non-trigger-cases.md` 第 7-44、159-176 行。

**证据**

| 路径 | 位置 | 支持的结论 |
| --- | --- | --- |
| `agent-skills-main/skills/using-agent-skills/SKILL.md` | 第 1-4 行 frontmatter；第 12-42 行 Skill Discovery；第 44-113 行 Core Operating Behaviors；第 130-191 行 Skill Rules、Lifecycle、Quick Reference | 目标静态指令确实定义中央 phase router、六项 always-on 行为、强制 workflow/verification 规则及多阶段序列；这是直接主体证据，而非 README 摘要。 |
| `agent-skills-main/hooks/hooks.json` | 第 1-14 行，尤其 SessionStart 注册第 3-9 行 | 目标配置在 SessionStart 调用 shell hook，并通过 `&#124;&#124; true` 保持失败开放。 |
| `agent-skills-main/hooks/session-start.sh` | 第 1-24 行，尤其路径解析第 5-7 行、jq gate 第 9-12 行、完整内容注入第 14-21 行 | 目标 hook 会读取整个 meta SKILL 并以 IMPORTANT 消息注入；缺 jq 或文件时只发 INFO，不阻止会话。 |
| `agent-skills-main/references/definition-of-done.md` | 第 3-19 行 standing gate；第 21-57 行 checklist 与分层应用 | 目标 meta SKILL 的直接依赖把 DoD 定义为常设门，覆盖 runtime、tests、regression、quality、integration、docs、security、observability、rollback 与 human review。 |
| `prompts/CLAUDE.fragment.md` | 第 3-20 行全部默认规则 | 当前 always-on 层已经覆盖材料假设、比例性、范围、授权与按风险验证，同时明确 workflow opt-in 和仅在材料信息缺失时提问。 |
| `README.md` | 第 19-38 行 Capability Boundaries；第 40-68 行 Skills；第 121-133 行 Capability Map；第 167-178 行 Customization | 当前设计明确轻量升级、单一 always-on prompt、按需 Skill、可选 harness、模型 guidance 非技术 enforcement，并避免使每个任务变慢。 |
| `tests/routing-contract.md` | 第 1-14 行 source-of-truth；第 16-61 行 core routing/composition；第 71-82 行 maintenance use | 当前维护合同已定义权威层级、普通工作基础层、窄 Skill 分工及最小组合。 |
| `tests/trigger-matrix.md` | 第 8-37 行 Default Behavior；第 220-249 行 shared/meta cases；第 250-257 行 failure signals | 当前正例要求普通工作留在 base，并明确 meta 路由不应发明新 router layer；静态合同也不等于 live behavior。 |
| `tests/non-trigger-cases.md` | 第 7-18 行 heavy-skill negative cases；第 159-176 行 corrective/meta explicit boundary | 当前负例明确防止小改动被 planning/design/test/review/meta 流程化。 |
| `plugins/capability-harness/skills/capability-harness/SKILL.md` | 第 1-35 行 decision/acceptance seed；第 37-53 行 selected-route/network boundary；第 68-87 行 module/integration | 当前已有可选、决策优先且不为 routine work 增加步骤的相邻 meta 能力，因此目标并非填补完全空白。 |
| `skills/test-strategy/SKILL.md` | 第 3、8 行 | 当前测试职责按明确测试设计/TDD/非显然 proof 触发，且明确不把每项任务变成 strict TDD。 |
| `skills/review-and-finish/SKILL.md` | 第 3、8 行 | 当前完成门按显式 review/done claim 或特定高风险完成变更触发，不对普通实现普遍触发。 |

**未知项**

- 未验证目标 hook 是否已被任何实际 Claude Code 安装加载；启动 gitStatus 只证明 `agent-skills-main/` 在本工作区快照未跟踪，静态 hook 文件本身不能证明 live activation。
- 未运行 hook、路由 eval 或模型行为测试；因此“会注入什么”是脚本静态事实，“模型是否遵守、延迟多少、路由是否稳定”仍未验证。当前测试自己也区分静态合同与 live 行为：`E:\projects\_drafts\tests\trigger-matrix.md` 第 241 行。
- 按用户边界未读取目标 lifecycle Skill bodies，所以未独立验证 meta SKILL 第 111 行所称“Every skill includes a verification step”，也未验证其各路由目标的真实 trigger；本结论只分类 meta 层自身。
- 反谄媚规则及固定 assumptions 模板的“缺失”仅从本次指定当前 prompt、README、tests 和直接相关 Skill 来源推断；未对仓库所有文档或宿主全局指令作绝对不存在声明。
- 未取得用户对是否希望新增一条窄的技术异议默认规则的价值判断；本动作仅为 Phase 2 临时分类，不是修改授权或仓库级风格决定。

##### Meta 对阶段 3“整体流程强度”决策的证据

**支持增加验证门的证据**

- 事实：目标提供了明确、可审计的非平凡实现前假设清单，以及遇到冲突时命名疑点、呈现权衡并等待解决的协议。推论：在材料歧义或高风险决策中，采用“仅限 material uncertainty”的轻量版本可能比隐式假设更早暴露返工风险。位置：`E:\projects\_drafts\agent-skills-main\skills\using-agent-skills\SKILL.md` 第 48-72 行；当前相邻原则位于 `E:\projects\_drafts\prompts\CLAUDE.fragment.md` 第 8、13 行。
- 事实：目标 DoD 将运行时行为、回归、边界/错误路径、集成、文档、安全、可观测性与回滚分别列出。推论：对确有这些受影响面的完成声明，显式 criterion-to-evidence 门可减少“单个 focused test 通过即宣告完成”的遗漏。位置：`E:\projects\_drafts\agent-skills-main\references\definition-of-done.md` 第 21-57 行。
- 事实：当前完成验证测试已要求在工具不可用、回滚证据缺失或已知失败时分别报告 `UNVERIFIED` 或 `BLOCK`，而非 `PASS`；这支持继续保留或加强“与具体风险绑定”的强门，而不是取消验证门。位置：`E:\projects\_drafts\tests\trigger-matrix.md` 第 71-77 行。
- 事实：当前可选 capability harness 已定义 outcome/scope、minimum observable signal、evidence path 和 unresolved risk 的轻量 acceptance seed，并要求 substantive work 在必要时显式化。该现有机制表明，增加前置验证结构有价值的场景可以被限定到实质性工作。位置：`E:\projects\_drafts\plugins\capability-harness\skills\capability-harness\SKILL.md` 第 22-35 行。
- 事实：目标的简化与范围自检具体询问代码行数、抽象收益和无关改动。推论：作为高复杂度实现或完成审查中的短检查项，它们可增强当前“轻流程、限范围”原则，而无需成为独立生命周期。位置：`E:\projects\_drafts\agent-skills-main\skills\using-agent-skills\SKILL.md` 第 85-107 行；当前原则位于 `E:\projects\_drafts\prompts\CLAUDE.fragment.md` 第 9 行。

**反对增加通用验证门的证据**

- 事实：当前套件明确采用“Start lightweight. Escalate only when ... justified”，并说明不把每个编码任务变成正式流程；这直接反对把目标的通用前置流程设为所有任务的默认门。位置：`E:\projects\_drafts\README.md` 第 19-23 行。
- 事实：目标要求开始前检查 Skill、把 Skill 当作不可跳步的 workflow，并在非平凡且无 spec 时默认启动 spec；当前静态路由则把普通编码放在基础层，并只期望最小组合。二者会增加普通任务的强制流程。位置：`E:\projects\_drafts\agent-skills-main\skills\using-agent-skills\SKILL.md` 第 130-139 行；`E:\projects\_drafts\tests\routing-contract.md` 第 16-35、37-61 行。
- 事实：当前负例明确规定小改动不得触发 planning、design、test-design 或 review 流程，且 corrective/meta Skill 必须保持显式；目标的会话级中央路由与默认 spec 会破坏这些负边界。位置：`E:\projects\_drafts\tests\non-trigger-cases.md` 第 7-18、159-176 行。
- 事实：当前 `test-strategy` 明示“不把每个任务变成 strict TDD”；目标 DoD 对每个 change 要求新行为测试在无改动时失败、改动后通过，并列出运行时、文档、集成、可观测性、回滚等常设检查。对低风险、纯说明或只读任务普遍强制这些项目会超出当前按结果与风险验证的边界。位置：`E:\projects\_drafts\skills\test-strategy\SKILL.md` 第 3、8 行；`E:\projects\_drafts\agent-skills-main\references\definition-of-done.md` 第 17-57 行；`E:\projects\_drafts\prompts\CLAUDE.fragment.md` 第 17 行。
- 事实：目标的“mandatory”主要是模型指令而非技术阻断；目标 SessionStart 命令吞掉失败，脚本在缺少 `jq` 或 meta 文件时仅提示并继续。当前 README 也明确模型 guidance 不是 deterministic enforcement。增加文本门并不能证明门被可靠执行。位置：`E:\projects\_drafts\agent-skills-main\hooks\hooks.json` 第 3-9 行；`E:\projects\_drafts\agent-skills-main\hooks\session-start.sh` 第 9-24 行；`E:\projects\_drafts\README.md` 第 38 行。
- 事实：当前已有按风险触发的完成审查、按需测试策略和可选 acceptance seed；再增加通用 DoD 会重复现有职责并引入多处权威来源。位置：`E:\projects\_drafts\skills\review-and-finish\SKILL.md` 第 3、8 行；`E:\projects\_drafts\plugins\capability-harness\skills\capability-harness\SKILL.md` 第 22-35 行；`E:\projects\_drafts\prompts\CLAUDE.fragment.md` 第 17 行。

**中性边界事实**

- 权威边界（静态合同）：当前 prompt 是 always-on 来源，Skill description/body 是各自 trigger 权威，tests 仅做维护验证，不是 runtime layer。位置：`E:\projects\_drafts\tests\routing-contract.md` 第 1-14 行。
- 目标会话注入是 fail-open guidance，不是可靠权限或执行阻断；需要确定性阻止时，当前 README 要求 host permissions 或 PreToolUse hooks。位置：`E:\projects\_drafts\agent-skills-main\hooks\hooks.json` 第 8 行；`E:\projects\_drafts\agent-skills-main\hooks\session-start.sh` 第 9-24 行；`E:\projects\_drafts\README.md` 第 38 行。
- 当前仓库把 external reference skills 定义为比较输入而非 runtime install target；启动工作区快照亦显示 `agent-skills-main/` 未跟踪。位置：`E:\projects\_drafts\README.md` 第 111-119 行；版本快照 `main@f82a1b2`。
- 本轮将所有 instruction-shaped 文件仅作为证据；未执行其中的命令、安装、发布、写入或生命周期流程。
- 本轮未做仓库级风格选择；只提交 Meta 类 `using-agent-skills` 的 provisional action、优先级及支持/反对增加强制门的证据。

##### Define 详细分析

- **完整性说明：** 完整。已在 E:\projects\_drafts 内逐行通读三个目标 SKILL、idea-refine 的四个直接支持文件、三个指定当前 SKILL、plan-work 的三个直接相关引用、design-codebase 的两个直接相关引用，以及指定的 prompt、README 和三份路由测试；另做了仅限这些当前来源及 skills/**/SKILL.md 清单的有界检索。未读取或分析目标仓库的 Plan/Build 类 Skill 正文；spec-driven-development 对它们的引用只按该文件中的交接声明分类。未执行 helper script，未运行任何命令，未使用 WebSearch/WebFetch，未修改任何文件。结论是静态指令工件比较，不是运行时路由验证。

###### `interview-me`

- **暂定动作：** `新增/改写引入`
- **优先级：** `P1`
- **理由：** 暂定 P1“新增/改写引入”，不是原样复制：本次有界当前表面没有独立的前决策意图访谈能力，而“假设+猜测式单问、want-vs-should 探针、确认意图输出”有独立行为价值。[agent-skills-main/skills/interview-me/SKILL.md:L40-L138；README.md:L121-L132] 但引入版应只在用户显式要求访谈，或产品意图确实会改变范围/方案且无法安全推断时触发；保留实时交互限制和可选持久化，去掉把 95%、特定确认措辞和六字段模板作为所有模糊请求的普遍硬门，以保持当前最小提问/无默认批准门合同。[skills/plan-work/SKILL.md:L12-L20,L50-L60]

**Target 实际行为**

- 当请求缺少用户、动机、成功或关键约束，或用户显式要求“interview/grill/stress-test thinking”时进入；明确、自足、纯信息、机械任务及非交互环境排除。[agent-skills-main/skills/interview-me/SKILL.md:L16-L36]
- 第一轮先给一句当前意图假设和 0–100% 置信度；低于约 70% 时说明缺口。[agent-skills-main/skills/interview-me/SKILL.md:L40-L51]
- 每次只问一个聚焦问题并附代理自己的猜测，等待用户反应；遇到最佳实践/身份展示式答案时追问实际想要什么。[agent-skills-main/skills/interview-me/SKILL.md:L53-L92]
- 高置信度时用 Outcome/User/Why now/Success/Constraint/Out of scope 六字段复述，其中非目标被设为必需。[agent-skills-main/skills/interview-me/SKILL.md:L94-L112]
- 只有用户显式 yes 才过门；以能预测用户对下一三个问题的反应作为约 95% 停止测试，并在多轮仍无法预测时停止升级。[agent-skills-main/skills/interview-me/SKILL.md:L113-L132]
- 交付物是已确认的意图陈述；只有用户确认持久化时才保存，并将已确认意图交给 idea/spec 等下游。[agent-skills-main/skills/interview-me/SKILL.md:L134-L139,L180-L186]

**当前已验证覆盖**

- [已验证] 默认 prompt 已要求区分事实、约束和假设，并在意图、价值、授权或不可逆范围只能由用户决定时取用户输入；同时只问会实质改变结果的问题。[prompts/CLAUDE.fragment.md:L6-L16]
- [已验证] plan-work 已覆盖目标一句话、实现约束、实质备选方案、风险、未知和 out-of-scope；需求不清时问最小必要问题。[skills/plan-work/SKILL.md:L18-L36]
- [已验证] design-questions 已覆盖一次一个问题，以及 outcome、使用者、兼容性和约束；它还规定何时比较备选和何时停止询问。[skills/plan-work/references/design-questions.md:L1-L33]
- [已验证] issue-workflow 的 PRD/agent-ready brief 已覆盖问题、方案、验收、测试和 out-of-scope，并只追问改变范围/验收等的事实。[skills/issue-workflow/SKILL.md:L20-L39]
- [已验证] 持久化授权已有通用覆盖：目标自身只在用户确认后保存 intent；当前 prompt 也只在请求或正确性/安全需要时创建持久工件。[agent-skills-main/skills/interview-me/SKILL.md:L134-L139；prompts/CLAUDE.fragment.md:L14-L16]
- [有界缺失] 当前 README 的完整能力图和 skills/**/SKILL.md 清单中没有独立的意图访谈所有者；这只证明本次有界当前表面没有同名/同责 Skill，不证明仓库外或宿主能力不存在。[README.md:L121-L132]

**独有或缺失部分**

- [有界独有] 当前指定来源没有“先公开假设和数值置信度、每问附 GUESS”的协议；现有最接近规则只是一次一个最小问题。该缺失仅限已全读/检索的当前 prompt、三个当前 Skill/相关引用、README 和三份指定测试。[agent-skills-main/skills/interview-me/SKILL.md:L40-L77；skills/plan-work/references/design-questions.md:L1-L11]
- [有界独有] “want vs. should want”信号识别及对应探针在当前指定 Define 相邻来源中无等价步骤。[agent-skills-main/skills/interview-me/SKILL.md:L79-L92；prompts/CLAUDE.fragment.md:L8-L13]
- [有界独有] 六字段逐行确认、对含糊同意的细分处理和“预测下一三个反应”停止测试没有当前等价合同。[agent-skills-main/skills/interview-me/SKILL.md:L94-L132；skills/plan-work/SKILL.md:L33-L36,L50-L60]
- [部分缺失] 当前有非交互时不得猜测的一般原则，但没有专门规定该访谈不得在 CI、/loop 或 autonomous-loop 中运行。[agent-skills-main/skills/interview-me/SKILL.md:L34-L36；prompts/CLAUDE.fragment.md:L8-L13]

**重叠部分**

- [与 plan-work] 两者都澄清 outcome、用户、约束、成功和非目标；区别是 interview-me 产出确认意图而不是实现计划。[agent-skills-main/skills/interview-me/SKILL.md:L94-L138；skills/plan-work/SKILL.md:L22-L36]
- [与 issue-workflow] 六字段 intent restate 与 PRD/agent-ready brief 的问题、验收和 out-of-scope 部分重叠，但 issue-workflow 只在用户明确要持久工作项/PRD 时触发。[agent-skills-main/skills/interview-me/SKILL.md:L94-L111；skills/issue-workflow/SKILL.md:L6-L16,L20-L27]
- [与 idea-refine/spec-driven-development] 目标明确把二者放在确认意图之后；这既提供了可用交接，也证明三者共享需求澄清前沿。[agent-skills-main/skills/interview-me/SKILL.md:L180-L185]
- [与当前默认层] “不要默默填假设”和“只在用户输入会改变结果时问”已存在；独有部分是访谈协议强度，而不是基本澄清原则。[agent-skills-main/skills/interview-me/SKILL.md:L40-L77；prompts/CLAUDE.fragment.md:L8-L13]

**冲突**

- [路由/哲学冲突] 目标把缺少 who/why/success/constraint 中任一项作为使用信号，并要求一直访谈到约 95%；当前默认层和 plan-work 只允许询问会实质改变结果、风险或方法的最小问题。[agent-skills-main/skills/interview-me/SKILL.md:L16-L24,L124-L132；prompts/CLAUDE.fragment.md:L9-L13；skills/plan-work/SKILL.md:L12-L20]
- [流程门冲突] 目标把六字段 restate、Out of scope 和显式 yes 设为不可跳过的实施前门，并拒绝“sounds good/whatever you think”；当前 plan-work 在决策已足够时自动退出到实施，且不默认要求批准门。[agent-skills-main/skills/interview-me/SKILL.md:L94-L136；skills/plan-work/SKILL.md:L50-L60]
- [默认决策冲突] 目标把“whatever you think”视为必须重问；当前 design-questions 明确允许在答案不会改变实现时优先采用已标明的假设。这需要按“产品意图是否负载决策”区分，而不能同时无条件成立。[agent-skills-main/skills/interview-me/SKILL.md:L113-L123；skills/plan-work/references/design-questions.md:L1-L11]
- [目标族内部路由重叠] interview-me 声称自己先于 idea-refine/spec-driven-development，但三者的描述分别以“underspecified ask”“vague idea”“unclear requirements”触发；若无优先级规则，同一句模糊功能请求可同时匹配。[agent-skills-main/skills/interview-me/SKILL.md:L3,L14,L180-L185；agent-skills-main/skills/idea-refine/SKILL.md:L1-L4；agent-skills-main/skills/spec-driven-development/SKILL.md:L1-L4]
- [短语级歧义，尚非运行时事实] “stress-test my thinking/are we sure”可能是前决策意图访谈，也可能是对既有方向的显式可靠性复核；当前 routing-contract 把后一类交给 reliability-check。[agent-skills-main/skills/interview-me/SKILL.md:L18-L24；tests/routing-contract.md:L26-L35]

**维护成本**

- [具体成本] 目标本体为 226 行，并含约 70%、约 95%、“下一三个问题”、多种非确认措辞等状态性规则；需要多轮行为用例，单靠静态 frontmatter/文本检查难以验证。[agent-skills-main/skills/interview-me/SKILL.md:L40-L51,L113-L132,L214-L226；tests/trigger-matrix.md:L241]
- [具体成本] 新增独立 Skill 必须同步 README 能力图、routing-contract、正向触发和负向不触发用例；当前维护规则要求新行为有匹配回归案例，且 tests 不能变成第二运行时层。[README.md:L109-L119；tests/routing-contract.md:L3-L14,L71-L81]
- [持续协调成本] 必须维护与 idea-refine、spec-driven-development、plan-work、issue-workflow、reliability-check 的优先级和交接，否则“模糊/压力测试”短语会多路匹配。[agent-skills-main/skills/interview-me/SKILL.md:L180-L186；tests/routing-contract.md:L26-L40]
- [工件成本] `docs/intent/[topic].md` 会新增一个持久工件约定；若引入，必须继续服从当前“不猜路径、只在明确持久化请求时写入”的边界。[agent-skills-main/skills/interview-me/SKILL.md:L134-L139；prompts/CLAUDE.fragment.md:L14-L16]

**证据**

| 路径 | 位置 | 支持的结论 |
| --- | --- | --- |
| `agent-skills-main/skills/interview-me/SKILL.md` | repo-relative: agent-skills-main/skills/interview-me/SKILL.md:L16-L36（When to Use / Loading Constraints） | 事实：目标的正/负触发条件及只适用于实时交互用户的限制。 |
| `agent-skills-main/skills/interview-me/SKILL.md` | repo-relative: agent-skills-main/skills/interview-me/SKILL.md:L40-L77（Step 1–2） | 事实：先给假设与置信度，再一次一问并附猜测、等待用户反应。 |
| `agent-skills-main/skills/interview-me/SKILL.md` | repo-relative: agent-skills-main/skills/interview-me/SKILL.md:L79-L138（Step 3–5 / 95% Stop / Output） | 事实：want-vs-should 探针、六字段复述、显式 yes、95% 停止条件和输出。 |
| `agent-skills-main/skills/interview-me/SKILL.md` | repo-relative: agent-skills-main/skills/interview-me/SKILL.md:L180-L225（Interaction / Verification） | 事实：目标自述的下游关系及完整验证清单。 |
| `prompts/CLAUDE.fragment.md` | repo-relative: prompts/CLAUDE.fragment.md:L6-L17 | 事实：当前默认层的证据、假设、最小提问、持久化和验证边界。 |
| `skills/plan-work/SKILL.md` | repo-relative: skills/plan-work/SKILL.md:L8-L36,L50-L60 | 事实：当前轻量规划、最小问题、自动退出实施和不默认批准门。 |
| `skills/plan-work/references/design-questions.md` | repo-relative: skills/plan-work/references/design-questions.md:L1-L33 | 事实：当前一次一问、关键澄清项、假设优先条件和停止条件。 |
| `skills/issue-workflow/SKILL.md` | repo-relative: skills/issue-workflow/SKILL.md:L20-L39 | 事实：当前 PRD/brief 字段及最小缺失事实问法。 |
| `README.md` | repo-relative: README.md:L19-L38,L121-L132 | 事实：当前轻量哲学、角色边界和能力图；用于限定“无独立访谈所有者”的有界推论。 |
| `tests/routing-contract.md` | repo-relative: tests/routing-contract.md:L16-L40 | 事实：当前 plan/design/reliability/issue 的路由所有权及最小组合原则。 |

**未知项**

- 是否存在足够频繁的真实“请访谈我”需求来证明新增独立 Skill，而不是在现有最小澄清规则中加一个短参考；本次仓库静态材料无法回答产品采用率。
- 宿主在不同安装中如何稳定维持多轮 Skill 状态未由本次指定来源证明；静态路由测试不能证明实时模型行为。[README.md:L38；tests/trigger-matrix.md:L241]
- “显式 yes”在不同语言/对话语境中的可靠判定没有可执行规范；目标只列示例措辞。[agent-skills-main/skills/interview-me/SKILL.md:L113-L123]

###### `idea-refine`

- **暂定动作：** `新增/改写引入`
- **优先级：** `P2`
- **理由：** 暂定 P2“新增/改写引入”，仅作为可选、明确意图的轻量 ideation Skill，而非复制五文件包。其真正缺口是 HMW/JTBD/SCAMPER 等发散镜头和“价值—可行性—差异化—关键假设”产品收敛；当前 plan/design/issue 只覆盖其收敛与工件部分。[agent-skills-main/skills/idea-refine/frameworks.md:L19-L99；agent-skills-main/skills/idea-refine/refinement-criteria.md:L5-L113；README.md:L121-L132] 改写版应把固定数量变为上限/按需、默认只在聊天输出、不带目录初始化脚本，并明确不接管实现规划或架构边界。因暂无仓库证据证明该需求高频，优先级低于 interview 的明确意图缺口，也不是最终引入授权。

**Target 实际行为**

- 以交互式“发散→收敛→交付”三阶段把原始想法变成可行动 one-pager。[agent-skills-main/skills/idea-refine/SKILL.md:L10-L18,L52-L55]
- 先用 HMW 重述，问 3–5 个关于用户、成功、约束、历史和 why-now 的问题，并在理解用户与成功前不继续。[agent-skills-main/skills/idea-refine/SKILL.md:L56-L70]
- 用 7 类镜头生成 5–8 个变体；在代码库内则扫描现有架构/模式/约束，并可选择性使用额外 frameworks。[agent-skills-main/skills/idea-refine/SKILL.md:L71-L84；agent-skills-main/skills/idea-refine/frameworks.md:L1-L100]
- 用户反应后聚类成 2–3 个方向，按用户价值、可行性、差异化评价，并列出赌注、致命条件和暂时忽略项。[agent-skills-main/skills/idea-refine/SKILL.md:L86-L106；agent-skills-main/skills/idea-refine/refinement-criteria.md:L5-L103]
- 产出 Problem/Recommended direction/Assumptions to validate/MVP/Not Doing/Open Questions one-pager，并在实施前要求用户确认方向。[agent-skills-main/skills/idea-refine/SKILL.md:L108-L140,L168-L179]
- 可选 helper 只负责创建 `docs/ideas`；主流程询问后才保存最终文件。[agent-skills-main/skills/idea-refine/SKILL.md:L20-L23,L138-L140；agent-skills-main/skills/idea-refine/scripts/idea-refine.sh:L1-L15]

**当前已验证覆盖**

- [已验证] plan-work 已覆盖检查当前代码/文档、目标、约束、实质方案比较、推荐、风险、未知和非目标。[skills/plan-work/SKILL.md:L22-L36]
- [已验证] design-codebase 已覆盖按当前项目证据导出决策标准、比较最小实质选项、推荐方案、迁移影响、验证和 out-of-scope。[skills/design-codebase/SKILL.md:L21-L30]
- [已验证] design-it-twice 已提供多镜头架构探索，但明确不设固定选项数并要求给出推荐；这是 idea-refine 收敛半段在架构域的现有覆盖。[skills/design-codebase/references/design-it-twice.md:L3-L26]
- [已验证] issue-workflow 的 PRD 已覆盖问题、方案、决策、测试和 out-of-scope；agent-ready brief 覆盖行为、接口和验收。[skills/issue-workflow/SKILL.md:L20-L39]
- [已验证] 当前持久计划默认留在聊天，只在用户明确请求文件时写入；默认 prompt 同样限制持久工件。[skills/plan-work/SKILL.md:L38-L43；prompts/CLAUDE.fragment.md:L14-L16]
- [有界缺失] 当前 README 自动/显式 Skill 表与 skills/**/SKILL.md 清单没有独立的“发散产品/流程创意”所有者；这不证明宿主或仓库外无此能力。[README.md:L40-L67,L121-L132]

**独有或缺失部分**

- [有界独有] 当前指定来源没有完整的 HMW、SCAMPER、JTBD、约束式创意、pre-mortem、类比灵感发散工具箱。[agent-skills-main/skills/idea-refine/frameworks.md:L5-L100；README.md:L121-L132]
- [有界独有] 当前相邻 Skill 没有产品层面的 user-value/feasibility/differentiation 三维 rubric；design-codebase 的标准限于项目架构决策。[agent-skills-main/skills/idea-refine/refinement-criteria.md:L5-L74；skills/design-codebase/SKILL.md:L25-L30]
- [有界独有] Must/Should/Might-be-true 假设分层及“MVP 首先验证最危险假设”没有当前等价 Define 合同。[agent-skills-main/skills/idea-refine/refinement-criteria.md:L75-L113]
- [部分缺失] 当前可写 PRD，但没有在形成 PRD/计划前专门生成多种产品或流程方向的明确路由。[agent-skills-main/skills/idea-refine/examples.md:L176-L218；skills/issue-workflow/SKILL.md:L20-L39；tests/routing-contract.md:L26-L35]
- [非独有] one-pager、推荐、风险、非目标和代码库取证均已有现有覆盖，不构成新增理由。[agent-skills-main/skills/idea-refine/SKILL.md:L82-L84,L108-L140；skills/plan-work/SKILL.md:L22-L43；skills/issue-workflow/SKILL.md:L20-L39]

**重叠部分**

- [与 plan-work] Phase 2/3 的方案选择、可行性、风险、推荐、MVP 范围和非目标与实现规划高度重叠。[agent-skills-main/skills/idea-refine/SKILL.md:L86-L140；skills/plan-work/SKILL.md:L22-L36]
- [与 design-codebase] “代码库感知的变体”和架构选项比较与 design-codebase/design-it-twice 重叠；仅产品价值/受众发散超出其架构域。[agent-skills-main/skills/idea-refine/SKILL.md:L71-L84,L90-L106；skills/design-codebase/SKILL.md:L21-L30；skills/design-codebase/references/design-it-twice.md:L3-L20]
- [与 issue-workflow] 最终 one-pager 的问题、推荐、假设、MVP、非目标和开放问题与 PRD/agent-ready brief 大幅重叠。[agent-skills-main/skills/idea-refine/SKILL.md:L108-L140；skills/issue-workflow/SKILL.md:L20-L39]
- [与 interview-me] 两者都问用户、成功、约束和 why now；目标定义的合理分界是 interview 先确认真实意图，idea-refine 再扩展解决方向。[agent-skills-main/skills/idea-refine/SKILL.md:L56-L80；agent-skills-main/skills/interview-me/SKILL.md:L180-L183]

**冲突**

- [路由冲突] “stress-test my plan”和方案比较已落入当前 plan-work；代码库中的非显然架构方案比较落入 design-codebase。idea-refine 同时声明这两种触发，若不收窄会抢占现有所有者。[agent-skills-main/skills/idea-refine/SKILL.md:L25-L29,L82-L104；tests/routing-contract.md:L26-L27]
- [流程哲学冲突] 固定 3–5 问、5–8 变体、2–3 方向与当前“最小有用方案集、不要为固定数量制造备选”相冲突。[agent-skills-main/skills/idea-refine/SKILL.md:L60-L80,L86-L104；skills/plan-work/SKILL.md:L18-L20；skills/design-codebase/references/design-it-twice.md:L3-L20]
- [架构所有权冲突] 目标要求在代码库中扫描架构并据此生成方案；示例直接推荐 WebSocket/锁字段等结构。当前 design-codebase 要先读直接调用者、依赖、测试和约束，并只在真实边界压力存在时作架构结论。[agent-skills-main/skills/idea-refine/SKILL.md:L82-L84；agent-skills-main/skills/idea-refine/examples.md:L130-L172；skills/design-codebase/SKILL.md:L21-L30,L44-L55]
- [持久化/副作用摩擦] 主 Skill 最终会询问是否保存，和当前授权边界大体一致；但可选 helper 一运行就创建 `docs/ideas`，且主文把“具体 markdown 工件”列为验证要求。自动运行 helper 会把对话式探索变成未必需要的持久工件。[agent-skills-main/skills/idea-refine/SKILL.md:L20-L23,L30-L38,L138-L140,L168-L179；agent-skills-main/skills/idea-refine/scripts/idea-refine.sh:L1-L15；prompts/CLAUDE.fragment.md:L14-L16]
- [目标族内部冲突] interview-me 说意图未清时先访谈、意图已确认但不会定范围时才交 idea-refine；idea-refine 自己却以“idea is still vague”自动触发。需要明确“问题/意图未知”与“意图已知、解空间开放”的分界。[agent-skills-main/skills/interview-me/SKILL.md:L180-L183；agent-skills-main/skills/idea-refine/SKILL.md:L1-L4,L56-L80]

**维护成本**

- [具体体量] 目标由 5 个文件、合计 647 行组成（179 行主 Skill、239 行示例、100 行 frameworks、114 行 rubric、15 行 shell helper）；原样引入会形成当前 Define 候选中最大的维护面。[agent-skills-main/skills/idea-refine/SKILL.md:L1-L179；agent-skills-main/skills/idea-refine/examples.md:L1-L239；agent-skills-main/skills/idea-refine/frameworks.md:L1-L100；agent-skills-main/skills/idea-refine/refinement-criteria.md:L1-L114；agent-skills-main/skills/idea-refine/scripts/idea-refine.sh:L1-L15]
- [重复漂移成本] 收敛、方案比较、风险、非目标和持久工件规则已经分别存在于 plan-work、design-codebase、issue-workflow；四处同时维护同义规则易漂移。[skills/plan-work/SKILL.md:L22-L43；skills/design-codebase/SKILL.md:L21-L30；skills/issue-workflow/SKILL.md:L20-L39]
- [路由测试成本] 至少需要区分：意图未知→interview；解空间开放→idea-refine；软件实现方案→plan-work；架构边界→design-codebase；PRD/工作项→issue-workflow，并为“stress-test”增加正负回归。[tests/routing-contract.md:L26-L40,L71-L81]
- [宿主/平台成本] 主文硬编码 `AskUserQuestion`，helper 硬编码 Bash 与相对目录；当前 README 允许多种安装组合，指定来源未证明所有宿主都有该工具或 shell。[agent-skills-main/skills/idea-refine/SKILL.md:L20-L23,L69；agent-skills-main/skills/idea-refine/scripts/idea-refine.sh:L1-L15；README.md:L69-L88]
- [内容维护成本] 大量产品启发式与示例会随项目语境变成意见性负担；当前 README 要求运行时层避免解释性重复并保持一个密切相关的决策族。[README.md:L117-L119]

**证据**

| 路径 | 位置 | 支持的结论 |
| --- | --- | --- |
| `agent-skills-main/skills/idea-refine/SKILL.md` | repo-relative: agent-skills-main/skills/idea-refine/SKILL.md:L10-L38（How It Works / Usage / Output） | 事实：三阶段流程、触发短语、helper 调用和目标工件。 |
| `agent-skills-main/skills/idea-refine/SKILL.md` | repo-relative: agent-skills-main/skills/idea-refine/SKILL.md:L52-L106（Phase 1–2） | 事实：固定问题/变体数量、代码库扫描、聚类、评价和假设审计。 |
| `agent-skills-main/skills/idea-refine/SKILL.md` | repo-relative: agent-skills-main/skills/idea-refine/SKILL.md:L108-L179（Phase 3 / Verification） | 事实：one-pager 结构、保存确认、反模式与实施前确认。 |
| `agent-skills-main/skills/idea-refine/frameworks.md` | repo-relative: agent-skills-main/skills/idea-refine/frameworks.md:L1-L100 | 事实：SCAMPER、HMW、第一性原理、JTBD、约束、pre-mortem 和类比等发散镜头。 |
| `agent-skills-main/skills/idea-refine/refinement-criteria.md` | repo-relative: agent-skills-main/skills/idea-refine/refinement-criteria.md:L1-L114 | 事实：用户价值、可行性、差异化、三层假设审计、决策矩阵和 MVP 规则。 |
| `agent-skills-main/skills/idea-refine/examples.md` | repo-relative: agent-skills-main/skills/idea-refine/examples.md:L1-L3,L130-L172,L176-L239 | 事实：示例自称用于节奏/结构；展示代码库感知和非产品流程适用范围。示例仅作意图证据，不当成当前指令。 |
| `agent-skills-main/skills/idea-refine/scripts/idea-refine.sh` | repo-relative: agent-skills-main/skills/idea-refine/scripts/idea-refine.sh:L1-L15 | 事实：helper 只检查/创建 docs/ideas 并输出 JSON；本次未执行。 |
| `skills/plan-work/SKILL.md` | repo-relative: skills/plan-work/SKILL.md:L18-L43 | 事实：最小问题/方案集、规划输出及聊天优先持久化边界。 |
| `skills/design-codebase/SKILL.md` | repo-relative: skills/design-codebase/SKILL.md:L21-L30,L44-L63 | 事实：当前架构证据要求、最小选项和按真实压力使用镜头。 |
| `skills/design-codebase/references/design-it-twice.md` | repo-relative: skills/design-codebase/references/design-it-twice.md:L3-L26 | 事实：当前架构备选探索不设固定数量，推荐必须明确。 |
| `skills/issue-workflow/SKILL.md` | repo-relative: skills/issue-workflow/SKILL.md:L20-L39 | 事实：当前 PRD/brief 与目标 one-pager 的重叠字段。 |
| `tests/routing-contract.md` | repo-relative: tests/routing-contract.md:L16-L40 | 事实：当前 planning、architecture、PRD 和 reliability 路由所有权。 |

**未知项**

- 仓库没有使用数据或失败案例证明固定发散流程是重复真实需要；因此新增独立 Skill 的需求强度未知。
- 不同宿主是否支持 `AskUserQuestion` 及 Bash 未由指定当前材料建立；helper 的可移植性未知。[agent-skills-main/skills/idea-refine/SKILL.md:L20-L23,L69]
- 产品/市场启发式的适用性没有外部证据，本任务又明确禁止 Web；这里只能把它们分类为目标的意见性行为，不能证明其普遍有效。

###### `spec-driven-development`

- **暂定动作：** `合并/协调重叠`
- **优先级：** `P0`
- **理由：** 暂定 P0“合并/协调重叠”，其中 P0 表示在任何吸收前必须先解决路由冲突，不表示批准原样引入。不要新增一个贯穿 Specify→Implement 的总控 Skill；把“用户显式要求工程 spec 时的需求工件”协调到 issue-workflow（或明确选定的单一 Define 工件所有者），只保留经验证项目事实、目标/用户/成功、关键假设、边界和开放问题；架构交 design-codebase，实施规划交 plan-work，测试/完成仍由现有所有者处理。[skills/issue-workflow/SKILL.md:L20-L39；tests/routing-contract.md:L16-L61] 删除自动大小/时长触发、四段普遍批准、固定 tasks 路径、约 5 文件阈值和自动 commit/PR 要求。[agent-skills-main/skills/spec-driven-development/SKILL.md:L12-L32,L141-L178]

**Target 实际行为**

- 在新项目/feature、模糊需求、多文件、架构决策或预计超过 30 分钟时，要求编码前先写结构化规格。[agent-skills-main/skills/spec-driven-development/SKILL.md:L8-L20]
- 采用 SPECIFY→PLAN→TASKS→IMPLEMENT 四阶段，每阶段都要人工 review 后才能前进。[agent-skills-main/skills/spec-driven-development/SKILL.md:L22-L32]
- 规格前先列假设；规格覆盖目标、命令、目录结构、代码风格、测试策略和 Always/Ask/Never 边界，并含技术栈、成功条件和开放问题。[agent-skills-main/skills/spec-driven-development/SKILL.md:L34-L115]
- 把模糊要求改写成具体可测成功条件并请求确认。[agent-skills-main/skills/spec-driven-development/SKILL.md:L117-L129]
- 经确认规格后生成技术计划和单会话任务，每个任务有验收、验证和文件清单，并写入固定 tasks 路径。[agent-skills-main/skills/spec-driven-development/SKILL.md:L131-L165]
- 按其他目标 Plan/Build Skill 执行；规格作为 living document，决策/范围变化先更新，并要求版本控制与 PR 引用。[agent-skills-main/skills/spec-driven-development/SKILL.md:L167-L178]

**当前已验证覆盖**

- [已验证] issue-workflow 已有 PRD（问题、方案、决策、测试、非目标）和 agent-ready brief（当前/期望行为、接口、验收、非目标），能承接大部分显式需求工件请求。[skills/issue-workflow/SKILL.md:L20-L39]
- [已验证] plan-work 已有目标、约束、方案、执行步骤、验证、风险和未知，并对持久计划提供模板与明确授权边界。[skills/plan-work/SKILL.md:L22-L48；skills/plan-work/references/plan-template.md:L1-L58]
- [已验证] design-codebase 已拥有架构、所有权、接口和依赖边界决策，并在必要时交回 plan-work 处理 rollout/sequencing。[skills/design-codebase/SKILL.md:L10-L30,L65-L76]
- [已验证] 默认 prompt 已覆盖假设与事实分离、复用现有项目约定、行动特定授权、验收/风险验证。[prompts/CLAUDE.fragment.md:L6-L17]
- [已验证到路由层，未读正文] README 将测试设计交给 test-strategy、完成审查交给 review-and-finish，而不是由一个 spec Skill 贯穿。[README.md:L42-L55,L121-L132]
- [有界缺失] 当前能力图、routing-contract 和 skills/**/SKILL.md 清单没有明确的“请写工程 specification”独立路由；现有最接近入口是 issue-workflow 的 PRD/agent-ready brief。此为有界缺失，不是仓库外/宿主级证明。[README.md:L40-L67,L121-L132；tests/routing-contract.md:L16-L35]

**独有或缺失部分**

- [部分独有] 当前相邻来源没有把 Objective、项目命令、结构、风格、测试、行为边界、成功条件和开放问题集中为一个显式工程 spec 契约。[agent-skills-main/skills/spec-driven-development/SKILL.md:L51-L115；skills/issue-workflow/SKILL.md:L20-L39；skills/plan-work/references/plan-template.md:L5-L49]
- [有界缺失] 当前 routing-contract 未命名“write a technical specification”入口；显式 PRD/brief 有入口，但工程 spec 的归属需决定。[tests/routing-contract.md:L16-L35；skills/issue-workflow/SKILL.md:L20-L27]
- [部分独有] “需求变化先更新 living spec”及从 PR 链接具体 spec section 在当前指定来源中无等价合同；这也是额外维护负担，不自动等于应采用。[agent-skills-main/skills/spec-driven-development/SKILL.md:L171-L178]
- [非独有] 假设显式化、可测成功、边界、计划、任务验收和验证都已有分散覆盖；缺的是统一工件，不是这些原则本身。[agent-skills-main/skills/spec-driven-development/SKILL.md:L38-L49,L117-L165；prompts/CLAUDE.fragment.md:L8-L17；skills/plan-work/SKILL.md:L22-L36]

**重叠部分**

- [与 issue-workflow] Objective、success criteria、boundaries、open questions 与 PRD/agent-ready brief 高度重叠。[agent-skills-main/skills/spec-driven-development/SKILL.md:L51-L115；skills/issue-workflow/SKILL.md:L20-L39]
- [与 plan-work] Phase 2/3 的组件、依赖、顺序、风险、并行、验收和验证几乎完全属于当前 plan-work/vertical-slices。[agent-skills-main/skills/spec-driven-development/SKILL.md:L131-L165；skills/plan-work/SKILL.md:L22-L48；skills/plan-work/references/vertical-slices.md:L3-L11]
- [与 design-codebase] 架构决策触发和技术方案内容重叠，但当前设计 Skill 有更窄的所有权与证据门。[agent-skills-main/skills/spec-driven-development/SKILL.md:L14-L18,L131-L145；skills/design-codebase/SKILL.md:L10-L30]
- [与默认 prompt] 假设显式化、边界、授权和验收验证已有通用原则；目标增加的是单一持久规格中的集中表达。[agent-skills-main/skills/spec-driven-development/SKILL.md:L38-L49,L77-L80,L198-L207；prompts/CLAUDE.fragment.md:L8-L17]
- [与目标 interview-me] 两者都处理模糊需求；interview 产出确认意图，spec 才应把已确认意图结构化，目标 interview 文档已经给出这一交接方向。[agent-skills-main/skills/interview-me/SKILL.md:L180-L184]

**冲突**

- [核心哲学冲突] 目标按新 feature、多文件、架构决策或 >30 分钟自动触发四阶段人工 review；当前套件明确大/多文件不是自动规划触发器，并坚持 ordinary coding 轻量。[agent-skills-main/skills/spec-driven-development/SKILL.md:L12-L32；README.md:L19-L23；skills/plan-work/SKILL.md:L12-L20]
- [角色边界冲突] 一个 Skill 同时拥有 Specify、Plan、Tasks、Implement，且在实施阶段指定其他 Build 技能；当前仓库按角色拆分默认、plan、design、test/review 等所有者，要求最小组合。[agent-skills-main/skills/spec-driven-development/SKILL.md:L22-L32,L131-L170；README.md:L25-L35,L121-L132；tests/routing-contract.md:L37-L61]
- [当前所有者冲突] 目标把架构决定作为 spec 触发条件，却没有先交给 design-codebase；当前路由要求先解决架构/所有权/接口边界，再规划依赖的 rollout。[agent-skills-main/skills/spec-driven-development/SKILL.md:L14-L18；skills/design-codebase/SKILL.md:L10-L19；tests/routing-contract.md:L43-L45]
- [工件授权冲突] 目标硬编码创建 `tasks/plan.md`、`tasks/todo.md` 和 `tasks/`；当前 plan-work 只在用户明确要求文件时写入，并且只能使用用户命名路径，不得猜测或复制目标。[agent-skills-main/skills/spec-driven-development/SKILL.md:L141-L165；skills/plan-work/SKILL.md:L38-L48,L57-L61]
- [Git 授权冲突] “Commit the spec”被写成常规保持动作；当前 prompt 明确 review/done 不授权 commit，分支动作必须单独授权并由 finish-branch 路由。[agent-skills-main/skills/spec-driven-development/SKILL.md:L171-L178；prompts/CLAUDE.fragment.md:L14-L15；tests/routing-contract.md:L23-L25]
- [机械门冲突] “每任务不超过约 5 文件”和规格六区全齐是固定代理指标；当前 vertical-slices 以独立可见/可验证行为为单位，而非文件数。[agent-skills-main/skills/spec-driven-development/SKILL.md:L51-L80,L147-L165；skills/plan-work/references/vertical-slices.md:L3-L11,L28-L33]
- [目标族内部路由冲突] spec 以“requirements unclear/vague idea”直接触发，而 interview-me 宣称此时应先确认真实意图；必须决定优先级，不能让两个强制门叠加。[agent-skills-main/skills/spec-driven-development/SKILL.md:L1-L4,L12-L20；agent-skills-main/skills/interview-me/SKILL.md:L8-L15,L180-L184]
- [范围张力] 目标一处排除单行修复，另一处又主张简单任务仍需两行 spec/acceptance criteria，并把任何无书面需求编码列为红旗；这会让触发边界难以稳定测试。[agent-skills-main/skills/spec-driven-development/SKILL.md:L20,L180-L196]

**维护成本**

- [跨域维护成本] 207 行目标正文同时重复 Define、Plan、Build、测试和提交规则；每个现有所有者变化都可能使该总控文档漂移。[agent-skills-main/skills/spec-driven-development/SKILL.md:L1-L207；README.md:L121-L132]
- [命名/依赖成本] 目标引用 `planning-and-task-breakdown`、`incremental-implementation`、`test-driven-development`、`context-engineering`，而当前表面使用 plan-work/test-strategy 等角色；必须重写交接或维护别名。本次依约未分析那些目标 Plan/Build Skill 正文。[agent-skills-main/skills/spec-driven-development/SKILL.md:L131-L170；README.md:L42-L55]
- [工件新鲜度成本] “决策/范围变化先更新 spec、提交 spec、PR 链接 spec”会要求持续双向同步；若不是用户选择的 source of truth，容易产生额外陈旧状态。[agent-skills-main/skills/spec-driven-development/SKILL.md:L171-L178；prompts/CLAUDE.fragment.md:L9,L16]
- [测试矩阵成本] 需要为 feature 大小、模糊程度、架构阻塞、显式 spec 请求、已有 PRD/计划、持久化路径和审批状态建立正负路由，且不能破坏现有小改动/多文件非触发案例。[tests/non-trigger-cases.md:L13-L23,L41-L44；tests/trigger-matrix.md:L182-L190]
- [模板漂移成本] 强制复制 commands、structure、style、testing、boundaries 等项目级信息到每个 feature spec，可能与仓库现有配置/文档重复；当前默认要求复用现有来源而非复制。[agent-skills-main/skills/spec-driven-development/SKILL.md:L51-L115；prompts/CLAUDE.fragment.md:L6-L9,L16]

**证据**

| 路径 | 位置 | 支持的结论 |
| --- | --- | --- |
| `agent-skills-main/skills/spec-driven-development/SKILL.md` | repo-relative: agent-skills-main/skills/spec-driven-development/SKILL.md:L8-L32（Overview / When to Use / Gated Workflow） | 事实：宽触发条件及四阶段逐段人工验证门。 |
| `agent-skills-main/skills/spec-driven-development/SKILL.md` | repo-relative: agent-skills-main/skills/spec-driven-development/SKILL.md:L34-L129（Phase 1: Specify） | 事实：假设清单、六类规格内容、模板和量化成功条件。 |
| `agent-skills-main/skills/spec-driven-development/SKILL.md` | repo-relative: agent-skills-main/skills/spec-driven-development/SKILL.md:L131-L170（Plan / Tasks / Implement） | 事实：跨 Plan/Build 的交接、固定任务路径、文件数阈值和实施依赖。未据此读取被禁止的目标 Plan/Build Skill。 |
| `agent-skills-main/skills/spec-driven-development/SKILL.md` | repo-relative: agent-skills-main/skills/spec-driven-development/SKILL.md:L171-L207（Living Spec / Rationalizations / Verification） | 事实：先更新 spec、提交/PR 引用、简单任务立场和实施前核对表。 |
| `skills/issue-workflow/SKILL.md` | repo-relative: skills/issue-workflow/SKILL.md:L6-L39 | 事实：当前显式 PRD/工作项所有权、聊天默认和规格相邻字段。 |
| `skills/plan-work/SKILL.md` | repo-relative: skills/plan-work/SKILL.md:L8-L20,L22-L61 | 事实：当前规划触发、内容、持久化和无默认批准门。 |
| `skills/plan-work/references/plan-template.md` | repo-relative: skills/plan-work/references/plan-template.md:L1-L58 | 事实：当前持久计划已覆盖目标、上下文、非目标、方法、步骤、风险和验证。 |
| `skills/plan-work/references/vertical-slices.md` | repo-relative: skills/plan-work/references/vertical-slices.md:L1-L33 | 事实：当前以完整可验证行为而非文件数切片。 |
| `skills/design-codebase/SKILL.md` | repo-relative: skills/design-codebase/SKILL.md:L10-L30,L65-L76 | 事实：当前架构所有权与 plan-work 交接边界。 |
| `prompts/CLAUDE.fragment.md` | repo-relative: prompts/CLAUDE.fragment.md:L6-L17 | 事实：当前假设、比例性、授权、工件和验证默认。 |
| `README.md` | repo-relative: README.md:L19-L38,L121-L132 | 事实：当前轻量哲学、按角色拆分及能力图。 |
| `tests/routing-contract.md` | repo-relative: tests/routing-contract.md:L16-L61 | 事实：当前 plan/design/issue/test/review 的所有权与组合顺序。 |

**未知项**

- 仓库是否希望支持一个明确命名的工程 spec 工件、以及它应属于 issue-workflow 还是另一个单一 Define 所有者，是产品/维护选择，当前材料不能决定。
- 若允许持久 spec，仓库没有在指定来源中给出规范路径；目标的 `tasks/` 路径仅适用于其自身约定，不能据此推断当前路径。[agent-skills-main/skills/spec-driven-development/SKILL.md:L141-L165；skills/plan-work/SKILL.md:L38-L43,L61]
- 本次依用户边界未读取目标 Plan/Build Skill 正文，也未读取当前 test-strategy 正文；因此只确认了路由归属和 spec 文件写出的交接，不评价下游方法质量。

##### Define 对阶段 3“整体流程强度”决策的证据

**支持增加验证门的证据**

- [目标源内论证，非外部实证] interview-me 把“在计划、规格或代码之前发现目标错配”视为最低成本时点，并用用户、成功、约束、非目标和显式确认形成可检查的意图输出；这支持在真实产品意图仍不确定时设置有界确认门。[agent-skills-main/skills/interview-me/SKILL.md:L8-L15,L94-L138]
- [已验证机制] idea-refine 要求在收敛前列出核心赌注、致命条件和暂不处理项，并为关键假设附验证方式；其 rubric 又区分 dealbreaker/important/nice-to-have，并要求 MVP 优先检验最危险假设。这支持对高不确定新方向增加假设验证门。[agent-skills-main/skills/idea-refine/SKILL.md:L86-L106,L121-L138,L168-L179；agent-skills-main/skills/idea-refine/refinement-criteria.md:L75-L113]
- [已验证机制] spec-driven-development 在写规格前显式暴露假设，并把模糊要求改写为可测成功条件；对于昂贵或难逆的范围，这类门能把隐含分歧变成可审查条件。[agent-skills-main/skills/spec-driven-development/SKILL.md:L34-L49,L117-L129]
- [已验证当前选择性门] 当前默认层已经要求由用户解决意图、价值、授权或不可逆范围，并要求按验收标准、受影响契约和具体风险验证；这支持“按风险选择性加门”，而非完全无门。[prompts/CLAUDE.fragment.md:L8-L17]
- [已验证当前定义/发布门] issue-workflow 只问会改变范围、归属、验收或发布目标的缺失事实，并在外部发布前确认系统、项目和具体动作；这表明当前仓库接受围绕持久/外部结果的强制门。[skills/issue-workflow/SKILL.md:L29-L52]

**反对增加通用验证门的证据**

- [已验证当前边界] 当前套件明确要求“Start lightweight”，并明确不把每个编码任务变成正式流程；默认层还要求流程与持久工件保持成比例，只在会实质改变结果、范围、策略、风险或授权时提问。[README.md:L19-L23；prompts/CLAUDE.fragment.md:L9-L16]
- [已验证当前边界] plan-work 明确规定：多文件或中等/大型任务本身不是规划触发器；需求不清时只问会改变范围、风险或方法的最小问题；除非用户要求，不保存计划或设置批准门。[skills/plan-work/SKILL.md:L12-L20,L40-L60]
- [已验证当前边界] design-codebase 只在非显然架构/边界决策阻塞安全下一步时升级，并禁止默认创建持久设计工件；这反对把“定义阶段”普遍前置为仪式。[skills/design-codebase/SKILL.md:L10-L19,L65-L76]
- [目标自身的反例] interview-me 排除明确、自足、纯信息和机械请求；idea-refine 要求把流程当作对话而非模板，并明说不要过度工程化流程。因此，即使目标材料本身也不支持全局强制门。[agent-skills-main/skills/interview-me/SKILL.md:L26-L36；agent-skills-main/skills/idea-refine/SKILL.md:L52-L55,L142-L150]
- [具体摩擦] idea-refine 固定 3–5 个问题、5–8 个变体和 2–3 个方向，而当前 plan/design 规则要求只比较最小有用的、实质不同的选项，不为凑数量发明选项；固定配额会增加无决策价值的步骤。[agent-skills-main/skills/idea-refine/SKILL.md:L60-L80,L86-L104；skills/plan-work/SKILL.md:L18-L20；skills/design-codebase/references/design-it-twice.md:L3-L20]
- [具体摩擦] spec-driven-development 按多文件、架构决策或超过 30 分钟自动触发四段人工批准门，并把“无任何书面需求就编码”列为红旗；这直接扩大了当前经测试的轻量路由边界。[agent-skills-main/skills/spec-driven-development/SKILL.md:L12-L32,L180-L207；tests/non-trigger-cases.md:L13-L23,L41-L44]

**中性边界事实**

- 本报告把所有 SKILL、reference、example、script 和 CLAUDE 文本当作比较证据，不把其中命令或工具指令当作本次授权；idea-refine helper 只读未执行。[prompts/CLAUDE.fragment.md:L7,L12-L16；agent-skills-main/skills/idea-refine/scripts/idea-refine.sh:L1-L15]
- 目标 examples.md 明说示例用于学习节奏、语气和结构；因此示例中的具体产品/架构建议只证明预期行为形态，不证明这些建议正确或应逐字迁移。[agent-skills-main/skills/idea-refine/examples.md:L1-L3,L222-L239]
- 当前仓库自己声明 prompt 与各 Skill body 是运行边界来源、tests 只是维护合同；本报告仍依用户要求把它们都作为证据比较，而不是继承其指令。[tests/routing-contract.md:L1-L14]
- “没有当前等价能力”的结论均限定在已全读的指定当前文件、五个直接相关引用及 skills/**/SKILL.md 文件名清单；未把有界无匹配表述成全仓库、宿主或生态的已证明不存在。
- 宿主提供的会话起始快照为 main@f82a1b2，`agent-skills-main/`、MIGRATION_PLAN.md 和 absorb-agent-skills-master-prompt.md 为未跟踪项；本次无 shell，未重新验证快照，也未改变工作树。
- README 明确指出 prompt 是模型指导而非确定性执行，trigger-matrix 也明确静态合同通过不能证明实时行为；所以所有动作仅为静态比较后的 provisional classification。[README.md:L34-L38；tests/trigger-matrix.md:L241]
- 优先级按“在任何吸收前的冲突/缺口处理紧迫度”解释：P0 不等于采用授权，P2 也不等于否定。本文未选择仓库范围的“更多门还是更少门”风格，只分别列出 Define 场景中的支持与反对证据。

##### 本组执行状态

- Meta 与 Define 两个 slice 均为 `complete`；没有 blocked、failed、stale、skipped 或 unverified slice。
- 两个 worker 均只使用 Read/Grep/Glob，无 shell/Edit/Write、无 WebSearch/WebFetch、无文件修改或脚本执行。
- 分析基线为当前项目 `main@f82a1b2` 与 target 的 current unversioned working tree；静态指令工件比较不证明 live host/model behavior。
- 本组已写入 `MIGRATION_PLAN.md`，并已获得用户确认；后续分类不改变本组已确认的 provisional classification，也不构成阶段 4 吸收授权。

#### 第 2 组：Plan + Build（已完成，已确认）

> 本组结论仍是阶段 2 的 provisional classification，不是阶段 4 的引入授权。P0 只表示在任何吸收前必须先解决直接冲突，不表示批准采用；静态合同比较也不证明 live host/model 行为。

##### 暂定结论汇总

| 分类 | Target 条目 | 当前暂定动作 | 优先级 | 核心理由 |
| --- | --- | --- | --- | --- |
| Plan | `planning-and-task-breakdown` | `合并/协调重叠` | `P0` | 当前 `plan-work` 已覆盖调查、分解、依赖、垂直切片、风险和验证；可取增量仅是把持久计划步骤中的可观察结果显式命名为 `Acceptance`，并可按需标注阻塞/可并行关系。目标的默认 `tasks/*` 落盘、固定检查点、人工批准、文件数/时长阈值和普遍 DoD 与当前权限和轻量合同直接冲突。[`skills/plan-work/SKILL.md:L8-L20,L33-L62`；`agent-skills-main/skills/planning-and-task-breakdown/SKILL.md:L79-L149,L203-L234`] |
| Build | `incremental-implementation` | `合并/协调重叠` | `P0` | 最小完整可验证片、contract-first/risk-first 和保持工作状态有窄增量价值，但普通多文件工作已有 base + `test-strategy` 覆盖；每片自动 commit、固定全套检查和按行数触发越过 Git、命令副作用和路由边界。[`agent-skills-main/skills/incremental-implementation/SKILL.md:L21-L87,L199-L249`；`skills/finish-branch/SKILL.md:L8-L30,L46-L55`] |
| Build | `test-driven-development` | `跳过` | `P1` | `test-strategy`、`tdd-mode`、`good-tests`、`mocking` 已覆盖 RED/GREEN/REFACTOR、回归、测试层级和安全运行；另建技能会重复所有权，并把普通逻辑改动、固定金字塔、full suite、浏览器 MCP 和自动 subagent 变成普遍门。[`skills/test-strategy/SKILL.md:L1-L61`；`agent-skills-main/skills/test-driven-development/SKILL.md:L12-L36,L38-L186,L312-L398`] |
| Build | `context-engineering` | `新增/改写引入` | `P1` | 当前没有专门的显式 context audit/setup 所有者；任务级 context pack、聚焦错误片段和选择性 packing 有独立价值。改写版必须默认只读、仅在明确配置意图或可观察退化时触发，并删除自动建 rules、固定 token/行数、普遍 planning/compaction 与静态 host/MCP 清单。[`agent-skills-main/skills/context-engineering/SKILL.md:L80-L178,L192-L290`；`prompts/CLAUDE.fragment.md:L6-L16`] |
| Build | `source-driven-development` | `跳过` | `P0` | 精确当前源、权威/一手来源、版本日期和未验证状态已由 prompt 与 Capability Harness 覆盖。目标的 URL-only、prompt-shaped 模型摘要缓存会把旧摘要伪装成当前精确源；普遍网络获取、逐模式代码引用和冲突即询问也与现有比例/证据合同冲突。[`prompts/CLAUDE.fragment.md:L6-L9`；`plugins/capability-harness/references/evidence-policy.md:L3-L31`；`agent-skills-main/hooks/SDD-CACHE.md:L53-L79,L154-L168`] |
| Build | `doubt-driven-development` | `合并/协调重叠` | `P0` | 去掉作者 CLAIM/推理、仅交 `ARTIFACT + CONTRACT` 的对抗核查，以及 reconcile 分类有窄价值；但每个 non-trivial 决策都 fresh-review、每轮询问跨模型和自建 orchestrator 会与 `agent-workflow`、`review-and-finish` 和最小组合冲突，并缺外部 artifact 数据边界。[`agent-skills-main/skills/doubt-driven-development/SKILL.md:L49-L191,L223-L244`；`skills/agent-workflow/references/fresh-context-verification.md:L1-L41`] |
| Build | `frontend-ui-engineering` | `新增/改写引入` | `P1` | 当前没有独立 UI/a11y 领域所有者；原生语义、键盘/焦点、可访问名称、动态通知、响应式和空/错/加载状态是真缺口。改写版须让普通标签/文案小改留在 base，先读项目栈/设计系统，并把 React/Tailwind/状态库、固定断点/行数和全量工具清单降为项目相关的条件选项。[`agent-skills-main/skills/frontend-ui-engineering/SKILL.md:L116-L293`；`agent-skills-main/references/accessibility-checklist.md:L13-L121`] |
| Build | `api-and-interface-design` | `合并/协调重叠` | `P0` | 公共接口、模块边界和组件 props 已由 `design-codebase` 拥有；不应再建同权自动 Skill。可把消费者可观察契约、机器可读错误、外部响应解析和兼容演进改写成按需 API/interface reference；固定 REST/TypeScript 规范、无条件信任内部数据、GraphQL 空承诺和悬空迁移依赖应删除或条件化。[`skills/design-codebase/SKILL.md:L2-L55`；`agent-skills-main/skills/api-and-interface-design/SKILL.md:L20-L295`] |

##### Plan 详细分析

- **完整性说明：** 已完整读取唯一 Plan 目标、其直接 DoD 依赖、当前 `plan-work` 与三个直接 references，以及足以裁定产物权限、依赖、验收、路由和验证的 prompt/README/三份维护合同。该 slice 未读取目标 Build Skill，未执行命令、Hook、测试或写入。

###### `planning-and-task-breakdown`

- **暂定动作：** `合并/协调重叠`
- **优先级：** `P0`
- **理由：** 不新增第二个 Plan 所有者。只候选吸收逐步骤 `Acceptance` 字段，并在确有协调价值时条件式标出 `Blocked by` / `Can parallelize`；实际 fan-out、写隔离和集成仍归 `agent-workflow`。P0 来自默认持久化、审批门和触发合同的直接冲突，不是采用授权。[`skills/plan-work/SKILL.md:L8-L20,L33-L62`；`tests/routing-contract.md:L20-L35,L48-L58`]

**Target 实际行为**

- 以已有规格/清晰需求后的任务分解为主，同时把任务太大或模糊、需要估算、可并行或顺序不明列为触发；单文件明显改动或规格已有清晰任务时排除。[`agent-skills-main/skills/planning-and-task-breakdown/SKILL.md:L1-L20`]
- 先只读规格和代码、识别模式/依赖/风险/未知；随后画依赖图，先建 foundations，再用完整用户行为做垂直切片。[同文件:L22-L77]
- 每项任务含描述、具体可测验收、验证、依赖、可能文件和估算；按文件数、约两小时、验收条数和标题 `and` 等机械信号继续拆分。[同文件:L79-L141]
- 默认创建 `tasks/plan.md` 与 `tasks/todo.md`，每 2–3 项设检查点并要求人工审阅；最终再套用项目级 DoD。[同文件:L106-L149,L221-L234；`agent-skills-main/references/definition-of-done.md:L3-L59`]
- 标记可并行、必须串行和需先协调共享 API 的工作。[`agent-skills-main/skills/planning-and-task-breakdown/SKILL.md:L195-L201`]

**当前已验证覆盖与重叠**

- `plan-work` 已拥有实现规划、方法比较、任务分解、roadmap、依赖/排序/迁移/兼容性和垂直切片；先读项目事实，再形成目标、约束、最小方案、步骤、风险和未知。[`skills/plan-work/SKILL.md:L8-L36`]
- 当前持久模板已经为每步提供 `Likely files`、`Verification`、`Depends on`，并在总体层列风险和按影响面扩展的验证；只缺独立命名的逐步 `Acceptance` 字段。[`skills/plan-work/references/plan-template.md:L23-L49`]
- 当前垂直切片同样要求窄而完整、可 demo/test/verify 的行为，并反对数据库/API/UI 横向分层和行为证明前的大型基础设施。[`skills/plan-work/references/vertical-slices.md:L3-L34`]
- 当前问题规则只询问会改变实现的问题，比较最少的实质方案；架构/ownership/interface 先交 `design-codebase`，多代理协调交 `agent-workflow`。[`skills/plan-work/references/design-questions.md:L3-L34`；`tests/routing-contract.md:L20-L29,L44-L58`]

**独有或缺失部分**

- [有界可取] 当前模板未把可观察结果独立标成逐步骤 `Acceptance criteria`；目标将 Acceptance 与 Verification 分开，能更清楚地区分“结果”与“证明方式”。[`skills/plan-work/references/plan-template.md:L29-L39`；target:L79-L104]
- [可选但未证明] 显式依赖图和 `Can parallelize` 字段比当前 `Depends on` 更显眼，但没有证据支持所有计划都需要绘图或并行标签。[target:L35-L55,L195-L201]
- [独有但应拒绝] 固定文件数/时长、默认双文件工件、固定检查点和普遍 DoD 是目标特有流程，不是当前能力真空白。[target:L106-L149,L221-L234]

**冲突与维护成本**

- 目标无条件创建 `tasks/*`；当前计划默认留在聊天，只能在用户明确请求文件或点名既有工件时写命名路径。[`skills/plan-work/SKILL.md:L38-L48,L55-L62`；`tests/non-trigger-cases.md:L67-L70`]
- 目标要求人工批准和“明显任务也必须有书面清单”；当前在安全下一步已清楚时直接执行，并明确不默认设置 approval gate。[`skills/plan-work/SKILL.md:L12-L16,L50-L61`；target:L203-L230]
- 仅因大、多文件或可并行触发会抢占 base 与 `agent-workflow`；Architecture Decisions 区又抢占 `design-codebase`。[`tests/trigger-matrix.md:L16-L22`；`tests/routing-contract.md:L26-L29,L44-L58`]
- 原样并列会复制调查、切片、依赖、验证和路由，并要求同步 README、prompt、三份维护合同及多个现有 Skill；只增加模板字段的维护面显著更小。

**关键证据**

| 路径 | 位置 | 支持的结论 |
| --- | --- | --- |
| `agent-skills-main/skills/planning-and-task-breakdown/SKILL.md` | L12-L149,L195-L234 | 目标触发、依赖图、逐任务契约、机械粒度、默认文件、并行和审批/DoD 门。 |
| `agent-skills-main/references/definition-of-done.md` | L3-L59 | Acceptance 与 standing DoD 的区分，以及普遍完成清单。 |
| `skills/plan-work/SKILL.md` | L8-L62 | 当前 Plan 所有权、轻量触发、默认聊天、命名路径和无默认批准门。 |
| `skills/plan-work/references/plan-template.md` | L23-L49 | 当前逐步文件/验证/依赖及风险响应验证；没有独立 Acceptance 字段。 |
| `tests/routing-contract.md` | L20-L35,L44-L58 | Plan、Design、Review 和 Agent Workflow 的现有所有权。 |

**未知项**

- 未运行 Plan 路由或行为 eval；不能证明当前 `observable outcome` 是否已经在实际输出中稳定等价于逐步 acceptance。
- 没有仓库使用数据证明数字化工时/文件数阈值、固定检查点或人工计划批准能改善结果。
- 目标声称下游 `/build` 依赖 `tasks/*`，但本 slice 未执行或验证该命令；这不是当前项目兼容要求。

##### Build 详细分析

- **完整性说明：** 三个 Build slice 合计完整分类 7/7 个目标条目：执行 2 项、上下文/证据 3 项、领域 2 项。每个 worker 只读完整目标 SKILL 及会实质定义行为的直接依赖，并读取指定当前 owner、prompt、README 和维护合同；没有修改、联网、脚本/Hook/测试执行或跨 slice 接管。

###### `incremental-implementation`

- **暂定动作：** `合并/协调重叠`
- **优先级：** `P0`
- **理由：** 不原样新增普遍 Build gate。只保留“明确需要时按最小完整可验证片推进、每片保持工作状态”的原则，以及 contract-first/risk-first 作为可选切片镜头；删除多文件/行数自动触发、自动 commit、固定全套检查、默认 feature flag/迁移回滚和统一 DoD。[`agent-skills-main/skills/incremental-implementation/SKILL.md:L21-L87,L89-L181,L199-L249`]

**Target 行为与当前覆盖**

- 目标对任何多文件、约 100 行以上、任务分解后的实施或重构广泛触发；循环为“最小完整片→测试→验证→commit→下一片”，并提供 vertical、contract-first、risk-first 三种切法。[target:L1-L87]
- 目标要求简单、限域、可构建/测试，并普遍建议 feature flag、安全默认、独立回滚；每片与最终都列 test/build/type/lint/行为/commit/full-suite/clean-tree 门。[target:L89-L181,L199-L249]
- 当前 base 已有简单/限域/按风险验证；`test-strategy` 已有“一项行为 + 证明 + 实现”的垂直片及最快高信号检查；`review-and-finish` 拥有完成声明，`finish-branch` 独占显式 commit。[`prompts/CLAUDE.fragment.md:L6-L17`；`skills/test-strategy/SKILL.md:L34-L43`；`skills/review-and-finish/SKILL.md:L108-L140`；`skills/finish-branch/SKILL.md:L8-L30,L46-L55`]

**独有、冲突与维护成本**

- [有界可取] contract-first/risk-first 与“一片后仍工作”比当前通用垂直切片更具体；feature flag/回滚则依赖真实部署与迁移能力，不能普遍化。
- 自动 commit 和 clean tree 完成条件直接越过动作级 Git 授权；广泛执行项目命令又没有先解析安装、联网、迁移或持久写入等传递副作用。[target:L36-L43,L199-L249；`skills/test-strategy/SKILL.md:L20-L28`]
- 多文件/行数触发会把普通编码和已批准计划执行从 base 升级；固定 DoD 与 `review-and-finish` 的按证据缺口完成判断重复。[`tests/trigger-matrix.md:L12-L28`；`tests/non-trigger-cases.md:L17-L18,L68`]
- 原样加入需同时协调 base、plan、test、review、Git 五个 owner；目标 eval 又把逐片 commit 固化为成功条件，连评测也必须重写。[`agent-skills-main/evals/cases/incremental-implementation.json:L29-L55`]

**关键证据与未知项**

- 主证据：`agent-skills-main/skills/incremental-implementation/SKILL.md:L21-L87,L199-L249`；`skills/test-strategy/SKILL.md:L20-L49`；`skills/finish-branch/SKILL.md:L8-L55`；`tests/trigger-matrix.md:L12-L28,L129-L139`。
- 未运行候选 eval 或 live routing，无法证明目标会实际自动 commit，也无法量化当前 base 自然采用增量片的程度。

###### `test-driven-development`

- **暂定动作：** `跳过`
- **优先级：** `P1`
- **理由：** 跳过整份独立 Skill，不建立第二个 TDD owner。当前 `test-strategy` 及 references 已覆盖核心方法且补有 advisory、命令副作用、现有代码安全和 sibling handoff；仅在未来出现具体重复失败时再考虑把 stack-discovery 清单小幅改写进现有 reference。[`skills/test-strategy/SKILL.md:L1-L61`]

**Target 行为与当前覆盖**

- 目标把几乎所有逻辑、bug 和行为变更纳入 strict TDD，先发现 stack/runner/布局/CI 命令，再执行 RED→最小 GREEN→REFACTOR；另规定固定金字塔、DAMP/AAA/mock 规则、浏览器 DevTools、复杂 bug subagent 和最终 full suite。[`agent-skills-main/skills/test-driven-development/SKILL.md:L12-L36,L38-L186,L188-L361,L387-L398`]
- 当前 `tdd-mode` 已完整覆盖逐行为预期 RED、最小 GREEN、green 后 refactor 和不得为制造 RED 破坏已有代码；`good-tests` 与 `mocking` 已覆盖行为断言、一个逻辑行为、描述性命名、真实失败路径和只在边界 mock。[`skills/test-strategy/references/tdd-mode.md:L1-L28`；`good-tests.md:L1-L24`；`mocking.md:L1-L29`]
- 当前主体还按 claim/成本/风险选择 unit/property/type/benchmark/integration/E2E，要求解析精确命令及副作用，并将 setup/import/discovery 失败与预期 RED 分开。[`skills/test-strategy/SKILL.md:L20-L45`]

**独有、冲突与维护成本**

- Stack discovery 的逐项清单和 DAMP/资源模型是说明性增量，但核心行为已有；Chrome MCP 与自动 subagent 属于领域/编排扩张，不是 TDD 核心缺口。
- “任何逻辑改动自动 strict TDD”、固定 80/15/5、每次 full suite 和所有浏览器改动必须 DevTools 与当前显式 TDD/风险比例触发冲突；命令规则也缺少传递副作用 gate。[target:L12-L34,L144-L186,L312-L341,L387-L398]
- 新增会重复触发词、TDD 循环、层级、mock、fixture、flaky 和完成验证，并带入 JS/TS testing patterns、browser skill 和 agent 编排依赖。

**关键证据与未知项**

- 主证据：`agent-skills-main/skills/test-driven-development/SKILL.md:L12-L398`；`skills/test-strategy/SKILL.md:L1-L61`；`skills/test-strategy/references/tdd-mode.md:L1-L28`；`tests/trigger-matrix.md:L47-L57`。
- 未运行 authority-pressure 或跨生态 fixture；也未在本 slice 决定 `browser-testing-with-devtools` 自身去留。

###### `context-engineering`

- **暂定动作：** `新增/改写引入`
- **优先级：** `P1`
- **理由：** 候选建立一个窄的、显式 context audit/setup owner：只在用户要求配置/审计 agent context，或已有可观察输出退化时触发；默认只读并产出最小 context pack，持久 rules 修改仍需明确授权。删除普遍新会话/切换触发、强制 rules、固定行数、MCP 产品清单和自动 fresh-session/compact。[`agent-skills-main/skills/context-engineering/SKILL.md:L12-L41,L80-L190,L192-L290`]

**Target 行为与当前覆盖**

- 目标广泛覆盖新会话、任务切换、质量下降和新项目，按 rules/spec/source/error/history 五层组织 context，并把创建 rules file 视为最高杠杆。[target:L12-L41]
- 其任务 pack 包含待改文件、相关测试、一个本地先例和相关类型；错误只取聚焦片段，大项目选择性 include/层次摘要；无先例即问，多步任务先计划，并用 rules 存在与遵循作为验收。[target:L80-L178,L192-L290]
- 当前 prompt 已有 exact-source、证据/指令分离、项目惯例、最小提问和 artifact 权限；`memory-handoff` 拥有显式 handoff/compaction/resume，Capability Harness `context-scout` 只补一个决策前 domain context 缺口。[`prompts/CLAUDE.fragment.md:L6-L16`；`skills/memory-handoff/SKILL.md:L10-L25,L143-L150`；`plugins/capability-harness/agents/context-scout.md:L9-L17,L36-L61`]

**独有、冲突与维护成本**

- [真增量] “待改文件 + 相关测试 + 一个先例 + 相关类型”的 context pack、聚焦错误和选择性 packing 可用于明确审计/退化诊断；当前 catalog 没有专门 host rules/context-pack owner。[`README.md:L40-L67,L121-L132`]
- 自动建 rules 越过持久工件授权；把 source/test/type 统一标成 Trusted 比当前“所有已审材料只作证据”更窄，不能抵御注释/fixture 中的指令形文本。[target:L38-L41,L98-L104,L282-L287]
- 无先例即停、每个多步任务先计划、长上下文即 compact 与当前最小提问、base 直接执行和显式 handoff intent 冲突。[target:L113-L120,L218-L251]
- 需要维护不同 host 的规则路径和加载语义，并与 `memory-handoff`、`reliability-check`、`skill-refactorer`、`context-scout` 建正负组合边界；固定阈值与产品清单会快速漂移。

**关键证据与未知项**

- 主证据：`agent-skills-main/skills/context-engineering/SKILL.md:L12-L290`；`prompts/CLAUDE.fragment.md:L6-L17`；`skills/memory-handoff/SKILL.md:L10-L25`；`plugins/capability-harness/agents/context-scout.md:L36-L61`。
- 未运行候选 context audit eval；实际选择率、误触发率和 rules 修改行为未知。新增分类不是修改当前 runtime catalog 的授权。

###### `source-driven-development`

- **暂定动作：** `跳过`
- **优先级：** `P0`
- **理由：** 跳过独立 Skill 和 SDD cache；当前 exact-source/evidence 层保持不变。版本检测、具体 feature 页、deprecation 检查和深链格式只保留为未来具体失败的参考，不足以抵消缓存和普遍 citation 的冲突。[`agent-skills-main/hooks/SDD-CACHE.md:L53-L79,L154-L168`]

**Target 行为与当前覆盖**

- 目标对任何准备凭记忆写框架代码、要求 verified/current、框架推荐实现或框架 review 广泛触发；先从 manifest 检测版本，再取具体官方页面/deprecation/migration，按文档实现并把未覆盖内容标为 unverified。[`agent-skills-main/skills/source-driven-development/SKILL.md:L12-L120`]
- 它要求每个 framework-specific pattern 引用完整深链，示例甚至把 URL 写入代码注释；可选 cache 以 URL 为唯一 key 保存旧 prompt 下经模型处理的摘要，并在 304 时复用。[同文件:L122-L160；`agent-skills-main/hooks/SDD-CACHE.md:L53-L79`]
- 当前 prompt 已强制 exact current source、项目事实/运行证据优先和外部技术主张用当前权威/一手源；Capability Harness 已有证据优先级、版本/日期、focused researcher 和未验证返回合同。[`prompts/CLAUDE.fragment.md:L6-L9`；`plugins/capability-harness/references/evidence-policy.md:L3-L31`；`plugins/capability-harness/agents/evidence-researcher.md:L9-L64`]

**独有、冲突与维护成本**

- [有限增量] 版本→功能页→弃用/迁移的顺序与精确 deep link 是有用格式提示，但不需要第二运行 workflow。
- 目标允许用户以速度为由关闭 source verification，版本或 docs/project 冲突又一律询问；前者弱化不可省的 exact-source 边界，后者比“仅问材料缺口”更阻塞。[target:L12-L25,L61,L95-L120]
- 逐模式引用和代码注释会制造风格噪声；目标 source hierarchy 还同时接受 official blog/changelog，却在最终清单排除 blog，内部不一致。[target:L67-L81,L122-L160,L183-L194]
- URL-only cache 的 304 只证明资源未变，不能证明旧 prompt 的摘要回答新问题；把 prior model summary 当刚读取的 exact source 与当前硬规则直接冲突。它还引入 Bash/jq/curl/hash、持久缓存和删除 entry 等未授权副作用。

**关键证据与未知项**

- 主证据：`agent-skills-main/skills/source-driven-development/SKILL.md:L12-L194`；`agent-skills-main/hooks/SDD-CACHE.md:L11-L79,L154-L168`；`plugins/capability-harness/references/evidence-policy.md:L3-L31`。
- 未执行 cache 或行为 eval；HEAD/304、prompt mismatch、freshness 与 citation 质量均未运行验证。

###### `doubt-driven-development`

- **暂定动作：** `合并/协调重叠`
- **优先级：** `P0`
- **理由：** 不新增独立通用 doubt cycle。只把去锚定 `ARTIFACT + CONTRACT`、adversarial mismatch framing 和有界 reconcile 合并进现有 fresh-context/controller reference；一个 verifier 保持 direct，多问题才由 `agent-workflow` 协调，完成态 red-team 仍归 `review-and-finish`。[`skills/agent-workflow/references/fresh-context-verification.md:L1-L41`]

**Target 行为与当前覆盖**

- 目标把 branching、跨模块/服务、非类型可证属性、隐含上下文或不可逆影响定义为 non-trivial；五步为 CLAIM→最小 artifact+contract→不带 CLAIM/作者推理的 fresh adversarial DOUBT→controller RECONCILE→最多三轮停止。[`agent-skills-main/skills/doubt-driven-development/SKILL.md:L14-L110,L168-L191`]
- 每轮单模型 review 后都必须给用户 Gemini/Codex/manual/skip 选择；外部 CLI 走 stdin/read-only sandbox；最终要求每个 non-trivial artifact 至少一次 fresh review。[同文件:L112-L166,L223-L244]
- 当前 `agent-workflow` 已区分一个 focused verifier 与需协调的多 verifier；fresh-context reference 已规定只给 spec/artifact/scope，省略 controller 推理并找 mismatch；skeptical evaluator 已按 actual artifact/constraints/evidence 分类 defect/risk/unverified。[`skills/agent-workflow/SKILL.md:L20-L48,L79-L145`；`fresh-context-verification.md:L13-L41`；`plugins/capability-harness/agents/skeptical-evaluator.md:L9-L52`]

**独有、冲突与维护成本**

- [可取增量] 明确不给 reviewer 作者 CLAIM、用 `ARTIFACT + CONTRACT` 去锚定，以及 reconcile 为 contract misread / valid actionable / valid trade-off / noise，比当前参考更具体。
- 每个 non-trivial 决策都额外 agent、每轮跨模型询问，与按风险升级和“不把每个小步骤变成 implementer+verifier”冲突；自建 orchestrator 又抢占 `agent-workflow`。[target:L42-L47,L112-L191,L231-L240]
- “与 /review 两者都用”重复最小组合；把 TDD RED 称作 fresh-context review 混淆反证与独立性；外部 CLI 只处理调用授权，没有先分类私有源码、秘密或出域限制。[target:L126-L165,L223-L244]
- 原样采用需维护 persona precedence、多家 CLI/auth/sandbox、临时文件、最多三轮失败路径，以及与 review/test/harness 的多重路由，成本显著。

**关键证据与未知项**

- 主证据：`agent-skills-main/skills/doubt-driven-development/SKILL.md:L14-L244`；`skills/agent-workflow/references/fresh-context-verification.md:L1-L41`；`tests/routing-contract.md:L37-L60`。
- 未执行 fresh agent 或 Gemini/Codex；persona precedence、read-only sandbox 和降级 self-questioning 均未验证。当前也没有建立 cross-model 功能的用户授权。

###### `frontend-ui-engineering`

- **暂定动作：** `新增/改写引入`
- **优先级：** `P1`
- **理由：** 当前确有 UI/a11y 领域缺口；改写版只在非平凡 UI 构建/交互、明确 accessibility/responsive/design-system 要求或现有模式不足时触发。普通标签/文案/已有模式小改留在 base，架构压力交 `design-codebase`，非显然验收接缝交 `test-strategy`。[`tests/trigger-matrix.md:L12-L16,L27,L34`]

**Target 行为与当前覆盖**

- 目标覆盖新建或修改页面/组件/布局/交互/状态，规定组件共置、composition、数据/展示分离和 local→global 状态阶梯；要求遵循实际设计系统并避免模板化 AI aesthetic。[`agent-skills-main/skills/frontend-ui-engineering/SKILL.md:L12-L164`]
- 目标把 WCAG 2.1 AA、键盘/ARIA/焦点、空错加载、移动优先和乐观更新列为生产基线，最终要求控制台、键盘、屏幕阅读器、四宽度、状态、设计系统和 axe 全套检查。[同文件:L165-L328]
- 当前通用层和 `design-codebase`/`test-strategy` 只覆盖项目约定、组件边界和风险验证；当前 runtime catalog 中没有独立 UI/a11y owner。[`prompts/CLAUDE.fragment.md:L6-L17`；`skills/design-codebase/SKILL.md:L10-L55`；`README.md:L42-L67`]

**独有、冲突与维护成本**

- [真增量] 原生语义、键盘/焦点、可访问名称、动态通知、颜色非唯一线索、缩放、表单错误关联、触控目标、响应式及空/错/加载状态。[`agent-skills-main/references/accessibility-checklist.md:L13-L121`]
- 目标触发会吞掉简单 UI 编辑；TSX/Tailwind、React Query/SWR、Zustand/Redux、三层 prop drilling、200 行组件和四断点不能凌驾于项目栈。其“Trap focus”示例也未展示完整焦点循环和关闭后恢复。[target:L20-L115,L203-L256,L309-L328]
- `npx axe-core` / `pa11y` 可能安装或联网，必须先经命令副作用边界；全量人工/工具清单应改成按触及行为选择的 acceptance menu。[`accessibility-checklist.md:L123-L138`；`skills/test-strategy/SKILL.md:L22-L43`]
- 需维护框架中立正文、可访问性参考的新鲜度、与 design/test 的交接，以及“小标签/文案不触发”的正负路由。

**关键证据与未知项**

- 主证据：`agent-skills-main/skills/frontend-ui-engineering/SKILL.md:L12-L328`；`agent-skills-main/references/accessibility-checklist.md:L13-L160`；`skills/design-codebase/SKILL.md:L10-L55`。
- 未运行 UI eval、浏览器、屏幕阅读器或工具；未外部核验 WCAG/工具/`dialog` 当前行为，具体项目栈也未知。

###### `api-and-interface-design`

- **暂定动作：** `合并/协调重叠`
- **优先级：** `P0`
- **理由：** 不新增同权自动 Skill。把消费者可观察行为、统一机器可读错误、外部响应解析、输入/输出分离和兼容演进改写为 `design-codebase` 的按需 API/interface reference；固定协议/语言规则和不可用 sibling 引用不保留。[`skills/design-codebase/SKILL.md:L2-L55`]

**Target 行为与当前覆盖**

- 目标对 REST/GraphQL、模块边界、组件 props、数据库影响的 API 形状和任何公共接口变化广泛触发；把全部可观察行为视为潜在契约，主张 contract-first、单版本和加法式兼容演进。[`agent-skills-main/skills/api-and-interface-design/SKILL.md:L2-L59,L125-L145`]
- 它规定统一 REST 错误体/状态、外部边界验证但信任内部代码/自有数据库，并给出 REST 资源/分页/PATCH 与 TypeScript union/input-output/branded ID 模式及固定最终清单。[同文件:L61-L295]
- 当前 `design-codebase` 已定义完整调用者接口、所有权/依赖/接缝和项目证据优先；`deep-modules`、`deepening`、`design-it-twice` 已覆盖小接口、外部 adapter、多调用方迁移和兼容方案，`test-strategy` 拥有契约证明。[`skills/design-codebase/SKILL.md:L21-L55`；`references/deep-modules.md:L5-L39`；`references/deepening.md:L5-L28`]

**独有、冲突与维护成本**

- [有限增量] API 协议层的消费者可观察风险、机器可读错误、第三方响应不可信、输入/输出模型分离和兼容演进提示，可作为渐进披露 reference。
- 模块/公共接口/props 与 `design-codebase` 直接双重所有；小端点参数本应留 base。“Trust internal code/database”无视真实信任边界和持久化不变量。[target:L12-L19,L88-L124；`tests/trigger-matrix.md:L12-L17,L89-L98`]
- “一次一个版本”与其直接依赖的迁移 material 要求旧新并行/adapter/flag/expand-contract 缺少稳态/迁移态区分；固定 REST 状态、命名、分页、PATCH 和 branded IDs 也必须服从项目事实。[target:L33-L35,L61-L260；`agent-skills-main/skills/deprecation-and-migration/SKILL.md:L120-L190`]
- 描述声称 GraphQL，但全文只在 description/overview 出现；又引用当前不存在的 `deprecation-and-migration`，单独迁移会留下悬空交接。维持跨 REST/GraphQL/语言/迁移的一套顶层规范成本高。

**关键证据与未知项**

- 主证据：`agent-skills-main/skills/api-and-interface-design/SKILL.md:L2-L295`；`skills/design-codebase/SKILL.md:L2-L76`；`skills/design-codebase/references/deep-modules.md:L5-L39`；`tests/routing-contract.md:L20-L31,L37-L61`。
- 未读取具体产品 API/消费者或运行契约，不能判断候选默认值适合任何项目；未运行 routing eval，P0 来自静态所有权重叠。

##### Plan + Build 对阶段 3“整体流程强度”决策的证据

**支持增加有条件验证门的证据**

- [Plan] 把每步 `Acceptance` 与 `Verification` 分开，可让“期望结果”和“证明方式”可追溯，并与当前 prompt 已有 acceptance-criteria 验证语义一致；这支持模板字段增强，不支持固定审批。[`skills/plan-work/references/plan-template.md:L29-L49`；`prompts/CLAUDE.fragment.md:L17`]
- [Build execution] contract-first/risk-first 和“一片后仍可工作”能降低大改的未证实跨度；但应由真实依赖/风险或显式请求触发。[`agent-skills-main/skills/incremental-implementation/SKILL.md:L44-L87`]
- [Context] 当已观察到 context 退化或用户明确审计时，最小 context pack、聚焦错误和选择性 packing 提供可检查的输入完整性信号。[`agent-skills-main/skills/context-engineering/SKILL.md:L80-L178`]
- [Source] 对版本敏感外部 API，先确认版本、具体 feature page 和 deprecation/migration，再标出未验证缺口，有助于避免过期模式；当前 evidence policy 已支持这种选择性升级。[`source-driven-development/SKILL.md:L27-L120`；`plugins/capability-harness/references/evidence-policy.md:L3-L31`]
- [Doubt] 对高影响且确定性检查不足的假设，去掉作者结论/推理的 `ARTIFACT + CONTRACT` 对抗核查能降低 anchoring；当前 fresh-context 参考也允许按里程碑风险升级。[`doubt-driven-development/SKILL.md:L62-L110`；`fresh-context-verification.md:L13-L41`]
- [Domain] UI 的键盘/焦点/可访问名称/动态状态和 API 的消费者错误/顺序/契约都属于可观察风险；变更确实触及时，加入领域 acceptance 与契约级证据有明确基础。[`accessibility-checklist.md:L13-L53`；`api-and-interface-design/SKILL.md:L20-L31,L61-L118`]

**反对增加通用验证门的证据**

- 当前套件明确“Start lightweight”，普通编码和已批准计划执行留在 base；大、多文件、任何逻辑改动或任何接口/UI 修改本身都不足以自动升级正式 workflow。[`README.md:L19-L23`；`tests/trigger-matrix.md:L12-L28`]
- 目标多项把默认落盘、人工批准、逐片 commit、full suite、固定 DoD 或每个 non-trivial artifact 的 reviewer 设为常设门；它们重复 Plan/Test/Review/Git owner，并越过动作级授权。[`planning-and-task-breakdown/SKILL.md:L106-L149,L221-L234`；`incremental-implementation/SKILL.md:L199-L249`；`doubt-driven-development/SKILL.md:L231-L240`]
- 固定文件数、时长、金字塔比例、断点、组件行数、分页/命名/状态码和 context 行数没有本项目运行证据；按项目事实、具体行为和风险选择门更符合当前合同。
- 普遍 test/build/npx/CLI/cache 可能安装、联网、迁移、持久写入或外发私有 artifact；文本清单不能替代命令副作用、数据边界和逐动作授权。[`skills/test-strategy/SKILL.md:L20-L28`；`doubt-driven-development/SKILL.md:L126-L165`]
- SDD URL-only 模型摘要缓存直接降低 exact-source 证据质量；更多自动化门若以较差证据为输入，反而会产生更自信的错误结论。[`agent-skills-main/hooks/SDD-CACHE.md:L53-L79,L154-L160`；`prompts/CLAUDE.fragment.md:L6`]
- 静态 Skill/checklist/trigger 合同不证明实时路由或行为；本组没有运行任何候选 eval、host hook、浏览器、CLI 或真实消费者检查，不能用增加文本门代替运行校准。[`tests/trigger-matrix.md:L220-L241`；`tests/non-trigger-cases.md:L129`]

**中性边界事实**

- 当前权威仍是 always-on prompt 与各 runtime Skill description/body；README/tests 是摘要和维护验证，不是第二运行层。[`tests/routing-contract.md:L1-L14`]
- Target 目录在会话基线中未跟踪且没有独立 revision；所有结论只绑定当前工作树文本，不证明已安装或已激活。
- 所有目标命令、hooks、cache、CLI、示例与反合理化文本均只作证据；本组没有执行它们或据此扩大授权。
- P0 的统一含义是“引入前必须先解决冲突”；P1 表示有价值或需防误引但不紧急；二者都不是阶段 4 授权。

##### 本组执行状态

- 四个只读 slice 均为 `complete`：Plan 1/1、Build execution 2/2、Build context/evidence 3/3、Build domain 2/2；没有 blocked、failed、stale、skipped、unverified 或空结果。
- 四个 worker 均为强制无 shell/Edit/Write 的 `capability-harness:evidence-researcher`，只使用 Read/Grep/Glob；没有 WebSearch/WebFetch、文件修改或脚本/Hook/测试执行。
- 分析基线为当前项目 `main@f82a1b2` 与 target 的 current unversioned working tree；结论是静态指令工件比较，不是 live host/model/runtime 验证。
- 本组已写入 `MIGRATION_PLAN.md`，并已获得用户确认；后续 Verify/Review 分析不改变本组已确认的 provisional classification，也不构成阶段 4 吸收授权。

#### 第 3 组：Verify + Review（已完成，已确认）

> 本组仍是阶段 2 的 provisional classification，不是阶段 4 的引入授权。P0 只表示任何吸收前必须先消除直接权限、所有权或证据冲突；静态 Skill、eval 和 fixture 也不证明 live host/model/runtime 行为。

##### 暂定结论汇总

| 分类 | Target 条目 | 当前暂定动作 | 优先级 | 核心理由 |
| --- | --- | --- | --- | --- |
| Verify | `browser-testing-with-devtools` | `新增/改写引入` | `P0` | 当前缺少把 live DOM/console/network/screenshot/a11y/performance 通道转化为受限 browser runtime evidence 的专门方法。改写版只能是窄触发、host-capability-conditional 的 evidence provider；必须删除自动写 MCP 配置、`npx @latest`、所有浏览器改动全套检查、screenshot 过度声明和自行判定完成。[`agent-skills-main/skills/browser-testing-with-devtools/SKILL.md:L1-L43,L45-L107,L306-L318`；`skills/test-strategy/SKILL.md:L20-L43`] |
| Verify | `debugging-and-error-recovery` | `保留现状不动` | `P0` | 当前 `debug-systematically` 已覆盖核心根因方法，并额外拥有窄触发、hypothesis 状态、预算/停止条件、动作授权、正确 regression seam 和诚实完成声明。目标的不可复现 taxonomy 与 `git bisect` recipe 不足以证明新增价值，反而带来普通错误宽触发、不可跳步、未授权 Git/install/load/CI 动作和普遍 full-suite gate。[`skills/debug-systematically/SKILL.md:L1-L100`；`agent-skills-main/skills/debugging-and-error-recovery/SKILL.md:L1-L300`] |
| Review | `code-review-and-quality` | `合并/协调重叠` | `P0` | 不新增第二个自动 Review owner，也不重定义宿主 `/code-review`。仅候选把 tests-first 阅读顺序和少量结构 remedy 菜单合并进现有 review reference；删除 every-change/no-exception、普遍多模型 review、自动 orphan cleanup 和 Ready-to-merge 动作暗示。[`skills/review-and-finish/SKILL.md:L10-L59,L102-L140`；`agent-skills-main/skills/code-review-and-quality/SKILL.md:L1-L20,L88-L101,L140-L239`] |
| Review | `code-simplification` | `跳过` | `P0` | 当前普通局部简化属于 base，明确主机 `simplify` 推荐保持 user-invocable-only，review finding 的实施需退出 Review 后另获修改授权。候选的行为不变量有参考价值，但不足以证明新 owner；逐改全测、自动 commit、拆 PR 和 500 行自动化规则直接冲突。[`prompts/CLAUDE.fragment.md:L6-L17`；`README.md:L90-L107`；`agent-skills-main/skills/code-simplification/SKILL.md:L30-L185,L319-L332`] |
| Review | `security-and-hardening` | `新增/改写引入` | `P0` | 当前 generic review 没有 trust-boundary→asset→STRIDE→abuse-case→control 的安全域方法，也缺 SSRF、供应链和产品 LLM threat model。改写版须仅由明确安全意图或非平凡 trust boundary 触发，并删除 blanket approval、自动 audit/提交前命令、密钥轮换/历史清理及 `/ship` fan-out。[`agent-skills-main/skills/security-and-hardening/SKILL.md:L12-L74,L189-L220,L272-L310,L356-L382`；`skills/review-and-finish/SKILL.md:L10-L59`] |
| Review | `performance-optimization` | `合并/协调重叠` | `P1` | measure→identify→fix→同条件 remeasure、方差判断、correctness-first、无收益回退和 metric-honesty 是真实缺口；但未知慢路径仍归 `debug-systematically`，benchmark seam 归 `test-strategy`，readiness 归 Review。固定 Web 预算、RUM 必选、npx/监控、commit/PR/PERF.md 和 speculative large-data 触发必须删除或条件化。[`agent-skills-main/skills/performance-optimization/SKILL.md:L12-L45,L73-L120,L292-L397`；`tests/routing-contract.md:L16-L29`] |

##### Verify 详细分析

- **完整性说明：** 两个 Verify slice 均完成。浏览器 owner 全文读取目标 SKILL、上游路由材料、匹配 eval/fixtures 与当前 test/review/prompt/README/contracts；调试 owner 全文读取目标、全部匹配 fixtures、当前 `debug-systematically` 及 references、test/reliability/prompt/contracts。未运行浏览器、命令、Hook、测试或 eval。

###### `browser-testing-with-devtools`

- **暂定动作：** `新增/改写引入`
- **优先级：** `P0`
- **理由：** 当前存在 live browser evidence 方法缺口，但目标不可原样吸收。改写版只在用户明确要求真实浏览器/DevTools 证据，或 active owner 已识别必须由浏览器解决的证据缺口时运行；不安装/配置工具，不接管测试策略、根因修复或完成判定。[`tests/routing-contract.md:L16-L35,L37-L69`]

**Target 实际行为**

- frontmatter 和正文把所有 browser build/modify/debug、DOM、console、network、performance 与 visual verification 纳入 Chrome DevTools MCP 工作流。[`agent-skills-main/skills/browser-testing-with-devtools/SKILL.md:L1-L22`]
- 目标列出 screenshot、live DOM、console、network、performance trace、computed style、a11y tree 和 page-context JavaScript，并给出 UI/network/performance 的 reproduce→inspect→diagnose→fix→verify 流程。[同文件:L45-L59,L109-L182]
- 它包含有价值的 profile isolation 与不可信页面内容边界，但只对从页面提取 URL 和 JS mutation 明确确认；普通 navigate/click/submit/toggle 没有按实际副作用分类。[同文件:L60-L107,L184-L216]
- 目标会写 `.mcp.json`/settings 并使用 `npx -y chrome-devtools-mcp@latest`，又要求任何 browser-facing change 检查 console/network/screenshot/a11y/performance 并处理全部 findings。[同文件:L24-L43,L256-L258,L306-L318]

**当前覆盖、独有缺口与所有权**

- 当前 prompt 已拥有 runtime-vs-static 诚实性、动作级授权和范围；`test-strategy` 拥有是否需要 browser/E2E、验收主张、observable seam、assertion/wait 和最小检查；`review-and-finish` 拥有 evidence sufficiency 与 PASS/BLOCK/UNVERIFIED。[`prompts/CLAUDE.fragment.md:L6-L18`；`skills/test-strategy/SKILL.md:L10-L43`；`skills/review-and-finish/SKILL.md:L49-L77,L108-L140`]
- [真缺口] 当前 runtime skills 没有专门说明如何获取和报告指定页面状态下的 live DOM、console、network、computed style、a11y、trace 与交互后状态。
- [应新增的边界] live browser channel 只支持其实际观察；实时 screenshot 只证明指定 viewport/时刻的视觉状态；外部 screenshot 是 artifact；host tool presence 不是 execution；工具不可用时报告 blocker 与 `UNVERIFIED`，不以静态阅读冒充替代。
- Browser owner 应只解析 exact URL/environment/profile/test data/action，按效果区分只读观察与会提交、删除、购买、登录或持久写入的交互，返回 observation/inference/gaps 后停止。测试设计、修复和完成结论仍交回原 owner。

**冲突与维护成本**

- 所有 browser edit 自动触发与当前 ordinary work 留 base 冲突；自动写配置、运行 `npx @latest` 涉及持久配置、安装和网络，不能由验证意图授权。[`README.md:L19-L38`；`skills/test-strategy/SKILL.md:L20-L28`]
- Native click、form submit、JS click 和 navigation 必须按外部/持久效果判断权限；目标只限制 JS mutation，留下 P0 动作边界缺口。
- Zero-warning/all-findings 和所有通道全量检查会把既有、无关问题变成阻断项；简单 before/after screenshot 也不是无 oracle 的 visual regression proof。[target:L218-L228,L256-L258,L306-L318]
- Provider 工具名、配置和 profile 行为会漂移；真实 eval 还需可复现浏览器、MCP allowlist、server 生命周期、端口/profile cleanup 和环境记录，维护成本显著高于静态 case。

**关键证据与未知项**

| 路径 | 位置 | 支持的结论 |
| --- | --- | --- |
| `agent-skills-main/skills/browser-testing-with-devtools/SKILL.md` | L1-L43,L45-L107,L109-L228,L256-L318 | 广触发、MCP 安装、evidence channels、安全边界、动作与 blanket completion gate。 |
| `skills/test-strategy/SKILL.md` | L10-L43 | 当前 test owner、命令副作用、tool-unavailable fallback 和 evidence-to-cost。 |
| `skills/review-and-finish/SKILL.md` | L49-L77,L108-L140 | 当前完成证据、危险检查与停止条件。 |
| `agent-skills-main/evals/cases/browser-testing-with-devtools.json` | L1-L44 | 仅显式 runtime/DevTools 正例和需真实 observation 的 behavior 期望。 |
| `agent-skills-main/scripts/run-evals.js` | L45-L50,L446-L528 | Tier-3 allowlist 未列 Chrome DevTools MCP，静态 eval 定义不证明实际 browser execution。 |

- 未验证 host 是否配置/允许 Chrome DevTools MCP；仓库无 `.mcp.json` 不能外推用户级配置。
- 未运行 eval/browser；fixture 可形成 network/JSON parse 故障假设，但 console/network/DOM 均未实际观察。
- Chrome/profile/CWV/contrast 等外部实现细节未联网核验；只作为目标文本主张。

###### `debugging-and-error-recovery`

- **暂定动作：** `保留现状不动`
- **优先级：** `P0`
- **理由：** 保留当前 `debug-systematically`，不新增第二个 project-debug owner。只有未来出现已证实的 regression bisection 或 non-repro 维护失败，才单独评估一个经权限收紧的 reference 小节。[`skills/debug-systematically/SKILL.md:L1-L100`]

**Target 行为与当前覆盖**

- 目标对 tests fail、build break、runtime mismatch、bug report、日志/console error 和任何 unexpected error 广泛触发，要求按 Reproduce→Localize→Reduce→Fix Root Cause→Guard→Verify 顺序且不跳步。[`agent-skills-main/skills/debugging-and-error-recovery/SKILL.md:L1-L39`]
- 对不可复现问题按 timing/environment/state/random 分类，建议 delay、load/concurrency、CI、隔离/顺序运行、alert 和 `git bisect`；完成普遍要求 regression、focused/full tests、build 和原场景 E2E。[同文件:L40-L170,L291-L300]
- “Error Recovery” 还加入配置默认、UI fallback 与永久 instrumentation，属于产品恢复/运维语义而非纯根因调查。[同文件:L214-L260]
- 当前 owner 已覆盖 observable signal、最小化、diff/working path、hypothesis、单变量 probe、根因修复和重跑原 signal；并额外拥有 active/ruled-out/confirmed/unverified 状态、数值 budget、一次恢复后停止、敏感工件边界和未重跑不得报 fixed。[`skills/debug-systematically/SKILL.md:L30-L94`]
- 当前 references 已覆盖深栈坏值回溯和按实际 bug 选择防线；`test-strategy` 拥有 regression seam/fixture/timing，宿主 `/debug` 拥有 Claude Code runtime，`reliability-check` 只处理显式证据挑战。[`skills/debug-systematically/references/root-cause-tracing.md:L1-L24`；`defense-in-depth.md:L1-L22`；`tests/routing-contract.md:L16-L29,L43-L50`]

**有限独有、冲突与维护成本**

- [有限独有] 更长的 non-repro taxonomy、可复制 `git bisect run` 和 stop/resume 口号；没有 incident/runtime 证据证明当前反复缺失它们。
- 目标把明显编译/单行错误也升级，且不可跳步；当前只对根因不清、flaky、跨组件、回归或反复失败升级，明显 direct failure 留 base。
- Load/CI/alert、Git checkout、`npm install` 均有共享环境、Git、网络或持久副作用；目标只防错误文本中的命令，不约束自身 recipe，低于当前权限合同。[`skills/debug-systematically/SKILL.md:L20-L28`]
- 普遍回归/full-suite/build/E2E 忽略正确 seam 和比例；默认值/空字符串/通用 fallback 还可能掩盖无效配置，不能由 debugging owner 普遍决定。
- 原样引入会同时复制 root-cause、test design、recovery、instrumentation 与 route summaries；target README 自称“五步”而正文有六个编号步骤，已存在摘要漂移。

**关键证据与未知项**

- 主证据：`agent-skills-main/skills/debugging-and-error-recovery/SKILL.md:L1-L300`；`skills/debug-systematically/SKILL.md:L1-L100`；`tests/trigger-matrix.md:L42-L57,L128`；`tests/non-trigger-cases.md:L45-L50,L64`。
- 未运行 target behavior eval；当前工作树也没有可审计 results。没有本地 incident 证明 bisection/non-repro taxonomy 的净收益。

##### Review 详细分析

- **完整性说明：** 两个 Review slice 合计完整分类 4/4 项。host-boundary owner 全文读取 `code-review-and-quality`、`code-simplification`、直接 persona/commands、匹配 eval 与当前 Review/prompt/README/contracts；domain owner 全文读取 security/performance、直接 checklists/personas/commands、匹配 eval/fixtures 和当前 design/test/review/prompt/contracts。未使用网络或执行任何目标命令。

###### `code-review-and-quality`

- **暂定动作：** `合并/协调重叠`
- **优先级：** `P0`
- **理由：** 不引入第二个自动 Review owner、自定义 `/review` 路径或对宿主 `/code-review` 的替代。只在阶段 4 获批时评估把 tests-first 阅读顺序和少量结构 remedy 菜单压缩进现有 `review-template.md`。[`skills/review-and-finish/references/review-template.md:L1-L40`]

**Target 行为与当前覆盖**

- 目标宣称每个 change、feature、bug fix 和 refactor 都必须在 merge 前做 correctness/readability/architecture 等多轴 review；先看上下文、测试、实现，输出 severity、file:line、修复和 Approve/Request Changes。[`agent-skills-main/skills/code-review-and-quality/SKILL.md:L1-L20,L140-L203`]
- 它还给出 dispatcher/重复分支/业务与 orchestration 分离/canonical helper 等结构 remedy、行数规模启发式、change description、dead-code cleanup、多模型 review 与 Ready-to-merge 结论；persona 与自定义 `/review` 再重复同一框架。[同文件:L88-L138,L205-L239,L302-L348,L385-L397；`agent-skills-main/agents/code-reviewer.md:L47-L98`]
- 当前 `review-and-finish` 已拥有自然语言 review、反馈评估、done/fixed/readiness、findings-first、failure-path-first、severity/file:line、证据复用和 Claim/Evidence/Gaps/Verdict；修复需退出 Review 回 base。[`skills/review-and-finish/SKILL.md:L10-L59,L102-L140`]
- 当前 template 已覆盖最窄 scope、需求/代码、Bug/回归/test gap、区分既有债务、按根因合并 findings 和影响驱动严重度；精确 `/code-review` 保持 host-owned，branch actions 另归 `finish-branch`。[`review-template.md:L1-L40`；`README.md:L90-L107`；`tests/routing-contract.md:L16-L25,L37-L54`]

**独有、冲突、所有权与成本**

- [有限可取] 固定 tests-first 阅读顺序和结构 remedy 菜单；当前没有运行证据证明应成为强门，只适合作为现有 reference 的短补充。
- Every-change/no-exception 与普通低风险编辑不自动 review 冲突；宽描述会在自然语言 owner 和 host `/code-review` 之外新增第三条 review path。
- Ready to merge 只能是判断，不能授权 commit/push/merge/PR；普遍多模型和 orphan cleanup 会越过“一个具体盲点才委派”与邻近 cleanup 范围。[`prompts/CLAUDE.fragment.md:L9,L14-L16`]
- 目标正文、persona、command 使用三套 severity 词汇且内容重复；引入后还需维护 host non-trigger、branch split、验证复用与 scope 回归。
- 主机 `/code-review` 内部清单不可见，因此只验证所有权，不声称逐项语义等价。

**关键证据**

- `agent-skills-main/skills/code-review-and-quality/SKILL.md:L1-L20,L88-L239,L302-L397`
- `skills/review-and-finish/SKILL.md:L10-L59,L102-L140`
- `skills/review-and-finish/references/review-template.md:L1-L40`
- `README.md:L25-L38,L90-L107`
- `agent-skills-main/evals/cases/code-review-and-quality.json:L1-L45`（只有声明；无匹配 fixture/运行结果）

###### `code-simplification`

- **暂定动作：** `跳过`
- **优先级：** `P0`
- **理由：** 不新增 332 行自动 Skill 或自定义 `/code-simplify`。当前 base 已承担请求范围内的最小局部简化，主机 `simplify` 推荐保持 user-invocable-only；未有失败证据证明需要新 owner。若未来出现真实简化回归，再抽取最小不变量清单。[`prompts/CLAUDE.fragment.md:L6-L17`；`README.md:L90-L107`]

**Target 行为与当前覆盖**

- 目标在 working-but-complex、feature/review/merge 后触发行为保持重构；要求精确保留输入、输出、副作用、错误与顺序，先读 conventions、caller/callee、tests/history，再处理 nesting、long function、flags、重复、dead code/wrapper。[`agent-skills-main/skills/code-simplification/SKILL.md:L1-L156`]
- 它每次做一个 simplification、每次跑测试，tests pass 后可 commit，并要求 refactor 与 feature/bug 分 commit/PR；超过 500 行倾向 codemod/sed/AST，最终全 tests/build/lint/clean diff。[同文件:L157-L185,L319-L332]
- 当前 prompt 已要求 conventions/contracts、最轻范围、禁止未请求 cleanup/restructure、分析与修改分离、Git 动作单独授权；review 中 complexity finding 只报告，用户授权实施后退出 Review 回 base。[`prompts/CLAUDE.fragment.md:L6-L17`；`skills/review-and-finish/SKILL.md:L102-L116`]

**独有、冲突、所有权与成本**

- [有限独有] exact-behavior 不变量、Chesterton/caller/test/history 清单、over-simplification traps 与 before/after 更难读则 revert；但宿主 `/simplify` 正文不可见，无法证明这些是实际宿主缺口。
- Feature/review/merge 后自动触发与 user-invocable-only 和禁止未请求 cleanup 冲突；tests pass→commit、拆 PR 直接侵入 `finish-branch` 权限。
- 逐改全套测试与 500 行自动化不是项目/风险驱动；自定义 command 还会在 simplification 后再启动目标 code review，重复 base→按需 Review composition。
- 维护新 Skill 需持续协调 host simplify、base、Review repair handoff、test safety 和 branch actions；候选 eval 只覆盖明确 simplify 请求，没有自动触发/授权近邻案例，也无 fixture/运行结果。

**关键证据与未知项**

- `agent-skills-main/skills/code-simplification/SKILL.md:L1-L185,L319-L332`
- `agent-skills-main/.claude/commands/code-simplify.md:L1-L22`
- `prompts/CLAUDE.fragment.md:L6-L17`
- `skills/review-and-finish/SKILL.md:L12-L21,L102-L116`
- `agent-skills-main/evals/cases/code-simplification.json:L1-L44`
- 主机 `/simplify` 语义及候选外链 Simplifier agent 因本地不可见/禁止网络而未验证。

###### `security-and-hardening`

- **暂定动作：** `新增/改写引入`
- **优先级：** `P0`
- **理由：** 当前确有安全域方法空白；新增应限定为 threat model、可利用路径、abuse-case/invariant、控制与专项 finding，不复制 persona、`/ship` 或第二套完成 verdict。[`README.md:L40-L67,L121-L132`]

**Target 行为与当前覆盖**

- 目标对任何用户输入、auth、敏感数据、外部 API、upload/webhook/payment/PII 广泛触发；先映射 trust boundary/assets，对每个边界做 STRIDE，并把 abuse case 作为首个测试，再应用 Always/Ask/Never。[`agent-skills-main/skills/security-and-hardening/SKILL.md:L12-L74`]
- 它展开 injection、auth/session、XSS、access control、headers/CORS、SSRF、upload、dependency/supply-chain、rate-limit、secrets 与 LLM hardening；security-auditor/persona 与 `/ship` 又增加 severity/PoC/并行审计。[同文件:L75-L382；`agent-skills-main/agents/security-auditor.md:L10-L112`]
- 当前 prompt 有 trust/authorization/证据边界，Review 有 failure-path/security finding 与 auth/authz high-risk readiness，Design/Test 有架构和测试方法，但没有 threat-boundary→asset→STRIDE→abuse-case 的攻击域流程。[`prompts/CLAUDE.fragment.md:L6-L17`；`skills/review-and-finish/SKILL.md:L10-L59,L108-L140`]

**独有、冲突、所有权与成本**

- [真缺口] SSRF scheme/host/IP/redirect/DNS-rebinding、资源级授权、上传/敏感字段、依赖 reachability/install scripts、产品 LLM output/tool/RAG 边界；这些应转成具体 invariants/abuse cases 交 `test-strategy` 选择验证。
- 改写版只在明确 security audit/hardening，或 auth/authz/permissions、敏感数据、upload、用户 URL/webhook、依赖脚本、模型工具权限等非平凡 trust boundary 时触发；普通模式清楚的小输入字段留 base。
- 技术类别本身不能成为 blanket human approval；package audit/pre-release grep 可能联网/依赖工具；密钥轮换、撤销、历史清理、commit 都需独立授权。Markdown 也不能替代 host permission/hook/CI 的确定性阻断。[`README.md:L25-L38`]
- 具体 Node 库、bcrypt rounds、rate limits、OWASP/LLM 年份和 package-manager 矩阵是时点/栈相关内容，本次未外部核验；应按需引用并标记时效，不写成通用硬门。
- 原包核心 SKILL、205 行 checklist、112 行 persona 与 `/ship` 高度重复；最低维护面应是一份窄 Skill、最多一份去重 reference、正负路由和一个对抗 fixture。

**关键证据与未知项**

- `agent-skills-main/skills/security-and-hardening/SKILL.md:L12-L74,L189-L220,L272-L310,L356-L382,L455-L467`
- `agent-skills-main/references/security-checklist.md:L102-L147`
- `skills/review-and-finish/SKILL.md:L10-L59,L108-L140`
- `skills/design-codebase/SKILL.md:L10-L30`
- `skills/test-strategy/SKILL.md:L30-L43`
- `agent-skills-main/evals/cases/security-and-hardening.json:L3-L45` 与 SSRF fixture 只有 happy path，不是安全行为已通过证据。
- 未验证外部时效事实或真实 headers/rate-limit/secret/SSRF runtime；安全自动触发上界仍需阶段 3 由用户决定。

###### `performance-optimization`

- **暂定动作：** `合并/协调重叠`
- **优先级：** `P1`
- **理由：** 保留窄性能域内核，但必须先与 debug/test/design/review 所有权协调。最终可落成独立窄 Skill 或域 reference；本阶段只确认不能原样新增，也不能把真实测量方法全部归入 generic review/test。

**Target 行为与当前覆盖**

- 目标对性能预算、慢报告、CWV 失败、回归怀疑、大数据/流量或已 profile bottleneck 触发；核心是 baseline→定位 bottleneck→只修该瓶颈→同方法复测→keep/revert→guard。[`agent-skills-main/skills/performance-optimization/SKILL.md:L12-L120`]
- 它要求同条件、单变量、重复测量、超过 run-to-run variance、correctness 优先、neutral/worse/test-red 回退；web auditor 进一步要求无 artifact 只能说 potential/not measured，并区分 field/lab/trace。[同文件:L292-L325；`agent-skills-main/agents/web-performance-auditor.md:L10-L55,L114-L123,L166-L184`]
- 当前 slow regression/latency tripled 的未知原因归 `debug-systematically`；`test-strategy` 有 benchmark/stress/property 但没有 baseline/噪声/attribution；Design/Review 分别拥有架构 trade-off 和完成证据。[`tests/trigger-matrix.md:L42-L47`；`skills/test-strategy/SKILL.md:L30-L43`]

**独有、冲突、所有权与成本**

- [真增量] measure-first 闭环、同条件与方差、correctness gates metric、无显著收益即撤回、field/lab/trace 诚实性和无 artifact 不声称指标。
- 未知慢/回归先 debug；只有明确性能目标、可测指标、已定位 anti-pattern/bottleneck 或显式 performance audit 才进入性能域。性能 owner 定指标/实验/attribution，test owner 定 harness/seam/runner，Design 处理非显然结构，Review 判 readiness。
- “未来大数据/流量”与“obvious anti-pattern 立即修”会诱发 speculative optimization；Synthetic+RUM 必选不适合 backend/CLI/microbenchmark，也可能引入遥测、用户数据和外部服务。
- Commit 带数字、PR/PERF.md 记录、固定 200KB/200ms/90 分、npx bundlesize/lhci、Lighthouse/CrUX/monitoring 均需项目预算、工具和动作授权，不能成为默认 gate。[target:L327-L397]
- 核心、154 行 checklist、185 行 web persona 和 `/webperf` 重复且有时效成本；最低维护是一个窄入口、栈特定按需 references、debug/performance 路由正负例和含 correctness/重复样本的 behavior fixture。

**关键证据与未知项**

- `agent-skills-main/skills/performance-optimization/SKILL.md:L12-L120,L292-L397`
- `agent-skills-main/references/performance-checklist.md:L14-L154`
- `agent-skills-main/agents/web-performance-auditor.md:L10-L55,L114-L123,L166-L184`
- `tests/routing-contract.md:L16-L29,L37-L61`
- `agent-skills-main/evals/fixtures/performance-optimization/benchmark.js:L1-L15` 只计时一次，无预热/重复/方差/correctness，不能证明目标最强行为。
- 未运行 benchmark/eval，也未外部核验 CWV、浏览器 API、CLI 或框架建议；不报告任何性能数值。

##### Verify + Review 对阶段 3“整体流程强度”决策的证据

**支持增加有条件验证门的证据**

- 当验收主张本身是浏览器渲染、事件、请求、持久化或 a11y 状态时，static code/test 不能闭合主张；需要指定 URL/state/channel 的真实 browser runtime signal。[`prompts/CLAUDE.fragment.md:L17`；`browser-testing-with-devtools.json:L29-L41`]
- Browser 运行前必须确定环境/profile/test data/action 与副作用；Security 需要在实质 trust boundary 上把 threat/abuse case 变成 observable invariant；这些是具体风险所要求的窄门，不是普遍流程。
- 高风险 auth/authz/permissions 完成项已有 focused readiness；新增 Security 应提供域证据而非第二次全面 Review。[`skills/review-and-finish/SKILL.md:L10-L21,L49-L59,L108-L130`]
- 性能 claim 必须有同条件 baseline/remeasure、正确性和超过噪声的结果；没有 artifact 只能标 potential/not measured。项目已有预算与可复现实验时，才有理由建立性能回归门。[`performance-optimization/SKILL.md:L292-L313`]
- 若新增/改变本组六项 runtime 行为，应补最小正/负/组合案例并至少做一次实际 behavior 验证；target Tier 2 只是词法近似，当前没有可审计 results。[`agent-skills-main/evals/README.md:L14-L22,L31-L38`]

**反对增加通用验证门的证据**

- 当前套件明确 Start lightweight；普通低风险编辑不自动 review、普通 UI/错误不自动升级，验证按 outcome/contract/risk 选择最小高信号检查并复用仍有效证据。[`README.md:L19-L23`；`skills/review-and-finish/SKILL.md:L15-L19,L108-L116`]
- Browser 全通道/零 warning/all findings、Debug 不可跳步/full suite、Review every change、多模型 review、Simplify 逐改全测、Security 每类 Ask First、Performance synthetic+RUM 都会把领域提示变成通用仪式。
- 工具不可用时增加文字 gate 不产生证据；应明确 blocker 与 `UNVERIFIED`。模型规则也不能替代 MCP/权限/PreToolUse/CI 的确定性能力。[`README.md:L25-L38`]
- `.mcp.json`、`npx`、load/CI/alert、Git bisect、audit、密钥轮换/历史清理、RUM/CrUX/monitoring、commit/PR/PERF.md 各自有不同副作用和授权，不能由“验证/审查/安全/性能”标题统一授权。
- 固定行数、时限、预算、CWV、库版本、rate limit、bcrypt rounds 和工具列表没有本项目运行证据且会随栈/时间漂移；按具体 claim 与项目事实选择门更可靠。
- 主机 `code-review`/`simplify` 推荐 user-invocable-only，且具体实现不可见；当前只能维护所有权边界，不能用候选自动 Skill 重建或宣称逐项优劣。[`README.md:L90-L107`]

**中性边界事实**

- 当前运行权威仍是 prompt 与 runtime Skill description/body；tests/evals/checklists/fixtures 是维护证据，不是第二运行层或执行授权。
- Target 目录是未跟踪、无独立 revision 的比较材料；目标命令、persona 和 hooks 未安装、未执行，也没有 checked-in behavior results。
- 主机 `code-review`/`simplify` 的 user-invocable-only 是 README 推荐配置，不是仓库强制设置；已验证的是项目推荐边界，不是本机实际配置或内部语义。
- P0 统一表示引入前必须解决直接冲突；P1 表示有价值且需协调但不紧急。两者都不是阶段 4 授权。

##### 本组执行状态

- 四个 slice 均为 `complete`：Verify/browser 1/1、Verify/debugging 1/1、Review/host-boundary 2/2、Review/domain 2/2；没有 blocked、failed、stale、skipped、unverified 或空结果。
- 四个 worker 均为强制无 shell/Edit/Write 的 `capability-harness:evidence-researcher`，只使用 Read/Grep/Glob；没有 WebSearch/WebFetch、文件修改、命令、Hook、测试或浏览器执行。
- 分析基线为当前项目 `main@f82a1b2` 与 target current unversioned working tree；结论是静态合同审计，不是 live host/model、security control、browser observation 或 performance measurement。
- 本组已写入 `MIGRATION_PLAN.md`，并已获得用户确认；后续 Ship 分析不改变本组已确认的 provisional classification，也不构成阶段 4 吸收授权。

#### 第 4 组：Ship（已完成，已确认）

> 本组仍是阶段 2 的 provisional classification，不是阶段 4 的引入授权。六项均为 `P0`，含义都是“若要吸收，必须先解决直接的权限、所有权、路由或证据冲突”，不表示六项都应采用，也不表示当前未跟踪 target 已经影响运行时。

##### 暂定结论汇总

| 分类 | Target 条目 | 当前暂定动作 | 优先级 | 核心理由 |
| --- | --- | --- | --- | --- |
| Ship | `git-workflow-and-versioning` | `合并/协调重叠` | `P0` | 当前 `finish-branch` 已安全拥有 commit/push/PR/merge/discard/cleanup 的逐动作边界。只值得把“明确 commit 授权之后”的原子拆分、独立绿色和解释 why 的消息 craft 合并进去；`Always`、auto-commit、`reset --hard`、自动 cleanup、tag+push、固定 trunk/npm/Husky 政策均应删除。[`skills/finish-branch/SKILL.md:L8-L30,L46-L118`；`agent-skills-main/skills/git-workflow-and-versioning/SKILL.md:L18-L189,L270-L356`] |
| Ship | `ci-cd-and-automation` | `新增/改写引入` | `P0` | 当前没有 repository-owned CI pipeline definition 的专门 owner。新增版应只负责发现项目 provider/toolchain 后设计或修改 trigger、job、dependency、artifact、secret reference 和 failure semantics；不得自动运行 hosted CI、改 branch protection/auto-merge、commit/push、部署或 rollback。[`agent-skills-main/skills/ci-cd-and-automation/SKILL.md:L16-L54,L56-L191,L193-L390`；`tests/routing-contract.md:L16-L35`] |
| Ship | `deprecation-and-migration` | `合并/协调重叠` | `P0` | 通用 migration planning/design/test/readiness 已有 owner；独有增量是 consumer inventory、通知/合同窗口、replacement/no-replacement、usage-gated removal、owner/exception 和有前提的 expand/contract criteria。最小落点是 `plan-work` 的按需 deprecation reference，而不是再建横跨设计、执行、验证和删除的同权 Skill。[`agent-skills-main/skills/deprecation-and-migration/SKILL.md:L37-L190,L231-L247`；`skills/plan-work/SKILL.md:L10-L36`] |
| Ship | `documentation-and-adrs` | `合并/协调重叠` | `P0` | 普通 README/API/comment/changelog 修改继续留在 base，架构决策继续归 `design-codebase`。只把 ADR convention discovery、编号/命名冲突、status 和 supersession 历史压缩并入现有 ADR reference；不新增广触发 documentation owner，不因 shipping/API change 自动落盘或默认创建 `docs/decisions/`。[`agent-skills-main/skills/documentation-and-adrs/SKILL.md:L23-L100,L200-L288`；`skills/design-codebase/SKILL.md:L57-L76`] |
| Ship | `observability-and-instrumentation` | `新增/改写引入` | `P0` | 当前缺少持久产品级 telemetry owner。保留 on-call question→最小 signal、structured event、cardinality、correlation/trace 和 actionable alert；删除“任何生产功能/I/O PR”、每端点 RED、每资源 USE、固定告警和 staging 注错等普遍要求，并与 debug/test/design/review 及远程监控动作严格分开。[`agent-skills-main/skills/observability-and-instrumentation/SKILL.md:L25-L165,L190-L203`；`skills/debug-systematically/SKILL.md:L20-L76`] |
| Ship | `shipping-and-launch` | `新增/改写引入` | `P0` | 当前 `review-and-finish` 只拥有 repository/development-artifact readiness，尚无针对一个 concrete production release 的环境、staging、SLO、telemetry、on-call、rollback owner/data semantics 和 GO/BLOCK/UNVERIFIED owner。新增版必须把 verdict 与 deploy/flag/migration/rollback/Git 动作分开，并删除固定三 persona、固定阈值、Web 全套清单和 sequential-as-parallel fallback。[`agent-skills-main/skills/shipping-and-launch/SKILL.md:L12-L75,L77-L265,L293-L310`；`skills/review-and-finish/SKILL.md:L108-L140`] |

##### Ship 详细分析

- **完整性说明：** 五个只读 slice 完整分类 6/6 项：Git 1 项、delivery 2 项、deprecation/migration 1 项、documentation 1 项、observability 1 项。各 owner 均读取目标 SKILL、物质相关的直接 references/personas/commands、匹配 eval/fixture，以及当前 prompt、相邻 runtime Skills、README 与路由合同；没有执行其中任何命令、Hook、eval、测试、Git、CI、部署、迁移、监控或发布动作。

###### `git-workflow-and-versioning`

- **暂定动作：** `合并/协调重叠`
- **优先级：** `P0`
- **理由：** 不新增第二个 Git owner。只在用户已明确授权 commit 且 `finish-branch` 已解析精确 scope 后，吸收最小 commit-craft 增量；版本语义只作为非执行建议，tag 写入能力不由本项顺带引入。

**Target 实际行为**

- frontmatter 同时声称“任何代码改动/Always”与 commit、branch、conflict、parallel stream、release/version/tag/changelog 意图；其自身普通 loading-spinner 负例却要求不触发，静态合同内部不一致。[`agent-skills-main/skills/git-workflow-and-versioning/SKILL.md:L2-L15`；`agent-skills-main/evals/cases/git-workflow-and-versioning.json:L18-L25`]
- 目标要求每个成功增量 commit、原子拆分、每个 commit 绿色、约 100 行、固定消息和分支惯例，并给出 npm/lint/tsc/Husky 示例。[target:L18-L145,L191-L242]
- 它把 worktree remove、分支删除和失败后的 `git reset --hard HEAD` 写成普通流程，又把 annotated tag 与 `git push origin <tag>` 紧邻展示。[target:L147-L189,L270-L311]

**当前覆盖、独有缺口与所有权**

- 当前 `finish-branch` 已拥有 commit、push、PR、local/remote merge、discard、branch deletion 和 worktree removal，区分每项授权、精确范围、恢复性、force、tag 和部分失败；`review-and-finish` 的 ready verdict 不授权这些动作。[`skills/finish-branch/SKILL.md:L8-L15,L32-L118`；`skills/review-and-finish/SKILL.md:L108-L140`]
- [有限增量] 当前 Commit 小节已有 scope/message 安全，但没有明确要求逻辑原子、独立绿色和消息解释 why；这些只应成为“commit 已获授权之后”的 craft，不得成为 auto-commit trigger。[`skills/finish-branch/SKILL.md:L46-L55`]
- [有限未知缺口] 当前指定来源没有 SemVer/changelog/tag-write owner；候选只展示不安全的 tag+push，不能据此扩展执行面。若未来真实需要 tag，必须分别定义 local-tag、push-tag、更新/force 和失败幂等合同。

**冲突、维护成本与证据边界**

- `Always`、tests-pass→commit、reset/cleanup 和 tag push 与动作级授权直接冲突；固定 trunk、1–3 天分支、前缀、行数、npm/tsc/Husky 也不能覆盖项目实际惯例。[`prompts/CLAUDE.fragment.md:L8-L16`]
- 原样引入 356 行常触发文本会与 base、`finish-branch`、Review 和目标自身 review material 重复；最小改法只触及现有 Commit 小节及相应边界回归。
- 候选唯一行为 eval 只证明其预期把一个混合 patch 拆成绿色提交，没有验证授权、push/tag、reset、cleanup、force/history rewrite 或 review/branch 分离；本组未运行该 eval。[`agent-skills-main/evals/cases/git-workflow-and-versioning.json:L28-L42`]

###### `ci-cd-and-automation`

- **暂定动作：** `新增/改写引入`
- **优先级：** `P0`
- **理由：** 新增一个窄版 CI-definition owner：负责 repository-owned pipeline definition，不负责 hosted execution、远端仓库策略、Git 动作或 production launch。

**Target 实际行为**

- 目标把 pipeline setup/modification、quality gates、CI test runner、deployment strategy 和 CI failure debugging 全列为触发，并规定 lint→type→unit→build→integration→可选 E2E→security→bundle 的固定序列。[`agent-skills-main/skills/ci-cd-and-automation/SKILL.md:L16-L54`]
- 正文直接给出 GitHub Actions、Node/npm、Postgres/Prisma、Playwright 配置；failure loop 包含自动修复、commit 和 push。[target:L56-L191]
- 它还承担 preview/production deploy、feature flag、staged rollout、rollback、Dependabot、branch protection、auto-merge 和“小于十分钟”门禁。[target:L193-L390]

**当前覆盖、独有缺口与所有权**

- 当前 `test-strategy` 拥有测试层级/seam/fixture/timing，`debug-systematically` 拥有未知失败根因，`review-and-finish` 消费 CI evidence 判断 readiness，`finish-branch` 拥有明确 Git 动作；根仓 `workflows/` 是 Claude saved workflows，不是项目 CI。[`skills/test-strategy/SKILL.md:L20-L43`；`workflows/README.md:L30-L40`]
- [真缺口] 当前 catalog 没有读取 manifest/lockfile/scripts/existing workflow/provider/runner 后，安全设计或修改 trigger、job dependency、artifact、secret reference 与 failure semantics 的 owner。[`README.md:L40-L67,L121-L133`]
- 改写版应区分：definition 存在、静态 parse、本地项目命令、hosted run、required status、merge blocking 六种 evidence state；没有远程证据时返回 `UNVERIFIED`，不能从 YAML 推导平台行为。
- 实际运行/重跑/取消/批准 hosted CI、修改 branch protection/auto-merge、部署、rollback、commit/push/merge/PR 均不属于该 Skill。若一次配置写入在后续 push 后会自动部署，写入前必须披露传递副作用。[`prompts/CLAUDE.fragment.md:L12-L17`]

**冲突、维护成本与证据边界**

- 固定全套 gate 与 path filter/定时慢测自身矛盾，也与当前按 acceptance/risk/evidence-cost 选择最小高信号检查冲突。[`skills/test-strategy/SKILL.md:L34-L43`]
- GitHub Actions/Node/npm/Vercel/Prisma/Playwright 示例必须降为项目事实支持时才选用的 reference；provider、版本、secret model 和 runner 都会漂移。
- 目标 eval 缺少 external run、deploy-now、launch readiness、commit/push 等相邻非触发；fixture 又没有 lockfile，不能证明 `npm ci` 或真实 merge-block behavior。本组没有运行 hosted CI 或 eval。[`agent-skills-main/evals/cases/ci-cd-and-automation.json:L3-L42`]

###### `deprecation-and-migration`

- **暂定动作：** `合并/协调重叠`
- **优先级：** `P0`
- **理由：** 不建立贯穿 Define/Plan/Build/Verify/Ship 的第二 migration owner。把真正独有的产品/API/schema 退役条件改写为 `plan-work` 的按需 reference，由已有 Design/Test/Review owner 分别处理架构、证明和最终就绪。

**Target 实际行为**

- 目标广泛触发旧系统/API/功能移除、用户迁移、重复实现、死代码和维护还是日落判断；用 unique value、消费者、replacement、迁移成本和持续维护成本决定 advisory/compulsory。[`agent-skills-main/skills/deprecation-and-migration/SKILL.md:L2-L65`]
- 四步过程要求先构建并生产验证 replacement，再通知、逐消费者迁移，最后在零使用后删除旧代码、测试、文档、配置和 notice。[target:L67-L118]
- 它提供 strangler、adapter、flag 与 schema expand→dual-write/backfill/read-switch→contract，并写成每个 migration 都有 tested down path 等绝对规则。[target:L120-L190]

**当前覆盖、独有缺口与所有权**

- 当前 `plan-work` 已拥有 migration/compatibility/sequencing/scope，`design-codebase` 拥有 seam/adapter/interface/ownership，`test-strategy` 拥有兼容性证明，`review-and-finish` 拥有已完成迁移、公共契约、持久数据和破坏动作的 PASS/BLOCK/UNVERIFIED。[`skills/plan-work/SKILL.md:L10-L36`；`skills/review-and-finish/SKILL.md:L108-L140`]
- [真增量] consumer inventory、合同/通知窗口、联系覆盖、replacement 或合法 no-replacement、每消费者责任、实测剩余 usage、exception owner 和 removal criteria 在当前通用流程中未明确。[`agent-skills-main/evals/fixtures/deprecation-and-migration/api-inventory.md:L1-L9`]
- schema 旧新版本共存和 late contract 可保留为有前提 heuristic；不能保留“additive 总是安全”或普遍运行 down migration。
- 产品 owner 决定维护/日落、advisory/compulsory、deadline 与残余消费者风险；规划、零使用证据或 Skill 激活都不授权通知、切流、backfill/down/drop、部署或删除。

**冲突、维护成本与证据边界**

- 原触发与 `plan-work`/`design-codebase`/`review-and-finish` 同权竞争，并把分析/计划请求直接推进 build、migrate、remove，构成 P0 权限冲突。
- 独立 Skill 会重复五个 owner 和大量 generic pattern；按需 reference 只需协调 `plan-work` frontmatter、组合路由及最小正负案例，维护面更小。
- 唯一行为 eval 只覆盖公共 v1 REST API 计划；没有 no-replacement、强制安全 cutoff、internal dead code、不可逆 schema 或授权边界，且本组未运行。[`agent-skills-main/evals/cases/deprecation-and-migration.json:L28-L42`]

###### `documentation-and-adrs`

- **暂定动作：** `合并/协调重叠`
- **优先级：** `P0`
- **理由：** 只合并 ADR lifecycle 的有界缺口，不新增把 architecture decision、README、API docs、comment、changelog 和 agent rules 混在一起的自动 Skill。

**Target 实际行为**

- 目标在 architecture decision、public API change、feature shipping、onboarding 或重复解释时触发，并要求 ADR 前发现 existing location/format/numbering/tooling。[`agent-skills-main/skills/documentation-and-adrs/SKILL.md:L3-L49`]
- 它提供 context/decision/alternatives/consequences 模板和 proposed/accepted/superseded/deprecated 生命周期，主张保留旧 ADR。[target:L46-L100]
- 同一 Skill 又覆盖 inline comments、TypeScript/OpenAPI、README、changelog、CLAUDE/rules/spec，并用“所有重大决定均有 ADR、所有文档均完整”等全项目 checklist 收尾。[target:L102-L288]

**当前覆盖、独有缺口与所有权**

- 当前 base 已能按具体请求编辑现有 README/API docs/comment/changelog；`design-codebase` 拥有架构决策和经用户同意的 ADR，`issue-workflow` 拥有 PRD/issue，`plan-work` 拥有 implementation plan，`skill-refactorer` 拥有 coding-agent instructions。[`prompts/CLAUDE.fragment.md:L6-L17`；`skills/design-codebase/SKILL.md:L57-L76`]
- [真增量] 写 ADR 前系统匹配 location/extension/format/numbering/headings/tooling、冲突时不引入第二套 scheme，以及用后继 ADR supersede 而非删除历史；当前 ADR reference 只定义高门槛和短格式。[`skills/design-codebase/references/domain-modeling.md:L30-L38`]
- 普通 code-adjacent docs 保持 base；架构决定必须先由 Design owner 选择，ADR 只是已选决定的持久 rationale。无 repo convention 时先在 chat 提案并取得 target agreement，不自动创建 `docs/decisions/`。
- Lessons、handoff、unresolved decision map、PRD、plan 和 agent instruction 各保留现有 owner；背景 artifact 不能扩大写入或发布授权。

**冲突、维护成本与证据边界**

- “发生架构/API/shipping 事件即创建文档”把事件误当写入授权，并与当前 ADR 用户请求/同意 gate 冲突；广泛 cleanup 也违反最小相关范围。
- 原样引入至少六种产物及长模板，会显著扩大与 base/design/issue/plan/memory/refactorer 的组合矩阵；最小改法只更新现有 Design ADR reference 和相应回归。
- 目标 eval 的正例/负例未覆盖相邻 owners、持久化授权、既有 convention、编号冲突或 supersession；唯一行为 fixture 也没有 repo convention。本组未运行 eval。[`agent-skills-main/evals/cases/documentation-and-adrs.json:L3-L42`]

###### `observability-and-instrumentation`

- **暂定动作：** `新增/改写引入`
- **优先级：** `P0`
- **理由：** 新增一个问题驱动、项目约定优先的持久 operational telemetry owner；不把普通生产小改、主动故障诊断、PR review 或远程监控操作自动升级为该流程。

**Target 实际行为**

- 目标同时对 logging/metrics/tracing/alerts、任何 production feature/service/endpoint/job/integration、数据不足的生产问题，以及含 I/O/retry/queue/cross-service 的 PR 触发。[`agent-skills-main/skills/observability-and-instrumentation/SKILL.md:L2-L24`]
- 有价值的核心是先写 2–4 个 on-call questions，再按聚合、跨服务位置或单事件原因选择 metric/trace/log；结构化事件、correlation、bounded labels、histogram、context propagation 和 actionable alert 均围绕可回答的问题。[target:L25-L155]
- 目标同时强制每端点/依赖 RED、每资源 USE、全链路 trace、至少一个告警，并要求 staging 注错、发流量、访问 tracing UI、改阈值和试发频道。[target:L93-L165,L190-L203]

**当前覆盖、独有缺口与所有权**

- 当前 `debug-systematically` 拥有未知故障、临时 instrumentation、敏感材料和清理；只有明确保留为 operational telemetry 的信号才转入本项。`test-strategy` 拥有 proof seam，`design-codebase` 拥有非显然 context ownership/interface，Review 拥有整体 verdict。[`skills/debug-systematically/SKILL.md:L20-L76`；`skills/debug-systematically/references/defense-in-depth.md:L16-L22`]
- [真缺口] 当前没有把 on-call question 转成最小 logs/metrics/traces，并检查事件 schema、cardinality、correlation/trace context、latency distribution 和 alert actionability 的产品可观测性 owner。
- 改写版先读项目现有 logger/meter/tracer、backend、命名、采样、隐私与配置惯例；不默认 prom-client/OpenTelemetry 或新增依赖。
- 最低安全边界可要求字段最小化/allowlist、禁止 secret/credential/个人数据和完整敏感 payload；具体标识符、保留期、第三方/跨境、SLO、paging threshold、severity、runbook owner 属于用户/项目安全与运维决策。
- 仓库内 instrumentation、依赖安装、远程 dashboard/alert、共享阈值、测试流量、故障注入和 deploy 是不同动作；缺少精确授权或环境时只报告 `UNVERIFIED`。

**冲突、维护成本与证据边界**

- “任何生产功能/I/O PR”与 Start lightweight、base implementation 和 Review owner 冲突；主动故障触发还与正文的 debug 排除条款自相矛盾。
- 每端点 RED/每资源 USE/固定告警/全服务 trace 会在无 SLO、历史、成本、隐私和值班证据时替用户作产品决定；launch pre-gate 也应从本项删除。
- 203 行 SKILL 与 91 行根级 checklist 大量重复，且根级 reference 不随单 Skill 目录分发；最小版应去重并把必要 reference 放在自身目录。
- 目标行为 eval 未断言敏感数据、远程授权或邻接 owner，fixture 只是最小 JS 函数；本组未运行真实 logger/backend、staging 或 eval。[`agent-skills-main/evals/cases/observability-and-instrumentation.json:L1-L44`]

###### `shipping-and-launch`

- **暂定动作：** `新增/改写引入`
- **优先级：** `P0`
- **理由：** 新增一个只针对 concrete production release 的 launch-readiness owner；它消费而不复制 repository review、test、CI、security、performance、accessibility 和 observability evidence，并只输出 GO/BLOCK/UNVERIFIED 与缺口。

**Target 实际行为**

- 目标覆盖 production deploy、重大 release、数据/基础设施 migration、beta 和所有风险部署，要求跨代码、安全、性能、a11y、基础设施与文档的统一 pre-launch checklist。[`agent-skills-main/skills/shipping-and-launch/SKILL.md:L12-L75`]
- 它要求 feature flag、固定 rollout 百分比/时间窗与固定 error/latency/client/business thresholds，并内嵌 monitoring、首小时检查和 rollback 命令。[target:L77-L265]
- `/ship` 固定 dispatch code reviewer/security auditor/test engineer，再从 staged/recent code report 合成 GO/NO-GO；fallback 甚至要求顺序输出按 parallel 对待。[`agent-skills-main/.claude/commands/ship.md:L5-L72`]

**当前覆盖、独有缺口与所有权**

- 当前 `review-and-finish` 判定最终代码/开发 artifact 是否 ready，`plan-work` 负责通用 rollout/migration planning，`test-strategy` 负责测试证明，`finish-branch` 负责 Git，`agent-workflow` 决定是否需要独立 verifier；这些都不拥有 concrete production launch。[`skills/review-and-finish/SKILL.md:L108-L140`；`skills/agent-workflow/SKILL.md:L20-L67`]
- [真缺口] 一个具体 release 的 release-specific acceptance、环境/配置、current staging evidence、SLO/baseline、dashboard/alert、on-call/runbook、rollback owner/target/data semantics/RTO 和 production GO/BLOCK/UNVERIFIED。
- 每个 required criterion 应标 VERIFIED、FAILED/BLOCKER 或 UNVERIFIED，并记录 environment、freshness 和 source；repository tests/persona opinion 不能升级为 production evidence。
- GO 是证据判断，不是 deploy、publish、通知、DNS/env/secret、flag、migration、rollback、commit/push/merge 授权。rollback evidence 与 action 分开；实际动作必须解析 exact environment/version/flag/data/remote 并另获授权。
- 安全、数据完整性、required test 或 rollback control 的已失败 blocker 与可由有权 owner 接受的残余风险必须区分；日期、sponsor 或 authority pressure 不是证据。[`agent-skills-main/evals/fixtures/shipping-and-launch/authority-pressure.md:L1-L6`]

**冲突、维护成本与证据边界**

- 固定 fan-out 和 diff/file-count 阈值违反当前最小切片 fit check；顺序执行不得冒充 independent/parallel，独立上下文不可用时应标 `UNVERIFIED` 或 `BLOCKED`。
- 固定 rollout 百分比、24h/48h/一周窗口、通用阈值、Web CWV/CSP/a11y/CDN/DNS 全套清单缺少项目 SLO、历史和 applicability，不得成为默认 gate。
- `git revert && git push`、数据库 rollback、flag 和生产操作是独立外部/持久动作；launch assessment 不能执行它们。
- 候选 launch-status fixture 证明 E2E failure、缺 staging smoke/专用告警/rollback owner/runbook 是 repository green 无法覆盖的真实证据类别，但本组没有运行 production check、persona 或 behavioral eval。[`agent-skills-main/evals/fixtures/shipping-and-launch/launch-status.md:L1-L11`]

##### Ship 对阶段 3“整体流程强度”决策的证据

**支持增加有条件验证门的证据**

- 项目已经确认需要的 lint/type/test/build/security 等检查，适合变成可重复 CI evidence；但具体门禁由项目风险、验收和工具链决定，不由候选固定列表决定。[`ci-cd-and-automation/SKILL.md:L24-L54`；`skills/test-strategy/SKILL.md:L34-L43`]
- repository readiness 与 production readiness 是不同 claim；concrete release 的 current environment、staging、telemetry、on-call 和 rollback evidence 不能由绿色单测或代码 review 代替。[`shipping-and-launch/launch-status.md:L1-L11`]
- 公共 API/consumer 退役在最终删除前确需通知/合同窗口、联系覆盖和实测 usage；schema contract step 也需要旧新版本共存和数据语义证据。[`deprecation-and-migration.json:L31-L40`；`api-inventory.md:L1-L9`]
- 持久 telemetry 需要回答明确 on-call questions，并对 sensitive fields、cardinality、context propagation 和 alert actionability 有专项验收；静态代码存在本身不能证明后台已收到可查询信号。[`observability-and-instrumentation/SKILL.md:L25-L155`]
- ADR 在 hard-to-reverse 且 surprising 的已选架构决定中，可用 repo convention、status 和 supersession 保留历史；这是有条件的持久化门，不是每个 feature 的普遍文档仪式。

**反对增加通用验证门的证据**

- 当前套件明确 Start lightweight，验证按 acceptance、affected contract、risk 和 evidence gap 扩展；任何 change 自动 commit、任何 production feature 自动 telemetry、任何 deploy 固定全套 gate 都与该合同冲突。[`README.md:L19-L38`]
- 固定工具、provider、阈值、百分比、时间窗、行数、分支策略、test pyramid、RED/USE、Web 指标和 persona 数没有当前项目运行证据，也会随平台和风险模型漂移。
- static YAML、Markdown checklist、fixture、persona report 或 lexical eval 都不能证明 hosted CI、branch protection、staging、production、monitoring、rollback 或 live model behavior。
- commit/push/tag/merge、hosted CI、deploy、flag、migration、rollback、远程 dashboard/alert、通知和删除是不同动作；任何 review/readiness/verification/GO 语言都不能统一授权。
- 固定多 agent fan-out 既增加成本又可能制造虚假独立性；只有真正独立的问题且当前 runtime 实际提供独立上下文时才值得使用。[`skills/agent-workflow/SKILL.md:L20-L67,L97-L102`]

**中性边界事实**

- 当前 runtime 权威仍是 always-on prompt 与各 Skill description/body；README、routing tests、target eval、fixtures、checklists、commands 和 personas 只作比较证据。
- 根仓 `workflows/` 仍是显式 opt-in Claude saved-workflow source，不是 `.github/workflows/`，也不承担 hosted CI 或 production launch。
- Target 目录在会话基线中未跟踪且没有独立 revision；本组结论绑定当前工作树文本，不证明 target 已安装、已激活或其行为 eval 已通过。
- P0 的统一含义是“引入前先消除直接冲突”；本组六项都为 P0 是因为原文均触及授权/owner/evidence 硬边界，不代表优先全部实施。

##### 本组执行状态

- 五个 slice 均为 `complete`：Ship/Git 1/1、Ship/delivery 2/2、Ship/deprecation-migration 1/1、Ship/documentation 1/1、Ship/observability 1/1；没有 blocked、failed、stale、skipped、unverified 或空结果。
- 五个 worker 均为强制无 shell/Edit/Write 的 `capability-harness:evidence-researcher`，只使用 Read/Grep/Glob；没有 WebSearch/WebFetch、文件修改、Git、命令、Hook、eval、测试、CI、部署、迁移、监控或发布执行。
- 工作流共完成 5/5 agents、358 次只读工具调用；分析基线为当前项目 `main@f82a1b2` 与 target current unversioned working tree。结论是静态合同审计，不是 live host/model、CI provider 或 production runtime 证明。
- 本组已写入 `MIGRATION_PLAN.md`，并已获得用户确认；后续基础设施分析不改变本组已确认的 provisional classification，也不构成阶段 4 吸收授权。

#### 基础设施组：agents、references、evals、hooks、commands 与分发维护（已完成，已确认）

> 本组仍是阶段 2 的 provisional classification，不是阶段 4 的引入授权。基础设施动作只判断落点、维护责任、权限和证据边界；不因为 target 有文件、manifest、eval 或安装说明就视为当前运行时能力。P0 表示原样引入前必须先解决直接冲突，不表示批准采用。

##### 覆盖与暂定结论汇总

本组覆盖 Phase 1 清单中的 163 个 target 文件：24 个 `SKILL.md` 与 4 个 `idea-refine` 支持文件继续由生命周期条目负责，不在基础设施组重新分类；基础设施账本覆盖其余 135 个文件，包括 4 个 agents、7 个 root references、9 个 hooks、17 个 command/validator 文件、23 个分发/维护文档与 manifest 文件、74 个 eval/validation 文件。`docs/agents.md` 归 agents/orchestration owner；三个命令文件中的 persona wiring 只作 commands owner 的证据，不产生第二个文件级动作；`validate-commands.js` 归 commands owner，其他四个验证脚本归 eval/validation owner。

| 基础设施面 | Target 条目或文件范围 | 当前暂定动作 | 优先级 | 核心理由 |
| --- | --- | --- | --- | --- |
| Agent | `code-reviewer.md` | `跳过` | P0 | 与当前 Review 方法及宿主 `/code-review` 重复，不建立第二个 Review owner。 |
| Agent | `security-auditor.md` | `合并/协调重叠` | P0 | 安全领域 lens 有价值，但应回到 Security Skill；不原样维护独立 persona、PoC 或固定 `/ship` fan-out。 |
| Agent | `test-engineer.md` | `跳过` | P0 | 与 `test-strategy`、现有测试方法和按需 verifier 重复。 |
| Agent | `web-performance-auditor.md` | `合并/协调重叠` | P0 | Quick/Deep、metric honesty 和性能 lens 回到 Performance owner，不新增宽泛 persona。 |
| Orchestration | `references/orchestration-patterns.md` + `docs/agents.md` | `合并/协调重叠` | P0 | 当前 `agent-workflow` 已拥有编排；只吸收必要的 host/agent 关系说明，命令文件由 commands owner 单独负责。 |
| Reference | `accessibility-checklist.md` | `合并/协调重叠` | P1 | 作为 UI/a11y 按需 reference；不建立全项目常驻 checklist。 |
| Reference | `definition-of-done.md` | `保留现状不动` | P0 | target 的 standing DoD 与当前按 acceptance/risk 验证冲突，不引入第二个全局完成门。 |
| Reference | `observability-checklist.md` | `合并/协调重叠` | P0 | 只保留问题驱动 telemetry 规则，去掉固定 RED/USE、launch gate 和未授权远程动作。 |
| Reference | `performance-checklist.md` | `合并/协调重叠` | P1 | 作为性能 owner 的按需、栈相关 reference；删除 Web 指标和固定预算的普遍要求。 |
| Reference | `security-checklist.md` | `合并/协调重叠` | P0 | 作为 Security Skill 的去重 reference；不复制固定 OWASP/供应链/LLM 硬门。 |
| Reference | `testing-patterns.md` | `跳过` | P1 | 当前 `test-strategy` 已有按风险选择测试层级、seam 与执行安全，target JS/TS 示例不足以形成独立缺口。 |
| Hook | SessionStart meta injection（三文件） | `合并/协调重叠` | P1 | 不启用第二个全局 router；仅保留 material-assumption/技术异议等已确认的窄行为候选。 |
| Hook | SDD WebFetch cache（三文件） | `跳过` | P0 | URL/ETag 缓存的是 prompt-shaped 结果，不能证明当前问题得到 exact source；当前 manifest 也未注册。 |
| Hook | simplify protected-block filter/restore（三文件） | `新增/改写引入` | P0 | 具有确定性保护价值，但必须改写为显式 opt-in、窄 scope，并先解决原地写入、路径、备份/恢复和宿主事件边界。 |
| Eval | `evals/README.md` | `合并/协调重叠` | P1 | 分层和成本说明有价值，但必须服从当前根 routing source，不成为第二运行时路由层。 |
| Eval | `scripts/run-evals.js` | `合并/协调重叠` | P0 | Tier 2 可协调为目录级静态检查；Tier 3 含 Edit/Write/Bash/WebFetch/WebSearch、临时 Git、headless Claude 和结果写入，必须保持明确 opt-in。 |
| Eval | `scripts/run-evals-test.js` | `新增/改写引入` | P1 | 可复用回归 scaffold，但需补齐 schema、collision、lint、权限和 Tier 3 安全边界，不能原样证明行为。 |
| Eval | `scripts/validate-skills.js` | `新增/改写引入` | P1 | 只读结构 wrapper 有价值，但需改为当前 13 个 Skill 与插件的 scope 和规则。 |
| Eval | `scripts/lib/skill-lint.js` | `新增/改写引入` | P1 | 纯函数结构规则可复用；必须先协调当前 frontmatter、required sections、trigger 和 reference 规则。 |
| Eval corpus | 24 cases / 45 fixtures | `新增/改写引入` | P1 | 可作为维护和验证资产接入当前静态模型，不引入第二运行时指令解释层；29 个 behavioral eval 仍无结果。 |
| Eval corpus | ownerless negative 与边界审计 | `合并/协调重叠` | P1 | 38 个 negative 有 owner，10 个没有；补相邻 owner 或明确 out-of-catalog，不能强行重分类 Skill。 |
| Eval corpus | browser runtime capability gate | `跳过` | P1 | 当前 executor 没有 browser/DevTools 工具；保留定义但不把静态 fixture 当 DOM/console/network 结果。 |
| Eval corpus | hidden patch/materialization | `保留现状不动` | P1 | 当前隔离 workspace 与 `.eval` patch 机制已有合理形状；不在 fixture 中再造权限指令。 |
| Eval corpus | fixture realism / 窄 gate | `保留现状不动` | P2 | 样本覆盖足够，真实性风险按少数 capability/result gate 处理，不普遍扩大静态门。 |
| Eval delivery | results/CI 接入边界 | `新增/改写引入` | P2 | 未来若需持续 gate，只接 deterministic 结果和独立产物；当前没有 `evals/results` 或 `.github/workflows`，不在本阶段创建。 |
| Command | `/spec`、`/plan`、`/planning`（4 files） | `跳过` | P1 | 与 Define/Plan Skill 和当前 chat-first 规划重复；不新增 custom command layer。 |
| Command | `/build`（2 files） | `跳过` | P0 | 自动执行、逐任务 commit 和 whole-plan 模式越过当前 base/测试/Git 授权边界。 |
| Command | `/test`（2 files） | `跳过` | P1 | 与 `test-strategy` 和宿主测试能力重复，且会把 browser/TDD 流程固定化。 |
| Command | `/review`、`/code-simplify`（4 files） | `跳过` | P0 | `/code-review` 与 `simplify` 继续让位宿主；目标命令会产生第二个 Review/Simplify 路径。 |
| Command | `/ship`（2 files） | `合并/协调重叠` | P0 | 仅可在未来 launch owner 与 agent-workflow 已获批后重新设计 explicit readiness 入口；不保留固定 fan-out 或实际 rollback/Git。 |
| Command | `/webperf`（2 files） | `跳过` | P2 | 领域方法属于 Performance/browser owner，custom slash alias 没有独立必要。 |
| Command | `scripts/validate-commands.js` | `跳过` | P1 | 当前没有 custom command surface；脚本只比较 description，不验证 body、host registration 或 Gemini 缺失，不能原样成为 parity gate。 |
| Distribution | 根 README 与多工具产品定位 | `保留现状不动` | P0 | 是否从 Claude-focused 轻量套件扩展到多平台是阶段 3 的产品选择；在决定前不改 current 英中定位。 |
| Distribution | Claude/plugin manifest | `合并/协调重叠` | P1 | 可参考 manifest 形状，但必须 current-owned、自包含、命名空间化，不能替换现有 capability-harness 或引入 target 上游身份。 |
| Distribution | Codex 与 `.agents` manifests | `跳过` | P1 | 静态 metadata 不证明当前 Codex/marketplace runtime；除非用户选择该平台范围，不引入维护面。 |
| Distribution | Antigravity/Gemini 包装与命令面 | `跳过` | P1 | `.gemini/commands` 实际缺失，且 host discovery/命名空间未验证；不把文档声明当作支持。 |
| Documentation | adoption/getting-started 与平台 setup docs | `保留现状不动` | P1 | 不替用户承诺多平台兼容；若未来选择扩展，必须新增 Tested/Experimental/Unverified 矩阵并同步双语 README。 |
| Documentation | contributor/anatomy/rule 基础设施 | `跳过` | P1 | target 依赖缺失的 `CONTRIBUTING.md`、`AGENTS.md`，且 rules/Skill anatomy 会增加第二套维护规范。 |
| Documentation | 文档/manifest 声明的验证与 CI 门 | `保留现状不动` | P1 | `.github/workflows`、顶层 `package.json` 缺失；不因文档声称 CI 就创建或运行外部 pipeline。 |
| Documentation | `docs/comparison.md` | `跳过` | P2 | 外部比较没有当前维护结果或产品需求，不进入 runtime 或维护层。 |
| Metadata | `.gitattributes`、`.gitignore` | `保留现状不动` | P2 | 文本换行与生成物忽略可作参考，但不是当前能力缺口。 |
| Attribution | LICENSE 与 manifest license metadata | `合并/协调重叠` | P0 | 以实际 LICENSE 的 GNU AGPL v3 为来源标准；manifest 的 MIT 是事实不一致，只作记录，不在本阶段作法律兼容结论。 |

##### 基础设施详细分析

###### Agents 与 orchestration

- 四个 persona 并不形成四个新的 runtime owner：`code-reviewer` 与当前 Review/宿主 `/code-review` 重复，`test-engineer` 与 `test-strategy` 重复，均暂定跳过；`security-auditor` 的 trust-boundary lens 和 `web-performance-auditor` 的 Quick/Deep、metric-honesty 可回到对应领域 Skill/reference，不原样保留独立 persona。
- `references/orchestration-patterns.md` 与 `docs/agents.md` 只可在当前 `agent-workflow` owner 内做窄协调。当前编排已拥有 fit check、独立问题拆分、最小 fan-out、真实报告 sequential/parallel 和 evidence handoff；不要复制固定三 persona 或把 persona 变成第二路由器。
- Target 自身有内部漂移：`docs/agents.md` 声称 `/review`、`/test` 包装 persona，但对应命令正文只调用 Skill；`/ship` 的固定 fan-out 与当前 fit check 冲突。三个命令文件由 commands 条目持有，不能与 orchestration 条目形成双重修改责任。
- 所有 persona 的名称解析、上下文隔离、插件注册和 host precedence 都未运行验证；静态 agent 文件不是当前宿主提供独立 fresh context 的证据。安全 PoC、测试执行、性能采样和最终 verdict 也不能由 persona 名称授权。

###### Root references/checklists

- 六个非-orchestration root reference 都是 target 根级文件，而当前仓库按 Skill 文件夹安装、以 skill-local references 维护；原样复制会产生路径不可移植和第二套长期规范。
- `accessibility-checklist` 适合在 UI Skill 按需引用；`observability-checklist` 只保留问题驱动 telemetry；`performance-checklist` 只保留 measure-first/variance/correctness；`security-checklist` 只保留 threat/abuse/invariant；这些都不能把 Web、RED/USE、OWASP 或固定阈值变成全局门。
- `testing-patterns` 的 JS/TS 示例与当前 `test-strategy` 的证据/成本方法没有足够独立 owner 价值，暂跳过；`definition-of-done` 的 standing universal bar 与当前按 acceptance/risk 复用证据冲突，保留现状不引入。
- 外部 WCAG、OWASP、CWV、工具版本及平台标准本轮未联网核验；reference 只能在阶段 4 获批后按项目栈和适用性改写，不能把目标表格当最新规范。

###### Hooks

- SessionStart 三文件暂不作为第二个全局 router 启用。当前 prompt 已是 always-on，Skills 按需，Capability Harness hook 只处理有界 UserPromptSubmit/SubagentStop；目标 `priority/message` payload、`CLAUDE_PLUGIN_ROOT`、插件发现和 fail-open 行为均未由宿主验证。若有窄增量，应写入现有 owner，不复制完整 meta-skill 注入。
- SDD cache 三文件跳过：pre/post hook 以 URL hash、ETag/Last-Modified 和 HTTP 304 缓存 prompt-shaped WebFetch 结果；304 不能证明该结果适合当前问题，且 target manifest 没有注册 WebFetch hooks。它还引入 jq/curl/哈希/持久缓存和 network side effects。
- simplify 三文件是唯一具有可考虑的确定性保护缺口：它试图在 Read/Edit/Write/Stop 事件中保护标记块，但存在原地占位、备份/恢复、异常 payload、路径边界、并发和宿主 event shape 的未验证风险。若阶段 3 批准，只能作为显式 opt-in 的窄 host hook，先做 host integration/backup-recovery 验证；不把文档设置片段视为已注册。

###### Eval/validation framework 与 corpus

- `evals/README.md` 的 Tier 1/2/3 分层有结构价值：结构 lint、词法 routing/collision、opt-in 行为 grading 应保持不同证据等级。Tier 2 可协调到当前根维护 tests；Tier 3 不能成为默认 CI 或完成门。
- `run-evals.js` 把 deterministic 检查与高副作用 executor 混在一起：Tier 3 会创建临时 workspace/Git、调用 headless Claude、允许 Edit/Write/Bash/WebFetch/WebSearch 并写 `evals/results`。这些动作必须单独授权、隔离、记录成本和 cleanup；静态读取不能证明执行安全或行为通过。
- `run-evals-test.js`、`validate-skills.js` 和 `skill-lint.js` 具有可复用的回归/结构 gate 形状，但 target 固定的 sections、frontmatter、trigger regex、exemptions 和 catalog 路径不能直接套用 current 13 Skills、plugins、host-owned boundary。需先确定当前 source of truth，再按需引入。
- Corpus 实际覆盖 24 个 case、29 个 behavioral records、76 positive、48 negative、45 个 fixture 文件；其中 22 个 execution case 有 fixture，2 个 dialogue case 无 fixture。当前没有 `evals/results` 或 `.github/workflows`，所以没有行为通过或 CI 接入证据。
- 38 个 negative 声明 owner、10 个未声明 owner；至少部分 ownerless negative 属于 frontend/spec/security/performance/shipping/git 相邻边界，另一些可能故意是 out-of-catalog。应补最小 pairwise 证据或保留明确无 owner，不能为通过率强配 owner。
- browser case 需要 DOM/console/network，但 executor allowlist 没有 browser/DevTools；保留静态定义、跳过行为结果。`.eval` patch 与临时 workspace 现状可保留，不在 fixture 内复制权限/副作用指令；fixture 现实性暂不增加普遍 gate。

###### Commands

- 当前根仓没有自定义 `.claude/commands`、`commands/*.toml` 或 `validate-commands.js`；target 的 8 对命令主要是 Skills 的第二入口。`/spec`/`/plan`、`/build`、`/test`、`/review`/`/code-simplify`、`/webperf` 均应跳过，避免重复当前 owner 或宿主命令。
- `/ship` 只保留为未来可能的显式 production readiness 入口候选，前提是 launch owner、agent-workflow fit check、CI/observability evidence 和动作授权先确定；不吸收固定 fan-out、顺序冒充并行、自动 deploy/rollback 或 Git。
- `validate-commands.js` 只比较 Claude/Gemini/Antigravity description，不检查 body、注册、权限或 host precedence；target 文档声称 8 个 Gemini commands，但 `.gemini/commands` 当前实际缺失。没有实际 command surface 前跳过 parity validator。
- 即使未来选择多工具，也必须先决定命令命名/namespace、宿主支持等级和实际安装验证；不同宿主的合法语法差异不能用字节级 parity 强行抹平。

###### 分发、维护文档、manifest 与来源

- Target 根 README 推动 24 Skill、4 persona、70+ agent 和多工具原生支持；当前 README/README.zh-CN 定义的是 Claude Code、13 Skill、轻量、按需安装和显式 workflow。多工具扩展是阶段 3 的产品范围选择，不是本阶段可擅自吸收的文档修正。
- Claude manifests 可以作为形状参考，但如果未来批准，应在 current `plugins/` 下建立 current-owned、自包含、命名空间化插件；不能将 target 上游 marketplace source、整套 host command 或重复 `/code-review` 当作当前插件。
- Codex、Antigravity、Gemini 和其他 setup docs/manifest 只证明 target 的静态支持叙事，不证明 host discovery、frontmatter、命令、agents、hooks 或 precedence。`.gemini/commands`、`.opencode`、`AGENTS.md`、`CONTRIBUTING.md`、`tests/`、`workflows/`、`.github/workflows`、顶层 `package.json` 均按当前快照记录为缺失/未验证，不补造文件。
- adoption/getting-started 文档暂保留 current positioning；若用户在阶段 3 选择扩展，必须用 Tested/Experimental/Unverified 支持矩阵，更新英中 README，并分别验证各宿主安装/发现/升级，不以文档声明替代 runtime smoke。
- contributor/anatomy/rule 与 comparison docs 不形成当前运行时缺口；target 对缺失 `CONTRIBUTING.md`、`AGENTS.md` 的引用是内部完整性问题，不能自动授权创建新维护层。
- 实际 `LICENSE` 是 GNU AGPL v3；`.claude-plugin/plugin.json`、marketplace manifest 和 `.codex-plugin/plugin.json` 中的 MIT 是客观元数据不一致。沿用既定规则以 GNU AGPL v3 作为来源/commit 标注标准，不在本阶段作法律兼容性结论。

##### 基础设施对阶段 3“整体流程强度”决策的证据

**支持增加有条件验证门的证据**

- `skill-lint`、Tier 2 routing/collision/schema 检查和 command/manifest presence 检查可以产生低副作用、可重复的结构证据；它们适合做维护门，但必须以当前 root Skill/source-of-truth 为范围。
- simplify protected-block hook 若获批，确实需要 host event、路径、备份/恢复、异常和并发的确定性 integration gate；静态设置片段无法证明保护生效。
- Tier 3 行为评估、browser case、Git patch/materialization 和 production/authority-pressure fixtures 证明某些主张不能由 Markdown 或静态 routing pass 闭合；可以保留显式 opt-in 的有界行为验证。
- 多工具支持若获批，必须验证各宿主的安装、发现、命令命名、namespace、权限和版本兼容性；target 文档与 manifests 不足以构成支持承诺。
- 根级 checklist 在 UI、安全、性能、observability 等具体域有可复用 acceptance seed，但应作为对应 owner 的按需 reference，而非全项目 standing bar。

**反对增加通用验证门的证据**

- 当前套件明确 Start lightweight；根级 DoD、每个任务 SessionStart router、每个命令 custom wrapper、所有 case Tier 3、每个生产 change 全 telemetry 都会把局部风险扩大为普遍仪式。
- Target scripts/hooks 含 jq/curl/Node/Bash、HTTP validators、临时 Git、headless Claude、Edit/Write/Bash/WebFetch/WebSearch、持久 cache/results 和外部宿主状态；文字 gate 不能替代逐动作授权或 host enforcement。
- 静态 tests、fixtures、manifest、lexical rank 和 expected_output 都不是 live model、browser、CI、host hook 或 production 证据；增加更多静态清单不能弥补缺工具或缺环境。
- 多工具 setup 与 commands 会持续受到 host 版本/路径/schema 漂移影响；在用户尚未选择产品范围前，建立完整 parity gate 只会提前锁定维护成本。
- 当前已有 `agent-workflow`、`test-strategy`、`review-and-finish`、`finish-branch` 和 Capability Harness 各自的 evidence/authorization/fit-check owner；重复 infrastructure gate 会形成第二运行时或同权所有者。

##### 基础设施执行状态与证据边界

- 七个 substantive read-only slice 已返回完整分类：personas/orchestration、root-checklists、commands、distribution/docs/manifests、hooks、eval-framework、eval-corpus；分别覆盖 6、6、17、23、9、5、69 个文件/路径单位（eval corpus 为 24 case + 45 fixture）。
- 所有 slice 使用 `capability-harness:evidence-researcher` 的 Read/Grep/Glob 边界；没有 WebSearch/WebFetch、shell、Git、安装、命令、Hook、eval、测试、浏览器、CI、部署、迁移、监控或发布执行。
- 初次基础设施交叉审计因两个 broad return 空结果而失败；窄化恢复补齐了 hooks 与 eval 两块。恢复后的最终 critic 又因 StructuredOutput/服务端中途失败未返回；主线程以 Phase 1 的 163-file inventory、各 slice ledger、直接路径计数和上述去重规则执行聚焦一致性检查，故不把自动 critic 结果写成已通过。
- 当前结论只绑定会话基线 `main@f82a1b2` 与 target current unversioned working tree；target 无独立 revision。静态定义、源码推演、fixture/manifest 存在和测试文本均不证明 live host/model/runtime 行为。
- 本组已写入 `MIGRATION_PLAN.md`；基础设施动作已获确认，但仍必须按阶段 4 的逐条授权和独立验证边界处理。

#### 后续分类状态

| 分类 | 状态 |
| --- | --- |
| Plan | 已完成，已确认 |
| Build | 已完成，已确认 |
| Verify | 已完成，已确认 |
| Review | 已完成，已确认 |
| Ship | 已完成，已确认 |
| 基础设施 | 已完成，已确认 |

## 阶段 3：最终差距清单与硬性暂停

阶段 2 的 Meta、Define、Plan、Build、Verify、Review、Ship 和基础设施均已完成静态核实。下面是合并后的最终 provisional 清单；详细证据仍保留在各生命周期章节及基础设施章节中。每一行都是阶段 3 的独立决策单位，除非用户明确要求拆分或合并，否则不把相邻行的确认互相推导。

### 逐项最终清单

| 生命周期/面 | Target 条目或基础设施单元 | 暂定动作 | 优先级 | 当前状态 |
| --- | --- | --- | --- | --- |
| Meta | `using-agent-skills`（含 SessionStart/DoD 依赖） | 合并/协调重叠 | P1 | 已确认，阶段 4 已完成 |
| Define | `interview-me` | 新增/改写引入 | P1 | 已确认，阶段 4 已完成 |
| Define | `idea-refine` | 新增/改写引入 | P2 | 已确认，阶段 4 已完成 |
| Define | `spec-driven-development` | 合并/协调重叠 | P0 | 已确认，阶段 4 已完成（并入 `issue-workflow/spec-authoring`，commit `ec2cdac`） |
| Plan | `planning-and-task-breakdown` | 合并/协调重叠 | P0 | 已确认，阶段 4 已完成（补充 `Acceptance criteria` 与 `Verification` 的逐步区分，commit `89ed5fb`） |
| Build | `incremental-implementation` | 合并/协调重叠 | P0 | 已确认，阶段 4 已完成（合并到 `plan-work` 的 vertical-slice reference，commit `c1581f0`） |
| Build | `test-driven-development` | 跳过 | P1 | 已确认 |
| Build | `context-engineering` | 新增/改写引入 | P1 | 已确认，阶段 4 已完成（新增窄触发、默认只读的 context audit/setup Skill，commit `6d8e137`） |
| Build | `source-driven-development` | 跳过 | P0 | 已确认 |
| Build | `doubt-driven-development` | 合并/协调重叠 | P0 | 已确认，阶段 4 已完成（合并到 `agent-workflow` fresh-context reference，commit `ef133f7`） |
| Build | `frontend-ui-engineering` | 新增/改写引入 | P1 | 已确认，阶段 4 已完成（新增框架中立的 UI/a11y owner 与 skill-local checklist，commit `bdd87b6`） |
| Build | `api-and-interface-design` | 合并/协调重叠 | P0 | 已确认，阶段 4 已完成（并入 `design-codebase` 的 API/interface reference，commit `722e65f`） |
| Verify | `browser-testing-with-devtools` | 新增/改写引入 | P0 | 已确认，阶段 4 已完成（窄触发 browser-runtime evidence owner，commit `1f32856`） |
| Verify | `debugging-and-error-recovery` | 保留现状不动 | P0 | 已确认，阶段 4 独立核实为 no-op |
| Review | `code-review-and-quality` | 合并/协调重叠 | P0 | 已确认，阶段 4 已完成（合并可选 tests-first 与 structural-remedy lenses 到 `review-and-finish` template，commit `3df0e10`） |
| Review | `code-simplification` | 跳过 | P0 | 已确认 |
| Review | `security-and-hardening` | 新增/改写引入 | P0 | 已确认，阶段 4 已完成（窄触发、框架中立的安全分析 owner，commit `05cfbf2`） |
| Review | `performance-optimization` | 合并/协调重叠 | P1 | 已确认，阶段 4 已完成（窄范围、框架中立、先测量的性能实验 owner，commit `145eba9`） |
| Ship | `git-workflow-and-versioning` | 合并/协调重叠 | P0 | 已确认，阶段 4 已完成（将显式 commit 授权后的 commit-craft 合并到 `finish-branch`，commit `78afc84`） |
| Ship | `ci-cd-and-automation` | 新增/改写引入 | P0 | 已确认，阶段 4 已完成（新增窄范围 repository-owned pipeline-definition owner，commit `4647b11`） |
| Ship | `deprecation-and-migration` | 合并/协调重叠 | P0 | 已确认，阶段 4 已完成（将按需 deprecation reference 合并到 `plan-work`，commit `a329d9a`） |
| Ship | `documentation-and-adrs` | 合并/协调重叠 | P0 | 已确认，阶段 4 已完成（将 ADR convention/lifecycle lens 合并到 `design-codebase`，commit `ae0ba21`） |
| Ship | `observability-and-instrumentation` | 新增/改写引入 | P0 | 已确认，阶段 4 已完成（新增问题驱动、项目约定优先的 telemetry owner，commit `5882531`） |
| Ship | `shipping-and-launch` | 新增/改写引入 | P0 | 已确认，阶段 4 已完成（新增 concrete-release launch-readiness owner，commit `d689afb`） |
| Infrastructure/agents | `code-reviewer` persona | 跳过 | P0 | 已确认 |
| Infrastructure/agents | `security-auditor` persona | 合并/协调重叠 | P0 | 已确认，阶段 4 完成（条件式 trust-boundary prompts 合并到 `security-and-hardening`，commit `0ca2867`） |
| Infrastructure/agents | `test-engineer` persona | 跳过 | P0 | 已确认 |
| Infrastructure/agents | `web-performance-auditor` persona | 合并/协调重叠 | P0 | 已确认，阶段 4 完成（source/artifact web audit lens 合并到 `performance-optimization`，commit `ec08152`） |
| Infrastructure/orchestration | `orchestration-patterns` + `docs/agents.md`（命令文件不随之修改） | 合并/协调重叠 | P0 | 已确认，阶段 4 完成（host/persona relationship guidance 合并到 `agent-workflow`，commit `d5cafaf`） |
| Infrastructure/references | `accessibility-checklist` | 合并/协调重叠 | P1 | 已确认，阶段 4 完成（page-shell、键盘、表单和 motion prompts 合并到 UI reference，commit `97a9bdf`） |
| Infrastructure/references | `definition-of-done` | 保留现状不动 | P0 | 已确认 |
| Infrastructure/references | `observability-checklist` | 合并/协调重叠 | P0 | 已确认，阶段 4 完成（conditional signal prompts 合并到 `observability-and-instrumentation`，commit `3ff5ece`） |
| Infrastructure/references | `performance-checklist` | 合并/协调重叠 | P1 | 已确认，阶段 4 完成（条件式 performance prompt set 合并到 `performance-optimization`，commit `fa5ad2d`） |
| Infrastructure/references | `security-checklist` | 合并/协调重叠 | P0 | 已确认，阶段 4 完成（条件式 security prompt set 合并到 `security-and-hardening`，commit `68ccac7`） |
| Infrastructure/references | `testing-patterns` | 跳过 | P1 | 已确认 |
| Infrastructure/hooks | SessionStart meta injection（三文件） | 合并/协调重叠 | P1 | 已确认，阶段 4 no-op（当前 prompt 已覆盖 material assumptions 与 technical tradeoffs；未启用第二 SessionStart router） |
| Infrastructure/hooks | SDD WebFetch cache（三文件） | 跳过 | P0 | 已确认，阶段 4 按确认跳过（不缓存 prompt-shaped WebFetch 结果） |
| Infrastructure/hooks | simplify protected-block filter/restore（三文件） | 新增/改写引入 | P0 | 已确认，阶段 4 完成（current-owned `simplify-protected-blocks` plugin，commit `e147a4a`） |
| Infrastructure/evals | eval README 分层说明 | 合并/协调重叠 | P1 | 已确认，阶段 4 完成（current-owned `tests/eval-contract.md`，commit `332d71b`） |
| Infrastructure/evals | `run-evals.js` Tier 2/Tier 3 runner | 合并/协调重叠 | P0 | 已确认，阶段 4 完成（current-owned `tests/check_routing_contract.py`，commit `1b4065a`；Tier 3 保持未执行） |
| Infrastructure/evals | `run-evals-test.js` | 新增/改写引入 | P1 | 已确认，阶段 4 完成（current-owned `tests/test_eval_contract.py`，commit `37f5ef9`；与 validator/routing focused tests 分离） |
| Infrastructure/evals | `validate-skills.js` | 新增/改写引入 | P1 | 已确认，阶段 4 完成（current-owned `tests/validate_suite.py` 与 focused tests，commit `03db3b3`） |
| Infrastructure/evals | `skill-lint.js` | 新增/改写引入 | P1 | 已确认，阶段 4 完成（current-owned lint extensions in `tests/validate_suite.py`，commit `458d435`） |
| Infrastructure/eval corpus | 24 cases + 45 fixtures 维护资产 | 新增/改写引入 | P1 | 已确认，阶段 4 完成（current-owned corpus disposition in `tests/eval-contract.md`，commit `c4da121`；不复制完整 corpus） |
| Infrastructure/eval corpus | ownerless negative / stale-boundary 审计 | 合并/协调重叠 | P1 | 已确认，阶段 4 完成（ownership audit in `tests/eval-contract.md`，commit `153e9a7`） |
| Infrastructure/eval corpus | browser runtime capability gate | 跳过 | P1 | 已确认，阶段 4 保持跳过/`UNVERIFIED`（无授权 live browser/DevTools channel；未运行 target browser case） |
| Infrastructure/eval corpus | hidden patch/materialization 边界 | 保留现状不动 | P1 | 已确认，阶段 4 保留现状（不复制 patch/workspace materializer 或 temporary Git path） |
| Infrastructure/eval corpus | fixture realism / 窄 gate | 保留现状不动 | P2 | 已确认，阶段 4 保留现状（不把 fixture realism 扩展为 universal gate） |
| Infrastructure/eval delivery | results/CI 接入边界 | 新增/改写引入 | P2 | 已确认，阶段 4 完成（current-owned `tests/eval-contract.md` boundary retained；不创建 `evals/results` 或 CI gate） |
| Infrastructure/commands | `/spec`、`/plan`、`/planning` | 跳过 | P1 | 已确认，阶段 4 按确认跳过（current `issue-workflow`/`plan-work` ownership retained; no target commands copied） |
| Infrastructure/commands | `/build` | 跳过 | P0 | 已确认，阶段 4 按确认跳过（current base execution + `plan-work`/`test-strategy` ownership retained; no target autonomous build command） |
| Infrastructure/commands | `/test` | 跳过 | P1 | 已确认，阶段 4 按确认跳过（current `test-strategy` owns test design/TDD/evidence; no target command or universal test gate copied） |
| Infrastructure/commands | `/review`、`/code-simplify` | 跳过 | P0 | 已确认，阶段 4 按确认跳过（host `/code-review`/`/simplify` and current `review-and-finish`/plugin ownership retained） |
| Infrastructure/commands | `/ship` | 合并/协调重叠 | P0 | 已确认，阶段 4 完成（bounded host-command coordination in `shipping-and-launch` + non-trigger contract，commit `34d8ff2`） |
| Infrastructure/commands | `/webperf` | 跳过 | P2 | 已确认，阶段 4 按确认跳过（current `performance-optimization` owns explicit measure-first performance work; no target specialist command or fixed CWV gate copied） |
| Infrastructure/commands | `validate-commands.js` | 跳过 | P1 | 已确认，阶段 4 按确认跳过（current repository has no multi-tool command surface to validate; no target wrapper copied） |
| Infrastructure/distribution | 多工具扩展与根 README 定位 | 保留现状不动 | P0 | 已确认，阶段 4 保留现状（Claude Code 优先；Markdown/optional plugin boundaries remain explicit） |
| Infrastructure/distribution | Claude/plugin manifest | 合并/协调重叠 | P1 | 已确认，阶段 4 no-op/coordination（现有 self-contained plugin manifests 保持；不创建 root marketplace manifest） |
| Infrastructure/distribution | Codex 与 `.agents` manifests | 跳过 | P1 | 已确认，阶段 4 按确认跳过（不承诺 Codex host discovery/permissions；不复制 target manifests） |
| Infrastructure/distribution | Antigravity/Gemini 包装与命令面 | 跳过 | P1 | 已确认，阶段 4 按确认跳过（不承诺 host package/command discovery、permissions 或 runtime） |
| Infrastructure/docs | adoption/getting-started 与平台 setup docs | 保留现状不动 | P1 | 已确认，阶段 4 保留现状（current README/README.zh-CN and plugin-local docs remain source of truth） |
| Infrastructure/docs | contributor/anatomy/rule 基础设施 | 跳过 | P1 | 已确认 |
| Infrastructure/docs | 文档/manifest 声明的验证与 CI 门 | 保留现状不动 | P1 | 已确认 |
| Infrastructure/docs | `comparison.md` | 跳过 | P2 | 已确认 |
| Infrastructure/metadata | `.gitattributes`、`.gitignore` | 保留现状不动 | P2 | 已确认 |
| Infrastructure/attribution | LICENSE 与 manifest license metadata | 合并/协调重叠 | P0 | 已确认 |

### 阶段 3 的两个独立范围决策

1. **整体流程强度：** 是否保持当前“Start lightweight、按风险和证据缺口升级、避免固定仪式”的哲学，还是选择更接近 target 的全生命周期、普遍 checklist、更多 approval/reviewer/gate 的重流程方向。阶段 2 同时记录了两侧证据，主线程不替用户预选。
2. **多工具支持范围：** 是保持 Claude Code 优先并把 Markdown/插件能力作为有限扩展，还是选择少数明确宿主，或承诺广泛 Cursor/Codex/Gemini/Copilot/Antigravity/OpenCode/Windsurf 等支持。静态 setup docs、manifest 和缺失路径不能替代用户的产品取舍或各宿主 runtime 验证。

### 确认规则

- 用户可以按行批准、修改动作/优先级、拆分或合并决策单位，也可以明确跳过全部或部分条目。
- `P0` 只表示原样引入前必须消除直接冲突；`P1`/`P2` 表示价值或紧迫度较低，不表示自动延期或自动采用。
- 未明确批准的条目不得进入阶段 4。阶段 4 即使收到某个 Skill 的批准，也不得顺带吸收其 agents、references、commands、hooks、evals、manifest 或多工具文档。
- 实际 LICENSE 的 GNU AGPL v3 来源标准已经在阶段 0 决定；用户确认的是吸收范围和落点，不是把 manifest 的 MIT 元数据当作新的许可结论。

在用户逐项确认/调整前停止，不修改任何 runtime Skill、README、测试、target 文件或其他吸收目标。

## 阶段 4：按生命周期大类吸收改写（仅处理已批准条目）

同一生命周期大类中的已批准条目可以连续处理；每个条目仍须独立完成以下步骤并创建独立本地 commit：

1. 完整读取 target 对应 `SKILL.md` 及其实际依赖的 references/agents。
2. 完整读取本项目相近 Skill，作为文风和边界参照。
3. 根据阶段 3 已批准的职责决定落点：`skills/`、`workflows/`、`plugins/` 或纯参考目录。
4. 用本项目确认后的风格改写，不逐字复制，并检查全项目 description/触发条件的冲突。
5. 增加对应的路由/边界回归用例。
6. 同步 `README.md` 与 `README.zh-CN.md`。
7. 更新本文件中该条目的状态、证据、验证结果和 commit。
8. 完成聚焦验证后，仅提交该条目授权修改的文件。Commit message 需注明内容参考自 `addyosmani/agent-skills` (GNU AGPL v3) 的具体技能名称，并简述吸收的核心规则。**注意：该源项目仅作临时参考（后续将删除），请勿在 commit 中记录其本地路径或目录结构，以免误导未来维护者，仅聚焦记录具体改动内容即可**

### 预期执行顺序

具体条目必须以阶段 2 的实际差距分析和阶段 3 的用户批准为准：

1. Meta
2. Define
3. Plan
4. Build
5. Verify
6. Review（特别核对与宿主 `code-review`/`simplify` 的冲突）
7. Ship
8. 基础设施（agents、references、evals、commands/hooks；仅在落点和维护责任清楚时处理）

每个大类内可以连续完成全部获批条目，每个条目一个独立 commit；大类结束后更新汇总并统一向用户汇报、暂停。不得将预期顺序视为当前批准清单。

## 阶段 5：定期可靠性自查

每完成 2-3 个生命周期大类，使用 `reliability-check` 的方法核对：

- 是否真的读取了每个结论所引用的当前源文件，而不是依据 README、记忆或猜测；
- 是否在阶段 3 未批准的情况下改变了整体流程强度；既不默认维持轻量，也不默认增加验证门；
- `MIGRATION_PLAN.md` 是否与实际变更、测试和 Git 状态一致；
- 是否仍保留当前获批的宿主能力让位政策、权限边界、失败/停止条件和证据诚实性。

## 阶段 6：全仓库收尾一致性检查

仅在所有用户批准条目处理完后执行：

- 检查 README 的技能表、Capability Map、Repository Layout 和 Recommended Start；
- 检查 `README.md` 与 `README.zh-CN.md` 同步；
- 检查 `skills.sh.json` 是否需要分组更新；
- 检查 `tests/` 的路由/边界案例和 Skill description 是否冲突；
- 检查每项借鉴内容的来源记录（当前仓库是否已有 `CREDITS.md` 需届时核实）；
- 检查 Capability Boundaries 是否仍准确；
- 区分静态验证、仓库内执行验证和真实宿主/runtime 验证，不能互相替代。

阶段 6 检查完成后必须先更新本文件、汇报结果并暂停；未经用户确认，不直接进入阶段 7 归档。

## 阶段 7：归档与收尾

用户批准的条目全部完成并通过收尾检查后，将本文件精简为迁移记录，放入届时核实后合适的维护位置；保留已吸收、保留、跳过和延期 P2 项目的理由与证据。未经用户另行授权，不做远程发布、推送、合并、分支清理或删除 target 的操作。

## 批次进度

- Meta / `using-agent-skills`：已完成独立 source audit、窄合并改写、README/测试/来源记录同步和聚焦静态验证；未新增 runtime Skill、未启用 SessionStart hook、未执行 target hook/script/eval；独立本地 commit：`5f98042`。
- Meta / `using-agent-skills` changed files：`prompts/CLAUDE.fragment.md`、`README.md`、`README.zh-CN.md`、`tests/routing-contract.md`、`tests/trigger-matrix.md`、`tests/non-trigger-cases.md`、`CREDITS.md`、本文件。
- Define / `interview-me`：已完成独立 target/current source audit、current-owned Skill 改写、README/测试/来源记录同步和聚焦静态验证；未创建默认 intent 工件或自动 handoff；独立本地 commit：`aaeedb1`。
- Define / `interview-me` changed files：`skills/interview-me/SKILL.md`、`README.md`、`README.zh-CN.md`、`tests/routing-contract.md`、`tests/trigger-matrix.md`、`tests/non-trigger-cases.md`、`CREDITS.md`、本文件。
- Define / `idea-refine`：已完成独立 target/current source audit、current-owned Skill 改写、README/测试/来源记录同步和聚焦静态验证；未迁移初始化脚本或示例文档，未创建默认概念文件；独立本地 commit：`edfc886`。
- Define / `spec-driven-development`：已将结构化 spec 字段改写合并到 `skills/issue-workflow/SKILL.md` 的显式 `spec-authoring` 模式；未创建新 spec owner、默认 `SPEC.md`/`tasks/*`、自动 handoff 或 branch action。已补充架构词汇与自动命令执行的非触发案例；`git diff --check` 及关键 frontmatter、路由、边界、双语 README、测试和来源标记静态检查通过；独立本地 commit：`ec2cdac`。
- Build / `api-and-interface-design`：已将项目事实优先的消费者可观察 contract lens 合并到 `skills/design-codebase/references/api-and-interface-design.md`，并在 `design-codebase` references 中登记；未创建新 API owner、固定协议规范或自动迁移/发布动作。已补充 API contract 的正向路由及固定约定/自动副作用的非触发案例；`git diff --check`、相对引用和 13 项关键静态标记检查通过；独立本地 commit：`722e65f`。
- Plan / `planning-and-task-breakdown`：已在 `skills/plan-work/references/plan-template.md` 中补充每个步骤的 `Acceptance criteria` 与 `Verification` 分离；未创建第二个 Plan owner、默认 `tasks/*`、审批门或固定拆分阈值。已完成模板和相对范围的静态检查；独立本地 commit：`89ed5fb`。
- Build / `incremental-implementation`：已将 contract-first、risk-first、扩展前 acceptance/evidence 检查和窄而可回退的增量规则合并到 `skills/plan-work/references/vertical-slices.md`；未创建新 Build owner、自动 commit、固定阈值、全套命令或 feature-flag 门。已补充多文件但上下文已明确的非触发案例；`git diff --check` 与 10 项关键静态标记检查通过；独立本地 commit：`c1581f0`。
- Build / `doubt-driven-development`：已将去锚定 `ARTIFACT + CONTRACT` 输入包、adversarial mismatch framing、四类 reconcile 分类和 independence gap 规则合并到 `skills/agent-workflow/references/fresh-context-verification.md`；未创建新 doubt owner、普遍 fresh review、跨模型 CLI、自动 orchestrator 或 branch action。已补充跨模块但下一步明确时不自动启动 review loop 的非触发案例；`git diff --check` 与 14 项关键静态标记检查通过；独立本地 commit：`ef133f7`。
- Build / `context-engineering`：已新增窄触发、默认只读的 `skills/context-engineering/SKILL.md`，并同步双语 README、`skills.sh.json`、路由/正负触发合同和来源记录；未自动创建规则文件、执行命令、compact、MCP 或下游 handoff。`git diff --check`、frontmatter、catalog JSON、26 项关键静态标记和 target-rule 排除检查通过；独立本地 commit：`6d8e137`。
- Build / `frontend-ui-engineering`：已新增框架中立、窄触发的 `skills/frontend-ui-engineering/SKILL.md` 与 skill-local accessibility checklist，并同步双语 README、`skills.sh.json`、路由/正负触发合同和来源记录；未引入固定框架/断点、自动浏览器或 a11y 工具、架构/测试/完成 owner。`git diff --check`、frontmatter、相对引用、catalog JSON、双语 README/路由/触发合同和固定规则排除检查通过；独立本地 commit：`bdd87b6`。
- Verify / `browser-testing-with-devtools`：已完成窄触发、框架/工具中立的 browser-runtime evidence Skill 实现，并同步双语 README、`skills.sh.json`、路由/正负触发合同和来源记录；未安装/配置浏览器工具、启动服务器、执行浏览器/网络/依赖动作或取得 live runtime 证据。`git diff --check`、frontmatter、catalog JSON、路由/正负触发合同、来源记录、固定规则排除和独立静态审查通过；独立本地 commit：`1f32856`。
- Verify / `debugging-and-error-recovery`：已独立核实为 no-op；保留 `debug-systematically` 作为唯一项目调试 owner，未创建第二 debug owner、未修改 runtime Skill、未创建空 commit。
- Review / `code-review-and-quality`：已将可选的 tests-first context reading 与 structural-remedy lens 合并到现有 `skills/review-and-finish/references/review-template.md`，未新增第二 Review owner、宿主 `/code-review` 替代路径、command、persona、hook、自动修复或 branch action。`git diff --check`、template marker、双语 README、非触发合同、GNU AGPL v3 来源和 changed-path scope 检查通过；独立本地 commit：`3df0e10`。
- Review / `security-and-hardening`：已完成窄触发、框架中立的安全分析 owner 及其 README、catalog、路由/正负触发合同和来源记录改写；未执行 exploit、依赖安装、网络/外部服务、脚本、凭据、分支或其他外部动作。`git diff --check`、frontmatter、25 项 Skill marker、catalog JSON、双语文档、路由/正负触发合同、来源记录、handoff 修正和 changed-path scope 检查通过；独立本地 commit：`05cfbf2`。
- Review / `performance-optimization`：已完成窄范围、框架中立、先测量的性能实验 owner 实现，并同步 `skills.sh.json`、双语 README、路由/正负触发合同和来源记录；未执行 benchmark、profiling、Lighthouse、CrUX、RUM/monitoring、工具安装、网络/外部服务、代码/配置修复或分支动作。`git diff --check`、frontmatter、catalog JSON、双语 README、路由/正负触发合同、来源记录、performance exclusions 和 changed-path scope 检查通过；独立本地 commit：`145eba9`。
- Ship / `git-workflow-and-versioning`：已将显式 commit 授权后的逻辑原子、独立可审阅范围、相关证据和解释 why 的消息 craft 合并到 `finish-branch`，并补充 finish-branch 行为合同；未引入 Always 触发、自动 commit、固定门禁、reset/cleanup、tag push 或其他 branch action。`git diff --check`、finish-branch markers、行为合同、GNU AGPL v3 来源和 changed-path scope 检查通过；独立本地 commit：`78afc84`。
- Ship / `ci-cd-and-automation`：已新增窄范围、框架中立的 repository-owned pipeline-definition owner，并同步 catalog、双语 README、路由/正负触发合同和来源记录；未运行 hosted workflow、修改远程策略、访问凭据、安装依赖、部署、rollback 或执行 Git 动作。`git diff --check`、frontmatter、catalog JSON、双语 README、路由/正负触发合同、来源记录、CI exclusions 和 changed-path scope 检查通过；独立本地 commit：`4647b11`。
- Ship / `deprecation-and-migration`：已将 consumer inventory、replacement/no-replacement、通知/兼容窗口、exception owner、usage-gated removal 和有前提的 expand/contract 规则并入 `plan-work` reference，并同步路由/正负触发合同和来源记录；未创建第二 migration owner、执行 migration/backfill/down/drop、通知、部署或分支动作。`git diff --check`、frontmatter、relative reference、路由/正负触发合同、来源记录、deprecation exclusions 和 changed-path scope 检查通过；独立本地 commit：`a329d9a`。
- Ship / `documentation-and-adrs`：已将 ADR convention discovery、冲突暴露、用户同意、status 和 successor/supersession 历史规则合并到 `design-codebase` 的 domain-modeling reference，并同步路由/正负触发合同和来源记录；未新增 documentation owner、自动创建路径、默认落盘、删除历史或发布动作。`git diff --check`、relative reference、ADR markers、路由/正负触发合同、来源记录、documentation exclusions 和 changed-path scope 检查通过；独立本地 commit：`ae0ba21`。
- Ship / `observability-and-instrumentation`：已新增问题驱动、项目约定优先的 telemetry owner，并同步 catalog、双语 README、路由/正负触发合同和来源记录；未执行 dashboard/alert publication、监控配置、网络、依赖安装、test traffic、failure injection、production access、部署或 Git 动作。`git diff --check`、frontmatter、catalog JSON、双语 README、路由/正负触发合同、来源记录、observability exclusions 和 changed-path scope 检查通过；独立本地 commit：`5882531`。
- Ship / `shipping-and-launch`：已新增只针对 concrete production release 的 launch-readiness owner，并同步 catalog、双语 README、路由/正负触发合同和来源记录；未执行 deploy、publish、flag、migration、rollback、monitoring、traffic、notification、credential、secret 或 Git 动作。`git diff --check`、frontmatter、catalog JSON、双语 README、路由/正负触发合同、来源记录、shipping exclusions 和 changed-path scope 检查通过；独立本地 commit：`d689afb`。
- Infrastructure / `security-auditor`：已将 target persona 的条件式 trust-boundary prompts 合并到现有 `security-and-hardening` owner，并保留单一安全分析责任；未保留独立 persona、固定 OWASP/STRIDE gate、PoC、命令、hook、eval、exploit、依赖安装或分支动作。`git diff --check`、owner/negative-contract markers、GNU AGPL source marker 和 changed-path scope 检查通过；独立本地 commit：`0ca2867`。
- Infrastructure / `security-checklist`：已将 target reference 改写为 `security-and-hardening` 内的条件式 threat/access/integration/data/dependency/evidence prompt set；未引入 universal OWASP/STRIDE、固定阈值、secret-scanning/install/audit 命令、pre-commit/release gate 或自动修复。`git diff --check`、conditional-reference markers、GNU AGPL source marker 和 changed-path scope 检查通过；独立本地 commit：`68ccac7`。
- Infrastructure / `web-performance-auditor`：已将 target 的 Quick/Deep、source-only `potential impact`、artifact source labeling、framework/rendering identification 与窄 web lens 改写并合并到 `performance-optimization`；未保留固定 CWV/预算/样本 gate、Lighthouse/CrUX/RUM 命令、工具安装、live capture、监控、修复或分支动作。`git diff --check`、web-audit markers、正负触发合同、GNU AGPL source marker 和 changed-path scope 检查通过；独立本地 commit：`ec08152`。
- Infrastructure / `performance-checklist`：已将 target reference 改写为 `performance-optimization` 内的条件式 loading/resource、rendering/input、data/backend、correctness/evidence prompt set；未引入固定 CWV/响应/包大小阈值、命令、profiling、安装、生产负载、RUM、release gate 或分支动作。`git diff --check`、conditional-checklist markers、negative-contract marker、GNU AGPL source marker 和 changed-path scope 检查通过；独立本地 commit：`fa5ad2d`。
- Infrastructure / `orchestration-patterns` + `docs/agents.md`：已将 direct-owner、no-router/no-persona-chain、host-capability reuse、subagent/team distinction 与 observed-support evidence 合并到 `agent-workflow`；未吸收 target-specific command wiring、固定 `/ship` fan-out、Agent Teams setup、manifest discovery claims 或第二 orchestration owner。`git diff --check`、host/persona markers、negative-contract markers、GNU AGPL source marker 和 changed-path scope 检查通过；独立本地 commit：`d5cafaf`。
- Infrastructure / `accessibility-checklist`：已将 target 中的 page-shell/skip path、自然键盘顺序、autocomplete/error focus、motion pause 与 text-size prompts 合并到现有 UI accessibility reference；未引入固定 WCAG/浏览器/axe gate、自动工具执行、第二 UI owner 或全局 checklist。`git diff --check`、accessibility markers、GNU AGPL source marker 和 changed-path scope 检查通过；独立本地 commit：`97a9bdf`。
- Infrastructure / `observability-checklist`：已将 target 中 conditional log/correlation、metric distribution/queue、trace propagation 与 symptom-based alert/dashboard prompts 合并到 `observability-and-instrumentation`；未引入 universal RED/USE/full-trace、固定阈值、vendor setup、dashboard/alert publication、test traffic、failure injection、production access 或 launch gate。`git diff --check`、conditional-signal markers、GNU AGPL source marker 和 changed-path scope 检查通过；独立本地 commit：`3ff5ece`。
- Infrastructure / SessionStart meta injection：已核对 target hook 与当前 prompt；material assumptions、technical tradeoffs、source/evidence 和 action-specific boundaries 已由现有 always-on prompt/Skills 覆盖，因此保持 no-op，不启用第二全局 router，也未执行 target hook。无实现 commit。
- Infrastructure / SDD WebFetch cache：按确认跳过；target 缓存 prompt-shaped、URL-keyed 内容并引入 curl/jq、ETag/HTTP、持久 cache 与 network side effects，不能证明当前问题获得 exact current source。未复制、注册或执行 target hook。无实现 commit。
- Infrastructure / simplify protected-block hook：已新增显式 opt-in 的 `plugins/simplify-protected-blocks`，使用标准库 Python 实现 project-root/symlink 边界、bounded backup/restore、Read/Edit|Write/Stop hook wiring 与 fail-open payload handling；同步双语 README、非触发合同、CREDITS 和 plugin-local tests。未执行 target hook、未改变 host `/code-simplify`、未引入 shell/jq/network/外部路径或自动安装。`git diff --check`、Python AST/JSON、3 个 plugin-local unit tests、临时目录 backup/update/restore lifecycle、README/contract/source markers 和 changed-path scope 检查通过；独立本地 commit：`e147a4a`。
- Infrastructure/evals / eval README：已将 target 的三层证据、case ownership、runtime/fixture 不可替代性和失败状态改写为 current-owned `tests/eval-contract.md`；未复制第二 routing layer、固定 rank/similarity gate、headless executor、browser/network/CI 或持久结果层。`git diff --check`、Markdown/source markers 和 changed-path scope 检查通过；独立本地 commit：`332d71b`。
- Infrastructure/evals / validate-skills：已将 target 的结构 wrapper 改写为 current-owned `tests/validate_suite.py`，检查 Skill 目录/frontmatter、presentation-only catalog references、维护合同路径和本地 Markdown links；`idea-refine`、`interview-me` 的已知未分组状态保留为 warning，不引入 target required sections、trigger regex、固定 gate 或插件/宿主 runtime claim。`python tests/validate_suite.py`、3 个 focused unit tests、`git diff --check` 和 changed-path scope 检查通过；独立本地 commit：`03db3b3`。
- Infrastructure/evals / run-evals Tier 2：已将 target 的静态 routing/collision 形状改写为 current-owned `tests/check_routing_contract.py`，核对已安装 owner、README/contract coverage 和 owner-like stale tokens；lexical overlap 仅作 informational output，不引入 rank/similarity floor 或自动 gate。Tier 3 headless Claude、fixture Git workspace、browser/network、external grader 和 `evals/results` 保持未执行/未创建。`python tests/check_routing_contract.py`、3 个 focused unit tests、`git diff --check` 和 changed-path scope 检查通过；独立本地 commit：`1b4065a`。
- Infrastructure/evals / skill-lint：已将 target 的可迁移结构规则收窄为目录 slug、frontmatter、非空 Skill body 与本地 Markdown link 检查，保留 current frontmatter/trigger/body 自主性；未复制 target required sections、固定 trigger regex、exemption 表或 universal gate。`python tests/validate_suite.py`、4 个 focused unit tests 和 `git diff --check` 通过；独立本地 commit：`458d435`。
- Infrastructure/evals / run-evals-test：已将 target 的 case/schema/fixture regression 形状收窄为 `tests/test_eval_contract.py` 的两个 current-owned deterministic contract tests，并复用 validator/routing focused tests；未创建临时 Git workspace、patch materializer、headless executor、browser/network runner、rank floor 或 external grader。`python tests/test_eval_contract.py`、validator/routing tests 和 `git diff --check` 通过；独立本地 commit：`37f5ef9`。
- Infrastructure/eval corpus / 24 cases + 45 fixtures：已把 target corpus 保留为比较证据，维护面仅记录 deterministic structure/routing、owner availability、runtime evidence 和 explicit `UNVERIFIED` 边界；未复制 prompt-shaped corpus、fixtures、fixture Git workflow 或 results layer。`tests/eval-contract.md`、contract tests、`git diff --check` 和 changed-path scope 检查通过；独立本地 commit：`c4da121`。
- Infrastructure/eval corpus / ownerless negative / stale-boundary audit：已明确 pairwise owner claim、ownerless out-of-catalog、stale owner-like token 和 unavailable runtime capability 的分离；未为通过率强配 owner，也未把 fixture/path/expected output 当作权限或 ownership 证据。`tests/test_eval_contract.py`、routing checks、`git diff --check` 和 changed-path scope 检查通过；独立本地 commit：`153e9a7`。
- Infrastructure/eval corpus / browser runtime capability gate：保持跳过并标记 `UNVERIFIED`；未配置或授权 live browser/DevTools channel，未执行 target browser case、network、screenshot、DOM 或 console observation，也未把静态 fixture 当作 runtime 证据。仅提交本条 ledger 记录，无实现 commit。
- Infrastructure/eval corpus / hidden patch/materialization：保持现状不动；不复制 target 的 patch application、fixture-to-workspace materialization、temporary Git baseline 或 cleanup behavior，也不把静态 patch shape 当作 live executor evidence。仅提交本条 ledger 记录，无实现 commit。
- Infrastructure/eval corpus / fixture realism：保持窄 gate 和现状不动；不复制 target fixture completeness/realism 作为普遍门槛，也不把 fixture 存在性、路径或内容当作 runtime behavior evidence。仅提交本条 ledger 记录，无实现 commit。
- Infrastructure/eval delivery / results and CI：沿用 current-owned `tests/eval-contract.md` 的 delivery boundary；不创建 `evals/results`、hosted CI status、deployment gate、external grader output 或 publication path，也不把 local static pass 变成 release authorization。仅提交本条 ledger 记录，无实现 commit。
- Infrastructure/commands / `/ship`：已将 target command 的有效 host-controller/merge 形状收窄合并到 `shipping-and-launch`，要求 `agent-workflow` fit check 后才可能协调真正独立 slices；未复制固定三 persona fan-out、顺序伪 parallel、rollback/deploy/Git actions 或第二 orchestration owner。`git diff --check`、shipping/non-trigger markers 和 changed-path scope 检查通过；独立本地 commit：`34d8ff2`。
- Infrastructure/commands / `/spec`、`/plan`、`/planning`：按确认跳过；当前 `issue-workflow` 的 chat-first `spec-authoring` 和 `plan-work` 已覆盖所需 owner，不复制 target command files、默认 `SPEC.md`/`tasks/*` persistence、自动 handoff 或 command execution。仅提交本条 ledger 记录，无实现 commit。
- Infrastructure/commands / `/build`：按确认跳过；当前 base execution、`plan-work` 和 `test-strategy` 已覆盖 settled implementation、planning 和 test-design boundaries，不复制 target autonomous build command、automatic full-plan execution、per-task commit 或 downstream handoff。仅提交本条 ledger 记录，无实现 commit。
- Infrastructure/commands / `/test`：按确认跳过；current `test-strategy` 已覆盖 test design、TDD mode、fixtures、timing 和 acceptance evidence，不复制 target `/test` command、browser escalation wording、universal test pyramid/coverage gate 或 command execution。仅提交本条 ledger 记录，无实现 commit。
- Infrastructure/commands / `/review`、`/code-simplify`：按确认跳过；host `/code-review`、`/simplify`、current `review-and-finish` 和 the explicit opt-in simplify plugin retain their ownership; 不复制 target review/simplify command、second review owner、automatic cleanup 或 branch action。仅提交本条 ledger 记录，无实现 commit。
- Infrastructure/commands / `/webperf`：按确认跳过；current `performance-optimization` 已覆盖显式 measure-first performance claims 和 source-only/artifact-backed honesty，不复制 target specialist command、fixed Web Vitals gate、DevTools/Lighthouse setup 或 automatic profiling. 仅提交本条 ledger 记录，无实现 commit。
- Infrastructure/commands / `validate-commands.js`：按确认跳过；当前仓库没有待验证的多工具 command surface，且 manifest/README 不证明其他宿主的 discovery、permission 或 command behavior；不复制 target cross-tool command parity wrapper，也不运行 target validator。仅提交本条 ledger 记录，无实现 commit。
- Infrastructure/distribution / multi-tool scope + root README：保留 current Claude Code-first positioning、plain-Markdown portability 和 optional self-contained plugin boundary；未复制 target marketplace identity、multi-host setup claims、root command surface 或 broad host support. 仅提交本条 ledger 记录，无实现 commit。
- Infrastructure/distribution / Claude/plugin manifest：现有 `capability-harness` 与 `simplify-protected-blocks` manifests 已是 current-owned self-contained plugin boundaries；不创建 target-style root manifest、marketplace identity、broad skill/agent/command discovery claim 或新的 plugin precedence。仅提交本条 ledger 记录，无实现 commit。
- Infrastructure/distribution / Codex 与 `.agents` manifests：按确认跳过；target manifest/static setup text 不证明 Codex host discovery、permission、command/hook support 或 runtime behavior，当前不增加 `.codex-plugin`/`.agents` surface。仅提交本条 ledger 记录，无实现 commit。
- Infrastructure/distribution / Antigravity/Gemini wrappers + commands：按确认跳过；target setup docs/commands 不证明这些宿主的 package discovery、permission、hook/command precedence 或 runtime behavior，当前不增加 wrappers 或 command surfaces。仅提交本条 ledger 记录，无实现 commit。
- Infrastructure/docs / adoption/getting-started + platform setup docs：保留 current README/README.zh-CN、plugin-local README 和 workflow docs；未复制 target full-lifecycle onboarding, host-specific setup claims, install commands, marketplace/network steps 或 additional runtime surfaces。仅提交本条 ledger 记录，无实现 commit。
- 当前批次未吸收其他 Define/Build 条目或任何未获本条目授权的 agents、references、commands、hooks、evals、manifest 或多工具文档。

## 当前暂停点

阶段 3 的逐项动作和两个范围决策已获用户确认；阶段 4 的 Define 第二批已完成，Plan + Build 批次已完成获批的 Plan/Build 条目：`api-and-interface-design` 独立提交为 `722e65f`，`planning-and-task-breakdown` 独立提交为 `89ed5fb`，`incremental-implementation` 独立提交为 `c1581f0`，`doubt-driven-development` 独立提交为 `ef133f7`，`context-engineering` 独立提交为 `6d8e137`，`frontend-ui-engineering` 独立提交为 `bdd87b6`。`test-driven-development` 和 `source-driven-development` 按确认跳过；Verify 批次已完成：`browser-testing-with-devtools` 独立提交为 `1f32856`，`debugging-and-error-recovery` 已独立核实为 no-op，未创建第二个 debug owner 或空 commit。Review 批次已完成：`code-review-and-quality` 独立提交为 `3df0e10`；`code-simplification` 按确认跳过；`security-and-hardening` 独立提交为 `05cfbf2`；`performance-optimization` 独立提交为 `145eba9`。Ship 批次已完成：`git-workflow-and-versioning` 独立提交为 `78afc84`；`ci-cd-and-automation` 独立提交为 `4647b11`；`deprecation-and-migration` 独立提交为 `a329d9a`；`documentation-and-adrs` 独立提交为 `ae0ba21`；`observability-and-instrumentation` 独立提交为 `5882531`；`shipping-and-launch` 独立提交为 `d689afb`。未执行 push、merge、PR、部署、target 删除、hook/eval/CI/浏览器或外部服务动作。当前暂停于 Infrastructure/agents、orchestration、references 批次完成，hooks、evals、commands、distribution、docs 等未处理范围之前，不自动进入下一批次。
