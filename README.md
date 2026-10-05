# Agent Task Skills

先讨论并确认目标，再由你启动执行。Agent 交付可检查的结果和证据。

这是两个面向 Codex、也可供其他能读取文件的 agent 使用的轻量 Skills，适用于研究、工程和需要证据的知识工作。当前是 **v0.2 初始实践**；来源与设计取舍见 [design-sources.md](docs/design-sources.md)，实际验证范围见 [validation.md](docs/validation.md)。

## 两个 Skills

| Skill | 用途 | 本轮交付与停止点 |
| --- | --- | --- |
| [`frame-agent-task`](skills/frame-agent-task/SKILL.md) | 讨论目的、目标、验收、边界和必要文档 | 简短的最终交付预览、目标文档或草稿、可复制的 Goal message；然后停止 |
| [`execute-agent-task`](skills/execute-agent-task/SKILL.md) | 收到你明确的启动或恢复指令后，依据确认的目标执行与验证 | 当前进度、实际工作记录、结果与验收证据 |

两者不自动串联。确认目标内容、保存 `goal.md` 或标记“ready”都不等于启动执行。Execute 可以读取其他流程准备的等价目标文档，不依赖 frame 已安装。开始后，范围内的普通步骤无需反复确认。

## 怎么用

先讨论和准备：

```text
用 $frame-agent-task 和我讨论这个任务：
我想判断某个优化方案是否值得继续投入。
先简洁预览最后会交付什么，再讨论 goal.md 和需要准备的文档。
内容确定后，在已授权范围内保存文档，并给我可复制的 Goal message。
本轮到交接为止，不执行任务，不激活 Goal。
```

Frame 会把具体结果、核心验收证据、重要约束和实际文档位置写入 Goal message。关键选择尚未确定时，文档和消息均标为草稿。你检查这些内容后，再决定何时启动。

随后明确开始：

```text
现在用 $execute-agent-task 按已确认的 tasks/<task-slug>/goal.md 开始执行。
核对目标文档、这条消息和可读取的宿主 Goal；有实质冲突先指出。
在约定范围内持续迭代，更新任务记录，最后逐项提供验收证据。
```

将示例路径换成实际文件。**Codex 的 `/goal` 文本也会作为首条任务指令，可能立即开始工作。** 因此，等你准备执行时，再提交包含 execute 指令的完整 Goal message。不假定“设置 Goal”之后还会等待另一条消息。只有宿主确实把保存目标和开始执行分开时，才分别操作。参见 [OpenAI 的长任务说明](https://learn.chatgpt.com/docs/long-running-work)。

无需持久 Goal 的环境，也可以用已确认的目标文档和明确的启动消息执行普通任务。Skill 本身不提供后台运行。更多例子见 [examples.md](docs/examples.md)。

## 跨 agent 启动消息

将第一段发给能读取仓库的 agent，并填写任务。该公开仓库无需私有仓库授权；agent 仍需具备读取链接或本地文件的能力。

**讨论阶段：**

```text
请读取并使用这个公开仓库的 skills/frame-agent-task/SKILL.md 及其引用文件：
https://github.com/yuxuandexter/agent-task-skills

和我讨论目标、验收与边界，先简短预览最终交付。
讨论所需文档，内容确定后在授权范围内准备 goal.md，并给我对应的 Goal message。
本轮交接后停止；不执行任务，不激活 Goal。
遵守当前项目规则。无法读取 Skill 时请说明，不要假装已加载。
我的任务：【描述任务】
```

**你确认目标后，再发送执行消息：**

```text
请读取并使用这个公开仓库的 skills/execute-agent-task/SKILL.md 及其引用文件：
https://github.com/yuxuandexter/agent-task-skills

现在开始执行已确认的目标：【实际 goal.md 路径或可访问链接】。
核对目标文档、这条消息和可读取的宿主 Goal；有实质冲突先指出。
在约定范围内推进并验证，在任务项目中记录进度与证据。
遵守当前项目规则和工具权限。无法读取 Skill 或目标文档时请明确说明。
```

这段是普通启动消息。用于宿主 Goal 的消息还应包含具体结果、核心验收和重要约束，不能只写“完成这个文件”；frame 会为实际任务生成这段内容。新会话或另一台设备必须能读取目标文档，本地路径不会自动传给它。

## 查看 agent 正在做什么

默认使用目标项目的任务目录；已有约定时沿用它：

```text
tasks/<task-slug>/
  goal.md         # 确认的目标、交付、验收、边界和必要上下文
  README.md       # 目标链接、当前阶段、下一步、待决定事项、证据摘要
  work-log.md     # 实际操作、结果、证据位置及必要的恢复说明
```

Frame 在内容确定且文档准备获授权后保存 `goal.md`；仅讨论时在聊天中保留草稿。Execute 开始后建立或更新进度记录。按需要增加 `context.md` 或 `plan.md`，不强制增加文件。

你通常只需查看任务首页，必要时再查工作记录。目标与验收保持稳定；进度变化只更新 README 和 work-log。目标的实质变更由你决定，并与启动消息和宿主 Goal 对齐。修改 Markdown 不会自动修改宿主 Goal。

Agent 在重要进展、阻塞和交接时更新记录。最后更新时间不保证进程仍在运行。只读请求、文件白名单、禁止保存和项目审批规则仍有效；无法保存时明确说明。不会创建全局 Todo 或复制已有任务系统。

本次更新记录见 [Goal 交接流程](tasks/goal-handoff/README.md)；旧版目录实践见 [历史记录](tasks/visible-task-records/README.md)。模板见 [goal-handoff.md](skills/frame-agent-task/references/goal-handoff.md) 和 [task-records.md](skills/execute-agent-task/references/task-records.md)。

## 安装

可在 Codex 中请求：

```text
用 skill-installer 从 GitHub 仓库 yuxuandexter/agent-task-skills 安装：
- skills/frame-agent-task
- skills/execute-agent-task
```

也可以把两个完整 Skill 目录分别放进 Codex 的用户 Skill 目录：通常为 `$CODEX_HOME/skills`，未设置时为 `~/.codex/skills`。已有同名目录时先比较内容，不要直接覆盖。

每个目录都包含自己的 `SKILL.md`、`agents/openai.yaml` 和 `references/task-contract.md`。Frame 另带 `references/goal-handoff.md`，execute 另带 `references/task-records.md`。两者保留正常自动匹配能力，也支持显式 `$skill-name` 调用。安装不提供后台执行、调度、持久 Goal、预算强制执行或外部服务权限；这些能力由宿主及用户授权决定。

## 共享交接约定

唯一维护源是 [`shared/task-contract.md`](shared/task-contract.md)。它定义目的、目标、验收与证据、上下文、范围、推进方式、预算与停止、交付的含义，允许用普通文字表达。

Communication 约定借鉴 ASD-STE100 和 Google 技术写作原则：沿用用户语言，先呈现结果或待决定问题，保持术语一致，把证据状态说清楚。简化表达时保留条件、例外和不确定性；不要求英文，不声称严格符合 ASD-STE100。规则应用于任务说明、进度、交接与最终报告，尊重用户对具体产物的风格要求。

为了让每个 Skill 可以独立安装，仓库将约定打包进两个 Skill 的 `references/`。修改维护源后运行：

```bash
python3 scripts/sync_contract.py
python3 scripts/sync_contract.py --check
python3 -B -m unittest discover -s tests -p 'test_*.py' -v
```

打包脚本只需要 Python 标准库，执行 Skill 时无需运行。维护者还应使用 Codex `skill-creator` 的 `quick_validate.py` 检查两个 Skill，并按 [behavioral-cases.md](tests/behavioral-cases.md) 进行适当的行为验证。结构检查不等于行为可靠性证明。

研究来源用于本仓库的独立撰写；没有把外部框架的完整流程或代码复制为依赖。
