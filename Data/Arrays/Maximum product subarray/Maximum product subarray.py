'''
#### Name:  Maximum product subarray
Link: [link]()

Use 2 variables

**O(n) O(1)**
'''


def max_prod(nums):
    max_val = nums[0]
    min_val = nums[0]
    res = nums[0]

    for number in nums[1:]:
        if number < 0:
            max_val, min_val = min_val, max_val

        max_val = max(number, number * max_val)
        min_val = min(number, min_val * number)

        res = max(max_val, res)

    print(res)


nums = [-1, -3, -10, 0, 60]
nums = [6, -3, -10, 0, 2]
max_prod(nums)
