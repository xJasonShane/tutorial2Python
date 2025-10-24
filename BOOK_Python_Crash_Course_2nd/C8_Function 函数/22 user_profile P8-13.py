# 复制前面的程序user_profile.py，在其中调用build_profile() 来创建有关你的简介。调用这个函数时，指定你的名和姓，以及三个描述你的键值对。
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile("albert", "einstein", location="princeton", field="physics")
print(user_profile)

user_profile = build_profile("marie", "curie", location="paris", field="chemistry")
print(user_profile)

user_profile = build_profile("nikola", "tesla", location="prague", field="electronics")
print(user_profile)
