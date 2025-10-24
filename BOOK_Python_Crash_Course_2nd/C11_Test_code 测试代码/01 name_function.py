def get_formatted_name(first, last):
    """生成整洁的姓名"""
    full_name = f"{first} {last}"
    return full_name.title()

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\nNeatly-formatted name: {formatted_name}")
