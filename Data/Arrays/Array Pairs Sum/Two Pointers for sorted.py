'''
#### Name:  Array Pairs Sum
Link: [link]()

#### Sub_question_name: Two Pointers for sorted 
Link: [link]()

Only Checks for pairs
'''


def pairs(nums, req_sum):
    nums.sort()

    ctr = 0
    i, j = 0, len(nums)-1

    while i < j:
        current_sum = nums[i] + nums[j]
        if current_sum > req_sum:
            j -= 1
        elif current_sum < req_sum:
            i += 1
        else:
            return True            
            

    return False

pairs([1, 2, 3, 4, 5, 5], 6)
