import json

filename = 'BOOK Python-Crash-Course/C10 Files-and-exceptions 文件和异常/username.json'
with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")
