# 在为完成练习9-1而编写的程序中，添加一个名为number_served的属性，并将其默认值设置为0。根据这个类创建一个名为restaurant的实例。打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
# 添加一个名为set_number_served()的方法，让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
# 添加一个名为increment_number_served()的方法，让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。

class Restaurant:
    """一个简单的餐馆类"""
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """初始化餐馆的属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """打印餐馆的信息"""
        print(f"The name of the restaurant is：{self.restaurant_name}")
        print(f"The type of the restaurant is：{self.cuisine_type}")

    def open_restaurant(self):
        """打印一条消息，指出餐馆正在营业"""
        print(f"{self.restaurant_name} is open now!")

    def read_number_served(self):
        """打印一条消息，指出餐馆有多少人就餐过"""
        print(f"{self.restaurant_name} has served {self.number_served} people.")

    def set_number_served(self, number_served):
        """设置就餐人数"""
        self.number_served = number_served
        print(f"{self.restaurant_name} has served {self.number_served} people.")

    def increment_number_served(self, number_served):
        """将就餐人数递增"""
        self.number_served += number_served
        print(f"{self.restaurant_name} has served {self.number_served} people.")

restaurant = Restaurant("The Big One", "Chinese")
restaurant.read_number_served()
restaurant.set_number_served(100)
restaurant.increment_number_served(200)
