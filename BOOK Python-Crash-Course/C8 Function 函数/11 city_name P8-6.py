# 编写一个名为city_country()的函数，它接受城市的名称及其所属的国家。这个函数应返回一个格式类似于下面的字符串：
# "Santiago, Chile"
# 至少使用三个城市国家对来调用这个函数，并打印它返回的值。

def city_country(city, country):
    """返回一个字符串，格式为'City, Country'"""
    return f"{city.title()}, {country.title()}"

print(city_country("santiago", "chile"))
print(city_country("paris", "france"))
print(city_country("tokyo", "japan"))
