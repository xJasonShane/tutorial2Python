# 编写一个程序，询问用户有多少人用餐。如果超过8位，就打印一条消息，指出没有空桌；否则指出有空桌。

number_of_people = input("How many people are in your dinner group? ")
number_of_people = int(number_of_people)

if number_of_people > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")
