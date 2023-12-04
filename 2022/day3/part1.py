import sys
sys.path.insert(0, "../")

from commons import readData
data = readData("data")

test_data= """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

def priority(char: str) -> int:
    # ASCII value of uppercase A -> 65, lowercase a -> 97
    if len(char) != 1:
        raise Exception("char length is not 1")
    if char.isupper():
        return ord(char) - 65 + 27
    return ord(char) - 96

def find_duplicates_in_rucksack(rucksack: str) -> list:
    charMap = {}
    dups = []
    size = len(rucksack)
    for i in rucksack[:size//2]:
        charMap[i] = 1
    for i in rucksack[size//2:]:
        if i in charMap.keys():
            if charMap[i] == 1:
                charMap[i] += 1
                dups.append(i)
    return dups

def solution(data: str) -> int:
    total = 0
    data = data.split("\n")
    for i in data:
        dups = find_duplicates_in_rucksack(i)
        for dup in dups:
            total += priority(dup)
    return total

print(solution(data))