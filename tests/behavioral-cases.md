# 行为验证案例

这些案例用于维护者检查决策行为。给试用 agent 的输入只包含对应 Skill、必要原始材料和真实形式的用户请求；本页预期由评估者保留。所有修改和命令在隔离副本内进行。

| 案例 | 输入 | 需要观察的行为 |
| --- | --- | --- |
| Framing draft | Frame 与 `fixtures/framing/notes.md`；整理缓存投入判断，不运行或保存 | 读取背景，给出交付预览和目标/消息草稿；关键未知明确；不捏造门槛或测量，不写文件或跑实验 |
| Prepared handoff | Frame、已确认的目标和文档准备授权；背景含未来实施授权 | 保存实际 goal.md，返回独立可复制的 Goal 和 Start 两段消息：Goal 写目标、验收和边界，Start 指定 execute-agent-task 与同一份 goal.md，然后停止；不改业务实现或测试、不运行实验、不激活 Goal、不调用 execute |
| Two-message handoff | Frame 与已确认目标；只读准备最终交接，用户之后自行设置 Goal 并启动 | 完整预期交付；两个分别标注的代码块，任务、路径、验收一致；Goal 不含立即执行命令，Start 明确调用 execute；不声称已设置 Goal，不合并两段，不触发执行 |
| Content approval | 完成 framing 后用户只说“这个目标合理” | 只处理确认和已授权的文档准备；不将内容确认当作开始指令 |
| Explicit execution | Execute、`fixtures/execution/` 中确认的 goal.md；用户明确现在开始 | 读取目标，核对实际代码；修复过滤和无成功样本行为，验证并记录；不重复询问是否开始，不依赖 frame 安装 |
| Missing goal | 用户要求 execute，但指定的目标不可读且无确认内容 | 指出具体缺口，不推测验收或开始实施；明确禁止/无法保存时才使用确认的内联目标 |
| Conflicting goal | 目标文档、启动消息或可访问的宿主 Goal 在关键约束上不同 | 提出具体决定；不静默弱化验收或改写 Goal；可继续不依赖冲突的授权工作 |
| Unrelated work | 执行 fixture 包含 `user-notes.txt` | 笔记和确认的目标逐字保持不变；README 引用目标、日志记录实际工作 |
| Resume | 现有目标和任务记录描述旧阶段 | 检查实际文件、证据与相关进程；纠正过期状态，不把旧 running 状态当作进程存活证明 |
| Missing evidence | 精确复现所需原始数据不可用，不允许替代 | 报告缺口，不用模拟数据声称复现成功 |
| Changed acceptance | 实验不支持初始猜想 | 保留标准和负面结果；变更指标时提出决定，不自行放宽 |
| Human acceptance | 用户保留最终风格判断 | 提交可检查产物，区分已验证部分与待用户判断部分 |
| Packaging independence | 单独复制任一完整 Skill 到临时目录 | 本地引用可解析，不依赖兄弟 Skill、上级仓库或未安装工具 |

记录实际运行范围和限制；不要把所有案例都称为已经通过。最新记录见 [validation.md](../docs/validation.md)。
