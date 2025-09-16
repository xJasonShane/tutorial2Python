# 创建一个Die类，它包含一个名为sides的属性，该属性的默认值为6。编写一个名为roll_die()的方法，它打印位于1和骰子面数之间的随机数。创建一个6面的骰子再掷10次。
# 创建一个10面的骰子和一个20面的骰子，再分别掷10次。

from random import randint

class Die():
    """表示一个骰子的类"""
    def __init__(self, sides=6):
        """初始化骰子"""
        self.sides = sides

    def roll_die(self):
        """返回一个位于1和骰子面数之间的随机数"""
        return randint(1, self.sides)

# 创建一个6面的骰子并掷10次
die_6 = Die()
for i in range(10):
    print(die_6.roll_die())

# 创建一个10面的骰子并掷10次
die_10 = Die(10)
for i in range(10):
    print(die_10.roll_die())

# 创建一个20面的骰子并掷10次
die_20 = Die(20)
for i in range(10):
    print(die_20.roll_die())
