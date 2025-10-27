"""
@-*- coding: utf-8 -*-
@ filename:01_Five_tips
@ author:JasonShane
"""

# tip1 following PEP
my_score: int = 0
print(my_score)
x: list[str] = ['a', 'b']

print('hello')

# tip2 prioritizing readability
# def f(n: int) -> int:
#     return 1 if n < 2 else (lambda f, n: f(f, n))(lambda f, n: n * f(f, n - 1) if n > 1 else 1, n)
#
# print(f(10))

def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if number == 0 or number == 1:
        return 1

    result: int = 1
    for i in range(2, number + 1):
        result *= i

    return result

print(factorial(10))

# tip3 and tip4 mypy
my_number: int = 10
print(my_number)

numbers: list[int] = [1, 2, 3, 4]
print(max(numbers))

# tip5 read the documentation