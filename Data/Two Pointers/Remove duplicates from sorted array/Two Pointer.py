'''
#### Name:  Remove duplicates from sorted array
Link: [link]()

#### Sub_question_name: Two Pointer 
Link: [link]()

'''

def removeDuplicates(nums):
    i = 1

    while i < len(nums):
        if nums[i] == nums[i-1]:
            nums.pop(i)
        else:
            i += 1
    


nums = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates(nums)
print(nums)