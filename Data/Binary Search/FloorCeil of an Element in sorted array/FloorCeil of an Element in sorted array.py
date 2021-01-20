'''
#### Name:  Floor/Ceil of an Element in sorted array
Link: [link](https://www.youtube.com/watch?v=uiz0IxPCUeU&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=11)


for a number num; floor(num) num itself if present in arr **or** greatest element smaller than num

##### Brute:
Linear search from (1, n-1)
If key return it else
If any number greater than key is found :=> floor
Prev element to it is :=> ciel

##### BS:
Add some if case after end of while loop
'''


def floor_ceil(arr, key):
    low = 0
    high = len(arr)

    while low <= high:
        mid = (low+high)//2

        if arr[mid] == key:
            return key,key

        elif key > arr[mid]:
            low = mid+1
        elif key < arr[mid]:
            high = mid-1

    # Upper loop will only end when key is found  or  low > high
    # Second case will occur after one element is left or may occur after 2 elements are left
    # In Second case  ceil = arr[low] and floor = arr[high]
    # As array is sorted so higher index have higher value

    return arr[high], arr[low]   


arr = [1, 2, 3, 4,4, 8, 10, 12, 19]
# arr=[12]   # arr[-1], arr[0]
key = 4

print(floor_ceil(arr, key))

'''
Aditya Verma
'''


def floor_ceil(arr, key):
    low = 0
    high = len(arr)

    # may be used to store index or item
    floor = -1
    ceil = -1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] == key:
            return key,key

        elif key > arr[mid]:
            low = mid+1
            floor = arr[mid] # Searching in upper arrays, so arr[mid] is current floor

        elif key < arr[mid]:
            high = mid-1 
            ceil = arr[mid]  # Searching in lower array, so arr[mid] is current ceil

    return floor, ceil


arr = [1, 2, 3, 4,4, 8, 10, 12, 19]
key = 5

print(floor_ceil(arr, key))
