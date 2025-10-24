# 让用户输入一个数，并指出该数是否是10的整数倍。

number = int(input("Enter a number, and I'll tell you if it's a multiple of 10: "))

if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of 10.")
else:
    print(f"\nThe number {number} is not a multiple of 10.")
