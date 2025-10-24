# 在6.3.1节编写的程序favorite_languages.py中执行以下操作。
# 创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。遍历这个人员名单。对于已参与调查的人，打印一条消息表示感谢；对于还未参与调查的人，打印一条消息邀请他参加。

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

investigator = ['jen', 'sarah']
for name in favorite_languages.keys():
    if name in investigator:
        print(f"Thanks {name.title()}!")
    else:
        print(f"{name.title()}, please take our poll!")
