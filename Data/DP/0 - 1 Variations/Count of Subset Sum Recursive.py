'''
#### Name:  0 - 1 Variations
Link: [link]()

#### Sub_question_name: Count of Subset Sum Recursive 
Link: [link]()

Instead of true or false we use 0 or 1

'''
from pprint import pprint


def count_subset(arr, req_sum):
    # print(req_sum, arr)
    if req_sum == 0:
        return 1

    if len(arr) == 0:
        return 0

    item = arr[-1]
    arr = arr[:-1]

    if item > req_sum:
        return count_subset(arr, req_sum)
    else:
        return count_subset(arr, req_sum) + count_subset(arr, req_sum-item)


# arr = [2, 3, 5]
arr = [1, 1, 2, 3]
n = len(arr)
req_sum = 4

print(count_subset(arr, req_sum))

# Memoization Solution


def count_subset(arr, req_sum, T):
    n = len(arr)
    if T[n][req_sum] != -1:
        return T[n][req_sum]

    if req_sum == 0:
        return 1

    if len(arr) == 0:
        return 0

    item = arr[-1]
    arr = arr[:-1]

    if item > req_sum:
        T[n][req_sum] = count_subset(arr, req_sum, T)
        return T[n][req_sum]
    else:
        T[n][req_sum] = count_subset(
            arr, req_sum, T) + count_subset(arr, req_sum-item, T)
        return T[n][req_sum]


# arr = [2, 3, 5]
arr = [1, 1, 2, 3]
req_sum = 4
T = [[-1 for j in range(req_sum+1)] for i in range(n+1)]

print(count_subset(arr, req_sum, T))

