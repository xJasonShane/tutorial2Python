# 修改为完成练习6-2而编写的程序，让每个人都可以有多个喜欢的数，然后将每个人的名字及其喜欢的数打印出来。

favorite_numbers = {
    'li': [1, 2, 3],
    'si': [4, 5, 6],
    'wu': [7, 8, 9],
}

for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")
    print('\n')
