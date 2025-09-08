# 按下面的说明编写一个程序，模拟网站如何确保每位用户的用户名都独一无二。
# 创建一个至少包含5个用户名的列表，并将其命名为current_users。
# 再创建一个包含5个用户名的列表，将其命名为new_users，并确保其中有一两个用户名也包含在列表current_users中。
# 遍历列表new_users，对于其中的每个用户名，都检查它是否已被使用。
# 如果是，就打印一条消息，指出需要输入别的用户名；
# 否则，打印一条消息，指出这个用户名未被使用。
# 确保比较时不区分大小写。换句话说，如果用户名'John'已被使用，应拒绝用户名'JOHN'。​（为此，需要创建列表current_users的副本，其中包含当前所有用户名的小写版本。​）

current_users = ['admin', 'guest', 'user1', 'user2', 'user3']
new_users = ['admin', 'guest', 'user4', 'user5', 'user6']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'Username {new_user} is already taken. Please enter a new username.')
    else:
        print(f'Username {new_user} is available.')
