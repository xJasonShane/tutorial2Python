# 你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
# 以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
# 使用pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。
# 每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐。
# 对于余下两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
# 使用del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。

guest_list = ["Amelia", "Swan Chin", "Chin", "Yung-Lo Emperor", "Jackie Chan", "Chan"]
print("Sorry guys, my new table won't arrive on time, so I can still only invite two guests to dinner.")
remove_guest = guest_list.pop()
print(f"Sorry, {remove_guest}, I can't invite you to dinner.")
remove_guest = guest_list.pop()
print(f"Sorry, {remove_guest}, I can't invite you to dinner.")
remove_guest = guest_list.pop()
print(f"Sorry, {remove_guest}, I can't invite you to dinner.")
remove_guest = guest_list.pop()
print(f"Sorry, {remove_guest}, I can't invite you to dinner.")

print(f"Hello, {guest_list[0]}! You are cordially invited to dinner.")
print(f"Hello, {guest_list[1]}! You are cordially invited to dinner.")

del guest_list[0]
del guest_list[0]

print(guest_list)
