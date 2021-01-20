'''
#### Name:  Find an Element in Rotated Sorted
Link: [link]()

#### Sub_question_name: Without finding minmum element 
Link: [link]()

1) In BS except one point(transition), every part is sorted
2) From mid, Only one side arr is sorted 
3) Don't got part where it is sorted and confirmed
'''


def search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high)//2

        if arr[mid] == key:
            return mid

        if arr[low] <= arr[mid]:  # Left part is sorted and right part is not
            if arr[low] <= key < arr[mid]:      # Go left
                high = mid - 1
            else:                               # Go right
                low = mid+1

        else:                 # Righ part is sorted and left is not
            if arr[mid] < key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


arr = [11, 12, 15, 18, 2, 5, 6, 8]
key = 6
# arr = [11,12,18,1]
arr = [4, 5, 6, 7, 8, 1, 2, 3]
key = 8
arr = [4, 5, 6, 7, 0, 1, 2]
key = 0

key_idx = search(arr, key)
print(key_idx)
