'''
#### Name:  kth Smallest Element]
Link: [heap_link](https://www.youtube.com/watch?v=hW8PrQrvMNc&list=PL_z_8CaSLPWdtY9W22VjnPxG30CXNZpI9)
Link: [link]()

Apporach one: Sorting **O(nlogn)**
Approach two: Heap **O(nlogk)**
Changes the sorting O(nlogn) to O(nlogk)

As whole array neednot be sorted, In heap we only sort only k elements

For smallest element we use heap

'''

from heapq  import heappush, heappop, heapify

max_heap = []
h_push = lambda item: heappush(max_heap,-1 * item)
h_pop = lambda: -1 * heappop(max_heap)
h_max = lambda: -1 * max_heap[0]


def ksmallest(arr, k):
    n = len(arr)

    for elem in arr:
        h_push(elem)
        if len(max_heap) > k:
            h_pop()
    
    return h_max()

arr = [4,5,13,123,1]
print(ksmallest(arr, 3))


# [4,5,13,123,1],3 =>  5 
