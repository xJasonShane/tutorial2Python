# 编写一个循环，提示用户输入一系列比萨配料，并在用户输入'quit'时结束循环。每当用户输入一种配料后，都打印一条消息，指出我们会在比萨中添加这种配料。

prompt = "\nPlease enter some pizza toppings:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")
