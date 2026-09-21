import json
import os
from ai_client import ask_ai

DATA_FILE = "data.json"

def load_inspirations():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE,"r",encoding="utf_8") as f:
            return json.load(f)
    except (json.JSONDecodeError,IOError):
        return[]

def save_inspirations(inspirations):
    with open(DATA_FILE,"w",encoding="utf-8") as f:
        json.dump(inspirations,f,ensure_ascii=False,indent=2)

def show_nemu():
    print("\n===写作助手===")
    print("1.添加灵感")
    print("2.查看灵感")
    print("3.删除灵感")
    print("4.和AI讨论灵感")
    print("0.退出")
    
def main():
    inspirations = load_inspirations()

    while True :

        show_nemu()
        
        choice = input("请选择：")

        if choice == "1":
            text = input("写下你的灵感：")
            inspirations.append(text)
            save_inspirations(inspirations)
            print("已保存")

        elif choice == "2":
            if not inspirations:
                print("还没有灵感")
            else:
                for i,item in enumerate(inspirations,1):
                    print(f"{i}.{item}")

        elif choice == "3":
            if not inspirations:
                print("还没有灵感可删除")
            else:
                for i,item in enumerate(inspirations,1):
                    print(f"{i}.{item}")

                try:
                    num = int(input("请输入要删除的编号："))

                    if 1 <= num <= len(inspirations):
                        deleted = inspirations.pop(num - 1)
                        save_inspirations(inspirations)
                        print(f"已删除：{deleted}")
                    else:
                        print("编号不存在")
                except ValueError:
                    print("请输入数字")

        elif choice == "4":
            prompt = input("你想和AI讨论什么：")
            answer = ask_ai(prompt)
            print("\nAI回应：",answer)

        elif choice == "0":
            save_inspirations(inspirations)
            print("再见")
            break

        else:
            print("输入有误，请重新选择")

if __name__ == "__main__":
    main()
    