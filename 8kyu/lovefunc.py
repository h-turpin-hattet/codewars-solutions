# Kata: Opposites Attract
# Difficulty: 8 kyu
# URL: https://www.codewars.com/kata/555086d53eac039a2a000083
# Date: 2026-10-05
#
# Description:
#Timmy & Sarah think they are in love, but around where they live,
# they will only know once they pick a flower each.
#If one of the flowers has an even number of petals and the other has an odd number of petals,
# it means they are in love.
#Write a function that will take the number of petals of each flower and 
# return true if they are in love and false if they aren't.

def lovefunc(flower1, flower2):
    if flower1 is None or flower2 is None or type(flower1) != int or type(flower2) != int:
        raise ValueError('Input must contain at least one integer per flower')

    return flower1 % 2 != flower2 % 2