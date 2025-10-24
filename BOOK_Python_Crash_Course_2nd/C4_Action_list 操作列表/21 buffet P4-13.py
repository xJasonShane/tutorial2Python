# 有一家自助式餐馆，只提供五种简单的食品。请想出五种简单的食品，并将其存储在一个元组中。
# 使用一个for 循环将该餐馆提供的五种食品都打印出来。
# 尝试修改其中的一个元素，核实Python确实会拒绝你这样做。
# 餐馆调整了菜单，替换了它提供的其中两种食品。请编写一个这样的代码块：给元组变量赋值，并使用一个for循环将新元组的每个元素都打印出来。

foods = ('pizza', 'falafel', 'carrot cake', 'ice cream', 'bread')
print("Original foods:")
for food in foods:
    print(food)

foods = ('pizza', 'falafel', 'noodles', 'ice cream', 'steak')
print("\nOriginal foods:")
for food in foods:
    print(food)
