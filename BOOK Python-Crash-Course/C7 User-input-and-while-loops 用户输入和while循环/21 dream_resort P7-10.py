# 编写一个程序，调查用户梦想的度假胜地。使用类似于下面的提示，并编写一个打印调查结果的代码块。
# If you could visit one place in the world, where would you go?

prompt = "If you could visit one place in the world, where would you go? "
response = ""
responses = []

while response != 'quit':
    response = input(prompt)
    responses.append(response)

print("\n--- Poll Results ---")
for response in responses:
    print(response)
