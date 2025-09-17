# 将为完成练习10-6而编写的代码放在一个while循环中，让用户犯错（输入的是文本而不是数）后能够继续输入数。

while True:
    try:
        x = int(input("请输入第一个数："))
        y = int(input("请输入第二个数："))
    except ValueError:
        print("请输入数字！")
    else:
        print(f"{x} + {y} = {x + y}")
        break
