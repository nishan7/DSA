'''
#### Name:  Find Missing and Duplicate Numbers in an Array (1 to N)
Link: [link]()

#### Sub_question_name: Multiple Sort and Check 
Link: [link]()

Find All Numbers Disappeared in an Array (1 to n)  [There can be multiple]
'''

'''
Sets solution
list(set(nums) ^ set(range(1, len(nums)+1)))
'''

def findDuplicate(nums):
    nums.sort()
    n = len(nums)
    res = []

    idx = 0
    natural_count = 1

    while idx < n:
        if natural_count == nums[idx]:
            natural_count += 1
            idx += 1
        
        elif nums[idx] < natural_count:
            idx += 1
        
        else:
            res.append(natural_count)
            natural_count += 1

    
    # in case of [1,1,1]; to add remaining [2,3]
    for number in range(natural_count, n+1):
        res.append(number)


    return res


arr = [4,3,2,7,8,2,3,1]
# arr = [1,1,1,2]
print(findDuplicate(arr))
