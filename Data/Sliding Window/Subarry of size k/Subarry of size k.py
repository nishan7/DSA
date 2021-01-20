'''
#### Name:  Subarry of size k
Link: [link]()

'''


def smallest_subarry(nums, k):
    n = len(nums)
    i, j, sums = 0, 0, 0
    min_len = float('inf')

    while i < n and j < n:
        if sums == k:
            min_len = min(min_len, j-i)
            sums -= nums[i]
            i += 1
            j += 1

        elif sums < k:   # increase window
            j += 1

        elif sums > k:   # Decrease windows
            sums -= nums[i]
            i += 1

        if j < n:
            sums += nums[j]

    print(min_len)


nums = [1, 6, 45, 6, 10, 19]
k = 51
smallest_subarry(nums, k)
