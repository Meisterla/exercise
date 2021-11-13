import numpy as np

# grid = [[0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0]]

#grid = [0, 0, 0, 0, 0, 0, 0, 0]
grid = [0, 0, 0, 0]
n = 4


def possible(col, row):
    if len(set(col[:row + 1])) != len(col[:row + 1]):  # 检查列
        return False

    for i in range(row):  # 检查对角线
        if abs(col[i] - col[row]) == int(row - i):
            return False
    return True


def print_grip(col, n):
    print
    col, '\n'
    for row in range(n):
        line = ""
        for column in range(n):
            if col[row] == column:
                line += " Q "
            else:
                line += " * "
        print(line)
    print('\n')


def solve(row):  # row:当前行，col:每一行皇后的位置 n为总行数
    global grid
    global n
    if row == n:
        print_grip(grid, n)  # 到最后一行，打印结果
        return

    for row_position in range(n):
        grid[row] = row_position  # row_position皇后所在列的位置
        if possible(grid, row):
            solve(row + 1)


solve(0)