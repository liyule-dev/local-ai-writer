# 1.导入模块
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# 2.加载环境变量
load_dotenv()
api_key = os.getenv("ZAI_API_KEY")

# 3.创建客户端
client = OpenAI(
    api_key = api_key,
    base_url = "https://open.bigmodel.cn/api/paas/v4/"
)

# 4.定义对话历史文件名
CHAT_FILE = "chat_history.json"

# 5.定义加载函数
def load_chat_history():
    try:
        with open(CHAT_FILE,"r",encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return [
                {"role":"system","content":"你是一个写作助手，用中文回答。"}
            ]


# 6.定义保存函数
def save_chat_history(history):
    with open(CHAT_FILE,"w",encoding="utf-8") as f:
        json.dump(history,f,ensure_ascii=False,indent=2)

# 7.加载对话历史
chat_history = load_chat_history()

# 8.和ai对话
def ask_ai(prompt):
    chat_history.append({"role":"user","content":prompt})
    save_chat_history(chat_history)

    response = client.chat.completions.create(
        model="glm-4-flash",
        messages=chat_history,
        temperature=0.8
    )

    answer = response.choices[0].message.content
    chat_history.append({"role":"assistant","content":answer})
    save_chat_history(chat_history)

    return answer

# 9.清除对话记录
def clear_chat_history():
    global chat_history
    chat_history = [
        {"role":"system","content":"你是一个写作助手，用中文回答。"}
    ]

    save_chat_history(chat_history)

# 10.测试代码
if __name__ == "__main__":
    prompt = input("请输入问题：")
    answer = ask_ai(prompt)
    print(answer)
    