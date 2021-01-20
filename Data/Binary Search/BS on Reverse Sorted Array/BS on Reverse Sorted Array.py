'''
#### Name:  BS on Reverse Sorted Array
Link: [link](https://www.youtube.com/watch?v=YbkELwnGRdo&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=3)

Descending sorted array
'''

def search(arr, key):
    low  = 0
    high = len(arr) -1 

    while(low<=high):
        mid = (low+high)//2

        if arr[mid] == key:
            return mid
        elif key > arr[mid]:
            high = mid -1
        elif key < arr[mid]:
            low = mid + 1


arr= [1,2,5,6,11,76,99]
print(search(arr[::-1], 11))