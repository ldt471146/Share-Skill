# Share-Skill

个人 AI Agent Skills 集合。当前仓库同步自本机 CC Switch skills，所有 `description` 已尽量改为中文说明 + 保留英文触发语，方便中文使用时识别用途，同时保留自动触发关键词。

## 统计

- Skills 数量：63
- 格式：每个 skill 一个目录，目录内包含 `SKILL.md`。
- 索引：`skills.json`。

## 来源

- `PanJitao/drawio-to-visio`：1 个
- `addyosmani/agent-skills`：24 个
- `impeccable.style`：1 个
- `ldt471146/Share-Skill`：3 个
- `mattpocock/skills`：34 个

## Skills

| Skill | 来源 | 说明 |
|---|---|---|
| [`api-and-interface-design`](api-and-interface-design/SKILL.md) | `addyosmani/agent-skills` | 设计稳定的 API、模块边界和公共接口，适用于 REST、GraphQL、类型契约以及前后端边界。；Guides stable API and interface design. Use when designing APIs, module boundaries, or any public interface. Use when creating ... |
| [`ask-matt`](ask-matt/SKILL.md) | `mattpocock/skills` | 路由选择器，用来判断当前情况该走哪个 Matt Pocock skill 或工作流。；Ask which skill or flow fits your situation. A router over the user-invoked skills in this repo. |
| [`browser-testing-with-devtools`](browser-testing-with-devtools/SKILL.md) | `addyosmani/agent-skills` | 用 Chrome DevTools MCP 做真实浏览器测试、DOM 检查、控制台错误、网络请求、性能和视觉验证。；Tests in real browsers via Chrome DevTools MCP. Use when building or debugging anything that runs in a browser. Use whe... |
| [`ci-cd-and-automation`](ci-cd-and-automation/SKILL.md) | `addyosmani/agent-skills` | 配置或修改 CI/CD、质量门禁、测试流水线和部署自动化。；Automates CI/CD pipeline setup. Use when setting up or modifying build and deployment pipelines. Use when you need to automate quality gates, confi... |
| [`cnki-search`](cnki-search/SKILL.md) | `ldt471146/Share-Skill` | 在中国知网 CNKI 检索中文学术论文、期刊、学位论文、会议论文、论文详情和参考文献。 在中国知网（CNKI）上检索学术论文。触发场景：用户要求搜索知网论文、查找文献、检索期刊/学位论文/会议论文， 或提到"知网"、"CNKI"、"中国知网"、"文献检索"、"论文搜索"等关键词时使用此 skill。 支持关键词检索、主题检索、作者检索、高级检索、论文详... |
| [`code-review-and-quality`](code-review-and-quality/SKILL.md) | `addyosmani/agent-skills` | 合并前做多维代码审查，评估自己、他人或 agent 写的代码质量。；Conducts multi-axis code review. Use before merging any change. Use when reviewing code written by yourself, another agent, or a human. Use whe... |
| [`code-simplification`](code-simplification/SKILL.md) | `addyosmani/agent-skills` | 在不改变行为的前提下简化代码，降低复杂度并提升可读性、可维护性和可扩展性。；Simplifies code for clarity. Use when refactoring code for clarity without changing behavior. Use when code works but is harder to read, ma... |
| [`codebase-design`](codebase-design/SKILL.md) | `mattpocock/skills` | 设计深模块和清晰接口，寻找模块边界、seam、可测试性和 AI 可导航性改进。；Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportuni... |
| [`context-engineering`](context-engineering/SKILL.md) | `addyosmani/agent-skills` | 为 agent 准备合适上下文、规则文件和项目环境，适用于新会话、切换任务或输出质量下降。；Optimizes agent context setup. Use when starting a new session, when agent output quality degrades, when switching between tasks, o... |
| [`debugging-and-error-recovery`](debugging-and-error-recovery/SKILL.md) | `addyosmani/agent-skills` | 系统化根因调试，适用于测试失败、构建失败、行为异常或未知错误。；Guides systematic root-cause debugging. Use when tests fail, builds break, behavior doesn't match expectations, or you encounter any unexpected e... |
| [`decision-mapping`](decision-mapping/SKILL.md) | `mattpocock/skills` | 把松散想法拆成一组有顺序的调查票据，并逐项推进到结论。；Turn a loose idea into a sequenced map of investigation tickets, then drive them to resolution one at a time. |
| [`deprecation-and-migration`](deprecation-and-migration/SKILL.md) | `addyosmani/agent-skills` | 规划废弃、迁移和下线旧系统、API 或功能，决定维护、迁移还是淘汰。；Manages deprecation and migration. Use when removing old systems, APIs, or features. Use when migrating users from one implementation to anoth... |
| [`design-an-interface`](design-an-interface/SKILL.md) | `mattpocock/skills` | 用并行子 agent 生成多个差异化接口设计，用于 API、模块形状和 design it twice 探索。；Generate multiple radically different interface designs for a module using parallel sub-agents. Use when user wants to de... |
| [`diagnosing-bugs`](diagnosing-bugs/SKILL.md) | `mattpocock/skills` | 诊断困难 bug 和性能回退，按复现、最小化、假设、埋点、修复、回归测试闭环推进。；Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/t... |
| [`documentation-and-adrs`](documentation-and-adrs/SKILL.md) | `addyosmani/agent-skills` | 记录架构决策、公共 API 变化、功能背景和未来工程师或 agent 需要理解的上下文。；Records decisions and documentation. Use when making architectural decisions, changing public APIs, shipping features, or when you n... |
| [`domain-modeling`](domain-modeling/SKILL.md) | `mattpocock/skills` | 建立和打磨项目领域模型、术语表、ubiquitous language 和 ADR。；Build and sharpen a project's domain model. Use when the user wants to pin down domain terminology or a ubiquitous language, record an... |
| [`doubt-driven-development`](doubt-driven-development/SKILL.md) | `addyosmani/agent-skills` | 对非平凡决策做 fresh-context 对抗审查，适用于高风险、陌生代码或正确性优先场景。；Subjects every non-trivial decision to a fresh-context adversarial review before it stands. Use when correctness matters more tha... |
| [`drawio-to-visio`](drawio-to-visio/SKILL.md) | `PanJitao/drawio-to-visio` | 将 draw.io 流程图导出为 Visio 兼容的 SVG 格式，修复 foreignObject 文本导致的 Visio 文字偏移和不可编辑问题，适用于将 .drawio 导出结果导入 Microsoft Visio 编辑。；Use when converting draw.io diagrams to Visio-compatible SVG, ... |
| [`edit-article`](edit-article/SKILL.md) | `mattpocock/skills` | 编辑文章草稿，重构章节、提升清晰度并压紧文字。；Edit and improve articles by restructuring sections, improving clarity, and tightening prose. Use when user wants to edit, revise, or improve an article ... |
| [`frontend-ui-engineering`](frontend-ui-engineering/SKILL.md) | `addyosmani/agent-skills` | 构建生产级前端界面、组件、布局、状态管理和可访问性体验。；Builds production-quality UIs. Use when building or modifying user-facing interfaces. Use when creating components, implementing layouts, managing s... |
| [`git-guardrails-claude-code`](git-guardrails-claude-code/SKILL.md) | `mattpocock/skills` | 为 Claude Code 设置 Git 安全钩子，阻止 push、reset --hard、clean、branch -D 等危险命令。；Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) befor... |
| [`git-workflow-and-versioning`](git-workflow-and-versioning/SKILL.md) | `addyosmani/agent-skills` | 组织 Git 工作流、分支、提交、冲突解决和多条并行工作流。；Structures git workflow practices. Use when making any code change. Use when committing, branching, resolving conflicts, or when you need to organ... |
| [`grill-me`](grill-me/SKILL.md) | `mattpocock/skills` | 通过高强度追问澄清计划或设计，适合非代码和通用决策。；A relentless interview to sharpen a plan or design. |
| [`grill-with-docs`](grill-with-docs/SKILL.md) | `mattpocock/skills` | 通过高强度追问澄清计划或设计，并同步生成 ADR、术语表和上下文文档。；A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. |
| [`grilling`](grilling/SKILL.md) | `mattpocock/skills` | 可复用的追问循环，用于压力测试计划、设计和所有 grill 类请求。；Interview the user relentlessly about a plan or design. Use when the user wants to stress-test a plan before building, or uses any 'grill' tri... |
| [`handoff`](handoff/SKILL.md) | `mattpocock/skills` | 把当前对话压缩成交接文档，方便另一个 agent 或后续会话接手。；Compact the current conversation into a handoff document for another agent to pick up. |
| [`idea-refine`](idea-refine/SKILL.md) | `addyosmani/agent-skills` | 把模糊想法通过发散和收敛思考打磨成可执行概念，适合 ideate、refine 和 stress-test。；Refines raw ideas into sharp, actionable concepts through structured divergent and convergent thinking. Use when an idea i... |
| [`impeccable`](impeccable/SKILL.md) | `impeccable.style` | 前端设计和界面打磨 skill，适用于设计、重设计、审查、审计、抛光、排版、配色、布局、动效、响应式、可访问性、性能、错误状态、空状态、设计系统和去 AI 味。；Use when the user wants to design, redesign, shape, critique, audit, polish, clarify, distill, h... |
| [`implement`](implement/SKILL.md) | `mattpocock/skills` | 根据 PRD 或 issues 执行实现工作。；Implement a piece of work based on a PRD or set of issues. |
| [`improve-codebase-architecture`](improve-codebase-architecture/SKILL.md) | `mattpocock/skills` | 扫描代码库架构深度改进机会，生成可视化 HTML 报告并追问选中的改进项。；Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. |
| [`incremental-implementation`](incremental-implementation/SKILL.md) | `addyosmani/agent-skills` | 分小步增量实现跨文件改动，避免一次写太多代码。；Delivers changes incrementally. Use when implementing any feature or change that touches more than one file. Use when you're about to write a large amoun... |
| [`interview-me`](interview-me/SKILL.md) | `addyosmani/agent-skills` | 一问一答挖掘用户真实需求，适用于需求不完整、意图模糊或需要 stress-test 的请求。；Extracts what the user actually wants instead of what they think they should want. Achieves this through one-question-at-a-time in... |
| [`migrate-to-shoehorn`](migrate-to-shoehorn/SKILL.md) | `mattpocock/skills` | 把 TypeScript 测试里的 as 类型断言迁移到 @total-typescript/shoehorn。；Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn, wants to re... |
| [`observability-and-instrumentation`](observability-and-instrumentation/SKILL.md) | `addyosmani/agent-skills` | 添加日志、指标、链路追踪和告警，让生产行为可观察、可诊断。；Instruments code so production behavior is visible and diagnosable. Use when adding logging, metrics, tracing, or alerting. Use when shipping any f... |
| [`obsidian-vault`](obsidian-vault/SKILL.md) | `mattpocock/skills` | 搜索、创建和管理 Obsidian vault 笔记、wikilinks 和索引笔记。；Search, create, and manage notes in the Obsidian vault with wikilinks and index notes. Use when user wants to find, create, or organi... |
| [`performance-optimization`](performance-optimization/SKILL.md) | `addyosmani/agent-skills` | 基于测量优化性能，适用于性能需求、回归、Core Web Vitals 或加载时间问题。；Optimizes application performance. Use when performance requirements exist, when you suspect performance regressions, or when Core W... |
| [`planning-and-task-breakdown`](planning-and-task-breakdown/SKILL.md) | `addyosmani/agent-skills` | 把规格或明确需求拆成有顺序、可实现、可验证、可并行的任务。；Breaks work into ordered tasks. Use when you have a spec or clear requirements and need to break work into implementable tasks. Use when a task fee... |
| [`prototype`](prototype/SKILL.md) | `mattpocock/skills` | 构建可丢弃原型，用终端应用或多套 UI 变体探索设计。；Build a throwaway prototype to flesh out a design — a runnable terminal app for state/business-logic questions, or several radically different UI var... |
| [`qa`](qa/SKILL.md) | `mattpocock/skills` | 交互式 QA 会话，用户口头报告 bug 后由 agent 补上下文并创建 GitHub issues。；Interactive QA session where user reports bugs or issues conversationally, and the agent files GitHub issues. Explores the c... |
| [`request-refactor-plan`](request-refactor-plan/SKILL.md) | `mattpocock/skills` | 通过访谈创建小提交粒度的重构计划，并作为 GitHub issue 发布。；Create a detailed refactor plan with tiny commits via user interview, then file it as a GitHub issue. Use when user wants to plan a refacto... |
| [`resolving-merge-conflicts`](resolving-merge-conflicts/SKILL.md) | `mattpocock/skills` | 解决正在进行的 git merge 或 rebase 冲突。；Use when you need to resolve an in-progress git merge/rebase conflict. |
| [`review`](review/SKILL.md) | `mattpocock/skills` | 从指定提交、分支、tag 或 merge-base 起审查改动，按标准符合度和规格符合度并行评审。；Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes — Standards (does the code follow th... |
| [`scaffold-exercises`](scaffold-exercises/SKILL.md) | `mattpocock/skills` | 生成课程练习目录、题目、解答和讲解结构，并确保通过 lint。；Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. Use when user wants to scaffold exerci... |
| [`security-and-hardening`](security-and-hardening/SKILL.md) | `addyosmani/agent-skills` | 加固处理用户输入、认证、数据存储和第三方集成的代码安全。；Hardens code against vulnerabilities. Use when handling user input, authentication, data storage, or external integrations. Use when building any fe... |
| [`setup-matt-pocock-skills`](setup-matt-pocock-skills/SKILL.md) | `mattpocock/skills` | 首次使用 Matt Pocock 工程 skills 前配置 issue tracker、triage 标签和领域文档路径。；Configure this repo for the engineering skills — set up its issue tracker, triage label vocabulary, and domain doc... |
| [`setup-pre-commit`](setup-pre-commit/SKILL.md) | `mattpocock/skills` | 配置 Husky、lint-staged、Prettier、类型检查和测试等提交前钩子。；Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add ... |
| [`shipping-and-launch`](shipping-and-launch/SKILL.md) | `addyosmani/agent-skills` | 准备生产发布清单、监控、分阶段发布和回滚策略。；Prepares production launches. Use when preparing to deploy to production. Use when you need a pre-launch checklist, when setting up monitoring, when plan... |
| [`skill-based-architecture`](skill-based-architecture/SKILL.md) | `ldt471146/Share-Skill` | 整理和优化 skill/规则架构，适用于规则分散、SKILL.md 过大、description 命中率差或需要迁移到 skills 目录。；This skill should be used when the user asks to "organize the project rules", "clean up scattered document... |
| [`source-driven-development`](source-driven-development/SKILL.md) | `addyosmani/agent-skills` | 用官方文档支撑实现决策，避免过时模式并保留来源引用。；Grounds every implementation decision in official documentation. Use when you want authoritative, source-cited code free from outdated patterns. Use w... |
| [`spec-driven-development`](spec-driven-development/SKILL.md) | `addyosmani/agent-skills` | 编码前先写规格，适用于新项目、新功能、重大变更或需求不清。；Creates specs before coding. Use when starting a new project, feature, or significant change and no specification exists yet. Use when requirements... |
| [`tdd`](tdd/SKILL.md) | `mattpocock/skills` | 使用红灯-绿灯-重构进行测试驱动开发，适用于 test-first 功能和 bug 修复。；Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants ... |
| [`teach`](teach/SKILL.md) | `mattpocock/skills` | 在当前工作区持续教学一个新 skill 或技术概念。；Teach the user a new skill or concept, within this workspace. |
| [`teach-step-by-step`](teach-step-by-step/SKILL.md) | `ldt471146/Share-Skill` | 一步一步教学、拆解文件/文章/代码库/技术概念，并结合实际案例或边教边实现。；当用户要求学习、理解、拆解或被教学一个文件、文章、代码库、技术概念、工作流或 skill 设计时使用。适用于用户说“慢慢教我”“一点一点教我”“仔细阅读这个文件”“拆解讲给我”“给实际案例”“边教边实现”“教学为主”“不要一次性讲完”等请求。Use this skill fo... |
| [`test-driven-development`](test-driven-development/SKILL.md) | `addyosmani/agent-skills` | 用测试驱动开发和验证逻辑变更，适用于实现逻辑、修 bug 或改变行为。；Drives development with tests. Use when implementing any logic, fixing any bug, or changing any behavior. Use when you need to prove that cod... |
| [`to-issues`](to-issues/SKILL.md) | `mattpocock/skills` | 把计划、规格或 PRD 拆成可独立领取的垂直切片 issues。；Break a plan, spec, or PRD into independently-grabbable issues on the project issue tracker using tracer-bullet vertical slices. |
| [`to-prd`](to-prd/SKILL.md) | `mattpocock/skills` | 把当前对话综合成 PRD 并发布到项目 issue tracker。；Turn the current conversation into a PRD and publish it to the project issue tracker — no interview, just synthesis of what you've already dis... |
| [`triage`](triage/SKILL.md) | `mattpocock/skills` | 按 triage 状态机处理 issues 和外部 PR，分类、核实、必要时追问并写 agent-ready brief。；Move issues and external PRs through a state machine of triage roles — categorise, verify, grill if needed, and wri... |
| [`ubiquitous-language`](ubiquitous-language/SKILL.md) | `mattpocock/skills` | 从当前对话提取 DDD 统一语言和术语表，消除歧义并保存到 UBIQUITOUS_LANGUAGE.md。；Extract a DDD-style ubiquitous language glossary from the current conversation, flagging ambiguities and proposing canonica... |
| [`using-agent-skills`](using-agent-skills/SKILL.md) | `addyosmani/agent-skills` | 总调度 skill，判断当前任务该调用哪个工程生命周期 skill。；Discovers and invokes agent skills. Use when starting a session or when you need to discover which skill applies to the current task. This is ... |
| [`writing-beats`](writing-beats/SKILL.md) | `mattpocock/skills` | 把文章素材整理成 beat 旅程，一段一段选择方向并写成叙事。；Shape an article as a journey of beats, choose-your-own-adventure style. The user picks a starting beat from the raw material, you write only tha... |
| [`writing-fragments`](writing-fragments/SKILL.md) | `mattpocock/skills` | 通过追问收集写作碎片、观点、故事和句子，作为未来文章原始材料。；Grilling session that mines the user for fragments — heterogeneous nuggets of writing (claims, vignettes, sharp sentences, half-thoughts) — and a... |
| [`writing-great-skills`](writing-great-skills/SKILL.md) | `mattpocock/skills` | 编写和编辑高质量 skills 的参考规则，帮助 skill 更可预测。；Reference for writing and editing skills well — the vocabulary and principles that make a skill predictable. |
| [`writing-shape`](writing-shape/SKILL.md) | `mattpocock/skills` | 把 markdown 原始材料通过对话打磨成可发布文章。；Take a markdown file of raw material and shape it into an article through a conversational session — drafting candidate openings, growing the piece ... |

## 安装说明

可将需要的 skill 目录复制到你的 agent skills 目录，例如 CC Switch / Codex 使用的 skills 目录。

```powershell
# 示例：复制某个 skill
Copy-Item -Recurse .\spec-driven-development C:\Users\Administrator\.cc-switch\skills\spec-driven-development
```

## 备注

- `name` 和目录名保持原样，避免破坏 agent 路由。
- `description` 使用中英双语，中文便于识别，英文保留原触发语义。
- 部分 skill 来自第三方仓库，使用前请自行检查许可证和适用范围。
