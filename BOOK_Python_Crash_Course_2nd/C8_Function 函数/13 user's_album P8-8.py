# 在为完成练习8-7编写的程序中，编写一个while循环，让用户输入专辑的歌手和名称。获取这些信息后，使用它们来调用函数make_album() 并将创建的字典打印出来。在这个while循环中，务必提供退出途径。

def make_album(artist, title, tracks=None):
    """创建一个描述音乐专辑的字典"""
    album = {"artist": artist, "title": title}
    if tracks:
        album["tracks"] = tracks
    return album

# 无限循环，直到用户退出
while True:
    print("\nPlease tell me the name of the artist and the title of the album:")
    print("(Enter 'quit' at any time to quit)")

    artist = input("Artist name: ")
    if artist == 'quit':
        break

    title = input("Album title: ")
    if title == 'quit':
        break

    album = make_album(artist, title)
    print(album)
