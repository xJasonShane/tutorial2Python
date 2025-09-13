# 编写一个函数，将一辆汽车的信息存储在字典中。这个函数总是接受制造商和型号，还接受任意数量的关键字实参。这样调用该函数：提供必不可少的信息，以及两个名称值对，如颜色和选装配件。这个函数必须能够像下面这样进行调用：
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# 打印字典即可确认信息是否正确。

def make_car(manufacturer, model, **car_info):
    """创建一个字典，其中包含有关一辆汽车的信息"""
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

car = make_car('audi', 'a4', color='red', year=2023)
print(car)
