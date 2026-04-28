import os
import sys

from dotenv import load_dotenv
from openai import OpenAI


# 这个函数专门负责加载并校验配置。
# 这样做的好处是：把“配置读取”与“业务逻辑”分开，初学者更容易定位问题。
def load_config():
    # 读取 .env 文件，把里面的键值对加载到当前进程环境变量中。
    # 如果 .env 不存在，load_dotenv() 不会直接报错，所以后面我们会自己做必填校验。
    load_dotenv()

    # OPENAI_API_KEY：用于身份认证。
    # 无论是 OpenAI 官方还是兼容 OpenAI 的聚合平台，通常都需要这个密钥。
    api_key = os.getenv("OPENAI_API_KEY", "").strip()

    # OPENAI_BASE_URL：接口地址。
    # - 留空：默认使用 OpenAI 官方地址
    # - 不留空：使用聚合平台提供的 OpenAI 兼容地址（常见形态是 https://xxx/v1）
    base_url = os.getenv("OPENAI_BASE_URL", "").strip()

    # OPENAI_MODEL：要调用的模型名称。
    # 例如 gpt-4o-mini、deepseek-chat 等，具体取值由你使用的平台决定。
    model = os.getenv("OPENAI_MODEL", "").strip()

    # API Key 是必填项，缺失时给出清晰提示并退出。
    if not api_key:
        print("配置错误：未检测到 OPENAI_API_KEY，请先在 .env 中填写 API Key。")
        sys.exit(1)

    # 模型名也是必填项，缺失时提示用户去 .env 补全。
    if not model:
        print("配置错误：未检测到 OPENAI_MODEL，请先在 .env 中填写模型名称。")
        sys.exit(1)

    return api_key, base_url, model


# 这个函数负责读取技能提示词文件。
# 我们把 skill 文档作为 system prompt，让模型先理解“输出规范”，再处理用户创意。
def read_skill(skill_path="skills/novel_outline.md"):
    if not os.path.exists(skill_path):
        print(f"文件错误：未找到 skill 文件：{skill_path}")
        sys.exit(1)

    # 使用 utf-8 读取，避免中文内容出现乱码。
    with open(skill_path, "r", encoding="utf-8") as f:
        return f.read().strip()


# 这个函数负责读取终端输入。
# 保持单独函数，便于后续扩展（例如改成从 inputs/ 文件读取）。
def read_user_input():
    user_input = input("请输入你的小说创意：\n").strip()

    # 如果用户直接回车，说明没有给出有效创意，此时不继续请求模型。
    if not user_input:
        print("输入错误：你还没有输入小说创意，请重新运行程序后再输入。")
        sys.exit(1)

    return user_input


# 这个函数负责创建 OpenAI 客户端。
# OpenAI 官方 SDK 同时支持官方地址和兼容 OpenAI 协议的第三方平台。
def create_client(api_key, base_url):
    # 当 base_url 有值时，明确传入自定义地址（聚合平台场景）。
    if base_url:
        return OpenAI(
            api_key=api_key,
            base_url=base_url,
        )

    # 当 base_url 为空时，不传该参数，SDK 会使用 OpenAI 官方默认地址。
    return OpenAI(api_key=api_key)


# 这个函数专门负责调用模型。
# 这里使用 chat.completions.create，是 OpenAI 兼容接口中最常见的对话调用方式。
def call_model(client, model, skill_prompt, user_input):
    # messages 是对话消息数组：
    # - system：放规则（skill 文本）
    # - user：放用户本次输入的创意
    messages = [
        {"role": "system", "content": skill_prompt},
        {"role": "user", "content": user_input},
    ]

    # 通过 model 指定要调用的具体模型。
    response = client.chat.completions.create(
        model=model,
        messages=messages,
    )

    # 兼容常见返回结构：取第一条候选结果。
    return response.choices[0].message.content or ""


# 主流程函数：把“读取配置 -> 读取 skill -> 读取输入 -> 调用模型 -> 打印结果”串起来。
def main():
    api_key, base_url, model = load_config()
    skill_prompt = read_skill("skills/novel_outline.md")
    user_input = read_user_input()
    client = create_client(api_key, base_url)

    # API 调用属于网络操作，可能因网络、鉴权、模型名错误等原因失败。
    # 因此必须用 try/except 给出友好提示，避免直接抛出难懂的报错栈给初学者。
    try:
        result = call_model(client, model, skill_prompt, user_input)
        print("\n===== 模型返回结果 =====\n")
        print(result)
    except Exception as e:
        print("API 调用失败")
        print(f"异常信息：{e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
