# 在为完成练习9-3而编写的User类中，添加一个名为login_attempts的属性。编写一个名为increment_login_attempts()的方法，将属性login_attempts的值加1。再编写一个名为reset_login_attempts()的方法，将属性login_attempts的值重置为0。
# 根据User类创建一个实例，再调用方法increment_login_attempts()多次。打印属性login_attempts的值，确认它被正确地递增。然后，调用方法reset_login_attempts()，并再次打印属性login_attempts的值，确认它被重置为0。

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

    def print_login_attempts(self):
        """打印用户的登录尝试次数"""
        print(f"{self.first_name} {self.last_name} has tried to log in {self.login_attempts} times.")

    def increment_login_attempts(self):
        """将属性login_attempts的值加1"""
        self.login_attempts += 1
        self.print_login_attempts()

    def reset_login_attempts(self):
        """将属性login_attempts的值重置为0"""
        self.login_attempts = 0
        self.print_login_attempts()
        print(f"{self.first_name} {self.last_name} has tried to log in {self.login_attempts} times.")

user = User("John", "Doe", 25, "male", "john.doe@example.com")
user.login_attempts = 0
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()
