filepath = 'BOOK Python-Crash-Course/C10 Files-and-exceptions 文件和异常/programming.txt'

# w 写入模式会覆盖文件原有的内容
with open(filepath, 'w') as file_object:
    file_object.write('I love programming.\n')
    file_object.write('I love creating new games.\n')

# a 写入模式会在文件末尾添加内容
with open(filepath, 'a') as file_object:
    file_object.write('I also love finding meaning in large datasets.\n')
    file_object.write('I love creating apps that can run in a browser.\n')
