'''
#### Name:  Maximum Subarray Sum
Link: [link]()

Given an array of integers (positive and negative) find the largest continuous sum.
'''

def max_continous_sum(arr):
    max_sum=current_sum = arr[0]
    
    for number in arr[1:]:
        current_sum = max(current_sum+number , number)
        max_sum = max(current_sum, max_sum)
    return max_sum

input_arr  = [1,2,-1,3,4,10,10,-10,-1]
print(max_continous_sum(input_arr))

