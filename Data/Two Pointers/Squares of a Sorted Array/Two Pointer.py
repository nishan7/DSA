'''
#### Name:  Squares of a Sorted Array
Link: [leetcode](https://leetcode.com/problems/squares-of-a-sorted-array/)

#### Sub_question_name: Two Pointer 
Link: [link]()

'''

def squared_sorted(nums):
    i, j = 0, len(nums)-1

    res = []
    while i <= j:
        if abs(nums[i]) > abs(nums[j]):
            res.append(nums[i] ** 2)
            i += 1
        else:
            res.append(nums[j] ** 2)
            j -= 1
    
    print(res)
    return res



nums = [-4,-1,0,3,10]
squared_sorted(nums)