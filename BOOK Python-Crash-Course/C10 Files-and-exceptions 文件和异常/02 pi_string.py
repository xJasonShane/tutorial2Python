filepath = 'BOOK Python-Crash-Course/C10 Files-and-exceptions 文件和异常/pi_digits.txt'
with open(filepath) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
