'''
#### Name:  Maximum sum of absolute difference of an array
Link: [link]()

To get the maximum sum, we should have a sequence 
in which small and large elements comes alternate. This is done to get maximum difference.

**O(nlogn)**
'''


def max_diff(nums):
    n = len(nums)
    nums.sort()

    temp = []
    i = 0
    j = n-1

    while i <= j:         # Add the greater and smaller numbers in alternate order
        if i == j:
            temp.append(nums[i])

        temp.append(nums[i])
        temp.append(nums[j])

        i += 1
        j -= 1

    sums = 0

    for i in range(n):
        next_idx = (i-1) % n
        sums += abs(temp[i] - temp[next_idx])

    print(sums)


def max_diff(nums):
    n = len(nums)
    nums.sort()

    sums = 0
    for i in range(n//2):
        sums -= (2 * nums[i])
        sums += (2 * nums[n-i-1])

    print(sums)


nums = [1, 2, 4, 8]
max_diff(nums)   # 18
