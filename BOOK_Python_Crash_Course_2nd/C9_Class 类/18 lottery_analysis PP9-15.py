# 可以使用一个循环来明白前述彩票大奖有多难中奖。为此，创建一个名为my_ticket的列表或元组，再编写一个循环，不断地随机选择数或字母，直到中大奖为止。请打印一条消息，报告执行循环多少次才中了大奖。

from random import sample

# 创建一个列表或元组，其中包含10个数和5个字母
lottery = list(range(10)) + list('abcde')

# 从列表或元组中随机选择4个数或字母
winners = sample(lottery, 4)

# 打印一条消息，指出只要彩票上是这4个数或字母，就中大奖了
print("The winning lottery tickets for this period are:" + str(winners))

# 创建一个名为my_ticket的列表或元组
my_ticket = sample(lottery, 4)

# 编写一个循环，不断地随机选择数或字母，直到中大奖为止
count = 0
while my_ticket != winners:
    my_ticket = sample(lottery, 4)
    count += 1

# 打印一条消息，报告执行循环多少次才中了大奖
print("It took " + str(count) + " tries to win the lottery.")
