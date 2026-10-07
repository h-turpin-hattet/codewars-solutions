# Kata: Vowel Count
# Difficulty: 7 kyu
# URL: https://www.codewars.com/kata/54ff3102c1bad923760001f3
# Date: 2026-10-07
#
# Description:
# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

def get_count_extended(sentence):
    if sentence is None:
        raise ValueError('Input can not be None')
    elif not sentence:
        return 0

    vowels = ('a', 'e', 'i', 'o', 'u')
    count = 0
    for i in sentence:
        if i in vowels:
            count += 1

    return count

def get_count(sentence):
    if sentence is None:
        raise ValueError('Input can not be None')
    elif not sentence:
        return 0
    vowels = ('a', 'e', 'i', 'o', 'u')

    return len([i for i in sentence if i in vowels])
