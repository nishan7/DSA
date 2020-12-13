'''
#### Name:  Find Missing and Duplicate Numbers in an Array (1 to N)
Link: [link]()

#### Sub_question_name: Sort and Check 
Link: [link]()

**O(nlogn)**
Sort and check if arr[i-1] == arr[i]
'''

def findDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            print(nums[i])

arr = [2,1, 3, 1, 5, 5]
print(findDuplicate(arr))