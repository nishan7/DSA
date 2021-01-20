'''
#### Name:  Find if there is any subarray with sum equal to 0
Link: [link]()

We calculate prefix sum, if anything repeats zero subset exists

**O(n) O(n)**
'''

def zero_subarry(nums):
    prefix = set([nums[0]])

    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i-1]
        if nums[i] in prefix:
            return True

        prefix.add(nums[i])

    return False

nums = [-3, -2, -1, 3, 1, 6]  # True
nums = [-3, -2, 3, 1, 6]  # False
nums = [-3, 2, 3, 1, -6]  # True

print(zero_subarry(nums))
