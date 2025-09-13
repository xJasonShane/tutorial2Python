# 创建一个列表，其中包含一系列简短的文本消息。将该列表传递给一个名为show_messages()的函数，这个函数会打印列表中的每条文本消息。

def show_messages(messages):
    """打印列表中的每条文本消息"""
    for message in messages:
        print(message)

messages = ["Hello, world!", "How are you?", "I'm fine, thanks!"]
show_messages(messages)
