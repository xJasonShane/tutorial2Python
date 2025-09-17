# 修改你在练习10-8中编写的except代码块，让程序在任意文件不存在时静默失败。

try:
    with open('cats.txt', encoding='utf-8') as f:
        contents = f.read()
        print(contents)
except FileNotFoundError:
    pass

try:
    with open('dogs.txt', encoding='utf-8') as f:
        contents = f.read()
        print(contents)
except FileNotFoundError:
    pass
