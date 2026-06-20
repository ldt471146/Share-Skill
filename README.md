# Share-Skill

这是一个用于收录和分享好用 AI Agent skills 的仓库。

每个 skill 都应该是一个独立目录，目录内必须包含 `SKILL.md`。如果 skill 需要额外规则、工作流、参考资料或脚本，可以继续放在同级的 `rules/`、`workflows/`、`references/`、`scripts/` 等目录中。

## 当前收录

| Skill | 用途 | 路径 |
| --- | --- | --- |
| Teach Step By Step | 用小步、可确认的方式教学文件、文章、代码、技术概念或 skill 设计。 | [`teach-step-by-step/`](teach-step-by-step/) |
| Skill-Based Architecture | 把散落的 Agent 规则、薄壳入口、工作流和参考资料整理成可路由、可验证、可维护的 skill 架构。 | [`skill-based-architecture/`](skill-based-architecture/) |
| CNKI Search | 使用本地 `cnki` CLI 在中国知网检索论文、获取详情、提取参考文献并输出表格或 GB/T 7714 引用格式。 | [`cnki-search/`](cnki-search/) |

## 使用方式

把需要的 skill 目录复制到你的 Codex skills 目录：

```powershell
Copy-Item -Recurse .\teach-step-by-step "$env:USERPROFILE\.codex\skills\teach-step-by-step"
```

然后重启 Codex 或开启新会话，让 Codex 重新加载 skill 列表。

## 收录原则

- 一个目录只放一个 skill。
- `SKILL.md` 只做触发和导航，不写成长篇百科。
- 稳定规则放 `rules/`。
- 有序步骤放 `workflows/`。
- 案例、背景和坑点放 `references/`。
- 可重复、确定性的检查放 `scripts/`。
- 收录前至少确认 `SKILL.md` frontmatter 有效。

## 目录建议

```text
skill-name/
├── SKILL.md
├── agents/
├── rules/
├── workflows/
├── references/
└── scripts/
```

不是每个目录都必须存在。只保留当前 skill 真正需要的内容。
