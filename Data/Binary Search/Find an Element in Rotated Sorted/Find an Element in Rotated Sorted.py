'''
#### Name:  Find an Element in Rotated Sorted
Link: [link](https://www.youtube.com/watch?v=Id-DdcWb5AU&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=8)

Search for element in sorted rotated array
1) Search for minimum element
2) Split based on minimum element
3) Apply binary search in both parts
'''


def min_element(arr):
    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high)//2

        if arr[mid-1] > arr[mid]:
            return mid

        elif arr[low] > arr[mid]:
            high = mid - 1

        elif arr[high] < arr[mid]:
            low = mid + 1

        else:
            return -1


def bs(arr, key, low, high):

    while low <= high:
        mid = (low + high)//2

        if arr[mid] == key:
            return mid
        elif key > arr[mid]:    
            low = mid+1
        elif key < arr[mid]:
            high = mid-1
    return -1

arr = [11,12,15,18,2,5,6,8]
# arr = [11,12,18,1]
key = 12
min_idx = min_element(arr)

print(min_idx)

search_idx = bs(arr, key, 0, min_idx-1)

if search_idx != -1:
    print(search_idx)

search_idx = bs(arr, key, min_idx, len(arr)-1)

# print(search_idx)






