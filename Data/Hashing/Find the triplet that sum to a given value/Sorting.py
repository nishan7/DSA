'''
#### Name:  Find the triplet that sum to a given value
Link: [link]()

#### Sub_question_name: Sorting 
Link: [link]()

Sort and search
**O(N^2) O(1)**
'''


def find_triplets(nums, k):
    n = len(nums)
    nums.sort()

    numbers_set = set(nums)

    for i in range(n-2):
        left = i+1
        right = n-1

        while (left < right):
            if nums[left] + nums[right] + nums[i] == k:
                return True
            elif nums[left] + nums[right] + nums[i] < k:
                left += 1
            else:
                right -= 1

    return False


nums = [1, 4, 45, 6, 10, 8]
k = 223
print(find_triplets(nums, k))
