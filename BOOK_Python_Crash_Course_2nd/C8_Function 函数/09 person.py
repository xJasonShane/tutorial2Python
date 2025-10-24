def build_person(first, last):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {"first": first, "last": last}
    return person

musician = build_person("jason", "shane")
print(musician)

# 可选实参
def build_person(first, last, age=None):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {"first": first, "last": last}
    if age:
        person["age"] = age
    return person

musician = build_person("jason", "shane", 27)
print(musician)
