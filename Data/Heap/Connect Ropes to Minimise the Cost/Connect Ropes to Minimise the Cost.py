'''
#### Name:  Connect Ropes to Minimise the Cost
Link: [link](https://www.youtube.com/watch?v=_k_c9nqzKN0&list=PL_z_8CaSLPWdtY9W22VjnPxG30CXNZpI9&index=9)


Connect ropes; each connect has cost as the sum of 2 ropes

We need to minimize ther cost

At any time take 2 ropes that are minimum
**TC: nlogn SC: O(n)**
**Insert and Extract take O(logn)**
'''
from heapq import heapify, heappush, heappop


def minimum_rope(arr):
    # min_heap = arr; heapify(min_heap)

    min_heap = []
    for elem in arr:
        heappush(min_heap, elem)

    while len(min_heap) > 1:  # Stop only when there is single element left
        rope1 = heappop(min_heap)
        rope2 = heappop(min_heap)

        heappush(min_heap, rope1+rope2)

    return min_heap[0]


arr = [4, 5, 2, 3, 1]

print(minimum_rope(arr))

# [4,5,2,3,1] =>  15
