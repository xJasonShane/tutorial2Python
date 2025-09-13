# 修改你为完成练习8-10而编写的程序，在调用函数send_messages()时，向它传递消息列表的副本。调用函数send_messages()后，将两个列表都打印出来，确认保留了原始列表中的消息。

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
        print(f"Message sent: {current_message}")
        print(f"Messages left: {messages}")
        print(f"Sent messages: {sent_messages}")
        print("\n")
