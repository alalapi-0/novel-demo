# novel-demo

## 项目用途

`novel-demo` 是一个**教学型 Python 项目仓库**，用于演示并练习一种清晰、可扩展的开发模式：

- **API**：后续会逐步接入模型 API 调用能力；
- **脚本**：通过可执行脚本维护项目结构与流程；
- **Skill 文件**：通过结构化提示模板沉淀写作与生成方法。

这个仓库的目标不是一次性做出完整产品，而是作为一个最小、可迭代的实验骨架，方便在每一轮学习中逐步增加能力。

## 当前阶段（Round 0）

当前为 **Round 0**，仅完成以下基础工作：

- 初始化目录结构；
- 创建最小可运行入口 `main.py`；
- 预留 `.env.example` 与 `requirements.txt`；
- 预留 `skills/`、`inputs/`、`outputs/`、`docs/` 等教学用目录与文件；
- 提供 `init_backup.sh`，用于结构检查与快照导出。

> 简单来说：现在先把“骨架”搭好，保证后续每一轮迭代都在同一套规范下进行。

## 后续轮次规划（简要）

后续 Round 会逐步加入：

1. 环境变量读取（如 API Key、Base URL、Model）；
2. API 调用最小闭环（输入 -> 请求 -> 输出）；
3. 输入与输出文件流程化（从 `inputs/` 读取，写入 `outputs/`）；
4. Skill 文件驱动的提示词拼装；
5. 更完整的错误处理、日志与教学文档。

## 依赖说明

`requirements.txt` 当前包含：

- `openai`
- `python-dotenv`

`requirements.txt` 文件本身不写注释（保持简洁），详细解释放在 README 与文档中。

## 快速开始（Round 0）

```bash
python main.py
```

预期输出：

```text
novel-demo initialized
```

如需检查并补齐目录结构、生成结构快照：

```bash
bash init_backup.sh
```

执行后会生成或更新：

- `docs/tree_snapshot.txt`

## 项目进度（更新到 Round 1）

- **Round 0（已完成）**：仓库骨架完成。
- **Round 1（已完成）**：小说大纲 skill 完成（`skills/novel_outline.md` 已从占位模板升级为可用版本）。
- **下一步（Round 2）**：接入 API，开始实现从输入到模型输出的脚本流程。

## Round 2 使用说明（最小 API 调用）

1. 安装依赖：

```bash
pip3 install -r requirements.txt
```

2. 复制配置文件：

```bash
cp .env.example .env
```

3. 编辑 `.env`：

- 填写 `OPENAI_API_KEY`
- 视情况填写 `OPENAI_BASE_URL`（聚合平台需要，OpenAI 官方可留空）
- 填写 `OPENAI_MODEL`

4. 运行程序：

```bash
python3 main.py
```

5. 在终端输入小说创意，查看模型返回结果。

> 说明：Round 2 只把结果打印到终端，暂时不保存到文件（文件保存将在 Round 3 处理）。
