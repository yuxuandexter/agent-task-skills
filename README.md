# Agent Task Skills

先讨论并确认目标，再由你启动执行。Agent 交付可检查的结果和证据。

这是两个面向 Codex、也可供其他能读取文件的 agent 使用的轻量 Skills，适用于研究、工程和需要证据的知识工作。当前是 **v0.2 初始实践**；来源与设计取舍见 [design-sources.md](docs/design-sources.md)，实际验证范围见 [validation.md](docs/validation.md)。

## 两个 Skills

| Skill | 用途 | 本轮交付与停止点 |
| --- | --- | --- |
| [`frame-agent-task`](skills/frame-agent-task/SKILL.md) | 讨论目的、目标、验收、边界和必要文档 | 完整、朴实的预期交付说明、目标文档或草稿、分别可复制的 Goal message 和 Start message；然后停止 |
| [`execute-agent-task`](skills/execute-agent-task/SKILL.md) | 收到你明确的启动或恢复指令后，依据确认的目标执行与验证 | 当前进度、实际工作记录、结果与验收证据 |

两者不自动串联。确认目标内容、保存 `goal.md` 或标记“ready”都不等于启动执行。Execute 可以读取其他流程准备的等价目标文档，不依赖 frame 已安装。开始后，范围内的普通步骤无需反复确认。

## 怎么用

先讨论和准备：

```text
用 $frame-agent-task 和我讨论这个任务：
我想判断某个优化方案是否值得继续投入。
先逐项说明预期交付及验收，再讨论 goal.md 和需要准备的文档。
内容确定后，在已授权范围内保存文档，并分别给我可复制的 Goal message 和 Start message。
本轮到交接为止，不执行任务，不激活 Goal。
```

Frame 最后会给你两个独立代码块：

- **Goal message**：用于设置目标，写清结果、预期交付、验收证据、边界和 `goal.md` 位置，不混入“现在开始执行”。
- **Start message**：明确调用 `execute-agent-task`，读取同一份 `goal.md`，开始执行、记录进度并逐项验证。

关键选择尚未确定时，文档和两段消息都标为草稿。你先检查完整的预期交付，再按宿主的实际方式设置 Goal 和启动任务。

Start message 的结构如下；Frame 会替你填入实际任务与路径：

```text
现在用 $execute-agent-task 按已确认的 tasks/<task-slug>/goal.md 开始执行。
核对目标文档、这条消息和可读取的宿主 Goal；有实质冲突先指出。
在约定范围内持续迭代，更新任务记录，最后逐项提供验收证据。
```

将示例路径换成实际文件。**Codex 的 `/goal` 激活后可能立即开始工作。** 两段消息不代表宿主会自动等待。如果支持只保存目标而不运行，可以先设置 Goal，之后发送 Start；否则先保留两段草稿，准备执行时再将 Goal 和 Start 的内容一起提交。参见 [OpenAI 的长任务说明](https://learn.chatgpt.com/docs/long-running-work)。

无需持久 Goal 的环境，也可以用已确认的目标文档和明确的启动消息执行普通任务。Skill 本身不提供后台运行。更多例子见 [examples.md](docs/examples.md)。

## 跨 agent 启动消息

将第一段发给能读取仓库的 agent，并填写任务。该公开仓库无需私有仓库授权；agent 仍需具备读取链接或本地文件的能力。

**讨论阶段：**

```text
请读取并使用这个公开仓库的 skills/frame-agent-task/SKILL.md 及其引用文件：
https://github.com/yuxuandexter/agent-task-skills

和我讨论目标、验收与边界；完整说明预期交付，措辞朴实。
讨论所需文档，内容确定后在授权范围内准备 goal.md，并分别给我 Goal message 和 Start message。
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

这段是 Start message 的跨 agent 用法。独立的 Goal message 保留具体结果、核心验收和重要约束，不能只写“完成这个文件”；Frame 会为实际任务生成这两段消息。新会话或另一台设备必须能读取目标文档，本地路径不会自动传给它。

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

早期实施记录见 [Goal 交接流程](tasks/goal-handoff/README.md)；旧版目录实践见 [历史记录](tasks/visible-task-records/README.md)。模板见 [goal-handoff.md](skills/frame-agent-task/references/goal-handoff.md) 和 [task-records.md](skills/execute-agent-task/references/task-records.md)。

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

普通讨论和进度保持简短；进度通常用 1–3 句。**预期交付和最终交付必须完整，不能为短而漏项。** Frame 逐项说明你会收到什么、里面包含什么、如何验收。Execute 最后逐项说明实际交付、查看位置、验证结果和缺口。你可以直接在回复中检查，方法细节和工作日志再看文档。Goal message 和 Start message 分别给出可复制版本；未保存的目标则提供完整草稿。

表达借鉴 ASD-STE100 和 Google 技术写作原则：短句、主动表达、一句一个意思、同一概念用同一个词。沿用你的语言，必要术语只作简短解释。不能为缩短文字而删掉条件、失败检查或未验证之处。这是写作适配，不声称严格符合 ASD-STE100；你要求详细解释时会展开。

为了让每个 Skill 可以独立安装，仓库将约定打包进两个 Skill 的 `references/`。修改维护源后运行：

```bash
python3 scripts/sync_contract.py
python3 scripts/sync_contract.py --check
python3 -B -m unittest discover -s tests -p 'test_*.py' -v
```

打包脚本只需要 Python 标准库，执行 Skill 时无需运行。维护者还应使用 Codex `skill-creator` 的 `quick_validate.py` 检查两个 Skill，并按 [behavioral-cases.md](tests/behavioral-cases.md) 进行适当的行为验证。结构检查不等于行为可靠性证明。

研究来源用于本仓库的独立撰写；没有把外部框架的完整流程或代码复制为依赖。
