import numpy as np


result = []


def printgrip(chess, n):

    lst = n * [n * ['1']]
    grip = np.array(lst)
    for i in range(n):
        grip[i][chess[i]] = 'Q'
    print(grip)


def conflict(pos, chess):
    len_chess = len(chess)

    for i in range(len_chess):
        if abs(chess[i] - pos) in (0, len_chess - i):
            return True
    return False


def solve(n, chess):
    if len(chess) == n:
        result.append(chess)

    else:
        for pos in range(n):
            if not conflict(pos, chess):
                chess1 = []
                for i in chess:
                    chess1.append(i)
                chess1.append(pos)
                solve(n, chess1)


solve(8, [])
for i in result:
    printgrip(i, 8)
    more = input('More?')
    if more == 'more':
        continue
    else:
        break

