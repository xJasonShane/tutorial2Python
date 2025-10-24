bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

# 访问列表第一元素
print(bicycles[0])
# 访问列表第一元素的标题格式
print(bicycles[0].title())

print(bicycles[1])
print(bicycles[3])

# 访问列表最后一个元素
print(bicycles[-1])

bicycles = ['trek','cannondale','redline','specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
