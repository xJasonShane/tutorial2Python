# 编写一个名为make_shirt()的函数，它接受一个尺码以及要印到T恤上的字样。这个函数应打印一个句子，概要地说明T恤的尺码和字样。
# 使用位置实参调用该函数来制作一件T恤，再使用关键字实参来调用这个函数。

def make_shirt(size, message):
    """打印T恤的尺码和字样"""
    print(f"\nI'm going to make a {size} T-shirt.")
    print(f'It will say, "{message}"')

make_shirt("medium", "I love Python")
make_shirt(size="small", message="I love C++")
