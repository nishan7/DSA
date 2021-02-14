'''
#### Name:  Count triplet with sum smaller than a given values
Link: [link]()

#### Sub_question_name: Naive 
Link: [link]()

'''


def triplets(nums, req_sum):
    n = len(nums)
    ctr = 0


    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] < req_sum:
                    ctr += 1

    print(ctr)

nums = [5, 1, 3, 4, 7]
triplets(nums, 12)  # 4
