# 你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
# 以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条print 语句，指出你找到了一个更大的餐桌。
# 使用insert() 将一位新嘉宾添加到名单开头。
# 使用insert() 将另一位新嘉宾添加到名单中间。
# 使用append() 将最后一位新嘉宾添加到名单末尾。
# 打印一系列消息，向名单中的每位嘉宾发出邀请。

guest_list = ["Swan Chin", "Yung-Lo Emperor", "Jackie Chan"]
print(f"Hello, {guest_list[0]}! You are cordially invited to dinner.")
print(f"Hello, {guest_list[1]}! You are cordially invited to dinner.")
print(f"Hello, {guest_list[2]}! You are cordially invited to dinner.")

print("\nI found a bigger table!")

guest_list.insert(0, "Amelia")
guest_list.insert(2, "Chin")
guest_list.append("Chan")

print(f"Hello, {guest_list[0]}! You are cordially invited to dinner.")
print(f"Hello, {guest_list[1]}! You are cordially invited to dinner.")
print(f"Hello, {guest_list[2]}! You are cordially invited to dinner.")
print(f"Hello, {guest_list[3]}! You are cordially invited to dinner.")
print(f"Hello, {guest_list[4]}! You are cordially invited to dinner.")
print(f"Hello, {guest_list[5]}! You are cordially invited to dinner.")
