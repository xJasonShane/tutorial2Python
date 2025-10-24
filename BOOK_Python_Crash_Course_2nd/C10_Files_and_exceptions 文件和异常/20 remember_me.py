import json

username = input("What is your name? ")
filename = 'BOOK Python-Crash-Course/C10 Files-and-exceptions 文件和异常/username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")
