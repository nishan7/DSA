'''
#### Name:  Magic Index
Link: [link]()

#### Sub_question_name: Binary Search 
Link: [link]()

'''

def magic_index(nums):
    n = len(nums)

    low = 0
    high = n-1
    
    while low < high:
        mid = (low + high)//2

        if mid == nums[mid]:
            print(mid)
            return
        
        elif nums[mid] > mid:
            high = mid -1
        
        elif nums[mid] < mid:
            low  = mid + 1

    print("No magic elements found")

magic_index([0,0,1,3,5,8,32])