'''
#### Name:  Rat in a maze
Link: [link]()

#### Sub_question_name: Backtrack
Link: [link]()

Backtracking is an algorithmic paradigm
that tries different solutions until finds a solution that "works".

**TC:  O((N^2)^4)**
**SC: O(L*X), L = length of the path, X = number of paths.**
'''


def is_valid(maze, row, col, visited):
    # out of bounds of matrix
    if row == -1 or row == n or col == -1 or col == n or maze[row][col] == 0 or visited[row][col]:
        return False  # We cant go to this cell

    return True


def rat(maze, row, col, path, visited, res):
    if row == -1 or col == -1 or row == n or col == n or visited[row][col] or maze[row][col] == 0:
        return False

    if row == n - 1 and col == n - 1:
        res.append(''.join(path))
        return

    visited[row][col] = True

    if is_valid(maze, row - 1, col, visited):
        path.append('U')
        rat(maze, row - 1, col, path, visited, res)
        path.pop()  # Backtrack

    if is_valid(maze, row + 1, col, visited):
        path.append('D')
        rat(maze, row + 1, col, path, visited, res)
        path.pop()  # Backtrack

    if is_valid(maze, row, col - 1, visited):
        path.append('L')
        rat(maze, row, col - 1, path, visited, res)
        path.pop()  # Backtrack

    if is_valid(maze, row, col + 1, visited):
        path.append('R')
        rat(maze, row, col + 1, path, visited, res)
        path.pop()  # Backtrack

    visited[row][col] = False


maze = [[1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1]]
n = 5

res = []
path = []
row = 0
col = 0
visited = [[False for _ in range(n)] for __ in range(n)]

rat(maze, row, col, path, visited, res)  # ['DDRURRRDDD', 'DDRRURRDDD', 'DRDRURRDDD', 'DRRRRDDD']
print(res)
