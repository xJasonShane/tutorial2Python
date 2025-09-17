filepath = 'BOOK Python-Crash-Course/C10 Files-and-exceptions 文件和异常/pi_digits.txt'
with open(filepath) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filepath) as file_object:
    contents = file_object.read()
print(contents.rstrip())

# 逐行输出
with open(filepath) as file_object:
    for line in file_object:
        print(line)
