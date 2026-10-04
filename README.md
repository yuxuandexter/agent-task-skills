# Agent Task Skills

把自然语言需求交清楚，再让 agent 在明确范围内执行、迭代并交付可检查的证据。

这是两个面向 Codex 的轻量 Skills，适用于研究、工程和需要证据的知识工作。当前是 **v0.1 初始实践**；来源与设计取舍见 [design-sources.md](docs/design-sources.md)，验证范围见 [validation.md](docs/validation.md)。

## 两个 Skills

| Skill | 用途 | 交付 |
| --- | --- | --- |
| [`frame-agent-task`](skills/frame-agent-task/SKILL.md) | 从自由描述和已有上下文整理目标、验收证据、边界和推进方式 | 以简短交付预览开头的任务说明，让用户在执行前看清将收到什么及其证据 |
| [`execute-agent-task`](skills/execute-agent-task/SKILL.md) | 执行明确且已获授权的任务，根据证据迭代，逐项验证完成条件 | 可查看的任务目录，以及结果、证据位置、限制和待判断事项 |

可以在同一段对话中顺序使用，也可以独立使用。执行 Skill 接受任何来源的清晰任务说明，不依赖另一个 Skill 已安装。

## 怎么用

需求还需要澄清时：

```text
用 $frame-agent-task 帮我把这个任务交清楚：
我想判断某个优化方案是否值得继续投入。
先整理目标、验收证据和边界，暂不执行。
```

准备执行时：

```text
用 $execute-agent-task 按上面的任务说明执行。
在已授权范围内根据结果选择下一步，最后逐项提供验证证据。
```

也可以一开始明确衔接：

```text
先用 $frame-agent-task 整理下面的任务。
只有影响方向、验收、重要成本或权限的问题才问我。
条件清楚后，用 $execute-agent-task 在我已经授权的范围内继续执行。
```

简短且明确的请求可以直接处理。已有授权会被沿用；实际工作区的 preview、写入、commit、push 或发布边界仍然有效。研究任务允许有依据的否定结果；代码运行、测试通过和研究结论成立分别需要相应证据。

更多使用例子见 [examples.md](docs/examples.md)。

## 跨 agent 启动消息

把下面这段消息和任务描述发给能读取仓库文件的 agent。无需依赖特定产品的调用符号。当前仓库已公开，无需私有仓库授权；agent 仍需具备读取链接或本地文件的能力。

```text
请读取并使用这个仓库中的两个 Skill 及其引用文件：
https://github.com/yuxuandexter/agent-task-skills
- skills/frame-agent-task/SKILL.md
- skills/execute-agent-task/SKILL.md

先整理目标、验收和边界，给我简短的交付预览。
只有影响方向、验收、重要成本或权限的问题才问我。
明确后，在我的授权范围内继续执行、验证，并按 Skill 规则在任务项目的 tasks/ 中记录进度。
遵守当前项目规则和工具权限。无法读取 Skill 时请明确说明，不要假装已加载。

我的任务：【在这里描述任务】
```

只想讨论时，将“明确后……”一句改为“本次只整理任务，等我确认后再执行”。不支持文件写入或执行工具的环境，只能完成其实际能力范围内的部分。

## 查看 agent 正在做什么

多步骤执行默认在正在处理的项目中维护任务目录；已有项目约定时沿用它。默认结构为：

```text
tasks/<task-slug>/
  README.md       # 目标、交付预览、当前阶段、下一步、待决定事项和验收证据
  work-log.md     # 实际操作、关键命令、结果、证据位置及必要的恢复说明
```

Agent 开始执行时给出任务路径，在重要阶段变化、结果、阻塞和交接时更新。你通常只需打开任务首页，必要时再查工作记录。最后更新时间表示最近一次记录，不保证进程仍在运行；这是可检查的执行记录，不是后台监控服务。

仅整理任务时不自动建目录。只读请求、限定写入范围、禁止保存和项目审批规则仍有效；无法保存时，agent 会说明并在聊天中保留等价摘要。不会创建全局 Todo、强制 lessons 文件或复制一套已有项目任务系统。

本仓库的实际使用记录见 [可查看的任务执行记录](tasks/visible-task-records/README.md)。随 Skill 分发的规则和模板见 [task-records.md](skills/execute-agent-task/references/task-records.md)。

## 安装

可在 Codex 中请求：

```text
用 skill-installer 从 GitHub 仓库 yuxuandexter/agent-task-skills 安装：
- skills/frame-agent-task
- skills/execute-agent-task
```

私有仓库需要当前环境有访问权限。也可以把两个完整 Skill 目录分别放进 Codex 的用户 Skill 目录：通常为 `$CODEX_HOME/skills`，未设置时为 `~/.codex/skills`。已有同名目录时先比较内容，不要直接覆盖。

每个目录都包含自己的 `SKILL.md`、`agents/openai.yaml` 和 `references/task-contract.md`；执行 Skill 另带 `references/task-records.md`，用于创建和恢复任务记录。两者保留正常自动匹配能力，也支持显式 `$skill-name` 调用。安装本仓库不会提供后台执行、调度、持久 Goal、预算强制执行或外部服务权限；这些能力由宿主及用户授权决定。

## 共享交接约定

唯一维护源是 [`shared/task-contract.md`](shared/task-contract.md)。它定义目的、目标、验收与证据、上下文、范围、推进方式、预算与停止、交付的含义，允许用普通文字表达。

其中的 Communication 约定借鉴 ASD-STE100 和 Google 技术写作原则：沿用用户语言，先呈现结果或待决定问题，保持术语一致，并把证据状态说清楚。简化表达时保留条件、例外和不确定性；不要求改成英文，不声称严格符合 ASD-STE100。规则应用于任务说明、进度、交接与最终报告，尊重用户对具体产物的格式和风格要求。

为了让每个 Skill 可以独立安装，仓库将这份约定打包进两个 Skill 的 `references/`。修改维护源后运行：

```bash
python3 scripts/sync_contract.py
python3 scripts/sync_contract.py --check
python3 -B -m unittest discover -s tests -p 'test_*.py' -v
```

打包脚本只需要 Python 标准库，执行 Skill 时无需运行。维护者还应使用 Codex `skill-creator` 自带的 `quick_validate.py` 检查两个 Skill，并按 [behavioral-cases.md](tests/behavioral-cases.md) 进行适当的行为验证。结构检查不等于行为可靠性证明。

## 目录

```text
skills/
  frame-agent-task/
  execute-agent-task/
shared/task-contract.md
scripts/sync_contract.py
docs/
  design-sources.md
  examples.md
  validation.md
tasks/
  visible-task-records/
tests/
  behavioral-cases.md
  fixtures/
```

研究来源用于指导本仓库的独立撰写；没有把外部框架的完整流程或代码复制为依赖。具体取舍和来源日期在设计说明中保留。
