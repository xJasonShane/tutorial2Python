# 在为完成练习6-1而编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为people的列表中。遍历这个列表，将其中每个人的所有信息都打印出来。

people = [
    {
    'first_name': 'li',
    'last_name': 'si',
    'age': 20,
    'city': 'beijing',
    },
    {
    'first_name': 'wang',
    'last_name': 'wu',
    'age': 21,
    'city': 'shanghai',
    },
    {
    'first_name': 'zhao',
    'last_name': 'sun',
    'age': 22,
    'city': 'guangzhou',
    },
]

for person in people:
    print(person)
    print(person['first_name'])
    print(person['last_name'])
    print(person['age'])
    print(person['city'])
    print('\n')
