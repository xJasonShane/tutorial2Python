# 在字典中可以使用get()方法来返回值，防止字典中没有该值报错
alien_0 = {"color": "green", "speed": "slow"}
point_value = alien_0.get('points','No point value assigned.')
print(point_value)
