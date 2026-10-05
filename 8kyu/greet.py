# Kata: Returning Strings
# Difficulty: 8 kyu
# URL: https://www.codewars.com/kata/55a70521798b14d4750000a4
# Date: 2026-10-05
#
# Description:
# Create a function that accepts a parameter representing a name and returns the message: 
#  "Hello, <name> how are you doing today?".

def greet(name):
    if name is None or type(name) != str:
        raise ValueError('Input must be a str')

    return f'Hello, {name} how are you doing today?'
