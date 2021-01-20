'''
#### Name:  Maximum element in a Bitonic Array
Link: [youtube](https://www.youtube.com/watch?v=BrrZL1RDMwc&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=18)

**Brute**: Use linear search to get the answer in O(n)    

Finding peak element (But bitonic array will have single peak element)   

'''


def max_elem(arr):
    n = len(arr)
    low = 0
    high = n-1

    if n == 1:  # If there is only one element in the array
        return 0

    while low <= high:
        mid = (low + high)//2

        if mid > 0 and mid < n-1:  # If mid is not last element or first element
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid+1] > arr[mid]:
                low = mid+1
            elif arr[mid-1] > arr[mid]:
                high = mid - 1

        elif mid == 0:   # if mid ever reaches to the first element
            if arr[mid] > arr[mid+1]:    # Reverse Sorted array 
                return mid
            else:
                return mid+1

        elif mid == n-1:   # If mid ever reaches to the first element
            if arr[mid] > arr[mid-1]:   # Sorted Array
                return mid
            else:
                return mid-1


arr = [1, 4, 5, 7, 8, 6, 3, 2]


print(max_elem(arr))
