import sys
sys.path.append("../")

# A or X -> Rock
# B or Y -> Paper
# C or Z -> Scissors

# Rock score = 1 Paper score = 2 Scissors score = 3
# Lost 0, Won 6, Draw 3

test_data = """
A Y
B X
C Z
"""
from commons import readData
data = readData("data")

def whoWins(player1, player2):
    rule = {
        'Rock' : 'Scissors',
        'Scissors' : 'Paper',
        'Paper' : 'Rock'
    }
    if rule[player1] == player2:
        return player1
    else:
        return player2

def calculatePoints(opponent, me):
    oppMap = {
        'A' : 'Rock',
        'B' : 'Paper',
        'C' : 'Scissors'
    }
    myMap = {
        'X' : 'Rock',
        'Y' : 'Paper',
        'Z' : 'Scissors'
    }
    pointsByShape = {
        'Rock' : 1,
        'Paper' : 2,
        'Scissors' : 3
    }
    currentPoints = pointsByShape[myMap[me]]
    if oppMap[opponent] == myMap[me]: # draw
        return 3 + currentPoints
    winner = whoWins(oppMap[opponent], myMap[me])
    if winner == oppMap[opponent]:
        return 0 + currentPoints
    else:
        return 6 + currentPoints

def solution(data):
    dataArr = [i for i in data.split("\n") if i]
    points = 0
    for l in dataArr:
        opp, me = l.split(" ")
        points += calculatePoints(opp, me)
    return points


print(solution(data))