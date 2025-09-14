# 根据为完成练习9-1而编写的类创建三个实例，并对每个实例调用方法describe_restaurant()。

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

restaurant1 = Restaurant("The Great Wall", "Chinese")
restaurant2 = Restaurant("The Palace", "French")
restaurant3 = Restaurant("The Plaza", "Italian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
