# Kata: Sum without highest and lowest number
# Difficulty: 8 kyu
# URL: https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
# Date: 2026-10-02
#
# Description:
# Sum all the numbers of a given array ( cq. list ),
# except the highest and the lowest element ( by value, not by index! ).
#The highest or lowest element respectively is a single element at each edge, 
#even if there are more than one with the same value.
#
#Input validation:
#If an empty value ( null, None, Nothing, nil etc. ) is given instead of an array, 
#or the given array is an empty list or a list with only 1 element, return 0.

def sum_array(arr):
    if arr is None or len(arr) < 3 or not all(type(i)==int for i in arr):
        return 0

    arr.remove(min(arr))
    arr.remove(max(arr))
    results = sum(arr)
    
    return results

