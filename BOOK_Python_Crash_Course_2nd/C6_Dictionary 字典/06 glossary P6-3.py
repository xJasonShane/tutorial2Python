# Python字典可用于模拟现实生活中的字典。
# 为避免混淆，我们将后者称为词汇表。想出你在前面学过的5个编程术语，将其用作词汇表中的键，并将它们的含义作为值存储在词汇表中。
# 以整洁的方式打印每个术语及其含义。为此，可先打印术语，在它后面加上一个冒号，再打印其含义；也可在一行打印术语，再使用换行符（\n ）插入一个空行，然后在下一行以缩进的方式打印其含义。

# 词汇表
glossary = {
    'list': '列表',
    'dictionary': '字典',
    'string': '字符串',
    'integer': '整数',
    'float': '浮点数',
}

# 打印每个术语及其含义
print("list: " + glossary['list'])
print("\n")
print("dictionary: " + glossary['dictionary'])
print("\n")
print("string: " + glossary['string'])
print("\n")
print("integer: " + glossary['integer'])
print("\n")
print("float: " + glossary['float'])
