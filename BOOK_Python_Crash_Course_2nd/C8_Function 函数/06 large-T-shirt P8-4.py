# 修改函数make_shirt()，使其在默认情况下制作一件印有“I love Python”字样的大号T恤。调用这个函数来制作：一件印有默认字样的大号T恤，一件印有默认字样的中号T恤，以及一件印有其他字样的T恤（尺码无关紧要）​。

def make_shirt(size="large", message="I love Python"):
    """打印T恤的尺码和字样"""
    print(f"\nI'm going to make a {size} T-shirt.")
    print(f'It will say, "{message}"')

make_shirt()
make_shirt(size="medium")
make_shirt("small", "I love C++")
