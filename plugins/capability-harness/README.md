# Capability Harness

一个项目范围的 Claude Code 插件：在实质工作前帮助主控判断是否需要当前证据、局部代码核查、可观察验证或独立评估。它不替代领域 Skill、宿主权限或用户已选择的工作流。

## Install

从仓库根目录执行：

```powershell
claude plugin marketplace add . --scope local
claude plugin install capability-harness@coding-agent-skills --scope local
```

现有会话安装后执行 `/reload-plugins`，或启动新会话。一次性验证可使用：

```powershell
claude --plugin-dir .\plugins\capability-harness
```

插件只修改当前项目范围的安装，不修改用户全局配置。

## Runtime behavior

`SessionStart` 在 startup、resume、compact 时注入当天日期和中文路由卡。`PreToolUse` 仅对 research-scout 的 Bash 限制为只读 `gh`/`git` 命令；守卫只约束请求形式、不判断仓库可见性，私有仓库须由主控在任务中明确授权；GH 查询拒绝 `--jq`/`-q` 和 `--template`/`-t` 输出过滤器，避免表达式读取进程环境；`gh api` 仅接受相对 GitHub API endpoint，拒绝绝对 URL 与 `//host`，避免请求本机或内网服务；含 `--web`/`-w` 的浏览器开关及单横线组合/附值短选项也会拒绝；Git 检查必须关闭 fsmonitor、pager、外部 diff、textconv 和可选锁写入，并拒绝 `diff --no-index`、带 `--` 路径分隔符及两个位置参数的 diff，避免读取仓库外路径。它也在 `SubagentHandback` 收到报告时检查非空结构；通过的 Bash 调用仍交给宿主权限流。该 hook 使用 `onFailure: block`：脚本启动失败或超时时，所有匹配的 Bash/Handback 调用都会 fail-closed，而不只 research-scout 的命令。research-scout 禁用独立的 PowerShell、Monitor 和委派工具；MCP 工具的只读边界由角色指令与工具自身权限约束，PreToolUse 不硬拦截其副作用。`SubagentStop` 只读取文档提供的 `last_assistant_message`；Handback 正文在对应的 `PreToolUse` 阶段处理。

不设置 Edit/Write 的无状态“先调研”硬拦截：PreToolUse 事件不携带本轮工具历史，提示钩子也不能读取完整对话，因此无法可靠判断是否已核查。主 Skill 仍要求按需检查本地依据。

保留的代理是：

- `capability-harness:research-scout` — 当前资料、代码事实和外部公开证据；
- `capability-harness:execution-verifier` — 一条边界清楚的可观察检查；
- `capability-harness:skeptical-evaluator` — 对实际候选或结果做独立挑刺。

直接、低风险任务不需要调用代理。复杂任务可显式使用 `/capability-harness:deep`。同一代理返回 Blocked 最多补派一次。

## Local validation

```powershell
claude plugin validate .\plugins\capability-harness --strict
$env:PYTHONDONTWRITEBYTECODE = "1"
python -B -m unittest discover -s .\plugins\capability-harness\tests -v
```

SessionStart 使用 Windows 自带的 PowerShell 输出动态路由卡，不依赖 Python 启动器。PreToolUse 的只读 Bash 守卫需要 `PATH` 中名为 `python` 的 Python 3.9+ 启动器，并要求 Claude Code v2.1.295+ 支持 `onFailure: block`；旧版上不要授予 research-scout Bash。宿主权限、用户授权和安全策略始终优先。
