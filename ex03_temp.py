import numpy as np

count = 0


def conflict(pos, chess):
    len_chess = len(chess)
    for i in range(len_chess):
        if abs(chess[i] - pos) in (0, len_chess - i):
            return True
    return False


def printgrip(chess, n):
    lst = n * [n * ['.']]
    grip = np.array(lst)
    for i in range(n):
        grip[i][chess[i]] = 1
    print(grip)


def solve(n, chess):
    global count
    if len(chess) == n:
        count += 1
        printgrip(chess, n)
    else:
        for pos in range(n):
            if not conflict(pos, chess):
                chess1 = []
                for i in chess:
                    chess1.append(i)
                chess1.append(pos)
                solve(n, chess1)


board = []
solve(8, board)
print('The number of schemes is ' + str(count) + '.')
