def get_formatted_name(first, last):
    """返回整洁的姓名"""
    full_name = f"{first} {last}"
    return full_name.title()

# 这是一个无限循环
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# 退出循环
    repeat = input("\nWould you like to repeat the program? (yes/yes) ")
    if repeat != "yes":
        break
