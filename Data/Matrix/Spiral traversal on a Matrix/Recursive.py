'''
#### Name:  Spiral traversal on a Matrix
Link: [link]()

#### Sub_question_name: Recursive 
Link: [link]()

Recusrion solution prints borders

**O(r*c) O(1) No stack**
'''


def spiral(matrix, i, j, r, c):
    if r <= 0 and c <= 0:  # matrix is empty
        return

    for k in range(j, c):
        print(matrix[i][k], end=" ")
    print("|", end=" ")

    for k in range(1+i, c):
        print(matrix[k][c-1], end=" ")
    print("|", end=" ")

    if r > 1:  # The must be aleast 2 row to print
        for k in range(c-1-1, j-1, -1):    # Skip bottom rightmost element
            print(matrix[r-1][k], end=" ")
        print("|", end=" ")

    if c > 1:  # There must be aleast 2 columns to print
        for k in range(r-1-1, i, -1):    # Skip left bottommsota and left topmost element
            print(matrix[k][j], end=" ")
        print("|", end=" ")

    spiral(matrix, i+1, j+1, r-1, c-1)  # Reduce boundaries


a = [[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18]]
R = 3
C = 6

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
R = 4      # 1 2 3 4 | 8 12 16 | 15 14 13 | 9 5 | 6 7 | 11 | 10 | |
C = 4


spiral(a, 0, 0, R, C)
