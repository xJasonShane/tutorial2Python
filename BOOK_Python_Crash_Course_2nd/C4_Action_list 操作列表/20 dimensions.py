dimensions = (200, 50)
print(dimensions)
print(dimensions[0])
print(dimensions[1])

# 尝试修改元组元素
# dimensions[0] = 250
# print(dimensions)
'''
    dimensions[0] = 250
    ~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
'''

# 遍历元组中的所有值
for dimension in dimensions:
    print(dimension)

# 覆盖变量的元组变相改变元组元素
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
