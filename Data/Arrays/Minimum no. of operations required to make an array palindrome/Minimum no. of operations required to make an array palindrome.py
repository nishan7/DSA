'''
#### Name:  Minimum no. of operations required to make an array palindrome
Link: [gfg](https://www.geeksforgeeks.org/find-minimum-number-of-merge-operations-to-make-an-array-palindrome/)


'''


def min_ops(nums):
    n = len(nums)

    start = 0
    end = n-1
    op = 0
    while start < end:
        if nums[start] == nums[end]:
            start += 1
            end -= 1
        elif nums[start] > nums[end]:
            nums[end-1] += nums[end]
            end -= 1
            op += 1

        else:
            nums[start+1] += nums[start]
            start += 1
            op += 1

    print(op)


nums = [1, 4, 5, 9, 1]
min_ops(nums)
