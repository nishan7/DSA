'''
#### Name:  Searching in Nearly Sorted Array
Link: [link]()

Value at index i, can be in ith , i-1 and i+1
'''

def search(arr, key):
    n = len(arr)
    low = 0
    high = len(arr) -1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] == key:
            return mid
        
        elif mid+1 < n and arr[mid+1] == key :
            return mid+1
        
        elif mid-1 > 0 and arr[mid-1] == key:
            return mid+1
        
        elif key > arr[mid]:
            low = mid+1
        elif key < arr[mid]:
            high = mid-1
    
    return -1


print(search([1,2,6,4,7,8,9,11], 9))  # 6
