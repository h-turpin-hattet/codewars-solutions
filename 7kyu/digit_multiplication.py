# Kata: Multiply Adjacent Digits
# Difficulty: 7 kyu
# URL: https://www.codewars.com/kata/67191920c29c7e09d9f40707
# Date: 2026-10-06
#
# Description:
# Multiply the adjacent digits which are not separated by a '-' or a '+' in a string,
#  then do the sum.

# Two approaches to solve this kata:

import re

# Version 1 - checks the VALUE of each element:
#   Iterates over the list and checks if the element is '+' or '-'.
#   More robust: does not depend on the position of elements in the list.

def digit_multiplication(expression):
    result = re.findall('\d+|[+-]',expression)
    operateur = '+'
    total = 0
    for i in result:
        if i == '+' or i =='-':
            operateur = i
        else:
            product = 1
            for x in i: 
                product *= int(x)
            if operateur == '+':
                total += product
            elif operateur == '-':
                total -= product

    return total

# Version 2 - checks the INDEX with enumerate():
#   Uses the fact that numbers are always at even indexes (0, 2, 4...)
#   and operators at odd indexes (1, 3, 5...).
#   Less robust: depends on the structure of the list.
def digit_multiplication_v2(expression):
    result = re.findall('\d+|[+-]',expression)
    operateur = '+'
    total = 0
    for i, val in enumerate(result):
        if i%2 == 0:
            product = 1
            for x in val: 
                product *= int(x)
            if operateur == '+':
                total += product
            elif operateur == '-':
                total -= product
        else:
            operateur = val

    return total

# Conclusion: v1 is preferred for readability and robustness.