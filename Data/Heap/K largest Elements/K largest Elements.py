'''
#### Name:  K largest Elements
Link: [youtube_link](https://www.youtube.com/watch?v=3DdP6Ef8YZM&list=PL_z_8CaSLPWdtY9W22VjnPxG30CXNZpI9&index=3)

'''

from heapq import heappush, heappop


def klargest_elements(arr, k):
    min_heap = []
    for elem in arr:
        heappush(min_heap, elem)

        if len(min_heap) > k:
            heappop(min_heap)

    output = []
    while len(min_heap) > 0:
        output.append(heappop(min_heap))

    return output


# arr = [4,5,13,123,1]
arr = [7, 10, 3, 2, 20, 15]
print(klargest_elements(arr, 3))

# [7, 10, 3, 2,20,15],3 => [10,15, 20]
