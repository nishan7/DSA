'''
#### Name:  Nearly Sorted Array/ K Sorted Array
Link: [youtube_link](https://www.youtube.com/watch?v=dYfM6J1y0mU&list=PL_z_8CaSLPWdtY9W22VjnPxG30CXNZpI9&index=4)

value for the index is in range of k
**TC: O(nlogk)**
'''

from heapq import heappush, heappop

def sort(arr, k):
    n = len(arr)

    min_heap= []
    
    output = []

    for elem in arr:
        heappush(min_heap, elem)
        
        if len(min_heap) > k:
            output.append(heappop(min_heap))
    
    while len(min_heap) > 0:
        output.append(heappop(min_heap))
    
    return output


arr = [6, 5, 3, 2, 8, 10, 9]
k = 3
print(sort(arr, k))

#[2, 3, 5, 6, 8, 9, 10]