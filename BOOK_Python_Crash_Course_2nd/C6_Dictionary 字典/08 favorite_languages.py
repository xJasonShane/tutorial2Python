favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

# 打印每个人的姓名和喜欢的语言
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

# 遍历字典的键
for name in favorite_languages.keys():
    print(name.title())

# 遍历字典的值
for language in favorite_languages.values():
    print(language.title())
