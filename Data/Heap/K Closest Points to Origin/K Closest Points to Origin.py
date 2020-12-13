'''
#### Name:  K Closest Points to Origin
Link: [link](https://www.youtube.com/watch?v=XC4EotTewro&list=PL_z_8CaSLPWdtY9W22VjnPxG30CXNZpI9&index=8)

We say that we can sort before we do anything

For list of coordinate values, find the k elements that are closest to origin

Nearest means smaller distance, max_heap

Create max_heap and remove(pop) higher values

'''

from heapq import heapify, heappush, heappop

max_heap = []
h_push = lambda x: heappush(max_heap, (-1*x[0], x[1]))
h_pop = lambda : heappop(max_heap)
h_max = lambda : -1* max_heap[0]

distance = lambda point: point[0]**2+ point[1]**2       # use ditch sqrt root for simiplicity


def k_nearest_to_origin(arr, k):
    
    for point in arr:
        h_push((distance(point), point))

        if len(max_heap) > k:
            h_pop()
    
    output = []
    while max_heap:
       output.append(h_pop()[1])
    
    return output
    





k = 3
arr = [[1,3],[-2,2],[5,8],[0,1]]

print(k_nearest_to_origin(arr, k))