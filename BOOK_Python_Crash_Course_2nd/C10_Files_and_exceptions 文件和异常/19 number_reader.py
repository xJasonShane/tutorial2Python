import json

filename = 'BOOK Python-Crash-Course/C10 Files-and-exceptions 文件和异常/number.json'
with open(filename) as f:
    number = json.load(f)

print(number)
