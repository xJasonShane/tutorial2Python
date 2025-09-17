# 将练习10-11中的程序合二为一。如果存储了用户喜欢的数，就向用户显示它，否则提示用户输入喜欢的数并将其存储到文件中。运行这个程序两次，看看它能否像预期的那样工作。

import json

filename = 'BOOK Python-Crash-Course/C10 Files-and-exceptions 文件和异常/favorite_number.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = int(input("What is your favorite number? "))
    with open(filename, 'w') as f:
        json.dump(number, f)
else:
    print(f"I know your favorite number! It's {number}.")
