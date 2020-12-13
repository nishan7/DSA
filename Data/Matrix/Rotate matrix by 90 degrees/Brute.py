'''
#### Name:  Rotate matrix by 90 degrees
Link: [link]()

#### Sub_question_name: Brute 
Link: [link]()


**O(n^2) O(n^2)**
'''


def rotate(mat):
    r = len(mat)
    c = len(mat[0])

    temp = [[0]*c for _ in range(r)]

    for i in range(c):
        for j in range(r):
            temp[i][c-j-1] = mat[j][i]   # First column to first row, First row to last columns

    print(temp)
    return temp

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(mat)