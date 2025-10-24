# 创建一个名为Restaurant的类，为其方法__init__()设置属性restaurant_name和cuisine_type。创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
# 根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法。

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

restaurant = Restaurant("The Great Wall", "Chinese")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
