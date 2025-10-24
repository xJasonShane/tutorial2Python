def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

'''
位置形参对于传入实参的顺序很重要
'''
describe_pet("hamster", "harry")
describe_pet("dog", "willie")

'''
关键字传参
'''
describe_pet(animal_type="hamster", pet_name="harry")
describe_pet(pet_name="willie", animal_type="dog")

'''
函数参数默认值
'''
def describe_pet(pet_name, animal_type="dog"):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name="willie")
describe_pet(pet_name="harry", animal_type="hamster")
