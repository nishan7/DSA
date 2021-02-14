'''
#### Name:  Magic Index
Link: [link]()

#### Sub_question_name: Brute 
Link: [link]()

A index is said to be magic index if A[i] = i
Input array is sorted

Brute Force O(n)

'''

def magic_index(nums):
    n = len(nums)

    for i in range(n):
        if i == nums[i]:
            print(i)
        




magic_index([0,0,1,3,5,8,32])