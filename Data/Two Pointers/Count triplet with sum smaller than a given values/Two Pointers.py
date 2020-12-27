'''
#### Name:  Count triplet with sum smaller than a given values
Link: [link]()

#### Sub_question_name: Two Pointers 
Link: [link]()

**O(nlogn + n^2)**
'''


def triplets(nums, req_sum):
    n = len(nums)
    nums.sort()
    print(nums)
    ans = 0

    # We use 2 pointer after in range (i+1, n-1)
    for i in range(n-2):
        l = i+1
        r = n-1

        while l < r:  # As only one index moves at a time
            cur_sum = nums[i] + nums[l] + nums[r]

            if cur_sum < req_sum:
                # for i, j; There are l-r third elements,  [1,3,4,5,7]
                ans += r-l
                l += 1

            else:
                r -= 1

    print(ans)


nums = [5, 1, 3, 4, 7]
triplets(nums, 12)  # 4
