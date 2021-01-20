'''
#### Name:  Frequency Sort
Link: [link]()


Max Heap , with key based on freq
'''


from heapq import heapify, heappush, heappop

max_heap = []
def h_push(x): return heappush(max_heap, (-1*x[0], x[1]))
def h_pop(): return heappop(max_heap)


def h_max(): return -1 * max_heap[0]


def freq_sort(arr):
    n = len(arr)

    min_heap = []

    counter = {}
    for elem in arr:
        if elem in counter.keys():
            counter[elem] += 1
        else:
            counter[elem] = 1

    for elem, freq in counter.items():
        h_push((freq, elem))

    output = []
    while max_heap:
        a, b = h_pop()
        freq, elem = -1 * a, b

        output = output + [elem]*freq

    return output


print(freq_sort([1, 1, 2, 1, 2, 2, 2, 3]))

# [1,1,2,1,2,2,2,3] => [2, 2, 2, 2, 1, 1, 1, 3]
