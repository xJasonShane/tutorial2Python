# 最后一个remember_me.py版本假设用户要么已输入用户名，要么是首次运行该程序。我们应该修改这个程序，以防当前用户并非上次运行该程序的用户。
# 为此，在greet_user()中打印欢迎用户回来的消息前，询问他用户名是否正确。如果不对，就调用get_new_username()让用户输入正确的用户名。

import json

filename = 'BOOK Python-Crash-Course/C10 Files-and-exceptions 文件和异常/favorite_number.json'

def get_new_username():
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")
        if username != get_new_username():
            username = get_new_username()
            print(f"Your username has been updated to {username}.")
