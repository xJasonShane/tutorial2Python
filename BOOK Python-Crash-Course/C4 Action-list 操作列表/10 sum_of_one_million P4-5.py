# 创建一个包含数1～1 000000的列表，再使用min() 和max() 核实该列表确实是从1开始、到1 000 000结束的。另外，对这个列表调用函数sum() ，看看Python将一百万个数相加需要多长时间。

numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
