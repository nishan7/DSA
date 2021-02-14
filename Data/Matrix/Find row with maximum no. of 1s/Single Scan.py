'''
#### Name:  Find row with maximum no. of 1s
Link: [link]()

#### Sub_question_name: Single Scan 
Link: [link]()

'''

'''
#### Name:  Find row with maximum no. of 1's
Link: [link]()

#### Sub_question_name: Single Scan 
Link: [link]()

'''
def find_max(n,m, arr):

    i,j = 0, m
    max_val = 0

    while i<n:
        while j>0:
            if arr[i][j-1] == 1:
                j = j-1
            else:
                break
        
        if (m-j) > max_val:
            max_val = m-j
            row = i

        i += 1
    
    print(m-j, row)
    


arr = [[0, 0, 0, 1],
       [0, 0, 0, 1],
       [0, 0, 0, 0],
       [0, 1, 1, 1]]

arr = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]

n = len(arr)
m = len(arr[0])
find_max(n,m, arr)
