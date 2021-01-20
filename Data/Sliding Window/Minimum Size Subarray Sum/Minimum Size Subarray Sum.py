'''
#### Name:  Minimum Size Subarray Sum
Link: [link]()

'''

def max_subarray(nums, s):
    n = len(nums)
    prefix_sum = [0] * n
    prefix_sum[0] = nums[0]
    for i in range(1, n):
        prefix_sum[i] = nums[i] + prefix_sum[i-1]
    
    res = float('inf')
    for i in range(n):
        for j in range(n):
            if i ==0:
                subarray_sum = prefix_sum[j]
            else:
                subarray_sum = prefix_sum[j] - prefix_sum[i-1]
            
            if subarray_sum >= s:
                res = min(res, j-i+1)

    print(res)
    return res

s = 7
nums = [2,3,1,2,4,3]

max_subarray(nums, s)