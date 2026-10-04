# 设计来源与取舍

这份记录说明两个 Skills 的设计依据。资料检索日期为 **2026-10-04**；它们是工程实践与实现先例，不是对本仓库效果的实验性证明。网页及上游主分支可能继续变化。

| 一手来源 | 采用的原则 | 在本仓库中的适配 |
| --- | --- | --- |
| [OpenAI — Using Goals in Codex](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex) | 用结果、验证证据、约束、边界、迭代策略和受阻条件定义工作 | 以普通任务说明承载这些含义；持久 Goal 需要明确请求和宿主支持 |
| [Karpathy — autoresearch/program.md](https://github.com/karpathy/autoresearch/blob/master/program.md) | 固定评价条件、限定可修改范围、先建立 baseline、记录实际实验结果 | 保留可比较性与结果记录；不沿用无限循环、固定五分钟预算或自动 Git 操作 |
| [Karpathy — Verifiability](https://karpathy.bearblog.dev/verifiability/) | 可验证的反馈影响自动优化的可行性 | 没有可靠验收方式时，先定义有限的验证方法探索 |
| [Google Antigravity — Best practices](https://www.antigravity.google/docs/cli/best-practices/) | 探索、规划、执行分阶段；让 agent 根据本地验证反馈迭代 | 简单请求可以直接处理，复杂任务才使用完整交接 |
| [Google Antigravity — Artifacts](https://www.antigravity.google/docs/artifacts) | 使用可评论、可检查的产物进行阶段性协作 | 默认聊天中的简短说明；有需要且获授权时保存文档和检查材料 |
| [Google ADK — Evaluation](https://adk.dev/evaluate/) | 同时检查最终结果与工具使用过程 | 关注会影响结论的来源、实际动作和结果；不把每个工具调用都变成人工审批 |
| [Google ADK — Loop workflow](https://adk.dev/agents/workflow-agents/loop-agents/) | 循环需要明确退出机制 | 区分完成、人工验收、受阻、预算或用户停止；不依赖具体旧版 LoopAgent API |
| [Google Cloud — Agent KPIs](https://cloud.google.com/transform/the-kpis-that-actually-matter-for-production-ai-agents) | 人的验证时间与返工影响 agent 的实际价值 | 交付直接证据链接与最小检查路径，不给用户建立个人评分表 |
| [Superpowers — Brainstorming](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md) | 先形成用户能识别和纠正的共同理解 | 沿用已知要求和授权；不引入每个简单任务都要重新批准的流程 |
| [Superpowers — Writing plans](https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md) / [Executing plans](https://github.com/obra/superpowers/blob/main/skills/executing-plans/SKILL.md) | 分离任务设计和执行，形成可验证增量 | 研究任务允许依据证据调整路线；不强制逐任务 TDD、commit 或多 agent |
| [Superpowers — Verification before completion](https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md) | 完成声明必须得到验证证据支持 | 验证覆盖当前相关状态；只因后续修改失效的证据需要重做 |
| [GitHub Spec Kit — Quickstart](https://github.com/github/spec-kit/blob/main/docs/quickstart.md) | 分开需求、技术计划和执行，最后回查遗漏 | 保留目标与实现细节的区分，省去固定文档链和任务数据库 |
| [GSD — Verifier](https://github.com/gsd-build/get-shit-done/blob/main/agents/gsd-verifier.md) | 从目标倒推必须成立的事实，检查实际产物与行为 | 完成核对以要求和证据为单位，不使用任务打勾比例推断成功 |
| [Anthropic — Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | 增量推进与清晰交接帮助跨上下文恢复工作 | 有需要且获授权时保留检查点；不声称一份 Skill 能提供常驻运行 |

## 本地创建规范

使用 Codex 提供的 `skill-creator` 初始化目录、生成 UI metadata 并验证。遵循其简短入口、按需引用、精确触发和保留用户意图的原则。该 Skill 属于创建环境，不作为本仓库运行时依赖。

## 共同约定的打包

两个独立 Skill 都需要读到交接含义。为了兼容只复制一个 Skill 目录的安装方式，`shared/task-contract.md` 是唯一维护源，两个随包副本由标准库脚本生成并可检查一致性。执行时只读 Skill 自己目录内的副本，不假设上级仓库或兄弟 Skill 存在。
