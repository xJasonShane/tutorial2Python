# 现在你知道了如何遍历字典，可以整理为完成练习6-3而编写的代码，将其中的一系列函数调用print() 替换为一个遍历字典中键和值的循环。确定该循环正确无误后，再在词汇表中添加5个Python术语。当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中。

glossary = {
    'list': '列表',
    'dictionary': '字典',
    'string': '字符串',
    'integer': '整数',
    'float': '浮点数',
}

# 遍历词汇表
for term, meaning in glossary.items():
    print(term + ": " + meaning)
    print("\n")

glossary = {
    'list': '列表',
    'dictionary': '字典',
    'string': '字符串',
    'integer': '整数',
    'float': '浮点数',
    'boolean': '布尔值',
    'tuple': '元组',
    'set': '集合',
    'function': '函数',
    'class': '类',
    'object': '对象',
    'method': '方法',
    'attribute': '属性',
    'inheritance': '继承',
    'polymorphism': '多态',
    'encapsulation': '封装',
    'abstraction': '抽象',
}

# 遍历词汇表
for term, meaning in glossary.items():
    print(term + ": " + meaning)
    print("\n")
