# Kata: Count of positives / sum of negatives
# Difficulty: 8 kyu
# URL: https://www.codewars.com/kata/576bb71bbbcf0951d5000044
# Date: 2026-10-05
#
# Description:
# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and 
#  the second element is sum of negative numbers. 0 is neither positive nor negative.
# If the input is an empty array or is null, return an empty array.

def count_positives_sum_negatives(arr):
    if arr is None or len(arr)<1:
        return []
    
    add = sum([i for i in arr if i<0])
    count= len([i for i in arr if i>0])
    
    return[count, add]
