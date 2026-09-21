import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("ZAI_API_KEY")

client = OpenAI(
    api_key = api_key,
    base_url = "https://open.bigmodel.cn/api/paas/v4/"
)

chat_history = [
    {"role":"system","content":"你是一个写作助手，用中文回答。"}
]

def ask_ai(prompt):
    chat_history.append({"role":"user","content":prompt})
    response = client.chat.completions.create(
        model="glm-4-flash",
        messages=chat_history,
        temperature=0.8
    )

    answer = response.choices[0].message.content

    chat_history.append({"role":"assistant","content":answer})

    return answer

if __name__ == "__main__":
    prompt = input("请输入问题：")
    answer = ask_ai(prompt)
    print(answer)
    