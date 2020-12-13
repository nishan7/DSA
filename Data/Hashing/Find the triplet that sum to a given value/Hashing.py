'''
#### Name:  Find the triplet that sum to a given value
Link: [link]()

#### Sub_question_name: Hashing 
Link: [gfg](https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/)

**O(N^2) O(N)**
'''


def find_triplets(nums, k):
    n = len(nums)

    numbers_set = set(nums)

    for i in range(n-1):
        for j in range(i+1, n):
            target = k - nums[i] - nums[j]
            if target in numbers_set:
                return True

    return False


nums = [1, 4, 45, 6, 10, 8]
k = 22
print(find_triplets(nums, k))
