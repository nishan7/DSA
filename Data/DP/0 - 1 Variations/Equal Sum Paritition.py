'''
#### Name:  0 - 1 Variations
Link: [link]()

#### Sub_question_name: Equal Sum Paritition 
Link: [link]()

Check if the array can be parititioned into equal sums

1) If sum of array is odd, return False
2) If sum of array is even, check if any subset of array has sum as (sum/2)
'''


def subset_sum(arr, req_sum, T):
    n = len(arr)
    if T[n][req_sum] != -1:
        return T[n][req_sum]

    if req_sum == 0:
        return True

    if len(arr) == 0:
        return False

    element = arr[-1]
    arr = arr[:-1]

    if element > req_sum:
        T[n][req_sum]= subset_sum(arr, req_sum, T)
        return T[n][req_sum]
    else:
        T[n][req_sum]= subset_sum(arr, req_sum, T) or subset_sum(arr, req_sum-element, T)
        return T[n][req_sum]


def is_equal_partition(arr):
    arr_sum = sum(arr)
    if arr_sum % 2 == 1:  # False
        return False

    else:  # if it is Even
        T = [[-1 for j in range(arr_sum//2 + 1)] for i in range(len(arr)+1)]
        # For it be equally parititon, it must have a subarray that has sum arr_sum//2
        return subset_sum(arr, arr_sum//2, T)


arr = [2, 3, 7, 8, 10]
print(is_equal_partition(arr))
