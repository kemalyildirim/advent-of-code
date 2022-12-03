
data = None
test_data = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

from common import readData

data = readData('data')

def solution(data):
    dataArr = data.split("\n")
    result = []
    tmp = 0
    for line in dataArr:
        if line != '':
            tmp += int(line)
        else:
            result.append(tmp)
            tmp = 0
    return max(result)



print(solution(data))