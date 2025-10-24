# 编写一个名为Privileges的类，它只有一个属性privileges，其中存储了练习9-7所述的字符串列表。将方法show_privileges()移到这个类中。在Admin类中，将一个Privileges实例用作其属性。创建一个Admin实例，并使用方法show_privileges()来显示其权限。

class Privileges:
    """一个类，用于存储管理员的权限"""
    def __init__(self, privileges):
        """初始化权限"""
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """显示管理员的权限"""
        print("The admin has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin = Privileges(['can add post', 'can delete post', 'can ban user'])
admin.show_privileges()
