'''
#### Name:  Missing Number in Arithmetic Progression
Link: [link]()

#### Sub_question_name: Linear 
Link: [link]()

**O(n)**
'''
def find_missing(nums):
    n = len(nums)
    if n < 2:
        return 
    
    a = nums[0]
    d = nums[1]- nums[0]

    n = 0
    for number in nums:
        ap_number = a + (n) * d
        if number != ap_number:
            print(ap_number)
            return

        n += 1


# nums = [2, 4, 8, 10, 12, 14]   # 6
nums = [1, 6, 11, 16, 21, 31]  # 26

find_missing(nums)