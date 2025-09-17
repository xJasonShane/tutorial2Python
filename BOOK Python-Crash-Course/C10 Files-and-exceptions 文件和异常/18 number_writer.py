import json

number = [2, 3, 5, 7, 11]
filename = 'BOOK Python-Crash-Course/C10 Files-and-exceptions 文件和异常/number.json'
with open(filename, 'w') as f:
    json.dump(number, f)
