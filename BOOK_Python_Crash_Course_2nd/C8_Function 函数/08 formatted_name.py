def get_formatted_name(first, last):
    """返回整洁的姓名"""
    full_name = f"{first} {last}"
    return full_name.title()

musician = get_formatted_name("jason", "shane")
print(musician)

# 可选实参
def get_formatted_name(first, last, middle=""):
    """返回整洁的姓名"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

musician = get_formatted_name("jason", "shane")
print(musician)

musician = get_formatted_name("jason", "shane", "lee")
print(musician)
