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

def find_badge_in_rucksacks(rucksacks: list) -> str:
    badge = set.intersection(*map(set, rucksacks))
    return badge.pop()

def solution(data: str) -> int:
    total = 0
    data = data.split("\n")
    badges = []
    for i in range(0, len(data), 3):
        rucksack_group = [data[i], data[i+1], data[i+2]]
        badge = find_badge_in_rucksacks(rucksack_group)
        badges.append(badge)
    for badge in badges:
        total += priority(badge)
    return total

print(solution(data))