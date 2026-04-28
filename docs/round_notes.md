# Round Notes

## Round 0 完成内容

- 初始化 `novel-demo` 教学型仓库骨架。
- 创建并整理基础目录：`skills/`、`inputs/`、`outputs/`、`docs/`。
- 添加 `main.py` 最小入口（仅输出初始化成功信息）。
- 添加 `.env.example`（环境变量占位）。
- 添加 `requirements.txt`（基础依赖）。
- 添加 `skills/novel_outline.md`（小说大纲 skill 占位模板）。
- 添加 `inputs/sample_idea.txt`（测试创意输入样例）。
- 添加 `init_backup.sh`（结构检查与快照导出脚本）。

## Round 1 完成内容

- 把 `skills/novel_outline.md` 从占位模板升级为可直接使用的小说大纲生成 skill。
- 在 skill 中补全固定输出结构（共 10 个部分）与行为规则，确保输出稳定、可复用。
- 更新 `README.md`，补充 Round 1 项目进度。
- 更新 `docs/code_explanation.md`，说明 skill 文件的作用与后续接入方式。
- 当前仍未接入 API 调用，项目继续保持教学节奏。
- 下一轮（Round 2）将开始编写 API 调用脚本，打通最小调用流程。

## Round 2 完成内容

- `main.py` 已接入最小 API 调用流程，能够从命令行发起一次完整请求。
- 已支持读取 `.env` 中的 `OPENAI_API_KEY`、`OPENAI_BASE_URL`、`OPENAI_MODEL`。
- 已支持读取 `skills/novel_outline.md`，并将其作为 system prompt。
- 已支持在终端输入小说创意作为 user message。
- 已接入 OpenAI 官方 Python SDK 的 `chat.completions.create` 调用。
- 已支持把模型返回结果直接打印到终端。
- 当前版本暂未把结果保存到 `outputs/`（保存能力放到 Round 3）。
