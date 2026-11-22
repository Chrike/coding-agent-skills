$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$today = Get-Date -Format 'yyyy-MM-dd'
$context = @(
    "当前日期是 $today。"
    '先判断哪个未知事实会改变当前决定，再选择最小的核查动作。'
    '涉及库版本、API、报错排查、开源项目或方案选型时，先派 capability-harness:research-scout 核查。'
    '训练数据早于当前日期；仅固定不变的基础常识可直接回答。'
    '本地代码、配置或历史决定答案时，先用 Read、Grep、Glob 或 LSP 检查。'
    '需要当前公开资料时，给 research-scout 一个边界清楚的问题，不要把私密内容放进查询。'
    '需要独立比较时再派 capability-harness:skeptical-evaluator；需要可观察事实时再派 capability-harness:execution-verifier。'
    '复杂任务可使用 /capability-harness:deep：调研、方案、实现、实测，再按需独立挑刺。'
    '同一子代理返回 Blocked 最多补派一次；宿主权限和用户边界始终优先。'
) -join "`n"

$output = @{
    hookSpecificOutput = @{
        hookEventName = 'SessionStart'
        additionalContext = $context
    }
} | ConvertTo-Json -Compress -Depth 4
[Console]::Out.Write($output)
