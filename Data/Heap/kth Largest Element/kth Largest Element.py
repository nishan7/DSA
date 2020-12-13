'''
#### Name:  kth Largest Element
Link: [youtube_link](https://www.youtube.com/watch?v=3DdP6Ef8YZM&list=PL_z_8CaSLPWdtY9W22VjnPxG30CXNZpI9&index=3)

** TC O(nlogk) **
'''

## We use min heap

from heapq import heappush, heappop

def klargest(arr, k):
    
    min_heap = []
    for elem in arr:
        heappush(min_heap, elem)
        
        if len(min_heap) > k :
            heappop(min_heap)
    
    return arr[0]


arr = [4,5,13,123,1]
print(klargest(arr, 3))

# [4,5,13,123,1],3 =>  5 