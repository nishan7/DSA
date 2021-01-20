'''
# Name:  0 - 1 Variations
Link: [link]()

# Sub_question_name: Count of Subset Sum
Link: [link]()

Just change true/false from subset or not to 0/1

'''
from pprint import pprint


def count_subset(arr, req_sum, T):

    for i in range(1, len(arr)+1):
        for j in range(1, req_sum+1):
            if arr[i-1] > j:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = T[i-1][j] + T[i-1][j-arr[i-1]]

    return T[len(arr)][req_sum]


arr = [2, 3, 5]
arr = [0, 0, 5, 5, 0, 0]
# arr = [1,1,2,3]
n = len(arr)
req_sum = 0

T = []
for i in range(n+1):
    row = []
    for j in range(req_sum + 1):
        if j == 0:
            row.append(1)
        elif i == 0:
            row.append(0)
        else:
            row.append(-1)
    T.append(row)




print(count_subset(arr, req_sum, T))
