# Kata: Find the smallest integer in the array
# Difficulty: 8 kyu
# URL: https://www.codewars.com/kata/55a2d7ebe362935a210000b2
# Date: 2026-10-05
#
# Description:
# Given an array of integers your solution should find the smallest integer.
# You can assume, for the purpose of this kata, that the supplied array will not be empty.

def find_smallest_int(arr):
    if not all(type(i) == int for i in arr):
        raise ValueError('Array must contain only integer')
    
    return min(arr)