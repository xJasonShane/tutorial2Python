def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

# 调用函数
filename = 'BOOK Python-Crash-Course/C10 Files-and-exceptions 文件和异常/alice.txt'
count_words(filename)
