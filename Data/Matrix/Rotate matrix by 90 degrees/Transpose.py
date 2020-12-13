'''
#### Name:  Rotate matrix by 90 degrees
Link: [link]()

#### Sub_question_name: Transpose 
Link: [link]()

1) Transpose the matrix
2) Inplace reversal
'''
def inplace_reverse(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    


def rotate(mat):
    r = len(mat)
    c = len(mat[0])

    for i in range(r):
        for j in range(i, c):  #!W
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    
    for row in range(r):
        inplace_reverse(mat[row])
    
    # print(mat)

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(mat)