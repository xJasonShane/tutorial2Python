# 想出至少5个你渴望去旅游的地方。
# 将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
# 按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始Python列表。
# 使用sorted() 按字母顺序打印这个列表，同时不要修改它。再次打印该列表，核实排列顺序未变。
# 使用sorted() 按与字母顺序相反的顺序打印这个列表，同时不要修改它。再次打印该列表，核实排列顺序未变。
# 使用reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
# 使用reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
# 使用sort() 修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
# 使用sort() 修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。

location = ['beijing', 'shanghai', 'Nara', 'London', 'Maldives']
print(location)

# 临时排序
print(sorted(location))
print(location)
# 反向临时排序
print(sorted(location, reverse=True))
print(location)

# 反转排序
location.reverse()
print(location)
# 再次反转
location.reverse()
print(location)

# 永久排序
location.sort()
print(location)
# 反向永久排序
location.sort(reverse=True)
print(location)
