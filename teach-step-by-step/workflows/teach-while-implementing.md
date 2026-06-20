# Teach While Implementing Workflow

用于边教学边创建或更新 skill、文档、工作流、代码或其他产物。

## Steps

1. 先解释当前概念。
2. 说明这个概念会映射到产物的哪个位置。
3. 判断内容应该放在 `SKILL.md`、`rules/`、`workflows/`、`references/` 还是 `scripts/`。
4. 只做当前最小有用编辑。
5. 解释刚才改了什么、为什么这样改。
6. 如果有校验脚本、格式检查或简单读回检查，完成后立刻验证。

不要一次性把最终系统全部写完。教学优先，产物随理解逐步长出来。

## Placement Guide

- 核心触发条件和导航 -> `SKILL.md`
- 所有任务都要遵守的稳定原则 -> `rules/`
- 某类任务的顺序步骤 -> `workflows/`
- 详细案例、背景解释、扩展材料 -> `references/`
- 可重复执行且需要确定性的检查或转换 -> `scripts/`

需要判断放置位置时，参考 `references/placement-examples.md`。

如果正在教学或实现 skill 设计，先参考 `references/skill-design-model.md`，用 Prompt / Context / Harness 三要素检查当前改动。
