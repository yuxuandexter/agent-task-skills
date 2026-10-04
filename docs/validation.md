# 初始验证记录

日期：2026-10-04。对象：本仓库 v0.1 初始版本。

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

`frame-agent-task` 现在要求先用简短预览说明预期产物、用途与可检查证据，再交接或进入执行。README 和例子已更新。回查文字确认仅整理时结束、已授权且无关键歧义时展示后继续、明确要求确认时等待的边界一致，且不把预期结果写成已完成事实。

实际重新运行的检查：framing Skill 的官方 `quick_validate.py` 通过，现有 3 项打包测试通过，`git diff --check` 通过。本次未新增独立 agent 行为试用；这些检查不证明所有宿主都会遵循预览要求。

## 可查看的任务目录更新 · 2026-10-04

执行 Skill 新增随包的 `references/task-records.md`，默认在目标项目中维护每个任务的首页和工作记录，并沿用现有项目约定。共享约定同步更新，保留 framing-only、只读、限定写入范围和已有审批规则的边界。本次实际任务记录位于 `tasks/visible-task-records/`。

实际检查：两个 Skill 的官方 `quick_validate.py` 均通过；现有 3 项打包测试通过，其中独立安装引用检查覆盖新增参考文件；20 个本地 Markdown 链接可解析；`git diff --check` 通过。回查了记录与实际命令结果，区分了计划、已执行检查和剩余限制。

本次未新增独立 agent 行为试用，也未验证后台运行或通知。本次实际记录展示了初始化、规则修改和验证结果，不构成跨模型、跨会话恢复行为的可靠性证明。

## 限制

这是一次局部行为检查，不是跨模型、跨宿主或长期运行的可靠性评测。没有在本轮实测完整安装流程、持久 Goal、资源预算强制中断、真实 GPU 实验、真实发布、人工视觉验收或所有授权冲突场景。[案例列表](../tests/behavioral-cases.md) 中尚未执行的项目是后续测试素材，不是已通过的检查。

后续根据真实使用暴露的问题做窄范围修订；避免为了单个案例增加普遍审批或固定流程。
