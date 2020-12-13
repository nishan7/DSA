'''
#### Name:  Spiral traversal on a Matrix
Link: [link]()

#### Sub_question_name: Iterative 
Link: [link]()

Use level to denote diagonal values

**O(m*n) O(1)**
'''



def spiral(matrix, r, c):
    level = 0
    while level <= r//2:

        if level < c//2 :
            # top left to top right, horizontal
            for k in range(level, c-level):
                print(matrix[level][k], end=" ")
            print('|', end=" ")


        if level  < r//2:
            # Top right to bottom right, vertical
            # Skip rightmost value in top row, as it is printed already
            for k in range(level+1, r-level):
                print(matrix[k][c-level-1], end=' ')
            print('|', end=" ")
       
        if level == c//2 or level == r//2:
            break

        if  level < c//2 :
            # Bottom right to bottom left,horizontal
            for k in range(c-1-level-1,level-1, -1):   # Extra -1 to skip bottom rightmost value that is printed already
                print(matrix[r-level-1][k], end=' ')
            print('|', end=" ")


        if level  < r//2:
            # Bottom left to Top left, vertical
            for k in range(r-1-level-1, level, -1):
                print(matrix[k][level], end=" ")
            print('|', end=" ")

        level += 1


a = [[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18]]
R = 3
C = 6

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
R = 4      # 1 2 3 4 | 8 12 16 | 15 14 13 | 9 5 | 6 7 | 11 | 10 | |
C = 4


spiral(a, R, C)   
