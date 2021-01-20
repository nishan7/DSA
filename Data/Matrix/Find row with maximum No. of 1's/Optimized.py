'''
#### Name:  Find row with maximum no. of 1's
Link: [link]()

#### Sub_question_name: Optimized 
Link: [link]()


**O(r+c)**  it can only traverse r rowwise and c columnwise  

'''

def bs(arr):
    low = 0
    high = len(arr)-1
    res = -1
    while low <= high:
        mid = (low + high)//2

        if arr[mid] == 1:
            res = mid
            high = mid-1

        elif arr[mid] == 0:
            low = mid + 1

    return res


def max_ones(mat, r, c):
    max_idx = 0
    j = bs(mat[0])
    if j == -1:
        j = c-1

    for row_idx, row in enumerate(mat):
        # Check if this row has 1 starting eariler than above row
        while j >= 0 and row[j] == 1:
            j -= 1
            max_idx = row_idx

    print(max_idx)



mat = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]
r = 4
c = 4

max_ones(mat, r, c)
