cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# 反转排序
cars.sort(reverse=True)
print(cars)

# 调用函数临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))
# 临时反向排序
print("\nHere is the reverse sorted list:")
print(sorted(cars, reverse=True))

print("\nHere is the original list again:")
print(cars)

# 反转列表元素
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()  # 注意反转列表元素方法不是按照字母顺序反向排序，而是将整个列表倒置
print(cars)

# 确定列表长度
print(len(cars))
