'''
#### Name:  Minimum swaps required bring elements less equal K together
Link: [link]()

1) Count the number of element to be swapped `cnt`
2) Using sliding window to find the window that the `max_nums`
3) No. of swaps = `cnt - max_nums`
'''


def min_swaps(nums, k):
    n = len(nums)
    cnt = 0

    for number in nums:
        if number <= k:
            cnt += 1

    i, j = 0, 0
    current_ctr = 0
    max_nums = 0

    while i < n and j < n:
        if j-i+1 < cnt:  # Window size is not met, increase window size
            if nums[j] <= k:
                current_ctr += 1
                max_nums = max(max_nums, current_ctr)
            j += 1

        else:                   # Else move window
            if nums[i] <= k:
                current_ctr -= 1
            i += 1
            j += 1

    print(cnt - max_nums)


nums = [2, 7, 9, 5, 8, 7, 4]
k = 5  # 2

nums = [2, 1, 5, 6, 3]
k = 3   # 1

min_swaps(nums, k)
