# 管理员是一种特殊的用户。编写一个名为Admin的类，让它继承为完成练习9-3或练习9-5而编写的User 类。添加一个名为privileges的属性，用于存储一个由字符串（如"can add post" 、"can delete post" 、"can ban user" 等）组成的列表。编写一个名为show_privileges()的方法，显示管理员的权限。创建一个Admin实例，并调用这个方法。

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

class Admin(User):
    """一个管理员类"""
    def __init__(self, first_name, last_name, age, sex, email):
        """初始化管理员的属性"""
        super().__init__(first_name, last_name, age, sex, email)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """显示管理员的权限"""
        print("The admin has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin = Admin("John", "Doe", 25, "male", "john.doe@example.com")
admin.show_privileges()
admin.describe_user()
admin.greet_user()
