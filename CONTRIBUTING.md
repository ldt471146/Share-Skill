# Contributing

这个仓库用于集中保存可复用的 AI Agent Skills。

## 目录规则

- 每个 skill 使用一个顶层目录。
- 每个目录必须包含 `SKILL.md`。
- 不要修改已有 skill 的 `name` 或目录名，避免破坏 agent 路由。
- `description` 可以使用中文说明 + 英文触发语，便于中文用户识别，同时保留自动触发关键词。

## 更新方式

1. 将新的 skill 目录复制到仓库根目录。
2. 确认每个 skill 目录都有 `SKILL.md`。
3. 更新 `README.md` 和 `skills.json` 索引。
4. 提交并推送。

## 注意

部分 skill 来自第三方仓库。同步或修改时请保留原始文件结构，并自行确认许可证和适用范围。
