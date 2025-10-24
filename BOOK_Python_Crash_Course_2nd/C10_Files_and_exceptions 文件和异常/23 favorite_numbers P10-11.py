# 编写一个程序，提示用户输入喜欢的数，并使用json.dump()将这个数存储到文件中。再编写一个程序，从文件中读取这个值，并打印如下所示的消息。
# I know your favorite number! It's _____.

import json

filename = 'BOOK Python-Crash-Course/C10 Files-and-exceptions 文件和异常/favorite_number.json'
number = int(input("What is your favorite number? "))

with open(filename, 'w') as f:
    json.dump(number, f)

with open(filename) as f:
    number = json.load(f)

print(f"I know your favorite number! It's {number}.")
