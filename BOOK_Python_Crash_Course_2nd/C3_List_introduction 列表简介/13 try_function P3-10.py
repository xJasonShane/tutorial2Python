# 想想可存储到列表中的东西，如山川、河流、国家、城市、语言或你喜欢的任何东西。编写一个程序，在其中创建一个包含这些元素的列表，然后，对于本章介绍的每个函数，都至少使用一次来处理这个列表。

city = ["Tokyo", "Beijing", "Shanghai", "Sao Paulo", "Mexico City"]
print(city)
print(city[0])
print(city[1])
print(city[2])
print(city[3])
print(city[4])

# 插入新城市
city.insert(0, "Delhi")
print(city)
# 添加新城市
city.append("Rio de Janeiro")
print(city)

# 删除城市
del city[0]
print(city)
# 弹出城市
popped_city = city.pop()
print(city)
print(popped_city)

# 临时排序
print(city)
print(sorted(city))
print(city)
# 永久排序
city.sort()
print(city)
# 永久反向排序
city.sort(reverse=True)
print(city)

# 确认city列表的长度
print(len(city))
