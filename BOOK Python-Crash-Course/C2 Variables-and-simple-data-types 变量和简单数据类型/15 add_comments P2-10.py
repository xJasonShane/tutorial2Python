# 选择你编写的两个程序，在每个程序中至少添加一条注释。如果程序太简单，实在没有什么需要说明的，就在程序文件开头加上你的姓名和当前日期，再用一句话阐述程序的功能。

'''
01 hello_world.py
'''
# 创建字符串赋值变量并打印它
message = "Hello Python World!"
print(message)

# 尝试覆盖变量内容并打印它查看结果
message = "Hello Python Crash Course world!"
print(message)

'''
05 full_name.py
'''
# 姓名拼接
first_name = "ada"
last_name = "lovelace"
full_name= f"{first_name} {last_name}"
print(full_name)

# 姓名拼接，并使用.title()方法将姓名首字母大写
first_name = "ada"
last_name = "lovelace"
full_name= f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# 姓名拼接，并使用.title()方法将姓名首字母大写，赋值变量并打印
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)
