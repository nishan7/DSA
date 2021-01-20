'''
#### Name:  Missing Number in Arithmetic Progression
Link: [link]()

#### Sub_question_name: BS 
Link: [link]()

**O(log(n))**
'''

def find_missing(nums):
    n = len(nums)
    if n < 2:
        return 
    
    a = nums[0]
    d = nums[1]- nums[0]

    low = 0
    high = n-1

    while low <= high:
        mid = low + (high-low)//2

        if nums[mid] == a + mid * d:
            low = mid +  1
        
        else:
            high = mid - 1
    
    print( a + low * d)




nums = [2, 4, 8, 10, 12, 14]   # 6
# nums = [1, 6, 11, 16, 21, 31]  # 26

find_missing(nums)