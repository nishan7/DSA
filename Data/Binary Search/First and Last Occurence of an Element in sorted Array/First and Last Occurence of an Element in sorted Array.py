'''
#### Name:  First and Last Occurence of an Element in sorted Array
Link: [link](https://www.youtube.com/watch?v=zr_AoTxzn0Y&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=5)

Use binary search even after the element is found
'''


def first_occurance(arr, key):
    low = 0
    high = len(arr) - 1
    res = -1

    while low <= high:
        mid = (low + high)//2

        if arr[mid] == key:
            res = mid   # Store the result, it can get updated

            high = mid - 1  # Search in section lower than mid

        elif arr[mid] > key:
            high = mid-1
        elif arr[mid] < key:
            low = mid+1

    return res


def last_occurance(arr, key):
    low = 0
    high = len(arr) - 1
    res = -1

    while low <= high:
        mid = (low + high)//2

        if arr[mid] == key:
            res = mid   # Store the result, it can get updated

            low = mid + 1  # Search in section upper than mid

        elif arr[mid] > key:
            high = mid-1
        elif arr[mid] < key:
            low = mid+1

    return res


arr = [2, 4, 10, 10, 10, 18, 20]
print(first_occurance(arr, 10))
print(last_occurance(arr, 10))
