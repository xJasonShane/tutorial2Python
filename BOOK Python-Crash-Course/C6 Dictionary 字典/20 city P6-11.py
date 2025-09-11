# 创建一个名为cities的字典，将三个城市名用作键。对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。在表示每座城市的字典中，应包含country、population和fact等键。将每座城市的名字以及有关信息都打印出来。

cities = {
    'beijing': {
        'country': 'china',
        'population': 21540000,
        'fact': 'beijing is the capital of china',
    },
    'shanghai': {
        'country': 'china',
        'population': 24240000,
        'fact': 'shanghai is the capital of china',
    },
    'guangzhou': {
        'country': 'china',
        'population': 14040000,
        'fact': 'guangzhou is the capital of china',
    },
}

for city, info in cities.items():
    print(f"{city.title()}'s information is:")
    print(f"- Country: {info['country'].title()}")
    print(f"- Population: {info['population']}")
    print(f"- Fact: {info['fact']}")
    print('\n')
