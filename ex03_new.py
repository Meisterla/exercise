grid = [0, 0, 0, 0, 0, 0, 0, 0]  # Create a list to collect results, the index of each element as row,
# the value of each element as column.
n = 8


def possible(col, row):
    '''
    :param col: The current grid.
    :param row: The current number of rows.
    :return: If compliance returns True, otherwise returns False.
    '''
    if len(set(col[:row + 1])) != len(col[:row + 1]):  # Check if there are two queens in a column.
        return False
    for i in range(row):  # Check if there are two queens on the diagonal.
        if col[i] - col[row] == int(row - i) or col[row] - col[i] == int(row - i):
            return False
    return True


def print_grip(grid, n):
    '''
    :param grid: The grid.
    :param n: The number of rows or columns or queens.
    '''
    for row in range(n):
        line = ''
        for column in range(n):
            if grid[row] == column:
                line += 'Q '
            else:
                line += '. '
        print(line)
    input('More?')  # After printing one result, ask if you want to proceed to the next one.


def solve(row):
    '''
    :param row:  The row number.
    '''
    global grid
    global n
    if row == n:  # If the queen position in the last row is determined, print it.
        print_grip(grid, n)
        return  # Return and find the next case recursively.
    for row_position in range(n):
        grid[row] = row_position  # row_position皇后所在列的位置
        if possible(grid, row):
            solve(row + 1)


solve(0)  # Execute main function, set the position of the Queen from the first row.
