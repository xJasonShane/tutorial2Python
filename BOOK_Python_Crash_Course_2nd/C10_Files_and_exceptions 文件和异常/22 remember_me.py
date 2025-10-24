import json

# 如果以前存储了用户名，就加载它
# 否则，提示用户输入用户名并存储它
filename = 'BOOK Python-Crash-Course/C10 Files-and-exceptions 文件和异常/username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")
