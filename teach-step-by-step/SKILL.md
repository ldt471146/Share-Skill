---
name: teach-step-by-step
description: 当用户要求学习、理解、拆解或被教学一个文件、文章、代码库、技术概念、工作流或 skill 设计时使用。适用于用户说“慢慢教我”“一点一点教我”“仔细阅读这个文件”“拆解讲给我”“给实际案例”“边教边实现”“教学为主”“不要一次性讲完”等请求。Use this skill for step-by-step teaching, careful explanation, practical examples, and teaching while implementing.
---

# Teach Step By Step

用小步、可确认的方式教学。`SKILL.md` 只负责导航：先读稳定教学原则，再按任务类型进入对应工作流。

## Always Read

1. `rules/teaching-principles.md`

## Common Tasks

- 教用户阅读文件、文章、代码或资料 -> follow `workflows/teach-source.md`
- 边教学边实现 skill、文档、工作流或代码 -> follow `workflows/teach-while-implementing.md`
- 用户说没懂、太快、要换个说法 -> follow `workflows/re-explain.md`
- 用户说时间久了、先回顾、再继续 -> follow `workflows/recap-and-continue.md`
- 多资料、多产物或 3 个以上相对独立教学子任务 -> follow `workflows/multi-subtask-teaching.md`
- Other / unlisted task -> read `rules/teaching-principles.md`, then use the closest workflow above.

## Session Discipline

同一会话中，只要用户提出新的教学目标、切换资料、要求边教边实现、或说没听懂，都必须重新匹配 `Common Tasks`，并重新读取对应 workflow。

检验：这次任务使用的 workflow 是否和 `Common Tasks` 里最匹配的路由一致？如果不是，回到 `Common Tasks` 重新选择。

## Routing Rules

- 每次只选择一个最匹配的 workflow。
- 不要把详细案例塞进 `SKILL.md`；案例应放入 `references/`。
- 如果新增了反复使用的教学步骤，优先新增或更新 workflow，而不是扩写本文件。
