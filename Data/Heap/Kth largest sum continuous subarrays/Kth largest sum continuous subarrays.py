'''
#### Name:  Kth largest sum continuous subarrays
Link: [link]()

1) using presum
2) Calculate contigous sum and put it in the array

**TC: O(N^2 log k) SC: O(k)**
'''
from heapq import heappush, heappop


def kthlargest(nums, k):
    n = len(nums)
    sums = [0] * n
    for i in range(n):
        if i == 0:
            sums[i] = nums[i]
        else:
            sums[i] = sums[i-1] + nums[i]

    print(sums)
    heap = []

    for i in range(n):
        for j in range(i, n):
            if i == 0:
                contiguous_sum = sums[j]  # First to j
            else:
                contiguous_sum = sums[j] - sums[i-1]

            heappush(heap, contiguous_sum)
            if len(heap) > k:
                heappop(heap)

    print(heap[0])


nums = [10, -10, 20, -40]
k = 6                            # -10
kthlargest(nums, k)
