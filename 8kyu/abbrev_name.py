# Kata: Abbreviate a Two Word Name
# Difficulty: 8 kyu
# URL: https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
# Date: 2026-10-03
#
# Description:
# Write a function to convert a name into initials.
# This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.

def abbrev_name(name):
    if name is None or len(name.split(' '))!=2:
        raise ValueError('Input must contain exactly two words')

    name_liste = name.split()
       
    return f'{name_liste[0][0].upper()}.{name_liste[1][0].upper()}'