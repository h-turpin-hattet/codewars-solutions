# Kata: Remove String Spaces
# Difficulty: 8 kyu
# URL: https://www.codewars.com/kata/57eae20f5500ad98e50002c5
# Date: 2026-10-05
#
# Description:
#Write a function that removes the spaces from the string, then return the resultant string.

def no_space(x):
    if x is None or len(x.strip())<1:
        raise ValueError('Input must contain at leas one character')   
    
    return ''.join(x.split())



