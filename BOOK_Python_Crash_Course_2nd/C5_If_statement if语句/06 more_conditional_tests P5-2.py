# 你并非只能创建10个测试。如果想尝试做更多比较，可再编写一些测试，并将它们加入conditional_tests.py中。对于下面列出的各种情况，至少编写两个结果分别为True 和False 的测试。

# 检查两个字符串相等和不等。
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# 使用方法lower()的测试。
name = 'Marie'
print("\nIs name == 'marie'? I predict True.")
print(name.lower() == 'marie')

# 涉及相等、不等、大于、小于、大于等于和小于等于的数值测试。
age = 18
print("\nIs age == 18? I predict True.")
print(age == 18)

print("\nIs age != 18? I predict False.")
print(age != 18)

print("\nIs age > 18? I predict False.")
print(age > 18)

print("\nIs age < 18? I predict False.")
print(age < 18)

print("\nIs age >= 18? I predict True.")
print(age >= 18)

print("\nIs age <= 18? I predict True.")
print(age <= 18)

# 使用关键字and和or的测试。
age_1 = 18
age_2 = 20
print("\nIs age_1 >= 18 and age_2 >= 20? I predict True.")
print(age_1 >= 18 and age_2 >= 20)

print("\nIs age_1 >= 18 or age_2 >= 20? I predict True.")
print(age_1 >= 18 or age_2 >= 20)

# 测试特定的值是否包含在列表中。
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print("\nDoes the list contain 'mushrooms'? I predict True.")
print('mushrooms' in requested_toppings)

print("\nDoes the list contain 'pepperoni'? I predict False.")
print('pepperoni' in requested_toppings)

# 测试特定的值是否未包含在列表中。
print("\nDoes the list contain 'mushrooms'? I predict False.")
print('mushrooms' not in requested_toppings)
