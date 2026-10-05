# 验证记录

## 简洁表达强化 · 2026-10-05

用户反馈回复太长、难以理解。本次收紧共享 Communication、两个 Skill 的输出方式、目标模板和 UI prompt：讨论时只回答当前问题，交接时集中提供材料；进度通常 1–3 句。用户随后明确要求预期交付保持完整，因此 framing 的最终预览逐项说明产物内容及验收；execute 最后逐项报告实际交付、证据和缺口。两者不受固定句数或条数限制，细节和日志仍可链接到文档。简写保留验收、权限、失败检查和未验证之处。

实际检查：两个官方 `quick_validate.py` 通过，3 项打包测试通过；共享副本一致，UI metadata 有效，31 个本地 Markdown 链接可解析，`git diff --check` 通过。回查差异确认 framing 停止点、execute 明确启动条件和证据要求仍然有效。

这次是表达规则的局部修改，没有新增独立 agent 行为试用。例子均明确标为虚构；结构检查不证明实际可读性已经改善，也不是 ASD-STE100 合规认证。用户要求将本次表达规则及完整交付说明的更新一并 commit。

## v0.2：讨论与执行分离 · 2026-10-05

本次更新 framing 的停止点、`goal.md` 交接、用户明确启动和三文件分工，并同步两个 Skill、UI、文档和行为案例。当前实现记录见 [任务首页](../tasks/goal-handoff/README.md)。

### 结构检查

- 两个 Skill 的官方 `quick_validate.py` 均通过；framing 启动消息规则收紧后再次通过。
- `sync_contract.py --check` 通过；3 项 `test_packaging.py` 测试通过。
- 两个 `openai.yaml` 可解析，简介为 39/29 字符，默认 prompt 引用了对应 Skill，默认自动匹配保持开启。
- 本地 Markdown 链接检查和 `git diff --check` 通过。

### 独立行为试用与实际边界

各试用仅获得对应 Skill、必要原始材料和用户请求，没有获得评估者的案例预期。保存和执行试用使用 [execution fixture](../tests/fixtures/execution/)，只读讨论使用 [framing fixture](../tests/fixtures/framing/notes.md)。本次新增确认目标 fixture；旧 v0.1 修复补丁保留为历史证据。

| 试用 | 实际观察 | 可以支持的结论 |
| --- | --- | --- |
| 已确认内容的 framing，背景含旧实施授权 | 读取实现和测试，尝试保存目标但被审批拦截；返回未保存草稿，未运行测试或修复 | 区分计划和事实，并在交接后停止；保存行为未完成验证 |
| 明确启动且有确认目标的 execute | 读取目标，尝试创建执行记录但被审批拦截；随后只读检查并报告未完成 | 没有把原有 2 项测试通过当作问题已修复；完整执行与记录流程未完成验证 |
| 收紧消息规则后的只读 framing | 返回交付预览、goal.md 草稿与普通会话启动消息；显式写出 execute-agent-task，保留未定门槛，标记未保存，随后停止 | 本案例满足只读讨论、草稿交接和显式指定执行 Skill 的要求 |

前两个试用的 `apply_patch` 被自动审批拒绝。审批理由是把隔离 latency 任务判定为超出用户授权的 Skill 改进范围，并可能来自不可信任务文本。没有重试或绕过这两个写入拒绝。因此本次**不宣称端到端执行通过**，也不把环境拦截当作 Skill 本身已通过写入行为验证。

第一次 framing 的普通启动消息漏掉了执行 Skill 名称。根据这个实际遗漏，在入口与 goal-handoff 指南中明确要求：普通启动消息和 native Goal message 都必须指定 `execute-agent-task`。之后只读试用的消息开头为：

> 使用 execute-agent-task，在普通 agent 会话中为缓存投入评估完成只读证据规划。

该试用把只读证据规划作为待用户确认的建议，没有擅自确定投入门槛或内存上限，也没有声称已获得 benchmark 结果。实际只读取了 Skill、两个引用文件和原始 notes。

评估者回查三个隔离目录：所有原始文件逐字不变，无新增文件。对 execution 副本独立运行 `python3 -B -m unittest -v test_latency_summary.py`，现有 2 项测试通过；这只是缺陷 fixture 的 baseline，不是修复证据。没有生成新的修复补丁。

### 本轮未验证

完整保存后执行、真实宿主 Goal 的激活与状态核对、跨会话恢复、所有冲突场景和跨模型可靠性仍未验证。新规则的结构检查与局部试用不能替代这些场景。验证时 Skill 未安装到用户目录，尚未 commit 或 push；用户随后单独授权提交和推送本次更新。

下列 2026-10-04 记录属于 v0.1 历史，不证明 v0.2 行为。v0.2 将 framing 改为交接后停止；旧版自动继续执行的说明不再适用。

## v0.1 初始验证 · 2026-10-04

验证分为结构与打包检查，以及两个使用隔离上下文、隔离文件副本的 agent 行为试用。行为试用者只获得对应 Skill、原始 fixture 和用户请求，没有获得预期答案或本仓库的案例判定表。

## 实际完成的检查

| 检查 | 结果 | 范围 |
| --- | --- | --- |
| `skill-creator/scripts/quick_validate.py` | 两个 Skill 均返回 `Skill is valid!` | frontmatter、名称、description、未完成占位符 |
| `agents/openai.yaml` | 两个文件可解析，UI 描述长度和 `$skill-name` 引用正确 | 默认自动匹配保持开启；未安装到用户目录 |
| `sync_contract.py --check` | 通过 | 两个随包副本与唯一维护源一致 |
| `tests/test_packaging.py` | 3 个测试通过 | 单独安装时的本地引用、只读漂移检测、同步修复 |
| Framing 行为试用 | 符合本次案例预期 | 读取背景后只返回 brief；保留否定结果；没有捏造测量值或性能门槛 |
| Execution 行为试用 | 符合本次案例预期 | 实际修复代码、补充验证、未再次要求开始授权 |
| 试用文件回查 | 通过 | framing 文件和目录未变；execution 的用户笔记逐字未变 |

初次运行官方 validator 时系统 Python 缺少 PyYAML；随后在临时 virtualenv 中安装验证依赖并成功运行。Skill 本身与打包测试不依赖 PyYAML。

## Framing 试用

输入为 [framing fixture](../tests/fixtures/framing/notes.md)，用户只要求整理缓存投入判断的任务，明确禁止运行实验和修改文件。

实际回应将目标表述为判断缓存是否值得投入，保留支持、不支持和证据不足三种可能。它分别列出可比较性、响应质量、延迟/内存和结论边界的拟议检查，并明确 workload 与测量工具尚未检查、当前没有 benchmark 结果。它指出投入门槛和可接受的内存代价仍需确定，并提出先取得受控比较证据的建议。

评估者回查：fixture 内容逐字一致，隔离工作目录仍只有原始 notes 文件。没有将“任务整理完毕”当作实验已执行。

## Execution 试用

输入为 [execution fixture](../tests/fixtures/execution/)，用户授权修改实现和相关测试，要求只统计 `status == "ok"` 的样本，没有成功样本时抛出 `ValueError`，保留函数接口和用户笔记，禁止 commit、push 与外部服务访问。

原始实现错误地把其他状态的样本也计入平均值。试用 agent 添加了覆盖混合状态和没有成功样本的回归测试，然后修复过滤逻辑。评估者检查了实际差异，并独立重跑了修改后的测试：

```text
test_completed_samples ... ok
test_empty_input ... ok
test_no_ok_samples_raises_value_error ... ok
test_other_statuses_are_ignored_even_with_durations ... ok

Ran 4 tests
OK
```

实际修改保存为 [execution.patch](../tests/results/execution.patch)。可将原始 execution fixture 复制到临时目录，在该目录用 `git apply <execution.patch 的绝对路径>` 应用补丁，然后运行：

```bash
python3 -B -m unittest -v test_latency_summary.py
```

仓库内的原始 fixture 刻意保留缺陷，供后续行为试用；补丁只作为本次结果证据，不代表待部署的软件。

## 清晰表达规则更新 · 2026-10-04

本次在共享约定中加入 Communication，并同步到两个独立 Skill 包。入口说明指向这项约定；来源说明和虚构报告对照一并更新。

实际重新运行的检查：两个 Skill 的官方 `quick_validate.py` 均通过，现有 3 项打包测试通过，`git diff --check` 通过。回查差异确认规则保留用户语言、必要术语、条件、例外和不确定性，并尊重用户要求的产物格式与风格。示例明确标为虚构，没有作为新执行结果入账。

本次是范围有限的表达规则修订，没有新增措辞匹配测试或重跑独立 agent 行为试用。上述初始行为记录仍仅描述初始版本；本次检查不证明跨 agent 的可读性收益，也不构成 ASD-STE100 合规验证。

## 交付预览更新 · 2026-10-04

当时的 `frame-agent-task` 要求先用简短预览说明预期产物、用途与可检查证据，再交接或进入执行。README 和例子已更新。回查文字确认仅整理时结束、已授权且无关键歧义时展示后继续、明确要求确认时等待的边界一致，且不把预期结果写成已完成事实。

实际重新运行的检查：framing Skill 的官方 `quick_validate.py` 通过，现有 3 项打包测试通过，`git diff --check` 通过。本次未新增独立 agent 行为试用；这些检查不证明所有宿主都会遵循预览要求。

## 可查看的任务目录更新 · 2026-10-04

执行 Skill 新增随包的 `references/task-records.md`，默认在目标项目中维护每个任务的首页和工作记录，并沿用现有项目约定。共享约定同步更新，保留 framing-only、只读、限定写入范围和已有审批规则的边界。本次实际任务记录位于 `tasks/visible-task-records/`。

实际检查：两个 Skill 的官方 `quick_validate.py` 均通过；现有 3 项打包测试通过，其中独立安装引用检查覆盖新增参考文件；20 个本地 Markdown 链接可解析；`git diff --check` 通过。回查了记录与实际命令结果，区分了计划、已执行检查和剩余限制。

本次未新增独立 agent 行为试用，也未验证后台运行或通知。本次实际记录展示了初始化、规则修改和验证结果，不构成跨模型、跨会话恢复行为的可靠性证明。

## 限制

这是一次局部行为检查，不是跨模型、跨宿主或长期运行的可靠性评测。没有在本轮实测完整安装流程、持久 Goal、资源预算强制中断、真实 GPU 实验、真实发布、人工视觉验收或所有授权冲突场景。[案例列表](../tests/behavioral-cases.md) 中尚未执行的项目是后续测试素材，不是已通过的检查。

后续根据真实使用暴露的问题做窄范围修订；避免为了单个案例增加普遍审批或固定流程。
