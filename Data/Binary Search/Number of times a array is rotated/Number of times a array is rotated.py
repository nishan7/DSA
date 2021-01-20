'''
#### Name:  Number of times a array is rotated
Link: [link](https://www.youtube.com/watch?v=4WmTRFZilj8&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=7)

1) There is a array that was sorted, then it is rotated
2) Index of the minimum index == no of types array is rotated
3) **Brute Force** Linearly find the element
4) For a mid if ``arr[mid-1] > arr[mid]`` it is minmum
5) if ``arr[low] > arr[mid];``  ``high = mid-1``  
6) if ``arr[high] < arr[mid];``  ``low = mid + 1``

'''


def n_rotations(arr):
    n = len(arr)
    low = 0
    high = n-1

    while low <= high:
        mid = (low + high) // 2
        print(mid)

        # if (low == mid):
        #     return mid

        # Check is this arr[mid] is smallest or not
        # next = (mid+1)%n; prev = (mid+n-1)% n
        if arr[mid-1] > arr[mid]:
            return mid  # Index of minimum requirement is the required answer

        if arr[high] > arr[mid]:  # Right part is sorted, Search left part
            high = mid - 1
            
        elif arr[low] < arr[mid]:  # Left part is sorted, Search Right part
            low = mid + 1
 
        else:
            return -1


arr = [11, 12, 18, 1]
arr = [11, 12, 15, 18, 2, 5, 6, 8,9,10]
# arr = [1,1]
print(n_rotations(arr))

# [11,12,18,2,5,6,8] => 3
