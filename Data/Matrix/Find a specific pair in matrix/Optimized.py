'''
#### Name:  Find a specific pair in matrix
Link: [link]()

#### Sub_question_name: Optimized 
Link: [link]()

'''

from pprint import pprint


def find_pairs(mat):
    r = len(mat)
    c = len(mat[0])

    mat_max = [[0] * c for _ in range(r)]
    mat_max[r-1][c-1] = mat[r-1][c-1]

    # Preprocess last row
    maxv = mat_max[r-1][c-1]
    for i in range(c-2, -1, -1):
        if mat[r-1][i] > maxv:
            maxv = mat[r-1][i]
        mat_max[r-1][i] = maxv

    # Preprocess last columns
    maxv = mat_max[r-1][c-1]
    for i in range(r-2, -1, -1):
        if mat[i][c-1] > maxv:
            maxv = mat[i][c-1]
        mat_max[i][c-1] = maxv

    for i in range(r-2, -1, -1):
        for j in range(c-2, -1, -1):
            maxv = max(maxv, mat_max[i+1][j+1] - mat[i][j])

            mat_max[i][j] = max(mat[i][j], mat_max[i][j+1], mat_max[i+1][j])

    print(maxv)


mat = [[1, 2, -1, -4, -20],
       [-8, -3, 4, 2, 1],
       [3, 8, 6, 1, 3],
       [-4, -1, 1, 7, -6],
       [0, -4, 10, -5, 1]]

find_pairs(mat)  # 18
