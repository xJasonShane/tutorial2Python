# 创建一个列表或元组，其中包含10个数和5个字母。从这个列表或元组中随机选择4个数或字母，并打印一条消息，指出只要彩票上是这4个数或字母，就中大奖了。

from random import sample

# 创建一个列表或元组，其中包含10个数和5个字母
lottery = list(range(10)) + list('abcde')

# 从列表或元组中随机选择4个数或字母
winners = sample(lottery, 4)

# 打印一条消息，指出只要彩票上是这4个数或字母，就中大奖了
print("The winning lottery tickets for this period are:" + str(winners))
