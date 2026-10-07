# 设计来源与取舍

这份记录说明两个 Skills 的设计依据。初始资料检索日期为 **2026-10-04**，Goal 交接流程于 **2026-10-05** 补充核对；它们是工程实践与实现先例，不是对本仓库效果的实验性证明。网页及上游主分支可能继续变化。

| 一手来源 | 采用的原则 | 在本仓库中的适配 |
| --- | --- | --- |
| [ASD-STE100 — About STE](https://www.asd-ste100.org/about_STE.html) | 受控表达、稳定词义和领域术语帮助减少技术沟通歧义 | 借鉴清晰性原则；沿用用户语言，不施加英文受控词典，也不声称标准合规 |
| [Google — Short sentences](https://developers.google.com/tech-writing/one/short-sentences) | 一句集中表达一个意思，删去多余词语，必要时拆分步骤 | 保留条件、因果、例外和不确定性；不以固定字数或句子越短越好作为验收 |
| [OpenAI — Using Goals in Codex](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex) | 用结果、验证证据、约束、边界、迭代策略和受阻条件定义工作 | 以普通任务说明承载这些含义；持久 Goal 需要明确请求和宿主支持 |
| [Karpathy — autoresearch/program.md](https://github.com/karpathy/autoresearch/blob/master/program.md) | 固定评价条件、限定可修改范围、先建立 baseline、记录实际实验结果 | 保留可比较性与结果记录；不沿用无限循环、固定五分钟预算或自动 Git 操作 |
| [Karpathy — Verifiability](https://karpathy.bearblog.dev/verifiability/) | 可验证的反馈影响自动优化的可行性 | 没有可靠验收方式时，先定义有限的验证方法探索 |
| [Google Antigravity — Best practices](https://www.antigravity.google/docs/cli/best-practices/) | 探索、规划、执行分阶段；让 agent 根据本地验证反馈迭代 | 简单请求可以直接处理，复杂任务才使用完整交接 |
| [Google Antigravity — Artifacts](https://www.antigravity.google/docs/artifacts) | 使用可评论、可检查的产物进行阶段性协作 | framing 给出完整、朴实的交付预览；多步骤 execution 在权限允许时保存可查看的任务记录与证据位置 |
| [Google ADK — Evaluation](https://adk.dev/evaluate/) | 同时检查最终结果与工具使用过程 | 关注会影响结论的来源、实际动作和结果；不把每个工具调用都变成人工审批 |
| [Google ADK — Loop workflow](https://adk.dev/agents/workflow-agents/loop-agents/) | 循环需要明确退出机制 | 区分完成、人工验收、受阻、预算或用户停止；不依赖具体旧版 LoopAgent API |
| [Google Cloud — Agent KPIs](https://cloud.google.com/transform/the-kpis-that-actually-matter-for-production-ai-agents) | 人的验证时间与返工影响 agent 的实际价值 | 交付直接证据链接与最小检查路径，不给用户建立个人评分表 |
| [Superpowers — Brainstorming](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md) | 先形成用户能识别和纠正的共同理解 | 沿用已知要求和授权；不引入每个简单任务都要重新批准的流程 |
| [Superpowers — Writing plans](https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md) / [Executing plans](https://github.com/obra/superpowers/blob/main/skills/executing-plans/SKILL.md) | 分离任务设计和执行，形成可验证增量 | 研究任务允许依据证据调整路线；不强制逐任务 TDD、commit 或多 agent |
| [Superpowers — Verification before completion](https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md) | 完成声明必须得到验证证据支持 | 验证覆盖当前相关状态；只因后续修改失效的证据需要重做 |
| [GitHub Spec Kit — Quickstart](https://github.com/github/spec-kit/blob/main/docs/quickstart.md) | 分开需求、技术计划和执行，最后回查遗漏 | 保留目标与实现细节的区分，省去固定文档链和任务数据库 |
| [GSD — Verifier](https://github.com/gsd-build/get-shit-done/blob/main/agents/gsd-verifier.md) | 从目标倒推必须成立的事实，检查实际产物与行为 | 完成核对以要求和证据为单位，不使用任务打勾比例推断成功 |
| [Anthropic — Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | 增量推进与清晰交接帮助跨上下文恢复工作 | 有需要且获授权时保留检查点；不声称一份 Skill 能提供常驻运行 |

## 清晰表达的适配边界

Communication 是本仓库独立撰写的轻量规则。ASD-STE100 的公开介绍和 Google 写作指南提供清晰表达原则；事实、推断、拟议检查和未验证结论的区分来自本仓库的证据要求。没有将这些要求宣称为 ASD-STE100 原文，也没有审查全文标准或完成严格合规认证。

规则用于降低任务说明和交付报告的阅读与核验成本，不强制用户填写新模板或查看写作检查表。准确性优先于简短，用户要求的产物风格保持有效。实际可读性收益仍需通过日常使用验证。

2026-10-05，用户反馈输出太长、难以理解，因此将“简洁”改为可执行的输出约定。[ASD-STE100 官方 FAQ](https://www.asd-ste100.org/STE_faq.html) 明确允许将短句、一个句子一个主题和主动表达等原则用于其他写作场景；本仓库据此保留中文及必要术语。默认短回复、文档承载细节和禁止重复粘贴是本仓库针对用户反馈的设计，不是 STE 标准原文。用户需要详细解释或重要条件无法简写时仍应展开。用户随后明确补充：措辞要朴实，但会仔细检查最终 expected delivery。因此，短回复建议仅用于普通讨论与进度；framing 交接必须完整说明每项预期交付及验收，execute 最终报告必须逐项对照实际交付。文件链接不能代替这份说明。

## 用户提供的 phase-workflow 与任务目录

2026-10-04，用户提供了一份 `phase-workflow` Skill 文本，并明确希望使用 tasks folder 查看和管理 agent 的工作。该文本的作者、上游地址和版本未核实；此处保留来源描述，不复制附件全文或本地附件路径。

借鉴其计划与实际记录分离、阶段验证、恢复任务前读取记录的思路。v0.1 默认保留每个任务的首页和工作记录，优先沿用项目已有格式；v0.2 将确认的目标独立保存为 `goal.md`，首页只引用目标并展示进度。阶段继续条件允许失败复现和有依据的否定结论；恢复操作需保护原有改动，不能采用整文件还原或目录删除作为通用撤销方式。

这次用户选择把多步骤执行从默认会话记录改为默认任务目录，仍受实际写入范围和项目规则约束。没有引入全局 Todo、逐步骤审批、固定层级编号或永不修订的 lessons 文件。记录描述观察到的状态，不能证明后台进程存活。

## 先讨论，再由用户启动 · 2026-10-05

用户明确选择分开 framing 和 execution：先讨论目标、预览交付、准备 `goal.md` 和 Goal message；然后由用户设置 Goal 并明确启动 execute。这是用户选择的工作方式，不是所有 agent 工作都必须遵守的通用流程。

[OpenAI 的 Goals 指南](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex) 建议先从自然语言形成目标草稿，核对成功条件、证据、约束和停止条件，再激活目标。本仓库据此将目标 agreement 与执行记录分开：`goal.md` 保留确认的目标，README 展示状态，work-log 记录实际工作。无需为每个任务建立完整 spec 链。

[OpenAI 的长任务说明](https://learn.chatgpt.com/docs/long-running-work) 指出 `/goal` 的文字同时是首条任务指令与完成条件。当时的版本将 execute 指令与成功条件放在同一条 Goal message 中，framing 只交付文字，不自行激活。2026-10-07 起按下述新约定拆为两段。不能承诺设置 Goal 后会等待另一条消息。普通宿主也可依确认文档和明确启动消息执行，但不因此获得持久运行能力。

当时以目标文档作为详细约定，Goal message 作为启动摘要；实质变更后保持一致。用户确认目标内容不等于启动。执行开始后，普通范围内步骤沿用授权，不逐步重新审批。

## Goal message 与 Start message 分开 · 2026-10-07

用户明确要求 framing 最后返回两个独立、可复制的消息。Goal message 定义结果、预期交付、验收、约束与停止条件，用于用户设置目标；Start message 明确调用 execute-agent-task，读取同一份目标文档并开始执行。完整预期交付说明仍保留在最终回复中，两段消息不代替交付预览。

再次核对 [OpenAI 的长任务说明](https://learn.chatgpt.com/docs/long-running-work)：激活 `/goal` 时，其文字也会作为首条指令。因此两段消息是交接材料的分工，不是宿主一定会暂停等待的承诺。支持只保存目标的宿主可分开设置与启动；激活即运行的宿主应由用户在准备好时提交两段内容。Framing 不代替用户提交任何一段，也不假定 Goal 已设置成功。

## 本地创建规范

使用 Codex 提供的 `skill-creator` 初始化目录、生成 UI metadata 并验证。遵循其简短入口、按需引用、精确触发和保留用户意图的原则。该 Skill 属于创建环境，不作为本仓库运行时依赖。

## 共同约定的打包

两个独立 Skill 都需要读到交接含义。为了兼容只复制一个 Skill 目录的安装方式，`shared/task-contract.md` 是唯一维护源，两个随包副本由标准库脚本生成并可检查一致性。执行时只读 Skill 自己目录内的副本，不假设上级仓库或兄弟 Skill 存在。
