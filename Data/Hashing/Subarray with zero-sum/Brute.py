'''
#### Name:  Subarray with zero-sum
Link: [link]()

#### Sub_question_name: Brute 
Link: [link]()

2 loops
'''

def check_zero(arr):
    n = len(arr)

    for i in range(1, n):
        for j in range(i):
            subarray = arr[j:i+1]
            if sum(subarray) == 0:
                return True
    
    return False


arr = [-3, 2, 3, 1, 6]    
print(check_zero(arr))