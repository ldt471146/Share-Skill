# Skill Design Model

用 Prompt / Context / Harness 三要素理解和检查一个 skill。

## Prompt：定义做什么

Prompt 决定 Agent 的行为方向。

在 skill 里，Prompt 主要有两层：

- `description`：决定 skill 什么时候被触发。
- `SKILL.md` 正文：决定触发之后怎么执行。

检查问题：

- 用户这样说时，description 能命中吗？
- 触发之后，Agent 能知道下一步该读什么、做什么吗？

## Multi-skill Priority：先选入口，再选规则

多 skill 项目先解决“工具能不能看见入口”，再解决“当前任务该听谁的规则”。

- 工具看不见某个 skill 时，优先检查注册入口或安装位置，不先改 skill 内容。
- 有默认 skill 时，只让一个入口承担默认角色；任务明确命中某个专门 skill 时，专门 skill 优先。
- 跨 skill 的稳定规则不要复制多份，放到共享规则中，再由各 skill 的 Always Read 引入。

注意：不同工具的 frontmatter 规则不同。Cursor 原文里的 `primary: true` 不要直接照搬到 Codex skill；Codex skill frontmatter 只保留 `name` 和 `description`。

## Split Signal：什么时候拆成多个 skill

当一个 skill 的入口开始变得不精准，优先考虑拆分，而不是继续扩写。

- 不同领域的 `Common Tasks` 基本不相交。
- `description` 需要列出大量跨领域触发词。
- 坑点、案例或背景材料能自然按领域分成两组。

拆分后的目标是：每个 skill 的 `description` 更精准，`SKILL.md` 更短，任务只激活最相关的那一个入口。

## Skill Composition：隔离规则，组合流程

总编排 skill 不需要重写所有专业细节，可以在 workflow 中调用其他 skill。

- 嵌入调用：先做项目自己的前置步骤，再调用另一个 skill 的 workflow，最后回到本 workflow 收尾。
- 直接路由：本 skill 不包装，`Common Tasks` 直接指向另一个 skill 的 workflow。
- 子 Agent 委派：把另一段工作隔离给子 Agent，只接收结构化结果。

选择标准：需要前后加项目规则时用嵌入调用；完全通用时用直接路由；需要隔离上下文或并行执行时用子 Agent 委派。

组合调用必须写清楚具体 skill 路径、目标、禁止事项和验收标准。缺少被调用 skill 时，停止并说明缺失，不要让 Agent 自己猜。

## Template Test：结构可复用，内容不预制

模板只应该固定骨架，不应该替具体项目预填结论。

添加模板内容前，做“两项目测试”：两个差异很大的真实项目是否都会同意复制这块内容？

- 会同意 -> 这是协议、骨架或占位符，可以进入模板。
- 不会同意 -> 这是项目特定内容，改成 `<!-- FILL: ... -->` 或记录为故意不预制。

故意不预制的内容要留下原因，避免以后被误当成遗漏重新塞进模板。

## Context：决定看得到什么

Context 是 Agent 执行时能看到的信息。

一个规则写了但没被读到，等于没有生效。所以 skill 要用渐进式加载：

- 永远要看的内容放在 `SKILL.md` 或 `Always Read`。
- 任务相关内容放在 `workflows/`、`rules/`、`references/`。
- 详细案例不要塞进 `SKILL.md`，需要时再读。

判断提示：如果规则内容本身没错，但 Agent 正常执行任务时没有读到它，这是 Context 或路由问题，不是 Prompt 问题。

快速诊断：

- 规则写错了、目标说错了 -> Prompt 问题。
- 规则写对了，但正常任务读不到 -> Context 问题。
- 不知道规则有没有被读到，或改完无法稳定复现 -> Harness 问题。

检查问题：

- 当前任务需要的信息是否在正常路由上？
- 是否把太多无关信息塞进了当前上下文？

## Harness：验证好不好用

Harness 是检查、拦截和反馈机制。

它不只问“写得对不对”，还问“以后会不会稳定触发、稳定执行、稳定检查”。

常见 Harness：

- 校验脚本：检查 frontmatter、路径、格式。
- 路径检查：确认 `Common Tasks` 引用文件真实存在。
- 人眼复查：确认教学节奏是否真的适合用户。

检查问题：

- 改完后有没有验证？
- 失败时能看出是内容问题、结构问题，还是工具问题吗？
