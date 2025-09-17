# 创建文件cats.txt和dogs.txt，在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。将这些代码放在一个try-except 代码块中，以便在文件不存在时捕获FileNotFound 错误，并显示一条友好的消息。将任意一个文件移到另一个地方，并确认except 代码块中的代码将正确执行。

try:
    with open('cats.txt', encoding='utf-8') as f:
        contents = f.read()
        print(contents)
except FileNotFoundError:
    print("Sorry, the file cats.txt does not exist.")

try:
    with open('dogs.txt', encoding='utf-8') as f:
        contents = f.read()
        print(contents)
except FileNotFoundError:
    print("Sorry, the file dogs.txt does not exist.")
