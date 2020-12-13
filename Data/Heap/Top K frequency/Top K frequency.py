'''
#### Name:  Top K frequency
Link: [link](https://www.youtube.com/watch?v=7VoJn544QrM&list=PL_z_8CaSLPWdtY9W22VjnPxG30CXNZpI9&index=6)


k numbers having highest frequency
'''

from heapq import heappush, heappop


def top_k_freq_numbers(arr, k):
    n = len(arr)

    min_heap = []

    counter = {}
    for elem in arr:
        if elem in counter.keys():
            counter[elem] += 1
        else:
            counter[elem] = 1

    for elem, freq in counter.items():
        heappush(min_heap, (freq, elem))

        if len(min_heap) > k:
            heappop(min_heap)

    output = []
    while min_heap:
        output.append(heappop(min_heap)[1])

    return output


arr = [1, 1, 1, 3, 2, 2, 4]   # [4, 2, 1]
k = 3

print(top_k_freq_numbers(arr, k))
