# 访问古登堡计划，找一些你想分析的图书。下载这些作品的文本文件或将浏览器中的原始文本复制到文本文件中。
# 可以使用方法count()来确定特定的单词或短语在字符串中出现了多少次。例如，下面的代码计算'row'在一个字符串中出现了多少次：
# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3
# 请注意，通过使用lower()将字符串转换为小写，可捕捉要查找单词的所有格式，而不管其大小写如何。
# 编写一个程序，它读取你在古登堡计划中获取的文件，并计算单词'the'在每个文件中分别出现了多少次。这里计算得到的结果并不准确，因为将诸如'then'和'there'等单词也计算在内了。请尝试计算'the '（包含空格）出现的次数，看看结果相差多少。

try:
    with open('alice.txt', encoding='utf-8') as f:
        contents = f.read()
        print(contents.count('the'))
        print(contents.count('the '))
except FileNotFoundError:
    print("Sorry, the file alice.txt does not exist.")
