# 创建一个名为User的类，其中包含属性first_name和last_name，以及用户简介通常会存储的其他几个属性。在类User中定义一个名为describe_user()的方法，用于打印用户信息摘要。再定义一个名为greet_user()的方法，用于向用户发出个性化的问候。
# 创建多个表示不同用户的实例，并对每个实例调用上述两个方法。

class User:
    """一个简单的用户类"""
    def __init__(self, first_name, last_name, age, sex, email):
        """初始化用户的属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.email = email

    def describe_user(self):
        """打印用户的信息"""
        print(f"The name of the user is：{self.first_name} {self.last_name}")
        print(f"The age of the user is：{self.age}")
        print(f"The sex of the user is：{self.sex}")
        print(f"The email of the user is：{self.email}")

    def greet_user(self):
        """打印一条消息，向用户发出个性化的问候"""
        print(f"Hello, {self.first_name} {self.last_name}!")

user1 = User("John", "Doe", 25, "male", "john.doe@example.com")
user2 = User("Jane", "Doe", 23, "female", "jane.doe@example.com")
user3 = User("Jim", "Beam", 27, "male", "jim.beam@example.com")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
