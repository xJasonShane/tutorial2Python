# 编写一个程序，提示用户输入名字。用户做出响应后，将其名字写入文件guest.txt中。

filepath = 'BOOK Python-Crash-Course/C10 Files-and-exceptions 文件和异常/guest.txt'
with open(filepath, 'w') as file_object:
    name = input('Please enter your name:')
    file_object.write(name)
    print(f'Your name has been written into the document {filepath}')
