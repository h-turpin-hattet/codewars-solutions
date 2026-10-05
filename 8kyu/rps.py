# Kata: Rock Paper Scissors!
# Difficulty: 8 kyu
# URL: https://www.codewars.com/kata/5672a98bdbdd995fad00000f
# Date: 2026-10-05
#
# Description:
# Rules of the "Rock, Paper, Scissors" game are:
#  Rock beats Scissors,
#  Scissors beat Paper,
#  Paper beats Rock,
#  Two identical moves are a draw.
# 
# Let's play! You will be given valid moves of two Rock, Paper, Scissors players,
#  and have to return which player won: "Player 1 won!" for player 1, 
#  and "Player 2 won!" for player 2. In case of a draw return Draw!.

def rps(p1,p2):
    wins = {
        'scissors' : 'paper',
        'rock' : 'scissors',
        'paper' : 'rock'
    }
    if p1 == p2:
        return 'Draw!'
    elif wins[p1] == p2:
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'


