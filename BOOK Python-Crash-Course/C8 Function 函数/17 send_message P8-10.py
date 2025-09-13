# 在你为完成练习8-9而编写的程序中，编写一个名为send_messages()的函数，将每条消息都打印出来并移到一个名为sent_messages的列表中。调用函数send_messages()，再将两个列表都打印出来，确认正确地移动了消息。

def show_messages(messages):
    """打印列表中的每条文本消息"""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """打印列表中的每条文本消息并将其移到sent_messages列表中"""
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)
        print(f"Messages left: {messages}")
        print(f"Sent messages: {sent_messages}")
        print("\n")
