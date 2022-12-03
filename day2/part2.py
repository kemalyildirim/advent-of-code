import sys
sys.path.append("../")

test_data = """
A Y
B X
C Z
"""
from commons import readData
data = readData("data")

RULE = {
        'Rock' : 'Scissors',
        'Scissors' : 'Paper',
        'Paper' : 'Rock'
    }

def get_key(dictionary: dict, value):
    for k, v in dictionary.items():
        if v == value:
            return k

def calculatePoints(opponent, me):
    oppMap = {
        'A' : 'Rock',
        'B' : 'Paper',
        'C' : 'Scissors'
    }
    myMap = {
        'X' : 'LOSE',
        'Y' : 'DRAW',
        'Z' : 'WIN'
    }
    pointsByShape = {
        'Rock' : 1,
        'Paper' : 2,
        'Scissors' : 3
    }
    print(f"opp: {oppMap[opponent]}")
    print(f"me: {myMap[me]}")
    if me == 'X': # lose
        currentPoints = pointsByShape[RULE[oppMap[opponent]]]
        print("lose\n")
        return 0 + currentPoints
    elif me == 'Y': # draw
        currentPoints = pointsByShape[oppMap[opponent]]
        print("draw\n")
        return 3 + currentPoints
    else: # win
        currentPoints = pointsByShape[get_key(RULE, oppMap[opponent])]
        print("win\n")
        return 6 + currentPoints

def solution(data):
    dataArr = [i for i in data.split("\n") if i]
    points = 0
    for l in dataArr:
        opp, me = l.split(" ")
        points += calculatePoints(opp, me)
    return points

print(solution(data))