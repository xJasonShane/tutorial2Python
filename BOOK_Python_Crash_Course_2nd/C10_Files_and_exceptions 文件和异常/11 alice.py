filepath = 'BOOK Python-Crash-Course/C10 Files-and-exceptions 文件和异常/alice.txt'

try:
    with open(filepath, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filepath} does not exist.")
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print(f"The file {filepath} has about {num_words} words.")
