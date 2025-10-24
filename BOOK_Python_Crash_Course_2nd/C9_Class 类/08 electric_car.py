class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """打印一条消息，指出汽车的里程"""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        拒绝将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

# 将实例用作属性
class Battery:
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=75):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

# 创建新类继承Car类
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """
        初始化父类的属性
        再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    
    # 重写父类的方法
    # Python允许在子类中定义与父类同名的方法，这称为方法重写（override）
    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar("Tesla", "Model S", 2022)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
