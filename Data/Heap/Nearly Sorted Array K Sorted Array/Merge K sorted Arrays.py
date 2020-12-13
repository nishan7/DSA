'''
#### Name:  Nearly Sorted Array/ K Sorted Array
Link: [link]()

#### Sub_question_name: Merge K sorted Arrays 
Link: [link]()

**O(nlogk) SC: O(k)**
'''

from heapq import heappush, heappop


def merge(arr):
    k = len(arr)
    n = len(arr[0])

    # iterator for every arrays, as index 0 is already in heap
    iterator = [1] * k
    res = []

    heap = []
    for array_id in range(k):
        heappush(heap, (arr[array_id][0], array_id))

    while len(heap) != 0:
        data, array_id = heappop(heap)
        res.append(data)

        if iterator[array_id] < size[array_id]:
            heappush(heap, (arr[array_id][iterator[array_id]], array_id))
            iterator[array_id] += 1

    print(res)


arr = [
    [2, 6, 12, 34],
    [1, 9, 20, 1000],
    [23, 34, 90, 2000, 4000]
]
size = [4, 4, 5]  # Size array can be used if the array is of different size
merge(arr)
