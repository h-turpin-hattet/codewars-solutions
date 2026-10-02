# Kata: Even or Odd
# Difficulty: 8 kyu
# URL: https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
# Date: 2026-09-28
#
# Description:
# Create a function that takes an integer as an argument
# and returns "Even" for even numbers or "Odd" for odd numbers.


def even_or_odd(number):
    result=number%2
    if result==0:
        return 'Even'
    else:
        return 'Odd'