'''
#### Name:  N-Queen Problem
Link: [link]()

'''

from pprint import pprint


def is_valid(board, row, col):
    # Check horizontal left
    for j in range(col):
        if board[row][j] == 1:
            return False

    # Vertical Up
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Upper Diagonal on left side
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Lower Diagonal on right side
    for i, j in zip(range(row+1, n, 1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def nqueen(board, col):
    if col == n:
        pprint(board)
        return True

    res = False
    for row in range(n):

        if is_valid(board, row, col):
            board[row][col] = 1

            res = nqueen(board, col+1) or res  # If solution is found return

            board[row][col] = 0       # Else backtrack

    return res


n = 2
n = 4
board = [[0 for i in range(n)] for j in range(n)]
nqueen(board, 0)

# [[0, 0, 1, 0],
#  [1, 0, 0, 0],
#  [0, 0, 0, 1],
#  [0, 1, 0, 0]]

# [[0, 1, 0, 0],
#  [0, 0, 0, 1],
#  [1, 0, 0, 0],
#  [0, 0, 1, 0]]
