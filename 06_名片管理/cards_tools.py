# 所有名片记录的列表
cards_list = []


def show_menu():
    """显示功能菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】 V 1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_cards():
    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 1. 提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入qq：")
    email_str = input("请输入邮箱：")
    # 2.使用用户输入的信息建立一个名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}
    # 3.将名片字典添加到列表中
    cards_list.append(card_dict)
    print(cards_list)
    # 4.提示用户添加成功
    print("%s的名片添加成功" % name_str)


def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示全部名片")
    # 判断是否有名片记录，如果没有提示用户且返回
    if len(cards_list) == 0:
        print("当前没有名片信息，请添加用户信息")
        # return 可以返回一个函数的执行结果
        # 下方的代码不会被执行
        return
    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")

    print("")
    # 打印分割线
    print("=" * 50)
    # 遍历名片列表依次输出字典信息
    for card_dict in cards_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))


def search_cards():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
    # 1.提示用户，输出要搜索的用户名片
    find_name = input("请输入你要查找的姓名：")
    # 2.遍历用户名片，查询用户要搜索的名片，如果没有，需要提示用户
    for card_dict in cards_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            # 针对查找到的信息作出修改和删除的操作
            deal_cards(card_dict)
            break
    else:
        print("抱歉，没有找到%s的信息" % find_name)


def deal_cards(find_dict):
    """处理名片信息

    :param find_dict: 查找到的名片信息
    """
    print(find_dict)
    action_str = input("请选择你要做得操作"
                       " [1] 修改 [2] 删除 0 退出到菜单")
    if action_str == "1":
        find_dict["name"] = input_dict_info(find_dict["name"], "姓名：")
        find_dict["phone"] = input_dict_info(find_dict["phone"], "电话：")
        find_dict["qq"] = input_dict_info(find_dict["qq"], "QQ:")
        find_dict["email"] = input_dict_info(find_dict["email"], "邮箱:")
        print("修改名片成功！")
    elif action_str == "2":
        cards_list.remove(find_dict)
        print("删除名片成功！")


def input_dict_info(dict_value, tip_message):
    """修改用户名片

    :param dict_value: 字典原有信息
    :param tip_message: 提示信息
    :return: 如果输入了信息则返回名片信息，如果没有输入则返回字典原有信息
    """
    # 1.提示用户输入内容
    result_str = input(tip_message)
    # 2.针对用户输出的值作出判断，如果用户输出了值直接返回这个值
    if len(result_str) > 0:
        return result_str
    # 3.如果用户没有输出，就返回"字典中原来的值"
    else:
        return dict_value
