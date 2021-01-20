'''
#### Name:  Fixed Point (Value equal to index)
Link: [link]()

Given an array of n distinct integers sorted in ascending order, write a function that returns a Fixed Point in the array, if there is any Fixed Point present in array, else returns -1. 
Fixed Point in an array is an index i such that arr[i] is equal to i. Note that integers in array can be negative.

1) Linear  **O(n)**
2) BS: compare mid with arr[mid]   **O(logn)** Divide and conquer
'''


def fixed_point(arr):
    n = len(arr)
    low = 0
    high = n-1

    while low <= high:
        mid = (low + high)//2

        if arr[mid] == mid:
            return mid

        if arr[mid] > mid:   # if value is already higher than index; It could never matching in higher index
            high = mid - 1

        elif mid > arr[mid]:  # if value is already lower than index; It could never match it in lower indices
            low = mid + 1

    return -1


arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100]    # 3 
arr = [1, 2, 3, 4, 5, 6, 6]          # -1 as the value is repeatign
print(fixed_point(arr))
