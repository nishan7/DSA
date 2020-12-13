'''
#### Name:  The celebrity Problem
Link: [link]()

#### Sub_question_name: Two Pointers 
Link: [link]()

**O(n) O(1)**

'''


def cel(matrix, n):
    celebrity = [1] * n

    a = 0
    b = n-1

    while a < b:
        if matrix[a][b]:   # A cant be celebrity
            a += 1
        else:              # B can't be celebrity
            b -= 1

    for i in range(n):

        # If any person doesn't
        # know 'a' or 'a' doesn't
        # know any person, return -1
        if ((i != a) and (matrix[a][i] or not(matrix[i][a]))):
            return -1

    return a


N = 8

# Person with 2 is celebrity
MATRIX = [[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0]]


print(cel(MATRIX, N//2))
