'''

#### Name:  Count of Element in a Sorted Array
Link: [link](https://www.youtube.com/watch?v=Ru_HhBFV3Xo&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=6)

Brute Force is linear search with count

So all the required numbers are together 

Find first and last occurance of the elemnt


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
first= first_occurance(arr, 10)
last = last_occurance(arr, 10)

print(last-first + 1)