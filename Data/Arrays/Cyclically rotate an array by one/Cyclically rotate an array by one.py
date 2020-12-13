'''
#### Name:  Cyclically rotate an array by one.
Link: [link]()

1) Store last element in a variable say x.
2) Shift all elements one position ahead.
3) Replace first element of array with x.

'''


def rotate_left(arr):
    n = len(arr)

    first = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]

    arr[n-1] = first


def rotate_right(arr):
    n = len(arr)

    last = arr[n-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]

    arr[0] = last


arr = [1, 2, 4, 6, 7]
rotate_left(arr)
print(arr)
rotate_right(arr)
print(arr)
