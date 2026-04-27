#!/usr/bin/env bash

# 打开严格模式：
# -e: 任一命令失败立即退出，避免错误被忽略；
# -u: 使用未定义变量时报错，避免隐藏拼写问题；
# -o pipefail: 管道中任一命令失败即整体失败，提升脚本可靠性。
set -euo pipefail

# 通过脚本所在目录定位项目根目录，避免从其他路径执行时出现相对路径错误。
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 定义需要确保存在的目录列表。
# 这些目录是教学仓库骨架的核心组成部分。
REQUIRED_DIRS=(
  "skills"
  "inputs"
  "outputs"
  "docs"
)

# 定义需要确保存在的文件列表。
# 如果缺失，脚本会创建空文件（或按下面逻辑补充最小内容）。
REQUIRED_FILES=(
  "README.md"
  ".env.example"
  "requirements.txt"
  "main.py"
  "skills/novel_outline.md"
  "inputs/sample_idea.txt"
  "outputs/.gitkeep"
  "docs/round_notes.md"
  "docs/code_explanation.md"
)

# 切换到项目根目录执行后续操作，保证路径一致。
cd "$PROJECT_ROOT"

# 逐个检查目录，不存在就自动创建。
for dir in "${REQUIRED_DIRS[@]}"; do
  if [[ ! -d "$dir" ]]; then
    mkdir -p "$dir"
    echo "[create-dir] $dir"
  else
    echo "[exists-dir]  $dir"
  fi
done

# 逐个检查文件，不存在就创建占位文件。
for file in "${REQUIRED_FILES[@]}"; do
  if [[ ! -f "$file" ]]; then
    mkdir -p "$(dirname "$file")"
    touch "$file"
    echo "[create-file] $file"
  else
    echo "[exists-file]  $file"
  fi
done

# 生成目录结构快照，写入 docs/tree_snapshot.txt。
# 这里优先使用 tree 命令；如果环境没有 tree，则回退到 find。
SNAPSHOT_FILE="docs/tree_snapshot.txt"
{
  echo "# Tree Snapshot"
  echo "Generated at: $(date -u +'%Y-%m-%d %H:%M:%S UTC')"
  echo

  if command -v tree >/dev/null 2>&1; then
    # 使用 tree 以更易读的层级格式输出，忽略常见缓存目录。
    tree -a -I '.git|__pycache__|.pytest_cache|.mypy_cache|.venv|venv'
  else
    # 回退方案：使用 find 列出文件与目录，再排序，确保输出稳定可比较。
    find . \
      -path './.git' -prune -o \
      -path './__pycache__' -prune -o \
      -path './.pytest_cache' -prune -o \
      -path './.mypy_cache' -prune -o \
      -path './.venv' -prune -o \
      -path './venv' -prune -o \
      -print | sort
  fi
} > "$SNAPSHOT_FILE"

# 输出完成提示，告知学习者快照文件位置。
echo "[done] snapshot saved to $SNAPSHOT_FILE"
