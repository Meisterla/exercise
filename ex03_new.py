grid = [0, 0, 0, 0, 0, 0, 0, 0]  # Create a list to collect results, the index of each element as row,
# the value of each element as column.
n = 8  # Set the number of rows, columns and queens.


def possible(col, row):
    if len(set(col[:row + 1])) != len(col[:row + 1]):  # 检查列
        return False
    for i in range(row):  # 检查对角线
        if col[i] - col[row] == int(row - i) or col[row] - col[i] == int(row - i):
            return False
    return True


def print_grip(grid, n):
    for row in range(n):
        line = ''
        for column in range(n):
            if grid[row] == column:
                line += 'Q '
            else:
                line += '. '
        print(line)
    input('More?')


def queen(row):
    global grid  # Use global variables.
    global n
    if row == n:  # If the queen position in the last row is determined, print it.
        print_grip(grid, n)  # Print it as a matrix.
        return  # Return and find the next case recursively.
    for row_position in range(n):
        grid[row] = row_position  # row_position皇后所在列的位置
        if possible(grid, row):
            queen(row + 1)


def solve():
    queen(0)  # Execute queen function, set the position of the Queen from the first row.


solve()  # Execute main function.
