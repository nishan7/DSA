'''
#### Name:  Search an element in an array where difference between adjacent elements is 1
Link: [link]()

#### Sub_question_name: Searching in an array where adjacent differ by at most k 
Link: [link]()

We can jump by (key - element)/k ; or 1 
'''


def search(arr, key, k):

    n = len(arr)
    i = 0

    while i < n:
        element = arr[i]
        if element == key:
            return i
        diff = key - element

        i += max(1, abs(diff) // k)   # We can safely go this values


arr = [2, 4, 5, 7, 7, 6]
key = 6
k = 2

print(search(arr, key, k))
