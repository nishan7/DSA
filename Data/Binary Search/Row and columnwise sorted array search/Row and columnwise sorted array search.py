'''
#### Name:  Row and columnwise sorted array search
Link: [youtube](https://www.youtube.com/watch?v=VS0BcOiKaGI&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=20)

**Brute** Traverse matrix in **O(n*m)** and find the key  

Matrix of n x m which is sorted columnwise and row wise  

Value in top right is highest in the row and lowest in the column  

**O(n+m)**  As maximum time is taken when, key is in bottom-left 



'''


def search(mat, row,col, key):
    # It can be started from top right or bottom left
    i = 0
    j = col-1

    # It tires to move from top right to bottom left
    while i < row and j >= 0:  # array out of bound(for any index)  ||   i == row-1 and j == 0 is bottom left
        if mat[i][j] == key:
            return i, j
        
        elif key > mat[i][j]: # So key won't exist in row i, so we can exclude that in next search
            i += 1
            
        elif key < mat[i][j]: # So key doesn't exists in column j, so we can exclude that in next search
            j -= 1

    return -1
    


mat = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
row = 3
col = 4
key  = 3

# mat = [ [10, 20, 30, 40, 42], 
#         [15, 25, 35, 45, 46], 
#         [27, 29, 37, 48, 49], 
#         [32, 33, 39, 50, 55] ] 

# row = 4
# col = 5
# key = 29
print(search(mat, row, col, key) )