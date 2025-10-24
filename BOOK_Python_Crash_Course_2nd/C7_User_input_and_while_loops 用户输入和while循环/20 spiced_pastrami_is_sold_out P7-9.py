# 使用为完成练习7-8而创建的列表sandwich_orders，并确保'pastrami'在其中至少出现了三次。在程序开头附近添加这样的代码：打印一条消息，指出熟食店的五香烟熏牛肉（pastrami）卖完了；再使用一个while循环将列表sandwich_orders中的'pastrami'都删除。确认最终的列表finished_sandwiches未包含'pastrami'。

sandwich_orders = ['tuna', 'blt', 'chicken', 'roast beef', 'veggie', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)
