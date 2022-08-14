#! /usr/bin/python3
import cards_tools
# True  表示无限循环
while True:

    # 显示功能菜单
    cards_tools.show_menu()
    action_str = input("请输入您要执行的操作：")
    print(f"您选择的操作是【{action_str}】")

    # 1，2，3针对名片的操作
    if action_str in ["1", "2", "3"]:
        # 新增名片
        if action_str == "1":
            cards_tools.new_cards()
            pass
        # 显示全部
        elif action_str == "2":
            cards_tools.show_all()
            pass
        # 查询名片
        elif action_str == "3":
            cards_tools.search_cards()
            pass
    # 0 退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")
        break
        # 如果在正常开发中不希望立刻编写后续代码，
        # 可以使用pass关键字，表示一个占位符，能够保证程序代码结构正确
        # pass关键字不会执行任何的操作
        # pass
    # 其他输入都是错误的，需要提醒用户重新输入
    else:
        print("您输入的不正确，请重新输入")
