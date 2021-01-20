#!/bin/python3
'''
#### Name:  Sliding Window
Link: [link]()

#### Sub_question_name: Max Sum of k Consecutive Element BF 
Link: [link]()


O(n^2)
'''


def subarray_sum(arr, k):
    n =  len(arr)
    min_ans = float('inf')
    max_ans = float('-inf')
    for i in range(n-k+1):
            # print(arr[i:i+k])
            current_sum = sum(arr[i:i+k])
            min_ans = min(min_ans, current_sum)
            max_ans = max(max_ans, current_sum)
    
    return min_ans , max_ans


arr = [1, 3, 4, 11, 8, 2]
k = 3
print(subarray_sum(arr, k))

# Min => 8 Max= 23;
