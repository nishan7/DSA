'''
#### Name:  K Closest Numbers
Link: [youtube_link](https://www.youtube.com/watch?v=J8yLD-x7fBI&list=PL_z_8CaSLPWdtY9W22VjnPxG30CXNZpI9&index=5)

Find the numbers closest to the numbers in array 

For array 5, 6, 7, 8, 9 .. find number closest to 7 

We can subtract 7 from all and use only those value that have value less, (use max heap to get k-smallest numbers)

'''

from heapq import heapify, heappush, heappop

max_heap = []
h_push = lambda x: heappush(max_heap, (-1*x[0], x[1]))
h_pop = lambda : heappop(max_heap)
h_max = lambda : -1* max_heap[0]


class Node:
    def __init__(self, diff, value):
        self.diff = diff
        self.value = value
    
    def __lt__(self, other):
        return self.diff < other.diff


def k_closest_numbers(arr,k, num):
    n = len(arr)

    for elem in arr:
        diff = abs(elem - num)
        h_push((diff, elem))

        if len(max_heap) > k:
            h_pop()
    

    print(max_heap)
    output = []
    while len(max_heap) > 0:
        output.append(h_pop()[1])
    
    return output




arr = [5,6,7,8]
k = 3
num = 7

print(k_closest_numbers(arr, k, num))