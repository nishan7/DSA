'''
#### Name:  The Knight's tour
Link: [link]()

**O(8^(N^2)) 8 choices for n^2 cells** 
'''
from pprint import pprint


def is_valid(x, y, board):
    if 8 > x >= 0 and 8 > y >= 0 and board[x][y] == -1:
        return True

    return False


def knight(board, pos, x, y):
    if pos == 64:
        return True

    for move_x, move_y in zip(pos_x, pos_y):
        # New position
        new_x = x + move_x
        new_y = y + move_y

        if is_valid(new_x, new_y, board):
            # We will check this new pos
            board[new_x][new_y] = pos

            if knight(board, pos+1, new_x, new_y):
                return True  # We got the solution, now who cares

            # But if we didn't that position for the knight was wrong
            board[new_x][new_y] = -1

    return False


n = 8
board = [[-1 for j in range(n)] for i in range(n)]

pos_x = [-1, -1, 1, 1, -2, -2, 2, 2]
pos_y = [-2, 2, -2, 2, -1, 1, -1, 1]

pos_x = [2, 1, -1, -2, -2, -1, 1, 2]
pos_y = [1, 2, 2, 1, -1, -2, -2, -1]

board[0][0] = 0
knight(board, pos=1, x=0, y=0)
pprint(board)

# [[0, 59, 38, 33, 30, 17, 8, 63],
#  [37, 34, 31, 60, 9, 62, 29, 16],
#  [58, 1, 36, 39, 32, 27, 18, 7],
#  [35, 48, 41, 26, 61, 10, 15, 28],
#  [42, 57, 2, 49, 40, 23, 6, 19],
#  [47, 50, 45, 54, 25, 20, 11, 14],
#  [56, 43, 52, 3, 22, 13, 24, 5],
#  [51, 46, 55, 44, 53, 4, 21, 12]]