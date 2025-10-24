# 编写一个while循环，询问用户为何喜欢编程。每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。

filepath = 'BOOK Python-Crash-Course/C10 Files-and-exceptions 文件和异常/programming_survey.txt'
with open(filepath, 'a') as file_object:
    while True:
        reason = input('Please input why you like programming:')
        if reason == 'exit':
            break
        file_object.write(reason + '\n')
        print(f'Your name has been written into the document {filepath}')
