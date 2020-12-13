'''
#### Name:  Floor/Ceil of an Element in sorted array
Link: [link]()

#### Sub_question_name: Minimum difference element in a sorted Array 
Link: [link](https://www.youtube.com/watch?v=3RhGdmoF_ac&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=15)

Use similar apporach in floor ceil
'''


def min_diff(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high)//2

        if key == arr[mid]:
            return 0

        elif key > arr[mid]:
            low = mid + 1
        elif key < arr[mid]:
            high = mid-1

    return min(arr[low]-key, key-arr[high])


arr = [1, 2, 3, 4, 4, 8, 10, 12, 19]
# arr=[12]   # arr[-1], arr[0]
key = 15

print(min_diff(arr, key))
