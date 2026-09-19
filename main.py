inspirations = []

while True :
    print("\n===写作助手===")
    print("1.添加灵感")
    print("2.查看灵感")
    print("3.退出")
    choice = input("请选择：")

    if choice == "1":
        text = input("写下你的灵感：")
        inspirations.append(text)
        print("已保存")
    elif choice == "2":
        if not inspirations:
            print("还没有灵感")
        else:
            for i,item in enumerate(inspirations,1):
                print(f"{i}.{item}")
    elif choice == "3":
        print("再见")
        break
    else:
        print("输入有误，请重新选择")
    