# 编写一个while循环，提示用户输入名字。用户输入名字后，在屏幕上打印一句问候语，并将一条到访记录添加到文件guest_book.txt中。确保这个文件中的每条记录都独占一行。

filepath = 'BOOK Python-Crash-Course/C10 Files-and-exceptions 文件和异常/guest_book.txt'
with open(filepath, 'a') as file_object:
    while True:
        name = input('Please enter your name:')
        if name == 'exit':
            break
        file_object.write(name + '\n')
        print(f'Your name has been written into the document {filepath}')
        print(f'Welcome {name}, to our Guest Book!')
