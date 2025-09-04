squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# 简易统计计算
print(min(squares))
print(max(squares))
print(sum(squares))

# 列表解析
squares = [value**2 for value in range(1, 11)]
print(squares)
