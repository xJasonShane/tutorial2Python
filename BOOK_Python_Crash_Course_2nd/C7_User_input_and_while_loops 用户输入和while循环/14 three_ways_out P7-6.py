# 以不同的方式完成练习7-4或练习7-5，在程序中采取如下做法。

# 在while循环中使用条件测试来结束循环。
age = int(input("Please enter your age:"))
while age != 'quit':
    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket is 10 dollars.")
    else:
        print("Your ticket is 15 dollars.")
    age = int(input("Please enter your age:"))

# 使用变量active来控制循环结束的时机。
active = True
while active:
    age = int(input("Please enter your age:"))
    if age == 'quit':
        active = False
    else:
        if age < 3:
            print("Your ticket is free.")
        elif age <= 12:
            print("Your ticket is 10 dollars.")
        else:
            print("Your ticket is 15 dollars.")

# 使用break语句在用户输入'quit'时退出循环。
age = int(input("Please enter your age:"))
while age != 'quit':
    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket is 10 dollars.")
    else:
        print("Your ticket is 15 dollars.")
    age = int(input("Please enter your age:"))
    if age == 'quit':
        break
