# 创建一个名为favorite_places 的字典。在这个字典中，将三个人的名字用作键，并存储每个人喜欢的1～3个地方。为了让这个练习更有趣些，可以让一些朋友说出他们喜欢的几个地方。遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。

favorite_places = {
    'li': ['beijing', 'shanghai', 'guangzhou'],
    'si': ['guangzhou', 'shanghai', 'shenzhen'],
    'wu': ['shenzhen', 'guangzhou', 'beijing'],
}

for name, places in favorite_places.items():
    print(f"{name}'s favorite place is:")
    for place in places:
        print(f"- {place}")
