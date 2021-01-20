'''
#### Name:  Find the position of element in infinite sorted Array
Link: [link](https://www.youtube.com/watch?v=FzvK5uuaki8&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=13)

Size is not known

'''


def binary_search(arr, low, high, key):
    while low <= high:
        mid = (low+high)//2

        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid-1
        elif key > arr[mid]:
            low = mid+1

    return -1


#  Start with window of size 1 and double the windows and move the window
def search(arr, key):
    low = 0
    high = 1

    while key > arr[high]:
        low = high
        high = high*2

    return binary_search(arr, low, high, key)


arr = [1, 2, 6, 7, 9, 11, 15, 18, 45, 56, 78, 79, 98, 99, 109, 103, 184]
key = 2

print(search(arr, key))
