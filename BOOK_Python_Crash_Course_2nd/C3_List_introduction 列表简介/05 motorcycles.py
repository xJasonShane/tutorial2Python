motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 修改列表中的元素
motorcycles[0] = 'ducati'
print(motorcycles)


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 列表末尾添加元素
motorcycles.append('ducati')
print(motorcycles)

# 创建空列表并添加元素
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 在列表中插入元素
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 删除列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# 使用方法pop()删除元素(弹出元素)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# 使用pop()删除列表中的任何元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)

# 根据值删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.remove('yamaha')
print(motorcycles)
