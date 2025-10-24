# 你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
# 以完成练习3-4时编写的程序为基础，在程序末尾添加一条print 语句，指出哪位嘉宾无法赴约。修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
# 再次打印一系列消息，向名单中的每位嘉宾发出邀请。

guest_list = ["Swan Chin", "Yung-Lo Emperor", "Jackie Chan"]
print(f"Hello, {guest_list[0]}! You are cordially invited to dinner.")
print(f"Hello, {guest_list[1]}! You are cordially invited to dinner.")
print(f"Hello, {guest_list[2]}! You are cordially invited to dinner.")

print(f"\n{guest_list[1]} can't make it to dinner.")

guest_list[1] = "Amelia"
print(f"Hello, {guest_list[1]}! You are cordially invited to dinner.")
