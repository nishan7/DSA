'''
#### Name:  Find row with maximum no. of 1's
Link: [link]()

#### Sub_question_name: BS 
Link: [link]()

1) Simple **O(N^2)**
2) BS on Rows **O(nlogn)**

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
    max_row = 0
    max_value = 0
    for row_idx, row in enumerate(mat):
        ones = c - bs(row) - 1

        if ones > max_value:
            max_value = ones
            max_row = row_idx

    print(max_row)


mat = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]
r = 4
c = 4

max_ones(mat, r, c)
