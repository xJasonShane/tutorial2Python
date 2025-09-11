# 创建多个表示宠物的字典，每个字典都包含宠物的类型及其主人的名字。将这些字典存储在一个名为pets 的列表中，再遍历该列表，并将有关每个宠物的所有信息都打印出来。

pets = [
    {
    'type': 'dog',
    'owner_name': 'li',
    },
    {
    'type': 'cat',
    'owner_name': 'si',
    },
    {
    'type': 'rabbit',
    'owner_name': 'wu',
    },
]

for pet in pets:
    print(pet)
    print(pet['type'])
    print(pet['owner_name'])
    print('\n')

# 遍历字典中的所有键值对
for pet in pets:
    for key, value in pet.items():
        print(key)
        print(value)
        print('\n')
