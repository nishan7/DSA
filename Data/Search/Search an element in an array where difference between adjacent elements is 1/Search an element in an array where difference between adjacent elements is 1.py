'''
#### Name:  Search an element in an array where difference between adjacent elements is 1
Link: [link]()

'''


def search(arr, key):

    n = len(arr)
    i = 0

    while i < n:
        element = arr[i]
        if element == key:
            return i
        diff = key - element    # To reach key from element we need aleast diff jumps,

        i +=  abs(diff)   # We can safely go this values


arr = [8 ,7, 6, 7, 6, 5, 4, 3, 2, 3, 4, 3 ] 
key = 3

print(search(arr, key))
