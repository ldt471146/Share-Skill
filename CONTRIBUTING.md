# 收录新 Skill

新增 skill 时，请按下面的检查顺序处理。

## 基本要求

1. 新建一个独立目录，目录名使用小写字母、数字和连字符。
2. 目录内必须有 `SKILL.md`。
3. `SKILL.md` frontmatter 至少包含 `name` 和 `description`。
4. `description` 写触发条件，不写宣传语。
5. 不要把会话日志、调试流水或一次性说明塞进 skill。

## 放置规则

| 内容类型 | 推荐位置 |
| --- | --- |
| 触发条件、Always Read、Common Tasks | `SKILL.md` |
| 所有任务都要遵守的稳定原则 | `rules/` |
| 某类任务的执行步骤 | `workflows/` |
| 详细案例、背景解释、坑点 | `references/` |
| 可重复执行的检查、转换、生成逻辑 | `scripts/` |

## 收录前检查

至少做这几项：

```powershell
py -X utf8 "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\skill-name"
```

如果 skill 自带检查脚本，也要运行对应脚本。例如：

```powershell
py -X utf8 ".\skill-name\scripts\check_paths.py" ".\skill-name"
```

## 索引更新

新增 skill 后，同步更新：

- `README.md` 的“当前收录”表格
- `skills.json`

`skills.json` 用于让脚本或 Agent 快速了解仓库里有哪些 skill。
