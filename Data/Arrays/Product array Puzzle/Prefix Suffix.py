'''
#### Name:  Product array Puzzle
Link: [link]()

#### Sub_question_name: Prefix Suffix 
Link: [link]()

Use 2 arrays to store prefix and suffix products   
Based on  that  get the answer for the specific index  

- Using power of -1 instead of division
**O(n) O(n)**


'''

def prefix_suffix(nums):
    n = len(nums)

    prefix = [0]* n
    prefix[0] = 1
    for i in range(1, n):
        prefix[i] = nums[i-1] * prefix[i-1]
    
    suffix = [0] * n
    suffix[n-1] = 1
    for i in range(n-2, -1, -1):
        suffix[i] = nums[i+1] * suffix[i+1]
    
    res = [0] * n
    for i in range(n):
        res[i] = prefix[i] * suffix[i]
    
    # print(res)
    return res

arr = [10, 3, 5, 6, 2]
prefix_suffix(arr) 