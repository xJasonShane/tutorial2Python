# 冰激凌小店是一种特殊的餐馆。编写一个名为IceCreamStand的类，让它继承为完成练习9-1或练习9-4而编写的Restaurant类。这两个版本的Restaurant类都可以，挑选你更喜欢的那个即可。添加一个名为flavors的属性，用于存储一个由各种口味的冰激凌组成的列表。编写一个显示这些冰激凌的方法。创建一个IceCreamStand实例，并调用这个方法。

class Restaurant:
    """一个简单的餐馆类"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化餐馆的属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印餐馆的信息"""
        print(f"The name of the restaurant is：{self.restaurant_name}")
        print(f"The type of the restaurant is：{self.cuisine_type}")

    def open_restaurant(self):
        """打印一条消息，指出餐馆正在营业"""
        print(f"{self.restaurant_name} is open now!")

class IceCreamStand(Restaurant):
    """一个冰激凌小店"""
    def __init__(self, name, cuisine_type):
        """初始化冰激凌小店"""
        super().__init__(name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']
    
    def show_flavors(self):
        """显示冰淇淋的口味"""
        print("We have the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

ice = IceCreamStand("The Ice Cream Shop", "Ice Cream")
ice.show_flavors()
