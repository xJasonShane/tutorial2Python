# 可使用方法replace()将字符串中的特定单词都替换为另一个单词。下面是一个简单的示例，演示了如何将句子中的'dog'替换为'cat'：
# 读取你刚创建的文件learning_python.txt中的每一行，将其中的Python都替换为另一门语言的名称，比如C。将修改后的各行都打印到屏幕上。

filepath = 'BOOK Python-Crash-Course/C10 Files-and-exceptions 文件和异常/learning_python.txt'

with open(filepath) as file_object:
    for line in file_object:
        line = line.replace('Python', 'C')
        print(line.rstrip())
