'''
#### Name:  Find an Element in Rotated Sorted
Link: [link]()

#### Sub_question_name: With duplicates 
Link: [link]()

**O(n)**
'''


def search(arr, key):
    arr = nums
    key = target

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high)//2

        if arr[mid] == key:
            return True

        while low < mid and arr[low] == arr[mid]:
            low += 1

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

    return False
