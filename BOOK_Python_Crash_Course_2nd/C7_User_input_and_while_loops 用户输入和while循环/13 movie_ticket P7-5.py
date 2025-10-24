# 有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；3～12岁的观众收费10美元；超过12岁的观众收费15美元。请编写一个循环，在其中询问用户的年龄，并指出其票价。

age = int(input("Please enter your age:"))
while age != 'quit':
    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket is 10 dollars.")
    else:
        print("Your ticket is 15 dollars.")
    age = int(input("Please enter your age:"))
