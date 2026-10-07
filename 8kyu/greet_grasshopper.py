# Kata: Grasshopper - Personalized Message
# Difficulty: 8 kyu
# URL: https://www.codewars.com/kata/5772da22b89313a4d50012f7
# Date: 2026-10-07
#
# Description:
# Create a function that gives a personalized greeting.
# This function takes two parameters: name and owner.
# Use conditionals to return the proper message:
#  name equals owner	'Hello boss'
#  otherwise	'Hello guest

def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    else:
        return 'Hello guest'

def greet_v2(name, owner):
    return 'Hello boss' if name == owner else 'Hello guest'

def greet_v3(name, owner):
    return f'Hello {'boss' if name == owner else 'guest'}'