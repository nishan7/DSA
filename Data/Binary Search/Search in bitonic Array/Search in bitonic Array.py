'''
#### Name:  Search in bitonic Array
Link: [youtube](https://www.youtube.com/watch?v=IjaP8qt1IYI&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=19)

**Brute** Linear Search   

Find peak element and split then apply 2 BS  **O(logn)** logarithmic  


'''


def bs_asc(arr, low, high, key):

    while low <= high:
        mid = (low + high)//2

        if arr[mid] == key:
            return mid

        elif key > arr[mid]:
            low = mid+1

        elif key < arr[mid]:
            high = mid - 1

    return -1


def bs_desc(arr, low, high, key):

    while low <= high:
        mid = (low + high)//2

        if arr[mid] == key:
            return mid

        elif key > arr[mid]:
            high = mid - 1

        elif key < arr[mid]:
            low = mid+1

    return -1


def peak(arr):
    n = len(arr)
    low = 0
    high = n-1

    if n == 1:
        return 0

    while low <= high:
        mid = (low + high)//2

        if mid > 0 and mid < n-1:  # Should not be first or last element
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid+1] > arr[mid]:
                low = mid + 1
            elif arr[mid-1] > arr[mid]:
                high = mid-1

        elif mid == 0:
            if arr[mid] > arr[mid+1]:   # Reverse sorted array
                return mid
            else:
                return mid+1

        elif mid == n-1:
            if arr[mid] > arr[mid-1]:  # Sorted array
                return mid
            else:
                return mid-1


arr = [1, 3, 8, 12, 4, 2]
key = 12

peak_idx = peak(arr)   # Get the index of the peak element



idx = bs_asc(arr, 0, peak_idx-1,key)
if idx != -1:
    print(idx)
else:
    idx = bs_desc(arr,peak_idx, len(arr)-1, key)
    print(idx)
